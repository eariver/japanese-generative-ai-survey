#!/usr/bin/env python3
"""Reproducible source-intake adapters for the weekly survey.

Collectors save exact HTTP response bytes under a run-specific Raw path and emit
separate summary plus collector-run provenance. They do not perform editorial
selection or promote any observation into verified evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = Path("config/source-intake.json")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_instant(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        raise ValueError(f"timestamp requires an explicit offset: {value}")
    return parsed.astimezone(timezone.utc)


def iso_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def run_stamp(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def run_base(issue_id: str, collector_slug: str, observed_at: datetime) -> str:
    return f"sources/{issue_id}/collectors/{collector_slug}/runs/{run_stamp(observed_at)}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-").lower()


def output_record(repo_path: str, data: bytes) -> dict[str, Any]:
    return {"path": repo_path, "sha256": sha256_bytes(data), "bytes": len(data)}


def save_bytes(root: Path, repo_path: str, data: bytes) -> dict[str, Any]:
    path = root / repo_path
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"source-intake output is append-only; refusing to overwrite {path}")
    path.write_bytes(data)
    return output_record(repo_path, data)


def http_get(url: str, *, user_agent: str, timeout: int, headers: dict[str, str] | None = None) -> tuple[bytes, dict[str, Any]]:
    request_headers = {"User-Agent": user_agent}
    if headers:
        request_headers.update(headers)
    req = urllib.request.Request(url, headers=request_headers, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        data = response.read()
        metadata = {
            "requested_url": url,
            "final_url": response.geturl(),
            "status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
        }
        return data, metadata


def arxiv_date(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y%m%d%H%M")


def arxiv_retryable_error(exc: Exception) -> bool:
    if isinstance(exc, urllib.error.HTTPError):
        return exc.code == 429 or 500 <= exc.code < 600
    if isinstance(exc, (TimeoutError, urllib.error.URLError)):
        return True
    return False


def arxiv_retry_delay(exc: Exception, *, base_seconds: float, attempt: int) -> float:
    delay = base_seconds * (2 ** max(0, attempt - 1))
    if isinstance(exc, urllib.error.HTTPError) and exc.headers:
        retry_after = exc.headers.get("Retry-After")
        if retry_after:
            try:
                delay = max(delay, float(retry_after))
            except ValueError:
                pass
    return delay


def parse_arxiv_atom(data: bytes) -> list[dict[str, Any]]:
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(data)
    entries: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ns):
        authors = [
            (node.findtext("atom:name", default="", namespaces=ns) or "").strip()
            for node in entry.findall("atom:author", ns)
        ]
        categories = [node.attrib.get("term", "") for node in entry.findall("atom:category", ns)]
        links = [
            {"href": node.attrib.get("href"), "rel": node.attrib.get("rel"), "type": node.attrib.get("type")}
            for node in entry.findall("atom:link", ns)
        ]
        primary = entry.find("arxiv:primary_category", ns)
        entries.append(
            {
                "id": (entry.findtext("atom:id", default="", namespaces=ns) or "").strip(),
                "title": " ".join((entry.findtext("atom:title", default="", namespaces=ns) or "").split()),
                "summary": " ".join((entry.findtext("atom:summary", default="", namespaces=ns) or "").split()),
                "published": (entry.findtext("atom:published", default="", namespaces=ns) or "").strip(),
                "updated": (entry.findtext("atom:updated", default="", namespaces=ns) or "").strip(),
                "authors": authors,
                "categories": categories,
                "primary_category": primary.attrib.get("term") if primary is not None else None,
                "links": links,
            }
        )
    return entries


def run_arxiv(plan: dict[str, Any], cfg: dict[str, Any], output_root: Path) -> dict[str, Any]:
    issue_id = plan["issue_id"]
    start = parse_instant(plan["collection_window_start"])
    end = parse_instant(plan["collection_window_end"])
    observed_at = datetime.now(timezone.utc)
    base = run_base(issue_id, "arxiv", observed_at)
    outputs: list[dict[str, Any]] = []
    summary: dict[str, Any] = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "collector": "arxiv-api",
        "observed_at": iso_utc(observed_at),
        "collection_window_start": iso_utc(start),
        "collection_window_end": iso_utc(end),
        "queries": [],
        "entries": [],
        "errors": [],
    }
    seen: set[str] = set()
    successes = 0

    arxiv_cfg = cfg["arxiv"]
    queries = arxiv_cfg.get("queries", [])
    request_timeout = int(arxiv_cfg.get("request_timeout_seconds", cfg.get("http_timeout_seconds", 45)))
    max_attempts = max(1, int(arxiv_cfg.get("max_attempts", 1)))
    retry_backoff = float(arxiv_cfg.get("retry_backoff_seconds", arxiv_cfg.get("delay_seconds", 3)))
    for index, item in enumerate(queries):
        query_id = safe_id(item["id"])
        search_query = f"({item['search_query']}) AND submittedDate:[{arxiv_date(start)} TO {arxiv_date(end)}]"
        params = urllib.parse.urlencode(
            {
                "search_query": search_query,
                "start": 0,
                "max_results": int(arxiv_cfg.get("max_results_per_query", 200)),
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
        )
        url = f"{arxiv_cfg['endpoint']}?{params}"
        raw_path = f"{base}/raw/{query_id}.atom"
        attempts: list[dict[str, Any]] = []
        attempt_number = 0
        try:
            while attempt_number < max_attempts:
                attempt_number += 1
                try:
                    data, http_meta = http_get(
                        url,
                        user_agent=cfg["user_agent"],
                        timeout=request_timeout,
                    )
                    break
                except Exception as exc:
                    retryable = arxiv_retryable_error(exc)
                    attempt_record: dict[str, Any] = {
                        "attempt": attempt_number,
                        "error": repr(exc),
                        "retryable": retryable,
                    }
                    if not retryable or attempt_number >= max_attempts:
                        attempts.append(attempt_record)
                        raise
                    wait_seconds = arxiv_retry_delay(
                        exc,
                        base_seconds=retry_backoff,
                        attempt=attempt_number,
                    )
                    attempt_record["retry_delay_seconds"] = wait_seconds
                    attempts.append(attempt_record)
                    time.sleep(wait_seconds)
            else:
                raise RuntimeError("arXiv request exhausted attempts without a response")

            outputs.append(save_bytes(output_root, raw_path, data))
            parsed = parse_arxiv_atom(data)
            successes += 1
            summary["queries"].append({
                "id": item["id"],
                "search_query": search_query,
                "request": http_meta,
                "raw_path": raw_path,
                "entry_count": len(parsed),
                "attempt_count": attempt_number,
                "retry_history": attempts,
            })
            for entry in parsed:
                key = entry["id"]
                if key and key not in seen:
                    seen.add(key)
                    summary["entries"].append(entry)
        except Exception as exc:
            summary["errors"].append({
                "id": item["id"],
                "url": url,
                "error": repr(exc),
                "attempt_count": attempt_number,
                "retry_history": attempts,
            })
        if index + 1 < len(queries):
            time.sleep(float(arxiv_cfg.get("delay_seconds", 3)))

    summary["unique_entry_count"] = len(summary["entries"])
    summary_bytes = (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    outputs.append(save_bytes(output_root, f"{base}/summary.json", summary_bytes))
    status = "success" if successes == len(queries) else ("partial" if successes else "failed")
    run = collector_run(
        issue_id=issue_id, stage="paper-discovery", collector_id="arxiv-api", provider="arXiv",
        observed_at=observed_at, plan=plan, outputs=outputs, status=status,
        tool_access=["HTTPS GET https://export.arxiv.org/api/query"],
        notes=[
            "Raw Atom responses are preserved unchanged; summary.json is collector-derived metadata for later screening.",
            "Transient arXiv HTTP 429/5xx and transport timeout failures use configured conservative retry/backoff before the query is marked failed.",
        ],
    )
    write_json(output_root / f"{base}/collector-run.json", run)
    return run


def in_window(value: str | None, start: datetime, end: datetime) -> bool:
    if not value:
        return False
    try:
        dt = parse_instant(value)
    except ValueError:
        return False
    return start <= dt <= end


def run_github_releases(plan: dict[str, Any], cfg: dict[str, Any], output_root: Path) -> dict[str, Any]:
    issue_id = plan["issue_id"]
    start = parse_instant(plan["collection_window_start"])
    end = parse_instant(plan["collection_window_end"])
    observed_at = datetime.now(timezone.utc)
    base = run_base(issue_id, "github-releases", observed_at)
    outputs: list[dict[str, Any]] = []
    summary: dict[str, Any] = {
        "schema_version": "1.0", "issue_id": issue_id, "collector": "github-releases",
        "observed_at": iso_utc(observed_at), "collection_window_start": iso_utc(start),
        "collection_window_end": iso_utc(end), "repositories": [], "matching_releases": [], "errors": [],
    }
    gh_cfg = cfg["github_releases"]
    token = os.environ.get("GITHUB_TOKEN")
    successes = 0

    for repo in gh_cfg.get("repositories", []):
        slug = safe_id(repo.replace("/", "__"))
        params = urllib.parse.urlencode({"per_page": int(gh_cfg.get("per_page", 100))})
        url = f"https://api.github.com/repos/{repo}/releases?{params}"
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": gh_cfg.get("api_version", "2026-03-10")}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        raw_path = f"{base}/raw/{slug}.json"
        try:
            data, http_meta = http_get(url, user_agent=cfg["user_agent"], timeout=int(cfg.get("http_timeout_seconds", 45)), headers=headers)
            outputs.append(save_bytes(output_root, raw_path, data))
            releases = json.loads(data.decode("utf-8"))
            if not isinstance(releases, list):
                raise ValueError("GitHub Releases API response was not a list")
            matches = []
            for release in releases:
                if release.get("draft"):
                    continue
                timestamp = release.get("published_at") or release.get("created_at")
                if in_window(timestamp, start, end):
                    item = {
                        "repository": repo, "id": release.get("id"), "tag_name": release.get("tag_name"),
                        "name": release.get("name"), "html_url": release.get("html_url"),
                        "created_at": release.get("created_at"), "published_at": release.get("published_at"),
                        "prerelease": bool(release.get("prerelease")),
                    }
                    matches.append(item)
                    summary["matching_releases"].append(item)
            successes += 1
            summary["repositories"].append({
                "repository": repo, "request": http_meta, "raw_path": raw_path,
                "returned_release_count": len(releases), "window_match_count": len(matches)
            })
        except Exception as exc:
            summary["errors"].append({"repository": repo, "url": url, "error": repr(exc)})

    summary["matching_release_count"] = len(summary["matching_releases"])
    summary_bytes = (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    outputs.append(save_bytes(output_root, f"{base}/summary.json", summary_bytes))
    total = len(gh_cfg.get("repositories", []))
    status = "success" if successes == total else ("partial" if successes else "failed")
    run = collector_run(
        issue_id=issue_id, stage="github-discovery", collector_id="github-releases", provider="GitHub REST API",
        observed_at=observed_at, plan=plan, outputs=outputs, status=status,
        tool_access=["GitHub REST Releases API"],
        notes=["The configured repository watchlist is intentionally curated and is not a complete search of GitHub."],
    )
    write_json(output_root / f"{base}/collector-run.json", run)
    return run


def run_official_pages(plan: dict[str, Any], cfg: dict[str, Any], output_root: Path) -> dict[str, Any]:
    issue_id = plan["issue_id"]
    observed_at = datetime.now(timezone.utc)
    base = run_base(issue_id, "official-pages", observed_at)
    outputs: list[dict[str, Any]] = []
    summary: dict[str, Any] = {
        "schema_version": "1.0", "issue_id": issue_id, "collector": "official-pages",
        "observed_at": iso_utc(observed_at), "pages": [], "errors": [],
    }
    pages = cfg["official_pages"].get("pages", [])
    successes = 0
    for item in pages:
        page_id = safe_id(item["id"])
        raw_path = f"{base}/raw/{page_id}.html"
        try:
            data, http_meta = http_get(item["url"], user_agent=cfg["user_agent"], timeout=int(cfg.get("http_timeout_seconds", 45)))
            outputs.append(save_bytes(output_root, raw_path, data))
            successes += 1
            summary["pages"].append({
                "id": item["id"], "url": item["url"], "request": http_meta, "raw_path": raw_path,
                "sha256": sha256_bytes(data), "bytes": len(data)
            })
        except Exception as exc:
            summary["errors"].append({"id": item["id"], "url": item["url"], "error": repr(exc)})

    summary_bytes = (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    outputs.append(save_bytes(output_root, f"{base}/summary.json", summary_bytes))
    total = len(pages)
    status = "success" if successes == total else ("partial" if successes else "failed")
    run = collector_run(
        issue_id=issue_id, stage="official-source-discovery", collector_id="official-pages", provider="Official publisher websites",
        observed_at=observed_at, plan=plan, outputs=outputs, status=status,
        tool_access=["HTTPS GET configured official news/blog index pages"],
        notes=[
            "This collector records deterministic snapshots of configured official index pages; it is not a complete web-discovery system.",
            "HTML snapshots are Raw observations. Technical claims still require candidate-specific primary-source verification.",
        ],
    )
    write_json(output_root / f"{base}/collector-run.json", run)
    return run


def collector_run(*, issue_id: str, stage: str, collector_id: str, provider: str, observed_at: datetime,
                  plan: dict[str, Any], outputs: list[dict[str, Any]], status: str,
                  tool_access: list[str], notes: list[str]) -> dict[str, Any]:
    stamp = run_stamp(observed_at)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "run_id": f"{collector_id}-{issue_id}-{stamp}",
        "stage": stage,
        "collector": {"id": collector_id, "provider": provider, "model": None, "prompt_id": None, "prompt_version": None, "prompt_hash": None},
        "time": {
            "started_at": None, "completed_at": iso_utc(observed_at), "observed_at": iso_utc(observed_at),
            "collection_window_start": plan.get("collection_window_start"),
            "collection_window_end": plan.get("collection_window_end"),
            "editorial_cutoff": plan["editorial_cutoff"],
        },
        "inputs": ["config/source-intake.json", "weekly plan"],
        "outputs": outputs,
        "tool_access": tool_access,
        "status": status,
        "notes": notes,
    }


def selected_collectors(value: str) -> list[str]:
    return ["arxiv", "github", "official"] if value == "all" else [value]


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

    cfg = load_json(config_path)
    plan = load_json(plan_path)
    if not plan.get("collection_window_start"):
        raise SystemExit("collection_window_start is unset; source intake refuses to guess a window start")

    runs = []
    for collector in selected_collectors(args.collector):
        if collector == "arxiv" and cfg["arxiv"].get("enabled", True):
            runs.append(run_arxiv(plan, cfg, output_root))
        elif collector == "github" and cfg["github_releases"].get("enabled", True):
            runs.append(run_github_releases(plan, cfg, output_root))
        elif collector == "official" and cfg["official_pages"].get("enabled", True):
            runs.append(run_official_pages(plan, cfg, output_root))

    failed = [run for run in runs if run["status"] == "failed"]
    partial = [run for run in runs if run["status"] == "partial"]
    report = {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "collector_count": len(runs),
        "runs": [{"run_id": r["run_id"], "collector": r["collector"]["id"], "status": r["status"]} for r in runs],
        "overall_status": "failed" if failed else ("partial" if partial else "success"),
    }
    write_json(output_root / "source-intake-report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
