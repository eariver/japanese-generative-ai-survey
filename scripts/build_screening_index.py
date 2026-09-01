#!/usr/bin/env python3
"""Build deterministic, batchable screening records from source-intake artifacts.

This is a loss-minimizing normalization layer, not an editorial ranking step.
Raw HTTP bytes remain authoritative and untouched. The output JSONL makes each
paper/release/feed item small enough for later LLM screening in bounded batches.
"""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
        dt = datetime.fromisoformat(normalized)
        if dt.tzinfo is not None:
            return dt.astimezone(timezone.utc)
    except ValueError:
        pass
    try:
        dt = email.utils.parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        return None


def in_window(value: str | None, start: datetime | None, end: datetime | None) -> bool:
    dt = parse_datetime(value)
    if dt is None:
        return False
    if start and dt < start:
        return False
    if end and dt > end:
        return False
    return True


def normalize_ws(value: str | None) -> str:
    return " ".join((value or "").split())


def html_visible_text(data: bytes, limit: int = 12000) -> str | None:
    """Return a bounded, derived text view for item-level supplemental HTML.

    Raw bytes remain authoritative. This helper exists only so Screening receives
    enough content to triage a specifically audited first-party page instead of
    seeing an opaque page id.
    """
    if not data:
        return None
    text = data.decode("utf-8", errors="replace")
    text = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1\s*>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    text = normalize_ws(text)
    return text[:limit] or None


def screening_record(
    *,
    issue_id: str,
    screening_id: str,
    source_type: str,
    collector_id: str,
    collector_run_id: str,
    observed_at: str,
    title: str,
    locator: str,
    raw_paths: list[str],
    published_at: str | None,
    summary_text: str | None,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "screening_id": screening_id,
        "source_type": source_type,
        "collector_id": collector_id,
        "collector_run_id": collector_run_id,
        "observed_at": observed_at,
        "title": normalize_ws(title),
        "locator": locator,
        "raw_paths": raw_paths,
        "published_at": published_at,
        "summary_text": normalize_ws(summary_text) if summary_text else None,
        "metadata": metadata,
    }


def arxiv_records(run_dir: Path, run: dict[str, Any], summary: dict[str, Any]) -> Iterable[dict[str, Any]]:
    query_raw_paths = [item["raw_path"] for item in summary.get("queries", []) if item.get("raw_path")]
    for entry in summary.get("entries", []):
        locator = entry.get("id") or ""
        if not locator:
            continue
        paper_id = locator.rstrip("/").split("/")[-1]
        yield screening_record(
            issue_id=run["issue_id"],
            screening_id=f"arxiv:{paper_id}",
            source_type="paper",
            collector_id=run["collector"]["id"],
            collector_run_id=run["run_id"],
            observed_at=run["time"]["observed_at"],
            title=entry.get("title", ""),
            locator=locator,
            raw_paths=query_raw_paths,
            published_at=entry.get("published"),
            summary_text=entry.get("summary"),
            metadata={
                "authors": entry.get("authors", []),
                "categories": entry.get("categories", []),
                "primary_category": entry.get("primary_category"),
                "updated": entry.get("updated"),
                "links": entry.get("links", []),
            },
        )


def github_release_records(input_root: Path, run: dict[str, Any], summary: dict[str, Any]) -> Iterable[dict[str, Any]]:
    raw_by_release_id: dict[str, tuple[dict[str, Any], str]] = {}
    for repo_info in summary.get("repositories", []):
        raw_path = repo_info.get("raw_path")
        if not raw_path:
            continue
        full = input_root / raw_path
        if not full.is_file():
            continue
        try:
            releases = load_json(full)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(releases, list):
            continue
        for release in releases:
            rid = str(release.get("id", ""))
            if rid:
                raw_by_release_id[rid] = (release, raw_path)

    for item in summary.get("matching_releases", []):
        rid = str(item.get("id", ""))
        raw_release, raw_path = raw_by_release_id.get(rid, ({}, ""))
        repo = item.get("repository", "")
        tag = item.get("tag_name") or rid
        locator = item.get("html_url") or f"https://github.com/{repo}/releases/tag/{tag}"
        body = raw_release.get("body") or ""
        body_limit = 12000
        excerpt = body[:body_limit]
        yield screening_record(
            issue_id=run["issue_id"],
            screening_id=f"github-release:{repo}@{tag}",
            source_type="github-release",
            collector_id=run["collector"]["id"],
            collector_run_id=run["run_id"],
            observed_at=run["time"]["observed_at"],
            title=item.get("name") or tag or repo,
            locator=locator,
            raw_paths=[raw_path] if raw_path else [],
            published_at=item.get("published_at") or item.get("created_at"),
            summary_text=excerpt or None,
            metadata={
                "repository": repo,
                "release_id": item.get("id"),
                "tag_name": item.get("tag_name"),
                "prerelease": item.get("prerelease", False),
                "created_at": item.get("created_at"),
                "body_truncated": len(body) > body_limit,
                "body_original_chars": len(body),
            },
        )


