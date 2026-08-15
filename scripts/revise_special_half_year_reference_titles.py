#!/usr/bin/env python3
"""Create an immutable Half-year descendant that restores reader-facing bibliography titles.

This pass exists for an already validated Half-year review repair whose References still expose
legacy ``Primary source N`` placeholders. It reuses only selected Draft Package Evidence metadata:
source URLs are matched to ``artifact.canonical_name`` exactly as in the established Special visual-
review repair contract. It also ensures Detailed Chronology sits between the conclusion and the
References intro/bibliography in sparse early Half-year sources.

Accepted article sections, Evidence cards, Technical Notes content, chronology content, and analysis
content are immutable. Any unresolved bibliography placeholder, undeclared article without a Draft
Package, or ambiguous structural placement fails closed.
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


_GENERIC_BIB_TITLE_RE = re.compile(r"\btitle\s*=\s*\{Primary source\s+\d+\b", re.IGNORECASE)
_REFERENCES_PRINT = r"\printbibliography[title={References / Source Notes}]"
_REFERENCES_NOTE_PREFIX = r"\noindent{\small\textit{以下のReferencesは"
_CHRONOLOGY_INPUT = r"\input{layout-bodies/chronology}"


def _normalize_chronology_reference_order(path: Path) -> bool:
    """Put the consolidated References intro after Detailed Chronology and before bibliography."""
    text = path.read_text(encoding="utf-8")
    if text.count(_REFERENCES_PRINT) != 1:
        raise ValueError("expected exactly one References / Source Notes bibliography")
    if text.count(_CHRONOLOGY_INPUT) != 1:
        raise ValueError("expected exactly one Detailed Chronology input")
    if text.count(_REFERENCES_NOTE_PREFIX) != 1:
        raise ValueError("expected exactly one consolidated References intro note")

    chronology_at = text.index(_CHRONOLOGY_INPUT)
    refs_at = text.index(_REFERENCES_PRINT)
    note_at = text.index(_REFERENCES_NOTE_PREFIX)
    if chronology_at > refs_at:
        raise ValueError("Detailed Chronology follows bibliography in sparse Half-year source")
    if chronology_at < note_at < refs_at:
        return False
    if note_at > refs_at:
        raise ValueError("References intro follows bibliography")

    # H1 v0.3 has: conclusion -> clearpage -> References intro -> clearpage -> chronology
    # -> clearpage -> bibliography. Remove only the first clearpage+intro block and place the intro
    # immediately before \printbibliography; the existing clearpage before bibliography is retained.
    intro_clearpage = text.rfind("\\clearpage\n", 0, note_at)
    if intro_clearpage < 0:
        raise ValueError("consolidated References intro has no preceding clearpage")
    note_end_marker = "\\smallskip\n"
    note_end = text.find(note_end_marker, note_at)
    if note_end < 0:
        raise ValueError("consolidated References intro has no smallskip terminator")
    note_end += len(note_end_marker)
    note_block = text[note_at:note_end]
    revised = text[:intro_clearpage] + text[note_end:]
    refs_at = revised.index(_REFERENCES_PRINT)
    revised = revised[:refs_at] + note_block + revised[refs_at:]

    chronology_at = revised.index(_CHRONOLOGY_INPUT)
    note_at = revised.index(_REFERENCES_NOTE_PREFIX)
    refs_at = revised.index(_REFERENCES_PRINT)
    if not chronology_at < note_at < refs_at:
        raise ValueError("failed to establish conclusion -> Detailed Chronology -> References order")
    path.write_text(revised, encoding="utf-8")
    return True


def _validate_marker(marker: dict[str, Any], issue_id: str, source_version: str) -> None:
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("reference-title repair marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_reference_title_repair") is not True:
        raise ValueError("marker does not request half_year_reference_title_repair")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("reference-title repair must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("reference-title repair must remain selected-Evidence-only")
    if constraints.get("accepted_article_claims_changed") is not False:
        raise ValueError("reference-title repair cannot change accepted Article Draft claims")
    if constraints.get("evidence_cards_mutated") is not False:
        raise ValueError("reference-title repair cannot mutate Evidence cards")


def _draft_package_manifest(manifest: dict[str, Any]) -> tuple[dict[str, Any], int, list[str]]:
    """Return a strict title-mapping view containing only real Draft Package articles.

    Sparse Half-year compatibility may append a declared derived chronology article. Such a reader
    layer has no Draft Package by design and contributes no bibliography Evidence. Any *undeclared*
    article lacking a Draft Package remains an error rather than being silently skipped.
    """
    source_articles: list[dict[str, Any]] = []
    skipped: list[str] = []
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            raise ValueError("source manifest articles must be objects")
        package_id = str(article.get("package_id") or "").strip()
        draft_path = str(article.get("draft_package_path") or "").strip()
        if draft_path:
            source_articles.append(article)
            continue
        if article.get("_sparse_architecture_derived") is True and article.get("derived_reader_layer") is True:
            skipped.append(package_id or "<unnamed-derived-layer>")
            continue
        raise ValueError(f"non-derived article lacks Draft Package while restoring bibliography titles: {package_id}")

    if not source_articles:
        raise ValueError("no Draft Package articles available for bibliography title restoration")
    evidence_manifest = deepcopy(manifest)
    evidence_manifest["articles"] = source_articles
    return evidence_manifest, len(source_articles), skipped


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = visual.load_json(marker_path)
    _validate_marker(marker, issue_id, source_version)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("Half-year reference-title descendant requires VALIDATED_DRAFT")
    if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "pending":
        raise ValueError("Half-year reference-title descendant requires validated claims and pending PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Half-year reference-title descendant requires Visual Review and Freeze pending")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or visual.sha(current_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned validated source manifest digest mismatch")
    current_manifest = visual.load_json(current_manifest_path)
    if current_manifest.get("source_version") == source_version:
        raise ValueError("reference-title repair must create a new immutable source version")
    current_lr = current_manifest.get("layout_revision") or {}
    if current_lr.get("half_year_review_repairs_v3") is not True:
        raise ValueError("reference-title repair requires a validated Half-year review-repair parent")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_manifest_path.parent, output_dir)

    manifest_path = output_dir / "source-manifest.json"
    new_manifest = visual.load_json(manifest_path)
    new_manifest["source_version"] = source_version
    # Keep the established Half-year repair status so the shared strict verifier continues to
    # validate all prior #139/#128/#153/#122/#55/#140/#54 invariants on this descendant.
    new_manifest["status"] = "VALIDATED_HALF_YEAR_REVIEW_REPAIR_V3_REVISION"
    basis = dict(new_manifest.get("basis") or {})
    basis["previous_source_manifest_path"] = str(current.get("path") or "")
    basis["previous_source_manifest_sha256"] = str(current.get("sha256") or "")
    new_manifest["basis"] = basis

    refs_rel = str((new_manifest.get("references") or {}).get("path") or "references.bib")
    refs_path = output_dir / refs_rel
    if not refs_path.is_file():
        raise ValueError("references bibliography missing")
    evidence_manifest, draft_article_count, skipped_derived = _draft_package_manifest(new_manifest)
    title_map = visual.source_title_map(repo_root, evidence_manifest)
    titles_changed, entry_count = visual.enrich_bibliography_titles(refs_path, title_map)
    refs_text = refs_path.read_text(encoding="utf-8")
    if _GENERIC_BIB_TITLE_RE.search(refs_text):
        raise ValueError("generic Primary source bibliography title remains after enrichment")
    if titles_changed < 1:
        raise ValueError("reference-title repair changed no bibliography titles")
    new_manifest["references"] = {"path": refs_rel, "sha256": visual.sha(refs_path)}

    main_info = new_manifest.get("main_tex") or {}
    main_rel = str(main_info.get("path") or "main.tex") if isinstance(main_info, dict) else "main.tex"
    main_path = output_dir / main_rel
    if not main_path.is_file():
        raise ValueError("main TeX missing")
    references_intro_moved = _normalize_chronology_reference_order(main_path)
    main_sha = visual.sha(main_path)
    new_manifest["main_tex"] = {"path": main_rel, "sha256": main_sha}

    lr = dict(new_manifest.get("layout_revision") or {})
    lr.update(
        {
            "from_source_version": current_manifest.get("source_version"),
            "half_year_reference_title_repair": True,
            "reference_title_issue_ref": 78,
            "reader_content_changed": True,
            "new_external_evidence": False,
            "selected_evidence_only": True,
            "accepted_article_sections_changed": False,
            "evidence_cards_changed": False,
            "technical_notes_changed_by_reference_title_repair": False,
            "half_year_analysis_changed_by_reference_title_repair": False,
            "chronology_content_changed_by_reference_title_repair": False,
            "bibliography_titles_enriched": titles_changed,
            "bibliography_entry_count": entry_count,
            "bibliography_generic_placeholder_count": 0,
            "bibliography_title_source": "selected Draft Package Evidence artifact.canonical_name keyed by exact source URL",
            "bibliography_traceability_fields_preserved": True,
            "bibliography_draft_package_article_count": draft_article_count,
            "bibliography_derived_reader_layers_skipped": skipped_derived,
            "detailed_chronology_before_references": True,
            "references_intro_moved_after_chronology": references_intro_moved,
        }
    )
    new_manifest["layout_revision"] = lr
    visual.write_json(manifest_path, new_manifest)
    manifest_sha = visual.sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    next_source = deepcopy(current)
    next_source.update(
        {
            "path": manifest_path.relative_to(repo_root).as_posix(),
            "sha256": manifest_sha,
            "source_version": source_version,
        }
    )
    state["provenance"]["validated_issue_source"] = next_source
    state["provenance"]["reference_title_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": visual.sha(marker_path),
        "bibliography_titles_enriched": titles_changed,
        "bibliography_entry_count": entry_count,
        "generic_placeholder_count": 0,
        "draft_package_article_count": draft_article_count,
        "derived_reader_layers_skipped": skipped_derived,
        "detailed_chronology_before_references": True,
        "references_intro_moved_after_chronology": references_intro_moved,
    }
    visual.write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": current_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "bibliography_titles_enriched": titles_changed,
        "bibliography_entry_count": entry_count,
        "bibliography_generic_placeholder_count": 0,
        "bibliography_draft_package_article_count": draft_article_count,
        "bibliography_derived_reader_layers_skipped": skipped_derived,
        "detailed_chronology_before_references": True,
        "references_intro_moved_after_chronology": references_intro_moved,
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
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
