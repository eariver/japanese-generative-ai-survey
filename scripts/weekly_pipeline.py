#!/usr/bin/env python3
"""Deterministic spine for the weekly survey pipeline.

This script intentionally does not call LLMs or publish content. It computes the
editorial calendar, creates non-destructive issue state, and validates that
expected repository artifacts exist before later editorial gates.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

DEFAULT_CONFIG = Path("config/weekly-pipeline.json")
INTAKE_SEGMENTS = ("full", "front", "back")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def parse_instant(value: str | None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include an explicit UTC offset or Z")
    return parsed.astimezone(timezone.utc)


def weekday_number(name: str) -> int:
    names = {
        "MONDAY": 0,
        "TUESDAY": 1,
        "WEDNESDAY": 2,
        "THURSDAY": 3,
        "FRIDAY": 4,
        "SATURDAY": 5,
        "SUNDAY": 6,
    }
    try:
        return names[name.upper()]
    except KeyError as exc:
        raise ValueError(f"unsupported weekday: {name}") from exc


def latest_cutoff(now_utc: datetime, cfg: dict[str, Any]) -> datetime:
    editorial = cfg["editorial"]
    zone = ZoneInfo(editorial["cutoff_timezone"])
    local_now = now_utc.astimezone(zone)
    target_weekday = weekday_number(editorial["cutoff_weekday"])
    days_since = (local_now.weekday() - target_weekday) % 7
    target_date = local_now.date() - timedelta(days=days_since)
    cutoff = datetime(
        target_date.year,
        target_date.month,
        target_date.day,
        int(editorial["cutoff_hour"]),
        int(editorial.get("cutoff_minute", 0)),
        tzinfo=zone,
    )
    if cutoff > local_now:
        cutoff -= timedelta(days=7)
    return cutoff


def issue_id_from_cutoff(cutoff: datetime) -> str:
    iso_calendar = cutoff.date().isocalendar()
    return f"{iso_calendar.year}-W{iso_calendar.week:02d}"


def iso(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")


def state_paths(repo_root: Path) -> list[Path]:
    return sorted(repo_root.glob("sources/*/pipeline-state.json"))


def previous_collection_anchor(repo_root: Path, current_issue: str) -> str | None:
    """Return the latest accepted observation anchor for continuity diagnostics.

    The anchor is deliberately *not* an editorial-window boundary. Starting with
    W33, issue membership is defined by cutoff-to-cutoff event time instead.
    """
    best: tuple[datetime, str] | None = None
    for path in state_paths(repo_root):
        if path.parent.name == current_issue:
            continue
        try:
            state = load_json(path)
            raw = state.get("calendar", {}).get("collection_anchor_at")
            if not raw:
                continue
            dt = parse_instant(raw)
            if best is None or dt > best[0]:
                best = (dt, raw)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
    return None if best is None else best[1]


def editorial_window(cutoff: datetime, cfg: dict[str, Any]) -> tuple[datetime, datetime]:
    intake_cfg = cfg.get("intake", {})
    days = int(intake_cfg.get("canonical_window_days", 7))
    if days <= 0:
        raise ValueError("intake.canonical_window_days must be positive")
    return cutoff - timedelta(days=days), cutoff


def intake_split_boundary(start: datetime, end: datetime, cfg: dict[str, Any]) -> datetime:
    intake_cfg = cfg.get("intake", {})
    days = int(intake_cfg.get("front_segment_days", 4))
    boundary = start + timedelta(days=days)
    if not start < boundary < end:
        raise ValueError("intake.front_segment_days must place the split inside the editorial window")
    return boundary


def segment_window(
    start: datetime,
    end: datetime,
    cfg: dict[str, Any],
    segment: str,
) -> tuple[datetime, datetime, datetime]:
    if segment not in INTAKE_SEGMENTS:
        raise ValueError(f"unsupported intake segment: {segment}")
    split = intake_split_boundary(start, end, cfg)
    if segment == "front":
        return start, split, split
    if segment == "back":
        return split, end, split
    return start, end, split


def build_plan(
    repo_root: Path,
    cfg: dict[str, Any],
    now_utc: datetime,
    intake_segment: str = "full",
) -> dict[str, Any]:
    cutoff = latest_cutoff(now_utc, cfg)
    issue_id = issue_id_from_cutoff(cutoff)
    compilation_zone = ZoneInfo(cfg["editorial"]["compilation_timezone"])
    editorial_start, editorial_end = editorial_window(cutoff, cfg)
    collection_start, collection_end, split = segment_window(
        editorial_start, editorial_end, cfg, intake_segment
    )
    previous_anchor = previous_collection_anchor(repo_root, issue_id)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "generated_at": iso(now_utc),
        "generated_at_local": iso(now_utc.astimezone(compilation_zone)),
        "editorial_window_start": iso(editorial_start),
        "editorial_window_end": iso(editorial_end),
        "editorial_cutoff": iso(cutoff),
        "editorial_cutoff_timezone": cfg["editorial"]["cutoff_timezone"],
        "intake_segment": intake_segment,
        "intake_split_boundary": iso(split),
        "collection_window_start": iso(collection_start),
        "collection_window_end": iso(collection_end),
        "previous_collection_anchor": previous_anchor,
        "automation_mode": "plan-only",
        "unattended_public_release": False,
        "notes": [
            "The canonical weekly editorial window is the half-open cutoff-to-cutoff interval [previous Friday 18:00, current Friday 18:00) in America/New_York.",
            "collection_window_start/end describe the selected intake segment, not fetch execution time.",
            "The previous collection anchor is retained only as an observation/provenance continuity signal and never defines issue membership.",
            "front and back intake segments are deterministic partitions of the same editorial window; full remains valid when splitting is unnecessary.",
            "This plan does not publish, merge, or call an LLM.",
        ],
    }


def build_plan_for_issue(
    repo_root: Path,
    cfg: dict[str, Any],
    now_utc: datetime,
    issue_id: str,
    intake_segment: str = "full",
) -> dict[str, Any]:
    """Build a plan for a named current issue or replay committed historical state.

    Current issues always use canonical cutoff-to-cutoff editorial time. Historical
    W33+ states can replay that canonical window. Older states remain replayable
    through their legacy committed collection window without rewriting frozen data.
    """
    current = build_plan(repo_root, cfg, now_utc, intake_segment=intake_segment)
    if current["issue_id"] == issue_id:
        current["plan_source"] = "latest-cutoff"
        return current

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if not state_path.is_file():
        raise ValueError(
            f"cannot plan requested issue {issue_id}: current completed cutoff maps to {current['issue_id']} "
            f"and {state_path.relative_to(repo_root)} does not exist"
        )

    state = load_json(state_path)
    if state.get("issue_id") not in (None, issue_id):
        raise ValueError(f"pipeline state issue_id does not match requested issue {issue_id}")
    calendar = state.get("calendar", {})
    cutoff_raw = calendar.get("editorial_cutoff")
    if not cutoff_raw:
        raise ValueError(f"historical replay for {issue_id} requires calendar.editorial_cutoff")
    cutoff = parse_instant(cutoff_raw).astimezone(ZoneInfo(cfg["editorial"]["cutoff_timezone"]))
    canonical_start_raw = calendar.get("editorial_window_start")
    compilation_zone = ZoneInfo(cfg["editorial"]["compilation_timezone"])

    if canonical_start_raw:
        editorial_start = parse_instant(canonical_start_raw).astimezone(cutoff.tzinfo)
        editorial_end = cutoff
        collection_start, collection_end, split = segment_window(
            editorial_start, editorial_end, cfg, intake_segment
        )
        mode = "historical-canonical-replay"
        notes = [
            "This named-issue plan replays the committed canonical editorial window.",
            "The selected front/back/full segment is derived deterministically from that window.",
            "Official-page snapshots fetched during replay are current snapshots unless the upstream service provides historical retrieval.",
            "This plan does not publish, merge, or call an LLM.",
        ]
    else:
        if intake_segment != "full":
            raise ValueError(
                f"legacy historical replay for {issue_id} does not define editorial_window_start; only --intake-segment full is supported"
            )
        legacy_start_raw = calendar.get("collection_window_start")
        legacy_end_raw = calendar.get("collection_anchor_at")
        if not legacy_start_raw or not legacy_end_raw:
            raise ValueError(
                f"legacy historical replay for {issue_id} requires calendar.collection_window_start and collection_anchor_at"
            )
        collection_start = parse_instant(legacy_start_raw).astimezone(compilation_zone)
        collection_end = parse_instant(legacy_end_raw).astimezone(compilation_zone)
        editorial_start = collection_start
        editorial_end = cutoff
        split = intake_split_boundary(cutoff - timedelta(days=7), cutoff, cfg)
        mode = "historical-legacy-replay"
        notes = [
            "This pre-W33 issue replays its committed legacy collection window exactly; frozen history is not rewritten.",
            "The legacy collection anchor is an observation boundary and is not retroactively reinterpreted as an editorial cutoff.",
            "Official-page snapshots fetched during replay are current snapshots unless the upstream service provides historical retrieval.",
            "This plan does not publish, merge, or call an LLM.",
        ]

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "generated_at": iso(now_utc),
        "generated_at_local": iso(now_utc.astimezone(compilation_zone)),
        "editorial_window_start": iso(editorial_start),
        "editorial_window_end": iso(editorial_end),
        "editorial_cutoff": cutoff_raw,
        "editorial_cutoff_timezone": calendar.get(
            "cutoff_timezone", cfg["editorial"]["cutoff_timezone"]
        ),
        "intake_segment": intake_segment,
        "intake_split_boundary": iso(split),
        "collection_window_start": iso(collection_start),
        "collection_window_end": iso(collection_end),
        "previous_collection_anchor": calendar.get("collection_anchor_at"),
        "automation_mode": mode,
        "plan_source": "pipeline-state",
        "unattended_public_release": False,
        "notes": notes,
    }


def plan_markdown(plan: dict[str, Any]) -> str:
    anchor = plan.get("previous_collection_anchor") or "UNSET"
    return (
        f"# Weekly Pipeline Plan — {plan['issue_id']}\n\n"
        f"- Generated: `{plan['generated_at_local']}`\n"
        f"- Editorial window: `[{plan['editorial_window_start']}, {plan['editorial_window_end']})`\n"
        f"- Editorial cutoff: `{plan['editorial_cutoff']}`\n"
        f"- Intake segment: `{plan.get('intake_segment', 'full')}`\n"
        f"- Intake split boundary: `{plan.get('intake_split_boundary')}`\n"
        f"- Collection window: `[{plan['collection_window_start']}, {plan['collection_window_end']})`\n"
        f"- Previous accepted observation anchor: `{anchor}`\n"
        f"- Mode: `{plan.get('automation_mode', 'plan-only')}`\n\n"
        "This artifact is an operational plan. It does not authorize unattended publication.\n"
    )


def default_state(plan: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "lifecycle_state": "ISSUE_INITIALIZED",
        "revision": "working",
        "calendar": {
            "editorial_window_start": plan["editorial_window_start"],
            "editorial_cutoff": plan["editorial_cutoff"],
            "cutoff_timezone": plan["editorial_cutoff_timezone"],
            "collection_window_start": plan["editorial_window_start"],
            "intake_split_boundary": plan["intake_split_boundary"],
            "collection_anchor_at": None,
        },
        "gates": {
            "raw_sources_preserved": "pending",
            "candidate_inventory": "pending",
            "evidence_normalized": "pending",
            "candidate_selection": "pending",
            "issue_architecture": "pending",
            "article_draft": "pending",
            "claim_and_chronology_validation": "pending",
            "latex_build": "pending",
            "visual_review": "pending",
            "freeze": "pending",
        },
        "automation": {
            "unattended_public_release": False,
            "human_gate_required_for_selection": True,
            "human_gate_required_for_freeze": True,
        },
    }


def glob_any(root: Path, pattern: str) -> bool:
    return any(root.glob(pattern))


def validation_checks(repo_root: Path, issue_id: str) -> list[dict[str, Any]]:
    issue_sources = repo_root / "sources" / issue_id
    issue_survey = repo_root / "surveys" / "weekly" / issue_id
    checks: list[tuple[str, bool, str]] = [
        ("pipeline_state", (issue_sources / "pipeline-state.json").is_file(), f"sources/{issue_id}/pipeline-state.json"),
        ("manifest", (issue_sources / "manifest.yaml").is_file(), f"sources/{issue_id}/manifest.yaml"),
        ("candidate_inventory", (issue_sources / "candidates" / "index.yaml").is_file(), f"sources/{issue_id}/candidates/index.yaml"),
        ("candidate_selection", (issue_sources / "candidate-selection.yaml").is_file(), f"sources/{issue_id}/candidate-selection.yaml"),
        ("issue_architecture", glob_any(issue_sources, "issue-architecture*.md"), f"sources/{issue_id}/issue-architecture*.md"),
        ("paper_evidence", (issue_sources / "evidence" / "papers" / "index.yaml").is_file(), f"sources/{issue_id}/evidence/papers/index.yaml"),
        ("survey_main", (issue_survey / "main.tex").is_file(), f"surveys/weekly/{issue_id}/main.tex"),
        ("bibliography", (issue_survey / "references.bib").is_file(), f"surveys/weekly/{issue_id}/references.bib"),
        ("draft_validation", glob_any(issue_sources, "draft-validation*.md"), f"sources/{issue_id}/draft-validation*.md"),
        ("claim_review", glob_any(issue_sources, "final-claim-review*.md"), f"sources/{issue_id}/final-claim-review*.md"),
        ("freeze_record", glob_any(issue_sources, "freeze*.md"), f"sources/{issue_id}/freeze*.md"),
    ]
    return [{"name": name, "passed": passed, "expected": expected} for name, passed, expected in checks]


def internal_page_reference_findings(repo_root: Path, issue_id: str) -> list[dict[str, Any]]:
    section_dir = repo_root / "surveys" / "weekly" / issue_id / "sections"
    findings: list[dict[str, Any]] = []
    if not section_dir.exists():
        return findings
    pattern = re.compile(r"(?:今号|本号)\s*p\.\s*\d+(?:\s*--\s*\d+)?")
    for tex in sorted(section_dir.glob("*.tex")):
        text = tex.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append({"file": str(tex.relative_to(repo_root)), "line": line, "text": match.group(0)})
    return findings


def required_names(target: str) -> set[str]:
    levels = {
        "selection": {"pipeline_state", "manifest", "candidate_inventory", "candidate_selection"},
        "draft": {"pipeline_state", "manifest", "candidate_inventory", "candidate_selection", "issue_architecture", "survey_main", "bibliography"},
        "release-candidate": {"pipeline_state", "manifest", "candidate_inventory", "candidate_selection", "issue_architecture", "survey_main", "bibliography", "draft_validation", "claim_review"},
        "frozen": {"pipeline_state", "manifest", "candidate_inventory", "candidate_selection", "issue_architecture", "survey_main", "bibliography", "draft_validation", "claim_review", "freeze_record"},
    }
    return levels[target]


def validate(repo_root: Path, issue_id: str, target: str) -> tuple[dict[str, Any], bool]:
    checks = validation_checks(repo_root, issue_id)
    required = required_names(target)
    failed = [c for c in checks if c["name"] in required and not c["passed"]]
    stale_refs = internal_page_reference_findings(repo_root, issue_id)
    report = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "target": target,
        "passed": not failed and not stale_refs,
        "checks": checks,
        "blocking_missing_artifacts": failed,
        "blocking_hardcoded_internal_page_references": stale_refs,
        "note": "This validator checks repository structure and known deterministic hazards. It does not replace claim review, chronology review, TeX compilation, or visual inspection.",
    }
    return report, report["passed"]


def cmd_plan(args: argparse.Namespace, cfg: dict[str, Any]) -> int:
    root = Path(args.repo_root).resolve()
    now = parse_instant(args.now)
    plan = (
        build_plan_for_issue(root, cfg, now, args.issue_id, intake_segment=args.intake_segment)
        if args.issue_id
        else build_plan(root, cfg, now, intake_segment=args.intake_segment)
    )
    if args.output:
        write_json(Path(args.output), plan)
    if args.markdown_output:
        path = Path(args.markdown_output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(plan_markdown(plan), encoding="utf-8")
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


def cmd_init(args: argparse.Namespace, cfg: dict[str, Any]) -> int:
    root = Path(args.repo_root).resolve()
    plan = build_plan(root, cfg, parse_instant(args.now), intake_segment="full")
    if args.issue_id and args.issue_id != plan["issue_id"]:
        print(
            f"refusing to initialize {args.issue_id}: current completed cutoff maps to {plan['issue_id']}; "
            "wait for that issue's editorial cutoff rather than fabricating a future calendar",
            file=sys.stderr,
        )
        return 2
    state_path = root / "sources" / plan["issue_id"] / "pipeline-state.json"
    if state_path.exists() and not args.force:
        print(f"refusing to overwrite existing state: {state_path}", file=sys.stderr)
        return 2
    write_json(state_path, default_state(plan))
    print(state_path)
    return 0


def cmd_validate(args: argparse.Namespace, cfg: dict[str, Any]) -> int:
    del cfg
    root = Path(args.repo_root).resolve()
    report, passed = validate(root, args.issue_id, args.target)
    if args.output:
        write_json(Path(args.output), report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="compute the current completed issue or replay a named issue")
    p_plan.add_argument("--now", help="override current instant (ISO-8601 with offset)")
    p_plan.add_argument("--issue-id", help="named issue for deterministic historical replay")
    p_plan.add_argument("--intake-segment", choices=INTAKE_SEGMENTS, default="full")
    p_plan.add_argument("--output")
    p_plan.add_argument("--markdown-output")

    p_init = sub.add_parser("init", help="create a non-destructive pipeline-state.json for the current completed issue")
    p_init.add_argument("--now", help="override current instant (ISO-8601 with offset)")
    p_init.add_argument("--issue-id", help="optional assertion of the current issue; future/historical IDs are rejected")
    p_init.add_argument("--force", action="store_true")

    p_val = sub.add_parser("validate", help="validate deterministic repository gates")
    p_val.add_argument("--issue-id", required=True)
    p_val.add_argument("--target", choices=["selection", "draft", "release-candidate", "frozen"], default="draft")
    p_val.add_argument("--output")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = repo_root / config_path
    cfg = load_json(config_path)
    if args.command == "plan":
        return cmd_plan(args, cfg)
    if args.command == "init":
        return cmd_init(args, cfg)
    if args.command == "validate":
        return cmd_validate(args, cfg)
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
