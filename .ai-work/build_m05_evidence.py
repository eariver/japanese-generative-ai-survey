#!/usr/bin/env python3
from __future__ import annotations

import argparse
import email.utils
import hashlib
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iso_time(value: str | None) -> str | None:
    if not value:
        return None
    text = str(value).strip()
    if len(text) >= 10 and text[4] == "-" and "T" in text:
        return text
    try:
        dt = email.utils.parsedate_to_datetime(text)
    except (TypeError, ValueError):
        return text
    if dt.tzinfo is None:
        return text
    return dt.isoformat().replace("+00:00", "Z")


def date_part(value: str | None) -> str | None:
    value = iso_time(value)
    return value[:10] if value and len(value) >= 10 else None


def load_overrides(directory: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    manifest = load_json(directory / "manifest.json")
    rows: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("part-*.json")):
        data = load_json(path)
        if data.get("issue_id") != manifest.get("issue_id"):
            raise ValueError(f"override issue mismatch: {path}")
        for row in data.get("overrides") or []:
            task_id = str(row.get("evidence_task_id") or "")
            if not task_id or task_id in rows:
                raise ValueError(f"invalid/duplicate override task id: {task_id}")
            rows[task_id] = row
    return manifest, rows


def load_queue(path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        sid = str(row.get("screening_id") or "")
        if not sid or sid in rows:
            raise ValueError(f"invalid/duplicate verification queue id: {sid}")
        rows[sid] = row
    return rows


def source_class(source_type: str) -> str:
    return {
        "paper": "PRIMARY_PAPER",
        "github-release": "PRIMARY_REPOSITORY",
        "official-feed-item": "PRIMARY_OFFICIAL",
        "official-index-snapshot": "PRIMARY_OFFICIAL",
    }[source_type]


def evidence_class(source_type: str) -> str:
    return {
        "paper": "AUTHOR_CLAIM",
        "github-release": "PROJECT_CLAIM",
        "official-feed-item": "VENDOR_CLAIM",
        "official-index-snapshot": "VENDOR_CLAIM",
    }[source_type]


def artifact_type(source_type: str, title: str) -> str:
    if source_type == "paper":
        return "PAPER"
    if source_type == "github-release":
        return "FRAMEWORK"
    low = title.casefold()
    if "system card" in low or "evaluation" in low or "cyber" in low:
        return "SAFETY_EVENT"
    if "gpt-5.5 instant" in low:
        return "MODEL_UPDATE"
    if "voice" in low and "api" in low:
        return "API"
    if "codex" in low:
        return "AGENT"
    if "mrc" in low:
        return "FRAMEWORK"
    return "OTHER"


def event_type(source_type: str) -> str:
    return {
        "paper": "PAPER_RELEASE",
        "github-release": "FRAMEWORK_RELEASE",
        "official-feed-item": "OFFICIAL_PUBLICATION",
        "official-index-snapshot": "OFFICIAL_INDEX_EVENT",
    }[source_type]


def organization(record: dict[str, Any], source_type: str, override: dict[str, Any]) -> str | None:
    if override.get("organization"):
        return str(override["organization"])
    if source_type == "official-feed-item":
        return "OpenAI"
    if source_type == "github-release":
        repo = (record.get("metadata") or {}).get("repository")
        return str(repo) if repo else None
    return None


def build_card(task: dict[str, Any], queue: dict[str, dict[str, Any]], override: dict[str, Any], generated_at: str) -> dict[str, Any]:
    screening_ids = task.get("screening_ids") or []
    qrows = [queue[sid] for sid in screening_ids]
    records = [row["record"] for row in qrows]
    source_type = str(task["source_types"][0])
    recommendation = str(override["candidate_recommendation"])
    rejected = recommendation == "REJECT"
    chronology_caution = bool(override.get("chronology_caution"))

    sources: list[dict[str, Any]] = []
    for index, record in enumerate(records, start=1):
        published = iso_time(record.get("published_at"))
        sources.append({
            "source_id": f"src-{index}",
            "url": str(record.get("locator") or ""),
            "source_class": source_class(source_type),
            "title": str(record.get("title") or record.get("screening_id") or "Primary source"),
            "published_at": published,
            "accessed_at": str(record.get("observed_at") or generated_at),
            "role": "Primary source used for chronology and technical verification; reported capability/performance remains attributed to the source owner/authors.",
        })
    source_ids = [source["source_id"] for source in sources]

    events: list[dict[str, Any]] = []
    if source_type == "official-index-snapshot":
        for index, item in enumerate(override.get("index_events") or [], start=1):
            events.append({
                "event_id": f"event-{index}",
                "event_type": str(item["event_type"]),
                "event_date": str(item["event_date"]),
                "source_published_at": None,
                "source_ids": ["src-1"],
            })
    else:
        for index, (record, source) in enumerate(zip(records, sources), start=1):
            published = iso_time(record.get("published_at"))
            events.append({
                "event_id": f"event-{index}",
                "event_type": event_type(source_type),
                "event_date": date_part(published),
                "source_published_at": published,
                "source_ids": [source["source_id"]],
            })

    claims: list[dict[str, Any]] = []
    if not rejected:
        for index, (record, source) in enumerate(zip(records, sources), start=1):
            date = date_part(record.get("published_at"))
            date_phrase = f" on {date}" if date else ""
            claims.append({
                "claim_id": f"claim-source-{index}",
                "text": f"The preserved primary source identifies “{record.get('title')}”{date_phrase}.",
                "evidence_class": "PRIMARY_FACT",
                "source_ids": [source["source_id"]],
                "context": "Source identity and chronology only.",
            })
    claims.append({
        "claim_id": "claim-reviewed-1",
        "text": str(override["claim"]),
        "evidence_class": "INFERENCE" if rejected else evidence_class(source_type),
        "source_ids": source_ids,
        "context": "Interactive primary-source normalization; author/vendor/project results are not upgraded to independent fact.",
    })

    metrics: list[dict[str, Any]] = []
    for index, metric in enumerate(override.get("metrics") or [], start=1):
        metrics.append({
            "metric_id": f"metric-{index}",
            "name": str(metric["name"]),
            "value": str(metric["value"]),
            "unit": metric.get("unit"),
            "context": str(metric["context"]),
            "evidence_class": evidence_class(source_type),
            "source_ids": source_ids,
        })

    limitation_text = {
        "paper": "The preserved original arXiv metadata/abstract is primary-paper evidence, but experimental results and generalization are author-reported and were not independently reproduced in this Evidence review.",
        "github-release": "Official repository release notes verify release chronology and listed implementation changes; project performance claims and cross-hardware generalization were not independently reproduced.",
        "official-feed-item": "The preserved first-party feed item is authoritative for publication chronology and vendor-described scope; detailed capability, benchmark, or safety claims were not independently reproduced.",
        "official-index-snapshot": "The preserved first-party index is authoritative for the listed chronology, but capability/benchmark descriptions remain vendor claims and month-only dates retain month precision.",
    }[source_type]
    limitations = [{
        "limitation_id": "limitation-1",
        "text": limitation_text,
        "evidence_class": "INFERENCE",
        "source_ids": source_ids,
    }]
    if chronology_caution:
        limitations.append({
            "limitation_id": "limitation-2",
            "text": "The collected arXiv publication timestamp falls in May while the arXiv identifier encodes a later month; this chronology is preserved as observed but remains unresolved for Candidate Selection.",
            "evidence_class": "INFERENCE",
            "source_ids": source_ids,
        })

    has_substantive_summary = any(bool((record.get("summary_text") or "").strip()) for record in records)
    unresolved_feed = source_type == "official-feed-item" and not has_substantive_summary
    targets: list[dict[str, Any]] = []
    for target in task.get("verification_targets") or []:
        verified = not rejected and not unresolved_feed
        if verified:
            finding = "The preserved primary source and interactive review establish the requested mechanism/evaluation scope; quantitative conclusions remain attributed to the original author/vendor/project."
            target_sources = source_ids
            status = "VERIFIED"
        else:
            finding = "The preserved primary source establishes the artifact/index identity, but the requested substantive target could not be fixed at item level from the collected source material."
            target_sources = []
            status = "UNRESOLVED"
        targets.append({"target": str(target), "status": status, "finding": finding, "source_ids": target_sources})

    unresolved_questions: list[str] = []
    if rejected:
        unresolved_questions.append("No concrete May technical item was resolved from the preserved first-party index snapshot.")
    if unresolved_feed:
        unresolved_questions.append("The preserved official feed item has no substantive summary body for the requested evaluation details.")
    if chronology_caution:
        unresolved_questions.append("Reconcile the collected May timestamp with the later-month arXiv identifier before treating chronology as exact.")

    first_record = records[0]
    name = str(override.get("artifact_name") or first_record.get("title") or task["evidence_task_id"])
    if task.get("task_type") == "VERIFY_SERIES" and not override.get("artifact_name"):
        repo = (first_record.get("metadata") or {}).get("repository")
        name = f"{repo or name} May 2026 release series"
    org = organization(first_record, source_type, override)

    card_status = "REJECTED" if rejected else ("PARTIAL" if recommendation == "HOLD" or unresolved_feed or chronology_caution else "VERIFIED")
    grouping_accepted = not rejected
    rationale = {
        "CANDIDATE": "Primary-source Evidence is sufficiently resolved to enter Candidate Selection comparison.",
        "HOLD": "Primary-source Evidence is credible but retained below Candidate-ready priority because of scope, setup, chronology, or supporting-role constraints.",
        "REJECT": "The Screening hypothesis did not resolve to a concrete May technical event in the preserved primary source.",
    }[recommendation]

    return {
        "schema_version": "1.0",
        "issue_id": task["issue_id"],
        "evidence_task_id": task["evidence_task_id"],
        "status": card_status,
        "grouping_resolution": {
            "accepted": grouping_accepted,
            "split_recommended": False,
            "note": "Reviewed grouping retained for Evidence normalization." if grouping_accepted else "Index grouping rejected because no concrete May item resolved.",
        },
        "artifact": {
            "canonical_name": name,
            "artifact_type": artifact_type(source_type, name),
            "organization": org,
            "canonical_url": str(first_record.get("locator") or "") or None,
        },
        "temporal": {
            "artifact_first_announced": events[0]["event_date"] if events else None,
            "events": events,
            "observed_at": generated_at,
        },
        "sources": sources,
        "claims": claims,
        "metrics": metrics,
        "limitations": limitations,
        "verification": {
            "targets": targets,
            "unresolved_questions": unresolved_questions,
            "contradictions": [],
        },
        "editorial": {
            "why_now_confirmed": bool(events) and not chronology_caution and not rejected,
            "why_now_note": "May-window primary-source chronology confirmed." if bool(events) and not chronology_caution and not rejected else "Chronology or May item resolution remains intentionally bounded.",
            "candidate_recommendation": recommendation,
            "rationale": rationale,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--package-root", required=True)
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--overrides-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    package_root = Path(args.package_root).resolve()
    repo_root = Path(args.repo_root).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    package = load_json(package_root / "evidence-execution-package.json")
    manifest, overrides = load_overrides(Path(args.overrides_dir).resolve())
    if manifest.get("issue_id") != package.get("issue_id"):
        raise ValueError("override/package issue mismatch")
    queue_path = repo_root / package["screening_basis"]["verification_queue_path"]
    queue = load_queue(queue_path)
    runner = manifest["runner"]
    prompt_sha = package["prompt"]["sha256"]
    task_entries = package["evidence_tasks"]["tasks"]
    expected_ids = {entry["evidence_task_id"] for entry in task_entries}
    if set(overrides) != expected_ids:
        raise ValueError(f"override/task mismatch: missing={sorted(expected_ids-set(overrides))}, extra={sorted(set(overrides)-expected_ids)}")

    counts = {"CANDIDATE": 0, "HOLD": 0, "REJECT": 0}
    for entry in task_entries:
        task_path = package_root / entry["path"]
        task = load_json(task_path)
        override = overrides[task["evidence_task_id"]]
        card = build_card(task, queue, override, runner["generated_at"])
        counts[card["editorial"]["candidate_recommendation"]] += 1
        run = {
            "schema_version": "1.0",
            "issue_id": task["issue_id"],
            "evidence_task_id": task["evidence_task_id"],
            "evidence_task_sha256": sha(task_path),
            "prompt_id": "primary-source-verification-v0.1",
            "prompt_sha256": prompt_sha,
            "runner": runner,
            "card": card,
        }
        (output_dir / task_path.name).write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if counts != {"CANDIDATE": 37, "HOLD": 18, "REJECT": 3}:
        raise ValueError(f"review count drift: {counts}")
    print(json.dumps({"issue_id": package["issue_id"], "task_count": len(task_entries), "recommendations": counts}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
