#!/usr/bin/env python3
"""Validate Candidate Selection against the exact deterministic comparison input.

This validator enforces exact candidate coverage, Evidence-route constraints,
post-cutoff handling, and explicit approval for selection-complete state.
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
    "X_REACTION_SUPPORT",
    "LATE_BREAKING",
    "CHRONOLOGY",
    "WATCHLIST",
    "HOLD_OUT",
    "EXCLUDE",
}
MAIN_ROLES = {"FEATURE_CORE", "SECTION_CORE", "PAPER_WATCH", "SUPPORTING_EVIDENCE", "X_REACTION_SUPPORT"}
HOLD_ROLES = {"HOLD_OUT", "WATCHLIST", "CHRONOLOGY", "EXCLUDE"}


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            rows.append(value)
    return rows


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def valid_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def validate(comparison_input: Path, selection_path: Path) -> tuple[dict[str, Any], bool]:
    records = read_jsonl(comparison_input)
    selection = read_json(selection_path)
    errors: list[str] = []

    if selection.get("schema_version") != "1.0":
        errors.append("selection.schema_version must be 1.0")
    if selection.get("status") not in {"selection-draft", "selection-complete"}:
        errors.append("selection.status must be selection-draft or selection-complete")
    if selection.get("comparison_input_sha256") != sha256_file(comparison_input):
        errors.append("comparison_input_sha256 does not match exact comparison input bytes")

    comparison_by_id: dict[str, dict[str, Any]] = {}
    issue_ids: set[str] = set()
    for record in records:
        comparison_id = record.get("comparison_id")
        if not isinstance(comparison_id, str) or not comparison_id:
            errors.append("comparison input contains empty comparison_id")
            continue
        if comparison_id in comparison_by_id:
            errors.append(f"comparison input contains duplicate comparison_id: {comparison_id}")
            continue
        comparison_by_id[comparison_id] = record
        issue_ids.add(record.get("issue_id"))
    expected_issue = next(iter(issue_ids)) if len(issue_ids) == 1 else None
    if expected_issue is None:
        errors.append(f"comparison input must contain exactly one issue_id: {sorted(str(v) for v in issue_ids)}")
    if selection.get("issue_id") != expected_issue:
        errors.append("selection.issue_id does not match comparison input")

    assignments = selection.get("assignments")
    if not isinstance(assignments, list):
        errors.append("selection.assignments must be an array")
        assignments = []

    seen: set[str] = set()
    role_counts: Counter[str] = Counter()
    unassigned: list[str] = []
    for index, assignment in enumerate(assignments):
        if not isinstance(assignment, dict):
            errors.append(f"assignments[{index}] must be an object")
            continue
        comparison_id = assignment.get("comparison_id")
        if not isinstance(comparison_id, str) or not comparison_id:
            errors.append(f"assignments[{index}].comparison_id must be non-empty")
            continue
        if comparison_id in seen:
            errors.append(f"selection contains duplicate comparison_id: {comparison_id}")
            continue
        seen.add(comparison_id)
        record = comparison_by_id.get(comparison_id)
        if record is None:
            errors.append(f"selection contains unknown comparison_id: {comparison_id}")
            continue

        if assignment.get("candidate_id") != record.get("candidate_id"):
            errors.append(f"{comparison_id}: candidate_id does not match comparison input")
        role = assignment.get("role")
        if role not in ROLES:
            errors.append(f"{comparison_id}: invalid role {role!r}")
            continue
        role_counts[role] += 1
        if role == "UNASSIGNED":
            unassigned.append(comparison_id)

        rationale = assignment.get("rationale")
        if role != "UNASSIGNED" and (not isinstance(rationale, str) or not rationale.strip()):
            errors.append(f"{comparison_id}: assigned role requires a non-empty rationale")

        recommendation = record.get("evidence", {}).get("recommendation")
        if recommendation == "REJECT" and role not in {"UNASSIGNED", "EXCLUDE"}:
            errors.append(f"{comparison_id}: Evidence recommendation=REJECT may only be UNASSIGNED or EXCLUDE")
        if recommendation in {"HOLD", "INSPECT_MORE"} and role not in ({"UNASSIGNED"} | HOLD_ROLES):
            errors.append(
                f"{comparison_id}: Evidence recommendation={recommendation} may only use UNASSIGNED/HOLD_OUT/WATCHLIST/CHRONOLOGY/EXCLUDE"
            )

        positions = set(record.get("temporal", {}).get("position_hints") or [])
        pure_post_cutoff = "POST_CUTOFF" in positions and not ({"PRE_WINDOW", "MAIN_WINDOW"} & positions)
        cutoff_unresolved = "CUTOFF_DAY_UNRESOLVED" in positions and not ({"PRE_WINDOW", "MAIN_WINDOW"} & positions)
        if role in MAIN_ROLES and (pure_post_cutoff or cutoff_unresolved):
            override = assignment.get("temporal_override_reason")
            if not isinstance(override, str) or not override.strip():
                errors.append(
                    f"{comparison_id}: main-content role with post-cutoff/cutoff-day-unresolved timing requires temporal_override_reason"
                )

    expected_ids = set(comparison_by_id)
    missing_ids = sorted(expected_ids - seen)
    unexpected_ids = sorted(seen - expected_ids)
    if missing_ids:
        errors.append(f"selection is missing comparison IDs: {missing_ids}")
    if unexpected_ids:
        errors.append(f"selection contains unexpected comparison IDs: {unexpected_ids}")
    if len(assignments) != len(records):
        errors.append(f"assignment count {len(assignments)} does not equal comparison record count {len(records)}")

    status = selection.get("status")
    gate = selection.get("gate")
    if not isinstance(gate, dict):
        errors.append("selection.gate must be an object")
        gate = {}
    approved = gate.get("approved")
    if not isinstance(approved, bool):
        errors.append("selection.gate.approved must be boolean")
    if status == "selection-complete":
        if unassigned:
            errors.append(f"selection-complete cannot contain UNASSIGNED roles: {unassigned}")
        if approved is not True:
            errors.append("selection-complete requires gate.approved=true")
        for field in ("approved_by", "approval_reference"):
            value = gate.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"selection-complete requires non-empty gate.{field}")
        if not valid_datetime(gate.get("approved_at")):
            errors.append("selection-complete requires timezone-aware gate.approved_at")
    elif status == "selection-draft":
        if approved is True:
            errors.append("selection-draft must not set gate.approved=true")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": expected_issue,
        "status": status,
        "comparison_record_count": len(records),
        "assignment_count": len(assignments),
        "unassigned_count": len(unassigned),
        "unassigned_comparison_ids": unassigned,
        "role_counts": {role: role_counts.get(role, 0) for role in sorted(ROLES)},
        "missing_comparison_ids": missing_ids,
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison-input", required=True)
    parser.add_argument("--selection", required=True)
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.comparison_input), Path(args.selection))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
