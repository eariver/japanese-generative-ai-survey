#!/usr/bin/env python3
"""Probe Automotive E/E Candidate Selection against the unchanged shared gate.

The persisted experiment output is a PENDING_APPROVAL Selection proposal plus a
separate domain-theme overlay.  A synthetic APPROVED copy is created only inside the
run output so that `build_architecture_input.py` can be exercised without changing the
repository pipeline state or pretending that a human approved the Selection.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).resolve()
REPO_DEFAULT = SCRIPT.parents[2]
if str(REPO_DEFAULT) not in sys.path:
    sys.path.insert(0, str(REPO_DEFAULT))

from scripts import build_architecture_input
from scripts import candidate_selection_gate


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(*, matrix_path: Path, profile_path: Path, edition_path: Path, output_root: Path) -> dict[str, Any]:
    matrix_path = matrix_path.resolve()
    profile_path = profile_path.resolve()
    edition_path = edition_path.resolve()
    output_root = output_root.resolve()
    profile = load_json(profile_path)
    matrix = load_json(matrix_path)
    edition = load_json(edition_path)

    issue_id = profile.get("issue_id")
    if matrix.get("issue_id") != issue_id or edition.get("special_id") != issue_id:
        raise ValueError("Selection profile/matrix/edition identity mismatch")

    candidate_rows = {
        row["evidence_task_id"]: row
        for row in matrix.get("rows", [])
        if row.get("recommendation") == "CANDIDATE"
    }
    configured = profile.get("candidate_assignments")
    if not isinstance(configured, list) or not configured:
        raise ValueError("profile.candidate_assignments must be a non-empty array")
    configured_by_id: dict[str, dict[str, Any]] = {}
    for entry in configured:
        if not isinstance(entry, dict):
            raise ValueError("candidate assignment entries must be objects")
        task_id = entry.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id or task_id in configured_by_id:
            raise ValueError(f"invalid/duplicate candidate assignment id: {task_id!r}")
        configured_by_id[task_id] = entry
    if set(configured_by_id) != set(candidate_rows):
        missing = sorted(set(candidate_rows) - set(configured_by_id))
        extra = sorted(set(configured_by_id) - set(candidate_rows))
        raise ValueError(f"Selection profile must cover every and only CANDIDATE row: missing={missing} extra={extra}")

    themes = profile.get("themes")
    if not isinstance(themes, dict) or not themes:
        raise ValueError("profile.themes must be a non-empty object")
    known_themes = set(themes)

    proposal_path = output_root / "candidate-selection-proposal-v0.1.json"
    proposal = candidate_selection_gate.initialize(matrix_path, proposal_path, profile.get("selection_version", "v0.1"))
    theme_assignments: list[dict[str, Any]] = []
    for assignment in proposal["assignments"]:
        task_id = assignment["evidence_task_id"]
        configured_entry = configured_by_id.get(task_id)
        if configured_entry is None:
            # Non-CANDIDATE rows keep the deterministic HOLD_OUT/EXCLUDE suggestion
            # emitted by the shared initializer.
            continue
        role = configured_entry.get("role")
        rationale = configured_entry.get("rationale")
        assigned_themes = configured_entry.get("themes")
        if role not in candidate_selection_gate.ROLES or role == "UNASSIGNED":
            raise ValueError(f"invalid configured role for {task_id}: {role!r}")
        if not isinstance(rationale, str) or not rationale.strip():
            raise ValueError(f"selection rationale required for {task_id}")
        if not isinstance(assigned_themes, list) or not assigned_themes:
            raise ValueError(f"at least one domain theme required for {task_id}")
        if len(assigned_themes) != len(set(assigned_themes)) or any(value not in known_themes for value in assigned_themes):
            raise ValueError(f"invalid theme assignment for {task_id}: {assigned_themes}")
        assignment["role"] = role
        assignment["rationale"] = rationale.strip()
        theme_assignments.append({
            "evidence_task_id": task_id,
            "title": candidate_rows[task_id]["title"],
            "role": role,
            "themes": assigned_themes,
        })

    proposal["status"] = "PENDING_APPROVAL"
    proposal["approval"] = {"approved_by": None, "approved_at": None, "approval_reference": None}
    write_json(proposal_path, proposal)
    selection_report, selection_passed = candidate_selection_gate.validate(
        proposal_path, matrix_path, require_approved=False
    )
    if not selection_passed:
        raise ValueError(f"shared Candidate Selection validator rejected proposal: {selection_report['errors']}")
    if selection_report.get("unassigned_count") != 0:
        raise ValueError("role-complete Selection proposal unexpectedly contains UNASSIGNED rows")

    overlay_path = output_root / "selection-theme-overlay-v0.1.json"
    overlay = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "profile_id": profile.get("profile_id"),
        "basis": {
            "matrix_sha256": sha256_file(matrix_path),
            "selection_proposal_sha256": sha256_file(proposal_path),
            "selection_profile_sha256": sha256_file(profile_path),
        },
        "themes": themes,
        "assignments": sorted(theme_assignments, key=lambda value: value["evidence_task_id"]),
        "rules": [
            "Theme metadata is an Automotive editorial overlay, not a field added to the shared Candidate Selection contract.",
            "HOLD_OUT/EXCLUDE rows are omitted from Architecture theme assignment.",
            "Architecture generation must preserve Evidence boundaries from the shared matrix in addition to this thematic grouping."
        ],
    }
    write_json(overlay_path, overlay)

    # Dry-run only: exercise the production Architecture-input builder. This file
    # must never be interpreted as user/human approval or used to advance lifecycle.
    synthetic_path = output_root / "dry-run" / "candidate-selection-synthetic-approved.json"
    synthetic = copy.deepcopy(proposal)
    synthetic["status"] = "APPROVED"
    synthetic["approval"] = {
        "approved_by": "EXPERIMENT_DRY_RUN_NOT_HUMAN",
        "approved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "approval_reference": "EXPERIMENT_ONLY_DO_NOT_PERSIST_OR_ADVANCE_LIFECYCLE",
    }
    write_json(synthetic_path, synthetic)
    synthetic_report, synthetic_passed = candidate_selection_gate.validate(
        synthetic_path, matrix_path, require_approved=True
    )
    if not synthetic_passed:
        raise ValueError(f"synthetic approved Selection failed shared validator: {synthetic_report['errors']}")

    shared_input = build_architecture_input.build(synthetic_path, matrix_path)
    shared_input_path = output_root / "dry-run" / "architecture-input-shared.json"
    write_json(shared_input_path, shared_input)

    page_budget = edition.get("page_budget") or {}
    constraints_overlay_path = output_root / "architecture-constraints-overlay-v0.1.json"
    constraints_overlay = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "basis": {
            "shared_architecture_input_sha256": sha256_file(shared_input_path),
            "selection_theme_overlay_sha256": sha256_file(overlay_path),
            "edition_manifest_sha256": sha256_file(edition_path),
        },
        "page_target": page_budget.get("target"),
        "page_max": page_budget.get("max"),
        "summary_semantics": "Retrospective executive synthesis written after package drafts stabilize; not a weekly 'This Week' section.",
        "late_breaking_semantics": "Not used for the fixed retrospective cutoff unless a post-cutoff event is deliberately added in a later revision.",
        "theme_overlay_path": "selection-theme-overlay-v0.1.json",
        "finding": "Shared Architecture Input mechanics are reusable, but page budget, summary wording and domain theme grouping are edition/profile context."
    }
    write_json(constraints_overlay_path, constraints_overlay)

    role_counts = Counter(assignment["role"] for assignment in proposal["assignments"])
    theme_counts = Counter()
    for entry in theme_assignments:
        for theme in entry["themes"]:
            theme_counts[theme] += 1
    positive_count = sum(role_counts.get(role, 0) for role in candidate_selection_gate.POSITIVE_ROLES)
    manifest = {
        "schema_version": "1.0",
        "experiment": "PROFILED_SELECTION_AND_ARCHITECTURE_INPUT_PROBE",
        "issue_id": issue_id,
        "matrix_sha256": sha256_file(matrix_path),
        "matrix_row_count": matrix.get("row_count"),
        "candidate_row_count": len(candidate_rows),
        "selection_proposal": {
            "path": "candidate-selection-proposal-v0.1.json",
            "sha256": sha256_file(proposal_path),
            "status": proposal["status"],
            "shared_validator_passed": selection_passed,
            "unassigned_count": selection_report.get("unassigned_count"),
            "role_counts": dict(sorted(role_counts.items())),
            "positive_architecture_role_count": positive_count,
        },
        "theme_overlay": {
            "path": "selection-theme-overlay-v0.1.json",
            "sha256": sha256_file(overlay_path),
            "theme_counts": dict(sorted(theme_counts.items())),
        },
        "shared_architecture_input_dry_run": {
            "path": "dry-run/architecture-input-shared.json",
            "sha256": sha256_file(shared_input_path),
            "selected_item_count": shared_input.get("selected_item_count"),
            "excluded_item_count": shared_input.get("excluded_item_count"),
            "shared_builder": "scripts/build_architecture_input.py",
            "synthetic_approval_only": True,
        },
        "constraints_overlay": {
            "path": "architecture-constraints-overlay-v0.1.json",
            "sha256": sha256_file(constraints_overlay_path),
        },
        "shared_selection_gate": "scripts/candidate_selection_gate.py",
        "shared_production_files_modified": False,
        "production_lifecycle_advanced": False,
        "human_selection_approval_recorded": False,
        "architecture_human_gate_reached": False,
        "finding": "Shared Selection safety roles and Architecture-input mechanics accept the complete Automotive matrix unchanged. Domain theme continuity and edition-specific editorial constraints belong in profile/overlay context rather than the shared Selection contract."
    }
    write_json(output_root / "selection-probe-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", required=True)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--edition", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    manifest = build(
        matrix_path=Path(args.matrix),
        profile_path=Path(args.profile),
        edition_path=Path(args.edition),
        output_root=Path(args.output_root),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
