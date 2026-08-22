#!/usr/bin/env python3
"""Agent-first production control for Survey Production Core v2.

ChatGPT is the research/editorial operator. This module provides the minimum
repository control needed to make that work resumable and provenance-aware:

- one compact Stage Checkpoint per local/model-assisted lifecycle transition;
- per-stage implementation/contract provenance, allowing reviewed tool upgrades;
- direct exact-byte Architecture Review and Publication Preview approvals;
- no Action Spec / Handoff / Action Result ceremony on the normal local path.

Richer workflow/reconciliation authority remains appropriate at external and
irreversible boundaries such as public Release.
"""
from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_schema_v2 as schema_gate

CHECKPOINT_SCHEMA = Path("schemas/stage-checkpoint-v2.schema.json")
STATE_SCHEMA = Path("schemas/survey-production-state.schema.json")
REVIEW_KINDS = {"DETERMINISTIC", "AGENT_RESEARCH", "AGENT_EDITORIAL", "AGENT_VISUAL"}


class AgentControlError(ValueError):
    pass


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _rel(repo_root: Path, path: Path, label: str) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root))
    except ValueError as exc:
        raise AgentControlError(f"{label} must be repository-local: {path}") from exc


def _authority(repo_root: Path, path: Path, label: str) -> dict[str, str]:
    rel = _rel(repo_root, path, label)
    resolved = core.repo_local_path(repo_root, rel, label)
    if resolved.is_symlink() or not resolved.is_file():
        raise AgentControlError(f"{label} missing or unsafe: {rel}")
    return {"path": rel, "sha256": core.sha256_file(resolved)}


def _named_authority(repo_root: Path, name: str, path: Path) -> dict[str, str]:
    if not isinstance(name, str) or not name.strip():
        raise AgentControlError("artifact name must be non-empty")
    return {"name": name, **_authority(repo_root, path, f"stage artifact {name}")}


def _profile_and_source(repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]) -> tuple[Path, dict[str, Any], Path]:
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "state.profile.path")
    if not profile_path.is_file() or core.sha256_file(profile_path) != state["profile"]["sha256"]:
        raise AgentControlError("Production Profile bytes differ from initialized State authority")
    profile = core.load_json(profile_path)
    errors = core.validate_profile(profile, cfg)
    if errors:
        raise AgentControlError("Production Profile invalid under current tool: " + "; ".join(errors))
    if profile.get("issue_id") != state.get("issue_id"):
        raise AgentControlError("Production Profile/State issue identity mismatch")
    if profile.get("research_profile") != state.get("research_profile") or profile.get("publication_profile") != state.get("publication_profile"):
        raise AgentControlError("Production Profile/State Profile identity mismatch")
    if profile.get("contract") != state.get("contract"):
        raise AgentControlError("Production State no longer binds its initialization Profile contract")
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    return profile_path, profile, source_root


def _expected_completed_checkpoints(cfg: dict[str, Any], lifecycle: str) -> set[str]:
    index = core.LIFECYCLE.index(lifecycle)
    result: set[str] = set()
    for state_name in core.LIFECYCLE[:index]:
        stage = cfg["orchestration"]["stage_plan"].get(state_name)
        if isinstance(stage, dict):
            result.update(stage.get("checkpoints", []))
    return result


def _producer_for_checkpoint(cfg: dict[str, Any], checkpoint: str) -> tuple[str, str] | None:
    for from_state, stage in cfg["orchestration"]["stage_plan"].items():
        if checkpoint in stage.get("checkpoints", []):
            return from_state, stage["next_state"]
    return None


