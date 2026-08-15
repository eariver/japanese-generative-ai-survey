#!/usr/bin/env python3
"""Incrementally enrich already-repaired Half-year Technical Notes.

A Half-year revision that already passed the v3 structural review repair has compact
chronology, explicit half-year analysis, consolidated References, and synthesis note
suppression in place. Re-running the full v3 transform would attempt those destructive
steps twice. This entry point detects that state and creates a new immutable revision by
changing only reader-facing Technical Notes, using the Screening-backed fail-closed detail
contract from v6/v7. Earlier Half-year sources still route through the full scoped v7 build.
"""
from __future__ import annotations

import argparse
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v7 as scoped

impl = scoped.impl
core = impl.core
base = core.base

_ALREADY_STRUCTURALLY_REPAIRED = {
    "VALIDATED_HALF_YEAR_REVIEW_REPAIR_V3_REVISION",
    "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION",
}


def _incremental_build(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
    marker: dict[str, Any],
    state: dict[str, Any],
    current: dict[str, Any],
    current_manifest: dict[str, Any],
) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    changes = marker.get("layout_changes") or {}
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False or constraints.get("selected_evidence_only") is not True:
        raise ValueError("incremental Half-year note enrichment must remain selected-Evidence-only")
    if constraints.get("accepted_article_claims_changed") is not False or constraints.get("evidence_cards_mutated") is not False:
        raise ValueError("incremental Half-year note enrichment must preserve accepted Article Drafts and Evidence cards")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE" or gates.get("latex_build") != "passed":
        raise ValueError("incremental Half-year note enrichment requires built RELEASE_CANDIDATE")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Visual Review and Freeze must remain pending")

    manifest_path = repo_root / str(current.get("path") or "")
    if not manifest_path.is_file() or core.sha(manifest_path) != current.get("sha256"):
        raise ValueError("current validated source digest mismatch")

    out = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if out.exists():
        raise ValueError(f"source revision already exists: {out}")
    shutil.copytree(manifest_path.parent, out)
    manifest = deepcopy(current_manifest)

    impl._ACTIVE_SOURCE_VERSION = source_version
    impl._ACTIVE_OVERRIDES = impl._load_overrides(repo_root, issue_id, source_version)
    try:
        evidence = impl.merge_evidence_index(repo_root, manifest)

        enriched = 0
        url_checks = 0
        changed_files = 0
        visible_cards = 0
        for article in manifest.get("articles") or []:
            if article.get("technical_notes_reader_facing") is not True:
                continue
            rel = str(article.get("technical_notes_path") or "").strip()
            if not rel:
                raise ValueError(f"reader-facing article missing technical_notes_path: {article.get('package_id')}")
            path = out / rel
            before = core.sha(path)
            facts, _limitations, checked = impl.repair_note_file(path, evidence)
            enriched += facts
            url_checks += checked
            visible_cards += len(list(core.NOTE_RE.finditer(path.read_text(encoding="utf-8"))))
            if core.sha(path) != before:
                changed_files += 1
            article["technical_notes_sha256"] = core.sha(path)

        if visible_cards < 1:
            raise ValueError("no reader-facing Technical Notes cards found for incremental enrichment")
        if enriched != visible_cards:
            raise ValueError(
                "not every reader-facing Technical Notes card was enriched: "
                f"enriched={enriched} visible_cards={visible_cards}"
            )
        if changed_files < 1:
            raise ValueError("incremental Half-year note enrichment changed no reader-facing note files")

        manifest["source_version"] = source_version
        manifest["status"] = "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION"
        manifest["derivation"] = (
            "Incremental Publication Preview repair for #139 over an already structurally repaired Half-year source. "
            "Selected Evidence and accepted Article Drafts remain immutable. Each reader-facing Technical Notes card "
            "is enriched with at least one source-specific technical detail joined through the exact accepted, "
            "hash-pinned Screening verification queue; URL/identifier identity and prior v0.6 layout repairs are preserved."
        )
        basis = dict(manifest.get("basis") or {})
        basis["previous_source_manifest_path"] = current["path"]
        basis["previous_source_manifest_sha256"] = current["sha256"]
        manifest["basis"] = basis

        reader = dict(manifest.get("reader_facing_technical_notes") or {})
        reader.update(
            {
                "generic_fallback_policy": "forbidden-fail-closed",
                "generic_fallback_findings": 0,
                "duplicate_bullet_findings": 0,
                "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED",
                "source_specific_detail_enrichment_count": enriched,
                "source_specific_detail_visible_card_count": visible_cards,
                "source_specific_detail_override_count": len(impl._ACTIVE_OVERRIDES),
                "source_specific_detail_url_identity_checks": url_checks,
            }
        )
        manifest["reader_facing_technical_notes"] = reader

        prior_layout_revision = dict(manifest.get("layout_revision") or {})
        prior_layout_revision.update(
            {
                "from_source_version": current_manifest.get("source_version"),
                "half_year_source_specific_notes_v1": True,
                "issue_refs": [int(x) for x in marker.get("review_issues") or []],
                "reader_content_changed": True,
                "reader_content_change_scope": "reader-facing Technical Notes source-specific details only",
                "new_external_evidence": False,
                "accepted_article_sections_changed": False,
                "evidence_cards_changed": False,
                "technical_notes_files_changed": changed_files,
                "technical_notes_source_specific_detail_enrichment_count": enriched,
                "technical_notes_visible_card_count": visible_cards,
                "technical_notes_url_identity_checks": url_checks,
                "technical_notes_detail_override_count": len(impl._ACTIVE_OVERRIDES),
                "prior_half_year_structure_preserved": True,
            }
        )
        manifest["layout_revision"] = prior_layout_revision

        main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
        refs_rel = str((manifest.get("references") or {}).get("path") or "references.bib")
        manifest["main_tex"] = {"path": main_rel, "sha256": core.sha(out / main_rel)}
        manifest["references"] = {"path": refs_rel, "sha256": core.sha(out / refs_rel)}

        new_manifest_path = out / "source-manifest.json"
        base.write_json(new_manifest_path, manifest)
        manifest_sha = core.sha(new_manifest_path)

        history = state.setdefault("provenance_history", {})
        history.setdefault("validated_issue_source", []).append(current)
        previous_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
        if previous_build:
            history.setdefault("latex_build", []).append(previous_build)
        state["lifecycle_state"] = "VALIDATED_DRAFT"
        state["gates"]["latex_build"] = "pending"
        state["gates"]["visual_review"] = "pending"
        state["gates"]["freeze"] = "pending"
        state["provenance"]["validated_issue_source"] = {
            "path": new_manifest_path.relative_to(repo_root).as_posix(),
            "sha256": manifest_sha,
            "source_version": source_version,
            "layout_mode": str((manifest.get("layout") or {}).get("body_mode") or current.get("layout_mode") or "mixed"),
            "layout_revision_sha256": core.sha(marker_path),
        }
        state["provenance"].pop("latex_build", None)
        state["provenance"]["reader_layout_revision"] = {
            "source_version": source_version,
            "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
            "layout_revision_sha256": core.sha(marker_path),
            "reason": str(marker.get("reason") or "Enrich Half-year Technical Notes with source-specific details."),
        }
        base.write_json(state_path, state)

        return {
            "schema_version": "1.0",
            "issue_id": issue_id,
            "special_slug": special_slug,
            "source_version": source_version,
            "previous_source_version": current_manifest.get("source_version"),
            "source_manifest": new_manifest_path.relative_to(repo_root).as_posix(),
            "source_manifest_sha256": manifest_sha,
            "issue_refs": manifest["layout_revision"]["issue_refs"],
            "technical_notes_source_specific_detail_enrichment_count": enriched,
            "technical_notes_visible_card_count": visible_cards,
            "technical_notes_url_identity_checks": url_checks,
            "technical_note_detail_overrides": len(impl._ACTIVE_OVERRIDES),
            "technical_note_detail_contract": "SCREENING_BACKED_FAIL_CLOSED",
            "prior_half_year_structure_preserved": True,
            "new_external_evidence": False,
            "lifecycle_state": state["lifecycle_state"],
            "latex_build_gate": state["gates"]["latex_build"],
            "visual_review_gate": state["gates"]["visual_review"],
            "freeze_gate": state["gates"]["freeze"],
        }
    finally:
        impl._ACTIVE_SOURCE_VERSION = ""
        impl._ACTIVE_OVERRIDES = {}


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    edition = base.load_json(repo_root / "specials" / special_slug / "edition.json")
    if edition.get("special_id") != issue_id or edition.get("edition_kind") != "RETROSPECTIVE_PERIOD":
        raise ValueError("Half-year source-specific notes repair requires RETROSPECTIVE_PERIOD")

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = base.load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_review_repairs_v3") is not True:
        raise ValueError("marker does not request half_year_review_repairs_v3")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = base.load_json(state_path)
    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    manifest_path = repo_root / str(current.get("path") or "")
    if not manifest_path.is_file() or core.sha(manifest_path) != current.get("sha256"):
        raise ValueError("current validated source digest mismatch")
    current_manifest = base.load_json(manifest_path)

    if str(current_manifest.get("status") or "") in _ALREADY_STRUCTURALLY_REPAIRED:
        return _incremental_build(
            repo_root,
            special_slug,
            issue_id,
            source_version,
            marker,
            state,
            current,
            current_manifest,
        )
    return scoped.build(repo_root, special_slug, issue_id, source_version)


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
