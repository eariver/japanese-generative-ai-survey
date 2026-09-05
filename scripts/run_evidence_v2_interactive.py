#!/usr/bin/env python3
"""Run Core v2 Evidence, Edition Views, Materiality, and Completeness from explicit interactive records.

The runner is profile-neutral and preserves the Core v2 factual/editorial split:
- one explicit interactive record is required for every non-DROP Evidence task;
- factual Evidence Cards are generated only from the Discovery-bounded source
  already carried by each task;
- Edition Views carry Profile-specific materiality/lineage annotations;
- Materiality Ledger is derived by the canonical implementation; and
- Completeness retains every Profile/named obligation and is validated by the
  authoritative profile-completeness guard.

It does not advance Production State and cannot resolve a Human Gate.
"""
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness
from scripts import survey_discovery_v2 as discovery
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening

INPUT_NAME = "interactive-evidence.json"
AUDIT_NAME = "interactive-audit.json"

SOURCE_CLASS_MAP = {
    "PRIMARY_OFFICIAL": "PRIMARY_OFFICIAL",
    "PRIMARY_PAPER": "PRIMARY_PAPER",
    "PRIMARY_REPOSITORY": "PRIMARY_REPOSITORY",
    "SOCIAL": "SOCIAL",
    "SECONDARY_INVESTOR_ACCOUNT": "SECONDARY",
    "SECONDARY": "SECONDARY",
}

ENTITY_TYPES = {
    "MODEL", "MODEL_FAMILY", "VARIANT", "API", "PRODUCT", "AGENT",
    "FRAMEWORK", "PAPER", "BENCHMARK", "DATASET", "ORGANIZATION", "OTHER",
}
ARTIFACT_TYPES = {
    "MODEL", "MODEL_UPDATE", "OPEN_WEIGHT", "API", "PRODUCT", "AGENT",
    "FRAMEWORK", "PAPER", "BENCHMARK", "DATASET", "SAFETY_EVENT",
    "SECURITY_EVENT", "INTEGRATION", "OTHER",
}
EVIDENCE_CLASSES = {
    "PRIMARY_FACT", "VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM",
    "SOCIAL_OBSERVATION", "INFERENCE",
}
CARD_STATUS = {"VERIFIED", "PARTIAL", "REJECTED", "NEEDS_MORE"}
VERIFY_STATUS = {"VERIFIED", "UNRESOLVED", "CONTRADICTED", "NOT_APPLICABLE"}
MATERIALITY = {"MATERIAL", "CONTEXT", "NON_MATERIAL", "HOLD"}
LINEAGE_ROLES = {"CORE", "BRIDGE", "CONTEXT", "PARALLEL", "COMPETING", "COUNTEREXAMPLE"}
OBLIGATION_STATUS = {"SATISFIED", "LIMITATION", "NEEDS_RESEARCH", "NOT_APPLICABLE"}


def _rel(repo_root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(repo_root.resolve()))


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any, *, allow_empty: bool = True) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and len(value) == len(set(value))
        and all(_nonempty(item) for item in value)
    )


def _source_class(source_type: Any) -> str:
    value = SOURCE_CLASS_MAP.get(source_type)
    if value is None:
        raise ValueError(f"unsupported Discovery source_type for Evidence: {source_type!r}")
    return value


def _validate_runner(value: Any) -> dict[str, str]:
    if not isinstance(value, dict) or set(value) != {"provider", "model", "invocation", "generated_at"}:
        raise ValueError("interactive Evidence runner fields invalid")
    result: dict[str, str] = {}
    for key in ("provider", "model", "invocation", "generated_at"):
        item = value.get(key)
        if not _nonempty(item):
            raise ValueError(f"interactive Evidence runner.{key} required")
        result[key] = item
    core.parse_instant(result["generated_at"])
    return result


