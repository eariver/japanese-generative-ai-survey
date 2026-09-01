#!/usr/bin/env python3
"""Close living-page event slices at documentation/table boundaries as well as dates.

Some historical release entries are the oldest dated item in a living README. There is no
next date after the selected event, so the flattened current README can flow directly from
the old release note into today's model table. v13 already prevents backtracking into later
dated releases; this layer additionally stops the event slice at common structural headings
that begin current documentation/model tables.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v14 as base

# v14.base is v13, whose merge resolves these helper names from module globals at runtime.
event = base.base
impl = base.impl

_LIVING_TAIL_MARKERS = (
    "current model table",
    "models name",
    "model introduction",
    "table of contents",
    "quick start",
    "🌱 source",
    "source :",
)


def _trim_living_structural_tail(segment: str) -> str:
    lower = segment.lower()
    positions: list[int] = []
    for marker in _LIVING_TAIL_MARKERS:
        pos = lower.find(marker.lower(), 48)
        if pos >= 0:
            positions.append(pos)
    if positions:
        segment = segment[: min(positions)]
    # Historical release entries are intentionally compact. The cap is a secondary guard after
    # date/heading boundaries, not a substitute for them.
    return segment[:600].strip()


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
    if event._is_living_changelog(summary):
        next_date = event._DATE_TOKEN_RE.search(segment, 24)
        if next_date is not None:
            segment = segment[: next_date.start()]
        return _trim_living_structural_tail(segment)

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


# Re-export helpers needed by tests/review tooling.
_reset_existing_fact_lines = event._reset_existing_fact_lines


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_window = event._safe_event_window
    previous_signals = event._safe_technical_signals
    event._safe_event_window = _safe_event_window
    event._safe_technical_signals = _safe_technical_signals
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["living_event_slice_boundary"] = "DATE_OR_DOCUMENT_STRUCTURE_V2"
        return result
    finally:
        event._safe_event_window = previous_window
        event._safe_technical_signals = previous_signals


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
