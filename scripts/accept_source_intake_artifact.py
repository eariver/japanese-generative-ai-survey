#!/usr/bin/env python3
"""Accept reviewed source-intake collector files into a weekly work tree.

Only non-reproducible collection artifacts are committed: collector Raw bytes,
collector-run provenance, and collector summary metadata. Deterministic screening
indexes/batches from the Actions artifact are deliberately not committed; they are
regenerated from accepted collector files when needed.

The accepted source-intake plan is also the authoritative bootstrap/transition
input for the weekly pipeline state. A new issue becomes DISCOVERY_COLLECTED only
after a reviewed successful source-intake artifact is accepted. Source collection
cannot be appended after downstream normalization/selection has begun.

Existing destination files are append-only: identical bytes are idempotent, while
a same-path byte change is a hard failure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

ALLOWED_SOURCE_STATES = {"ISSUE_INITIALIZED", "DISCOVERY_COLLECTED"}


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


def parse_timestamp(value: str, label: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"{label} must be ISO-8601 date-time") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{label} must include an explicit UTC offset or Z")
    return parsed


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


def validate_plan(artifact_root: Path, issue_id: str) -> tuple[Path, dict[str, Any]]:
    plan_path = artifact_root / "source-intake-control" / "plan.json"
    if not plan_path.is_file():
        raise ValueError("source-intake-control/plan.json missing from artifact")
    plan = load_json(plan_path)
    if plan.get("schema_version") != "1.0":
        raise ValueError("unsupported source-intake plan schema_version")
    if plan.get("issue_id") != issue_id:
        raise ValueError("source-intake plan issue_id mismatch")
    if plan.get("editorial_cutoff_timezone") != "America/New_York":
        raise ValueError("source-intake plan cutoff timezone mismatch")
    if plan.get("unattended_public_release") is not False:
        raise ValueError("source-intake plan must not authorize unattended public release")
    for key in ("editorial_cutoff", "collection_window_start", "collection_window_end"):
        value = plan.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError(f"source-intake plan {key} must be a non-empty date-time string")
        parse_timestamp(value, f"source-intake plan {key}")
    if parse_timestamp(plan["collection_window_end"], "source-intake plan collection_window_end") < parse_timestamp(
        plan["collection_window_start"], "source-intake plan collection_window_start"
    ):
        raise ValueError("source-intake plan collection window end precedes start")
    return plan_path, plan


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


def new_discovery_state(plan: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "lifecycle_state": "DISCOVERY_COLLECTED",
        "revision": "working",
        "calendar": {
            "editorial_cutoff": plan["editorial_cutoff"],
            "cutoff_timezone": plan["editorial_cutoff_timezone"],
            "collection_window_start": plan["collection_window_start"],
            "collection_anchor_at": plan["collection_window_end"],
        },
        "gates": {
            "raw_sources_preserved": "passed",
            "candidate_inventory": "pending",
            "evidence_normalized": "pending",
            "candidate_selection": "pending",
            "issue_architecture": "pending",
            "article_draft": "pending",
            "claim_and_chronology_validation": "pending",
            "latex_build": "pending",
            "visual_review": "pending",
            "freeze": "pending",
        },
        "automation": {
            "unattended_public_release": False,
            "human_gate_required_for_selection": True,
            "human_gate_required_for_freeze": True,
        },
    }


def transition_discovery_state(existing: dict[str, Any] | None, plan: dict[str, Any]) -> dict[str, Any]:
    if existing is None:
        return new_discovery_state(plan)
    if existing.get("issue_id") != plan["issue_id"]:
        raise ValueError("existing pipeline state issue_id mismatch")
    lifecycle = existing.get("lifecycle_state")
    if lifecycle not in ALLOWED_SOURCE_STATES:
        raise ValueError(
            f"source intake cannot modify issue after downstream work has begun: lifecycle_state={lifecycle!r}"
        )
    calendar = existing.get("calendar")
    if not isinstance(calendar, dict):
        raise ValueError("existing pipeline state calendar is missing")
    if calendar.get("editorial_cutoff") != plan["editorial_cutoff"]:
        raise ValueError("existing pipeline state editorial_cutoff differs from accepted source plan")
    if calendar.get("cutoff_timezone") != plan["editorial_cutoff_timezone"]:
        raise ValueError("existing pipeline state cutoff_timezone differs from accepted source plan")
    if calendar.get("collection_window_start") != plan["collection_window_start"]:
        raise ValueError("existing pipeline state collection_window_start differs from accepted source plan")

    updated = deepcopy(existing)
    updated["lifecycle_state"] = "DISCOVERY_COLLECTED"
    current_anchor = calendar.get("collection_anchor_at")
    candidate_anchor = plan["collection_window_end"]
    if current_anchor:
        current_dt = parse_timestamp(current_anchor, "existing collection_anchor_at")
        candidate_dt = parse_timestamp(candidate_anchor, "source-intake plan collection_window_end")
        updated["calendar"]["collection_anchor_at"] = current_anchor if current_dt >= candidate_dt else candidate_anchor
    else:
        updated["calendar"]["collection_anchor_at"] = candidate_anchor
    gates = updated.get("gates")
    if not isinstance(gates, dict):
        raise ValueError("existing pipeline state gates are missing")
    gates["raw_sources_preserved"] = "passed"
    return updated


def accept(
    *,
    artifact_root: Path,
    repo_root: Path,
    issue_id: str,
    workflow_run_id: int,
    artifact_id: int,
    artifact_name: str,
    artifact_digest: str,
    review_reference: str,
) -> tuple[dict[str, Any], bool]:
    if not artifact_digest.startswith("sha256:") or len(artifact_digest) != 71:
        raise ValueError("artifact_digest must be sha256:<64 hex>")
    try:
        int(artifact_digest.split(":", 1)[1], 16)
    except ValueError as exc:
        raise ValueError("artifact_digest contains non-hex SHA-256") from exc
    if not isinstance(review_reference, str) or not review_reference.strip():
        raise ValueError("review_reference must be a non-empty string")

    repo_root = repo_root.resolve()
    artifact_root = artifact_root.resolve()
    report_path, report = validate_report(artifact_root, issue_id)
    plan_path, plan = validate_plan(artifact_root, issue_id)
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
            "review_reference": review_reference.strip(),
        },
        "source_intake_report_sha256": sha256_file(report_path),
        "source_plan_sha256": sha256_file(plan_path),
        "collector_run_count": len(report["runs"]),
        "files": sorted(planned_records, key=lambda value: value["path"]),
        "raw_file_count": raw_count,
        "derived_screening_committed": False,
        "state_transition": {
            "target_lifecycle_state": "DISCOVERY_COLLECTED",
            "collection_anchor_candidate": plan["collection_window_end"],
            "raw_sources_preserved": "passed",
        },
        "rules": [
            "Collector Raw bytes, collector-run provenance, and collector summary metadata are accepted append-only.",
            "A same-path byte change is a hard failure; identical bytes are idempotent.",
            "Deterministic screening indexes/batches from the Actions artifact are not committed and must be regenerated.",
            "The accepted source plan initializes/advances only ISSUE_INITIALIZED or DISCOVERY_COLLECTED state.",
            "New source intake is rejected after downstream normalization/selection has begun.",
            "The source Actions run/artifact identity, artifact digest, plan digest, and review reference are recorded for auditability.",
        ],
    }

    manifest_path = acceptance_path(repo_root, issue_id, workflow_run_id)
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if manifest_path.exists():
        existing_manifest = load_json(manifest_path)
        if existing_manifest != manifest:
            raise ValueError(f"acceptance manifest already exists with different content: {manifest_path}")
        if not state_path.is_file():
            raise ValueError("accepted source-intake manifest exists but pipeline-state.json is missing")
        state = load_json(state_path)
        if state.get("issue_id") != issue_id:
            raise ValueError("accepted source-intake manifest exists but pipeline state issue_id mismatches")
        return {
            "schema_version": "1.0",
            "passed": True,
            "issue_id": issue_id,
            "status": "ALREADY_ACCEPTED",
            "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
            "new_file_count": 0,
            "total_file_count": len(planned_records),
            "raw_file_count": raw_count,
            "pipeline_state": state_path.relative_to(repo_root).as_posix(),
        }, True

    existing_state = load_json(state_path) if state_path.is_file() else None
    updated_state = transition_discovery_state(existing_state, plan)

    for source, destination in copies:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if sha256_file(destination) != sha256_file(source) or destination.stat().st_size != source.stat().st_size:
            raise RuntimeError(f"copy verification failed: {destination}")

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(updated_state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "schema_version": "1.0",
        "passed": True,
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "acceptance_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "new_file_count": len(copies) + 1 + (0 if existing_state is not None else 1),
        "total_file_count": len(planned_records),
        "raw_file_count": raw_count,
        "pipeline_state": state_path.relative_to(repo_root).as_posix(),
        "pipeline_state_created": existing_state is None,
        "pipeline_state_updated": existing_state is not None and existing_state != updated_state,
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
    parser.add_argument("--review-reference", required=True)
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
