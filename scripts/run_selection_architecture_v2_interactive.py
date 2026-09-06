#!/usr/bin/env python3
"""Build Core v2 Candidate Selection and proposed Architecture from explicit interactive decisions.

The runner is profile-neutral. Candidate identities and the Candidate Matrix are derived from
accepted Evidence/View/Materiality/Completeness artifacts by the canonical implementation.
Interactive input addresses candidates by Discovery ID for operator ergonomics; every ID is
resolved to the deterministic Matrix candidate before Selection/Architecture validation.

This runner does not advance Production State and never records Human Gate approval.
"""
from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2 as architecture
from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening

INPUT_NAME = "interactive-selection-architecture.json"


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve()))


def _unique_strings(value: Any, label: str, *, allow_empty: bool = True) -> list[str]:
    if not isinstance(value, list) or (not allow_empty and not value) or any(not _nonempty(x) for x in value):
        raise ValueError(f"{label} must be a {'non-empty ' if not allow_empty else ''}string array")
    if len(value) != len(set(value)):
        raise ValueError(f"{label} must not contain duplicates")
    return list(value)


def _validate_input(doc: dict[str, Any], issue_id: str, expected_discovery_ids: set[str]) -> None:
    required = {
        "schema_version", "issue_id", "runner", "assignments", "architecture",
    }
    if not isinstance(doc, dict) or set(doc) != required:
        raise ValueError("interactive Selection/Architecture fields invalid")
    if doc.get("schema_version") != "2.0-rc1" or doc.get("issue_id") != issue_id:
        raise ValueError("interactive Selection/Architecture identity mismatch")
    runner = doc.get("runner")
    if not isinstance(runner, dict) or not all(_nonempty(runner.get(k)) for k in ("provider", "model", "invocation", "generated_at")):
        raise ValueError("interactive Selection/Architecture runner metadata invalid")
    assignments = doc.get("assignments")
    if not isinstance(assignments, list):
        raise ValueError("interactive assignments must be an array")
    ids: list[str] = []
    fields = {
        "discovery_id", "disposition", "rationale", "architecture_usage",
        "publication_role", "architecture_role", "profile_extensions",
    }
    for index, row in enumerate(assignments):
        if not isinstance(row, dict) or set(row) != fields:
            raise ValueError(f"interactive assignments[{index}] fields invalid")
        did = row.get("discovery_id")
        if did not in expected_discovery_ids:
            raise ValueError(f"interactive assignments[{index}] unknown Discovery ID: {did}")
        ids.append(did)
        if row.get("disposition") not in {"SELECTED", "HOLD", "REJECT", "INSPECT"}:
            raise ValueError(f"interactive assignments[{index}] disposition invalid")
        if row.get("architecture_usage") not in {"PRIMARY", "SUPPORTING", "NONE"}:
            raise ValueError(f"interactive assignments[{index}] architecture_usage invalid")
        if not _nonempty(row.get("rationale")) or not isinstance(row.get("profile_extensions"), dict):
            raise ValueError(f"interactive assignments[{index}] rationale/extensions invalid")
        for key in ("publication_role", "architecture_role"):
            if row.get(key) is not None and not _nonempty(row.get(key)):
                raise ValueError(f"interactive assignments[{index}] {key} invalid")
    if len(ids) != len(set(ids)) or set(ids) != expected_discovery_ids:
        raise ValueError("interactive assignments must cover every Matrix Discovery exactly once")

    plan = doc.get("architecture")
    if not isinstance(plan, dict) or set(plan) != {
        "editorial_thesis", "architecture_goals", "page_plan", "packages",
        "selected_exceptions", "profile_extensions", "publication_extensions",
    }:
        raise ValueError("interactive architecture fields invalid")
    if not _nonempty(plan.get("editorial_thesis")):
        raise ValueError("interactive architecture editorial_thesis required")
    _unique_strings(plan.get("architecture_goals"), "architecture_goals", allow_empty=False)
    page = plan.get("page_plan")
    if not isinstance(page, dict) or set(page) != {"target_pages", "max_pages", "notes"}:
        raise ValueError("interactive page_plan fields invalid")
    for key in ("target_pages", "max_pages"):
        value = page.get(key)
        if value is not None and (not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0):
            raise ValueError(f"interactive page_plan.{key} invalid")
    if page.get("notes") is not None and not _nonempty(page.get("notes")):
        raise ValueError("interactive page_plan.notes invalid")
    packages = plan.get("packages")
    if not isinstance(packages, list) or not packages:
        raise ValueError("interactive architecture requires packages")
    package_ids: list[str] = []
    package_fields = {
        "package_id", "title", "purpose", "primary_discovery_ids", "supporting_discovery_ids",
        "must_cover_requirements", "boundaries", "drafting_order", "profile_extensions", "publication_extensions",
    }
    for index, package in enumerate(packages):
        if not isinstance(package, dict) or set(package) != package_fields:
            raise ValueError(f"interactive packages[{index}] fields invalid")
        if not all(_nonempty(package.get(k)) for k in ("package_id", "title", "purpose")):
            raise ValueError(f"interactive packages[{index}] identity/title/purpose invalid")
        package_ids.append(package["package_id"])
        for key in ("primary_discovery_ids", "supporting_discovery_ids", "must_cover_requirements", "boundaries"):
            values = _unique_strings(package.get(key), f"packages[{index}].{key}")
            if key.endswith("discovery_ids") and any(x not in expected_discovery_ids for x in values):
                raise ValueError(f"interactive packages[{index}] references unknown Discovery")
        if set(package["primary_discovery_ids"]) & set(package["supporting_discovery_ids"]):
            raise ValueError(f"interactive packages[{index}] duplicates primary/supporting Discovery")
        order = package.get("drafting_order")
        if not isinstance(order, int) or isinstance(order, bool) or order < 1:
            raise ValueError(f"interactive packages[{index}] drafting_order invalid")
        if not isinstance(package.get("profile_extensions"), dict) or not isinstance(package.get("publication_extensions"), dict):
            raise ValueError(f"interactive packages[{index}] extensions invalid")
    if len(package_ids) != len(set(package_ids)):
        raise ValueError("interactive package_id values must be unique")
    exceptions = plan.get("selected_exceptions")
    if not isinstance(exceptions, list):
        raise ValueError("interactive selected_exceptions must be an array")
    for index, item in enumerate(exceptions):
        if not isinstance(item, dict) or set(item) != {"discovery_id", "reason", "exception_kind"}:
            raise ValueError(f"interactive selected_exceptions[{index}] fields invalid")
        if item.get("discovery_id") not in expected_discovery_ids or not _nonempty(item.get("reason")):
            raise ValueError(f"interactive selected_exceptions[{index}] identity/reason invalid")
        if item.get("exception_kind") not in {"OMITTED_FROM_ARCHITECTURE", "DEFERRED", "STRUCTURAL_EXCEPTION"}:
            raise ValueError(f"interactive selected_exceptions[{index}] kind invalid")
    if not isinstance(plan.get("profile_extensions"), dict) or not isinstance(plan.get("publication_extensions"), dict):
        raise ValueError("interactive architecture extensions invalid")


