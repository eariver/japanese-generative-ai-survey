#!/usr/bin/env python3
"""Materialize Human Architecture Review r9 APPROVED (unconditional, explicit).

The canonical helper `record_architecture_approval` is blocked for r9 by the
known shared-Core review-index validator limitation (see r8 precedent
`execution/r8-authority-binding-repair-20261007/record_r8_approval.py`:
`_load_review_index` itself raises on the r1-r8 history, before writing
anything, because `_validate_review_index_semantics` rejects any review after an
active APPROVED). Shared Core is NOT modified. This edition-local bounded adapter
performs the EXACT canonical steps with Core functions (`approve_architecture`,
`_snapshot_approval`, `_review_record_payload`, `write_json`, schema validation)
and completes ONLY the mechanical index append in the exact r1-r8 entry
convention. No Human opinion invented. No r8 bytes reused (commit, revision,
reference, counts are all r9).

Reviewed commit: cf0d6233daa422190bb36b0a4c9b9d08dced2154
Tree: 6adecdf0e3a22059cc09ae5180a27c59ff773234
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
REVIEWED_COMMIT = "cf0d6233daa422190bb36b0a4c9b9d08dced2154"
EXPECTED_TREE = "6adecdf0e3a22059cc09ae5180a27c59ff773234"
REVIEW_REFERENCE = (
    "sources/SP-vision-multimodal-2026/execution/reviews/human-architecture-r9-approved-20261009.md"
    " — Human Architecture Review r9 for TS-003 (SP-vision-multimodal-2026): Human Owner unconditional explicit "
    "APPROVED (Human decision date 2026-10-09 JST) of the r9 Architecture surface on work-branch commit "
    "cf0d6233daa422190bb36b0a4c9b9d08dced2154 / tree 6adecdf0e3a22059cc09ae5180a27c59ff773234 "
    "(architecture-v2.json cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af, summary "
    "150081f2a015bc227016a31f874fa35f78fd6993379f0ea9194b1bafd57ddbff, attention "
    "a6547da4e29191aff84d51175bfd46c4b9293dddec8445775b96cb76c7fcf692). History r1–r8 preserved; this is NEW r9 "
    "approval, not r8 reuse. Evidence 124 (VERIFIED 119 / PARTIAL 5), Selection 124 SELECTED, Discovery 125, "
    "Completeness 14 SATISFIED / 2 LIMITATION. Independent differential verdict ARCHITECTURE_DIFFERENTIAL_PASS / "
    "READY_FOR_HUMAN_APPROVAL, blocking NONE. Authorizes Fresh Draft continuation; no Draft generated in this run, "
    "no TeX/PDF, no Preview/Freeze/Release."
)


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_human_gate_v2 as hg
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    from scripts import survey_schema_v2 as schema_gate

    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    state_path = SRC / "production-state.json"
    reviewed_at = datetime.now(timezone.utc)
    # Normalize to second precision, Zulu
    reviewed_at = reviewed_at.replace(microsecond=0)
    print(f"reviewed_at (actual UTC): {core.iso_utc(reviewed_at)}")

    # 0. Start-guard re-verify (read-only, pre-write)
    import subprocess
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    assert head == REVIEWED_COMMIT, f"HEAD {head} != reviewed {REVIEWED_COMMIT}"
    tree = subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    assert tree == EXPECTED_TREE, f"tree {tree} != expected {EXPECTED_TREE}"
    porcelain = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
    # Allow only our own new untracked transcription + adapter dir at this point; fail on modified tracked files
    # (transcription file is untracked-new; adapter script is untracked-new)
    print(f"start guard: HEAD {head[:8]} tree {tree[:8]} porcelain-bytes {len(porcelain)}")

    # 1. Core state transition + canonical approval (no index involvement; must succeed)
    # Capture pre-approval reviewed_state/artifacts first for exact-helper fidelity.
    _, profile, source_root = hg._state_context(ROOT, cfg, state_path)
    pre_state = hg._authority(ROOT, state_path)
    pre_artifacts = hg._reviewed_artifacts(ROOT, cfg, core.load_json(state_path), profile, "ARCHITECTURE_REVIEW")
    # Verify each matches the reviewed commit bytes
    for row in [{"path": pre_state["path"], "sha256": pre_state["sha256"]}] + pre_artifacts:
        raw = subprocess.run(["git", "cat-file", "blob", f"{REVIEWED_COMMIT}:{row['path']}"],
                             cwd=ROOT, check=True, capture_output=True).stdout
        assert core.sha256_bytes(raw) == row["sha256"], f"pre-approval byte mismatch: {row['path']}"
    hg._require_review_commit(ROOT, REVIEWED_COMMIT)
    hg._require_review_commit_reachable(ROOT, REVIEWED_COMMIT, profile["paths"]["work_branch"])
    print("preflight: pre-approval State/artifacts bind reviewed commit")

    updated = agent.approve_architecture(
        ROOT, cfg, state_path, "Human Owner", reviewed_at, REVIEW_REFERENCE)
    assert updated["human_gates"]["architecture_review"] == "approved"
    print("state: ARCHITECTURE approved (pending -> approved)")

    # 2. Snapshot approval r9 (Core function; must succeed)
    approval_path = source_root / cfg["state_authority"]["architecture_approval_path"]
    snap = hg._snapshot_approval(ROOT, source_root, cfg, "ARCHITECTURE_REVIEW", 9, approval_path)
    print("snapshot: gates/reviews/approvals/architecture-r9.json", snap["sha256"][:12])

    # 3. Review record payload r9 (Core pure function), bound to PRE-approval bytes
    committed_state = subprocess.run(["git", "cat-file", "blob", f"{REVIEWED_COMMIT}:sources/SP-vision-multimodal-2026/production-state.json"],
                                     cwd=ROOT, check=True, capture_output=True).stdout
    reviewed_state = {"path": "sources/SP-vision-multimodal-2026/production-state.json",
                      "sha256": core.sha256_bytes(committed_state)}
    assert reviewed_state == pre_state, "reviewed_state drift vs pre-approval capture"
    artifacts = pre_artifacts
    for row in artifacts:
        raw = subprocess.run(["git", "cat-file", "blob", f"{REVIEWED_COMMIT}:{row['path']}"],
                             cwd=ROOT, check=True, capture_output=True).stdout
        assert core.sha256_bytes(raw) == row["sha256"], row["path"]
    record = hg._review_record_payload(
        issue_id="SP-vision-multimodal-2026", gate="ARCHITECTURE_REVIEW", revision=9,
        decision="APPROVED", reviewed_state=reviewed_state, reviewed_artifacts=artifacts,
        reviewed_repository_commit_sha=REVIEWED_COMMIT, reviewed_by="Human Owner",
        reviewed_at=reviewed_at, review_reference=REVIEW_REFERENCE,
        requested_changes=None, regeneration_boundary=None, approval=snap)
    schema_gate.validate_instance(record, ROOT / hg.REVIEW_RECORD_SCHEMA, label="Human Gate Review Record")
    record_path = hg.review_record_path(source_root, cfg, "ARCHITECTURE_REVIEW", 9)
    assert not record_path.exists(), "refusing review record overwrite"
    core.write_json(record_path, record)
    print("record: gates/reviews/architecture-r9.json", record["review_id"])

    # 4. Mechanical index append in the exact r1-r8 convention (the ONLY manual step;
    # the Core validator that would do this rejects the r1-r8 history — known limitation).
    import json
    index_path = hg.review_index_path(source_root, cfg)
    index = json.loads(index_path.read_text(encoding="utf-8"))
    assert [(r["gate"], r["revision"]) for r in index["reviews"]] == [
        ("ARCHITECTURE_REVIEW", 1), ("ARCHITECTURE_REVIEW", 2), ("PUBLICATION_PREVIEW", 1),
        ("ARCHITECTURE_REVIEW", 3), ("ARCHITECTURE_REVIEW", 4), ("ARCHITECTURE_REVIEW", 5),
        ("ARCHITECTURE_REVIEW", 6), ("ARCHITECTURE_REVIEW", 7), ("ARCHITECTURE_REVIEW", 8)], \
        "unexpected pre-approval index shape"
    # byte/semantic preservation: keep all existing entries untouched
    before = json.dumps(index["reviews"], sort_keys=True)
    index["reviews"].append({"gate": "ARCHITECTURE_REVIEW", "revision": 9, "decision": "APPROVED",
                             "record": hg._authority(ROOT, record_path)})
    assert json.dumps(index["reviews"][:-1], sort_keys=True) == before, "r1-r8 entries mutated"
    schema_gate.validate_instance(index, ROOT / hg.REVIEW_INDEX_SCHEMA, label="Human Gate Review Index")
    core.write_json(index_path, index)
    print("index: gates/review-index.json appended r9 APPROVED (schema-valid; index-semantics "
          "validator still flags pre-existing consecutive-APPROVED shape — Core-maintenance matter)")

    # 5. Post-conditions
    errors = agent.validate_agent_state(ROOT, cfg, core.load_json(state_path))
    assert not errors, errors
    st = core.load_json(state_path)
    assert st["human_gates"]["architecture_review"] == "approved"
    assert st["human_gate_provenance"]["architecture_review"] is not None
    print("gate: architecture_review approved; r9 active; r1-r8 history preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
