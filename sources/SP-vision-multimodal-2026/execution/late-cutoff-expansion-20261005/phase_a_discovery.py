#!/usr/bin/env python3
"""TS-003 Phase A (late-cutoff expansion): Discovery append 8 (VM-D113..VM-D120) +
acceptance rebuild (120) + advance ISSUE_INITIALIZED -> DISCOVERY_COLLECTED.

- 112 existing lines carried byte-identical; 8 appended as NORMAL root items
  (origin BASE, research_pass 0) per the VM-D112 formal-intake precedent.
- Old 112-acceptance superseded under §2-pre-authorized re-entry; rebuilt + validated.
- Advance via stage_validation + build_stage_checkpoint + advance_with_checkpoint.
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
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
JSONL_REL = f"{SRC}/discovery/discovery-v2.jsonl"
ACC_REL = f"{SRC}/discovery/discovery-accepted-v2.json"
X_REL = f"{SRC}/external/x/x-source-intake-v2.json"
VALIDATION_REL = f"{EDIR}/validation"
NOW = "2026-10-05T00:00:00Z"


def rec(did, rawfile, obligations, reason, title, locator, summary, lane, modality, role, x_axes,
        retrieval="ARXIV_VERIFIED", ts_overlap="TS-001 partial / TS-002 absent",
        scope_limitation="Pre-cutoff primary; version-bind at Evidence."):
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
            "collector_run_id": "vision-multimodal-discovery-late-cutoff-20261005",
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
                "ts_overlap": ts_overlap,
                "retrieval_status": retrieval,
                "evidence_boundary": "source-local claims only until Evidence verification",
                "scope_limitation": scope_limitation,
            },
        },
    }


NEW_RECORDS = [
    rec("VM-D113", "discovery-observations-late-cutoff-vm-d113-dinov3.md", ["VM-O06"],
        "Late-cutoff formal collection for VM-O06: DINOv3 (Meta, 2025-08-13) scalable SSL with Gram-anchored dense refinement; frozen reusable dense representation.",
        "DINOv3 (Meta AI, 2025)", "https://arxiv.org/abs/2508.10104",
        "7B SSL on LVD-1689M; dense degradation under long training fixed by Gram anchoring; post-hoc resolution/distillation/text-alignment adaptation; frozen dense SOTA.",
        "d06", "image", "foundation-transition", ["X01"]),
    rec("VM-D114", "discovery-observations-late-cutoff-vm-d114-siglip2.md", ["VM-O06", "VM-O07"],
        "Late-cutoff formal collection for VM-O06/VM-O07: SigLIP 2 (Zhai et al., 2025-02-20) staged multilingual encoder recipe (sigmoid + captioning + self-distillation + masked prediction + data curation).",
        "SigLIP 2 (Zhai et al., 2025)", "https://arxiv.org/abs/2502.14786",
        "SigLIP objective inheritance plus caption decoder, self-distillation, masked prediction, online curation; multilingual/debiased mixture; native aspect/multi-resolution; localization and dense gains; VLM encoder transfer.",
        "d06", "image-text", "foundation-transition", ["X01", "X02"]),
    rec("VM-D115", "discovery-observations-late-cutoff-vm-d115-sam3.md", ["VM-O03", "VM-O08"],
        "Late-cutoff formal collection for VM-O03/VM-O08: SAM 3 (Meta, 2025-11-19) promptable concept segmentation (detect/segment/track by noun phrase or exemplar).",
        "SAM 3: Segment Anything with Concepts (Meta, 2025)", "https://arxiv.org/abs/2511.16719",
        "Text-NP/image-exemplar/visual prompts; image detector; memory video tracker; shared backbone; recognition/localization decoupling; SAM/SAM2 inheritance plus language-grounded concept interface. No SAM 3D; SAM 3.1 successor-context only.",
        "d03", "image-video-text", "grounding-transition", ["X02"]),
    rec("VM-D116", "discovery-observations-late-cutoff-vm-d116-pi-zero.md", ["VM-O14"],
        "Late-cutoff formal collection for VM-O14: pi-zero (Physical Intelligence, 2024-10-31) flow-matching VLA (continuous action expert on PaliGemma VLM).",
        "pi-zero: A Vision-Language-Action Flow Model (Physical Intelligence, 2024)", "https://arxiv.org/abs/2410.24164",
        "Pretrained PaliGemma VLM plus flow-matching action expert; multi-robot dexterous data regime; continuous 50Hz action chunks; discrete-token vs flow-matching interface transition vs RT-2/OpenVLA. No robotics-control survey expansion.",
        "d13", "vision-language-action", "action-interface-transition", ["X02"]),
    rec("VM-D117", "discovery-observations-late-cutoff-vm-d117-fast.md", ["VM-O14"],
        "Late-cutoff formal collection for VM-O14: FAST (Pertsch et al., 2025-01-16) DCT/frequency-space action tokenization (representation transition, not a general VLA system).",
        "FAST: Efficient Action Tokenization for VLA Models (Pertsch et al., 2025)", "https://arxiv.org/abs/2501.09747",
        "Per-dim/per-timestep binning failure mode; DCT frequency representation; chunk compression; FAST+ universal tokenizer; pi-zero/OpenVLA relationship; AR vs flow trade-off. Kept separate from pi-zero.",
        "d13", "action-representation", "action-interface-transition", ["X02", "X03"]),
    rec("VM-D118", "discovery-observations-late-cutoff-vm-d118-aimv2.md", ["VM-O06"],
        "Late-cutoff residual admission for VM-O06: AIMv2 (Apple, 2024-11-21) autoregressive prefix-ViT plus causal multimodal decoder (distinct objective family from masked/contrastive/distillation).",
        "AIMv2 (Apple, 2024)", "https://arxiv.org/abs/2411.14402",
        "Autoregressive raw-patch-then-text generation with dense per-token signal; frozen-trunk transfer; CVPR 2025 Highlight. Admitted per sweep criteria 1-5.",
        "d06", "image-text", "objective-variant", ["X01"]),
    rec("VM-D119", "discovery-observations-late-cutoff-vm-d119-uground.md", ["VM-O13", "VM-O08"],
        "Late-cutoff residual admission for VM-O13/VM-O08: UGround (2024-10-07, ICLR 2025 Oral) universal visual grounder (10M-element web-synthetic recipe; SeeAct-V vision-only interface context).",
        "UGround (2024)", "https://arxiv.org/abs/2410.05243",
        "Universal screenshot grounder breaking the accessibility-tree interface contract toward vision-only pixel action; SeeAct-V interface context folded in-card, not a separate node.",
        "d12", "screenshot-action", "interface-transition", ["X02"]),
    rec("VM-D120", "discovery-observations-late-cutoff-vm-d120-screenspot-pro.md", ["VM-O13"],
        "Late-cutoff residual admission for VM-O13: ScreenSpot-Pro (2025) professional high-resolution grounding evaluation plus planner-guided cascaded search contract.",
        "ScreenSpot-Pro (2025)", "https://arxiv.org/abs/2504.07981",
        "Full-screen professional-task grounding (0.07% area) plus ScreenSeekeR inference-time search contract; evaluation-methodology anchor for Computer Use.",
        "d12", "evaluation", "evaluation-contract", ["X04"]),
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
    if len(lines) == 112:
        assert not any(r["discovery_id"] in have for r in NEW_RECORDS)
        (root / JSONL_REL).write_text(
            "\n".join(lines + [json.dumps(r, ensure_ascii=False) for r in NEW_RECORDS]) + "\n",
            encoding="utf-8")
    elif len(lines) == 120:
        assert all(r["discovery_id"] in have for r in NEW_RECORDS), "unexpected 120-line state"
    else:
        raise ValueError(f"unexpected discovery line count: {len(lines)}")

    acc = root / ACC_REL
    acc.unlink(missing_ok=True)  # superseded 112-record stage output under §2-pre-authorized re-entry (already removed by rewind if absent)
    out = discovery.build_acceptance(root, root / JSONL_REL, root / X_REL, ISSUE_ID, acc)
    accepted = discovery.validate_acceptance(root, out)
    assert accepted["record_count"] == 120, accepted["record_count"]
    print("discovery records:", accepted["record_count"])

    with agent_tool.current_stage_basis_override():
        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "discovery-stage-validation-120.json"
        reviews_path = vdir / "discovery-stage-reviews-120.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Discovery stage-contract validation passed over canonical 120-record "
                         "acceptance (112 carried BASE + 8 late-cutoff BASE root collection). "
                         "Machine validation only; Sol Discovery review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"discovery-acceptance": acc}, reviews_path,
            ("TS-003 Discovery (re-)collection complete: 120 BASE root records "
             "(VM-D001-VM-D112 carried + 8 late-cutoff: DINOv3/SigLIP 2/SAM 3/pi-zero/FAST/AIMv2/UGround/ScreenSpot-Pro). "
             "Proceed to Screening; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "DISCOVERY_COLLECTED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
