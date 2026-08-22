#!/usr/bin/env python3
"""Exact-byte publication authority for Survey Production Core v2.

Publication Preview is the second and final normal Human Gate. Approval binds one
Publication Candidate and its PDF SHA. All later Visual Review, Freeze, merge
verification and Release records must consume the same exact bytes.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_quality_v2 as quality
from scripts import survey_schema_v2 as schema_gate

CANDIDATE_SCHEMA = Path("schemas/publication-candidate-v2.schema.json")
PREVIEW_APPROVAL_SCHEMA = Path("schemas/publication-preview-approval-v2.schema.json")
VISUAL_REVIEW_SCHEMA = Path("schemas/visual-review-record-v2.schema.json")
FREEZE_SCHEMA = Path("schemas/freeze-record-v2.schema.json")
RELEASE_MANIFEST_SCHEMA = Path("schemas/release-manifest-v2.schema.json")
MERGE_VERIFICATION_SCHEMA = Path("schemas/merge-verification-v2.schema.json")
RELEASE_RECORD_SCHEMA = Path("schemas/release-record-v2.schema.json")


def _rel(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root))
    except ValueError as exc:
        raise ValueError(f"publication artifact must be repository-local: {path}") from exc


def _safe_file(repo_root: Path, path: Path, label: str) -> Path:
    _rel(repo_root, path)
    resolved = path.resolve()
    if resolved.is_symlink() or not resolved.is_file():
        raise ValueError(f"{label} missing or unsafe: {path}")
    return resolved


def _authority(repo_root: Path, path: Path) -> dict[str, Any]:
    value = _safe_file(repo_root, path, "publication authority input")
    return {"path": _rel(repo_root, value), "sha256": core.sha256_file(value), "byte_count": value.stat().st_size}


def _write_immutable(path: Path, payload: dict[str, Any], label: str) -> Path:
    if path.exists():
        if core.load_json(path) != payload:
            raise ValueError(f"refusing to overwrite divergent {label}: {path}")
        return path
    core.write_json(path, payload)
    return path


def release_identity(publication_profile: str, issue_id: str) -> str:
    if publication_profile == "WEEKLY_MAGAZINE":
        return f"weekly/{issue_id}"
    if publication_profile == "LONGFORM_SPECIAL":
        return f"special/{issue_id}"
    raise ValueError(f"unsupported publication profile: {publication_profile}")


def build_candidate(
    repo_root: Path,
    issue_id: str,
    publication_profile: str,
    source_path: Path,
    pdf_path: Path,
    page_count: int,
    quality_bundle_path: Path,
    output_path: Path,
) -> Path:
    if not isinstance(page_count, int) or page_count < 1:
        raise ValueError("Publication Candidate page_count must be positive")
    source = _safe_file(repo_root, source_path, "validated publication source")
    pdf = _safe_file(repo_root, pdf_path, "publication PDF")
    bundle = quality.validate_bundle(repo_root, quality_bundle_path, issue_id=issue_id)
    if bundle["publication_profile"] != publication_profile:
        raise ValueError("Publication Candidate publication_profile differs from bound Quality Production Profile")
    if bundle["source"]["path"] != _rel(repo_root, source) or bundle["source"]["sha256"] != core.sha256_file(source):
        raise ValueError("quality bundle does not bind exact Publication Candidate source bytes")
    pdf_authority = dict(bundle["pdf"])
    if pdf_authority["sha256"] != core.sha256_file(pdf) or pdf_authority["byte_count"] != pdf.stat().st_size:
        raise ValueError("quality bundle does not bind exact Publication Candidate PDF bytes")
    if pdf_authority["storage"] == "REPOSITORY_FILE" and pdf_authority["path"] != _rel(repo_root, pdf):
        raise ValueError("quality bundle repository PDF path differs from Publication Candidate bytes")
    base = {
        "schema_version": "2.0-rc1",
        "issue_id": issue_id,
        "publication_profile": publication_profile,
        "status": "READY_FOR_PUBLICATION_PREVIEW",
        "source": _authority(repo_root, source),
        "pdf": {**pdf_authority, "page_count": page_count},
        "quality_bundle": _authority(repo_root, quality_bundle_path),
    }
    payload = dict(base)
    payload["candidate_sha256"] = core.sha256_object(base)
    schema_gate.validate_instance(payload, repo_root / CANDIDATE_SCHEMA, label="Publication Candidate")
    _write_immutable(output_path, payload, "Publication Candidate")
    return output_path


def validate_candidate(repo_root: Path, path: Path, *, issue_id: str | None = None) -> dict[str, Any]:
    payload = schema_gate.load_and_validate_json(path, repo_root / CANDIDATE_SCHEMA, label="Publication Candidate")
    if issue_id is not None and payload["issue_id"] != issue_id:
        raise ValueError("Publication Candidate issue_id mismatch")
    base = {key: payload[key] for key in ("schema_version", "issue_id", "publication_profile", "status", "source", "pdf", "quality_bundle")}
    if payload["candidate_sha256"] != core.sha256_object(base):
        raise ValueError("Publication Candidate content digest mismatch")
    for key in ("source", "quality_bundle"):
        ref = payload[key]
        artifact = _safe_file(repo_root, repo_root / ref["path"], f"Publication Candidate {key}")
        if core.sha256_file(artifact) != ref["sha256"] or artifact.stat().st_size != ref["byte_count"]:
            raise ValueError(f"Publication Candidate {key} bytes drifted")
    bundle = quality.validate_bundle(repo_root, repo_root / payload["quality_bundle"]["path"], issue_id=payload["issue_id"])
    if bundle["publication_profile"] != payload["publication_profile"]:
        raise ValueError("Publication Candidate publication_profile diverges from coupled Quality Production Profile")
    candidate_pdf = {key: payload["pdf"][key] for key in ("storage", "path", "sha256", "byte_count", "actions_artifact")}
    if candidate_pdf != bundle["pdf"]:
        raise ValueError("Publication Candidate PDF authority diverges from coupled quality bundle")
    return payload


def build_preview_approval(
    repo_root: Path,
    candidate_path: Path,
    output_path: Path,
    reviewed_by: str,
    reviewed_at: datetime,
    review_reference: str,
) -> Path:
    candidate = validate_candidate(repo_root, candidate_path)
    if not reviewed_by.strip() or not review_reference.strip():
        raise ValueError("Publication Preview reviewed_by/review_reference required")
    seed = {
        "issue_id": candidate["issue_id"],
        "candidate_sha256": core.sha256_file(candidate_path),
        "pdf_sha256": candidate["pdf"]["sha256"],
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
    }
    payload = {
        "schema_version": "2.0-rc1",
        "approval_id": f"publication-preview:{candidate['issue_id']}:{core.sha256_object(seed)[:20]}",
        "issue_id": candidate["issue_id"],
        "gate": "PUBLICATION_PREVIEW",
        "decision": "APPROVED",
        "publication_candidate_path": _rel(repo_root, candidate_path),
        "publication_candidate_sha256": core.sha256_file(candidate_path),
        "pdf_path": candidate["pdf"]["path"],
        "pdf_sha256": candidate["pdf"]["sha256"],
        "page_count": candidate["pdf"]["page_count"],
        "reviewed_by": reviewed_by,
        "reviewed_at": core.iso_utc(reviewed_at),
        "review_reference": review_reference,
    }
    schema_gate.validate_instance(payload, repo_root / PREVIEW_APPROVAL_SCHEMA, label="Publication Preview approval")
    _write_immutable(output_path, payload, "Publication Preview approval")
    return output_path


def validate_preview_approval(repo_root: Path, path: Path, *, issue_id: str | None = None) -> dict[str, Any]:
    approval = schema_gate.load_and_validate_json(path, repo_root / PREVIEW_APPROVAL_SCHEMA, label="Publication Preview approval")
    if issue_id is not None and approval["issue_id"] != issue_id:
        raise ValueError("Publication Preview approval issue_id mismatch")
    candidate_path = _safe_file(repo_root, repo_root / approval["publication_candidate_path"], "Publication Candidate")
    if core.sha256_file(candidate_path) != approval["publication_candidate_sha256"]:
        raise ValueError("Publication Preview approved candidate bytes drifted")
    candidate = validate_candidate(repo_root, candidate_path, issue_id=approval["issue_id"])
    if (
        candidate["pdf"]["path"] != approval["pdf_path"]
        or candidate["pdf"]["sha256"] != approval["pdf_sha256"]
        or candidate["pdf"]["page_count"] != approval["page_count"]
    ):
        raise ValueError("Publication Preview approval does not bind exact candidate PDF")
    return approval


def build_visual_review(
    repo_root: Path,
    approval_path: Path,
    checks: list[dict[str, str]],
    review_tool: str,
    recorded_at: datetime,
    output_path: Path,
) -> Path:
    approval = validate_preview_approval(repo_root, approval_path)
    if not checks or any(set(row) != {"check_id", "status", "detail"} or row.get("status") != "PASS" for row in checks):
        raise ValueError("Visual Review requires one or more all-PASS checks")
    if not review_tool.strip():
        raise ValueError("Visual Review review_tool required")
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": approval["issue_id"],
        "status": "PASSED",
        "publication_preview_approval_path": _rel(repo_root, approval_path),
        "publication_preview_approval_sha256": core.sha256_file(approval_path),
        "pdf_path": approval["pdf_path"],
        "pdf_sha256": approval["pdf_sha256"],
        "page_count": approval["page_count"],
        "checks": checks,
        "review_tool": review_tool,
        "recorded_at": core.iso_utc(recorded_at),
    }
    schema_gate.validate_instance(payload, repo_root / VISUAL_REVIEW_SCHEMA, label="Visual Review record")
    _write_immutable(output_path, payload, "Visual Review record")
    return output_path


def validate_visual_review(repo_root: Path, path: Path, approval_path: Path) -> dict[str, Any]:
    review = schema_gate.load_and_validate_json(path, repo_root / VISUAL_REVIEW_SCHEMA, label="Visual Review record")
    approval = validate_preview_approval(repo_root, approval_path, issue_id=review["issue_id"])
    if review["publication_preview_approval_path"] != _rel(repo_root, approval_path) or review["publication_preview_approval_sha256"] != core.sha256_file(approval_path):
        raise ValueError("Visual Review does not bind exact Publication Preview approval")
    if review["pdf_path"] != approval["pdf_path"] or review["pdf_sha256"] != approval["pdf_sha256"] or review["page_count"] != approval["page_count"]:
        raise ValueError("Visual Review does not bind exact approved PDF")
    return review


def build_freeze(
    repo_root: Path,
    candidate_path: Path,
    approval_path: Path,
    visual_review_path: Path,
    frozen_at: datetime,
    freeze_path: Path,
    release_manifest_path: Path,
) -> tuple[Path, Path]:
    candidate = validate_candidate(repo_root, candidate_path)
    approval = validate_preview_approval(repo_root, approval_path, issue_id=candidate["issue_id"])
    review = validate_visual_review(repo_root, visual_review_path, approval_path)
    if candidate["pdf"]["sha256"] != approval["pdf_sha256"] or review["pdf_sha256"] != approval["pdf_sha256"]:
        raise ValueError("Freeze exact-PDF authority chain diverged")
    freeze = {
        "schema_version": "2.0-rc1",
        "issue_id": candidate["issue_id"],
        "status": "FROZEN",
        "publication_candidate_path": _rel(repo_root, candidate_path),
        "publication_candidate_sha256": core.sha256_file(candidate_path),
        "publication_preview_approval_path": _rel(repo_root, approval_path),
        "publication_preview_approval_sha256": core.sha256_file(approval_path),
        "visual_review_path": _rel(repo_root, visual_review_path),
        "visual_review_sha256": core.sha256_file(visual_review_path),
        "source_path": candidate["source"]["path"],
        "source_sha256": candidate["source"]["sha256"],
        "pdf_path": candidate["pdf"]["path"],
        "pdf_sha256": candidate["pdf"]["sha256"],
        "page_count": candidate["pdf"]["page_count"],
        "frozen_at": core.iso_utc(frozen_at),
    }
    schema_gate.validate_instance(freeze, repo_root / FREEZE_SCHEMA, label="Freeze record")
    _write_immutable(freeze_path, freeze, "Freeze record")
    manifest = {
        "schema_version": "2.0-rc1",
        "issue_id": candidate["issue_id"],
        "release_identity": release_identity(candidate["publication_profile"], candidate["issue_id"]),
        "status": "AUTHORIZED",
        "freeze_record_path": _rel(repo_root, freeze_path),
        "freeze_record_sha256": core.sha256_file(freeze_path),
        "source_path": freeze["source_path"],
        "source_sha256": freeze["source_sha256"],
        "pdf_path": freeze["pdf_path"],
        "pdf_sha256": freeze["pdf_sha256"],
        "page_count": freeze["page_count"],
    }
    schema_gate.validate_instance(manifest, repo_root / RELEASE_MANIFEST_SCHEMA, label="Release manifest")
    _write_immutable(release_manifest_path, manifest, "Release manifest")
    return freeze_path, release_manifest_path


def validate_release_manifest(repo_root: Path, path: Path) -> dict[str, Any]:
    manifest = schema_gate.load_and_validate_json(path, repo_root / RELEASE_MANIFEST_SCHEMA, label="Release manifest")
    freeze_path = _safe_file(repo_root, repo_root / manifest["freeze_record_path"], "Freeze record")
    if core.sha256_file(freeze_path) != manifest["freeze_record_sha256"]:
        raise ValueError("Release manifest Freeze record SHA drift")
    freeze = schema_gate.load_and_validate_json(freeze_path, repo_root / FREEZE_SCHEMA, label="Freeze record")
    for field in ("source_path", "source_sha256", "pdf_path", "pdf_sha256", "page_count"):
        if manifest[field] != freeze[field]:
            raise ValueError(f"Release manifest diverges from Freeze record: {field}")
    source = _safe_file(repo_root, repo_root / manifest["source_path"], "source_path")
    if core.sha256_file(source) != manifest["source_sha256"]:
        raise ValueError("frozen artifact bytes drift before release: source_path")
    candidate_path = _safe_file(repo_root, repo_root / freeze["publication_candidate_path"], "Publication Candidate")
    if core.sha256_file(candidate_path) != freeze["publication_candidate_sha256"]:
        raise ValueError("Freeze record Publication Candidate SHA drift")
    candidate = validate_candidate(repo_root, candidate_path, issue_id=manifest["issue_id"])
    if (
        candidate["pdf"]["path"] != manifest["pdf_path"]
        or candidate["pdf"]["sha256"] != manifest["pdf_sha256"]
        or candidate["pdf"]["page_count"] != manifest["page_count"]
    ):
        raise ValueError("Release manifest diverges from durable Publication Candidate PDF authority")
    return manifest


def build_merge_verification(
    repo_root: Path,
    manifest_path: Path,
    merged_commit_sha: str,
    verified_at: datetime,
    output_path: Path,
) -> Path:
    if len(merged_commit_sha) != 40 or any(c not in "0123456789abcdef" for c in merged_commit_sha):
        raise ValueError("merged_commit_sha must be lowercase 40-hex")
    manifest = validate_release_manifest(repo_root, manifest_path)
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": manifest["issue_id"],
        "status": "VERIFIED",
        "release_manifest_path": _rel(repo_root, manifest_path),
        "release_manifest_sha256": core.sha256_file(manifest_path),
        "merged_commit_sha": merged_commit_sha,
        "source_sha256": manifest["source_sha256"],
        "pdf_sha256": manifest["pdf_sha256"],
        "verified_at": core.iso_utc(verified_at),
    }
    schema_gate.validate_instance(payload, repo_root / MERGE_VERIFICATION_SCHEMA, label="Merge verification")
    _write_immutable(output_path, payload, "Merge verification")
    return output_path


def build_release_record(
    repo_root: Path,
    manifest_path: Path,
    merge_verification_path: Path,
    released_at: datetime,
    release_reference: str,
    output_path: Path,
) -> Path:
    manifest = validate_release_manifest(repo_root, manifest_path)
    verification = schema_gate.load_and_validate_json(
        merge_verification_path, repo_root / MERGE_VERIFICATION_SCHEMA, label="Merge verification"
    )
    if verification["issue_id"] != manifest["issue_id"]:
        raise ValueError("Merge verification issue_id mismatch")
    if verification["release_manifest_path"] != _rel(repo_root, manifest_path) or verification["release_manifest_sha256"] != core.sha256_file(manifest_path):
        raise ValueError("Merge verification does not bind exact Release manifest")
    if verification["source_sha256"] != manifest["source_sha256"] or verification["pdf_sha256"] != manifest["pdf_sha256"]:
        raise ValueError("Merge verification does not bind frozen source/PDF bytes")
    if not release_reference.strip():
        raise ValueError("release_reference required")
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": manifest["issue_id"],
        "release_identity": manifest["release_identity"],
        "status": "RELEASED",
        "release_manifest_path": _rel(repo_root, manifest_path),
        "release_manifest_sha256": core.sha256_file(manifest_path),
        "merge_verification_path": _rel(repo_root, merge_verification_path),
        "merge_verification_sha256": core.sha256_file(merge_verification_path),
        "pdf_sha256": manifest["pdf_sha256"],
        "released_at": core.iso_utc(released_at),
        "release_reference": release_reference,
    }
    schema_gate.validate_instance(payload, repo_root / RELEASE_RECORD_SCHEMA, label="Release record")
    _write_immutable(output_path, payload, "Release record")
    return output_path


def validate_release_record(repo_root: Path, path: Path) -> dict[str, Any]:
    record = schema_gate.load_and_validate_json(path, repo_root / RELEASE_RECORD_SCHEMA, label="Release record")
    manifest_path = _safe_file(repo_root, repo_root / record["release_manifest_path"], "Release manifest")
    verification_path = _safe_file(repo_root, repo_root / record["merge_verification_path"], "Merge verification")
    if core.sha256_file(manifest_path) != record["release_manifest_sha256"] or core.sha256_file(verification_path) != record["merge_verification_sha256"]:
        raise ValueError("Release record authority bytes drift")
    manifest = validate_release_manifest(repo_root, manifest_path)
    verification = schema_gate.load_and_validate_json(verification_path, repo_root / MERGE_VERIFICATION_SCHEMA, label="Merge verification")
    if record["release_identity"] != manifest["release_identity"] or record["pdf_sha256"] != manifest["pdf_sha256"] or verification["pdf_sha256"] != manifest["pdf_sha256"]:
        raise ValueError("Release record does not bind exact frozen PDF")
    return record