def _validate_record(row: Any, profile: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(row, dict):
        raise ValueError("interactive Evidence record must be an object")
    required = {
        "discovery_id", "status", "entity", "artifact_type", "claims",
        "limitations", "verification", "materiality", "materiality_rationale",
        "scope_dimensions", "lineage_role", "branch_ids", "transition_ids",
        "inheritance_note", "historical_attribution_caveat",
    }
    if set(row) != required:
        raise ValueError(f"interactive Evidence record fields invalid: {row.get('discovery_id')}")
    discovery_id = row.get("discovery_id")
    if not _nonempty(discovery_id):
        raise ValueError("interactive Evidence discovery_id required")
    if row.get("status") not in CARD_STATUS:
        raise ValueError(f"{discovery_id}: invalid Evidence status")

    entity = row.get("entity")
    if not isinstance(entity, dict) or set(entity) != {
        "entity_id", "canonical_name", "entity_type", "organization", "canonical_url"
    }:
        raise ValueError(f"{discovery_id}: entity fields invalid")
    if not _nonempty(entity.get("entity_id")) or not _nonempty(entity.get("canonical_name")):
        raise ValueError(f"{discovery_id}: entity identity required")
    if entity.get("entity_type") not in ENTITY_TYPES:
        raise ValueError(f"{discovery_id}: invalid entity_type")
    if entity.get("organization") is not None and not isinstance(entity.get("organization"), str):
        raise ValueError(f"{discovery_id}: entity.organization must be string/null")
    if entity.get("canonical_url") is not None and not isinstance(entity.get("canonical_url"), str):
        raise ValueError(f"{discovery_id}: entity.canonical_url must be string/null")
    if row.get("artifact_type") not in ARTIFACT_TYPES:
        raise ValueError(f"{discovery_id}: invalid artifact_type")

    claims = row.get("claims")
    if not isinstance(claims, list):
        raise ValueError(f"{discovery_id}: claims must be an array")
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict) or set(claim) != {"text", "evidence_class", "context"}:
            raise ValueError(f"{discovery_id}: claims[{index}] fields invalid")
        if not _nonempty(claim.get("text")) or claim.get("evidence_class") not in EVIDENCE_CLASSES:
            raise ValueError(f"{discovery_id}: claims[{index}] invalid")
        if claim.get("context") is not None and not isinstance(claim.get("context"), str):
            raise ValueError(f"{discovery_id}: claims[{index}].context must be string/null")

    limitations = row.get("limitations")
    if not _string_list(limitations):
        raise ValueError(f"{discovery_id}: limitations must be a unique string array")

    verification = row.get("verification")
    if not isinstance(verification, list):
        raise ValueError(f"{discovery_id}: verification must be an array")
    targets: set[str] = set()
    for index, item in enumerate(verification):
        if not isinstance(item, dict) or set(item) != {"target", "status", "finding"}:
            raise ValueError(f"{discovery_id}: verification[{index}] fields invalid")
        if not _nonempty(item.get("target")) or item["target"] in targets:
            raise ValueError(f"{discovery_id}: invalid/duplicate verification target")
        targets.add(item["target"])
        if item.get("status") not in VERIFY_STATUS or not _nonempty(item.get("finding")):
            raise ValueError(f"{discovery_id}: verification[{index}] invalid")

    if row.get("materiality") not in MATERIALITY or not _nonempty(row.get("materiality_rationale")):
        raise ValueError(f"{discovery_id}: materiality invalid")
    if row["status"] == "REJECTED" and row["materiality"] != "NON_MATERIAL":
        raise ValueError(f"{discovery_id}: REJECTED Evidence must be NON_MATERIAL")
    if row["status"] == "NEEDS_MORE" and row["materiality"] != "HOLD":
        raise ValueError(f"{discovery_id}: NEEDS_MORE Evidence must be HOLD")

    allowed_dims = set(profile["research_scope"]["scope_dimensions"])
    dims = row.get("scope_dimensions")
    if not _string_list(dims) or any(item not in allowed_dims for item in dims):
        raise ValueError(f"{discovery_id}: scope_dimensions invalid")
    if row.get("lineage_role") not in LINEAGE_ROLES:
        raise ValueError(f"{discovery_id}: invalid lineage_role")
    for key in ("branch_ids", "transition_ids"):
        if not _string_list(row.get(key)):
            raise ValueError(f"{discovery_id}: {key} invalid")
    for key in ("inheritance_note", "historical_attribution_caveat"):
        if row.get(key) is not None and not isinstance(row.get(key), str):
            raise ValueError(f"{discovery_id}: {key} must be string/null")
    return row


