#!/usr/bin/env python3
"""Profile-neutral Candidate Matrix, Selection, Architecture, and Review Summary."""

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

MATRIX_SCHEMA = Path("schemas/candidate-matrix-v2.schema.json")
SELECTION_SCHEMA = Path("schemas/candidate-selection-v2.schema.json")
ARCHITECTURE_SCHEMA = Path("schemas/issue-architecture-v2.schema.json")
REVIEW_SCHEMA = Path("schemas/architecture-review-summary-v2.schema.json")
DISPOSITIONS = {"SELECTED", "HOLD", "REJECT", "INSPECT"}
USAGES = {"PRIMARY", "SUPPORTING", "NONE"}
MATERIAL_REVIEW = {"MATERIAL", "CONTEXT"}


def candidate_id(issue_id: str, task_id: str) -> str:
    return f"candidate:{issue_id}:{hashlib.sha256(task_id.encode('utf-8')).hexdigest()[:16]}"


def _counter(values: list[str]) -> dict[str, int]:
    count = Counter(values)
    return {key: count[key] for key in sorted(count)}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _aware_datetime(value: Any) -> bool:
    if not _nonempty(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _require_contracts(repo_root: Path) -> None:
    for rel in (MATRIX_SCHEMA, SELECTION_SCHEMA, ARCHITECTURE_SCHEMA, REVIEW_SCHEMA):
        if not (repo_root / rel).is_file():
            raise ValueError(f"WU-008 contract file missing: {rel}")


def _load_upstream(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_path: Path,
    evidence_path: Path,
    views_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    implementation_sha: str,
) -> dict[str, Any]:
    _require_contracts(repo_root)
    profile = core.load_json(profile_path)
    screening_acceptance, _, discoveries = evidence.validate_screening_acceptance(
        repo_root, screening_path, discovery_path, profile["issue_id"], implementation_sha
    )
    evidence_acceptance, _ = evidence.validate_evidence_acceptance(
        repo_root, evidence_path, implementation_sha
    )
    views_acceptance = evidence.validate_edition_views_acceptance(
        repo_root, profile_path, evidence_path, views_path, implementation_sha
    )
    ledger = core.load_json(ledger_path)
    evidence.validate_materiality_ledger(
        ledger, repo_root, profile_path, discovery_path, screening_path,
        evidence_path, views_path, implementation_sha,
    )
    complete = core.load_json(completeness_path)
    complete_errors = completeness.validate_profile_completeness(
        complete, repo_root, profile_path, discovery_path, screening_path,
        evidence_path, views_path, ledger_path, implementation_sha,
    )
    if complete_errors:
        raise ValueError(f"Profile Completeness invalid: {'; '.join(complete_errors)}")
    for payload, label in ((screening_acceptance, "Screening"), (evidence_acceptance, "Evidence"), (views_acceptance, "Edition View"), (ledger, "Materiality"), (complete, "Completeness")):
        if payload.get("issue_id") != profile["issue_id"] or payload.get("research_profile") != profile["research_profile"]:
            raise ValueError(f"WU-008 {label}/Profile identity divergence")
    return {
        "profile": profile,
        "discoveries": discoveries,
        "screening": screening_acceptance,
        "evidence": evidence_acceptance,
        "views": views_acceptance,
        "ledger": ledger,
        "completeness": complete,
    }


def derive_candidate_matrix(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_path: Path,
    evidence_path: Path,
    views_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    implementation_sha: str,
) -> dict[str, Any]:
    up = _load_upstream(
        repo_root, profile_path, discovery_path, screening_path, evidence_path,
        views_path, ledger_path, completeness_path, implementation_sha,
    )
    profile = up["profile"]
    evidence_acceptance = up["evidence"]
    views_acceptance = up["views"]
    ledger = up["ledger"]
    ledger_by_task: dict[str, dict[str, Any]] = {}
    for row in ledger["rows"]:
        for task_id in row["evidence_task_ids"]:
            if task_id in ledger_by_task:
                raise ValueError(f"Materiality maps task more than once: {task_id}")
            ledger_by_task[task_id] = row
    view_meta = {row["evidence_task_id"]: row for row in views_acceptance["views"]}
    rows: list[dict[str, Any]] = []
    for e_row in sorted(evidence_acceptance["results"], key=lambda value: value["evidence_task_id"]):
        task_id = e_row["evidence_task_id"]
        if task_id not in ledger_by_task or task_id not in view_meta:
            raise ValueError(f"silent drop before Matrix: {task_id}")
        card_path = evidence_path.parent / "results" / e_row["filename"]
        view_path = views_path.parent / "views" / evidence.view_filename(task_id)
        if core.sha256_file(card_path) != e_row["sha256"] or core.sha256_file(view_path) != view_meta[task_id]["view_sha256"]:
            raise ValueError(f"Matrix input bytes changed: {task_id}")
        card = core.load_json(card_path)
        view = core.load_json(view_path)
        boundaries = list(dict.fromkeys([
            *[item["text"] for item in card["limitations"]],
            *card["verification"]["unresolved_questions"],
            *card["verification"]["contradictions"],
        ]))
        rows.append({
            "candidate_id": candidate_id(profile["issue_id"], task_id),
            "evidence_task_id": task_id,
            "discovery_ids": list(e_row["discovery_ids"]),
            "evidence_sha256": e_row["sha256"],
            "edition_view_sha256": view_meta[task_id]["view_sha256"],
            "title": card["artifact"]["canonical_name"],
            "artifact_type": card["artifact"]["artifact_type"],
            "evidence_status": e_row["status"],
            "materiality": view_meta[task_id]["materiality"],
            "scope_dimensions": list(view_meta[task_id]["scope_dimensions"]),
            "comparison": {
                "source_count": len(card["sources"]),
                "claim_count": len(card["claims"]),
                "metric_count": len(card["metrics"]),
                "limitation_count": len(card["limitations"]),
                "unresolved_question_count": len(card["verification"]["unresolved_questions"]),
                "contradiction_count": len(card["verification"]["contradictions"]),
                "entity_count": len(card["entities"]),
            },
            "remaining_boundaries": boundaries,
            "profile_extensions": view["profile_annotations"],
        })
    if set(ledger_by_task) != {row["evidence_task_id"] for row in rows}:
        raise ValueError("Matrix/Evidence/Materiality task set divergence")
    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "evidence_acceptance_sha256": core.sha256_file(evidence_path),
            "edition_views_acceptance_sha256": core.sha256_file(views_path),
        },
        "rows": rows,
        "summary": {
            "candidate_count": len(rows),
            "materiality_counts": _counter([row["materiality"] for row in rows]),
            "evidence_status_counts": _counter([row["evidence_status"] for row in rows]),
        },
    }


