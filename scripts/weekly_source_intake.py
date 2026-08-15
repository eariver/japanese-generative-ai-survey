#!/usr/bin/env python3
"""Weekly source-intake orchestration with bounded temporal partitioning.

The shared collector primitives in ``source_intake.py`` remain responsible for
fetching and preserving exact Raw bytes. This wrapper adds Weekly-specific
orchestration:

- the plan's canonical cutoff-to-cutoff window is authoritative;
- arXiv begins with two equal half-week slices;
- a slice that reaches the configured per-query cap is bisected recursively;
- inclusive minute boundaries intentionally overlap and are deduplicated later by
  ``build_screening_index.py`` using stable screening ids;
- GitHub Releases and official-page snapshots are collected once over the full
  canonical window;
- unresolved cap hits remain explicit coverage limitations rather than being
  silently called complete.
"""

from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import source_intake as base

DEFAULT_CONFIG = base.DEFAULT_CONFIG
DEFAULT_INITIAL_SLICES = 2
DEFAULT_MIN_SLICE_MINUTES = 360


def partition_evenly(start: datetime, end: datetime, count: int) -> list[tuple[datetime, datetime]]:
    if count < 1:
        raise ValueError("count must be >= 1")
    if end <= start:
        raise ValueError("collection window end must be after start")
    span = end - start
    boundaries = [start + span * index / count for index in range(count + 1)]
    return [(boundaries[index], boundaries[index + 1]) for index in range(count)]


def subplan(plan: dict[str, Any], start: datetime, end: datetime) -> dict[str, Any]:
    item = copy.deepcopy(plan)
    item["collection_window_start"] = base.iso_utc(start)
    item["collection_window_end"] = base.iso_utc(end)
    return item


def cap_hits_for_run(output_root: Path, run: dict[str, Any], max_results: int) -> list[dict[str, Any]]:
    summary_candidates = [
        output_root / output["path"]
        for output in run.get("outputs", [])
        if str(output.get("path", "")).endswith("/summary.json")
    ]
    if len(summary_candidates) != 1 or not summary_candidates[0].is_file():
        return []
    summary = base.load_json(summary_candidates[0])
    hits: list[dict[str, Any]] = []
    for query in summary.get("queries", []):
        count = int(query.get("entry_count", 0))
        if count >= max_results:
            hits.append(
                {
                    "query_id": query.get("id"),
                    "entry_count": count,
                    "configured_cap": max_results,
                }
            )
    return hits


