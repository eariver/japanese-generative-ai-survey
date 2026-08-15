#!/usr/bin/env python3
"""Make Half-year V3 repairs re-entrant when the parent already removed common limitations.

The original v3 repair was intentionally a one-shot migration and asserts that at least one
repeated generic limitation is removed. Later immutable revisions can legitimately start from a
parent where that migration has already completed, while still needing fresh source-specific
Technical Note regeneration (for example a stronger entity-binding contract).

This compatibility layer keeps the old assertion fail-closed and permits a re-entrant bridge only
when the marker explicitly opts in and the state-pinned, actually rendered Technical Notes prove
that the old limitation is already absent and the consolidated COMMON_BOUNDARY is present.
The legacy one-shot counter is bridged only in memory; after a successful build the persisted
manifest/state/result are corrected to the truthful removal count (zero) and record that the
limitation was already absent before this revision.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v3 as legacy
from scripts import revise_special_half_year_review_repairs_v28 as base


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _validate_parent_common_limitation_already_absent(
    repo_root: Path, issue_id: str
) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load_json(state_path)
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_rel = str(source.get("path") or "")
    manifest_path = repo_root / manifest_rel
    if not manifest_rel or not manifest_path.is_file():
        raise ValueError("state-pinned validated source manifest missing for re-entrant Half-year repair")
    expected_sha = str(source.get("sha256") or "")
    if expected_sha and _sha(manifest_path) != expected_sha:
        raise ValueError("state-pinned validated source manifest digest mismatch for re-entrant Half-year repair")
    manifest = _load_json(manifest_path)
    source_dir = manifest_path.parent

    rendered_paths = base._rendered_technical_note_paths(repo_root, {"issue_id": issue_id})
    if not rendered_paths:
        raise ValueError("re-entrant Half-year repair found no state-pinned rendered Technical Notes")

    checked = 0
    for rel in sorted(rendered_paths):
        path = source_dir / rel
        if not path.is_file():
            raise ValueError(f"state-pinned rendered Technical Notes file missing: {rel}")
        text = path.read_text(encoding="utf-8")
        if legacy.GENERIC_LIMITATION in text:
            raise ValueError(
                "re-entrant Half-year repair cannot bypass limitation removal: "
                f"legacy repeated limitation still present in {rel}"
            )
        if legacy.COMMON_BOUNDARY not in text:
            raise ValueError(
                "re-entrant Half-year repair cannot prove prior boundary consolidation: "
                f"COMMON_BOUNDARY missing in {rel}"
            )
        checked += 1

    return {
        "parent_source_version": str(manifest.get("source_version") or source.get("source_version") or ""),
        "parent_source_manifest_path": manifest_rel,
        "parent_source_manifest_sha256": _sha(manifest_path),
        "rendered_note_file_count": checked,
        "generic_limitation_present_count": 0,
        "common_boundary_present_count": checked,
    }


def _correct_persisted_reentrant_audit(
    repo_root: Path,
    issue_id: str,
    result: dict[str, Any],
    proof: dict[str, Any],
) -> dict[str, Any]:
    manifest_rel = str(result.get("source_manifest") or "")
    manifest_path = repo_root / manifest_rel
    if not manifest_rel or not manifest_path.is_file():
        raise ValueError("successful re-entrant Half-year repair returned no source manifest")
    manifest = _load_json(manifest_path)

    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader["common_limitation_removed_count"] = 0
    reader["common_limitation_already_absent_before_revision"] = True
    reader["common_limitation_reentrant_parent_proof"] = dict(proof)
    manifest["reader_facing_technical_notes"] = reader

    revision = dict(manifest.get("layout_revision") or {})
    revision["technical_notes_common_limitation_removed_count"] = 0
    revision["technical_notes_common_limitation_already_absent_before_revision"] = True
    revision["technical_notes_common_limitation_reentrant_parent_proof"] = dict(proof)
    manifest["layout_revision"] = revision

    _write_json(manifest_path, manifest)
    manifest_sha = _sha(manifest_path)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load_json(state_path)
    current = (state.get("provenance") or {}).get("validated_issue_source") or {}
    if str(current.get("path") or "") != manifest_rel:
        raise ValueError(
            "re-entrant Half-year repair state/source mismatch after successful build: "
            f"state={current.get('path')} result={manifest_rel}"
        )
    current["sha256"] = manifest_sha
    _write_json(state_path, state)

    result = dict(result)
    result["source_manifest_sha256"] = manifest_sha
    result["technical_notes_common_limitation_removed_count"] = 0
    result["technical_notes_common_limitation_already_absent_before_revision"] = True
    result["technical_notes_common_limitation_reentrant_parent_proof"] = dict(proof)
    result["half_year_reentrant_repair_contract"] = "EXPLICIT_PARENT_CLEAN_PROOF_V1"
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = _load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    allow_reentrant = changes.get("allow_reentrant_half_year_repairs") is True
    if not allow_reentrant:
        return base.build(repo_root, special_slug, issue_id, source_version)

    proof = _validate_parent_common_limitation_already_absent(repo_root, issue_id)

    # v3's historical assertion requires a positive migration count. The parent proof above
    # establishes that the true count for this revision must be zero. Bridge exactly one in-memory
    # count so the one-shot assertion can complete, then rewrite every persisted audit surface to
    # the truthful zero count below. No reader content is changed by the bridge itself.
    original_repair = legacy.repair_note_file
    bridge_used = False

    def reentrant_repair(path: Path, evidence: dict[str, dict[str, Any]]) -> tuple[int, int, int]:
        nonlocal bridge_used
        facts, removed, checked = original_repair(path, evidence)
        if removed != 0:
            raise ValueError(
                "re-entrant Half-year parent proof contradicted during repair: "
                f"unexpected common limitation removal in {path}"
            )
        if not bridge_used:
            bridge_used = True
            return facts, 1, checked
        return facts, 0, checked

    legacy.repair_note_file = reentrant_repair
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        legacy.repair_note_file = original_repair

    if not isinstance(result, dict):
        raise ValueError("re-entrant Half-year repair returned malformed result")
    if not bridge_used:
        raise ValueError("re-entrant Half-year repair did not traverse any rendered Technical Notes file")
    return _correct_persisted_reentrant_audit(repo_root, issue_id, result, proof)


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
