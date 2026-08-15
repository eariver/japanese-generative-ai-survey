#!/usr/bin/env python3
"""Add bounded LLaVA-OneVision multimodal-transfer signals."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v19 as base
from scripts import revise_special_half_year_review_repairs_v16 as event_layer

impl = event_layer.impl

_EXTRA_SIGNAL_PATTERNS_V20: tuple[tuple[str, str], ...] = (
    (
        "single-image / multi-image / videoを単一modelで扱うscope",
        r"single[- ]image, multi[- ]image, and video scenarios",
    ),
    (
        "cross-scenario visual task transfer",
        r"strong transfer learning across different modalities/scenarios|cross[- ]scenario capabilities",
    ),
    (
        "image→video task transfer",
        r"task transfer from images to videos",
    ),
    (
        "open large multimodal model family",
        r"family of open large multimodal models",
    ),
)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS_V20 + previous
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["llava_onevision_signal_contract"] = "MULTI_SCENARIO_TRANSFER_V1"
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