def validate_candidate_matrix(matrix: dict[str, Any], *args: Any) -> list[str]:
    try:
        expected = derive_candidate_matrix(*args)
    except ValueError as exc:
        return [str(exc)]
    return [] if matrix == expected else ["Candidate Matrix does not exactly match validated upstream Evidence/View/Materiality derivation"]


def write_candidate_matrix(path: Path, payload: dict[str, Any]) -> Path:
    if path.exists():
        raise ValueError(f"refusing to overwrite Candidate Matrix: {path}")
    core.write_json(path, payload)
    return path


def validate_selection(selection: dict[str, Any], matrix_path: Path, completeness_path: Path, ledger_path: Path) -> list[str]:
    errors: list[str] = []
    matrix = core.load_json(matrix_path)
    complete = core.load_json(completeness_path)
    ledger = core.load_json(ledger_path)
    required = {"schema_version", "issue_id", "research_profile", "selection_version", "status", "basis", "assignments", "summary"}
    if set(selection) != required:
        return ["Candidate Selection fields must exactly match v2 contract; Human approval fields are forbidden"]
    if selection.get("schema_version") != "2.0-rc1" or selection.get("status") != "ESTABLISHED":
        errors.append("Candidate Selection schema/status invalid")
    if selection.get("issue_id") != matrix.get("issue_id") or selection.get("research_profile") != matrix.get("research_profile"):
        errors.append("Candidate Selection Matrix identity mismatch")
    if selection.get("basis") != {
        "candidate_matrix_sha256": core.sha256_file(matrix_path),
        "profile_completeness_sha256": core.sha256_file(completeness_path),
        "materiality_ledger_sha256": core.sha256_file(ledger_path),
    }:
        errors.append("Candidate Selection basis does not bind exact Matrix/Completeness/Materiality bytes")
    if not _nonempty(selection.get("selection_version")):
        errors.append("selection_version must be non-empty")
    rows = matrix.get("rows")
    assignments = selection.get("assignments")
    if not isinstance(rows, list) or not isinstance(assignments, list):
        return errors + ["Matrix rows and Selection assignments must be arrays"]
    by_id = {row.get("candidate_id"): row for row in rows if isinstance(row, dict)}
    ids: list[str] = []
    dispositions: list[str] = []
    fields = {"candidate_id", "disposition", "rationale", "architecture_usage", "publication_role", "architecture_role", "profile_extensions"}
    for index, assignment in enumerate(assignments):
        prefix = f"assignments[{index}]"
        if not isinstance(assignment, dict) or set(assignment) != fields:
            errors.append(f"{prefix} fields invalid")
            continue
        cid = assignment.get("candidate_id")
        if cid not in by_id:
            errors.append(f"{prefix} references unknown Matrix candidate: {cid}")
            continue
        ids.append(cid)
        disposition = assignment.get("disposition")
        dispositions.append(disposition)
        if disposition not in DISPOSITIONS:
            errors.append(f"{prefix} disposition invalid")
            continue
        if not _nonempty(assignment.get("rationale")):
            errors.append(f"{prefix} rationale required")
        usage = assignment.get("architecture_usage")
        if usage not in USAGES:
            errors.append(f"{prefix} architecture_usage invalid")
        pub_role = assignment.get("publication_role")
        arch_role = assignment.get("architecture_role")
        if pub_role is not None and not _nonempty(pub_role):
            errors.append(f"{prefix} publication_role invalid")
        if arch_role is not None and not _nonempty(arch_role):
            errors.append(f"{prefix} architecture_role invalid")
        if not isinstance(assignment.get("profile_extensions"), dict):
            errors.append(f"{prefix} profile_extensions must be an object")
        row = by_id[cid]
        if disposition == "SELECTED":
            if usage not in {"PRIMARY", "SUPPORTING"}:
                errors.append(f"{cid}: SELECTED candidate requires PRIMARY or SUPPORTING architecture_usage")
            if pub_role is None and arch_role is None:
                errors.append(f"{cid}: SELECTED candidate requires a Profile/Publication-owned proposed role")
            if row["materiality"] in {"NON_MATERIAL", "HOLD"}:
                errors.append(f"{cid}: {row['materiality']} candidate cannot be SELECTED")
            if row["evidence_status"] in {"REJECTED", "NEEDS_MORE"}:
                errors.append(f"{cid}: unresolved/rejected Evidence cannot be SELECTED")
        elif usage != "NONE" or pub_role is not None or arch_role is not None:
            errors.append(f"{cid}: non-selected candidate must not carry publication/architecture assignment")
    if len(ids) != len(set(ids)):
        errors.append("Candidate Selection contains duplicate candidate assignments")
    if set(ids) != set(by_id) or len(ids) != len(by_id):
        errors.append("Candidate Selection must assign every Matrix candidate exactly once")
    expected_summary = {
        "candidate_count": len(rows),
        "disposition_counts": _counter(dispositions),
        "selected_count": sum(value == "SELECTED" for value in dispositions),
    }
    if selection.get("summary") != expected_summary:
        errors.append("Candidate Selection summary does not match assignments")
    if complete.get("issue_id") != selection.get("issue_id") or ledger.get("issue_id") != selection.get("issue_id"):
        errors.append("Candidate Selection upstream issue identity divergence")
    return errors


