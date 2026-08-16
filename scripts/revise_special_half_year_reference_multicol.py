#!/usr/bin/env python3
"""Create an immutable layout-only Half-year References multicol descendant.

This pass is reserved for a fully reviewed Half-year Special whose final bibliography page remains
low-density after boilerplate removal and typography compaction. It changes no bibliography data,
reader claims, Evidence cards, accepted Article Drafts, Technical Notes, Half-year analysis, or
Detailed Chronology. It keeps the References heading full-width and renders only bibliography entries
in two balanced columns.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_visual_review_repairs as visual

BIB_BLOCK_RE = re.compile(
    r"% half-year final bibliography compaction\n"
    r"\\begingroup\n"
    r"\\scriptsize\n"
    r"\\setlength\{\\bibitemsep\}\{0pt\}\n"
    r"\\printbibliography\[title=\{References / Source Notes\}\]\n"
    r"\\endgroup"
)
BIB_ENTRY_RE = re.compile(r"^@\w+\{", re.MULTILINE)


def _validate_marker(marker: dict[str, Any], issue_id: str, source_version: str) -> None:
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("reference-multicol marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_reference_multicol_compaction") is not True:
        raise ValueError("marker does not request half_year_reference_multicol_compaction")
    constraints = marker.get("constraints") or {}
    for key in (
        "new_external_evidence_allowed",
        "accepted_article_claims_changed",
        "evidence_cards_mutated",
        "technical_notes_content_changed",
        "half_year_analysis_content_changed",
        "chronology_event_content_changed",
        "bibliography_data_changed",
    ):
        if constraints.get(key) is not False:
            raise ValueError(f"reference multicol compaction requires {key}=false")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("reference multicol compaction must remain selected-Evidence-only")


def _rewrite_reference_layout(main_path: Path) -> bool:
    text = main_path.read_text(encoding="utf-8")
    if "% half-year References two-column compaction" in text:
        return False
    match = BIB_BLOCK_RE.search(text)
    if match is None:
        raise ValueError("expected v0.7 compact bibliography block not found")
    replacement = (
        "% half-year References two-column compaction\n"
        "\\section*{References / Source Notes}\n"
        "\\addcontentsline{toc}{section}{References / Source Notes}\n"
        "\\begingroup\n"
        "\\scriptsize\n"
        "\\setlength{\\bibitemsep}{0pt}\n"
        "\\begin{multicols}{2}\n"
        "\\printbibliography[heading=none]\n"
        "\\end{multicols}\n"
        "\\endgroup"
    )
    revised = text[:match.start()] + replacement + text[match.end():]
    if revised.count(r"\printbibliography") != 1:
        raise ValueError("References rewrite must retain exactly one printbibliography")
    if revised.count(r"\section*{References / Source Notes}") != 1:
        raise ValueError("References rewrite must retain exactly one full-width heading")
    main_path.write_text(revised, encoding="utf-8")
    return True


def _reset_pdf_gate(state: dict[str, Any]) -> None:
    gates = state.get("gates") or {}
    lifecycle = str(state.get("lifecycle_state") or "")
    if lifecycle == "RELEASE_CANDIDATE":
        old_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
        if not old_build:
            raise ValueError("RELEASE_CANDIDATE has no prior latex_build provenance")
        state.setdefault("provenance_history", {}).setdefault("latex_build", []).append(old_build)
        state.setdefault("provenance", {}).pop("latex_build", None)
    elif lifecycle != "VALIDATED_DRAFT":
        raise ValueError(f"reference multicol compaction requires RELEASE_CANDIDATE or VALIDATED_DRAFT, got {lifecycle}")
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    gates["latex_build"] = "pending"
    gates["visual_review"] = "pending"
    gates["freeze"] = "pending"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = visual.load_json(marker_path)
    _validate_marker(marker, issue_id, source_version)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    if state.get("gates", {}).get("claim_and_chronology_validation") != "passed":
        raise ValueError("reference multicol compaction requires passed claim/chronology validation")
    if state.get("gates", {}).get("visual_review") != "pending" or state.get("gates", {}).get("freeze") != "pending":
        raise ValueError("reference multicol compaction cannot run after Visual Review or Freeze")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    if parent_manifest.get("source_version") == source_version:
        raise ValueError("reference multicol compaction must create a new immutable source version")
    parent_lr = parent_manifest.get("layout_revision") or {}
    if parent_lr.get("half_year_reader_quality_cleanup") is not True:
        raise ValueError("reference multicol compaction requires the validated reader-quality-cleanup lineage")
    reader = parent_manifest.get("reader_facing_technical_notes") or {}
    if reader.get("generic_fallback_findings") != 0:
        raise ValueError("reference multicol parent must have zero generic Technical Notes fallbacks")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(parent_manifest_path.parent, output_dir)

    manifest_path = output_dir / "source-manifest.json"
    manifest = visual.load_json(manifest_path)
    manifest["source_version"] = source_version
    basis = dict(manifest.get("basis") or {})
    basis["previous_source_manifest_path"] = str(current.get("path") or "")
    basis["previous_source_manifest_sha256"] = str(current.get("sha256") or "")
    manifest["basis"] = basis

    references_rel = str((manifest.get("references") or {}).get("path") or "references.bib")
    references_path = output_dir / references_rel
    if not references_path.is_file():
        raise ValueError("references.bib missing")
    references_sha_before = visual.sha(references_path)
    references_text = references_path.read_text(encoding="utf-8")
    entry_count = len(BIB_ENTRY_RE.findall(references_text))
    if entry_count < 1:
        raise ValueError("reference multicol compaction found no bibliography entries")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    if not main_path.is_file():
        raise ValueError("main.tex missing")
    layout_changed = _rewrite_reference_layout(main_path)

    if visual.sha(references_path) != references_sha_before:
        raise ValueError("reference multicol compaction changed bibliography data")
    manifest["main_tex"] = {"path": main_rel, "sha256": visual.sha(main_path)}

    lr = dict(manifest.get("layout_revision") or {})
    lr.update(
        {
            "from_source_version": parent_manifest.get("source_version"),
            "half_year_reference_multicol_compaction": True,
            "reference_multicol_issue_refs": [140],
            "reference_multicol_reader_semantic_content_changed": False,
            "new_external_evidence": False,
            "selected_evidence_only": True,
            "accepted_article_sections_changed": False,
            "evidence_cards_changed": False,
            "technical_notes_changed_by_reference_multicol": False,
            "half_year_analysis_changed_by_reference_multicol": False,
            "chronology_event_content_changed": False,
            "bibliography_data_changed": False,
            "bibliography_sha256_before": references_sha_before,
            "bibliography_sha256_after": visual.sha(references_path),
            "bibliography_entry_count": entry_count,
            "references_columns": 2,
            "references_heading_full_width": True,
            "references_heading_toc_navigation": True,
            "references_entry_font": "scriptsize",
            "references_bibitemsep": "0pt",
            "references_layout_changed": layout_changed,
        }
    )
    manifest["layout_revision"] = lr
    visual.write_json(manifest_path, manifest)
    manifest_sha = visual.sha(manifest_path)

    state.setdefault("provenance_history", {}).setdefault("validated_issue_source", []).append(current)
    next_source = deepcopy(current)
    next_source.update(
        {
            "path": manifest_path.relative_to(repo_root).as_posix(),
            "sha256": manifest_sha,
            "source_version": source_version,
        }
    )
    state.setdefault("provenance", {})["validated_issue_source"] = next_source
    state["provenance"]["reference_multicol_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": visual.sha(marker_path),
        "bibliography_entry_count": entry_count,
        "bibliography_sha256": references_sha_before,
        "references_columns": 2,
        "references_heading_full_width": True,
        "reader_semantic_content_changed": False,
    }
    _reset_pdf_gate(state)
    visual.write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": parent_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "bibliography_entry_count": entry_count,
        "bibliography_sha256": references_sha_before,
        "references_columns": 2,
        "references_heading_full_width": True,
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
