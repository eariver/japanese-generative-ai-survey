#!/usr/bin/env python3
"""Create an immutable Annual bibliography pagination v7 revision.

Restricted #140 fallback after v6. The Reference entries, typography, URL presentation,
metadata values, and bibliography bytes are already compact enough; only one final entry remains
isolated. This pass reclaims non-semantic vertical whitespace around the full-width References
heading while preserving heading text, TOC navigation, all reference data, chronology,
accepted drafts, Technical Notes, Evidence, Selection, and Architecture.
"""
from __future__ import annotations

import argparse
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_reference_compaction as annual_refs
from scripts import revise_special_visual_review_repairs as visual

OLD = r"""\Needspace{0.20\textheight}
\smallskip
\noindent{\small Referencesには本文・Detailed Chronologyの検証に用いた一次資料の識別情報とURLを掲載する。各entryに共通する用途説明はここに集約する。}\par
\smallskip
% annual References two-column final compaction
\section*{References / Source Notes}
\addcontentsline{toc}{section}{References / Source Notes}
\begingroup
"""
NEW = r"""\Needspace{0.12\textheight}
\noindent{\small Referencesには本文・Detailed Chronologyの検証に用いた一次資料の識別情報とURLを掲載する。各entryに共通する用途説明はここに集約する。}\par
% annual References compact final-heading spacing
\vspace{-0.35em}
\section*{References / Source Notes}
\addcontentsline{toc}{section}{References / Source Notes}
\vspace{-1.05\baselineskip}
\begingroup
"""


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("Annual References pagination v7 requires RELEASE_CANDIDATE")
    if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "passed":
        raise ValueError("pagination v7 requires passed validation and PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("pagination v7 cannot run after Visual Review/Freeze authority")
    if "publication_preview" in (state.get("provenance") or {}):
        raise ValueError("pagination v7 cannot run after Publication Preview approval")
    if not special_slug.endswith("-Y") or not issue_id.endswith("-Y"):
        raise ValueError("pagination v7 is Annual-only")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    parent_version = str(parent_manifest.get("source_version") or current.get("source_version") or "")
    annual_refs._next_version(parent_version, source_version)
    lr0 = parent_manifest.get("layout_revision") or {}
    required_parent = {
        "annual_reference_pagination_v6": True,
        "references_columns": 3,
        "references_entry_font": "6.0pt/6.5pt",
        "references_columnsep": "6pt",
        "references_raggedright_command": "RaggedRight",
        "references_url_style": "same",
        "references_url_visible_value_changed": False,
        "references_url_hyperlink_target_changed": False,
        "references_metadata_values_changed": False,
        "bibliography_data_changed": False,
        "chronology_event_content_changed": False,
        "reader_semantic_content_changed": False,
    }
    for key, value in required_parent.items():
        if lr0.get(key) != value:
            raise ValueError(f"pagination v7 parent contract mismatch: {key}")
    if int((parent_manifest.get("reader_facing_technical_notes") or {}).get("generic_fallback_findings") or 0) != 0:
        raise ValueError("pagination v7 requires zero generic Technical Notes fallbacks")
    issue272 = parent_manifest.get("issue_272") or {}
    if issue272.get("q1_q4_narrative_preserved") is not True or int(issue272.get("dated_event_count") or 0) != int(issue272.get("cited_event_count") or -1):
        raise ValueError("pagination v7 requires preserved and fully cited Annual chronology")

    chronology = deepcopy((state.get("provenance") or {}).get("annual_chronology") or {})
    chronology_path = repo_root / str(chronology.get("path") or "")
    if not chronology_path.is_file() or visual.sha(chronology_path) != str(chronology.get("sha256") or ""):
        raise ValueError("state-pinned Annual chronology missing or SHA mismatch")
    chronology_sha = visual.sha(chronology_path)
    chronology_event_count = int(chronology.get("event_count") or -1)

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(parent_manifest_path.parent, output_dir)
    manifest_path = output_dir / "source-manifest.json"
    manifest = visual.load_json(manifest_path)
    manifest["source_version"] = source_version
    manifest["status"] = "VALIDATED_ANNUAL_REFERENCE_PAGINATION_V7"
    basis = dict(manifest.get("basis") or {})
    basis.update({
        "previous_source_manifest_path": str(current.get("path") or ""),
        "previous_source_manifest_sha256": str(current.get("sha256") or ""),
    })
    manifest["basis"] = basis

    refs_rel = str((manifest.get("references") or {}).get("path") or "references.bib")
    refs_path = output_dir / refs_rel
    refs_sha = visual.sha(refs_path)
    expected_refs_sha = str((parent_manifest.get("references") or {}).get("sha256") or "")
    if not expected_refs_sha or refs_sha != expected_refs_sha:
        raise ValueError("bibliography bytes differ from parent before pagination v7")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    main_before = visual.sha(main_path)
    text = main_path.read_text(encoding="utf-8")
    if text.count(OLD) != 1:
        raise ValueError(f"expected exactly one v6 References heading block, found {text.count(OLD)}")
    main_path.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")

    if visual.sha(refs_path) != refs_sha or visual.sha(chronology_path) != chronology_sha:
        raise ValueError("pagination v7 changed bibliography or chronology data")
    for article in manifest.get("articles") or []:
        section = output_dir / str(article["article_section_path"])
        if visual.sha(section) != article["article_section_sha256"]:
            raise ValueError(f"accepted article changed: {article['package_id']}")
        notes_rel = str(article.get("technical_notes_path") or "")
        if notes_rel and visual.sha(output_dir / notes_rel) != article["technical_notes_sha256"]:
            raise ValueError(f"Technical Notes changed: {article['package_id']}")

    manifest["main_tex"] = dict(manifest.get("main_tex") or {})
    manifest["main_tex"].update({"path": main_rel, "sha256": visual.sha(main_path)})
    lr = dict(manifest.get("layout_revision") or {})
    lr.update({
        "from_source_version": parent_version,
        "annual_reference_pagination_v7": True,
        "annual_reference_pagination_v7_issue_refs": [140],
        "annual_reference_heading_spacing_compacted": True,
        "references_needspace": "0.12textheight",
        "references_heading_preserved": True,
        "references_heading_toc_navigation": True,
        "references_heading_post_vspace": "-1.05baselineskip",
        "references_intro_pre_section_vspace": "-0.35em",
        "reader_semantic_content_changed": False,
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "accepted_article_sections_changed": False,
        "evidence_cards_changed": False,
        "technical_notes_changed_by_reference_compaction": False,
        "chronology_event_content_changed": False,
        "bibliography_data_changed": False,
        "references_metadata_values_changed": False,
        "references_url_visible_value_changed": False,
        "references_url_hyperlink_target_changed": False,
        "main_tex_sha256_before": main_before,
        "main_tex_sha256_after": visual.sha(main_path),
        "bibliography_sha256_before": refs_sha,
        "bibliography_sha256_after": visual.sha(refs_path),
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
    })
    manifest["layout_revision"] = lr
    visual.write_json(manifest_path, manifest)
    manifest_sha = visual.sha(manifest_path)

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"annual-reference-pagination-v7-{source_version}.json"
    marker = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": parent_version,
        "previous_source_manifest_path": str(current.get("path") or ""),
        "previous_source_manifest_sha256": str(current.get("sha256") or ""),
        "source_manifest_path": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "issue_refs": [140],
        "reason": "v6 left only the final reference isolated; reclaim only non-semantic References heading whitespace without changing reference typography or data.",
        "layout_changes": {
            "references_needspace": "0.12textheight",
            "references_heading_post_vspace": "-1.05baselineskip",
            "references_intro_pre_section_vspace": "-0.35em",
        },
        "constraints": {
            "reader_semantic_content_changed": False,
            "reference_metadata_values_changed": False,
            "visible_url_values_changed": False,
            "url_hyperlink_targets_changed": False,
            "new_external_evidence_allowed": False,
            "accepted_article_claims_changed": False,
            "technical_notes_content_changed": False,
            "chronology_event_content_changed": False,
            "bibliography_data_changed": False,
        },
        "bibliography_sha256": refs_sha,
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
    }
    visual.write_json(marker_path, marker)

    state.setdefault("provenance_history", {}).setdefault("validated_issue_source", []).append(current)
    next_source = deepcopy(current)
    next_source.update({
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "annual-reference-pagination-v7",
    })
    state.setdefault("provenance", {})["validated_issue_source"] = next_source
    state["provenance"]["annual_reference_pagination_v7"] = {
        "source_version": source_version,
        "path": marker_path.relative_to(repo_root).as_posix(),
        "sha256": visual.sha(marker_path),
        "bibliography_sha256": refs_sha,
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
        "reader_semantic_content_changed": False,
        "reference_metadata_values_changed": False,
        "visible_url_values_changed": False,
        "url_hyperlink_targets_changed": False,
    }
    annual_refs._reset_pdf_gate(state)
    visual.write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": parent_version,
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "bibliography_sha256": refs_sha,
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
        "reader_semantic_content_changed": False,
        "reference_metadata_values_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
        "visual_review_gate": state["gates"]["visual_review"],
        "freeze_gate": state["gates"]["freeze"],
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--special-slug", required=True)
    p.add_argument("--issue-id", required=True)
    p.add_argument("--source-version", required=True)
    a = p.parse_args()
    print(json.dumps(build(Path(a.repo_root).resolve(), a.special_slug, a.issue_id, a.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
