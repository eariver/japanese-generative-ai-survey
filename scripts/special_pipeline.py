#!/usr/bin/env python3
"""Deterministic planning spine for Japanese Generative AI Technical Survey Special editions.

Special editions intentionally do not reuse the Weekly calendar resolver. A Special
manifest explicitly fixes its coverage window and editorial purpose, while the
later Evidence/Selection/Architecture/Freeze gates remain equivalent in spirit to
the Weekly pipeline.
"""
from __future__ import annotations

import argparse
import calendar
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = Path("config/special-pipeline.json")

LIFECYCLE = [
    "ISSUE_INITIALIZED", "DISCOVERY_COLLECTED", "CANDIDATES_NORMALIZED", "EVIDENCE_REVIEWED",
    "SELECTION_COMPLETE", "ARCHITECTURE_ESTABLISHED", "DRAFT_COMPLETE", "VALIDATED_DRAFT",
    "RELEASE_CANDIDATE", "FROZEN",
]


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_instant(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        raise ValueError(f"timestamp requires explicit timezone: {value}")
    return dt.astimezone(timezone.utc)


def iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "special_id", "special_slug", "display_label", "series_title", "edition_kind",
        "status", "coverage", "topic_scope", "community_research", "editorial_policy", "page_budget", "paths",
    }
    missing = sorted(required - set(manifest))
    if missing:
        errors.append(f"missing manifest fields: {missing}")
        return errors
    if manifest.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    special_id = manifest.get("special_id")
    if not isinstance(special_id, str) or not special_id.startswith("SP-"):
        errors.append("special_id must begin with SP-")
    if manifest.get("series_title") != "Japanese Generative AI Technical Survey Special":
        errors.append("unexpected series_title")
    kind = manifest.get("edition_kind")
    if kind not in {"RETROSPECTIVE_PERIOD", "THEMATIC"}:
        errors.append(f"unsupported edition_kind: {kind!r}")
    if kind == "RETROSPECTIVE_PERIOD" and manifest.get("topic_scope") is not None:
        errors.append("RETROSPECTIVE_PERIOD topic_scope must be null")
    if kind == "THEMATIC" and not isinstance(manifest.get("topic_scope"), str):
        errors.append("THEMATIC topic_scope must be a string")
    community = manifest.get("community_research") or {}
    if community.get("mode") not in {"DISABLED", "OPTIONAL", "ENABLED"}:
        errors.append("community_research.mode invalid")
    if kind == "RETROSPECTIVE_PERIOD" and community.get("mode") == "ENABLED":
        errors.append("retrospective editions may not require Grok/X research by default; use OPTIONAL only for exceptional historical-reaction context")
    coverage = manifest.get("coverage") or {}
    try:
        start = parse_instant(coverage["start"])
        end = parse_instant(coverage["end"])
        as_of = parse_instant(coverage["retrospective_as_of"])
        if start >= end:
            errors.append("coverage.start must be before coverage.end")
        if as_of < end:
            errors.append("retrospective_as_of must be at or after coverage.end")
    except (KeyError, TypeError, ValueError) as exc:
        errors.append(f"invalid coverage: {exc}")
    paths = manifest.get("paths") or {}
    slug = manifest.get("special_slug")
    if paths.get("work_branch") != f"special/{slug}-work":
        errors.append("work_branch must be canonical special/<slug>-work")
    if paths.get("source_root") != f"sources/{special_id}":
        errors.append("source_root must be sources/<special_id>")
    return errors


def build_plan(manifest: dict[str, Any]) -> dict[str, Any]:
    errors = validate_manifest(manifest)
    if errors:
        raise ValueError("; ".join(errors))
    coverage = manifest["coverage"]
    return {
        "schema_version": "1.0",
        "series": "SPECIAL",
        "issue_id": manifest["special_id"],
        "special_slug": manifest["special_slug"],
        "display_label": manifest["display_label"],
        "edition_kind": manifest["edition_kind"],
        "topic_scope": manifest["topic_scope"],
        "collection_window_start": iso_utc(parse_instant(coverage["start"])),
        "collection_window_end": iso_utc(parse_instant(coverage["end"])),
        "editorial_cutoff": iso_utc(parse_instant(coverage["end"])),
        "cutoff_timezone": coverage["timezone"],
        "retrospective_as_of": iso_utc(parse_instant(coverage["retrospective_as_of"])),
        "community_research": manifest["community_research"],
        "automation_mode": "retrospective-explicit-window" if manifest["edition_kind"] == "RETROSPECTIVE_PERIOD" else "thematic-explicit-window",
        "survey_root": manifest["paths"]["survey_root"],
        "source_root": manifest["paths"]["source_root"],
        "work_branch": manifest["paths"]["work_branch"],
        "human_gates": ["candidate_selection", "issue_architecture", "visual_review", "freeze", "public_release"],
    }


