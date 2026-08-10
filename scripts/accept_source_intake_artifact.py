#!/usr/bin/env python3
"""Accept reviewed source-intake collector files into a weekly work tree.

Only non-reproducible collection artifacts are committed: collector Raw bytes,
collector-run provenance, and collector summary metadata. Deterministic screening
indexes/batches from the Actions artifact are deliberately not committed; they are
regenerated from accepted collector files when needed.

Existing destination files are append-only: identical bytes are idempotent, while
a same-path byte change is a hard failure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


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


def file_record(repo_root: Path, path: Path, kind: str) -> dict[str, Any]:
    return {
        "path": path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
        "kind": kind,
    }


def artifact_source_root(artifact_root: Path, issue_id: str) -> Path:
    path = artifact_root / "source-intake" / "sources" / issue_id / "collectors"
    if not path.is_dir():
        raise ValueError(f"collector tree missing from artifact: {path}")
    return path


def classify_source_file(relative: Path) -> str:
    if "raw" in relative.parts:
        if relative.parts.count("raw") != 1:
            raise ValueError(f"invalid nested Raw path: {relative}")
        return "RAW"
    if relative.name == "collector-run.json":
        return "COLLECTOR_RUN"
    if relative.name == "summary.json":
        return "SUMMARY"
    raise ValueError(f"unexpected file in source-intake collector tree: {relative}")


def discover_files(source_root: Path) -> list[tuple[Path, Path, str]]:
    values: list[tuple[Path, Path, str]] = []
    for path in sorted(source_root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink is forbidden in accepted source-intake artifact: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(source_root)
        if any(part in {"", ".", ".."} for part in relative.parts):
            raise ValueError(f"invalid source-intake relative path: {relative}")
        kind = classify_source_file(relative)
        values.append((path, relative, kind))
    if not values:
        raise ValueError("source-intake collector tree contains no files")
    return values


def validate_report(artifact_root: Path, issue_id: str) -> tuple[Path, dict[str, Any]]:
    report_path = artifact_root / "source-intake" / "source-intake-report.json"
    if not report_path.is_file():
        raise ValueError("source-intake-report.json missing from artifact")
    report = load_json(report_path)
    if report.get("schema_version") != "1.0":
        raise ValueError("unsupported source-intake report schema_version")
    if report.get("issue_id") != issue_id:
        raise ValueError("source-intake report issue_id mismatch")
    if report.get("overall_status") != "success":
        raise ValueError(f"only overall_status=success may be accepted, got {report.get('overall_status')!r}")
    runs = report.get("runs")
    if not isinstance(runs, list) or not runs:
        raise ValueError("source-intake report must contain at least one collector run")
    if report.get("collector_count") != len(runs):
        raise ValueError("source-intake report collector_count does not match runs length")
    for index, run in enumerate(runs):
        if not isinstance(run, dict):
            raise ValueError(f"source-intake report runs[{index}] must be an object")
        if run.get("status") != "success":
            raise ValueError(f"collector run is not successful: {run}")
        if not isinstance(run.get("run_id"), str) or not run["run_id"]:
            raise ValueError(f"collector run missing run_id: {run}")
        if not isinstance(run.get("collector"), str) or not run["collector"]:
            raise ValueError(f"collector run missing collector: {run}")
    return report_path, report


def validate_collector_runs(source_root: Path, report: dict[str, Any], issue_id: str) -> None:
    expected = {run["run_id"]: run["collector"] for run in report["runs"]}
    found: dict[str, str] = {}
    for path in sorted(source_root.rglob("collector-run.json")):
        value = load_json(path)
        run_id = value.get("run_id")
        collector_id = value.get("collector", {}).get("id") if isinstance(value.get("collector"), dict) else None
        if value.get("issue_id") != issue_id:
            raise ValueError(f"collector-run issue_id mismatch: {path}")
        if not isinstance(run_id, str) or not run_id:
            raise ValueError(f"collector-run run_id missing: {path}")
        if not isinstance(collector_id, str) or not collector_id:
            raise ValueError(f"collector-run collector.id missing: {path}")
        if run_id in found:
            raise ValueError(f"duplicate collector run_id in artifact: {run_id}")
        found[run_id] = collector_id
    if set(found) != set(expected):
        raise ValueError(
            f"collector-run files do not match source-intake report: missing={sorted(set(expected)-set(found))} "
            f"extra={sorted(set(found)-set(expected))}"
        )
    for run_id, collector in expected.items():
        if found[run_id] != collector:
            raise ValueError(
                f"collector identity mismatch for {run_id}: report={collector} collector-run={found[run_id]}"
            )


def acceptance_path(repo_root: Path, issue_id: str, workflow_run_id: int) -> Path:
    return repo_root / "sources" / issue_id / "imports" / "source-intake" / f"actions-run-{workflow_run_id}.json"


def accept(
    *,
    artifact_root: Path,
    repo_root: Path,
    issue_id: str,
    workflow_run_id: int,
    artifact_id: int,
    artifact_name: str,
    artifact_digest: str,
) -> tuple[dict[str, Any], bool]:
    if not artifact_digest.startswith("sha256:") or len(artifact_digest) != 71:
        raise ValueError("artifact_digest must be sha256:<64 hex>")
    try:
        int(artifact_digest.split(":", 1)[1], 16)
    except ValueError as exc:
        raise ValueError("artifact_digest contains non-hex SHA-256") from exc

    repo_root = repo_root.resolve()
    artifact_root = artifact_root.resolve()
    report_path, report = validate_report(artifact_root, issue_id)
    source_root = artifact_source_root(artifact_root, issue_id)
    validate_collector_runs(source_root, report, issue_id)
    discovered = discover_files(source_root)

    destination_root = repo_root / "sources" / issue_id / "collectors"
    planned_records: list[dict[str, Any]] = []
    copies: list[tuple[Path, Path]] = []
    raw_count = 0
    for source_path, relative, kind in discovered:
        destination = destination_root / relative
        source_sha = sha256_file(source_path)
        source_bytes = source_path.stat().st_size
        if destination.exists():
            if not destination.is_file():
                raise ValueError(f"destination exists and is not a file: {destination}")
            if sha256_file(destination) != source_sha or destination.stat().st_size != source_bytes:
                raise ValueError(f"append-only conflict: destination path already exists with different bytes: {destination}")
        else:
            copies.append((source_path, destination))
        planned_records.append(
            {
                "path": destination.relative_to(repo_root).as_posix(),
                "sha256": source_sha,
                "bytes": source_bytes,
                "kind": kind,
            }
        )
        if kind == "RAW":
            raw_count += 1
    if raw_count == 0:
        raise ValueError("accepted source-intake artifact contains no Raw files")

    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "source_actions": {
            "workflow_run_id": workflow_run_id,
            "artifact_id": artifact_id,
            "artifact_name": artifact_name,
            "artifact_digest": artifact_digest,
        },
        "source_intake_report_sha256": sha256_file(report_path),
        "collector_run_count": len(report["runs"]),
        "files": sorted(planned_records, key=lambda value: value["path"]),
        "raw_file_count": raw_count,
        "derived_screening_committed": False,
        "rules": [
            "Collector Raw bytes, collector-run provenance, and collector summary metadata are accepted append-only.",
            "A same-path byte change is a hard failure; identical bytes are idempotent.",
            "Deterministic screening indexes/batches from the Actions artifact are not committed and must be regenerated.",
            "The source Actions run/artifact identity and artifact digest are recorded for auditability.",
        ],
    }

    manifest_path = acceptance_path(repo_root, issue_id, workflow_run_id)
    if manifest_path.exists():
        existing = load_json(manifest_path)
        if existing != manifest:
            raise ValueError(f"acceptance manifest already exists with different content: {manifest_path}")
        return {
            "schema_version": "1.0",
            "passed": True,
            "issue_id": issue_id,
            "status": "ALREADY_ACCEPTED",
            "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
            "new_file_count": 0,
            "total_file_count": len(planned_records),
            "raw_file_count": raw_count,
        }, True

    for source, destination in copies:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if sha256_file(destination) != sha256_file(source) or destination.stat().st_size != source.stat().st_size:
            raise RuntimeError(f"copy verification failed: {destination}")

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "schema_version": "1.0",
        "passed": True,
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "new_file_count": len(copies) + 1,
        "total_file_count": len(planned_records),
        "raw_file_count": raw_count,
    }
    return result, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--workflow-run-id", required=True, type=int)
    parser.add_argument("--artifact-id", required=True, type=int)
    parser.add_argument("--artifact-name", required=True)
    parser.add_argument("--artifact-digest", required=True)
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result, passed = accept(
        artifact_root=Path(args.artifact_root),
        repo_root=Path(args.repo_root),
        issue_id=args.issue_id,
        workflow_run_id=args.workflow_run_id,
        artifact_id=args.artifact_id,
        artifact_name=args.artifact_name,
        artifact_digest=args.artifact_digest,
    )
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
