#!/usr/bin/env python3
"""Validate the Automotive E/E Evidence vertical slice against one pinned package.

This experiment reuses the production stdlib Evidence invariant validator unchanged
and adds strict validation against the generated domain Evidence Run/Card schemas.
It never enters the production Evidence acceptance/lifecycle path.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = SCRIPT_PATH.parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import validate_evidence_run

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - CI installs it explicitly.
    raise SystemExit("jsonschema is required for the vertical-slice schema probe") from exc


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


def require_file(root: Path, relative: str, label: str) -> Path:
    if not isinstance(relative, str) or not relative:
        raise ValueError(f"{label} path missing")
    path = root / relative
    if not path.is_file():
        raise ValueError(f"required {label} missing: {path}")
    return path


def inline_card_schema(run_schema: dict[str, Any], card_schema: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(run_schema)
    card = result.get("properties", {}).get("card")
    if not isinstance(card, dict) or card.get("$ref") != "evidence-card.schema.json":
        raise ValueError("generated Evidence Run schema no longer has the expected card $ref")
    result["properties"]["card"] = card_schema
    return result


def validate(*, repo_root: Path, package_root: Path, manifest_path: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    package_root = package_root.resolve()
    manifest_path = manifest_path.resolve()
    manifest = load_json(manifest_path)
    if manifest.get("schema_version") != "1.0":
        raise ValueError("unsupported vertical-slice manifest schema")
    if manifest.get("production_ai_pipeline_modified") is not False:
        raise ValueError("vertical slice no longer asserts an untouched production AI pipeline")

    package = load_json(package_root / "evidence-execution-package.json")
    pinned = manifest.get("pinned_evidence_package")
    if not isinstance(pinned, dict):
        raise ValueError("pinned_evidence_package missing")
    if package.get("issue_id") != manifest.get("issue_id"):
        raise ValueError("Evidence package issue mismatch")
    expected_package_fields = {
        "task_count": package["evidence_tasks"]["task_count"],
        "evidence_task_manifest_sha256": package["evidence_tasks"]["manifest_sha256"],
        "evidence_task_index_sha256": package["evidence_tasks"]["index_sha256"],
        "prompt_id": package["prompt"]["prompt_id"],
        "prompt_sha256": package["prompt"]["sha256"],
        "evidence_run_schema_sha256": package["contracts"]["evidence_run"]["sha256"],
        "evidence_card_schema_sha256": package["contracts"]["evidence_card"]["sha256"],
    }
    for key, actual in expected_package_fields.items():
        if pinned.get(key) != actual:
            raise ValueError(f"pinned Evidence package field mismatch for {key}: {pinned.get(key)!r} != {actual!r}")

    prompt_path = require_file(package_root, package["prompt"]["path"], "Evidence prompt")
    run_schema_path = require_file(package_root, package["contracts"]["evidence_run"]["path"], "Evidence Run schema")
    card_schema_path = require_file(package_root, package["contracts"]["evidence_card"]["path"], "Evidence Card schema")
    if sha256_file(prompt_path) != pinned["prompt_sha256"]:
        raise ValueError("prompt bytes do not match vertical-slice pin")
    if sha256_file(run_schema_path) != pinned["evidence_run_schema_sha256"]:
        raise ValueError("Evidence Run schema bytes do not match vertical-slice pin")
    if sha256_file(card_schema_path) != pinned["evidence_card_schema_sha256"]:
        raise ValueError("Evidence Card schema bytes do not match vertical-slice pin")

    run_schema = load_json(run_schema_path)
    card_schema = load_json(card_schema_path)
    inlined_run_schema = inline_card_schema(run_schema, card_schema)
    task_entries = {
        entry["evidence_task_id"]: entry
        for entry in package["evidence_tasks"]["tasks"]
        if isinstance(entry, dict) and isinstance(entry.get("evidence_task_id"), str)
    }

    cases = manifest.get("cases")
    if not isinstance(cases, list) or len(cases) != manifest.get("expected_case_count"):
        raise ValueError("vertical-slice case count mismatch")
    expected_types = set(manifest.get("expected_artifact_types") or [])
    observed_types: set[str] = set()
    reports: list[dict[str, Any]] = []
    seen_task_ids: set[str] = set()

    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("vertical-slice cases must be objects")
        task_id = case.get("evidence_task_id")
        if not isinstance(task_id, str) or task_id in seen_task_ids:
            raise ValueError(f"invalid/duplicate case evidence_task_id: {task_id!r}")
        seen_task_ids.add(task_id)
        task_entry = task_entries.get(task_id)
        if task_entry is None:
            raise ValueError(f"vertical-slice task absent from pinned package: {task_id}")
        if task_entry.get("sha256") != case.get("evidence_task_sha256"):
            raise ValueError(f"vertical-slice task SHA pin mismatch: {task_id}")

        task_path = require_file(package_root, task_entry["path"], f"Evidence Task {task_id}")
        result_path = require_file(manifest_path.parent, case.get("result_path"), f"vertical-slice result {task_id}")
        result_sha = sha256_file(result_path)
        if result_sha != case.get("result_sha256"):
            raise ValueError(f"vertical-slice result SHA mismatch for {task_id}: {result_sha}")

        invariant_report, passed = validate_evidence_run.validate(task_path, result_path, prompt_path)
        if not passed:
            raise ValueError(f"production Evidence invariant validator failed for {task_id}: {invariant_report['errors']}")

        run = load_json(result_path)
        jsonschema.Draft202012Validator(card_schema).validate(run["card"])
        jsonschema.Draft202012Validator(inlined_run_schema).validate(run)

        artifact_type = run["card"]["artifact"]["artifact_type"]
        observed_types.add(artifact_type)
        if artifact_type != case.get("artifact_type"):
            raise ValueError(f"artifact type mismatch for {task_id}: {artifact_type}")
        if run["card"]["status"] != case.get("expected_status"):
            raise ValueError(f"card status mismatch for {task_id}")
        if run["card"]["editorial"]["candidate_recommendation"] != case.get("expected_recommendation"):
            raise ValueError(f"recommendation mismatch for {task_id}")

        reports.append({
            "case_id": case.get("case_id"),
            "evidence_task_id": task_id,
            "result_sha256": result_sha,
            "artifact_type": artifact_type,
            "status": run["card"]["status"],
            "recommendation": run["card"]["editorial"]["candidate_recommendation"],
            "production_invariant_validator_passed": True,
            "generated_schema_validation_passed": True,
            "source_count": invariant_report.get("source_count"),
            "event_count": invariant_report.get("event_count"),
            "claim_count": invariant_report.get("claim_count"),
            "metric_count": invariant_report.get("metric_count"),
            "limitation_count": invariant_report.get("limitation_count"),
        })

    if observed_types != expected_types:
        raise ValueError(f"vertical-slice ontology coverage mismatch: observed={sorted(observed_types)} expected={sorted(expected_types)}")

    return {
        "schema_version": "1.0",
        "experiment": "AUTOMOTIVE_EE_EVIDENCE_VERTICAL_SLICE_VALIDATION",
        "issue_id": manifest["issue_id"],
        "passed": True,
        "case_count": len(reports),
        "artifact_types": sorted(observed_types),
        "cases": reports,
        "production_validator": "scripts/validate_evidence_run.py",
        "production_validator_modified": False,
        "production_ai_pipeline_modified": False,
        "finding": "Three representative Automotive Evidence Runs validate against exact shared task/prompt provenance, the unchanged production invariant validator, and the generated strict domain schemas."
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = validate(
        repo_root=Path(args.repo_root),
        package_root=Path(args.package_root),
        manifest_path=Path(args.manifest),
    )
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
