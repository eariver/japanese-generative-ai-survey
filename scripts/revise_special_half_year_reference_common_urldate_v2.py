#!/usr/bin/env python3
"""Normalize Half-year common References access-date rendering without weakening layout checks.

The first common-urldate pass placed the biblatex hook immediately before ``printbibliography``,
which interrupted the exact, audited two-column References block. This compatibility layer keeps the
same semantics but places the hook immediately before the References ``multicols`` environment.
It also accepts an already-consolidated parent so an immutable failed-build revision can be repaired
by a descendant rather than mutated.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts import revise_special_half_year_reference_common_urldate as base

HOOK = r"\AtEveryBibitem{\clearfield{urldate}\clearfield{urlyear}\clearfield{urlmonth}\clearfield{urlday}}"
REFERENCE_MULTICOL_MARKER = "% half-year References two-column compaction"
RAGGED_MARKER = "% half-year References ragged-right compaction"


def normalized_rewrite_main(main_path: Path, access_date: str) -> bool:
    text = main_path.read_text(encoding="utf-8")
    old_intro = base.OLD_INTRO
    new_intro = (
        r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。"
        r"各entryでは識別・追跡に必要な資料名、組織、URLを示す。全URLの参照日は"
        + access_date
        + r"である。}}\par"
    )
    if old_intro in text:
        if text.count(old_intro) != 1:
            raise ValueError("legacy References introduction is ambiguous")
        text = text.replace(old_intro, new_intro, 1)
    elif new_intro not in text:
        raise ValueError("neither legacy nor consolidated References introduction is present")

    # Remove the hook from any previous position before re-inserting it at the audited boundary.
    hook_block = base.HOOK_MARKER + "\n" + HOOK + "\n"
    text = text.replace(hook_block, "")
    if base.HOOK_MARKER in text or HOOK in text:
        raise ValueError("common urldate hook remains in an unexpected shape")

    marker_at = text.find(REFERENCE_MULTICOL_MARKER)
    if marker_at < 0:
        raise ValueError("two-column References marker missing")
    begin = r"\begin{multicols}{2}"
    begin_at = text.find(begin, marker_at)
    if begin_at < 0:
        raise ValueError("References multicols start missing")
    ragged_at = text.find(RAGGED_MARKER, begin_at)
    print_at = text.find(base.PRINT_BIB, begin_at)
    if ragged_at < begin_at or print_at < ragged_at:
        raise ValueError("unexpected References two-column/ragged-right structure")

    insertion = base.HOOK_MARKER + "\n" + HOOK + "\n"
    revised = text[:begin_at] + insertion + text[begin_at:]
    expected_body = (
        begin
        + "\n"
        + RAGGED_MARKER
        + "\n"
        + r"\raggedright"
        + "\n"
        + base.PRINT_BIB
        + "\n"
        + r"\end{multicols}"
    )
    if expected_body not in revised:
        raise ValueError("normalized hook placement did not preserve audited References body")
    if revised.count(HOOK) != 1 or revised.count(base.HOOK_MARKER) != 1:
        raise ValueError("common urldate hook cardinality mismatch")
    main_path.write_text(revised, encoding="utf-8")
    return revised != main_path.read_text(encoding="utf-8") if False else True


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str):
    previous = base.rewrite_main
    base.rewrite_main = normalized_rewrite_main
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base.rewrite_main = previous
    if isinstance(result, dict):
        result = dict(result)
        result["common_urldate_hook_position"] = "BEFORE_REFERENCES_MULTICOLS_V2"
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
