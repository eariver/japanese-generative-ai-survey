#!/usr/bin/env python3
"""Coupled quality regression authority for final Survey Production Core v2 bytes."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

QUALITY_SCHEMA = Path("schemas/quality-regression-bundle-v2.schema.json")
REQUIRED_CHECKS = {
    "SUBJECT_ENTITY_PROPERTY_BINDING",
    "IDENTIFIER_PRESERVATION",
    "SOURCE_SPECIFIC_FAIL_CLOSED_NOTES",
    "BIBLIOGRAPHY_METADATA",
    "CHRONOLOGY_SOURCE_MAPPING",
    "EMPTY_WRAPPER_SUPPRESSION",
    "TOC_HIERARCHY",
    "TECHNICAL_NOTES_TAIL_NEEDSPACE",
    "REQUIRED_SYNTHESIS_SURVIVAL",
    "POST_TRANSFORM_SEMANTIC_REVALIDATION",
    "PDF_PREFLIGHT",
}


def _rel(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root))
    except ValueError as exc:
        raise ValueError(f"quality artifact must be repository-local: {path}") from exc


def _safe_file(repo_root: Path, path: Path, label: str) -> Path:
    _rel(repo_root, path)
    if path.resolve().is_symlink() or not path.resolve().is_file():
        raise ValueError(f"{label} missing or unsafe: {path}")
    return path.resolve()


def _safe_artifact_member(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Actions artifact PDF member path must be non-empty")
    member = PurePosixPath(value)
    if member.is_absolute() or ".." in member.parts or "." in member.parts:
        raise ValueError("Actions artifact PDF member path must be normalized and relative")
    return member.as_posix()


def _repository_pdf_authority(repo_root: Path, pdf: Path) -> dict[str, Any]:
    return {
        "storage": "REPOSITORY_FILE",
        "path": _rel(repo_root, pdf),
        "sha256": core.sha256_file(pdf),
        "byte_count": pdf.stat().st_size,
        "actions_artifact": None,
    }


def bind_pdf_authority(
    repo_root: Path,
    materialized_pdf_path: Path,
    durable_authority: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Bind inspected PDF bytes to either repository or durable Actions authority.

    `materialized_pdf_path` is the exact local file inspected by quality checks.
    For Actions-backed production it is intentionally ephemeral; the returned
    authority contains only durable workflow/artifact identity plus exact content
    digest/size and the member path used for deterministic rehydration.
    """
    pdf = _safe_file(repo_root, materialized_pdf_path, "publication PDF")
    if durable_authority is None:
        return _repository_pdf_authority(repo_root, pdf)
    if not isinstance(durable_authority, dict):
        raise ValueError("durable PDF authority must be an object")
    expected = {"storage", "path", "sha256", "byte_count", "actions_artifact"}
    if set(durable_authority) != expected:
        raise ValueError("durable PDF authority fields are invalid")
    authority = dict(durable_authority)
    if authority.get("storage") != "GITHUB_ACTIONS_ARTIFACT":
        raise ValueError("explicit durable PDF authority currently supports GITHUB_ACTIONS_ARTIFACT only")
    authority["path"] = _safe_artifact_member(authority.get("path"))
    if authority.get("sha256") != core.sha256_file(pdf):
        raise ValueError("durable PDF authority SHA does not match materialized quality bytes")
    if authority.get("byte_count") != pdf.stat().st_size:
        raise ValueError("durable PDF authority byte_count does not match materialized quality bytes")
    return authority


def validate_checks(checks: list[dict[str, Any]]) -> None:
    ids: list[str] = []
    for row in checks:
        if not isinstance(row, dict) or set(row) != {"check_id", "status", "evidence"}:
            raise ValueError("quality check fields must be check_id/status/evidence")
        check_id = row.get("check_id")
        if not isinstance(check_id, str) or not check_id:
            raise ValueError("quality check_id must be non-empty")
        if row.get("status") != "PASS":
            raise ValueError(f"quality check did not pass: {check_id}")
        if not isinstance(row.get("evidence"), str) or not row["evidence"].strip():
            raise ValueError(f"quality check evidence required: {check_id}")
        ids.append(check_id)
    if len(ids) != len(set(ids)):
        raise ValueError("quality check IDs must be unique")
    missing = sorted(REQUIRED_CHECKS - set(ids))
    if missing:
        raise ValueError("coupled quality regression family incomplete: " + ", ".join(missing))


def build_bundle(
    repo_root: Path,
    issue_id: str,
    source_path: Path,
    pdf_path: Path,
    checks: list[dict[str, Any]],
    output_path: Path,
    pdf_authority: dict[str, Any] | None = None,
) -> Path:
    source = _safe_file(repo_root, source_path, "validated publication source")
    pdf = _safe_file(repo_root, pdf_path, "publication PDF")
    validate_checks(checks)
    basis = {
        "schema_version": "2.0-rc1",
        "issue_id": issue_id,
        "source": {"path": _rel(repo_root, source), "sha256": core.sha256_file(source)},
        "pdf": bind_pdf_authority(repo_root, pdf, pdf_authority),
        "checks": sorted(checks, key=lambda row: row["check_id"]),
        "status": "PASS",
    }
    payload = dict(basis)
    payload["bundle_sha256"] = core.sha256_object(basis)
    schema_gate.validate_instance(payload, repo_root / QUALITY_SCHEMA, label="quality regression bundle")
    if output_path.exists():
        raise ValueError(f"refusing to overwrite quality regression bundle: {output_path}")
    core.write_json(output_path, payload)
    return output_path


def validate_bundle(repo_root: Path, path: Path, *, issue_id: str | None = None) -> dict[str, Any]:
    payload = schema_gate.load_and_validate_json(path, repo_root / QUALITY_SCHEMA, label="quality regression bundle")
    if issue_id is not None and payload["issue_id"] != issue_id:
        raise ValueError("quality regression bundle issue_id mismatch")
    validate_checks(payload["checks"])
    basis = {key: payload[key] for key in ("schema_version", "issue_id", "source", "pdf", "checks", "status")}
    if payload["bundle_sha256"] != core.sha256_object(basis):
        raise ValueError("quality regression bundle content digest mismatch")
    source_ref = payload["source"]
    source = _safe_file(repo_root, repo_root / source_ref["path"], "quality source")
    if core.sha256_file(source) != source_ref["sha256"]:
        raise ValueError("quality regression source bytes drifted after validation")
    pdf_ref = payload["pdf"]
    if pdf_ref["storage"] == "REPOSITORY_FILE":
        pdf = _safe_file(repo_root, repo_root / pdf_ref["path"], "quality pdf")
        if core.sha256_file(pdf) != pdf_ref["sha256"] or pdf.stat().st_size != pdf_ref["byte_count"]:
            raise ValueError("quality regression pdf bytes drifted after validation")
    else:
        _safe_artifact_member(pdf_ref["path"])
    return payload