def _validate_checkpoint_record(repo_root: Path, cfg: dict[str, Any], state: dict[str, Any], checkpoint: str, authority: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(authority, dict) or set(authority) != {"path", "sha256"}:
        return [f"checkpoint {checkpoint} provenance fields invalid"]
    try:
        path = core.repo_local_path(repo_root, authority["path"], f"checkpoint {checkpoint}")
    except (TypeError, ValueError) as exc:
        return [str(exc)]
    if not path.is_file():
        return [f"checkpoint {checkpoint} provenance file missing"]
    if core.sha256_file(path) != authority.get("sha256"):
        return [f"checkpoint {checkpoint} provenance SHA drift"]
    try:
        record = schema_gate.load_and_validate_json(path, repo_root / CHECKPOINT_SCHEMA, label=f"Stage Checkpoint {checkpoint}")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)]
    producer = _producer_for_checkpoint(cfg, checkpoint)
    if producer is None:
        return [f"checkpoint {checkpoint} has no lifecycle producer"]
    from_state, to_state = producer
    if record.get("issue_id") != state.get("issue_id"):
        errors.append(f"checkpoint {checkpoint} issue identity mismatch")
    if record.get("from_state") != from_state or record.get("to_state") != to_state:
        errors.append(f"checkpoint {checkpoint} lifecycle producer mismatch")
    if checkpoint not in record.get("checkpoints", []):
        errors.append(f"checkpoint {checkpoint} missing from Stage Checkpoint record")
    for artifact in record.get("artifacts", []):
        try:
            resolved = core.repo_local_path(repo_root, artifact["path"], f"checkpoint artifact {artifact['name']}")
        except (TypeError, ValueError) as exc:
            errors.append(str(exc))
            continue
        if not resolved.is_file() or core.sha256_file(resolved) != artifact.get("sha256"):
            errors.append(f"Stage Checkpoint artifact drift: {artifact.get('name')}")
    for row in record.get("reviews", []):
        if row.get("kind") == "DETERMINISTIC":
            result = row.get("result")
            if not isinstance(result, dict):
                errors.append(f"deterministic review lacks result authority: {row.get('check_id')}")
                continue
            try:
                result_path = core.repo_local_path(repo_root, result["path"], f"review result {row.get('check_id')}")
            except (TypeError, ValueError) as exc:
                errors.append(str(exc))
                continue
            if not result_path.is_file() or core.sha256_file(result_path) != result.get("sha256"):
                errors.append(f"deterministic review result drift: {row.get('check_id')}")
    return errors


