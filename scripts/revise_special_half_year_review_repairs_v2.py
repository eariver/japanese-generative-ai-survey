#!/usr/bin/env python3
"""Compatibility wrapper for duplicate fallbacks and historical H2 taxonomy forms."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs as core
from scripts.render_article_draft_tex import tex_escape


def replace_generic_items(
    block: str,
    title: str,
    replacements: dict[str, list[dict[str, str]]],
) -> tuple[str, int]:
    generic_lines = [
        line
        for line in block.splitlines()
        if line.startswith(r"\item ") and any(p in line for p in core._GENERIC_FALLBACKS)
    ]
    if not generic_lines:
        return block, 0
    items = replacements.get(title)
    if items is None:
        raise ValueError(f"generic Technical Notes fallback has no reviewed replacement: {title}")
    if len(items) != len(generic_lines):
        raise ValueError(
            f"Technical Notes replacement count mismatch for {title}: {len(generic_lines)} != {len(items)}"
        )
    revised = block
    for old, item in zip(generic_lines, items):
        if old not in revised:
            raise ValueError(f"fallback bullet disappeared before replacement in {title}")
        new = r"\item \textbf{" + tex_escape(item["label"]) + "}: " + tex_escape(item["text_ja"])
        revised = revised.replace(old, new, 1)
    return revised, len(items)


_ORIGINAL_TRANSLATE = core.reader_notes.translate_machine_labels_compat


def translate_historical_h2_taxonomy(text: str) -> str:
    rendered = _ORIGINAL_TRANSLATE(text)
    replacements = {
        "製品 TOOLING（公開）": "製品ツール（公開）",
        "CODING Agent（更新）": "Coding Agent（更新）",
    }
    for old, new in replacements.items():
        rendered = rendered.replace(old, new)
    return rendered


# The core build resolves these operations from module globals. Rebind narrowly;
# all evidence/source/state validators and the final taxonomy checker remain unchanged.
core.replace_generic_items = replace_generic_items
core.reader_notes.translate_machine_labels_compat = translate_historical_h2_taxonomy


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    return core.build(repo_root, special_slug, issue_id, source_version)


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
