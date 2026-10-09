#!/usr/bin/env python3
"""Execute the Human-authorized Owner Exception rewind r7 (Core-controlled only).

DRAFT_COMPLETE -> CANDIDATES_NORMALIZED via ONLY Core functions. Creates NO
Human-gate decision record. r1-r6 review/approval snapshots preserved as history.
"""
from __future__ import annotations
import datetime
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/r7-targeted-authority-repair-20261007"
BOUNDARY = "CANDIDATES_NORMALIZED"
GATE_CTX = "PUBLICATION_PREVIEW"  # cross-gate revision context (r6 APPROVED active)

PROTECTED_SUFFIXES = [
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r6.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r5.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r4.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r3.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r2.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r1.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/publication-r1.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/approvals/architecture-r6.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/approvals/architecture-r5.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/approvals/architecture-r4.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/approvals/architecture-r2.json",
    "sources/SP-vision-multimodal-2026/gates/review-index.json",
    "sources/SP-vision-multimodal-2026/discovery/discovery-v2.jsonl",
    "sources/SP-vision-multimodal-2026/discovery/discovery-accepted-v2.json",
]


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_human_gate_v2 as human_gate
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core

    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    state_path = SRC / "production-state.json"
    prior_state = core.load_json(state_path)
    assert prior_state["lifecycle_state"] == "DRAFT_COMPLETE", prior_state["lifecycle_state"]
    assert prior_state["human_gates"]["architecture_review"] == "approved"
    import hashlib
    prior_sha = hashlib.sha256(state_path.read_bytes()).hexdigest()
    _, profile, source_root = human_gate._state_context(ROOT, cfg, state_path)

    updated = human_gate._revised_state(ROOT, cfg, prior_state, GATE_CTX, BOUNDARY)
    assert updated["lifecycle_state"] == "CANDIDATES_NORMALIZED"
    assert updated["human_gates"]["architecture_review"] == "pending"
    assert updated["human_gate_provenance"]["architecture_review"] is None

    regen_paths, canonical = human_gate._superseded_paths_for_regeneration(
        ROOT, cfg, prior_state, profile, source_root, BOUNDARY, GATE_CTX)
    gate_paths = human_gate._superseded_gate_authority_paths(
        ROOT, cfg, prior_state, source_root, GATE_CTX, BOUNDARY)
    doomed = sorted({_rel(ROOT, p) for p in [*regen_paths, *gate_paths]})
    print("Core-computed superseded set:")
    for r in doomed:
        print(" -", r)
    for prot in PROTECTED_SUFFIXES:
        assert prot not in doomed, f"Core set touches protected path: {prot}"
    assert not any(p.startswith("sources/SP-vision-multimodal-2026/gates/reviews/") for p in doomed), doomed
    assert not any("approvals" in p for p in doomed), doomed
    assert not any("/draft/" in p for p in doomed), doomed
    assert not any(p.startswith("sources/SP-vision-multimodal-2026/evidence/") for p in doomed), doomed
    assert not any("/discovery/" in p or "/screening/" in p for p in doomed), doomed
    assert not any("/publication/" in p or "main.pdf" in p or "main.tex" in p for p in doomed), doomed

    removed = []
    for rel in doomed:
        p = ROOT / rel
        if p.exists():
            assert p.is_file() and not p.is_symlink()
            p.unlink()
            removed.append(rel)

    core.write_json(state_path, updated)
    new_sha = hashlib.sha256(state_path.read_bytes()).hexdigest()
    errors = agent.validate_agent_state(ROOT, cfg, core.load_json(state_path))
    assert not errors, errors

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    record = {
        "schema_version": "1.0",
        "record_kind": "owner-exception-execution",
        "issue_id": "SP-vision-multimodal-2026",
        "authorization": {"path": "sources/SP-vision-multimodal-2026/execution/r7-targeted-authority-repair-20261007/owner-exception-authorization.md"},
        "core_machinery": ["survey_human_gate_v2._revised_state",
                           "survey_human_gate_v2._superseded_paths_for_regeneration",
                           "survey_human_gate_v2._superseded_gate_authority_paths",
                           "survey_production_v2.write_json",
                           "survey_agent_control_v2.validate_agent_state"],
        "human_gate_decision_functions_called": [],
        "gate_context": GATE_CTX,
        "regeneration_boundary": BOUNDARY,
        "prior_state": {"path": "sources/SP-vision-multimodal-2026/production-state.json", "sha256": prior_sha,
                        "lifecycle_state": "DRAFT_COMPLETE"},
        "new_state": {"path": "sources/SP-vision-multimodal-2026/production-state.json", "sha256": new_sha,
                      "lifecycle_state": "CANDIDATES_NORMALIZED"},
        "removed_paths": removed,
        "protected_paths_verified_intact": PROTECTED_SUFFIXES,
        "recorded_at": now,
        "executor": "Muse Spark (Work execution role under explicit Owner Exception; not a Human/Sol decision)",
    }
    (EXECDIR / "owner-exception-execution.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prior_lifecycle": "DRAFT_COMPLETE", "new_lifecycle": "CANDIDATES_NORMALIZED",
                      "removed_count": len(removed), "agent_state": "CLEAN"}, indent=2))
    return 0


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


if __name__ == "__main__":
    raise SystemExit(main())
