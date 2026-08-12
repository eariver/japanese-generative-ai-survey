#!/usr/bin/env python3
"""Generic break-quality policy for Special Technical Notes card tails.

The whole tcolorbox remains breakable.  Only the reader-facing boundary/limitation
block and primary-source block are kept together so a page cannot begin with a
source-only or tiny limitation/source remainder.
"""
from __future__ import annotations

import re
from typing import NamedTuple

GENERIC_TAIL_GROUP_MARKER = "% reader-facing Technical Notes generic boundary/source tail group"
LEGACY_PROTECTED_MARKERS = (
    "% reader-facing Technical Notes coherent tail group",
    "% reader-facing Technical Notes limitation/source fallback group",
)
BOUNDARY_HEADING = r"{\bfseries 読む際の境界}"
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


def unprotected_tail_titles(text: str) -> list[str]:
    result: list[str] = []
    for match in NOTE_RE.finditer(text):
        body = match.group("body")
        if BOUNDARY_HEADING not in body or SOURCE_HEADING not in body:
            continue
        if not _tail_is_protected(body):
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