def validate_agent_state(repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]) -> list[str]:
    """Validate resumable State without globally pinning the edition tool commit.

    State.contract and State.implementation preserve initialization provenance.
    Each completed stage separately pins the implementation and current contract
    used at that boundary through its Stage Checkpoint record.
    """
    errors: list[str] = []
    try:
        schema_gate.validate_instance(state, repo_root / STATE_SCHEMA, label="Production State")
    except ValueError as exc:
        return [str(exc)]
    if state.get("lifecycle_state") not in core.LIFECYCLE:
        return ["Production State lifecycle_state invalid"]
    try:
        _, profile, source_root = _profile_and_source(repo_root, cfg, state)
    except (OSError, ValueError, KeyError) as exc:
        return [str(exc)]

    legacy = state.get("legacy_compatibility", {})
    try:
        legacy_path = core.repo_local_path(repo_root, legacy["legacy_state_path"], "legacy_state_path")
    except (KeyError, TypeError, ValueError) as exc:
        errors.append(str(exc))
    else:
        present = legacy_path.is_file()
        digest = core.sha256_file(legacy_path) if present else None
        if present != legacy.get("legacy_state_present") or digest != legacy.get("legacy_state_sha256"):
            errors.append("legacy compatibility artifact changed after v2 initialization")

    expected = _expected_completed_checkpoints(cfg, state["lifecycle_state"])
    if state.get("human_gates", {}).get("publication_preview") == "approved":
        expected.add("publication_preview")
    checkpoints = state.get("machine_checkpoints", {})
    provenance = state.get("checkpoint_provenance", {})
    for name in core.CHECKPOINTS:
        wanted = "passed" if name in expected else "pending"
        if checkpoints.get(name) != wanted:
            errors.append(f"Production State checkpoint {name}={checkpoints.get(name)!r}; expected {wanted!r}")
        authority = provenance.get(name)
        if name == "publication_preview" and wanted == "passed":
            if not isinstance(authority, dict):
                errors.append("Publication Preview checkpoint lacks approval provenance")
            else:
                approval_path = source_root / cfg["state_authority"]["publication_preview_approval_path"]
                if authority.get("path") != _rel(repo_root, approval_path, "Publication Preview approval"):
                    errors.append("Publication Preview checkpoint provenance path is not canonical")
                elif not approval_path.is_file() or core.sha256_file(approval_path) != authority.get("sha256"):
                    errors.append("Publication Preview checkpoint approval provenance drift")
                else:
                    try:
                        publication.validate_preview_approval(repo_root, approval_path, issue_id=state["issue_id"])
                    except ValueError as exc:
                        errors.append(str(exc))
        elif wanted == "passed":
            if authority is None:
                errors.append(f"passed checkpoint lacks Stage Checkpoint provenance: {name}")
            else:
                errors.extend(_validate_checkpoint_record(repo_root, cfg, state, name, authority))
        elif authority is not None:
            errors.append(f"pending checkpoint must not carry provenance: {name}")

    index = core.LIFECYCLE.index(state["lifecycle_state"])
    history = state.get("history")
    if not isinstance(history, list) or len(history) != index + 1:
        errors.append("Production State history length must exactly match lifecycle position")
    else:
        previous: datetime | None = None
        for row_index, row in enumerate(history):
            expected_to = core.LIFECYCLE[row_index]
            expected_from = None if row_index == 0 else core.LIFECYCLE[row_index - 1]
            if not isinstance(row, dict) or row.get("from") != expected_from or row.get("to") != expected_to:
                errors.append(f"Production State history[{row_index}] lifecycle path invalid")
                continue
            sha = row.get("repository_commit_sha")
            if not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
                errors.append(f"Production State history[{row_index}] implementation SHA invalid")
            try:
                instant = core.parse_instant(str(row.get("recorded_at", "")))
                if previous is not None and instant < previous:
                    errors.append("Production State history timestamps must be monotonic")
                previous = instant
            except ValueError:
                errors.append(f"Production State history[{row_index}].recorded_at invalid")

    gate_provenance = state.get("human_gate_provenance", {})
    current_index = core.LIFECYCLE.index(state["lifecycle_state"])
    arch_index = core.LIFECYCLE.index("ARCHITECTURE_ESTABLISHED")
    arch_status = state.get("human_gates", {}).get("architecture_review")
    arch_auth = gate_provenance.get("architecture_review")
    if current_index < arch_index and arch_status != "pending":
        errors.append("Architecture Review cannot resolve before ARCHITECTURE_ESTABLISHED")
    if current_index > arch_index and arch_status != "approved":
        errors.append("post-Architecture lifecycle requires approved Architecture Review")
    if arch_status == "pending":
        if arch_auth is not None:
            errors.append("pending Architecture Review must not carry provenance")
    else:
        approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
        if not isinstance(arch_auth, dict) or arch_auth.get("path") != _rel(repo_root, approval_path, "Architecture approval"):
            errors.append("resolved Architecture Review lacks canonical approval provenance")
        elif not approval_path.is_file() or core.sha256_file(approval_path) != arch_auth.get("sha256"):
            errors.append("Architecture approval provenance drift")
        elif arch_status == "approved":
            architecture = source_root / "architecture-v2.json"
            summary = source_root / "architecture-review-summary-v2.json"
            if not architecture.is_file() or not summary.is_file():
                errors.append("approved Architecture Review lacks canonical review bytes")
            else:
                try:
                    approval = core.load_json(approval_path)
                    approval_errors = drafting.validate_architecture_approval(approval, architecture, summary, state["issue_id"])
                    errors.extend(approval_errors)
                except (OSError, ValueError, json.JSONDecodeError) as exc:
                    errors.append(str(exc))

    pub_index = core.LIFECYCLE.index("RELEASE_CANDIDATE")
    pub_status = state.get("human_gates", {}).get("publication_preview")
    if current_index < pub_index and pub_status != "pending":
        errors.append("Publication Preview cannot resolve before RELEASE_CANDIDATE")
    if current_index > pub_index and pub_status != "approved":
        errors.append("post-Publication Preview lifecycle requires approved Publication Preview")

    try:
        expected_action, expected_terminal = core.derive_control_fields(state, cfg)
    except (KeyError, ValueError) as exc:
        errors.append(f"Production State controller fields cannot be derived: {exc}")
    else:
        if state.get("next_action") != expected_action:
            errors.append(f"Production State next_action drift: {state.get('next_action')!r} != {expected_action!r}")
        if state.get("terminal_reason") != expected_terminal:
            errors.append(f"Production State terminal_reason drift: {state.get('terminal_reason')!r} != {expected_terminal!r}")
    return errors


