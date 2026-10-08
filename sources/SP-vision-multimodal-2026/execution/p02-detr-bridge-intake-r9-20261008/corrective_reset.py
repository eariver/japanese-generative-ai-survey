#!/usr/bin/env python3
"""Corrective single-stage reset after a worker carry-basis error in phase_b.

Situation: phase_b_screening.py selected the OLDEST 122-record screening
acceptance (43c55814, D122 KEEP) instead of the current one (b3f93319, D122
DROP), producing void acceptance 8769eab4 (D122 KEEP) and advancing to
CANDIDATES_NORMALIZED on the wrong basis.

Recovery, Core-controlled only: _revised_state (gate ARCHITECTURE_REVIEW,
boundary DISCOVERY_COLLECTED) steps state back one stage; then delete ONLY this
run's void phase_b outputs. No hand-edited state. No history rewrite beyond
Core truncation. Recorded transparently in rewind-execution-2.json.
"""
from __future__ import annotations
import datetime
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/p02-detr-bridge-intake-r9-20261008"

VOID_PATHS = [
    "sources/SP-vision-multimodal-2026/screening-package-125",  # not present; kept for record
    "sources/SP-vision-multimodal-2026/execution/p02-detr-bridge-intake-r9-20261008/screening-package-125",
    "sources/SP-vision-multimodal-2026/execution/p02-detr-bridge-intake-r9-20261008/screening-results-125",
    "sources/SP-vision-multimodal-2026/screening/v2/accepted/8769eab491f44f3529433a3ade2507ac16ac63199f9d80187f52e5e794a44303",
    "sources/SP-vision-multimodal-2026/execution/p02-detr-bridge-intake-r9-20261008/validation/screening-stage-validation-125.json",
    "sources/SP-vision-multimodal-2026/execution/p02-detr-bridge-intake-r9-20261008/validation/screening-stage-reviews-125.json",
]


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_human_gate_v2 as human_gate
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    import shutil

    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    state_path = SRC / "production-state.json"
    prior_state = core.load_json(state_path)
    assert prior_state["lifecycle_state"] == "CANDIDATES_NORMALIZED", prior_state["lifecycle_state"]
    import hashlib
    prior_sha = hashlib.sha256(state_path.read_bytes()).hexdigest()
    _, profile, source_root = human_gate._state_context(ROOT, cfg, state_path)

    updated = human_gate._revised_state(ROOT, cfg, prior_state, "ARCHITECTURE_REVIEW", "DISCOVERY_COLLECTED")
    assert updated["lifecycle_state"] == "DISCOVERY_COLLECTED"

    regen_paths, _ = human_gate._superseded_paths_for_regeneration(
        ROOT, cfg, prior_state, profile, source_root, "DISCOVERY_COLLECTED", "ARCHITECTURE_REVIEW")
    doomed = sorted({_rel(ROOT, p) for p in regen_paths})
    print("Core-computed superseded set:")
    for r in doomed:
        print(" -", r)
    assert all("gates/reviews" not in r and "approvals" not in r for r in doomed)
    assert all("/draft/" not in r and "/discovery/" not in r and "/evidence/" not in r for r in doomed)
    removed = []
    for rel in doomed:
        p = ROOT / rel
        if p.exists():
            assert p.is_file() and not p.is_symlink()
            p.unlink()
            removed.append(rel)
    for rel in VOID_PATHS:
        p = ROOT / rel
        if p.exists():
            if p.is_dir() and not p.is_symlink():
                shutil.rmtree(p)
            elif p.is_file():
                p.unlink()
            else:
                raise ValueError(f"unsafe void path: {rel}")
            removed.append(rel + " (void phase_b output)")

    core.write_json(state_path, updated)
    new_sha = hashlib.sha256(state_path.read_bytes()).hexdigest()
    errors = agent.validate_agent_state(ROOT, cfg, core.load_json(state_path))
    assert not errors, errors

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (EXECDIR / "rewind-execution-2.json").write_text(json.dumps({
        "schema_version": "1.0",
        "record_kind": "corrective-single-stage-reset",
        "issue_id": "SP-vision-multimodal-2026",
        "cause": ("phase_b carry-basis error: oldest 122-acceptance used instead of current; "
                  "void acceptance 8769eab4 carried D122 KEEP instead of DROP"),
        "core_machinery": ["survey_human_gate_v2._revised_state",
                           "survey_human_gate_v2._superseded_paths_for_regeneration",
                           "survey_production_v2.write_json",
                           "survey_agent_control_v2.validate_agent_state"],
        "human_gate_decision_functions_called": [],
        "gate_context": "ARCHITECTURE_REVIEW",
        "regeneration_boundary": "DISCOVERY_COLLECTED",
        "prior_state": {"sha256": prior_sha, "lifecycle_state": "CANDIDATES_NORMALIZED"},
        "new_state": {"sha256": new_sha, "lifecycle_state": "DISCOVERY_COLLECTED"},
        "removed_paths": removed,
        "recorded_at": now,
        "executor": "Muse Spark (Work execution role; corrective reset, not a Human/Sol decision)",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prior_lifecycle": "CANDIDATES_NORMALIZED",
                      "new_lifecycle": "DISCOVERY_COLLECTED",
                      "removed_count": len(removed), "agent_state": "CLEAN"}, indent=2))
    return 0


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


if __name__ == "__main__":
    raise SystemExit(main())
