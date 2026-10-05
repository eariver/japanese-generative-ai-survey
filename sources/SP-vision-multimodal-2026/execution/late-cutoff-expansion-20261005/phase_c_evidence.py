#!/usr/bin/env python3
"""TS-003 Phase C (late-cutoff expansion): Evidence (120) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package with union supplement (VM-D112 + VM-D077 +
  VM-D074 + VM-D075 + VM-D074-history entries).
- Cards: 111 carried byte-identical (basis rebind) + 8 NEW (DINOv3/SigLIP 2/SAM 3/
  pi-zero/FAST/AIMv2/UGround/ScreenSpot-Pro, primary-grounded) + VM-D074 claim-3
  era-separation reword (license conclusion unchanged).
- Canonical accept (append-only). Frozen Core only.
"""
from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-120"
CURR = "446f359c726546411244389d66c60dd5037d9d16a671cb5842accc02a10fa2da"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
TID074 = "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c"
NOW = "2026-10-05T00:00:00Z"

SUPS = [
    f"{SRC}/execution/architecture-r3-intake-20261003/evidence-authority-supplement-112.json",
    f"{SRC}/execution/vm-d077-authority-repair-20261004/evidence-authority-supplement-vm-d077.json",
    f"{SRC}/execution/license-authority-repair-r5-20261004/evidence-authority-supplement-vm-d074.json",
    f"{SRC}/execution/license-authority-repair-r5-20261004/evidence-authority-supplement-vm-d075.json",
    f"{EDIR}/evidence-authority-supplement-vm-d074-history.json",
]
UNION = f"{EDIR}/evidence-authority-supplement-union-120.json"
UNION_ID = "ts003-late-cutoff-supplement-union-20261005"

D074_HIST_IDS = []  # filled at runtime from history manifest


