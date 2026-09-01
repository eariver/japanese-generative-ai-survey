#!/usr/bin/env python3
"""Convert a screening verification queue into deterministic Evidence tasks.

This layer does not verify claims and does not create editorial candidates. It
only turns triage output into primary-source inspection work. LLM duplicate_group
values are treated as unconfirmed grouping hints, never as verified identity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROMOTED = {"KEEP", "MAYBE", "INSPECT"}


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


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_slug(value: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:10]
    if not base:
        return digest
    base = base[:40].strip("-")
    return f"{base}-{digest}" if base else digest


def unique_strings(values: list[Any]) -> list[str]:
    return sorted({str(value).strip() for value in values if isinstance(value, str) and value.strip()})


def validate_queue_item(item: dict[str, Any], index: int) -> None:
    if not isinstance(item.get("record"), dict) or not isinstance(item.get("screening"), dict):
        raise ValueError(f"queue item {index} must contain record and screening objects")
    record = item["record"]
    screening = item["screening"]
    if item.get("screening_id") != record.get("screening_id") or item.get("screening_id") != screening.get("screening_id"):
        raise ValueError(f"queue item {index} screening_id mismatch")
    if screening.get("decision") not in PROMOTED:
        raise ValueError(f"queue item {index} contains non-promoted decision {screening.get('decision')!r}")


def grouping_key(item: dict[str, Any]) -> tuple[str, str]:
    screening = item["screening"]
    duplicate_group = screening.get("duplicate_group")
    if isinstance(duplicate_group, str) and duplicate_group.strip():
        return ("duplicate", duplicate_group.strip())
    return ("single", item["screening_id"])


def build_task(issue_id: str, group_kind: str, group_value: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    decisions = unique_strings([item["screening"].get("decision") for item in items])
    source_types = unique_strings([item["record"].get("source_type") for item in items])
    screening_ids = unique_strings([item["screening_id"] for item in items])
    locators = unique_strings([item["record"].get("locator") for item in items])
    lanes: list[str] = []
    why_now: list[str] = []
    verification_targets: list[str] = []
    for item in items:
        screening = item["screening"]
        lanes.extend(screening.get("topic_lanes") or [])
        if screening.get("why_now"):
            why_now.append(screening["why_now"])
        verification_targets.extend(screening.get("verification_targets") or [])

    duplicate_group = group_value if group_kind == "duplicate" else None
    if group_kind == "duplicate":
        grouping_basis = "llm-duplicate-group"
        requires_confirmation = True
        if len(items) >= 2:
            task_type = "VERIFY_SERIES"
            task_key = f"series:{group_value}"
        else:
            task_type = "VERIFY_ITEM"
            task_key = f"duplicate-hint:{group_value}:{items[0]['screening_id']}"
    else:
        only = items[0]
        if only["screening"].get("decision") == "INSPECT" or only["record"].get("source_type") == "official-index-snapshot":
            task_type = "INSPECT_INDEX"
        else:
            task_type = "VERIFY_ITEM"
        grouping_basis = "single-screening-item"
        requires_confirmation = False
        task_key = f"item:{only['screening_id']}"

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "evidence_task_id": f"evidence:{issue_id}:{stable_slug(task_key)}",
        "task_type": task_type,
        "grouping": {
            "basis": grouping_basis,
            "duplicate_group": duplicate_group,
            "requires_confirmation": requires_confirmation,
        },
        "screening_ids": screening_ids,
        "screening_decisions": decisions,
        "source_types": source_types,
        "locators": locators,
        "topic_lanes": unique_strings(lanes),
        "why_now": unique_strings(why_now),
        "verification_targets": unique_strings(verification_targets),
        "status": "PENDING_VERIFICATION",
    }


def task_filename(task: dict[str, Any]) -> str:
    return task["evidence_task_id"].rsplit(":", 1)[-1] + ".json"


def build(queue_path: Path, output_dir: Path) -> tuple[dict[str, Any], bool]:
    queue = read_jsonl(queue_path)
    if not queue:
        raise ValueError("verification queue is empty")
    for index, item in enumerate(queue):
        validate_queue_item(item, index)

    issue_ids = {item["record"].get("issue_id") for item in queue}
    if len(issue_ids) != 1 or None in issue_ids:
        raise ValueError(f"verification queue must contain exactly one issue_id: {issue_ids}")
    issue_id = next(iter(issue_ids))

    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in queue:
        groups[grouping_key(item)].append(item)

    tasks = [build_task(issue_id, kind, value, items) for (kind, value), items in groups.items()]
    tasks.sort(key=lambda task: task["evidence_task_id"])

    seen_ids: set[str] = set()
    covered: list[str] = []
    errors: list[str] = []
    for task in tasks:
        task_id = task["evidence_task_id"]
        if task_id in seen_ids:
            errors.append(f"duplicate evidence_task_id: {task_id}")
        seen_ids.add(task_id)
        covered.extend(task["screening_ids"])

    expected_ids = sorted(item["screening_id"] for item in queue)
    covered_counts = Counter(covered)
    missing = sorted(set(expected_ids) - set(covered))
    duplicate_coverage = sorted(key for key, count in covered_counts.items() if count > 1)
    unexpected = sorted(set(covered) - set(expected_ids))
    if missing:
        errors.append(f"missing screening coverage: {missing}")
    if duplicate_coverage:
        errors.append(f"screening IDs covered by multiple evidence tasks: {duplicate_coverage}")
    if unexpected:
        errors.append(f"unexpected screening coverage: {unexpected}")

    write_jsonl(output_dir / "evidence-tasks.jsonl", tasks)
    task_files: list[dict[str, Any]] = []
    for task in tasks:
        relative = Path("tasks") / task_filename(task)
        path = output_dir / relative
        write_json(path, task)
        task_files.append(
            {
                "evidence_task_id": task["evidence_task_id"],
                "path": relative.as_posix(),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )

    type_counts = Counter(task["task_type"] for task in tasks)
    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "passed": not errors,
        "input_queue_count": len(queue),
        "evidence_task_count": len(tasks),
        "task_type_counts": {
            "VERIFY_ITEM": type_counts.get("VERIFY_ITEM", 0),
            "VERIFY_SERIES": type_counts.get("VERIFY_SERIES", 0),
            "INSPECT_INDEX": type_counts.get("INSPECT_INDEX", 0),
        },
        "screening_coverage_count": len(covered_counts),
        "missing_screening_ids": missing,
        "duplicate_screening_coverage": duplicate_coverage,
        "errors": errors,
        "note": "LLM screening duplicate_group remains unconfirmed until Evidence review. Singleton duplicate hints stay VERIFY_ITEM until another retained member is present. Evidence Runner consumes one file under tasks/ so its exact input SHA-256 is stable.",
        "outputs": {
            "task_index": "evidence-tasks.jsonl",
            "task_directory": "tasks/",
        },
        "task_files": task_files,
    }
    write_json(output_dir / "evidence-task-manifest.json", manifest)
    return manifest, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verification-queue", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = build(Path(args.verification_queue), Path(args.output_dir))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