def _rss_items(data: bytes) -> list[dict[str, str | None]]:
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return []

    items: list[dict[str, str | None]] = []
    root_name = root.tag.rsplit("}", 1)[-1].lower()
    if root_name == "rss":
        for item in root.findall("./channel/item"):
            items.append(
                {
                    "title": item.findtext("title"),
                    "link": item.findtext("link"),
                    "published": item.findtext("pubDate"),
                    "summary": item.findtext("description"),
                    "guid": item.findtext("guid"),
                }
            )
        return items

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    if root_name == "feed":
        for entry in root.findall("atom:entry", ns):
            link = None
            for node in entry.findall("atom:link", ns):
                if node.attrib.get("rel") in (None, "alternate"):
                    link = node.attrib.get("href")
                    if link:
                        break
            items.append(
                {
                    "title": entry.findtext("atom:title", namespaces=ns),
                    "link": link,
                    "published": entry.findtext("atom:published", namespaces=ns)
                    or entry.findtext("atom:updated", namespaces=ns),
                    "summary": entry.findtext("atom:summary", namespaces=ns)
                    or entry.findtext("atom:content", namespaces=ns),
                    "guid": entry.findtext("atom:id", namespaces=ns),
                }
            )
    return items


def official_records(input_root: Path, run: dict[str, Any], summary: dict[str, Any]) -> Iterable[dict[str, Any]]:
    start = parse_datetime(run.get("time", {}).get("collection_window_start"))
    end = parse_datetime(run.get("time", {}).get("collection_window_end"))
    for page in summary.get("pages", []):
        raw_path = page.get("raw_path")
        if not raw_path:
            continue
        full = input_root / raw_path
        data = full.read_bytes() if full.is_file() else b""

        if page.get("supplemental") is True:
            yield screening_record(
                issue_id=run["issue_id"],
                screening_id=f"official-index:{page.get('id')}",
                source_type="official-index-snapshot",
                collector_id=run["collector"]["id"],
                collector_run_id=run["run_id"],
                observed_at=run["time"]["observed_at"],
                title=page.get("title") or page.get("id", "supplemental primary source"),
                locator=page.get("url", ""),
                raw_paths=[raw_path],
                published_at=page.get("published_at"),
                summary_text=html_visible_text(data),
                metadata={
                    "content_type": page.get("request", {}).get("content_type"),
                    "etag": page.get("request", {}).get("etag"),
                    "last_modified": page.get("request", {}).get("last_modified"),
                    "bytes": page.get("bytes"),
                    "supplemental": True,
                    "publisher": page.get("publisher"),
                    "coverage_gap_reason": page.get("coverage_gap_reason"),
                    "supplemental_metadata": page.get("metadata", {}),
                    "requires_page_item_extraction": False,
                },
            )
            continue

        feed_items = _rss_items(data)
        emitted = False
        for index, item in enumerate(feed_items):
            published = item.get("published")
            if (start or end) and not in_window(published, start, end):
                continue
            locator = item.get("link") or item.get("guid") or page.get("url")
            if not locator:
                continue
            stable = item.get("guid") or item.get("link") or f"{page.get('id')}:{index}"
            screening_id = "official-feed:" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:20]
            emitted = True
            yield screening_record(
                issue_id=run["issue_id"],
                screening_id=screening_id,
                source_type="official-feed-item",
                collector_id=run["collector"]["id"],
                collector_run_id=run["run_id"],
                observed_at=run["time"]["observed_at"],
                title=item.get("title") or page.get("id", ""),
                locator=locator,
                raw_paths=[raw_path],
                published_at=published,
                summary_text=item.get("summary"),
                metadata={"publisher_page_id": page.get("id"), "publisher_index_url": page.get("url")},
            )

        if not emitted:
            yield screening_record(
                issue_id=run["issue_id"],
                screening_id=f"official-index:{page.get('id')}",
                source_type="official-index-snapshot",
                collector_id=run["collector"]["id"],
                collector_run_id=run["run_id"],
                observed_at=run["time"]["observed_at"],
                title=page.get("id", "official index snapshot"),
                locator=page.get("url", ""),
                raw_paths=[raw_path],
                published_at=None,
                summary_text=None,
                metadata={
                    "content_type": page.get("request", {}).get("content_type"),
                    "etag": page.get("request", {}).get("etag"),
                    "last_modified": page.get("request", {}).get("last_modified"),
                    "bytes": page.get("bytes"),
                    "requires_page_item_extraction": True,
                },
            )


