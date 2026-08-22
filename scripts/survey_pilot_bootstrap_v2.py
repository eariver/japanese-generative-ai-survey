#!/usr/bin/env python3
"""Repository-owned W33/SP001 bootstrap for Survey Production Core v2.

The registry fixes launch identity, not Thematic editorial content. For SP001 the
registry points to the canonical TS-001 planning authority; ChatGPT reads that
source and materializes one schema-valid research-scope file before deterministic
initialization. `plan` remains side-effect free and ordinary scope materialization
is an internal agent action, not a Human/Exception Gate.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent_control
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

PILOT_REGISTRY = Path("config/survey-production-v2-pilots.json")
PILOT_SCHEMA = Path("schemas/pilot-bootstrap-v2.schema.json")
THEMATIC_SCOPE_SCHEMA = Path("schemas/thematic-scope-spec-v2.schema.json")


def _load_registry(repo_root: Path) -> dict[str, Any]:
    return schema_gate.load_and_validate_json(
        repo_root / PILOT_REGISTRY,
        repo_root / PILOT_SCHEMA,
        label="Core v2 Pilot bootstrap registry",
    )


def _pilot(registry: dict[str, Any], pilot_id: str) -> dict[str, Any]:
    value = registry["pilots"].get(pilot_id)
    if not isinstance(value, dict):
        raise ValueError(f"unknown Core v2 Pilot: {pilot_id}")
    if value.get("pilot_id") != pilot_id:
        raise ValueError(f"Pilot registry key/id divergence: {pilot_id}")
    return value


def _validate_profile_against_registry(profile: dict[str, Any], pilot: dict[str, Any]) -> None:
    scope = pilot["research_scope"]
    if profile.get("issue_id") != pilot["issue_id"]:
        raise ValueError("Pilot Production Profile issue_id drift")
    if profile.get("research_profile") != pilot["research_profile"]:
        raise ValueError("Pilot Production Profile research_profile drift")
    if profile.get("publication_profile") != pilot["publication_profile"]:
        raise ValueError("Pilot Production Profile publication_profile drift")
    if profile.get("paths") != pilot["expected_paths"]:
        raise ValueError("Pilot Production Profile canonical path/work-branch drift")
    research_scope = profile.get("research_scope")
    if not isinstance(research_scope, dict):
        raise ValueError("Pilot Production Profile research_scope missing")
    temporal = research_scope.get("temporal_policy")
    if not isinstance(temporal, dict) or temporal.get("mode") != scope["temporal_mode"]:
        raise ValueError("Pilot Production Profile temporal mode drift")
    if pilot["kind"] == "WEEKLY":
        if temporal.get("cutoff") != scope["expected_cutoff"]:
            raise ValueError("Pilot Weekly cutoff drift")
    elif pilot["kind"] == "THEMATIC":
        if scope.get("as_of_policy") != "SET_AT_INITIALIZATION":
            raise ValueError("Thematic Pilot requires SET_AT_INITIALIZATION as_of policy")
        if set(temporal) != {"mode", "as_of"}:
            raise ValueError("Pilot Thematic temporal policy fields drift")
        core.parse_instant(str(temporal["as_of"]))
    else:
        raise ValueError(f"unsupported Pilot kind: {pilot['kind']}")


def _scope_spec_path(repo_root: Path, pilot: dict[str, Any]) -> Path:
    return core.repo_local_path(repo_root, pilot["research_scope"]["scope_spec_path"], "Pilot thematic scope spec")


def _planning_authority(repo_root: Path, pilot: dict[str, Any]) -> tuple[Path, dict[str, str]]:
    authority = pilot["research_scope"]["planning_authority"]
    path = core.repo_local_path(repo_root, authority["path"], "Pilot planning authority")
    if not path.is_file():
        raise ValueError(f"Pilot planning authority missing: {authority['path']}")
    text = path.read_text(encoding="utf-8")
    if authority["entry"] not in text:
        raise ValueError(f"Pilot planning authority entry not found: {authority['entry']}")
    return path, {
        "path": authority["path"],
        "entry": authority["entry"],
        "sha256": core.sha256_file(path),
    }


def _load_scope_spec(repo_root: Path, pilot: dict[str, Any]) -> dict[str, Any]:
    path = _scope_spec_path(repo_root, pilot)
    scope = schema_gate.load_and_validate_json(path, repo_root / THEMATIC_SCOPE_SCHEMA, label="Thematic scope materialization")
    if scope["issue_id"] != pilot["issue_id"]:
        raise ValueError("Thematic scope materialization issue_id mismatch")
    _, current_authority = _planning_authority(repo_root, pilot)
    if scope["planning_authority"] != current_authority:
        raise ValueError("Thematic scope materialization does not bind current canonical planning authority bytes")
    dimensions = set(scope["scope_dimensions"])
    obligation_dimensions = {row["dimension"] for row in scope["initial_obligations"]}
    if not dimensions.issubset(obligation_dimensions):
        raise ValueError("Thematic scope materialization obligations do not cover every declared dimension")
    return scope


def _materialize_profile(repo_root: Path, cfg: dict[str, Any], pilot: dict[str, Any], recorded_at: datetime) -> dict[str, Any]:
    kind = pilot["kind"]
    scope = pilot["research_scope"]
    if kind == "WEEKLY":
        profile = core.weekly_profile(repo_root, cfg, recorded_at, pilot["issue_id"])
    elif kind == "THEMATIC":
        materialized = _load_scope_spec(repo_root, pilot)
        spec = {
            "issue_id": pilot["issue_id"],
            "question": materialized["question"],
            "temporal_mode": scope["temporal_mode"],
            "as_of": core.iso_utc(recorded_at),
            "inclusion": list(materialized["inclusion"]),
            "exclusion": list(materialized["exclusion"]),
            "scope_dimensions": list(materialized["scope_dimensions"]),
            "initial_obligations": [dict(row) for row in materialized["initial_obligations"]],
            **pilot["expected_paths"],
        }
        profile = core.thematic_profile(repo_root, cfg, spec)
    else:
        raise ValueError(f"unsupported Pilot kind: {kind}")
    _validate_profile_against_registry(profile, pilot)
    return profile


def _repository_status(repo_root: Path, cfg: dict[str, Any], pilot: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
    source_root = core.repo_local_path(repo_root, pilot["expected_paths"]["source_root"], "Pilot source_root")
    profile_path = source_root / cfg["state_authority"]["profile_filename"]
    state_path = source_root / cfg["state_authority"]["authoritative_filename"]
    profile_exists = profile_path.is_file()
    state_exists = state_path.is_file()
    common = {
        "profile_path": str(profile_path.relative_to(repo_root)),
        "state_path": str(state_path.relative_to(repo_root)),
        "profile_exists": profile_exists,
        "state_exists": state_exists,
    }
    if profile_exists != state_exists:
        return {**common, "status": "PARTIAL_INITIALIZATION_EXCEPTION", "lifecycle_state": None}, None
    if not profile_exists:
        return {**common, "status": "READY_TO_INITIALIZE", "lifecycle_state": None}, None
    existing_profile = core.load_json(profile_path)
    profile_errors = core.validate_profile(existing_profile, cfg)
    if profile_errors:
        raise ValueError("existing Pilot Production Profile invalid: " + "; ".join(profile_errors))
    _validate_profile_against_registry(existing_profile, pilot)
    state = core.load_json(state_path)
    if state.get("profile", {}).get("path") != common["profile_path"]:
        raise ValueError("existing Pilot Production State points at a different Profile path")
    if state.get("profile", {}).get("sha256") != core.sha256_file(profile_path):
        raise ValueError("existing Pilot Production State/Profile SHA divergence")
    agent_control.verify_agent_state_basis(repo_root, cfg, state)
    return {**common, "status": "RESUME_EXISTING_STATE", "lifecycle_state": state["lifecycle_state"]}, existing_profile


def build_plan(repo_root: Path, pilot_id: str, recorded_at: datetime) -> dict[str, Any]:
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    registry = _load_registry(repo_root)
    pilot = _pilot(registry, pilot_id)
    existing, existing_profile = _repository_status(repo_root, cfg, pilot)
    scope_materialization = None
    if existing_profile is not None:
        profile = existing_profile
    elif pilot["kind"] == "THEMATIC" and not _scope_spec_path(repo_root, pilot).is_file():
        _, authority = _planning_authority(repo_root, pilot)
        profile = None
        scope_materialization = {
            "status": "REQUIRED_INTERNAL_AGENT_ACTION",
            "planning_authority": authority,
            "scope_spec_path": pilot["research_scope"]["scope_spec_path"],
            "scope_schema": str(THEMATIC_SCOPE_SCHEMA),
            "instruction": "ChatGPT must read the named planning-authority entry and materialize the research question, inclusion/exclusion, dimensions and initial obligations. This is not a Human Gate.",
        }
    else:
        profile = _materialize_profile(repo_root, cfg, pilot, recorded_at)
    if existing["status"] == "PARTIAL_INITIALIZATION_EXCEPTION":
        operation = "EXCEPTION_GATE_REQUIRED"
    elif existing["status"] == "RESUME_EXISTING_STATE":
        operation = "RESUME"
    elif scope_materialization is not None:
        operation = "MATERIALIZE_SCOPE"
    else:
        operation = "INITIALIZE"
    return {
        "schema_version": "2.0-rc1",
        "pilot_id": pilot_id,
        "recorded_at": core.iso_utc(recorded_at),
        "target_gate": pilot["target_gate"],
        "profile": profile,
        "scope_materialization": scope_materialization,
        "repository_status": existing,
        "next_operation": operation,
    }


def initialize_pilot(repo_root: Path, pilot_id: str, recorded_at: datetime, implementation_sha: str | None) -> tuple[Path, Path]:
    plan = build_plan(repo_root, pilot_id, recorded_at)
    if plan["next_operation"] != "INITIALIZE":
        raise ValueError(f"Pilot {pilot_id} is not ready for deterministic initialization: {plan['next_operation']}")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    impl = core.repository_commit_sha(repo_root, implementation_sha)
    return core.initialize(repo_root, cfg, plan["profile"], impl, plan["target_gate"], recorded_at)


def _instant(value: str | None) -> datetime:
    return core.parse_instant(value) if value else datetime.now(timezone.utc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan")
    plan.add_argument("--pilot", required=True)
    plan.add_argument("--recorded-at")
    initialize = sub.add_parser("initialize")
    initialize.add_argument("--pilot", required=True)
    initialize.add_argument("--recorded-at")
    initialize.add_argument("--implementation-sha")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    try:
        recorded_at = _instant(args.recorded_at)
        if args.command == "plan":
            result = build_plan(root, args.pilot, recorded_at)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 2 if result["next_operation"] == "EXCEPTION_GATE_REQUIRED" else 0
        profile_path, state_path = initialize_pilot(root, args.pilot, recorded_at, args.implementation_sha)
        print(json.dumps({"profile": str(profile_path.relative_to(root)), "state": str(state_path.relative_to(root))}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
