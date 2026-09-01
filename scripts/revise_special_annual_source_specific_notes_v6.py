#!/usr/bin/env python3
"""Annual Technical Notes repair with 2022/2023 legacy claim-label compatibility.

Older Annual generated sources encode accepted Evidence fact bullets with reader-visible labels
such as ``Author claim`` or ``Project claim``.  The hardened reset/enrichment stack expects the
canonical ``一次情報で確認できる事実`` label before replacing generic bullets with source-specific
technical points.  This adapter normalizes only those known legacy claim labels in the immutable
revision copy, delegates to the v5 fail-closed stack, and restores the original text on failure.

No accepted Evidence, source URL set, chronology, or #191 subject-binding rule is widened.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes_v5 as base

_CONTRACT = "ANNUAL_LEGACY_CLAIM_LABEL_RESET_V2"
_CANONICAL_PREFIX = r"\item \textbf{一次情報で確認できる事実}: "
_LEGACY_PREFIXES = (
    r"\item \textbf{Author claim}: ",
    r"\item \textbf{Project claim}: ",
)


def _annual_reset_existing_fact_lines(path: Path, evidence: dict[str, dict[str, Any]]) -> str:
    original = path.read_text(encoding="utf-8")
    normalized = original
    for prefix in _LEGACY_PREFIXES:
        normalized = normalized.replace(prefix, _CANONICAL_PREFIX)
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")
    try:
        base._ORIGINAL_RESET(path, evidence)
    except Exception:
        path.write_text(original, encoding="utf-8")
        raise
    return original


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = base._annual_reset_existing_fact_lines
    base._annual_reset_existing_fact_lines = _annual_reset_existing_fact_lines
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base._annual_reset_existing_fact_lines = previous
    result = dict(result)
    result["annual_legacy_claim_label_reset_contract"] = _CONTRACT
    result["normalized_legacy_claim_labels"] = ["Author claim", "Project claim"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