def discover_runs(input_root: Path, issue_id: str) -> list[Path]:
    pattern = f"**/sources/{issue_id}/collectors/*/runs/*/collector-run.json"
    return sorted(input_root.glob(pattern))


def build_records(input_root: Path, issue_id: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for run_path in discover_runs(input_root, issue_id):
        run = load_json(run_path)
        summary_path = run_path.parent / "summary.json"
        if not summary_path.is_file():
            continue
        summary = load_json(summary_path)
        collector_id = run.get("collector", {}).get("id")
        if collector_id == "arxiv-api":
            records.extend(arxiv_records(run_path.parent, run, summary))
        elif collector_id == "github-releases":
            records.extend(github_release_records(input_root, run, summary))
        elif collector_id == "official-pages":
            records.extend(official_records(input_root, run, summary))

    unique: dict[str, dict[str, Any]] = {}
    for record in records:
        key = record["screening_id"]
        if key not in unique:
            unique[key] = record
    return sorted(
        unique.values(),
        key=lambda r: (r["source_type"], r.get("published_at") or "", r["screening_id"]),
    )


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def make_batches(records: list[dict[str, Any]], max_records: int, max_chars: int) -> list[list[dict[str, Any]]]:
    batches: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_chars = 0
    for record in records:
        encoded_chars = len(json.dumps(record, ensure_ascii=False))
        if current and (len(current) >= max_records or current_chars + encoded_chars > max_chars):
            batches.append(current)
            current = []
            current_chars = 0
        current.append(record)
        current_chars += encoded_chars
    if current:
        batches.append(current)
    return batches


def build(input_root: Path, output_dir: Path, issue_id: str, max_records: int, max_chars: int) -> dict[str, Any]:
    records = build_records(input_root, issue_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "screening-index.jsonl"
    write_jsonl(index_path, records)

    batch_dir = output_dir / "batches"
    batches = make_batches(records, max_records=max_records, max_chars=max_chars)
    batch_meta = []
    for number, batch in enumerate(batches, start=1):
        path = batch_dir / f"batch-{number:03d}.jsonl"
        write_jsonl(path, batch)
        batch_meta.append(
            {
                "batch": number,
                "path": path.relative_to(output_dir).as_posix(),
                "record_count": len(batch),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )

    counts = Counter(record["source_type"] for record in records)
    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "record_count": len(records),
        "counts_by_source_type": dict(sorted(counts.items())),
        "screening_index": {
            "path": "screening-index.jsonl",
            "sha256": sha256_file(index_path),
            "bytes": index_path.stat().st_size,
        },
        "batch_policy": {"max_records": max_records, "max_json_chars": max_chars},
        "batch_count": len(batches),
        "batches": batch_meta,
        "semantics": [
            "This layer normalizes source-intake outputs; it does not rank or reject candidates.",
            "Raw HTTP bytes remain authoritative and are referenced through raw_paths.",
            "ordinary official-index-snapshot means the index page still needs item-level extraction during screening.",
            "supplemental official-index-snapshot records are audited item-level first-party pages and retain title/date/derived text with requires_page_item_extraction=false.",
        ],
    }
    write_json(output_dir / "screening-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--max-records", type=int, default=40)
    parser.add_argument("--max-json-chars", type=int, default=80000)
    args = parser.parse_args()

    manifest = build(
        Path(args.input_root).resolve(),
        Path(args.output_dir).resolve(),
        args.issue_id,
        max_records=args.max_records,
        max_chars=args.max_json_chars,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