def verify_agent_state_basis(repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]) -> None:
    errors = validate_agent_state(repo_root, cfg, state)
    if errors:
        raise AgentControlError("Production State is not safely resumable: " + "; ".join(errors))


def canonical_checkpoint_path(repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]) -> Path:
    _, _, source_root = _profile_and_source(repo_root, cfg, state)
    return source_root / cfg["state_authority"]["agent_checkpoint_dir"] / f"{state['lifecycle_state']}.json"


def _expand_stage_path(template: str, profile: dict[str, Any]) -> str:
    value = template.replace("{source_root}", profile["paths"]["source_root"])
    if "{" in value or "}" in value:
        raise AgentControlError(f"unsupported stage path template: {template}")
    return value


def _validate_stage_artifacts(repo_root: Path, cfg: dict[str, Any], state: dict[str, Any], profile: dict[str, Any], artifacts: list[dict[str, str]]) -> None:
    names = [row["name"] for row in artifacts]
    if len(names) != len(set(names)):
        raise AgentControlError("Stage Checkpoint artifact names must be unique")
    stage = cfg["orchestration"]["stage_plan"].get(state["lifecycle_state"])
    if not isinstance(stage, dict):
        raise AgentControlError(f"no lifecycle stage configured for {state['lifecycle_state']}")
    by_name = {row["name"]: row for row in artifacts}
    for configured in stage.get("artifacts", []):
        name = configured["name"]
        row = by_name.get(name)
        if row is None:
            raise AgentControlError(f"Stage Checkpoint missing configured canonical artifact: {name}")
        expected_path = _expand_stage_path(configured["path"], profile)
        if row["path"] != expected_path:
            raise AgentControlError(f"Stage Checkpoint artifact path is not canonical for {name}: {expected_path}")


def _load_reviews(repo_root: Path, path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    payload = core.load_json(path)
    rows = payload.get("reviews")
    if not isinstance(rows, list):
        raise AgentControlError("review file must contain a reviews array")
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise AgentControlError(f"reviews[{index}] must be an object")
        allowed = {"check_id", "kind", "executor", "evidence", "result_path"}
        if set(row) - allowed:
            raise AgentControlError(f"reviews[{index}] has unsupported fields")
        check_id = row.get("check_id")
        kind = row.get("kind")
        executor = row.get("executor")
        evidence_text = row.get("evidence")
        if not isinstance(check_id, str) or not check_id.strip() or check_id in seen:
            raise AgentControlError(f"reviews[{index}].check_id must be unique and non-empty")
        seen.add(check_id)
        if kind not in REVIEW_KINDS:
            raise AgentControlError(f"reviews[{index}].kind invalid")
        if not isinstance(executor, str) or not executor.strip() or not isinstance(evidence_text, str) or not evidence_text.strip():
            raise AgentControlError(f"reviews[{index}] executor/evidence required")
        result_path_value = row.get("result_path")
        result_ref = None
        if kind == "DETERMINISTIC":
            if not isinstance(result_path_value, str) or not result_path_value:
                raise AgentControlError(f"deterministic review {check_id} requires result_path")
            result_ref = _authority(repo_root, core.repo_local_path(repo_root, result_path_value, f"review result {check_id}"), f"review result {check_id}")
        elif result_path_value is not None:
            raise AgentControlError(f"agent review {check_id} must not claim deterministic result_path")
        result.append({
            "check_id": check_id,
            "kind": kind,
            "status": "PASS",
            "executor": executor,
            "evidence": evidence_text,
            "result": result_ref,
        })
    return result


def build_stage_checkpoint(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    artifacts: dict[str, Path],
    reviews_path: Path | None,
    summary: str,
    recorded_at: datetime,
    implementation_sha: str | None = None,
) -> Path:
    state = core.load_json(state_path)
    verify_agent_state_basis(repo_root, cfg, state)
    if state.get("terminal_reason") is not None:
        raise AgentControlError(f"cannot advance while State is terminal: {state['terminal_reason']}")
    stage = cfg["orchestration"]["stage_plan"].get(state["lifecycle_state"])
    if not isinstance(stage, dict):
        raise AgentControlError(f"no stage configured for {state['lifecycle_state']}")
    if stage.get("action_kind") == "WORKFLOW_DISPATCH":
        raise AgentControlError("external WORKFLOW_DISPATCH stage must use its dedicated workflow")
    if not isinstance(summary, str) or not summary.strip():
        raise AgentControlError("Stage Checkpoint summary required")
    _, profile, _ = _profile_and_source(repo_root, cfg, state)
    artifact_rows = [_named_authority(repo_root, name, path) for name, path in sorted(artifacts.items())]
    _validate_stage_artifacts(repo_root, cfg, state, profile, artifact_rows)
    reviews = _load_reviews(repo_root, reviews_path)
    if not reviews:
        raise AgentControlError("Stage Checkpoint requires at least one deterministic or ChatGPT review row")
    impl = core.repository_commit_sha(repo_root, implementation_sha)
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": state["issue_id"],
        "from_state": state["lifecycle_state"],
        "to_state": stage["next_state"],
        "checkpoints": list(stage.get("checkpoints", [])),
        "recorded_at": core.iso_utc(recorded_at),
        "implementation": {
            "repository_commit_sha": impl,
            "orchestrator_version": cfg["orchestrator_version"],
        },
        "contract": core.contract_identity(repo_root, cfg, state["research_profile"], state["publication_profile"]),
        "artifacts": artifact_rows,
        "reviews": reviews,
        "summary": summary,
    }
    schema_gate.validate_instance(payload, repo_root / CHECKPOINT_SCHEMA, label="Agent Stage Checkpoint")
    path = canonical_checkpoint_path(repo_root, cfg, state)
    if path.exists():
        if core.load_json(path) != payload:
            raise AgentControlError(f"refusing divergent Stage Checkpoint overwrite: {path}")
    else:
        core.write_json(path, payload)
    return path


