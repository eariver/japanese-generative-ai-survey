#!/usr/bin/env python3
"""Compatibility router for adaptive and Publication Preview Special repairs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_adaptive_spacing_core as core

# Static compatibility markers retained for the Special source-expansion contract.
# The unchanged implementation lives in revise_special_adaptive_spacing_core.py:
#   \Needspace{0.45\textheight}
#   forced_bibliography_clearpage


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    if changes.get("suppress_zero_evidence_technical_notes") is True:
        from scripts.revise_special_suppress_empty_technical_notes import build as suppress_empty_notes_build
        return suppress_empty_notes_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_reference_common_urldate_consolidation") is True:
        from scripts.revise_special_half_year_reference_common_urldate_v3 import build as common_urldate_build
        return common_urldate_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_reference_raggedright_compaction") is True:
        from scripts.revise_special_half_year_reference_raggedright import build as reference_raggedright_build
        return reference_raggedright_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_reference_multicol_compaction") is True:
        from scripts.revise_special_half_year_reference_multicol import build as reference_multicol_build
        return reference_multicol_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_reader_quality_cleanup") is True:
        from scripts.revise_special_half_year_reader_quality_cleanup import build as reader_quality_build
        return reader_quality_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_final_pagination_compaction") is True:
        from scripts.revise_special_half_year_final_pagination_compaction import build as final_pagination_build
        return final_pagination_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_visual_compaction") is True:
        from scripts.revise_special_half_year_visual_compaction import build as visual_compaction_build
        return visual_compaction_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_reference_title_repair") is True:
        from scripts.revise_special_half_year_reference_titles import build as reference_title_build
        return reference_title_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("sparse_half_year_architecture_repairs") is True:
        from scripts.revise_special_half_year_sparse_architecture_repairs_v3 import build as sparse_half_year_build
        return sparse_half_year_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_review_repairs_v3") is True:
        from scripts.revise_special_half_year_review_repairs_v34 import build as half_year_v3_build
        return half_year_v3_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("dense_theme_table_font_guard") is True:
        from scripts.revise_special_dense_theme_table import build as dense_theme_build
        return dense_theme_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("prebuild_visual_review_repairs") is True:
        from scripts.revise_special_prebuild_visual_review_repairs import build as prebuild_repair
        return prebuild_repair(repo_root, special_slug, issue_id, source_version)
    if changes.get("h1_publication_preview_repairs") is True:
        from scripts.revise_special_h1_publication_preview_repairs import build as h1_build
        return h1_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("half_year_review_repairs") is True:
        from scripts.revise_special_half_year_review_repairs_v2 import build as half_year_build
        return half_year_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("generic_technical_note_tail_policy") is True:
        from scripts.revise_special_technical_note_tail_policy import build as tail_policy_build
        return tail_policy_build(repo_root, special_slug, issue_id, source_version)
    if changes.get("preserve_current_layout_visual_review_repairs") is True:
        from scripts.revise_special_preserve_preview_repairs_retrospective import build as preserve_build
        return preserve_build(repo_root, special_slug, issue_id, source_version)
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
