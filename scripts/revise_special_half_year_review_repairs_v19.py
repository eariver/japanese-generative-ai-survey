#!/usr/bin/env python3
"""Resolve target dates inside living-page release-history regions before slicing.

Living READMEs can repeat a historical release date later in a current model table. The
existing event locator chooses the last matching date in the whole flattened page, which can
therefore jump from the release-history entry into a later documentation table. This layer
first identifies a bounded release-history region (Project Updates, Change Log, or a dated
News history), then resolves the selected event date only inside that region. Pages without a
recognized history region retain the previous locator unchanged.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v18 as base
from scripts import revise_special_half_year_review_repairs_v16 as event_layer

# v16/v15 ultimately resolve event positions through the shared v13 module.
event = event_layer.event
_BASE_LAST_EVENT_POSITION = event._last_event_position

_HISTORY_START_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bProject Updates\b", re.IGNORECASE),
    re.compile(r"\bChange Log\s+(?:On this page\s+Change Log\s+)?Date\s*:", re.IGNORECASE),
    re.compile(r"\bOn this page\s+Change Log\s+Date\s*:", re.IGNORECASE),
    re.compile(
        r"\bNews\s*:?[ \t]*(?:20\d{2}[-/]\d{1,2}[-/]\d{1,2}|"
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+"
        r"\d{1,2}(?:st|nd|rd|th)?,?\s+20\d{2})",
        re.IGNORECASE,
    ),
)

_HISTORY_END_MARKERS: tuple[str, ...] = (
    "table of contents",
    "model introduction",
    "models name",
    "quick start",
    "🌱 source",
    "source :",
)


def _history_bounds(summary: str) -> tuple[int, int] | None:
    """Return the most plausible release-history interval in flattened page text."""
    starts: list[int] = []
    for pattern in _HISTORY_START_PATTERNS:
        match = pattern.search(summary)
        if match is not None:
            starts.append(match.start())
    if not starts:
        return None

    # Project/Change-log headings are stronger than generic page chrome. Taking the earliest
    # recognized history marker also preserves LTX pages where Table of Contents appears before
    # the News history: end markers are searched only *after* the selected history start.
    start = min(starts)
    lower = summary.lower()
    ends: list[int] = []
    for marker in _HISTORY_END_MARKERS:
        pos = lower.find(marker.lower(), start + 32)
        if pos >= 0:
            ends.append(pos)
    end = min(ends) if ends else len(summary)
    if end <= start:
        return None
    return start, end


def _matching_event_positions(text: str, events: list[tuple[str, str]]) -> list[int]:
    lower = text.lower()
    positions: list[int] = []
    for date, _kind in events:
        try:
            variants = event._date_variants(date)
        except ValueError:
            continue
        for variant in variants:
            needle = variant.lower()
            cursor = 0
            while True:
                pos = lower.find(needle, cursor)
                if pos < 0:
                    break
                positions.append(pos)
                cursor = pos + max(1, len(needle))
    return positions


def _last_event_position(summary: str, events: list[tuple[str, str]]) -> int | None:
    bounds = _history_bounds(summary)
    if bounds is None:
        return _BASE_LAST_EVENT_POSITION(summary, events)
    start, end = bounds
    local_positions = _matching_event_positions(summary[start:end], events)
    if local_positions:
        # Multiple entries can share one date (CogVideoX has a VAE entry followed by the actual
        # model release). The last occurrence *inside the history interval* is the desired event,
        # while identical dates in later current model tables are now unreachable.
        return start + max(local_positions)
    # A recognized history with no target date is not permission to widen to the rest of the
    # living page. Returning None preserves fail-closed behavior.
    return None


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = event._last_event_position
    event._last_event_position = _last_event_position
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["living_history_date_resolution"] = "HISTORY_REGION_ONLY_V1"
        return result
    finally:
        event._last_event_position = previous


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
