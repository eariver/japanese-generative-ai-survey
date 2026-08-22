#!/usr/bin/env python3
"""Apply an already-recorded Human Candidate/Architecture approval to a Weekly work branch.

This command does not create approval authority. It consumes SHA-bound approval
records already committed by the editor, validates them against the Candidate
Matrix / Architecture bytes, applies the approved roles to the pending Selection,
and advances pipeline-state only through ARCHITECTURE_ESTABLISHED.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from candidate_selection_gate import validate as validate_selection


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


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def apply(repo_root: Path, issue_id: str) -> dict[str, Any]:
    issue = repo_root / "sources" / issue_id
    selection_path = issue / "selection" / "candidate-selection-v0.1.json"
    role_approval_path = issue / "selection" / "human-role-approval-v0.1.json"
    architecture_approval_path = issue / "architecture" / "human-architecture-approval-v0.2.json"
    state_path = issue / "pipeline-state.json"

    for path in (selection_path, role_approval_path, architecture_approval_path, state_path):
        if not path.is_file():
            raise ValueError(f"required file missing: {path.relative_to(repo_root)}")

    selection = load_json(selection_path)
    role_approval = load_json(role_approval_path)
    arch_approval = load_json(architecture_approval_path)
    state = load_json(state_path)

    if selection.get("issue_id") != issue_id or role_approval.get("issue_id") != issue_id or arch_approval.get("issue_id") != issue_id:
        raise ValueError("approval/selection issue_id mismatch")
    if role_approval.get("status") != "HUMAN_ROLE_APPROVAL_RECORDED":
        raise ValueError("Human role approval is not recorded")
    if arch_approval.get("status") != "APPROVED":
        raise ValueError("Human Architecture approval is not APPROVED")

    matrix_rel = selection.get("basis", {}).get("matrix_path")
    if not isinstance(matrix_rel, str) or not matrix_rel:
        raise ValueError("selection basis.matrix_path missing")
    matrix_path = repo_root / matrix_rel
    if not matrix_path.is_file():
        raise ValueError(f"Candidate Matrix missing: {matrix_rel}")
    matrix_sha = sha256_file(matrix_path)
    expected_matrix = selection.get("basis", {}).get("matrix_sha256")
    if expected_matrix != matrix_sha:
        raise ValueError("pending Selection is not bound to current Candidate Matrix bytes")
    if role_approval.get("matrix_sha256") != matrix_sha:
        raise ValueError("Human role approval matrix SHA does not match current Candidate Matrix")
    if arch_approval.get("candidate_matrix_sha256") != matrix_sha:
        raise ValueError("Architecture approval matrix SHA does not match current Candidate Matrix")

    evidence_sha = role_approval.get("evidence_run_sha")
    if not isinstance(evidence_sha, str) or len(evidence_sha) != 64:
        raise ValueError("Human role approval evidence_run_sha is invalid")
    if arch_approval.get("evidence_run_sha") != evidence_sha:
        raise ValueError("Candidate and Architecture approvals are bound to different Evidence runs")
    evidence_run = issue / "evidence" / "runs" / evidence_sha / "evidence-reviewed.jsonl"
    if not evidence_run.is_file():
        raise ValueError("approved Evidence run is not present")

    architecture_rel = arch_approval.get("architecture_path")
    if not isinstance(architecture_rel, str) or not architecture_rel:
        raise ValueError("architecture approval path missing")
    architecture_path = repo_root / architecture_rel
    if not architecture_path.is_file():
        raise ValueError(f"approved Architecture missing: {architecture_rel}")
    expected_blob = arch_approval.get("architecture_git_blob_sha")
    actual_blob = git_blob_sha(architecture_path)
    if expected_blob != actual_blob:
        raise ValueError(f"Architecture blob SHA mismatch: expected {expected_blob}, got {actual_blob}")

    approved_roles = role_approval.get("assignments")
    if not isinstance(approved_roles, list) or not approved_roles:
        raise ValueError("Human role approval assignments missing")
    role_by_id = {}
    for item in approved_roles:
        if not isinstance(item, dict):
            raise ValueError("role approval assignment must be object")
        task_id = item.get("evidence_task_id")
        role = item.get("role")
        if not isinstance(task_id, str) or not task_id or not isinstance(role, str) or not role:
            raise ValueError("role approval assignment requires evidence_task_id and role")
        if task_id in role_by_id:
            raise ValueError(f"duplicate approved role: {task_id}")
        role_by_id[task_id] = item

    assignments = selection.get("assignments")
    if not isinstance(assignments, list):
        raise ValueError("selection assignments must be array")
    seen = set()
    for assignment in assignments:
        if not isinstance(assignment, dict):
            raise ValueError("selection assignment must be object")
        task_id = assignment.get("evidence_task_id")
        approved = role_by_id.get(task_id)
        if approved is None:
            continue
        if assignment.get("title") != approved.get("title"):
            raise ValueError(f"approved title mismatch: {task_id}")
        assignment["role"] = approved["role"]
        assignment["rationale"] = (
            "Human Candidate Selection approved this editorial role; "
            "see selection/human-role-approval-v0.1.json."
        )
        seen.add(task_id)
    missing = sorted(set(role_by_id) - seen)
    if missing:
        raise ValueError(f"approved role references missing Selection rows: {missing}")

    if any(a.get("role") == "UNASSIGNED" for a in assignments if isinstance(a, dict)):
        raise ValueError("Human-approved Selection still contains UNASSIGNED rows")

    selection["status"] = "APPROVED"
    selection["approval"] = {
        "approved_by": role_approval.get("approved_by"),
        "approved_at": role_approval.get("approved_at"),
        "approval_reference": role_approval.get("approval_reference"),
    }
    write_json(selection_path, selection)

    report, passed = validate_selection(selection_path, matrix_path, require_approved=True)
    if not passed:
        raise ValueError("Candidate Selection validator rejected the Human-approved Selection: " + "; ".join(report["errors"]))

    if state.get("lifecycle_state") not in {"EVIDENCE_REVIEWED", "SELECTION_COMPLETE", "ARCHITECTURE_ESTABLISHED"}:
        raise ValueError(f"unexpected lifecycle_state: {state.get('lifecycle_state')}")
    gates = state.get("gates")
    if not isinstance(gates, dict) or gates.get("evidence_normalized") != "passed":
        raise ValueError("Evidence gate must be passed before Architecture approval")
    gates["candidate_selection"] = "passed"
    gates["issue_architecture"] = "passed"
    state["lifecycle_state"] = "ARCHITECTURE_ESTABLISHED"
    write_json(state_path, state)

    audit = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "ARCHITECTURE_APPROVAL_APPLIED",
        "evidence_run_sha": evidence_sha,
        "candidate_matrix_sha256": matrix_sha,
        "candidate_selection_path": selection_path.relative_to(repo_root).as_posix(),
        "candidate_selection_validation": report,
        "role_approval_path": role_approval_path.relative_to(repo_root).as_posix(),
        "architecture_path": architecture_rel,
        "architecture_git_blob_sha": actual_blob,
        "architecture_approval_path": architecture_approval_path.relative_to(repo_root).as_posix(),
        "approved_by": arch_approval.get("approved_by"),
        "approved_at": arch_approval.get("approved_at"),
        "approval_reference": arch_approval.get("approval_reference"),
        "resulting_lifecycle_state": "ARCHITECTURE_ESTABLISHED",
        "article_draft_gate": "pending",
    }
    audit_path = issue / "architecture" / "architecture-approval-audit-v0.2.json"
    write_json(audit_path, audit)
    return audit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    audit = apply(root, args.issue_id)
    if args.audit_output:
        write_json(Path(args.audit_output), audit)
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
