#!/usr/bin/env python3
"""Compatibility entry point for Half-year review repair v3 with TeX-title binding.

Reader-facing Technical Notes titles are TeX-escaped renderings of canonical Evidence
artifact names. Bind both forms to the same structured Evidence record while continuing
to use the unescaped canonical title when generating prose.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v3 as core
from scripts.render_article_draft_tex import tex_escape

_ORIGINAL_MERGE = core.merge_evidence_index
_ORIGINAL_FACT = core.source_specific_fact


def merge_evidence_index(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    index = _ORIGINAL_MERGE(repo_root, manifest)
    aliases: dict[str, dict[str, Any]] = {}
    for canonical_title, info in list(index.items()):
        info.setdefault('canonical_title', canonical_title)
        escaped = tex_escape(canonical_title)
        existing = index.get(escaped) or aliases.get(escaped)
        if existing is not None and existing is not info:
            raise ValueError(f'TeX-escaped Technical Notes title collides across Evidence: {escaped}')
        aliases[escaped] = info
    index.update(aliases)
    return index


def source_specific_fact(title: str, info: dict[str, Any]) -> str:
    canonical_title = str(info.get('canonical_title') or title)
    return _ORIGINAL_FACT(canonical_title, info)


# v3 resolves these helpers from module globals at build time.
core.merge_evidence_index = merge_evidence_index
core.source_specific_fact = source_specific_fact


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    return core.build(repo_root, special_slug, issue_id, source_version)


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
