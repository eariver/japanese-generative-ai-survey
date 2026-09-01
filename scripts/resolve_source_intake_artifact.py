#!/usr/bin/env python3
"""Verify the exact GitHub Actions source-intake run and artifact selected for import."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ISSUE_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
EXPECTED_WORKFLOW_PATH = ".github/workflows/weekly-pipeline.yml"
EXPECTED_EVENT = "workflow_dispatch"
EXPECTED_HEAD_BRANCH = "main"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def _repo_full_name(value: Any) -> str | None:
    if not isinstance(value, dict):
        return None
    full_name = value.get("full_name")
    return full_name if isinstance(full_name, str) and full_name else None


def resolve(
    *,
    run: dict[str, Any],
    artifacts: dict[str, Any],
    repository: str,
    issue_id: str,
    source_run_id: int,
) -> dict[str, Any]:
    if not ISSUE_RE.fullmatch(issue_id):
        raise ValueError("issue_id must use YYYY-Www form")
    if source_run_id <= 0:
        raise ValueError("source_run_id must be a positive integer")
    if not repository or "/" not in repository:
        raise ValueError("repository must use owner/name form")

    if run.get("id") != source_run_id:
        raise ValueError("source Actions run id mismatch")
    if run.get("status") != "completed" or run.get("conclusion") != "success":
        raise ValueError(
            f"source Actions run must be completed successfully; "
            f"status={run.get('status')!r} conclusion={run.get('conclusion')!r}"
        )
    if _repo_full_name(run.get("repository")) != repository:
        raise ValueError("source Actions run repository mismatch")
    if _repo_full_name(run.get("head_repository")) != repository:
        raise ValueError("source Actions run head_repository mismatch")
    if run.get("path") != EXPECTED_WORKFLOW_PATH:
        raise ValueError(f"source Actions run must come from {EXPECTED_WORKFLOW_PATH}")
    if run.get("event") != EXPECTED_EVENT:
        raise ValueError(f"source Actions run event must be {EXPECTED_EVENT}")
    if run.get("head_branch") != EXPECTED_HEAD_BRANCH:
        raise ValueError(f"source Actions run head_branch must be {EXPECTED_HEAD_BRANCH}")
    head_sha = run.get("head_sha")
    if not isinstance(head_sha, str) or not GIT_SHA_RE.fullmatch(head_sha):
        raise ValueError("source Actions run head_sha is missing or invalid")

    values = artifacts.get("artifacts")
    if not isinstance(values, list):
        raise ValueError("artifacts response must contain an artifacts array")
    expected_name = f"weekly-source-intake-{issue_id}"
    matches = [value for value in values if isinstance(value, dict) and value.get("name") == expected_name]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one artifact named {expected_name}, found {len(matches)}")
    artifact = matches[0]

    artifact_id = artifact.get("id")
    if not isinstance(artifact_id, int) or artifact_id <= 0:
        raise ValueError("source artifact id is missing or invalid")
    if artifact.get("expired") is not False:
        raise ValueError("source artifact is expired")
    digest = artifact.get("digest")
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        raise ValueError(f"source artifact digest is missing or invalid: {digest!r}")
    artifact_run = artifact.get("workflow_run")
    artifact_run_id = artifact_run.get("id") if isinstance(artifact_run, dict) else None
    if artifact_run_id != source_run_id:
        raise ValueError("source artifact workflow_run id mismatch")

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "VERIFIED",
        "source_actions": {
            "workflow_run_id": source_run_id,
            "workflow_path": EXPECTED_WORKFLOW_PATH,
            "event": EXPECTED_EVENT,
            "head_branch": EXPECTED_HEAD_BRANCH,
            "head_sha": head_sha,
            "html_url": run.get("html_url"),
        },
        "artifact": {
            "id": artifact_id,
            "name": expected_name,
            "digest": digest,
            "expired": False,
            "archive_download_url": artifact.get("archive_download_url"),
        },
    }


def write_github_output(path: Path, result: dict[str, Any]) -> None:
    artifact = result["artifact"]
    source_actions = result["source_actions"]
    with path.open("a", encoding="utf-8") as fh:
        fh.write(f"artifact_name={artifact['name']}\n")
        fh.write(f"artifact_id={artifact['id']}\n")
        fh.write(f"artifact_digest={artifact['digest']}\n")
        fh.write(f"source_head_sha={source_actions['head_sha']}\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-json", required=True)
    parser.add_argument("--artifacts-json", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-run-id", required=True, type=int)
    parser.add_argument("--output", required=True)
    parser.add_argument("--github-output")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = resolve(
        run=load_json(Path(args.run_json)),
        artifacts=load_json(Path(args.artifacts_json)),
        repository=args.repository,
        issue_id=args.issue_id,
        source_run_id=args.source_run_id,
    )
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.github_output:
        write_github_output(Path(args.github_output), result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
