#!/usr/bin/env python3
"""Prevent repeated source-specific details during incremental Half-year note repair.

Older reader-facing Special sources may already contain a source-specific technical point in the
legacy fact returned by v5. v6 historically appended the same point again, producing duplicated
prose on a later incremental pass. This compatibility layer suppresses only points that are already
present verbatim in the inherited fact; all Screening-backed fail-closed provenance checks remain
owned by v30/v6.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v30 as base
from scripts import revise_special_half_year_review_repairs_v6 as detail


def deduplicated_source_specific_fact(title: str, info: dict[str, Any]) -> str:
    canonical_title = str(info.get("canonical_title") or title)
    chronology = detail._ORIGINAL_FACT(canonical_title, info)
    points = [str(point).strip() for point in (info.get("technical_points") or []) if str(point).strip()]
    if not points:
        raise ValueError(f"source-specific technical points missing: {canonical_title}")
    extras = [point for point in points if point not in chronology]
    if not extras:
        return chronology
    return chronology + " " + " ".join(extras)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = detail.source_specific_fact
    detail.source_specific_fact = deduplicated_source_specific_fact
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        detail.source_specific_fact = previous
    if isinstance(result, dict):
        result = dict(result)
        result["source_specific_detail_dedup_contract"] = "INHERITED_FACT_POINT_DEDUP_V1"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
