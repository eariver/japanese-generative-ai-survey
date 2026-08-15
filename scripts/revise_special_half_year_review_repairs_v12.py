#!/usr/bin/env python3
"""Add bounded action/tool/research-paper signals for Half-year Technical Notes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v11 as base

impl = base.impl

_EXTRA_SIGNAL_PATTERNS_V12: tuple[tuple[str, str], ...] = (
    ("foundation GUI action model", r"\bfoundational GUI action model\b|\bfoundation action model\b"),
    ("GUI grounding", r"\bGUI grounding\b"),
    ("cross-platform GUI grounding corpus", r"\bcross[- ]platform GUI grounding corpus\b"),
    ("13M超のGUI elements", r"\bover 13 million GUI elements\b|\b13 million GUI elements\b"),
    ("6 benchmarks / mobile・desktop・web", r"\bsix benchmarks\b.{0,100}\bmobile\b.{0,100}\bdesktop\b.{0,100}\bweb\b"),
    ("stateful tool execution", r"\bstateful tool execution\b"),
    ("implicit state dependencies between tools", r"\bimplicit state dependencies between tools\b"),
    ("on-policy conversational evaluation", r"\bon[- ]policy conversational evaluation\b"),
    ("dynamic milestone evaluation", r"\bdynamic evaluation strategy\b.{0,100}\bintermediate and final milestones\b"),
    ("fully automatic scientific discovery framework", r"\bframework for fully automatic scientific discovery\b"),
    ("idea→code→experiment→paper workflow", r"\bgenerates novel research ideas\b.{0,220}\bwrites code\b.{0,220}\bexecutes experiments\b.{0,220}\bfull scientific paper\b"),
    ("simulated review process", r"\bsimulated review process\b"),
)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS_V12 + previous
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
