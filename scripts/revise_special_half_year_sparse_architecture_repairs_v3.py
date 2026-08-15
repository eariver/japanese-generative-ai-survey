#!/usr/bin/env python3
"""Legacy reader-surface compatibility for sparse Half-year repairs.

Early validated source manifests predate the per-article ``technical_notes_reader_facing`` flag.
Their ``main.tex`` nevertheless directly renders the Technical Notes files.  V28 intentionally
requires the flag for modern manifests, so this wrapper relaxes only the legacy *absence* case:
an article is reader-facing when its Technical Notes path is directly input by the state-pinned
main TeX unless the manifest explicitly sets ``technical_notes_reader_facing`` to false.

The semantic/provenance repair itself remains v2 and therefore the current v30 fail-closed chain.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v28 as rendered
from scripts import revise_special_half_year_sparse_architecture_repairs_v2 as base


def _legacy_rendered_note_context(
    repo_root: Path, manifest: dict[str, Any]
) -> tuple[Path, dict[str, Any], set[str]]:
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    state = rendered._load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_rel = str(source.get("path") or "")
    current_manifest_path = repo_root / manifest_rel
    if not manifest_rel or not current_manifest_path.is_file():
        raise ValueError("state-pinned validated source manifest missing while resolving rendered Technical Notes")
    current_manifest = rendered._load_json(current_manifest_path)
    source_dir = current_manifest_path.parent

    main_info = current_manifest.get("main_tex")
    main_rel = "main.tex"
    if isinstance(main_info, dict):
        main_rel = rendered._normalize_tex_path(str(main_info.get("path") or main_rel))
    main_path = source_dir / main_rel
    if not main_path.is_file():
        raise ValueError(f"state-pinned main TeX missing while resolving rendered Technical Notes: {main_rel}")
    inputs = {
        rendered._normalize_tex_path(match.group(1))
        for match in rendered._INPUT_RE.finditer(main_path.read_text(encoding="utf-8"))
        if rendered._normalize_tex_path(match.group(1))
    }

    rendered_paths: set[str] = set()
    legacy_absent_flags = 0
    for article in current_manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        if article.get("technical_notes_reader_facing") is False:
            continue
        if "technical_notes_reader_facing" not in article:
            legacy_absent_flags += 1
        rel = rendered._normalize_tex_path(str(article.get("technical_notes_path") or ""))
        if rel and rel in inputs:
            rendered_paths.add(rel)
    if not rendered_paths:
        raise ValueError("state-pinned main TeX contains no rendered Technical Notes files under legacy-compatible detection")
    if legacy_absent_flags < 1:
        # Do not silently weaken the modern contract. Sparse compatibility should only invoke this
        # path for genuinely legacy manifests missing the field.
        raise ValueError("legacy rendered-note compatibility requested but no article flags are absent")
    return source_dir, current_manifest, rendered_paths


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    original = rendered._state_pinned_rendered_note_context
    rendered._state_pinned_rendered_note_context = _legacy_rendered_note_context
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        rendered._state_pinned_rendered_note_context = original
    result = dict(result)
    result["legacy_rendered_note_detection"] = "main-tex-direct-input-unless-explicit-false-v1"
    return result


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
