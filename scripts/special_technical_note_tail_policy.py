#!/usr/bin/env python3
"""Generic break-quality policy for Special Technical Notes card tails.

The whole tcolorbox remains breakable. Only the reader-facing coherent tail is kept
together so a page cannot begin with a source-only or tiny remainder. Cards with a
boundary keep boundary/source together; compact event-only cards with exactly one
verified fact keep that fact/source tail together.
"""
from __future__ import annotations

import re
from typing import NamedTuple

GENERIC_TAIL_GROUP_MARKER = "% reader-facing Technical Notes generic boundary/source tail group"
EVENT_ONLY_TAIL_GROUP_MARKER = "% reader-facing Technical Notes event-only fact/source tail group"
LEGACY_PROTECTED_MARKERS = (
    "% reader-facing Technical Notes coherent tail group",
    "% reader-facing Technical Notes limitation/source fallback group",
)
BOUNDARY_HEADING = r"{\bfseries 読む際の境界}"
TECHNICAL_POINTS_HEADING = r"{\bfseries 一次資料から整理したtechnical points}"
VERIFIED_FACT_MARKER = r"\item \textbf{一次情報で確認できる事実}:"
SOURCE_HEADING = r"{\bfseries 一次資料}"
SOURCE_END = r"\end{samepage}"

NOTE_RE = re.compile(
    r"(?P<open>\\begin\{technicalnote\}\{(?P<title>.*?)\}\{.*?\}\n)"
    r"(?P<body>.*?)"
    r"(?P<close>\\end\{technicalnote\})",
    re.DOTALL,
)


class TailPolicyResult(NamedTuple):
    text: str
    groups_added: int
    card_count: int
    protected_card_count: int


def _tail_is_protected(body: str) -> bool:
    source_pos = body.find(SOURCE_HEADING)
    boundary_pos = body.find(BOUNDARY_HEADING)
    if source_pos < 0 or boundary_pos < 0 or boundary_pos > source_pos:
        return False
    markers = (GENERIC_TAIL_GROUP_MARKER,) + LEGACY_PROTECTED_MARKERS
    marker_positions = [body.find(marker) for marker in markers if marker in body]
    if not marker_positions:
        return False
    marker_pos = min(pos for pos in marker_positions if pos >= 0)
    end_pos = body.find(r"\end{minipage}", source_pos)
    return marker_pos < boundary_pos and end_pos > source_pos


def _event_only_tail_is_protected(body: str) -> bool:
    points_pos = body.find(TECHNICAL_POINTS_HEADING)
    source_pos = body.find(SOURCE_HEADING, max(points_pos, 0))
    if points_pos < 0 or source_pos < 0 or EVENT_ONLY_TAIL_GROUP_MARKER not in body:
        return False
    marker_pos = body.find(EVENT_ONLY_TAIL_GROUP_MARKER)
    end_pos = body.find(r"\end{minipage}", source_pos)
    return marker_pos < points_pos < source_pos < end_pos


def unprotected_tail_titles(text: str) -> list[str]:
    result: list[str] = []
    for match in NOTE_RE.finditer(text):
        body = match.group("body")
        if BOUNDARY_HEADING in body and SOURCE_HEADING in body:
            if not _tail_is_protected(body):
                result.append(match.group("title"))
            continue
        if (
            TECHNICAL_POINTS_HEADING in body
            and SOURCE_HEADING in body
            and body.count(VERIFIED_FACT_MARKER) == 1
        ):
            if not _event_only_tail_is_protected(body):
                result.append(match.group("title"))
    return result


def apply_generic_tail_policy(text: str) -> TailPolicyResult:
    groups_added = 0
    card_count = 0
    protected_count = 0

    def replace_note(match: re.Match[str]) -> str:
        nonlocal groups_added, card_count, protected_count
        card_count += 1
        body = match.group("body")

        # Event-only Evidence cards do not have a limitation/boundary block. When
        # they contain exactly one directly verified fact, keep the compact
        # fact/source tail together. This avoids a URL-only or source-only page-top
        # remainder without making the whole Technical Notes card unbreakable.
        if BOUNDARY_HEADING not in body and TECHNICAL_POINTS_HEADING in body and SOURCE_HEADING in body:
            if _event_only_tail_is_protected(body):
                protected_count += 1
                return match.group(0)
            points_pos = body.find(TECHNICAL_POINTS_HEADING)
            source_pos = body.find(SOURCE_HEADING, points_pos)
            source_end_pos = body.find(SOURCE_END, source_pos)
            points_segment = body[points_pos:source_pos]
            item_count = len(re.findall(r"(?m)^\\item\b", points_segment))
            fact_count = points_segment.count(VERIFIED_FACT_MARKER)
            if source_end_pos >= 0 and item_count == 1 and fact_count == 1:
                source_end_pos += len(SOURCE_END)
                tail = body[points_pos:source_end_pos]
                replacement = (
                    body[:points_pos]
                    + r"\begin{minipage}{\linewidth}"
                    + "\n"
                    + EVENT_ONLY_TAIL_GROUP_MARKER
                    + "\n"
                    + tail
                    + "\n"
                    + r"\end{minipage}"
                    + body[source_end_pos:]
                )
                groups_added += 1
                protected_count += 1
                return match.group("open") + replacement + match.group("close")

        if BOUNDARY_HEADING not in body or SOURCE_HEADING not in body:
            return match.group(0)
        if _tail_is_protected(body):
            protected_count += 1
            return match.group(0)

        boundary_pos = body.find(BOUNDARY_HEADING)
        samepage_pos = body.find(r"\begin{samepage}", boundary_pos)
        source_pos = body.find(SOURCE_HEADING, boundary_pos)
        source_end_pos = body.find(SOURCE_END, source_pos)
        if samepage_pos < 0 or source_pos < 0 or source_end_pos < 0:
            return match.group(0)
        if not (boundary_pos < samepage_pos < source_pos < source_end_pos):
            return match.group(0)

        source_end_pos += len(SOURCE_END)
        tail = body[boundary_pos:source_end_pos]
        replacement = (
            body[:boundary_pos]
            + r"\begin{minipage}{\linewidth}"
            + "\n"
            + GENERIC_TAIL_GROUP_MARKER
            + "\n"
            + tail
            + "\n"
            + r"\end{minipage}"
            + body[source_end_pos:]
        )
        groups_added += 1
        protected_count += 1
        return match.group("open") + replacement + match.group("close")

    revised = NOTE_RE.sub(replace_note, text)
    return TailPolicyResult(revised, groups_added, card_count, protected_count)