def advance_with_checkpoint(repo_root: Path, cfg: dict[str, Any], state_path: Path, checkpoint_path: Path) -> dict[str, Any]:
    state = core.load_json(state_path)
    verify_agent_state_basis(repo_root, cfg, state)
    canonical = canonical_checkpoint_path(repo_root, cfg, state)
    if checkpoint_path.resolve() != canonical.resolve():
        raise AgentControlError(f"Stage Checkpoint must use canonical path: {_rel(repo_root, canonical, 'Stage Checkpoint')}")
    record = schema_gate.load_and_validate_json(checkpoint_path, repo_root / CHECKPOINT_SCHEMA, label="Agent Stage Checkpoint")
    stage = cfg["orchestration"]["stage_plan"].get(state["lifecycle_state"])
    if not isinstance(stage, dict):
        raise AgentControlError(f"no stage configured for {state['lifecycle_state']}")
    if record["issue_id"] != state["issue_id"] or record["from_state"] != state["lifecycle_state"] or record["to_state"] != stage["next_state"]:
        raise AgentControlError("Stage Checkpoint does not match current lifecycle")
    if set(record["checkpoints"]) != set(stage.get("checkpoints", [])):
        raise AgentControlError("Stage Checkpoint checkpoint set does not match lifecycle contract")
    current_contract = core.contract_identity(repo_root, cfg, state["research_profile"], state["publication_profile"])
    if record["contract"] != current_contract:
        raise AgentControlError("Stage Checkpoint was not reviewed under the current repository contract")
    current_impl = core.repository_commit_sha(repo_root)
    if record["implementation"]["repository_commit_sha"] != current_impl or record["implementation"]["orchestrator_version"] != cfg["orchestrator_version"]:
        raise AgentControlError("Stage Checkpoint implementation identity differs from current executing tool")
    _, profile, _ = _profile_and_source(repo_root, cfg, state)
    _validate_stage_artifacts(repo_root, cfg, state, profile, record["artifacts"])
    authority = _authority(repo_root, checkpoint_path, "Stage Checkpoint")
    updated = deepcopy(state)
    for checkpoint in stage.get("checkpoints", []):
        updated["machine_checkpoints"][checkpoint] = "passed"
        updated["checkpoint_provenance"][checkpoint] = deepcopy(authority)
    current = state["lifecycle_state"]
    updated["lifecycle_state"] = stage["next_state"]
    updated["history"].append({
        "from": current,
        "to": stage["next_state"],
        "recorded_at": record["recorded_at"],
        "repository_commit_sha": current_impl,
    })
    updated = core.refresh_state_control(updated, cfg)
    errors = validate_agent_state(repo_root, cfg, updated)
    if errors:
        raise AgentControlError("refusing inconsistent agent-first transition: " + "; ".join(errors))
    core.write_json(state_path, updated)
    return updated


