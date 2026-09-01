#!/usr/bin/env python3
"""Extend Half-year source-specific signal coverage for concise accepted summaries.

Some accepted first-party Screening records intentionally store a concise feed summary
rather than the full article body. Those summaries can still contain concrete, useful
release semantics (speech-to-speech, repeated-input caching, web-source links, preview
reasoning traces, etc.). Install these narrowly-scoped patterns only while the routed
Half-year build runs, then restore the base extractor table.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v8 as base

impl = base.impl

_EXTRA_SIGNAL_PATTERNS: tuple[tuple[str, str], ...] = (
    ("speech-to-speech API", r"\bspeech[- ]to[- ]speech\b"),
    ("recent-input reuse / caching discount", r"\bdiscounts?\b.{0,80}\binputs?\b.{0,80}\brecently seen\b"),
    ("source links in search answers", r"\blinks?\b.{0,80}\b(?:web )?sources?\b|\b(?:web )?sources?\b.{0,80}\blinks?\b"),
    ("machine-learning-engineering agent benchmark", r"\bbenchmark\b.{0,80}\bmachine learning engineering\b"),
    ("rule-based rewards", r"\bRule[- ]Based Rewards\b|\bRBRs\b"),
    ("transparent reasoning trace", r"\bTransparent thought process\b"),
    ("inference scaling behavior", r"\bInference Scaling Laws\b|\binference scaling\b"),
    ("chat preview availability", r"\bTry it now at\b.{0,120}\bchat\.deepseek\.com\b"),
    ("open model/API still forthcoming at preview time", r"\bOpen[- ]source models?\s*&\s*API coming soon\b"),
    ("fine-tuning from frontier-model outputs", r"\bFine[- ]tune\b.{0,120}\boutputs?\b.{0,120}\bfrontier model\b|\boutputs?\b.{0,120}\bfrontier model\b.{0,120}\bFine[- ]tune\b"),
    ("short fact-seeking QA evaluation", r"\bshort,? fact[- ]seeking questions\b"),
    ("developer-supplied JSON Schema conformance", r"\bdeveloper[- ]supplied JSON Schemas?\b"),
)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    # Prepend the concise-summary patterns so a short first-party description produces a
    # meaningful reader-facing point before broader technical concepts are considered.
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS + previous
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
