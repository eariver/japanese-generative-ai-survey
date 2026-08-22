#!/usr/bin/env python3
"""Accepted Discovery graph + Raw byte identity for Survey Production Core v2."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_x_intake_v2 as x_intake

DISCOVERY_ACCEPTANCE_SCHEMA = Path("schemas/discovery-acceptance-v2.schema.json")
EXPANSION_REQUIRING_PARENT = {
    "REFERENCE_EXPANSION",
    "SUCCESSOR_EXPANSION",
    "PARALLEL_EXPANSION",
    "COMPETING_EXPANSION",
    "BRIDGE_EXPANSION",
}
ORIGINS = {
    "BASE",
    "CARRY_OVER",
    *EXPANSION_REQUIRING_PARENT,
    "GAP_FILL",
}


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


def _safe_repo_file(repo_root: Path, rel: str) -> Path:
    path = Path(rel)
    if path.is_absolute():
        raise ValueError(f"Raw path must be repository-relative: {rel}")
    root = repo_root.resolve()
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Raw path escapes repository: {rel}") from exc
    if resolved.is_symlink() or not resolved.is_file():
        raise ValueError(f"Raw path missing or unsafe: {rel}")
    return resolved


def _parse_parent(ref: str, issue_id: str) -> dict[str, Any]:
    if ref.startswith("local:"):
        discovery_id = ref[len("local:") :]
        if not discovery_id or ":" in discovery_id:
            raise ValueError(f"invalid same-run parent ref: {ref}")
        return {"scope": "SAME_RUN", "ref": ref, "issue_id": issue_id, "discovery_id": discovery_id}
    if ref.startswith("external:"):
        parts = ref.split(":", 2)
        if len(parts) != 3 or not parts[1] or not parts[2]:
            raise ValueError(f"invalid external parent ref: {ref}")
        return {"scope": "EXTERNAL", "ref": ref, "issue_id": parts[1], "discovery_id": parts[2]}
    raise ValueError(
        f"parent ref must use explicit local:<discovery_id> or external:<issue_id>:<discovery_id> namespace: {ref}"
    )


def _trigger(origin: str, parent_refs: list[str], obligations: list[str]) -> dict[str, Any]:
    if origin == "BASE":
        return {"kind": "PROFILE_SEED", "refs": []}
    if origin == "CARRY_OVER":
        return {"kind": "CARRY_OVER", "refs": parent_refs}
    if origin == "GAP_FILL":
        return {"kind": "OBLIGATION_GAP", "refs": obligations}
    return {"kind": "PARENT_EDGE", "refs": parent_refs}


def _normalize_record(repo_root: Path, record: dict[str, Any], issue_id: str) -> dict[str, Any]:
    if record.get("schema_version") != "2.0-rc1" or record.get("issue_id") != issue_id:
        raise ValueError("Discovery record identity mismatch")
    discovery_id = record.get("discovery_id")
    if not isinstance(discovery_id, str) or not discovery_id:
        raise ValueError("Discovery record requires discovery_id")
    provenance = record.get("provenance")
    source = record.get("source")
    if not isinstance(provenance, dict) or not isinstance(source, dict):
        raise ValueError(f"Discovery {discovery_id} requires provenance and source objects")
    origin = provenance.get("origin")
    research_pass = provenance.get("research_pass")
    parent_refs = provenance.get("parent_refs")
    obligations = provenance.get("obligation_ids")
    if origin not in ORIGINS:
        raise ValueError(f"Discovery {discovery_id} has unsupported origin {origin}")
    if not isinstance(research_pass, int) or research_pass < 0:
        raise ValueError(f"Discovery {discovery_id} research_pass must be non-negative")
    if not isinstance(parent_refs, list) or any(not isinstance(value, str) or not value for value in parent_refs):
        raise ValueError(f"Discovery {discovery_id} parent_refs must be non-empty strings")
    if len(parent_refs) != len(set(parent_refs)):
        raise ValueError(f"Discovery {discovery_id} parent_refs must be unique")
    if not isinstance(obligations, list) or any(not isinstance(value, str) or not value for value in obligations):
        raise ValueError(f"Discovery {discovery_id} obligation_ids must be non-empty strings")
    if len(obligations) != len(set(obligations)):
        raise ValueError(f"Discovery {discovery_id} obligation_ids must be unique")
    if origin in EXPANSION_REQUIRING_PARENT and not parent_refs:
        raise ValueError(f"Discovery {discovery_id} {origin} requires parent refs")
    if origin == "GAP_FILL" and not obligations:
        raise ValueError(f"Discovery {discovery_id} GAP_FILL requires obligation ids")
    if origin == "BASE" and parent_refs:
        raise ValueError(f"Discovery {discovery_id} BASE must not have parent refs")

    edges = [_parse_parent(value, issue_id) for value in parent_refs]
    if origin == "CARRY_OVER" and (not edges or any(edge["scope"] != "EXTERNAL" for edge in edges)):
        raise ValueError(f"Discovery {discovery_id} CARRY_OVER requires only explicit external parent refs")

    raw_paths = source.get("raw_paths")
    if not isinstance(raw_paths, list) or not raw_paths or any(not isinstance(value, str) or not value for value in raw_paths):
        raise ValueError(f"Discovery {discovery_id} requires source.raw_paths")
    raw_refs: list[dict[str, Any]] = []
    for rel in raw_paths:
        raw = _safe_repo_file(repo_root, rel)
        raw_refs.append({"path": rel, "sha256": core.sha256_file(raw), "byte_count": raw.stat().st_size})

    collector_id = source.get("collector_id")
    collector_run_id = source.get("collector_run_id")
    locator = source.get("locator")
    if not isinstance(collector_id, str) or not collector_id:
        raise ValueError(f"Discovery {discovery_id} requires collector_id")
    if not isinstance(collector_run_id, str) or not collector_run_id:
        raise ValueError(f"Discovery {discovery_id} requires collector_run_id")
    if not isinstance(locator, str) or not locator:
        raise ValueError(f"Discovery {discovery_id} requires source locator")

    return {
        "discovery_id": discovery_id,
        "origin": origin,
        "research_pass": research_pass,
        "parent_edges": edges,
        "obligation_ids": obligations,
        "method": {
            "kind": origin,
            "collector_id": collector_id,
            "collector_run_id": collector_run_id,
            "trigger": _trigger(origin, parent_refs, obligations),
        },
        "source_locator": locator,
        "raw_refs": raw_refs,
    }


def _validate_graph(records: list[dict[str, Any]]) -> None:
    by_id = {record["discovery_id"]: record for record in records}
    if len(by_id) != len(records):
        raise ValueError("accepted Discovery graph has duplicate discovery_id")
    for record in records:
        for edge in record["parent_edges"]:
            if edge["scope"] != "SAME_RUN":
                continue
            parent = by_id.get(edge["discovery_id"])
            if parent is None:
                raise ValueError(
                    f"Discovery {record['discovery_id']} has dangling same-run parent {edge['discovery_id']}"
                )
            if parent["research_pass"] >= record["research_pass"]:
                raise ValueError(
                    f"Discovery {record['discovery_id']} research_pass must be greater than same-run parent {edge['discovery_id']}"
                )


def _canonical_graph_sha(records: list[dict[str, Any]]) -> str:
    return core.sha256_object(sorted(records, key=lambda value: value["discovery_id"]))


def _validate_x_integration(manifest: dict[str, Any], records: list[dict[str, Any]]) -> None:
    by_id = {record["discovery_id"]: record for record in records}
    for run in manifest.get("runs", []):
        result = run.get("result")
        if result is None:
            raise ValueError(f"completed X Source Intake run missing result: {run.get('run_id')}")
        disposition = result.get("discovery_disposition")
        discovery_ids = result.get("discovery_ids", [])
        if disposition == "NO_MATERIAL_DISCOVERY":
            if discovery_ids:
                raise ValueError(f"X run {run['run_id']} NO_MATERIAL_DISCOVERY must not name Discovery IDs")
            continue
        if disposition != "DISCOVERY_RECORDED" or not discovery_ids:
            raise ValueError(f"X run {run['run_id']} has invalid Discovery disposition")
        raw_path = result["raw"]["path"]
        for discovery_id in discovery_ids:
            record = by_id.get(discovery_id)
            if record is None:
                raise ValueError(f"X run {run['run_id']} references unknown Discovery {discovery_id}")
            if raw_path not in {ref["path"] for ref in record.get("raw_refs", [])}:
                raise ValueError(
                    f"Discovery {discovery_id} does not bind imported Grok Raw for X run {run['run_id']}"
                )


def build_acceptance(
    repo_root: Path,
    discovery_path: Path,
    x_manifest_path: Path,
    issue_id: str,
    output_path: Path,
) -> Path:
    if discovery_path.is_symlink() or not discovery_path.is_file():
        raise ValueError(f"Discovery JSONL missing or unsafe: {discovery_path}")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    x_manifest = x_intake.validate_manifest(repo_root, cfg, x_manifest_path, require_complete=True)
    if x_manifest["issue_id"] != issue_id:
        raise ValueError("X Source Intake/Discovery issue identity mismatch")
    raw_records = read_jsonl(discovery_path)
    if not raw_records:
        raise ValueError("Discovery set must not be empty")
    records = [_normalize_record(repo_root, value, issue_id) for value in raw_records]
    _validate_graph(records)
    records_sorted = sorted(records, key=lambda value: value["discovery_id"])
    _validate_x_integration(x_manifest, records_sorted)
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": issue_id,
        "x_source_intake": {
            "path": str(x_manifest_path.resolve().relative_to(repo_root.resolve())),
            "sha256": core.sha256_file(x_manifest_path),
        },
        "discovery_path": str(discovery_path.resolve().relative_to(repo_root.resolve())),
        "discovery_sha256": core.sha256_file(discovery_path),
        "record_count": len(records_sorted),
        "records": records_sorted,
        "graph_sha256": _canonical_graph_sha(records_sorted),
    }
    schema_gate.validate_instance(payload, repo_root / DISCOVERY_ACCEPTANCE_SCHEMA, label="Discovery acceptance")
    if output_path.exists():
        raise ValueError(f"refusing to overwrite Discovery acceptance: {output_path}")
    core.write_json(output_path, payload)
    validate_acceptance(repo_root, output_path)
    return output_path


def validate_acceptance(repo_root: Path, acceptance_path: Path) -> dict[str, Any]:
    payload = schema_gate.load_and_validate_json(
        acceptance_path, repo_root / DISCOVERY_ACCEPTANCE_SCHEMA, label="Discovery acceptance"
    )
    x_ref = payload["x_source_intake"]
    x_path = _safe_repo_file(repo_root, x_ref["path"])
    if core.sha256_file(x_path) != x_ref["sha256"]:
        raise ValueError("accepted X Source Intake manifest SHA drift")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    x_manifest = x_intake.validate_manifest(repo_root, cfg, x_path, require_complete=True)
    if x_manifest["issue_id"] != payload["issue_id"]:
        raise ValueError("accepted X Source Intake/Discovery issue identity mismatch")
    discovery_path = _safe_repo_file(repo_root, payload["discovery_path"])
    if core.sha256_file(discovery_path) != payload["discovery_sha256"]:
        raise ValueError("accepted Discovery JSONL SHA drift")
    raw_records = read_jsonl(discovery_path)
    rebuilt = [_normalize_record(repo_root, value, payload["issue_id"]) for value in raw_records]
    _validate_graph(rebuilt)
    rebuilt_sorted = sorted(rebuilt, key=lambda value: value["discovery_id"])
    _validate_x_integration(x_manifest, rebuilt_sorted)
    if payload["record_count"] != len(rebuilt_sorted) or payload["records"] != rebuilt_sorted:
        raise ValueError("accepted Discovery graph differs from current Discovery/Raw bytes")
    if payload["graph_sha256"] != _canonical_graph_sha(rebuilt_sorted):
        raise ValueError("accepted Discovery graph SHA mismatch")
    return payload
