#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

from scripts.release_identity import special_release_identity

PUBLICATION_PREVIEW_AUTHORIZES = ["visual_review", "freeze", "work_pr_merge", "public_release"]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Record an approved Special Publication Preview and create a deterministic Freeze candidate."
    )
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--approved-pdf", required=True)
    parser.add_argument("--approved-pdf-sha256", required=True)
    parser.add_argument("--approval-reference", required=True)
    parser.add_argument("--approved-at", required=True)
    parser.add_argument("--artifact-name", required=True)
    parser.add_argument("--artifact-id", required=True, type=int)
    parser.add_argument("--artifact-digest", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    state_path = root / "sources" / args.issue_id / "pipeline-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise SystemExit(f"expected RELEASE_CANDIDATE, got {state.get('lifecycle_state')!r}")
    if gates.get("latex_build") != "passed" or gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise SystemExit("Publication Preview acceptance requires latex_build=passed and visual_review/freeze=pending")

    automation = state.get("automation") or {}
    model = automation.get("human_gate_model")
    if model is not None and model != "ARCHITECTURE_PUBLICATION_PREVIEW_WITH_EXCEPTION":
        raise SystemExit(f"unsupported Human Gate model for Publication Preview: {model!r}")

    latex = (state.get("provenance") or {}).get("latex_build") or {}
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    if latex.get("pdf_sha256") != args.approved_pdf_sha256:
        raise SystemExit("approved PDF SHA does not match pipeline state")
    approved_pdf = Path(args.approved_pdf)
    actual_pdf_sha = sha256_file(approved_pdf)
    if actual_pdf_sha != args.approved_pdf_sha256:
        raise SystemExit("downloaded PDF SHA does not match the approved SHA")
    source_path = root / source["path"]
    if sha256_file(source_path) != source.get("sha256"):
        raise SystemExit("validated source manifest SHA mismatch")
    if source.get("source_version") != latex.get("source_version"):
        raise SystemExit("validated source and PDF build source versions differ")

    approved_at = datetime.fromisoformat(args.approved_at)
    if approved_at.tzinfo is None:
        raise SystemExit("approved_at must include timezone")

    identity = special_release_identity(args.special_slug)
    source_version = source["source_version"]
    visual_dir = root / "sources" / args.issue_id / "visual-review" / source_version
    approval_path = visual_dir / "approval.json"
    candidate_path = root / "sources" / args.issue_id / "freeze" / "freeze-candidate.json"
    if approval_path.exists() or candidate_path.exists():
        raise SystemExit("Publication Preview approval or versionless Freeze candidate already exists")

    approval = {
        "schema_version": "1.0",
        "issue_id": args.issue_id,
        "special_slug": args.special_slug,
        "status": "APPROVED",
        "approval_mode": "PUBLICATION_PREVIEW_APPROVAL",
        "approved_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "authorizes": list(PUBLICATION_PREVIEW_AUTHORIZES),
        "source_version": source_version,
        "validated_issue_source": {"path": source["path"], "sha256": source["sha256"]},
        "pdf": {
            "sha256": actual_pdf_sha,
            "page_count": latex.get("page_count"),
            "workflow_run_id": latex.get("workflow_run_id"),
            "artifact_name": args.artifact_name,
            "artifact_id": args.artifact_id,
            "artifact_digest": args.artifact_digest,
        },
        "scope": "Human Publication Preview approval for these exact PDF bytes. It records Visual Review and authorizes deterministic Freeze, work-PR merge, and public Release without a second normal Human Gate.",
    }
    write_json(approval_path, approval)
    approval_sha = sha256_file(approval_path)

    candidate = {
        "schema_version": "1.0",
        "issue_id": args.issue_id,
        "special_slug": args.special_slug,
        "status": "READY_FOR_DETERMINISTIC_FREEZE",
        **identity,
        "source_version": source_version,
        "validated_issue_source": {"path": source["path"], "sha256": source["sha256"]},
        "publication_authority": {
            "mode": "PUBLICATION_PREVIEW_APPROVAL",
            "approval_path": str(approval_path.relative_to(root)),
            "approval_sha256": approval_sha,
            "approved_at": args.approved_at,
            "approval_reference": args.approval_reference,
            "authorizes": list(PUBLICATION_PREVIEW_AUTHORIZES),
        },
        "visual_review": {
            "path": str(approval_path.relative_to(root)),
            "sha256": approval_sha,
            "approved_at": args.approved_at,
        },
        "canonical_pdf_candidate": {
            "sha256": actual_pdf_sha,
            "page_count": latex.get("page_count"),
            "workflow_run_id": latex.get("workflow_run_id"),
            "artifact_name": args.artifact_name,
            "artifact_id": args.artifact_id,
            "artifact_digest": args.artifact_digest,
        },
        "machine_checkpoints": {
            "visual_review": "passed",
            "freeze": "pending",
        },
        "note": "Public identity is issue-only. Internal source_version is provenance, not a Release version. Freeze is deterministic under the recorded Publication Preview authority.",
    }
    write_json(candidate_path, candidate)
    candidate_sha = sha256_file(candidate_path)

    gates["visual_review"] = "passed"
    gates["freeze"] = "pending"
    state["gates"] = gates
    provenance = state.setdefault("provenance", {})
    provenance["publication_preview"] = {
        "path": str(approval_path.relative_to(root)),
        "sha256": approval_sha,
        "approved_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "source_version": source_version,
        "pdf_sha256": actual_pdf_sha,
        "authorizes": list(PUBLICATION_PREVIEW_AUTHORIZES),
    }
    provenance["visual_review"] = {
        "path": str(approval_path.relative_to(root)),
        "sha256": approval_sha,
        "approved_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "source_version": source_version,
        "pdf_sha256": actual_pdf_sha,
        "authority": "PUBLICATION_PREVIEW_APPROVAL",
    }
    provenance["freeze_candidate"] = {
        "path": str(candidate_path.relative_to(root)),
        "sha256": candidate_sha,
        "status": "READY_FOR_DETERMINISTIC_FREEZE",
        "release_identity_mode": "ISSUE_ONLY",
        "release_tag": identity["release_tag"],
        "authority": "PUBLICATION_PREVIEW_APPROVAL",
    }
    write_json(state_path, state)

    print(json.dumps({
        "schema_version": "1.0",
        "issue_id": args.issue_id,
        "source_version": source_version,
        "publication_preview": "approved",
        "visual_review": "passed",
        "freeze": "ready-for-deterministic-finalization",
        "release_identity_mode": "ISSUE_ONLY",
        "release_tag": identity["release_tag"],
        "freeze_candidate_path": str(candidate_path.relative_to(root)),
        "freeze_candidate_sha256": candidate_sha,
        "pdf_sha256": actual_pdf_sha,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
