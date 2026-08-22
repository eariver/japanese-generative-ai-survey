#!/usr/bin/env python3
"""Profile-aware exact-byte quality authority for Survey Production Core v2.

Quality review has three kinds:
- DETERMINISTIC: crisp machine-checkable invariant with a result artifact;
- AGENT_SEMANTIC: ChatGPT semantic/editorial review with reasoned evidence;
- AGENT_VISUAL: ChatGPT rendered-PDF review with reasoned evidence.

The bundle itself binds one exact source/PDF pair, so agent judgments are still
revision-specific without pretending that qualitative judgment is a validator.
"""
from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

QUALITY_SCHEMA = Path("schemas/quality-regression-bundle-v2.schema.json")
VALID_KINDS = {"DETERMINISTIC", "AGENT_SEMANTIC", "AGENT_VISUAL"}


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


def bind_pdf_authority(repo_root: Path, materialized_pdf_path: Path, durable_authority: dict[str, Any] | None = None) -> dict[str, Any]:
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


def expected_checks(cfg: dict[str, Any], research_profile: str, publication_profile: str) -> dict[str, str]:
    quality = cfg.get("quality_review")
    if not isinstance(quality, dict):
        raise ValueError("quality_review contract missing")
    rows: list[dict[str, Any]] = []
    rows.extend(quality.get("core", []))
    research = quality.get("research_profiles", {}).get(research_profile)
    publication = quality.get("publication_profiles", {}).get(publication_profile)
    if not isinstance(research, list):
        raise ValueError(f"quality_review missing research Profile: {research_profile}")
    if not isinstance(publication, list):
        raise ValueError(f"quality_review missing publication Profile: {publication_profile}")
    rows.extend(research)
    rows.extend(publication)
    result: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"check_id", "kind"}:
            raise ValueError("quality_review check contract rows must be check_id/kind")
        check_id = row.get("check_id")
        kind = row.get("kind")
        if not isinstance(check_id, str) or not check_id or check_id in result:
            raise ValueError(f"quality_review check IDs must be unique/non-empty: {check_id}")
        if kind not in VALID_KINDS:
            raise ValueError(f"quality_review kind invalid for {check_id}: {kind}")
        result[check_id] = kind
    return result


def _validate_result_ref(repo_root: Path, row: dict[str, Any]) -> None:
    result = row.get("result")
    if row["kind"] == "DETERMINISTIC":
        if not isinstance(result, dict) or set(result) != {"path", "sha256"}:
            raise ValueError(f"deterministic quality check requires result authority: {row['check_id']}")
        path = core.repo_local_path(repo_root, result["path"], f"quality result {row['check_id']}")
        if not path.is_file() or core.sha256_file(path) != result.get("sha256"):
            raise ValueError(f"deterministic quality result drift: {row['check_id']}")
    elif result is not None:
        raise ValueError(f"agent quality check must not claim deterministic result authority: {row['check_id']}")


def validate_checks(repo_root: Path, cfg: dict[str, Any], research_profile: str, publication_profile: str, checks: list[dict[str, Any]]) -> None:
    expected = expected_checks(cfg, research_profile, publication_profile)
    ids: list[str] = []
    for row in checks:
        required_fields = {"check_id", "kind", "status", "executor", "evidence", "recorded_at", "result"}
        if not isinstance(row, dict) or set(row) != required_fields:
            raise ValueError("quality check fields do not match agent-first contract")
        check_id = row.get("check_id")
        if not isinstance(check_id, str) or not check_id:
            raise ValueError("quality check_id must be non-empty")
        if check_id not in expected:
            raise ValueError(f"quality check is not applicable to this Profile combination: {check_id}")
        if row.get("kind") != expected[check_id]:
            raise ValueError(f"quality check kind differs from Profile contract: {check_id}")
        if row.get("status") != "PASS":
            raise ValueError(f"quality check did not pass: {check_id}")
        if not isinstance(row.get("executor"), str) or not row["executor"].strip():
            raise ValueError(f"quality check executor required: {check_id}")
        if not isinstance(row.get("evidence"), str) or not row["evidence"].strip():
            raise ValueError(f"quality check evidence required: {check_id}")
        try:
            core.parse_instant(str(row.get("recorded_at", "")))
        except ValueError as exc:
            raise ValueError(f"quality check recorded_at invalid: {check_id}") from exc
        _validate_result_ref(repo_root, row)
        ids.append(check_id)
    if len(ids) != len(set(ids)):
        raise ValueError("quality check IDs must be unique")
    missing = sorted(set(expected) - set(ids))
    if missing:
        raise ValueError("applicable quality review family incomplete: " + ", ".join(missing))


