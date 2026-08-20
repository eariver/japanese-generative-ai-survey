#!/usr/bin/env python3
"""Annual Publication Preview repair with strict actual-source bibliography titles.

Issue #78 is broader than the old ``Primary source N`` fallback: legacy Annual sources may already
carry readable but story-level labels such as ``GPT-3``, ``RAG``, ``REALM`` or ``GShard``.  For an
Annual edition we already have an immutable accepted chronology whose exact locator is paired with
the source's paper/article title.  This wrapper therefore replaces a bibliography title whenever
that exact URL has a chronology-backed title, even if the existing title is not a generic fallback.

The operation is deliberately Annual-only and URL-exact.  It does not widen the shared Special
bibliography helper, mutate chronology identities, fetch external metadata, or change accepted
Article Draft claims / Evidence / Architecture.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_review_sequence as annual
from scripts import revise_special_annual_review_sequence_generic_v2 as base
from scripts.revise_special_visual_review_repairs import bib_escape

_ENTRY_RE = re.compile(r"@online\{.*?\n\}", re.DOTALL)
_URL_RE = re.compile(r"\n\s*url\s*=\s*\{([^}]*)\},?")
_TITLE_RE = re.compile(r"(\n\s*title\s*=\s*\{)(.*?)(\},)", re.DOTALL)
_CONTRACT = "ANNUAL_EXACT_LOCATOR_ACTUAL_SOURCE_TITLE_V1"


def _strict_actual_source_titles(path: Path, title_by_url: dict[str, str]) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    changed = 0
    mapped = 0

    def replace_entry(match: re.Match[str]) -> str:
        nonlocal changed, mapped
        block = match.group(0)
        url_match = _URL_RE.search(block)
        title_match = _TITLE_RE.search(block)
        if not url_match or not title_match:
            return block
        url = url_match.group(1).strip()
        actual = str(title_by_url.get(url) or "").strip()
        if not actual:
            return block
        mapped += 1
        expected = bib_escape(actual)
        current = title_match.group(2).strip()
        if current == expected:
            return block
        replacement = title_match.group(1) + expected + title_match.group(3)
        changed += 1
        return block[: title_match.start()] + replacement + block[title_match.end() :]

    revised = _ENTRY_RE.sub(replace_entry, text)
    # Fail closed for every bibliography entry whose exact URL has an accepted title mapping.
    mismatches: list[dict[str, str]] = []
    for match in _ENTRY_RE.finditer(revised):
        block = match.group(0)
        url_match = _URL_RE.search(block)
        title_match = _TITLE_RE.search(block)
        if not url_match or not title_match:
            continue
        url = url_match.group(1).strip()
        actual = str(title_by_url.get(url) or "").strip()
        if not actual:
            continue
        expected = bib_escape(actual)
        current = title_match.group(2).strip()
        if current != expected:
            mismatches.append({"url": url, "expected": expected, "current": current})
    if mismatches:
        raise ValueError(f"#78 actual-source title mismatch remains: {mismatches[:5]}")
    if mapped < 1:
        raise ValueError("#78 strict Annual title repair found no exact-locator title mappings")
    path.write_text(revised, encoding="utf-8")
    return changed, len(_ENTRY_RE.findall(revised))


def build(repo_root: Path, special_slug: str, issue_id: str, parent_version: str) -> dict[str, Any]:
    previous = annual.enrich_bibliography_titles
    annual.enrich_bibliography_titles = _strict_actual_source_titles
    try:
        result = base.build(repo_root, special_slug, issue_id, parent_version)
    finally:
        annual.enrich_bibliography_titles = previous
    result = dict(result)
    result["annual_actual_source_title_contract"] = _CONTRACT
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--parent-source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root), args.special_slug, args.issue_id, args.parent_source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