def validate_architecture(
    architecture: dict[str, Any], profile_path: Path, completeness_path: Path,
    ledger_path: Path, matrix_path: Path, selection_path: Path,
    require_approved: bool = False,
) -> list[str]:
    selection = core.load_json(selection_path)
    selection_errors = validate_selection(selection, matrix_path, completeness_path, ledger_path)
    if selection_errors:
        return [f"Candidate Selection invalid: {'; '.join(selection_errors)}"]
    profile = core.load_json(profile_path)
    matrix = core.load_json(matrix_path)
    errors: list[str] = []
    required = {"schema_version", "issue_id", "research_profile", "publication_profile", "status", "basis", "editorial_thesis", "architecture_goals", "page_plan", "packages", "selected_exceptions", "profile_extensions", "publication_extensions", "human_review"}
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
        errors.append("Issue Architecture architecture_goals invalid")
    if not isinstance(architecture.get("profile_extensions"), dict) or not isinstance(architecture.get("publication_extensions"), dict):
        errors.append("Issue Architecture extensions must be objects")
    page = architecture.get("page_plan")
    if not isinstance(page, dict) or set(page) != {"target_pages", "max_pages", "notes"}:
        errors.append("Issue Architecture page_plan fields invalid")
    else:
        target, maximum = page.get("target_pages"), page.get("max_pages")
        for key, value in (("target_pages", target), ("max_pages", maximum)):
            if value is not None and (not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0):
                errors.append(f"page_plan.{key} must be positive or null")
        if isinstance(target, (int, float)) and isinstance(maximum, (int, float)) and maximum < target:
            errors.append("page_plan.max_pages cannot be less than target_pages")
        if page.get("notes") is not None and not _nonempty(page.get("notes")):
            errors.append("page_plan.notes must be non-empty or null")

    matrix_by_id = {row["candidate_id"]: row for row in matrix["rows"]}
    selected = {row["candidate_id"]: row for row in selection["assignments"] if row["disposition"] == "SELECTED"}
    nonselected = set(matrix_by_id) - set(selected)
    primary: dict[str, list[str]] = defaultdict(list)
    supporting: dict[str, list[str]] = defaultdict(list)
    package_ids: list[str] = []
    orders: list[int] = []
    packages = architecture.get("packages")
    if not isinstance(packages, list) or not packages:
        errors.append("Issue Architecture requires at least one package")
        packages = []
    package_fields = {"package_id", "title", "purpose", "primary_candidate_ids", "supporting_candidate_ids", "must_cover_requirements", "boundaries", "drafting_order", "profile_extensions", "publication_extensions"}
    for index, package in enumerate(packages):
        prefix = f"packages[{index}]"
        if not isinstance(package, dict) or set(package) != package_fields:
            errors.append(f"{prefix} fields invalid")
            continue
        package_id = package.get("package_id")
        if _nonempty(package_id):
            package_ids.append(package_id)
        else:
            errors.append(f"{prefix}.package_id required")
        if not _nonempty(package.get("title")) or not _nonempty(package.get("purpose")):
            errors.append(f"{prefix} title/purpose required")
        order = package.get("drafting_order")
        if isinstance(order, int) and not isinstance(order, bool) and order > 0:
            orders.append(order)
        else:
            errors.append(f"{prefix}.drafting_order invalid")
        for key in ("primary_candidate_ids", "supporting_candidate_ids", "must_cover_requirements", "boundaries"):
            values = package.get(key)
            if not isinstance(values, list) or len(values) != len(set(values)) or any(not _nonempty(value) for value in values):
                errors.append(f"{prefix}.{key} must be a unique string array")
        if not isinstance(package.get("profile_extensions"), dict) or not isinstance(package.get("publication_extensions"), dict):
            errors.append(f"{prefix} extensions must be objects")
        primaries = package.get("primary_candidate_ids") if isinstance(package.get("primary_candidate_ids"), list) else []
        supports = package.get("supporting_candidate_ids") if isinstance(package.get("supporting_candidate_ids"), list) else []
        if set(primaries) & set(supports):
            errors.append(f"{prefix}: same candidate cannot be primary and supporting")
        for cid, kind in [(value, "PRIMARY") for value in primaries] + [(value, "SUPPORTING") for value in supports]:
            if cid in nonselected:
                errors.append(f"{prefix}: non-selected candidate used: {cid}")
                continue
            if cid not in selected:
                errors.append(f"{prefix}: unknown selected candidate: {cid}")
                continue
            if selected[cid]["architecture_usage"] != kind:
                errors.append(f"{prefix}: {kind} placement conflicts with Selection usage for {cid}")
                continue
            (primary if kind == "PRIMARY" else supporting)[cid].append(package_id or prefix)
            missing = [value for value in matrix_by_id[cid]["remaining_boundaries"] if value not in set(package.get("boundaries") or [])]
            if missing:
                errors.append(f"{prefix}: missing Evidence boundaries for {cid}: {missing}")
    if len(package_ids) != len(set(package_ids)):
        errors.append("Issue Architecture package_id values must be unique")
    if len(orders) != len(set(orders)):
        errors.append("Issue Architecture drafting_order values must be unique")

    exception_by_id: dict[str, dict[str, Any]] = {}
    exceptions = architecture.get("selected_exceptions")
    if not isinstance(exceptions, list):
        errors.append("selected_exceptions must be an array")
        exceptions = []
    for item in exceptions:
        if not isinstance(item, dict) or set(item) != {"candidate_id", "reason", "exception_kind"}:
            errors.append("selected exception fields invalid")
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
        if primary.get(cid) or supporting.get(cid):
            errors.append(f"selected candidate cannot have placement and exception: {cid}")
    for cid, assignment in selected.items():
        if cid in exception_by_id:
            continue
        if assignment["architecture_usage"] == "PRIMARY" and len(primary.get(cid, [])) != 1:
            errors.append(f"selected PRIMARY candidate requires exactly one Architecture destination: {cid} count={len(primary.get(cid, []))}")
        if assignment["architecture_usage"] == "SUPPORTING" and not supporting.get(cid):
            errors.append(f"selected SUPPORTING candidate requires at least one Architecture destination: {cid}")

    status = architecture.get("status")
    review = architecture.get("human_review")
    if status not in {"PROPOSED", "APPROVED"}:
        errors.append("Issue Architecture status invalid")
    if not isinstance(review, dict) or set(review) != {"reviewed_by", "reviewed_at", "review_reference"}:
        errors.append("Issue Architecture human_review fields invalid")
        review = {}
    if status == "APPROVED":
        for key in ("reviewed_by", "reviewed_at", "review_reference"):
            if not _nonempty(review.get(key)):
                errors.append(f"APPROVED Architecture requires human_review.{key}")
        if _nonempty(review.get("reviewed_at")) and not _aware_datetime(review["reviewed_at"]):
            errors.append("human_review.reviewed_at must be timezone-aware ISO-8601")
    elif any(review.get(key) is not None for key in ("reviewed_by", "reviewed_at", "review_reference")):
        errors.append("PROPOSED Architecture must not contain completed Human Review metadata")
    if require_approved and status != "APPROVED":
        errors.append("Issue Architecture must be APPROVED after Architecture Review")
    return errors