def _infer_profiles(issue_id: str) -> tuple[str, str]:
    if core.WEEKLY_ISSUE_RE.fullmatch(issue_id):
        return "WEEKLY", "WEEKLY_MAGAZINE"
    return "THEMATIC", "LONGFORM_SPECIAL"


def build_bundle(
    repo_root: Path,
    issue_id: str,
    source_path: Path,
    pdf_path: Path,
    checks: list[dict[str, Any]],
    output_path: Path,
    pdf_authority: dict[str, Any] | None = None,
    *,
    research_profile: str | None = None,
    publication_profile: str | None = None,
) -> Path:
    source = _safe_file(repo_root, source_path, "validated publication source")
    pdf = _safe_file(repo_root, pdf_path, "publication PDF")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    inferred_research, inferred_publication = _infer_profiles(issue_id)
    research = research_profile or inferred_research
    publication = publication_profile or inferred_publication
    validate_checks(repo_root, cfg, research, publication, checks)
    basis = {
        "schema_version": "2.0-rc1",
        "issue_id": issue_id,
        "research_profile": research,
        "publication_profile": publication,
        "source": {"path": _rel(repo_root, source), "sha256": core.sha256_file(source)},
        "pdf": bind_pdf_authority(repo_root, pdf, pdf_authority),
        "checks": sorted(checks, key=lambda row: row["check_id"]),
        "status": "PASS",
    }
    payload = dict(basis)
    payload["bundle_sha256"] = core.sha256_object(basis)
    schema_gate.validate_instance(payload, repo_root / QUALITY_SCHEMA, label="quality review bundle")
    if output_path.exists():
        raise ValueError(f"refusing to overwrite quality review bundle: {output_path}")
    core.write_json(output_path, payload)
    return output_path


def validate_bundle(repo_root: Path, path: Path, *, issue_id: str | None = None) -> dict[str, Any]:
    payload = schema_gate.load_and_validate_json(path, repo_root / QUALITY_SCHEMA, label="quality review bundle")
    if issue_id is not None and payload["issue_id"] != issue_id:
        raise ValueError("quality review bundle issue_id mismatch")
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    validate_checks(repo_root, cfg, payload["research_profile"], payload["publication_profile"], payload["checks"])
    basis = {key: payload[key] for key in (
        "schema_version", "issue_id", "research_profile", "publication_profile", "source", "pdf", "checks", "status"
    )}
    if payload["bundle_sha256"] != core.sha256_object(basis):
        raise ValueError("quality review bundle content digest mismatch")
    source_ref = payload["source"]
    source = _safe_file(repo_root, repo_root / source_ref["path"], "quality source")
    if core.sha256_file(source) != source_ref["sha256"]:
        raise ValueError("quality review source bytes drifted after validation")
    pdf_ref = payload["pdf"]
    if pdf_ref["storage"] == "REPOSITORY_FILE":
        pdf = _safe_file(repo_root, repo_root / pdf_ref["path"], "quality pdf")
        if core.sha256_file(pdf) != pdf_ref["sha256"] or pdf.stat().st_size != pdf_ref["byte_count"]:
            raise ValueError("quality review pdf bytes drifted after validation")
    else:
        _safe_artifact_member(pdf_ref["path"])
    return payload
