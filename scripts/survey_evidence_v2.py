#!/usr/bin/env python3
"""Factual Evidence, Edition Views, Materiality and Completeness for Core v2.

WU-007 keeps edition significance outside factual Evidence and enforces two P0
historical lessons before Architecture:
- #166: no discovered material may disappear without a disposition;
- #191: claims/metrics/properties bind explicit subject entities.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any, Iterable

from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening

PROMPT_PATH = Path("config/prompts/evidence-verification-v2.md")
TASK_SCHEMA = Path("schemas/evidence-v2-task.schema.json")
CARD_SCHEMA = Path("schemas/evidence-v2-card.schema.json")
PACKAGE_SCHEMA = Path("schemas/evidence-v2-run-package.schema.json")
VIEW_SCHEMA = Path("schemas/edition-evidence-view.schema.json")
LEDGER_SCHEMA = Path("schemas/materiality-ledger.schema.json")
COMPLETENESS_SCHEMA = Path("schemas/profile-completeness-result.schema.json")

CARD_KEYS = {
    "schema_version", "issue_id", "evidence_task_id", "basis", "status",
    "entities", "artifact", "temporal", "sources", "claims", "metrics",
    "limitations", "verification",
}
EVIDENCE_CLASSES = {
    "PRIMARY_FACT", "VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM",
    "SOCIAL_OBSERVATION", "INFERENCE",
}
VIEW_MATERIALITY = {"MATERIAL", "CONTEXT", "NON_MATERIAL", "HOLD"}
OBLIGATION_STATUS = {"SATISFIED", "LIMITATION", "NEEDS_RESEARCH", "NOT_APPLICABLE"}


def _rel(repo_root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(repo_root.resolve()))


def stable_task_id(issue_id: str, discovery_id: str) -> str:
    digest = hashlib.sha256(discovery_id.encode("utf-8")).hexdigest()[:16]
    return f"evidence:{issue_id}:{digest}"


def task_filename(task_id: str) -> str:
    digest = hashlib.sha256(task_id.encode("utf-8")).hexdigest()[:20]
    return f"task-{digest}.json"


def validate_screening_acceptance(
    repo_root: Path,
    screening_acceptance_path: Path,
    discovery_path: Path,
    issue_id: str,
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    acceptance = core.load_json(screening_acceptance_path)
    if acceptance.get("schema_version") != "2.0-rc1" or acceptance.get("issue_id") != issue_id:
        raise ValueError("Screening acceptance identity mismatch")
    package_path = screening_acceptance_path.parent / "package.json"
    if not package_path.is_file():
        raise ValueError("accepted Screening package copy is missing")
    package = core.load_json(package_path)
    if core.sha256_file(package_path) != acceptance.get("package_sha256"):
        raise ValueError("accepted Screening package SHA mismatch")
    if package.get("basis", {}).get("discovery_sha256") != core.sha256_file(discovery_path):
        raise ValueError("Screening acceptance discovery basis no longer matches")
    discoveries = screening.read_jsonl(discovery_path)
    screening.validate_discovery_set(discoveries, issue_id)
    expected = {row["discovery_id"] for row in discoveries}
    decisions = acceptance.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("Screening acceptance decisions missing")
    actual = [row.get("discovery_id") for row in decisions if isinstance(row, dict)]
    if len(actual) != len(set(actual)) or set(actual) != expected:
        raise ValueError("Screening acceptance does not cover discovery set exactly")
    return acceptance, package, discoveries


def prepare_evidence_package(
    repo_root: Path,
    state_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    output_dir: Path,
    implementation_sha: str,
) -> Path:
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    core.verify_state_basis(repo_root, cfg, state, implementation_sha)
    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    issue_id = state["issue_id"]
    acceptance, _, discoveries = validate_screening_acceptance(
        repo_root, screening_acceptance_path, discovery_path, issue_id
    )
    discovery_map = {row["discovery_id"]: row for row in discoveries}
    decisions = {row["discovery_id"]: row for row in acceptance["decisions"]}

    for required in (PROMPT_PATH, TASK_SCHEMA, CARD_SCHEMA):
        if not (repo_root / required).is_file():
            raise ValueError(f"Evidence v2 contract file missing: {required}")
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"refusing to overwrite non-empty Evidence package directory: {output_dir}")
    task_dir = output_dir / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)
    tasks_meta: list[dict[str, Any]] = []

    for discovery_id in sorted(discovery_map):
        decision = decisions[discovery_id]
        if decision["decision"] == "DROP":
            continue
        task_id = stable_task_id(issue_id, discovery_id)
        task = {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "evidence_task_id": task_id,
            "discovery_ids": [discovery_id],
            "source_records": [discovery_map[discovery_id]["source"]],
            "verification_targets": list(decision["verification_targets"]),
            "screening_basis": {
                "screening_acceptance_sha256": core.sha256_file(screening_acceptance_path),
                "decisions": [{
                    "discovery_id": discovery_id,
                    "decision": decision["decision"],
                    "scope_tags": list(decision["scope_tags"]),
                }],
            },
        }
        filename = task_filename(task_id)
        path = task_dir / filename
        core.write_json(path, task)
        tasks_meta.append({
            "evidence_task_id": task_id,
            "path": f"tasks/{filename}",
            "sha256": core.sha256_file(path),
            "discovery_ids": [discovery_id],
        })

    package = {
        "schema_version": "2.0-rc1",
        "issue_id": issue_id,
        "research_profile": profile["research_profile"],
        "basis": {
            "profile_path": _rel(repo_root, profile_path),
            "profile_sha256": core.sha256_file(profile_path),
            "state_path": _rel(repo_root, state_path),
            "state_sha256": core.sha256_file(state_path),
            "discovery_path": _rel(repo_root, discovery_path),
            "discovery_sha256": core.sha256_file(discovery_path),
            "screening_acceptance_path": _rel(repo_root, screening_acceptance_path),
            "screening_acceptance_sha256": core.sha256_file(screening_acceptance_path),
        },
        "prompt": {"path": str(PROMPT_PATH), "sha256": core.sha256_file(repo_root / PROMPT_PATH)},
        "contracts": {
            "task": {"path": str(TASK_SCHEMA), "sha256": core.sha256_file(repo_root / TASK_SCHEMA)},
            "card": {"path": str(CARD_SCHEMA), "sha256": core.sha256_file(repo_root / CARD_SCHEMA)},
        },
        "tasks": tasks_meta,
        "expected_outputs": {"one_result_per_task": True, "filename_pattern": "<evidence_task_id>.json"},
        "rules": [
            "Factual Evidence contains no Weekly why_now or Candidate Selection recommendation.",
            "Every event/claim/metric/limitation binds an explicit subject entity.",
            "Comparator values remain bound to comparator entities.",
            "Only a complete exact one-result-per-task set may be accepted.",
        ],
    }
    package_path = output_dir / "package.json"
    core.write_json(package_path, package)
    return package_path


def validate_evidence_card(card: dict[str, Any], task: dict[str, Any], task_sha: str, package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(card) != CARD_KEYS:
        errors.append("Evidence Card top-level fields must exactly match factual v2 contract; editorial fields are forbidden")
        return errors
    if card.get("schema_version") != "2.0-rc1":
        errors.append("Evidence Card schema_version mismatch")
    if card.get("issue_id") != task.get("issue_id") or card.get("evidence_task_id") != task.get("evidence_task_id"):
        errors.append("Evidence Card task identity mismatch")
    expected_basis = {
        "task_sha256": task_sha,
        "screening_acceptance_sha256": task["screening_basis"]["screening_acceptance_sha256"],
        "prompt_sha256": package["prompt"]["sha256"],
        "result_contract_sha256": package["contracts"]["card"]["sha256"],
    }
    if card.get("basis") != expected_basis:
        errors.append("Evidence Card basis hashes do not match exact task/package")
    if card.get("status") not in {"VERIFIED", "PARTIAL", "REJECTED", "NEEDS_MORE"}:
        errors.append("Evidence Card status invalid")

    entities = card.get("entities")
    if not isinstance(entities, list) or not entities:
        errors.append("Evidence Card requires at least one entity")
        return errors
    entity_ids = [e.get("entity_id") for e in entities if isinstance(e, dict)]
    if len(entity_ids) != len(entities) or any(not isinstance(x, str) or not x for x in entity_ids) or len(entity_ids) != len(set(entity_ids)):
        errors.append("Evidence Card entity_id values must be unique non-empty strings")
        return errors
    entity_set = set(entity_ids)
    artifact = card.get("artifact")
    if not isinstance(artifact, dict) or artifact.get("primary_subject_id") not in entity_set:
        errors.append("artifact.primary_subject_id must reference a registered entity")

    sources = card.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("Evidence Card requires at least one source")
        return errors
    source_ids = [s.get("source_id") for s in sources if isinstance(s, dict)]
    if len(source_ids) != len(sources) or any(not isinstance(x, str) or not x for x in source_ids) or len(source_ids) != len(set(source_ids)):
        errors.append("Evidence Card source_id values must be unique non-empty strings")
        return errors
    source_set = set(source_ids)

    def check_refs(subject_id: Any, refs: Any, label: str) -> None:
        if subject_id not in entity_set:
            errors.append(f"{label} subject_id is not a registered entity")
        if not isinstance(refs, list) or not refs or any(ref not in source_set for ref in refs):
            errors.append(f"{label} source_ids must reference registered sources")

    temporal = card.get("temporal")
    if not isinstance(temporal, dict):
        errors.append("temporal must be an object")
    else:
        try:
            core.parse_instant(str(temporal.get("observed_at", "")))
        except ValueError:
            errors.append("temporal.observed_at must be offset-aware")
        for event in temporal.get("events", []):
            if not isinstance(event, dict):
                errors.append("temporal event must be an object")
                continue
            check_refs(event.get("subject_id"), event.get("source_ids"), f"event {event.get('event_id')}")

    for collection_name in ("claims", "limitations"):
        values = card.get(collection_name)
        if not isinstance(values, list):
            errors.append(f"{collection_name} must be an array")
            continue
        for item in values:
            if not isinstance(item, dict):
                errors.append(f"{collection_name} item must be an object")
                continue
            if item.get("evidence_class") not in EVIDENCE_CLASSES:
                errors.append(f"{collection_name} evidence_class invalid")
            check_refs(item.get("subject_id"), item.get("source_ids"), f"{collection_name} {item.get('statement_id')}")

    metrics = card.get("metrics")
    if not isinstance(metrics, list):
        errors.append("metrics must be an array")
    else:
        for metric in metrics:
            if not isinstance(metric, dict):
                errors.append("metric must be an object")
                continue
            if metric.get("evidence_class") not in EVIDENCE_CLASSES:
                errors.append("metric evidence_class invalid")
            subject = metric.get("subject_id")
            check_refs(subject, metric.get("source_ids"), f"metric {metric.get('metric_id')}")
            comparators = metric.get("comparison_subject_ids")
            if not isinstance(comparators, list) or any(x not in entity_set for x in comparators):
                errors.append(f"metric {metric.get('metric_id')} comparison_subject_ids must reference registered entities")
            elif subject in comparators:
                errors.append(f"metric {metric.get('metric_id')} cannot list its own subject as comparator")

    verification = card.get("verification")
    if not isinstance(verification, dict):
        errors.append("verification must be an object")
    else:
        for target in verification.get("targets", []):
            if not isinstance(target, dict):
                errors.append("verification target must be an object")
                continue
            subjects = target.get("subject_ids")
            refs = target.get("source_ids")
            if not isinstance(subjects, list) or any(x not in entity_set for x in subjects):
                errors.append("verification subject_ids must reference registered entities")
            if not isinstance(refs, list) or any(x not in source_set for x in refs):
                errors.append("verification source_ids must reference registered sources")
    return errors


def validate_evidence_package_basis(repo_root: Path, package_path: Path, package: dict[str, Any], implementation_sha: str) -> None:
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    basis = package["basis"]
    for path_key, sha_key in (
        ("profile_path", "profile_sha256"), ("state_path", "state_sha256"),
        ("discovery_path", "discovery_sha256"), ("screening_acceptance_path", "screening_acceptance_sha256"),
    ):
        path = repo_root / basis[path_key]
        if not path.is_file() or core.sha256_file(path) != basis[sha_key]:
            raise ValueError(f"Evidence package basis drift: {sha_key}")
    for meta in (package["prompt"], package["contracts"]["task"], package["contracts"]["card"]):
        path = repo_root / meta["path"]
        if not path.is_file() or core.sha256_file(path) != meta["sha256"]:
            raise ValueError(f"Evidence contract drift: {meta['path']}")
    state = core.load_json(repo_root / basis["state_path"])
    core.verify_state_basis(repo_root, cfg, state, implementation_sha)


def accept_evidence_results(
    repo_root: Path,
    package_path: Path,
    results_dir: Path,
    accepted_root: Path,
    implementation_sha: str,
) -> Path:
    package = core.load_json(package_path)
    validate_evidence_package_basis(repo_root, package_path, package, implementation_sha)
    package_dir = package_path.parent
    expected = {Path(task["path"]).name for task in package["tasks"]}
    actual = {path.name for path in results_dir.glob("*.json") if path.is_file()}
    if actual != expected:
        raise ValueError(f"Evidence result set must be complete and exact: missing={sorted(expected-actual)} extra={sorted(actual-expected)}")
    entries: list[dict[str, Any]] = []
    task_map: dict[str, list[str]] = {}
    for meta in package["tasks"]:
        task_path = package_dir / meta["path"]
        if core.sha256_file(task_path) != meta["sha256"]:
            raise ValueError(f"Evidence Task bytes changed: {meta['evidence_task_id']}")
        task = core.load_json(task_path)
        result_path = results_dir / Path(meta["path"]).name
        card = core.load_json(result_path)
        errors = validate_evidence_card(card, task, meta["sha256"], package)
        if errors:
            raise ValueError(f"Evidence Card {meta['evidence_task_id']} invalid: {'; '.join(errors)}")
        entries.append({
            "evidence_task_id": meta["evidence_task_id"],
            "discovery_ids": list(meta["discovery_ids"]),
            "sha256": core.sha256_file(result_path),
            "status": card["status"],
            "filename": result_path.name,
        })
        task_map[meta["evidence_task_id"]] = list(meta["discovery_ids"])
    result_set_sha = core.sha256_object({"package_sha256": core.sha256_file(package_path), "results": sorted(entries, key=lambda x: x["evidence_task_id"])})
    run_dir = accepted_root / result_set_sha
    if run_dir.exists():
        raise ValueError(f"accepted Evidence result set already exists: {run_dir}")
    (run_dir / "results").mkdir(parents=True)
    shutil.copy2(package_path, run_dir / "package.json")
    for meta in package["tasks"]:
        shutil.copy2(results_dir / Path(meta["path"]).name, run_dir / "results" / Path(meta["path"]).name)
    acceptance = {
        "schema_version": "2.0-rc1",
        "issue_id": package["issue_id"],
        "research_profile": package["research_profile"],
        "result_set_sha256": result_set_sha,
        "package_sha256": core.sha256_file(package_path),
        "screening_acceptance_sha256": package["basis"]["screening_acceptance_sha256"],
        "result_count": len(entries),
        "results": sorted(entries, key=lambda x: x["evidence_task_id"]),
    }
    path = run_dir / "evidence-accepted.json"
    core.write_json(path, acceptance)
    return path


def validate_edition_view(view: dict[str, Any], profile: dict[str, Any], evidence_sha: str) -> list[str]:
    errors: list[str] = []
    required = {"schema_version", "issue_id", "research_profile", "evidence_task_id", "evidence_sha256", "materiality", "scope_dimensions", "profile_annotations"}
    if set(view) != required:
        errors.append("Edition Evidence View fields must exactly match v2 contract")
        return errors
    if view.get("schema_version") != "2.0-rc1" or view.get("issue_id") != profile["issue_id"] or view.get("research_profile") != profile["research_profile"]:
        errors.append("Edition Evidence View identity mismatch")
    if view.get("evidence_sha256") != evidence_sha:
        errors.append("Edition Evidence View does not bind exact factual Evidence bytes")
    materiality = view.get("materiality")
    if not isinstance(materiality, dict) or set(materiality) != {"status", "rationale"} or materiality.get("status") not in VIEW_MATERIALITY or not isinstance(materiality.get("rationale"), str) or not materiality["rationale"].strip():
        errors.append("Edition Evidence View materiality invalid")
    dims = view.get("scope_dimensions")
    allowed_dims = set(profile["research_scope"]["scope_dimensions"])
    if not isinstance(dims, list) or len(dims) != len(set(dims)) or any(x not in allowed_dims for x in dims):
        errors.append("Edition Evidence View scope_dimensions must come from Production Profile")
    ann = view.get("profile_annotations")
    if not isinstance(ann, dict):
        errors.append("profile_annotations must be an object")
        return errors
    research_profile = profile["research_profile"]
    if research_profile == "WEEKLY":
        expected = {"why_this_issue", "window_relation", "carry_over"}
        if set(ann) != expected or not isinstance(ann.get("why_this_issue"), str) or not ann.get("why_this_issue", "").strip() or not isinstance(ann.get("carry_over"), bool):
            errors.append("Weekly Edition View annotations invalid")
        if ann.get("window_relation") not in {"MAIN_EVENT", "PRE_WINDOW_RELEVANCE", "POST_CUTOFF", "CARRY_OVER", "OTHER"}:
            errors.append("Weekly window_relation invalid")
    elif research_profile == "THEMATIC":
        expected = {"lineage_role", "branch_ids", "transition_ids", "inheritance_note", "historical_attribution_caveat"}
        if set(ann) != expected:
            errors.append("Thematic Edition View annotations invalid")
        if ann.get("lineage_role") not in {"CORE", "BRIDGE", "CONTEXT", "PARALLEL", "COMPETING", "COUNTEREXAMPLE"}:
            errors.append("Thematic lineage_role invalid")
        for key in ("branch_ids", "transition_ids"):
            vals = ann.get(key)
            if not isinstance(vals, list) or len(vals) != len(set(vals)) or any(not isinstance(x, str) or not x for x in vals):
                errors.append(f"Thematic {key} invalid")
        for key in ("inheritance_note", "historical_attribution_caveat"):
            if ann.get(key) is not None and not isinstance(ann.get(key), str):
                errors.append(f"Thematic {key} must be string or null")
    elif research_profile == "RETROSPECTIVE_PERIOD":
        expected = {"period_role", "chronology_relevance"}
        if set(ann) != expected or not isinstance(ann.get("period_role"), str) or not isinstance(ann.get("chronology_relevance"), bool):
            errors.append("Period Edition View annotations invalid")
    return errors


def accept_edition_views(
    repo_root: Path,
    profile_path: Path,
    evidence_acceptance_path: Path,
    views_dir: Path,
    accepted_root: Path,
) -> Path:
    profile = core.load_json(profile_path)
    evidence_acceptance = core.load_json(evidence_acceptance_path)
    expected = {entry["evidence_task_id"]: entry for entry in evidence_acceptance["results"]}
    files = {path.stem: path for path in views_dir.glob("*.json") if path.is_file()}
    expected_file_keys = {hashlib.sha256(task_id.encode("utf-8")).hexdigest()[:20] for task_id in expected}
    if set(files) != expected_file_keys:
        raise ValueError("Edition Evidence View set must contain exactly one view per Evidence Task")
    rows: list[dict[str, Any]] = []
    for task_id, entry in expected.items():
        key = hashlib.sha256(task_id.encode("utf-8")).hexdigest()[:20]
        path = files[key]
        view = core.load_json(path)
        if view.get("evidence_task_id") != task_id:
            raise ValueError(f"Edition View filename/task mismatch: {task_id}")
        errors = validate_edition_view(view, profile, entry["sha256"])
        if errors:
            raise ValueError(f"Edition Evidence View {task_id} invalid: {'; '.join(errors)}")
        rows.append({
            "evidence_task_id": task_id,
            "evidence_sha256": entry["sha256"],
            "view_sha256": core.sha256_file(path),
            "materiality": view["materiality"]["status"],
            "scope_dimensions": list(view["scope_dimensions"]),
        })
    view_set_sha = core.sha256_object(sorted(rows, key=lambda x: x["evidence_task_id"]))
    run_dir = accepted_root / view_set_sha
    if run_dir.exists():
        raise ValueError(f"accepted Edition View set already exists: {run_dir}")
    (run_dir / "views").mkdir(parents=True)
    for path in views_dir.glob("*.json"):
        shutil.copy2(path, run_dir / "views" / path.name)
    acceptance = {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "view_set_sha256": view_set_sha,
        "profile_sha256": core.sha256_file(profile_path),
        "evidence_acceptance_sha256": core.sha256_file(evidence_acceptance_path),
        "views": sorted(rows, key=lambda x: x["evidence_task_id"]),
    }
    path = run_dir / "edition-views-accepted.json"
    core.write_json(path, acceptance)
    return path


def build_materiality_ledger(
    profile_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    evidence_acceptance_path: Path,
    views_acceptance_path: Path,
) -> dict[str, Any]:
    profile = core.load_json(profile_path)
    discoveries = screening.read_jsonl(discovery_path)
    screening_acceptance = core.load_json(screening_acceptance_path)
    evidence_acceptance = core.load_json(evidence_acceptance_path)
    views_acceptance = core.load_json(views_acceptance_path)
    screening_map = {row["discovery_id"]: row for row in screening_acceptance["decisions"]}
    evidence_by_discovery: dict[str, list[str]] = {}
    for row in evidence_acceptance["results"]:
        for discovery_id in row["discovery_ids"]:
            evidence_by_discovery.setdefault(discovery_id, []).append(row["evidence_task_id"])
    view_map = {row["evidence_task_id"]: row["materiality"] for row in views_acceptance["views"]}
    rows: list[dict[str, Any]] = []
    for discovery in discoveries:
        discovery_id = discovery["discovery_id"]
        decision = screening_map.get(discovery_id)
        if decision is None:
            raise ValueError(f"silent drop: discovery lacks Screening disposition: {discovery_id}")
        tasks = sorted(evidence_by_discovery.get(discovery_id, []))
        statuses = sorted({view_map[task] for task in tasks if task in view_map})
        if decision["decision"] == "DROP":
            if tasks:
                raise ValueError(f"DROP discovery unexpectedly has Evidence task: {discovery_id}")
            if decision.get("duplicate_group"):
                disposition = "DUPLICATE"
                duplicate_target = decision["duplicate_group"]
            else:
                disposition = "EXCLUDED"
                duplicate_target = None
            rationale = decision["reason"]
        else:
            if not tasks:
                raise ValueError(f"silent drop: non-DROP discovery lacks Evidence task: {discovery_id}")
            if len(statuses) != len(set(statuses)) or not statuses:
                raise ValueError(f"Evidence discovery lacks Edition View materiality: {discovery_id}")
            disposition = "HOLD" if statuses == ["HOLD"] else "EVIDENCE"
            duplicate_target = None
            rationale = f"Screening={decision['decision']}; Edition View={','.join(statuses)}"
        rows.append({
            "discovery_id": discovery_id,
            "origin": discovery["provenance"]["origin"],
            "screening_decision": decision["decision"],
            "downstream_disposition": disposition,
            "evidence_task_ids": tasks,
            "evidence_view_statuses": statuses,
            "duplicate_target": duplicate_target,
            "rationale": rationale,
        })
    ledger = {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "basis": {
            "discovery_sha256": core.sha256_file(discovery_path),
            "screening_acceptance_sha256": core.sha256_file(screening_acceptance_path),
            "evidence_set_sha256": evidence_acceptance["result_set_sha256"],
            "edition_view_set_sha256": views_acceptance["view_set_sha256"],
        },
        "rows": sorted(rows, key=lambda x: x["discovery_id"]),
    }
    validate_materiality_ledger(ledger, discoveries, screening_acceptance, evidence_acceptance, views_acceptance)
    return ledger


def validate_materiality_ledger(
    ledger: dict[str, Any],
    discoveries: list[dict[str, Any]],
    screening_acceptance: dict[str, Any],
    evidence_acceptance: dict[str, Any],
    views_acceptance: dict[str, Any],
) -> None:
    expected_ids = {row["discovery_id"] for row in discoveries}
    rows = ledger.get("rows")
    if not isinstance(rows, list):
        raise ValueError("Materiality Ledger rows missing")
    actual_ids = [row.get("discovery_id") for row in rows if isinstance(row, dict)]
    if len(actual_ids) != len(set(actual_ids)) or set(actual_ids) != expected_ids:
        raise ValueError("Materiality Ledger must contain exactly one row per discovery; silent drop/extra row detected")
    screening_ids = {row["discovery_id"] for row in screening_acceptance["decisions"]}
    if screening_ids != expected_ids:
        raise ValueError("Screening/Discovery set mismatch")
    evidence_tasks = {row["evidence_task_id"] for row in evidence_acceptance["results"]}
    view_tasks = {row["evidence_task_id"] for row in views_acceptance["views"]}
    if evidence_tasks != view_tasks:
        raise ValueError("every accepted Evidence task requires exactly one Edition View")
    for row in rows:
        disposition = row.get("downstream_disposition")
        tasks = row.get("evidence_task_ids")
        statuses = row.get("evidence_view_statuses")
        if disposition in {"EVIDENCE", "HOLD"}:
            if not tasks or any(task not in evidence_tasks for task in tasks):
                raise ValueError(f"Materiality row {row.get('discovery_id')} has invalid Evidence task refs")
            if not statuses:
                raise ValueError(f"Materiality row {row.get('discovery_id')} lacks Edition View disposition")
        elif disposition in {"EXCLUDED", "DUPLICATE"}:
            if tasks or statuses:
                raise ValueError(f"excluded/duplicate row {row.get('discovery_id')} must not silently retain Evidence refs")
        else:
            raise ValueError(f"Materiality row {row.get('discovery_id')} has invalid downstream disposition")
        if any(status in {"MATERIAL", "CONTEXT"} for status in statuses) and disposition not in {"EVIDENCE", "HOLD"}:
            raise ValueError(f"material discovery silently disappeared: {row.get('discovery_id')}")


def validate_completeness(result: dict[str, Any], profile_path: Path, ledger_path: Path) -> list[str]:
    errors: list[str] = []
    profile = core.load_json(profile_path)
    ledger = core.load_json(ledger_path)
    required = {"schema_version", "issue_id", "research_profile", "basis", "overall_status", "obligations", "residual_limitations", "closure"}
    if set(result) != required:
        return ["Completeness fields must exactly match v2 contract"]
    if result.get("schema_version") != "2.0-rc1" or result.get("issue_id") != profile["issue_id"] or result.get("research_profile") != profile["research_profile"]:
        errors.append("Completeness identity mismatch")
    if result.get("basis") != {"production_profile_sha256": core.sha256_file(profile_path), "materiality_ledger_sha256": core.sha256_file(ledger_path)}:
        errors.append("Completeness basis hashes do not match exact Profile/Ledger")
    obligations = result.get("obligations")
    if not isinstance(obligations, list):
        errors.append("Completeness obligations must be an array")
        return errors
    ids: list[str] = []
    ledger_discovery_ids = {row["discovery_id"] for row in ledger["rows"]}
    ledger_task_ids = {task for row in ledger["rows"] for task in row["evidence_task_ids"]}
    for obligation in obligations:
        if not isinstance(obligation, dict):
            errors.append("Completeness obligation must be an object")
            continue
        oid = obligation.get("obligation_id")
        if not isinstance(oid, str) or not oid:
            errors.append("Completeness obligation_id invalid")
        else:
            ids.append(oid)
        if obligation.get("status") not in OBLIGATION_STATUS:
            errors.append(f"Completeness obligation {oid} has invalid status")
        if any(x not in ledger_discovery_ids for x in obligation.get("discovery_ids", [])):
            errors.append(f"Completeness obligation {oid} references unknown discovery")
        if any(x not in ledger_task_ids for x in obligation.get("evidence_task_ids", [])):
            errors.append(f"Completeness obligation {oid} references unknown Evidence task")
    if len(ids) != len(set(ids)):
        errors.append("Completeness obligation_id values must be unique")
    dimensions = set(profile["research_scope"]["scope_dimensions"])
    covered_dimensions = {o.get("dimension") for o in obligations if isinstance(o, dict)}
    if dimensions - covered_dimensions:
        errors.append(f"Completeness lacks obligations for Profile dimensions: {sorted(dimensions-covered_dimensions)}")
    needs_research = sum(1 for o in obligations if isinstance(o, dict) and o.get("status") == "NEEDS_RESEARCH")
    limitations = [o for o in obligations if isinstance(o, dict) and o.get("status") == "LIMITATION"]
    residual = result.get("residual_limitations")
    if not isinstance(residual, list) or any(not isinstance(x, str) or not x for x in residual):
        errors.append("residual_limitations invalid")
        residual = []
    expected_status = "INCOMPLETE" if needs_research else ("LIMITED" if limitations or residual else "READY")
    if result.get("overall_status") != expected_status:
        errors.append(f"overall_status must be {expected_status} for current obligations/limitations")

    closure = result.get("closure")
    if profile["research_profile"] == "THEMATIC":
        if not isinstance(closure, dict):
            errors.append("Thematic Completeness requires closure/saturation evidence")
        else:
            required_closure = {"expansion_passes", "final_pass_new_sources", "final_pass_new_material_obligations", "final_pass_new_material_obligations_open", "targeted_gap_fill_completed", "open_material_obligations", "limitations", "status"}
            if set(closure) != required_closure:
                errors.append("Thematic closure fields invalid")
            else:
                if not isinstance(closure["expansion_passes"], int) or closure["expansion_passes"] < 1:
                    errors.append("Thematic closure requires at least one expansion pass")
                if not closure["targeted_gap_fill_completed"] and closure["status"] in {"COMPLETE", "LIMITED"}:
                    errors.append("Thematic closure cannot finish before targeted residual gap-fill")
                if closure["open_material_obligations"] != needs_research:
                    errors.append("Thematic closure open_material_obligations must equal unresolved material obligations")
                if closure["final_pass_new_material_obligations_open"] > closure["final_pass_new_material_obligations"]:
                    errors.append("final-pass open material obligations cannot exceed new material obligations")
                if closure["status"] in {"COMPLETE", "LIMITED"}:
                    if closure["open_material_obligations"] != 0 or closure["final_pass_new_material_obligations_open"] != 0:
                        errors.append("Thematic closure cannot complete with open material obligations")
                expected_closure = "NEEDS_RESEARCH" if expected_status == "INCOMPLETE" else ("LIMITED" if expected_status == "LIMITED" else "COMPLETE")
                if closure["status"] != expected_closure:
                    errors.append(f"Thematic closure status must be {expected_closure}")
                if closure["status"] == "COMPLETE" and closure["limitations"]:
                    errors.append("COMPLETE Thematic closure cannot retain unresolved limitations")
                if closure["status"] == "LIMITED" and not closure["limitations"]:
                    errors.append("LIMITED Thematic closure must state limitations")
    else:
        if closure is not None:
            errors.append(f"{profile['research_profile']} Completeness does not use Thematic closure payload")
    return errors
