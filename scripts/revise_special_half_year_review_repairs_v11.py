#!/usr/bin/env python3
"""Allow hash-bound suppression of genuinely ungrounded reader-facing Technical Notes cards.

Issue #139 requires source-specific Technical Notes. If the exact accepted Screening raw
provenance for a selected Evidence URL contains only bibliographic identity (for example,
title/link/date) and no technical release scope, inventing a detail would violate the
Evidence boundary. This layer permits an explicit editorial override to suppress that
single reader-facing card while preserving the Article citation, References entry, selected
Evidence identity, and all other Technical Notes.

Suppression is fail-closed: the override remains bound to the exact selected Evidence URL
set and the exact accepted Screening verification-queue SHA-256 through the existing v6
contract. A non-empty editorial reason is also required.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v10 as base

impl = base.impl
core = impl.core

_ORIGINAL_VALIDATE_OVERRIDE = impl._validate_override
_ORIGINAL_MERGE_EVIDENCE_INDEX = impl.merge_evidence_index
_ORIGINAL_REPAIR_NOTE_FILE = impl.repair_note_file


def _validate_override_with_suppression(title: str, override: dict[str, Any], info: dict[str, Any]) -> list[str]:
    if override.get("suppress_reader_facing_card") is not True:
        return _ORIGINAL_VALIDATE_OVERRIDE(title, override, info)
    expected_urls = sorted(str(url) for url in (info.get("urls") or []))
    actual_urls = sorted(str(url) for url in (override.get("source_urls") or []))
    if actual_urls != expected_urls:
        raise ValueError(
            f"Technical Notes suppression override URL mismatch for {title}: "
            f"actual={actual_urls} expected={expected_urls}"
        )
    reason = str(override.get("suppression_reason") or "").strip()
    if not reason:
        raise ValueError(f"Technical Notes suppression override requires suppression_reason: {title}")
    if override.get("technical_points"):
        raise ValueError(f"Technical Notes suppression override must not also provide technical_points: {title}")
    return []


def merge_evidence_index(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    previous_validate = impl._validate_override
    impl._validate_override = _validate_override_with_suppression
    try:
        index = _ORIGINAL_MERGE_EVIDENCE_INDEX(repo_root, manifest)
    finally:
        impl._validate_override = previous_validate

    by_identity: dict[int, dict[str, Any]] = {}
    for info in index.values():
        by_identity[id(info)] = info
    for info in by_identity.values():
        canonical_title = str(info.get("canonical_title") or "")
        override = impl._ACTIVE_OVERRIDES.get(canonical_title)
        if override and override.get("suppress_reader_facing_card") is True:
            info["suppress_reader_facing_card"] = True
            info["suppression_reason"] = str(override.get("suppression_reason") or "").strip()
            info["technical_point_mode"] = "HASH_BOUND_READER_CARD_SUPPRESSION"
    return index


def _strip_suppressed_cards(text: str, evidence: dict[str, dict[str, Any]]) -> tuple[str, int]:
    matches = list(core.NOTE_RE.finditer(text))
    changes: list[tuple[int, int, str]] = []
    suppressed_titles: list[str] = []
    for match in matches:
        title = match.group(1)
        info = evidence.get(title)
        if info is None:
            raise ValueError(f"Technical Notes title not bound to selected Evidence: {title}")
        if info.get("suppress_reader_facing_card") is True:
            changes.append((match.start(), match.end(), ""))
            suppressed_titles.append(title)
    for start, end, replacement in reversed(changes):
        text = text[:start] + replacement + text[end:]

    if suppressed_titles:
        raw_titles = set(suppressed_titles)
        escaped_titles = {core.tex_escape(title) for title in suppressed_titles}
        kept: list[str] = []
        removed_rows = 0
        for line in text.splitlines():
            stripped = line.strip()
            is_row = stripped.endswith(r"\\") and " & " in stripped
            if is_row and any(
                stripped.startswith(title + " & ")
                for title in raw_titles | escaped_titles
            ):
                removed_rows += 1
                continue
            kept.append(line)
        if removed_rows != len(suppressed_titles):
            raise ValueError(
                "Technical Notes suppression must remove exactly one Theme-at-a-glance row per card: "
                f"cards={len(suppressed_titles)} rows={removed_rows} titles={suppressed_titles}"
            )
        text = "\n".join(kept) + ("\n" if text.endswith("\n") else "")
    return text, len(suppressed_titles)


def repair_note_file(path: Path, evidence: dict[str, dict[str, Any]]) -> tuple[int, int, int]:
    original = path.read_text(encoding="utf-8")
    stripped, suppressed = _strip_suppressed_cards(original, evidence)
    if suppressed:
        path.write_text(stripped, encoding="utf-8")
    try:
        return _ORIGINAL_REPAIR_NOTE_FILE(path, evidence)
    except Exception:
        # Preserve failure atomicity for local callers. The workflow itself commits only after a
        # successful build, but restoring here also keeps unit tests and ad-hoc invocations clean.
        if suppressed:
            path.write_text(original, encoding="utf-8")
        raise


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_merge = impl.merge_evidence_index
    previous_repair = impl.repair_note_file
    impl.merge_evidence_index = merge_evidence_index
    impl.repair_note_file = repair_note_file
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["reader_card_suppression_contract"] = "HASH_BOUND_FAIL_CLOSED"
        return result
    finally:
        impl.merge_evidence_index = previous_merge
        impl.repair_note_file = previous_repair


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
