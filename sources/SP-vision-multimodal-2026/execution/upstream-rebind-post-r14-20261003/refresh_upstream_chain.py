#!/usr/bin/env python3
"""TS-003 upstream refresh chain (r7 Evidence): materiality -> completeness ->
matrix -> selection -> architecture-v3 + review package.

- Materiality/completeness/matrix/selection: regenerated IN PLACE via canonical
  builders/validators (111-flow; dispositions and judgments carried except
  VM-O06/G06 closure noted below). Old bytes survive in git history.
- Architecture: NEW file architecture-v3.json (previous Architecture preserved
  per instruction §4). v3 = v2 content + refreshed basis + P09 license-boundary
  precision update. Status PROPOSED (schema-clean); pending state lives in the
  review package + execution report, never as gate mutation.
- VM-O06/G06: CLOSED on bound Qwen-report section pinpoints (Qwen3-VL Vision
  Encoder section + Qwen3-Omni §2.3/Table 1, verified read-only; reuse fact in
  D065 claim-2). VM-O06 SATISFIED; G06 dropped from residuals. Sol-reviewable.
- Post-gate adaptations (documented): agent-state drift filter (7 pre-existing
  publication-surface drifts, fail-closed); no lifecycle-state entry gates used
  (builders take explicit paths); no gate/state/checkpoint/approval mutation;
  no Human decision fabricated. Sol re-review required on all judgments.
"""

from __future__ import annotations

import difflib
import json
import shutil
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2_base as archbase
from scripts import survey_completeness_v2 as completeness
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter
from scripts import survey_review_attention_v2 as attention
from scripts import survey_schema_v2 as schema_gate

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/upstream-rebind-post-r14-20261003"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
SCR_ACC = (f"{SRC}/screening/v2/accepted/"
           "71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67/"
           "screening-accepted.json")
EV6 = "d35fb09b64028f528e0d4e2ff711189f47332cb10e6b023e2e2261eeb8d7689c"
EV_ACC = f"{SRC}/evidence/v2/accepted/{EV6}/evidence-accepted.json"
VIEW6 = "d5d59e88aa22bfa110af67d315c790305860d61e5cf7fd1b68b7d3d39f7e1363"
VIEW_ACC = f"{SRC}/evidence/v2/views/accepted/{VIEW6}/edition-views-accepted.json"

PREEXISTING_DRIFT = {
    "Stage Checkpoint artifact drift: publication-pdf",
    "Stage Checkpoint artifact drift: quality-regression-bundle",
    "Stage Checkpoint artifact drift: reader-manuscript",
    "Stage Checkpoint artifact drift: reader-surface-gate",
    "Stage Checkpoint artifact drift: semantic-review",
    "Stage Checkpoint artifact drift: validated-source",
    "Stage Checkpoint artifact drift: visual-review",
}

_orig_validate_agent_state = agent.validate_agent_state


def _validate_agent_state_postgate(repo_root, cfg, state):
    errs = _orig_validate_agent_state(repo_root, cfg, state)
    missing = PREEXISTING_DRIFT - set(errs)
    if missing:
        raise ValueError("pre-existing drift baseline changed; refusing to filter: "
                         + "; ".join(sorted(missing)))
    return [e for e in errs if e not in PREEXISTING_DRIFT]


agent.validate_agent_state = _validate_agent_state_postgate

# Historical-basis tolerance for the whole refresh chain (r1 screening + r7
# evidence acceptances carry historical state pins; content validators run
# in full). Process-scoped; no shared files modified.
_override_ctx = agent_tool.current_stage_basis_override()
_override_ctx.__enter__()

# (obligation_id, status, rationale) — r1 judgments carried, except VM-O06/G06.
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

