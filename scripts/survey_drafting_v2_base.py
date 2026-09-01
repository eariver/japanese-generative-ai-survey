#!/usr/bin/env python3
"""Profile-neutral Drafting and Profile Synthesis for Survey Production Core v2.

WU-009 consumes an independent Architecture Approval Record. WU-010 owns
creating that record and advancing Human Gate state; this module validates the
exact reviewed-byte authorization and preserves the Matrix/Evidence provenance
chain through Drafting and Synthesis.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import survey_architecture_v2 as architecture
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

APPROVAL_SCHEMA = Path("schemas/architecture-approval-record-v2.schema.json")
DRAFT_PACKAGE_SCHEMA = Path("schemas/draft-v2-package.schema.json")
DRAFT_RESULT_SCHEMA = Path("schemas/draft-v2-result.schema.json")
SYNTHESIS_INPUT_SCHEMA = Path("schemas/profile-synthesis-v2-input.schema.json")
SYNTHESIS_RESULT_SCHEMA = Path("schemas/profile-synthesis-v2-result.schema.json")
DRAFT_PROMPT = Path("config/prompts/article-drafting-v2.md")
SYNTHESIS_PROMPT = Path("config/prompts/profile-synthesis-v2.md")

DRAFT_PACKAGE_FIELDS = {
    "schema_version", "issue_id", "research_profile", "publication_profile",
    "package_id", "basis", "package", "candidate_matrix",
    "evidence_acceptance", "evidence_inputs", "drafting_constraints",
    "profile_extensions", "publication_extensions",
}
DRAFT_RESULT_FIELDS = {
    "schema_version", "issue_id", "research_profile", "publication_profile",
    "package_id", "draft_version", "status", "basis", "runner", "headline",
    "deck", "deck_attribution_mode", "deck_evidence_refs", "blocks",
    "must_cover_coverage", "boundary_dispositions", "profile_extensions",
    "publication_extensions",
}
APPROVAL_FIELDS = {
    "schema_version", "approval_id", "issue_id", "gate", "decision",
    "architecture_sha256", "architecture_review_summary_sha256",
    "architecture_review_attention_sha256", "reviewed_by",
    "reviewed_at", "review_reference",
}
ATTRIBUTION_MODES = {"NONE", "FACTUAL", "ATTRIBUTED", "SOCIAL", "INFERENCE", "MIXED"}
BLOCK_TYPES = {"HEADING", "PARAGRAPH", "BULLET_LIST", "TABLE", "CLAIM_BOUNDARY", "NOTE"}
SUBJECT_ROLES = {"PRIMARY_SUBJECT", "COMPARATOR", "RELATED"}
REF_KINDS = {"EVENT", "CLAIM", "METRIC", "LIMITATION"}
BOUNDARY_HANDLING = {"EXPLICITLY_STATED", "RESPECTED_BY_OMISSION"}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _aware(value: Any) -> bool:
    if not _nonempty(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _payload_value_present(value: Any) -> bool:
    """Require an explicit value without inventing cross-Profile emptiness rules.

    Empty arrays can be semantically meaningful for Profile-owned fields such as
    unresolved questions, so the generic Core only rejects null/blank strings.
    """
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return True


def _object_sha(value: Any) -> str:
    """SHA of the canonical bytes produced by core.write_json/json_bytes."""
    return core.sha256_bytes(core.json_bytes(value))


def _require_contracts(repo_root: Path) -> None:
    for rel in (
        APPROVAL_SCHEMA,
        DRAFT_PACKAGE_SCHEMA,
        DRAFT_RESULT_SCHEMA,
        SYNTHESIS_INPUT_SCHEMA,
        SYNTHESIS_RESULT_SCHEMA,
        DRAFT_PROMPT,
        SYNTHESIS_PROMPT,
    ):
        if not (repo_root / rel).is_file():
            raise ValueError(f"WU-009 contract file missing: {rel}")


def validate_architecture_approval(
    approval: dict[str, Any],
    architecture_path: Path,
    review_summary_path: Path,
    expected_issue_id: str,
) -> list[str]:
    errors: list[str] = []
    if set(approval) != APPROVAL_FIELDS:
        return ["Architecture Approval Record fields must exactly match v2 contract"]
    if approval.get("schema_version") != "2.0-rc1":
        errors.append("Architecture Approval Record schema_version mismatch")
    if approval.get("issue_id") != expected_issue_id:
        errors.append("Architecture Approval Record issue identity mismatch")
    if approval.get("gate") != "ARCHITECTURE_REVIEW" or approval.get("decision") != "APPROVED":
        errors.append("Architecture Approval Record must authorize ARCHITECTURE_REVIEW")
    if approval.get("architecture_sha256") != core.sha256_file(architecture_path):
        errors.append("Architecture Approval Record does not bind exact Architecture bytes")
    if approval.get("architecture_review_summary_sha256") != core.sha256_file(review_summary_path):
        errors.append("Architecture Approval Record does not bind exact Review Summary bytes")
    attention_path = architecture_path.parent / "architecture-review-attention-v2.json"
    if not attention_path.is_file():
        errors.append("Architecture Approval Record requires canonical Review Attention bytes")
    elif approval.get("architecture_review_attention_sha256") != core.sha256_file(attention_path):
        errors.append("Architecture Approval Record does not bind exact Review Attention bytes")
    for key in ("approval_id", "reviewed_by", "review_reference"):
        if not _nonempty(approval.get(key)):
            errors.append(f"Architecture Approval Record {key} required")
    if not _aware(approval.get("reviewed_at")):
        errors.append("Architecture Approval Record reviewed_at must be timezone-aware ISO-8601")
    return errors


def _load_drafting_basis(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_path: Path,
    evidence_path: Path,
    views_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    matrix_path: Path,
    selection_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
    implementation_sha: str,
) -> dict[str, Any]:
    _require_contracts(repo_root)
    profile = core.load_json(profile_path)
    matrix = core.load_json(matrix_path)
    selection = core.load_json(selection_path)
    plan = core.load_json(architecture_path)
    review = core.load_json(review_summary_path)
    approval = core.load_json(approval_path)

    errors = architecture.validate_candidate_matrix(
        matrix,
        repo_root,
        profile_path,
        discovery_path,
        screening_path,
        evidence_path,
        views_path,
        ledger_path,
        completeness_path,
        implementation_sha,
    )
    errors += architecture.validate_selection(
        repo_root, selection, profile_path, matrix_path, completeness_path, ledger_path
    )
    errors += architecture.validate_architecture(
        repo_root,
        plan,
        profile_path,
        completeness_path,
        ledger_path,
        matrix_path,
        selection_path,
        require_approved=False,
    )
    if errors:
        raise ValueError("WU-009 upstream Architecture basis invalid: " + "; ".join(errors))
    if plan.get("status") != "PROPOSED":
        raise ValueError("WU-009 requires immutable PROPOSED Architecture bytes plus separate Approval Record")
    if review.get("issue_id") != profile["issue_id"] or review.get("research_profile") != profile["research_profile"]:
        raise ValueError("Architecture Review Summary/Profile identity mismatch")
    if review.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise ValueError("Architecture Review Summary was not ready for Human Gate")
    if review.get("basis", {}).get("architecture_sha256") != core.sha256_file(architecture_path):
        raise ValueError("Architecture Review Summary does not bind exact Architecture bytes")
    approval_errors = validate_architecture_approval(
        approval, architecture_path, review_summary_path, profile["issue_id"]
    )
    if approval_errors:
        raise ValueError("Architecture Approval Record invalid: " + "; ".join(approval_errors))

    evidence_acceptance, _ = evidence.validate_evidence_acceptance(
        repo_root, evidence_path, implementation_sha
    )
    if evidence_acceptance.get("issue_id") != profile["issue_id"]:
        raise ValueError("Evidence acceptance/Profile identity mismatch")
    return {
        "profile": profile,
        "matrix": matrix,
        "selection": selection,
        "architecture": plan,
        "review": review,
        "approval": approval,
        "evidence": evidence_acceptance,
    }


def derive_draft_package(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_path: Path,
    evidence_path: Path,
    views_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    matrix_path: Path,
    selection_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
    package_id: str,
    implementation_sha: str,
) -> dict[str, Any]:
    upstream = _load_drafting_basis(
        repo_root, profile_path, discovery_path, screening_path, evidence_path,
        views_path, ledger_path, completeness_path, matrix_path, selection_path,
        architecture_path, review_summary_path, approval_path, implementation_sha,
    )
    profile = upstream["profile"]
    matrix = upstream["matrix"]
    plan = upstream["architecture"]
    evidence_acceptance = upstream["evidence"]
    packages = [row for row in plan["packages"] if row["package_id"] == package_id]
    if len(packages) != 1:
        raise ValueError(f"Draft package_id must resolve exactly once in Architecture: {package_id}")
    plan_package = packages[0]
    matrix_by_id = {row["candidate_id"]: row for row in matrix["rows"]}
    evidence_by_task = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}

    inputs: list[dict[str, Any]] = []
    placements = [
        *[(cid, "PRIMARY") for cid in plan_package["primary_candidate_ids"]],
        *[(cid, "SUPPORTING") for cid in plan_package["supporting_candidate_ids"]],
    ]
    for candidate_id, usage in placements:
        row = matrix_by_id.get(candidate_id)
        if row is None:
            raise ValueError(f"Architecture Draft package references unknown Matrix candidate: {candidate_id}")
        task_id = row["evidence_task_id"]
        result_meta = evidence_by_task.get(task_id)
        if result_meta is None or result_meta["sha256"] != row["evidence_sha256"]:
            raise ValueError(f"Draft Evidence/Matrix identity mismatch: {task_id}")
        card_path = evidence_path.parent / "results" / result_meta["filename"]
        if core.sha256_file(card_path) != result_meta["sha256"]:
            raise ValueError(f"Draft Evidence bytes changed: {task_id}")
        inputs.append({
            "candidate_id": candidate_id,
            "architecture_usage": usage,
            "evidence_task_id": task_id,
            "evidence_sha256": result_meta["sha256"],
            "evidence_card": core.load_json(card_path),
        })
    if not inputs:
        raise ValueError(f"Architecture package has no factual Evidence inputs: {package_id}")
    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "package_id": package_id,
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "architecture_sha256": core.sha256_file(architecture_path),
            "architecture_review_summary_sha256": core.sha256_file(review_summary_path),
            "architecture_approval_sha256": core.sha256_file(approval_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
            "evidence_acceptance_sha256": core.sha256_file(evidence_path),
        },
        "package": {
            "title": plan_package["title"],
            "purpose": plan_package["purpose"],
            "drafting_order": plan_package["drafting_order"],
            "primary_candidate_ids": list(plan_package["primary_candidate_ids"]),
            "supporting_candidate_ids": list(plan_package["supporting_candidate_ids"]),
            "must_cover_requirements": list(plan_package["must_cover_requirements"]),
            "boundaries": list(plan_package["boundaries"]),
        },
        "candidate_matrix": matrix,
        "evidence_acceptance": evidence_acceptance,
        "evidence_inputs": inputs,
        "drafting_constraints": {
            "language": "ja",
            "raw_sources_forbidden": True,
            "unknowns_remain_unknown": True,
            "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
        },
        "profile_extensions": dict(plan_package["profile_extensions"]),
        "publication_extensions": dict(plan_package["publication_extensions"]),
    }


def validate_draft_package(package: dict[str, Any], *derive_args: Any) -> list[str]:
    try:
        expected = derive_draft_package(*derive_args)
    except ValueError as exc:
        return [str(exc)]
    return [] if package == expected else ["Draft Package does not exactly match authorized Architecture/Evidence derivation"]


def validate_self_contained_draft_package(
    package: dict[str, Any],
    profile_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
) -> list[str]:
    """Reconstruct the Draft provenance chain without mutable upstream work dirs."""
    errors: list[str] = []
    if set(package) != DRAFT_PACKAGE_FIELDS:
        return ["Draft Package fields must exactly match self-contained v2 contract"]
    profile = core.load_json(profile_path)
    plan = core.load_json(architecture_path)
    approval = core.load_json(approval_path)
    errors += validate_architecture_approval(
        approval, architecture_path, review_summary_path, profile["issue_id"]
    )
    for key in ("issue_id", "research_profile", "publication_profile"):
        if package.get(key) != profile.get(key):
            errors.append(f"Draft Package {key} does not match Production Profile")
    if package.get("schema_version") != "2.0-rc1":
        errors.append("Draft Package schema_version mismatch")

    basis = package.get("basis")
    if not isinstance(basis, dict):
        return errors + ["Draft Package basis must be an object"]
    current_basis = {
        "production_profile_sha256": core.sha256_file(profile_path),
        "architecture_sha256": core.sha256_file(architecture_path),
        "architecture_review_summary_sha256": core.sha256_file(review_summary_path),
        "architecture_approval_sha256": core.sha256_file(approval_path),
    }
    for key, value in current_basis.items():
        if basis.get(key) != value:
            errors.append(f"Draft Package basis drift: {key}")

    matrix = package.get("candidate_matrix")
    acceptance = package.get("evidence_acceptance")
    if not isinstance(matrix, dict) or not isinstance(acceptance, dict):
        return errors + ["Draft Package embedded Matrix/Evidence acceptance must be objects"]
    matrix_sha = _object_sha(matrix)
    acceptance_sha = _object_sha(acceptance)
    if basis.get("candidate_matrix_sha256") != matrix_sha:
        errors.append("Draft Package embedded Candidate Matrix does not match basis SHA")
    if basis.get("evidence_acceptance_sha256") != acceptance_sha:
        errors.append("Draft Package embedded Evidence acceptance does not match basis SHA")
    if plan.get("basis", {}).get("candidate_matrix_sha256") != matrix_sha:
        errors.append("Draft Package Candidate Matrix is not the Matrix authorized by Architecture")
    if plan.get("basis", {}).get("candidate_selection_sha256") != basis.get("candidate_selection_sha256"):
        errors.append("Draft Package Candidate Selection SHA is not the Selection authorized by Architecture")
    if matrix.get("basis", {}).get("evidence_acceptance_sha256") != acceptance_sha:
        errors.append("Draft Package Evidence acceptance is not the acceptance bound by Candidate Matrix")
    if matrix.get("issue_id") != profile["issue_id"] or matrix.get("research_profile") != profile["research_profile"]:
        errors.append("Draft Package embedded Candidate Matrix identity mismatch")
    if acceptance.get("issue_id") != profile["issue_id"] or acceptance.get("research_profile") != profile["research_profile"]:
        errors.append("Draft Package embedded Evidence acceptance identity mismatch")

    matching_packages = [row for row in plan.get("packages", []) if row.get("package_id") == package.get("package_id")]
    if len(matching_packages) != 1:
        return errors + ["Draft Package package_id does not resolve exactly once in Architecture"]
    plan_package = matching_packages[0]
    expected_package = {
        "title": plan_package["title"],
        "purpose": plan_package["purpose"],
        "drafting_order": plan_package["drafting_order"],
        "primary_candidate_ids": list(plan_package["primary_candidate_ids"]),
        "supporting_candidate_ids": list(plan_package["supporting_candidate_ids"]),
        "must_cover_requirements": list(plan_package["must_cover_requirements"]),
        "boundaries": list(plan_package["boundaries"]),
    }
    if package.get("package") != expected_package:
        errors.append("Draft Package editorial package does not exactly match authorized Architecture package")
    if package.get("profile_extensions") != plan_package.get("profile_extensions"):
        errors.append("Draft Package Profile extensions drift from Architecture")
    if package.get("publication_extensions") != plan_package.get("publication_extensions"):
        errors.append("Draft Package Publication extensions drift from Architecture")

    matrix_rows = matrix.get("rows")
    acceptance_results = acceptance.get("results")
    inputs = package.get("evidence_inputs")
    if not isinstance(matrix_rows, list) or not isinstance(acceptance_results, list) or not isinstance(inputs, list):
        return errors + ["Draft Package Matrix rows/Evidence results/inputs must be arrays"]
    matrix_by_id = {
        row.get("candidate_id"): row for row in matrix_rows
        if isinstance(row, dict) and _nonempty(row.get("candidate_id"))
    }
    evidence_by_task = {
        row.get("evidence_task_id"): row for row in acceptance_results
        if isinstance(row, dict) and _nonempty(row.get("evidence_task_id"))
    }
    expected_usage = {
        **{cid: "PRIMARY" for cid in plan_package["primary_candidate_ids"]},
        **{cid: "SUPPORTING" for cid in plan_package["supporting_candidate_ids"]},
    }
    seen: set[str] = set()
    for offset, item in enumerate(inputs):
        prefix = f"evidence_inputs[{offset}]"
        if not isinstance(item, dict) or set(item) != {
            "candidate_id", "architecture_usage", "evidence_task_id",
            "evidence_sha256", "evidence_card",
        }:
            errors.append(f"{prefix} fields invalid")
            continue
        cid = item.get("candidate_id")
        if cid in seen:
            errors.append(f"Draft Package duplicates candidate Evidence input: {cid}")
            continue
        seen.add(cid)
        row = matrix_by_id.get(cid)
        if row is None or cid not in expected_usage:
            errors.append(f"{prefix} references candidate outside authorized Architecture package: {cid}")
            continue
        if item.get("architecture_usage") != expected_usage[cid]:
            errors.append(f"{prefix} Architecture usage mismatch")
        task_id = item.get("evidence_task_id")
        if task_id != row.get("evidence_task_id") or item.get("evidence_sha256") != row.get("evidence_sha256"):
            errors.append(f"{prefix} Candidate Matrix Evidence binding mismatch")
            continue
        meta = evidence_by_task.get(task_id)
        if meta is None or meta.get("sha256") != item.get("evidence_sha256"):
            errors.append(f"{prefix} Evidence acceptance binding mismatch")
        card = item.get("evidence_card")
        if not isinstance(card, dict) or _object_sha(card) != item.get("evidence_sha256"):
            errors.append(f"{prefix} embedded Evidence Card bytes do not match accepted Evidence SHA")
        elif card.get("evidence_task_id") != task_id or card.get("issue_id") != profile["issue_id"]:
            errors.append(f"{prefix} embedded Evidence Card identity mismatch")
    if seen != set(expected_usage):
        errors.append("Draft Package must contain exactly one Evidence input for every Architecture candidate placement")

    constraints = package.get("drafting_constraints")
    if constraints != {
        "language": "ja",
        "raw_sources_forbidden": True,
        "unknowns_remain_unknown": True,
        "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
    }:
        errors.append("Draft Package generic drafting constraints drift")
    return errors


def _card_ref_index(package: dict[str, Any]) -> dict[tuple[str, str, str], tuple[str, str, str | None]]:
    index: dict[tuple[str, str, str], tuple[str, str, str | None]] = {}
    for item in package["evidence_inputs"]:
        task_id = item["evidence_task_id"]
        card = item["evidence_card"]
        for row in card["temporal"]["events"]:
            index[(task_id, "EVENT", row["event_id"])] = (row["subject_id"], row["subject_role"], None)
        for kind, rows, id_key in (
            ("CLAIM", card["claims"], "statement_id"),
            ("METRIC", card["metrics"], "metric_id"),
            ("LIMITATION", card["limitations"], "statement_id"),
        ):
            for row in rows:
                index[(task_id, kind, row[id_key])] = (
                    row["subject_id"], row["subject_role"], row.get("evidence_class")
                )
    return index


def _validate_refs(
    refs: Any,
    index: dict[tuple[str, str, str], tuple[str, str, str | None]],
    label: str,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    classes: list[str] = []
    if not isinstance(refs, list):
        return [f"{label} evidence_refs must be an array"], classes
    seen: set[tuple[str, str, str, str, str]] = set()
    for offset, ref in enumerate(refs):
        prefix = f"{label}.evidence_refs[{offset}]"
        if not isinstance(ref, dict) or set(ref) != {
            "evidence_task_id", "kind", "evidence_id", "subject_id", "subject_role"
        }:
            errors.append(f"{prefix} fields invalid")
            continue
        if ref.get("kind") not in REF_KINDS or ref.get("subject_role") not in SUBJECT_ROLES:
            errors.append(f"{prefix} kind/subject_role invalid")
            continue
        key = (ref.get("evidence_task_id"), ref.get("kind"), ref.get("evidence_id"))
        expected = index.get(key)
        if expected is None:
            errors.append(f"{prefix} references Evidence outside Draft Package or unknown stable ID")
            continue
        if (ref.get("subject_id"), ref.get("subject_role")) != expected[:2]:
            errors.append(f"{prefix} subject binding does not match factual Evidence")
        classes.append(expected[2] or "PRIMARY_FACT")
        full = (key[0], key[1], key[2], ref.get("subject_id"), ref.get("subject_role"))
        if full in seen:
            errors.append(f"{prefix} duplicates an Evidence reference")
        seen.add(full)
    return errors, classes


def _validate_attribution(mode: Any, refs: list[Any], classes: list[str], label: str) -> list[str]:
    errors: list[str] = []
    if mode not in ATTRIBUTION_MODES:
        return [f"{label} attribution_mode invalid"]
    if mode == "NONE" and refs:
        errors.append(f"{label} attribution_mode NONE cannot carry Evidence refs")
    if mode != "NONE" and not refs:
        errors.append(f"{label} attributed/factual text requires Evidence refs")
    if "INFERENCE" in classes and mode not in {"INFERENCE", "MIXED"}:
        errors.append(f"{label} inference Evidence requires INFERENCE or MIXED attribution")
    if "SOCIAL_OBSERVATION" in classes and mode not in {"SOCIAL", "MIXED"}:
        errors.append(f"{label} social Evidence requires SOCIAL or MIXED attribution")
    if any(value in {"VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM"} for value in classes) and mode not in {"ATTRIBUTED", "MIXED"}:
        errors.append(f"{label} claimed Evidence requires ATTRIBUTED or MIXED attribution")
    return errors


def validate_draft_result(
    result: dict[str, Any],
    package_path: Path,
    prompt_path: Path,
) -> list[str]:
    errors: list[str] = []
    package = core.load_json(package_path)
    if set(result) != DRAFT_RESULT_FIELDS:
        return ["Draft Result fields must exactly match generic v2 contract"]
    for key in ("issue_id", "research_profile", "publication_profile", "package_id"):
        if result.get(key) != package.get(key):
            errors.append(f"Draft Result {key} does not match Draft Package")
    if result.get("schema_version") != "2.0-rc1" or result.get("status") not in {"DRAFT", "REVISED", "ESTABLISHED"}:
        errors.append("Draft Result schema/status invalid")
    expected_basis = {
        "draft_package_sha256": core.sha256_file(package_path),
        "prompt_id": "article-drafting-v2",
        "prompt_sha256": core.sha256_file(prompt_path),
    }
    if result.get("basis") != expected_basis:
        errors.append("Draft Result basis does not bind exact Package/prompt bytes")
    if not _nonempty(result.get("draft_version")) or not _nonempty(result.get("headline")) or not _nonempty(result.get("deck")):
        errors.append("Draft Result version/headline/deck required")
    runner = result.get("runner")
    if not isinstance(runner, dict) or set(runner) != {"provider", "model", "invocation", "generated_at", "run_reference"}:
        errors.append("Draft Result runner fields invalid")
    else:
        for key in ("provider", "model", "invocation"):
            if not _nonempty(runner.get(key)):
                errors.append(f"Draft Result runner.{key} required")
        if not _aware(runner.get("generated_at")):
            errors.append("Draft Result runner.generated_at must be timezone-aware ISO-8601")
        if runner.get("run_reference") is not None and not _nonempty(runner.get("run_reference")):
            errors.append("Draft Result runner.run_reference must be non-empty or null")

    ref_index = _card_ref_index(package)
    deck_refs = result.get("deck_evidence_refs")
    ref_errors, classes = _validate_refs(deck_refs, ref_index, "deck")
    errors += ref_errors
    errors += _validate_attribution(
        result.get("deck_attribution_mode"),
        deck_refs if isinstance(deck_refs, list) else [], classes, "deck"
    )

    blocks = result.get("blocks")
    block_ids: list[str] = []
    if not isinstance(blocks, list) or not blocks:
        errors.append("Draft Result blocks must be a non-empty array")
        blocks = []
    for offset, block in enumerate(blocks):
        prefix = f"blocks[{offset}]"
        if not isinstance(block, dict) or set(block) != {
            "block_id", "block_type", "text", "attribution_mode", "evidence_refs"
        }:
            errors.append(f"{prefix} fields invalid")
            continue
        if not _nonempty(block.get("block_id")) or not _nonempty(block.get("text")) or block.get("block_type") not in BLOCK_TYPES:
            errors.append(f"{prefix} identity/type/text invalid")
            continue
        block_ids.append(block["block_id"])
        ref_errors, classes = _validate_refs(block.get("evidence_refs"), ref_index, prefix)
        errors += ref_errors
        errors += _validate_attribution(
            block.get("attribution_mode"),
            block.get("evidence_refs") if isinstance(block.get("evidence_refs"), list) else [],
            classes,
            prefix,
        )
    if len(block_ids) != len(set(block_ids)):
        errors.append("Draft Result block_id values must be unique")
    block_set = set(block_ids)

    must_cover = result.get("must_cover_coverage")
    expected_requirements = set(package["package"]["must_cover_requirements"])
    actual_requirements: list[str] = []
    if not isinstance(must_cover, list):
        errors.append("must_cover_coverage must be an array")
        must_cover = []
    for row in must_cover:
        if not isinstance(row, dict) or set(row) != {"requirement", "block_ids"}:
            errors.append("must_cover_coverage row fields invalid")
            continue
        actual_requirements.append(row.get("requirement"))
        ids = row.get("block_ids")
        if not isinstance(ids, list) or not ids or len(ids) != len(set(ids)) or any(value not in block_set for value in ids):
            errors.append(f"must_cover_coverage block_ids invalid for {row.get('requirement')}")
    if len(actual_requirements) != len(set(actual_requirements)) or set(actual_requirements) != expected_requirements:
        errors.append("Draft Result must cover every Architecture must-cover requirement exactly once")

    boundaries = result.get("boundary_dispositions")
    expected_boundaries = set(package["package"]["boundaries"])
    actual_boundaries: list[str] = []
    if not isinstance(boundaries, list):
        errors.append("boundary_dispositions must be an array")
        boundaries = []
    for row in boundaries:
        if not isinstance(row, dict) or set(row) != {"boundary", "handling", "block_ids", "rationale"}:
            errors.append("boundary_disposition fields invalid")
            continue
        actual_boundaries.append(row.get("boundary"))
        handling = row.get("handling")
        ids = row.get("block_ids")
        if handling not in BOUNDARY_HANDLING or not isinstance(ids, list) or len(ids) != len(set(ids)) or any(value not in block_set for value in ids):
            errors.append(f"boundary_disposition invalid for {row.get('boundary')}")
        if handling == "EXPLICITLY_STATED" and not ids:
            errors.append(f"explicit boundary requires at least one block: {row.get('boundary')}")
        if handling == "RESPECTED_BY_OMISSION" and ids:
            errors.append(f"omission boundary must not claim reader-facing block coverage: {row.get('boundary')}")
        if not _nonempty(row.get("rationale")):
            errors.append(f"boundary rationale required: {row.get('boundary')}")
    if len(actual_boundaries) != len(set(actual_boundaries)) or set(actual_boundaries) != expected_boundaries:
        errors.append("Draft Result must dispose every Architecture boundary exactly once")
    if not isinstance(result.get("profile_extensions"), dict) or not isinstance(result.get("publication_extensions"), dict):
        errors.append("Draft Result extensions must be objects")
    return errors


def build_synthesis_input(
    repo_root: Path,
    profile_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
    draft_pairs: list[tuple[Path, Path]],
) -> dict[str, Any]:
    _require_contracts(repo_root)
    profile = core.load_json(profile_path)
    plan = core.load_json(architecture_path)
    approval = core.load_json(approval_path)
    approval_errors = validate_architecture_approval(
        approval, architecture_path, review_summary_path, profile["issue_id"]
    )
    if approval_errors:
        raise ValueError("Synthesis Architecture authorization invalid: " + "; ".join(approval_errors))
    expected_packages = {row["package_id"]: row for row in plan["packages"]}
    seen: set[str] = set()
    drafts: list[dict[str, Any]] = []
    for package_path, result_path in draft_pairs:
        package = core.load_json(package_path)
        package_errors = validate_self_contained_draft_package(
            package, profile_path, architecture_path, review_summary_path, approval_path
        )
        if package_errors:
            raise ValueError("Draft Package invalid before Synthesis: " + "; ".join(package_errors))
        result = core.load_json(result_path)
        errors = validate_draft_result(result, package_path, repo_root / DRAFT_PROMPT)
        if errors:
            raise ValueError("Draft Result invalid before Synthesis: " + "; ".join(errors))
        package_id = package["package_id"]
        if package_id not in expected_packages or package_id in seen:
            raise ValueError(f"Synthesis Draft package set invalid: {package_id}")
        if package["package"]["drafting_order"] != expected_packages[package_id]["drafting_order"]:
            raise ValueError(f"Synthesis drafting order drift: {package_id}")
        seen.add(package_id)
        drafts.append({
            "package_id": package_id,
            "drafting_order": package["package"]["drafting_order"],
            "draft_package_sha256": core.sha256_file(package_path),
            "draft_result_sha256": core.sha256_file(result_path),
            "draft_result": result,
        })
    if seen != set(expected_packages):
        raise ValueError(
            "Synthesis requires one validated Draft Result per Architecture package: "
            f"missing={sorted(set(expected_packages)-seen)}"
        )
    drafts.sort(key=lambda row: (row["drafting_order"], row["package_id"]))
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    research_contract = cfg["research_profiles"][profile["research_profile"]]
    publication_contract = cfg["publication_profiles"][profile["publication_profile"]]
    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "architecture_sha256": core.sha256_file(architecture_path),
            "architecture_approval_sha256": core.sha256_file(approval_path),
        },
        "editorial_thesis": plan["editorial_thesis"],
        "architecture_goals": list(plan["architecture_goals"]),
        "drafts": drafts,
        "profile_payload_requirements": list(research_contract.get("synthesis_payload_required", [])),
        "publication_payload_requirements": list(publication_contract.get("synthesis_payload_required", [])),
    }


def validate_synthesis_result(
    result: dict[str, Any],
    synthesis_input_path: Path,
    prompt_path: Path,
) -> list[str]:
    errors: list[str] = []
    synthesis_input = core.load_json(synthesis_input_path)
    required = {
        "schema_version", "issue_id", "research_profile", "publication_profile",
        "synthesis_version", "status", "basis", "runner", "profile_payload",
        "publication_payload",
    }
    if set(result) != required:
        return ["Profile Synthesis Result fields must exactly match generic v2 envelope"]
    for key in ("issue_id", "research_profile", "publication_profile"):
        if result.get(key) != synthesis_input.get(key):
            errors.append(f"Profile Synthesis {key} does not match input")
    if result.get("schema_version") != "2.0-rc1" or result.get("status") not in {"DRAFT", "REVISED", "ESTABLISHED"}:
        errors.append("Profile Synthesis schema/status invalid")
    expected_basis = {
        "synthesis_input_sha256": core.sha256_file(synthesis_input_path),
        "prompt_id": "profile-synthesis-v2",
        "prompt_sha256": core.sha256_file(prompt_path),
    }
    if result.get("basis") != expected_basis:
        errors.append("Profile Synthesis basis does not bind exact input/prompt bytes")
    if not _nonempty(result.get("synthesis_version")):
        errors.append("Profile Synthesis synthesis_version required")
    runner = result.get("runner")
    if not isinstance(runner, dict) or set(runner) != {"provider", "model", "invocation", "generated_at", "run_reference"}:
        errors.append("Profile Synthesis runner fields invalid")
    else:
        for key in ("provider", "model", "invocation"):
            if not _nonempty(runner.get(key)):
                errors.append(f"Profile Synthesis runner.{key} required")
        if not _aware(runner.get("generated_at")):
            errors.append("Profile Synthesis runner.generated_at must be timezone-aware ISO-8601")
        if runner.get("run_reference") is not None and not _nonempty(runner.get("run_reference")):
            errors.append("Profile Synthesis runner.run_reference must be non-empty or null")
    for payload_key, requirements_key, label in (
        ("profile_payload", "profile_payload_requirements", "Research Profile"),
        ("publication_payload", "publication_payload_requirements", "Publication Profile"),
    ):
        payload = result.get(payload_key)
        requirements = synthesis_input.get(requirements_key)
        if not isinstance(payload, dict) or not isinstance(requirements, list):
            errors.append(f"{label} synthesis payload/requirements invalid")
            continue
        if set(payload) != set(requirements):
            errors.append(f"{label} synthesis payload keys must exactly match Profile-owned requirements")
            continue
        for key, value in payload.items():
            if not _payload_value_present(value):
                errors.append(f"{label} synthesis payload value is absent: {key}")
    return errors


def _path(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--implementation-sha", required=False)
    sub = parser.add_subparsers(dest="command", required=True)

    package = sub.add_parser("draft-package")
    for key in (
        "profile", "discovery", "screening", "evidence", "views", "ledger",
        "completeness", "matrix", "selection", "architecture", "review-summary",
        "approval", "package-id", "output",
    ):
        package.add_argument(f"--{key}", required=True)

    check = sub.add_parser("draft-check")
    check.add_argument("--package", required=True)
    check.add_argument("--result", required=True)

    synthesis = sub.add_parser("synthesis-input")
    for key in ("profile", "architecture", "review-summary", "approval", "output"):
        synthesis.add_argument(f"--{key}", required=True)
    synthesis.add_argument(
        "--draft-pair", action="append", default=[],
        help="PACKAGE_PATH=RESULT_PATH; repeat for every Architecture package",
    )

    synthesis_check = sub.add_parser("synthesis-check")
    synthesis_check.add_argument("--input", required=True)
    synthesis_check.add_argument("--result", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.repo_root).resolve()
    try:
        if args.command == "draft-package":
            impl = args.implementation_sha or core.repository_commit_sha(root)
            payload = derive_draft_package(
                root,
                _path(root, args.profile), _path(root, args.discovery),
                _path(root, args.screening), _path(root, args.evidence),
                _path(root, args.views), _path(root, args.ledger),
                _path(root, args.completeness), _path(root, args.matrix),
                _path(root, args.selection), _path(root, args.architecture),
                _path(root, args.review_summary), _path(root, args.approval),
                args.package_id, impl,
            )
            output = _path(root, args.output)
            if output.exists():
                raise ValueError(f"refusing to overwrite Draft Package: {output}")
            core.write_json(output, payload)
            print(output)
            return 0
        if args.command == "draft-check":
            package_path = _path(root, args.package)
            errors = validate_draft_result(
                core.load_json(_path(root, args.result)), package_path, root / DRAFT_PROMPT
            )
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        if args.command == "synthesis-input":
            pairs: list[tuple[Path, Path]] = []
            for raw in args.draft_pair:
                if "=" not in raw:
                    raise ValueError("--draft-pair must be PACKAGE_PATH=RESULT_PATH")
                left, right = raw.split("=", 1)
                pairs.append((_path(root, left), _path(root, right)))
            payload = build_synthesis_input(
                root, _path(root, args.profile), _path(root, args.architecture),
                _path(root, args.review_summary), _path(root, args.approval), pairs,
            )
            output = _path(root, args.output)
            if output.exists():
                raise ValueError(f"refusing to overwrite Synthesis Input: {output}")
            core.write_json(output, payload)
            print(output)
            return 0
        if args.command == "synthesis-check":
            errors = validate_synthesis_result(
                core.load_json(_path(root, args.result)), _path(root, args.input),
                root / SYNTHESIS_PROMPT,
            )
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