def _collect_arxiv_slice(
    *,
    plan: dict[str, Any],
    cfg: dict[str, Any],
    output_root: Path,
    start: datetime,
    end: datetime,
    depth: int,
    min_slice: timedelta,
    max_results: int,
    runs: list[dict[str, Any]],
    observations: list[dict[str, Any]],
    residual_cap_hits: list[dict[str, Any]],
) -> None:
    slice_plan = subplan(plan, start, end)
    run = base.run_arxiv(slice_plan, cfg, output_root)
    runs.append(run)
    hits = cap_hits_for_run(output_root, run, max_results)
    observation = {
        "run_id": run.get("run_id"),
        "status": run.get("status"),
        "depth": depth,
        "start": base.iso_utc(start),
        "end": base.iso_utc(end),
        "duration_minutes": int((end - start).total_seconds() // 60),
        "cap_hits": hits,
    }
    observations.append(observation)

    if not hits:
        observation["terminal_reason"] = "BELOW_CAP"
        return

    if end - start <= min_slice:
        observation["terminal_reason"] = "MIN_SLICE_REACHED_WITH_CAP_HIT"
        residual_cap_hits.append(
            {
                "run_id": run.get("run_id"),
                "start": base.iso_utc(start),
                "end": base.iso_utc(end),
                "cap_hits": hits,
            }
        )
        return

    midpoint = start + (end - start) / 2
    if midpoint <= start or midpoint >= end:
        observation["terminal_reason"] = "UNSPLITTABLE_WITH_CAP_HIT"
        residual_cap_hits.append(
            {
                "run_id": run.get("run_id"),
                "start": base.iso_utc(start),
                "end": base.iso_utc(end),
                "cap_hits": hits,
            }
        )
        return

    observation["terminal_reason"] = "SPLIT_ON_CAP"
    for child_start, child_end in ((start, midpoint), (midpoint, end)):
        _collect_arxiv_slice(
            plan=plan,
            cfg=cfg,
            output_root=output_root,
            start=child_start,
            end=child_end,
            depth=depth + 1,
            min_slice=min_slice,
            max_results=max_results,
            runs=runs,
            observations=observations,
            residual_cap_hits=residual_cap_hits,
        )


def run(plan: dict[str, Any], cfg: dict[str, Any], output_root: Path, collector: str) -> dict[str, Any]:
    start = base.parse_instant(plan["collection_window_start"])
    end = base.parse_instant(plan["collection_window_end"])
    if end <= start:
        raise ValueError("collection window end must be after start")

    policy = cfg.get("coverage_policy", {})
    initial_slices = max(1, int(policy.get("weekly_arxiv_initial_slices", DEFAULT_INITIAL_SLICES)))
    min_slice_minutes = max(1, int(policy.get("weekly_arxiv_min_slice_minutes", DEFAULT_MIN_SLICE_MINUTES)))
    min_slice = timedelta(minutes=min_slice_minutes)
    max_results = int(cfg.get("arxiv", {}).get("max_results_per_query", 200))

    runs: list[dict[str, Any]] = []
    arxiv_observations: list[dict[str, Any]] = []
    residual_cap_hits: list[dict[str, Any]] = []
    selected = base.selected_collectors(collector)

    if "arxiv" in selected and cfg.get("arxiv", {}).get("enabled", True):
        for slice_start, slice_end in partition_evenly(start, end, initial_slices):
            _collect_arxiv_slice(
                plan=plan,
                cfg=cfg,
                output_root=output_root,
                start=slice_start,
                end=slice_end,
                depth=0,
                min_slice=min_slice,
                max_results=max_results,
                runs=runs,
                observations=arxiv_observations,
                residual_cap_hits=residual_cap_hits,
            )

    if "github" in selected and cfg.get("github_releases", {}).get("enabled", True):
        runs.append(base.run_github_releases(plan, cfg, output_root))
    if "official" in selected and cfg.get("official_pages", {}).get("enabled", True):
        runs.append(base.run_official_pages(plan, cfg, output_root))

    failed = [item for item in runs if item.get("status") == "failed"]
    partial = [item for item in runs if item.get("status") == "partial"]
    overall_status = "failed" if failed else ("partial" if partial else "success")
    coverage_status = "INCOMPLETE_CAP_HIT" if residual_cap_hits else "BASE_INTAKE_COLLECTED"

    report = {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "collector_count": len(runs),
        "runs": [
            {
                "run_id": item.get("run_id"),
                "collector": item.get("collector", {}).get("id"),
                "status": item.get("status"),
            }
            for item in runs
        ],
        "overall_status": overall_status,
        "coverage": {
            "canonical_window_start": base.iso_utc(start),
            "canonical_window_end": base.iso_utc(end),
            "base_intake_role": policy.get("base_intake_role", "BROAD_SEED_NOT_EXHAUSTIVE"),
            "coverage_audit_required": bool(policy.get("weekly_requires_coverage_audit", True)),
            "coverage_status": coverage_status,
            "arxiv_temporal_partition": "ADAPTIVE_HALF_WEEK_BISECTION" if "arxiv" in selected else "NOT_RUN",
            "arxiv_initial_slice_count": initial_slices,
            "arxiv_min_slice_minutes": min_slice_minutes,
            "arxiv_boundary_policy": "INCLUSIVE_MINUTE_OVERLAP_DEDUP_BY_SCREENING_ID",
            "arxiv_slice_observations": arxiv_observations,
            "arxiv_residual_cap_hits": residual_cap_hits,
            "notes": [
                "Collector success proves configured retrieval completed; it is not a completeness proof.",
                "A cap-hit arXiv interval is recursively bisected until below the configured cap or the minimum slice is reached.",
                "Parent and child Raw responses are retained immutably; downstream Screening deduplicates stable source ids.",
                "Residual cap hits are explicit blockers for calling paper intake complete and require further gap handling.",
            ],
        },
    }
    base.write_json(output_root / "source-intake-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
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
    if not plan.get("collection_window_start") or not plan.get("collection_window_end"):
        raise SystemExit("weekly source intake requires an explicit canonical collection window")

    report = run(plan, cfg, output_root, args.collector)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["overall_status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
