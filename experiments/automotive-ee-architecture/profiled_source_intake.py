#!/usr/bin/env python3
"""Experimental domain-profile adapter for the existing Source Intake collectors.

This file intentionally lives outside scripts/ and does not modify the production AI
Source Intake implementation. It reuses scripts/source_intake.py as-is, replacing only
the provenance labels that are currently hard-coded to config/source-intake.json and a
weekly plan. The experiment therefore measures how far configuration-level reuse can
go before a shared domain-neutral collector API is justified.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Callable

from scripts import source_intake as base


def repo_relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def install_profiled_provenance(*, profile_path: Path, plan_path: Path, repo_root: Path) -> None:
    original: Callable[..., dict[str, Any]] = base.collector_run
    profile_ref = repo_relative(profile_path, repo_root)
    plan_ref = repo_relative(plan_path, repo_root)

    def profiled_collector_run(**kwargs: Any) -> dict[str, Any]:
        value = original(**kwargs)
        value["inputs"] = [profile_ref, plan_ref]
        value["notes"] = list(value.get("notes") or []) + [
            "EXPERIMENTAL_DOMAIN_PROFILE: production AI Source Intake code/config were not modified.",
            "Profile provenance replaces the production collector's historical weekly/config labels only; Raw acquisition behavior is unchanged.",
        ]
        return value

    base.collector_run = profiled_collector_run


def selected_collectors(value: str) -> list[str]:
    return ["arxiv", "github", "official"] if value == "all" else [value]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--profile", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--collector", choices=["all", "arxiv", "github", "official"], default="all")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    profile_path = Path(args.profile)
    if not profile_path.is_absolute():
        profile_path = repo_root / profile_path
    plan_path = Path(args.plan)
    if not plan_path.is_absolute():
        plan_path = repo_root / plan_path
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = repo_root / output_root

    cfg = base.load_json(profile_path)
    plan = base.load_json(plan_path)
    if not plan.get("collection_window_start"):
        raise SystemExit("collection_window_start is unset; profiled Source Intake refuses to guess a window start")

    install_profiled_provenance(
        profile_path=profile_path,
        plan_path=plan_path,
        repo_root=repo_root,
    )

    runs: list[dict[str, Any]] = []
    for collector in selected_collectors(args.collector):
        if collector == "arxiv" and cfg["arxiv"].get("enabled", True):
            runs.append(base.run_arxiv(plan, cfg, output_root))
        elif collector == "github" and cfg["github_releases"].get("enabled", True):
            runs.append(base.run_github_releases(plan, cfg, output_root))
        elif collector == "official" and cfg["official_pages"].get("enabled", True):
            runs.append(base.run_official_pages(plan, cfg, output_root))

    failed = [run for run in runs if run["status"] == "failed"]
    partial = [run for run in runs if run["status"] == "partial"]
    report = {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "experiment": "PROFILED_SOURCE_INTAKE",
        "profile": repo_relative(profile_path, repo_root),
        "plan": repo_relative(plan_path, repo_root),
        "collector_count": len(runs),
        "runs": [
            {
                "run_id": run["run_id"],
                "collector": run["collector"]["id"],
                "status": run["status"],
            }
            for run in runs
        ],
        "overall_status": "failed" if failed else ("partial" if partial else "success"),
        "production_files_modified": [],
    }
    base.write_json(output_root / "source-intake-report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
