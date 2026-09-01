#!/usr/bin/env python3
"""Retrospective Period Profile/bootstrap helper for Survey Production Core v2.

This is deliberately small. It resolves configured calendar periods or accepts an
explicit bounded custom spec, constructs the generic RETROSPECTIVE_PERIOD Profile,
and delegates authoritative State initialization to survey_production_v2.
Editorial research/Architecture remain ChatGPT-owned and are guided by the
applicable period documents.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, time, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from scripts import survey_agent_control_v2 as agent_control
from scripts import survey_production_v2 as core

SPECIAL_CONFIG = Path("config/special-pipeline.json")
GRANULARITY_GUIDES = {
    "monthly": "docs/special-editions.md",
    "half_year": "docs/half-year-retrospective-specials.md",
    "annual": "docs/annual-retrospective-specials.md",
    "custom": "docs/special-editions.md",
}


def _calendar_instant(value: str, zone: ZoneInfo, *, end: bool = False) -> str:
    day = date.fromisoformat(value)
    clock = time(23, 59, 59) if end else time(0, 0, 0)
    return datetime.combine(day, clock, tzinfo=zone).isoformat(timespec="seconds")


def resolve_configured_period(repo_root: Path, special_slug: str, recorded_at: datetime) -> dict[str, Any]:
    special_cfg = core.load_json(repo_root / SPECIAL_CONFIG)
    matches: list[tuple[str, dict[str, Any]]] = []
    for granularity in ("monthly", "half_year", "annual"):
        for row in special_cfg.get("historical_granularity", {}).get(granularity, {}).get("periods", []):
            if row.get("special_slug") == special_slug:
                matches.append((granularity, row))
    if len(matches) != 1:
        raise ValueError(f"configured Retrospective Period slug must resolve exactly once: {special_slug}")
    granularity, row = matches[0]
    zone = ZoneInfo("Asia/Tokyo")
    issue_id = f"SP-{special_slug}"
    return {
        "issue_id": issue_id,
        "period_label": row["label"],
        "granularity": granularity,
        "start": _calendar_instant(row["start"], zone),
        "end": _calendar_instant(row["end"], zone, end=True),
        "as_of": core.iso_utc(recorded_at),
        "timezone": "Asia/Tokyo",
        "question": f"What materially changed in generative AI during {row['label']}, and how should the period be understood in retrospect?",
        "inclusion": ["material generative-AI developments inside the bounded period and evidence needed to explain their trajectory"],
        "exclusion": ["later facts used as if they were known inside the period; unrelated developments without retrospective explanatory value"],
        "scope_dimensions": ["period coverage", "technical developments", "ecosystem actors", "period synthesis"],
        "initial_obligations": [
            {"obligation_id": "period:coverage", "dimension": "period coverage", "description": "Audit the bounded period for temporal/source/actor coverage and record residual gaps."},
            {"obligation_id": "period:technical", "dimension": "technical developments", "description": "Identify and verify material technical developments and their within-period relationships."},
            {"obligation_id": "period:actors", "dimension": "ecosystem actors", "description": "Check that material organizations/model families/research actors are not omitted by a narrow source reconstruction."},
            {"obligation_id": "period:synthesis", "dimension": "period synthesis", "description": "Establish the period-wide trajectory and cross-feature synthesis required by the Retrospective Period Profile."}
        ],
        "source_root": f"sources/{issue_id}",
        "survey_root": f"surveys/special/{special_slug}",
        "work_branch": f"special/{special_slug}-v2-work",
        "guide": GRANULARITY_GUIDES[granularity],
    }


def period_profile(repo_root: Path, cfg: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    required = ("issue_id", "start", "end", "as_of", "timezone", "question", "scope_dimensions")
    missing = [key for key in required if not spec.get(key)]
    if missing:
        raise ValueError("period spec missing required fields: " + ", ".join(missing))
    issue_id = spec["issue_id"]
    dimensions = list(spec["scope_dimensions"])
    if not dimensions:
        raise ValueError("period scope_dimensions must not be empty")
    supplied = spec.get("initial_obligations")
    if supplied is None:
        obligations = [
            {
                "obligation_id": f"period:{index:02d}",
                "dimension": dimension,
                "description": f"Establish evidence-backed retrospective coverage for: {dimension}.",
            }
            for index, dimension in enumerate(dimensions, start=1)
        ]
    elif isinstance(supplied, list):
        obligations = [dict(row) if isinstance(row, dict) else row for row in supplied]
    else:
        raise ValueError("period initial_obligations must be an array")
    start = core.parse_instant(str(spec["start"]))
    end = core.parse_instant(str(spec["end"]))
    as_of = core.parse_instant(str(spec["as_of"]))
    if end < start:
        raise ValueError("period end must not precede start")
    if as_of < end:
        raise ValueError("Retrospective Period cannot initialize before its bounded period has ended")
    profile = {
        "schema_version": cfg["schema_version"],
        "issue_id": issue_id,
        "research_profile": "RETROSPECTIVE_PERIOD",
        "publication_profile": "LONGFORM_SPECIAL",
        "research_scope": {
            "question": spec["question"],
            "inclusion": list(spec.get("inclusion", [])),
            "exclusion": list(spec.get("exclusion", [])),
            "scope_dimensions": dimensions,
            "initial_obligations": obligations,
            "temporal_policy": {
                "mode": "BOUNDED_PERIOD",
                "start": start.isoformat(timespec="seconds"),
                "end": end.isoformat(timespec="seconds"),
                "as_of": core.iso_utc(as_of),
                "timezone": spec["timezone"],
            },
        },
        "paths": {
            "source_root": spec.get("source_root", f"sources/{issue_id}"),
            "survey_root": spec.get("survey_root", f"surveys/special/{issue_id}"),
            "work_branch": spec.get("work_branch", f"special/{issue_id}-v2-work"),
        },
        "contract": core.contract_identity(repo_root, cfg, "RETROSPECTIVE_PERIOD", "LONGFORM_SPECIAL"),
    }
    errors = core.validate_profile(profile, cfg)
    if errors:
        raise ValueError("invalid generated Retrospective Period profile: " + "; ".join(errors))
    return profile


def _stable_period_identity(profile: dict[str, Any], spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if profile.get("issue_id") != spec.get("issue_id"):
        errors.append("issue_id")
    if profile.get("research_profile") != "RETROSPECTIVE_PERIOD" or profile.get("publication_profile") != "LONGFORM_SPECIAL":
        errors.append("Profile type")
    policy = profile.get("research_scope", {}).get("temporal_policy", {})
    for key in ("start", "end", "timezone"):
        expected = spec.get(key)
        if key in {"start", "end"} and expected:
            expected = core.parse_instant(str(expected)).isoformat(timespec="seconds")
        if policy.get(key) != expected:
            errors.append(f"temporal_policy.{key}")
    expected_paths = {
        "source_root": spec.get("source_root", f"sources/{spec['issue_id']}"),
        "survey_root": spec.get("survey_root", f"surveys/special/{spec['issue_id']}"),
        "work_branch": spec.get("work_branch", f"special/{spec['issue_id']}-v2-work"),
    }
    if profile.get("paths") != expected_paths:
        errors.append("paths")
    return errors


def build_plan(repo_root: Path, cfg: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    source_root = core.repo_local_path(repo_root, spec.get("source_root", f"sources/{spec['issue_id']}"), "period source_root")
    profile_path = source_root / cfg["state_authority"]["profile_filename"]
    state_path = source_root / cfg["state_authority"]["authoritative_filename"]
    if profile_path.is_file() != state_path.is_file():
        operation = "EXCEPTION_GATE_REQUIRED"
        profile = None
    elif profile_path.is_file():
        profile = core.load_json(profile_path)
        profile_errors = core.validate_profile(profile, cfg)
        if profile_errors:
            raise ValueError("existing Retrospective Period Profile invalid: " + "; ".join(profile_errors))
        drift = _stable_period_identity(profile, spec)
        if drift:
            raise ValueError("existing Retrospective Period identity differs from requested period: " + ", ".join(drift))
        state = core.load_json(state_path)
        if state.get("profile", {}).get("path") != str(profile_path.relative_to(repo_root)) or state.get("profile", {}).get("sha256") != core.sha256_file(profile_path):
            raise ValueError("existing Retrospective Period State/Profile authority mismatch")
        agent_control.verify_agent_state_basis(repo_root, cfg, state)
        operation = "RESUME"
    else:
        profile = period_profile(repo_root, cfg, spec)
        operation = "INITIALIZE"
    return {
        "schema_version": "2.0-rc1",
        "profile": profile,
        "profile_path": str(profile_path.relative_to(repo_root)),
        "state_path": str(state_path.relative_to(repo_root)),
        "next_operation": operation,
        "guide": spec.get("guide", GRANULARITY_GUIDES.get(spec.get("granularity", "custom"), GRANULARITY_GUIDES["custom"])),
    }


def _spec_from_args(args: argparse.Namespace, repo_root: Path, recorded_at: datetime) -> dict[str, Any]:
    if args.special_slug:
        return resolve_configured_period(repo_root, args.special_slug, recorded_at)
    if not args.spec:
        raise ValueError("either --special-slug or --spec is required")
    path = Path(args.spec)
    if not path.is_absolute():
        path = repo_root / path
    return core.load_json(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("plan", "initialize"):
        cmd = sub.add_parser(name)
        group = cmd.add_mutually_exclusive_group(required=True)
        group.add_argument("--special-slug")
        group.add_argument("--spec")
        cmd.add_argument("--recorded-at")
        cmd.add_argument("--target-gate", choices=["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"], default="ARCHITECTURE_REVIEW")
        cmd.add_argument("--implementation-sha")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    try:
        cfg = core.load_json(root / core.DEFAULT_CONFIG)
        recorded_at = core.parse_instant(args.recorded_at) if args.recorded_at else datetime.now(timezone.utc)
        spec = _spec_from_args(args, root, recorded_at)
        plan = build_plan(root, cfg, spec)
        if args.command == "plan":
            print(json.dumps(plan, ensure_ascii=False, indent=2))
            return 2 if plan["next_operation"] == "EXCEPTION_GATE_REQUIRED" else 0
        if plan["next_operation"] != "INITIALIZE":
            raise ValueError(f"Retrospective Period is not cleanly uninitialized: {plan['next_operation']}")
        impl = core.repository_commit_sha(root, args.implementation_sha)
        profile_path, state_path = core.initialize(root, cfg, plan["profile"], impl, args.target_gate, recorded_at)
        print(json.dumps({"profile": str(profile_path.relative_to(root)), "state": str(state_path.relative_to(root)), "guide": plan["guide"]}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
