#!/usr/bin/env python3
"""Build a deterministic Evidence execution package from accepted screening.

The package pins one accepted screening result set, its verification queue, the
current candidate-normalized pipeline state, every deterministic Evidence Task,
and the exact primary-source verification prompt/result contracts. It performs
no network verification or inference and writes nothing to the source tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from scripts import build_evidence_tasks

ISSUE_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
PROMPT_ID = "primary-source-verification-v0.1"
PROMPT_RELATIVE = Path("config/prompts/evidence/primary-source-verification-v0.1.md")
RUN_SCHEMA_RELATIVE = Path("schemas/evidence-run.schema.json")
CARD_SCHEMA_RELATIVE = Path("schemas/evidence-card.schema.json")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def copy_verified(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    if source.stat().st_size != destination.stat().st_size or sha256_file(source) != sha256_file(destination):
        raise RuntimeError(f"copy verification failed: {destination}")


def validate_screening_run(repo_root: Path, issue_id: str, screening_run_sha: str) -> tuple[Path, dict[str, Any], Path]:
    if not SHA256_RE.fullmatch(screening_run_sha):
        raise ValueError("screening_run_sha must be a lowercase SHA-256 hex digest")
    run_dir = repo_root / "sources" / issue_id / "screening" / "runs" / screening_run_sha
    acceptance_path = run_dir / "acceptance.json"
    queue_path = run_dir / "verification-queue.jsonl"
    if not acceptance_path.is_file():
        raise ValueError(f"accepted screening manifest missing: {acceptance_path}")
    if not queue_path.is_file():
        raise ValueError(f"accepted screening verification queue missing: {queue_path}")
    acceptance = load_json(acceptance_path)
    if acceptance.get("schema_version") != "1.0" or acceptance.get("status") != "ACCEPTED":
        raise ValueError("screening acceptance manifest is not ACCEPTED schema 1.0")
    if acceptance.get("issue_id") != issue_id:
        raise ValueError("screening acceptance issue_id mismatch")
    if acceptance.get("result_set_sha256") != screening_run_sha:
        raise ValueError("screening acceptance result_set_sha256 mismatch")
    return acceptance_path, acceptance, queue_path


def build_package(
    *,
    repo_root: Path,
    output_root: Path,
    issue_id: str,
    screening_run_sha: str,
    source_ref: str,
    source_commit: str,
) -> dict[str, Any]:
    if not ISSUE_RE.fullmatch(issue_id):
        raise ValueError("issue_id must use YYYY-Www form")
    if not source_ref.strip():
        raise ValueError("source_ref must be non-empty")
    if not GIT_SHA_RE.fullmatch(source_commit):
        raise ValueError("source_commit must be a 40-character lowercase Git SHA")

    repo_root = repo_root.resolve()
    output_root = output_root.resolve()
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if not state_path.is_file():
        raise ValueError(f"pipeline state missing: {state_path}")
    state = load_json(state_path)
    if state.get("issue_id") != issue_id:
        raise ValueError("pipeline state issue_id mismatch")
    if state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError(
            "Evidence package requires lifecycle_state=CANDIDATES_NORMALIZED; "
            f"got {state.get('lifecycle_state')!r}"
        )
    gates = state.get("gates")
    if not isinstance(gates, dict) or gates.get("candidate_inventory") != "passed":
        raise ValueError("Evidence package requires candidate_inventory gate=passed")
    if gates.get("evidence_normalized") != "pending":
        raise ValueError("Evidence package requires evidence_normalized gate=pending")

    acceptance_path, _acceptance, queue_path = validate_screening_run(repo_root, issue_id, screening_run_sha)
    retained_count = sum(1 for line in queue_path.read_text(encoding="utf-8").splitlines() if line.strip())
    if retained_count == 0:
        raise ValueError("accepted screening verification queue is empty; zero-Evidence issue handling requires an explicit no-task path")

    prompt_path = repo_root / PROMPT_RELATIVE
    run_schema_path = repo_root / RUN_SCHEMA_RELATIVE
    card_schema_path = repo_root / CARD_SCHEMA_RELATIVE
    for path, label in (
        (prompt_path, "Evidence prompt"),
        (run_schema_path, "Evidence Run schema"),
        (card_schema_path, "Evidence Card schema"),
    ):
        if not path.is_file():
            raise ValueError(f"required {label} missing: {path}")

    input_root = output_root / "input"
    task_build_root = output_root / "task-build"
    task_manifest, passed = build_evidence_tasks.build(queue_path, task_build_root)
    if not passed:
        raise ValueError(f"Evidence Task build failed: {task_manifest}")
    if task_manifest.get("issue_id") != issue_id:
        raise ValueError("Evidence Task manifest issue_id mismatch")
    task_count = task_manifest.get("evidence_task_count")
    if not isinstance(task_count, int) or task_count <= 0:
        raise ValueError("Evidence Task build produced no tasks")

    # Flatten deterministic builder outputs into stable package names.
    input_root.mkdir(parents=True, exist_ok=True)
    copy_verified(task_build_root / "evidence-task-manifest.json", input_root / "evidence-task-manifest.json")
    copy_verified(task_build_root / "evidence-tasks.jsonl", input_root / "evidence-task-index.jsonl")
    tasks_dir = input_root / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    task_records: list[dict[str, Any]] = []
    for entry in task_manifest.get("task_files", []):
        if not isinstance(entry, dict):
            raise ValueError("Evidence Task manifest task_files entries must be objects")
        task_id = entry.get("evidence_task_id")
        relative = entry.get("path")
        if not isinstance(task_id, str) or not task_id or not isinstance(relative, str) or not relative:
            raise ValueError(f"invalid Evidence Task manifest entry: {entry}")
        task_source = task_build_root / relative
        if not task_source.is_file():
            raise ValueError(f"Evidence Task file missing: {task_source}")
        if sha256_file(task_source) != entry.get("sha256") or task_source.stat().st_size != entry.get("bytes"):
            raise ValueError(f"Evidence Task bytes disagree with builder manifest: {task_id}")
        task = load_json(task_source)
        if task.get("evidence_task_id") != task_id or task.get("issue_id") != issue_id:
            raise ValueError(f"Evidence Task identity mismatch: {task_source}")
        target = tasks_dir / task_source.name
        copy_verified(task_source, target)
        task_records.append(
            {
                "evidence_task_id": task_id,
                "path": f"input/tasks/{target.name}",
                "sha256": sha256_file(target),
                "bytes": target.stat().st_size,
            }
        )
    if len(task_records) != task_count:
        raise ValueError("Evidence Task file count does not match task manifest")
    shutil.rmtree(task_build_root)

    contract_root = output_root / "contract"
    prompt_copy = contract_root / "primary-source-verification-v0.1.md"
    run_schema_copy = contract_root / "evidence-run.schema.json"
    card_schema_copy = contract_root / "evidence-card.schema.json"
    copy_verified(prompt_path, prompt_copy)
    copy_verified(run_schema_path, run_schema_copy)
    copy_verified(card_schema_path, card_schema_copy)

    package = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source": {
            "ref": source_ref.strip(),
            "commit_sha": source_commit,
            "pipeline_state_sha256": sha256_file(state_path),
        },
        "screening_basis": {
            "result_set_sha256": screening_run_sha,
            "acceptance_path": acceptance_path.relative_to(repo_root).as_posix(),
            "acceptance_sha256": sha256_file(acceptance_path),
            "verification_queue_path": queue_path.relative_to(repo_root).as_posix(),
            "verification_queue_sha256": sha256_file(queue_path),
        },
        "prompt": {
            "prompt_id": PROMPT_ID,
            "path": "contract/primary-source-verification-v0.1.md",
            "sha256": sha256_file(prompt_copy),
        },
        "contracts": {
            "evidence_run": {
                "path": "contract/evidence-run.schema.json",
                "sha256": sha256_file(run_schema_copy),
            },
            "evidence_card": {
                "path": "contract/evidence-card.schema.json",
                "sha256": sha256_file(card_schema_copy),
            },
        },
        "evidence_tasks": {
            "manifest_path": "input/evidence-task-manifest.json",
            "manifest_sha256": sha256_file(input_root / "evidence-task-manifest.json"),
            "index_path": "input/evidence-task-index.jsonl",
            "index_sha256": sha256_file(input_root / "evidence-task-index.jsonl"),
            "task_count": task_count,
            "tasks": sorted(task_records, key=lambda value: value["evidence_task_id"]),
        },
        "expected_outputs": {
            "one_result_per_task": True,
            "schema_version": "1.0",
            "naming": "results/<input task filename>",
        },
        "rules": [
            "Run primary-source verification independently for every supplied Evidence Task using the pinned prompt bytes.",
            "Each Evidence Run must preserve the exact evidence_task_sha256 and prompt_sha256 required by the Evidence Run contract.",
            "Evidence recommendations are CANDIDATE/HOLD/INSPECT_MORE/REJECT inputs to later comparison; they are not Candidate Selection decisions.",
            "A later acceptance step must revalidate every Evidence Run against these exact task/prompt bytes before persistence.",
            "The package is read-only and must not modify accepted screening or source Raw bytes.",
        ],
    }
    package_path = output_root / "evidence-execution-package.json"
    package_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return package


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--screening-run-sha", required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--source-commit", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    package = build_package(
        repo_root=Path(args.repo_root),
        output_root=Path(args.output_root),
        issue_id=args.issue_id,
        screening_run_sha=args.screening_run_sha,
        source_ref=args.source_ref,
        source_commit=args.source_commit,
    )
    print(json.dumps(package, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
