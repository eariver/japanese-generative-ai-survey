#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--issue-id", required=True)
    ap.add_argument("--special-slug", required=True)
    ap.add_argument("--release-revision", required=True)
    ap.add_argument("--approved-at", required=True)
    ap.add_argument("--approval-reference", required=True)
    args = ap.parse_args()

    root = args.repo_root.resolve()
    issue = args.issue_id
    state_path = root / "sources" / issue / "pipeline-state.json"
    candidate_path = root / "sources" / issue / "freeze" / f"freeze-candidate-{args.release_revision}.json"
    state = read_json(state_path)
    candidate = read_json(candidate_path)

    assert state["lifecycle_state"] == "RELEASE_CANDIDATE", state["lifecycle_state"]
    assert state["gates"]["visual_review"] == "passed"
    assert state["gates"]["freeze"] == "pending"
    assert candidate["status"] == "PENDING_HUMAN_FREEZE_APPROVAL"
    assert candidate["proposed_release_revision"] == args.release_revision
    assert candidate["special_slug"] == args.special_slug

    source = candidate["validated_issue_source"]
    source_path = root / source["path"]
    assert source_path.is_file()
    assert sha256_file(source_path) == source["sha256"]

    vr = candidate["visual_review"]
    vr_path = root / vr["path"]
    assert vr_path.is_file()
    assert sha256_file(vr_path) == vr["sha256"]
    vr_doc = read_json(vr_path)
    assert vr_doc["status"] == "APPROVED"

    pdf = candidate["canonical_pdf_candidate"]
    state_pdf = state["provenance"]["latex_build"]
    assert pdf["sha256"] == state_pdf["pdf_sha256"]
    assert pdf["page_count"] == state_pdf["page_count"]
    assert pdf["workflow_run_id"] == state_pdf["workflow_run_id"]
    assert state["provenance"]["validated_issue_source"]["sha256"] == source["sha256"]

    approved = dt.datetime.fromisoformat(args.approved_at)
    assert approved.tzinfo is not None

    freeze_record_path = root / "sources" / issue / "freeze" / f"freeze-{args.release_revision}.json"
    release_manifest_path = root / "sources" / issue / "release-manifest.json"
    assert not freeze_record_path.exists(), freeze_record_path
    assert not release_manifest_path.exists(), release_manifest_path

    freeze_record = {
        "schema_version": "1.0",
        "issue_id": issue,
        "special_slug": args.special_slug,
        "status": "FROZEN",
        "release_revision": args.release_revision,
        "frozen_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "release_authority": "FREEZE_APPROVAL",
        "release": {
            "tag": candidate["proposed_release_tag"],
            "title": candidate["proposed_release_title"],
            "pdf_asset_name": candidate["proposed_pdf_asset_name"],
        },
        "source_version": candidate["source_version"],
        "validated_issue_source": source,
        "visual_review": vr,
        "canonical_pdf": pdf,
        "candidate": {
            "path": str(candidate_path.relative_to(root)),
            "sha256": sha256_file(candidate_path),
        },
        "scope": "Human Freeze approval is the final editorial gate and authorizes work-PR merge plus publication of the exact frozen PDF. Frozen source/PDF bytes may not change downstream.",
    }
    dump(freeze_record_path, freeze_record)

    release_manifest = {
        "schema_version": "1.0",
        "issue_id": issue,
        "special_slug": args.special_slug,
        "revision": args.release_revision,
        "status": "frozen",
        "source_version": candidate["source_version"],
        "source_manifest_path": source["path"],
        "source_manifest_sha256": source["sha256"],
        "release_tag": candidate["proposed_release_tag"],
        "release_title": candidate["proposed_release_title"],
        "asset_name": candidate["proposed_pdf_asset_name"],
        "expected_pdf_sha256": pdf["sha256"],
        "page_count": pdf["page_count"],
        "survey_root": f"surveys/special/{args.special_slug}/revisions/{candidate['source_version']}",
        "freeze_record": str(freeze_record_path.relative_to(root)),
        "pdf_source": {
            "mode": "actions-artifact",
            "workflow_run_id": pdf["workflow_run_id"],
            "artifact_id": pdf["artifact_id"],
            "artifact_name": pdf["artifact_name"],
            "artifact_digest": pdf["artifact_digest"],
        },
        "public_release_authorized": True,
        "release_authorization": {
            "mode": "FREEZE_APPROVAL",
            "authorized_at": args.approved_at,
            "approval_reference": args.approval_reference,
        },
        "notes": [
            "The exact Visual-Review-approved PDF artifact is the canonical frozen release asset.",
            "The release workflow must verify expected_pdf_sha256 before creating or publishing a GitHub Release.",
            "Human Freeze approval is the final publication authority; downstream merge/release is execution of that approval, not a new editorial gate.",
        ],
    }
    dump(release_manifest_path, release_manifest)

    state["lifecycle_state"] = "FROZEN"
    state["revision"] = args.release_revision
    state["calendar"]["frozen_at"] = args.approved_at
    state["gates"]["freeze"] = "passed"
    state["automation"]["human_gate_required_for_public_release"] = False
    state.setdefault("provenance", {})["freeze"] = {
        "path": str(freeze_record_path.relative_to(root)),
        "sha256": sha256_file(freeze_record_path),
        "release_revision": args.release_revision,
        "frozen_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "release_authority": "FREEZE_APPROVAL",
        "release_manifest_path": str(release_manifest_path.relative_to(root)),
        "release_manifest_sha256": sha256_file(release_manifest_path),
    }
    dump(state_path, state)

    out = {
        "status": "FROZEN",
        "issue_id": issue,
        "release_revision": args.release_revision,
        "freeze_record": str(freeze_record_path.relative_to(root)),
        "freeze_record_sha256": sha256_file(freeze_record_path),
        "release_manifest": str(release_manifest_path.relative_to(root)),
        "release_manifest_sha256": sha256_file(release_manifest_path),
        "source_sha256": source["sha256"],
        "pdf_sha256": pdf["sha256"],
        "page_count": pdf["page_count"],
        "work_pr_merge": "authorized-by-freeze",
        "public_release": "authorized-by-freeze",
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
