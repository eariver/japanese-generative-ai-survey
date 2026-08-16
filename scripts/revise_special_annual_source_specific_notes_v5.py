#!/usr/bin/env python3
"""Annual Technical Notes repair with legacy Author-claim reset compatibility.

SP-2023-Y v0.4 predates the Half-year reset convention and labels paper-card fact bullets as
``Author claim`` rather than ``一次情報で確認できる事実``.  The hardened Half-year reset correctly
requires one canonical fact line, so an Annual-only adapter normalizes that legacy label in the
new revision copy before delegating to the unchanged reset/enrichment stack.  On failure the exact
pre-normalization text is restored.  No accepted Evidence, source window, or #191 binding rule is
changed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes_v4 as base
from scripts import revise_special_half_year_review_repairs_v13 as reset_layer

_ORIGINAL_RESET = reset_layer._reset_existing_fact_lines
_CONTRACT = "ANNUAL_LEGACY_AUTHOR_CLAIM_RESET_V1"
_AUTHOR_PREFIX = r"\item \textbf{Author claim}: "
_CANONICAL_PREFIX = r"\item \textbf{一次情報で確認できる事実}: "


def _annual_reset_existing_fact_lines(path: Path, evidence: dict[str, dict[str, Any]]) -> str:
    original = path.read_text(encoding="utf-8")
    normalized = original.replace(_AUTHOR_PREFIX, _CANONICAL_PREFIX)
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")
    try:
        _ORIGINAL_RESET(path, evidence)
    except Exception:
        path.write_text(original, encoding="utf-8")
        raise
    # v13 expects the reset function to return the pre-enrichment text for rollback.
    return original


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = reset_layer._reset_existing_fact_lines
    reset_layer._reset_existing_fact_lines = _annual_reset_existing_fact_lines
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        reset_layer._reset_existing_fact_lines = previous
    result = dict(result)
    result["annual_legacy_author_claim_reset_contract"] = _CONTRACT
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
