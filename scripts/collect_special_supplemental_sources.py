#!/usr/bin/env python3
"""Collect audited supplemental primary sources into a Special work tree.

This collector is intentionally narrow: its input is an edition-scoped coverage-gap
plan produced after the canonical base Source Intake. It is not a replacement for
base discovery. Every planned URL is fetched as immutable Raw bytes and normalized
later through the same Screening/Evidence boundary as base collector records.

Supplemental article pages use the existing `official-pages` collector identity so
the canonical Screening normalizer treats each fetched page as an
`official-index-snapshot`. The collector-run stage and summary metadata preserve the
fact that these observations are coverage-gap supplements rather than base-watchlist
pages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import source_intake as base


ISSUE_RE = re.compile(r"^SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")


def load_plan(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("supplemental plan must be a JSON object")
    if value.get("schema_version") != "1.0":
        raise ValueError("unsupported supplemental plan schema_version")
    issue_id = value.get("issue_id")
    if not isinstance(issue_id, str) or not ISSUE_RE.fullmatch(issue_id):
        raise ValueError("supplemental plan issue_id must use SP-* form")
    coverage = value.get("coverage")
    if not isinstance(coverage, dict):
        raise ValueError("supplemental plan coverage is required")
    start = base.parse_instant(coverage.get("start"))
    end = base.parse_instant(coverage.get("end"))
    if end < start:
        raise ValueError("supplemental coverage end precedes start")
    items = value.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError("supplemental plan items must be a non-empty array")
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("supplemental plan items must be objects")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip() or item_id in seen:
            raise ValueError(f"invalid or duplicate supplemental id: {item_id!r}")
        if not item_id.startswith("supplemental-"):
            raise ValueError(f"supplemental id must start with 'supplemental-': {item_id!r}")
        seen.add(item_id)
        url = item.get("url")
        parsed = urlparse(url) if isinstance(url, str) else None
        if parsed is None or parsed.scheme != "https" or not parsed.netloc:
            raise ValueError(f"supplemental source must use https: {url!r}")
        title = item.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"supplemental source title missing: {item_id}")
        reason = item.get("coverage_gap_reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"coverage_gap_reason missing: {item_id}")
        published = item.get("published_at")
        if published is not None:
            instant = base.parse_instant(published)
            if instant < start or instant > end:
                raise ValueError(f"published_at outside coverage: {item_id}")
    return value


def collector_run(*, issue_id: str, observed_at: datetime, plan: dict[str, Any], outputs: list[dict[str, Any]], status: str) -> dict[str, Any]:
    stamp = base.run_stamp(observed_at)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "run_id": f"official-pages-{issue_id}-{stamp}",
        "stage": "supplemental-primary-source-discovery",
        "collector": {
            "id": "official-pages",
            "provider": "Audited first-party web sources",
            "model": None,
            "prompt_id": None,
            "prompt_version": None,
            "prompt_hash": None,
        },
        "time": {
            "started_at": None,
            "completed_at": base.iso_utc(observed_at),
            "observed_at": base.iso_utc(observed_at),
            "collection_window_start": plan["coverage"]["start"],
            "collection_window_end": plan["coverage"]["end"],
            "editorial_cutoff": plan["coverage"]["end"],
        },
        "inputs": [plan.get("repository_path", "edition-scoped supplemental coverage-gap plan")],
        "outputs": outputs,
        "tool_access": ["HTTPS GET edition-scoped first-party URLs from coverage-gap plan"],
        "status": status,
        "notes": [
            "SUPPLEMENTAL_COVERAGE_GAP_FILL: this run supplements and never replaces canonical base Source Intake.",
            "Raw HTTP response bodies are preserved unchanged.",
            "The existing official-pages Screening adapter intentionally materializes each item-level article as an official-index-snapshot for triage.",
            "Candidate-specific factual claims still require Evidence verification.",
        ],
    }


def run(*, plan_path: Path, output_root: Path, user_agent: str, timeout: int = 45) -> dict[str, Any]:
    plan = load_plan(plan_path)
    issue_id = plan["issue_id"]
    observed_at = datetime.now(timezone.utc)
    collector_id = "official-pages"
    run_root = base.run_base(issue_id, collector_id, observed_at)
    outputs: list[dict[str, Any]] = []
    pages: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    try:
        repository_path = plan_path.resolve().relative_to(output_root.resolve()).as_posix()
    except ValueError:
        repository_path = plan_path.as_posix()
    plan = dict(plan)
    plan["repository_path"] = repository_path

    for item in plan["items"]:
        item_id = base.safe_id(item["id"])
        raw_path = f"{run_root}/raw/{item_id}.html"
        try:
            data, http_meta = base.http_get(item["url"], user_agent=user_agent, timeout=timeout)
            outputs.append(base.save_bytes(output_root, raw_path, data))
            pages.append(
                {
                    "id": item["id"],
                    "url": item["url"],
                    "request": http_meta,
                    "raw_path": raw_path,
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data),
                    "supplemental": True,
                    "title": item["title"],
                    "published_at": item.get("published_at"),
                    "publisher": item.get("publisher"),
                    "coverage_gap_reason": item["coverage_gap_reason"],
                    "metadata": item.get("metadata", {}),
                }
            )
        except Exception as exc:
            errors.append({"id": item["id"], "url": item["url"], "error": repr(exc)})

    summary = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "collector": "official-pages",
        "collection_mode": "SUPPLEMENTAL_COVERAGE_GAP_FILL",
        "observed_at": base.iso_utc(observed_at),
        "coverage": plan["coverage"],
        "plan_path": repository_path,
        "pages": pages,
        "errors": errors,
        "page_count": len(pages),
        "planned_count": len(plan["items"]),
    }
    summary_bytes = (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    outputs.append(base.save_bytes(output_root, f"{run_root}/summary.json", summary_bytes))
    status = "success" if len(pages) == len(plan["items"]) else ("partial" if pages else "failed")
    run_doc = collector_run(
        issue_id=issue_id,
        observed_at=observed_at,
        plan=plan,
        outputs=outputs,
        status=status,
    )
    base.write_json(output_root / f"{run_root}/collector-run.json", run_doc)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "collector_run_id": run_doc["run_id"],
        "status": status,
        "planned_count": len(plan["items"]),
        "collected_count": len(pages),
        "errors": errors,
        "summary_path": f"{run_root}/summary.json",
        "screening_ids": [f"official-index:{item['id']}" for item in pages],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output-root", default=".")
    parser.add_argument("--config", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    output_root = Path(args.output_root).resolve()
    config_path = Path(args.config).resolve()
    cfg = base.load_json(config_path)
    audit = run(
        plan_path=Path(args.plan).resolve(),
        output_root=output_root,
        user_agent=cfg["user_agent"],
        timeout=int(cfg.get("http_timeout_seconds", 45)),
    )
    if args.audit_output:
        base.write_json(Path(args.audit_output), audit)
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0 if audit["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
