#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path

from scripts.release_identity import special_release_identity

EXPECTED_AUTHORIZES = ["visual_review", "freeze", "work_pr_merge", "public_release"]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_current_release(root: Path, slug: str, issue: str, candidate: dict, release_manifest_rel: str) -> Path:
    survey_dir = root / "surveys" / "special" / slug
    path = survey_dir / "CURRENT_RELEASE.md"
    source_version = candidate["source_version"]
    source_root = f"revisions/{source_version}/"
    text = f"""# Current frozen release — {issue}

This directory contains working/history material as well as the canonical frozen source.

- Public issue identity: `{slug}`
- Public Release tag: `{candidate['release_tag']}`
- Public Release title: `{candidate['release_title']}`
- Canonical source: [`{source_root}`]({source_root})
- Canonical source manifest: [`{source_root}source-manifest.json`]({source_root}source-manifest.json)
- Internal source revision: `{source_version}` — provenance only; it is not a public Release version.
- Frozen PDF SHA-256: `{candidate['canonical_pdf_candidate']['sha256']}`
- Release manifest: `/{release_manifest_rel}`

The top-level `main.tex` is a workspace entry point and must not be treated as the source of the frozen public PDF unless it resolves to the canonical source above. The SHA-bound release manifest is authoritative.
"""
    path.write_text(text, encoding="utf-8")

    top_main = survey_dir / "main.tex"
    if top_main.is_file():
        existing = top_main.read_text(encoding="utf-8")
        marker = "% WORKSPACE ENTRY POINT — NOT THE CANONICAL FROZEN RELEASE SOURCE. See CURRENT_RELEASE.md.\n"
        if not existing.startswith(marker):
            top_main.write_text(marker + existing, encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Finalize an issue-only Special Freeze under an existing Publication Preview approval."
    )
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--issue-id", required=True)
    ap.add_argument("--special-slug", required=True)
    ap.add_argument("--approved-at", required=True)
    ap.add_argument("--approval-reference", required=True)
    args = ap.parse_args()

    root = args.repo_root.resolve()
    issue = args.issue_id
    state_path = root / "sources" / issue / "pipeline-state.json"
    candidate_path = root / "sources" / issue / "freeze" / "freeze-candidate.json"
    state = read_json(state_path)
    candidate = read_json(candidate_path)
    identity = special_release_identity(args.special_slug)

    assert state["lifecycle_state"] == "RELEASE_CANDIDATE", state["lifecycle_state"]
    assert state["gates"]["visual_review"] == "passed"
    assert state["gates"]["freeze"] == "pending"
    assert candidate["status"] == "READY_FOR_DETERMINISTIC_FREEZE"
    assert candidate["special_slug"] == args.special_slug
    assert candidate["release_identity_mode"] == "ISSUE_ONLY"
    for key, value in identity.items():
        assert candidate[key] == value, (key, candidate[key], value)

    authority = candidate.get("publication_authority") or {}
    assert authority.get("mode") == "PUBLICATION_PREVIEW_APPROVAL"
    assert authority.get("approved_at") == args.approved_at
    assert authority.get("approval_reference") == args.approval_reference
    assert authority.get("authorizes") == EXPECTED_AUTHORIZES
    approval_path = root / authority["approval_path"]
    assert approval_path.is_file()
    assert sha256_file(approval_path) == authority["approval_sha256"]
    approval = read_json(approval_path)
    assert approval["status"] == "APPROVED"
    assert approval["approval_mode"] == "PUBLICATION_PREVIEW_APPROVAL"
    assert approval["approved_at"] == args.approved_at
    assert approval["approval_reference"] == args.approval_reference
    assert approval["authorizes"] == EXPECTED_AUTHORIZES

    source = candidate["validated_issue_source"]
    source_path = root / source["path"]
    assert source_path.is_file()
    assert sha256_file(source_path) == source["sha256"]

    vr = candidate["visual_review"]
    vr_path = root / vr["path"]
    assert vr_path == approval_path
    assert hashlib.sha256(vr_path.read_bytes()).hexdigest() == vr["sha256"]

    pdf = candidate["canonical_pdf_candidate"]
    state_pdf = state["provenance"]["latex_build"]
    assert pdf["sha256"] == state_pdf["pdf_sha256"]
    assert pdf["page_count"] == state_pdf["page_count"]
    assert pdf["workflow_run_id"] == state_pdf["workflow_run_id"]
    assert state["provenance"]["validated_issue_source"]["sha256"] == source["sha256"]

    approved = dt.datetime.fromisoformat(args.approved_at)
    assert approved.tzinfo is not None

    freeze_record_path = root / "sources" / issue / "freeze" / "freeze.json"
    release_manifest_path = root / "sources" / issue / "release-manifest.json"
    assert not freeze_record_path.exists(), freeze_record_path
    assert not release_manifest_path.exists(), release_manifest_path

    freeze_record = {
        "schema_version": "1.0",
        "issue_id": issue,
        "special_slug": args.special_slug,
        "status": "FROZEN",
        "release_identity_mode": "ISSUE_ONLY",
        "frozen_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "release_authority": "PUBLICATION_PREVIEW_APPROVAL",
        "release": {
            "tag": candidate["release_tag"],
            "title": candidate["release_title"],
            "pdf_asset_name": candidate["asset_name"],
        },
        "source_version": candidate["source_version"],
        "validated_issue_source": source,
        "publication_preview": {
            "path": str(approval_path.relative_to(root)),
            "sha256": sha256_file(approval_path),
            "approved_at": args.approved_at,
            "approval_reference": args.approval_reference,
        },
        "visual_review": vr,
        "canonical_pdf": pdf,
        "candidate": {
            "path": str(candidate_path.relative_to(root)),
            "sha256": sha256_file(candidate_path),
        },
        "scope": "Publication Preview approval fixes the exact reviewed PDF bytes and authorizes deterministic Freeze, normal work-PR merge, and publication. Public identity is the issue number only; internal source_version remains provenance.",
    }
    dump(freeze_record_path, freeze_record)

    release_manifest = {
        "schema_version": "1.0",
        "issue_id": issue,
        "special_slug": args.special_slug,
        "release_identity_mode": "ISSUE_ONLY",
        "status": "frozen",
        "source_version": candidate["source_version"],
        "source_manifest_path": source["path"],
        "source_manifest_sha256": source["sha256"],
        "release_tag": candidate["release_tag"],
        "release_title": candidate["release_title"],
        "asset_name": candidate["asset_name"],
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
            "mode": "PUBLICATION_PREVIEW_APPROVAL",
            "authorized_at": args.approved_at,
            "approval_reference": args.approval_reference,
            "approval_path": str(approval_path.relative_to(root)),
            "approval_sha256": sha256_file(approval_path),
        },
        "notes": [
            "The issue number is the sole public release identity; no public semantic version is assigned.",
            "Internal source_version is retained only for deterministic provenance and source-history reconstruction.",
            "The exact Publication-Preview-approved PDF artifact is the canonical frozen release asset.",
            "Freeze, merge, and public Release are deterministic consequences of the recorded Publication Preview approval.",
            "The publisher must reverify source and PDF SHA-256 before creating the GitHub Release.",
        ],
    }
    dump(release_manifest_path, release_manifest)

    current_release_path = write_current_release(
        root,
        args.special_slug,
        issue,
        candidate,
        str(release_manifest_path.relative_to(root)),
    )

    state["lifecycle_state"] = "FROZEN"
    state["calendar"]["frozen_at"] = args.approved_at
    state["gates"]["freeze"] = "passed"
    state["automation"]["human_gate_required_for_public_release"] = False
    state.setdefault("provenance", {})["freeze"] = {
        "path": str(freeze_record_path.relative_to(root)),
        "sha256": sha256_file(freeze_record_path),
        "frozen_at": args.approved_at,
        "approval_reference": args.approval_reference,
        "release_authority": "PUBLICATION_PREVIEW_APPROVAL",
        "release_identity_mode": "ISSUE_ONLY",
        "release_tag": identity["release_tag"],
        "release_manifest_path": str(release_manifest_path.relative_to(root)),
        "release_manifest_sha256": sha256_file(release_manifest_path),
        "current_release_path": str(current_release_path.relative_to(root)),
        "current_release_sha256": sha256_file(current_release_path),
    }
    dump(state_path, state)

    print(json.dumps({
        "status": "FROZEN",
        "issue_id": issue,
        "release_identity_mode": "ISSUE_ONLY",
        "release_tag": identity["release_tag"],
        "release_authority": "PUBLICATION_PREVIEW_APPROVAL",
        "freeze_record": str(freeze_record_path.relative_to(root)),
        "freeze_record_sha256": sha256_file(freeze_record_path),
        "release_manifest": str(release_manifest_path.relative_to(root)),
        "release_manifest_sha256": sha256_file(release_manifest_path),
        "current_release": str(current_release_path.relative_to(root)),
        "source_sha256": source["sha256"],
        "pdf_sha256": pdf["sha256"],
        "page_count": pdf["page_count"],
        "work_pr_merge": "authorized-by-publication-preview",
        "public_release": "authorized-by-publication-preview",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
