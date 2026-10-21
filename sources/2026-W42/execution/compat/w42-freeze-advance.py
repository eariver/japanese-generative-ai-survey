#!/usr/bin/env python3
"""W42 edition-local Freeze checkpoint + advance (NO CORE PATCH, NO MANUAL STATE).

Runs AFTER w42-freeze-compat-driver.py validation PASS, in the same Human-
authorized bounded compat: installs the identical in-process admission shim,
writes the CORE_STAGE_CONTRACT-anchored reviews file, then calls the unchanged
frozen Core `agent.build_stage_checkpoint` and `agent.advance_with_checkpoint`,
and finally `agent.validate_agent_state`. Any failure aborts with no mutation.

Evidence label: EDITION_LOCAL_RUNTIME_COMPAT (disclosed, not an operator-bridge PASS).
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    repo_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    sys.path.insert(0, str(repo_root))

    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location(
        "w42_freeze_compat_driver",
        repo_root / "sources/2026-W42/execution/compat/w42-freeze-compat-driver.py")
    driver = _ilu.module_from_spec(_spec)
    assert _spec.loader is not None
    _spec.loader.exec_module(driver)
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core

    scope = driver._install_compat(repo_root)
    print("compat scope: " + scope["adapted"])

    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state_path = repo_root / "sources/2026-W42/production-state.json"
    state = core.load_json(state_path)
    assert state["lifecycle_state"] == "RELEASE_CANDIDATE", state["lifecycle_state"]

    supplied = {
        "freeze-record": repo_root / "sources/2026-W42/publication/v2/freeze-record-v2.json",
        "release-manifest": repo_root / "sources/2026-W42/publication/v2/release-manifest-v2.json",
        "visual-review-record": repo_root / "sources/2026-W42/publication/v2/visual-review-v2.json",
        "publication-candidate": repo_root / "sources/2026-W42/publication/v2/publication-candidate-v2.json",
    }
    # Re-assert candidate pinned identity (same as validation phase).
    vd = json.loads((repo_root / "sources/2026-W42/orchestration/v2/checkpoints/VALIDATED_DRAFT.json").read_text())
    pinned = [r for r in vd.get("artifacts", []) if r.get("name") == "publication-candidate"]
    assert len(pinned) == 1
    assert core.sha256_file(supplied["publication-candidate"]) == pinned[0]["sha256"], "candidate drift"

    recorded_at = datetime.now(timezone.utc)
    reviews = {"reviews": [
        {"check_id": "CORE_STAGE_CONTRACT",
         "kind": "DETERMINISTIC",
         "executor": "survey_stage_validation_v2 (frozen Core, W42 edition-local runtime compat admission)",
         "evidence": "Canonical Core stage contract validated for W42 Freeze; see validation file.",
         "result_path": "sources/2026-W42/execution/validation/freeze-validation-r34.json"},
        {"check_id": "W42_R34_FREEZE_EXACT_PDF",
         "kind": "AGENT_VISUAL",
         "executor": "Muse (W42 r34 compat freeze execution)",
         "evidence": "Freeze binds exact approved PDF 827a93d8 (505694B, 21pp) via approved candidate + preview approval r3 + candidate-bound visual review."},
        {"check_id": "W42_R34_COMPAT_SCOPE",
         "kind": "AGENT_EDITORIAL",
         "executor": "Muse (W42 r34 compat freeze execution)",
         "evidence": "In-process admission only for approval-vs-checkpoint typing and the two contract-required extras; all frozen validators/checkpoint/advance unmodified. Run 39455215003 remains the failed trusted attempt."},
    ]}
    reviews_path = repo_root / "sources/2026-W42/execution/compat/w42-freeze-stage-reviews.json"
    reviews_path.write_text(json.dumps(reviews, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("reviews written:", reviews_path.relative_to(repo_root))

    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo_root,
                          capture_output=True, text=True, check=True).stdout.strip()
    cp = agent.build_stage_checkpoint(
        repo_root, cfg, state_path,
        {k: v for k, v in supplied.items()},
        reviews_path,
        "W42 r34 Freeze: exact approved 21-page PDF bound via candidate + preview approval r3; edition-local runtime compat admission disclosed.",
        recorded_at, head)
    print("checkpoint built:", cp.relative_to(repo_root))
    updated = agent.advance_with_checkpoint(repo_root, cfg, state_path, cp)
    print("advanced to:", updated["lifecycle_state"], "| terminal:", updated.get("terminal_reason"))
    errors = agent.validate_agent_state(repo_root, cfg, core.load_json(state_path))
    assert not errors, errors
    print("state valid; lifecycle:", core.load_json(state_path)["lifecycle_state"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
