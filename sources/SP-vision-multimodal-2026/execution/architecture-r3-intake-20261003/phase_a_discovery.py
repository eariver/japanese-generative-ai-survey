#!/usr/bin/env python3
"""TS-003 Phase A (r3 re-entry): canonical Discovery 112 as ROOT collection +
advance ISSUE_INITIALIZED -> DISCOVERY_COLLECTED.

- VM-D112 materialized as a NORMAL canonical root Discovery item (origin BASE,
  research_pass 0, parent_refs []), appropriate to ISSUE_INITIALIZED-stage
  collection. The staged GAP_FILL/research_pass=1 form is NOT reused (it belongs
  to the invalid derived-expansion representation).
- 111 existing lines carried byte-identical; VM-D112 appended.
- Old 111-acceptance superseded under Human-gated re-entry (bytes in history);
  rebuilt + validated via canonical builders (112 records).
- Advance via stage_validation + build_stage_checkpoint + advance_with_checkpoint.
- Frozen Core only + documented post-gate adaptation (override + current HEAD).
  Sol review owed on all judgments (screening decisions carried; VM-D112 KEEP
  per genuine formal evaluation recorded in the turn record).
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
EDIR = f"{SRC}/execution/architecture-r3-intake-20261003"
STATE_REL = f"{SRC}/production-state.json"
JSONL_REL = f"{SRC}/discovery/discovery-v2.jsonl"
ACC_REL = f"{SRC}/discovery/discovery-accepted-v2.json"
X_REL = f"{SRC}/external/x/x-source-intake-v2.json"
VALIDATION_REL = f"{EDIR}/validation"
NOW = "2026-10-03T12:30:00Z"

VM_D112 = {
    "schema_version": "2.0-rc1",
    "issue_id": ISSUE_ID,
    "discovery_id": "VM-D112",
    "provenance": {
        "origin": "BASE",
        "research_pass": 0,
        "parent_refs": [],
        "obligation_ids": ["VM-O10", "VM-O12"],
        "reason": ("Formal canonical collection for VM-O10/VM-O12: official "
                   "2026-09-01 Google release of query-driven on-demand timeline "
                   "navigation (token-acquisition transition + third video-processing "
                   "contract); bounded to this candidate only."),
    },
    "source": {
        "source_type": "first_party_release_or_docs",
        "collector_id": "muse-primary-web",
        "collector_run_id": "vision-multimodal-discovery-r3-formal",
        "observed_at": NOW,
        "title": "Agentic video understanding in Gemini (Google, 2026-09-01)",
        "locator": ("https://blog.google/innovation-and-ai/models-and-research/"
                    "gemini-models/introducing-agentic-video-in-gemini/"),
        "raw_paths": [f"{SRC}/raw/discovery-observations-currency-supplement-agentic-video.md"],
        "published_at": "2026-09",
        "summary_text": ("Official 2026-09-01 release: agentic loop over video timelines "
                         "(transcript/frame/audio on demand, adaptive FPS/resolution, "
                         "prompt-driven); up to 88% fewer tokens (long-form) / 66% lower "
                         "cost (benchmarks) / ~7% higher quality (vendor ceilings); "
                         "3.7/3.6/3.5-Lite launch, 3.8 in docs by 09-16; TTFT caveat "
                         "<5 min; thinking/tool token accounting; NOT streaming."),
        "metadata": {
            "lane": "d09",
            "modality": "video",
            "role": "processing-contract-transition",
            "x_axes": ["X03"],
            "ts_overlap": "TS-001 partial / TS-002 absent",
            "retrieval_status": "BLOG_VERIFIED",
            "evidence_boundary": "source-local claims only until Evidence verification",
            "scope_limitation": ("Vendor-reported ceilings; benchmark-row binding deferred "
                                 "to Evidence; implementation may change after cutoff."),
        },
    },
}


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "ISSUE_INITIALIZED":
        raise ValueError("expected canonical State at ISSUE_INITIALIZED")
    impl = core.repository_commit_sha(root)

    lines = (root / JSONL_REL).read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 111, len(lines)
    assert all(json.loads(l)["discovery_id"] != "VM-D112" for l in lines)
    (root / JSONL_REL).write_text(
        "\n".join(lines + [json.dumps(VM_D112, ensure_ascii=False)]) + "\n",
        encoding="utf-8")

    acc = root / ACC_REL
    acc.unlink()  # superseded 111-record stage output under Human-gated re-entry
    out = discovery.build_acceptance(root, root / JSONL_REL, root / X_REL, ISSUE_ID, acc)
    accepted = discovery.validate_acceptance(root, out)
    assert accepted["record_count"] == 112, accepted["record_count"]
    print("discovery records:", accepted["record_count"])

    with agent_tool.current_stage_basis_override():
        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "discovery-stage-validation-112.json"
        reviews_path = vdir / "discovery-stage-reviews-112.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Discovery stage-contract validation passed over canonical "
                         "112-record acceptance (111 carried BASE + VM-D112 BASE root "
                         "collection). Machine validation only; Sol Discovery "
                         "completeness review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, reviews_path,
            ("TS-003 Discovery (re-)collection complete: 112 BASE root records "
             "(VM-D001-VM-D111 carried + VM-D112 Agentic Video Understanding as normal "
             "root item). Proceed to Screening; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "DISCOVERY_COLLECTED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
