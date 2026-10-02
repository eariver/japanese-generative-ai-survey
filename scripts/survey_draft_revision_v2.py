#!/usr/bin/env python3
"""Generic reviewed-Draft supersession authority (pre-VALIDATED_DRAFT).

A Draft may legitimately receive Sol/editorial-reviewed revisions after the
normal ``ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE`` transition while the
historical Stage Checkpoint must remain immutable. Without a sanctioned
authority, later re-validation fail-closes on artifact drift even though the
successor bytes were explicitly reviewed.

This module provides that authority with the same trust shape as the
post-VALIDATED_DRAFT publication-surface revalidation mechanism:

- historical Stage Checkpoints are never rewritten;
- normal drift detection is not weakened;
- Production State carries an optional exact ``{path, sha256}`` pointer
  (``draft_revision_provenance``) to the active immutable revision record;
- an unreferenced record is inert; a corrupt pointer fails closed;
- versioned records chain via exact ``supersedes`` authority;
- only ``draft-result:*`` / ``synthesis-input`` / ``synthesis-result`` rows
  may be superseded; Draft Packages and all upstream authority stay drift-bound;
- successors are revalidated with the existing generic Draft validators
  (never a bare SHA override) and require an exact reviewed-PASS authority;
- no Human gate is created or inferred.

Both ``survey_agent_control_v2.validate_agent_state`` and
``survey_stage_validation_v2._prior_artifacts`` consult
:func:`resolve_active_draft_revision` so there is exactly one
active-authority implementation.
"""
from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_drafting_v2_base as drafting_base
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

DRAFT_REVISION_SCHEMA = Path("schemas/draft-surface-revision.schema.json")
DRAFT_REVISION_BASENAME = "draft-surface-revision"
DRAFT_REVISION_REASON_CLASSES = {"REVIEWED_DRAFT_REVISION"}
DRAFT_REVISION_CHAIN_LIMIT = 32


class DraftRevisionError(ValueError):
    """Fail-closed reviewed-Draft revision error."""


def _rel(repo_root: Path, path: Path, label: str) -> str:
    resolved = path.resolve() if isinstance(path, Path) else Path(path).resolve()
    try:
        return str(resolved.relative_to(repo_root.resolve()))
    except ValueError as exc:
        raise DraftRevisionError(f"{label} escapes repository: {path}") from exc


def _eligible_superseded_name(name: Any) -> bool:
    """Only Draft-result/synthesis rows may be superseded. Nothing else."""
    return (
        isinstance(name, str)
        and name
        and (
            name in ("synthesis-input", "synthesis-result")
            or name.startswith("draft-result:")
        )
    )


