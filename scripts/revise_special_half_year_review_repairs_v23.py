#!/usr/bin/env python3
"""Distinguish standalone blog publish/update dates from living News histories.

A standalone technical article can contain navigation text such as ``Blog & News`` plus a
publication date and a later update/comment date. The v16 heuristic treated any early
``News`` token plus multiple dates as a living release history, which cut FlashAttention-3's
article body off immediately after its publish date. Tighten that classifier so ``News``
counts as a history only when the already-established v19 history-region parser can identify
an actual dated News block; explicit Project Updates/Change Log handling remains unchanged.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v22 as base
from scripts import revise_special_half_year_review_repairs_v16 as news_layer
from scripts import revise_special_half_year_review_repairs_v19 as history_layer

_BASE_CLASSIFIER = news_layer._BASE_IS_LIVING_CHANGELOG


def _strict_is_living_changelog(summary: str) -> bool:
    # Keep the original v13 explicit changelog/date-density rules. The later v16 generic
    # ``news in head + >=2 dates`` rule is intentionally replaced by v19's structural parser.
    return _BASE_CLASSIFIER(summary) or history_layer._history_bounds(summary) is not None


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = news_layer._is_living_changelog
    news_layer._is_living_changelog = _strict_is_living_changelog
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["standalone_blog_date_metadata_contract"] = "STRUCTURAL_NEWS_HISTORY_ONLY_V1"
        return result
    finally:
        news_layer._is_living_changelog = previous


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
