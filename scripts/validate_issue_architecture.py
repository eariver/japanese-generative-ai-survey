#!/usr/bin/env python3
"""Validate one Issue Architecture Plan against its exact Architecture Input.

The validator enforces the Human Selection boundary before drafting: exact input
SHA binding, complete primary coverage, no HOLD/EXCLUDE intrusion, Late Breaking
placement, evidence-boundary propagation, per-package/page accounting, and
approval metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ARCHITECTURE_ROLES = {
    "FEATURE_CORE",
    "SECTION_CORE",
    "PAPER_WATCH",
    "SUPPORTING_EVIDENCE",
    "LATE_BREAKING",
    "CHRONOLOGY",
    "WATCHLIST",
}
PACKAGE_TYPES = {
    "FRONTMATTER",
    "LEAD",
    "FEATURE",
    "COMPARISON",
    "SECTION",
    "DEEP_DIVE",
    "PAPER_WATCH",
    "X_COMMUNITY",
    "LATE_BREAKING",
    "WATCHLIST_CHRONOLOGY",
    "REFERENCES",
}
MAX_PACKAGE_PAGES = 8


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_datetime(value: Any) -> bool:
    if not nonempty(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def selected_maps(architecture_input: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, str], set[str]]:
    selected: dict[str, dict[str, Any]] = {}
    role_by_id: dict[str, str] = {}
    selected_by_role = architecture_input.get("selected_by_role")
    if not isinstance(selected_by_role, dict):
        raise ValueError("architecture input selected_by_role must be an object")

    for role, items in selected_by_role.items():
        if role not in ARCHITECTURE_ROLES:
            raise ValueError(f"architecture input contains unsupported role: {role}")
        if not isinstance(items, list):
            raise ValueError(f"architecture input role {role} must be an array")
        for item in items:
            if not isinstance(item, dict):
                raise ValueError(f"architecture input role {role} contains a non-object item")
            task_id = item.get("evidence_task_id")
            if not nonempty(task_id):
                raise ValueError(f"architecture input role {role} item lacks evidence_task_id")
            if task_id in selected:
                raise ValueError(f"architecture input repeats evidence_task_id: {task_id}")
            if item.get("role") != role:
                raise ValueError(f"architecture input item role mismatch for {task_id}: {item.get('role')} != {role}")
            selected[task_id] = item
            role_by_id[task_id] = role

    excluded_ids: set[str] = set()
    excluded = architecture_input.get("not_selected_for_architecture") or []
    if not isinstance(excluded, list):
        raise ValueError("architecture input not_selected_for_architecture must be an array")
    for item in excluded:
        if not isinstance(item, dict) or not nonempty(item.get("evidence_task_id")):
            raise ValueError("not_selected_for_architecture contains invalid item")
        excluded_ids.add(item["evidence_task_id"])
    return selected, role_by_id, excluded_ids


def validate(
    architecture_input_path: Path,
    plan_path: Path,
    require_approved: bool,
) -> tuple[dict[str, Any], bool]:
    architecture_input = load_json(architecture_input_path)
    plan = load_json(plan_path)
    errors: list[str] = []

    if plan.get("schema_version") != "1.0":
        errors.append("plan.schema_version must be 1.0")
    if plan.get("issue_id") != architecture_input.get("issue_id"):
        errors.append("plan.issue_id does not match Architecture Input")

    basis = plan.get("basis")
    input_basis = architecture_input.get("basis")
    if not isinstance(basis, dict):
        errors.append("plan.basis must be an object")
        basis = {}
    if not isinstance(input_basis, dict):
        raise ValueError("architecture input basis must be an object")
    exact_input_sha = sha256_file(architecture_input_path)
    if basis.get("architecture_input_sha256") != exact_input_sha:
        errors.append("plan.basis.architecture_input_sha256 does not match exact input bytes")
    if basis.get("selection_sha256") != input_basis.get("selection_sha256"):
        errors.append("plan.basis.selection_sha256 does not match Architecture Input")
    if basis.get("matrix_sha256") != input_basis.get("matrix_sha256"):
        errors.append("plan.basis.matrix_sha256 does not match Architecture Input")

    selected, role_by_id, excluded_ids = selected_maps(architecture_input)
    selected_ids = set(selected)
    supporting_role_ids = {task_id for task_id, role in role_by_id.items() if role == "SUPPORTING_EVIDENCE"}
    primary_required = selected_ids - supporting_role_ids

    packages = plan.get("packages")
    if not isinstance(packages, list) or not packages:
        errors.append("plan.packages must be a non-empty array")
        packages = []

    package_ids: list[str] = []
    drafting_orders: list[int] = []
    primary_occurrences: dict[str, list[str]] = defaultdict(list)
    support_occurrences: dict[str, list[str]] = defaultdict(list)
    planned_sum = 0.0

    for index, package in enumerate(packages):
        prefix = f"packages[{index}]"
        if not isinstance(package, dict):
            errors.append(f"{prefix} must be an object")
            continue
        package_id = package.get("package_id")
        package_type = package.get("package_type")
        late_breaking = package.get("late_breaking")
        page_target = package.get("page_target")
        drafting_order = package.get("drafting_order")
        if not nonempty(package_id):
            errors.append(f"{prefix}.package_id must be non-empty")
        else:
            package_ids.append(package_id)
        if package_type not in PACKAGE_TYPES:
            errors.append(f"{prefix}.package_type is invalid: {package_type!r}")
        if not isinstance(late_breaking, bool):
            errors.append(f"{prefix}.late_breaking must be boolean")
        if package_type == "LATE_BREAKING" and late_breaking is not True:
            errors.append(f"{prefix}: package_type=LATE_BREAKING requires late_breaking=true")
        if late_breaking is True and package_type != "LATE_BREAKING":
            errors.append(f"{prefix}: late_breaking=true requires package_type=LATE_BREAKING")
        if not isinstance(page_target, (int, float)) or isinstance(page_target, bool) or page_target <= 0:
            errors.append(f"{prefix}.page_target must be positive")
        else:
            if page_target > MAX_PACKAGE_PAGES:
                errors.append(
                    f"{prefix}.page_target {page_target!r} exceeds package maximum {MAX_PACKAGE_PAGES}"
                )
            planned_sum += float(page_target)
        if not isinstance(drafting_order, int) or isinstance(drafting_order, bool) or drafting_order < 1:
            errors.append(f"{prefix}.drafting_order must be a positive integer")
        else:
            drafting_orders.append(drafting_order)

        primaries = package.get("primary_evidence_task_ids")
        supports = package.get("supporting_evidence_task_ids")
        boundaries = package.get("boundaries")
        if not isinstance(primaries, list):
            errors.append(f"{prefix}.primary_evidence_task_ids must be an array")
            primaries = []
        if not isinstance(supports, list):
            errors.append(f"{prefix}.supporting_evidence_task_ids must be an array")
            supports = []
        if not isinstance(boundaries, list):
            errors.append(f"{prefix}.boundaries must be an array")
            boundaries = []
        if len(primaries) != len(set(primaries)):
            errors.append(f"{prefix}.primary_evidence_task_ids contains duplicates")
        if len(supports) != len(set(supports)):
            errors.append(f"{prefix}.supporting_evidence_task_ids contains duplicates")
        overlap = sorted(set(primaries) & set(supports))
        if overlap:
            errors.append(f"{prefix}: same item cannot be primary and support in one package: {overlap}")
        if len(boundaries) != len(set(boundaries)):
            errors.append(f"{prefix}.boundaries contains duplicates")

        for task_id in primaries:
            if task_id in excluded_ids:
                errors.append(f"{prefix}: excluded/HOLD item used as primary: {task_id}")
                continue
            if task_id not in selected_ids:
                errors.append(f"{prefix}: unknown primary Evidence Task: {task_id}")
                continue
            if task_id in supporting_role_ids:
                errors.append(f"{prefix}: SUPPORTING_EVIDENCE role cannot be promoted to primary: {task_id}")
            primary_occurrences[task_id].append(package_id or prefix)
            item = selected[task_id]
            if role_by_id[task_id] == "LATE_BREAKING" or item.get("timing_relation") == "POST_CUTOFF":
                if late_breaking is not True or package_type != "LATE_BREAKING":
                    errors.append(f"{prefix}: Late Breaking/Post-Cutoff primary must be in LATE_BREAKING package: {task_id}")

        for task_id in supports:
            if task_id in excluded_ids:
                errors.append(f"{prefix}: excluded/HOLD item used as support: {task_id}")
                continue
            if task_id not in selected_ids:
                errors.append(f"{prefix}: unknown supporting Evidence Task: {task_id}")
                continue
            support_occurrences[task_id].append(package_id or prefix)

        package_boundary_set = {value for value in boundaries if isinstance(value, str)}
        for task_id in list(dict.fromkeys([*primaries, *supports])):
            if task_id not in selected:
                continue
            required_boundaries = selected[task_id].get("remaining_boundaries") or []
            if not isinstance(required_boundaries, list):
                errors.append(f"Architecture Input remaining_boundaries must be an array for {task_id}")
                continue
            missing_boundaries = sorted(
                boundary for boundary in required_boundaries
                if isinstance(boundary, str) and boundary not in package_boundary_set
            )
            if missing_boundaries:
                errors.append(f"{prefix}: missing Evidence boundaries for {task_id}: {missing_boundaries}")

    duplicate_package_ids = sorted(key for key, count in Counter(package_ids).items() if count > 1)
    duplicate_orders = sorted(key for key, count in Counter(drafting_orders).items() if count > 1)
    if duplicate_package_ids:
        errors.append(f"duplicate package_id values: {duplicate_package_ids}")
    if duplicate_orders:
        errors.append(f"duplicate drafting_order values: {duplicate_orders}")

    missing_primary = sorted(task_id for task_id in primary_required if not primary_occurrences.get(task_id))
    duplicate_primary = sorted(task_id for task_id, placements in primary_occurrences.items() if len(placements) > 1)
    if missing_primary:
        errors.append(f"selected non-support items missing primary package placement: {missing_primary}")
    if duplicate_primary:
        errors.append(f"selected items have multiple primary package placements: {duplicate_primary}")

    page_budget = plan.get("page_budget")
    constraints = architecture_input.get("editorial_constraints")
    if not isinstance(page_budget, dict):
        errors.append("plan.page_budget must be an object")
        page_budget = {}
    if not isinstance(constraints, dict):
        raise ValueError("architecture input editorial_constraints must be an object")
    target = page_budget.get("target")
    maximum = page_budget.get("max")
    planned = page_budget.get("planned")
    input_target = constraints.get("page_target")
    input_max = constraints.get("page_max")
    if target != input_target:
        errors.append(f"plan.page_budget.target {target!r} does not match input target {input_target!r}")
    if maximum != input_max:
        errors.append(f"plan.page_budget.max {maximum!r} does not match input max {input_max!r}")
    if not isinstance(planned, (int, float)) or isinstance(planned, bool) or planned <= 0:
        errors.append("plan.page_budget.planned must be positive")
    else:
        if isinstance(maximum, (int, float)) and planned > maximum:
            errors.append(f"planned page budget {planned} exceeds maximum {maximum}")
        if not math.isclose(float(planned), planned_sum, rel_tol=0.0, abs_tol=1e-9):
            errors.append(f"package page_target sum {planned_sum:g} does not equal page_budget.planned {planned}")

    cover = plan.get("cover")
    if not isinstance(cover, dict):
        errors.append("plan.cover must be an object")
    else:
        if cover.get("headline_deferred") is not True:
            errors.append("cover.headline_deferred must be true at Architecture stage")
        if cover.get("headline") is not None:
            errors.append("cover.headline must remain null until drafts are stable")
        anchors = cover.get("anchor_candidates")
        if not isinstance(anchors, list):
            errors.append("cover.anchor_candidates must be an array")
        elif len(anchors) != len(set(anchors)):
            errors.append("cover.anchor_candidates contains duplicates")

    if plan.get("this_week_summary_written_last") is not True:
        errors.append("this_week_summary_written_last must be true")

    status = plan.get("status")
    if status not in {"PROPOSED", "APPROVED"}:
        errors.append("plan.status must be PROPOSED or APPROVED")
    approval = plan.get("approval")
    if not isinstance(approval, dict):
        errors.append("plan.approval must be an object")
        approval = {}
    if status == "APPROVED":
        for key in ("approved_by", "approved_at", "approval_reference"):
            if not nonempty(approval.get(key)):
                errors.append(f"APPROVED Architecture requires approval.{key}")
        if nonempty(approval.get("approved_at")) and not valid_datetime(approval.get("approved_at")):
            errors.append("approval.approved_at must be timezone-aware ISO-8601")
    if require_approved and status != "APPROVED":
        errors.append("Architecture Plan must be APPROVED for drafting gate")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": architecture_input.get("issue_id"),
        "architecture_input_sha256": exact_input_sha,
        "plan_status": status,
        "package_count": len(packages),
        "selected_item_count": len(selected_ids),
        "primary_required_count": len(primary_required),
        "primary_covered_count": len({task_id for task_id in primary_occurrences if task_id in primary_required}),
        "supporting_role_count": len(supporting_role_ids),
        "planned_page_sum": planned_sum,
        "missing_primary_items": missing_primary,
        "duplicate_primary_items": duplicate_primary,
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--architecture-input", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--report")
    parser.add_argument("--require-approved", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(
        Path(args.architecture_input),
        Path(args.plan),
        args.require_approved,
    )
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
