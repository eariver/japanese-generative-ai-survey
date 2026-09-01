#!/usr/bin/env python3
"""Create an immutable layout-only Half-year Publication Preview descendant.

This pass addresses visual density regressions found only after full-page PDF rendering. It changes
no accepted article wording, Evidence cards, Technical Notes wording, Half-year analysis wording,
chronology events, citations, or bibliography data. The permitted transforms are deliberately narrow:

* move the existing table of contents before Retrospective Signals so a long section-level TOC does
  not leave a nearly empty continuation page;
* remove the forced page break between the conclusion and Detailed Chronology so a conclusion-tail
  page can be reused by chronology;
* tighten chronology item spacing without changing any chronology item text/order/citations.

All source files are copied into a new immutable source revision and hash-bound in pipeline state.
"""
from __future__ import annotations

import argparse
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_visual_review_repairs as visual


TOC = r"\tableofcontents"
SIGNALS = r"\section*{Retrospective Signals}"
CHRONOLOGY_SECTION = r"\section{Detailed Chronology}"
CHRONOLOGY_OLD_SPACING = r"\begin{itemize}[leftmargin=1.5em,itemsep=0.45em]"
CHRONOLOGY_NEW_SPACING = r"\begin{itemize}[leftmargin=1.5em,itemsep=0.25em]"


def _validate_marker(marker: dict[str, Any], issue_id: str, source_version: str) -> None:
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("visual-compaction marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_visual_compaction") is not True:
        raise ValueError("marker does not request half_year_visual_compaction")
    constraints = marker.get("constraints") or {}
    required_false = (
        "new_external_evidence_allowed",
        "accepted_article_claims_changed",
        "evidence_cards_mutated",
        "technical_notes_content_changed",
        "half_year_analysis_content_changed",
        "chronology_semantic_content_changed",
        "bibliography_data_changed",
    )
    for key in required_false:
        if constraints.get(key) is not False:
            raise ValueError(f"visual compaction requires {key}=false")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("visual compaction must remain selected-Evidence-only")


