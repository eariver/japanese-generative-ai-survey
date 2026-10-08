#!/usr/bin/env python3
"""TS-003 Phase C (P02 bounded bridge intake): Evidence (124) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package over Discovery (125) + Screening (125) +
  carried r6final authority supplement (23 entries; unchanged binding scope).
- Cards: 121 carried (deterministic basis rebind, byte-identical) + 3 NEW
  (VM-D123 Deformable DETR; VM-D124 DAB-DETR; VM-D125 DN-DETR), each authored
  from consumed primary bodies and canonical-validated here.
- DINO card NOT recollected (intact carry); re-read recorded in the Sol
  authority-consumption review.
- Canonical accept (append-only). Frozen Core only. No state advance here.
"""
from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-124"
UNION = f"{EDIR}/evidence-authority-supplement-union-125.json"
CURR = "1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
NOW = "2026-10-08T00:00:00Z"


def _card_base(tid, subj, name, url, pub_date):
    return {
        "schema_version": "2.0-rc1", "issue_id": ISSUE_ID, "evidence_task_id": tid,
        "basis": {}, "status": "VERIFIED",
        "entities": [{"entity_id": subj, "canonical_name": name, "entity_type": "MODEL",
                       "organization": None, "canonical_url": url}],
        "artifact": {"primary_subject_id": subj, "artifact_type": "PAPER",
                     "canonical_name": name, "canonical_url": url},
        "temporal": {"observed_at": NOW, "events": [{
            "event_id": "event-1", "event_type": "SOURCE_PUBLICATION_OR_RELEASE",
            "event_date": pub_date, "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
            "source_ids": ["src-1"]}]},
        "sources": [], "claims": [], "metrics": [], "limitations": [],
        "verification": {"targets": [], "unresolved_questions": [], "contradictions": []},
    }


def _src(url, title, pub):
    return {"source_id": "src-1", "url": url, "source_class": "PRIMARY_PAPER",
            "title": title, "published_at": pub, "accessed_at": NOW,
            "role": "Discovery-bounded source used for factual verification"}


def _claim(sid_, text, subj, cls, ctx):
    assert len(text) <= 600, (sid_, len(text))
    return {"statement_id": sid_, "text": text, "subject_id": subj,
            "subject_role": "PRIMARY_SUBJECT", "evidence_class": cls,
            "source_ids": ["src-1"], "context": ctx}


def _lim(sid_, text, subj):
    return {"statement_id": sid_, "text": text, "subject_id": subj,
            "subject_role": "PRIMARY_SUBJECT", "evidence_class": "AUTHOR_CLAIM",
            "source_ids": ["src-1"],
            "context": "Evidence boundary retained for downstream editorial use."}


NEW_CARDS = {}


