#!/usr/bin/env python3
"""Add bounded Emu3 next-token multimodal architecture signals."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v20 as base
from scripts import revise_special_half_year_review_repairs_v16 as event_layer

impl = event_layer.impl

_EXTRA_SIGNAL_PATTERNS_V21: tuple[tuple[str, str], ...] = (
    (
        "next-token predictionのみでmultimodal training",
        r"trained solely with next[- ]token prediction",
    ),
    (
        "image / text / videoをdiscrete token spaceへ統一",
        r"tokenizing images, text, and videos into a discrete space",
    ),
    (
        "single Transformer over mixed multimodal sequences",
        r"single transformer from scratch on a mixture of multimodal sequences",
    ),
    (
        "diffusion / compositional architectureを不要化",
        r"(?:eliminat(?:e|es|ing)) the need for diffusion or compositional architectures",
    ),
    (
        "video sequenceのnext-token predictionによるvideo生成",
        r"(?:generat(?:e|es|ing)) high[- ]fidelity video via predicting the next token in a video sequence",
    ),
)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS_V21 + previous
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["emu3_signal_contract"] = "NEXT_TOKEN_MULTIMODAL_V1"
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
