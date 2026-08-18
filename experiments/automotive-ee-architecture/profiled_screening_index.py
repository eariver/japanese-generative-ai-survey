#!/usr/bin/env python3
"""Experiment-only page-role adapter around the production Screening normalizer.

The production normalizer intentionally remains unchanged. This adapter calls its
record builders first, then applies domain-profile semantics only to official HTML
pages explicitly declared as ITEM rather than INDEX. It preserves Raw provenance and
reuses the production batching/manifest primitives.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = SCRIPT_PATH.parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_screening_index as base


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def page_roles(profile: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for page in (profile.get("official_pages") or {}).get("pages", []):
        page_id = page.get("id")
        role = page.get("page_role", "INDEX")
        if not isinstance(page_id, str) or not page_id:
            raise ValueError("official page id must be non-empty")
        if role not in {"INDEX", "ITEM"}:
            raise ValueError(f"unsupported page_role for {page_id}: {role!r}")
        result[page_id] = role
    return result


def apply_page_roles(*, input_root: Path, records: list[dict[str, Any]], profile: dict[str, Any]) -> list[dict[str, Any]]:
    roles = page_roles(profile)
    transformed: list[dict[str, Any]] = []
    for original in records:
        record = dict(original)
        screening_id = record.get("screening_id")
        if not isinstance(screening_id, str) or not screening_id.startswith("official-index:"):
            transformed.append(record)
            continue
        page_id = screening_id.removeprefix("official-index:")
        if roles.get(page_id) != "ITEM":
            transformed.append(record)
            continue
        raw_paths = record.get("raw_paths") or []
        if len(raw_paths) != 1:
            raise ValueError(f"ITEM page {page_id} must reference exactly one Raw path")
        raw_path = input_root / raw_paths[0]
        if not raw_path.is_file():
            raise ValueError(f"ITEM page Raw file missing: {raw_path}")
        metadata = dict(record.get("metadata") or {})
        metadata["profile_page_role"] = "ITEM"
        metadata["requires_page_item_extraction"] = False
        record["source_type"] = "official-page-snapshot"
        record["summary_text"] = base.html_visible_text(raw_path.read_bytes())
        record["metadata"] = metadata
        transformed.append(record)
    return sorted(
        transformed,
        key=lambda r: (r["source_type"], r.get("published_at") or "", r["screening_id"]),
    )


def build(*, input_root: Path, output_dir: Path, issue_id: str, profile_path: Path,
          max_records: int = 40, max_chars: int = 80000) -> dict[str, Any]:
    profile = load_json(profile_path)
    records = base.build_records(input_root, issue_id)
    records = apply_page_roles(input_root=input_root, records=records, profile=profile)

    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "screening-index.jsonl"
    base.write_jsonl(index_path, records)
    batch_dir = output_dir / "batches"
    batches = base.make_batches(records, max_records=max_records, max_chars=max_chars)
    batch_meta: list[dict[str, Any]] = []
    for number, batch in enumerate(batches, start=1):
        path = batch_dir / f"batch-{number:03d}.jsonl"
        base.write_jsonl(path, batch)
        batch_meta.append({
            "batch": number,
            "path": path.relative_to(output_dir).as_posix(),
            "record_count": len(batch),
            "sha256": base.sha256_file(path),
            "bytes": path.stat().st_size,
        })

    counts = Counter(record["source_type"] for record in records)
    item_pages = sum(1 for record in records if record["source_type"] == "official-page-snapshot")
    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "experiment": "PROFILED_SCREENING_NORMALIZATION",
        "profile": profile_path.as_posix(),
        "record_count": len(records),
        "counts_by_source_type": dict(sorted(counts.items())),
        "profiled_item_page_count": item_pages,
        "screening_index": {
            "path": "screening-index.jsonl",
            "sha256": base.sha256_file(index_path),
            "bytes": index_path.stat().st_size,
        },
        "batch_policy": {"max_records": max_records, "max_json_chars": max_chars},
        "batch_count": len(batches),
        "batches": batch_meta,
        "semantics": [
            "Production build_screening_index.py remains unchanged.",
            "Official HTML explicitly profiled as ITEM is represented as official-page-snapshot with derived visible text and requires_page_item_extraction=false.",
            "Official HTML profiled as INDEX retains the production official-index-snapshot behavior.",
            "Raw HTTP bytes remain authoritative through raw_paths; visible text is a derived screening convenience only."
        ]
    }
    base.write_json(output_dir / "screening-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--max-records", type=int, default=40)
    parser.add_argument("--max-json-chars", type=int, default=80000)
    args = parser.parse_args()
    manifest = build(
        input_root=Path(args.input_root).resolve(),
        output_dir=Path(args.output_dir).resolve(),
        issue_id=args.issue_id,
        profile_path=Path(args.profile),
        max_records=args.max_records,
        max_chars=args.max_json_chars,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
