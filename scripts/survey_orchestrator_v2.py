#!/usr/bin/env python3
"""Executable orchestration and Human Gate authority for Survey Production Core v2.

production-state.json remains the sole lifecycle authority. Action Specs and
Action Results are immutable execution provenance. Runtime execution always uses
the implementation commit pinned in Production State; artifact-only HEAD motion
is tolerated only when implementation-controlled paths are unchanged.
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import subprocess
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core

Handler = Callable[[Path, dict[str, Any], dict[str, Any], dict[str, Any], str], list[dict[str, Any]]]
HandlerRegistry = dict[str, Handler]

GATE_KEYS = {
    "ARCHITECTURE_REVIEW": "architecture_review",
    "PUBLICATION_PREVIEW": "publication_preview",
}
TERMINAL_KINDS = {"HUMAN_GATE", "COMPLETE", "EXCEPTION"}
EXECUTABLE_KINDS = {"LOCAL_SCRIPT", "WORKFLOW_DISPATCH"}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _sha40(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 40 and all(c in "0123456789abcdef" for c in value)


def _git(repo_root: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args], cwd=repo_root, check=True, capture_output=True, text=True
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        stderr = getattr(exc, "stderr", "") or ""
        raise ValueError(f"git {' '.join(args)} failed: {stderr.strip()}") from exc
    return result.stdout.strip()


def observed_repository_head(repo_root: Path) -> str:
    value = _git(repo_root, "rev-parse", "HEAD")
    if not _sha40(value):
        raise ValueError("repository HEAD is not a lowercase 40-hex commit")
    return value


def _changed_control_paths(
    repo_root: Path,
    cfg: dict[str, Any],
    pinned_sha: str,
    observed_sha: str,
) -> list[str]:
    roots = cfg.get("implementation_control_roots")
    if not isinstance(roots, list) or not roots or any(not isinstance(value, str) or not value for value in roots):
        raise ValueError("implementation_control_roots contract missing or invalid")
    committed = [] if pinned_sha == observed_sha else [
        line for line in _git(repo_root, "diff", "--name-only", f"{pinned_sha}..{observed_sha}", "--", *roots).splitlines()
        if line.strip()
    ]
    unstaged = [
        line for line in _git(repo_root, "diff", "--name-only", "--", *roots).splitlines()
        if line.strip()
    ]
    staged = [
        line for line in _git(repo_root, "diff", "--cached", "--name-only", "--", *roots).splitlines()
        if line.strip()
    ]
    untracked = [
        line for line in _git(repo_root, "ls-files", "--others", "--exclude-standard", "--", *roots).splitlines()
        if line.strip()
    ]
    return sorted(set(committed + unstaged + staged + untracked))


def verify_runtime_implementation(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    observed_head_sha: str | None = None,
) -> str:
    pinned = state.get("implementation", {}).get("repository_commit_sha")
    if not _sha40(pinned):
        raise ValueError("Production State implementation commit is invalid")
    core.verify_state_basis(repo_root, cfg, state, pinned)
    observed = observed_head_sha or observed_repository_head(repo_root)
    if not _sha40(observed):
        raise ValueError("observed repository HEAD must be lowercase 40-hex")
    changed = _changed_control_paths(repo_root, cfg, pinned, observed)
    if changed:
        raise ValueError(
            "implementation-controlled files differ from State-pinned implementation: "
            + ", ".join(changed)
        )
    return observed


def _control_fields(state: dict[str, Any], cfg: dict[str, Any]) -> tuple[str | None, str | None]:
    if state["exception_gate"]["status"] == "required":
        return "EXCEPTION", "EXCEPTION_GATE_REQUIRED"
    lifecycle = state["lifecycle_state"]
    gate = cfg["orchestration"]["gate_at_state"].get(lifecycle)
    if gate:
        key = GATE_KEYS[gate]
        gate_status = state["human_gates"][key]
        if gate_status == "pending":
            return gate, "HUMAN_GATE_REACHED"
        if gate_status == "rejected":
            return "EXCEPTION", "EXCEPTION_GATE_REQUIRED"
    if lifecycle == "FROZEN":
        return None, "COMPLETE"
    stage = cfg["orchestration"]["stage_plan"].get(lifecycle)
    if not isinstance(stage, dict):
        raise ValueError(f"no orchestration stage registered for lifecycle state {lifecycle}")
    return stage["handler"], None


def refresh_state_control(state: dict[str, Any], cfg: dict[str, Any]) -> dict[str, Any]:
    updated = deepcopy(state)
    next_action, terminal = _control_fields(updated, cfg)
    updated["next_action"] = next_action
    updated["terminal_reason"] = terminal
    return updated


def _artifact_ref(name: str, path: str | None, sha256: str | None, required: bool = True) -> dict[str, Any]:
    return {"name": name, "path": path, "sha256": sha256, "required": required}


def _expected_output(name: str, checkpoint: str | None = None, path: str | None = None, required: bool = True) -> dict[str, Any]:
    return {"name": name, "checkpoint": checkpoint, "path": path, "required": required}


def _expand_path_template(template: str, profile: dict[str, Any]) -> str:
    if not isinstance(template, str) or not template:
        raise ValueError("orchestration artifact path template must be non-empty")
    value = template.replace("{source_root}", profile["paths"]["source_root"])
    if "{" in value or "}" in value:
        raise ValueError(f"unsupported orchestration path template token: {template}")
    return value


def _configured_expected_artifacts(stage: dict[str, Any], profile: dict[str, Any]) -> list[dict[str, Any]]:
    artifacts = stage.get("artifacts", [])
    if not isinstance(artifacts, list):
        raise ValueError("stage artifacts must be an array")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in artifacts:
        if not isinstance(item, dict) or set(item) != {"name", "path"}:
            raise ValueError("stage artifact fields must be name/path")
        name = item["name"]
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError("stage artifact names must be unique non-empty strings")
        seen.add(name)
        rows.append(_expected_output(name, path=_expand_path_template(item["path"], profile)))
    return rows


def _configured_gate_inputs(
    repo_root: Path,
    cfg: dict[str, Any],
    profile: dict[str, Any],
    gate: str,
) -> list[dict[str, Any]]:
    configured = cfg["orchestration"].get("gate_inputs", {}).get(gate, [])
    if not isinstance(configured, list):
        raise ValueError(f"gate_inputs.{gate} must be an array")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in configured:
        if not isinstance(item, dict) or set(item) != {"name", "path"}:
            raise ValueError(f"gate_inputs.{gate} item fields must be name/path")
        name = item["name"]
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError(f"gate_inputs.{gate} names must be unique non-empty strings")
        seen.add(name)
        rel = _expand_path_template(item["path"], profile)
        path = core.repo_local_path(repo_root, rel, f"Human Gate input {name}")
        if not path.is_file():
            raise ValueError(f"Human Gate input missing: {rel}")
        rows.append(_artifact_ref(name, rel, core.sha256_file(path)))
    return rows


def _action_identity_payload(payload: dict[str, Any]) -> dict[str, Any]:
    identity = deepcopy(payload)
    identity["action_id"] = ""
    basis = identity.get("basis")
    if isinstance(basis, dict):
        basis.pop("observed_repository_head_sha", None)
    return identity


def _action_id(payload: dict[str, Any]) -> str:
    digest = core.sha256_object(_action_identity_payload(payload))[:20]
    return f"action:{payload['issue_id']}:{digest}"


def _spec_matches_current_plan(spec: dict[str, Any], expected: dict[str, Any]) -> bool:
    left = deepcopy(spec)
    right = deepcopy(expected)
    left_basis = left.get("basis")
    right_basis = right.get("basis")
    if not isinstance(left_basis, dict) or not isinstance(right_basis, dict):
        return False
    if not _sha40(left_basis.get("observed_repository_head_sha")):
        return False
    left_basis["observed_repository_head_sha"] = right_basis.get("observed_repository_head_sha")
    return left == right


def plan_action(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    observed_head_sha: str | None = None,
) -> dict[str, Any]:
    state = core.load_json(state_path)
    observed = verify_runtime_implementation(repo_root, cfg, state, observed_head_sha)
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "state.profile.path")
    profile = core.load_json(profile_path)
    next_action, terminal = _control_fields(state, cfg)
    lifecycle = state["lifecycle_state"]

    required_inputs = [
        _artifact_ref("production-state", str(state_path.resolve().relative_to(repo_root.resolve())), core.sha256_file(state_path)),
        _artifact_ref("production-profile", state["profile"]["path"], core.sha256_file(profile_path)),
    ]
    expected_outputs: list[dict[str, Any]] = []
    handler: str | None = None
    next_state: str | None = None

    if terminal == "EXCEPTION_GATE_REQUIRED":
        action_kind = "EXCEPTION"
    elif terminal == "HUMAN_GATE_REACHED":
        action_kind = "HUMAN_GATE"
        gate = next_action
        if gate not in GATE_KEYS:
            raise ValueError(f"unknown Human Gate control action: {gate}")
        required_inputs.extend(_configured_gate_inputs(repo_root, cfg, profile, gate))
        if gate == "ARCHITECTURE_REVIEW":
            handler = "human:architecture-review"
            expected_outputs = [_expected_output("architecture-approval-record")]
        else:
            handler = "human:publication-preview"
            expected_outputs = [_expected_output("publication-preview-approval")]
    elif terminal == "COMPLETE":
        action_kind = "COMPLETE"
    else:
        stage = cfg["orchestration"]["stage_plan"][lifecycle]
        action_kind = stage.get("action_kind")
        if action_kind not in EXECUTABLE_KINDS:
            raise ValueError(f"invalid stage action_kind for {lifecycle}: {action_kind}")
        handler = stage["handler"]
        next_state = stage["next_state"]
        expected_outputs = [
            _expected_output(checkpoint, checkpoint=checkpoint)
            for checkpoint in stage.get("checkpoints", [])
        ]
        expected_outputs.extend(_configured_expected_artifacts(stage, profile))
        if handler == "stage:publication-candidate":
            expected_outputs.append(_expected_output("publication-candidate"))

    basis = {
        "production_state_sha256": core.sha256_file(state_path),
        "production_profile_sha256": core.sha256_file(profile_path),
        "pipeline_contract_sha256": state["contract"]["pipeline_contract_sha256"],
        "quality_contract_sha256": state["contract"]["quality_contract_sha256"],
        "implementation_commit_sha": state["implementation"]["repository_commit_sha"],
        "observed_repository_head_sha": observed,
        "orchestrator_version": state["implementation"]["orchestrator_version"],
    }
    payload = {
        "schema_version": "2.0-rc1",
        "action_id": "",
        "issue_id": state["issue_id"],
        "current_stage": lifecycle,
        "target_gate": state["target_gate"],
        "action_kind": action_kind,
        "handler": handler,
        "basis": basis,
        "required_inputs": required_inputs,
        "expected_outputs": expected_outputs,
        "retry_policy": dict(cfg["orchestration"]["retry_policy"]),
        "next_state": next_state,
        "next_terminal_reason": terminal,
    }
    payload["action_id"] = _action_id(payload)
    return payload


def write_action_spec(path: Path, spec: dict[str, Any]) -> Path:
    if path.exists():
        existing = core.load_json(path)
        if existing == spec:
            return path
        raise ValueError(f"refusing to overwrite divergent Action Spec: {path}")
    core.write_json(path, spec)
    return path


def _validate_handler_outputs(repo_root: Path, spec: dict[str, Any], outputs: Any) -> list[dict[str, Any]]:
    if not isinstance(outputs, list):
        raise ValueError("handler must return an output array")
    expected = {row["name"]: row for row in spec["expected_outputs"]}
    actual: dict[str, dict[str, Any]] = {}
    required_fields = {"name", "checkpoint", "path", "sha256"}
    for index, row in enumerate(outputs):
        if not isinstance(row, dict) or set(row) != required_fields:
            raise ValueError(f"handler output[{index}] fields invalid")
        name = row.get("name")
        if name in actual:
            raise ValueError(f"handler returned duplicate output: {name}")
        if name not in expected:
            raise ValueError(f"handler returned unexpected output: {name}")
        contract = expected[name]
        if row.get("checkpoint") != contract.get("checkpoint"):
            raise ValueError(f"handler output checkpoint mismatch: {name}")
        if contract.get("path") is not None and row.get("path") != contract.get("path"):
            raise ValueError(f"handler output path mismatch: {name}")
        path_value = row.get("path")
        sha_value = row.get("sha256")
        if path_value is not None:
            artifact_path = core.repo_local_path(repo_root, path_value, f"Action output {name}")
            if not artifact_path.is_file():
                raise ValueError(f"Action output missing: {path_value}")
            if sha_value != core.sha256_file(artifact_path):
                raise ValueError(f"Action output SHA mismatch: {name}")
        elif sha_value is not None:
            raise ValueError(f"Action output without path cannot claim SHA: {name}")
        actual[name] = row
    missing = sorted(name for name, row in expected.items() if row["required"] and name not in actual)
    if missing:
        raise ValueError(f"handler omitted required outputs: {missing}")
    return [actual[name] for name in sorted(actual)]


def _result_payload(
    spec: dict[str, Any],
    spec_path: Path,
    status: str,
    observed_head_sha: str,
    attempts: int,
    started_at: datetime,
    completed_at: datetime,
    state_before_sha: str,
    state_after_sha: str | None,
    outputs: list[dict[str, Any]],
    error: dict[str, str] | None,
) -> dict[str, Any]:
    return {
        "schema_version": "2.0-rc1",
        "action_id": spec["action_id"],
        "issue_id": spec["issue_id"],
        "action_spec_sha256": core.sha256_file(spec_path),
        "status": status,
        "handler": spec["handler"],
        "implementation_commit_sha": spec["basis"]["implementation_commit_sha"],
        "observed_repository_head_sha": observed_head_sha,
        "attempts": attempts,
        "started_at": core.iso_utc(started_at),
        "completed_at": core.iso_utc(completed_at),
        "state_before_sha256": state_before_sha,
        "state_after_sha256": state_after_sha,
        "outputs": outputs,
        "error": error,
    }


def _transaction_paths(result_path: Path) -> tuple[Path, Path]:
    return Path(str(result_path) + ".pending"), Path(str(result_path) + ".state-next")


def _recover_pending_transaction(state_path: Path, result_path: Path) -> bool:
    pending_result, state_next = _transaction_paths(result_path)
    if result_path.exists():
        if pending_result.exists() or state_next.exists():
            raise ValueError(f"committed Action Result has leftover transaction files: {result_path}")
        return False
    if not pending_result.exists():
        if state_next.exists():
            state_next.unlink()
        return False
    result = core.load_json(pending_result)
    before_sha = result.get("state_before_sha256")
    after_sha = result.get("state_after_sha256")
    if not isinstance(before_sha, str) or not isinstance(after_sha, str):
        raise ValueError("pending Action Result lacks committed state SHA pair")
    current_sha = core.sha256_file(state_path)
    if current_sha == before_sha:
        if not state_next.is_file() or core.sha256_file(state_next) != after_sha:
            raise ValueError("pending Action Result cannot recover missing/divergent next State")
        os.replace(state_next, state_path)
        current_sha = core.sha256_file(state_path)
    elif current_sha == after_sha:
        if state_next.exists():
            state_next.unlink()
    else:
        raise ValueError("pending Action Result does not match current State before/after identity")
    if current_sha != after_sha:
        raise ValueError("State transaction did not reach expected after SHA")
    os.replace(pending_result, result_path)
    return True


def _commit_state_and_result(
    state_path: Path,
    updated_state: dict[str, Any],
    result_path: Path,
    result: dict[str, Any],
) -> None:
    if result_path.exists():
        raise ValueError(f"refusing to overwrite Action Result: {result_path}")
    pending_result, state_next = _transaction_paths(result_path)
    if pending_result.exists() or state_next.exists():
        _recover_pending_transaction(state_path, result_path)
        if result_path.exists():
            raise ValueError(f"Action transaction already committed: {result_path}")
    result_path.parent.mkdir(parents=True, exist_ok=True)
    core.write_json(state_next, updated_state)
    if core.sha256_file(state_next) != result.get("state_after_sha256"):
        state_next.unlink(missing_ok=True)
        raise ValueError("prepared State bytes do not match Action Result state_after_sha256")
    core.write_json(pending_result, result)
    _recover_pending_transaction(state_path, result_path)


def _recover_all_pending(state_path: Path, results_dir: Path) -> None:
    if not results_dir.exists():
        return
    for pending in sorted(results_dir.glob("*.json.pending")):
        _recover_pending_transaction(state_path, Path(str(pending)[:-len(".pending")]))


def execute_action(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    spec_path: Path,
    result_path: Path,
    registry: HandlerRegistry,
    clock: Callable[[], datetime] = _now,
) -> dict[str, Any]:
    _recover_pending_transaction(state_path, result_path)
    if result_path.exists():
        raise ValueError(f"refusing to overwrite Action Result: {result_path}")
    spec = core.load_json(spec_path)
    expected = plan_action(repo_root, cfg, state_path)
    if not _spec_matches_current_plan(spec, expected):
        raise ValueError("Action Spec is stale or does not match current authoritative plan")
    if spec["action_kind"] not in EXECUTABLE_KINDS:
        raise ValueError(f"Action kind {spec['action_kind']} is terminal/non-executable by deterministic dispatcher")
    handler = registry.get(spec["handler"])
    if handler is None:
        raise ValueError(f"registered handler unavailable: {spec['handler']}")

    state = core.load_json(state_path)
    pinned = state["implementation"]["repository_commit_sha"]
    state_before_sha = core.sha256_file(state_path)
    started = clock()
    attempts = 0
    last_error: Exception | None = None
    outputs: list[dict[str, Any]] = []
    max_attempts = spec["retry_policy"]["max_attempts"]
    retryable = spec["retry_policy"]["retryable"]
    while attempts < max_attempts:
        attempts += 1
        try:
            outputs = _validate_handler_outputs(
                repo_root, spec, handler(repo_root, cfg, state, spec, pinned)
            )
            last_error = None
            break
        except Exception as exc:
            last_error = exc
            if not retryable:
                break
    completed = clock()
    observed_after = verify_runtime_implementation(repo_root, cfg, state)
    if last_error is not None:
        status = "RETRYABLE_FAILURE" if retryable else "FAILED"
        result = _result_payload(
            spec, spec_path, status, observed_after, attempts, started, completed,
            state_before_sha, None, [],
            {"kind": type(last_error).__name__, "message": str(last_error)},
        )
        core.write_json(result_path, result)
        return result

    updated = core.transition_state(repo_root, cfg, state, spec["next_state"], pinned, completed)
    for row in outputs:
        checkpoint = row.get("checkpoint")
        if checkpoint is not None:
            if checkpoint not in updated["machine_checkpoints"]:
                raise ValueError(f"Action output references unknown machine checkpoint: {checkpoint}")
            updated["machine_checkpoints"][checkpoint] = "passed"
    updated = refresh_state_control(updated, cfg)
    state_after_sha = core.sha256_bytes(core.json_bytes(updated))
    result = _result_payload(
        spec, spec_path, "SUCCEEDED", observed_after, attempts, started, completed,
        state_before_sha, state_after_sha, outputs, None,
    )
    _commit_state_and_result(state_path, updated, result_path, result)
    return result


def _relative_repo_path(repo_root: Path, path: Path, label: str) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root))
    except ValueError as exc:
        raise ValueError(f"{label} must be inside repository root") from exc


def _required_input_by_name(spec: dict[str, Any], name: str) -> dict[str, Any]:
    rows = [row for row in spec.get("required_inputs", []) if isinstance(row, dict) and row.get("name") == name]
    if len(rows) != 1:
        raise ValueError(f"Human Gate Action Spec must bind exactly one {name} input")
    return rows[0]


def apply_architecture_approval(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    spec_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
    result_path: Path,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
) -> dict[str, Any]:
    _recover_pending_transaction(state_path, result_path)
    if result_path.exists():
        raise ValueError(f"refusing to overwrite Architecture Review Action Result: {result_path}")
    state = core.load_json(state_path)
    observed = verify_runtime_implementation(repo_root, cfg, state)
    expected = plan_action(repo_root, cfg, state_path, observed)
    spec = core.load_json(spec_path)
    if not _spec_matches_current_plan(spec, expected):
        raise ValueError("Architecture Review Action Spec is stale or divergent")
    if spec["action_kind"] != "HUMAN_GATE" or spec["handler"] != "human:architecture-review":
        raise ValueError("current Action Spec is not Architecture Review")
    if state["lifecycle_state"] != "ARCHITECTURE_ESTABLISHED":
        raise ValueError("Architecture approval requires ARCHITECTURE_ESTABLISHED lifecycle")
    if state["machine_checkpoints"].get("architecture") != "passed":
        raise ValueError("Architecture approval requires passed Architecture machine checkpoint")
    if state["human_gates"]["architecture_review"] != "pending":
        raise ValueError("Architecture Review gate is not pending")

    architecture_rel = _relative_repo_path(repo_root, architecture_path, "Architecture")
    review_rel = _relative_repo_path(repo_root, review_summary_path, "Architecture Review Summary")
    architecture_input = _required_input_by_name(spec, "issue-architecture")
    review_input = _required_input_by_name(spec, "architecture-review-summary")
    if architecture_input.get("path") != architecture_rel or architecture_input.get("sha256") != core.sha256_file(architecture_path):
        raise ValueError("Architecture bytes differ from Human Gate Action Spec")
    if review_input.get("path") != review_rel or review_input.get("sha256") != core.sha256_file(review_summary_path):
        raise ValueError("Architecture Review Summary bytes differ from Human Gate Action Spec")

    plan = core.load_json(architecture_path)
    review = core.load_json(review_summary_path)
    if plan.get("issue_id") != state["issue_id"] or plan.get("status") != "PROPOSED":
        raise ValueError("Architecture approval requires exact immutable PROPOSED Architecture for this issue")
    if review.get("issue_id") != state["issue_id"] or review.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise ValueError("Architecture Review Summary is not ready for this issue")
    if review.get("basis", {}).get("architecture_sha256") != core.sha256_file(architecture_path):
        raise ValueError("Architecture Review Summary does not bind exact reviewed Architecture bytes")
    if not isinstance(reviewed_by, str) or not reviewed_by.strip() or not isinstance(review_reference, str) or not review_reference.strip():
        raise ValueError("reviewed_by and review_reference are required")

    approval_seed = {
        "issue_id": state["issue_id"],
        "architecture_sha256": architecture_input["sha256"],
        "review_summary_sha256": review_input["sha256"],
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
    }
    approval = {
        "schema_version": "2.0-rc1",
        "approval_id": f"approval:{state['issue_id']}:{core.sha256_object(approval_seed)[:20]}",
        "issue_id": state["issue_id"],
        "gate": "ARCHITECTURE_REVIEW",
        "decision": "APPROVED",
        "architecture_sha256": architecture_input["sha256"],
        "architecture_review_summary_sha256": review_input["sha256"],
        "reviewed_by": reviewed_by,
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
    }
    approval_errors = drafting.validate_architecture_approval(
        approval, architecture_path, review_summary_path, state["issue_id"]
    )
    if approval_errors:
        raise ValueError("Architecture Approval Record invalid: " + "; ".join(approval_errors))
    if approval_path.exists():
        if core.load_json(approval_path) != approval:
            raise ValueError("refusing to overwrite divergent Architecture Approval Record")
    else:
        core.write_json(approval_path, approval)

    before_sha = core.sha256_file(state_path)
    updated = deepcopy(state)
    updated["human_gates"]["architecture_review"] = "approved"
    if updated["target_gate"] == "ARCHITECTURE_REVIEW":
        updated["target_gate"] = "PUBLICATION_PREVIEW"
    updated = refresh_state_control(updated, cfg)
    after_sha = core.sha256_bytes(core.json_bytes(updated))
    output = {
        "name": "architecture-approval-record",
        "checkpoint": None,
        "path": _relative_repo_path(repo_root, approval_path, "Architecture Approval Record"),
        "sha256": core.sha256_file(approval_path),
    }
    result = _result_payload(
        spec, spec_path, "SUCCEEDED", observed, 1, reviewed_at, reviewed_at,
        before_sha, after_sha, [output], None,
    )
    _commit_state_and_result(state_path, updated, result_path, result)
    return result


def advance_to_gate(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    orchestration_dir: Path,
    registry: HandlerRegistry,
    clock: Callable[[], datetime] = _now,
    max_actions: int = 64,
) -> dict[str, Any]:
    specs_dir = orchestration_dir / "specs"
    results_dir = orchestration_dir / "results"
    specs_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)
    _recover_all_pending(state_path, results_dir)
    executed = 0
    while executed < max_actions:
        spec = plan_action(repo_root, cfg, state_path)
        sequence = len(list(specs_dir.glob("*.json"))) + 1
        safe_id = spec["action_id"].replace(":", "-")
        spec_path = specs_dir / f"{sequence:03d}-{safe_id}.json"
        write_action_spec(spec_path, spec)
        if spec["action_kind"] in TERMINAL_KINDS:
            return {
                "terminal_reason": spec["next_terminal_reason"],
                "action_spec_path": _relative_repo_path(repo_root, spec_path, "terminal Action Spec"),
                "executed_actions": executed,
            }
        result_path = results_dir / f"{sequence:03d}-{safe_id}.json"
        result = execute_action(repo_root, cfg, state_path, spec_path, result_path, registry, clock)
        if result["status"] != "SUCCEEDED":
            raise ValueError(
                f"deterministic action failed without creating a Human Gate: {spec['action_id']} status={result['status']}"
            )
        executed += 1
    raise ValueError(f"advance-to-gate exceeded max_actions={max_actions}; orchestration cycle suspected")


def load_handler_module(module_name: str, registry: HandlerRegistry) -> None:
    module = importlib.import_module(module_name)
    register = getattr(module, "register_handlers", None)
    if not callable(register):
        raise ValueError(f"handler module must expose register_handlers(registry): {module_name}")
    register(registry)


def _path(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(core.DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan")
    plan.add_argument("--state", required=True)
    plan.add_argument("--output")

    advance = sub.add_parser("advance-to-gate")
    advance.add_argument("--state", required=True)
    advance.add_argument("--orchestration-dir", required=True)
    advance.add_argument("--handler-module", action="append", default=[])

    approve = sub.add_parser("approve-architecture")
    for key in ("state", "action-spec", "architecture", "review-summary", "approval", "result"):
        approve.add_argument(f"--{key}", required=True)
    approve.add_argument("--reviewed-by", required=True)
    approve.add_argument("--reviewed-at", required=True)
    approve.add_argument("--review-reference", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.repo_root).resolve()
    cfg = core.load_json(_path(root, args.config))
    try:
        if args.command == "plan":
            spec = plan_action(root, cfg, _path(root, args.state))
            if args.output:
                output = _path(root, args.output)
                write_action_spec(output, spec)
                print(output)
            else:
                print(json.dumps(spec, ensure_ascii=False, indent=2))
            return 0
        if args.command == "advance-to-gate":
            registry: HandlerRegistry = {}
            for module_name in args.handler_module:
                load_handler_module(module_name, registry)
            result = advance_to_gate(
                root, cfg, _path(root, args.state), _path(root, args.orchestration_dir), registry
            )
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        if args.command == "approve-architecture":
            result = apply_architecture_approval(
                root,
                cfg,
                _path(root, args.state),
                _path(root, args.action_spec),
                _path(root, args.architecture),
                _path(root, args.review_summary),
                _path(root, args.approval),
                _path(root, args.result),
                args.reviewed_by,
                core.parse_instant(args.reviewed_at),
                args.review_reference,
            )
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
