#!/usr/bin/env python3
"""Deterministic execution bridge for ChatGPT-owned Survey Production Core v2 work.

This helper exists for operator runtimes that can edit the repository but cannot
mount a checkout and invoke the canonical Core CLI directly. It does not perform
research, editorial judgment, source selection, Architecture design, drafting,
semantic review, visual review, or Human decision-making.

A ChatGPT production session commits one immutable request under
``<source_root>/execution/requests/``. The bridge validates that request,
executes only a small allowlist of canonical deterministic Core operations, and
writes only edition-local generated authorities under the Profile-bound source
root. Human Gate operations only record an explicit Human APPROVED or
REQUEST_CHANGES decision and execute its already-specified deterministic
consequence; they never infer the decision or regeneration boundary.

The GitHub Actions wrapper is transport/execution infrastructure. The semantic
content supplied in artifacts, agent review evidence, stage summaries, requested
changes, and regeneration boundaries remains ChatGPT/Human-authored repository
input.
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
from scripts import survey_human_gate_v2 as human_gate
from scripts import survey_period_v2 as period
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_stage_validation_v2 as stage_validation

REQUEST_SCHEMA = Path("schemas/operator-execution-request-v2.schema.json")
THEMATIC_SCOPE_SCHEMA = Path("schemas/thematic-scope-spec-v2.schema.json")
REQUEST_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
INITIALIZE_KINDS = {"INITIALIZE_WEEKLY", "INITIALIZE_RETROSPECTIVE", "INITIALIZE_THEMATIC"}
HUMAN_GATE_KINDS = {
    "RECORD_ARCHITECTURE_APPROVAL",
    "REQUEST_ARCHITECTURE_REVISION",
    "RECORD_PUBLICATION_PREVIEW_APPROVAL",
    "REQUEST_PUBLICATION_PREVIEW_REVISION",
}


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


def _thematic_profile_from_spec(
    repo_root: Path,
    cfg: dict[str, Any],
    request: dict[str, Any],
    spec_path: Path,
    recorded_at,
) -> dict[str, Any]:
    """Accept either a raw Core thematic spec or canonical scope materialization.

    Canonical ``thematic-scope-spec-v2`` deliberately owns editorial scope but
    not temporal execution identity. The operator request supplies temporal mode
    and the immutable request timestamp supplies ``as_of``. This mirrors the
    repository-owned pilot bootstrap without introducing an SP001-specific path.
    """
    raw = core.load_json(spec_path)
    operation = request["operation"]

    # Historical/generic raw Core specs remain supported. When the request also
    # carries a temporal mode, require it to agree rather than silently override.
    if "planning_authority" not in raw:
        requested_mode = operation.get("temporal_mode")
        if requested_mode is not None and raw.get("temporal_mode") != requested_mode:
            raise OperatorBridgeError("raw Thematic spec temporal_mode differs from operator request")
        return core.thematic_profile(repo_root, cfg, raw)

    materialized = schema_gate.load_and_validate_json(
        spec_path,
        repo_root / THEMATIC_SCOPE_SCHEMA,
        label="Thematic scope materialization",
    )
    if materialized["issue_id"] != request["issue_id"]:
        raise OperatorBridgeError("Thematic scope materialization issue_id differs from operator request")

    authority = materialized["planning_authority"]
    authority_path = core.repo_local_path(
        repo_root,
        authority["path"],
        "Thematic planning authority",
    )
    if authority_path.is_symlink() or not authority_path.is_file():
        raise OperatorBridgeError("Thematic planning authority missing or unsafe")
    authority_text = authority_path.read_text(encoding="utf-8")
    if authority["entry"] not in authority_text:
        raise OperatorBridgeError("Thematic planning authority entry is not present in current authority bytes")
    if core.sha256_file(authority_path) != authority["sha256"]:
        raise OperatorBridgeError("Thematic scope materialization planning-authority SHA drift")

    temporal_mode = operation.get("temporal_mode")
    if temporal_mode not in {"OPEN_HISTORY_AS_OF", "CURRENT_STATE_AS_OF"}:
        raise OperatorBridgeError(
            "canonical Thematic scope materialization requires operation.temporal_mode"
        )

    spec: dict[str, Any] = {
        "issue_id": request["issue_id"],
        "question": materialized["question"],
        "temporal_mode": temporal_mode,
        "as_of": core.iso_utc(recorded_at),
        "inclusion": list(materialized["inclusion"]),
        "exclusion": list(materialized["exclusion"]),
        "scope_dimensions": list(materialized["scope_dimensions"]),
        "initial_obligations": [dict(row) for row in materialized["initial_obligations"]],
        "source_root": request["source_root"],
        "work_branch": request["work_branch"],
    }
    if operation.get("survey_root"):
        spec["survey_root"] = operation["survey_root"]
    return core.thematic_profile(repo_root, cfg, spec)


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
        spec = period.resolve_configured_period(repo_root, operation["special_slug"], recorded_at)
        profile = period.period_profile(repo_root, cfg, spec)
    elif kind == "INITIALIZE_THEMATIC":
        spec_path = _load_scoped_spec(
            repo_root,
            source_root,
            operation["spec_path"],
            "thematic scope spec",
        )
        profile = _thematic_profile_from_spec(
            repo_root,
            cfg,
            request,
            spec_path,
            recorded_at,
        )
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


def _canonical_existing_state(
    repo_root: Path,
    cfg: dict[str, Any],
    request: dict[str, Any],
) -> tuple[Path, dict[str, Any]]:
    source_root = _source_root(repo_root, request)
    operation = request["operation"]
    state_path = core.repo_local_path(repo_root, operation["state_path"], "operator bridge Production State")
    _, expected_state = _canonical_profile_state(source_root, cfg)
    if state_path.resolve() != expected_state.resolve():
        raise OperatorBridgeError("operator state_path is not the canonical edition Production State")
    if state_path.is_symlink() or not state_path.is_file():
        raise OperatorBridgeError("canonical Production State missing or unsafe")
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise OperatorBridgeError("Production State is not resumable: " + "; ".join(errors))
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "Production Profile")
    _validate_profile_identity(core.load_json(profile_path), request)
    return state_path, state


def _advance_stage(
    repo_root: Path,
    cfg: dict[str, Any],
    request: dict[str, Any],
    event_sha: str,
    run_root: Path,
) -> tuple[Path, list[str], list[str], str, str | None]:
    operation = request["operation"]
    state_path, state = _canonical_existing_state(repo_root, cfg, request)
    if state.get("lifecycle_state") != operation["expected_from_state"]:
        raise OperatorBridgeError(
            f"stale bridge request: expected {operation['expected_from_state']}, current {state.get('lifecycle_state')}"
        )
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
        [],
        updated["lifecycle_state"],
        updated.get("terminal_reason"),
    )


def _human_gate_operation(
    repo_root: Path,
    cfg: dict[str, Any],
    request: dict[str, Any],
    event_sha: str,
) -> tuple[Path, list[str], list[str], str, str | None]:
    operation = request["operation"]
    state_path, _ = _canonical_existing_state(repo_root, cfg, request)
    reviewed_at = core.parse_instant(operation["reviewed_at"])
    common = {
        "expected_revision": operation["expected_revision"],
        "reviewed_commit_sha": operation["reviewed_repository_commit_sha"],
    }
    kind = operation["kind"]
    removed: list[str] = []
    if kind == "RECORD_ARCHITECTURE_APPROVAL":
        updated, record_path, index_path = human_gate.record_architecture_approval(
            repo_root,
            cfg,
            state_path,
            operation["reviewed_by"],
            reviewed_at,
            operation["review_reference"],
            **common,
        )
        source_root = _source_root(repo_root, request)
        approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
        generated = [_rel(repo_root, approval_path), _rel(repo_root, record_path), _rel(repo_root, index_path)]
    elif kind == "REQUEST_ARCHITECTURE_REVISION":
        updated, record_path, index_path, removed = human_gate.request_architecture_revision(
            repo_root,
            cfg,
            state_path,
            operation["regeneration_boundary"],
            operation["requested_changes"],
            operation["reviewed_by"],
            reviewed_at,
            operation["review_reference"],
            **common,
        )
        generated = [_rel(repo_root, record_path), _rel(repo_root, index_path)]
    elif kind == "RECORD_PUBLICATION_PREVIEW_APPROVAL":
        updated, record_path, index_path = human_gate.record_publication_preview_approval(
            repo_root,
            cfg,
            state_path,
            operation["reviewed_by"],
            reviewed_at,
            operation["review_reference"],
            **common,
        )
        source_root = _source_root(repo_root, request)
        approval_path = source_root / cfg["state_authority"]["publication_preview_approval_path"]
        generated = [_rel(repo_root, approval_path), _rel(repo_root, record_path), _rel(repo_root, index_path)]
    elif kind == "REQUEST_PUBLICATION_PREVIEW_REVISION":
        updated, record_path, index_path, removed = human_gate.request_publication_preview_revision(
            repo_root,
            cfg,
            state_path,
            operation["regeneration_boundary"],
            operation["requested_changes"],
            operation["reviewed_by"],
            reviewed_at,
            operation["review_reference"],
            **common,
        )
        generated = [_rel(repo_root, record_path), _rel(repo_root, index_path)]
    else:
        raise OperatorBridgeError(f"unsupported Human Gate bridge operation: {kind}")
    return state_path, generated, removed, updated["lifecycle_state"], updated.get("terminal_reason")


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
    removed: list[str] = []
    if operation["kind"] in INITIALIZE_KINDS:
        profile_path, state_path, record_paths = _initialize(repo_root, cfg, request, event_sha)
        generated.extend([_rel(repo_root, profile_path), _rel(repo_root, state_path), *record_paths])
        state = core.load_json(state_path)
        lifecycle = state["lifecycle_state"]
        terminal_reason = state.get("terminal_reason")
    elif operation["kind"] == "ADVANCE_STAGE":
        state_path, stage_paths, removed, lifecycle, terminal_reason = _advance_stage(
            repo_root, cfg, request, event_sha, run_root
        )
        generated.extend(stage_paths)
    elif operation["kind"] in HUMAN_GATE_KINDS:
        state_path, gate_paths, removed, lifecycle, terminal_reason = _human_gate_operation(
            repo_root, cfg, request, event_sha
        )
        generated.extend(gate_paths)
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
        "removed_paths": sorted(set(removed)),
        "status": "PASS",
    }
    if operation["kind"] in HUMAN_GATE_KINDS:
        receipt["reviewed_repository_commit_sha"] = operation["reviewed_repository_commit_sha"]
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
        "removed_paths": sorted(set(removed)),
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
