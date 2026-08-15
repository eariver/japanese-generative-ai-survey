#!/usr/bin/env python3
"""Recognize date-headed News histories as living release pages.

LTX-style READMEs can present a short release history as ``News <date>: ...`` without a
literal ``Changelog`` heading and with fewer than six dates. Treat a leading News block
with multiple dated entries as a living page so v15's date/structure boundary logic is
applied instead of standalone-article anchoring.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v15 as base

# v15.event is v13. Capture its original classifier before this module installs the extended
# predicate during build; otherwise the extension would recurse through the patched global.
event = base.event
impl = base.impl
_BASE_IS_LIVING_CHANGELOG = event._is_living_changelog


def _is_living_changelog(summary: str) -> bool:
    if _BASE_IS_LIVING_CHANGELOG(summary):
        return True
    head = summary[:900].lower()
    dated_entries = event._DATE_TOKEN_RE.findall(summary[:2200])
    return "news " in head and len(dated_entries) >= 2


def _safe_event_window(summary: str, events: list[tuple[str, str]], title: str = "") -> str:
    if not summary:
        return ""

    abstract = event._abstract_window(summary)
    if abstract:
        return abstract

    pos = event._last_event_position(summary, events)
    if pos is None:
        return summary[:4000]

    segment = summary[pos:]
    if _is_living_changelog(summary):
        next_date = event._DATE_TOKEN_RE.search(segment, 24)
        if next_date is not None:
            segment = segment[: next_date.start()]
        return base._trim_living_structural_tail(segment)

    anchor = event._artifact_anchor(segment, title)
    if anchor is not None:
        segment = segment[anchor:]
    return segment[:4200].strip()


def _safe_technical_signals(summary: str, events: list[tuple[str, str]], title: str = "") -> list[str]:
    window = _safe_event_window(summary, events, title)
    if not window:
        return []
    signals: list[str] = []
    for signal in impl._dynamic_signals(window):
        if signal not in signals:
            signals.append(signal)
    for display, pattern in impl._SIGNAL_PATTERNS:
        if display in event._UNSAFE_SIGNAL_NAMES:
            continue
        if re.search(pattern, window, flags=re.IGNORECASE | re.DOTALL) and display not in signals:
            signals.append(display)
        if len(signals) >= 7:
            break
    return signals[:7]


_reset_existing_fact_lines = event._reset_existing_fact_lines


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_window = event._safe_event_window
    previous_signals = event._safe_technical_signals
    previous_living = event._is_living_changelog
    event._safe_event_window = _safe_event_window
    event._safe_technical_signals = _safe_technical_signals
    event._is_living_changelog = _is_living_changelog
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["living_news_history_detection"] = "NEWS_PLUS_MULTIPLE_DATES_V1"
        return result
    finally:
        event._safe_event_window = previous_window
        event._safe_technical_signals = previous_signals
        event._is_living_changelog = previous_living


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
