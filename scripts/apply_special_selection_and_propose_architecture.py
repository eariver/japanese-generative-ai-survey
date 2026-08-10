#!/usr/bin/env python3
"""Apply an explicitly human-approved Special Candidate Selection and propose Architecture.

This command is intentionally split at the two human gates:
- it may mark Candidate Selection APPROVED only from an explicit reviewed decision file;
- it generates and validates an Issue Architecture Plan with status=PROPOSED only.

The existing deterministic comparison, Selection, Architecture Input, and Architecture
validators remain authoritative.  This wrapper only supplies Special page constraints
and reviewed editorial grouping while preserving exact SHA bindings.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import build_architecture_input
from scripts import build_candidate_matrix
from scripts import candidate_selection_gate
from scripts import validate_issue_architecture


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


def union_boundaries(architecture_input: dict[str, Any], ids: list[str]) -> list[str]:
    item_by_id: dict[str, dict[str, Any]] = {}
    for values in architecture_input.get("selected_by_role", {}).values():
        for item in values:
            item_by_id[item["evidence_task_id"]] = item
    result: list[str] = []
    seen: set[str] = set()
    for task_id in ids:
        item = item_by_id.get(task_id)
        if item is None:
            raise ValueError(f"Architecture proposal references non-selected Evidence Task: {task_id}")
        for boundary in item.get("remaining_boundaries") or []:
            if isinstance(boundary, str) and boundary and boundary not in seen:
                seen.add(boundary)
                result.append(boundary)
    return result


def apply_selection(
    *, matrix_path: Path, decision: dict[str, Any], selection_path: Path,
    approval_reference: str,
) -> dict[str, Any]:
    initialized = candidate_selection_gate.initialize(matrix_path, selection_path, decision.get("selection_version", "v0.1"))
    overrides = decision.get("selection_assignments")
    if not isinstance(overrides, list) or not overrides:
        raise ValueError("decision.selection_assignments must be a non-empty array")
    by_id: dict[str, dict[str, Any]] = {}
    for entry in overrides:
        if not isinstance(entry, dict):
            raise ValueError("selection assignment entries must be objects")
        task_id = entry.get("evidence_task_id")
        role = entry.get("role")
        rationale = entry.get("rationale")
        if not isinstance(task_id, str) or not task_id or task_id in by_id:
            raise ValueError(f"invalid/duplicate selection assignment id: {task_id!r}")
        if role not in candidate_selection_gate.ROLES or role == "UNASSIGNED":
            raise ValueError(f"invalid reviewed selection role for {task_id}: {role!r}")
        if not isinstance(rationale, str) or not rationale.strip():
            raise ValueError(f"reviewed selection rationale required for {task_id}")
        by_id[task_id] = entry

    candidate_ids = {
        row["evidence_task_id"]
        for row in load_json(matrix_path).get("rows", [])
        if row.get("recommendation") == "CANDIDATE"
    }
    if set(by_id) != candidate_ids:
        missing = sorted(candidate_ids - set(by_id))
        extra = sorted(set(by_id) - candidate_ids)
        raise ValueError(f"reviewed Selection must assign every and only CANDIDATE row: missing={missing} extra={extra}")

    for assignment in initialized["assignments"]:
        reviewed = by_id.get(assignment["evidence_task_id"])
        if reviewed is not None:
            assignment["role"] = reviewed["role"]
            assignment["rationale"] = reviewed["rationale"]

    initialized["status"] = "APPROVED"
    initialized["approval"] = {
        "approved_by": decision.get("approved_by", "eariver"),
        "approved_at": decision["approved_at"],
        "approval_reference": approval_reference,
    }
    write_json(selection_path, initialized)
    report, passed = candidate_selection_gate.validate(selection_path, matrix_path, require_approved=True)
    if not passed:
        raise ValueError(f"approved Candidate Selection failed validation: {report['errors']}")
    return report


def build_architecture_plan(
    *, architecture_input_path: Path, decision: dict[str, Any], plan_path: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    architecture_input = load_json(architecture_input_path)
    proposal = decision.get("architecture_proposal")
    if not isinstance(proposal, dict):
        raise ValueError("decision.architecture_proposal must be an object")
    packages_spec = proposal.get("packages")
    if not isinstance(packages_spec, list) or not packages_spec:
        raise ValueError("architecture_proposal.packages must be a non-empty array")

    packages: list[dict[str, Any]] = []
    for order, spec in enumerate(packages_spec, start=1):
        if not isinstance(spec, dict):
            raise ValueError("architecture package specs must be objects")
        primaries = spec.get("primary_evidence_task_ids") or []
        supports = spec.get("supporting_evidence_task_ids") or []
        if not isinstance(primaries, list) or not isinstance(supports, list):
            raise ValueError("package primary/support ids must be arrays")
        package = {
            "package_id": spec["package_id"],
            "title": spec["title"],
            "package_type": spec["package_type"],
            "primary_evidence_task_ids": primaries,
            "supporting_evidence_task_ids": supports,
            "page_target": spec["page_target"],
            "editorial_angle": spec["editorial_angle"],
            "must_cover": spec.get("must_cover") or [],
            "boundaries": union_boundaries(architecture_input, [*primaries, *supports]),
            "late_breaking": bool(spec.get("late_breaking", False)),
            "drafting_order": order,
        }
        packages.append(package)

    plan = {
        "schema_version": "1.0",
        "issue_id": architecture_input["issue_id"],
        "architecture_version": proposal.get("architecture_version", "v0.1"),
        "status": "PROPOSED",
        "basis": {
            "architecture_input_sha256": sha256_file(architecture_input_path),
            "selection_sha256": architecture_input["basis"]["selection_sha256"],
            "matrix_sha256": architecture_input["basis"]["matrix_sha256"],
        },
        "approval": {"approved_by": None, "approved_at": None, "approval_reference": None},
        "editorial_thesis": proposal["editorial_thesis"],
        "architecture_goals": proposal["architecture_goals"],
        "page_budget": {
            "target": architecture_input["editorial_constraints"]["page_target"],
            "max": architecture_input["editorial_constraints"]["page_max"],
            "planned": sum(float(package["page_target"]) for package in packages),
        },
        "cover": {
            "headline_deferred": True,
            "headline": None,
            "anchor_candidates": proposal.get("cover_anchor_candidates") or [],
        },
        "packages": packages,
        "this_week_summary_written_last": True,
    }
    write_json(plan_path, plan)
    report, passed = validate_issue_architecture.validate(architecture_input_path, plan_path, require_approved=False)
    if not passed:
        raise ValueError(f"proposed Issue Architecture failed validation: {report['errors']}")
    return plan, report


def run(
    *, repo_root: Path, issue_id: str, evidence_run_sha: str, decision_path: Path,
    special_manifest_path: Path, approval_reference: str, audit_output: Path | None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    decision_path = decision_path.resolve()
    decision = load_json(decision_path)
    special_manifest = load_json(special_manifest_path)
    if decision.get("schema_version") != "1.0" or decision.get("issue_id") != issue_id:
        raise ValueError("reviewed editorial decision identity mismatch")
    if special_manifest.get("special_id") != issue_id:
        raise ValueError("Special manifest issue identity mismatch")
    if not isinstance(approval_reference, str) or not approval_reference.strip():
        raise ValueError("approval_reference is required")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError(f"Selection requires lifecycle EVIDENCE_REVIEWED; got {state.get('lifecycle_state')!r}")
    gates = state.get("gates") or {}
    if gates.get("evidence_normalized") != "passed" or gates.get("candidate_selection") != "pending":
        raise ValueError("Selection requires evidence_normalized=passed and candidate_selection=pending")

    evidence_dir = repo_root / "sources" / issue_id / "evidence" / "runs" / evidence_run_sha
    reviewed_path = evidence_dir / "evidence-reviewed.jsonl"
    if not reviewed_path.is_file():
        raise ValueError(f"accepted Evidence reviewed set missing: {reviewed_path}")

    selection_root = repo_root / "sources" / issue_id / "selection"
    matrix_path = selection_root / "candidate-matrix-v0.1.json"
    matrix_md_path = selection_root / "candidate-matrix-v0.1.md"
    selection_path = selection_root / "candidate-selection-v0.1.json"
    matrix = build_candidate_matrix.build(reviewed_path, state_path)
    selection_root.mkdir(parents=True, exist_ok=True)
    write_json(matrix_path, matrix)
    matrix_md_path.write_text(build_candidate_matrix.render_markdown(matrix), encoding="utf-8")
    selection_report = apply_selection(
        matrix_path=matrix_path, decision=decision, selection_path=selection_path,
        approval_reference=approval_reference.strip(),
    )

    updated_state = deepcopy(state)
    updated_state["lifecycle_state"] = "SELECTION_COMPLETE"
    updated_state["gates"]["candidate_selection"] = "passed"
    updated_state.setdefault("provenance", {})["candidate_selection"] = {
        "path": selection_path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(selection_path),
        "matrix_path": matrix_path.relative_to(repo_root).as_posix(),
        "matrix_sha256": sha256_file(matrix_path),
        "approval_reference": approval_reference.strip(),
    }
    write_json(state_path, updated_state)

    architecture_root = repo_root / "sources" / issue_id / "architecture"
    architecture_input_path = architecture_root / "architecture-input-v0.1.json"
    architecture_input = build_architecture_input.build(selection_path, matrix_path)
    page_budget = special_manifest.get("page_budget") or {}
    architecture_input["editorial_constraints"]["page_target"] = page_budget["target"]
    architecture_input["editorial_constraints"]["page_max"] = page_budget["max"]
    architecture_input["editorial_constraints"]["this_week_summary_written_last"] = True
    architecture_input["editorial_constraints"]["special_single_volume"] = True
    write_json(architecture_input_path, architecture_input)

    plan_path = architecture_root / "issue-architecture-v0.1.json"
    plan, architecture_report = build_architecture_plan(
        architecture_input_path=architecture_input_path, decision=decision, plan_path=plan_path,
    )

    audit = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "evidence_run_sha": evidence_run_sha,
        "decision_path": decision_path.relative_to(repo_root).as_posix(),
        "selection": {
            "status": "APPROVED",
            "path": selection_path.relative_to(repo_root).as_posix(),
            "sha256": sha256_file(selection_path),
            "validation": selection_report,
        },
        "state": {
            "lifecycle_state": "SELECTION_COMPLETE",
            "candidate_selection": "passed",
            "issue_architecture": updated_state["gates"].get("issue_architecture"),
        },
        "architecture": {
            "status": "PROPOSED",
            "input_path": architecture_input_path.relative_to(repo_root).as_posix(),
            "input_sha256": sha256_file(architecture_input_path),
            "plan_path": plan_path.relative_to(repo_root).as_posix(),
            "plan_sha256": sha256_file(plan_path),
            "planned_pages": plan["page_budget"]["planned"],
            "validation": architecture_report,
        },
        "human_gate": "Issue Architecture remains pending until explicit user approval.",
    }
    if audit_output is not None:
        write_json(audit_output, audit)
    return audit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--evidence-run-sha", required=True)
    parser.add_argument("--decision", required=True)
    parser.add_argument("--special-manifest", required=True)
    parser.add_argument("--approval-reference", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    result = run(
        repo_root=Path(args.repo_root), issue_id=args.issue_id,
        evidence_run_sha=args.evidence_run_sha, decision_path=Path(args.decision),
        special_manifest_path=Path(args.special_manifest), approval_reference=args.approval_reference,
        audit_output=Path(args.audit_output) if args.audit_output else None,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
