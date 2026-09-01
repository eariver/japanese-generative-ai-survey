#!/usr/bin/env python3
"""Materialize deterministic pre-selection Candidate Records from Evidence output.

One validated Evidence Run recommendation=CANDIDATE becomes one Markdown record.
This script does not merge separate Evidence Runs and does not select articles.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected a JSON object")
            values.append(value)
    return values


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized[:56].rstrip("-") or "candidate"


def candidate_id(item: dict[str, Any]) -> str:
    card = item["card"]
    base = slug(card["artifact"]["canonical_name"])
    suffix = hashlib.sha256(item["evidence_task_id"].encode("utf-8")).hexdigest()[:8]
    return f"{base}-{suffix}"


def yaml_string(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def bullet(text: str) -> str:
    return " ".join(text.split())


def render(item: dict[str, Any], cid: str) -> str:
    card = item["card"]
    artifact = card["artifact"]
    temporal = card["temporal"]
    editorial = card["editorial"]
    source_by_id = {source["source_id"]: source for source in card["sources"]}
    event_dates = sorted({event.get("event_date") for event in temporal.get("events", []) if event.get("event_date")})

    lines = [
        "---",
        f"candidate_id: {cid}",
        f"issue_id: {yaml_string(item['issue_id'])}",
        f"title: {yaml_string(artifact['canonical_name'])}",
        "record_type: pre-selection-candidate",
        "status: candidate-ready-from-evidence",
        f"artifact_type: {artifact['artifact_type']}",
        f"evidence_task_id: {yaml_string(item['evidence_task_id'])}",
        f"evidence_status: {card['status']}",
        f"why_now_confirmed: {'true' if editorial['why_now_confirmed'] else 'false'}",
        f"event_dates: {yaml_string(event_dates)}",
        "---",
        "",
        f"# {artifact['canonical_name']} — Pre-selection Candidate Record",
        "",
        "> Generated deterministically from a validated Evidence Run. Candidate-ready does not mean selected.",
        "",
        "## Evidence summary",
        f"- Evidence status: `{card['status']}`",
        f"- Artifact type: `{artifact['artifact_type']}`",
        f"- Organization: {artifact.get('organization') or 'UNKNOWN'}",
        f"- Canonical URL: {artifact.get('canonical_url') or 'UNKNOWN'}",
        f"- First announced: {temporal.get('artifact_first_announced') or 'UNKNOWN'}",
        f"- Why-now confirmed: `{'yes' if editorial['why_now_confirmed'] else 'no'}`",
        f"- Why-now note: {editorial.get('why_now_note') or 'None'}",
        f"- Evidence recommendation: `{editorial['candidate_recommendation']}`",
        f"- Recommendation rationale: {bullet(editorial['rationale'])}",
        "",
        "## Verified event chronology",
    ]
    if temporal.get("events"):
        for event in temporal["events"]:
            source_labels = ", ".join(event["source_ids"])
            lines.append(
                f"- `{event['event_type']}` — event_date={event.get('event_date') or 'UNKNOWN'}, "
                f"source_published_at={event.get('source_published_at') or 'UNKNOWN'}; sources: {source_labels}"
            )
    else:
        lines.append("- No concrete event was established.")

    lines.extend(["", "## Claims"])
    if card.get("claims"):
        for claim in card["claims"]:
            lines.append(
                f"- **{claim['evidence_class']}** — {bullet(claim['text'])} "
                f"(sources: {', '.join(claim['source_ids'])})"
            )
            if claim.get("context"):
                lines.append(f"  - Context: {bullet(claim['context'])}")
    else:
        lines.append("- None recorded.")

    lines.extend(["", "## Metrics / concrete comparisons"])
    if card.get("metrics"):
        for metric in card["metrics"]:
            unit = f" {metric['unit']}" if metric.get("unit") else ""
            lines.append(
                f"- **{metric['evidence_class']}** — {metric['name']}: `{metric['value']}{unit}` "
                f"— {bullet(metric['context'])} (sources: {', '.join(metric['source_ids'])})"
            )
    else:
        lines.append("- None recorded.")

    lines.extend(["", "## Limitations / boundaries"])
    if card.get("limitations"):
        for limitation in card["limitations"]:
            lines.append(
                f"- **{limitation['evidence_class']}** — {bullet(limitation['text'])} "
                f"(sources: {', '.join(limitation['source_ids'])})"
            )
    else:
        lines.append("- None recorded.")

    lines.extend(["", "## Verification targets"])
    for target in card["verification"]["targets"]:
        source_text = ", ".join(target.get("source_ids") or []) or "none"
        lines.append(
            f"- `{target['status']}` — {bullet(target['target'])}: {bullet(target['finding'])} "
            f"(sources: {source_text})"
        )

    lines.extend(["", "## Unresolved questions"])
    unresolved = card["verification"].get("unresolved_questions") or []
    if unresolved:
        lines.extend(f"- {bullet(value)}" for value in unresolved)
    else:
        lines.append("- None recorded.")

    lines.extend(["", "## Contradictions"])
    contradictions = card["verification"].get("contradictions") or []
    if contradictions:
        lines.extend(f"- {bullet(value)}" for value in contradictions)
    else:
        lines.append("- None recorded.")

    lines.extend(["", "## Sources"])
    for source_id in sorted(source_by_id):
        source = source_by_id[source_id]
        lines.append(
            f"- `{source_id}` [{source['source_class']}] — {source['title']} — {source['url']} "
            f"(published: {source.get('published_at') or 'UNKNOWN'}; role: {source['role']})"
        )

    lines.extend(
        [
            "",
            "## Selection note",
            "This record is eligible for comparison in Candidate Selection. It is not an article assignment, ranking, or table-of-contents decision.",
            "",
        ]
    )
    return "\n".join(lines)


def materialize(candidate_ready: Path, output_dir: Path) -> tuple[dict[str, Any], bool]:
    items = read_jsonl(candidate_ready)
    output_dir.mkdir(parents=True, exist_ok=True)
    ids: set[str] = set()
    records: list[dict[str, Any]] = []
    errors: list[str] = []

    for index, item in enumerate(items):
        if item.get("card", {}).get("editorial", {}).get("candidate_recommendation") != "CANDIDATE":
            errors.append(f"input item {index} is not recommendation=CANDIDATE")
            continue
        card = item["card"]
        if card.get("status") in {"REJECTED", "NEEDS_MORE"}:
            errors.append(f"input item {index} has incompatible evidence status {card.get('status')}")
            continue
        if card.get("grouping_resolution", {}).get("split_recommended") is True:
            errors.append(f"input item {index} requests grouping split before candidate materialization")
            continue

        cid = candidate_id(item)
        if cid in ids:
            errors.append(f"candidate_id collision: {cid}")
            continue
        ids.add(cid)
        filename = f"{cid}.md"
        path = output_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        content = render(item, cid)
        path.write_text(content, encoding="utf-8")
        records.append(
            {
                "candidate_id": cid,
                "file": filename,
                "title": card["artifact"]["canonical_name"],
                "artifact_type": card["artifact"]["artifact_type"],
                "status": "candidate-ready-from-evidence",
                "evidence_task_id": item["evidence_task_id"],
                "evidence_status": card["status"],
                "why_now_confirmed": card["editorial"]["why_now_confirmed"],
            }
        )

    records.sort(key=lambda record: record["candidate_id"])
    issue_ids = {item.get("issue_id") for item in items}
    issue_id = next(iter(issue_ids)) if len(issue_ids) == 1 else None
    if len(issue_ids) > 1:
        errors.append(f"candidate-ready input contains multiple issue IDs: {sorted(str(v) for v in issue_ids)}")

    index = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "pre-selection-candidate-inventory",
        "record_count": len(records),
        "passed": not errors,
        "rules": [
            "One validated Evidence Run recommendation=CANDIDATE maps to one pre-selection Candidate Record.",
            "Candidate-ready does not mean selected.",
            "Separate Evidence Runs are not automatically merged by canonical name or URL.",
            "Article construction begins only after Candidate Selection and Issue Architecture.",
        ],
        "records": records,
        "errors": errors,
    }
    (output_dir / "candidate-index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return index, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-ready", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    index, passed = materialize(Path(args.candidate_ready), Path(args.output_dir))
    print(json.dumps(index, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
