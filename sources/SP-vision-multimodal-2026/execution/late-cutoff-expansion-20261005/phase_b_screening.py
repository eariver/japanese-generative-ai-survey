#!/usr/bin/env python3
"""TS-003 Phase B (late-cutoff expansion): Screening (120) + advance to CANDIDATES_NORMALIZED.

- Fresh screening package over canonical 120-record Discovery.
- Decisions: 112 carried byte-identical objects + 8 new KEEP decisions, each genuinely
  evaluated (cutoff pre-2026-09-30 official primary; obligation materiality;
  non-duplicate vs covered neighbors; vendor-ceiling boundaries where applicable).
- Canonical accept + advance. Frozen Core only.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/screening-package-120"
VALIDATION_REL = f"{EDIR}/validation"
CURR_ACC = "0b09cde03485a852df7ca5ff84b7eff768ecc0efae9c3615ea2662f71dc4d6bf"

NEW_DECISIONS = [
    {"discovery_id": "VM-D113", "decision": "KEEP",
     "reason": ("Meta DINOv3 2025-08-13 (pre-cutoff official paper + pages + code): 7B SSL on "
                "LVD-1689M with Gram-anchored dense refinement under long training; frozen reusable "
                "dense representation; P06 load-bearing transition; non-duplicate of DINOv2 "
                "(Gram phase is the transition); open research paper, no vendor ceilings."),
     "scope_tags": ["VM-O06"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (Gram/objective/numbers)"],
     "confidence": "high"},
    {"discovery_id": "VM-D114", "decision": "KEEP",
     "reason": ("SigLIP 2 2025-02-20 (pre-cutoff paper + Big Vision release): staged sigmoid + "
                "captioning + self-distillation + masked-prediction + curation recipe with "
                "multilingual/debiased mixture and native-aspect/multi-resolution; P06/P07 "
                "alignment and localization transfer; non-duplicate of SigLIP (recipe transition); "
                "open paper, no vendor ceilings."),
     "scope_tags": ["VM-O06", "VM-O07"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (recipe/objective/numbers)"],
     "confidence": "high"},
    {"discovery_id": "VM-D115", "decision": "KEEP",
     "reason": ("Meta SAM 3 2025-11-19/20 (pre-cutoff pages + paper + code): promptable concept "
                "segmentation (text-NP/exemplar/visual prompts; detector + memory tracker; shared "
                "backbone); P03/P07B/P11 late convergence node; non-duplicate of SAM 2 (concept "
                "interface is the transition); SAM 3D excluded; SAM 3.1 successor-context only."),
     "scope_tags": ["VM-O03", "VM-O08"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (contract/mechanism/numbers)"],
     "confidence": "high"},
    {"discovery_id": "VM-D116", "decision": "KEEP",
     "reason": ("Physical Intelligence pi-zero 2024-10-31 (pre-cutoff paper + official pages): "
                "flow-matching continuous action expert on PaliGemma VLM with dexterous multi-robot "
                "regime; discrete-token vs flow-matching interface transition vs RT-2/OpenVLA; P13 "
                "primary transition; no robotics-control survey expansion."),
     "scope_tags": ["VM-O14"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (topology/data/numbers)"],
     "confidence": "high"},
    {"discovery_id": "VM-D117", "decision": "KEEP",
     "reason": ("FAST 2025-01-16 (pre-cutoff paper): DCT frequency-space action tokenization with "
                "chunk compression and FAST+ universal scope; action representation/tokenization "
                "transition (not a general VLA system); kept separate from pi-zero; P13 transition."),
     "scope_tags": ["VM-O14"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (representation/numbers)"],
     "confidence": "high"},
    {"discovery_id": "VM-D118", "decision": "KEEP",
     "reason": ("Apple AIMv2 2024-11-21 (pre-cutoff paper, CVPR 2025 Highlight): autoregressive "
                "prefix-ViT plus causal multimodal decoder; objective family distinct from "
                "masked/contrastive/distillation; P06 supporting objective variant."),
     "scope_tags": ["VM-O06"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage verification of objective/transfer claims"],
     "confidence": "medium"},
    {"discovery_id": "VM-D119", "decision": "KEEP",
     "reason": ("UGround 2024-10-07 (pre-cutoff paper, ICLR 2025 Oral): universal screenshot grounder "
                "from web-synthetic recipe; vision-only pixel-action interface break (SeeAct-V folded "
                "as interface context, not a separate node); P12/P08 grounding relevance."),
     "scope_tags": ["VM-O13", "VM-O08"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage verification of grounding/interface claims"],
     "confidence": "medium"},
    {"discovery_id": "VM-D120", "decision": "KEEP",
     "reason": ("ScreenSpot-Pro 2025 (pre-cutoff paper, ACM MM 2025): professional high-resolution "
                "grounding evaluation plus planner-guided cascaded search contract (ScreenSeekeR "
                "folded in-card); P12 evaluation-methodology anchor; distinct from OSWorld task "
                "bench and ScreenSpot-v2 bug-fix."),
     "scope_tags": ["VM-O13"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage verification of evaluation-contract claims"],
     "confidence": "medium"},
]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State at DISCOVERY_COLLECTED")
    impl = core.repository_commit_sha(root)
    for dec in NEW_DECISIONS:
        assert screening.validate_decision(dec) == [], dec["discovery_id"]
    by_new = {d["discovery_id"]: d for d in NEW_DECISIONS}

    with agent_tool.current_stage_basis_override():
        pkg_path = screening.prepare_package(
            root, root / STATE_REL, root / DISC_REL, root / PKGDIR, impl)
        package = core.load_json(pkg_path)
        assert package["input"]["record_count"] == 120, package["input"]

        carried = {}
        r1dir = root / SRC / "screening/v2/accepted" / CURR_ACC / "results"
        for res in sorted(r1dir.glob("batch-*.json")):
            for dec in core.load_json(res)["decisions"]:
                assert dec["discovery_id"] not in carried
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 112 and not any(
            d in carried for d in by_new), len(carried)

        results_dir = root / EDIR / "screening-results-120"
        results_dir.mkdir(parents=True, exist_ok=True)
        total = 0
        for b in package["input"]["batches"]:
            recs = screening.read_jsonl(root / PKGDIR / b["path"])
            ids = [r["discovery_id"] for r in recs]
            decs = [by_new[did] if did in by_new else carried[did] for did in ids]
            total += len(decs)
            core.write_json(results_dir / f"{b['batch_id']}.json", {
                "schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
                "batch_id": b["batch_id"],
                "basis": screening.expected_result_basis(
                    Path("."), root / PKGDIR / "package.json", package, b),
                "decisions": decs})
        assert total == 120, total

        acceptance_path = screening.accept_results(
            root, root / PKGDIR / "package.json", results_dir,
            root / f"{SRC}/screening/v2/accepted", impl)
        acceptance = screening.validate_acceptance(root, acceptance_path, impl)
        assert acceptance["record_count"] == 120
        counts = {}
        for d in acceptance["decisions"]:
            counts[d["decision"]] = counts.get(d["decision"], 0) + 1
        print("screening acceptance:", acceptance_path.relative_to(root), counts)

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "screening-stage-validation-120.json"
        reviews_path = vdir / "screening-stage-reviews-120.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Screening stage-contract validation passed over canonical 120-record "
                         "acceptance (112 carried + 8 late-cutoff KEEP per formal evaluation). "
                         "Machine validation only; Sol review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening complete over 120-record canonical Discovery (112 carried + "
             "8 KEEP: DINOv3/SigLIP 2/SAM 3/pi-zero/FAST/AIMv2/UGround/ScreenSpot-Pro, "
             "each cutoff-verified and non-duplicate). Proceed to Evidence; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "CANDIDATES_NORMALIZED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
