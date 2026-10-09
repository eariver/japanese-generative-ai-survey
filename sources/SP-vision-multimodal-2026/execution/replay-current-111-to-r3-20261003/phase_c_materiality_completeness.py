#!/usr/bin/env python3
"""TS-003 replay Phase C: Materiality + Completeness + advance to EVIDENCE_REVIEWED.

- Materiality rebuilt at the canonical path (deleted by re-entry) via canonical
  builder + validator. Dispositions re-derived (expect 101/10 pattern).
- Completeness rebuilt at the canonical path with carried judgments (16;
  VM-O06 SATISFIED on Qwen-report section binding carried from r8; G06 dropped;
  all other gaps preserved). SSv2 scan enforced on new files.
- Advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED (advance_evidence pattern).
- Frozen Core only + documented post-gate adaptation. Sol review owed.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness_mod
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_stage_validation_v2 as stage_validation
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/replay-current-111-to-r3-20261003"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
VALIDATION_REL = f"{EDIR}/validation"

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
("VM-O06", "SATISFIED",
 "Token-formulation and label-free representation lineage complete (ViT/DeiT/Swin/MAE/DINO/DINOv2) and encoder reuse into Qwen established with exact citation binding now specified: SigLIP2-So400m initialization and dynamic-resolution continual training per Qwen3-VL report Vision Encoder section and Qwen3-Omni report section 2.3/Table 1 (read-only verified 2026-10-03; reuse fact in D065 claim-2)."),
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
 "Access barriers: LeNet author-PDF custom-font encoding; Neocognitron paywall (both context-scope only).",
 "Living surfaces: repo commit pinning, vendor page drift, InternVL3.5/ScreenSpot-successor currency deferred to later stages.",
]


def _latest_acceptance(root: Path, kind: str) -> Path:
    cands = sorted((root / SRC / kind).glob("*/*.json" if kind == "screening/v2/accepted" else "*/evidence-accepted.json"))
    return max(cands, key=lambda p: p.stat().st_mtime)


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL
    profile = core.load_json(profile_path)

    with agent_tool.current_stage_basis_override():
        scr_acc = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                      key=lambda p: p.stat().st_mtime)
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        view_acc = max((root / SRC / "evidence/v2/views/accepted").glob("*/edition-views-accepted.json"),
                       key=lambda p: p.stat().st_mtime)
        print("screening:", scr_acc.parent.name[:12], "| evidence:", ev_acc.parent.name[:12],
              "| views:", view_acc.parent.name[:12])

        ledger = evidence.build_materiality_ledger(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc, view_acc, impl)
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        assert not ledger_path.exists(), "canonical ledger should have been invalidated"
        core.write_json(ledger_path, ledger)
        evidence.validate_materiality_ledger(
            ledger, root, profile_path, root / DISC_REL, scr_acc,
            ev_acc, view_acc, impl)
        from collections import Counter
        print("materiality rows:", len(ledger["rows"]),
              dict(Counter(r["downstream_disposition"] for r in ledger["rows"])))

        by_id = {o["obligation_id"]: o for o in profile["research_scope"]["initial_obligations"]}
        assert set(by_id) == {j[0] for j in JUDGMENTS} == {f"VM-O{i:02d}" for i in range(1, 17)}
        discovery_records = [json.loads(l) for l in open(root / DISC_REL, encoding="utf-8")]
        assert len(discovery_records) == 111
        input_value = {
            "obligations": [{"obligation_id": oid, "status": st, "rationale": ra}
                            for oid, st, ra in JUDGMENTS],
            "residual_limitations": RESIDUAL,
            "closure": {"targeted_gap_fill_completed": True,
                        "limitations": RESIDUAL, "status": "LIMITED"},
        }
        inter._validate_completeness_input(input_value, profile)
        result = inter._build_completeness(root, profile, profile_path,
                                           discovery_records, ledger_path, ledger, input_value)
        schema_gate.validate_instance(
            result, root / "schemas/profile-completeness-result.schema.json",
            label="Profile Completeness")
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        assert not comp_path.exists(), "canonical completeness should have been invalidated"
        core.write_json(comp_path, result)
        errs = completeness_mod.validate_profile_completeness(
            result, root, profile_path, root / DISC_REL, scr_acc,
            ev_acc, view_acc, ledger_path, impl)
        assert not errs, errs[:3]
        print("completeness:", result["overall_status"])

        # SSv2 purge check on fresh canonical files: the entity misbinding
        # "Something-Something V2" must be absent. Bare "SSv2" has two known
        # legitimate contexts only: (a) the frozen Production Profile's own
        # VM-O12 obligation description echo (profile bytes, immutable, out of
        # scope), (b) V-JEPA's benchmark score citation "SSv2 72.2" in carried
        # historical task content (correct benchmark name, byte-identical carry).
        import re
        blob = ledger_path.read_text(encoding="utf-8") + comp_path.read_text(encoding="utf-8")
        assert "Something-Something V2" not in blob, "V2 entity regression"
        for m in re.finditer(r".{0,40}SSv2.{0,40}", blob):
            ctx = m.group(0)
            assert ("Kinetics/SSv2/Ego4D predecessor" in ctx), f"unexpected SSv2 context: {ctx}"
        print("SSv2 purge: clean (V1 entity consistent; profile-echo only)")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "evidence-materiality-completeness-validation-111.json"
        reviews_path = vdir / "evidence-materiality-completeness-reviews-111.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": view_acc,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Combined Evidence/Materiality/Completeness stage-contract validation "
                         "passed over replayed 111 authority (no VM-D112). Machine validation "
                         "only; Sol Materiality/Completeness review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": view_acc,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path}, reviews_path,
            ("TS-003 Evidence/Materiality/Completeness replay complete over 111-record "
             "canonical authority (r8 repairs preserved, SSv2-free). Proceed to Selection; "
             "Sol Materiality/Completeness review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "EVIDENCE_REVIEWED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
