#!/usr/bin/env python3
"""Candidate Matrix, internal Selection, Architecture and Review Summary for Core v2.

WU-008 preserves the mature exact-basis/no-silent-drop mechanics while removing
Weekly-only timing, role and package vocabulary from the generic Core contract.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import survey_completeness_v2 as completeness
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening

MATRIX_SCHEMA = Path("schemas/candidate-matrix-v2.schema.json")
SELECTION_SCHEMA = Path("schemas/candidate-selection-v2.schema.json")
ARCHITECTURE_SCHEMA = Path("schemas/issue-architecture-v2.schema.json")
REVIEW_SCHEMA = Path("schemas/architecture-review-summary-v2.schema.json")

DISPOSITIONS = {"SELECTED", "HOLD", "REJECT", "INSPECT"}
ARCHITECTURE_USAGE = {"PRIMARY", "SUPPORTING", "NONE"}
MATERIAL_FOR_REVIEW = {"MATERIAL", "CONTEXT"}


def candidate_id(issue_id: str, evidence_task_id: str) -> str:
    digest = hashlib.sha256(evidence_task_id.encode("utf-8")).hexdigest()[:16]
    return f"candidate:{issue_id}:{digest}"


def _counter(values: list[str]) -> dict[str, int]:
    counts = Counter(values)
    return {key: counts[key] for key in sorted(counts)}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_datetime(value: Any) -> bool:
    if not _nonempty(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _require_contract_files(repo_root: Path) -> None:
    for path in (MATRIX_SCHEMA, SELECTION_SCHEMA, ARCHITECTURE_SCHEMA, REVIEW_SCHEMA):
        if not (repo_root / path).is_file():
            raise ValueError(f"WU-008 contract file missing: {path}")


def _load_upstream(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    evidence_acceptance_path: Path,
    views_acceptance_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    implementation_sha: str,
) -> dict[str, Any]:
    _require_contract_files(repo_root)
    profile = core.load_json(profile_path)
    screening_acceptance, _, discoveries = evidence.validate_screening_acceptance(
        repo_root,
        screening_acceptance_path,
        discovery_path,
        profile["issue_id"],
        implementation_sha,
    )
    evidence_acceptance, _ = evidence.validate_evidence_acceptance(
        repo_root, evidence_acceptance_path, implementation_sha
    )
    views_acceptance = evidence.validate_edition_views_acceptance(
        repo_root,
        profile_path,
        evidence_acceptance_path,
        views_acceptance_path,
        implementation_sha,
    )
    ledger = core.load_json(ledger_path)
    evidence.validate_materiality_ledger(
        ledger,
        repo_root,
        profile_path,
        discovery_path,
        screening_acceptance_path,
        evidence_acceptance_path,
        views_acceptance_path,
        implementation_sha,
    )
    completeness_result = core.load_json(completeness_path)
    completeness_errors = completeness.validate_profile_completeness(
        completeness_result,
        repo_root,
        profile_path,
        discovery_path,
        screening_acceptance_path,
        evidence_acceptance_path,
        views_acceptance_path,
        ledger_path,
        implementation_sha,
    )
    if completeness_errors:
        raise ValueError(f"Profile Completeness invalid: {'; '.join(completeness_errors)}")
    if evidence_acceptance["issue_id"] != profile["issue_id"] or views_acceptance["issue_id"] != profile["issue_id"]:
        raise ValueError("WU-008 upstream issue identity divergence")
    if evidence_acceptance["research_profile"] != profile["research_profile"] or views_acceptance["research_profile"] != profile["research_profile"]:
        raise ValueError("WU-008 upstream research profile divergence")
    return {
        "profile": profile,
        "discoveries": discoveries,
        "screening": screening_acceptance,
        "evidence": evidence_acceptance,
        "views": views_acceptance,
        "ledger": ledger,
        "completeness": completeness_result,
    }


def _card_path(evidence_acceptance_path: Path, evidence_row: dict[str, Any]) -> Path:
    return evidence_acceptance_path.parent / "results" / evidence_row["filename"]


def _view_path(views_acceptance_path: Path, task_id: str) -> Path:
    return views_acceptance_path.parent / "views" / evidence.view_filename(task_id)


def derive_candidate_matrix(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    evidence_acceptance_path: Path,
    views_acceptance_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    implementation_sha: str,
) -> dict[str, Any]:
    upstream = _load_upstream(
        repo_root,
        profile_path,
        discovery_path,
        screening_acceptance_path,
        evidence_acceptance_path,
        views_acceptance_path,
        ledger_path,
        completeness_path,
        implementation_sha,
    )
    profile = upstream["profile"]
    ledger = upstream["ledger"]
    evidence_acceptance = upstream["evidence"]
    views_acceptance = upstream["views"]
    ledger_by_task: dict[str, dict[str, Any]] = {}
    for row in ledger["rows"]:
        for task_id in row["evidence_task_ids"]:
            if task_id in ledger_by_task:
                raise ValueError(f"Materiality Ledger maps Evidence task to multiple Discovery rows: {task_id}")
            ledger_by_task[task_id] = row
    view_meta = {row["evidence_task_id"]: row for row in views_acceptance["views"]}

    rows: list[dict[str, Any]] = []
    for evidence_row in sorted(evidence_acceptance["results"], key=lambda row: row["evidence_task_id"]):
        task_id = evidence_row["evidence_task_id"]
        ledger_row = ledger_by_task.get(task_id)
        if ledger_row is None:
            raise ValueError(f"silent drop before Matrix: Evidence task lacks Materiality row: {task_id}")
        view_row = view_meta.get(task_id)
        if view_row is None:
            raise ValueError(f"silent drop before Matrix: Evidence task lacks accepted Edition View: {task_id}")
        card_path = _card_path(evidence_acceptance_path, evidence_row)
        view_path = _view_path(views_acceptance_path, task_id)
        card = core.load_json(card_path)
        view = core.load_json(view_path)
        if core.sha256_file(card_path) != evidence_row["sha256"] or core.sha256_file(view_path) != view_row["view_sha256"]:
            raise ValueError(f"Matrix input bytes changed for {task_id}")
        limitations = [item["text"] for item in card["limitations"]]
        unresolved = list(card["verification"]["unresolved_questions"])
        contradictions = list(card["verification"]["contradictions"])
        boundaries = list(dict.fromkeys([*limitations, *unresolved, *contradictions]))
        rows.append(
            {
                "candidate_id": candidate_id(profile["issue_id"], task_id),
                "evidence_task_id": task_id,
                "discovery_ids": list(evidence_row["discovery_ids"]),
                "evidence_sha256": evidence_row["sha256"],
                "edition_view_sha256": view_row["view_sha256"],
                "title": card["artifact"]["canonical_name"],
                "artifact_type": card["artifact"]["artifact_type"],
                "evidence_status": evidence_row["status"],
                "materiality": view_row["materiality"],
                "scope_dimensions": list(view_row["scope_dimensions"]),
                "comparison": {
                    "source_count": len(card["sources"]),
                    "claim_count": len(card["claims"]),
                    "metric_count": len(card["metrics"]),
                    "limitation_count": len(card["limitations"]),
                    "unresolved_question_count": len(unresolved),
                    "contradiction_count": len(contradictions),
                    "entity_count": len(card["entities"]),
                },
                "remaining_boundaries": boundaries,
                "profile_extensions": view["profile_annotations"],
            }
        )
    if set(ledger_by_task) != {row["evidence_task_id"] for row in rows}:
        raise ValueError("Matrix/Evidence/Materiality task set divergence")
    matrix = {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "evidence_acceptance_sha256": core.sha256_file(evidence_acceptance_path),
            "edition_views_acceptance_sha256": core.sha256_file(views_acceptance_path),
        },
        "rows": rows,
        "summary": {
            "candidate_count": len(rows),
            "materiality_counts": _counter([row["materiality"] for row in rows]),
            "evidence_status_counts": _counter([row["evidence_status"] for row in rows]),
        },
    }
    return matrix


def validate_candidate_matrix(
    matrix: dict[str, Any],
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    evidence_acceptance_path: Path,
    views_acceptance_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    implementation_sha: str,
) -> list[str]:
    try:
        expected = derive_candidate_matrix(
            repo_root,
            profile_path,
            discovery_path,
            screening_acceptance_path,
            evidence_acceptance_path,
            views_acceptance_path,
            ledger_path,
            completeness_path,
            implementation_sha,
        )
    except ValueError as exc:
        return [str(exc)]
    return [] if matrix == expected else ["Candidate Matrix does not exactly match validated upstream Evidence/View/Materiality derivation"]


def write_candidate_matrix(path: Path, matrix: dict[str, Any]) -> Path:
    if path.exists():
        raise ValueError(f"refusing to overwrite Candidate Matrix: {path}")
    core.write_json(path, matrix)
    return path


def validate_selection(
    selection: dict[str, Any], matrix_path: Path, completeness_path: Path, ledger_path: Path
) -> list[str]:
    errors: list[str] = []
    matrix = core.load_json(matrix_path)
    completeness_result = core.load_json(completeness_path)
    ledger = core.load_json(ledger_path)
    required = {"schema_version", "issue_id", "research_profile", "selection_version", "status", "basis", "assignments", "summary"}
    if set(selection) != required:
        return ["Candidate Selection fields must exactly match v2 contract; Human approval fields are forbidden"]
    if selection.get("schema_version") != "2.0-rc1" or selection.get("status") != "ESTABLISHED":
        errors.append("Candidate Selection schema/status invalid")
    if selection.get("issue_id") != matrix.get("issue_id") or selection.get("research_profile") != matrix.get("research_profile"):
        errors.append("Candidate Selection Matrix identity mismatch")
    expected_basis = {
        "candidate_matrix_sha256": core.sha256_file(matrix_path),
        "profile_completeness_sha256": core.sha256_file(completeness_path),
        "materiality_ledger_sha256": core.sha256_file(ledger_path),
    }
    if selection.get("basis") != expected_basis:
        errors.append("Candidate Selection basis does not bind exact Matrix/Completeness/Materiality bytes")
    if not _nonempty(selection.get("selection_version")):
        errors.append("selection_version must be non-empty")

    rows = matrix.get("rows")
    assignments = selection.get("assignments")
    if not isinstance(rows, list) or not isinstance(assignments, list):
        return errors + ["Matrix rows and Selection assignments must be arrays"]
    row_by_id = {row.get("candidate_id"): row for row in rows if isinstance(row, dict)}
    ids: list[str] = []
    disposition_values: list[str] = []
    for index, assignment in enumerate(assignments):
        prefix = f"assignments[{index}]"
        expected_fields = {
            "candidate_id", "disposition", "rationale", "architecture_usage",
            "publication_role", "architecture_role", "profile_extensions",
        }
        if not isinstance(assignment, dict) or set(assignment) != expected_fields:
            errors.append(f"{prefix} fields invalid")
            continue
        cid = assignment.get("candidate_id")
        if cid not in row_by_id:
            errors.append(f"{prefix} references unknown Matrix candidate: {cid}")
            continue
        ids.append(cid)
        disposition = assignment.get("disposition")
        disposition_values.append(disposition)
        if disposition not in DISPOSITIONS:
            errors.append(f"{prefix} disposition invalid")
            continue
        if not _nonempty(assignment.get("rationale")):
            errors.append(f"{prefix} rationale required")
        usage = assignment.get("architecture_usage")
        if usage not in ARCHITECTURE_USAGE:
            errors.append(f"{prefix} architecture_usage invalid")
        pub_role = assignment.get("publication_role")
        arch_role = assignment.get("architecture_role")
        if pub_role is not None and not _nonempty(pub_role):
            errors.append(f"{prefix} publication_role must be non-empty or null")
        if arch_role is not None and not _nonempty(arch_role):
            errors.append(f"{prefix} architecture_role must be non-empty or null")
        if not isinstance(assignment.get("profile_extensions"), dict):
            errors.append(f"{prefix} profile_extensions must be an object")
        row = row_by_id[cid]
        if disposition == "SELECTED":
            if usage not in {"PRIMARY", "SUPPORTING"}:
                errors.append(f"{cid}: SELECTED candidate requires PRIMARY or SUPPORTING architecture_usage")
            if pub_role is None and arch_role is None:
                errors.append(f"{cid}: SELECTED candidate requires a Profile/Publication-owned proposed role")
            if row["materiality"] in {"NON_MATERIAL", "HOLD"}:
                errors.append(f"{cid}: {row['materiality']} candidate cannot be SELECTED")
            if row["evidence_status"] in {"REJECTED", "NEEDS_MORE"}:
                errors.append(f"{cid}: unresolved/rejected Evidence cannot be SELECTED")
        else:
            if usage != "NONE" or pub_role is not None or arch_role is not None:
                errors.append(f"{cid}: non-selected candidate must not carry publication/architecture assignment")
    expected_ids = set(row_by_id)
    if len(ids) != len(set(ids)):
        errors.append("Candidate Selection contains duplicate candidate assignments")
    if set(ids) != expected_ids or len(ids) != len(expected_ids):
        errors.append("Candidate Selection must assign every Matrix candidate exactly once")

    summary = selection.get("summary")
    expected_summary = {
        "candidate_count": len(rows),
        "disposition_counts": _counter(disposition_values),
        "selected_count": sum(1 for value in disposition_values if value == "SELECTED"),
    }
    if summary != expected_summary:
        errors.append("Candidate Selection summary does not match assignments")
    if completeness_result.get("issue_id") != selection.get("issue_id") or ledger.get("issue_id") != selection.get("issue_id"):
        errors.append("Candidate Selection upstream issue identity divergence")
    return errors


def validate_architecture(
    architecture: dict[str, Any],
    profile_path: Path,
    completeness_path: Path,
    ledger_path: Path,
    matrix_path: Path,
    selection_path: Path,
    require_approved: bool = False,
) -> list[str]:
    errors: list[str] = []
    profile = core.load_json(profile_path)
    matrix = core.load_json(matrix_path)
    selection = core.load_json(selection_path)
    selection_errors = validate_selection(selection, matrix_path, completeness_path, ledger_path)
    if selection_errors:
        return [f"Candidate Selection invalid: {'; '.join(selection_errors)}"]
    required = {
        "schema_version", "issue_id", "research_profile", "publication_profile", "status", "basis",
        "editorial_thesis", "architecture_goals", "page_plan", "packages", "selected_exceptions",
        "profile_extensions", "publication_extensions", "human_review",
    }
    if set(architecture) != required:
        return ["Issue Architecture fields must exactly match generic v2 envelope"]
    if architecture.get("schema_version") != "2.0-rc1":
        errors.append("Issue Architecture schema_version mismatch")
    if architecture.get("issue_id") != profile["issue_id"] or architecture.get("research_profile") != profile["research_profile"]:
        errors.append("Issue Architecture Profile identity mismatch")
    if architecture.get("publication_profile") != profile["publication_profile"]:
        errors.append("Issue Architecture Publication Profile mismatch")
    expected_basis = {
        "production_profile_sha256": core.sha256_file(profile_path),
        "profile_completeness_sha256": core.sha256_file(completeness_path),
        "materiality_ledger_sha256": core.sha256_file(ledger_path),
        "candidate_matrix_sha256": core.sha256_file(matrix_path),
        "candidate_selection_sha256": core.sha256_file(selection_path),
    }
    if architecture.get("basis") != expected_basis:
        errors.append("Issue Architecture basis does not bind exact upstream artifacts")
    if not _nonempty(architecture.get("editorial_thesis")):
        errors.append("Issue Architecture editorial_thesis required")
    goals = architecture.get("architecture_goals")
    if not isinstance(goals, list) or not goals or len(goals) != len(set(goals)) or any(not _nonempty(value) for value in goals):
        errors.append("Issue Architecture architecture_goals must be unique non-empty strings")
    if not isinstance(architecture.get("profile_extensions"), dict) or not isinstance(architecture.get("publication_extensions"), dict):
        errors.append("Issue Architecture extensions must be objects")

    page_plan = architecture.get("page_plan")
    if not isinstance(page_plan, dict) or set(page_plan) != {"target_pages", "max_pages", "notes"}:
        errors.append("Issue Architecture page_plan fields invalid")
    else:
        target = page_plan.get("target_pages")
        maximum = page_plan.get("max_pages")
        for key, value in (("target_pages", target), ("max_pages", maximum)):
            if value is not None and (not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0):
                errors.append(f"page_plan.{key} must be positive or null")
        if isinstance(target, (int, float)) and isinstance(maximum, (int, float)) and maximum < target:
            errors.append("page_plan.max_pages cannot be less than target_pages")
        if page_plan.get("notes") is not None and not _nonempty(page_plan.get("notes")):
            errors.append("page_plan.notes must be non-empty or null")

    matrix_by_id = {row["candidate_id"]: row for row in matrix["rows"]}
    selected = {
        row["candidate_id"]: row for row in selection["assignments"] if row["disposition"] == "SELECTED"
    }
    nonselected_ids = set(matrix_by_id) - set(selected)
    packages = architecture.get("packages")
    if not isinstance(packages, list) or not packages:
        errors.append("Issue Architecture requires at least one package")
        packages = []
    package_ids: list[str] = []
    drafting_orders: list[int] = []
    primary_occurrences: dict[str, list[str]] = defaultdict(list)
    supporting_occurrences: dict[str, list[str]] = defaultdict(list)
    for index, package in enumerate(packages):
        prefix = f"packages[{index}]"
        expected_fields = {
            "package_id", "title", "purpose", "primary_candidate_ids", "supporting_candidate_ids",
            "must_cover_requirements", "boundaries", "drafting_order", "profile_extensions", "publication_extensions",
        }
        if not isinstance(package, dict) or set(package) != expected_fields:
            errors.append(f"{prefix} fields invalid")
            continue
        package_id = package.get("package_id")
        if not _nonempty(package_id):
            errors.append(f"{prefix}.package_id required")
        else:
            package_ids.append(package_id)
        for key in ("title", "purpose"):
            if not _nonempty(package.get(key)):
                errors.append(f"{prefix}.{key} required")
        order = package.get("drafting_order")
        if not isinstance(order, int) or isinstance(order, bool) or order < 1:
            errors.append(f"{prefix}.drafting_order must be a positive integer")
        else:
            drafting_orders.append(order)
        for key in ("primary_candidate_ids", "supporting_candidate_ids", "must_cover_requirements", "boundaries"):
            values = package.get(key)
            if not isinstance(values, list) or len(values) != len(set(values)) or any(not _nonempty(value) for value in values):
                errors.append(f"{prefix}.{key} must be a unique string array")
        if not isinstance(package.get("profile_extensions"), dict) or not isinstance(package.get("publication_extensions"), dict):
            errors.append(f"{prefix} extensions must be objects")
        primaries = package.get("primary_candidate_ids") if isinstance(package.get("primary_candidate_ids"), list) else []
        supports = package.get("supporting_candidate_ids") if isinstance(package.get("supporting_candidate_ids"), list) else []
        overlap = set(primaries) & set(supports)
        if overlap:
            errors.append(f"{prefix}: candidate cannot be both primary and supporting: {sorted(overlap)}")
        for cid in primaries:
            if cid in nonselected_ids:
                errors.append(f"{prefix}: non-selected candidate used as primary: {cid}")
            elif cid not in selected:
                errors.append(f"{prefix}: unknown primary candidate: {cid}")
            elif selected[cid]["architecture_usage"] != "PRIMARY":
                errors.append(f"{prefix}: PRIMARY placement conflicts with Selection usage for {cid}")
            else:
                primary_occurrences[cid].append(package_id or prefix)
        for cid in supports:
            if cid in nonselected_ids:
                errors.append(f"{prefix}: non-selected candidate used as supporting: {cid}")
            elif cid not in selected:
                errors.append(f"{prefix}: unknown supporting candidate: {cid}")
            elif selected[cid]["architecture_usage"] != "SUPPORTING":
                errors.append(f"{prefix}: SUPPORTING placement conflicts with Selection usage for {cid}")
            else:
                supporting_occurrences[cid].append(package_id or prefix)
        boundary_set = set(package.get("boundaries") or [])
        for cid in [*primaries, *supports]:
            row = matrix_by_id.get(cid)
            if row is None:
                continue
            missing_boundaries = [value for value in row["remaining_boundaries"] if value not in boundary_set]
            if missing_boundaries:
                errors.append(f"{prefix}: missing Evidence boundaries for {cid}: {missing_boundaries}")
    if len(package_ids) != len(set(package_ids)):
        errors.append("Issue Architecture package_id values must be unique")
    if len(drafting_orders) != len(set(drafting_orders)):
        errors.append("Issue Architecture drafting_order values must be unique")

    exceptions = architecture.get("selected_exceptions")
    exception_by_id: dict[str, dict[str, Any]] = {}
    if not isinstance(exceptions, list):
        errors.append("selected_exceptions must be an array")
        exceptions = []
    for index, item in enumerate(exceptions):
        if not isinstance(item, dict) or set(item) != {"candidate_id", "reason", "exception_kind"}:
            errors.append(f"selected_exceptions[{index}] fields invalid")
            continue
        cid = item.get("candidate_id")
        if cid not in selected:
            errors.append(f"selected exception references non-selected candidate: {cid}")
            continue
        if cid in exception_by_id:
            errors.append(f"duplicate selected exception: {cid}")
        exception_by_id[cid] = item
        if not _nonempty(item.get("reason")):
            errors.append(f"selected exception requires reason: {cid}")
        if item.get("exception_kind") not in {"OMITTED_FROM_ARCHITECTURE", "DEFERRED", "STRUCTURAL_EXCEPTION"}:
            errors.append(f"selected exception kind invalid: {cid}")
        if primary_occurrences.get(cid) or supporting_occurrences.get(cid):
            errors.append(f"selected candidate cannot have both package placement and exception: {cid}")

    for cid, assignment in selected.items():
        if cid in exception_by_id:
            continue
        if assignment["architecture_usage"] == "PRIMARY":
            count = len(primary_occurrences.get(cid, []))
            if count != 1:
                errors.append(f"selected PRIMARY candidate requires exactly one Architecture destination: {cid} count={count}")
        elif assignment["architecture_usage"] == "SUPPORTING":
            if not supporting_occurrences.get(cid):
                errors.append(f"selected SUPPORTING candidate requires at least one Architecture destination: {cid}")

    status = architecture.get("status")
    if status not in {"PROPOSED", "APPROVED"}:
        errors.append("Issue Architecture status invalid")
    review = architecture.get("human_review")
    if not isinstance(review, dict) or set(review) != {"reviewed_by", "reviewed_at", "review_reference"}:
        errors.append("Issue Architecture human_review fields invalid")
        review = {}
    if status == "APPROVED":
        for key in ("reviewed_by", "reviewed_at", "review_reference"):
            if not _nonempty(review.get(key)):
                errors.append(f"APPROVED Architecture requires human_review.{key}")
        if _nonempty(review.get("reviewed_at")) and not _valid_datetime(review["reviewed_at"]):
            errors.append("human_review.reviewed_at must be timezone-aware ISO-8601")
    elif any(review.get(key) is not None for key in ("reviewed_by", "reviewed_at", "review_reference")):
        errors.append("PROPOSED Architecture must not contain completed Human Review metadata")
    if require_approved and status != "APPROVED":
        errors.append("Issue Architecture must be APPROVED after Architecture Review")
    return errors


def build_architecture_review_summary(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    evidence_acceptance_path: Path,
    views_acceptance_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    matrix_path: Path,
    selection_path: Path,
    architecture_path: Path,
    implementation_sha: str,
) -> dict[str, Any]:
    upstream = _load_upstream(
        repo_root,
        profile_path,
        discovery_path,
        screening_acceptance_path,
        evidence_acceptance_path,
        views_acceptance_path,
        ledger_path,
        completeness_path,
        implementation_sha,
    )
    matrix = core.load_json(matrix_path)
    matrix_errors = validate_candidate_matrix(
        matrix,
        repo_root,
        profile_path,
        discovery_path,
        screening_acceptance_path,
        evidence_acceptance_path,
        views_acceptance_path,
        ledger_path,
        completeness_path,
        implementation_sha,
    )
    selection = core.load_json(selection_path)
    selection_errors = validate_selection(selection, matrix_path, completeness_path, ledger_path)
    architecture = core.load_json(architecture_path)
    architecture_errors = validate_architecture(
        architecture,
        profile_path,
        completeness_path,
        ledger_path,
        matrix_path,
        selection_path,
        require_approved=False,
    )
    errors = [*matrix_errors, *selection_errors, *architecture_errors]
    completeness_result = upstream["completeness"]
    if completeness_result["overall_status"] == "INCOMPLETE":
        errors.append("Profile Completeness is INCOMPLETE; Architecture Review is not ready")

    discoveries = upstream["discoveries"]
    screening_acceptance = upstream["screening"]
    evidence_acceptance = upstream["evidence"]
    ledger = upstream["ledger"]
    matrix_by_id = {row["candidate_id"]: row for row in matrix.get("rows", [])}
    selection_by_id = {row["candidate_id"]: row for row in selection.get("assignments", [])}
    primary_dest: dict[str, list[str]] = defaultdict(list)
    supporting_dest: dict[str, list[str]] = defaultdict(list)
    for package in architecture.get("packages", []):
        if not isinstance(package, dict):
            continue
        package_id = package.get("package_id")
        for cid in package.get("primary_candidate_ids", []):
            primary_dest[cid].append(package_id)
        for cid in package.get("supporting_candidate_ids", []):
            supporting_dest[cid].append(package_id)
    exceptions = {
        row["candidate_id"]: row for row in architecture.get("selected_exceptions", []) if isinstance(row, dict) and "candidate_id" in row
    }
    major: list[dict[str, Any]] = []
    for cid, row in sorted(matrix_by_id.items()):
        if row["materiality"] not in MATERIAL_FOR_REVIEW:
            continue
        assignment = selection_by_id.get(cid)
        disposition = assignment.get("disposition") if assignment else "INSPECT"
        if primary_dest.get(cid):
            kind = "PRIMARY"
            destinations = primary_dest[cid]
            reason = None
        elif supporting_dest.get(cid):
            kind = "SUPPORTING"
            destinations = supporting_dest[cid]
            reason = None
        elif cid in exceptions:
            kind = "EXCEPTION"
            destinations = []
            reason = exceptions[cid].get("reason")
        else:
            kind = "NOT_SELECTED"
            destinations = []
            reason = assignment.get("rationale") if assignment else "Selection assignment missing"
        major.append(
            {
                "candidate_id": cid,
                "title": row["title"],
                "materiality": row["materiality"],
                "selection_disposition": disposition,
                "destination_kind": kind,
                "destinations": sorted(destinations),
                "exception_reason": reason,
            }
        )

    obligations = completeness_result["obligations"]
    summary = {
        "schema_version": "2.0-rc1",
        "issue_id": upstream["profile"]["issue_id"],
        "research_profile": upstream["profile"]["research_profile"],
        "basis": {
            "architecture_sha256": core.sha256_file(architecture_path),
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
        },
        "readiness": {
            "status": "READY_FOR_ARCHITECTURE_REVIEW" if not errors else "BLOCKED",
            "errors": errors,
        },
        "discovery": {
            "total": len(discoveries),
            "counts": _counter([row["provenance"]["origin"] for row in discoveries]),
        },
        "screening": {
            "total": len(screening_acceptance["decisions"]),
            "counts": _counter([row["decision"] for row in screening_acceptance["decisions"]),
        },
        "evidence": {
            "total": len(evidence_acceptance["results"]),
            "counts": _counter([row["status"] for row in evidence_acceptance["results"]),
        },
        "materiality": {
            "total": len(ledger["rows"]),
            "counts": _counter([row["downstream_disposition"] for row in ledger["rows"]),
        },
        "selection": {
            "total": len(selection.get("assignments", [])),
            "counts": _counter([row["disposition"] for row in selection.get("assignments", []) if isinstance(row, dict) and row.get("disposition") in DISPOSITIONS]),
        },
        "completeness": {
            "overall_status": completeness_result["overall_status"],
            "obligation_counts": _counter([row["status"] for row in obligations]),
        },
        "major_material_destinations": major,
        "residual_limitations": list(completeness_result["residual_limitations"]),
        "architecture": {
            "status": architecture.get("status"),
            "editorial_thesis": architecture.get("editorial_thesis"),
            "package_count": len(architecture.get("packages", [])),
            "packages": [row.get("title") for row in architecture.get("packages", []) if isinstance(row, dict) and _nonempty(row.get("title"))],
            "page_plan": architecture.get("page_plan"),
        },
    }
    return summary


def write_json_non_destructive(path: Path, payload: dict[str, Any], label: str) -> Path:
    if path.exists():
        raise ValueError(f"refusing to overwrite {label}: {path}")
    core.write_json(path, payload)
    return path


def _path(repo_root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else repo_root / path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--implementation-sha")
    sub = parser.add_subparsers(dest="command", required=True)

    matrix = sub.add_parser("matrix")
    for name in ("profile", "discovery", "screening", "evidence", "views", "ledger", "completeness", "output"):
        matrix.add_argument(f"--{name}", required=True)

    selection_check = sub.add_parser("selection-check")
    selection_check.add_argument("--selection", required=True)
    selection_check.add_argument("--matrix", required=True)
    selection_check.add_argument("--completeness", required=True)
    selection_check.add_argument("--ledger", required=True)

    architecture_check = sub.add_parser("architecture-check")
    architecture_check.add_argument("--architecture", required=True)
    architecture_check.add_argument("--profile", required=True)
    architecture_check.add_argument("--completeness", required=True)
    architecture_check.add_argument("--ledger", required=True)
    architecture_check.add_argument("--matrix", required=True)
    architecture_check.add_argument("--selection", required=True)
    architecture_check.add_argument("--require-approved", action="store_true")

    review = sub.add_parser("review-summary")
    for name in ("profile", "discovery", "screening", "evidence", "views", "ledger", "completeness", "matrix", "selection", "architecture", "output"):
        review.add_argument(f"--{name}", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    implementation_sha = core.repository_commit_sha(repo_root, args.implementation_sha)
    try:
        if args.command == "matrix":
            payload = derive_candidate_matrix(
                repo_root,
                _path(repo_root, args.profile),
                _path(repo_root, args.discovery),
                _path(repo_root, args.screening),
                _path(repo_root, args.evidence),
                _path(repo_root, args.views),
                _path(repo_root, args.ledger),
                _path(repo_root, args.completeness),
                implementation_sha,
            )
            output = _path(repo_root, args.output)
            write_candidate_matrix(output, payload)
            print(output)
            return 0
        if args.command == "selection-check":
            path = _path(repo_root, args.selection)
            errors = validate_selection(
                core.load_json(path),
                _path(repo_root, args.matrix),
                _path(repo_root, args.completeness),
                _path(repo_root, args.ledger),
            )
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        if args.command == "architecture-check":
            path = _path(repo_root, args.architecture)
            errors = validate_architecture(
                core.load_json(path),
                _path(repo_root, args.profile),
                _path(repo_root, args.completeness),
                _path(repo_root, args.ledger),
                _path(repo_root, args.matrix),
                _path(repo_root, args.selection),
                args.require_approved,
            )
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        if args.command == "review-summary":
            payload = build_architecture_review_summary(
                repo_root,
                _path(repo_root, args.profile),
                _path(repo_root, args.discovery),
                _path(repo_root, args.screening),
                _path(repo_root, args.evidence),
                _path(repo_root, args.views),
                _path(repo_root, args.ledger),
                _path(repo_root, args.completeness),
                _path(repo_root, args.matrix),
                _path(repo_root, args.selection),
                _path(repo_root, args.architecture),
                implementation_sha,
            )
            output = _path(repo_root, args.output)
            write_json_non_destructive(output, payload, "Architecture Review Summary")
            print(output)
            return 0 if payload["readiness"]["status"] == "READY_FOR_ARCHITECTURE_REVIEW" else 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
