#!/usr/bin/env python3
"""Add bounded benchmark-construction signals for Half-year Technical Notes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v17 as base

# The event-bounded extractor lives in the v16 -> v15 -> v13 stack and resolves the
# controlled signal table from the shared implementation module at runtime.
from scripts import revise_special_half_year_review_repairs_v16 as event_layer

impl = event_layer.impl

_EXTRA_SIGNAL_PATTERNS_V18: tuple[tuple[str, str], ...] = (
    (
        "expert-vetted original mathematics benchmark",
        r"benchmark of hundreds of original, exceptionally challenging mathematics problems.{0,140}crafted and vetted by expert mathematicians",
    ),
    (
        "broad modern-mathematics coverage",
        r"cover most major branches of modern mathematics",
    ),
    (
        "unpublished problems for contamination control",
        r"new, unpublished problems.{0,160}minimizing risk of data contamination",
    ),
    (
        "automated verification",
        r"automated verification",
    ),
)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS_V18 + previous
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["benchmark_construction_signal_contract"] = "EXPERT_VETTING_AND_CONTAMINATION_CONTROL_V1"
        return result
    finally:
        impl._SIGNAL_PATTERNS = previous


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