def initial_state(manifest: dict[str, Any]) -> dict[str, Any]:
    plan = build_plan(manifest)
    pending = {
        "raw_sources_preserved": "pending", "candidate_inventory": "pending", "evidence_normalized": "pending",
        "candidate_selection": "pending", "issue_architecture": "pending", "article_draft": "pending",
        "claim_and_chronology_validation": "pending", "latex_build": "pending", "visual_review": "pending", "freeze": "pending",
    }
    return {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "edition_kind": plan["edition_kind"],
        "lifecycle_state": "ISSUE_INITIALIZED",
        "revision": "v0.1",
        "calendar": {
            "editorial_cutoff": plan["editorial_cutoff"],
            "cutoff_timezone": plan["cutoff_timezone"],
            "collection_window_start": plan["collection_window_start"],
            "collection_window_end": plan["collection_window_end"],
            "collection_anchor_at": None,
            "retrospective_as_of": plan["retrospective_as_of"],
            "frozen_at": None,
        },
        "gates": pending,
        "automation": {
            "unattended_public_release": False,
            "human_gate_required_for_selection": True,
            "human_gate_required_for_architecture": True,
            "human_gate_required_for_visual_review": True,
            "human_gate_required_for_freeze": True,
            "human_gate_required_for_public_release": True,
        },
        "provenance": {"edition_manifest": f"specials/{manifest['special_slug']}/edition.json"},
    }


def month_end(year: int, month: int) -> datetime:
    day = calendar.monthrange(year, month)[1]
    return datetime(year, month, day, 23, 59, 59, tzinfo=timezone.utc)


def add_months(year: int, month: int, delta: int) -> tuple[int, int]:
    index = year * 12 + (month - 1) + delta
    return index // 12, index % 12 + 1


def historical_plan(config: dict[str, Any]) -> dict[str, Any]:
    hist = config["historical_granularity"]
    result: list[dict[str, Any]] = []

    monthly_start = datetime.fromisoformat(hist["monthly"]["start"] + "T00:00:00+00:00")
    monthly_end = datetime.fromisoformat(hist["monthly"]["end"] + "T23:59:59+00:00")
    y, m = monthly_start.year, monthly_start.month
    while (y, m) <= (monthly_end.year, monthly_end.month):
        start = datetime(y, m, 1, tzinfo=timezone.utc)
        end = month_end(y, m)
        result.append({
            "tier": "MONTHLY", "special_slug": f"{y:04d}-M{m:02d}",
            "start": iso_utc(start), "end": iso_utc(min(end, monthly_end)),
        })
        y, m = add_months(y, m, 1)

    half_start = datetime.fromisoformat(hist["half_year"]["start"] + "T00:00:00+00:00")
    half_end = datetime.fromisoformat(hist["half_year"]["end"] + "T23:59:59+00:00")
    cursor = half_start
    while cursor <= half_end:
        end_y, end_m = add_months(cursor.year, cursor.month, 5)
        end = min(month_end(end_y, end_m), half_end)
        result.append({
            "tier": "HALF_YEAR", "special_slug": f"{cursor.year:04d}-{cursor.month:02d}_{end.year:04d}-{end.month:02d}",
            "start": iso_utc(cursor), "end": iso_utc(end),
        })
        next_y, next_m = add_months(cursor.year, cursor.month, 6)
        cursor = datetime(next_y, next_m, 1, tzinfo=timezone.utc)

    result.sort(key=lambda item: item["start"])
    return {
        "schema_version": "1.0",
        "monthly_tier_start": hist["monthly"]["start"],
        "half_year_tier_start": hist["half_year"]["start"],
        "annual_before": hist["annual"]["before"],
        "planned_period_specials": result,
        "note": "Annual editions before the half-year tier are intentionally not exhaustively enumerated here; create them on demand. Fine-grained historical subjects should prefer a thematic Special instead of expanding the default cadence.",
    }


def markdown_plan(plan: dict[str, Any]) -> str:
    return (
        f"# {plan['display_label']} — Special operational plan\n\n"
        f"- Special ID: `{plan['issue_id']}`\n"
        f"- Kind: `{plan['edition_kind']}`\n"
        f"- Coverage: `{plan['collection_window_start']}` → `{plan['collection_window_end']}`\n"
        f"- Retrospective as of: `{plan['retrospective_as_of']}`\n"
        f"- Community research: `{plan['community_research']['mode']}` — {plan['community_research']['reason']}\n"
        f"- Work branch: `{plan['work_branch']}`\n\n"
        "This explicit historical window is independent from the Weekly cutoff resolver. Public release still requires the normal human editorial gates.\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)
    p_validate = sub.add_parser("validate")
    p_validate.add_argument("--manifest", required=True)
    p_plan = sub.add_parser("plan")
    p_plan.add_argument("--manifest", required=True)
    p_plan.add_argument("--output")
    p_plan.add_argument("--markdown-output")
    p_init = sub.add_parser("init")
    p_init.add_argument("--manifest", required=True)
    p_init.add_argument("--output", required=True)
    p_history = sub.add_parser("history-plan")
    p_history.add_argument("--output")
    args = parser.parse_args()

    config = load_json(Path(args.config))
    if args.command == "history-plan":
        value = historical_plan(config)
        if args.output:
            write_json(Path(args.output), value)
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0

    manifest = load_json(Path(args.manifest))
    errors = validate_manifest(manifest)
    if args.command == "validate":
        report = {"passed": not errors, "errors": errors, "special_id": manifest.get("special_id")}
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if not errors else 1
    if errors:
        raise SystemExit("; ".join(errors))
    if args.command == "plan":
        value = build_plan(manifest)
        if args.output:
            write_json(Path(args.output), value)
        if args.markdown_output:
            path = Path(args.markdown_output)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(markdown_plan(value), encoding="utf-8")
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0
    if args.command == "init":
        value = initial_state(manifest)
        write_json(Path(args.output), value)
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
