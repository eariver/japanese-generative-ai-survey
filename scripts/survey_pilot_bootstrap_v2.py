#!/usr/bin/env python3
"""Repository-owned W33/SP001 bootstrap for Survey Production Core v2.

`plan` is side-effect free. `initialize` is the only operation that creates the
Production Profile/State and delegates all state construction to the canonical
Core v2 implementation. Pilot scope is loaded from a schema-validated registry;
chat history is never a launch authority.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

PILOT_REGISTRY = Path("config/survey-production-v2-pilots.json")
PILOT_SCHEMA = Path("schemas/pilot-bootstrap-v2.schema.json")


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


def _materialize_profile(
    repo_root: Path,
    cfg: dict[str, Any],
    pilot: dict[str, Any],
    recorded_at: datetime,
) -> dict[str, Any]:
    kind = pilot["kind"]
    scope = pilot["research_scope"]
    if kind == "WEEKLY":
        profile = core.weekly_profile(repo_root, cfg, recorded_at, pilot["issue_id"])
        cutoff = profile["research_scope"]["temporal_policy"]["cutoff"]
        if cutoff != scope["expected_cutoff"]:
            raise ValueError(
                f"Pilot {pilot['pilot_id']} Weekly cutoff drift: expected={scope['expected_cutoff']} actual={cutoff}"
            )
    elif kind == "THEMATIC":
        if scope.get("as_of_policy") != "SET_AT_INITIALIZATION":
            raise ValueError("Thematic Pilot requires SET_AT_INITIALIZATION as_of policy")
        spec = {
            "issue_id": pilot["issue_id"],
            "question": scope["question"],
            "temporal_mode": scope["temporal_mode"],
            "as_of": core.iso_utc(recorded_at),
            "scope_dimensions": list(scope["scope_dimensions"]),
            "initial_obligations": [dict(row) for row in scope["initial_obligations"]],
        }
        profile = core.thematic_profile(repo_root, cfg, spec)
    else:
        raise ValueError(f"unsupported Pilot kind: {kind}")

    if profile["issue_id"] != pilot["issue_id"]:
        raise ValueError("materialized Pilot Profile issue_id drift")
    if profile["research_profile"] != pilot["research_profile"]:
        raise ValueError("materialized Pilot research_profile drift")
    if profile["publication_profile"] != pilot["publication_profile"]:
        raise ValueError("materialized Pilot publication_profile drift")
    if profile["paths"] != pilot["expected_paths"]:
        raise ValueError("materialized Pilot canonical path/work-branch drift")
    if profile["research_scope"]["temporal_policy"]["mode"] != scope["temporal_mode"]:
        raise ValueError("materialized Pilot temporal mode drift")
    return profile


def _existing_status(repo_root: Path, cfg: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "Pilot source_root")
    profile_path = source_root / cfg["state_authority"]["profile_filename"]
    state_path = source_root / cfg["state_authority"]["authoritative_filename"]
    profile_exists = profile_path.is_file()
    state_exists = state_path.is_file()
    if profile_exists != state_exists:
        return {
            "status": "PARTIAL_INITIALIZATION_EXCEPTION",
            "profile_path": str(profile_path.relative_to(repo_root)),
            "state_path": str(state_path.relative_to(repo_root)),
            "profile_exists": profile_exists,
            "state_exists": state_exists,
            "lifecycle_state": None,
        }
    if not profile_exists:
        return {
            "status": "READY_TO_INITIALIZE",
            "profile_path": str(profile_path.relative_to(repo_root)),
            "state_path": str(state_path.relative_to(repo_root)),
            "profile_exists": False,
            "state_exists": False,
            "lifecycle_state": None,
        }

    existing_profile = core.load_json(profile_path)
    if existing_profile != profile:
        raise ValueError("existing Pilot Production Profile differs from registry/materialized Profile")
    state = core.load_json(state_path)
    if state.get("profile", {}).get("path") != str(profile_path.relative_to(repo_root)):
        raise ValueError("existing Pilot Production State points at a different Profile path")
    if state.get("profile", {}).get("sha256") != core.sha256_file(profile_path):
        raise ValueError("existing Pilot Production State/Profile SHA divergence")
    semantic_errors = core.validate_state_semantics(repo_root, cfg, state)
    if semantic_errors:
        raise ValueError("existing Pilot Production State semantic inconsistency: " + "; ".join(semantic_errors))
    return {
        "status": "RESUME_EXISTING_STATE",
        "profile_path": str(profile_path.relative_to(repo_root)),
        "state_path": str(state_path.relative_to(repo_root)),
        "profile_exists": True,
        "state_exists": True,
        "lifecycle_state": state["lifecycle_state"],
    }


def build_plan(repo_root: Path, pilot_id: str, recorded_at: datetime) -> dict[str, Any]:
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    registry = _load_registry(repo_root)
    pilot = _pilot(registry, pilot_id)
    profile = _materialize_profile(repo_root, cfg, pilot, recorded_at)
    existing = _existing_status(repo_root, cfg, profile)
    return {
        "schema_version": "2.0-rc1",
        "pilot_id": pilot_id,
        "recorded_at": core.iso_utc(recorded_at),
        "target_gate": pilot["target_gate"],
        "profile": profile,
        "repository_status": existing,
        "next_operation": (
            "INITIALIZE"
            if existing["status"] == "READY_TO_INITIALIZE"
            else "RESUME"
            if existing["status"] == "RESUME_EXISTING_STATE"
            else "EXCEPTION_GATE_REQUIRED"
        ),
    }


def initialize_pilot(
    repo_root: Path,
    pilot_id: str,
    recorded_at: datetime,
    implementation_sha: str | None,
) -> tuple[Path, Path]:
    plan = build_plan(repo_root, pilot_id, recorded_at)
    status = plan["repository_status"]["status"]
    if status != "READY_TO_INITIALIZE":
        raise ValueError(f"Pilot {pilot_id} is not cleanly uninitialized: {status}")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    impl = core.repository_commit_sha(repo_root, implementation_sha)
    return core.initialize(
        repo_root,
        cfg,
        plan["profile"],
        impl,
        plan["target_gate"],
        recorded_at,
    )


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
        print(
            json.dumps(
                {
                    "profile": str(profile_path.relative_to(root)),
                    "state": str(state_path.relative_to(root)),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