def _validate_completeness_input(value: Any, profile: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != {"obligations", "residual_limitations", "closure"}:
        raise ValueError("interactive Completeness fields invalid")
    obligations = value.get("obligations")
    if not isinstance(obligations, list):
        raise ValueError("interactive Completeness obligations must be an array")
    by_id: dict[str, dict[str, str]] = {}
    for row in obligations:
        if not isinstance(row, dict) or set(row) != {"obligation_id", "status", "rationale"}:
            raise ValueError("interactive Completeness obligation fields invalid")
        oid = row.get("obligation_id")
        if not _nonempty(oid) or oid in by_id:
            raise ValueError(f"invalid/duplicate Completeness obligation: {oid!r}")
        if row.get("status") not in OBLIGATION_STATUS or not _nonempty(row.get("rationale")):
            raise ValueError(f"Completeness obligation invalid: {oid}")
        by_id[oid] = row
    expected_ids = {
        row["obligation_id"] for row in profile["research_scope"]["initial_obligations"]
    }
    if set(by_id) != expected_ids:
        raise ValueError(
            f"interactive Completeness must cover exact Profile obligations: missing={sorted(expected_ids-set(by_id))} extra={sorted(set(by_id)-expected_ids)}"
        )
    residual = value.get("residual_limitations")
    if not _string_list(residual):
        raise ValueError("interactive Completeness residual_limitations invalid")
    closure = value.get("closure")
    required_closure = {
        "targeted_gap_fill_completed", "limitations", "status"
    }
    if profile["research_profile"] == "THEMATIC":
        if not isinstance(closure, dict) or set(closure) != required_closure:
            raise ValueError("interactive Thematic closure fields invalid")
        if not isinstance(closure.get("targeted_gap_fill_completed"), bool):
            raise ValueError("interactive Thematic targeted_gap_fill_completed must be boolean")
        if not _string_list(closure.get("limitations")):
            raise ValueError("interactive Thematic closure limitations invalid")
        if closure.get("status") not in {"COMPLETE", "LIMITED", "NEEDS_RESEARCH"}:
            raise ValueError("interactive Thematic closure status invalid")
    elif closure is not None:
        raise ValueError("non-Thematic interactive Completeness closure must be null")
    return value


def validate_interactive_input(value: dict[str, Any], profile: dict[str, Any], expected_ids: set[str]) -> tuple[dict[str, dict[str, Any]], dict[str, str], dict[str, Any]]:
    if set(value) != {"schema_version", "issue_id", "runner", "records", "completeness"}:
        raise ValueError("interactive Evidence input fields invalid")
    if value.get("schema_version") != "2.0-rc1" or value.get("issue_id") != profile["issue_id"]:
        raise ValueError("interactive Evidence input identity mismatch")
    runner = _validate_runner(value.get("runner"))
    rows = value.get("records")
    if not isinstance(rows, list):
        raise ValueError("interactive Evidence records must be an array")
    by_id: dict[str, dict[str, Any]] = {}
    for raw in rows:
        row = _validate_record(raw, profile)
        did = row["discovery_id"]
        if did in by_id:
            raise ValueError(f"duplicate interactive Evidence discovery_id: {did}")
        by_id[did] = row
    if set(by_id) != expected_ids:
        raise ValueError(
            f"interactive Evidence records must cover exact non-DROP Discovery IDs: missing={sorted(expected_ids-set(by_id))} extra={sorted(set(by_id)-expected_ids)}"
        )
    completeness_input = _validate_completeness_input(value.get("completeness"), profile)
    return by_id, runner, completeness_input


def _build_card(task: dict[str, Any], meta: dict[str, Any], package: dict[str, Any], record: dict[str, Any], runner: dict[str, str]) -> dict[str, Any]:
    source_record = task["source_records"][0]
    locator = source_record.get("locator")
    if not _nonempty(locator):
        raise ValueError(f"{task['evidence_task_id']}: Discovery source locator missing")
    entity = dict(record["entity"])
    if entity["canonical_url"] is None:
        entity["canonical_url"] = locator
    entity_id = entity["entity_id"]
    source_id = "src-1"
    source = {
        "source_id": source_id,
        "url": locator,
        "source_class": _source_class(source_record.get("source_type")),
        "title": source_record.get("title") or locator,
        "published_at": source_record.get("published_at"),
        "accessed_at": runner["generated_at"],
        "role": "Discovery-bounded source used for factual verification",
    }

    claims: list[dict[str, Any]] = []
    for index, item in enumerate(record["claims"], start=1):
        claims.append({
            "statement_id": f"claim-{index}",
            "text": item["text"],
            "subject_id": entity_id,
            "subject_role": "PRIMARY_SUBJECT",
            "evidence_class": item["evidence_class"],
            "source_ids": [source_id],
            "context": item["context"],
        })
    limitations: list[dict[str, Any]] = []
    for index, text in enumerate(record["limitations"], start=1):
        limitations.append({
            "statement_id": f"limitation-{index}",
            "text": text,
            "subject_id": entity_id,
            "subject_role": "PRIMARY_SUBJECT",
            "evidence_class": "INFERENCE",
            "source_ids": [source_id],
            "context": "Evidence boundary retained for downstream editorial use.",
        })

    verification_map = {row["target"]: row for row in record["verification"]}
    expected_targets = list(task.get("verification_targets", []))
    if set(verification_map) != set(expected_targets):
        raise ValueError(
            f"{task['discovery_ids'][0]}: verification input must cover exact task targets: missing={sorted(set(expected_targets)-set(verification_map))} extra={sorted(set(verification_map)-set(expected_targets))}"
        )
    verification_targets: list[dict[str, Any]] = []
    unresolved: list[str] = []
    contradictions: list[str] = []
    for target in expected_targets:
        item = verification_map[target]
        verification_targets.append({
            "target": target,
            "status": item["status"],
            "finding": item["finding"],
            "subject_ids": [entity_id],
            "source_ids": [source_id],
        })
        if item["status"] == "UNRESOLVED":
            unresolved.append(f"{target}: {item['finding']}")
        elif item["status"] == "CONTRADICTED":
            contradictions.append(f"{target}: {item['finding']}")

    events: list[dict[str, Any]] = []
    published = source_record.get("published_at")
    if published is not None:
        events.append({
            "event_id": "event-1",
            "event_type": "SOURCE_PUBLICATION_OR_RELEASE",
            "event_date": str(published),
            "subject_id": entity_id,
            "subject_role": "PRIMARY_SUBJECT",
            "source_ids": [source_id],
        })

    return {
        "schema_version": "2.0-rc1",
        "issue_id": task["issue_id"],
        "evidence_task_id": task["evidence_task_id"],
        "basis": {
            "task_sha256": meta["sha256"],
            "screening_acceptance_sha256": task["screening_basis"]["screening_acceptance_sha256"],
            "prompt_sha256": package["prompt"]["sha256"],
            "result_contract_sha256": package["contracts"]["card"]["sha256"],
        },
        "status": record["status"],
        "entities": [entity],
        "artifact": {
            "primary_subject_id": entity_id,
            "artifact_type": record["artifact_type"],
            "canonical_name": entity["canonical_name"],
            "canonical_url": entity["canonical_url"],
        },
        "temporal": {
            "observed_at": runner["generated_at"],
            "events": events,
        },
        "sources": [source],
        "claims": claims,
        "metrics": [],
        "limitations": limitations,
        "verification": {
            "targets": verification_targets,
            "unresolved_questions": unresolved,
            "contradictions": contradictions,
        },
    }


def _build_view(profile: dict[str, Any], task_id: str, evidence_sha: str, record: dict[str, Any]) -> dict[str, Any]:
    annotations: dict[str, Any]
    if profile["research_profile"] == "THEMATIC":
        annotations = {
            "lineage_role": record["lineage_role"],
            "branch_ids": list(record["branch_ids"]),
            "transition_ids": list(record["transition_ids"]),
            "inheritance_note": record["inheritance_note"],
            "historical_attribution_caveat": record["historical_attribution_caveat"],
        }
    else:
        raise ValueError("interactive Evidence runner currently requires explicit Profile annotation support; only THEMATIC is implemented")
    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "evidence_task_id": task_id,
        "evidence_sha256": evidence_sha,
        "materiality": {
            "status": record["materiality"],
            "rationale": record["materiality_rationale"],
        },
        "scope_dimensions": list(record["scope_dimensions"]),
        "profile_annotations": annotations,
    }