def approve_architecture(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
) -> dict[str, Any]:
    state = core.load_json(state_path)
    verify_agent_state_basis(repo_root, cfg, state)
    if state["lifecycle_state"] != "ARCHITECTURE_ESTABLISHED" or state["human_gates"]["architecture_review"] != "pending":
        raise AgentControlError("Architecture approval requires pending ARCHITECTURE_ESTABLISHED Human Gate")
    if state["machine_checkpoints"].get("architecture") != "passed":
        raise AgentControlError("Architecture approval requires completed Architecture checkpoint")
    if not reviewed_by.strip() or not review_reference.strip():
        raise AgentControlError("reviewed_by and review_reference are required")
    _, _, source_root = _profile_and_source(repo_root, cfg, state)
    architecture = source_root / "architecture-v2.json"
    review = source_root / "architecture-review-summary-v2.json"
    attention = source_root / "architecture-review-attention-v2.json"
    for path, label in ((architecture, "Architecture"), (review, "Architecture Review Summary"), (attention, "Architecture Review Attention")):
        if not path.is_file():
            raise AgentControlError(f"{label} missing: {path}")
    review_attention.validate_attention(repo_root, attention)
    plan = core.load_json(architecture)
    summary = core.load_json(review)
    if plan.get("issue_id") != state["issue_id"] or plan.get("status") != "PROPOSED":
        raise AgentControlError("Architecture Human Gate requires immutable PROPOSED Architecture for this issue")
    if summary.get("issue_id") != state["issue_id"] or summary.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise AgentControlError("Architecture Review Summary is not ready for this issue")
    if summary.get("basis", {}).get("architecture_sha256") != core.sha256_file(architecture):
        raise AgentControlError("Architecture Review Summary does not bind exact Architecture bytes")
    approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
    seed = {
        "issue_id": state["issue_id"],
        "architecture_sha256": core.sha256_file(architecture),
        "review_summary_sha256": core.sha256_file(review),
        "review_attention_sha256": core.sha256_file(attention),
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
    }
    approval = {
        "schema_version": "2.0-rc1",
        "approval_id": f"approval:{state['issue_id']}:{core.sha256_object(seed)[:20]}",
        "issue_id": state["issue_id"],
        "gate": "ARCHITECTURE_REVIEW",
        "decision": "APPROVED",
        "architecture_sha256": core.sha256_file(architecture),
        "architecture_review_summary_sha256": core.sha256_file(review),
        "architecture_review_attention_sha256": core.sha256_file(attention),
        "reviewed_by": reviewed_by,
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
    }
    approval_errors = drafting.validate_architecture_approval(approval, architecture, review, state["issue_id"])
    if approval_errors:
        raise AgentControlError("Architecture Approval Record invalid: " + "; ".join(approval_errors))
    if approval_path.exists() and core.load_json(approval_path) != approval:
        raise AgentControlError("refusing divergent Architecture Approval overwrite")
    if not approval_path.exists():
        core.write_json(approval_path, approval)
    updated = deepcopy(state)
    updated["human_gates"]["architecture_review"] = "approved"
    updated["human_gate_provenance"]["architecture_review"] = _authority(repo_root, approval_path, "Architecture approval")
    updated = core.refresh_state_control(updated, cfg)
    errors = validate_agent_state(repo_root, cfg, updated)
    if errors:
        raise AgentControlError("refusing inconsistent Architecture approval State: " + "; ".join(errors))
    core.write_json(state_path, updated)
    return updated