def build_architecture_review_summary(
    repo_root: Path, profile_path: Path, discovery_path: Path, screening_path: Path,
    evidence_path: Path, views_path: Path, ledger_path: Path, completeness_path: Path,
    matrix_path: Path, selection_path: Path, architecture_path: Path, implementation_sha: str,
) -> dict[str, Any]:
    up = _load_upstream(
        repo_root, profile_path, discovery_path, screening_path, evidence_path,
        views_path, ledger_path, completeness_path, implementation_sha,
    )
    matrix = core.load_json(matrix_path)
    selection = core.load_json(selection_path)
    plan = core.load_json(architecture_path)
    errors = validate_candidate_matrix(
        matrix, repo_root, profile_path, discovery_path, screening_path, evidence_path,
        views_path, ledger_path, completeness_path, implementation_sha,
    )
    errors += validate_selection(selection, matrix_path, completeness_path, ledger_path)
    errors += validate_architecture(plan, profile_path, completeness_path, ledger_path, matrix_path, selection_path)
    if up["completeness"]["overall_status"] == "INCOMPLETE":
        errors.append("Profile Completeness is INCOMPLETE; Architecture Review is not ready")

    matrix_by_id = {row["candidate_id"]: row for row in matrix.get("rows", [])}
    selection_by_id = {row["candidate_id"]: row for row in selection.get("assignments", []) if isinstance(row, dict)}
    primary: dict[str, list[str]] = defaultdict(list)
    supporting: dict[str, list[str]] = defaultdict(list)
    for package in plan.get("packages", []):
        if not isinstance(package, dict):
            continue
        for cid in package.get("primary_candidate_ids", []):
            primary[cid].append(package.get("package_id"))
        for cid in package.get("supporting_candidate_ids", []):
            supporting[cid].append(package.get("package_id"))
    exceptions = {row["candidate_id"]: row for row in plan.get("selected_exceptions", []) if isinstance(row, dict) and row.get("candidate_id")}
    major: list[dict[str, Any]] = []
    for cid, row in sorted(matrix_by_id.items()):
        if row["materiality"] not in MATERIAL_REVIEW:
            continue
        assignment = selection_by_id.get(cid)
        disposition = assignment.get("disposition") if assignment else "INSPECT"
        if primary.get(cid):
            kind, destinations, reason = "PRIMARY", sorted(primary[cid]), None
        elif supporting.get(cid):
            kind, destinations, reason = "SUPPORTING", sorted(supporting[cid]), None
        elif cid in exceptions:
            kind, destinations, reason = "EXCEPTION", [], exceptions[cid].get("reason")
        else:
            kind, destinations = "NOT_SELECTED", []
            reason = assignment.get("rationale") if assignment else "Selection assignment missing"
        major.append({
            "candidate_id": cid,
            "title": row["title"],
            "materiality": row["materiality"],
            "selection_disposition": disposition,
            "destination_kind": kind,
            "destinations": destinations,
            "exception_reason": reason,
        })
    obligations = up["completeness"]["obligations"]
    return {
        "schema_version": "2.0-rc1",
        "issue_id": up["profile"]["issue_id"],
        "research_profile": up["profile"]["research_profile"],
        "basis": {
            "architecture_sha256": core.sha256_file(architecture_path),
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
        },
        "readiness": {"status": "READY_FOR_ARCHITECTURE_REVIEW" if not errors else "BLOCKED", "errors": errors},
        "discovery": {"total": len(up["discoveries"]), "counts": _counter([row["provenance"]["origin"] for row in up["discoveries"]])},
        "screening": {"total": len(up["screening"]["decisions"]), "counts": _counter([row["decision"] for row in up["screening"]["decisions"]])},
        "evidence": {"total": len(up["evidence"]["results"]), "counts": _counter([row["status"] for row in up["evidence"]["results"]])},
        "materiality": {"total": len(up["ledger"]["rows"]), "counts": _counter([row["downstream_disposition"] for row in up["ledger"]["rows"]])},
        "selection": {"total": len(selection.get("assignments", [])), "counts": _counter([row["disposition"] for row in selection.get("assignments", []) if isinstance(row, dict) and row.get("disposition") in DISPOSITIONS])},
        "completeness": {"overall_status": up["completeness"]["overall_status"], "obligation_counts": _counter([row["status"] for row in obligations])},
        "major_material_destinations": major,
        "residual_limitations": list(up["completeness"]["residual_limitations"]),
        "architecture": {
            "status": plan.get("status"),
            "editorial_thesis": plan.get("editorial_thesis"),
            "package_count": len(plan.get("packages", [])),
            "packages": [row.get("title") for row in plan.get("packages", []) if isinstance(row, dict) and _nonempty(row.get("title"))],
            "page_plan": plan.get("page_plan"),
        },
    }


