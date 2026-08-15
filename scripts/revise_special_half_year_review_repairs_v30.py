#!/usr/bin/env python3
"""Preserve Half-year incremental enrichment across proven layout-only descendants.

V8 chooses between a destructive first-time structural migration and incremental Technical Notes
enrichment from the parent manifest status. A later layout-only revision can legitimately replace
that status while preserving the already-repaired reader/source structure. In that case, routing
back through the first-time migration is wrong and can re-trigger one-shot assertions.

This layer recognizes such descendants only when the state-pinned current manifest is explicitly
layout-only, its parent manifest digest is still available and hash-matched, and that parent has a
status V8 already accepts as structurally repaired. The current status is then admitted to V8's
incremental set only for the duration of this build. Other sources remain on the existing V29
fail-closed path.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v8 as incremental
from scripts import revise_special_half_year_review_repairs_v29 as base

_LAYOUT_ONLY_DESCENDANT_STATUSES = {
    "VALIDATED_DENSE_THEME_TABLE_LAYOUT_REVISION",
}


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _prove_incremental_layout_descendant(repo_root: Path, issue_id: str) -> dict[str, Any] | None:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load_json(state_path)
    current = (state.get("provenance") or {}).get("validated_issue_source") or {}
    current_rel = str(current.get("path") or "")
    current_path = repo_root / current_rel
    if not current_rel or not current_path.is_file():
        raise ValueError("state-pinned source manifest missing while resolving Half-year incremental ancestry")
    expected_current_sha = str(current.get("sha256") or "")
    if expected_current_sha and _sha(current_path) != expected_current_sha:
        raise ValueError("state-pinned source manifest digest mismatch while resolving Half-year incremental ancestry")

    manifest = _load_json(current_path)
    status = str(manifest.get("status") or "")
    if status in incremental._ALREADY_STRUCTURALLY_REPAIRED:
        return None
    if status not in _LAYOUT_ONLY_DESCENDANT_STATUSES:
        return None

    revision = manifest.get("layout_revision") or {}
    if revision.get("reader_content_changed") is not False:
        raise ValueError(f"layout-only descendant changed reader content: status={status}")
    if revision.get("technical_notes_content_changed") is not False:
        raise ValueError(f"layout-only descendant changed Technical Notes content: status={status}")
    if revision.get("new_external_evidence") is not False:
        raise ValueError(f"layout-only descendant introduced external Evidence: status={status}")

    reader = manifest.get("reader_facing_technical_notes") or {}
    if reader.get("source_specific_detail_contract") != "SCREENING_BACKED_FAIL_CLOSED":
        raise ValueError(
            "layout-only descendant lacks prior source-specific Technical Notes contract: "
            f"status={status}"
        )
    half_year_analysis = manifest.get("half_year_analysis") or {}
    if not str(half_year_analysis.get("path") or "") or half_year_analysis.get("selected_evidence_only") is not True:
        raise ValueError(f"layout-only descendant lacks preserved Half-year analysis proof: status={status}")

    basis = manifest.get("basis") or {}
    parent_rel = str(basis.get("previous_source_manifest_path") or "")
    parent_expected_sha = str(basis.get("previous_source_manifest_sha256") or "")
    parent_path = repo_root / parent_rel
    if not parent_rel or not parent_expected_sha or not parent_path.is_file():
        raise ValueError(f"layout-only descendant lacks hash-pinned parent manifest: status={status}")
    parent_actual_sha = _sha(parent_path)
    if parent_actual_sha != parent_expected_sha:
        raise ValueError(
            "layout-only descendant parent manifest digest mismatch: "
            f"actual={parent_actual_sha} expected={parent_expected_sha}"
        )
    parent = _load_json(parent_path)
    parent_status = str(parent.get("status") or "")
    if parent_status not in incremental._ALREADY_STRUCTURALLY_REPAIRED:
        raise ValueError(
            "layout-only descendant parent is not a recognized structurally repaired Half-year source: "
            f"status={status} parent_status={parent_status}"
        )

    return {
        "contract": "HASH_PINNED_LAYOUT_ONLY_DESCENDANT_TO_INCREMENTAL_V1",
        "current_status": status,
        "current_source_manifest_path": current_rel,
        "current_source_manifest_sha256": _sha(current_path),
        "parent_status": parent_status,
        "parent_source_manifest_path": parent_rel,
        "parent_source_manifest_sha256": parent_actual_sha,
        "source_specific_detail_contract": reader.get("source_specific_detail_contract"),
        "half_year_analysis_path": half_year_analysis.get("path"),
    }


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    proof = _prove_incremental_layout_descendant(repo_root, issue_id)
    if proof is None:
        return base.build(repo_root, special_slug, issue_id, source_version)

    status = str(proof["current_status"])
    already_present = status in incremental._ALREADY_STRUCTURALLY_REPAIRED
    incremental._ALREADY_STRUCTURALLY_REPAIRED.add(status)
    try:
        # Bypass V29's one-shot migration bridge. The hash-pinned ancestry proof above establishes
        # that this source belongs on V8's ordinary incremental path, not on a re-entrant full
        # structural migration path.
        result = base.base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        if not already_present:
            incremental._ALREADY_STRUCTURALLY_REPAIRED.discard(status)

    if not isinstance(result, dict):
        raise ValueError("incremental layout-descendant Half-year repair returned malformed result")
    result = dict(result)
    result["incremental_parent_recognition_contract"] = proof["contract"]
    result["incremental_parent_recognition_proof"] = proof
    return result


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