def _load_revision_record(
    repo_root: Path, ref: dict[str, Any], label: str
) -> tuple[dict[str, Any] | None, str | None]:
    """Load one revision record with structural validation.

    Returns (record, error). Error is a single string; None means success.
    """
    if not isinstance(ref, dict) or set(ref) != {"path", "sha256"}:
        return None, f"{label} authority fields invalid"
    try:
        path = core.repo_local_path(repo_root, ref["path"], label)
    except (TypeError, ValueError) as exc:
        return None, str(exc)
    if path.is_symlink() or not path.is_file():
        return None, f"{label} missing or unsafe"
    if core.sha256_file(path) != ref.get("sha256"):
        return None, f"{label} SHA mismatch"
    try:
        record = schema_gate.load_and_validate_json(
            path, repo_root / DRAFT_REVISION_SCHEMA, label="Draft Surface Revision"
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return None, f"{label} invalid: {exc}"
    return record, None


def _check_revision_chain(
    repo_root: Path, record: dict[str, Any]
) -> list[str]:
    """Walk the immutable supersession chain; every link must exist byte-identical."""
    errors: list[str] = []
    seen: set[str] = set()
    current: dict[str, Any] | None = record
    for _ in range(DRAFT_REVISION_CHAIN_LIMIT):
        if current is None:
            return errors
        link = current.get("supersedes")
        if link is None:
            return errors
        linked, error = _load_revision_record(repo_root, link, "superseded Draft revision record")
        if error is not None:
            errors.append(error)
            return errors
        assert linked is not None
        digest = core.sha256_file(
            core.repo_local_path(repo_root, link["path"], "superseded Draft revision record")
        )
        if digest in seen:
            errors.append("Draft revision supersession chain cycle")
            return errors
        seen.add(digest)
        if linked.get("issue_id") != record.get("issue_id"):
            errors.append("Draft revision chain issue identity mismatch")
            return errors
        current = linked
    errors.append("Draft revision supersession chain too deep")
    return errors


def _check_review_authority(
    repo_root: Path, record: dict[str, Any]
) -> list[str]:
    """The successor must be explicitly reviewed PASS; the evidence is bound, not parsed as prose."""
    errors: list[str] = []
    review = record.get("review")
    if not isinstance(review, dict):
        return ["Draft revision review authority missing"]
    raw_path = review.get("path")
    try:
        path = core.repo_local_path(repo_root, raw_path, "Draft revision review authority")
    except (TypeError, ValueError) as exc:
        return [str(exc)]
    if path.is_symlink() or not path.is_file():
        return ["Draft revision review authority missing or unsafe"]
    if core.sha256_file(path) != review.get("sha256"):
        return ["Draft revision review authority SHA mismatch"]
    try:
        payload = core.load_json(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [f"Draft revision review authority unreadable: {exc}"]
    if not isinstance(payload, dict):
        return ["Draft revision review authority must be a JSON object"]
    if payload.get("decision") != "PASS" or review.get("decision") != "PASS":
        errors.append("Draft revision review authority is not an accepted PASS review")
    if not isinstance(payload.get("reviewed_by"), str) or not payload["reviewed_by"].strip():
        errors.append("Draft revision review authority lacks reviewer identity")
    if payload.get("reviewed_by") != review.get("reviewed_by"):
        errors.append("Draft revision review authority reviewer mismatch")
    return errors


def draft_superseded_map(record: dict[str, Any]) -> dict[tuple[str, str], str]:
    """New SHA-256 by (name, path) for rows this record supersedes. Shared helper."""
    result: dict[tuple[str, str], str] = {}
    for row in record.get("superseded_artifacts", []):
        if isinstance(row, dict):
            result[(row.get("name"), row.get("path"))] = row.get("new_sha256")
    return result


def record_revised_rows(record: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Current-byte authority of every Draft row as rebound by this record.

    Superseded rows bind new bytes; preserved rows bind prior bytes. Shared
    helper so validators and CLIs consult one row map.
    """
    revised: dict[str, dict[str, str]] = {}
    for row in record.get("superseded_artifacts", []):
        if isinstance(row, dict):
            revised[row.get("name")] = {
                "path": row.get("path"), "sha256": row.get("new_sha256")}
    for row in record.get("preserved_artifacts", []):
        if isinstance(row, dict) and row.get("name") not in revised:
            revised[row.get("name")] = {
                "path": row.get("path"), "sha256": row.get("sha256")}
    return revised


def _validate_record_tree(
    repo_root: Path,
    record: dict[str, Any],
    issue_id: str,
    prior_checkpoint: dict[str, Any],
    prior_rows: dict[tuple[str, str], str],
    depth: int,
) -> list[str]:
    """Recursively validate one revision record against its base rows.

    Rootless records (supersedes None) validate against the historical Draft
    checkpoint rows. Chained records validate against the revised rows of
    their recursively validated superseded record; every link must bind the
    same historical prior checkpoint so history is never rewritten.
    """
    errors: list[str] = []
    if depth > DRAFT_REVISION_CHAIN_LIMIT:
        return ["Draft revision supersession chain too deep"]
    if record.get("issue_id") != issue_id:
        errors.append("Draft revision issue identity mismatch")
    if record.get("reason_class") not in DRAFT_REVISION_REASON_CLASSES:
        errors.append("Draft revision reason class unrecognized")
    if record.get("prior_checkpoint") != prior_checkpoint:
        errors.append("Draft revision does not bind the active Draft checkpoint")
    link = record.get("supersedes")
    if link is None:
        base_rows = dict(prior_rows)
    else:
        base_record, error = _load_revision_record(
            repo_root, link, "superseded Draft revision record")
        if error is not None:
            return errors + [error]
        assert base_record is not None
        errors.extend(_validate_record_tree(
            repo_root, base_record, issue_id, prior_checkpoint, prior_rows, depth + 1))
        base_rows = {
            (name, row["path"]): row["sha256"]
            for name, row in record_revised_rows(base_record).items()
            if isinstance(row, dict) and row.get("path") and row.get("sha256")
        }
    seen: set[tuple[str, str]] = set()
    for row in record.get("superseded_artifacts", []):
        key = (row.get("name"), row.get("path"))
        if key in seen:
            errors.append(f"Draft revision duplicate superseded row: {row.get('name')}")
            continue
        seen.add(key)
        if not _eligible_superseded_name(row.get("name")):
            errors.append(f"Draft revision supersession not eligible: {row.get('name')}")
            continue
        if base_rows.get(key) != row.get("prior_sha256"):
            errors.append(f"Draft revision prior SHA mismatch: {row.get('name')}")
            continue
        if row.get("new_sha256") == row.get("prior_sha256"):
            errors.append(f"Draft revision supersession without byte change: {row.get('name')}")
    for row in record.get("preserved_artifacts", []):
        key = (row.get("name"), row.get("path"))
        if key in seen:
            errors.append(f"Draft revision duplicate artifact row: {row.get('name')}")
            continue
        seen.add(key)
        if base_rows.get(key) != row.get("sha256"):
            errors.append(f"Draft revision preserved row mismatch: {row.get('name')}")
    covered = set(base_rows)
    if set(seen) != covered:
        errors.append(
            "Draft revision must account for every prior Draft checkpoint row: "
            f"missing={sorted(set(covered) - set(seen))}"
        )
    errors.extend(_check_revision_chain(repo_root, record))
    errors.extend(_check_review_authority(repo_root, record))
    return errors


def resolve_active_draft_revision(
    repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]
) -> tuple[dict[str, Any] | None, list[str]]:
    """Resolve the State-bound active reviewed-Draft revision authority.

    Returns (record, errors); (None, []) when the State carries no reference.
    A referenced-but-invalid record is a fail-closed error, never a fallback.
    An unreferenced record file is inert and never consulted.
    """
    repo_root = repo_root.resolve()
    pointer = state.get("draft_revision_provenance")
    if pointer is None:
        return None, []
    record, error = _load_revision_record(repo_root, pointer, "active Draft revision authority")
    if error is not None:
        return None, [error]
    assert record is not None
    errors: list[str] = []
    if record.get("reason_class") not in DRAFT_REVISION_REASON_CLASSES:
        errors.append("Draft revision reason class unrecognized")
    prior_ref = record.get("prior_checkpoint")
    if not isinstance(prior_ref, dict) or set(prior_ref) != {"path", "sha256"}:
        errors.append("Draft revision prior checkpoint authority fields invalid")
        return None, errors
    draft_provenance = (state.get("checkpoint_provenance") or {}).get("draft")
    if not isinstance(draft_provenance, dict) or draft_provenance != prior_ref:
        errors.append("Draft revision does not bind the active Draft checkpoint")
        return None, errors
    try:
        prior_path = core.repo_local_path(repo_root, prior_ref["path"], "Draft revision prior checkpoint")
    except (TypeError, ValueError) as exc:
        return None, [str(exc)]
    if prior_path.is_symlink() or not prior_path.is_file():
        return None, ["Draft revision prior checkpoint missing or unsafe"]
    if core.sha256_file(prior_path) != prior_ref.get("sha256"):
        return None, ["Draft revision prior checkpoint provenance drift"]
    try:
        prior_record = schema_gate.load_and_validate_json(
            prior_path, repo_root / agent.CHECKPOINT_SCHEMA, label="Draft revision prior Stage Checkpoint"
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return None, [f"Draft revision prior checkpoint unreadable: {exc}"]
    prior_rows = {
        (row.get("name"), row.get("path")): row.get("sha256")
        for row in prior_record.get("artifacts", [])
        if isinstance(row, dict)
    }
    errors.extend(_validate_record_tree(
        repo_root, record, state.get("issue_id"), prior_ref, prior_rows, 0))
    if errors:
        return None, errors
    return record, []


def _draft_checkpoint_rows(
    repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]
) -> dict[str, dict[str, str]]:
    """Current historical Draft checkpoint rows by artifact name."""
    draft_provenance = (state.get("checkpoint_provenance") or {}).get("draft")
    if not isinstance(draft_provenance, dict):
        raise DraftRevisionError("Draft revision requires Draft checkpoint provenance")
    try:
        prior_path = core.repo_local_path(repo_root, draft_provenance["path"], "Draft checkpoint")
    except (TypeError, ValueError) as exc:
        raise DraftRevisionError(str(exc)) from exc
    if prior_path.is_symlink() or not prior_path.is_file():
        raise DraftRevisionError("Draft checkpoint missing or unsafe")
    if core.sha256_file(prior_path) != draft_provenance.get("sha256"):
        raise DraftRevisionError("Draft checkpoint provenance drift")
    try:
        prior_record = schema_gate.load_and_validate_json(
            prior_path, repo_root / agent.CHECKPOINT_SCHEMA, label="Draft revision prior Stage Checkpoint"
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise DraftRevisionError(f"Draft checkpoint unreadable: {exc}") from exc
    if prior_record.get("issue_id") != state.get("issue_id"):
        raise DraftRevisionError("Draft checkpoint issue identity mismatch")
    producer = agent._producer_for_checkpoint(cfg, "draft")
    if producer is None:
        raise DraftRevisionError("no lifecycle producer for Draft checkpoint")
    from_state, to_state = producer
    if prior_record.get("from_state") != from_state or prior_record.get("to_state") != to_state:
        raise DraftRevisionError("Draft checkpoint lifecycle producer mismatch")
    rows: dict[str, dict[str, str]] = {}
    for row in prior_record.get("artifacts", []):
        if not isinstance(row, dict) or not row.get("name") or row.get("name") in rows:
            raise DraftRevisionError("Draft checkpoint artifact rows invalid")
        rows[row["name"]] = {"path": row.get("path"), "sha256": row.get("sha256")}
    return rows


def _establishment_gates(
    repo_root: Path, cfg: dict[str, Any], state: dict[str, Any]
) -> tuple[dict[str, Any], Path]:
    """Enforce the narrow DRAFT_COMPLETE establishment boundary. Returns (profile, source_root)."""
    if state.get("lifecycle_state") != "DRAFT_COMPLETE":
        raise DraftRevisionError("Draft revision establishment requires DRAFT_COMPLETE lifecycle")
    if state.get("human_gates", {}).get("architecture_review") != "approved":
        raise DraftRevisionError("Draft revision establishment requires approved Architecture Review")
    if state.get("human_gates", {}).get("publication_preview") != "pending":
        raise DraftRevisionError("Draft revision establishment requires pending Publication Preview")
    if state.get("human_gate_provenance", {}).get("publication_preview") is not None:
        raise DraftRevisionError("Draft revision forbids existing Publication Preview provenance")
    for gate in ("validation", "freeze", "release"):
        if state.get("machine_checkpoints", {}).get(gate) != "pending":
            raise DraftRevisionError(f"Draft revision forbids resolved {gate} checkpoint")
    exception = state.get("exception_gate", {})
    if exception.get("status") != "inactive":
        raise DraftRevisionError("Draft revision forbids active Exception Gate")
    try:
        _, profile, source_root = agent._profile_and_source(repo_root, cfg, state)
    except (OSError, ValueError, KeyError) as exc:
        raise DraftRevisionError(str(exc)) from exc
    arch_auth = state.get("human_gate_provenance", {}).get("architecture_review")
    approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
    if (
        not isinstance(arch_auth, dict)
        or arch_auth.get("path") != str(approval_path.resolve().relative_to(repo_root.resolve()))
        or not approval_path.is_file()
        or core.sha256_file(approval_path) != arch_auth.get("sha256")
    ):
        raise DraftRevisionError("Draft revision requires intact Architecture approval provenance")
    return profile, source_root


def _architecture_paths(
    repo_root: Path, cfg: dict[str, Any], profile: dict[str, Any], source_root: Path
) -> tuple[Path, Path, Path]:
    """Resolve canonical Architecture / review-summary / approval paths.

    Filenames follow the same Core-wide source_root conventions used by the
    drafting runners and agent control; the approval path additionally comes
    from Core configuration, never edition-specific code.
    """
    architecture_path = core.repo_local_path(
        repo_root, str(profile["paths"]["source_root"]) + "/architecture-v2.json", "Issue Architecture"
    )
    review_summary_path = architecture_path.parent / "architecture-review-summary-v2.json"
    approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
    for path, label in (
        (architecture_path, "Issue Architecture"),
        (review_summary_path, "Architecture Review Summary"),
    ):
        if path.is_symlink() or not path.is_file():
            raise DraftRevisionError(f"{label} missing or unsafe")
    return architecture_path, review_summary_path, approval_path


def establish_draft_revision(
    repo_root: Path,
    cfg: dict[str, Any],
    state_path: Path,
    reason: str,
    executor: str,
    review_path: Path,
    recorded_at: datetime,
    implementation_sha: str | None = None,
) -> Path:
    """Establish new immutable authority for a reviewed Draft revision.

    Historical checkpoints are never rewritten. The new record explicitly
    supersedes named Draft-result/synthesis rows only; every other
    checkpoint-bound byte must match exactly. Successors are revalidated with
    the existing generic Draft validators, never a bare SHA override, and the
    review authority must be an explicit PASS binding.
    """
    repo_root = repo_root.resolve()
    if not isinstance(reason, str) or not reason.strip():
        raise DraftRevisionError("Draft revision requires a non-empty reason")
    if not isinstance(executor, str) or not executor.strip():
        raise DraftRevisionError("Draft revision requires executor identity")
    state = core.load_json(state_path)
    profile, source_root = _establishment_gates(repo_root, cfg, state)
    try:
        review_file = core.repo_local_path(repo_root, str(review_path), "Draft revision review authority")
    except (TypeError, ValueError) as exc:
        raise DraftRevisionError(str(exc)) from exc
    if review_file.is_symlink() or not review_file.is_file():
        raise DraftRevisionError("Draft revision review authority missing or unsafe")
    try:
        review_payload = core.load_json(review_file)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise DraftRevisionError(f"Draft revision review authority unreadable: {exc}") from exc
    if not isinstance(review_payload, dict):
        raise DraftRevisionError("Draft revision review authority must be a JSON object")
    if review_payload.get("decision") != "PASS":
        raise DraftRevisionError("Draft revision review authority is not an accepted PASS review")
    reviewed_by = review_payload.get("reviewed_by")
    if not isinstance(reviewed_by, str) or not reviewed_by.strip():
        raise DraftRevisionError("Draft revision review authority lacks reviewer identity")

    rows = _draft_checkpoint_rows(repo_root, cfg, state)
    # A State-bound active record means earlier reviewed bytes already
    # supersede history: new drift chains against the active record's revised
    # rows, never by rewriting the historical checkpoint. A referenced but
    # invalid record is fail-closed here; recovery is rollback, not repair.
    pointer = state.get("draft_revision_provenance")
    supersedes: dict[str, str] | None = None
    base_rows = rows
    if pointer is not None:
        active, active_errors = resolve_active_draft_revision(repo_root, cfg, state)
        if active is None or active_errors:
            detail = "; ".join(active_errors) if active_errors else "missing"
            raise DraftRevisionError(
                f"active Draft revision invalid; cannot chain: {detail}")
        base_rows = record_revised_rows(active)
        if not base_rows:
            raise DraftRevisionError("active Draft revision carries no revised rows")
        try:
            active_path = core.repo_local_path(
                repo_root, pointer["path"], "active Draft revision record")
        except (TypeError, ValueError) as exc:
            raise DraftRevisionError(str(exc)) from exc
        supersedes = {"path": pointer["path"], "sha256": core.sha256_file(active_path)}
    # Every non-draft passed checkpoint must be clean; drift may only exist on
    # eligible Draft rows. This single expectation proves upstream + packages intact.
    actual_errors = agent.validate_agent_state(repo_root, cfg, state)
    drifted: set[str] = set()
    other_errors: list[str] = []
    for error in actual_errors:
        if error.startswith("Stage Checkpoint artifact drift: "):
            drifted.add(error[len("Stage Checkpoint artifact drift: "):])
        else:
            other_errors.append(error)
    if other_errors:
        raise DraftRevisionError(
            "Draft revision requires otherwise-intact Production State: " + "; ".join(other_errors)
        )
    if not drifted:
        raise DraftRevisionError("Draft revision requires at least one regenerated Draft artifact")
    for name in sorted(drifted):
        if not _eligible_superseded_name(name):
            raise DraftRevisionError(f"Draft revision supersession not eligible: {name}")
        row = base_rows.get(name)
        if row is None:
            raise DraftRevisionError(f"Draft revision superseded row not in prior checkpoint: {name}")
        try:
            resolved = core.repo_local_path(repo_root, row["path"], f"superseded artifact {name}")
        except (TypeError, ValueError) as exc:
            raise DraftRevisionError(str(exc)) from exc
        if resolved.is_symlink() or not resolved.is_file():
            raise DraftRevisionError(f"Draft revision successor bytes missing: {name}")
        if core.sha256_file(resolved) == row["sha256"]:
            raise DraftRevisionError(f"Draft revision successor bytes unchanged: {name}")

    architecture_path, review_summary_path, approval_path = _architecture_paths(
        repo_root, cfg, profile, source_root
    )
    architecture = core.load_json(architecture_path)
    plan_packages = architecture.get("packages", [])
    pairs: list[tuple[Path, Path]] = []
    result_rows: list[dict[str, str]] = []
    ordered_ids = sorted(
        (row.get("package_id") for row in plan_packages if isinstance(row, dict)),
    )
    for package_id in ordered_ids:
        package_name, result_name = f"draft-package:{package_id}", f"draft-result:{package_id}"
        for required in (package_name, result_name):
            if required not in base_rows:
                raise DraftRevisionError(f"Draft checkpoint lacks canonical row: {required}")
        package_path = core.repo_local_path(repo_root, base_rows[package_name]["path"], f"Draft package {package_id}")
        result_path = core.repo_local_path(repo_root, base_rows[result_name]["path"], f"Draft Result {package_id}")
        result = core.load_json(result_path)
        errors = drafting_base.validate_draft_result(
            result, package_path, repo_root / drafting_base.DRAFT_PROMPT
        )
        if errors:
            raise DraftRevisionError(f"Draft Result invalid for {package_id}: " + "; ".join(errors))
        if result.get("package_id") != package_id:
            raise DraftRevisionError(f"Draft Result package identity mismatch: {package_id}")
        pairs.append((package_path, result_path))
        result_rows.append({
            "package_id": package_id,
            "path": _rel(repo_root, result_path, f"Draft Result {package_id}"),
            "sha256": core.sha256_file(result_path),
        })
    expected_input = drafting_base.build_synthesis_input(
        repo_root,
        repo_root / state["profile"]["path"],
        architecture_path,
        review_summary_path,
        approval_path,
        pairs,
    )
    synthesis_input_row = rows.get("synthesis-input")
    synthesis_result_row = rows.get("synthesis-result")
    if synthesis_input_row is None or synthesis_result_row is None:
        raise DraftRevisionError("Draft checkpoint lacks canonical synthesis rows")
    synthesis_input_path = core.repo_local_path(
        repo_root, synthesis_input_row["path"], "profile synthesis input"
    )
    if core.load_json(synthesis_input_path) != expected_input:
        raise DraftRevisionError("Profile Synthesis Input differs from current reviewed Draft Results")
    synthesis_result_path = core.repo_local_path(
        repo_root, synthesis_result_row["path"], "profile synthesis result"
    )
    synthesis_errors = drafting_base.validate_synthesis_result(
        core.load_json(synthesis_result_path),
        synthesis_input_path,
        repo_root / drafting_base.SYNTHESIS_PROMPT,
    )
    if synthesis_errors:
        raise DraftRevisionError("Profile Synthesis Result invalid: " + "; ".join(synthesis_errors))

    superseded: list[dict[str, Any]] = []
    preserved: list[dict[str, Any]] = []
    for name in sorted(base_rows):
        row = base_rows[name]
        resolved = core.repo_local_path(repo_root, row["path"], f"checkpoint artifact {name}")
        current_sha = core.sha256_file(resolved)
        if name in drifted:
            superseded.append({
                "name": name,
                "path": row["path"],
                "prior_sha256": row["sha256"],
                "new_sha256": current_sha,
                "byte_count": resolved.stat().st_size,
            })
        else:
            preserved.append({"name": name, "path": row["path"], "sha256": current_sha})
    if not superseded:
        raise DraftRevisionError("Draft revision requires at least one superseded artifact")

    sequences: list[int] = []
    revision_dir = source_root / "draft" / "v2"
    if revision_dir.is_dir():
        for child in sorted(revision_dir.iterdir()):
            if child.is_symlink() or not child.is_file():
                continue
            name = child.name
            prefix = DRAFT_REVISION_BASENAME + "-r"
            if name.startswith(prefix) and name.endswith(".json"):
                middle = name[len(prefix):-len(".json")]
                if middle.isdigit() and not middle.startswith("0"):
                    sequences.append(int(middle))
    sequences = sorted(sequences)
    sequence = (max(sequences) + 1) if sequences else 1
    record_path = revision_dir / f"{DRAFT_REVISION_BASENAME}-r{sequence}.json"
    if record_path.exists():
        raise DraftRevisionError("Draft revision sequence collision")
    draft_provenance = (state.get("checkpoint_provenance") or {}).get("draft")
    establishment_state_sha = core.sha256_file(state_path)
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": state["issue_id"],
        "reason_class": "REVIEWED_DRAFT_REVISION",
        "reason": reason.strip(),
        "lifecycle": "DRAFT_COMPLETE",
        "prior_checkpoint": {"path": draft_provenance["path"], "sha256": draft_provenance["sha256"]},
        "superseded_artifacts": superseded,
        "preserved_artifacts": preserved,
        "review": {
            "path": _rel(repo_root, review_file, "Draft revision review authority"),
            "sha256": core.sha256_file(review_file),
            "decision": "PASS",
            "reviewed_by": reviewed_by.strip(),
        },
        "validation": {
            "draft_results": result_rows,
            "synthesis_input": {
                "path": synthesis_input_row["path"],
                "sha256": core.sha256_file(synthesis_input_path),
            },
            "synthesis_result": {
                "path": synthesis_result_row["path"],
                "sha256": core.sha256_file(synthesis_result_path),
            },
            "architecture": {
                "path": _rel(repo_root, architecture_path, "Issue Architecture"),
                "sha256": core.sha256_file(architecture_path),
            },
            "architecture_approval": {
                "path": _rel(repo_root, approval_path, "Architecture approval"),
                "sha256": core.sha256_file(approval_path),
            },
            "summary": (
                f"reviewed Draft revision r{sequence} ({reviewed_by.strip()}): "
                f"{len(superseded)} artifact(s) rebound with fresh generic Draft validation; "
                "upstream authority preserved byte-identical"
            ),
        },
        "core": {
            "contract": core.contract_identity(
                repo_root, cfg, state["research_profile"], state["publication_profile"]
            ),
            "implementation_commit_sha": core.repository_commit_sha(repo_root, implementation_sha),
        },
        "executor": executor.strip(),
        "recorded_at": core.iso_utc(recorded_at),
        "supersedes": supersedes,
        "establishment": {
            "state_sha256": establishment_state_sha,
            "lifecycle": "DRAFT_COMPLETE",
            "architecture_review": "approved",
            "publication_preview": "pending",
            "validation": "pending",
            "freeze": "pending",
            "release": "pending",
            "implementation_commit_sha": core.repository_commit_sha(repo_root, implementation_sha),
            "recorded_at": core.iso_utc(recorded_at),
        },
    }
    schema_gate.validate_instance(payload, repo_root / DRAFT_REVISION_SCHEMA, label="Draft Surface Revision")
    core.write_json(record_path, payload)
    updated = deepcopy(state)
    updated["draft_revision_provenance"] = {
        "path": str(record_path.resolve().relative_to(repo_root.resolve())),
        "sha256": core.sha256_file(record_path),
    }
    core.write_json(state_path, updated)
    post_errors = validate_agent_state_proxy(repo_root, cfg, state_path)
    if post_errors:
        raise DraftRevisionError(
            "Draft revision established but resulting State invalid: " + "; ".join(post_errors)
        )
    return record_path


def validate_agent_state_proxy(repo_root: Path, cfg: dict[str, Any], state_path: Path) -> list[str]:
    """validate_agent_state without a hard cross-module import cycle at call time."""
    return agent.validate_agent_state(repo_root, cfg, core.load_json(state_path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--state", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--executor", required=True)
    parser.add_argument("--review", required=True)
    parser.add_argument("--recorded-at")
    parser.add_argument("--implementation-sha")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = Path(args.state)
    if not state_path.is_absolute():
        state_path = root / state_path
    review_path = Path(args.review)
    if not review_path.is_absolute():
        review_path = root / review_path
    try:
        recorded = core.parse_instant(args.recorded_at) if args.recorded_at else datetime.now().astimezone()
        path = establish_draft_revision(
            root,
            cfg,
            state_path,
            args.reason,
            args.executor,
            review_path,
            recorded,
            args.implementation_sha,
        )
    except (DraftRevisionError, OSError, ValueError) as exc:
        raise SystemExit(str(exc))
    print(str(path.resolve().relative_to(root)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