def _path(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--implementation-sha")
    sub = parser.add_subparsers(dest="command", required=True)
    matrix = sub.add_parser("matrix")
    for key in ("profile", "discovery", "screening", "evidence", "views", "ledger", "completeness", "output"):
        matrix.add_argument(f"--{key}", required=True)
    selection = sub.add_parser("selection-check")
    for key in ("selection", "matrix", "completeness", "ledger"):
        selection.add_argument(f"--{key}", required=True)
    plan = sub.add_parser("architecture-check")
    for key in ("architecture", "profile", "completeness", "ledger", "matrix", "selection"):
        plan.add_argument(f"--{key}", required=True)
    plan.add_argument("--require-approved", action="store_true")
    review = sub.add_parser("review-summary")
    for key in ("profile", "discovery", "screening", "evidence", "views", "ledger", "completeness", "matrix", "selection", "architecture", "output"):
        review.add_argument(f"--{key}", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.repo_root).resolve()
    impl = core.repository_commit_sha(root, args.implementation_sha)
    try:
        if args.command == "matrix":
            payload = derive_candidate_matrix(
                root, _path(root, args.profile), _path(root, args.discovery), _path(root, args.screening),
                _path(root, args.evidence), _path(root, args.views), _path(root, args.ledger),
                _path(root, args.completeness), impl,
            )
            write_candidate_matrix(_path(root, args.output), payload)
            return 0
        if args.command == "selection-check":
            errors = validate_selection(core.load_json(_path(root, args.selection)), _path(root, args.matrix), _path(root, args.completeness), _path(root, args.ledger))
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        if args.command == "architecture-check":
            errors = validate_architecture(core.load_json(_path(root, args.architecture)), _path(root, args.profile), _path(root, args.completeness), _path(root, args.ledger), _path(root, args.matrix), _path(root, args.selection), args.require_approved)
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        if args.command == "review-summary":
            payload = build_architecture_review_summary(
                root, _path(root, args.profile), _path(root, args.discovery), _path(root, args.screening),
                _path(root, args.evidence), _path(root, args.views), _path(root, args.ledger), _path(root, args.completeness),
                _path(root, args.matrix), _path(root, args.selection), _path(root, args.architecture), impl,
            )
            output = _path(root, args.output)
            if output.exists():
                raise ValueError(f"refusing to overwrite Architecture Review Summary: {output}")
            core.write_json(output, payload)
            return 0 if payload["readiness"]["status"] == "READY_FOR_ARCHITECTURE_REVIEW" else 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
