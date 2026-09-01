#!/usr/bin/env python3
"""Create an immutable layout-only Half-year pagination compaction descendant.

This pass is intentionally narrow. It changes no accepted Article Draft wording, Evidence cards,
Technical Notes wording, Half-year analysis wording, chronology events/order/citations, or
bibliography data. It only reduces frontmatter vertical overhead and renders bibliography entries
at footnote size so low-density continuation pages do not survive into Publication Preview.
"""
from __future__ import annotations

import argparse
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_visual_review_repairs as visual

SIGNALS_HEADING = r"\section*{Retrospective Signals}"
SCOPE_BEGIN = r"\begin{claimboundary}[Retrospective scope]"
SCOPE_END = r"\end{claimboundary}"
PRINT_BIB = r"\printbibliography[title={References / Source Notes}]"


def _validate_marker(marker: dict[str, Any], issue_id: str, source_version: str) -> None:
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("pagination-compaction marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_final_pagination_compaction") is not True:
        raise ValueError("marker does not request half_year_final_pagination_compaction")
    constraints = marker.get("constraints") or {}
    for key in (
        "new_external_evidence_allowed",
        "accepted_article_claims_changed",
        "evidence_cards_mutated",
        "technical_notes_content_changed",
        "half_year_analysis_content_changed",
        "chronology_semantic_content_changed",
        "bibliography_data_changed",
    ):
        if constraints.get(key) is not False:
            raise ValueError(f"pagination compaction requires {key}=false")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("pagination compaction must remain selected-Evidence-only")


def _compact_frontmatter(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if text.count(SIGNALS_HEADING) != 1 or text.count(SCOPE_BEGIN) != 1 or text.count(SCOPE_END) != 1:
        raise ValueError("frontmatter signals/scope anchors are ambiguous")
    if "% half-year final frontmatter compaction" in text:
        return False

    signals_at = text.index(SIGNALS_HEADING)
    scope_at = text.index(SCOPE_BEGIN)
    scope_end = text.index(SCOPE_END, scope_at) + len(SCOPE_END)
    if not signals_at < scope_at < scope_end:
        raise ValueError("unexpected signals/scope order")

    prefix = text[:signals_at]
    middle = text[signals_at:scope_end]
    suffix = text[scope_end:]
    heading_end = middle.index("\n", middle.index(SIGNALS_HEADING)) + 1
    heading = middle[:heading_end]
    body = middle[heading_end:]

    # Keep heading/TOC identity and every prose byte. Only reduce font size and vertical glue.
    body = body.replace(r"\smallskip" + "\n", r"\vspace{0.08em}" + "\n")
    body = body.replace(r"\medskip" + "\n" + SCOPE_BEGIN, SCOPE_BEGIN, 1)
    revised_middle = (
        heading
        + "% half-year final frontmatter compaction\n"
        + "\\begingroup\\small\n"
        + body
        + "\n\\endgroup"
    )
    revised = prefix + revised_middle + suffix
    path.write_text(revised, encoding="utf-8")
    return True


def _compact_references(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if text.count(PRINT_BIB) != 1:
        raise ValueError("expected exactly one References / Source Notes printbibliography")
    marker = "% half-year final bibliography compaction"
    if marker in text:
        return False
    replacement = (
        marker
        + "\n\\begingroup\n"
        + "\\footnotesize\n"
        + "\\setlength{\\bibitemsep}{0pt}\n"
        + PRINT_BIB
        + "\n\\endgroup"
    )
    path.write_text(text.replace(PRINT_BIB, replacement, 1), encoding="utf-8")
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
        raise ValueError(f"pagination compaction requires RELEASE_CANDIDATE or VALIDATED_DRAFT, got {lifecycle}")
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
        raise ValueError("pagination compaction requires passed claim/chronology validation")
    if state.get("gates", {}).get("visual_review") != "pending" or state.get("gates", {}).get("freeze") != "pending":
        raise ValueError("pagination compaction cannot run after Visual Review or Freeze")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    if parent_manifest.get("source_version") == source_version:
        raise ValueError("pagination compaction must create a new immutable source version")
    parent_lr = parent_manifest.get("layout_revision") or {}
    if parent_lr.get("half_year_visual_compaction") is not True:
        raise ValueError("pagination compaction requires the validated v0.5 visual-compaction lineage")
    if (parent_manifest.get("reader_facing_technical_notes") or {}).get("generic_fallback_findings") != 0:
        raise ValueError("pagination compaction parent must have zero generic Technical Notes fallbacks")

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

    front_rel = str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    front_path = output_dir / front_rel
    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    if not front_path.is_file() or not main_path.is_file():
        raise ValueError("frontmatter/main source missing")

    front_changed = _compact_frontmatter(front_path)
    refs_changed = _compact_references(main_path)

    manifest["frontmatter"] = {"path": front_rel, "sha256": visual.sha(front_path)}
    manifest["main_tex"] = {"path": main_rel, "sha256": visual.sha(main_path)}
    lr = dict(manifest.get("layout_revision") or {})
    lr.update(
        {
            "from_source_version": parent_manifest.get("source_version"),
            "half_year_final_pagination_compaction": True,
            "visual_issue_refs": [122, 140],
            "visual_pagination_reader_semantic_content_changed": False,
            "new_external_evidence": False,
            "selected_evidence_only": True,
            "accepted_article_sections_changed": False,
            "evidence_cards_changed": False,
            "technical_notes_changed_by_final_pagination_compaction": False,
            "half_year_analysis_changed_by_final_pagination_compaction": False,
            "chronology_semantic_content_changed": False,
            "bibliography_data_changed": False,
            "frontmatter_compacted": front_changed,
            "references_typography_compacted": refs_changed,
            "references_entry_font": "footnotesize",
            "references_bibitemsep": "0pt",
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
    state["provenance"]["final_pagination_compaction_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": visual.sha(marker_path),
        "frontmatter_compacted": True,
        "references_entry_font": "footnotesize",
        "references_bibitemsep": "0pt",
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
        "frontmatter_compacted": True,
        "references_entry_font": "footnotesize",
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
