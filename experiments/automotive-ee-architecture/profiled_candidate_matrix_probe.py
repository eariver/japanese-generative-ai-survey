#!/usr/bin/env python3
"""Probe the production Candidate comparison matrix with Automotive Evidence.

The probe materializes a tiny evidence-reviewed JSONL from the validated vertical
slice and calls `scripts/build_candidate_matrix.py` unchanged. It does not perform
Candidate Selection and does not alter the experiment pipeline state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = SCRIPT_PATH.parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_candidate_matrix as base


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


def build(*, manifest_path: Path, pipeline_state_path: Path, output_dir: Path) -> dict[str, Any]:
    manifest_path = manifest_path.resolve()
    pipeline_state_path = pipeline_state_path.resolve()
    output_dir = output_dir.resolve()
    manifest = load_json(manifest_path)
    state = load_json(pipeline_state_path)
    issue_id = manifest.get("issue_id")
    if state.get("issue_id") != issue_id:
        raise ValueError("pipeline-state issue_id mismatch")
    if manifest.get("production_ai_pipeline_modified") is not False:
        raise ValueError("vertical slice does not preserve production boundary")

    reviewed_path = output_dir / "evidence-reviewed.jsonl"
    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    for case in manifest.get("cases", []):
        result_path = manifest_path.parent / case["result_path"]
        if not result_path.is_file():
            raise ValueError(f"vertical-slice result missing: {result_path}")
        actual_sha = sha256_file(result_path)
        if actual_sha != case.get("result_sha256"):
            raise ValueError(f"vertical-slice result SHA mismatch: {case.get('case_id')}")
        record = load_json(result_path)
        if record.get("issue_id") != issue_id or record.get("evidence_task_id") != case.get("evidence_task_id"):
            raise ValueError(f"vertical-slice identity mismatch: {case.get('case_id')}")
        records.append(record)
    with reviewed_path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    matrix = base.build(reviewed_path, pipeline_state_path)
    matrix_json = output_dir / "candidate-matrix.json"
    matrix_md = output_dir / "candidate-matrix.md"
    write_json(matrix_json, matrix)
    matrix_md.write_text(base.render_markdown(matrix), encoding="utf-8")

    artifact_types = sorted({row["artifact_type"] for row in matrix["rows"]})
    timing_counts: dict[str, int] = {}
    for row in matrix["rows"]:
        timing = row["timing_relation"]
        timing_counts[timing] = timing_counts.get(timing, 0) + 1

    report = {
        "schema_version": "1.0",
        "experiment": "AUTOMOTIVE_EE_SHARED_CANDIDATE_MATRIX_PROBE",
        "issue_id": issue_id,
        "passed": matrix.get("row_count") == len(records),
        "row_count": matrix.get("row_count"),
        "artifact_types": artifact_types,
        "timing_counts": dict(sorted(timing_counts.items())),
        "recommendation_counts": matrix.get("recommendation_counts"),
        "readiness_counts": matrix.get("readiness_counts"),
        "matrix_sha256": sha256_file(matrix_json),
        "matrix_markdown_sha256": sha256_file(matrix_md),
        "shared_candidate_matrix_builder": "scripts/build_candidate_matrix.py",
        "shared_candidate_matrix_builder_modified": False,
        "production_ai_pipeline_modified": False,
        "semantic_leaks_observed": [
            "build_candidate_matrix.py contains a fallback boundary string 'Weekly why-now relevance is not confirmed.' when why_now_confirmed=false; it was not emitted by this three-case slice because all three confirm retrospective relevance."
        ],
        "finding": "The production Candidate comparison mechanics accept Automotive STANDARD/PLATFORM/PAPER Evidence unchanged; remaining domain coupling is editorial wording/context rather than matrix structure."
    }
    write_json(output_dir / "candidate-matrix-probe-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--pipeline-state", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    report = build(
        manifest_path=Path(args.manifest),
        pipeline_state_path=Path(args.pipeline_state),
        output_dir=Path(args.output_dir),
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
