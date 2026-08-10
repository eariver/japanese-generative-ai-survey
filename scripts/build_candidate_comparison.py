#!/usr/bin/env python3
"""Build a deterministic pre-selection comparison substrate from validated Evidence Runs.

This stage does not rank or select candidates. It projects the Evidence Card into
stable comparison fields and computes only conservative temporal-position hints.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from scripts import materialize_candidate_records as materializer

POSITION_ORDER = ["PRE_WINDOW", "MAIN_WINDOW", "CUTOFF_DAY_UNRESOLVED", "POST_CUTOFF", "UNKNOWN"]


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            rows.append(value)
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for value in values:
            fh.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def parse_date_only(value: str | None) -> date | None:
    if not value:
        return None
    if "T" in value or " " in value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def temporal_position(value: str | None, start: datetime, cutoff: datetime) -> str:
    exact = parse_datetime(value)
    if exact is not None:
        if exact < start:
            return "PRE_WINDOW"
        if exact > cutoff:
            return "POST_CUTOFF"
        return "MAIN_WINDOW"

    day = parse_date_only(value)
    if day is None:
        return "UNKNOWN"
    start_day = start.date()
    cutoff_day = cutoff.date()
    if day < start_day:
        return "PRE_WINDOW"
    if day > cutoff_day:
        return "POST_CUTOFF"
    if day == cutoff_day:
        return "CUTOFF_DAY_UNRESOLVED"
    return "MAIN_WINDOW"


def task_index(tasks_dir: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for path in sorted(tasks_dir.glob("*.json")):
        task = read_json(path)
        task_id = task.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError(f"{path}: evidence_task_id missing")
        if task_id in index:
            raise ValueError(f"duplicate evidence_task_id in tasks: {task_id}")
        index[task_id] = task
    return index


def compact_text(value: str | None, limit: int = 180) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def build_record(item: dict[str, Any], task: dict[str, Any], start: datetime, cutoff: datetime) -> dict[str, Any]:
    card = item["card"]
    artifact = card["artifact"]
    editorial = card["editorial"]
    grouping = card["grouping_resolution"]

    recommendation = editorial["candidate_recommendation"]
    candidate_id = None
    if recommendation == "CANDIDATE" and not grouping.get("split_recommended"):
        candidate_id = materializer.candidate_id(item)

    events: list[dict[str, Any]] = []
    positions: set[str] = set()
    for event in card["temporal"].get("events") or []:
        position = temporal_position(event.get("event_date"), start, cutoff)
        positions.add(position)
        events.append(
            {
                "event_type": event["event_type"],
                "event_date": event.get("event_date"),
                "source_published_at": event.get("source_published_at"),
                "position_hint": position,
            }
        )
    if not positions:
        positions.add("UNKNOWN")

    source_counts = Counter(source["source_class"] for source in card.get("sources") or [])
    claim_counts = Counter(claim["evidence_class"] for claim in card.get("claims") or [])

    return {
        "schema_version": "1.0",
        "issue_id": item["issue_id"],
        "comparison_id": item["evidence_task_id"],
        "candidate_id": candidate_id,
        "evidence_task_id": item["evidence_task_id"],
        "artifact": {
            "canonical_name": artifact["canonical_name"],
            "artifact_type": artifact["artifact_type"],
            "organization": artifact.get("organization"),
            "canonical_url": artifact.get("canonical_url"),
        },
        "evidence": {
            "status": card["status"],
            "recommendation": recommendation,
            "rationale": editorial["rationale"],
            "why_now_confirmed": editorial["why_now_confirmed"],
            "why_now_note": editorial.get("why_now_note"),
            "grouping_note": grouping.get("note"),
        },
        "temporal": {
            "artifact_first_announced": card["temporal"].get("artifact_first_announced"),
            "events": events,
            "position_hints": [position for position in POSITION_ORDER if position in positions],
        },
        "topic_lanes": sorted(set(task.get("topic_lanes") or [])),
        "source_depth": {
            "total": len(card.get("sources") or []),
            "by_class": dict(sorted(source_counts.items())),
        },
        "claim_counts": dict(sorted(claim_counts.items())),
        "metric_count": len(card.get("metrics") or []),
        "limitation_count": len(card.get("limitations") or []),
        "unresolved_questions": list(card["verification"].get("unresolved_questions") or []),
        "contradictions": list(card["verification"].get("contradictions") or []),
    }


def markdown(records: list[dict[str, Any]], issue_id: str, start: str, cutoff: str) -> str:
    lines = [
        f"# {issue_id} Deterministic Candidate Comparison Substrate",
        "",
        "Status: pre-selection; generated from validated Evidence Runs. This file does not rank or select stories.",
        "",
        f"- Collection window start: `{start}`",
        f"- Editorial cutoff: `{cutoff}`",
        "- Temporal hints are conservative machine classifications. `CUTOFF_DAY_UNRESOLVED` means the Evidence Card has only a date on cutoff day, so the event cannot safely be placed before/after 18:00 America/New_York.",
        "",
        "| ID | Artifact | Type | Evidence route | Timing hints | Sources | Claims / metrics | Remaining boundary |",
        "|---|---|---|---|---|---:|---|---|",
    ]
    for record in records:
        identifier = record["candidate_id"] or record["comparison_id"]
        positions = ", ".join(record["temporal"]["position_hints"])
        claim_summary = ", ".join(f"{key}:{value}" for key, value in record["claim_counts"].items()) or "none"
        claim_summary += f"; metrics:{record['metric_count']}"
        boundaries = list(record["unresolved_questions"]) + list(record["contradictions"])
        if not boundaries and record["limitation_count"]:
            boundary_text = f"{record['limitation_count']} recorded limitation(s)"
        elif boundaries:
            boundary_text = compact_text(" / ".join(boundaries))
        else:
            boundary_text = "none recorded"
        lines.append(
            "| `{}` | {} | `{}` | `{}` / `{}` | {} | {} | {} | {} |".format(
                identifier,
                record["artifact"]["canonical_name"].replace("|", "\\|"),
                record["artifact"]["artifact_type"],
                record["evidence"]["status"],
                record["evidence"]["recommendation"],
                positions,
                record["source_depth"]["total"],
                claim_summary,
                boundary_text.replace("|", "\\|"),
            )
        )
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "The next stage is explicit Candidate Selection. No role assignment in this comparison substrate implies inclusion, page budget, or article priority.",
            "",
        ]
    )
    return "\n".join(lines)


def build(evidence_reviewed: Path, tasks_dir: Path, pipeline_state: Path, output_dir: Path) -> tuple[dict[str, Any], bool]:
    items = read_jsonl(evidence_reviewed)
    if not items:
        raise ValueError("evidence-reviewed input is empty")
    state = read_json(pipeline_state)
    calendar = state.get("calendar") or {}
    start_text = calendar.get("collection_window_start")
    cutoff_text = calendar.get("editorial_cutoff")
    start = parse_datetime(start_text)
    cutoff = parse_datetime(cutoff_text)
    if start is None or cutoff is None:
        raise ValueError("pipeline state must contain timezone-aware collection_window_start and editorial_cutoff")
    if start > cutoff:
        raise ValueError("collection_window_start must not be after editorial_cutoff")

    issue_ids = {item.get("issue_id") for item in items}
    if len(issue_ids) != 1 or None in issue_ids:
        raise ValueError(f"evidence-reviewed must contain exactly one issue_id: {issue_ids}")
    issue_id = next(iter(issue_ids))
    if state.get("issue_id") != issue_id:
        raise ValueError("pipeline-state issue_id does not match evidence-reviewed")

    tasks = task_index(tasks_dir)
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    seen: set[str] = set()
    for item in items:
        task_id = item.get("evidence_task_id")
        if task_id in seen:
            errors.append(f"duplicate evidence_task_id in evidence-reviewed: {task_id}")
            continue
        seen.add(task_id)
        task = tasks.get(task_id)
        if task is None:
            errors.append(f"missing Evidence Task for reviewed run: {task_id}")
            continue
        records.append(build_record(item, task, start, cutoff))

    records.sort(key=lambda record: (record["artifact"]["artifact_type"], record["artifact"]["canonical_name"].lower(), record["comparison_id"]))
    output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_dir / "candidate-comparison-input.jsonl", records)
    (output_dir / "candidate-comparison.md").write_text(
        markdown(records, issue_id, start_text, cutoff_text) + "\n", encoding="utf-8"
    )

    recommendation_counts = Counter(record["evidence"]["recommendation"] for record in records)
    temporal_counts = Counter(position for record in records for position in record["temporal"]["position_hints"])
    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "passed": not errors,
        "record_count": len(records),
        "recommendation_counts": dict(sorted(recommendation_counts.items())),
        "temporal_hint_counts": {key: temporal_counts.get(key, 0) for key in POSITION_ORDER},
        "errors": errors,
        "outputs": {
            "comparison_jsonl": "candidate-comparison-input.jsonl",
            "comparison_markdown": "candidate-comparison.md",
        },
        "note": "Deterministic comparison substrate only. Candidate Selection remains an explicit gate.",
    }
    write_json(output_dir / "candidate-comparison-manifest.json", manifest)
    return manifest, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-reviewed", required=True)
    parser.add_argument("--tasks-dir", required=True)
    parser.add_argument("--pipeline-state", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = build(
        Path(args.evidence_reviewed),
        Path(args.tasks_dir),
        Path(args.pipeline_state),
        Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
