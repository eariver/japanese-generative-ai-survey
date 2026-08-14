#!/usr/bin/env python3
"""Compatibility entry point that restores Technical Notes source URLs from Evidence.

Historical reader-facing revisions may already contain a mutated URL before the identifier-safe
translator runs. For a new immutable derived revision, rebuild each Technical Notes URL list from
the selected structured Evidence when (and only when) the number of displayed source URLs matches
the Evidence URL count. The v3 strict URL-set check then verifies exact canonical identity.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v4 as compat

core = compat.core
_ORIGINAL_REPAIR_NOTE_FILE = core.repair_note_file


def restore_note_urls_from_evidence(path: Path, evidence: dict[str, dict[str, Any]]) -> int:
    text = path.read_text(encoding='utf-8')
    matches = list(core.NOTE_RE.finditer(text))
    changes: list[tuple[int, int, str]] = []
    repaired = 0
    for match in matches:
        block = match.group(0)
        title = match.group(1)
        info = evidence.get(title)
        if info is None:
            # Let the canonical binding validator produce the definitive error later.
            continue
        expected_urls = list(info.get('urls') or [])
        actual_urls = core.URL_RE.findall(block)
        if actual_urls == expected_urls:
            continue
        if len(actual_urls) != len(expected_urls):
            raise ValueError(
                f'Technical Notes canonical URL restoration count mismatch for {title}: '
                f'actual={len(actual_urls)} expected={len(expected_urls)}'
            )
        iterator = iter(expected_urls)

        def replace_url(_match):
            nonlocal repaired
            repaired += 1
            return r'\url{' + next(iterator) + '}'

        revised = core.URL_RE.sub(replace_url, block)
        changes.append((match.start(), match.end(), revised))
    for start, end, revised in reversed(changes):
        text = text[:start] + revised + text[end:]
    if changes:
        path.write_text(text, encoding='utf-8')
    return repaired


def repair_note_file(path: Path, evidence: dict[str, dict[str, Any]]) -> tuple[int, int, int]:
    restore_note_urls_from_evidence(path, evidence)
    return _ORIGINAL_REPAIR_NOTE_FILE(path, evidence)


# v3 build resolves the note repair from its module global at runtime.
core.repair_note_file = repair_note_file


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    return compat.build(repo_root, special_slug, issue_id, source_version)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', default='.')
    parser.add_argument('--special-slug', required=True)
    parser.add_argument('--issue-id', required=True)
    parser.add_argument('--source-version', required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
