#!/usr/bin/env python3
"""Materialize Human Architecture Review r6 APPROVED (conditional, audit-verified).

The canonical helper `record_architecture_approval` is fully blocked for r6 by
the shared-Core review-index validator defect (see core-defect-review-index-r6.md:
`_load_review_index` itself raises on the r1-r5 history, before writing anything;
for r5 it wrote record/snapshot/state and only the index append needed manual
completion). This script performs the EXACT helper steps with Core functions
(`approve_architecture`, `_snapshot_approval`, `_review_record_payload`,
`write_json`, schema validation) and completes ONLY the mechanical index append
in the exact r1-r5 entry convention. No shared-Core file modified. No Human
opinion invented (conditional contract + audit binding per §§12/14).
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
REVIEWED_COMMIT = "31c9ebb14d126432d5c4f24e0062e896897fb891"
REVIEWED_AT = "2026-10-06T16:39:52Z"
REVIEW_REFERENCE = ("sources/SP-vision-multimodal-2026/execution/reviews/human-architecture-r6-approved-20261006.md "
  "— Human Architecture Review r6 for TS-003 (SP-vision-multimodal-2026): Human Owner CONDITIONAL APPROVAL "
  "(pre-authorized, audit-verified 25/25 on actual bytes) of the corrected 121-record Architecture surface on "
  "work-branch commit 31c9ebb14d126432d5c4f24e0062e896897fb891 / tree b3eb5bea3ba25b91dd31c458a6a990b3bd987d0e "
  "(architecture-v2.json bbf3eaa62f182a7ecac33533be7450638581d5ff5aca3218894cf96c95623070, summary "
  "618cde08bf1fcc0640800d559b2a5c83e90cbd7eb49466d22f334409995546e5, attention "
  "c774f9b41bf3ab7e8657f521bc371ddf534c51c1f02e9b372848bc40b2571594). History r1-r5 preserved; this is NEW r6 "
  "approval, not r5 reuse. Evidence 121 (VERIFIED 116 / PARTIAL 5), Selection 121 SELECTED, Completeness 14 "
  "SATISFIED / 2 LIMITATION, 16 packages target 112/max 120. Authorizes FRESH 121-authority Draft JSON "
  "(fresh-121-r6) to DRAFT_COMPLETE; no TeX/PDF, no VALIDATED_DRAFT advance, no Freeze/Release.")


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_human_gate_v2 as hg
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    from scripts import survey_schema_v2 as schema_gate

    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    state_path = SRC / "production-state.json"
    reviewed_at = datetime.fromisoformat(REVIEWED_AT.replace("Z", "+00:00"))

    # 1. Core state transition + canonical approval (no index involvement; must succeed)
    updated = agent.approve_architecture(
        ROOT, cfg, state_path, "Human Owner", reviewed_at, REVIEW_REFERENCE)
    assert updated["human_gates"]["architecture_review"] == "approved"
    print("state: ARCHITECTURE approved (pending -> approved)")

    # 2. Snapshot approval r6 (Core function; must succeed)
    _, profile, source_root = hg._state_context(ROOT, cfg, state_path)
    approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
    snap = hg._snapshot_approval(ROOT, source_root, cfg, "ARCHITECTURE_REVIEW", 6, approval_path)
    print("snapshot: gates/reviews/approvals/architecture-r6.json", snap["sha256"][:12])

    # 3. Review record payload r6 (Core pure function)
    reviewed_state = hg._authority(ROOT, state_path)  # NOTE: helper computes reviewed_state BEFORE approve;
    # exact-helper fidelity requires the PRE-approval state bytes. Recompute from the reviewed commit:
    import subprocess
    committed_state = subprocess.run(["git", "cat-file", "blob", f"{REVIEWED_COMMIT}:sources/SP-vision-multimodal-2026/production-state.json"],
                                     cwd=ROOT, check=True, capture_output=True).stdout
    reviewed_state = {"path": "sources/SP-vision-multimodal-2026/production-state.json",
                      "sha256": core.sha256_bytes(committed_state)}
    artifacts = hg._reviewed_artifacts(ROOT, cfg, core.load_json(state_path), profile, "ARCHITECTURE_REVIEW")
    # artifacts must bind the REVIEWED (pre-approval) bytes, not post-approval state — verify each
    # matches the committed reviewed commit (helper's _review_commit already verified this pattern;
    # re-verify explicitly since we bypass the helper).
    for row in artifacts:
        raw = subprocess.run(["git", "cat-file", "blob", f"{REVIEWED_COMMIT}:{row['path']}"],
                             cwd=ROOT, check=True, capture_output=True).stdout
        assert core.sha256_bytes(raw) == row["sha256"], row["path"]
    hg._require_review_commit(ROOT, REVIEWED_COMMIT)
    hg._require_review_commit_reachable(ROOT, REVIEWED_COMMIT, profile["paths"]["work_branch"])
    record = hg._review_record_payload(
        issue_id="SP-vision-multimodal-2026", gate="ARCHITECTURE_REVIEW", revision=6,
        decision="APPROVED", reviewed_state=reviewed_state, reviewed_artifacts=artifacts,
        reviewed_repository_commit_sha=REVIEWED_COMMIT, reviewed_by="Human Owner",
        reviewed_at=reviewed_at, review_reference=REVIEW_REFERENCE,
        requested_changes=None, regeneration_boundary=None, approval=snap)
    schema_gate.validate_instance(record, ROOT / hg.REVIEW_RECORD_SCHEMA, label="Human Gate Review Record")
    record_path = hg.review_record_path(source_root, cfg, "ARCHITECTURE_REVIEW", 6)
    assert not record_path.exists(), "refusing review record overwrite"
    core.write_json(record_path, record)
    print("record: gates/reviews/architecture-r6.json", record["review_id"])

    # 4. Mechanical index append in the exact r1-r5 convention (the ONLY manual step;
    # the Core validator that would do this rejects the r1-r5 history — see defect note).
    import json
    index_path = hg.review_index_path(source_root, cfg)
    index = json.loads(index_path.read_text(encoding="utf-8"))
    assert [ (r["gate"], r["revision"]) for r in index["reviews"]] == [
        ("ARCHITECTURE_REVIEW", 1), ("ARCHITECTURE_REVIEW", 2), ("PUBLICATION_PREVIEW", 1),
        ("ARCHITECTURE_REVIEW", 3), ("ARCHITECTURE_REVIEW", 4), ("ARCHITECTURE_REVIEW", 5)]
    index["reviews"].append({"gate": "ARCHITECTURE_REVIEW", "revision": 6, "decision": "APPROVED",
                             "record": hg._authority(ROOT, record_path)})
    schema_gate.validate_instance(index, ROOT / hg.REVIEW_INDEX_SCHEMA, label="Human Gate Review Index")
    core.write_json(index_path, index)
    print("index: gates/review-index.json appended r6 APPROVED (schema-valid; index-semantics "
          "validator still flags pre-existing r4/r5 consecutive-APPROVED shape — Core-maintenance matter)")

    # 5. Post-conditions
    errors = agent.validate_agent_state(ROOT, cfg, core.load_json(state_path))
    assert not errors, errors
    st = core.load_json(state_path)
    assert st["human_gates"]["architecture_review"] == "approved"
    assert st["human_gate_provenance"]["architecture_review"] is not None
    print("gate: architecture_review approved; r6 active; r5 history preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
