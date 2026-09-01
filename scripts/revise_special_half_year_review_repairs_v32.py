#!/usr/bin/env python3
"""Fail closed on long unanchored Half-year source pages and accept zero-padded dates.

Issue #191 exposed a remaining provenance boundary in reader-facing Technical Notes. Some
first-party historical pages are preserved as current HTML snapshots whose navigation chrome
precedes the dated article body. The event-bounded extractor already avoids looking backward
once it finds the event date, but its date variants normalized ``Apr 04, 2024`` to
``Apr 4, 2024``. When the literal marker was therefore missed, every unanchored source fell
through to the concise-feed fallback and the first 4,000 characters of current navigation
could be mined as if they were event-local facts.

V32 tightens that boundary without mutating accepted Evidence:

* month-name dates accept both zero-padded and unpadded day forms;
* an unanchored fallback is retained only for genuinely concise summaries;
* long HTML/snapshot text with no target event marker fails closed, forcing a hash-bound
  editorial override instead of widening the provenance window.

All V31 deduplication, V3 subject/component/variant/property binding, rendered-card scoping,
and immutable-revision behavior remain inherited.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v13 as legacy_event
from scripts import revise_special_half_year_review_repairs_v15 as event_layer
from scripts import revise_special_half_year_review_repairs_v31 as base

_ORIGINAL_DATE_VARIANTS = legacy_event._date_variants
_LONG_UNANCHORED_SOURCE_LIMIT = 6000
_EVENT_WINDOW_CONTRACT = "ZERO_PADDED_DATE_AND_LONG_HTML_FAIL_CLOSED_V1"


def _date_variants(date: str) -> tuple[str, ...]:
    """Return legacy variants plus literal zero-padded month-name forms."""
    variants = list(_ORIGINAL_DATE_VARIANTS(date))
    dt = datetime.strptime(str(date)[:10], "%Y-%m-%d")
    variants.extend(
        (
            dt.strftime("%B %d, %Y"),
            dt.strftime("%b %d, %Y"),
        )
    )
    out: list[str] = []
    seen: set[str] = set()
    for value in variants:
        key = value.lower()
        if key not in seen:
            seen.add(key)
            out.append(value)
    return tuple(out)


def _safe_event_window(summary: str, events: list[tuple[str, str]], title: str = "") -> str:
    if not summary:
        return ""

    abstract = legacy_event._abstract_window(summary)
    if abstract:
        return abstract

    pos = legacy_event._last_event_position(summary, events)
    if pos is None:
        # The historical fallback exists for concise feed/RSS records. A long current HTML
        # snapshot is semantically different: its head is normally navigation or page chrome,
        # so mining it without an event anchor can back-project current product terminology.
        if len(summary) > _LONG_UNANCHORED_SOURCE_LIMIT:
            return ""
        return summary[:4000]

    segment = summary[pos:]
    if legacy_event._is_living_changelog(summary):
        next_date = legacy_event._DATE_TOKEN_RE.search(segment, 24)
        if next_date is not None:
            segment = segment[: next_date.start()]
        return event_layer._trim_living_structural_tail(segment)

    anchor = legacy_event._artifact_anchor(segment, title)
    if anchor is not None:
        segment = segment[anchor:]
    return segment[:4200].strip()


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_date_variants = legacy_event._date_variants
    previous_window = event_layer._safe_event_window
    legacy_event._date_variants = _date_variants
    event_layer._safe_event_window = _safe_event_window
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        legacy_event._date_variants = previous_date_variants
        event_layer._safe_event_window = previous_window
    if isinstance(result, dict):
        result = dict(result)
        result["event_window_contract"] = _EVENT_WINDOW_CONTRACT
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
