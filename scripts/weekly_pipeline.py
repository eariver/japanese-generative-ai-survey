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
    iso = cutoff.date().isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def iso(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")


def state_paths(repo_root: Path) -> list[Path]:
    return sorted(repo_root.glob("sources/*/pipeline-state.json"))


def previous_collection_anchor(repo_root: Path, current_issue: str) -> str | None:
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


def build_plan(repo_root: Path, cfg: dict[str, Any], now_utc: datetime) -> dict[str, Any]:
    cutoff = latest_cutoff(now_utc, cfg)
    issue_id = issue_id_from_cutoff(cutoff)
    compilation_zone = ZoneInfo(cfg["editorial"]["compilation_timezone"])
    previous_anchor = previous_collection_anchor(repo_root, issue_id)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "generated_at": iso(now_utc),
        "generated_at_local": iso(now_utc.astimezone(compilation_zone)),
        "editorial_cutoff": iso(cutoff),
        "editorial_cutoff_timezone": cfg["editorial"]["cutoff_timezone"],
        "collection_window_start": previous_anchor,
        "collection_window_end": iso(now_utc.astimezone(compilation_zone)),
        "automation_mode": "plan-only",
        "unattended_public_release": False,
        "notes": [
            "Issue ID is derived from the ISO week containing the editorial cutoff; it remains an edition label, not a strict content window.",
            "If collection_window_start is null, establish or import a prior successful collection anchor before unattended collection.",
            "This plan does not publish, merge, or call an LLM.",
        ],
    }


def plan_markdown(plan: dict[str, Any]) -> str:
    start = plan["collection_window_start"] or "UNSET — bootstrap required"
    return (
        f"# Weekly Pipeline Plan — {plan['issue_id']}\n\n"
        f"- Generated: `{plan['generated_at_local']}`\n"
        f"- Editorial cutoff: `{plan['editorial_cutoff']}`\n"
        f"- Collection window start: `{start}`\n"
        f"- Collection window end: `{plan['collection_window_end']}`\n"
        "- Mode: `plan-only`\n\n"
        "This artifact is an operational plan. It does not authorize unattended publication.\n"
    )


def default_state(plan: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "lifecycle_state": "ISSUE_INITIALIZED",
        "revision": "working",
        "calendar": {
            "editorial_cutoff": plan["editorial_cutoff"],
            "cutoff_timezone": plan["editorial_cutoff_timezone"],
            "collection_window_start": plan["collection_window_start"],
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
        "selection": {
            "pipeline_state",
            "manifest",
            "candidate_inventory",
            "candidate_selection",
        },
        "draft": {
            "pipeline_state",
            "manifest",
            "candidate_inventory",
            "candidate_selection",
            "issue_architecture",
            "survey_main",
            "bibliography",
        },
        "release-candidate": {
            "pipeline_state",
            "manifest",
            "candidate_inventory",
            "candidate_selection",
            "issue_architecture",
            "survey_main",
            "bibliography",
            "draft_validation",
            "claim_review",
        },
        "frozen": {
            "pipeline_state",
            "manifest",
            "candidate_inventory",
            "candidate_selection",
            "issue_architecture",
            "survey_main",
            "bibliography",
            "draft_validation",
            "claim_review",
            "freeze_record",
        },
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
    plan = build_plan(root, cfg, parse_instant(args.now))
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
    plan = build_plan(root, cfg, parse_instant(args.now))
    if args.issue_id:
        plan["issue_id"] = args.issue_id
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

    p_plan = sub.add_parser("plan", help="compute the current completed issue and collection window")
    p_plan.add_argument("--now", help="override current instant (ISO-8601 with offset)")
    p_plan.add_argument("--output")
    p_plan.add_argument("--markdown-output")

    p_init = sub.add_parser("init", help="create a non-destructive pipeline-state.json for an issue")
    p_init.add_argument("--now", help="override current instant (ISO-8601 with offset)")
    p_init.add_argument("--issue-id")
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
