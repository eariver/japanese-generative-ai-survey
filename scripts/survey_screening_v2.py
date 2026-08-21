#!/usr/bin/env python3
"""Discovery provenance and profile-neutral Screening for Survey Production Core v2.

This module intentionally reuses the mature v1 *mechanical* contract pattern:
immutable inputs, bounded batches, exact hashes, complete-only acceptance, and
content-addressed accepted result sets. It does not reuse Weekly semantic fields
such as why_now or fixed A-L topic lanes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Iterable

from scripts import survey_production_v2 as core

DISCOVERY_SCHEMA = Path("schemas/survey-discovery-record.schema.json")
RUN_PACKAGE_SCHEMA = Path("schemas/screening-v2-run-package.schema.json")
RESULT_SCHEMA = Path("schemas/screening-v2-batch-result.schema.json")
PROMPT_PATH = Path("config/prompts/source-screening-v2.md")

ORIGINS = {
    "BASE",
    "CARRY_OVER",
    "REFERENCE_EXPANSION",
    "SUCCESSOR_EXPANSION",
    "PARALLEL_EXPANSION",
    "COMPETING_EXPANSION",
    "BRIDGE_EXPANSION",
    "GAP_FILL",
}
EXPANSION_REQUIRING_PARENT = {
    "REFERENCE_EXPANSION",
    "SUCCESSOR_EXPANSION",
    "PARALLEL_EXPANSION",
    "COMPETING_EXPANSION",
    "BRIDGE_EXPANSION",
}
DECISIONS = {"KEEP", "MAYBE", "DROP", "INSPECT"}
CONFIDENCE = {"low", "medium", "high"}

DISCOVERY_KEYS = {"schema_version", "issue_id", "discovery_id", "provenance", "source"}
PROVENANCE_KEYS = {"origin", "research_pass", "parent_refs", "obligation_ids", "reason"}
SOURCE_KEYS = {
    "source_type",
    "collector_id",
    "collector_run_id",
    "observed_at",
    "title",
    "locator",
    "raw_paths",
    "published_at",
    "summary_text",
    "metadata",
}
DECISION_KEYS = {
    "discovery_id",
    "decision",
    "reason",
    "scope_tags",
    "duplicate_group",
    "verification_targets",
    "confidence",
}


def canonical_line(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            values.append(value)
    return values


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as fh:
        for record in records:
            fh.write(canonical_line(record))


def _exact_regular_files(directory: Path, expected: set[str], label: str) -> dict[str, Path]:
    if not directory.is_dir():
        raise ValueError(f"{label} directory missing: {directory}")
    entries = list(directory.iterdir())
    if any(path.is_symlink() for path in entries):
        raise ValueError(f"{label} may not contain symlinks")
    non_files = sorted(path.name for path in entries if not path.is_file())
    if non_files:
        raise ValueError(f"{label} may contain files only: {non_files}")
    actual = {path.name for path in entries}
    if actual != expected:
        raise ValueError(
            f"{label} must be complete and exact: missing={sorted(expected-actual)} extra={sorted(actual-expected)}"
        )
    return {path.name: path for path in entries}


def validate_discovery(record: dict[str, Any], expected_issue_id: str | None = None) -> list[str]:
    errors: list[str] = []
    extra = sorted(set(record) - DISCOVERY_KEYS)
    missing = sorted(DISCOVERY_KEYS - set(record))
    if extra:
        errors.append(f"unexpected discovery fields: {', '.join(extra)}")
    if missing:
        errors.append(f"missing discovery fields: {', '.join(missing)}")
        return errors
    if record.get("schema_version") != "2.0-rc1":
        errors.append("discovery schema_version must be 2.0-rc1")
    issue_id = record.get("issue_id")
    if not isinstance(issue_id, str) or not issue_id:
        errors.append("issue_id must be a non-empty string")
    elif expected_issue_id is not None and issue_id != expected_issue_id:
        errors.append(f"issue_id mismatch: {issue_id} != {expected_issue_id}")
    if not isinstance(record.get("discovery_id"), str) or not record["discovery_id"]:
        errors.append("discovery_id must be a non-empty string")

    provenance = record.get("provenance")
    if not isinstance(provenance, dict):
        errors.append("provenance must be an object")
    else:
        if set(provenance) != PROVENANCE_KEYS:
            errors.append("provenance fields must exactly match the v2 discovery contract")
        origin = provenance.get("origin")
        if origin not in ORIGINS:
            errors.append(f"unsupported discovery origin: {origin}")
        research_pass = provenance.get("research_pass")
        if not isinstance(research_pass, int) or research_pass < 0:
            errors.append("research_pass must be a non-negative integer")
        parents = provenance.get("parent_refs")
        obligations = provenance.get("obligation_ids")
        if not isinstance(parents, list) or any(not isinstance(x, str) or not x for x in parents):
            errors.append("parent_refs must be a list of non-empty strings")
            parents = []
        if not isinstance(obligations, list) or any(not isinstance(x, str) or not x for x in obligations):
            errors.append("obligation_ids must be a list of non-empty strings")
            obligations = []
        if isinstance(parents, list) and len(parents) != len(set(parents)):
            errors.append("parent_refs must be unique")
        if isinstance(obligations, list) and len(obligations) != len(set(obligations)):
            errors.append("obligation_ids must be unique")
        if origin in EXPANSION_REQUIRING_PARENT and not parents:
            errors.append(f"{origin} requires at least one parent_ref")
        if origin == "GAP_FILL" and not obligations:
            errors.append("GAP_FILL requires at least one obligation_id")
        if origin == "BASE" and parents:
            errors.append("BASE discovery must not claim parent_refs")
        if not isinstance(provenance.get("reason"), str) or not provenance["reason"].strip():
            errors.append("discovery provenance reason must be non-empty")

    source = record.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
    else:
        if set(source) != SOURCE_KEYS:
            errors.append("source fields must exactly match the v2 discovery contract")
        for key in ("source_type", "collector_id", "collector_run_id", "observed_at", "locator"):
            if not isinstance(source.get(key), str) or not source[key]:
                errors.append(f"source.{key} must be a non-empty string")
        try:
            core.parse_instant(str(source.get("observed_at", "")))
        except ValueError:
            errors.append("source.observed_at must be an offset-aware ISO-8601 instant")
        raw_paths = source.get("raw_paths")
        if not isinstance(raw_paths, list) or not raw_paths or any(not isinstance(x, str) or not x for x in raw_paths):
            errors.append("source.raw_paths must be a non-empty list of non-empty strings")
        if not isinstance(source.get("metadata"), dict):
            errors.append("source.metadata must be an object")
    return errors


def validate_discovery_set(records: list[dict[str, Any]], issue_id: str) -> None:
    if not records:
        raise ValueError("discovery set must not be empty")
    seen: set[str] = set()
    for idx, record in enumerate(records, start=1):
        errors = validate_discovery(record, issue_id)
        if errors:
            raise ValueError(f"discovery record {idx} invalid: {'; '.join(errors)}")
        discovery_id = record["discovery_id"]
        if discovery_id in seen:
            raise ValueError(f"duplicate discovery_id: {discovery_id}")
        seen.add(discovery_id)


def partition_batches(records: list[dict[str, Any]], max_records: int, max_json_chars: int) -> list[list[dict[str, Any]]]:
    if max_records < 1 or max_json_chars < 1:
        raise ValueError("batch limits must be positive")
    batches: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    chars = 0
    for record in records:
        size = len(canonical_line(record).decode("utf-8"))
        if size > max_json_chars:
            raise ValueError(f"single discovery record exceeds max_json_chars: {record['discovery_id']}")
        if current and (len(current) >= max_records or chars + size > max_json_chars):
            batches.append(current)
            current = []
            chars = 0
        current.append(record)
        chars += size
    if current:
        batches.append(current)
    return batches


def _rel(repo_root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(repo_root.resolve()))


def prepare_package(
    repo_root: Path,
    state_path: Path,
    discovery_path: Path,
    output_dir: Path,
    implementation_sha: str,
    max_records: int = 50,
    max_json_chars: int = 120_000,
) -> Path:
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    core.verify_state_basis(repo_root, cfg, state, implementation_sha)
    if state["lifecycle_state"] not in {"ISSUE_INITIALIZED", "DISCOVERY_COLLECTED"}:
        raise ValueError("Screening preparation requires ISSUE_INITIALIZED or DISCOVERY_COLLECTED state")
    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    issue_id = state["issue_id"]
    records = read_jsonl(discovery_path)
    validate_discovery_set(records, issue_id)

    prompt_path = repo_root / PROMPT_PATH
    result_schema_path = repo_root / RESULT_SCHEMA
    if not prompt_path.is_file() or not result_schema_path.is_file():
        raise ValueError("Screening v2 prompt/result contract files are missing")

    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"refusing to overwrite non-empty Screening package directory: {output_dir}")
    batch_dir = output_dir / "input/batches"
    batch_dir.mkdir(parents=True, exist_ok=True)
    batch_meta: list[dict[str, Any]] = []
    for index, batch in enumerate(partition_batches(records, max_records, max_json_chars), start=1):
        batch_id = f"batch-{index:03d}"
        path = batch_dir / f"{batch_id}.jsonl"
        write_jsonl(path, batch)
        batch_meta.append(
            {
                "batch_id": batch_id,
                "path": f"input/batches/{batch_id}.jsonl",
                "record_count": len(batch),
                "sha256": core.sha256_file(path),
            }
        )

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
        },
        "prompt": {"path": str(PROMPT_PATH), "sha256": core.sha256_file(prompt_path)},
        "result_contract": {"path": str(RESULT_SCHEMA), "sha256": core.sha256_file(result_schema_path)},
        "input": {
            "record_count": len(records),
            "batch_policy": {"max_records": max_records, "max_json_chars": max_json_chars},
            "batches": batch_meta,
        },
        "expected_outputs": {
            "file_pattern": "results/batch-###.json",
            "one_result_per_batch": True,
            "schema_version": "2.0-rc1",
        },
        "rules": [
            "Exactly one decision is required for every discovery record and no extra discovery_id is allowed.",
            "Core Screening uses free-form scope_tags; Weekly why_now and fixed A-L topic lanes are not result fields.",
            "Discovery provenance is not evidence of materiality; uncertain records remain INSPECT/MAYBE until verified.",
        ],
    }
    package_path = output_dir / "package.json"
    core.write_json(package_path, package)
    return package_path


def validate_decision(decision: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(decision) != DECISION_KEYS:
        errors.append("decision fields must exactly match Screening v2; Weekly why_now/topic-lane fields are forbidden")
        return errors
    if not isinstance(decision.get("discovery_id"), str) or not decision["discovery_id"]:
        errors.append("discovery_id must be non-empty")
    if decision.get("decision") not in DECISIONS:
        errors.append("decision must be KEEP/MAYBE/DROP/INSPECT")
    if not isinstance(decision.get("reason"), str) or not decision["reason"].strip():
        errors.append("reason must be non-empty")
    for key in ("scope_tags", "verification_targets"):
        values = decision.get(key)
        if not isinstance(values, list) or any(not isinstance(x, str) or not x for x in values):
            errors.append(f"{key} must be a list of non-empty strings")
        elif len(values) != len(set(values)):
            errors.append(f"{key} must be unique")
    duplicate_group = decision.get("duplicate_group")
    if duplicate_group is not None and (not isinstance(duplicate_group, str) or not duplicate_group):
        errors.append("duplicate_group must be null or a non-empty string")
    if decision.get("confidence") not in CONFIDENCE:
        errors.append("confidence must be low/medium/high")
    return errors


def expected_result_basis(repo_root: Path, package_path: Path, package: dict[str, Any], batch: dict[str, Any]) -> dict[str, str]:
    return {
        "package_sha256": core.sha256_file(package_path),
        "batch_sha256": batch["sha256"],
        "profile_sha256": package["basis"]["profile_sha256"],
        "state_sha256": package["basis"]["state_sha256"],
        "prompt_sha256": package["prompt"]["sha256"],
        "result_contract_sha256": package["result_contract"]["sha256"],
    }


def _validate_archived_screening_files(package_path: Path, package: dict[str, Any]) -> None:
    acceptance_path = package_path.parent / "screening-accepted.json"
    if not acceptance_path.is_file():
        return
    acceptance = core.load_json(acceptance_path)
    if core.sha256_file(package_path) != acceptance.get("package_sha256"):
        raise ValueError("accepted Screening package copy changed")
    batch_meta = {row.get("batch_id"): row for row in acceptance.get("batches", []) if isinstance(row, dict)}
    expected_inputs = {f"{batch['batch_id']}.jsonl" for batch in package["input"]["batches"]}
    expected_results = {f"{batch['batch_id']}.json" for batch in package["input"]["batches"]}
    input_files = _exact_regular_files(package_path.parent / "input/batches", expected_inputs, "accepted Screening input batches")
    result_files = _exact_regular_files(package_path.parent / "results", expected_results, "accepted Screening result batches")
    for batch in package["input"]["batches"]:
        batch_id = batch["batch_id"]
        if core.sha256_file(input_files[f"{batch_id}.jsonl"]) != batch["sha256"]:
            raise ValueError(f"accepted Screening input batch changed: {batch_id}")
        accepted_batch = batch_meta.get(batch_id)
        if not isinstance(accepted_batch, dict):
            raise ValueError(f"accepted Screening batch metadata missing: {batch_id}")
        if core.sha256_file(result_files[f"{batch_id}.json"]) != accepted_batch.get("result_sha256"):
            raise ValueError(f"accepted Screening result batch changed: {batch_id}")


def validate_package_basis(repo_root: Path, package_path: Path, package: dict[str, Any], implementation_sha: str) -> None:
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    basis = package["basis"]
    checks = {
        "profile_sha256": repo_root / basis["profile_path"],
        "state_sha256": repo_root / basis["state_path"],
        "discovery_sha256": repo_root / basis["discovery_path"],
    }
    for hash_key, path in checks.items():
        if path.is_symlink() or not path.is_file() or core.sha256_file(path) != basis[hash_key]:
            raise ValueError(f"Screening package basis drift: {hash_key}")
    prompt_path = repo_root / package["prompt"]["path"]
    schema_path = repo_root / package["result_contract"]["path"]
    if prompt_path.is_symlink() or not prompt_path.is_file() or core.sha256_file(prompt_path) != package["prompt"]["sha256"]:
        raise ValueError("Screening prompt contract drift")
    if schema_path.is_symlink() or not schema_path.is_file() or core.sha256_file(schema_path) != package["result_contract"]["sha256"]:
        raise ValueError("Screening result contract drift")
    state = core.load_json(repo_root / basis["state_path"])
    core.verify_state_basis(repo_root, cfg, state, implementation_sha)
    if state["issue_id"] != package["issue_id"] or state["research_profile"] != package["research_profile"]:
        raise ValueError("Screening package/state profile identity divergence")
    _validate_archived_screening_files(package_path, package)


def _validate_result_batch(
    package_path: Path,
    package: dict[str, Any],
    batch: dict[str, Any],
    result_path: Path,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    batch_id = batch["batch_id"]
    batch_path = package_path.parent / batch["path"]
    if batch_path.is_symlink() or not batch_path.is_file() or core.sha256_file(batch_path) != batch["sha256"]:
        raise ValueError(f"Screening batch bytes changed: {batch_id}")
    inputs = read_jsonl(batch_path)
    expected_ids = [row["discovery_id"] for row in inputs]
    result = core.load_json(result_path)
    if set(result) != {"schema_version", "issue_id", "batch_id", "basis", "decisions"}:
        raise ValueError(f"{batch_id}: unexpected top-level result fields")
    if result.get("schema_version") != "2.0-rc1" or result.get("issue_id") != package["issue_id"] or result.get("batch_id") != batch_id:
        raise ValueError(f"{batch_id}: result identity mismatch")
    if result.get("basis") != expected_result_basis(Path("."), package_path, package, batch):
        raise ValueError(f"{batch_id}: result basis hashes do not match package")
    decisions = result.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError(f"{batch_id}: decisions must be an array")
    decision_ids: list[str] = []
    for decision in decisions:
        if not isinstance(decision, dict):
            raise ValueError(f"{batch_id}: every decision must be an object")
        errors = validate_decision(decision)
        if errors:
            raise ValueError(f"{batch_id}/{decision.get('discovery_id')}: {'; '.join(errors)}")
        discovery_id = decision["discovery_id"]
        if discovery_id in decision_ids:
            raise ValueError(f"{batch_id}: duplicate decision for {discovery_id}")
        decision_ids.append(discovery_id)
    if set(decision_ids) != set(expected_ids) or len(decision_ids) != len(expected_ids):
        raise ValueError(f"{batch_id}: decisions must cover exactly the batch discovery IDs")
    return decisions, {
        "batch_id": batch_id,
        "input_sha256": batch["sha256"],
        "result_sha256": core.sha256_file(result_path),
        "decision_count": len(decisions),
    }


def _result_set_digest(package_sha256: str, batches: list[dict[str, Any]], decisions: list[dict[str, Any]]) -> str:
    return core.sha256_object(
        {
            "package_sha256": package_sha256,
            "batches": batches,
            "decisions": sorted(decisions, key=lambda row: row["discovery_id"]),
        }
    )


def validate_acceptance(repo_root: Path, acceptance_path: Path, implementation_sha: str) -> dict[str, Any]:
    acceptance = core.load_json(acceptance_path)
    expected_keys = {
        "schema_version", "issue_id", "research_profile", "result_set_sha256",
        "package_sha256", "record_count", "batch_count", "batches", "decisions",
    }
    if set(acceptance) != expected_keys or acceptance.get("schema_version") != "2.0-rc1":
        raise ValueError("Screening acceptance fields/schema_version invalid")
    run_dir = acceptance_path.parent
    package_path = run_dir / "package.json"
    if not package_path.is_file() or core.sha256_file(package_path) != acceptance["package_sha256"]:
        raise ValueError("accepted Screening package copy missing or changed")
    package = core.load_json(package_path)
    validate_package_basis(repo_root, package_path, package, implementation_sha)
    if package["issue_id"] != acceptance["issue_id"] or package["research_profile"] != acceptance["research_profile"]:
        raise ValueError("Screening package/acceptance identity mismatch")

    expected_results = {f"{batch['batch_id']}.json" for batch in package["input"]["batches"]}
    result_files = _exact_regular_files(run_dir / "results", expected_results, "accepted Screening result batches")
    accepted_batches: list[dict[str, Any]] = []
    flattened: list[dict[str, Any]] = []
    all_seen: set[str] = set()
    for batch in package["input"]["batches"]:
        decisions, meta = _validate_result_batch(
            package_path, package, batch, result_files[f"{batch['batch_id']}.json"]
        )
        overlap = all_seen.intersection(row["discovery_id"] for row in decisions)
        if overlap:
            raise ValueError(f"cross-batch duplicate decisions: {sorted(overlap)}")
        all_seen.update(row["discovery_id"] for row in decisions)
        flattened.extend(decisions)
        accepted_batches.append(meta)
    if acceptance["record_count"] != len(flattened) or acceptance["record_count"] != package["input"]["record_count"]:
        raise ValueError("Screening acceptance record_count mismatch")
    if acceptance["batch_count"] != len(accepted_batches) or acceptance["batches"] != accepted_batches:
        raise ValueError("Screening acceptance batch metadata mismatch")
    sorted_decisions = sorted(flattened, key=lambda row: row["discovery_id"])
    if acceptance["decisions"] != sorted_decisions:
        raise ValueError("Screening acceptance decisions differ from archived result bytes")
    digest = _result_set_digest(acceptance["package_sha256"], accepted_batches, flattened)
    if acceptance["result_set_sha256"] != digest or run_dir.name != digest:
        raise ValueError("Screening acceptance content-addressed identity mismatch")
    return acceptance


def accept_results(
    repo_root: Path,
    package_path: Path,
    results_dir: Path,
    accepted_root: Path,
    implementation_sha: str,
) -> Path:
    package = core.load_json(package_path)
    validate_package_basis(repo_root, package_path, package, implementation_sha)
    expected_files = {f"{batch['batch_id']}.json" for batch in package["input"]["batches"]}
    result_files = _exact_regular_files(results_dir, expected_files, "Screening result set")

    accepted_batches: list[dict[str, Any]] = []
    flattened: list[dict[str, Any]] = []
    all_seen: set[str] = set()
    for batch in package["input"]["batches"]:
        decisions, meta = _validate_result_batch(
            package_path, package, batch, result_files[f"{batch['batch_id']}.json"]
        )
        decision_ids = [row["discovery_id"] for row in decisions]
        overlap = all_seen.intersection(decision_ids)
        if overlap:
            raise ValueError(f"cross-batch duplicate decisions: {sorted(overlap)}")
        all_seen.update(decision_ids)
        flattened.extend(decisions)
        accepted_batches.append(meta)

    if len(flattened) != package["input"]["record_count"]:
        raise ValueError("accepted decision count does not equal discovery record count")
    package_sha = core.sha256_file(package_path)
    result_set_sha = _result_set_digest(package_sha, accepted_batches, flattened)
    run_dir = accepted_root / result_set_sha
    acceptance_path = run_dir / "screening-accepted.json"
    if run_dir.exists():
        if acceptance_path.is_file():
            validate_acceptance(repo_root, acceptance_path, implementation_sha)
            return acceptance_path
        raise ValueError(f"incomplete pre-existing Screening acceptance directory: {run_dir}")

    (run_dir / "input/batches").mkdir(parents=True)
    (run_dir / "results").mkdir(parents=True)
    shutil.copy2(package_path, run_dir / "package.json")
    for batch in package["input"]["batches"]:
        batch_id = batch["batch_id"]
        source_input = package_path.parent / batch["path"]
        shutil.copy2(source_input, run_dir / "input/batches" / f"{batch_id}.jsonl")
        shutil.copy2(result_files[f"{batch_id}.json"], run_dir / "results" / f"{batch_id}.json")
    accepted = {
        "schema_version": "2.0-rc1",
        "issue_id": package["issue_id"],
        "research_profile": package["research_profile"],
        "result_set_sha256": result_set_sha,
        "package_sha256": package_sha,
        "record_count": package["input"]["record_count"],
        "batch_count": len(accepted_batches),
        "batches": accepted_batches,
        "decisions": sorted(flattened, key=lambda row: row["discovery_id"]),
    }
    core.write_json(acceptance_path, accepted)
    validate_acceptance(repo_root, acceptance_path, implementation_sha)
    return acceptance_path


def cmd_validate_discovery(args: argparse.Namespace, repo_root: Path) -> int:
    path = Path(args.discovery)
    if not path.is_absolute():
        path = repo_root / path
    records = read_jsonl(path)
    validate_discovery_set(records, args.issue_id)
    print(json.dumps({"passed": True, "record_count": len(records)}, indent=2))
    return 0


def cmd_prepare(args: argparse.Namespace, repo_root: Path) -> int:
    state_path = Path(args.state)
    discovery_path = Path(args.discovery)
    output_dir = Path(args.output_dir)
    for name, value in (("state", state_path), ("discovery", discovery_path), ("output_dir", output_dir)):
        if not value.is_absolute():
            if name == "output_dir":
                output_dir = repo_root / value
            elif name == "state":
                state_path = repo_root / value
            else:
                discovery_path = repo_root / value
    impl = core.repository_commit_sha(repo_root, args.implementation_sha)
    package = prepare_package(repo_root, state_path, discovery_path, output_dir, impl, args.max_records, args.max_json_chars)
    print(package)
    return 0


def cmd_accept(args: argparse.Namespace, repo_root: Path) -> int:
    package_path = Path(args.package)
    results_dir = Path(args.results_dir)
    accepted_root = Path(args.accepted_root)
    if not package_path.is_absolute():
        package_path = repo_root / package_path
    if not results_dir.is_absolute():
        results_dir = repo_root / results_dir
    if not accepted_root.is_absolute():
        accepted_root = repo_root / accepted_root
    impl = core.repository_commit_sha(repo_root, args.implementation_sha)
    accepted = accept_results(repo_root, package_path, results_dir, accepted_root, impl)
    print(accepted)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-discovery")
    validate.add_argument("--issue-id", required=True)
    validate.add_argument("--discovery", required=True)

    prepare = sub.add_parser("prepare")
    prepare.add_argument("--state", required=True)
    prepare.add_argument("--discovery", required=True)
    prepare.add_argument("--output-dir", required=True)
    prepare.add_argument("--max-records", type=int, default=50)
    prepare.add_argument("--max-json-chars", type=int, default=120000)
    prepare.add_argument("--implementation-sha")

    accept = sub.add_parser("accept")
    accept.add_argument("--package", required=True)
    accept.add_argument("--results-dir", required=True)
    accept.add_argument("--accepted-root", required=True)
    accept.add_argument("--implementation-sha")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    try:
        if args.command == "validate-discovery":
            return cmd_validate_discovery(args, repo_root)
        if args.command == "prepare":
            return cmd_prepare(args, repo_root)
        if args.command == "accept":
            return cmd_accept(args, repo_root)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
