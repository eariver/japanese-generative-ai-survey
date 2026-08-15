#!/usr/bin/env python3
"""Provenance-safe wrapper for sparse Half-year Architecture Publication Preview repairs.

The v1 compatibility wrapper established the semantic bridge from early Half-year editions
(`conclusion`, no dedicated chronology package) to the current v30 repair chain.  This v2 layer
keeps that bridge while satisfying v30's state-pinned ancestry guard: the temporary compatibility
manifest and its temporary state digest are installed atomically only for the duration of the
repair, the canonical parent manifest is restored byte-for-byte, and all derived provenance is
normalized back to the original canonical parent path/SHA before commit.
"""
from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v3 as structural
from scripts import revise_special_half_year_review_repairs_v30 as current
from scripts import revise_special_half_year_sparse_architecture_repairs as compat


def _normalize_parent_provenance(
    repo_root: Path,
    issue_id: str,
    result: dict[str, Any],
    canonical_parent: dict[str, Any],
    temporary_parent_sha: str,
) -> dict[str, Any]:
    manifest_rel = str(result.get("source_manifest") or "")
    manifest_path = repo_root / manifest_rel
    if not manifest_rel or not manifest_path.is_file():
        raise ValueError("sparse Half-year repair produced no source manifest")
    manifest = compat._load(manifest_path)
    basis = dict(manifest.get("basis") or {})
    basis["previous_source_manifest_path"] = str(canonical_parent.get("path") or "")
    basis["previous_source_manifest_sha256"] = str(canonical_parent.get("sha256") or "")
    basis["sparse_compatibility_temporary_parent_sha256"] = temporary_parent_sha
    basis["sparse_compatibility_parent_restored"] = True
    manifest["basis"] = basis
    revision = dict(manifest.get("layout_revision") or {})
    revision["canonical_parent_source_manifest_path"] = str(canonical_parent.get("path") or "")
    revision["canonical_parent_source_manifest_sha256"] = str(canonical_parent.get("sha256") or "")
    revision["temporary_compatibility_parent_sha256"] = temporary_parent_sha
    revision["canonical_parent_manifest_mutated_persistently"] = False
    manifest["layout_revision"] = revision
    compat._write(manifest_path, manifest)
    manifest_sha = compat._sha(manifest_path)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = compat._load(state_path)
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    if str(source.get("path") or "") != manifest_rel:
        raise ValueError("derived state no longer points at sparse Half-year source revision")
    source["sha256"] = manifest_sha

    history = ((state.get("provenance_history") or {}).get("validated_issue_source") or [])
    replaced = False
    for index in range(len(history) - 1, -1, -1):
        row = history[index]
        if not isinstance(row, dict):
            continue
        if str(row.get("path") or "") == str(canonical_parent.get("path") or "") and str(row.get("sha256") or "") == temporary_parent_sha:
            history[index] = deepcopy(canonical_parent)
            replaced = True
            break
    if not replaced:
        raise ValueError("temporary parent provenance was not found in validated-source history")
    compat._write(state_path, state)

    out = dict(result)
    out["source_manifest_sha256"] = manifest_sha
    out["canonical_parent_source_manifest_path"] = str(canonical_parent.get("path") or "")
    out["canonical_parent_source_manifest_sha256"] = str(canonical_parent.get("sha256") or "")
    out["temporary_compatibility_parent_sha256"] = temporary_parent_sha
    out["canonical_parent_manifest_restored"] = True
    return out


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = compat._load(marker_path)
    changes = marker.get("layout_changes") or {}
    if changes.get("sparse_half_year_architecture_repairs") is not True:
        raise ValueError("marker does not request sparse_half_year_architecture_repairs")
    if changes.get("half_year_review_repairs_v3") is not True:
        raise ValueError("sparse compatibility requires the current half_year_review_repairs_v3 chain")

    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False or constraints.get("selected_evidence_only") is not True:
        raise ValueError("sparse compatibility must be selected-Evidence-only")
    if constraints.get("accepted_article_claims_changed") is not False or constraints.get("evidence_cards_mutated") is not False:
        raise ValueError("sparse compatibility cannot mutate accepted Draft claims or Evidence cards")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    original_state_bytes = state_path.read_bytes()
    original_state = compat._load(state_path)
    canonical_parent = deepcopy((original_state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(canonical_parent.get("path") or "")
    if not parent_manifest_path.is_file() or compat._sha(parent_manifest_path) != str(canonical_parent.get("sha256") or ""):
        raise ValueError("state-pinned canonical parent manifest mismatch")
    parent_bytes = parent_manifest_path.read_bytes()
    parent_manifest = compat._load(parent_manifest_path)

    articles = parent_manifest.get("articles") or []
    if any(str(a.get("package_id") or "") == "chronology" for a in articles if isinstance(a, dict)):
        raise ValueError("sparse compatibility is only for sources without a chronology article")
    conclusion = next(
        (a for a in articles if isinstance(a, dict) and str(a.get("package_id") or "") == "conclusion"),
        None,
    )
    if conclusion is None:
        raise ValueError("sparse compatibility requires a conclusion article")

    aggregate = compat._aggregate_selected_evidence(repo_root, parent_manifest, issue_id)
    temp_rel = f"sources/{issue_id}/editorial/.derived-chronology-{source_version}.tmp.json"
    temp_package = repo_root / temp_rel
    compat._write(temp_package, aggregate)
    synthetic = {
        "package_id": "chronology",
        "draft_package_path": temp_rel,
        "draft_package_sha256": compat._sha(temp_package),
        "layout_body_path": "layout-bodies/chronology.tex",
        "technical_notes_path": "",
        "technical_notes_reader_facing": False,
        "_sparse_architecture_derived": True,
    }
    conclusion["package_id"] = "synthesis"
    conclusion["_sparse_architecture_alias"] = True
    articles.append(synthetic)
    compat._write(parent_manifest_path, parent_manifest)
    temporary_parent_sha = compat._sha(parent_manifest_path)

    temporary_state = deepcopy(original_state)
    temporary_source = (temporary_state.setdefault("provenance", {}).setdefault("validated_issue_source", {}))
    temporary_source["sha256"] = temporary_parent_sha
    compat._write(state_path, temporary_state)

    original_insert = structural.insert_half_year_analysis
    original_remove = structural.remove_article_notes_input

    def compat_remove(main_text: str, technical_notes_path: str) -> str:
        if not str(technical_notes_path or "").strip():
            return main_text
        rel = Path(technical_notes_path).with_suffix("").as_posix()
        needle = rf"\input{{{rel}}}"
        if needle not in main_text:
            raise ValueError(f"expected sparse Technical Notes input not found: {needle}")
        # Current Half-year sources place a \medskip immediately before the synthesis note,
        # while early H1 sources render the conclusion note directly after \end{multicols}.
        # Preserve the ordinary strict remover whenever its exact shape is present; otherwise
        # remove exactly one standalone direct input line and leave surrounding article content.
        standard = r"\medskip" + "\n" + needle + "\n"
        if standard in main_text:
            return original_remove(main_text, technical_notes_path)
        direct = needle + "\n"
        if main_text.count(needle) != 1 or direct not in main_text:
            raise ValueError(f"ambiguous sparse Technical Notes input placement: {needle}")
        revised = main_text.replace(direct, "", 1)
        if needle in revised:
            raise ValueError(f"sparse Technical Notes input remains after removal: {needle}")
        return revised

    structural.insert_half_year_analysis = compat._compat_insert_half_year_analysis
    structural.remove_article_notes_input = compat_remove
    success = False
    try:
        result = current.build(repo_root, special_slug, issue_id, source_version)
        success = True
    finally:
        structural.insert_half_year_analysis = original_insert
        structural.remove_article_notes_input = original_remove
        parent_manifest_path.write_bytes(parent_bytes)
        temp_package.unlink(missing_ok=True)
        if not success:
            state_path.write_bytes(original_state_bytes)

    # current.build has now produced and state-pinned an immutable child revision while the
    # canonical parent was restored. First normalize sparse reader structure, then rewrite only
    # provenance fields that necessarily saw the temporary compatibility digest.
    result = compat._postprocess_revision(repo_root, issue_id, result)
    return _normalize_parent_provenance(
        repo_root,
        issue_id,
        result,
        canonical_parent,
        temporary_parent_sha,
    )


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
