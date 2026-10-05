#!/usr/bin/env python3
"""Second bounded rewind (§2 pre-authorized): ARCHITECTURE_ESTABLISHED -> SELECTION_COMPLETE.

Reason: P09 code-bucket line must include Qwen3-Omni (§11); arch edit requires
checkpoint rebuild + re-advance from SELECTION_COMPLETE. Core machinery only.
"""
from __future__ import annotations
import datetime
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/late-cutoff-expansion-20261005"

PROTECTED_SUFFIXES = [
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r4.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r1.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r2.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/architecture-r3.json",
    "sources/SP-vision-multimodal-2026/gates/reviews/publication-r1.json",
    "sources/SP-vision-multimodal-2026/gates/review-index.json",
    "sources/SP-vision-multimodal-2026/architecture-v3.json",
    "sources/SP-vision-multimodal-2026/architecture-v4.json",
    "sources/SP-vision-multimodal-2026/discovery/discovery-v2.jsonl",
    "sources/SP-vision-multimodal-2026/discovery/discovery-accepted-v2.json",
    "sources/SP-vision-multimodal-2026/candidate-matrix-v2.json",
    "sources/SP-vision-multimodal-2026/candidate-selection-v2.json",
    "sources/SP-vision-multimodal-2026/materiality-ledger-v2.json",
    "sources/SP-vision-multimodal-2026/profile-completeness-v2.json",
]


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_human_gate_v2 as human_gate
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core

    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    state_path = SRC / "production-state.json"
    prior_state = core.load_json(state_path)
    assert prior_state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED", prior_state["lifecycle_state"]
    assert prior_state["human_gates"]["architecture_review"] == "pending"
    import hashlib
    prior_sha = hashlib.sha256(state_path.read_bytes()).hexdigest()
    _, profile, source_root = human_gate._state_context(ROOT, cfg, state_path)

    updated = human_gate._revised_state(ROOT, cfg, prior_state, "ARCHITECTURE_REVIEW", "SELECTION_COMPLETE")
    assert updated["lifecycle_state"] == "SELECTION_COMPLETE"
    regen_paths, _ = human_gate._superseded_paths_for_regeneration(
        ROOT, cfg, prior_state, profile, source_root, "SELECTION_COMPLETE", "ARCHITECTURE_REVIEW")
    gate_paths = human_gate._superseded_gate_authority_paths(
        ROOT, cfg, prior_state, source_root, "ARCHITECTURE_REVIEW", "SELECTION_COMPLETE")
    doomed = sorted({_rel(ROOT, p) for p in [*regen_paths, *gate_paths]})
    for prot in PROTECTED_SUFFIXES:
        assert prot not in doomed, f"Core set touches protected path: {prot}"
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
    (EXECDIR / "rewind-execution-2.json").write_text(json.dumps({
        "schema_version": "1.0", "record_kind": "section2-preauthorized-execution-2",
        "issue_id": "SP-vision-multimodal-2026",
        "reason": "P09 code-bucket Qwen3-Omni inclusion (§11); arch edit needs checkpoint rebuild",
        "regeneration_boundary": "SELECTION_COMPLETE",
        "prior_state_sha256": prior_sha, "new_state_sha256": new_sha,
        "removed_paths": removed, "recorded_at": now,
        "executor": "Muse Spark (Work execution role; not a Human/Sol decision)",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"new_lifecycle": "SELECTION_COMPLETE",
                      "removed_count": len(removed), "agent_state": "CLEAN"}, indent=2))
    for r in removed:
        print(" -", r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
