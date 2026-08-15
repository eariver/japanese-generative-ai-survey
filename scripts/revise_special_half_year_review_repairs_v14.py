#!/usr/bin/env python3
"""Suppression-aware scoped wrapper for event-bounded Half-year note synthesis.

v13 narrows source windows correctly, but the existing hash-bound reader-card suppression
contract is installed by the v11 merge hook. When v13 replaces that merge hook, suppression
metadata must be propagated explicitly. This wrapper keeps the v13 event-bounded semantics
while making its merge suppression-aware, then restores every patched module global.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v13 as base
from scripts import revise_special_half_year_review_repairs_v11 as suppression

impl = base.impl


def _merge_event_bounded_with_suppression(
    repo_root: Path,
    manifest: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    previous_validate = impl._validate_override
    impl._validate_override = suppression._validate_override_with_suppression
    try:
        index = base._merge_event_bounded(repo_root, manifest)
    finally:
        impl._validate_override = previous_validate

    seen: set[int] = set()
    for info in index.values():
        identity = id(info)
        if identity in seen:
            continue
        seen.add(identity)
        canonical_title = str(info.get("canonical_title") or "")
        override = impl._ACTIVE_OVERRIDES.get(canonical_title)
        if override and override.get("suppress_reader_facing_card") is True:
            info["suppress_reader_facing_card"] = True
            info["suppression_reason"] = str(override.get("suppression_reason") or "").strip()
            info["technical_point_mode"] = "HASH_BOUND_READER_CARD_SUPPRESSION"
    return index


# Re-export pure helpers for contract tests.
_safe_event_window = base._safe_event_window
_safe_technical_signals = base._safe_technical_signals
_reset_existing_fact_lines = base._reset_existing_fact_lines


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_suppression_merge = suppression.merge_evidence_index
    suppression.merge_evidence_index = _merge_event_bounded_with_suppression
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["reader_card_suppression_preserved_under_event_bounding"] = True
        return result
    finally:
        suppression.merge_evidence_index = previous_suppression_merge


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
