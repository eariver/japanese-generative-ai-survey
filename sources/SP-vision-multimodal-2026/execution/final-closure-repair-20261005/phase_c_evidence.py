#!/usr/bin/env python3
"""TS-003 Phase C (final closure): Evidence (122) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package (no supplement needed: both new cards cite
  Discovery-bounded src-1 paper locators only).
- Cards: 120 carried (deterministic basis rebind) + 2 NEW (VM-D121 V-JEPA 2/2-AC
  two-stage contract; VM-D122 planning-limits methodology).
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

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/final-closure-repair-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-122"
UNION = f"{EDIR}/evidence-authority-supplement-union-122.json"
CURR = "3cd37179fe5c5a70d549dfabc9399864dea6a49ce79f1e85dcafd086ac61d412"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
NOW = "2026-10-05T00:00:00Z"


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
    s = "ev-vmd121"
    c = _card_base("", s, "V-JEPA 2 / V-JEPA 2-AC (Meta, 2025)",
                   "https://arxiv.org/abs/2506.09985", "2025-06")
    c["sources"] = [_src("https://arxiv.org/abs/2506.09985",
                          "V-JEPA 2 / V-JEPA 2-AC (Meta, 2025)", "2025-06")]
    c["claims"] = [
        _claim("claim-1", "Stage-1 V-JEPA 2 action-free JEPA pretraining: mask-denoising in representation space with EMA teacher on 1M+ hours video (VideoMix22M); ViT-L 300M to ViT-g 1B encoders with fixed ViT-s predictor.", s, "AUTHOR_CLAIM", "Paper §2 (objective/architecture/data/scale)."),
        _claim("claim-2", "Stage-2 V-JEPA 2-AC frozen-encoder action-conditioned predictor (~300M block-causal) trained on 62h unlabeled DROID; image-goal planning by MPC energy minimization with CEM receding-horizon control; zero-shot Franka deployment.", s, "AUTHOR_CLAIM", "Paper §3-4 (AC training + MPC planning + robot deployment)."),
        _claim("claim-3", "Inherits V-JEPA mask-predict/EMA/frozen-probe protocol; new: 3D-RoPE stability, data/model scale, AC post-training plus planning use, and LLM alignment for VideoQA.", s, "AUTHOR_CLAIM", "Paper §2/§5/§7-8 (inheritance + novelty)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Camera-position sensitivity from RGB-only inference; long-horizon rollout error accumulation needing subgoals; image goals only (language future); kitchen closed-vocab prediction scope.", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "V-JEPA 2 paper body consumed via arXiv HTML: two-stage contract, MPC planning, VideoQA alignment and limits verified as one contract.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D121"] = c

    s = "ev-vmd122"
    c = _card_base("", s, "The Planning Limits of Latent World Models (2026)",
                   "https://arxiv.org/abs/2609.39235", "2026-09")
    c["sources"] = [_src("https://arxiv.org/abs/2609.39235",
                          "The Planning Limits of Latent World Models (2026-09-30)", "2026-09")]
    c["claims"] = [
        _claim("claim-1", "Cross-backbone action-conditioned predictor evaluation (V-JEPA 2/2.1, VideoMAEv2, VideoPrism, DINOv2) with plannable-range metric P*: reliable only 5-10 steps vs 16-53 needed; V-JEPA 2.1 most consistent.", s, "AUTHOR_CLAIM", "Paper §3-4 + Fig.2-3 (metric + cross-backbone result)."),
        _claim("claim-2", "Predictor scaling non-result (81x larger predicts better, plans no further); perfect-prediction limit via simulator reference (92% at L=5 to 41% at L=20): closeness-score weakness, not predictor error.", s, "AUTHOR_CLAIM", "Paper §5.1/§5.5 + App (scaling + exact-dynamics reference)."),
        _claim("claim-3", "Imagination/MPC/subgoal matrix: pure K=5 23%, K=30 36%, MPC K=30 52%, expert subgoals 76%; VLA candidate-action ranking with π₀ 65% to 77%; sim plus BridgeData offline coverage (offline only, not control).", s, "AUTHOR_CLAIM", "Paper §6-7 + App (matrix + VLA ranking + offline scope)."),
    ]
    c["limitations"] = [_lim("limitation-1", "Single-arm closed-loop scope enabling exact-dynamics swap; paired-episode tests mostly one seed; K ranges are lower bounds; subgoals from same-episode expert (generation without expert is next step).", s)]
    c["verification"]["targets"] = [{"target": "Evidence-stage full-body verification", "status": "VERIFIED", "finding": "Planning-limits paper body consumed via arXiv HTML: metric, horizon/scaling limits, comparison matrix and scope verified.", "subject_ids": [s], "source_ids": ["src-1"]}]
    NEW_CARDS["VM-D122"] = c


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
        assert scr_acc["record_count"] == 122, scr_acc["record_count"]
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, root / UNION)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 120 + 2, len(package["tasks"])
        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]
        by_task = {m["evidence_task_id"]: m for m in package["tasks"]}
        new_ids = {}
        for did in ("VM-D121", "VM-D122"):
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
            assert carried == 120 and len(added) == 2, (carried, added)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 122
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| added:", added)
    print("EVIDENCE REPLAY COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
