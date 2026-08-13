#!/usr/bin/env python3
"""Shared reader-facing text normalization for Special mixed-layout rendering.

Accepted Article Drafts and Evidence remain immutable. These helpers operate only on
derived LaTeX presentation text so the reader-facing layout can enforce two invariants:

- an opening bold standfirst stays full-width ahead of local narrative multicols; and
- list environments own their bullet marker, avoiding duplicated handwritten bullets.
"""
from __future__ import annotations

import re
from typing import Iterable

MANUAL_BULLET_MARKERS = "・•●◦▪‣"
ITEM_LINE_RE = re.compile(
    r"^(?P<indent>\s*)\\item(?P<label>\[[^\]]*\])?\s+(?P<text>.*?)(?P<newline>\r?\n)?$"
)
MANUAL_BULLET_RE = re.compile(rf"^[{re.escape(MANUAL_BULLET_MARKERS)}]\s*")
MANUAL_ITEM_RE = re.compile(
    rf"(?m)^\s*\\item(?:\[[^\]]*\])?\s+[{re.escape(MANUAL_BULLET_MARKERS)}]"
)
ITEMIZE_BLOCK_RE = re.compile(
    r"\\begin\{itemize\}\n(?P<body>.*?)\\end\{itemize\}",
    re.DOTALL,
)


def first_substantive_line(text: str) -> str:
    """Return the first nonblank, non-comment LaTeX source line."""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or line.lstrip().startswith("%"):
            continue
        return stripped
    return ""


def split_leading_standfirst(lines: list[str]) -> tuple[list[str], list[str]]:
    """Split a generated opening bold standfirst from the narrative body.

    The drafting renderer emits the standfirst as the first substantive paragraph in
    ``\\noindent\\textbf{...}`` form. Leading generated comments and blank lines are
    carried with the standfirst file so the remaining narrative can enter multicols
    without the standfirst becoming a left-column-only block.
    """
    index = 0
    prefix: list[str] = []
    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped or lines[index].lstrip().startswith("%"):
            prefix.append(lines[index])
            index += 1
            continue
        break

    if index >= len(lines) or not lines[index].lstrip().startswith(r"\noindent\textbf{"):
        return [], lines

    end = index + 1
    while end < len(lines) and lines[end].strip():
        end += 1
    if end < len(lines) and not lines[end].strip():
        end += 1
    return prefix + lines[index:end], lines[end:]


def manual_item_marker_findings(text: str) -> list[str]:
    """Return source snippets where an itemize marker would duplicate a manual bullet."""
    return [match.group(0).strip() for match in MANUAL_ITEM_RE.finditer(text)]


def normalize_itemize_manual_markers(text: str) -> tuple[str, int, int]:
    """Normalize simple generated itemize blocks without changing claim wording.

    Every ``\\item`` owns its marker through LaTeX. A leading Japanese/interpunct or
    Unicode bullet in the item text is therefore removed. When a simple generated
    list has one unmarked lead item, a contiguous run of at least three manually
    marked items, and optionally one unmarked trailing item, the unmarked wrapper
    items are lifted out as ordinary paragraphs. This yields the intended structure:
    lead sentence -> sibling bullet list -> trailing explanation.

    Nested or structurally complex itemize blocks are left untouched rather than
    guessed at.
    """
    removed = 0
    lifted = 0

    def replace_block(match: re.Match[str]) -> str:
        nonlocal removed, lifted
        body = match.group("body")
        if r"\begin{itemize}" in body or r"\end{itemize}" in body:
            return match.group(0)

        lines = body.splitlines(keepends=True)
        records: list[tuple[int, re.Match[str], bool]] = []
        for index, line in enumerate(lines):
            if not line.strip() or line.lstrip().startswith("%"):
                continue
            item = ITEM_LINE_RE.match(line)
            if item is None:
                return match.group(0)
            has_manual_marker = MANUAL_BULLET_RE.match(item.group("text")) is not None
            records.append((index, item, has_manual_marker))

        if not records:
            return match.group(0)

        flags = [record[2] for record in records]
        for index, item, has_manual_marker in records:
            if not has_manual_marker:
                continue
            cleaned = MANUAL_BULLET_RE.sub("", item.group("text"), count=1)
            newline = item.group("newline") or ""
            lines[index] = (
                f"{item.group('indent')}\\item{item.group('label') or ''} "
                f"{cleaned}{newline}"
            )
            removed += 1

        marked = [index for index, flag in enumerate(flags) if flag]
        if len(marked) >= 3 and marked == list(range(marked[0], marked[-1] + 1)):
            prefix_count = marked[0]
            suffix_count = len(flags) - marked[-1] - 1
            if prefix_count <= 1 and suffix_count <= 1 and (prefix_count or suffix_count):
                lead = records[0][1].group("text").strip() if prefix_count == 1 else ""
                tail = records[-1][1].group("text").strip() if suffix_count == 1 else ""
                inner: list[str] = []
                for record_index in range(marked[0], marked[-1] + 1):
                    line_index = records[record_index][0]
                    inner.append(lines[line_index])

                parts: list[str] = []
                if lead:
                    parts.append(lead + "\n\n")
                parts.append(r"\begin{itemize}" + "\n")
                parts.extend(inner)
                parts.append(r"\end{itemize}")
                if tail:
                    parts.append("\n\n" + tail)
                lifted += prefix_count + suffix_count
                return "".join(parts)

        return r"\begin{itemize}" + "\n" + "".join(lines) + r"\end{itemize}"

    return ITEMIZE_BLOCK_RE.sub(replace_block, text), removed, lifted
