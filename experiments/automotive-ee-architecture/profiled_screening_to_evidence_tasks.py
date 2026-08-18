#!/usr/bin/env python3
"""Materialize Automotive Screening decisions and reuse the production Evidence-task builder.

This experiment deliberately keeps the production Screening acceptance path and
`scripts/build_evidence_tasks.py` unchanged. It binds a compact domain selection to
one immutable profiled Screening index, expands every omitted record to DROP, writes
an experiment verification queue, and then calls the production Evidence-task builder
as-is.

The goal is to measure the abstraction boundary, not to create a second production
pipeline.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = SCRIPT_PATH.parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_evidence_tasks as evidence_tasks

PROMOTED = {"KEEP", "MAYBE", "INSPECT"}
LANES = set("ABCDEFGHIJKL")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_no}: expected JSON object")
        values.append(value)
    return values


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for value in values:
            fh.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def default_verification_targets(record: dict[str, Any]) -> list[str]:
    title = " ".join(str(record.get("title") or record.get("screening_id") or "artifact").split())
    source_type = record.get("source_type")
    if source_type == "paper":
        return [
            f"Verify the architecture, evaluation setup, material claims and limitations reported for {title}; preserve paper results as AUTHOR_CLAIM unless independently established."
        ]
    if source_type == "github-release":
        return [
            f"Verify the release date, material technical changes and maturity significance of {title}; distinguish release existence from maintainer/project claims."
        ]
    if source_type == "official-page-snapshot":
        return [
            f"Verify the official scope/status and architecture-significant statements on {title}; distinguish directly checkable facts from organization/project claims."
        ]
    if source_type == "official-index-snapshot":
        return [f"Inspect {title} for concrete item-level primary sources before making architecture claims."]
    return [f"Verify architecture-significant claims and limitations for {title} against primary sources."]


def validate_and_index_selection(
    *, selection: dict[str, Any], records: list[dict[str, Any]], screening_index_path: Path
) -> dict[str, dict[str, Any]]:
    issue_id = selection.get("issue_id")
    if not isinstance(issue_id, str) or not issue_id:
        raise ValueError("selection.issue_id must be non-empty")
    basis = selection.get("basis")
    if not isinstance(basis, dict):
        raise ValueError("selection.basis must be an object")
    expected_sha = basis.get("profiled_screening_index_sha256")
    actual_sha = sha256_file(screening_index_path)
    if expected_sha != actual_sha:
        raise ValueError(f"profiled Screening index SHA mismatch: expected {expected_sha}, got {actual_sha}")
    if basis.get("record_count") != len(records):
        raise ValueError(f"record-count mismatch: expected {basis.get('record_count')}, got {len(records)}")

    records_by_id: dict[str, dict[str, Any]] = {}
    for record in records:
        sid = record.get("screening_id")
        if not isinstance(sid, str) or not sid:
            raise ValueError("Screening record without screening_id")
        if record.get("issue_id") != issue_id:
            raise ValueError(f"Screening record issue mismatch: {sid}")
        if sid in records_by_id:
            raise ValueError(f"duplicate Screening record: {sid}")
        records_by_id[sid] = record

    selections = selection.get("selections")
    if not isinstance(selections, list):
        raise ValueError("selection.selections must be an array")
    indexed: dict[str, dict[str, Any]] = {}
    for item in selections:
        if not isinstance(item, dict):
            raise ValueError("selection entries must be objects")
        sid = item.get("screening_id")
        if not isinstance(sid, str) or not sid or sid in indexed:
            raise ValueError(f"invalid/duplicate selected screening_id: {sid!r}")
        if sid not in records_by_id:
            raise ValueError(f"selected screening_id absent from pinned index: {sid}")
        if item.get("decision") not in PROMOTED:
            raise ValueError(f"selected decision must be KEEP/MAYBE/INSPECT: {sid}")
        lanes = item.get("topic_lanes")
        if not isinstance(lanes, list) or len(lanes) != len(set(lanes)) or any(x not in LANES for x in lanes):
            raise ValueError(f"invalid topic_lanes: {sid}")
        duplicate_group = item.get("duplicate_group")
        if duplicate_group is not None and (not isinstance(duplicate_group, str) or not duplicate_group.strip()):
            raise ValueError(f"invalid duplicate_group: {sid}")
        indexed[sid] = item
    return indexed


def materialize_decision(record: dict[str, Any], selected: dict[str, Any] | None) -> dict[str, Any]:
    sid = record["screening_id"]
    if selected is None:
        return {
            "screening_id": sid,
            "decision": "DROP",
            "reason": "Not retained by the pinned Automotive E/E thematic selection.",
            "why_now": None,
            "topic_lanes": [],
            "duplicate_group": None,
            "verification_targets": [],
            "confidence": "high",
        }
    decision = selected["decision"]
    return {
        "screening_id": sid,
        "decision": decision,
        "reason": "Retained by the pinned Automotive E/E thematic selection for primary-source verification.",
        "why_now": "Potentially material to the 2023-2026 Automotive E/E architecture transition.",
        "topic_lanes": selected.get("topic_lanes", []),
        "duplicate_group": selected.get("duplicate_group"),
        "verification_targets": default_verification_targets(record),
        "confidence": "high" if decision == "KEEP" else "medium",
    }


def build(*, screening_index_path: Path, selection_path: Path, output_dir: Path) -> dict[str, Any]:
    screening_index_path = screening_index_path.resolve()
    selection_path = selection_path.resolve()
    output_dir = output_dir.resolve()
    records = load_jsonl(screening_index_path)
    selection = load_json(selection_path)
    selected_by_id = validate_and_index_selection(
        selection=selection, records=records, screening_index_path=screening_index_path
    )

    decisions: list[dict[str, Any]] = []
    queue: list[dict[str, Any]] = []
    decision_counts: Counter[str] = Counter()
    retained_source_counts: Counter[str] = Counter()
    for record in records:
        selected = selected_by_id.get(record["screening_id"])
        decision = materialize_decision(record, selected)
        decisions.append(decision)
        decision_counts[decision["decision"]] += 1
        if decision["decision"] in PROMOTED:
            queue.append({
                "screening_id": record["screening_id"],
                "record": record,
                "screening": decision,
            })
            retained_source_counts[str(record.get("source_type"))] += 1

    if len(decisions) != len(records):
        raise RuntimeError("not every Screening record received exactly one decision")
    if len(queue) != len(selected_by_id):
        raise RuntimeError("verification queue size does not match pinned selection")

    decisions_path = output_dir / "screening-decisions.jsonl"
    queue_path = output_dir / "verification-queue.jsonl"
    write_jsonl(decisions_path, decisions)
    write_jsonl(queue_path, queue)

    evidence_output = output_dir / "evidence"
    evidence_manifest, passed = evidence_tasks.build(queue_path, evidence_output)
    if not passed:
        raise RuntimeError(f"production Evidence-task builder rejected experiment queue: {evidence_manifest}")

    manifest = {
        "schema_version": "1.0",
        "experiment": "PROFILED_SCREENING_TO_SHARED_EVIDENCE_TASKS",
        "issue_id": selection["issue_id"],
        "pinned_input": {
            "screening_index_path": screening_index_path.as_posix(),
            "screening_index_sha256": sha256_file(screening_index_path),
            "selection_path": selection_path.as_posix(),
            "selection_sha256": sha256_file(selection_path),
            "record_count": len(records),
        },
        "decision_counts": dict(sorted(decision_counts.items())),
        "retained_count": len(queue),
        "retained_source_counts": dict(sorted(retained_source_counts.items())),
        "verification_queue": {
            "path": "verification-queue.jsonl",
            "sha256": sha256_file(queue_path),
        },
        "screening_decisions": {
            "path": "screening-decisions.jsonl",
            "sha256": sha256_file(decisions_path),
        },
        "shared_evidence_task_builder": "scripts/build_evidence_tasks.py",
        "shared_evidence_task_builder_modified": False,
        "evidence_task_manifest": evidence_manifest,
        "production_ai_pipeline_modified": False,
        "finding": "Automotive-specific Screening selection can be reduced to domain decisions/lane/group context; the existing deterministic Evidence-task builder accepts the resulting queue unchanged.",
    }
    write_json(output_dir / "screening-to-evidence-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screening-index", required=True)
    parser.add_argument("--selection", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    manifest = build(
        screening_index_path=Path(args.screening_index),
        selection_path=Path(args.selection),
        output_dir=Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
