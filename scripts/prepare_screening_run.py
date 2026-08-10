#!/usr/bin/env python3
"""Build a deterministic screening package from accepted weekly collector data.

The package is read-only input for an LLM/tool runner. It pins the repository
commit, Raw provenance index, prompt bytes, result schema, screening index, and
every batch SHA-256. It performs no inference and writes nothing to the source
tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from scripts import build_screening_index

ISSUE_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
PROMPT_ID = "source-screening-v0.1"
PROMPT_RELATIVE = Path("config/prompts/screening/source-screening-v0.1.md")
RESULT_SCHEMA_RELATIVE = Path("schemas/screening-batch-result.schema.json")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_verified(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    if source.stat().st_size != destination.stat().st_size or sha256_file(source) != sha256_file(destination):
        raise RuntimeError(f"copy verification failed: {destination}")


def build_package(
    *,
    repo_root: Path,
    output_root: Path,
    issue_id: str,
    source_ref: str,
    source_commit: str,
    max_records: int = 40,
    max_json_chars: int = 80000,
) -> dict[str, Any]:
    if not ISSUE_RE.fullmatch(issue_id):
        raise ValueError("issue_id must use YYYY-Www form")
    if not source_ref.strip():
        raise ValueError("source_ref must be non-empty")
    if not GIT_SHA_RE.fullmatch(source_commit):
        raise ValueError("source_commit must be a 40-character lowercase Git SHA")
    if max_records <= 0 or max_json_chars <= 0:
        raise ValueError("batch policy values must be positive")

    repo_root = repo_root.resolve()
    output_root = output_root.resolve()
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    raw_index_path = repo_root / "sources" / issue_id / "raw-index.json"
    collectors_path = repo_root / "sources" / issue_id / "collectors"
    prompt_path = repo_root / PROMPT_RELATIVE
    result_schema_path = repo_root / RESULT_SCHEMA_RELATIVE

    for path, label in (
        (state_path, "pipeline-state.json"),
        (raw_index_path, "raw-index.json"),
        (prompt_path, "screening prompt"),
        (result_schema_path, "screening result schema"),
    ):
        if not path.is_file():
            raise ValueError(f"required {label} missing: {path}")
    if not collectors_path.is_dir():
        raise ValueError(f"accepted collector tree missing: {collectors_path}")

    state = load_json(state_path)
    if not isinstance(state, dict) or state.get("issue_id") != issue_id:
        raise ValueError("pipeline state issue_id mismatch")
    raw_index = load_json(raw_index_path)
    if not isinstance(raw_index, dict) or raw_index.get("issue_id") != issue_id:
        raise ValueError("raw index issue_id mismatch")

    input_dir = output_root / "input"
    screening_manifest = build_screening_index.build(
        repo_root,
        input_dir,
        issue_id,
        max_records=max_records,
        max_chars=max_json_chars,
    )
    if screening_manifest.get("record_count", 0) <= 0 or screening_manifest.get("batch_count", 0) <= 0:
        raise ValueError("screening normalization produced no records/batches")

    contract_dir = output_root / "contract"
    prompt_copy = contract_dir / "source-screening-v0.1.md"
    schema_copy = contract_dir / "screening-batch-result.schema.json"
    copy_verified(prompt_path, prompt_copy)
    copy_verified(result_schema_path, schema_copy)

    manifest_path = input_dir / "screening-manifest.json"
    index_path = input_dir / "screening-index.jsonl"
    batches: list[dict[str, Any]] = []
    for item in screening_manifest["batches"]:
        batch_path = input_dir / item["path"]
        if not batch_path.is_file():
            raise ValueError(f"screening batch missing after generation: {batch_path}")
        batch_id = batch_path.stem
        batches.append(
            {
                "batch_id": batch_id,
                "path": f"input/{item['path']}",
                "record_count": item["record_count"],
                "sha256": sha256_file(batch_path),
                "bytes": batch_path.stat().st_size,
            }
        )

    package = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source": {
            "ref": source_ref.strip(),
            "commit_sha": source_commit,
        },
        "provenance": {
            "pipeline_state_sha256": sha256_file(state_path),
            "raw_index_sha256": sha256_file(raw_index_path),
        },
        "prompt": {
            "prompt_id": PROMPT_ID,
            "path": "contract/source-screening-v0.1.md",
            "sha256": sha256_file(prompt_copy),
        },
        "result_contract": {
            "path": "contract/screening-batch-result.schema.json",
            "sha256": sha256_file(schema_copy),
        },
        "screening_input": {
            "manifest_path": "input/screening-manifest.json",
            "manifest_sha256": sha256_file(manifest_path),
            "index_path": "input/screening-index.jsonl",
            "index_sha256": sha256_file(index_path),
            "record_count": screening_manifest["record_count"],
            "batch_policy": screening_manifest["batch_policy"],
            "batches": batches,
        },
        "expected_outputs": {
            "file_pattern": "results/batch-###.json",
            "one_result_per_batch": True,
            "schema_version": "1.0",
        },
        "rules": [
            "Run screening independently for each supplied batch using the pinned prompt bytes.",
            "Each result must preserve the exact input_batch_sha256 and prompt_sha256 required by the screening result contract.",
            "Screening is triage, not factual verification; retained items still require the Evidence stage.",
            "Do not modify source collector Raw bytes or the generated screening inputs.",
            "A later acceptance step must regenerate these inputs from the recorded source commit and revalidate every result before persistence.",
        ],
    }
    package_path = output_root / "screening-run-package.json"
    package_path.parent.mkdir(parents=True, exist_ok=True)
    package_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return package


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--max-records", type=int, default=40)
    parser.add_argument("--max-json-chars", type=int, default=80000)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    package = build_package(
        repo_root=Path(args.repo_root),
        output_root=Path(args.output_root),
        issue_id=args.issue_id,
        source_ref=args.source_ref,
        source_commit=args.source_commit,
        max_records=args.max_records,
        max_json_chars=args.max_json_chars,
    )
    print(json.dumps(package, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
