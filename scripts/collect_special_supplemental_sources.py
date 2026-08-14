#!/usr/bin/env python3
"""Collect audited supplemental primary sources into a Special work tree.

This collector is intentionally narrow: its input is an edition-scoped coverage-gap
plan produced after the canonical base Source Intake. It is not a replacement for
base discovery. Every planned URL is fetched as immutable Raw bytes and normalized
later through the same Screening/Evidence boundary as base collector records.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import source_intake as base


ISSUE_RE = re.compile(r"^SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"} and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip and data.strip():
            self.parts.append(data)


def visible_text(data: bytes, *, limit: int = 16000) -> str:
    text = data.decode("utf-8", errors="replace")
    parser = VisibleTextParser()
    try:
        parser.feed(text)
        normalized = " ".join(" ".join(parser.parts).split())
    except Exception:
        normalized = " ".join(text.split())
    return normalized[:limit]


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


def run(*, plan_path: Path, output_root: Path, user_agent: str, timeout: int = 45) -> dict[str, Any]:
    plan = load_plan(plan_path)
    issue_id = plan["issue_id"]
    observed_at = datetime.now(timezone.utc)
    collector_id = "supplemental-primary-sources"
    run_base = base.run_base(issue_id, collector_id, observed_at)
    outputs: list[dict[str, Any]] = []
    entries: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    for item in plan["items"]:
        item_id = base.safe_id(item["id"])
        extension = ".html"
        raw_path = f"{run_base}/raw/{item_id}{extension}"
        try:
            data, http_meta = base.http_get(item["url"], user_agent=user_agent, timeout=timeout)
            outputs.append(base.save_bytes(output_root, raw_path, data))
            entries.append(
                {
                    "id": item["id"],
                    "title": item["title"],
                    "url": item["url"],
                    "published_at": item.get("published_at"),
                    "publisher": item.get("publisher"),
                    "coverage_gap_reason": item["coverage_gap_reason"],
                    "raw_path": raw_path,
                    "request": http_meta,
                    "summary_text": visible_text(data),
                    "metadata": item.get("metadata", {}),
                }
            )
        except Exception as exc:
            errors.append({"id": item["id"], "url": item["url"], "error": repr(exc)})

    summary = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "collector": collector_id,
        "observed_at": base.iso_utc(observed_at),
        "coverage": plan["coverage"],
        "plan_path": plan_path.as_posix(),
        "entries": entries,
        "errors": errors,
        "entry_count": len(entries),
        "planned_count": len(plan["items"]),
    }
    summary_bytes = (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    outputs.append(base.save_bytes(output_root, f"{run_base}/summary.json", summary_bytes))
    status = "success" if len(entries) == len(plan["items"]) else ("partial" if entries else "failed")
    collector_run = base.collector_run(
        issue_id=issue_id,
        stage="supplemental-primary-source-discovery",
        collector_id=collector_id,
        provider="Audited first-party web sources",
        observed_at=observed_at,
        plan={
            "editorial_cutoff": plan["coverage"]["end"],
            "collection_window_start": plan["coverage"]["start"],
            "collection_window_end": plan["coverage"]["end"],
        },
        outputs=outputs,
        status=status,
        tool_access=["HTTPS GET edition-scoped first-party URLs from coverage-gap plan"],
        notes=[
            "This collector supplements, and never replaces, the canonical base Source Intake.",
            "Each Raw response is retained unchanged; summary_text is derived only for Screening triage.",
            "Candidate-specific factual claims still require Evidence verification.",
        ],
    )
    base.write_json(output_root / f"{run_base}/collector-run.json", collector_run)
    audit = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "collector_run_id": collector_run["run_id"],
        "status": status,
        "planned_count": len(plan["items"]),
        "collected_count": len(entries),
        "errors": errors,
        "summary_path": f"{run_base}/summary.json",
    }
    return audit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output-root", default=".")
    parser.add_argument("--config", default=str(base.DEFAULT_CONFIG))
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    output_root = Path(args.output_root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = output_root / config_path
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
