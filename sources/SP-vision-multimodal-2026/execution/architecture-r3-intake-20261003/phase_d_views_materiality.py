#!/usr/bin/env python3
"""TS-003 Phase D (r3 re-entry): Edition Views (112) + Materiality + Completeness
+ advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

- Views: 111 rebuilt from authority input records + VM-D112 view (MATERIAL,
  native_omni_fusion + video_temporal_streaming, BRIDGE transition annotations);
  canonical accept_edition_views (append-only).
- Materiality rebuilt at the canonical path (112 rows; VM-D112 MATERIAL with
  P09/P11 rationale). Completeness rebuilt: carried 16 judgments + VM-O10/VM-O12
  rationale updates recording the VM-D112 disposition; other gaps preserved.
  V1-entity wording enforced on generated texts ("Kinetics / Something-Something
  V1 / Ego4D" style; frozen-profile echo noted, not edited).
- Advance via stage_validation + build_stage_checkpoint + advance_with_checkpoint.
- Frozen Core only + documented post-gate adaptation. Sol review owed.
"""

from __future__ import annotations

import json
import re
import tempfile
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

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/architecture-r3-intake-20261003"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
INPUT_REL = f"{SRC}/execution/screening-evidence-20260930/evidence-interactive-input.json"
VALIDATION_REL = f"{EDIR}/validation"

VM112_VIEW_RECORD = {
    "discovery_id": "VM-D112",
    "status": "VERIFIED",
    "materiality": "MATERIAL",
    "materiality_rationale": ("Query-driven acquisition transition material to P09 token/context "
                              "economics + third video-processing contract for P11; vendor ceilings."),
    "scope_dimensions": ["native_omni_fusion", "video_temporal_streaming"],
    "lineage_role": "BRIDGE",
    "branch_ids": ["d09-acquisition-economics", "d11-video-processing-contract"],
    "transition_ids": ["d09-fixed-to-selective-acquisition"],
    "inheritance_note": ("Static fixed-rate ingest redirected to query-driven selective "
                         "acquisition; cross-contract transition, not streaming."),
    "historical_attribution_caveat": None,
}

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
 "Qwen staged recipe, audio-input chain (Whisper/BEATs/CLAP), omni fusion with absolute-time sync, two technically distinct open families (InternVL3 paradigm contrast, Molmo 2 grounding comparator) plus repos; query-driven selective acquisition transition admitted via VM-D112 (static fixed-rate ingest redirected; token/context economics second axis); generation side excluded by boundary. G04/G05 are measurement-reproduction gaps, not fusion-coverage gaps."),
("VM-O11", "SATISFIED",
 "Polling (POPE), control-pair attribution (HallusionBench), CircularEval/bilingual (MMBench) and visual-math (MathVista) instruments kept distinct; scaffold-vs-perception attribution discipline recorded; no general-intelligence scores."),
("VM-O12", "SATISFIED",
 "Action/event/egocentric predecessors, duration-breadth (Video-MME), referred-reasoning (LongVideoBench), streaming system (Flash-VStream) and streaming eval (StreamingBench) bound; query-driven selective acquisition admitted via VM-D112 as the third video-processing contract (stored-timeline navigation, neither offline breadth nor online state); offline vs online contracts never share a metric column."),
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


def _latest(root: Path, pattern: str):
    cands = sorted((root / SRC / pattern).glob("*/" + pattern.split("/")[-1]))
    assert cands, pattern
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
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        ev_acceptance = core.load_json(ev_acc)
        assert ev_acceptance["result_count"] == 112, ev_acceptance["result_count"]
        print("evidence basis:", ev_acc.parent.name[:12])

        # Views: 111 rebuilt + VM-D112.
        doc = core.load_json(root / INPUT_REL)
        records = {r["discovery_id"]: r for r in
                   (doc["records"] if isinstance(doc, dict) else doc)}
        assert len(records) == 111 and "VM-D112" not in records
        records["VM-D112"] = dict(VM112_VIEW_RECORD)
        by_task_rows = {row["evidence_task_id"]: row for row in ev_acceptance["results"]}
        assert len(by_task_rows) == 112
        with tempfile.TemporaryDirectory() as temp:
            views_dir = Path(temp) / "views"
            views_dir.mkdir()
            for row in ev_acceptance["results"]:
                task_id = row["evidence_task_id"]
                did = row["discovery_ids"][0]
                view = inter._build_view(profile, task_id, row["sha256"], records[did])
                errs = evidence.validate_edition_view(
                    view, profile, row["sha256"], row["status"])
                if errs:
                    raise ValueError(f"View {task_id} invalid: {'; '.join(errs)}")
                core.write_json(views_dir / evidence.view_filename(task_id), view)
            source_root = core.repo_local_path(
                root, profile["paths"]["source_root"], "paths.source_root")
            views_acceptance_path = evidence.accept_edition_views(
                root, profile_path, ev_acc, views_dir,
                source_root / "evidence/v2/views/accepted", impl)
            evidence.validate_edition_views_acceptance(
                root, profile_path, ev_acc, views_acceptance_path, impl)
        print("views acceptance:", views_acceptance_path.relative_to(root))

        scr_acc = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                      key=lambda p: p.stat().st_mtime)
        ledger = evidence.build_materiality_ledger(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc,
            views_acceptance_path, impl)
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        assert not ledger_path.exists(), "canonical ledger should have been invalidated"
        core.write_json(ledger_path, ledger)
        evidence.validate_materiality_ledger(
            ledger, root, profile_path, root / DISC_REL, scr_acc,
            ev_acc, views_acceptance_path, impl)
        assert len(ledger["rows"]) == 112, len(ledger["rows"])
        vm112_rows = [r for r in ledger["rows"] if r["discovery_id"] == "VM-D112"]
        assert len(vm112_rows) == 1 and vm112_rows[0]["downstream_disposition"] == "MATERIAL"
        print("materiality rows:", len(ledger["rows"]), "| VM-D112:", vm112_rows[0]["downstream_disposition"])

        by_id = {o["obligation_id"]: o for o in profile["research_scope"]["initial_obligations"]}
        assert set(by_id) == {j[0] for j in JUDGMENTS} == {f"VM-O{i:02d}" for i in range(1, 17)}
        discovery_records = [json.loads(l) for l in
                             open(root / DISC_REL, encoding="utf-8")]
        assert len(discovery_records) == 112
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
            ev_acc, views_acceptance_path, ledger_path, impl)
        assert not errs, errs[:3]
        print("completeness:", result["overall_status"])

        blob = ledger_path.read_text(encoding="utf-8") + comp_path.read_text(encoding="utf-8")
        assert "Something-Something V2" not in blob, "V2 entity regression"
        for m in re.finditer(r".{0,40}SSv2.{0,40}", blob):
            assert "Kinetics/SSv2/Ego4D predecessor" in m.group(0), m.group(0)
        print("SSv2 purge: clean (V1 entity consistent; profile-echo only)")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "evidence-materiality-completeness-validation-112.json"
        reviews_path = vdir / "evidence-materiality-completeness-reviews-112.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Combined Evidence/Materiality/Completeness stage-contract validation "
                         "passed over canonical 112 authority (VM-D112 MATERIAL, V1 held). "
                         "Machine validation only; Sol review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path}, reviews_path,
            ("TS-003 Evidence/Materiality/Completeness complete over 112-record canonical "
             "authority (VM-D112 admitted MATERIAL, V1 identity held, SSv2-free generated "
             "texts). Proceed to Selection; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "EVIDENCE_REVIEWED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