def _build_new_cards():
    s = "ev-vmd123"
    c = _card_base("", s, "Deformable DETR (Zhu et al., 2020)",
                   "https://arxiv.org/abs/2010.04159", "2020-10")
    c["sources"] = [_src("https://arxiv.org/abs/2010.04159",
                          "Deformable DETR: Deformable Transformers for End-to-End Object Detection", "2020-10")]
    c["claims"] = [
        _claim("claim-1", "DETR motivation repair: slow convergence and limited feature spatial resolution from Transformer attention limits on image feature maps; deformable attention attends only a small set of key sampling points around a reference point.", s, "AUTHOR_CLAIM", "Paper abstract/§1/§4 (motivation + deformable attention mechanism)."),
        _claim("claim-2", "Multi-scale handling without FPN help (small objects from high-resolution maps); 10x fewer training epochs than DETR with better performance especially on small objects; COCO benchmark; code released; ICLR 2021 Oral.", s, "AUTHOR_CLAIM", "Paper abstract/§4-5 (multi-scale design + COCO convergence/small-object results)."),
        _claim("claim-3", "Reference-point/query machinery (2D reference points as queries; two-stage query-selection variant; iterative box refinement) feeds later DETR-family development including DN/DAB/DINO query-selection use.", s, "AUTHOR_CLAIM", "Paper §4 + DINO related-work build-on statement (query-selection adoption)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Single-scale vs multi-scale variant scope; two-stage query-selection and iterative refinement are optional extensions; FPN-general survey stays outside this bridge role.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "Deformable DETR body consumed via arXiv HTML: motivation, deformable attention mechanism, multi-scale handling, convergence and small-object results verified as the P02 bridge.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D123"] = c

    s = "ev-vmd124"
    c = _card_base("", s, "DAB-DETR (Liu et al., 2022)",
                   "https://arxiv.org/abs/2201.12329", "2022-01")
    c["sources"] = [_src("https://arxiv.org/abs/2201.12329",
                          "DAB-DETR: Dynamic Anchor Boxes are Better Queries for DETR", "2022-01")]
    c["claims"] = [
        _claim("claim-1", "Decoder queries directly formulated as 4D box coordinates (x, y, w, h) with layer-by-layer dynamic anchor updates; explicit positional priors improve query-to-feature similarity and convergence; width/height modulate positional attention.", s, "AUTHOR_CLAIM", "Paper abstract/§3 (dynamic anchor-box query formulation)."),
        _claim("claim-2", "Queries read as layer-by-layer cascade soft ROI pooling; 45.7 AP on COCO with ResNet50-DC5 at 50 epochs (best among DETR-like under same setting); code released; ICLR 2022.", s, "AUTHOR_CLAIM", "Paper abstract/§4-5 (cascade reading + COCO results)."),
        _claim("claim-3", "4D anchor-box query formulation directly feeds DINO anchor-query design (DINO refines dynamic anchor boxes step-by-step across decoder layers following DAB-DETR).", s, "AUTHOR_CLAIM", "DINO §§1/3 build-on statement (dynamic anchor-box adoption)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Single-scale DETR-baseline scope; Anchor/Conditional DETR taxonomy stays outside; brief supporting treatment only.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "DAB-DETR abstract/body consumed: dynamic anchor-box formulation, layer-wise updates, COCO result verified as the P02 supporting bridge.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D124"] = c

    s = "ev-vmd125"
    c = _card_base("", s, "DN-DETR (Li et al., 2022)",
                   "https://arxiv.org/abs/2203.01305", "2022-03")
    c["sources"] = [_src("https://arxiv.org/abs/2203.01305",
                          "DN-DETR: Accelerate DETR Training by Introducing Query DeNoising", "2022-03")]
    c["claims"] = [
        _claim("claim-1", "Slow convergence diagnosed as bipartite-graph-matching instability (inconsistent early optimization goals); noised GT boxes and labels fed to the decoder as a denoising part alongside the matching part; reconstruction of original targets; attention mask blocks leakage.", s, "AUTHOR_CLAIM", "Paper abstract/§§3-4 (instability diagnosis + denoising mechanism)."),
        _claim("claim-2", "Built on DAB-DETR 4D-anchor formulation (decoder embedding as label embedding for box+label denoising); +1.9 AP over DAB-DETR same setting (43.4/48.6 AP R50 at 12/50 epochs); parity at ~50% epochs; also applied to Deformable DETR, Anchor DETR, Faster R-CNN, Mask2Former; CVPR 2022 Oral.", s, "AUTHOR_CLAIM", "Paper abstract/§§4-6 (DAB-based evaluation + generality results)."),
        _claim("claim-3", "Denoising-training branch directly feeds DINO contrastive denoising (DINO improves DN-style denoising and reports +6.0/+2.7 AP over DN-DETR at 12/24 epochs).", s, "AUTHOR_CLAIM", "DINO abstract (DN-DETR as previous best + improvement margin)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Uniform-distribution noise sampling only; query-denoising training, not diffusion-model denoising; transition-node treatment only.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "DN-DETR abstract/body consumed via CVPR open access: instability diagnosis, denoising mechanism, DAB-based results and generality verified as the P02 bridge.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D125"] = c


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
        assert scr_acc["record_count"] == 125, scr_acc["record_count"]
        assert {d["discovery_id"]: d["decision"] for d in scr_acc["decisions"]}["VM-D122"] == "DROP"
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        supplement_path = root / UNION
        evidence.validate_evidence_authority_supplement(
            root, supplement_path, impl, expected_issue_id=ISSUE_ID,
            expected_discovery_path=root / DISC_REL,
            expected_screening_acceptance_path=scr_acc_path)
        sup = core.load_json(supplement_path)
        assert len(sup["sources"]) == 23, len(sup["sources"])
        print("supplement: union-125 (23 carried r6final sources, rebound basis)")

        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, supplement_path)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 121 + 3, len(package["tasks"])

        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]
        by_task = {m["evidence_task_id"]: m for m in package["tasks"]}
        new_ids = {}
        for did in ("VM-D123", "VM-D124", "VM-D125"):
            tid = evidence.stable_task_id(ISSUE_ID, did)
            assert tid in by_task, did
            new_ids[did] = tid

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, added = 0, []
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
            assert carried == 121 and len(added) == 3, (carried, added)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 124
        statuses = {}
        for r in evidence_acceptance["results"]:
            statuses[r["status"]] = statuses.get(r["status"], 0) + 1
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| added:", added, "| statuses:", statuses)
        assert statuses.get("VERIFIED", 0) >= 116 + 3, statuses
        (root / EDIR / "evidence-replay-report.json").write_text(json.dumps(
            {"acceptance": str(evidence_acceptance_path.relative_to(root)),
             "result_count": 124, "statuses": statuses,
             "carried_byte_identical": carried, "added": sorted(added),
             "supplement": str(supplement_path.relative_to(root))},
            ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("EVIDENCE COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