def _matrix_discovery_map(matrix: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in matrix["rows"]:
        ids = row.get("discovery_ids")
        if not isinstance(ids, list) or len(ids) != 1:
            raise ValueError("interactive Selection/Architecture requires one Discovery per Matrix candidate")
        did = ids[0]
        if did in result:
            raise ValueError(f"Matrix maps Discovery more than once: {did}")
        result[did] = row
    return result


def run(repo_root: Path, state_path: Path, input_path: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    state_path = state_path.resolve()
    input_path = input_path.resolve()
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before Selection/Architecture: " + "; ".join(errors))
    if state.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("interactive Selection/Architecture requires EVIDENCE_REVIEWED Production State")

    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    discovery_acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
    accepted_discovery = discovery.validate_acceptance(repo_root, discovery_acceptance_path)
    root_discovery_path = core.repo_local_path(repo_root, accepted_discovery["discovery_path"], "accepted Discovery JSONL")
    ledger_path = source_root / "materiality-ledger-v2.json"
    completeness_path = source_root / "profile-completeness-v2.json"
    implementation_sha = core.repository_commit_sha(repo_root)
    active_evidence_views = agent.resolve_active_evidence_views(repo_root, cfg, state)
    evidence_path = active_evidence_views["evidence_path"]
    views_path = active_evidence_views["views_path"]
    screening_path = screening.resolve_active_screening_acceptance(
        repo_root, state_path, implementation_sha
    )["path"]
    effective = screening.resolve_effective_discovery_basis(
        repo_root,
        screening_path.parent / "package.json",
        implementation_sha,
        accepted_root_path=root_discovery_path,
    )
    discovery_path = effective["path"]

    matrix_path = source_root / "candidate-matrix-v2.json"
    selection_path = source_root / "candidate-selection-v2.json"
    architecture_path = source_root / "architecture-v2.json"
    review_path = source_root / "architecture-review-summary-v2.json"
    attention_path = source_root / "architecture-review-attention-v2.json"
    archive_path = source_root / "orchestration/v2/interactive/selection-architecture-input.json"
    for path in (matrix_path, selection_path, architecture_path, review_path, attention_path, archive_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite Selection/Architecture artifact: {path}")

    with agent_tool.current_stage_basis_override():
        matrix = architecture.derive_candidate_matrix(
            repo_root, profile_path, discovery_path, screening_path, evidence_path,
            views_path, ledger_path, completeness_path, implementation_sha,
        )
    schema_gate.validate_instance(matrix, repo_root / architecture.MATRIX_SCHEMA, label="Candidate Matrix")
    architecture.write_candidate_matrix(matrix_path, matrix)
    matrix_by_discovery = _matrix_discovery_map(matrix)

    interactive = core.load_json(input_path)
    _validate_input(interactive, state["issue_id"], set(matrix_by_discovery))
    assignment_input = {row["discovery_id"]: row for row in interactive["assignments"]}
    assignments: list[dict[str, Any]] = []
    for did in sorted(matrix_by_discovery):
        src = assignment_input[did]
        assignments.append({
            "candidate_id": matrix_by_discovery[did]["candidate_id"],
            "disposition": src["disposition"],
            "rationale": src["rationale"],
            "architecture_usage": src["architecture_usage"],
            "publication_role": src["publication_role"],
            "architecture_role": src["architecture_role"],
            "profile_extensions": src["profile_extensions"],
        })
    dispositions = [row["disposition"] for row in assignments]
    selection = {
        "schema_version": "2.0-rc1",
        "issue_id": state["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "selection_version": "interactive-v2-1",
        "status": "ESTABLISHED",
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        },
        "assignments": assignments,
        "summary": {
            "candidate_count": len(assignments),
            "disposition_counts": dict(sorted(Counter(dispositions).items())),
            "selected_count": sum(value == "SELECTED" for value in dispositions),
        },
    }
    schema_gate.validate_instance(selection, repo_root / architecture.SELECTION_SCHEMA, label="Candidate Selection")
    errors = architecture.validate_selection(repo_root, selection, profile_path, matrix_path, completeness_path, ledger_path)
    if errors:
        raise ValueError("Candidate Selection invalid: " + "; ".join(errors))
    core.write_json(selection_path, selection)

    candidate_id = {did: row["candidate_id"] for did, row in matrix_by_discovery.items()}
    plan_input = interactive["architecture"]
    packages: list[dict[str, Any]] = []
    for src in plan_input["packages"]:
        primary_ids = [candidate_id[x] for x in src["primary_discovery_ids"]]
        supporting_ids = [candidate_id[x] for x in src["supporting_discovery_ids"]]
        inherited = [
            boundary
            for cid in [*primary_ids, *supporting_ids]
            for boundary in next(row for row in matrix["rows"] if row["candidate_id"] == cid)["remaining_boundaries"]
        ]
        boundaries = list(dict.fromkeys([*src["boundaries"], *inherited]))
        packages.append({
            "package_id": src["package_id"],
            "title": src["title"],
            "purpose": src["purpose"],
            "primary_candidate_ids": primary_ids,
            "supporting_candidate_ids": supporting_ids,
            "must_cover_requirements": list(src["must_cover_requirements"]),
            "boundaries": boundaries,
            "drafting_order": src["drafting_order"],
            "profile_extensions": src["profile_extensions"],
            "publication_extensions": src["publication_extensions"],
        })
    exceptions = [
        {
            "candidate_id": candidate_id[row["discovery_id"]],
            "reason": row["reason"],
            "exception_kind": row["exception_kind"],
        }
        for row in plan_input["selected_exceptions"]
    ]
    proposed = {
        "schema_version": "2.0-rc1",
        "issue_id": state["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "status": "PROPOSED",
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
        },
        "editorial_thesis": plan_input["editorial_thesis"],
        "architecture_goals": list(plan_input["architecture_goals"]),
        "page_plan": dict(plan_input["page_plan"]),
        "packages": packages,
        "selected_exceptions": exceptions,
        "profile_extensions": plan_input["profile_extensions"],
        "publication_extensions": plan_input["publication_extensions"],
        "human_review": {"reviewed_by": None, "reviewed_at": None, "review_reference": None},
    }
    schema_gate.validate_instance(proposed, repo_root / architecture.ARCHITECTURE_SCHEMA, label="Issue Architecture")
    errors = architecture.validate_architecture(
        repo_root, proposed, profile_path, completeness_path, ledger_path, matrix_path, selection_path, require_approved=False
    )
    if errors:
        raise ValueError("Issue Architecture invalid: " + "; ".join(errors))
    core.write_json(architecture_path, proposed)

    with agent_tool.current_stage_basis_override():
        review = architecture.build_architecture_review_summary(
            repo_root, profile_path, discovery_path, screening_path, evidence_path, views_path,
            ledger_path, completeness_path, matrix_path, selection_path, architecture_path, implementation_sha,
        )
    if review.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise ValueError("Architecture Review Summary is BLOCKED: " + "; ".join(review.get("readiness", {}).get("errors", [])))
    schema_gate.validate_instance(review, repo_root / architecture.REVIEW_SCHEMA, label="Architecture Review Summary")
    core.write_json(review_path, review)
    review_attention.build_attention(repo_root, screening_path, ledger_path, selection_path, attention_path)
    review_attention.validate_attention(repo_root, attention_path)

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(input_path, archive_path)
    audit_path = archive_path.parent / "selection-architecture-audit.json"
    core.write_json(audit_path, {
        "schema_version": "2.0-rc1",
        "issue_id": state["issue_id"],
        "interactive_input": {"path": _rel(repo_root, archive_path), "sha256": core.sha256_file(archive_path)},
        "runner": interactive["runner"],
        "outputs": {
            "candidate_matrix": {"path": _rel(repo_root, matrix_path), "sha256": core.sha256_file(matrix_path)},
            "candidate_selection": {"path": _rel(repo_root, selection_path), "sha256": core.sha256_file(selection_path)},
            "issue_architecture": {"path": _rel(repo_root, architecture_path), "sha256": core.sha256_file(architecture_path)},
            "architecture_review_summary": {"path": _rel(repo_root, review_path), "sha256": core.sha256_file(review_path)},
            "architecture_review_attention": {"path": _rel(repo_root, attention_path), "sha256": core.sha256_file(attention_path)},
        },
    })
    return {
        "candidate_matrix": _rel(repo_root, matrix_path),
        "candidate_selection": _rel(repo_root, selection_path),
        "issue_architecture": _rel(repo_root, architecture_path),
        "architecture_review_summary": _rel(repo_root, review_path),
        "architecture_review_attention": _rel(repo_root, attention_path),
        "selected_count": selection["summary"]["selected_count"],
        "architecture_package_count": len(packages),
        "review_readiness": review["readiness"]["status"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--state", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    state = Path(args.state)
    input_path = Path(args.input)
    if not state.is_absolute(): state = root / state
    if not input_path.is_absolute(): input_path = root / input_path
    try:
        print(json.dumps(run(root, state, input_path), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=__import__("sys").stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
