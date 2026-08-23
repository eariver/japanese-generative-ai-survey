#!/usr/bin/env python3
"""Deterministic execution bridge for ChatGPT-owned Survey Production Core v2 work.

This helper exists for operator runtimes that can edit the repository but cannot
mount a checkout and invoke the canonical Core CLI directly. It does not perform
research, editorial judgment, source selection, Architecture design, drafting,
semantic review, visual review, or Human approval.

A ChatGPT production session commits one immutable request under
``<source_root>/execution/requests/``. The bridge validates that request,
executes only a small allowlist of canonical deterministic Core operations, and
writes only edition-local generated authorities under the Profile-bound source
root.

The GitHub Actions wrapper is transport/execution infrastructure. The semantic
content supplied in artifacts, agent review evidence, and stage summaries remains
ChatGPT-authored repository input.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_execution_record_v2 as execution_record
from scripts import survey_production_v2 as core
from scripts import survey_retrospective_profile_v2 as retrospective
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_stage_validation_v2 as stage_validation

REQUEST_SCHEMA = Path("schemas/operator-execution-request-v2.schema.json")
REQUEST_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")


class OperatorBridgeError(ValueError):
    pass


def _rel(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError as exc:
        raise OperatorBridgeError(f"path escapes repository: {path}") from exc


def _authority(repo_root: Path, path: Path) -> dict[str, str]:
    if path.is_symlink() or not path.is_file():
        raise OperatorBridgeError(f"authority file missing or unsafe: {_rel(repo_root, path)}")
    return {"path": _rel(repo_root, path), "sha256": core.sha256_file(path)}


def _validate_sha(value: str, label: str) -> str:
    if not isinstance(value, str) or not SHA40_RE.fullmatch(value):
        raise OperatorBridgeError(f"{label} must be exact lowercase 40-hex commit SHA")
    return value


def _source_root(repo_root: Path, request: dict[str, Any]) -> Path:
    source_root = core.repo_local_path(
        repo_root,
        request["source_root"],
        "operator bridge source root",
    )
    rel = _rel(repo_root, source_root)
    if rel == "sources" or not rel.startswith("sources/"):
        raise OperatorBridgeError("operator bridge source_root must be under sources/")
    return source_root


def _request_path(repo_root: Path, request: dict[str, Any], request_path: Path) -> Path:
    request_id = request["request_id"]
    if not REQUEST_ID_RE.fullmatch(request_id):
        raise OperatorBridgeError("request_id is not a safe filename stem")
    expected = _source_root(repo_root, request) / "execution" / "requests" / f"{request_id}.json"
    actual = request_path.resolve()
    if actual != expected.resolve():
        raise OperatorBridgeError(
            "operator request must use canonical path: " + _rel(repo_root, expected)
        )
    if request_path.is_symlink() or not request_path.is_file():
        raise OperatorBridgeError("operator request is missing or unsafe")
    return expected


def _load_request(repo_root: Path, request_path: Path, ref_name: str) -> dict[str, Any]:
    payload = schema_gate.load_and_validate_json(
        request_path,
        repo_root / REQUEST_SCHEMA,
        label="Operator Execution Request",
    )
    _request_path(repo_root, payload, request_path)
    try:
        core.parse_instant(payload["recorded_at"])
    except ValueError as exc:
        raise OperatorBridgeError("recorded_at must be an offset-aware ISO-8601 instant") from exc
    if ref_name == "main":
        raise OperatorBridgeError("operator bridge must not execute edition requests on main")
    if payload["work_branch"] != ref_name:
        raise OperatorBridgeError(
            f"request work_branch {payload['work_branch']!r} does not match executing ref {ref_name!r}"
        )
    return payload


def _ensure_under(repo_root: Path, path: Path, parent: Path, label: str) -> None:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError as exc:
        raise OperatorBridgeError(
            f"{label} must stay under {_rel(repo_root, parent)}"
        ) from exc


def _canonical_profile_state(source_root: Path, cfg: dict[str, Any]) -> tuple[Path, Path]:
    return (
        source_root / cfg["state_authority"]["profile_filename"],
        source_root / cfg["state_authority"]["authoritative_filename"],
    )


def _validate_profile_identity(profile: dict[str, Any], request: dict[str, Any]) -> None:
    if profile.get("issue_id") != request["issue_id"]:
        raise OperatorBridgeError("generated/current Production Profile issue_id differs from request")
    paths = profile.get("paths", {})
    if paths.get("source_root") != request["source_root"]:
        raise OperatorBridgeError("generated/current Production Profile source_root differs from request")
    if paths.get("work_branch") != request["work_branch"]:
        raise OperatorBridgeError("generated/current Production Profile work_branch differs from request")


def _load_scoped_spec(
    repo_root: Path,
    source_root: Path,
    value: str,
    label: str,
) -> Path:
    spec_path = core.repo_local_path(repo_root, value, label)
    _ensure_under(repo_root, spec_path, source_root, label)
    if spec_path.is_symlink() or not spec_path.is_file():
        raise OperatorBridgeError(f"{label} missing or unsafe")
    return spec_path


def _initialize(
    repo_root: Path,
    cfg: dict[str, Any],
    request: dict[str, Any],
    event_sha: str,
) -> tuple[Path, Path, list[str]]:
    source_root = _source_root(repo_root, request)
    profile_path, state_path = _canonical_profile_state(source_root, cfg)
    if profile_path.exists() or state_path.exists():
        raise OperatorBridgeError("operator initialization requires absent canonical Profile/State")

    operation = request["operation"]
    recorded_at = core.parse_instant(request["recorded_at"])
    kind = operation["kind"]
    if kind == "INITIALIZE_WEEKLY":
        profile = core.weekly_profile(repo_root, cfg, recorded_at, request["issue_id"])
    elif kind == "INITIALIZE_RETROSPECTIVE":
        spec_path = _load_scoped_spec(
            repo_root,
            source_root,
            operation["spec_path"],
            "retrospective scope spec",
        )
        profile = retrospective.build_profile(
            repo_root,
            cfg,
            retrospective.load_scope(repo_root, spec_path),
            recorded_at,
        )
    elif kind == "INITIALIZE_THEMATIC":
        spec_path = _load_scoped_spec(
            repo_root,
            source_root,
            operation["spec_path"],
            "thematic scope spec",
        )
        profile = core.thematic_profile(repo_root, cfg, core.load_json(spec_path))
    else:
        raise OperatorBridgeError(f"unsupported initialization operation: {kind}")

    _validate_profile_identity(profile, request)
    core.initialize(
        repo_root,
        cfg,
        profile,
        event_sha,
        operation["target_gate"],
        recorded_at,
    )
    if not profile_path.is_file() or not state_path.is_file():
        raise OperatorBridgeError("canonical initialization did not materialize Profile/State")

    record_cfg = operation["execution_record"]
    index_path, session_path = execution_record.initialize(
        repo_root,
        cfg,
        profile_path,
        state_path,
        session_id=record_cfg["session_id"],
        started_at=request["recorded_at"],
        main_sha=record_cfg["reviewed_main_sha"],
        branch_head=event_sha,
        objective=record_cfg["objective"],
        requested_stop=record_cfg["requested_stop"],
    )
    record_errors = execution_record.validate(repo_root, cfg, profile_path, state_path)
    if record_errors:
        raise OperatorBridgeError("execution record validation failed: " + "; ".join(record_errors))
    return profile_path, state_path, [_rel(repo_root, index_path), _rel(repo_root, session_path)]


def _artifact_map(repo_root: Path, rows: list[dict[str, str]]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for row in rows:
        name = row["name"]
        if name in result:
            raise OperatorBridgeError(f"duplicate stage artifact name: {name}")
        path = core.repo_local_path(repo_root, row["path"], f"stage artifact {name}")
        if path.is_symlink() or not path.is_file():
            raise OperatorBridgeError(f"stage artifact missing or unsafe: {row['path']}")
        result[name] = path
    return result


def _write_reviews(
    repo_root: Path,
    request: dict[str, Any],
    result_path: Path,
    reviews_path: Path,
) -> None:
    operation = request["operation"]
    rows: list[dict[str, Any]] = [
        {
            "check_id": agent.CORE_STAGE_REVIEW_ID,
            "kind": "DETERMINISTIC",
            "executor": "survey_core_execution_bridge_v2",
            "evidence": f"Canonical Core stage contract validated for immutable request {request['request_id']}.",
            "result_path": _rel(repo_root, result_path),
        }
    ]
    seen = {agent.CORE_STAGE_REVIEW_ID}
    for row in operation["agent_reviews"]:
        check_id = row["check_id"]
        if check_id in seen:
            raise OperatorBridgeError(f"duplicate/reserved review check_id: {check_id}")
        seen.add(check_id)
        rows.append(dict(row))
    core.write_json(reviews_path, {"reviews": rows})


def _advance_stage(
    repo_root: Path,
    cfg: dict[str, Any],
    request: dict[str, Any],
    event_sha: str,
    run_root: Path,
) -> tuple[Path, list[str], str, str | None]:
    operation = request["operation"]
    source_root = _source_root(repo_root, request)
    state_path = core.repo_local_path(repo_root, operation["state_path"], "operator bridge Production State")
    _, expected_state = _canonical_profile_state(source_root, cfg)
    if state_path.resolve() != expected_state.resolve():
        raise OperatorBridgeError("ADVANCE_STAGE state_path is not the canonical edition Production State")
    if state_path.is_symlink() or not state_path.is_file():
        raise OperatorBridgeError("canonical Production State missing or unsafe")

    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise OperatorBridgeError("Production State is not resumable: " + "; ".join(errors))
    if state.get("lifecycle_state") != operation["expected_from_state"]:
        raise OperatorBridgeError(
            f"stale bridge request: expected {operation['expected_from_state']}, current {state.get('lifecycle_state')}"
        )
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "Production Profile")
    profile = core.load_json(profile_path)
    _validate_profile_identity(profile, request)

    artifacts = _artifact_map(repo_root, operation["artifacts"])
    recorded_at = core.parse_instant(request["recorded_at"])
    result_path = run_root / "core-stage-contract.json"
    reviews_path = run_root / "reviews.json"
    stage_validation.validate_stage(
        repo_root,
        cfg,
        state_path,
        artifacts,
        result_path,
        recorded_at,
    )
    _write_reviews(repo_root, request, result_path, reviews_path)

    checkpoint_path = agent.build_stage_checkpoint(
        repo_root,
        cfg,
        state_path,
        artifacts,
        reviews_path,
        operation["summary"],
        recorded_at,
        event_sha,
    )
    updated = agent.advance_with_checkpoint(repo_root, cfg, state_path, checkpoint_path)
    return (
        state_path,
        [_rel(repo_root, result_path), _rel(repo_root, reviews_path), _rel(repo_root, checkpoint_path)],
        updated["lifecycle_state"],
        updated.get("terminal_reason"),
    )


def execute_request(
    repo_root: Path,
    request_path: Path,
    *,
    event_sha: str,
    ref_name: str,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    event_sha = _validate_sha(event_sha, "event_sha")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    request = _load_request(repo_root, request_path, ref_name)
    source_root = _source_root(repo_root, request)
    run_root = source_root / "execution" / "bridge-runs" / request["request_id"]
    if run_root.exists():
        raise OperatorBridgeError(f"bridge request_id already executed: {request['request_id']}")
    run_root.mkdir(parents=True, exist_ok=False)

    request_authority = _authority(repo_root, request_path)
    operation = request["operation"]
    generated: list[str] = []
    if operation["kind"] in {"INITIALIZE_WEEKLY", "INITIALIZE_RETROSPECTIVE", "INITIALIZE_THEMATIC"}:
        profile_path, state_path, record_paths = _initialize(repo_root, cfg, request, event_sha)
        generated.extend([_rel(repo_root, profile_path), _rel(repo_root, state_path), *record_paths])
        state = core.load_json(state_path)
        lifecycle = state["lifecycle_state"]
        terminal_reason = state.get("terminal_reason")
    elif operation["kind"] == "ADVANCE_STAGE":
        state_path, stage_paths, lifecycle, terminal_reason = _advance_stage(
            repo_root, cfg, request, event_sha, run_root
        )
        generated.extend(stage_paths)
    else:
        raise OperatorBridgeError(f"unsupported operator bridge operation: {operation['kind']}")

    receipt_path = run_root / "receipt.json"
    receipt = {
        "schema_version": "2.0-rc1",
        "request_id": request["request_id"],
        "issue_id": request["issue_id"],
        "source_root": request["source_root"],
        "work_branch": request["work_branch"],
        "operation": operation["kind"],
        "request": request_authority,
        "event_commit_sha": event_sha,
        "recorded_at": core.iso_utc(core.parse_instant(request["recorded_at"])),
        "production_state": _authority(repo_root, state_path),
        "lifecycle_state": lifecycle,
        "terminal_reason": terminal_reason,
        "generated_paths": sorted(set(generated)),
        "status": "PASS",
    }
    core.write_json(receipt_path, receipt)
    generated.append(_rel(repo_root, receipt_path))

    return {
        "request_id": request["request_id"],
        "issue_id": request["issue_id"],
        "source_root": _rel(repo_root, source_root),
        "state_path": _rel(repo_root, state_path),
        "lifecycle_state": lifecycle,
        "terminal_reason": terminal_reason,
        "generated_paths": sorted(set(generated)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--request", required=True)
    parser.add_argument("--event-sha", required=True)
    parser.add_argument("--ref-name", required=True)
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    request_path = Path(args.request)
    if not request_path.is_absolute():
        request_path = root / request_path
    try:
        result = execute_request(
            root,
            request_path,
            event_sha=args.event_sha,
            ref_name=args.ref_name,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
