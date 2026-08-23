#!/usr/bin/env python3
"""Canonical Retrospective Period Profile materialization for Survey Production Core v2.

Configured period identity, coverage and repository paths come from the existing
Special planning authority in ``config/special-pipeline.json`` through
``special_pipeline.bootstrap_plan``. ChatGPT authors only the edition-local
research question/scope/initial obligations after reading the applicable period
guides. This module binds those two authorities and computes the Core contract
identity; it does not choose stories, Evidence, Architecture, or publication
content.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts import special_pipeline
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

SPECIAL_CONFIG = Path("config/special-pipeline.json")
SCOPE_SCHEMA = Path("schemas/retrospective-scope-spec-v2.schema.json")


def planning_authority(repo_root: Path, special_slug: str) -> tuple[dict[str, Any], dict[str, str]]:
    config_path = repo_root / SPECIAL_CONFIG
    special_cfg = core.load_json(config_path)
    plan = special_pipeline.bootstrap_plan(special_cfg, special_slug)
    authority = {
        "path": str(SPECIAL_CONFIG),
        "entry": special_slug,
        "sha256": core.sha256_file(config_path),
    }
    return plan, authority


def load_scope(repo_root: Path, spec_path: Path) -> dict[str, Any]:
    return schema_gate.load_and_validate_json(
        spec_path,
        repo_root / SCOPE_SCHEMA,
        label="Retrospective Period scope materialization",
    )


def build_profile(
    repo_root: Path,
    cfg: dict[str, Any],
    spec: dict[str, Any],
    recorded_at: datetime,
) -> dict[str, Any]:
    special_slug = spec["special_slug"]
    plan, authority = planning_authority(repo_root, special_slug)
    if spec["planning_authority"] != authority:
        raise ValueError("Retrospective scope materialization does not bind current configured-period authority bytes")
    if spec["issue_id"] != plan["special_id"]:
        raise ValueError("Retrospective scope materialization issue_id differs from configured period identity")
    if authority["entry"] != special_slug:
        raise ValueError("Retrospective scope materialization planning entry differs from special_slug")

    materialized_at = core.parse_instant(spec["materialized_at"])
    recorded_utc = recorded_at.astimezone(timezone.utc)
    if materialized_at > recorded_utc:
        raise ValueError("Retrospective scope materialization cannot be dated after initialization")
    period_end = core.parse_instant(plan["coverage"]["end"])
    if recorded_utc < period_end:
        raise ValueError("Retrospective Period cannot initialize before configured period end")

    dimensions = list(spec["scope_dimensions"])
    profile = {
        "schema_version": cfg["schema_version"],
        "issue_id": plan["special_id"],
        "research_profile": "RETROSPECTIVE_PERIOD",
        "publication_profile": "LONGFORM_SPECIAL",
        "research_scope": {
            "question": spec["question"],
            "inclusion": list(spec["inclusion"]),
            "exclusion": list(spec["exclusion"]),
            "scope_dimensions": dimensions,
            "initial_obligations": [dict(row) for row in spec["initial_obligations"]],
            "temporal_policy": {
                "mode": "BOUNDED_PERIOD",
                "start": plan["coverage"]["start"],
                "end": plan["coverage"]["end"],
                "as_of": core.iso_utc(recorded_utc),
                "timezone": plan["coverage"]["timezone"],
            },
        },
        "paths": {
            "source_root": plan["paths"]["source_root"],
            "survey_root": plan["paths"]["survey_root"],
            "work_branch": plan["branches"]["work"],
        },
        "contract": core.contract_identity(
            repo_root,
            cfg,
            "RETROSPECTIVE_PERIOD",
            "LONGFORM_SPECIAL",
        ),
    }
    errors = core.validate_profile(profile, cfg)
    if errors:
        raise ValueError("invalid generated Retrospective Period profile: " + "; ".join(errors))
    return profile


def plan_scope(repo_root: Path, special_slug: str, recorded_at: datetime) -> dict[str, Any]:
    plan, authority = planning_authority(repo_root, special_slug)
    period_end = core.parse_instant(plan["coverage"]["end"])
    if recorded_at.astimezone(timezone.utc) < period_end:
        raise ValueError("Retrospective Period cannot initialize before configured period end")
    return {
        "schema_version": "2.0-rc1",
        "issue_id": plan["special_id"],
        "special_slug": special_slug,
        "tier": plan["tier"],
        "label": plan["label"],
        "coverage": plan["coverage"],
        "paths": {
            "source_root": plan["paths"]["source_root"],
            "survey_root": plan["paths"]["survey_root"],
            "work_branch": plan["branches"]["work"],
        },
        "required_guides": list(plan["required_guides"]),
        "planning_authority": authority,
        "scope_schema": str(SCOPE_SCHEMA),
        "instruction": "ChatGPT reads the configured period and required guides, then materializes the research question, inclusion/exclusion, scope dimensions and initial obligations. This is not a Human Gate.",
    }


def _resolve_spec(repo_root: Path, value: str) -> Path:
    return core.repo_local_path(repo_root, value, "Retrospective Period scope spec")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan")
    plan.add_argument("--special-slug", required=True)
    plan.add_argument("--recorded-at")

    init = sub.add_parser("init")
    init.add_argument("--spec", required=True)
    init.add_argument("--recorded-at")
    init.add_argument("--target-gate", choices=["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"], default="ARCHITECTURE_REVIEW")
    init.add_argument("--implementation-sha")

    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    recorded_at = core.parse_instant(args.recorded_at) if args.recorded_at else datetime.now(timezone.utc)
    try:
        if args.command == "plan":
            print(json.dumps(plan_scope(repo_root, args.special_slug, recorded_at), ensure_ascii=False, indent=2))
            return 0

        cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
        spec_path = _resolve_spec(repo_root, args.spec)
        spec = load_scope(repo_root, spec_path)
        profile = build_profile(repo_root, cfg, spec, recorded_at)
        implementation_sha = core.repository_commit_sha(repo_root, args.implementation_sha)
        profile_path, state_path = core.initialize(
            repo_root,
            cfg,
            profile,
            implementation_sha,
            args.target_gate,
            recorded_at,
        )
        print(json.dumps({
            "profile": str(profile_path.relative_to(repo_root)),
            "state": str(state_path.relative_to(repo_root)),
        }, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
