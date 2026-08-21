#!/usr/bin/env python3
"""Create an immutable layout-only Annual Special final visual compaction revision.

This pass is intentionally narrow and may run only after the standard Annual final References
compaction has already produced a RELEASE_CANDIDATE that remains visually unsatisfactory.  It
addresses two observed render regressions without changing reader semantic content:

* a section-level TOC that still strands one final entry on a mostly empty continuation page;
* a two-column References block whose final page remains low-density.

The pass preserves bibliography bytes, accepted Article Drafts, Technical Notes, Detailed
Chronology, Evidence, Selection, and Architecture.  It only reduces TOC display size and tightens
the already-declared two-column bibliography typography.
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


TOC_OLD = "\\begingroup\n\\footnotesize\n\\setlength{\\parskip}{0pt}\n\\tableofcontents\n\\endgroup"
TOC_NEW = "\\begingroup\n\\scriptsize\n\\setlength{\\parskip}{0pt}\n\\tableofcontents\n\\endgroup"
REF_FONT_OLD = "\\scriptsize\n\\setlength{\\bibitemsep}{0pt}"
REF_FONT_NEW = "\\fontsize{7pt}{8pt}\\selectfont\n\\setlength{\\bibitemsep}{0pt}"
REF_START_OLD = "\\Needspace{0.30\\textheight}\n\\bigskip\n\\noindent{\\small Referencesには本文・Detailed Chronologyの検証に用いた一次資料の識別情報とURLを掲載する。各entryに共通する用途説明はここに集約する。}\\par\n\\smallskip"
REF_START_NEW = "\\Needspace{0.20\\textheight}\n\\smallskip\n\\noindent{\\small Referencesには本文・Detailed Chronologyの検証に用いた一次資料の識別情報とURLを掲載する。各entryに共通する用途説明はここに集約する。}\\par\n\\smallskip"


def _replace_exact(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"expected exactly one {label} block, found {count}")
    return text.replace(old, new, 1)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("Annual final visual compaction requires RELEASE_CANDIDATE")
    if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "passed":
        raise ValueError("Annual final visual compaction requires passed validation and PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Annual final visual compaction cannot run after Visual Review/Freeze authority")
    if "publication_preview" in (state.get("provenance") or {}):
        raise ValueError("Annual final visual compaction cannot run after Publication Preview approval")
    if not special_slug.endswith("-Y") or not issue_id.endswith("-Y"):
        raise ValueError("Annual final visual compaction is restricted to Annual Special editions")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    parent_version = str(parent_manifest.get("source_version") or current.get("source_version") or "")
    annual_refs._next_version(parent_version, source_version)

    parent_lr = parent_manifest.get("layout_revision") or {}
    if parent_lr.get("annual_final_reference_compaction") is not True:
        raise ValueError("final visual compaction requires the prior Annual References compaction")
    if parent_lr.get("references_columns") != 2 or parent_lr.get("references_raggedright") is not True:
        raise ValueError("prior Annual References compaction contract is incomplete")
    if parent_lr.get("bibliography_data_changed") is not False or parent_lr.get("chronology_event_content_changed") is not False:
        raise ValueError("prior Annual References compaction did not preserve bibliography/chronology")

    reader = parent_manifest.get("reader_facing_technical_notes") or {}
    if int(reader.get("generic_fallback_findings") or 0) != 0:
        raise ValueError("final visual compaction requires zero generic Technical Notes fallbacks")
    issue272 = parent_manifest.get("issue_272") or {}
    if issue272.get("q1_q4_narrative_preserved") is not True:
        raise ValueError("final visual compaction requires preserved Q1-Q4 chronology narrative")
    if int(issue272.get("dated_event_count") or 0) != int(issue272.get("cited_event_count") or -1):
        raise ValueError("final visual compaction requires every dated chronology event to remain cited")

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
    manifest["status"] = "VALIDATED_ANNUAL_FINAL_VISUAL_COMPACTION"
    manifest["derivation"] = (
        "Layout-only final visual compaction for Annual Publication Preview issues #122 and #140. "
        "Reader wording, bibliography data, Technical Notes, accepted Article Drafts, Evidence, and "
        "Detailed Chronology remain unchanged; only TOC and References typography are tightened."
    )
    basis = dict(manifest.get("basis") or {})
    basis["previous_source_manifest_path"] = str(current.get("path") or "")
    basis["previous_source_manifest_sha256"] = str(current.get("sha256") or "")
    manifest["basis"] = basis

    references_rel = str((manifest.get("references") or {}).get("path") or "references.bib")
    references_path = output_dir / references_rel
    references_sha = visual.sha(references_path)
    expected_refs_sha = str((parent_manifest.get("references") or {}).get("sha256") or "")
    if not expected_refs_sha or references_sha != expected_refs_sha:
        raise ValueError("bibliography bytes differ from parent manifest before visual compaction")

    front_rel = str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    front_path = output_dir / front_rel
    front_before = visual.sha(front_path)
    front_text = front_path.read_text(encoding="utf-8")
    front_text = _replace_exact(front_text, TOC_OLD, TOC_NEW, "footnotesize section-level TOC")
    front_path.write_text(front_text, encoding="utf-8")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    main_before = visual.sha(main_path)
    main_text = main_path.read_text(encoding="utf-8")
    if main_text.count("% annual References two-column final compaction") != 1:
        raise ValueError("expected exactly one prior Annual References compaction marker")
    main_text = _replace_exact(main_text, REF_FONT_OLD, REF_FONT_NEW, "scriptsize References font")
    main_text = _replace_exact(main_text, REF_START_OLD, REF_START_NEW, "References start spacing")
    main_path.write_text(main_text, encoding="utf-8")

    # Hard preservation checks after the two allowed presentation edits.
    if visual.sha(references_path) != references_sha:
        raise ValueError("final visual compaction changed bibliography data")
    if visual.sha(chronology_path) != chronology_sha:
        raise ValueError("final visual compaction changed chronology data")
    for article in manifest.get("articles") or []:
        section = output_dir / str(article["article_section_path"])
        if visual.sha(section) != article["article_section_sha256"]:
            raise ValueError(f"accepted article changed: {article['package_id']}")
        notes_rel = str(article.get("technical_notes_path") or "")
        if notes_rel:
            notes = output_dir / notes_rel
            if visual.sha(notes) != article["technical_notes_sha256"]:
                raise ValueError(f"Technical Notes changed: {article['package_id']}")

    manifest["frontmatter"] = dict(manifest.get("frontmatter") or {})
    manifest["frontmatter"]["path"] = front_rel
    manifest["frontmatter"]["sha256"] = visual.sha(front_path)
    manifest["main_tex"] = dict(manifest.get("main_tex") or {})
    manifest["main_tex"]["path"] = main_rel
    manifest["main_tex"]["sha256"] = visual.sha(main_path)
    layout = dict(manifest.get("layout") or {})
    layout["toc_depth"] = "section"
    layout["toc_render_size"] = "scriptsize"
    layout["references_start_policy"] = "Needspace(0.20 textheight), no forced clearpage"
    manifest["layout"] = layout

    lr = dict(manifest.get("layout_revision") or {})
    lr.update({
        "from_source_version": parent_version,
        "annual_final_reference_compaction": True,
        "annual_final_visual_compaction": True,
        "annual_final_visual_compaction_issue_refs": [122, 140],
        "reader_semantic_content_changed": False,
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "accepted_article_sections_changed": False,
        "evidence_cards_changed": False,
        "technical_notes_changed_by_reference_compaction": False,
        "chronology_event_content_changed": False,
        "bibliography_data_changed": False,
        "toc_render_size_before": "footnotesize",
        "toc_render_size": "scriptsize",
        "frontmatter_sha256_before": front_before,
        "frontmatter_sha256_after": visual.sha(front_path),
        "main_tex_sha256_before": main_before,
        "main_tex_sha256_after": visual.sha(main_path),
        "bibliography_sha256_before": references_sha,
        "bibliography_sha256_after": visual.sha(references_path),
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
        "references_columns": 2,
        "references_heading_full_width": True,
        "references_heading_toc_navigation": True,
        "references_entry_font": "7pt/8pt",
        "references_bibitemsep": "0pt",
        "references_raggedright": True,
        "references_start_needspace_textheight": 0.20,
    })
    manifest["layout_revision"] = lr
    visual.write_json(manifest_path, manifest)
    manifest_sha = visual.sha(manifest_path)

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"annual-final-visual-compaction-{source_version}.json"
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
        "issue_refs": [122, 140],
        "reason": "Render-first review found one isolated TOC entry and a low-density final References page after the first Annual compaction.",
        "layout_changes": {
            "toc_render_size": "scriptsize",
            "references_columns": 2,
            "references_entry_font": "7pt/8pt",
            "references_bibitemsep": "0pt",
            "references_raggedright": True,
            "references_start_needspace_textheight": 0.20,
        },
        "constraints": {
            "reader_semantic_content_changed": False,
            "new_external_evidence_allowed": False,
            "accepted_article_claims_changed": False,
            "technical_notes_content_changed": False,
            "chronology_event_content_changed": False,
            "bibliography_data_changed": False,
        },
        "bibliography_sha256": references_sha,
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
        "layout_mode": "annual-final-visual-compaction",
    })
    state.setdefault("provenance", {})["validated_issue_source"] = next_source
    state["provenance"]["annual_final_visual_compaction"] = {
        "source_version": source_version,
        "path": marker_path.relative_to(repo_root).as_posix(),
        "sha256": visual.sha(marker_path),
        "bibliography_sha256": references_sha,
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
        "reader_semantic_content_changed": False,
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
        "toc_render_size": "scriptsize",
        "references_columns": 2,
        "references_entry_font": "7pt/8pt",
        "bibliography_sha256": references_sha,
        "chronology_sha256": chronology_sha,
        "chronology_event_count": chronology_event_count,
        "reader_semantic_content_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
        "visual_review_gate": state["gates"]["visual_review"],
        "freeze_gate": state["gates"]["freeze"],
    }


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
