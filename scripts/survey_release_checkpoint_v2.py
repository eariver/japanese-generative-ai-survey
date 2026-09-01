#!/usr/bin/env python3
"""Adopt the external FROZEN -> RELEASED boundary with one compact checkpoint.

The public Release workflow performs the irreversible/external work and exact-byte
reconciliation. This helper records that result using the same agent-first Stage
Checkpoint format as local stages, without recreating Action/Handoff ceremony.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_schema_v2 as schema_gate


def build_release_checkpoint(
    repo_root: Path,
    cfg: dict,
    state_path: Path,
    merge_verification: Path,
    release_record: Path,
    recorded_at: datetime,
) -> Path:
    state = core.load_json(state_path)
    agent.verify_agent_state_basis(repo_root, cfg, state)
    if state.get("lifecycle_state") != "FROZEN":
        raise ValueError("release checkpoint requires FROZEN Production State")
    stage = cfg["orchestration"]["stage_plan"].get("FROZEN")
    if not isinstance(stage, dict) or stage.get("action_kind") != "WORKFLOW_DISPATCH" or stage.get("next_state") != "RELEASED":
        raise ValueError("FROZEN release stage contract is not canonical")
    release = publication.validate_release_record(repo_root, release_record)
    if release.get("issue_id") != state.get("issue_id"):
        raise ValueError("Release Record issue_id mismatch")
    verification_ref = release.get("merge_verification_path")
    if verification_ref != str(merge_verification.resolve().relative_to(repo_root.resolve())):
        raise ValueError("Release Record does not bind supplied Merge Verification path")
    if core.sha256_file(merge_verification) != release.get("merge_verification_sha256"):
        raise ValueError("Release Record does not bind supplied Merge Verification bytes")
    _, profile, _ = agent._profile_and_source(repo_root, cfg, state)
    artifacts = [
        agent._named_authority(repo_root, "merge-verification", merge_verification),
        agent._named_authority(repo_root, "release-record", release_record),
    ]
    agent._validate_stage_artifacts(repo_root, cfg, state, profile, artifacts)
    impl = core.repository_commit_sha(repo_root)
    result_authority = agent._authority(repo_root, release_record, "Release Record")
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": state["issue_id"],
        "from_state": "FROZEN",
        "to_state": "RELEASED",
        "checkpoints": ["release"],
        "recorded_at": core.iso_utc(recorded_at),
        "implementation": {
            "repository_commit_sha": impl,
            "orchestrator_version": cfg["orchestrator_version"],
        },
        "contract": core.contract_identity(repo_root, cfg, state["research_profile"], state["publication_profile"]),
        "artifacts": artifacts,
        "reviews": [
            {
                "check_id": "RELEASE_EXACT_BYTE_RECONCILIATION",
                "kind": "DETERMINISTIC",
                "status": "PASS",
                "executor": "survey-production-v2-release.yml",
                "evidence": "Public issue-only Release identity, target and downloaded asset bytes were reconciled against the frozen Release Manifest before adoption.",
                "result": result_authority,
            }
        ],
        "summary": "Exact frozen publication bytes were released or reconciled idempotently and the immutable Release Record was validated.",
    }
    schema_gate.validate_instance(payload, repo_root / agent.CHECKPOINT_SCHEMA, label="Release Stage Checkpoint")
    path = agent.canonical_checkpoint_path(repo_root, cfg, state)
    if path.exists():
        if core.load_json(path) != payload:
            raise ValueError("refusing divergent Release Stage Checkpoint overwrite")
    else:
        core.write_json(path, payload)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(core.DEFAULT_CONFIG))
    parser.add_argument("--state", required=True)
    parser.add_argument("--merge-verification", required=True)
    parser.add_argument("--release-record", required=True)
    parser.add_argument("--recorded-at")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    def path(value: str) -> Path:
        p = Path(value)
        return p.resolve() if p.is_absolute() else (root / p).resolve()
    try:
        cfg = core.load_json(path(args.config))
        when = core.parse_instant(args.recorded_at) if args.recorded_at else datetime.now(timezone.utc)
        checkpoint = build_release_checkpoint(root, cfg, path(args.state), path(args.merge_verification), path(args.release_record), when)
        state = agent.advance_with_checkpoint(root, cfg, path(args.state), checkpoint)
        print(json.dumps({"checkpoint": str(checkpoint.relative_to(root)), "state": state}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