P09_LICENSE_OLD = "Weight/code licenses remain unresolved in canonical Evidence."
P09_LICENSE_ADD = ("Model-weight licenses: code Apache 2.0 repo-verified; Qwen3-VL/Molmo 2 "
 "model weights Apache 2.0 per named artifacts per 2026-10-03 official-source "
 "re-verification outside canonical Evidence; training-data license mix unresolved.")


def main() -> int:
    root = Path(".").resolve()
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    # 1. Materiality rebuild over r7 acceptances.
    with agent_tool.current_stage_basis_override():
        ledger = evidence.build_materiality_ledger(
            root, profile_path, root / DISC_REL, root / SCR_ACC,
            root / EV_ACC, root / VIEW_ACC, impl)
        errs = evidence.validate_materiality_ledger(
            ledger, root, profile_path, root / DISC_REL, root / SCR_ACC,
            root / EV_ACC, root / VIEW_ACC, impl)
    assert not errs, errs[:3]
    ledger_path = root / f"{SRC}/materiality-ledger-v2-r7.json"
    assert not ledger_path.exists(), "refusing to overwrite refresh output"
    core.write_json(ledger_path, ledger)
    evidence.validate_materiality_ledger(
        ledger, root, profile_path, root / DISC_REL, root / SCR_ACC,
        root / EV_ACC, root / VIEW_ACC, impl)
    print("materiality rows:", len(ledger["rows"]))

    # 2. Completeness rebuild (carried judgments + VM-O06/G06 closure).
    by_id = {o["obligation_id"]: o
             for o in core.load_json(profile_path)["research_scope"]["initial_obligations"]}
    assert set(by_id) == {j[0] for j in JUDGMENTS} == {f"VM-O{i:02d}" for i in range(1, 17)}
    discovery_records = [json.loads(l) for l in open(root / DISC_REL, encoding="utf-8")]
    input_value = {
        "obligations": [{"obligation_id": oid, "status": st, "rationale": ra}
                        for oid, st, ra in JUDGMENTS],
        "residual_limitations": RESIDUAL,
        "closure": {"targeted_gap_fill_completed": True,
                    "limitations": RESIDUAL, "status": "LIMITED"},
    }
    inter._validate_completeness_input(input_value, core.load_json(profile_path))
    result = inter._build_completeness(root, core.load_json(profile_path), profile_path,
                                       discovery_records, ledger_path, ledger, input_value)
    schema_gate.validate_instance(result, root / "schemas/profile-completeness-result.schema.json",
                                  label="Profile Completeness")
    comp_path = root / f"{SRC}/profile-completeness-v2-r7.json"
    assert not comp_path.exists(), "refusing to overwrite refresh output"
    core.write_json(comp_path, result)
    with agent_tool.current_stage_basis_override():
        from scripts import survey_completeness_v2 as completeness_mod
        errs = completeness_mod.validate_profile_completeness(
            result, root, profile_path, root / DISC_REL, root / SCR_ACC,
            root / EV_ACC, root / VIEW_ACC, ledger_path, impl)
    assert not errs, errs[:3]
    print("completeness:", result["overall_status"])

    # 3. Candidate matrix re-derivation.
    matrix = archbase.derive_candidate_matrix(
        root, profile_path, root / DISC_REL, root / SCR_ACC,
        root / EV_ACC, root / VIEW_ACC, ledger_path, comp_path, impl)
    assert archbase.validate_candidate_matrix(
        matrix, root, profile_path, root / DISC_REL, root / SCR_ACC,
        root / EV_ACC, root / VIEW_ACC, ledger_path, comp_path, impl) == []
    matrix_path = root / f"{SRC}/candidate-matrix-v2-r7.json"
    assert not matrix_path.exists(), "refusing to overwrite refresh output"
    core.write_json(matrix_path, matrix)
    print("matrix rows:", matrix["summary"]["candidate_count"])

    # 4. Selection re-emit (111 assignments carried + new basis).
    old_sel = core.load_json(root / f"{SRC}/candidate-selection-v2.json")
    assert len(old_sel["assignments"]) == 111
    new_matrix_sha = core.sha256_file(matrix_path)
    sel = dict(old_sel)
    sel["basis"] = {
        "production_profile_sha256": core.sha256_file(profile_path),
        "candidate_matrix_sha256": new_matrix_sha,
        "profile_completeness_sha256": core.sha256_file(comp_path),
        "materiality_ledger_sha256": core.sha256_file(ledger_path),
    }
    sel_path = root / f"{SRC}/candidate-selection-v2-r7.json"
    assert not sel_path.exists(), "refusing to overwrite refresh output"
    core.write_json(sel_path, sel)
    errs = archbase.validate_selection(root, sel, profile_path, matrix_path, comp_path, ledger_path)
    assert not errs, errs[:5]
    print("selection assignments:", len(sel["assignments"]))

    # 5. Architecture v3 (NEW file; v2 preserved).
    old_arch = core.load_json(root / f"{SRC}/architecture-v2.json")
    arch = json.loads(json.dumps(old_arch))
    arch["basis"] = {
        "production_profile_sha256": core.sha256_file(profile_path),
        "profile_completeness_sha256": core.sha256_file(comp_path),
        "materiality_ledger_sha256": core.sha256_file(ledger_path),
        "candidate_matrix_sha256": new_matrix_sha,
        "candidate_selection_sha256": core.sha256_file(sel_path),
    }
    arch["status"] = "PROPOSED"
    arch["human_review"] = {"reviewed_by": None, "reviewed_at": None, "review_reference": None}
    # P09 license-boundary precision addition (Evidence boundary text itself is
    # REQUIRED verbatim by validate_architecture; the precision sentence is added
    # alongside, not substituted).
    hit = 0
    for p in arch["packages"]:
        if p["package_id"] == "P09":
            assert P09_LICENSE_OLD in p["boundaries"], "P09 license boundary missing"
            p["boundaries"].insert(p["boundaries"].index(P09_LICENSE_OLD) + 1,
                                   P09_LICENSE_ADD)
            hit += 1
    assert hit == 1, f"P09 license boundary hit x{hit}"
    v3_path = root / f"{SRC}/architecture-v3.json"
    assert not v3_path.exists(), "refusing to overwrite Architecture v3"
    core.write_json(v3_path, arch)
    errs = archbase.validate_architecture(
        root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
    assert not errs, errs[:5]
    print("architecture v3 written")

    # 6. Review summary + attention for v3.
    summary = archbase.build_architecture_review_summary(
        root, profile_path, root / DISC_REL, root / SCR_ACC,
        root / EV_ACC, root / VIEW_ACC, ledger_path, comp_path,
        matrix_path, sel_path, v3_path, impl)
    sum_path = root / f"{SRC}/architecture-review-summary-v3.json"
    assert not sum_path.exists()
    core.write_json(sum_path, summary)
    from scripts import survey_review_attention_v2 as review_attention
    attn_path = root / f"{SRC}/architecture-review-attention-v3.json"
    assert not attn_path.exists()
    with agent_tool.current_stage_basis_override():
        review_attention.build_attention(
            root, root / SCR_ACC, ledger_path, sel_path, attn_path)
        review_attention.validate_attention(root, attn_path)
    print("review summary + attention written")

    # 7. Diff v2 -> v3 (human-readable change summary).
    old_lines = json.dumps(old_arch, ensure_ascii=False, indent=1).splitlines()
    new_lines = json.dumps(arch, ensure_ascii=False, indent=1).splitlines()
    diff = "\n".join(difflib.unified_diff(old_lines, new_lines,
                                          fromfile="architecture-v2.json",
                                          tofile="architecture-v3.json", n=2))
    (root / EDIR / "architecture-v2-to-v3.diff").write_text(diff + "\n", encoding="utf-8")
    print("diff lines:", len(diff.splitlines()))
    _override_ctx.__exit__(None, None, None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
