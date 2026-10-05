#!/usr/bin/env python3
"""TS-003 Phase A (final closure): Discovery append 2 (VM-D121/VM-D122) +
acceptance rebuild (122) + advance ISSUE_INITIALIZED -> DISCOVERY_COLLECTED.

- 120 existing lines carried byte-identical; 2 appended as NORMAL root items.
- Old 120-acceptance superseded under pre-authorized re-entry; rebuilt + validated.
- Frozen Core only.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/final-closure-repair-20261005"
STATE_REL = f"{SRC}/production-state.json"
JSONL_REL = f"{SRC}/discovery/discovery-v2.jsonl"
ACC_REL = f"{SRC}/discovery/discovery-accepted-v2.json"
X_REL = f"{SRC}/external/x/x-source-intake-v2.json"
VALIDATION_REL = f"{EDIR}/validation"
NOW = "2026-10-05T00:00:00Z"


def rec(did, rawfile, obligations, reason, title, locator, summary, lane, modality, role, x_axes):
    return {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "discovery_id": did,
        "provenance": {
            "origin": "BASE",
            "research_pass": 0,
            "parent_refs": [],
            "obligation_ids": obligations,
            "reason": reason,
        },
        "source": {
            "source_type": "arxiv_primary",
            "collector_id": "muse-primary-web",
            "collector_run_id": "vision-multimodal-discovery-final-closure-20261005",
            "observed_at": NOW,
            "title": title,
            "locator": locator,
            "raw_paths": [f"{SRC}/raw/" + rawfile],
            "published_at": None,
            "summary_text": summary,
            "metadata": {
                "lane": lane,
                "modality": modality,
                "role": role,
                "x_axes": x_axes,
                "ts_overlap": "TS-001 partial / TS-002 absent",
                "retrieval_status": "ARXIV_VERIFIED",
                "evidence_boundary": "source-local claims only until Evidence verification",
                "scope_limitation": "Pre-cutoff primary; version-bind at Evidence.",
            },
        },
    }


NEW_RECORDS = [
    rec("VM-D121", "discovery-observations-final-closure-vm-d121-vjepa2.md",
        ["VM-O15"],
        "Final-closure admission for VM-O15: V-JEPA 2 / V-JEPA 2-AC (Meta, 2025-06-11) action-free pretraining plus action-conditioned latent world-model post-training and planning use; prior defer recorded as false-negative.",
        "V-JEPA 2 / V-JEPA 2-AC (Meta, 2025)", "https://arxiv.org/abs/2506.09985",
        "One two-stage contract: action-free JEPA video pretraining plus frozen-encoder action-conditioned predictor with MPC image-goal planning and VideoQA alignment.",
        "d14", "video-prediction-action", "predictive-transition", ["X02"]),
    rec("VM-D122", "discovery-observations-final-closure-vm-d122-planning-limits.md",
        ["VM-O15"],
        "Final-closure admission for VM-O15: Planning Limits paper (2026-09-30) cross-backbone planning-range evidence bounding control-oriented world-model claims; methodology/evaluation authority.",
        "The Planning Limits of Latent World Models (2026-09-30)", "https://arxiv.org/abs/2609.39235",
        "Plannable-range metric, horizon limits, scaling non-result, perfect-prediction limit, imagination/MPC/subgoal matrix, VLA ranking; sim + BridgeData offline coverage.",
        "d14", "evaluation", "evaluation-contract", ["X04"]),
]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "ISSUE_INITIALIZED":
        raise ValueError("expected canonical State at ISSUE_INITIALIZED")
    impl = core.repository_commit_sha(root)

    lines = (root / JSONL_REL).read_text(encoding="utf-8").strip().split("\n")
    have = {json.loads(l)["discovery_id"] for l in lines}
    if len(lines) == 120:
        assert not any(r["discovery_id"] in have for r in NEW_RECORDS)
        (root / JSONL_REL).write_text(
            "\n".join(lines + [json.dumps(r, ensure_ascii=False) for r in NEW_RECORDS]) + "\n",
            encoding="utf-8")
    elif len(lines) == 122:
        assert all(r["discovery_id"] in have for r in NEW_RECORDS), "unexpected 122-line state"
    else:
        raise ValueError(f"unexpected discovery line count: {len(lines)}")

    acc = root / ACC_REL
    acc.unlink(missing_ok=True)
    out = discovery.build_acceptance(root, root / JSONL_REL, root / X_REL, ISSUE_ID, acc)
    accepted = discovery.validate_acceptance(root, out)
    assert accepted["record_count"] == 122, accepted["record_count"]
    print("discovery records:", accepted["record_count"])

    with agent_tool.current_stage_basis_override():
        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "discovery-stage-validation-122.json"
        reviews_path = vdir / "discovery-stage-reviews-122.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Discovery stage-contract validation passed over canonical 122-record "
                         "acceptance (120 carried + VM-D121/VM-D122 final-closure admissions). "
                         "Machine validation only; Sol review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, reviews_path,
            ("TS-003 Discovery complete: 122 BASE root records (120 carried + V-JEPA 2/2-AC "
             "and Planning Limits final-closure admissions). Proceed to Screening."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "DISCOVERY_COLLECTED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
