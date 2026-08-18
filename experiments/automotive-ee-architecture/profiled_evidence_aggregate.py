#!/usr/bin/env python3
"""Aggregate all Automotive E/E Evidence batches and exercise shared Candidate comparison.

This experiment remains read-only with respect to the production lifecycle. It treats
the pinned 45-task Evidence execution package as the authoritative task set, discovers
results only from explicit experiment manifests, revalidates every result against the
exact task/prompt plus the generated domain schemas, proves one-to-one task coverage,
then invokes the production `scripts/build_candidate_matrix.py` unchanged.
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

from jsonschema import Draft202012Validator, RefResolver
from scripts import build_candidate_matrix
from scripts import validate_evidence_run

DEFAULT_MANIFESTS = [
    "experiments/automotive-ee-architecture/evidence-vertical-slice/vertical-slice-manifest.json",
    "experiments/automotive-ee-architecture/evidence-batches/batch-01/batch-manifest.json",
    "experiments/automotive-ee-architecture/evidence-batches/batch-02/batch-manifest.json",
    "experiments/automotive-ee-architecture/evidence-batches/batch-03/batch-manifest.json",
    "experiments/automotive-ee-architecture/evidence-batches/batch-04/batch-manifest.json",
    "experiments/automotive-ee-architecture/evidence-batches/batch-05/batch-manifest.json",
]


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


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


def load_package_tasks(package_root: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    package = load_json(package_root / "evidence-execution-package.json")
    tasks_meta = package.get("evidence_tasks")
    if not isinstance(tasks_meta, dict):
        raise ValueError("Evidence package evidence_tasks metadata is missing")
    task_entries = tasks_meta.get("tasks")
    if not isinstance(task_entries, list):
        raise ValueError("Evidence package tasks must be an array")
    result: dict[str, dict[str, Any]] = {}
    for entry in task_entries:
        if not isinstance(entry, dict):
            raise ValueError("Evidence package task entries must be objects")
        task_id = entry.get("evidence_task_id")
        relative = entry.get("path")
        expected_sha = entry.get("sha256")
        if not isinstance(task_id, str) or not task_id or task_id in result:
            raise ValueError(f"invalid/duplicate package task id: {task_id!r}")
        if not isinstance(relative, str) or not relative:
            raise ValueError(f"task path missing for {task_id}")
        task_path = package_root / relative
        if not task_path.is_file():
            raise ValueError(f"package task missing: {relative}")
        actual_sha = sha256_file(task_path)
        if actual_sha != expected_sha:
            raise ValueError(f"package task SHA mismatch for {task_id}")
        task = load_json(task_path)
        if task.get("evidence_task_id") != task_id:
            raise ValueError(f"package task identity mismatch: {task_id}")
        result[task_id] = {"entry": entry, "path": task_path, "task": task}
    expected_count = tasks_meta.get("task_count")
    if expected_count != len(result):
        raise ValueError(f"package task count mismatch: expected {expected_count}, got {len(result)}")
    return package, result


def validators(package_root: Path) -> tuple[Draft202012Validator, Draft202012Validator]:
    run_path = package_root / "contract" / "evidence-run.schema.json"
    card_path = package_root / "contract" / "evidence-card.schema.json"
    run_schema = load_json(run_path)
    card_schema = load_json(card_path)
    store = {
        "evidence-run.schema.json": run_schema,
        "evidence-card.schema.json": card_schema,
        run_schema.get("$id", "evidence-run.schema.json"): run_schema,
        card_schema.get("$id", "evidence-card.schema.json"): card_schema,
    }
    resolver = RefResolver.from_schema(run_schema, store=store)
    return Draft202012Validator(run_schema, resolver=resolver), Draft202012Validator(card_schema)


def discover_cases(repo_root: Path, manifests: list[str]) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for relative_manifest in manifests:
        manifest_path = repo_root / relative_manifest
        manifest = load_json(manifest_path)
        if manifest.get("issue_id") != "SP-automotive-ee-architecture-2023-2026":
            raise ValueError(f"unexpected issue_id in {relative_manifest}")
        entries = manifest.get("cases")
        if not isinstance(entries, list):
            raise ValueError(f"manifest cases must be array: {relative_manifest}")
        base = manifest_path.parent
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError(f"invalid case in {relative_manifest}")
            result_rel = entry.get("result_path")
            task_id = entry.get("evidence_task_id")
            if not isinstance(result_rel, str) or not isinstance(task_id, str):
                raise ValueError(f"case missing result/task identity in {relative_manifest}")
            result_path = base / result_rel
            if not result_path.is_file():
                raise ValueError(f"Evidence result missing: {result_path}")
            expected_result_sha = entry.get("result_sha256")
            if sha256_file(result_path) != expected_result_sha:
                raise ValueError(f"Evidence result SHA mismatch: {task_id}")
            cases.append({
                "manifest": relative_manifest,
                "case": entry,
                "result_path": result_path,
            })
    return cases


def aggregate(*, repo_root: Path, package_root: Path, output_root: Path, manifests: list[str]) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    package_root = package_root.resolve()
    output_root = output_root.resolve()
    package, package_tasks = load_package_tasks(package_root)
    prompt_path = package_root / package["prompt"]["path"]
    if sha256_file(prompt_path) != package["prompt"]["sha256"]:
        raise ValueError("package prompt SHA mismatch")
    run_validator, _ = validators(package_root)
    cases = discover_cases(repo_root, manifests)

    by_task: dict[str, list[dict[str, Any]]] = {}
    for item in cases:
        task_id = item["case"]["evidence_task_id"]
        by_task.setdefault(task_id, []).append(item)

    expected_ids = set(package_tasks)
    actual_ids = set(by_task)
    missing = sorted(expected_ids - actual_ids)
    unexpected = sorted(actual_ids - expected_ids)
    duplicates = sorted(task_id for task_id, values in by_task.items() if len(values) != 1)
    if missing or unexpected or duplicates:
        raise ValueError(
            f"Evidence coverage failure: missing={missing}, unexpected={unexpected}, duplicates={duplicates}"
        )

    reviewed: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    recommendation_counts: Counter[str] = Counter()
    artifact_type_counts: Counter[str] = Counter()
    source_class_counts: Counter[str] = Counter()
    evidence_class_counts: Counter[str] = Counter()
    partial_ids: list[str] = []
    inspect_more_ids: list[str] = []
    hold_ids: list[str] = []
    verification_reports: list[dict[str, Any]] = []

    for task_id in sorted(expected_ids):
        case = by_task[task_id][0]
        result_path = case["result_path"]
        run = load_json(result_path)
        task_meta = package_tasks[task_id]
        expected_task_sha = task_meta["entry"]["sha256"]
        if case["case"].get("evidence_task_sha256") != expected_task_sha:
            raise ValueError(f"manifest task SHA mismatch: {task_id}")
        if run.get("evidence_task_sha256") != expected_task_sha:
            raise ValueError(f"Evidence Run task SHA mismatch: {task_id}")
        if run.get("prompt_sha256") != package["prompt"]["sha256"]:
            raise ValueError(f"Evidence Run prompt SHA mismatch: {task_id}")

        invariant_report, invariant_passed = validate_evidence_run.validate(
            task_meta["path"], result_path, prompt_path
        )
        schema_errors = sorted(run_validator.iter_errors(run), key=lambda err: list(err.absolute_path))
        if not invariant_passed or schema_errors:
            raise ValueError(
                f"Evidence validation failed for {task_id}: invariant={invariant_report.get('errors')}, "
                f"schema={[error.message for error in schema_errors[:5]]}"
            )

        card = run["card"]
        status = card["status"]
        recommendation = card["editorial"]["candidate_recommendation"]
        artifact_type = card["artifact"]["artifact_type"]
        status_counts[status] += 1
        recommendation_counts[recommendation] += 1
        artifact_type_counts[artifact_type] += 1
        if status == "PARTIAL":
            partial_ids.append(task_id)
        if recommendation == "INSPECT_MORE":
            inspect_more_ids.append(task_id)
        if recommendation == "HOLD":
            hold_ids.append(task_id)
        for source in card.get("sources") or []:
            source_class_counts[source.get("source_class")] += 1
        for field in ("claims", "metrics", "limitations"):
            for evidence in card.get(field) or []:
                evidence_class_counts[evidence.get("evidence_class")] += 1

        reviewed.append(run)
        verification_reports.append({
            "evidence_task_id": task_id,
            "result_path": result_path.relative_to(repo_root).as_posix(),
            "result_sha256": sha256_file(result_path),
            "status": status,
            "recommendation": recommendation,
            "artifact_type": artifact_type,
            "production_invariant_validator_passed": True,
            "generated_schema_validation_passed": True,
        })

    reviewed_path = output_root / "evidence-reviewed.jsonl"
    write_jsonl(reviewed_path, reviewed)
    pipeline_state = repo_root / "sources" / package["issue_id"] / "pipeline-state.json"
    matrix = build_candidate_matrix.build(reviewed_path, pipeline_state)
    matrix_json = output_root / "candidate-matrix.json"
    matrix_md = output_root / "candidate-matrix.md"
    write_json(matrix_json, matrix)
    matrix_md.write_text(build_candidate_matrix.render_markdown(matrix), encoding="utf-8")

    readiness_counts = Counter(row["comparison_readiness"] for row in matrix["rows"])
    timing_counts = Counter(row["timing_relation"] for row in matrix["rows"])
    result = {
        "schema_version": "1.0",
        "experiment": "PROFILED_EVIDENCE_AGGREGATE_AND_SHARED_CANDIDATE_MATRIX",
        "issue_id": package["issue_id"],
        "expected_task_count": len(package_tasks),
        "result_count": len(reviewed),
        "coverage": {
            "missing_task_ids": missing,
            "unexpected_task_ids": unexpected,
            "duplicate_task_ids": duplicates,
            "complete_one_to_one": not (missing or unexpected or duplicates) and len(reviewed) == len(package_tasks),
        },
        "evidence_status_counts": dict(sorted(status_counts.items())),
        "recommendation_counts": dict(sorted(recommendation_counts.items())),
        "artifact_type_counts": dict(sorted(artifact_type_counts.items())),
        "source_class_counts": dict(sorted((str(k), v) for k, v in source_class_counts.items())),
        "evidence_class_counts": dict(sorted((str(k), v) for k, v in evidence_class_counts.items())),
        "partial_task_ids": sorted(partial_ids),
        "inspect_more_task_ids": sorted(inspect_more_ids),
        "hold_task_ids": sorted(hold_ids),
        "validation": {
            "production_validator": "scripts/validate_evidence_run.py",
            "production_validator_modified": False,
            "generated_domain_schema": package["contracts"].get("profile_id"),
            "all_results_revalidated": True,
            "reports": verification_reports,
        },
        "reviewed_evidence": {
            "path": "evidence-reviewed.jsonl",
            "sha256": sha256_file(reviewed_path),
        },
        "candidate_matrix": {
            "shared_builder": "scripts/build_candidate_matrix.py",
            "shared_builder_modified": False,
            "row_count": matrix["row_count"],
            "recommendation_counts": matrix["recommendation_counts"],
            "readiness_counts": dict(sorted(readiness_counts.items())),
            "timing_counts": dict(sorted(timing_counts.items())),
            "json_path": "candidate-matrix.json",
            "json_sha256": sha256_file(matrix_json),
            "markdown_path": "candidate-matrix.md",
            "markdown_sha256": sha256_file(matrix_md),
        },
        "production_ai_pipeline_modified": False,
        "lifecycle_advanced": False,
        "semantics": [
            "complete_one_to_one means one validated experimental Evidence result exists for every pinned Evidence Task; it does not mean every card is VERIFIED.",
            "PARTIAL, HOLD and INSPECT_MORE remain explicit and are preserved into Candidate comparison.",
            "The production Special/weekly lifecycle state is not modified or advanced by this aggregate probe.",
            "The shared Candidate Matrix is comparison-only and does not perform final Candidate Selection."
        ],
        "finding": "All pinned Evidence tasks can be represented by domain-profiled Evidence Runs and fed into the unchanged shared Candidate comparison mechanics without modifying the production AI pipeline."
    }
    write_json(output_root / "aggregate-manifest.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--manifest", action="append", dest="manifests")
    args = parser.parse_args()
    result = aggregate(
        repo_root=Path(args.repo_root),
        package_root=Path(args.package_root),
        output_root=Path(args.output_root),
        manifests=args.manifests or DEFAULT_MANIFESTS,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
