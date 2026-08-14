#!/usr/bin/env python3
"""Run Special Source Intake with temporal coverage for long retrospective windows.

The reusable weekly collector intentionally stays lightweight. Special retrospectives
cover much longer windows, so a single arXiv query per category with a bounded
max_results value can collapse the paper pool onto the newest part of the period.
This wrapper partitions long retrospective arXiv collection by calendar month while
leaving GitHub and official-page collection on the exact full Special window.

This improves temporal coverage; it is still a broad discovery seed rather than an
exhaustive arXiv crawl. Query slices that exactly hit max_results are reported as
possible truncation and must be considered by the period-specific coverage audit.
"""
from __future__ import annotations

import argparse
import json
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import source_intake as base


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def next_month_start(value: datetime) -> datetime:
    if value.month == 12:
        return value.replace(year=value.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    return value.replace(month=value.month + 1, day=1, hour=0, minute=0, second=0, microsecond=0)


def calendar_month_slices(start: datetime, end: datetime) -> list[tuple[datetime, datetime]]:
    """Return inclusive UTC calendar-month slices covering start..end exactly."""
    start = start.astimezone(timezone.utc)
    end = end.astimezone(timezone.utc)
    if end < start:
        raise ValueError("collection window end precedes start")
    result: list[tuple[datetime, datetime]] = []
    cursor = start
    while cursor <= end:
        boundary = next_month_start(cursor)
        slice_end = min(end, boundary - timedelta(seconds=1))
        result.append((cursor, slice_end))
        cursor = boundary
    return result


def should_partition_arxiv(plan: dict[str, Any], cfg: dict[str, Any]) -> bool:
    policy = cfg.get("coverage_policy", {})
    if plan.get("edition_kind") != "RETROSPECTIVE_PERIOD":
        return False
    threshold_days = int(policy.get("long_window_partition_threshold_days", 45))
    start = base.parse_instant(plan["collection_window_start"])
    end = base.parse_instant(plan["collection_window_end"])
    return (end - start).total_seconds() > threshold_days * 86400


def run_summary_path(output_root: Path, run: dict[str, Any]) -> Path | None:
    for item in run.get("outputs", []):
        path = item.get("path")
        if isinstance(path, str) and path.endswith("/summary.json"):
            candidate = output_root / path
            if candidate.is_file():
                return candidate
    return None


def arxiv_cap_observations(output_root: Path, runs: list[dict[str, Any]], max_results: int) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    for run in runs:
        if run.get("collector", {}).get("id") != "arxiv-api":
            continue
        path = run_summary_path(output_root, run)
        if path is None:
            continue
        summary = json.loads(path.read_text(encoding="utf-8"))
        for query in summary.get("queries", []):
            count = int(query.get("entry_count", 0))
            if count >= max_results:
                observations.append(
                    {
                        "collector_run_id": run.get("run_id"),
                        "query_id": query.get("id"),
                        "entry_count": count,
                        "max_results_per_query": max_results,
                        "possible_truncation": True,
                    }
                )
    return observations


def run(plan: dict[str, Any], cfg: dict[str, Any], output_root: Path, collector: str) -> dict[str, Any]:
    selected = base.selected_collectors(collector)
    runs: list[dict[str, Any]] = []
    temporal_slices: list[dict[str, str]] = []

    if "arxiv" in selected and cfg["arxiv"].get("enabled", True):
        start = base.parse_instant(plan["collection_window_start"])
        end = base.parse_instant(plan["collection_window_end"])
        slices = calendar_month_slices(start, end) if should_partition_arxiv(plan, cfg) else [(start, end)]
        for slice_start, slice_end in slices:
            subplan = deepcopy(plan)
            subplan["collection_window_start"] = base.iso_utc(slice_start)
            subplan["collection_window_end"] = base.iso_utc(slice_end)
            temporal_slices.append(
                {
                    "start": subplan["collection_window_start"],
                    "end": subplan["collection_window_end"],
                }
            )
            runs.append(base.run_arxiv(subplan, cfg, output_root))

    if "github" in selected and cfg["github_releases"].get("enabled", True):
        runs.append(base.run_github_releases(plan, cfg, output_root))
    if "official" in selected and cfg["official_pages"].get("enabled", True):
        runs.append(base.run_official_pages(plan, cfg, output_root))

    failed = [run for run in runs if run["status"] == "failed"]
    partial = [run for run in runs if run["status"] == "partial"]
    max_results = int(cfg.get("arxiv", {}).get("max_results_per_query", 200))
    cap_hits = arxiv_cap_observations(output_root, runs, max_results)
    report = {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "collector_count": len(runs),
        "runs": [
            {"run_id": r["run_id"], "collector": r["collector"]["id"], "status": r["status"]}
            for r in runs
        ],
        "overall_status": "failed" if failed else ("partial" if partial else "success"),
        "coverage": {
            "base_intake_role": cfg.get("coverage_policy", {}).get("base_intake_role", "BROAD_SEED_NOT_EXHAUSTIVE"),
            "arxiv_temporal_partition": "CALENDAR_MONTH" if len(temporal_slices) > 1 else "NONE",
            "arxiv_slices": temporal_slices,
            "arxiv_possible_truncation_count": len(cap_hits),
            "arxiv_possible_truncation": cap_hits,
            "coverage_audit_required": bool(
                plan.get("edition_kind") == "RETROSPECTIVE_PERIOD"
                and cfg.get("coverage_policy", {}).get("retrospective_period_requires_coverage_audit", False)
            ),
        },
    }
    write_json(output_root / "source-intake-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(base.DEFAULT_CONFIG))
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--collector", choices=["all", "arxiv", "github", "official"], default="all")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = repo_root / config_path
    plan_path = Path(args.plan)
    if not plan_path.is_absolute():
        plan_path = repo_root / plan_path
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = repo_root / output_root

    cfg = base.load_json(config_path)
    plan = base.load_json(plan_path)
    if not plan.get("collection_window_start"):
        raise SystemExit("collection_window_start is unset; source intake refuses to guess a window start")
    report = run(plan, cfg, output_root, args.collector)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["overall_status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