def approve_publication_preview(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
) -> dict[str, Any]:
    state = core.load_json(state_path)
    verify_agent_state_basis(repo_root, cfg, state)
    if state["lifecycle_state"] != "RELEASE_CANDIDATE" or state["human_gates"]["publication_preview"] != "pending":
        raise AgentControlError("Publication Preview approval requires pending RELEASE_CANDIDATE Human Gate")
    if not reviewed_by.strip() or not review_reference.strip():
        raise AgentControlError("reviewed_by and review_reference are required")
    _, _, source_root = _profile_and_source(repo_root, cfg, state)
    candidate = source_root / "publication/v2/publication-candidate-v2.json"
    if not candidate.is_file():
        raise AgentControlError("canonical Publication Candidate missing")
    publication.validate_candidate(repo_root, candidate, issue_id=state["issue_id"])
    approval_path = source_root / cfg["state_authority"]["publication_preview_approval_path"]
    publication.build_preview_approval(repo_root, candidate, approval_path, reviewed_by, reviewed_at, review_reference)
    updated = deepcopy(state)
    updated["human_gates"]["publication_preview"] = "approved"
    approval_authority = _authority(repo_root, approval_path, "Publication Preview approval")
    updated["human_gate_provenance"]["publication_preview"] = deepcopy(approval_authority)
    updated["machine_checkpoints"]["publication_preview"] = "passed"
    updated["checkpoint_provenance"]["publication_preview"] = deepcopy(approval_authority)
    updated = core.refresh_state_control(updated, cfg)
    errors = validate_agent_state(repo_root, cfg, updated)
    if errors:
        raise AgentControlError("refusing inconsistent Publication Preview approval State: " + "; ".join(errors))
    core.write_json(state_path, updated)
    return updated


def _parse_artifacts(repo_root: Path, values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        if "=" not in value:
            raise AgentControlError("--artifact must use NAME=PATH")
        name, raw = value.split("=", 1)
        if not name or not raw or name in result:
            raise AgentControlError("--artifact names/paths must be unique and non-empty")
        result[name] = core.repo_local_path(repo_root, raw, f"artifact {name}")
    return result


def _path(repo_root: Path, value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (repo_root / path).resolve()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(core.DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-state")
    validate.add_argument("--state", required=True)

    stage = sub.add_parser("advance-stage")
    stage.add_argument("--state", required=True)
    stage.add_argument("--artifact", action="append", default=[])
    stage.add_argument("--reviews", required=True)
    stage.add_argument("--summary", required=True)
    stage.add_argument("--recorded-at")
    stage.add_argument("--implementation-sha")

    approve_a = sub.add_parser("approve-architecture")
    approve_a.add_argument("--state", required=True)
    approve_a.add_argument("--reviewed-by", required=True)
    approve_a.add_argument("--reviewed-at", required=True)
    approve_a.add_argument("--review-reference", required=True)

    approve_p = sub.add_parser("approve-publication-preview")
    approve_p.add_argument("--state", required=True)
    approve_p.add_argument("--reviewed-by", required=True)
    approve_p.add_argument("--reviewed-at", required=True)
    approve_p.add_argument("--review-reference", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.repo_root).resolve()
    cfg = core.load_json(_path(root, args.config))
    state_path = _path(root, args.state)
    try:
        if args.command == "validate-state":
            errors = validate_agent_state(root, cfg, core.load_json(state_path))
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        if args.command == "advance-stage":
            when = core.parse_instant(args.recorded_at) if args.recorded_at else _now()
            checkpoint = build_stage_checkpoint(
                root, cfg, state_path,
                _parse_artifacts(root, args.artifact),
                _path(root, args.reviews), args.summary, when, args.implementation_sha,
            )
            state = advance_with_checkpoint(root, cfg, state_path, checkpoint)
            print(json.dumps({"checkpoint": _rel(root, checkpoint, "Stage Checkpoint"), "state": state}, ensure_ascii=False, indent=2))
            return 0
        if args.command == "approve-architecture":
            state = approve_architecture(root, cfg, state_path, args.reviewed_by, core.parse_instant(args.reviewed_at), args.review_reference)
            print(json.dumps(state, ensure_ascii=False, indent=2))
            return 0
        if args.command == "approve-publication-preview":
            state = approve_publication_preview(root, cfg, state_path, args.reviewed_by, core.parse_instant(args.reviewed_at), args.review_reference)
            print(json.dumps(state, ensure_ascii=False, indent=2))
            return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
