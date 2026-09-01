#!/usr/bin/env python3
"""Extend Half-year note synthesis with additional bounded first-party signals.

This layer handles concise accepted summaries that still contain concrete technical scope,
without relaxing the source-specific fail-closed contract. Patterns are active only while
the routed Half-year build executes and are restored afterward.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v9 as base

impl = base.impl

_EXTRA_SIGNAL_PATTERNS_V10: tuple[tuple[str, str], ...] = (
    ("safety specificationを直接教示し、その仕様上でreasoning", r"directly taught safety specifications?.{0,100}reason over them|safety specifications?.{0,100}reason over them"),
    ("real-time voice AI", r"\breal[- ]time voice AI\b"),
    ("sora.comでのvideo生成提供", r"\bSora\b.{0,100}\bavailable to use at sora\.com\b|\bavailable to use at sora\.com\b"),
    ("最大1080p video", r"\b1080p\b"),
    ("最大20秒video", r"\b20\s+sec(?:ond)?s?\b"),
    ("extend / remix / blend", r"\bextend\b.{0,100}\bremix\b.{0,100}\bblend\b"),
    ("human-validated SWE-bench subset", r"\bhuman[- ]validated subset of SWE[- ]bench\b"),
    ("prover-verifier games", r"\bprover[- ]verifier games\b"),
)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS_V10 + previous
    try:
        return base.build(repo_root, special_slug, issue_id, source_version)
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
