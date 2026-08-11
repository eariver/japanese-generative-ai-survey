#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Accept a human Visual Review for a Special issue and materialize a Freeze candidate without freezing it.")
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
    parser.add_argument("--proposed-release-revision", default="v0.1")
    args = parser.parse_args()

    root = Path(args.repo_root)
    state_path = root / "sources" / args.issue_id / "pipeline-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))

    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise SystemExit(f"expected RELEASE_CANDIDATE, got {state.get('lifecycle_state')!r}")
    gates = state.get("gates") or {}
    if gates.get("latex_build") != "passed":
        raise SystemExit("latex_build must be passed before Visual Review acceptance")
    if gates.get("visual_review") != "pending":
        raise SystemExit(f"visual_review must be pending, got {gates.get('visual_review')!r}")
    if gates.get("freeze") != "pending":
        raise SystemExit("freeze must still be pending")

    latex = (state.get("provenance") or {}).get("latex_build") or {}
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    expected_pdf_sha = latex.get("pdf_sha256")
    if expected_pdf_sha != args.approved_pdf_sha256:
        raise SystemExit(f"approved PDF SHA does not match state: {args.approved_pdf_sha256} != {expected_pdf_sha}")
    approved_pdf = Path(args.approved_pdf)
    actual_pdf_sha = sha256_file(approved_pdf)
    if actual_pdf_sha != args.approved_pdf_sha256:
        raise SystemExit(f"downloaded PDF SHA mismatch: {actual_pdf_sha} != {args.approved_pdf_sha256}")

    source_path = root / source["path"]
    actual_source_sha = sha256_file(source_path)
    if actual_source_sha != source.get("sha256"):
        raise SystemExit(f"validated source manifest SHA mismatch: {actual_source_sha} != {source.get('sha256')}")
    if source.get("source_version") != latex.get("source_version"):
        raise SystemExit("validated source version and PDF build source version differ")

    # Ensure timestamp is parseable and carries an explicit timezone.
    approved_at = datetime.fromisoformat(args.approved_at)
    if approved_at.tzinfo is None:
        raise SystemExit("approved_at must include a timezone offset")

    source_version = source["source_version"]
    visual_dir = root / "sources" / args.issue_id / "visual-review" / source_version
    approval_path = visual_dir / "approval.json"
    freeze_dir = root / "sources" / args.issue_id / "freeze"
    freeze_candidate_path = freeze_dir / f"freeze-candidate-{args.proposed_release_revision}.json"

    if approval_path.exists() or freeze_candidate_path.exists():
        raise SystemExit("Visual Review approval or Freeze candidate already exists; refusing overwrite")

    approval = {
        "schema_version": "1.0",
        "issue_id": args.issue_id,
        "special_slug": args.special_slug,
        "status": "APPROVED",
        "approved_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "source_version": source_version,
        "validated_issue_source": {
            "path": source["path"],
            "sha256": source["sha256"],
        },
        "pdf": {
            "sha256": actual_pdf_sha,
            "page_count": latex.get("page_count"),
            "workflow_run_id": latex.get("workflow_run_id"),
            "artifact_name": args.artifact_name,
            "artifact_id": args.artifact_id,
            "artifact_digest": args.artifact_digest,
        },
        "scope": "Human Visual Review approval only. This record does not approve Freeze, work-PR merge, or public Release.",
    }
    write_json(approval_path, approval)
    approval_sha = sha256_file(approval_path)

    release_revision = args.proposed_release_revision
    release_tag = f"special/{args.special_slug}/{release_revision}"
    release_asset = f"Japanese_Generative_AI_Technical_Survey_Special_{args.special_slug}_{release_revision}.pdf"
    freeze_candidate = {
        "schema_version": "1.0",
        "issue_id": args.issue_id,
        "special_slug": args.special_slug,
        "status": "PENDING_HUMAN_FREEZE_APPROVAL",
        "proposed_release_revision": release_revision,
        "proposed_release_tag": release_tag,
        "proposed_release_title": f"Japanese Generative AI Technical Survey Special — {args.special_slug} {release_revision}",
        "proposed_pdf_asset_name": release_asset,
        "source_version": source_version,
        "validated_issue_source": {
            "path": source["path"],
            "sha256": source["sha256"],
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
        "human_gates": {
            "visual_review": "passed",
            "freeze": "pending",
            "work_pr_merge": "pending",
            "public_release": "pending",
        },
        "note": "Candidate only. Freeze must not occur until a separate explicit human Freeze approval is recorded.",
    }
    write_json(freeze_candidate_path, freeze_candidate)
    freeze_candidate_sha = sha256_file(freeze_candidate_path)

    gates["visual_review"] = "passed"
    gates["freeze"] = "pending"
    state["gates"] = gates
    provenance = state.setdefault("provenance", {})
    provenance["visual_review"] = {
        "path": str(approval_path.relative_to(root)),
        "sha256": approval_sha,
        "approved_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "source_version": source_version,
        "pdf_sha256": actual_pdf_sha,
    }
    provenance["freeze_candidate"] = {
        "path": str(freeze_candidate_path.relative_to(root)),
        "sha256": freeze_candidate_sha,
        "status": "PENDING_HUMAN_FREEZE_APPROVAL",
        "proposed_release_revision": release_revision,
    }
    write_json(state_path, state)

    audit = {
        "schema_version": "1.0",
        "issue_id": args.issue_id,
        "source_version": source_version,
        "visual_review": "passed",
        "freeze": "pending",
        "approval_path": str(approval_path.relative_to(root)),
        "approval_sha256": approval_sha,
        "freeze_candidate_path": str(freeze_candidate_path.relative_to(root)),
        "freeze_candidate_sha256": freeze_candidate_sha,
        "pdf_sha256": actual_pdf_sha,
        "page_count": latex.get("page_count"),
    }
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
