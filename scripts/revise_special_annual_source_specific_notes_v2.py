#!/usr/bin/env python3
"""Annual source-specific Technical Notes repair with manifest-shape compatibility.

The Annual source manifest predates the Half-year per-article
``technical_notes_reader_facing`` flag.  The hardened incremental engine intentionally uses that
flag to decide which note files are reader-facing.  This adapter marks only Annual articles that
carry selected Evidence records in an in-memory copy passed to the inherited engine.  The current
validated source on disk is never mutated; the flag is materialized only in the new immutable
revision.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes as base


_INCREMENTAL = base.incremental
_ORIGINAL_INCREMENTAL_BUILD = _INCREMENTAL._incremental_build


def _annual_incremental_build(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
    marker: dict[str, Any],
    state: dict[str, Any],
    current: dict[str, Any],
    current_manifest: dict[str, Any],
) -> dict[str, Any]:
    compatible = copy.deepcopy(current_manifest)
    visible_articles = 0
    for article in compatible.get("articles") or []:
        evidence_count = int(article.get("evidence_record_count") or 0)
        if evidence_count > 0:
            article["technical_notes_reader_facing"] = True
            visible_articles += 1
        else:
            article["technical_notes_reader_facing"] = False
    if visible_articles < 1:
        raise ValueError("Annual compatibility shim found no Evidence-backed Technical Notes articles")
    return _ORIGINAL_INCREMENTAL_BUILD(
        repo_root,
        special_slug,
        issue_id,
        source_version,
        marker,
        state,
        current,
        compatible,
    )


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = _INCREMENTAL._incremental_build
    _INCREMENTAL._incremental_build = _annual_incremental_build
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        _INCREMENTAL._incremental_build = previous
    result = dict(result)
    result["annual_manifest_compatibility"] = "EVIDENCE_BACKED_READER_FACING_FLAGS_IN_MEMORY_V1"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
