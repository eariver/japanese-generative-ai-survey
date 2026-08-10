#!/usr/bin/env python3
"""Accept one complete, validated Evidence result set into a weekly work tree.

Every Evidence Run is revalidated against the exact Evidence Task and prompt
bytes pinned by an Evidence execution package. Persistence is complete-only and
append-only. A successful new acceptance advances the coarse lifecycle from
CANDIDATES_NORMALIZED to EVIDENCE_REVIEWED and marks evidence_normalized=passed.

This remains pre-selection material: CANDIDATE/HOLD/INSPECT_MORE/REJECT are
Evidence recommendations and never constitute Candidate Selection approval.
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

from scripts import merge_evidence_runs
from scripts import validate_evidence_run

ISSUE_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_LIFECYCLE = "CANDIDATES_NORMALIZED"
TARGET_LIFECYCLE = "EVIDENCE_REVIEWED"


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


def validate_sha(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValueError(f"{label} must be a lowercase SHA-256 hex digest")
    return value


def require_file(root: Path, relative: str, label: str) -> Path:
    if not isinstance(relative, str) or not relative:
        raise ValueError(f"{label} path is missing")
    path = root / relative
    if path.is_symlink():
        raise ValueError(f"symlink is forbidden for {label}: {relative}")
    if not path.is_file():
        raise ValueError(f"required {label} missing: {relative}")
    return path


def count_jsonl(path: Path) -> int:
    count = 0
    with path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            if raw.strip():
                json.loads(raw)
                count += 1
    return count


def validate_package_files(package_root: Path, issue_id: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    manifest_path = require_file(package_root, "evidence-execution-package.json", "Evidence package manifest")
    package = load_json(manifest_path)
    if package.get("schema_version") != "1.0":
        raise ValueError("unsupported Evidence package schema_version")
    if package.get("issue_id") != issue_id:
        raise ValueError("Evidence package issue_id mismatch")

    source = package.get("source")
    if not isinstance(source, dict):
        raise ValueError("Evidence package source metadata is missing")
    if not isinstance(source.get("ref"), str) or not source["ref"]:
        raise ValueError("Evidence package source.ref is invalid")
    if not isinstance(source.get("commit_sha"), str) or not GIT_SHA_RE.fullmatch(source["commit_sha"]):
        raise ValueError("Evidence package source.commit_sha is invalid")
    validate_sha(source.get("pipeline_state_sha256"), "source.pipeline_state_sha256")

    screening = package.get("screening_basis")
    if not isinstance(screening, dict):
        raise ValueError("Evidence package screening_basis is missing")
    validate_sha(screening.get("result_set_sha256"), "screening_basis.result_set_sha256")
    validate_sha(screening.get("acceptance_sha256"), "screening_basis.acceptance_sha256")
    validate_sha(screening.get("verification_queue_sha256"), "screening_basis.verification_queue_sha256")
    if not isinstance(screening.get("acceptance_path"), str) or not screening["acceptance_path"]:
        raise ValueError("screening_basis.acceptance_path is invalid")
    if not isinstance(screening.get("verification_queue_path"), str) or not screening["verification_queue_path"]:
        raise ValueError("screening_basis.verification_queue_path is invalid")

    prompt_meta = package.get("prompt")
    if not isinstance(prompt_meta, dict) or prompt_meta.get("prompt_id") != "primary-source-verification-v0.1":
        raise ValueError("Evidence package prompt metadata is invalid")
    prompt_path = require_file(package_root, prompt_meta.get("path"), "Evidence prompt")
    if sha256_file(prompt_path) != validate_sha(prompt_meta.get("sha256"), "prompt.sha256"):
        raise ValueError("Evidence prompt bytes do not match package digest")

    contracts = package.get("contracts")
    if not isinstance(contracts, dict):
        raise ValueError("Evidence package contracts are missing")
    for key in ("evidence_run", "evidence_card"):
        meta = contracts.get(key)
        if not isinstance(meta, dict):
            raise ValueError(f"Evidence package contract missing: {key}")
        path = require_file(package_root, meta.get("path"), f"{key} contract")
        if sha256_file(path) != validate_sha(meta.get("sha256"), f"contracts.{key}.sha256"):
            raise ValueError(f"{key} contract bytes do not match package digest")
        json.loads(path.read_text(encoding="utf-8"))

    tasks_meta = package.get("evidence_tasks")
    if not isinstance(tasks_meta, dict):
        raise ValueError("Evidence package evidence_tasks metadata is missing")
    task_manifest = require_file(package_root, tasks_meta.get("manifest_path"), "Evidence Task manifest")
    task_index = require_file(package_root, tasks_meta.get("index_path"), "Evidence Task index")
    if sha256_file(task_manifest) != validate_sha(tasks_meta.get("manifest_sha256"), "evidence_tasks.manifest_sha256"):
        raise ValueError("Evidence Task manifest bytes do not match package digest")
    if sha256_file(task_index) != validate_sha(tasks_meta.get("index_sha256"), "evidence_tasks.index_sha256"):
        raise ValueError("Evidence Task index bytes do not match package digest")
    json.loads(task_manifest.read_text(encoding="utf-8"))
    task_count = tasks_meta.get("task_count")
    if not isinstance(task_count, int) or task_count <= 0:
        raise ValueError("Evidence package task_count must be positive")
    if count_jsonl(task_index) != task_count:
        raise ValueError("Evidence Task index count does not match package task_count")

    task_entries = tasks_meta.get("tasks")
    if not isinstance(task_entries, list) or len(task_entries) != task_count:
        raise ValueError("Evidence package task list does not match task_count")
    seen_ids: set[str] = set()
    seen_names: set[str] = set()
    tasks: list[dict[str, Any]] = []
    for entry in task_entries:
        if not isinstance(entry, dict):
            raise ValueError("Evidence package task entries must be objects")
        task_id = entry.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id or task_id in seen_ids:
            raise ValueError(f"invalid or duplicate evidence_task_id: {task_id!r}")
        seen_ids.add(task_id)
        task_path = require_file(package_root, entry.get("path"), f"Evidence Task {task_id}")
        if task_path.name in seen_names:
            raise ValueError(f"duplicate Evidence Task filename: {task_path.name}")
        seen_names.add(task_path.name)
        expected_sha = validate_sha(entry.get("sha256"), f"Evidence Task {task_id} sha256")
        if sha256_file(task_path) != expected_sha:
            raise ValueError(f"Evidence Task bytes do not match package digest: {task_id}")
        if task_path.stat().st_size != entry.get("bytes"):
            raise ValueError(f"Evidence Task byte count mismatch: {task_id}")
        task = load_json(task_path)
        if task.get("issue_id") != issue_id or task.get("evidence_task_id") != task_id:
            raise ValueError(f"Evidence Task identity mismatch: {task_id}")
        tasks.append({**entry, "_path": task_path, "_filename": task_path.name})
    return package, tasks


def validate_repo_basis(package: dict[str, Any], repo_root: Path, issue_id: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if not state_path.is_file():
        raise ValueError("weekly pipeline-state.json is missing before Evidence acceptance")
    if sha256_file(state_path) != package["source"]["pipeline_state_sha256"]:
        raise ValueError("weekly pipeline-state bytes no longer match the Evidence package basis")
    state = load_json(state_path)
    if state.get("issue_id") != issue_id:
        raise ValueError("weekly pipeline state issue_id mismatch")

    screening = package["screening_basis"]
    acceptance_path = repo_root / screening["acceptance_path"]
    queue_path = repo_root / screening["verification_queue_path"]
    if not acceptance_path.is_file() or not queue_path.is_file():
        raise ValueError("accepted screening basis files are missing from the weekly work tree")
    if sha256_file(acceptance_path) != screening["acceptance_sha256"]:
        raise ValueError("screening acceptance bytes no longer match the Evidence package basis")
    if sha256_file(queue_path) != screening["verification_queue_sha256"]:
        raise ValueError("screening verification queue bytes no longer match the Evidence package basis")
    acceptance = load_json(acceptance_path)
    if acceptance.get("issue_id") != issue_id or acceptance.get("status") != "ACCEPTED":
        raise ValueError("screening acceptance identity/status mismatch")
    if acceptance.get("result_set_sha256") != screening["result_set_sha256"]:
        raise ValueError("screening acceptance result-set SHA mismatch")
    return state


def result_set_digest(records: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for record in sorted(records, key=lambda value: value["evidence_task_id"]):
        digest.update(record["evidence_task_id"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(record["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def acceptance_dir(repo_root: Path, issue_id: str, result_set_sha256: str) -> Path:
    return repo_root / "sources" / issue_id / "evidence" / "runs" / result_set_sha256


def transition_state(state: dict[str, Any]) -> dict[str, Any]:
    if state.get("lifecycle_state") != ALLOWED_LIFECYCLE:
        raise ValueError(
            f"new Evidence results may be accepted only in {ALLOWED_LIFECYCLE}; "
            f"current lifecycle_state={state.get('lifecycle_state')!r}"
        )
    gates = state.get("gates")
    if not isinstance(gates, dict):
        raise ValueError("weekly pipeline gates are missing")
    if gates.get("candidate_inventory") != "passed":
        raise ValueError("Evidence acceptance requires candidate_inventory=passed")
    if gates.get("evidence_normalized") != "pending":
        raise ValueError("Evidence acceptance requires evidence_normalized=pending")
    updated = deepcopy(state)
    updated["lifecycle_state"] = TARGET_LIFECYCLE
    updated["gates"]["evidence_normalized"] = "passed"
    return updated


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
        raise ValueError(f"Evidence results directory missing: {results_dir}")

    package, tasks = validate_package_files(package_root, issue_id)
    entries = list(results_dir.iterdir())
    if any(path.is_symlink() for path in entries):
        raise ValueError("symlinks are forbidden in Evidence results")
    non_files = sorted(path.name for path in entries if not path.is_file())
    if non_files:
        raise ValueError(f"Evidence results directory may contain files only: {non_files}")
    expected_names = {task["_filename"] for task in tasks}
    actual_names = {path.name for path in entries}
    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    if missing or extra:
        raise ValueError(f"Evidence result set must be complete and exact: missing={missing} extra={extra}")

    prompt_path = package_root / package["prompt"]["path"]
    result_records: list[dict[str, Any]] = []
    validation_reports: dict[str, dict[str, Any]] = {}
    for task in tasks:
        task_id = task["evidence_task_id"]
        result_path = results_dir / task["_filename"]
        report, passed = validate_evidence_run.validate(task["_path"], result_path, prompt_path)
        if not passed:
            raise ValueError(f"Evidence Run validation failed for {task_id}: {report.get('errors', [])}")
        run = load_json(result_path)
        validation_reports[task_id] = report
        result_records.append(
            {
                "evidence_task_id": task_id,
                "filename": task["_filename"],
                "sha256": sha256_file(result_path),
                "bytes": result_path.stat().st_size,
                "runner": run["runner"],
                "recommendation": run["card"]["editorial"]["candidate_recommendation"],
                "card_status": run["card"]["status"],
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
        "evidence_package": {
            "source_ref": package["source"]["ref"],
            "source_commit_sha": package["source"]["commit_sha"],
            "package_manifest_sha256": sha256_file(package_root / "evidence-execution-package.json"),
            "pipeline_state_sha256": package["source"]["pipeline_state_sha256"],
            "screening_result_set_sha256": package["screening_basis"]["result_set_sha256"],
            "screening_acceptance_sha256": package["screening_basis"]["acceptance_sha256"],
            "verification_queue_sha256": package["screening_basis"]["verification_queue_sha256"],
            "prompt_sha256": package["prompt"]["sha256"],
            "task_manifest_sha256": package["evidence_tasks"]["manifest_sha256"],
            "task_index_sha256": package["evidence_tasks"]["index_sha256"],
        },
        "results": sorted(result_records, key=lambda value: value["evidence_task_id"]),
        "state_transition": {
            "from": ALLOWED_LIFECYCLE,
            "to": TARGET_LIFECYCLE,
            "gate": "evidence_normalized",
            "gate_value": "passed",
        },
        "rules": [
            "Only a complete one-result-per-task Evidence set is accepted into the weekly work tree.",
            "Every Evidence Run is revalidated against the exact package task and prompt bytes before persistence.",
            "Accepted Evidence result bytes are append-only and addressed by a deterministic result-set SHA-256.",
            "Evidence acceptance advances evidence_normalized only; Candidate Selection remains an explicit later human gate.",
        ],
    }

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if manifest_path.exists():
        existing = load_json(manifest_path)
        if existing != acceptance:
            raise ValueError(f"Evidence acceptance path exists with different manifest: {manifest_path}")
        if not state_path.is_file():
            raise ValueError("accepted Evidence set exists but pipeline-state.json is missing")
        current = load_json(state_path)
        recovered = False
        if current.get("lifecycle_state") == ALLOWED_LIFECYCLE:
            # Recover the only safe interrupted transaction shape: artifacts were
            # committed/written but the coarse state transition was not.
            if sha256_file(state_path) != package["source"]["pipeline_state_sha256"]:
                raise ValueError("accepted Evidence set exists but current candidate-normalized state no longer matches package basis")
            updated = transition_state(current)
            state_path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            recovered = True
        return {
            "schema_version": "1.0",
            "passed": True,
            "issue_id": issue_id,
            "status": "ALREADY_ACCEPTED",
            "result_set_sha256": set_sha,
            "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
            "state_transition_recovered": recovered,
        }, True

    state = validate_repo_basis(package, repo_root, issue_id)
    updated_state = transition_state(state)

    with tempfile.TemporaryDirectory() as tmp:
        derived = Path(tmp) / "derived"
        merge_manifest, merged = merge_evidence_runs.merge(
            package_root / "input" / "tasks",
            results_dir,
            prompt_path,
            derived,
            require_complete=True,
        )
        if not merged or not merge_manifest.get("complete"):
            raise ValueError(f"complete Evidence merge failed: {merge_manifest}")

        destination.mkdir(parents=True, exist_ok=False)
        (destination / "results").mkdir()
        for record in result_records:
            source = results_dir / record["filename"]
            target = destination / "results" / record["filename"]
            shutil.copyfile(source, target)
            if sha256_file(target) != record["sha256"]:
                raise RuntimeError(f"Evidence result copy verification failed: {target}")

        shutil.copyfile(package_root / "evidence-execution-package.json", destination / "evidence-execution-package.json")
        for name in (
            "evidence-reviewed.jsonl",
            "candidate-ready.jsonl",
            "evidence-hold.jsonl",
            "evidence-rejected.jsonl",
            "evidence-progress.json",
        ):
            shutil.copyfile(derived / name, destination / name)
        validations = destination / "validation"
        validations.mkdir()
        for task_id, report in sorted(validation_reports.items()):
            safe_name = hashlib.sha256(task_id.encode("utf-8")).hexdigest()[:16]
            (validations / f"{safe_name}.json").write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        manifest_path.write_text(json.dumps(acceptance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    state_path.write_text(json.dumps(updated_state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "schema_version": "1.0",
        "passed": True,
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "result_set_sha256": set_sha,
        "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "evidence_task_count": merge_manifest["evidence_task_count"],
        "candidate_ready_count": merge_manifest["candidate_ready_count"],
        "hold_count": merge_manifest["hold_count"],
        "rejected_count": merge_manifest["rejected_count"],
        "lifecycle_state": TARGET_LIFECYCLE,
        "evidence_normalized_gate": "passed",
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
