#!/usr/bin/env python3
"""TS-003 Phase A (P02 bounded bridge intake): Discovery append 3
(VM-D123/VM-D124/VM-D125) + acceptance rebuild (125) + advance
ISSUE_INITIALIZED -> DISCOVERY_COLLECTED.

- 122 existing lines carried byte-identical; 3 appended as NORMAL root items
  (VM-O02, pre-cutoff primaries, non-duplicate, bounded bridge roles).
- VM-D122 NOT reused. No hand-edited counters (next IDs via normal append).
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
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
STATE_REL = f"{SRC}/production-state.json"
JSONL_REL = f"{SRC}/discovery/discovery-v2.jsonl"
ACC_REL = f"{SRC}/discovery/discovery-accepted-v2.json"
X_REL = f"{SRC}/external/x/x-source-intake-v2.json"
VALIDATION_REL = f"{EDIR}/validation"
NOW = "2026-10-08T00:00:00Z"


def rec(did, rawfile, obligations, reason, title, locator, summary):
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
            "collector_run_id": "vision-multimodal-discovery-p02-bridge-20261008",
            "observed_at": NOW,
            "title": title,
            "locator": locator,
            "raw_paths": [f"{SRC}/raw/" + rawfile],
            "published_at": None,
            "summary_text": summary,
            "metadata": {
                "lane": "d02",
                "modality": "detection",
                "role": "transition-bridge",
                "x_axes": [],
                "ts_overlap": "TS-001 absent / TS-002 absent",
                "retrieval_status": "ARXIV_VERIFIED",
                "evidence_boundary": "source-local claims only until Evidence verification",
                "scope_limitation": "Pre-cutoff primary; bounded P02 bridge role; version-bind at Evidence.",
            },
        },
    }


NEW_RECORDS = [
    rec("VM-D123", "discovery-observations-p02-vm-d123-deformable-detr.md",
        ["VM-O02"],
        "P02 bounded bridge admission for VM-O02: Deformable DETR (ICLR 2021 Oral) efficient multi-scale sparse-attention bridge (small sampling set around reference point; 10x fewer epochs; small-object repair). Detector-DINO explicitly builds on this branch.",
        "Deformable DETR: Deformable Transformers for End-to-End Object Detection (2020)",
        "https://arxiv.org/abs/2010.04159",
        "Deformable attention over a small sampling set around a reference point; multi-scale handling without FPN; 10x fewer epochs than DETR with better small-object behavior.",
        ),
    rec("VM-D124", "discovery-observations-p02-vm-d124-dab-detr.md",
        ["VM-O02"],
        "P02 bounded bridge admission for VM-O02: DAB-DETR (ICLR 2022) dynamic anchor-box query bridge (4D box-coordinate queries, layer-by-layer dynamic update, explicit positional priors). Detector-DINO explicitly formulates queries this way. Brief supporting treatment.",
        "DAB-DETR: Dynamic Anchor Boxes are Better Queries for DETR (2022)",
        "https://arxiv.org/abs/2201.12329",
        "Box coordinates as queries with layer-by-layer dynamic anchor updates; explicit positional priors; soft ROI pooling cascade reading; 45.7 AP R50-DC5 at 50 epochs.",
        ),
    rec("VM-D125", "discovery-observations-p02-vm-d125-dn-detr.md",
        ["VM-O02"],
        "P02 bounded bridge admission for VM-O02: DN-DETR (CVPR 2022 Oral) denoising-training bridge (bipartite-matching instability diagnosis; noised GT boxes/labels reconstructed; built on DAB-DETR; also applied to Deformable DETR). Detector-DINO explicitly builds on this branch.",
        "DN-DETR: Accelerate DETR Training by Introducing Query DeNoising (2022)",
        "https://arxiv.org/abs/2203.01305",
        "Query denoising training against matching instability; noised GT reconstruction; +1.9 AP over DAB-DETR; parity at ~50% epochs; plug-in generality.",
        ),
]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "ISSUE_INITIALIZED":
        raise ValueError("expected canonical State at ISSUE_INITIALIZED")
    impl = core.repository_commit_sha(root)

    lines = (root / JSONL_REL).read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 122, len(lines)
    have = {json.loads(l)["discovery_id"] for l in lines}
    assert "VM-D122" in have and not any(r["discovery_id"] in have for r in NEW_RECORDS)
    assert max(have) == "VM-D122", "canonical counter head unexpected"
    (root / JSONL_REL).write_text(
        "\n".join(lines + [json.dumps(r, ensure_ascii=False) for r in NEW_RECORDS]) + "\n",
        encoding="utf-8")

    acc = root / ACC_REL
    acc.unlink(missing_ok=True)
    out = discovery.build_acceptance(root, root / JSONL_REL, root / X_REL, ISSUE_ID, acc)
    accepted = discovery.validate_acceptance(root, out)
    assert accepted["record_count"] == 125, accepted["record_count"]
    print("discovery records:", accepted["record_count"])

    with agent_tool.current_stage_basis_override():
        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "discovery-stage-validation-125.json"
        reviews_path = vdir / "discovery-stage-reviews-125.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Discovery stage-contract validation passed over canonical 125-record "
                         "acceptance (122 carried + VM-D123/VM-D124/VM-D125 P02 bridge admissions). "
                         "Machine validation only; Sol review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, reviews_path,
            ("TS-003 Discovery complete: 125 BASE root records (122 carried + Deformable DETR, "
             "DAB-DETR, DN-DETR P02 bridge admissions). Proceed to Screening."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "DISCOVERY_COLLECTED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
