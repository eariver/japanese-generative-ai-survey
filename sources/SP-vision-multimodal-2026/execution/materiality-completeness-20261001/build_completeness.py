#!/usr/bin/env python3
"""Build TS-003 Profile Completeness from r5 Evidence/Views + operator obligation judgments.

Operator (Work role) coverage judgments below are analytical accounting over the
accepted r5 corpus, not Sol/Human decisions. No new research performed.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter
from scripts import survey_schema_v2 as schema_gate

ISSUE = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE}"

# (obligation_id, status, rationale) — evidence-grounded, scope-constrained per Sol request §4/§5
JUDGMENTS = [
("VM-O01", "SATISFIED",
 "Context-capped scope met: Neocognitron/LeNet predecessor context + AlexNet/ResNet anchors with mechanism, bottleneck and transfer detail. LeNet PDF encoding barrier and Neocognitron paywall do not block the context-level claim. No pre-deep CV expansion."),
("VM-O02", "SATISFIED",
 "Region/two-stage, one-stage operating points, DETR set-prediction transition and OV bridge all bound with mechanism detail; DINO detector/ss disambiguated. OWOD remains a D07B footnote by design."),
("VM-O03", "SATISFIED",
 "Dense/instance/panoptic/promptable distinctions bound; SAM dual reading and SAM 2 video bridge recorded. U-Net confined to segmentation role (TS-002 boundary intact)."),
("VM-O04", "SATISFIED",
 "Four-node support cap met exactly (MiDaS/OpenPose/Visual Genome/DUSt3R) with stated limits; support-substrate purpose fulfilled; refusals (NeRF/3DGS/SLAM/MVS) ledgered, not silently omitted."),
("VM-O05", "SATISFIED",
 "LayoutLM lineage, OCR-free branch, Nougat/GOT specialist poles with failure profiles, Pix2Struct UI bridge and retrieval sub-lane all bound. Specialist-vs-generalist comparison stands on the qualitative five-axis contract; numeric ranking prohibited by contract (G03 concerns same-protocol head-to-head absence, not a coverage deficit)."),
("VM-O06", "LIMITATION",
 "Token-formulation and label-free representation lineage complete (ViT/DeiT/Swin/MAE/DINO/DINOv2) and encoder reuse into Qwen established; residual is G06: SigLIP2 exact primary citation still unbound. Bounded residual that does not prevent the reuse claim."),
("VM-O07", "SATISFIED",
 "Captioning/VQA predecessors, CLIP addressability break with preserved bag-of-words limitation, and ALIGN/SigLIP variants bound; image-level metric identity never merged with grounding metrics."),
("VM-O08", "SATISFIED",
 "Full 12-step minimum chain (phrase task, REC contract, OVD formulation, distillation/region/vocabulary poles, reformulation, modulation, fusion poles, web-scale, OVS branch) plus LVIS eval home; redundancy calls recorded; GoldG composition is an Evidence-depth detail, not a coverage gap."),
("VM-O09", "SATISFIED",
 "Frozen precursor, Flamingo/BLIP-2 anchors, InstructBLIP/MiniGPT-4 bridge gap filled, and LLaVA instruction-tuning anchor bound with distinct connector strategies; no flattening."),
("VM-O10", "SATISFIED",
 "Qwen staged recipe, audio-input chain (Whisper/BEATs/CLAP), omni fusion with absolute-time sync, two technically distinct open families (InternVL3 paradigm contrast, Molmo 2 grounding comparator) plus repos; generation side excluded by boundary. G04/G05 are measurement-reproduction gaps, not fusion-coverage gaps."),
("VM-O11", "SATISFIED",
 "Polling (POPE), control-pair attribution (HallusionBench), CircularEval/bilingual (MMBench) and visual-math (MathVista) instruments kept distinct; scaffold-vs-perception attribution discipline recorded; no general-intelligence scores."),
("VM-O12", "SATISFIED",
 "Action/event/egocentric predecessors, duration-breadth (Video-MME), referred-reasoning (LongVideoBench), streaming system (Flash-VStream) and streaming eval (StreamingBench) bound; offline vs online contracts never share a metric column."),
("VM-O13", "SATISFIED",
 "OSWorld grounding thesis, OSWorld 2.0 state-management thesis with cost curves, ScreenSpot pure-localization accuracy and interface-contract comparison bound; endpoint bounded, no agent-survey expansion."),
("VM-O14", "LIMITATION",
 "Seven-node minimum chain complete (planner-side, data regime, joint representation, cross-embodiment data, action tokenization, open implementation, card-scoped endpoint) within the representation/action interface; residual is G01: independent/non-vendor VLA evaluation scarcity bounds policy-evaluation claims."),
("VM-O15", "LIMITATION",
 "Four-pole separation established (historical formulation, Dreamer latent dynamics, JEPA/V-JEPA predictive representation, Genie interactive generative) with anti-collapse rows and non-ancestry guard; residual is G02: no transferable control-oriented world-model benchmark, bounding dynamics-usability claims."),
("VM-O16", "SATISFIED",
 "Retain-set benchmarks with distinct contracts, ANLS/relaxed-accuracy/private-set disciplines, version/config/judge/budget/contamination binding rules and vendor-vs-independent separation; catalogue and cross-task ranking refused."),
]

RESIDUAL = [
 "G01 independent/non-vendor VLA evaluation scarcity (bounds O14 policy-evaluation claims).",
 "G02 transferable control-oriented world-model benchmark absent (bounds O15 dynamics-use claims).",
 "G03 same-protocol document specialist vs generalist comparison absent (numeric ranking prohibited; qualitative contract stands).",
 "G04 real-deployment latency/VRAM beyond author-reported values (bounds deployment claims).",
 "G05 independent reproduction of current vendor/model-report scores (all vendor scores quarantined with attribution).",
 "G06 SigLIP2 exact citation binding (encoder-reuse lineage established; citation to be bound later).",
 "Access barriers: LeNet author-PDF custom-font encoding; Neocognitron paywall (both context-scope only).",
 "Living surfaces: repo commit pinning, vendor page drift, InternVL3.5/ScreenSpot-successor currency deferred to later stages.",
]

# Validator semantics (survey_evidence_v2.validate_completeness): LIMITED closure requires
# targeted_gap_fill_completed=true. The targeted gap-fill *process* completed via the
# pre-production rally (Rounds B/D targeted follow-up) and the Discovery coverage design
# (streaming resolved, second open-VLM family resolved, grounding chain completed);
# G01-G06 are bounded residual limitations, not un-attempted gap-fills.
CLOSURE_LIMITS = None  # replaced: closure.limitations must superset residual_limitations


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    profile_path = root / f"{SRC}/production-profile.json"
    profile = core.load_json(profile_path)
    ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
    ledger = core.load_json(ledger_path)
    discovery_records = [json.loads(l) for l in open(root / f"{SRC}/discovery/discovery-v2.jsonl")]

    by_id = {o["obligation_id"]: o for o in profile["research_scope"]["initial_obligations"]}
    assert set(by_id) == {j[0] for j in JUDGMENTS} == {f"VM-O{i:02d}" for i in range(1, 17)}, "obligation set mismatch"
    assert [j[0] for j in JUDGMENTS] == sorted(j[0] for j in JUDGMENTS)

    input_value = {
        "obligations": [{"obligation_id": oid, "status": st, "rationale": ra} for oid, st, ra in JUDGMENTS],
        "residual_limitations": RESIDUAL,
        "closure": {"targeted_gap_fill_completed": True,
                    "limitations": RESIDUAL,
                    "status": "LIMITED"},
    }
    # validate input shape via canonical validator path
    inter._validate_completeness_input(input_value, profile)

    result = inter._build_completeness(root, profile, profile_path, discovery_records,
                                       ledger_path, ledger, input_value)
    schema_gate.validate_instance(result, root / "schemas/profile-completeness-result.schema.json",
                                  label="Profile Completeness")
    out = root / f"{SRC}/profile-completeness-v2.json"
    if out.exists():
        raise ValueError("refusing to overwrite Profile Completeness")
    core.write_json(out, result)
    with agent_tool.current_stage_basis_override():
        errors = completeness.validate_profile_completeness(
            result, root, profile_path,
            root / f"{SRC}/discovery/discovery-v2.jsonl",
            root / f"{SRC}/screening/v2/accepted/71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67/screening-accepted.json",
            root / f"{SRC}/evidence/v2/accepted/4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34/evidence-accepted.json",
            root / f"{SRC}/evidence/v2/views/accepted/e3d0b3b33588b235e1c9be41259fb5bb5e07cbd1105ac0ff31a7bf7b34bfd0c5/edition-views-accepted.json",
            ledger_path,
            core.repository_commit_sha(root))
    if errors:
        raise ValueError("Profile Completeness invalid: " + "; ".join(errors))
    from collections import Counter
    print("overall:", result["overall_status"], "| closure:", result["closure"]["status"])
    print("statuses:", dict(Counter(o["status"] for o in result["obligations"])))
    print("closure counters:", {k: result["closure"][k] for k in
          ["expansion_passes", "final_pass_new_sources", "final_pass_new_material_obligations",
           "final_pass_new_material_obligations_open", "targeted_gap_fill_completed", "open_material_obligations"]})
    print("wrote:", out.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
