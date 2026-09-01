#!/usr/bin/env python3
"""Create an immutable layout-only Annual Special References compaction revision.

This pass is for a reviewed Annual Special whose bibliography leaves a low-density final page.
It changes presentation only: bibliography data, accepted Article Drafts, Technical Notes,
Detailed Chronology, Evidence, Selection, and Architecture remain byte/identity stable.
The References heading stays full-width while entries are rendered in compact two-column,
ragged-right form, matching the established frozen Half-year presentation policy.
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

BIB_ENTRY_RE = re.compile(r"^@\w+\{", re.MULTILINE)
VERSION_RE = re.compile(r"v(\d+)\.(\d+)$")
REFERENCE_BLOCK_RE = re.compile(
    r"(?:\\Needspace\{0\.30\\textheight\}\n\\bigskip\n){1,2}"
    r"(\\noindent\{\\small Referencesには本文・Detailed Chronologyの検証に用いた一次資料の識別情報とURLを掲載する。各entryに共通する用途説明はここに集約する。\}\\par\n"
    r"\\smallskip\n)"
    r"\\printbibliography\[title=\{References / Source Notes\}\]"
)


def _next_version(parent: str, target: str) -> None:
    pm = VERSION_RE.fullmatch(parent)
    tm = VERSION_RE.fullmatch(target)
    if pm is None or tm is None:
        raise ValueError(f"invalid source revision: parent={parent!r} target={target!r}")
    if pm.group(1) != tm.group(1) or int(tm.group(2)) != int(pm.group(2)) + 1:
        raise ValueError(f"Annual reference compaction target must be the next immutable revision: {parent} -> {target}")


def _rewrite_reference_layout(main_path: Path) -> tuple[bool, int]:
    text = main_path.read_text(encoding="utf-8")
    if "% annual References two-column final compaction" in text:
        return False, 0
    match = REFERENCE_BLOCK_RE.search(text)
    if match is None:
        raise ValueError("expected Annual compact References block not found")
    duplicate_needspace_pairs = text[match.start():match.end()].count(r"\Needspace{0.30\textheight}") - 1
    replacement = (
        r"\Needspace{0.30\textheight}" + "\n"
        + r"\bigskip" + "\n"
        + match.group(1)
        + "% annual References two-column final compaction\n"
        + r"\section*{References / Source Notes}" + "\n"
        + r"\addcontentsline{toc}{section}{References / Source Notes}" + "\n"
        + r"\begingroup" + "\n"
        + r"\scriptsize" + "\n"
        + r"\setlength{\bibitemsep}{0pt}" + "\n"
        + r"\begin{multicols}{2}" + "\n"
        + r"\raggedright" + "\n"
        + r"\printbibliography[heading=none]" + "\n"
        + r"\end{multicols}" + "\n"
        + r"\endgroup"
    )
    revised = text[:match.start()] + replacement + text[match.end():]
    if revised.count(r"\printbibliography") != 1:
        raise ValueError("References compaction must retain exactly one printbibliography")
    if revised.count(r"\section*{References / Source Notes}") != 1:
        raise ValueError("References compaction must retain exactly one explicit full-width heading")
    if revised.count("% annual References two-column final compaction") != 1:
        raise ValueError("References compaction marker multiplicity mismatch")
    main_path.write_text(revised, encoding="utf-8")
    return True, max(0, duplicate_needspace_pairs)


def _reset_pdf_gate(state: dict[str, Any]) -> None:
    gates = state.get("gates") or {}
    lifecycle = str(state.get("lifecycle_state") or "")
    if lifecycle != "RELEASE_CANDIDATE":
        raise ValueError(f"Annual final reference compaction requires RELEASE_CANDIDATE, got {lifecycle}")
    if gates.get("latex_build") != "passed":
        raise ValueError("Annual final reference compaction requires a passed PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Annual final reference compaction cannot run after Publication Preview/Freeze authority")
    old_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
    if not old_build:
        raise ValueError("RELEASE_CANDIDATE has no latex_build provenance")
    state.setdefault("provenance_history", {}).setdefault("latex_build", []).append(old_build)
    state.setdefault("provenance", {}).pop("latex_build", None)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    gates["latex_build"] = "pending"
    gates["visual_review"] = "pending"
    gates["freeze"] = "pending"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    gates = state.get("gates") or {}
    if gates.get("claim_and_chronology_validation") != "passed":
        raise ValueError("Annual reference compaction requires passed claim/chronology validation")
    if "publication_preview" in (state.get("provenance") or {}):
        raise ValueError("Annual reference compaction cannot run after Publication Preview approval")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    parent_version = str(parent_manifest.get("source_version") or current.get("source_version") or "")
    _next_version(parent_version, source_version)

    if not special_slug.endswith("-Y") or not issue_id.endswith("-Y"):
        raise ValueError("Annual reference compaction is restricted to Annual Special editions")
    reader = parent_manifest.get("reader_facing_technical_notes") or {}
    if int(reader.get("generic_fallback_findings") or 0) != 0:
        raise ValueError("Annual reference compaction requires zero generic Technical Notes fallbacks")
    issue272 = parent_manifest.get("issue_272") or {}
    if issue272.get("q1_q4_narrative_preserved") is not True:
        raise ValueError("Annual reference compaction requires preserved Q1-Q4 chronology narrative")
    if int(issue272.get("dated_event_count") or 0) != int(issue272.get("cited_event_count") or -1):
        raise ValueError("Annual reference compaction requires all material chronology events cited")

    chronology = deepcopy((state.get("provenance") or {}).get("annual_chronology") or {})
    chronology_path = repo_root / str(chronology.get("path") or "")
    if not chronology_path.is_file() or visual.sha(chronology_path) != str(chronology.get("sha256") or ""):
        raise ValueError("state-pinned Annual chronology missing or SHA mismatch")
    chronology_sha_before = visual.sha(chronology_path)
    chronology_event_count = int(chronology.get("event_count") or -1)

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(parent_manifest_path.parent, output_dir)
    manifest_path = output_dir / "source-manifest.json"
    manifest = visual.load_json(manifest_path)
    manifest["source_version"] = source_version
    manifest["status"] = "VALIDATED_ANNUAL_FINAL_REFERENCE_COMPACTION"
    basis = dict(manifest.get("basis") or {})
    basis["previous_source_manifest_path"] = str(current.get("path") or "")
    basis["previous_source_manifest_sha256"] = str(current.get("sha256") or "")
    manifest["basis"] = basis

    references_rel = str((manifest.get("references") or {}).get("path") or "references.bib")
    references_path = output_dir / references_rel
    if not references_path.is_file():
        raise ValueError("references.bib missing")
    references_sha_before = visual.sha(references_path)
    entry_count = len(BIB_ENTRY_RE.findall(references_path.read_text(encoding="utf-8")))
    if entry_count < 1:
        raise ValueError("Annual reference compaction found no bibliography entries")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    if not main_path.is_file():
        raise ValueError("main.tex missing")
    main_sha_before = visual.sha(main_path)
    changed, duplicate_needspace_pairs_removed = _rewrite_reference_layout(main_path)
    if not changed:
        raise ValueError("Annual reference compaction produced no layout change")
    if visual.sha(references_path) != references_sha_before:
        raise ValueError("Annual reference compaction changed bibliography data")
    if visual.sha(chronology_path) != chronology_sha_before:
        raise ValueError("Annual reference compaction changed chronology data")

    manifest["main_tex"] = {"path": main_rel, "sha256": visual.sha(main_path)}
    lr = dict(manifest.get("layout_revision") or {})
    lr.update({
        "from_source_version": parent_version,
        "annual_final_reference_compaction": True,
        "annual_final_reference_compaction_issue_refs": [140],
        "reader_semantic_content_changed": False,
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "accepted_article_sections_changed": False,
        "evidence_cards_changed": False,
        "technical_notes_changed_by_reference_compaction": False,
        "chronology_event_content_changed": False,
        "bibliography_data_changed": False,
        "main_tex_sha256_before": main_sha_before,
        "main_tex_sha256_after": visual.sha(main_path),
        "bibliography_sha256_before": references_sha_before,
        "bibliography_sha256_after": visual.sha(references_path),
        "bibliography_entry_count": entry_count,
        "chronology_sha256": chronology_sha_before,
        "chronology_event_count": chronology_event_count,
        "references_columns": 2,
        "references_heading_full_width": True,
        "references_heading_toc_navigation": True,
        "references_entry_font": "scriptsize",
        "references_bibitemsep": "0pt",
        "references_raggedright": True,
        "duplicate_reference_needspace_pairs_removed": duplicate_needspace_pairs_removed,
    })
    manifest["layout_revision"] = lr
    visual.write_json(manifest_path, manifest)
    manifest_sha = visual.sha(manifest_path)

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"annual-final-reference-compaction-{source_version}.json"
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
        "reason": "Human-visible final References page remained low-density after Annual Publication Preview repairs; compact bibliography entries using established Special two-column presentation policy.",
        "layout_changes": {
            "references_columns": 2,
            "references_entry_font": "scriptsize",
            "references_bibitemsep": "0pt",
            "references_raggedright": True,
            "references_heading_full_width": True,
            "duplicate_reference_needspace_pairs_removed": duplicate_needspace_pairs_removed,
        },
        "constraints": {
            "new_external_evidence_allowed": False,
            "selected_evidence_only": True,
            "accepted_article_claims_changed": False,
            "evidence_cards_mutated": False,
            "technical_notes_content_changed": False,
            "chronology_event_content_changed": False,
            "bibliography_data_changed": False,
        },
        "bibliography_entry_count": entry_count,
        "bibliography_sha256": references_sha_before,
        "chronology_event_count": chronology_event_count,
        "chronology_sha256": chronology_sha_before,
    }
    visual.write_json(marker_path, marker)

    state.setdefault("provenance_history", {}).setdefault("validated_issue_source", []).append(current)
    next_source = deepcopy(current)
    next_source.update({
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "annual-final-reference-compaction",
    })
    state.setdefault("provenance", {})["validated_issue_source"] = next_source
    state["provenance"]["annual_final_reference_compaction"] = {
        "source_version": source_version,
        "path": marker_path.relative_to(repo_root).as_posix(),
        "sha256": visual.sha(marker_path),
        "bibliography_entry_count": entry_count,
        "bibliography_sha256": references_sha_before,
        "chronology_event_count": chronology_event_count,
        "chronology_sha256": chronology_sha_before,
        "reader_semantic_content_changed": False,
    }
    _reset_pdf_gate(state)
    visual.write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": parent_version,
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "bibliography_entry_count": entry_count,
        "bibliography_sha256": references_sha_before,
        "chronology_event_count": chronology_event_count,
        "chronology_sha256": chronology_sha_before,
        "references_columns": 2,
        "references_entry_font": "scriptsize",
        "references_raggedright": True,
        "duplicate_reference_needspace_pairs_removed": duplicate_needspace_pairs_removed,
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