def _move_toc_before_signals(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if text.count(TOC) != 1 or text.count(SIGNALS) != 1:
        raise ValueError("frontmatter must contain exactly one TOC and one Retrospective Signals heading")
    if text.index(TOC) < text.index(SIGNALS):
        return False

    # In the H1 source the TOC is the final frontmatter command, preceded only by \medskip.
    suffix = "\\medskip\n" + TOC + "\n"
    if not text.endswith(suffix):
        raise ValueError("expected legacy H1 TOC tail shape is absent")
    body = text[: -len(suffix)]
    signals_at = body.index(SIGNALS)
    revised = body[:signals_at] + TOC + "\n\\medskip\n" + body[signals_at:]
    if revised.index(TOC) > revised.index(SIGNALS):
        raise ValueError("TOC reorder failed")
    path.write_text(revised, encoding="utf-8")
    return True


def _remove_conclusion_chronology_clearpage(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if text.count(CHRONOLOGY_SECTION) != 1:
        raise ValueError("expected exactly one Detailed Chronology section")
    chronology_at = text.index(CHRONOLOGY_SECTION)
    prefix = text[:chronology_at]
    expected = "\\end{multicols}\n\n\\clearpage\n"
    if not prefix.endswith(expected):
        raise ValueError("Detailed Chronology is not preceded by the expected conclusion clearpage")
    revised_prefix = prefix[: -len(expected)] + "\\end{multicols}\n\n"
    revised = revised_prefix + text[chronology_at:]
    path.write_text(revised, encoding="utf-8")
    return True


def _tighten_chronology_spacing(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    old_count = text.count(CHRONOLOGY_OLD_SPACING)
    new_count = text.count(CHRONOLOGY_NEW_SPACING)
    if old_count == 0 and new_count == 1:
        return False
    if old_count != 1 or new_count != 0:
        raise ValueError(
            f"chronology spacing marker is ambiguous: old={old_count} new={new_count}"
        )
    revised = text.replace(CHRONOLOGY_OLD_SPACING, CHRONOLOGY_NEW_SPACING, 1)
    # Prove this pass changes only the itemize spacing token in chronology content.
    if revised.replace(CHRONOLOGY_NEW_SPACING, CHRONOLOGY_OLD_SPACING, 1) != text:
        raise ValueError("chronology compaction changed more than item spacing")
    path.write_text(revised, encoding="utf-8")
    return True


def _reset_pdf_gate(state: dict[str, Any]) -> None:
    gates = state.get("gates") or {}
    lifecycle = str(state.get("lifecycle_state") or "")
    if lifecycle == "RELEASE_CANDIDATE":
        old_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
        if not old_build:
            raise ValueError("RELEASE_CANDIDATE has no prior latex_build provenance")
        state.setdefault("provenance_history", {}).setdefault("latex_build", []).append(old_build)
        (state.get("provenance") or {}).pop("latex_build", None)
    elif lifecycle != "VALIDATED_DRAFT":
        raise ValueError(f"visual compaction requires RELEASE_CANDIDATE or VALIDATED_DRAFT, got {lifecycle}")
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
        raise ValueError("visual compaction requires passed claim/chronology validation")
    if state.get("gates", {}).get("visual_review") != "pending" or state.get("gates", {}).get("freeze") != "pending":
        raise ValueError("visual compaction cannot run after Visual Review or Freeze")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    if parent_manifest.get("source_version") == source_version:
        raise ValueError("visual compaction must create a new immutable source version")
    parent_lr = parent_manifest.get("layout_revision") or {}
    if parent_lr.get("half_year_review_repairs_v3") is not True:
        raise ValueError("visual compaction requires the validated Half-year review-repair lineage")
    if (parent_manifest.get("reader_facing_technical_notes") or {}).get("generic_fallback_findings") != 0:
        raise ValueError("visual compaction parent must have zero generic Technical Notes fallbacks")

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

    chronology = next(
        (a for a in (manifest.get("articles") or []) if isinstance(a, dict) and a.get("package_id") == "chronology"),
        None,
    )
    if chronology is None or chronology.get("_sparse_architecture_derived") is not True or chronology.get("derived_reader_layer") is not True:
        raise ValueError("declared derived chronology reader layer missing")
    chronology_rel = str(chronology.get("layout_body_path") or "")
    chronology_path = output_dir / chronology_rel
    if not chronology_rel or not chronology_path.is_file():
        raise ValueError("chronology layout body missing")

    toc_moved = _move_toc_before_signals(front_path)
    conclusion_break_removed = _remove_conclusion_chronology_clearpage(main_path)
    chronology_spacing_tightened = _tighten_chronology_spacing(chronology_path)

    manifest["frontmatter"] = {"path": front_rel, "sha256": visual.sha(front_path)}
    manifest["main_tex"] = {"path": main_rel, "sha256": visual.sha(main_path)}
    chronology["layout_body_sha256"] = visual.sha(chronology_path)

    # layout_revision is cumulative lineage metadata. Keep the parent's semantic
    # reader_content_changed=true from the v0.3 Half-year repair, and record the
    # current descendant's semantic delta separately as false.
    lr = dict(manifest.get("layout_revision") or {})
    lr.update(
        {
            "from_source_version": parent_manifest.get("source_version"),
            "half_year_visual_compaction": True,
            "visual_issue_refs": [122, 55, 153],
            "visual_compaction_reader_semantic_content_changed": False,
            "new_external_evidence": False,
            "selected_evidence_only": True,
            "accepted_article_sections_changed": False,
            "evidence_cards_changed": False,
            "technical_notes_changed_by_visual_compaction": False,
            "half_year_analysis_changed_by_visual_compaction": False,
            "chronology_semantic_content_changed": False,
            "bibliography_data_changed": False,
            "toc_before_retrospective_signals": True,
            "toc_moved": toc_moved,
            "conclusion_chronology_forced_clearpage": False,
            "conclusion_clearpage_removed": conclusion_break_removed,
            "chronology_itemsep": "0.25em",
            "chronology_spacing_tightened": chronology_spacing_tightened,
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
    state["provenance"]["visual_compaction_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": visual.sha(marker_path),
        "toc_before_retrospective_signals": True,
        "conclusion_chronology_forced_clearpage": False,
        "chronology_itemsep": "0.25em",
        "reader_content_changed": False,
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
        "toc_before_retrospective_signals": True,
        "conclusion_chronology_forced_clearpage": False,
        "chronology_itemsep": "0.25em",
        "reader_content_changed": False,
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