def _build_completeness(
    repo_root: Path,
    profile: dict[str, Any],
    profile_path: Path,
    discovery_records: list[dict[str, Any]],
    ledger_path: Path,
    ledger: dict[str, Any],
    input_value: dict[str, Any],
) -> dict[str, Any]:
    by_input = {row["obligation_id"]: row for row in input_value["obligations"]}
    ledger_task_by_discovery = {
        row["discovery_id"]: list(row["evidence_task_ids"])
        for row in ledger["rows"]
    }
    obligations: list[dict[str, Any]] = []
    for initial in profile["research_scope"]["initial_obligations"]:
        oid = initial["obligation_id"]
        declaring = sorted(
            row["discovery_id"]
            for row in discovery_records
            if oid in row.get("provenance", {}).get("obligation_ids", [])
        )
        task_ids = sorted({
            task_id
            for did in declaring
            for task_id in ledger_task_by_discovery.get(did, [])
        })
        decision = by_input[oid]
        obligations.append({
            "obligation_id": oid,
            "dimension": initial["dimension"],
            "description": initial["description"],
            "status": decision["status"],
            "discovery_ids": declaring,
            "evidence_task_ids": task_ids,
            "rationale": decision["rationale"],
        })

    needs_research = sum(row["status"] == "NEEDS_RESEARCH" for row in obligations)
    residual = list(input_value["residual_limitations"])
    limitations = [row for row in obligations if row["status"] == "LIMITATION"]
    overall = "INCOMPLETE" if needs_research else ("LIMITED" if limitations or residual else "READY")

    closure_input = input_value["closure"]
    closure = None
    if profile["research_profile"] == "THEMATIC":
        max_pass = max(
            (row.get("provenance", {}).get("research_pass", 0) for row in discovery_records),
            default=0,
        )
        final_records = [
            row for row in discovery_records
            if max_pass > 0 and row.get("provenance", {}).get("research_pass") == max_pass
        ]
        obligation_status = {row["obligation_id"]: row["status"] for row in obligations}
        final_ids = {
            oid for row in final_records
            for oid in row.get("provenance", {}).get("obligation_ids", [])
            if oid in obligation_status
        }
        material_ids = {
            oid for oid in final_ids
            if obligation_status[oid] in {"SATISFIED", "LIMITATION", "NEEDS_RESEARCH"}
        }
        open_ids = {oid for oid in material_ids if obligation_status[oid] == "NEEDS_RESEARCH"}
        closure = {
            "expansion_passes": max(1, max_pass),
            "final_pass_new_sources": len(final_records),
            "final_pass_new_material_obligations": len(material_ids),
            "final_pass_new_material_obligations_open": len(open_ids),
            "targeted_gap_fill_completed": closure_input["targeted_gap_fill_completed"],
            "open_material_obligations": needs_research,
            "limitations": list(closure_input["limitations"]),
            "status": closure_input["status"],
        }

    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        },
        "overall_status": overall,
        "obligations": obligations,
        "residual_limitations": residual,
        "closure": closure,
    }