def _screening_acceptance(root: Path) -> Path:
    cands = [p for p in sorted((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"))
             if core.load_json(p)["record_count"] == 120]
    assert len(cands) == 1, [str(p) for p in cands]
    return cands[0]


def _card_base(issue, tid, subj, name, url, pub_date, observed="2026-10-05T00:00:00Z"):
    return {
        "schema_version": "2.0-rc1", "issue_id": issue, "evidence_task_id": tid,
        "basis": {}, "status": "VERIFIED",
        "entities": [{"entity_id": subj, "canonical_name": name, "entity_type": "MODEL",
                      "organization": None, "canonical_url": url}],
        "artifact": {"primary_subject_id": subj, "artifact_type": "PAPER",
                     "canonical_name": name, "canonical_url": url},
        "temporal": {"observed_at": observed, "events": [{
            "event_id": "event-1", "event_type": "SOURCE_PUBLICATION_OR_RELEASE",
            "event_date": pub_date, "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
            "source_ids": ["src-1"]}]},
        "sources": [], "claims": [], "metrics": [], "limitations": [],
        "verification": {"targets": [], "unresolved_questions": [], "contradictions": []},
    }


def _src(url, cls, title, pub, role="Discovery-bounded source used for factual verification"):
    return {"source_id": "src-1", "url": url, "source_class": cls, "title": title,
            "published_at": pub, "accessed_at": NOW, "role": role}


def _claim(sid_, text, subj, cls, sids, ctx):
    assert len(text) <= 600, (sid_, len(text))
    return {"statement_id": sid_, "text": text, "subject_id": subj,
            "subject_role": "PRIMARY_SUBJECT", "evidence_class": cls,
            "source_ids": sids, "context": ctx}


def _lim(sid_, text, subj, cls="AUTHOR_CLAIM"):
    return {"statement_id": sid_, "text": text, "subject_id": subj,
            "subject_role": "PRIMARY_SUBJECT", "evidence_class": cls,
            "source_ids": ["src-1"],
            "context": "Evidence boundary retained for downstream editorial use."}


NEW_CARDS = {}


def _build_new_cards():
    s = "ev-vmd113"
    c = _card_base(ISSUE_ID, "TBD", s, "DINOv3 (Meta AI, 2025)", "https://arxiv.org/abs/2508.10104", "2025-08")
    c["sources"] = [_src("https://arxiv.org/abs/2508.10104", "PRIMARY_PAPER", "DINOv3 (Meta AI, 2025)", "2025-08")]
    c["claims"] = [
        _claim("claim-1", "7B self-supervised vision model on LVD-1689M (1,689M hierarchical sampling); objective L_Pre = L_DINO + L_iBOT + 0.1*L_DKoleo with Sinkhorn-Knopp replacing centering, axial RoPE, constant schedule over 1M iterations.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §3 (data/scale/objective/architecture)."),
        _claim("claim-2", "Dense feature maps degrade under long training (VOC mIoU peaks ~200k then declines); fixed by Gram anchoring against an early Gram-teacher, preserving patch consistency without pinning features.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §3.2/§4.1-4.3 (degradation diagnosis + Gram refinement)."),
        _claim("claim-3", "Post-hoc adaptation without retraining: resolution scaling, multi-student distillation to ViT-S/B/L/H+ and ConvNeXt, plus dino.txt LiT-style text alignment on frozen vision.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §5 (adaptation suite)."),
        _claim("claim-4", "Inherits DINOv2 DINO+iBOT/multi-crop/Koleo/registers; changes scale, RoPE, Sinkhorn, Gram phase. Frozen reusable dense representation reaching task SOTA without fine-tuning.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §1/§6-8 (lineage + frozen-backbone results)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Training compute/carbon cost; fairness gaps vs DINOv2 narrowed but present; OCR-heavy content hard for SSL; intermediate-layer use ill-conditioned without normalization.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "DINOv3 paper body consumed via arXiv HTML: objective/scale, Gram refinement, adaptation suite, frozen results verified.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D113"] = c

    s = "ev-vmd114"
    c = _card_base(ISSUE_ID, "TBD", s, "SigLIP 2 (Zhai et al., 2025)", "https://arxiv.org/abs/2502.14786", "2025-02")
    c["sources"] = [_src("https://arxiv.org/abs/2502.14786", "PRIMARY_PAPER", "SigLIP 2 (Zhai et al., 2025)", "2025-02")]
    c["claims"] = [
        _claim("claim-1", "Keeps SigLIP sigmoid per-pair loss; staged recipe adds captioning decoder (LocCa), self-distillation (SILC local-to-global) and masked prediction (TIPS/DINO-line) with online data curation.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §1/§2.2/§2.3/§2.5 (staged recipe)."),
        _claim("claim-2", "Multilingual WebLI mixture (109 langs) with de-bias filtering; native aspect ratio and multi-resolution training (NaFlex); gains attributed to recipe combination, not a new loss.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §2.1/§2.4/§5 (data + resolution + conclusion)."),
        _claim("claim-3", "Localization and dense transfer: RefCOCO grounding, OWL-ViT open-vocabulary detection and dense probes improve over SigLIP; frozen-encoder VLM transfer gains in PaliGemma-style setups.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §3.2-3.4 (localization/detection/VLM transfer)."),
    ]
    c["limitations"] = [_lim("limitation-1", "NaFlex omits self-distillation/masked losses and extrapolates poorly; RefCOCO still below English-only LocCa (multilingual tradeoff); small-model gains depend on distillation stage.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "SigLIP 2 paper body consumed via arXiv HTML: recipe, data, resolution, localization and VLM transfer verified.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D114"] = c

    s = "ev-vmd115"
    c = _card_base(ISSUE_ID, "TBD", s, "SAM 3: Segment Anything with Concepts (Meta, 2025)", "https://arxiv.org/abs/2511.16719", "2025-11")
    c["sources"] = [_src("https://arxiv.org/abs/2511.16719", "PRIMARY_PAPER", "SAM 3 (Meta Superintelligence Labs, 2025)", "2025-11")]
    c["claims"] = [
        _claim("claim-1", "Promptable Concept Segmentation contract: detect, segment and track all instances of a visual concept in image or short video, returning masks plus unique identities.", s, "AUTHOR_CLAIM", ["src-1"], "Paper Abstract/§2 (PCS definition)."),
        _claim("claim-2", "Prompts are simple text noun phrases, image exemplars (positive/negative boxes) and SAM 2-style visual clicks; DETR-paradigm image detector plus memory-based video tracker share one Perception Encoder; presence-token decoupling separates recognition from localization.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §3 (prompts/detector/tracker/backbone/decoupling)."),
        _claim("claim-3", "Inherits SAM/SAM2 point-visual prompting and memory machinery; novelty is the language-grounded concept interface over image+video data scale. SAM 3D excluded; SAM 3.1 is successor context only.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §1/§5/§7 (lineage + data + related work)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Fine-grained out-of-domain zero-shot weak; simple noun phrases only (no long referring queries); video cost linear in object count.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "SAM 3 paper body consumed via arXiv HTML: PCS contract, prompts, detector/tracker, lineage and limits verified.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D115"] = c

    s = "ev-vmd116"
    c = _card_base(ISSUE_ID, "TBD", s, "pi-zero (Physical Intelligence, 2024)", "https://arxiv.org/abs/2410.24164", "2024-10")
    c["sources"] = [_src("https://arxiv.org/abs/2410.24164", "PRIMARY_PAPER", "pi-zero (Physical Intelligence, 2024)", "2024-10")]
    c["claims"] = [
        _claim("claim-1", "Pretrained PaliGemma VLM backbone (3B) plus 300M flow-matching action expert; continuous 50Hz 50-step action chunks for dexterous contact tasks.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §III/§IV (backbone + flow-matching contract)."),
        _claim("claim-2", "Multi-robot dexterous data regime (10,000+ hours, 903M timesteps, 7 configs/68 tasks, OXE/Bridge/DROID mixture); fine-tune from hours to 100+ hours per task family.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §V (data regime + recipe)."),
        _claim("claim-3", "Discrete language-like action tokens (RT-2/OpenVLA style) vs continuous flow-matching generation: binning suffices for simple tasks but breaks down at precision/high-frequency dexterity.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §II/§VI (interface contrast + evaluations)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Prototype scope; hardest/longest tasks need fine-tuning plus a high-level language planner; scale/hardware sensitivity and inference cost retained.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "pi-zero paper body consumed via arXiv HTML: topology, data regime, interface contrast and limits verified.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D116"] = c

    s = "ev-vmd117"
    c = _card_base(ISSUE_ID, "TBD", s, "FAST (Pertsch et al., 2025)", "https://arxiv.org/abs/2501.09747", "2025-01")
    c["sources"] = [_src("https://arxiv.org/abs/2501.09747", "PRIMARY_PAPER", "FAST (Pertsch et al., 2025)", "2025-01")]
    c["claims"] = [
        _claim("claim-1", "Per-dimension/per-timestep discretization fails on high-frequency actions (next-token loss trivialized); DCT frequency-space representation with quantile norm, gamma scaling and BPE-1024 tokens is fully invertible with two hyperparameters.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §III-V (failure diagnosis + DCT/BPE construction)."),
        _claim("claim-2", "Action-chunk compression up to 13.2x at 50Hz with ~30 tokens per arm per chunk; FAST+ universal tokenizer over ~1M chunks across embodiments; pi-zero/OpenVLA backbones supported.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §VI-A/C (compression + FAST+ scope)."),
        _claim("claim-3", "Autoregressive vs flow trade-off: matched diffusion performance with 5x fewer GPU-hours and better language following, but ~750ms AR inference vs 100ms diffusion per chunk; pi-zero-FAST swaps the head on the same backbone.", s, "AUTHOR_CLAIM", ["src-1"], "Paper §VI-E/F/§VII (trade-off + pi-zero-FAST)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Policy evaluation on static manipulators only; alternative compressions and FAST+diffusion untested; inference-speed gap unresolved.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "FAST paper body consumed via arXiv HTML: representation, compression, FAST+ scope and trade-offs verified.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D117"] = c

    s = "ev-vmd118"
    c = _card_base(ISSUE_ID, "TBD", s, "AIMv2 (Apple, 2024)", "https://arxiv.org/abs/2411.14402", "2024-11")
    c["sources"] = [_src("https://arxiv.org/abs/2411.14402", "PRIMARY_PAPER", "AIMv2 (Apple, 2024)", "2024-11")]
    c["claims"] = [
        _claim("claim-1", "Autoregressive prefix-ViT plus causal multimodal decoder generating raw patches then text tokens; dense per-token signal without large-batch contrastive training.", s, "AUTHOR_CLAIM", ["src-1"], "Paper objective (residual-sweep admission)."),
        _claim("claim-2", "Frozen-trunk transfer competitive with masked/contrastive/distillation families; CVPR 2025 Highlight.", s, "AUTHOR_CLAIM", ["src-1"], "Paper transfer results."),
    ]
    c["limitations"] = [_lim("limitation-1", "Single-paper scope; scaling/robustness beyond reported conditions unbound.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage verification", "status": "VERIFIED", "finding": "AIMv2 objective and transfer claims verified against the bound paper locator.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D118"] = c

    s = "ev-vmd119"
    c = _card_base(ISSUE_ID, "TBD", s, "UGround (2024)", "https://arxiv.org/abs/2410.05243", "2024-10")
    c["sources"] = [_src("https://arxiv.org/abs/2410.05243", "PRIMARY_PAPER", "UGround (2024)", "2024-10")]
    c["claims"] = [
        _claim("claim-1", "Universal screenshot grounder trained on a 10M-element web-synthetic grounding recipe (1.3M screenshots).", s, "AUTHOR_CLAIM", ["src-1"], "Paper data recipe (residual-sweep admission)."),
        _claim("claim-2", "Vision-only screenshot plus pixel-action interface break over accessibility-tree/DOM tooling (SeeAct-V folded here as interface context, not a separate node).", s, "INFERENCE", ["src-1"], "Edition interface-contract reading over the paper."),
    ]
    c["limitations"] = [_lim("limitation-1", "Web-synthetic domain limits; live-OS long-horizon state needs OSWorld-side sources.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage verification", "status": "VERIFIED", "finding": "UGround recipe and interface claims verified against the bound paper locator.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D119"] = c

    s = "ev-vmd120"
    c = _card_base(ISSUE_ID, "TBD", s, "ScreenSpot-Pro (2025)", "https://arxiv.org/abs/2504.07981", "2025-04")
    c["sources"] = [_src("https://arxiv.org/abs/2504.07981", "PRIMARY_PAPER", "ScreenSpot-Pro (2025)", "2025-04")]
    c["claims"] = [
        _claim("claim-1", "Professional high-resolution grounding evaluation: full-screen tasks with tiny targets (0.07% area regime), distinct from cropped easy grounding.", s, "AUTHOR_CLAIM", ["src-1"], "Paper evaluation regime (residual-sweep admission)."),
        _claim("claim-2", "Planner-guided cascaded inference-time search contract (ScreenSeekeR folded here as method context, not a separate node).", s, "INFERENCE", ["src-1"], "Edition method-contract reading over the paper."),
    ]
    c["limitations"] = [_lim("limitation-1", "Evaluation-only scope; agent policy claims need OSWorld-side sources.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage verification", "status": "VERIFIED", "finding": "ScreenSpot-Pro regime and search-contract claims verified against the bound paper locator.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D120"] = c


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    impl = core.repository_commit_sha(root)
    _build_new_cards()

    with agent_tool.current_stage_basis_override():
        scr_acc_path = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                           key=lambda p: p.stat().st_mtime)
        scr_acc = core.load_json(scr_acc_path)
        assert scr_acc["record_count"] == 120, scr_acc["record_count"]
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        # Union manifest (idempotent builder).
        import sys as _sys
        _sys.path.insert(0, str(root / EDIR))
        import build_union as _bu
        union_out = _bu.build_union(root)

        import build_package as _bp
        package_path, package = _bp.build_package(root)
        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]
        by_task = {m["evidence_task_id"]: m for m in package["tasks"]}
        by_disc = {}
        for r in core.load_json(root / SRC / "candidate-matrix-v2.json")["rows"] \
                if (root / SRC / "candidate-matrix-v2.json").exists() else []:
            for d in r.get("discovery_ids", []):
                by_disc[d] = r["evidence_task_id"]
        # task ids for the 8 new discoveries via stable ids
        new_ids = {}
        for did in ("VM-D113", "VM-D114", "VM-D115", "VM-D116", "VM-D117", "VM-D118", "VM-D119", "VM-D120"):
            tid = evidence.stable_task_id(ISSUE_ID, did)
            assert tid in by_task, did
            new_ids[did] = tid

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, added, fixed = 0, [], []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] in new_ids.values():
                    did = next(d for d, t in new_ids.items() if t == meta["evidence_task_id"])
                    card = copy.deepcopy(NEW_CARDS[did])
                    card["evidence_task_id"] = meta["evidence_task_id"]
                    card["basis"] = {
                        "task_sha256": meta["sha256"],
                        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                        "prompt_sha256": PROMPT_SHA,
                        "result_contract_sha256": CONTRACT_SHA,
                    }
                    errs = evidence.validate_evidence_card(
                        card, task, meta["sha256"], package, repo_root=root)
                    assert not errs, (did, errs)
                    added.append(did)
                elif meta["evidence_task_id"] == "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c":
                    # VM-D074: start from the license-run staged card (code + weights authority),
                    # then apply the §11 era-separation reword to claim-3 (predecessor history vs
                    # Qwen3-VL-era trees) + register the history supplement sources.
                    staged074 = core.load_json(root / EDIR / "staged-vm-d074-merged.json")
                    card = copy.deepcopy(staged074)
                    card["basis"] = {
                        "task_sha256": meta["sha256"],
                        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                        "prompt_sha256": PROMPT_SHA,
                        "result_contract_sha256": CONTRACT_SHA,
                    }
                    errs = evidence.validate_evidence_card(
                        card, task, meta["sha256"], package, repo_root=root)
                    assert not errs, errs
                    fixed.append("VM-D074")
                elif meta["evidence_task_id"] == "evidence:SP-vision-multimodal-2026:4b007409a575a02d":
                    # VM-D075: staged omni-license card (code + weights resolved buckets;
                    # limitation-2 removed as resolved).
                    staged075 = core.load_json(root / EDIR / "staged-vm-d075-license.json")
                    card = copy.deepcopy(staged075)
                    card["basis"] = {
                        "task_sha256": meta["sha256"],
                        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                        "prompt_sha256": PROMPT_SHA,
                        "result_contract_sha256": CONTRACT_SHA,
                    }
                    errs = evidence.validate_evidence_card(
                        card, task, meta["sha256"], package, repo_root=root)
                    assert not errs, errs
                    fixed.append("VM-D075")
                else:
                    base = core.load_json(root / CURR_RES / fname)
                    base["basis"]["task_sha256"] = meta["sha256"]
                    base["basis"]["screening_acceptance_sha256"] = core.sha256_file(scr_acc_path)
                    assert base["basis"]["prompt_sha256"] == PROMPT_SHA, meta["evidence_task_id"]
                    assert base["basis"]["result_contract_sha256"] == CONTRACT_SHA
                    errs = evidence.validate_evidence_card(
                        base, task, meta["sha256"], package, repo_root=root)
                    if errs:
                        raise ValueError(f"Card {meta['evidence_task_id']} invalid: {'; '.join(errs)}")
                    card = base
                    carried += 1
                core.write_json(results_dir / fname, card)
            assert carried == 110 and len(added) == 8 and fixed == ["VM-D074", "VM-D075"], (carried, added, fixed)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 120
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| added:", len(added), "| fixed:", fixed)
    print("EVIDENCE REPLAY COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
