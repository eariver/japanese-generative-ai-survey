#!/usr/bin/env python3
"""Build a deterministic, non-ranking Candidate comparison matrix from Evidence Runs.

The matrix exposes comparison readiness, temporal position, evidence classes and
remaining boundaries. It never assigns importance scores or selects candidates.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, time, timezone
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            values.append(value)
    return values


def parse_temporal(value: str | None, *, end_of_day: bool = False) -> datetime | None:
    if not value:
        return None
    text = value.strip()
    if len(text) == 10:
        day = datetime.fromisoformat(text).date()
        return datetime.combine(day, time.max if end_of_day else time.min, tzinfo=timezone.utc)
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def timing_relation(card: dict[str, Any], window_start: datetime | None, cutoff: datetime) -> tuple[str, list[str]]:
    raw_dates = sorted({event.get("event_date") for event in card["temporal"].get("events", []) if event.get("event_date")})
    parsed = [(raw, parse_temporal(raw, end_of_day=True)) for raw in raw_dates]
    parsed = [(raw, value) for raw, value in parsed if value is not None]
    if not parsed:
        return "TIMING_UNRESOLVED", raw_dates

    instants = [value for _, value in parsed]
    has_post = any(value > cutoff for value in instants)
    has_main = window_start is not None and any(window_start <= value <= cutoff for value in instants)
    has_pre = window_start is not None and any(value < window_start for value in instants)

    if has_post and (has_main or has_pre):
        return "MIXED_WINDOW", raw_dates
    if has_post:
        return "POST_CUTOFF", raw_dates
    if has_main:
        return "MAIN_EVENT", raw_dates
    if window_start is None:
        return "TIMING_UNRESOLVED", raw_dates
    if all(value < window_start for value in instants):
        return ("PRE_WINDOW_RELEVANCE" if card["editorial"]["why_now_confirmed"] else "PRE_WINDOW"), raw_dates
    return "TIMING_UNRESOLVED", raw_dates


def readiness(card: dict[str, Any]) -> str:
    recommendation = card["editorial"]["candidate_recommendation"]
    if recommendation == "REJECT":
        return "REJECT"
    if recommendation in {"HOLD", "INSPECT_MORE"}:
        return "HOLD"
    if recommendation != "CANDIDATE":
        return "HOLD"
    if card["status"] not in {"VERIFIED", "PARTIAL"}:
        return "HOLD"
    unresolved = card["verification"].get("unresolved_questions") or []
    contradictions = card["verification"].get("contradictions") or []
    limitations = card.get("limitations") or []
    if card["status"] == "VERIFIED" and not unresolved and not contradictions and not limitations:
        return "READY"
    return "READY_WITH_CAVEAT"


def evidence_class_counts(card: dict[str, Any]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for field in ("claims", "metrics", "limitations"):
        for item in card.get(field) or []:
            value = item.get("evidence_class")
            if value:
                counts[value] += 1
    order = ["PRIMARY_FACT", "VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM", "SOCIAL_OBSERVATION", "INFERENCE"]
    return {key: counts.get(key, 0) for key in order}


def source_class_counts(card: dict[str, Any]) -> dict[str, int]:
    counts = Counter(source.get("source_class") for source in card.get("sources") or [])
    order = ["PRIMARY_OFFICIAL", "PRIMARY_PAPER", "PRIMARY_REPOSITORY", "SOCIAL", "SECONDARY"]
    return {key: counts.get(key, 0) for key in order}


def boundary_summary(card: dict[str, Any]) -> list[str]:
    values: list[str] = []
    values.extend(card["verification"].get("unresolved_questions") or [])
    values.extend(card["verification"].get("contradictions") or [])
    if card["grouping_resolution"].get("split_recommended"):
        values.append("Evidence grouping requires split before selection.")
    if not card["editorial"].get("why_now_confirmed"):
        values.append("Weekly why-now relevance is not confirmed.")
    for limitation in card.get("limitations") or []:
        values.append(limitation["text"])
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        normalized = " ".join(value.split())
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return result


def build(evidence_reviewed: Path, pipeline_state: Path) -> dict[str, Any]:
    reviewed = read_jsonl(evidence_reviewed)
    state = read_json(pipeline_state)
    issue_id = state["issue_id"]
    start = parse_temporal(state.get("calendar", {}).get("collection_window_start"))
    cutoff = parse_temporal(state.get("calendar", {}).get("editorial_cutoff"), end_of_day=False)
    if cutoff is None:
        raise ValueError("pipeline state editorial_cutoff is required")

    rows: list[dict[str, Any]] = []
    for item in reviewed:
        if item.get("issue_id") != issue_id:
            raise ValueError(f"Evidence item issue mismatch: {item.get('issue_id')} != {issue_id}")
        card = item["card"]
        relation, event_dates = timing_relation(card, start, cutoff)
        rows.append(
            {
                "evidence_task_id": item["evidence_task_id"],
                "title": card["artifact"]["canonical_name"],
                "artifact_type": card["artifact"]["artifact_type"],
                "organization": card["artifact"].get("organization"),
                "timing_relation": relation,
                "event_dates": event_dates,
                "evidence_status": card["status"],
                "recommendation": card["editorial"]["candidate_recommendation"],
                "why_now_confirmed": card["editorial"]["why_now_confirmed"],
                "comparison_readiness": readiness(card),
                "source_class_counts": source_class_counts(card),
                "evidence_class_counts": evidence_class_counts(card),
                "metric_count": len(card.get("metrics") or []),
                "unresolved_question_count": len(card["verification"].get("unresolved_questions") or []),
                "contradiction_count": len(card["verification"].get("contradictions") or []),
                "remaining_boundaries": boundary_summary(card),
            }
        )
    rows.sort(key=lambda row: (row["title"].lower(), row["evidence_task_id"]))

    recommendation_counts = Counter(row["recommendation"] for row in rows)
    readiness_counts = Counter(row["comparison_readiness"] for row in rows)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "pre-selection-comparison",
        "ranking": None,
        "row_count": len(rows),
        "collection_window_start": state.get("calendar", {}).get("collection_window_start"),
        "editorial_cutoff": state.get("calendar", {}).get("editorial_cutoff"),
        "recommendation_counts": dict(sorted(recommendation_counts.items())),
        "readiness_counts": dict(sorted(readiness_counts.items())),
        "rows": rows,
        "rules": [
            "This matrix does not rank candidates or imply inclusion.",
            "Evidence Runner recommendation is distinct from final Candidate Selection.",
            "Source volume is displayed as evidence depth, not importance.",
            "Remaining boundaries must travel with any candidate promoted by Selection.",
        ],
    }


def compact_counts(counts: dict[str, int]) -> str:
    return ", ".join(f"{key}={value}" for key, value in counts.items() if value) or "none"


def render_markdown(matrix: dict[str, Any]) -> str:
    lines = [
        f"# {matrix['issue_id']} Pre-selection Candidate Comparison Matrix",
        "",
        "Status: **pre-selection comparison**",
        "",
        "This matrix is deterministic and non-ranking. It does not imply article inclusion.",
        "",
        f"- Collection window start: `{matrix['collection_window_start'] or 'UNSET'}`",
        f"- Editorial cutoff: `{matrix['editorial_cutoff']}`",
        f"- Rows: {matrix['row_count']}",
        "",
        "| Candidate | Type | Timing | Evidence | Recommendation | Readiness | Evidence classes | Remaining boundary |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in matrix["rows"]:
        boundaries = "<br>".join(row["remaining_boundaries"]) or "None recorded"
        title = row["title"].replace("|", "\\|")
        classes = compact_counts(row["evidence_class_counts"])
        lines.append(
            f"| {title} | `{row['artifact_type']}` | `{row['timing_relation']}` | `{row['evidence_status']}` | "
            f"`{row['recommendation']}` | `{row['comparison_readiness']}` | {classes} | {boundaries} |"
        )
    lines.extend(
        [
            "",
            "## Rules",
            "",
            *[f"- {rule}" for rule in matrix["rules"]],
            "",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-reviewed", required=True)
    parser.add_argument("--pipeline-state", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--markdown-output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    matrix = build(Path(args.evidence_reviewed), Path(args.pipeline_state))
    json_path = Path(args.json_output)
    md_path = Path(args.markdown_output)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(matrix), encoding="utf-8")
    print(json.dumps({"issue_id": matrix["issue_id"], "row_count": matrix["row_count"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
