#!/usr/bin/env python3
"""Limit Half-year Technical Note enrichment to cards that are actually reader-rendered.

The selected Evidence set also contains chronology-only and other non-card roles. Earlier
fail-closed enrichment walked every selected Evidence record and therefore required a
reader-facing Technical Notes technical point even for items that never appear in a Technical
Notes file. That is the wrong scope: provenance must remain strict for rendered cards, while a
chronology-only item should keep its selected Evidence/chronology identity without inventing a
Technical Notes claim solely to satisfy the regeneration pipeline.

V28 preserves the V3 component/variant/property binding contract and changes only the enrichment
scope. It derives the current rendered Technical Note titles from the state-pinned source and
applies Screening-backed signal extraction / hash-bound overrides only to those titles.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v13 as event
from scripts import revise_special_half_year_review_repairs_v27 as base


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def _title_key(value: str) -> str:
    text = str(value or "")
    for encoded, plain in (
        (r"\&", "&"),
        (r"\_", "_"),
        (r"\%", "%"),
        (r"\#", "#"),
        (r"\{", "{"),
        (r"\}", "}"),
    ):
        text = text.replace(encoded, plain)
    return re.sub(r"\s+", " ", text).strip().lower()


def _rendered_technical_note_titles(repo_root: Path, manifest: dict[str, Any]) -> set[str]:
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    state = _load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_rel = str(source.get("path") or "")
    current_manifest_path = repo_root / manifest_rel
    if not manifest_rel or not current_manifest_path.is_file():
        raise ValueError("state-pinned validated source manifest missing while resolving rendered Technical Notes")
    current_manifest = _load_json(current_manifest_path)
    source_dir = current_manifest_path.parent

    titles: set[str] = set()
    for article in current_manifest.get("articles") or []:
        if not isinstance(article, dict) or article.get("technical_notes_reader_facing") is not True:
            continue
        rel = str(article.get("technical_notes_path") or "")
        path = source_dir / rel
        if not rel or not path.is_file():
            raise ValueError(f"state-pinned reader-facing Technical Notes file missing: {rel}")
        for match in event.core.NOTE_RE.finditer(path.read_text(encoding="utf-8")):
            titles.add(_title_key(match.group(1)))
    if not titles:
        raise ValueError("state-pinned source contains no reader-facing Technical Note cards")
    return titles


def _merge_rendered_scope(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    index = event.impl._ORIGINAL_MERGE(repo_root, manifest)
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    rendered_titles = _rendered_technical_note_titles(repo_root, manifest)
    screening_by_url, queue_path = event._screening_index_with_source_type(repo_root, issue_id)
    queue_sha = event.impl._sha256(queue_path)

    for override_title, override in event.impl._ACTIVE_OVERRIDES.items():
        if _title_key(override_title) not in rendered_titles:
            continue
        expected_queue_sha = str(override.get("_expected_queue_sha256") or "").strip()
        if expected_queue_sha != queue_sha:
            raise ValueError(
                f"Technical Notes detail override Screening digest mismatch for {override_title}: "
                f"actual={queue_sha} expected={expected_queue_sha}"
            )

    seen: set[int] = set()
    enriched = 0
    skipped_nonrendered = 0
    for title, info in list(index.items()):
        identity = id(info)
        if identity in seen:
            continue
        seen.add(identity)
        canonical_title = str(info.get("canonical_title") or title)
        if _title_key(canonical_title) not in rendered_titles:
            skipped_nonrendered += 1
            continue

        records: list[dict[str, Any]] = []
        for url in info.get("urls") or []:
            record = screening_by_url.get(event.impl._normalize_url(str(url)))
            if record is not None and record not in records:
                records.append(record)
        if not records:
            raise ValueError(
                f"Rendered selected Evidence has no matching accepted Screening provenance for Technical Notes: "
                f"{canonical_title} urls={info.get('urls')}"
            )
        info["screening_records"] = records
        info["screening_queue_path"] = queue_path.relative_to(repo_root).as_posix()
        info["screening_queue_sha256"] = queue_sha

        override = event.impl._ACTIVE_OVERRIDES.get(canonical_title)
        if override is not None:
            points = event.impl._validate_override(canonical_title, override, info)
            info["technical_points"] = points
            info["technical_point_mode"] = "EDITORIAL_OVERRIDE"
            enriched += 1
            continue

        signals: list[str] = []
        events = list(info.get("events") or [])
        for record in records:
            for signal in event._safe_technical_signals(
                str(record.get("summary_text") or ""),
                events,
                canonical_title,
            ):
                if signal not in signals:
                    signals.append(signal)
                if len(signals) >= 7:
                    break
            if len(signals) >= 7:
                break
        if not signals:
            raise ValueError(
                f"Event-bounded accepted Screening provenance is too thin for reader-facing Technical Notes: "
                f"{canonical_title}. Provide a hash-bound editorial technical-point override instead of widening the source window."
            )
        info["technical_points"] = [
            "対象event近傍の一次資料から " + " / ".join(signals) + " を確認できる。"
        ]
        info["technical_point_mode"] = "EVENT_BOUNDED_SCREENING_SIGNAL_EXTRACTION"
        enriched += 1

    # Non-reader Evidence remains in the returned index for chronology/selection provenance;
    # only reader-card enrichment is scoped. The counters are attached to the manifest-local
    # index metadata through a synthetic private key only during this build and removed by the
    # ordinary downstream renderer, which iterates canonical Evidence records.
    manifest.setdefault("_technical_note_enrichment_scope", {})
    if isinstance(manifest["_technical_note_enrichment_scope"], dict):
        manifest["_technical_note_enrichment_scope"].update(
            {
                "rendered_title_count": len(rendered_titles),
                "enriched_record_count": enriched,
                "skipped_nonrendered_record_count": skipped_nonrendered,
            }
        )
    return index


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_merge = event._merge_event_bounded
    event._merge_event_bounded = _merge_rendered_scope
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        event._merge_event_bounded = previous_merge
    if isinstance(result, dict):
        result["technical_note_enrichment_scope"] = "CURRENT_READER_RENDERED_CARDS_ONLY_V1"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
