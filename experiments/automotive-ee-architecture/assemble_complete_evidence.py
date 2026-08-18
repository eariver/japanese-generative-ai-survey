#!/usr/bin/env python3
"""Assemble and revalidate the complete Automotive E/E Evidence set.

This experiment is deliberately read-only with respect to the production lifecycle.
It gathers the 3-case vertical slice and Evidence batches 01-05, proves that they form
an exact one-to-one cover of the 45 Tasks in the pinned execution package, reruns the
unchanged production invariant validator and the generated domain JSON Schema, then
feeds the resulting reviewed JSONL to the unchanged production Candidate-matrix
builder.

No production pipeline state is advanced and no Candidate Selection is performed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).resolve()
REPO_DEFAULT = SCRIPT.parents[2]
if str(REPO_DEFAULT) not in sys.path:
    sys.path.insert(0, str(REPO_DEFAULT))

from scripts import build_candidate_matrix, validate_evidence_run

RESULT_ROOTS = [
    "experiments/automotive-ee-architecture/evidence-vertical-slice/results",
    "experiments/automotive-ee-architecture/evidence-batches/batch-01/results",
    "experiments/automotive-ee-architecture/evidence-batches/batch-02/results",
    "experiments/automotive-ee-architecture/evidence-batches/batch-03/results",
    "experiments/automotive-ee-architecture/evidence-batches/batch-04/results",
    "experiments/automotive-ee-architecture/evidence-batches/batch-05/results",
]


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for value in values:
            fh.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")


def load_package_tasks(package_root: Path) -> tuple[dict[str, Any], dict[str, Path]]:
    package = load_json(package_root / "evidence-execution-package.json")
    tasks_meta = package.get("evidence_tasks")
    if not isinstance(tasks_meta, dict):
        raise ValueError("package evidence_tasks missing")
    entries = tasks_meta.get("tasks")
    if not isinstance(entries, list) or not entries:
        raise ValueError("package task list missing")
    task_paths: dict[str, Path] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("package task entry must be object")
        task_id = entry.get("evidence_task_id")
        relative = entry.get("path")
        if not isinstance(task_id, str) or not task_id or task_id in task_paths:
            raise ValueError(f"invalid/duplicate package task id: {task_id!r}")
        if not isinstance(relative, str) or not relative:
            raise ValueError(f"package task path missing: {task_id}")
        path = package_root / relative
        if not path.is_file():
            raise ValueError(f"package task file missing: {relative}")
        if sha256_file(path) != entry.get("sha256"):
            raise ValueError(f"package task SHA mismatch: {task_id}")
        task_paths[task_id] = path
    if len(task_paths) != tasks_meta.get("task_count"):
        raise ValueError("package task count mismatch")
    return package, task_paths


def collect_results(repo_root: Path) -> dict[str, Path]:
    result_paths: dict[str, Path] = {}
    for relative_root in RESULT_ROOTS:
        root = repo_root / relative_root
        if not root.is_dir():
            raise ValueError(f"result root missing: {relative_root}")
        for path in sorted(root.glob("*.json")):
            run = load_json(path)
            task_id = run.get("evidence_task_id")
            if not isinstance(task_id, str) or not task_id:
                raise ValueError(f"Evidence result missing task id: {path}")
            if task_id in result_paths:
                raise ValueError(f"duplicate Evidence result for {task_id}: {result_paths[task_id]} and {path}")
            result_paths[task_id] = path
    return result_paths


def validate_schema(package_root: Path, run: dict[str, Any]) -> None:
    try:
        from jsonschema import Draft202012Validator, RefResolver
    except ImportError as exc:  # pragma: no cover - CI installs it explicitly
        raise RuntimeError("jsonschema is required for complete Evidence assembly") from exc
    run_schema = load_json(package_root / "contract" / "evidence-run.schema.json")
    card_schema = load_json(package_root / "contract" / "evidence-card.schema.json")
    run_path = (package_root / "contract" / "evidence-run.schema.json").resolve()
    card_path = (package_root / "contract" / "evidence-card.schema.json").resolve()
    resolver = RefResolver(
        base_uri=run_path.as_uri(),
        referrer=run_schema,
        store={"evidence-card.schema.json": card_schema, card_path.as_uri(): card_schema},
    )
    errors = sorted(Draft202012Validator(run_schema, resolver=resolver).iter_errors(run), key=lambda e: list(e.path))
    if errors:
        error = errors[0]
        location = ".".join(str(x) for x in error.path) or "<root>"
        raise ValueError(f"generated Evidence schema rejected {location}: {error.message}")


def build(*, repo_root: Path, package_root: Path, output_root: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    package_root = package_root.resolve()
    output_root = output_root.resolve()
    package, tasks = load_package_tasks(package_root)
    results = collect_results(repo_root)

    expected = set(tasks)
    actual = set(results)
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing or unexpected:
        raise ValueError(f"Evidence coverage mismatch: missing={missing}, unexpected={unexpected}")

    prompt_path = package_root / package["prompt"]["path"]
    if sha256_file(prompt_path) != package["prompt"]["sha256"]:
        raise ValueError("pinned Evidence prompt SHA mismatch")

    reviewed: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    recommendation_counts: Counter[str] = Counter()
    artifact_type_counts: Counter[str] = Counter()
    source_class_counts: Counter[str] = Counter()
    evidence_class_counts: Counter[str] = Counter()
    provenance_rows: list[dict[str, Any]] = []

    for task_id in sorted(expected):
        task_path = tasks[task_id]
        result_path = results[task_id]
        run = load_json(result_path)
        invariant_report, invariant_passed = validate_evidence_run.validate(task_path, result_path, prompt_path)
        if not invariant_passed:
            raise ValueError(f"production invariant validator rejected {task_id}: {invariant_report.get('errors')}")
        validate_schema(package_root, run)
        reviewed.append(run)
        card = run["card"]
        status_counts[card["status"]] += 1
        recommendation_counts[card["editorial"]["candidate_recommendation"]] += 1
        artifact_type_counts[card["artifact"]["artifact_type"]] += 1
        for source in card.get("sources") or []:
            source_class_counts[source.get("source_class")] += 1
        for field in ("claims", "metrics", "limitations"):
            for item in card.get(field) or []:
                evidence_class_counts[item.get("evidence_class")] += 1
        provenance_rows.append({
            "evidence_task_id": task_id,
            "task_sha256": sha256_file(task_path),
            "result_path": result_path.relative_to(repo_root).as_posix(),
            "result_sha256": sha256_file(result_path),
            "status": card["status"],
            "recommendation": card["editorial"]["candidate_recommendation"],
            "artifact_type": card["artifact"]["artifact_type"],
        })

    reviewed_path = output_root / "evidence-reviewed.jsonl"
    write_jsonl(reviewed_path, reviewed)
    state_path = repo_root / "sources" / package["issue_id"] / "pipeline-state.json"
    matrix = build_candidate_matrix.build(reviewed_path, state_path)
    matrix_path = output_root / "candidate-matrix.json"
    write_json(matrix_path, matrix)
    provenance_path = output_root / "evidence-provenance.json"
    write_json(provenance_path, {"schema_version": "1.0", "issue_id": package["issue_id"], "rows": provenance_rows})

    timing_counts = Counter(row["timing_relation"] for row in matrix["rows"])
    readiness_counts = Counter(row["comparison_readiness"] for row in matrix["rows"])
    manifest = {
        "schema_version": "1.0",
        "experiment": "COMPLETE_AUTOMOTIVE_EE_EVIDENCE_SET",
        "issue_id": package["issue_id"],
        "pinned_evidence_package_run_id": 32144428137,
        "expected_task_count": len(tasks),
        "result_count": len(results),
        "missing_task_ids": missing,
        "unexpected_task_ids": unexpected,
        "all_production_invariant_validations_passed": True,
        "all_generated_schema_validations_passed": True,
        "status_counts": dict(sorted(status_counts.items())),
        "recommendation_counts": dict(sorted(recommendation_counts.items())),
        "artifact_type_counts": dict(sorted(artifact_type_counts.items())),
        "source_class_counts": dict(sorted((str(k), v) for k, v in source_class_counts.items())),
        "evidence_class_counts": dict(sorted((str(k), v) for k, v in evidence_class_counts.items())),
        "evidence_reviewed": {"path": "evidence-reviewed.jsonl", "sha256": sha256_file(reviewed_path)},
        "evidence_provenance": {"path": "evidence-provenance.json", "sha256": sha256_file(provenance_path)},
        "candidate_matrix": {
            "path": "candidate-matrix.json",
            "sha256": sha256_file(matrix_path),
            "row_count": matrix["row_count"],
            "recommendation_counts": matrix["recommendation_counts"],
            "readiness_counts": matrix["readiness_counts"],
            "timing_counts": dict(sorted(timing_counts.items())),
        },
        "shared_invariant_validator": "scripts/validate_evidence_run.py",
        "shared_candidate_matrix_builder": "scripts/build_candidate_matrix.py",
        "shared_production_files_modified": False,
        "production_lifecycle_advanced": False,
        "candidate_selection_performed": False,
        "finding": "All 45 Automotive Evidence Tasks have exactly one validated result and the complete set can be compared by the production Candidate-matrix builder unchanged. Lifecycle acceptance and Candidate Selection remain intentionally outside this probe.",
    }
    write_json(output_root / "complete-evidence-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    manifest = build(repo_root=Path(args.repo_root), package_root=Path(args.package_root), output_root=Path(args.output_root))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
