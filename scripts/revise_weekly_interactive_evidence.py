#!/usr/bin/env python3
"""Create an append-only pre-selection revision of accepted Weekly Evidence.

This is the Weekly counterpart of ``revise_special_interactive_evidence.py``.
It reuses the exact package bytes and CANDIDATES_NORMALIZED state that backed the
prior accepted Evidence run, expands the current compact Weekly review into one
complete result per Evidence Task, validates the new set, and stores it under a
new result-set SHA. The current coarse pipeline state remains EVIDENCE_REVIEWED
and Candidate Selection must still be pending.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path
from typing import Any

from scripts import accept_evidence_results, validate_evidence_run
from scripts import run_special_interactive_evidence as shared
from scripts import run_weekly_interactive_evidence as weekly

WEEKLY_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_current_state(repo_root: Path, issue_id: str) -> tuple[Path, dict[str, Any], bytes]:
    path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if not path.is_file():
        raise ValueError("current Weekly pipeline-state.json is missing")
    raw = path.read_bytes()
    state = json.loads(raw.decode("utf-8"))
    if state.get("issue_id") != issue_id:
        raise ValueError("current Weekly pipeline state issue mismatch")
    if state.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("Evidence revision is allowed only from EVIDENCE_REVIEWED")
    gates = state.get("gates") or {}
    if gates.get("candidate_inventory") != "passed" or gates.get("evidence_normalized") != "passed":
        raise ValueError("Evidence revision requires candidate_inventory/evidence_normalized passed")
    if gates.get("candidate_selection") != "pending":
        raise ValueError("Evidence revision is forbidden after Candidate Selection")
    if gates.get("issue_architecture") != "pending":
        raise ValueError("Evidence revision is forbidden after Issue Architecture work begins")
    return path, state, raw


def validate_prior_run(repo_root: Path, issue_id: str, prior_sha: str, package_root: Path) -> dict[str, Any]:
    if not SHA256_RE.fullmatch(prior_sha):
        raise ValueError("prior_evidence_run_sha must be a lowercase SHA-256 digest")
    run_dir = repo_root / "sources" / issue_id / "evidence" / "runs" / prior_sha
    acceptance_path = run_dir / "acceptance.json"
    if not acceptance_path.is_file():
        raise ValueError("prior accepted Evidence run is missing")
    acceptance = load_json(acceptance_path)
    if acceptance.get("status") != "ACCEPTED" or acceptance.get("result_set_sha256") != prior_sha:
        raise ValueError("prior Evidence run is not an accepted result set")
    package_path = package_root / "evidence-execution-package.json"
    if not package_path.is_file():
        raise ValueError("rebuilt prior Evidence package is missing")
    expected_package_sha = (acceptance.get("evidence_package") or {}).get("package_manifest_sha256")
    if sha256_file(package_path) != expected_package_sha:
        raise ValueError("rebuilt Evidence package bytes do not match the prior accepted package")
    return acceptance


def load_review(review_path: Path, issue_id: str, screening_run_sha: str) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    doc = load_json(review_path)
    overrides = weekly.validate_review(doc, issue_id, screening_run_sha)
    return doc["runner"], overrides


def run(
    *,
    repo_root: Path,
    issue_id: str,
    prior_evidence_run_sha: str,
    package_root: Path,
    basis_state_path: Path,
    review_path: Path,
    review_reference: str,
    audit_output: Path | None = None,
) -> dict[str, Any]:
    if not WEEKLY_RE.fullmatch(issue_id):
        raise ValueError("Weekly Evidence revision requires YYYY-Www issue_id")
    if not review_reference.strip():
        raise ValueError("review_reference is required")
    repo_root = repo_root.resolve()
    package_root = package_root.resolve()
    basis_state_path = basis_state_path.resolve()
    review_path = review_path.resolve()

    state_path, current_state, current_state_bytes = validate_current_state(repo_root, issue_id)
    prior = validate_prior_run(repo_root, issue_id, prior_evidence_run_sha, package_root)
    package = load_json(package_root / "evidence-execution-package.json")
    if package.get("issue_id") != issue_id:
        raise ValueError("rebuilt package issue mismatch")
    screening_run_sha = (package.get("screening_basis") or {}).get("result_set_sha256")
    if not isinstance(screening_run_sha, str) or not SHA256_RE.fullmatch(screening_run_sha):
        raise ValueError("rebuilt package screening basis is invalid")
    if (prior.get("evidence_package") or {}).get("screening_result_set_sha256") != screening_run_sha:
        raise ValueError("prior Evidence run and rebuilt package use different Screening results")

    if not basis_state_path.is_file():
        raise ValueError("basis pipeline state is missing")
    basis_state_bytes = basis_state_path.read_bytes()
    if hashlib.sha256(basis_state_bytes).hexdigest() != (prior.get("evidence_package") or {}).get("pipeline_state_sha256"):
        raise ValueError("basis pipeline state bytes do not match prior Evidence acceptance")
    basis_state = json.loads(basis_state_bytes.decode("utf-8"))
    if basis_state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("prior Evidence package basis must be CANDIDATES_NORMALIZED")

    runner, overrides = load_review(review_path, issue_id, screening_run_sha)
    expected = {task["evidence_task_id"]: task for task in package["evidence_tasks"]["tasks"]}
    extra = sorted(set(overrides) - set(expected))
    if extra:
        raise ValueError(f"review contains unknown Evidence Tasks: {extra}")
    queue = weekly.load_verification_queue(repo_root, package)

    recommendation_counts = {key: 0 for key in sorted(weekly.RECOMMENDATIONS)}
    status_counts = {key: 0 for key in sorted(weekly.CARD_STATUSES)}
    overridden_count = 0
    with tempfile.TemporaryDirectory() as tmp:
        results = Path(tmp) / "results"
        results.mkdir()
        for task_id, meta in expected.items():
            task_path = package_root / meta["path"]
            task = load_json(task_path)
            entry = weekly.default_entry(task, queue, issue_id)
            if task_id in overrides:
                entry = weekly.merge_entry(entry, overrides[task_id])
                overridden_count += 1
            shared.validate_override(entry)
            card = shared.build_card(task, entry, issue_id, runner["generated_at"])
            recommendation_counts[card["editorial"]["candidate_recommendation"]] += 1
            status_counts[card["status"]] += 1
            result = {
                "schema_version": "1.0",
                "issue_id": issue_id,
                "evidence_task_id": task_id,
                "evidence_task_sha256": weekly.sha(task_path),
                "prompt_id": package["prompt"]["prompt_id"],
                "prompt_sha256": package["prompt"]["sha256"],
                "runner": runner,
                "card": card,
            }
            result_path = results / task_path.name
            result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            validation, passed = validate_evidence_run.validate(
                task_path,
                result_path,
                package_root / package["prompt"]["path"],
            )
            if not passed:
                raise ValueError(f"Evidence revision validation failed for {task_id}: {validation.get('errors', [])}")

        state_path.write_bytes(basis_state_bytes)
        try:
            report, passed = accept_evidence_results.accept(
                package_root=package_root,
                results_dir=results,
                repo_root=repo_root,
                issue_id=issue_id,
                review_reference=review_reference,
            )
            if not passed:
                raise ValueError(f"Evidence revision acceptance failed: {report}")
            after_state = load_json(state_path)
            if after_state != current_state:
                raise ValueError("Evidence revision changed coarse pipeline state unexpectedly")
        finally:
            state_path.write_bytes(current_state_bytes)

    new_sha = report["result_set_sha256"]
    if new_sha == prior_evidence_run_sha:
        raise ValueError("Evidence revision produced identical result-set SHA; no revision is necessary")
    new_run_dir = repo_root / "sources" / issue_id / "evidence" / "runs" / new_sha
    supersession = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "PRE_SELECTION_EVIDENCE_REVISION",
        "supersedes_result_set_sha256": prior_evidence_run_sha,
        "result_set_sha256": new_sha,
        "review_reference": review_reference.strip(),
        "basis_package_sha256": sha256_file(package_root / "evidence-execution-package.json"),
        "pipeline_state_unchanged": True,
        "candidate_selection_gate": "pending",
    }
    (new_run_dir / "supersession.json").write_text(json.dumps(supersession, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = dict(report)
    result.update({
        "status": "ACCEPTED_REVISION",
        "supersedes_result_set_sha256": prior_evidence_run_sha,
        "supersession_manifest": (new_run_dir / "supersession.json").relative_to(repo_root).as_posix(),
        "pipeline_state_unchanged": True,
        "interactive_review_path": review_path.relative_to(repo_root).as_posix(),
        "override_count": overridden_count,
        "defaulted_count": len(expected) - overridden_count,
        "runner": runner,
        "recommendation_counts": recommendation_counts,
        "card_status_counts": status_counts,
    })
    if audit_output:
        audit_output.parent.mkdir(parents=True, exist_ok=True)
        audit_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--prior-evidence-run-sha", required=True)
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--basis-state", required=True)
    parser.add_argument("--review", required=True)
    parser.add_argument("--review-reference", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    result = run(
        repo_root=Path(args.repo_root),
        issue_id=args.issue_id,
        prior_evidence_run_sha=args.prior_evidence_run_sha,
        package_root=Path(args.package_root),
        basis_state_path=Path(args.basis_state),
        review_path=Path(args.review),
        review_reference=args.review_reference,
        audit_output=Path(args.audit_output) if args.audit_output else None,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
