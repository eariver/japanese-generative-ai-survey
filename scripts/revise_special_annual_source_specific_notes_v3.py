#!/usr/bin/env python3
"""Annual Technical Notes repair with Toolformer-specific subject-bound signals.

Toolformer is a single-paper card. Its accepted arXiv abstract contains concrete method details, but
the Annual vocabulary did not include the paper's self-supervised API-call formulation, so the
fail-closed extractor correctly rejected it. Add only those concepts, keep them scope-sensitive,
and delegate to the existing Annual v2 repair stack.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes as base
from scripts import revise_special_annual_source_specific_notes_v2 as annual_v2

_TOOLFORMER_PATTERNS: tuple[tuple[str, str], ...] = (
    ("self-supervised tool-use learning", r"\bself[- ]supervised\b"),
    ("model-selected external API calls", r"\bexternal tools?\b|\bAPI calls?\b|\bAPIs?\b"),
)
_TOOLFORMER_SIGNALS = {name for name, _pattern in _TOOLFORMER_PATTERNS}
_CONTRACT = "TOOLFORMER_SUBJECT_BOUND_SIGNALS_V1"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    old_patterns = base._ANNUAL_SIGNAL_PATTERNS
    old_scoped = set(base._ANNUAL_SCOPED_SIGNALS)
    existing = {name for name, _pattern in old_patterns}
    base._ANNUAL_SIGNAL_PATTERNS = old_patterns + tuple(
        item for item in _TOOLFORMER_PATTERNS if item[0] not in existing
    )
    base._ANNUAL_SCOPED_SIGNALS = old_scoped | _TOOLFORMER_SIGNALS
    try:
        result = annual_v2.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base._ANNUAL_SIGNAL_PATTERNS = old_patterns
        base._ANNUAL_SCOPED_SIGNALS = old_scoped
    result = dict(result)
    result["toolformer_signal_contract"] = _CONTRACT
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
