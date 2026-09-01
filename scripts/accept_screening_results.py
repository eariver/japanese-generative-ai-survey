#!/usr/bin/env python3
"""Accept one complete, validated screening result set into a weekly work tree.

The supplied screening package is treated as immutable input provenance. Every
result batch must match the exact batch bytes and prompt bytes pinned by that
package. Acceptance is complete-only: partial screening may be resumed outside
the repository, but a weekly work branch receives one auditable complete result
set at a time.

A successful new acceptance closes discovery and advances the coarse lifecycle to
CANDIDATES_NORMALIZED. It still does not imply primary-source Evidence review,
Candidate Selection, Issue Architecture, or any publication gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import merge_screening_results
from scripts import validate_screening_result

ISSUE_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ALLOWED_LIFECYCLE = "DISCOVERY_COLLECTED"
TARGET_LIFECYCLE = "CANDIDATES_NORMALIZED"


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


def count_jsonl(path: Path) -> int:
    count = 0
    with path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            if raw.strip():
                json.loads(raw)
                count += 1
    return count


def require_regular_file(root: Path, relative: str) -> Path:
    path = root / relative
    if path.is_symlink():
        raise ValueError(f"symlink is forbidden in screening package: {relative}")
    if not path.is_file():
        raise ValueError(f"required screening package file missing: {relative}")
    return path


def validate_sha_field(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValueError(f"{label} must be a lowercase SHA-256 hex digest")
    return value


def validate_package_files(package_root: Path, issue_id: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    package_path = require_regular_file(package_root, "screening-run-package.json")
    package = load_json(package_path)
    if package.get("schema_version") != "1.0":
        raise ValueError("unsupported screening package schema_version")
    if package.get("issue_id") != issue_id:
        raise ValueError("screening package issue_id mismatch")

    source = package.get("source")
    if not isinstance(source, dict) or not isinstance(source.get("ref"), str) or not source["ref"]:
        raise ValueError("screening package source metadata is missing")
    commit_sha = source.get("commit_sha")
    if not isinstance(commit_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise ValueError("screening package source commit_sha is invalid")

    provenance = package.get("provenance")
    if not isinstance(provenance, dict):
        raise ValueError("screening package provenance is missing")
    validate_sha_field(provenance.get("pipeline_state_sha256"), "pipeline_state_sha256")
    validate_sha_field(provenance.get("raw_index_sha256"), "raw_index_sha256")

    prompt_meta = package.get("prompt")
    if not isinstance(prompt_meta, dict) or prompt_meta.get("prompt_id") != "source-screening-v0.1":
        raise ValueError("screening package prompt metadata is invalid")
    prompt_rel = prompt_meta.get("path")
    if not isinstance(prompt_rel, str) or not prompt_rel:
        raise ValueError("screening package prompt path is invalid")
    prompt_path = require_regular_file(package_root, prompt_rel)
    if sha256_file(prompt_path) != validate_sha_field(prompt_meta.get("sha256"), "prompt.sha256"):
        raise ValueError("screening package prompt bytes do not match prompt.sha256")

    contract_meta = package.get("result_contract")
    if not isinstance(contract_meta, dict):
        raise ValueError("screening package result contract metadata is missing")
    contract_rel = contract_meta.get("path")
    if not isinstance(contract_rel, str) or not contract_rel:
        raise ValueError("screening package result contract path is invalid")
    contract_path = require_regular_file(package_root, contract_rel)
    if sha256_file(contract_path) != validate_sha_field(contract_meta.get("sha256"), "result_contract.sha256"):
        raise ValueError("screening result contract bytes do not match the package digest")
    json.loads(contract_path.read_text(encoding="utf-8"))

    screening = package.get("screening_input")
    if not isinstance(screening, dict):
        raise ValueError("screening package input metadata is missing")
    manifest_rel = screening.get("manifest_path")
    index_rel = screening.get("index_path")
    if not isinstance(manifest_rel, str) or not isinstance(index_rel, str):
        raise ValueError("screening package manifest/index paths are invalid")
    manifest_path = require_regular_file(package_root, manifest_rel)
    index_path = require_regular_file(package_root, index_rel)
    if sha256_file(manifest_path) != validate_sha_field(screening.get("manifest_sha256"), "screening manifest SHA"):
        raise ValueError("screening manifest bytes do not match the package digest")
    if sha256_file(index_path) != validate_sha_field(screening.get("index_sha256"), "screening index SHA"):
        raise ValueError("screening index bytes do not match the package digest")
    if count_jsonl(index_path) != screening.get("record_count"):
        raise ValueError("screening index record count does not match package metadata")

    batches = screening.get("batches")
    if not isinstance(batches, list) or not batches:
        raise ValueError("screening package must contain at least one batch")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for item in batches:
        if not isinstance(item, dict):
            raise ValueError("screening package batch metadata must be objects")
        batch_id = item.get("batch_id")
        relative = item.get("path")
        if not isinstance(batch_id, str) or not re.fullmatch(r"batch-[0-9]{3,}", batch_id):
            raise ValueError(f"invalid screening batch_id: {batch_id!r}")
        if batch_id in seen:
            raise ValueError(f"duplicate screening batch_id: {batch_id}")
        seen.add(batch_id)
        if not isinstance(relative, str) or Path(relative).stem != batch_id:
            raise ValueError(f"screening batch path does not match batch_id: {item!r}")
        path = require_regular_file(package_root, relative)
        expected_sha = validate_sha_field(item.get("sha256"), f"{batch_id}.sha256")
        if sha256_file(path) != expected_sha:
            raise ValueError(f"screening batch bytes do not match package digest: {batch_id}")
        if path.stat().st_size != item.get("bytes"):
            raise ValueError(f"screening batch byte count mismatch: {batch_id}")
        if count_jsonl(path) != item.get("record_count"):
            raise ValueError(f"screening batch record count mismatch: {batch_id}")
        normalized.append({**item, "_path": path})

    if sum(item["record_count"] for item in normalized) != screening.get("record_count"):
        raise ValueError("sum of screening batch records does not equal screening index record_count")
    return package, normalized


def validate_repo_basis(package: dict[str, Any], repo_root: Path, issue_id: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    raw_index_path = repo_root / "sources" / issue_id / "raw-index.json"
    if not state_path.is_file() or not raw_index_path.is_file():
        raise ValueError("weekly work tree must contain pipeline-state.json and raw-index.json before screening acceptance")
    provenance = package["provenance"]
    if sha256_file(state_path) != provenance["pipeline_state_sha256"]:
        raise ValueError("weekly pipeline-state bytes no longer match the screening package basis")
    if sha256_file(raw_index_path) != provenance["raw_index_sha256"]:
        raise ValueError("weekly raw-index bytes no longer match the screening package basis")
    state = load_json(state_path)
    if state.get("issue_id") != issue_id:
        raise ValueError("weekly pipeline state issue_id mismatch")
    return state


def result_set_digest(result_records: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for item in sorted(result_records, key=lambda value: value["batch_id"]):
        digest.update(item["batch_id"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def acceptance_dir(repo_root: Path, issue_id: str, result_set_sha256: str) -> Path:
    return repo_root / "sources" / issue_id / "screening" / "runs" / result_set_sha256


def accept(
    *,
    package_root: Path,
    results_dir: Path,
    repo_root: Path,
    issue_id: str,
    review_reference: str,
) -> tuple[dict[str, Any], bool]:
    if not ISSUE_RE.fullmatch(issue_id):
        raise ValueError("issue_id must use YYYY-Www form")
    if not isinstance(review_reference, str) or not review_reference.strip():
        raise ValueError("review_reference must be a non-empty string")

    package_root = package_root.resolve()
    results_dir = results_dir.resolve()
    repo_root = repo_root.resolve()
    if not results_dir.is_dir():
        raise ValueError(f"screening results directory missing: {results_dir}")

    package, batches = validate_package_files(package_root, issue_id)

    entries = list(results_dir.iterdir())
    if any(path.is_symlink() for path in entries):
        raise ValueError("symlinks are forbidden in screening results")
    non_files = sorted(path.name for path in entries if not path.is_file())
    if non_files:
        raise ValueError(f"screening results directory may contain files only: {non_files}")
    actual_paths = sorted(entries)
    expected_names = {f"{item['batch_id']}.json" for item in batches}
    actual_names = {path.name for path in actual_paths}
    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    if missing or extra:
        raise ValueError(f"screening result set must be complete and exact: missing={missing} extra={extra}")

    prompt_path = package_root / package["prompt"]["path"]
    result_records: list[dict[str, Any]] = []
    validation_reports: dict[str, dict[str, Any]] = {}
    for item in batches:
        batch_id = item["batch_id"]
        result_path = results_dir / f"{batch_id}.json"
        report, passed = validate_screening_result.validate(item["_path"], result_path, prompt_path)
        if not passed:
            raise ValueError(f"screening result validation failed for {batch_id}: {report['errors']}")
        validation_reports[batch_id] = report
        result_records.append(
            {
                "batch_id": batch_id,
                "sha256": sha256_file(result_path),
                "bytes": result_path.stat().st_size,
                "runner": load_json(result_path)["runner"],
            }
        )

    set_sha = result_set_digest(result_records)
    destination = acceptance_dir(repo_root, issue_id, set_sha)
    manifest_path = destination / "acceptance.json"
    acceptance = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "result_set_sha256": set_sha,
        "review_reference": review_reference.strip(),
        "screening_package": {
            "source_ref": package["source"]["ref"],
            "source_commit_sha": package["source"]["commit_sha"],
            "package_manifest_sha256": sha256_file(package_root / "screening-run-package.json"),
            "pipeline_state_sha256": package["provenance"]["pipeline_state_sha256"],
            "raw_index_sha256": package["provenance"]["raw_index_sha256"],
            "prompt_sha256": package["prompt"]["sha256"],
            "screening_index_sha256": package["screening_input"]["index_sha256"],
        },
        "results": sorted(result_records, key=lambda value: value["batch_id"]),
        "state_transition": {
            "from": ALLOWED_LIFECYCLE,
            "to": TARGET_LIFECYCLE,
            "gate": "candidate_inventory",
            "gate_value": "passed",
        },
        "rules": [
            "Only a complete one-result-per-batch screening set is accepted into the weekly work tree.",
            "Every result is revalidated against the exact package batch and prompt bytes before persistence.",
            "Accepted result bytes are append-only and addressed by a deterministic result-set SHA-256.",
            "Successful screening acceptance closes discovery by advancing lifecycle to CANDIDATES_NORMALIZED and candidate_inventory to passed.",
            "Screening acceptance does not imply primary-source Evidence review, Candidate Selection, Issue Architecture, or publication approval.",
        ],
    }

    if manifest_path.exists():
        existing = load_json(manifest_path)
        if existing != acceptance:
            raise ValueError(f"screening acceptance path exists with different manifest: {manifest_path}")
        return {
            "schema_version": "1.0",
            "passed": True,
            "issue_id": issue_id,
            "status": "ALREADY_ACCEPTED",
            "result_set_sha256": set_sha,
            "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
        }, True

    state = validate_repo_basis(package, repo_root, issue_id)
    if state.get("lifecycle_state") != ALLOWED_LIFECYCLE:
        raise ValueError(
            f"new screening results may be accepted only in {ALLOWED_LIFECYCLE}; "
            f"current lifecycle_state={state.get('lifecycle_state')!r}"
        )
    gates = state.get("gates")
    if not isinstance(gates, dict) or "candidate_inventory" not in gates:
        raise ValueError("weekly pipeline state candidate_inventory gate is missing")
    updated_state = deepcopy(state)
    updated_state["lifecycle_state"] = TARGET_LIFECYCLE
    updated_state["gates"]["candidate_inventory"] = "passed"

    with tempfile.TemporaryDirectory() as tmp:
        derived = Path(tmp) / "derived"
        merge_manifest, merged = merge_screening_results.merge(
            package_root / "input" / "batches",
            results_dir,
            prompt_path,
            derived,
            require_complete=True,
        )
        if not merged or not merge_manifest.get("complete"):
            raise ValueError(f"complete screening merge failed: {merge_manifest}")

        destination.mkdir(parents=True, exist_ok=False)
        (destination / "results").mkdir()
        for record in result_records:
            source = results_dir / f"{record['batch_id']}.json"
            target = destination / "results" / source.name
            shutil.copyfile(source, target)
            if sha256_file(target) != record["sha256"]:
                raise RuntimeError(f"screening result copy verification failed: {target}")

        shutil.copyfile(package_root / "screening-run-package.json", destination / "screening-run-package.json")
        for name in ("screening-reviewed.jsonl", "verification-queue.jsonl", "screening-progress.json"):
            shutil.copyfile(derived / name, destination / name)
        validations = destination / "validation"
        validations.mkdir()
        for batch_id, report in sorted(validation_reports.items()):
            (validations / f"{batch_id}.json").write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        manifest_path.write_text(json.dumps(acceptance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state_path.write_text(json.dumps(updated_state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return {
        "schema_version": "1.0",
        "passed": True,
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "result_set_sha256": set_sha,
        "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "batch_count": len(result_records),
        "reviewed_record_count": merge_manifest["reviewed_record_count"],
        "verification_queue_count": merge_manifest["verification_queue_count"],
        "lifecycle_state": TARGET_LIFECYCLE,
        "candidate_inventory_gate": "passed",
    }, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--review-reference", required=True)
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result, passed = accept(
        package_root=Path(args.package_root),
        results_dir=Path(args.results_dir),
        repo_root=Path(args.repo_root),
        issue_id=args.issue_id,
        review_reference=args.review_reference,
    )
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
