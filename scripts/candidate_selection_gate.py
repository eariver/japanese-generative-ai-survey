#!/usr/bin/env python3
"""Create and validate a SHA-bound Human Candidate Selection decision.

The initializer never approves a selection. It creates deterministic suggestions
only for evidence-imposed roles (REJECT -> EXCLUDE, HOLD/INSPECT_MORE -> HOLD_OUT,
POST_CUTOFF CANDIDATE -> LATE_BREAKING). All other CANDIDATE rows remain UNASSIGNED.

Validation binds the decision to the exact matrix bytes and prevents editorial
promotion across unresolved Evidence or cutoff boundaries without first revising
upstream Evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

ROLES = {
    "UNASSIGNED",
    "FEATURE_CORE",
    "SECTION_CORE",
    "PAPER_WATCH",
    "SUPPORTING_EVIDENCE",
    "LATE_BREAKING",
    "CHRONOLOGY",
    "WATCHLIST",
    "HOLD_OUT",
    "EXCLUDE",
}
POSITIVE_ROLES = {"FEATURE_CORE", "SECTION_CORE", "PAPER_WATCH", "SUPPORTING_EVIDENCE", "CHRONOLOGY"}
POST_CUTOFF_ALLOWED = {"LATE_BREAKING", "WATCHLIST", "HOLD_OUT", "EXCLUDE"}
HOLD_ALLOWED = {"WATCHLIST", "HOLD_OUT", "EXCLUDE"}
REJECT_ALLOWED = {"HOLD_OUT", "EXCLUDE"}


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


def suggested_role(row: dict[str, Any]) -> tuple[str, str | None]:
    recommendation = row["recommendation"]
    timing = row["timing_relation"]
    if recommendation == "REJECT":
        return "EXCLUDE", "Evidence Runner recommendation is REJECT; re-verify Evidence before promotion."
    if recommendation in {"HOLD", "INSPECT_MORE"}:
        return "HOLD_OUT", "Evidence remains HOLD/INSPECT_MORE; re-verify Evidence before promotion."
    if recommendation == "CANDIDATE" and timing == "POST_CUTOFF":
        return "LATE_BREAKING", "Objective event is post-cutoff; preserve Late Breaking boundary."
    return "UNASSIGNED", None


def initialize(matrix_path: Path, output: Path, selection_version: str) -> dict[str, Any]:
    matrix = load_json(matrix_path)
    assignments = []
    for row in matrix.get("rows", []):
        role, rationale = suggested_role(row)
        assignments.append(
            {
                "evidence_task_id": row["evidence_task_id"],
                "title": row["title"],
                "role": role,
                "rationale": rationale,
            }
        )
    value = {
        "schema_version": "1.0",
        "issue_id": matrix["issue_id"],
        "selection_version": selection_version,
        "status": "PENDING_APPROVAL",
        "basis": {
            "matrix_path": matrix_path.as_posix(),
            "matrix_sha256": sha256_file(matrix_path),
        },
        "approval": {
            "approved_by": None,
            "approved_at": None,
            "approval_reference": None,
        },
        "assignments": assignments,
        "rules": [
            "Every matrix row must receive exactly one role before approval.",
            "Evidence recommendation CANDIDATE does not imply selection.",
            "HOLD/INSPECT_MORE/REJECT cannot be promoted to positive editorial roles without an upstream Evidence revision.",
            "POST_CUTOFF items cannot be promoted into normal main-window roles.",
            "Article drafting begins only after this selection is APPROVED and Issue Architecture is established.",
        ],
    }
    write_json(output, value)
    return value


def valid_approval(selection: dict[str, Any]) -> bool:
    approval = selection.get("approval")
    if not isinstance(approval, dict):
        return False
    if not all(isinstance(approval.get(key), str) and approval[key].strip() for key in ("approved_by", "approved_at", "approval_reference")):
        return False
    normalized = approval["approved_at"][:-1] + "+00:00" if approval["approved_at"].endswith("Z") else approval["approved_at"]
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def validate(selection_path: Path, matrix_path: Path, require_approved: bool) -> tuple[dict[str, Any], bool]:
    selection = load_json(selection_path)
    matrix = load_json(matrix_path)
    errors: list[str] = []

    if selection.get("schema_version") != "1.0":
        errors.append("selection.schema_version must be 1.0")
    if selection.get("issue_id") != matrix.get("issue_id"):
        errors.append("selection issue_id does not match matrix")
    if selection.get("basis", {}).get("matrix_sha256") != sha256_file(matrix_path):
        errors.append("selection basis matrix_sha256 does not match exact matrix bytes")

    rows = matrix.get("rows")
    assignments = selection.get("assignments")
    if not isinstance(rows, list) or not isinstance(assignments, list):
        errors.append("matrix rows and selection assignments must be arrays")
        rows = rows if isinstance(rows, list) else []
        assignments = assignments if isinstance(assignments, list) else []

    row_by_id = {row.get("evidence_task_id"): row for row in rows if isinstance(row, dict)}
    assignment_ids: list[str] = []
    for index, assignment in enumerate(assignments):
        if not isinstance(assignment, dict):
            errors.append(f"assignments[{index}] must be an object")
            continue
        task_id = assignment.get("evidence_task_id")
        role = assignment.get("role")
        if not isinstance(task_id, str) or not task_id:
            errors.append(f"assignments[{index}].evidence_task_id must be non-empty")
            continue
        assignment_ids.append(task_id)
        row = row_by_id.get(task_id)
        if row is None:
            errors.append(f"assignment references unknown matrix row: {task_id}")
            continue
        if assignment.get("title") != row.get("title"):
            errors.append(f"assignment title does not match matrix for {task_id}")
        if role not in ROLES:
            errors.append(f"invalid role for {task_id}: {role!r}")
            continue
        rationale = assignment.get("rationale")
        if role != "UNASSIGNED" and (not isinstance(rationale, str) or not rationale.strip()):
            errors.append(f"assigned role requires rationale: {task_id}")

        recommendation = row.get("recommendation")
        timing = row.get("timing_relation")
        if recommendation in {"HOLD", "INSPECT_MORE"} and role not in HOLD_ALLOWED | {"UNASSIGNED"}:
            errors.append(f"{task_id}: {recommendation} Evidence cannot be promoted to role {role}")
        if recommendation == "REJECT" and role not in REJECT_ALLOWED | {"UNASSIGNED"}:
            errors.append(f"{task_id}: REJECT Evidence cannot be promoted to role {role}")
        if timing == "POST_CUTOFF" and role not in POST_CUTOFF_ALLOWED | {"UNASSIGNED"}:
            errors.append(f"{task_id}: POST_CUTOFF item cannot use main-window role {role}")
        if role in POSITIVE_ROLES and recommendation != "CANDIDATE":
            errors.append(f"{task_id}: positive role {role} requires Evidence recommendation CANDIDATE")

    duplicate_ids = sorted(key for key, count in Counter(assignment_ids).items() if count > 1)
    missing_ids = sorted(set(row_by_id) - set(assignment_ids))
    if duplicate_ids:
        errors.append(f"duplicate selection assignments: {duplicate_ids}")
    if missing_ids:
        errors.append(f"matrix rows missing from selection: {missing_ids}")

    status = selection.get("status")
    if status not in {"PENDING_APPROVAL", "APPROVED"}:
        errors.append("selection status must be PENDING_APPROVAL or APPROVED")
    unassigned = sorted(
        assignment.get("evidence_task_id")
        for assignment in assignments
        if isinstance(assignment, dict) and assignment.get("role") == "UNASSIGNED"
    )
    if status == "APPROVED":
        if unassigned:
            errors.append(f"APPROVED selection cannot contain UNASSIGNED rows: {unassigned}")
        if not valid_approval(selection):
            errors.append("APPROVED selection requires valid approved_by/approved_at/approval_reference")
    if require_approved and status != "APPROVED":
        errors.append("selection must be APPROVED for this gate")

    role_counts = Counter(
        assignment.get("role") for assignment in assignments if isinstance(assignment, dict) and assignment.get("role") in ROLES
    )
    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": matrix.get("issue_id"),
        "matrix_sha256": sha256_file(matrix_path),
        "selection_status": status,
        "assignment_count": len(assignments),
        "unassigned_count": len(unassigned),
        "unassigned": unassigned,
        "role_counts": {key: role_counts.get(key, 0) for key in sorted(ROLES)},
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--matrix", required=True)
    init.add_argument("--output", required=True)
    init.add_argument("--selection-version", default="v0.1")

    check = sub.add_parser("validate")
    check.add_argument("--selection", required=True)
    check.add_argument("--matrix", required=True)
    check.add_argument("--report")
    check.add_argument("--require-approved", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "init":
        value = initialize(Path(args.matrix), Path(args.output), args.selection_version)
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0

    report, passed = validate(Path(args.selection), Path(args.matrix), args.require_approved)
    if args.report:
        write_json(Path(args.report), report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
