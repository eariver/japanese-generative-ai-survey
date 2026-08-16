#!/usr/bin/env python3
"""Annual source-specific Technical Notes repair with manifest-shape compatibility.

The Annual source manifest predates the Half-year per-article
``technical_notes_reader_facing`` flag.  The hardened incremental engine and its rendered-scope
preflight intentionally use that flag to decide which note files are reader-facing.  This adapter
marks only Annual articles that carry selected Evidence records in in-memory copies passed to those
inherited layers.  The current validated source on disk is never mutated; the flag is materialized
only in the new immutable revision.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes as base
from scripts import revise_special_half_year_review_repairs_v28 as render_scope


_INCREMENTAL = base.incremental
_ORIGINAL_INCREMENTAL_BUILD = _INCREMENTAL._incremental_build
_ORIGINAL_RENDER_CONTEXT = render_scope._state_pinned_rendered_note_context
_COMPAT_CONTRACT = "EVIDENCE_BACKED_READER_FACING_FLAGS_IN_MEMORY_V2"


def _reader_flagged_manifest(manifest: dict[str, Any]) -> tuple[dict[str, Any], int]:
    compatible = copy.deepcopy(manifest)
    visible_articles = 0
    for article in compatible.get("articles") or []:
        if not isinstance(article, dict):
            continue
        evidence_count = int(article.get("evidence_record_count") or 0)
        article["technical_notes_reader_facing"] = evidence_count > 0
        if evidence_count > 0:
            visible_articles += 1
    if visible_articles < 1:
        raise ValueError("Annual compatibility shim found no Evidence-backed Technical Notes articles")
    return compatible, visible_articles


def _annual_incremental_build(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
    marker: dict[str, Any],
    state: dict[str, Any],
    current: dict[str, Any],
    current_manifest: dict[str, Any],
) -> dict[str, Any]:
    compatible, _visible_articles = _reader_flagged_manifest(current_manifest)
    return _ORIGINAL_INCREMENTAL_BUILD(
        repo_root,
        special_slug,
        issue_id,
        source_version,
        marker,
        state,
        current,
        compatible,
    )


def _annual_state_pinned_rendered_note_context(
    repo_root: Path, manifest: dict[str, Any]
) -> tuple[Path, dict[str, Any], set[str]]:
    """Resolve V28 rendered scope without mutating the legacy Annual parent manifest.

    V28 reloads the state-pinned manifest from disk before the incremental copy is made, so the
    incremental adapter alone cannot expose reader-facing flags soon enough.  Reproduce V28's
    state-pinned input-graph check against an in-memory reader-flagged copy of that exact manifest.
    The main.tex path and direct input membership checks remain identical to V28.
    """
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    state = render_scope._load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_rel = str(source.get("path") or "")
    current_manifest_path = repo_root / manifest_rel
    if not manifest_rel or not current_manifest_path.is_file():
        raise ValueError("state-pinned validated source manifest missing while resolving Annual Technical Notes")
    current_manifest = render_scope._load_json(current_manifest_path)
    compatible, _visible_articles = _reader_flagged_manifest(current_manifest)
    source_dir = current_manifest_path.parent

    main_info = compatible.get("main_tex")
    main_rel = "main.tex"
    if isinstance(main_info, dict):
        main_rel = render_scope._normalize_tex_path(str(main_info.get("path") or main_rel))
    main_path = source_dir / main_rel
    if not main_path.is_file():
        raise ValueError(f"state-pinned main TeX missing while resolving Annual Technical Notes: {main_rel}")
    inputs = {
        render_scope._normalize_tex_path(match.group(1))
        for match in render_scope._INPUT_RE.finditer(main_path.read_text(encoding="utf-8"))
        if render_scope._normalize_tex_path(match.group(1))
    }

    rendered_paths: set[str] = set()
    for article in compatible.get("articles") or []:
        if not isinstance(article, dict) or article.get("technical_notes_reader_facing") is not True:
            continue
        rel = render_scope._normalize_tex_path(str(article.get("technical_notes_path") or ""))
        if rel and rel in inputs:
            rendered_paths.add(rel)
    if not rendered_paths:
        raise ValueError("state-pinned Annual main TeX contains no rendered Evidence-backed Technical Notes files")
    return source_dir, compatible, rendered_paths


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_incremental = _INCREMENTAL._incremental_build
    previous_render_context = render_scope._state_pinned_rendered_note_context
    _INCREMENTAL._incremental_build = _annual_incremental_build
    render_scope._state_pinned_rendered_note_context = _annual_state_pinned_rendered_note_context
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        _INCREMENTAL._incremental_build = previous_incremental
        render_scope._state_pinned_rendered_note_context = previous_render_context
    result = dict(result)
    result["annual_manifest_compatibility"] = _COMPAT_CONTRACT
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
