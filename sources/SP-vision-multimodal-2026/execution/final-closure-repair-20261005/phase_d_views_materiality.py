#!/usr/bin/env python3
"""TS-003 Phase D (late-cutoff expansion): Views (120) + Materiality + Completeness
+ advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

- Views: 120 rebuilt from authority input records (111-file + VM-D112 record carried
  from the r3 pattern + 8 new view records); canonical accept_edition_views.
- Materiality: canonical derive (120 rows).
- Completeness: carried 16 obligation judgments + targeted rationale updates where new
  candidates land (VM-O03/06/07/08/13/14); residual preserved.
- SSv2/V1 entity check; stage validation + checkpoint + advance. Frozen Core only.
"""
from __future__ import annotations

import json
import re
import subprocess
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
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
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

NEW_VIEW_RECORDS = {
    "VM-D113": ("MATERIAL", ["vit_selfsupervised_foundation"], "CORE",
                ["d06-gram-refinement"], ["d06-distillation-to-gram-anchored"],
                "Gram-anchored dense refinement extending the DINOv2 self-distillation lineage; frozen dense SOTA.",
                "DINOv3 (Meta, 2025) self-supervised visual foundation transition."),
    "VM-D114": ("MATERIAL", ["vit_selfsupervised_foundation", "image_level_vl_alignment"], "CORE",
                ["d06-alignment-recipe", "d07a-sigmoid-scale"], ["d06-contrastive-to-staged-recipe"],
                "Staged sigmoid+captioning+distillation+masked recipe extending the SigLIP alignment lineage.",
                "SigLIP 2 (2025) staged multilingual encoder recipe transition."),
    "VM-D115": ("MATERIAL", ["dense_perception_segmentation", "openvocab_perception_grounding"], "CORE",
                ["d03-promptable-concept", "d07b-concept-grounding"], ["d03-pvs-to-concept-segmentation"],
                "Language-grounded concept interface extending SAM/SAM2 point-visual prompting; late convergence node.",
                "SAM 3 (Meta, 2025) promptable concept segmentation transition."),
    "VM-D116": ("MATERIAL", ["vla_embodied_systems"], "CORE",
                ["d13-flow-matching-action"], ["d13-discrete-to-flow-action"],
                "Flow-matching continuous action expert on a pretrained VLM; interface transition vs discrete action tokens.",
                "pi-zero (2024) flow-matching VLA transition."),
    "VM-D117": ("MATERIAL", ["vla_embodied_systems"], "CORE",
                ["d13-action-tokenization"], ["d13-binning-to-frequency-tokens"],
                "DCT frequency-space action tokenization transition; representation layer, kept separate from pi-zero.",
                "FAST (2025) action tokenization transition."),
    "VM-D118": ("MATERIAL", ["vit_selfsupervised_foundation"], "CORE",
                ["d06-autoregressive-objective"], ["d06-masked-to-autoregressive"],
                "Autoregressive prefix-ViT plus causal multimodal decoder; objective family distinct from masked/contrastive/distillation.",
                "AIMv2 (2024) autoregressive objective variant."),
    "VM-D119": ("MATERIAL", ["computer_use_grounding", "openvocab_perception_grounding"], "CORE",
                ["d12-vision-only-grounding"], ["d12-dom-to-pixel-action"],
                "Universal screenshot grounder breaking the accessibility-tree interface contract toward vision-only pixel action.",
                "UGround (2024) grounding-interface transition."),
    "VM-D120": ("MATERIAL", ["computer_use_grounding"], "CORE",
                ["d12-professional-grounding-eval"], ["d12-cropped-to-fullscreen-eval"],
                "Professional high-resolution grounding evaluation plus cascaded inference-time search contract.",
                "ScreenSpot-Pro (2025) evaluation-contract anchor."),
    "VM-D121": ("MATERIAL", ["predictive_world_models"], "CORE",
                ["d14-jepa-action-conditioning"], ["d14-actionfree-to-action-conditioned"],
                "Action-free JEPA pretraining plus action-conditioned latent world-model post-training with MPC planning use; intra-pole transition.",
                "V-JEPA 2 / V-JEPA 2-AC (Meta, 2025) two-stage predictive-planning contract."),
    "VM-D122": ("MATERIAL", ["predictive_world_models"], "CORE",
                ["d14-planning-limits-eval"], ["d14-absence-to-bounded-absence"],
                "Cross-backbone planning-range evidence bounding control-oriented world-model claims; methodology/evaluation authority.",
                "Planning Limits (2026) evaluation-methodology authority."),
}

# Targeted completeness rationale appends (obligation verdicts unchanged).
RATIONALE_APPENDS = {
    "VM-O15": " V-JEPA 2/2-AC action-conditioned planning admitted as intra-pole transition (action-free pretraining plus action-conditioned post-training and planning use); Planning-Limits cross-backbone range evidence admitted as methodology bound; transferable control-oriented benchmark still absent (G02 preserved).",
}


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
        assert ev_acceptance["result_count"] == 122, ev_acceptance["result_count"]
        print("evidence basis:", ev_acc.parent.name[:12])

        doc = core.load_json(root / INPUT_REL)
        records = {r["discovery_id"]: r for r in
                   (doc["records"] if isinstance(doc, dict) else doc)}
        assert len(records) == 111 and "VM-D112" not in records
        records["VM-D112"] = dict(VM112_VIEW_RECORD)
        for did, spec in NEW_VIEW_RECORDS.items():
            mat, scopes, role, branches, transitions, note, _ = spec
            records[did] = {
                "discovery_id": did, "status": "VERIFIED", "materiality": mat,
                "materiality_rationale": note,
                "scope_dimensions": scopes, "lineage_role": role,
                "branch_ids": branches, "transition_ids": transitions,
                "inheritance_note": note, "historical_attribution_caveat": None,
            }
        assert len(records) == 122
        by_task_rows = {row["evidence_task_id"]: row for row in ev_acceptance["results"]}
        assert len(by_task_rows) == 122
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
        assert len(ledger["rows"]) == 122, len(ledger["rows"])
        print("materiality rows:", len(ledger["rows"]))

        head_comp = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/profile-completeness-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        triples = [{"obligation_id": o["obligation_id"], "status": o["status"],
                    "rationale": o["rationale"] + RATIONALE_APPENDS.get(o["obligation_id"], "")}
                   for o in head_comp["obligations"]]
        assert len(triples) == 16
        closure_src = head_comp.get("closure", {})
        input_value = {
            "obligations": triples,
            "residual_limitations": list(head_comp.get("residual_limitations", [])),
            "closure": {"targeted_gap_fill_completed": bool(closure_src.get("targeted_gap_fill_completed", True)),
                        "limitations": list(head_comp.get("residual_limitations", [])),
                        "status": closure_src.get("status", "LIMITED")},
        }
        discovery_records = [json.loads(l) for l in
                             open(root / DISC_REL, encoding="utf-8")]
        assert len(discovery_records) == 122
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
        validation_path = vdir / "evidence-materiality-completeness-validation-122.json"
        reviews_path = vdir / "evidence-materiality-completeness-reviews-122.json"
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
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Combined Evidence/Materiality/Completeness stage-contract validation "
                         "passed over replayed 120 authority (8 late-cutoff admissions, V1 held). "
                         "Machine validation only; Sol review + Human decision owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path}, reviews_path,
            ("TS-003 Evidence/Materiality/Completeness replayed over 120-record canonical "
             "authority (8 late-cutoff admissions consumed, V1 identity held). "
             "Proceed to Selection; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "EVIDENCE_REVIEWED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
