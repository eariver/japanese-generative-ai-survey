#!/usr/bin/env python3
"""Production handler/validator registry for Survey Production Core v2.

A stage never searches for a convenient "latest" run. Before planning an
executable stage, production prepares one canonical Stage Handoff whose exact
bytes are pinned in the Action Spec. The generic handler only returns the exact
handoff outputs; stage validators then re-run the authoritative WU-006..WU-011
contracts over those bytes before the orchestrator may attest a checkpoint.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import survey_architecture_v2 as architecture
from scripts import survey_completeness_v2 as completeness
from scripts import survey_discovery_v2 as discovery
from scripts import survey_draft_profile_v2 as draft_profile
from scripts import survey_drafting_v2 as drafting
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_quality_v2 as quality
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening

HANDOFF_SCHEMA = Path("schemas/stage-handoff-v2.schema.json")


class StageContractError(ValueError):
    pass


def canonical_handoff_path(repo_root: Path, state: dict[str, Any]) -> Path:
    profile = core.load_json(core.repo_local_path(repo_root, state["profile"]["path"], "state.profile.path"))
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    return source_root / "orchestration/v2/handoffs" / f"{state['lifecycle_state']}.json"


def _spec_input(spec: dict[str, Any], name: str) -> dict[str, Any]:
    rows = [row for row in spec.get("required_inputs", []) if isinstance(row, dict) and row.get("name") == name]
    if len(rows) != 1:
        raise StageContractError(f"Action Spec must bind exactly one {name} input")
    return rows[0]


def _safe_bound_file(repo_root: Path, ref: dict[str, Any], label: str) -> Path:
    path = core.repo_local_path(repo_root, ref.get("path"), label)
    if path.is_symlink() or not path.is_file():
        raise StageContractError(f"{label} missing or unsafe: {ref.get('path')}")
    if core.sha256_file(path) != ref.get("sha256"):
        raise StageContractError(f"{label} SHA drift: {ref.get('path')}")
    return path


def load_handoff(
    repo_root: Path,
    state: dict[str, Any],
    spec: dict[str, Any],
) -> dict[str, Any]:
    handoff_ref = _spec_input(spec, "stage-handoff")
    handoff_path = canonical_handoff_path(repo_root, state)
    expected_rel = str(handoff_path.resolve().relative_to(repo_root.resolve()))
    if handoff_ref.get("path") != expected_rel:
        raise StageContractError("Action Spec Stage Handoff path is not canonical")
    if handoff_ref.get("sha256") != core.sha256_file(handoff_path):
        raise StageContractError("Action Spec Stage Handoff SHA drift")
    handoff = schema_gate.load_and_validate_json(
        handoff_path, repo_root / HANDOFF_SCHEMA, label="Stage Handoff"
    )
    if handoff["issue_id"] != state["issue_id"]:
        raise StageContractError("Stage Handoff issue_id mismatch")
    if handoff["lifecycle_state"] != state["lifecycle_state"]:
        raise StageContractError("Stage Handoff lifecycle_state mismatch")
    if handoff["handler"] != spec.get("handler"):
        raise StageContractError("Stage Handoff handler identity mismatch")
    expected_basis = {
        "production_state_sha256": spec["basis"]["production_state_sha256"],
        "production_profile_sha256": spec["basis"]["production_profile_sha256"],
        "pipeline_contract_sha256": spec["basis"]["pipeline_contract_sha256"],
        "quality_contract_sha256": spec["basis"]["quality_contract_sha256"],
        "implementation_commit_sha": spec["basis"]["implementation_commit_sha"],
    }
    if handoff["basis"] != expected_basis:
        raise StageContractError("Stage Handoff basis does not match current authoritative Action Spec")

    for collection_name in ("inputs", "outputs"):
        rows = handoff[collection_name]
        names = [row["name"] for row in rows]
        if len(names) != len(set(names)):
            raise StageContractError(f"Stage Handoff {collection_name} names must be unique")
        for row in rows:
            _safe_bound_file(repo_root, row, f"Stage Handoff {collection_name[:-1]} {row['name']}")

    expected_outputs = {row["name"]: row for row in spec.get("expected_outputs", [])}
    actual_outputs = {row["name"]: row for row in handoff["outputs"]}
    required_names = {name for name, row in expected_outputs.items() if row.get("required") is True}
    if set(actual_outputs) != required_names:
        raise StageContractError(
            f"Stage Handoff outputs must exactly cover required Action outputs: expected={sorted(required_names)} actual={sorted(actual_outputs)}"
        )
    for name, actual in actual_outputs.items():
        expected = expected_outputs[name]
        if actual.get("checkpoint") != expected.get("checkpoint"):
            raise StageContractError(f"Stage Handoff output checkpoint mismatch: {name}")
        if expected.get("path") is not None and actual.get("path") != expected.get("path"):
            raise StageContractError(f"Stage Handoff output path mismatch: {name}")
    return handoff


def _inputs(repo_root: Path, handoff: dict[str, Any]) -> dict[str, Path]:
    return {
        row["name"]: _safe_bound_file(repo_root, row, f"Stage input {row['name']}")
        for row in handoff["inputs"]
    }


def _outputs(repo_root: Path, handoff: dict[str, Any]) -> dict[str, Path]:
    return {
        row["name"]: _safe_bound_file(repo_root, row, f"Stage output {row['name']}")
        for row in handoff["outputs"]
    }


def _require(mapping: dict[str, Path], *names: str) -> list[Path]:
    missing = [name for name in names if name not in mapping]
    if missing:
        raise StageContractError(f"Stage Handoff missing required named artifacts: {missing}")
    return [mapping[name] for name in names]


def _same_authority(handoff: dict[str, Any], left_kind: str, left_name: str, right_kind: str, right_name: str) -> None:
    left_rows = {row["name"]: row for row in handoff[left_kind]}
    right_rows = {row["name"]: row for row in handoff[right_kind]}
    left = left_rows.get(left_name)
    right = right_rows.get(right_name)
    if left is None or right is None or left.get("path") != right.get("path") or left.get("sha256") != right.get("sha256"):
        raise StageContractError(f"Stage Handoff authority mismatch: {left_name} != {right_name}")


def _materialized_pdf_matches(repo_root: Path, ref: dict[str, Any], pdf_path: Path, label: str) -> None:
    if ref.get("sha256") != core.sha256_file(pdf_path) or ref.get("byte_count") != pdf_path.stat().st_size:
        raise StageContractError(f"{label} does not bind exact materialized publication PDF bytes")
    if ref.get("storage") == "REPOSITORY_FILE" and ref.get("path") != str(pdf_path.relative_to(repo_root)):
        raise StageContractError(f"{label} repository PDF path differs from Stage Handoff materialization")


def stage_handoff_handler(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    spec: dict[str, Any],
    implementation_sha: str,
) -> list[dict[str, Any]]:
    del cfg, implementation_sha
    handoff = load_handoff(repo_root, state, spec)
    return [dict(row) for row in handoff["outputs"]]


def _validator_errors(fn):
    def wrapped(repo_root, cfg, state, spec, outputs, implementation_sha):
        del outputs
        try:
            handoff = load_handoff(repo_root, state, spec)
            fn(repo_root, cfg, state, spec, handoff, implementation_sha)
            return []
        except (OSError, ValueError, KeyError) as exc:
            return [str(exc)]
    return wrapped


@_validator_errors
def validate_discovery(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec, implementation_sha
    outputs = _outputs(repo_root, handoff)
    (accepted,) = _require(outputs, "discovery-acceptance")
    payload = discovery.validate_acceptance(repo_root, accepted)
    if payload["issue_id"] != state["issue_id"]:
        raise StageContractError("Discovery acceptance issue identity mismatch")
    _same_authority(handoff, "outputs", "discovery", "outputs", "discovery-acceptance")


@_validator_errors
def validate_screening(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec
    inputs = _inputs(repo_root, handoff)
    discovery_path, acceptance_path = _require(inputs, "discovery-jsonl", "screening-acceptance")
    accepted = screening.validate_acceptance(repo_root, acceptance_path, implementation_sha)
    if accepted["issue_id"] != state["issue_id"]:
        raise StageContractError("Screening acceptance issue identity mismatch")
    effective = screening.resolve_effective_discovery_basis(
        repo_root, acceptance_path.parent / "package.json", implementation_sha
    )
    if effective["path"].resolve() != discovery_path.resolve():
        raise StageContractError("Stage Handoff Discovery is not the effective Screening Discovery basis")
    _same_authority(handoff, "inputs", "screening-acceptance", "outputs", "screening")
    package = core.load_json(acceptance_path.parent / "package.json")
    if package.get("basis", {}).get("discovery_sha256") != effective["sha256"]:
        raise StageContractError("Screening acceptance does not bind Stage Handoff Discovery bytes")


def _evidence_basis(repo_root: Path, state: dict[str, Any], handoff: dict[str, Any], implementation_sha: str):
    inputs = _inputs(repo_root, handoff)
    names = (
        "discovery-jsonl", "screening-acceptance", "evidence-acceptance",
        "edition-views-acceptance", "materiality-ledger", "profile-completeness",
    )
    discovery_path, screening_path, evidence_path, views_path, ledger_path, completeness_path = _require(inputs, *names)
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "state.profile.path")
    evidence.validate_screening_acceptance(repo_root, screening_path, discovery_path, state["issue_id"], implementation_sha)
    evidence.validate_evidence_acceptance(repo_root, evidence_path, implementation_sha)
    evidence.validate_edition_views_acceptance(repo_root, profile_path, evidence_path, views_path, implementation_sha)
    ledger = core.load_json(ledger_path)
    evidence.validate_materiality_ledger(
        ledger, repo_root, profile_path, discovery_path, screening_path,
        evidence_path, views_path, implementation_sha,
    )
    completeness_payload = schema_gate.load_and_validate_json(
        completeness_path, repo_root / Path("schemas/profile-completeness-result.schema.json"),
        label="Profile Completeness",
    )
    errors = completeness.validate_profile_completeness(
        completeness_payload, repo_root, profile_path, discovery_path, screening_path,
        evidence_path, views_path, ledger_path, implementation_sha,
    )
    if errors:
        raise StageContractError("Profile Completeness invalid: " + "; ".join(errors))
    return {
        "profile": profile_path,
        "discovery": discovery_path,
        "screening": screening_path,
        "evidence": evidence_path,
        "views": views_path,
        "ledger": ledger_path,
        "completeness": completeness_path,
    }


@_validator_errors
def validate_evidence_materiality_completeness(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec
    _evidence_basis(repo_root, state, handoff, implementation_sha)
    _same_authority(handoff, "inputs", "evidence-acceptance", "outputs", "evidence")
    _same_authority(handoff, "inputs", "materiality-ledger", "outputs", "materiality")
    _same_authority(handoff, "inputs", "profile-completeness", "outputs", "completeness")


def _selection_basis(repo_root: Path, state: dict[str, Any], handoff: dict[str, Any], implementation_sha: str):
    basis = _evidence_basis(repo_root, state, handoff, implementation_sha)
    inputs = _inputs(repo_root, handoff)
    matrix_path, selection_path = _require(inputs, "candidate-matrix", "candidate-selection")
    matrix = schema_gate.load_and_validate_json(
        matrix_path, repo_root / Path("schemas/candidate-matrix-v2.schema.json"), label="Candidate Matrix"
    )
    errors = architecture.validate_candidate_matrix(
        matrix, repo_root, basis["profile"], basis["discovery"], basis["screening"],
        basis["evidence"], basis["views"], basis["ledger"], basis["completeness"], implementation_sha,
    )
    if errors:
        raise StageContractError("Candidate Matrix invalid: " + "; ".join(errors))
    selection = schema_gate.load_and_validate_json(
        selection_path, repo_root / Path("schemas/candidate-selection-v2.schema.json"), label="Candidate Selection"
    )
    errors = architecture.validate_selection(
        repo_root, selection, basis["profile"], matrix_path, basis["completeness"], basis["ledger"]
    )
    if errors:
        raise StageContractError("Candidate Selection invalid: " + "; ".join(errors))
    basis.update({"matrix": matrix_path, "selection": selection_path})
    return basis


@_validator_errors
def validate_selection(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec
    _selection_basis(repo_root, state, handoff, implementation_sha)
    _same_authority(handoff, "inputs", "candidate-selection", "outputs", "selection")


@_validator_errors
def validate_architecture(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec
    basis = _selection_basis(repo_root, state, handoff, implementation_sha)
    inputs = _inputs(repo_root, handoff)
    architecture_path, review_path, attention_path = _require(
        inputs, "issue-architecture", "architecture-review-summary", "architecture-review-attention"
    )
    plan = schema_gate.load_and_validate_json(
        architecture_path, repo_root / Path("schemas/issue-architecture-v2.schema.json"), label="Issue Architecture"
    )
    errors = architecture.validate_architecture(
        repo_root, plan, basis["profile"], basis["completeness"], basis["ledger"],
        basis["matrix"], basis["selection"], require_approved=False,
    )
    if errors:
        raise StageContractError("Issue Architecture invalid: " + "; ".join(errors))
    review = schema_gate.load_and_validate_json(
        review_path, repo_root / Path("schemas/architecture-review-summary-v2.schema.json"),
        label="Architecture Review Summary",
    )
    expected_review = architecture.build_architecture_review_summary(
        repo_root, basis["profile"], basis["discovery"], basis["screening"], basis["evidence"],
        basis["views"], basis["ledger"], basis["completeness"], basis["matrix"], basis["selection"],
        architecture_path, implementation_sha,
    )
    if review != expected_review:
        raise StageContractError("Architecture Review Summary differs from validated derivation")
    review_attention.validate_attention(repo_root, attention_path)
    _same_authority(handoff, "inputs", "issue-architecture", "outputs", "architecture")
    _same_authority(handoff, "inputs", "issue-architecture", "outputs", "issue-architecture")
    _same_authority(handoff, "inputs", "architecture-review-summary", "outputs", "architecture-review-summary")
    _same_authority(handoff, "inputs", "architecture-review-attention", "outputs", "architecture-review-attention")


@_validator_errors
def validate_drafting_synthesis(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec, implementation_sha
    inputs = _inputs(repo_root, handoff)
    architecture_path, review_path, approval_path, synthesis_input_path, synthesis_result_path = _require(
        inputs,
        "issue-architecture", "architecture-review-summary", "architecture-approval",
        "synthesis-input", "synthesis-result",
    )
    profile_path = core.repo_local_path(repo_root, state["profile"]["path"], "state.profile.path")
    package_names = sorted(name for name in inputs if name.startswith("draft-package:"))
    result_names = sorted(name for name in inputs if name.startswith("draft-result:"))
    package_ids = {name.split(":", 1)[1] for name in package_names}
    result_ids = {name.split(":", 1)[1] for name in result_names}
    if not package_ids or package_ids != result_ids:
        raise StageContractError("Drafting handoff requires exactly paired draft-package:/draft-result: inputs")
    for package_id in sorted(package_ids):
        package_path = inputs[f"draft-package:{package_id}"]
        result_path = inputs[f"draft-result:{package_id}"]
        package = schema_gate.load_and_validate_json(
            package_path, repo_root / drafting.DRAFT_PACKAGE_SCHEMA, label=f"Draft Package {package_id}"
        )
        errors = drafting.validate_self_contained_draft_package(
            package, profile_path, architecture_path, review_path, approval_path
        )
        result = schema_gate.load_and_validate_json(
            result_path, repo_root / drafting.DRAFT_RESULT_SCHEMA, label=f"Draft Result {package_id}"
        )
        errors += drafting.validate_draft_result(result, package_path, repo_root / drafting.DRAFT_PROMPT)
        errors += draft_profile.validate_extension_propagation(result, package)
        if errors:
            raise StageContractError(f"Draft package/result {package_id} invalid: " + "; ".join(errors))
    schema_gate.load_and_validate_json(
        synthesis_input_path, repo_root / drafting.SYNTHESIS_INPUT_SCHEMA, label="Profile Synthesis Input"
    )
    synthesis_result = schema_gate.load_and_validate_json(
        synthesis_result_path, repo_root / drafting.SYNTHESIS_RESULT_SCHEMA, label="Profile Synthesis Result"
    )
    errors = drafting.validate_synthesis_result(
        synthesis_result, synthesis_input_path, repo_root / drafting.SYNTHESIS_PROMPT
    )
    if errors:
        raise StageContractError("Profile Synthesis Result invalid: " + "; ".join(errors))
    _same_authority(handoff, "inputs", "synthesis-result", "outputs", "draft")


@_validator_errors
def validate_semantic_publication(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec, implementation_sha
    inputs = _inputs(repo_root, handoff)
    source_path, pdf_path, bundle_path = _require(
        inputs, "validated-source", "publication-pdf", "quality-regression-bundle"
    )
    bundle = quality.validate_bundle(repo_root, bundle_path, issue_id=state["issue_id"])
    if bundle["source"]["path"] != str(source_path.relative_to(repo_root)) or bundle["source"]["sha256"] != core.sha256_file(source_path):
        raise StageContractError("Quality bundle does not bind exact validated source")
    _materialized_pdf_matches(repo_root, bundle["pdf"], pdf_path, "Quality bundle")
    _same_authority(handoff, "inputs", "quality-regression-bundle", "outputs", "validation")


@_validator_errors
def validate_publication_candidate(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec, implementation_sha
    inputs = _inputs(repo_root, handoff)
    source_path, pdf_path, bundle_path, candidate_path = _require(
        inputs, "validated-source", "publication-pdf", "quality-regression-bundle", "publication-candidate"
    )
    candidate = publication.validate_candidate(repo_root, candidate_path, issue_id=state["issue_id"])
    for key, path in {"source": source_path, "quality_bundle": bundle_path}.items():
        ref = candidate[key]
        if ref["path"] != str(path.relative_to(repo_root)) or ref["sha256"] != core.sha256_file(path):
            raise StageContractError(f"Publication Candidate {key} does not match Stage Handoff authority")
    _materialized_pdf_matches(repo_root, candidate["pdf"], pdf_path, "Publication Candidate")
    _same_authority(handoff, "inputs", "publication-candidate", "outputs", "publication-candidate")


@_validator_errors
def validate_freeze(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec, implementation_sha
    inputs = _inputs(repo_root, handoff)
    candidate_path, approval_path, visual_path, freeze_path, manifest_path = _require(
        inputs,
        "publication-candidate", "publication-preview-approval", "visual-review-record",
        "freeze-record", "release-manifest",
    )
    candidate = publication.validate_candidate(repo_root, candidate_path, issue_id=state["issue_id"])
    approval = publication.validate_preview_approval(repo_root, approval_path, issue_id=state["issue_id"])
    visual = publication.validate_visual_review(repo_root, visual_path, approval_path)
    freeze = schema_gate.load_and_validate_json(
        freeze_path, repo_root / publication.FREEZE_SCHEMA, label="Freeze record"
    )
    manifest = publication.validate_release_manifest(repo_root, manifest_path)
    exact = {
        "publication_candidate_path": str(candidate_path.relative_to(repo_root)),
        "publication_candidate_sha256": core.sha256_file(candidate_path),
        "publication_preview_approval_path": str(approval_path.relative_to(repo_root)),
        "publication_preview_approval_sha256": core.sha256_file(approval_path),
        "visual_review_path": str(visual_path.relative_to(repo_root)),
        "visual_review_sha256": core.sha256_file(visual_path),
        "source_path": candidate["source"]["path"],
        "source_sha256": candidate["source"]["sha256"],
        "pdf_path": approval["pdf_path"],
        "pdf_sha256": approval["pdf_sha256"],
        "page_count": approval["page_count"],
    }
    for key, value in exact.items():
        if freeze.get(key) != value:
            raise StageContractError(f"Freeze record authority mismatch: {key}")
    if visual["pdf_sha256"] != freeze["pdf_sha256"] or manifest["pdf_sha256"] != freeze["pdf_sha256"]:
        raise StageContractError("Freeze/Visual/Manifest exact PDF authority diverged")
    _same_authority(handoff, "inputs", "freeze-record", "outputs", "freeze")
    _same_authority(handoff, "inputs", "visual-review-record", "outputs", "visual-review-record")
    _same_authority(handoff, "inputs", "freeze-record", "outputs", "freeze-record")
    _same_authority(handoff, "inputs", "release-manifest", "outputs", "release-manifest")


@_validator_errors
def validate_release(repo_root, cfg, state, spec, handoff, implementation_sha):
    del cfg, spec, implementation_sha
    inputs = _inputs(repo_root, handoff)
    manifest_path, verification_path, release_path = _require(
        inputs, "release-manifest", "merge-verification", "release-record"
    )
    publication.validate_release_manifest(repo_root, manifest_path)
    schema_gate.load_and_validate_json(
        verification_path, repo_root / publication.MERGE_VERIFICATION_SCHEMA, label="Merge verification"
    )
    release = publication.validate_release_record(repo_root, release_path)
    if release["issue_id"] != state["issue_id"]:
        raise StageContractError("Release record issue identity mismatch")
    _same_authority(handoff, "inputs", "release-record", "outputs", "release")
    _same_authority(handoff, "inputs", "merge-verification", "outputs", "merge-verification")
    _same_authority(handoff, "inputs", "release-record", "outputs", "release-record")


def register_handlers(registry: dict[str, Any]) -> None:
    for handler_name in (
        "stage:discovery",
        "stage:screening",
        "stage:evidence-materiality-completeness",
        "stage:selection",
        "stage:architecture",
        "stage:drafting-synthesis",
        "stage:semantic-publication-validation",
        "stage:publication-candidate",
        "stage:freeze",
        "stage:release",
    ):
        registry[handler_name] = stage_handoff_handler
    registry.update(
        {
            "validate:discovery": validate_discovery,
            "validate:screening": validate_screening,
            "validate:evidence-materiality-completeness": validate_evidence_materiality_completeness,
            "validate:selection": validate_selection,
            "validate:architecture": validate_architecture,
            "validate:drafting-synthesis": validate_drafting_synthesis,
            "validate:semantic-publication": validate_semantic_publication,
            "validate:publication-candidate": validate_publication_candidate,
            "validate:freeze": validate_freeze,
            "validate:release": validate_release,
        }
    )
