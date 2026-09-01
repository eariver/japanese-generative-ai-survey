#!/usr/bin/env python3
"""Place the Half-year common access-date biblatex hook in the LaTeX preamble.

``\\AtEveryBibitem`` is a preamble-only biblatex command. Earlier immutable descendants established
the correct reader semantics but placed the hook in the document body. This compatibility layer
removes any prior body placement, preserves the audited References block exactly, and inserts the
same hook immediately after ``\\addbibresource{references.bib}`` in the preamble.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts import revise_special_half_year_reference_common_urldate as base
from scripts import revise_special_half_year_reference_common_urldate_v2 as v2

HOOK = v2.HOOK
PREAMBLE_ANCHOR = r"\addbibresource{references.bib}"
BEGIN_DOCUMENT = r"\begin{document}"


def preamble_rewrite_main(main_path: Path, access_date: str) -> bool:
    original = main_path.read_text(encoding="utf-8")
    text = original

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

    hook_block = base.HOOK_MARKER + "\n" + HOOK + "\n"
    text = text.replace(hook_block, "")
    # Also fail closed on an unmarked command left by a malformed prior descendant.
    if HOOK in text:
        raise ValueError("common urldate hook remains in an unexpected shape")
    if base.HOOK_MARKER in text:
        raise ValueError("common urldate marker remains without its hook")

    if text.count(PREAMBLE_ANCHOR) != 1 or text.count(BEGIN_DOCUMENT) != 1:
        raise ValueError("LaTeX preamble anchors are ambiguous")
    anchor_at = text.index(PREAMBLE_ANCHOR)
    document_at = text.index(BEGIN_DOCUMENT)
    if anchor_at > document_at:
        raise ValueError("bibliography resource anchor is not in the preamble")

    insertion = PREAMBLE_ANCHOR + "\n" + base.HOOK_MARKER + "\n" + HOOK
    revised = text.replace(PREAMBLE_ANCHOR, insertion, 1)
    marker_at = revised.index(base.HOOK_MARKER)
    hook_at = revised.index(HOOK)
    document_at = revised.index(BEGIN_DOCUMENT)
    if not marker_at < hook_at < document_at:
        raise ValueError("common urldate hook was not placed in the preamble")

    expected_body = (
        r"\begin{multicols}{2}"
        + "\n"
        + v2.RAGGED_MARKER
        + "\n"
        + r"\raggedright"
        + "\n"
        + base.PRINT_BIB
        + "\n"
        + r"\end{multicols}"
    )
    if expected_body not in revised:
        raise ValueError("preamble hook rewrite did not preserve audited References body")
    if revised.count(HOOK) != 1 or revised.count(base.HOOK_MARKER) != 1:
        raise ValueError("common urldate preamble hook cardinality mismatch")

    main_path.write_text(revised, encoding="utf-8")
    return revised != original


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str):
    previous = base.rewrite_main
    base.rewrite_main = preamble_rewrite_main
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base.rewrite_main = previous
    if isinstance(result, dict):
        result = dict(result)
        result["common_urldate_hook_position"] = "LATEX_PREAMBLE_AFTER_BIBRESOURCE_V3"
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
