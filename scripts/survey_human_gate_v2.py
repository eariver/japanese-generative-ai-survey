#!/usr/bin/env python3
"""Canonical Human Gate round-trip protocol for Survey Production Core v2.

Human judgment remains external. This module only records an explicit Human
APPROVED or REQUEST_CHANGES decision against exact reviewed bytes and applies
the deterministic lifecycle consequence.

APPROVED delegates to the existing exact-byte approval recorders. A routine
REQUEST_CHANGES decision records immutable review provenance, selectively
invalidates downstream checkpoint authority, removes only superseded canonical
authority that would block regeneration, and returns Production State to an
allowed regeneration boundary. Publication Preview corrections may explicitly
reopen Architecture Review when the Human-selected boundary is upstream of the
approved Architecture. This module never chooses the decision or boundary.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_schema_v2 as schema_gate

REVIEW_RECORD_SCHEMA = Path("schemas/human-gate-review-record-v2.schema.json")
REVIEW_INDEX_SCHEMA = Path("schemas/human-gate-review-index-v2.schema.json")
GATE_KEYS = {
    "ARCHITECTURE_REVIEW": "architecture_review",
    "PUBLICATION_PREVIEW": "publication_preview",
}
GATE_STATES = {
    "ARCHITECTURE_REVIEW": "ARCHITECTURE_ESTABLISHED",
    "PUBLICATION_PREVIEW": "RELEASE_CANDIDATE",
}
GATE_SLUGS = {
    "ARCHITECTURE_REVIEW": "architecture",
    "PUBLICATION_PREVIEW": "publication",
}


class HumanGateError(ValueError):
    pass


def _rel(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError as exc:
        raise HumanGateError(f"path escapes repository: {path}") from exc


def _authority(repo_root: Path, path: Path) -> dict[str, str]:
    if path.is_symlink() or not path.is_file():
        raise HumanGateError(f"authority file missing or unsafe: {_rel(repo_root, path)}")
    return {"path": _rel(repo_root, path), "sha256": core.sha256_file(path)}


def _named_authority(repo_root: Path, name: str, path: Path) -> dict[str, str]:
    return {"name": name, **_authority(repo_root, path)}


def _state_context(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], Path]:
    state = core.load_json(state_path)
    agent.verify_agent_state_basis(repo_root, cfg, state)
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "Production Profile")
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    expected_state = source_root / cfg["state_authority"]["authoritative_filename"]
    if state_path.resolve() != expected_state.resolve():
        raise HumanGateError("Human Gate protocol requires canonical Production State path")
    return state, profile, source_root


def _review_dir(source_root: Path, cfg: dict[str, Any]) -> Path:
    return source_root / cfg["state_authority"]["human_review_dir"]


def review_index_path(source_root: Path, cfg: dict[str, Any]) -> Path:
    return source_root / cfg["state_authority"]["human_review_index_path"]


def review_record_path(
    source_root: Path,
    cfg: dict[str, Any],
    gate: str,
    revision: int,
) -> Path:
    return _review_dir(source_root, cfg) / f"{GATE_SLUGS[gate]}-r{revision}.json"


def approval_snapshot_path(
    source_root: Path,
    cfg: dict[str, Any],
    gate: str,
    revision: int,
) -> Path:
    return _review_dir(source_root, cfg) / "approvals" / f"{GATE_SLUGS[gate]}-r{revision}.json"


def _reopens_architecture(regeneration_boundary: str | None) -> bool:
    if regeneration_boundary is None:
        return False
    return core.LIFECYCLE.index(regeneration_boundary) < core.LIFECYCLE.index("ARCHITECTURE_ESTABLISHED")


def _validate_review_index_semantics(
    repo_root: Path,
    payload: dict[str, Any],
    expected_issue_id: str,
) -> None:
    if payload.get("issue_id") != expected_issue_id:
        raise HumanGateError("Human Gate review index issue identity mismatch")
    expected_revision = {gate: 1 for gate in GATE_KEYS}
    approved_active = {gate: False for gate in GATE_KEYS}
    for row in payload.get("reviews", []):
        gate = row["gate"]
        revision = row["revision"]
        if approved_active[gate]:
            raise HumanGateError(f"Human Gate review index has review after active APPROVED decision: {gate}")
        if revision != expected_revision[gate]:
            raise HumanGateError(
                f"Human Gate review revisions must be contiguous for {gate}: expected {expected_revision[gate]}, got {revision}"
            )
        expected_revision[gate] += 1
        record_ref = row["record"]
        record_path = core.repo_local_path(repo_root, record_ref["path"], "Human Gate review record")
        if record_path.is_symlink() or not record_path.is_file():
            raise HumanGateError(f"Human Gate review record missing: {record_ref['path']}")
        if core.sha256_file(record_path) != record_ref["sha256"]:
            raise HumanGateError(f"Human Gate review record SHA drift: {record_ref['path']}")
        record = schema_gate.load_and_validate_json(
            record_path,
            repo_root / REVIEW_RECORD_SCHEMA,
            label="Human Gate Review Record",
        )
        if (
            record.get("issue_id") != expected_issue_id
            or record.get("gate") != gate
            or record.get("revision") != revision
            or record.get("decision") != row["decision"]
        ):
            raise HumanGateError("Human Gate review index/record identity mismatch")
        if row["decision"] == "APPROVED":
            approval = record.get("approval")
            if not isinstance(approval, dict):
                raise HumanGateError("APPROVED Human Gate review lacks immutable approval snapshot")
            approval_path = core.repo_local_path(repo_root, approval["path"], "Human Gate approval snapshot")
            if approval_path.is_symlink() or not approval_path.is_file():
                raise HumanGateError(f"Human Gate approval snapshot missing: {approval['path']}")
            if core.sha256_file(approval_path) != approval["sha256"]:
                raise HumanGateError(f"Human Gate approval snapshot SHA drift: {approval['path']}")
            approved_active[gate] = True
        elif (
            gate == "PUBLICATION_PREVIEW"
            and row["decision"] == "REQUEST_CHANGES"
            and _reopens_architecture(record.get("regeneration_boundary"))
        ):
            if not approved_active["ARCHITECTURE_REVIEW"]:
                raise HumanGateError("Publication cross-gate revision has no active approved Architecture to reopen")
            approved_active["ARCHITECTURE_REVIEW"] = False


def _load_review_index(
    repo_root: Path,
    cfg: dict[str, Any],
    source_root: Path,
    issue_id: str,
) -> dict[str, Any]:
    path = review_index_path(source_root, cfg)
    if not path.exists():
        return {"schema_version": "2.0-rc1", "issue_id": issue_id, "reviews": []}
    payload = schema_gate.load_and_validate_json(
        path,
        repo_root / REVIEW_INDEX_SCHEMA,
        label="Human Gate Review Index",
    )
    _validate_review_index_semantics(repo_root, payload, issue_id)
    return payload


def _next_revision(index: dict[str, Any], gate: str, expected_revision: int | None) -> int:
    revision = 1 + sum(1 for row in index["reviews"] if row["gate"] == gate)
    if expected_revision is not None and expected_revision != revision:
        raise HumanGateError(
            f"stale Human Gate request for {gate}: expected revision {expected_revision}, current next revision is {revision}"
        )
    return revision


def _expand_gate_path(template: str, profile: dict[str, Any]) -> str:
    value = template
    for key, replacement in profile["paths"].items():
        value = value.replace("{" + key + "}", replacement)
    if "{" in value or "}" in value:
        raise HumanGateError(f"unsupported Human Gate path template token: {template}")
    return value


def _reviewed_artifacts(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    profile: dict[str, Any],
    gate: str,
    *,
    require_current_candidate_validity: bool = True,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for item in cfg["orchestration"]["gate_inputs"][gate]:
        path = core.repo_local_path(
            repo_root,
            _expand_gate_path(item["path"], profile),
            f"Human Gate input {item['name']}",
        )
        rows.append(_named_authority(repo_root, item["name"], path))
    if gate == "PUBLICATION_PREVIEW":
        candidate_path = next(
            core.repo_local_path(repo_root, row["path"], "Publication Candidate")
            for row in rows
            if row["name"] == "publication-candidate"
        )
        if require_current_candidate_validity:
            candidate = publication.validate_candidate(
                repo_root, candidate_path, issue_id=state["issue_id"]
            )
        else:
            # REQUEST_CHANGES records the exact historical review surface. A
            # newer Candidate schema or substantive validator may be the reason
            # the Human is rejecting these bytes, so rejection must not require
            # the historical artifact to satisfy current acceptance contracts.
            candidate = core.load_json(candidate_path)
            if candidate.get("issue_id") != state["issue_id"]:
                raise HumanGateError("Publication Candidate historical review issue identity mismatch")
            if candidate.get("publication_profile") != profile.get("publication_profile"):
                raise HumanGateError("Publication Candidate historical review profile identity mismatch")
        pdf = candidate.get("pdf")
        if not isinstance(pdf, dict) or not isinstance(pdf.get("path"), str):
            raise HumanGateError("Publication Candidate lacks durable PDF authority")
        pdf_path = core.repo_local_path(repo_root, pdf["path"], "Publication Preview PDF")
        pdf_authority = _named_authority(repo_root, "publication-pdf", pdf_path)
        if pdf_authority["sha256"] != pdf.get("sha256"):
            raise HumanGateError("Publication Candidate PDF authority drift")
        rows.append(pdf_authority)
    return rows


def _review_record_payload(
    *,
    issue_id: str,
    gate: str,
    revision: int,
    decision: str,
    reviewed_state: dict[str, str],
    reviewed_artifacts: list[dict[str, str]],
    reviewed_repository_commit_sha: str,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
    requested_changes: str | None,
    regeneration_boundary: str | None,
    approval: dict[str, str] | None,
) -> dict[str, Any]:
    seed = {
        "issue_id": issue_id,
        "gate": gate,
        "revision": revision,
        "decision": decision,
        "reviewed_state": reviewed_state,
        "reviewed_artifacts": reviewed_artifacts,
        "reviewed_repository_commit_sha": reviewed_repository_commit_sha,
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
        "regeneration_boundary": regeneration_boundary,
    }
    return {
        "schema_version": "2.0-rc1",
        "review_id": f"review:{issue_id}:{GATE_SLUGS[gate]}:r{revision}:{core.sha256_object(seed)[:16]}",
        "issue_id": issue_id,
        "gate": gate,
        "revision": revision,
        "decision": decision,
        "reviewed_state": reviewed_state,
        "reviewed_artifacts": reviewed_artifacts,
        "reviewed_repository_commit_sha": reviewed_repository_commit_sha,
        "reviewed_by": reviewed_by,
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
        "requested_changes": requested_changes,
        "regeneration_boundary": regeneration_boundary,
        "approval": approval,
    }


def _write_review_record(
    repo_root: Path,
    cfg: dict[str, Any],
    source_root: Path,
    index: dict[str, Any],
    record: dict[str, Any],
) -> tuple[Path, Path]:
    schema_gate.validate_instance(record, repo_root / REVIEW_RECORD_SCHEMA, label="Human Gate Review Record")
    record_path = review_record_path(source_root, cfg, record["gate"], record["revision"])
    if record_path.exists():
        raise HumanGateError(f"refusing Human Gate review record overwrite: {_rel(repo_root, record_path)}")
    core.write_json(record_path, record)
    updated_index = deepcopy(index)
    updated_index["reviews"].append(
        {
            "gate": record["gate"],
            "revision": record["revision"],
            "decision": record["decision"],
            "record": _authority(repo_root, record_path),
        }
    )
    schema_gate.validate_instance(
        updated_index,
        repo_root / REVIEW_INDEX_SCHEMA,
        label="Human Gate Review Index",
    )
    _validate_review_index_semantics(repo_root, updated_index, record["issue_id"])
    index_path = review_index_path(source_root, cfg)
    core.write_json(index_path, updated_index)
    return record_path, index_path


def _validate_gate_pending(state: dict[str, Any], gate: str) -> None:
    key = GATE_KEYS[gate]
    expected_state = GATE_STATES[gate]
    if state.get("lifecycle_state") != expected_state or state.get("human_gates", {}).get(key) != "pending":
        raise HumanGateError(f"{gate} decision requires pending {expected_state} Human Gate")


def _require_review_commit(repo_root: Path, commit_sha: str) -> None:
    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{commit_sha}^{{commit}}"],
            cwd=repo_root,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise HumanGateError(
            f"Human Gate reviewed repository commit does not exist: {commit_sha}"
        ) from exc


def _require_review_commit_reachable(repo_root: Path, commit_sha: str, work_branch: str) -> None:
    try:
        subprocess.run(
            ["git", "check-ref-format", "--branch", work_branch],
            cwd=repo_root,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise HumanGateError(f"invalid Human Gate work branch: {work_branch}") from exc

    origin = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        cwd=repo_root,
        capture_output=True,
    )
    if origin.returncode == 0:
        ref = f"refs/remotes/origin/{work_branch}"
        label = f"origin/{work_branch}"
    else:
        ref = f"refs/heads/{work_branch}"
        label = work_branch

    present = subprocess.run(
        ["git", "show-ref", "--verify", "--quiet", ref],
        cwd=repo_root,
    )
    if present.returncode != 0:
        raise HumanGateError(
            f"Human Gate reviewed repository commit is not retained on canonical work branch {label}; push/fetch the review surface first"
        )
    reachable = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit_sha, ref],
        cwd=repo_root,
    )
    if reachable.returncode != 0:
        raise HumanGateError(
            f"Human Gate reviewed repository commit is not reachable from canonical work branch {label}: {commit_sha}"
        )


def _committed_file_bytes(repo_root: Path, commit_sha: str, rel: str) -> bytes:
    try:
        listing = subprocess.run(
            ["git", "ls-tree", "-z", commit_sha, "--", rel],
            cwd=repo_root,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise HumanGateError(
            f"cannot inspect Human Gate reviewed repository commit path: {commit_sha}:{rel}"
        ) from exc
    entries = [entry for entry in listing.stdout.split(b"\0") if entry]
    if len(entries) != 1:
        raise HumanGateError(
            f"Human Gate reviewed repository commit is missing reviewed path: {rel}"
        )
    try:
        meta, encoded_path = entries[0].split(b"\t", 1)
        mode, object_type, object_sha = meta.decode("ascii").split()
        listed_path = encoded_path.decode("utf-8")
    except (UnicodeDecodeError, ValueError) as exc:
        raise HumanGateError(
            f"Human Gate reviewed repository tree entry invalid for: {rel}"
        ) from exc
    if listed_path != rel or object_type != "blob" or mode not in {"100644", "100755"}:
        raise HumanGateError(
            f"Human Gate reviewed repository path is not a regular file: {rel}"
        )
    try:
        blob = subprocess.run(
            ["git", "cat-file", "blob", object_sha],
            cwd=repo_root,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise HumanGateError(
            f"cannot read Human Gate reviewed repository blob: {rel}"
        ) from exc
    return blob.stdout


def _review_commit(
    repo_root: Path,
    override: str | None,
    work_branch: str,
    reviewed_state: dict[str, str],
    reviewed_artifacts: list[dict[str, str]],
) -> str:
    commit_sha = core.repository_commit_sha(repo_root, override)
    _require_review_commit(repo_root, commit_sha)
    _require_review_commit_reachable(repo_root, commit_sha, work_branch)
    refs: list[tuple[str, dict[str, str]]] = [("Production State", reviewed_state)]
    refs.extend(
        (f"Human Gate artifact {row['name']}", row)
        for row in reviewed_artifacts
    )
    for label, ref in refs:
        rel = ref["path"]
        current = core.repo_local_path(repo_root, rel, label)
        if current.is_symlink() or not current.is_file():
            raise HumanGateError(f"{label} missing or unsafe while verifying reviewed commit: {rel}")
        committed = _committed_file_bytes(repo_root, commit_sha, rel)
        if core.sha256_bytes(committed) != ref["sha256"]:
            raise HumanGateError(
                f"Human Gate reviewed repository commit bytes differ for {label}: {rel}"
            )
    return commit_sha


def _snapshot_approval(
    repo_root: Path,
    source_root: Path,
    cfg: dict[str, Any],
    gate: str,
    revision: int,
    canonical_approval: Path,
) -> dict[str, str]:
    canonical = _authority(repo_root, canonical_approval)
    snapshot = approval_snapshot_path(source_root, cfg, gate, revision)
    if snapshot.exists():
        existing = _authority(repo_root, snapshot)
        if existing["sha256"] != canonical["sha256"]:
            raise HumanGateError(f"Human Gate approval snapshot collision: {_rel(repo_root, snapshot)}")
        return existing
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    snapshot.write_bytes(canonical_approval.read_bytes())
    snap = _authority(repo_root, snapshot)
    if snap["sha256"] != canonical["sha256"]:
        raise HumanGateError("Human Gate approval snapshot byte mismatch")
    return snap


def record_architecture_approval(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
    *,
    expected_revision: int | None = None,
    reviewed_commit_sha: str | None = None,
) -> tuple[dict[str, Any], Path, Path]:
    state, profile, source_root = _state_context(repo_root, cfg, state_path)
    _validate_gate_pending(state, "ARCHITECTURE_REVIEW")
    index = _load_review_index(repo_root, cfg, source_root, state["issue_id"])
    revision = _next_revision(index, "ARCHITECTURE_REVIEW", expected_revision)
    reviewed_state = _authority(repo_root, state_path)
    artifacts = _reviewed_artifacts(repo_root, cfg, state, profile, "ARCHITECTURE_REVIEW")
    commit_sha = _review_commit(
        repo_root,
        reviewed_commit_sha,
        profile["paths"]["work_branch"],
        reviewed_state,
        artifacts,
    )
    updated = agent.approve_architecture(
        repo_root,
        cfg,
        state_path,
        reviewed_by,
        reviewed_at,
        review_reference,
    )
    approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
    approval_snapshot = _snapshot_approval(
        repo_root, source_root, cfg, "ARCHITECTURE_REVIEW", revision, approval_path
    )
    record = _review_record_payload(
        issue_id=state["issue_id"],
        gate="ARCHITECTURE_REVIEW",
        revision=revision,
        decision="APPROVED",
        reviewed_state=reviewed_state,
        reviewed_artifacts=artifacts,
        reviewed_repository_commit_sha=commit_sha,
        reviewed_by=reviewed_by,
        reviewed_at=reviewed_at,
        review_reference=review_reference,
        requested_changes=None,
        regeneration_boundary=None,
        approval=approval_snapshot,
    )
    record_path, index_path = _write_review_record(repo_root, cfg, source_root, index, record)
    return updated, record_path, index_path


def record_publication_preview_approval(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
    *,
    expected_revision: int | None = None,
    reviewed_commit_sha: str | None = None,
) -> tuple[dict[str, Any], Path, Path]:
    state, profile, source_root = _state_context(repo_root, cfg, state_path)
    _validate_gate_pending(state, "PUBLICATION_PREVIEW")
    index = _load_review_index(repo_root, cfg, source_root, state["issue_id"])
    revision = _next_revision(index, "PUBLICATION_PREVIEW", expected_revision)
    reviewed_state = _authority(repo_root, state_path)
    artifacts = _reviewed_artifacts(repo_root, cfg, state, profile, "PUBLICATION_PREVIEW")
    commit_sha = _review_commit(
        repo_root,
        reviewed_commit_sha,
        profile["paths"]["work_branch"],
        reviewed_state,
        artifacts,
    )
    updated = agent.approve_publication_preview(
        repo_root,
        cfg,
        state_path,
        reviewed_by,
        reviewed_at,
        review_reference,
    )
    approval_path = source_root / cfg["state_authority"]["publication_preview_approval_path"]
    approval_snapshot = _snapshot_approval(
        repo_root, source_root, cfg, "PUBLICATION_PREVIEW", revision, approval_path
    )
    record = _review_record_payload(
        issue_id=state["issue_id"],
        gate="PUBLICATION_PREVIEW",
        revision=revision,
        decision="APPROVED",
        reviewed_state=reviewed_state,
        reviewed_artifacts=artifacts,
        reviewed_repository_commit_sha=commit_sha,
        reviewed_by=reviewed_by,
        reviewed_at=reviewed_at,
        review_reference=review_reference,
        requested_changes=None,
        regeneration_boundary=None,
        approval=approval_snapshot,
    )
    record_path, index_path = _write_review_record(repo_root, cfg, source_root, index, record)
    return updated, record_path, index_path


def _completed_checkpoints(cfg: dict[str, Any], lifecycle: str) -> set[str]:
    index = core.LIFECYCLE.index(lifecycle)
    result: set[str] = set()
    for state_name in core.LIFECYCLE[:index]:
        stage = cfg["orchestration"]["stage_plan"].get(state_name)
        if isinstance(stage, dict):
            result.update(stage.get("checkpoints", []))
    return result


def _superseded_checkpoint_paths(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    source_root: Path,
    regeneration_boundary: str,
    gate: str,
) -> list[Path]:
    keep = _completed_checkpoints(cfg, regeneration_boundary)
    paths: dict[str, Path] = {}
    for checkpoint in core.CHECKPOINTS:
        if checkpoint in keep:
            continue
        authority = state.get("checkpoint_provenance", {}).get(checkpoint)
        if isinstance(authority, dict):
            path = core.repo_local_path(repo_root, authority["path"], f"superseded checkpoint {checkpoint}")
            try:
                path.resolve().relative_to(source_root.resolve())
            except ValueError as exc:
                raise HumanGateError(f"superseded checkpoint authority escapes source_root: {authority['path']}") from exc
            paths[_rel(repo_root, path)] = path

    start = core.LIFECYCLE.index(regeneration_boundary)
    end = core.LIFECYCLE.index(GATE_STATES[gate])
    checkpoint_dir = source_root / cfg["state_authority"]["agent_checkpoint_dir"]
    for state_name in core.LIFECYCLE[start:end]:
        path = checkpoint_dir / f"{state_name}.json"
        if path.exists():
            paths[_rel(repo_root, path)] = path
    return [paths[key] for key in sorted(paths)]


def _superseded_gate_authority_paths(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    source_root: Path,
    gate: str,
    regeneration_boundary: str,
) -> list[Path]:
    if gate != "PUBLICATION_PREVIEW" or not _reopens_architecture(regeneration_boundary):
        return []
    if state["human_gates"]["architecture_review"] != "approved":
        raise HumanGateError("Publication cross-gate revision requires active approved Architecture Review")
    path = source_root / cfg["state_authority"]["architecture_approval_path"]
    authority = _authority(repo_root, path)
    provenance = state.get("human_gate_provenance", {}).get("architecture_review")
    if not isinstance(provenance, dict) or provenance.get("path") != authority["path"] or provenance.get("sha256") != authority["sha256"]:
        raise HumanGateError("active Architecture approval provenance does not match canonical approval bytes")
    return [path]


def _revised_state(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    gate: str,
    regeneration_boundary: str,
) -> dict[str, Any]:
    allowed = cfg["orchestration"].get("human_gate_revision_boundaries", {}).get(gate, [])
    if regeneration_boundary not in allowed:
        raise HumanGateError(
            f"regeneration boundary {regeneration_boundary!r} is not allowed for {gate}; allowed={allowed}"
        )
    target_index = core.LIFECYCLE.index(regeneration_boundary)
    gate_index = core.LIFECYCLE.index(GATE_STATES[gate])
    if target_index >= gate_index:
        raise HumanGateError("regeneration boundary must precede the reviewed Human Gate state")

    updated = deepcopy(state)
    keep = _completed_checkpoints(cfg, regeneration_boundary)
    for checkpoint in core.CHECKPOINTS:
        if checkpoint in keep:
            continue
        updated["machine_checkpoints"][checkpoint] = "pending"
        updated["checkpoint_provenance"][checkpoint] = None
    updated["lifecycle_state"] = regeneration_boundary
    updated["history"] = updated["history"][: target_index + 1]

    if gate == "ARCHITECTURE_REVIEW":
        updated["human_gates"]["architecture_review"] = "pending"
        updated["human_gate_provenance"]["architecture_review"] = None
        updated["human_gates"]["publication_preview"] = "pending"
        updated["human_gate_provenance"]["publication_preview"] = None
    else:
        if updated["human_gates"]["architecture_review"] != "approved":
            raise HumanGateError("Publication Preview revision requires active approved Architecture Review")
        if _reopens_architecture(regeneration_boundary):
            updated["human_gates"]["architecture_review"] = "pending"
            updated["human_gate_provenance"]["architecture_review"] = None
        updated["human_gates"]["publication_preview"] = "pending"
        updated["human_gate_provenance"]["publication_preview"] = None

    updated = core.refresh_state_control(updated, cfg)
    errors = agent.validate_agent_state(repo_root, cfg, updated)
    if errors:
        raise HumanGateError("refusing inconsistent Human Gate revision State: " + "; ".join(errors))
    return updated


def request_changes(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    gate: str,
    regeneration_boundary: str,
    requested_changes: str,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
    *,
    expected_revision: int | None = None,
    reviewed_commit_sha: str | None = None,
) -> tuple[dict[str, Any], Path, Path, list[str]]:
    if gate not in GATE_KEYS:
        raise HumanGateError(f"unsupported Human Gate: {gate}")
    if not isinstance(requested_changes, str) or not requested_changes.strip():
        raise HumanGateError("REQUEST_CHANGES requires a non-empty requested_changes summary")
    if not reviewed_by.strip() or not review_reference.strip():
        raise HumanGateError("reviewed_by and review_reference are required")

    state, profile, source_root = _state_context(repo_root, cfg, state_path)
    _validate_gate_pending(state, gate)
    index = _load_review_index(repo_root, cfg, source_root, state["issue_id"])
    revision = _next_revision(index, gate, expected_revision)
    reviewed_state = _authority(repo_root, state_path)
    artifacts = _reviewed_artifacts(
        repo_root,
        cfg,
        state,
        profile,
        gate,
        require_current_candidate_validity=False,
    )
    commit_sha = _review_commit(
        repo_root,
        reviewed_commit_sha,
        profile["paths"]["work_branch"],
        reviewed_state,
        artifacts,
    )
    updated = _revised_state(repo_root, cfg, state, gate, regeneration_boundary)
    superseded = _superseded_checkpoint_paths(
        repo_root, cfg, state, source_root, regeneration_boundary, gate
    )
    superseded.extend(
        _superseded_gate_authority_paths(
            repo_root, cfg, state, source_root, gate, regeneration_boundary
        )
    )
    record = _review_record_payload(
        issue_id=state["issue_id"],
        gate=gate,
        revision=revision,
        decision="REQUEST_CHANGES",
        reviewed_state=reviewed_state,
        reviewed_artifacts=artifacts,
        reviewed_repository_commit_sha=commit_sha,
        reviewed_by=reviewed_by,
        reviewed_at=reviewed_at,
        review_reference=review_reference,
        requested_changes=requested_changes.strip(),
        regeneration_boundary=regeneration_boundary,
        approval=None,
    )
    record_path, index_path = _write_review_record(repo_root, cfg, source_root, index, record)
    removed: list[str] = []
    for path in sorted(set(superseded), key=lambda item: _rel(repo_root, item)):
        if path.exists():
            path.unlink()
            removed.append(_rel(repo_root, path))
    core.write_json(state_path, updated)
    final_errors = agent.validate_agent_state(repo_root, cfg, core.load_json(state_path))
    if final_errors:
        raise HumanGateError("Human Gate revision did not produce resumable State: " + "; ".join(final_errors))
    return updated, record_path, index_path, removed


def request_architecture_revision(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    regeneration_boundary: str,
    requested_changes: str,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
    *,
    expected_revision: int | None = None,
    reviewed_commit_sha: str | None = None,
) -> tuple[dict[str, Any], Path, Path, list[str]]:
    return request_changes(
        repo_root,
        cfg,
        state_path,
        "ARCHITECTURE_REVIEW",
        regeneration_boundary,
        requested_changes,
        reviewed_by,
        reviewed_at,
        review_reference,
        expected_revision=expected_revision,
        reviewed_commit_sha=reviewed_commit_sha,
    )


def request_publication_preview_revision(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    regeneration_boundary: str,
    requested_changes: str,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
    *,
    expected_revision: int | None = None,
    reviewed_commit_sha: str | None = None,
) -> tuple[dict[str, Any], Path, Path, list[str]]:
    return request_changes(
        repo_root,
        cfg,
        state_path,
        "PUBLICATION_PREVIEW",
        regeneration_boundary,
        requested_changes,
        reviewed_by,
        reviewed_at,
        review_reference,
        expected_revision=expected_revision,
        reviewed_commit_sha=reviewed_commit_sha,
    )


def _path(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(core.DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)

    for command in ("record-architecture-approval", "record-publication-preview-approval"):
        child = sub.add_parser(command)
        child.add_argument("--state", required=True)
        child.add_argument("--expected-revision", type=int)
        child.add_argument("--reviewed-by", required=True)
        child.add_argument("--reviewed-at", required=True)
        child.add_argument("--review-reference", required=True)
        child.add_argument("--reviewed-commit-sha")

    for command in ("request-architecture-revision", "request-publication-preview-revision"):
        child = sub.add_parser(command)
        child.add_argument("--state", required=True)
        child.add_argument("--expected-revision", type=int)
        child.add_argument("--regeneration-boundary", required=True)
        child.add_argument("--requested-changes", required=True)
        child.add_argument("--reviewed-by", required=True)
        child.add_argument("--reviewed-at", required=True)
        child.add_argument("--review-reference", required=True)
        child.add_argument("--reviewed-commit-sha")

    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    try:
        cfg = core.load_json(_path(root, args.config))
        state_path = _path(root, args.state)
        reviewed_at = core.parse_instant(args.reviewed_at)
        common = {
            "expected_revision": args.expected_revision,
            "reviewed_commit_sha": args.reviewed_commit_sha,
        }
        if args.command == "record-architecture-approval":
            state, record, index = record_architecture_approval(
                root, cfg, state_path, args.reviewed_by, reviewed_at, args.review_reference, **common
            )
            removed: list[str] = []
        elif args.command == "record-publication-preview-approval":
            state, record, index = record_publication_preview_approval(
                root, cfg, state_path, args.reviewed_by, reviewed_at, args.review_reference, **common
            )
            removed = []
        elif args.command == "request-architecture-revision":
            state, record, index, removed = request_architecture_revision(
                root,
                cfg,
                state_path,
                args.regeneration_boundary,
                args.requested_changes,
                args.reviewed_by,
                reviewed_at,
                args.review_reference,
                **common,
            )
        elif args.command == "request-publication-preview-revision":
            state, record, index, removed = request_publication_preview_revision(
                root,
                cfg,
                state_path,
                args.regeneration_boundary,
                args.requested_changes,
                args.reviewed_by,
                reviewed_at,
                args.review_reference,
                **common,
            )
        else:
            raise HumanGateError(f"unsupported Human Gate command: {args.command}")
        print(
            json.dumps(
                {
                    "state": _rel(root, state_path),
                    "lifecycle_state": state["lifecycle_state"],
                    "next_action": state["next_action"],
                    "terminal_reason": state["terminal_reason"],
                    "review_record": _rel(root, record),
                    "review_index": _rel(root, index),
                    "removed_paths": removed,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