def _archive_input(repo_root: Path, evidence_acceptance_path: Path, input_path: Path, runner: dict[str, str], outputs: dict[str, str]) -> dict[str, Any]:
    run_dir = evidence_acceptance_path.parent
    archived = run_dir / INPUT_NAME
    if archived.exists():
        if core.sha256_file(archived) != core.sha256_file(input_path):
            raise ValueError("accepted Evidence run has conflicting interactive input bytes")
    else:
        shutil.copy2(input_path, archived)
    audit = {
        "schema_version": "2.0-rc1",
        "issue_id": core.load_json(evidence_acceptance_path)["issue_id"],
        "interactive_input": {"path": _rel(repo_root, archived), "sha256": core.sha256_file(archived)},
        "runner": runner,
        "outputs": outputs,
    }
    audit_path = run_dir / AUDIT_NAME
    if audit_path.exists():
        if core.load_json(audit_path) != audit:
            raise ValueError("accepted Evidence run has conflicting interactive audit bytes")
    else:
        core.write_json(audit_path, audit)
    return audit


def run(repo_root: Path, state_path: Path, input_path: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    state_path = state_path.resolve()
    input_path = input_path.resolve()
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before interactive Evidence: " + "; ".join(errors))
    if state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("interactive Evidence requires CANDIDATES_NORMALIZED Production State")

    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    discovery_acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
    accepted_discovery = discovery.validate_acceptance(repo_root, discovery_acceptance_path)
    root_discovery_path = core.repo_local_path(repo_root, accepted_discovery["discovery_path"], "accepted Discovery JSONL")

    implementation_sha = core.repository_commit_sha(repo_root)
    active_screening = screening.resolve_active_screening_acceptance(
        repo_root, state_path, implementation_sha
    )
    screening_acceptance_path = active_screening["path"]
    effective = screening.resolve_effective_discovery_basis(
        repo_root,
        screening_acceptance_path.parent / "package.json",
        implementation_sha,
        accepted_root_path=root_discovery_path,
    )
    discovery_path = effective["path"]
    discovery_records = effective["records"]
    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        package_root = temp_root / "evidence-package"
        with agent_tool.current_stage_basis_override():
            package_path = evidence.prepare_evidence_package(
                repo_root,
                state_path,
                discovery_path,
                screening_acceptance_path,
                package_root,
                implementation_sha,
            )
        package = core.load_json(package_path)
        task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
        expected_ids = set(task_meta)
        interactive_doc = core.load_json(input_path)
        records_by_id, runner, completeness_input = validate_interactive_input(
            interactive_doc, profile, expected_ids
        )

        results_dir = temp_root / "evidence-results"
        results_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task = core.load_json(package_path.parent / meta["path"])
            card = _build_card(task, meta, package, records_by_id[did], runner)
            errors = evidence.validate_evidence_card(card, task, meta["sha256"], package)
            if errors:
                raise ValueError(f"interactive Evidence Card {did} invalid: {'; '.join(errors)}")
            core.write_json(results_dir / Path(meta["path"]).name, card)

        evidence_root = source_root / "evidence/v2/accepted"
        with agent_tool.current_stage_basis_override():
            evidence_acceptance_path = evidence.accept_evidence_results(
                repo_root,
                package_path,
                results_dir,
                evidence_root,
                implementation_sha,
            )
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                repo_root, evidence_acceptance_path, implementation_sha
            )

        evidence_by_task = {
            row["evidence_task_id"]: row for row in evidence_acceptance["results"]
        }
        views_dir = temp_root / "views"
        views_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task_id = meta["evidence_task_id"]
            entry = evidence_by_task[task_id]
            view = _build_view(profile, task_id, entry["sha256"], records_by_id[did])
            errors = evidence.validate_edition_view(
                view, profile, entry["sha256"], entry["status"]
            )
            if errors:
                raise ValueError(f"interactive Edition View {did} invalid: {'; '.join(errors)}")
            core.write_json(views_dir / evidence.view_filename(task_id), view)

        views_root = source_root / "evidence/v2/views/accepted"
        with agent_tool.current_stage_basis_override():
            views_acceptance_path = evidence.accept_edition_views(
                repo_root,
                profile_path,
                evidence_acceptance_path,
                views_dir,
                views_root,
                implementation_sha,
            )
            evidence.validate_edition_views_acceptance(
                repo_root,
                profile_path,
                evidence_acceptance_path,
                views_acceptance_path,
                implementation_sha,
            )

        ledger_path = source_root / "materiality-ledger-v2.json"
        if ledger_path.exists():
            raise ValueError(f"refusing to overwrite Materiality Ledger: {ledger_path}")
        with agent_tool.current_stage_basis_override():
            ledger = evidence.build_materiality_ledger(
                repo_root,
                profile_path,
                discovery_path,
                screening_acceptance_path,
                evidence_acceptance_path,
                views_acceptance_path,
                implementation_sha,
            )
        evidence.write_materiality_ledger(ledger_path, ledger)

        completeness_path = source_root / "profile-completeness-v2.json"
        if completeness_path.exists():
            raise ValueError(f"refusing to overwrite Profile Completeness: {completeness_path}")
        result = _build_completeness(
            repo_root,
            profile,
            profile_path,
            discovery_records,
            ledger_path,
            ledger,
            completeness_input,
        )
        schema_gate.validate_instance(
            result,
            repo_root / "schemas/profile-completeness-result.schema.json",
            label="Profile Completeness",
        )
        with agent_tool.current_stage_basis_override():
            errors = completeness.validate_profile_completeness(
                result,
                repo_root,
                profile_path,
                discovery_path,
                screening_acceptance_path,
                evidence_acceptance_path,
                views_acceptance_path,
                ledger_path,
                implementation_sha,
            )
        if errors:
            raise ValueError("Profile Completeness invalid: " + "; ".join(errors))
        core.write_json(completeness_path, result)

    outputs = {
        "evidence_acceptance": _rel(repo_root, evidence_acceptance_path),
        "edition_views_acceptance": _rel(repo_root, views_acceptance_path),
        "materiality_ledger": _rel(repo_root, ledger_path),
        "profile_completeness": _rel(repo_root, completeness_path),
    }
    _archive_input(repo_root, evidence_acceptance_path, input_path, runner, outputs)
    return {
        **outputs,
        "evidence_result_count": core.load_json(evidence_acceptance_path)["result_count"],
        "completeness_status": core.load_json(completeness_path)["overall_status"],
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
    if not state.is_absolute():
        state = root / state
    if not input_path.is_absolute():
        input_path = root / input_path
    try:
        print(json.dumps(run(root, state, input_path), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=__import__("sys").stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
