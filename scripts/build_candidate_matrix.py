#!/usr/bin/env python3
"""Build a deterministic, non-ranking Candidate comparison matrix from Evidence Runs.

The matrix exposes comparison readiness, temporal position, evidence classes and
remaining boundaries. It never assigns importance scores or selects candidates.
"""

from __future__ import annotations

import argparse
import email.utils
import json
from collections import Counter
from datetime import datetime, timezone
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


def is_date_only(value: str) -> bool:
    return len(value.strip()) == 10


def is_month_only(value: str) -> bool:
    text = value.strip()
    if len(text) != 7:
        return False
    try:
        datetime.strptime(text, "%Y-%m")
    except ValueError:
        return False
    return True


def parse_instant(value: str | None) -> datetime | None:
    if not value:
        return None
    text = value.strip()
    if is_date_only(text):
        return datetime.fromisoformat(text).replace(tzinfo=timezone.utc)
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(text)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError(f"unsupported event timestamp: {value!r}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def timing_relation(
    card: dict[str, Any],
    window_start_raw: str | None,
    cutoff_raw: str,
) -> tuple[str, list[str]]:
    raw_dates = sorted({event.get("event_date") for event in card["temporal"].get("events", []) if event.get("event_date")})
    if not raw_dates:
        return "TIMING_UNRESOLVED", raw_dates

    # Month-precision evidence cannot be placed safely relative to a day/time
    # cutoff. Preserve the source precision instead of inventing a day.
    if any(is_month_only(raw) for raw in raw_dates):
        return "TIMING_UNRESOLVED", raw_dates

    window_start = parse_instant(window_start_raw)
    cutoff = parse_instant(cutoff_raw)
    if cutoff is None:
        raise ValueError("editorial cutoff is required")

    # Date-only events on the cutoff calendar day cannot be assigned to Main or
    # Post-Cutoff because the editorial cutoff has a clock time. Preserve that
    # uncertainty instead of manufacturing 00:00/23:59 semantics.
    cutoff_calendar_date = cutoff.date()
    if any(is_date_only(raw) and datetime.fromisoformat(raw).date() == cutoff_calendar_date for raw in raw_dates):
        return "TIMING_UNRESOLVED", raw_dates

    has_post = False
    has_main = False
    has_pre = False
    start_date = window_start.date() if window_start is not None else None
    cutoff_date = cutoff.date()

    for raw in raw_dates:
        if is_date_only(raw):
            day = datetime.fromisoformat(raw).date()
            if day > cutoff_date:
                has_post = True
            elif start_date is not None and start_date <= day < cutoff_date:
                has_main = True
            elif start_date is not None and day < start_date:
                has_pre = True
            else:
                return "TIMING_UNRESOLVED", raw_dates
        else:
            instant = parse_instant(raw)
            if instant is None:
                return "TIMING_UNRESOLVED", raw_dates
            if instant > cutoff:
                has_post = True
            elif window_start is not None and instant >= window_start:
                has_main = True
            elif window_start is not None and instant < window_start:
                has_pre = True
            else:
                return "TIMING_UNRESOLVED", raw_dates

    categories = sum(bool(value) for value in (has_post, has_main, has_pre))
    if categories > 1:
        return "MIXED_WINDOW", raw_dates
    if has_post:
        return "POST_CUTOFF", raw_dates
    if has_main:
        return "MAIN_EVENT", raw_dates
    if has_pre:
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
    window_start_raw = state.get("calendar", {}).get("collection_window_start")
    cutoff_raw = state.get("calendar", {}).get("editorial_cutoff")
    if not cutoff_raw:
        raise ValueError("pipeline state editorial_cutoff is required")

    rows: list[dict[str, Any]] = []
    for item in reviewed:
        if item.get("issue_id") != issue_id:
            raise ValueError(f"Evidence item issue mismatch: {item.get('issue_id')} != {issue_id}")
        card = item["card"]
        relation, event_dates = timing_relation(card, window_start_raw, cutoff_raw)
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
        "collection_window_start": window_start_raw,
        "editorial_cutoff": cutoff_raw,
        "recommendation_counts": dict(sorted(recommendation_counts.items())),
        "readiness_counts": dict(sorted(readiness_counts.items())),
        "rows": rows,
        "rules": [
            "This matrix does not rank candidates or imply inclusion.",
            "Evidence Runner recommendation is distinct from final Candidate Selection.",
            "Source volume is displayed as evidence depth, not importance.",
            "Month-only event dates remain TIMING_UNRESOLVED rather than inventing day precision.",
            "Date-only events on the cutoff day remain TIMING_UNRESOLVED unless a source provides time-of-day evidence.",
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
    lines.extend(["", "## Rules", "", *[f"- {rule}" for rule in matrix["rules"]], ""])
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
