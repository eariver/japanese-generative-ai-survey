#!/usr/bin/env python3
"""Stage 3 targeted Evidence authority corrections (STAGED ONLY - no acceptance, no state change).

Targets (all from already-bound primary papers, re-verified read-only 2026-10-06):
- VM-D023 LayoutLM: MVLM pre-training = text + 2D layout (no image-embedding
  pre-training); Faster R-CNN image features = downstream integration;
  image-embedding pre-training = stated future work.
- VM-D039 CLIP: remove bag-of-words/compositionality misattribution; replace with
  original-paper limitation scope (§6 + §3.1.5).
- VM-D116 pi-zero: separate H=50 output chunk / platform control rates / replan cadence.
All other 118 cards untouched. Staged outputs validated with canonical
survey_evidence_v2.validate_evidence_card; written only under execution/
evidence-authority-repair-r6-20261006/staged-cards/. Canonical accepted store read-only.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
CURR = "f6ef98cb6b5e6246affbde9c899e8018cac8983aa9848cc14b8ced77f54ccd24"
EVROOT = SRC / "evidence/v2/accepted" / CURR / "results"
OUTDIR = SRC / "execution/evidence-authority-repair-r6-20261006/staged-cards"
ACC = json.loads((EVROOT.parent / "evidence-accepted.json").read_text(encoding="utf-8"))
BY_TASK = {r["evidence_task_id"]: r for r in ACC["results"]}
MX = json.load(open(SRC / "candidate-matrix-v2.json"))
DISC2TASK = {}
for row in MX["rows"]:
    for d in row.get("discovery_ids", []):
        DISC2TASK[d] = row["evidence_task_id"]

REVERIFY = ("Bound primary paper re-verified read-only 2026-10-06 (arXiv HTML of the "
            "already-bound locator; no new source).")


def load_card(disc: str):
    tid = DISC2TASK[disc]
    meta = BY_TASK[tid]
    card = json.loads((EVROOT / meta["filename"]).read_text(encoding="utf-8"))
    return tid, meta, card


def claim(sid, text, role, cls, ctx, subj):
    return {"statement_id": sid, "text": text, "subject_id": subj, "subject_role": role,
            "evidence_class": cls, "source_ids": ["src-1"], "context": ctx}


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    OUTDIR.mkdir(parents=True, exist_ok=True)
    staged = {}

    # ---- VM-D023 LayoutLM: pre-training contract correction ----
    tid, meta, card = load_card("VM-D023")
    subj = "ev-vmd023"
    card["claims"] = [
        claim("claim-1",
              "MVLM pre-training learns text + 2D layout representation: input tokens masked (15%, 80/10/10 masking policy) while 2D position embeddings (x0/y0/x1/y1 scaled to 0-1000) are kept, predicting masked tokens from language + layout context; optional MDC multi-label document classification on IIT-CDIP tags. Pre-trained on IIT-CDIP (6M+ documents / 11M images, Tesseract OCR hOCR layout); BASE 113M / LARGE 343M BERT-initialized.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper §§2.4/3.1/3.3/3.4 (arXiv:1912.13318v5).", subj),
        claim("claim-2",
              "Faster R-CNN (ResNet-101 backbone, Visual Genome pre-trained) image region features enter as token image embeddings and a whole-image [CLS] embedding for downstream fine-tuning/evaluation (FUNSD/SROIE/RVL-CDIP Text+Layout+Image settings, 160M params; FUNSD 0.7927, SROIE LARGE 0.9524, RVL-CDIP 94.42%) — distinct from image modality in the MVLM pre-training objective.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper §§2.3/3.5/3.6 Tables 1/4/5 (arXiv:1912.13318v5).", subj),
        claim("claim-3",
              "Paper's stated forward program: more data/compute, LARGE text+layout training, involving image embeddings in the pre-training step, new architectures and self-supervised objectives — the data/compute scaling reading that explains the later lineage transition.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper §5 Conclusion and Future Work (arXiv:1912.13318v5).", subj),
    ]
    card["limitations"] = [
        claim("limitation-1",
              "Base-version scope; unified successors (v3) needed for image-modality completeness.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Discovery scope limitation + paper forward program (arXiv:1912.13318v5).", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted authority correction (LayoutLM v1 pre-training contract)",
         "status": "VERIFIED",
         "finding": REVERIFY + " Removed internal contradiction: image embeddings are NOT part of the v1 MVLM pre-training contract (downstream integration only); image-embedding pre-training is the paper's stated future work.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D023"] = (tid, meta, card)

    # ---- VM-D039 CLIP: remove BoW misattribution, source-accurate limits ----
    tid, meta, card = load_card("VM-D039")
    subj = "ev-vmd039"
    assert len(card["claims"]) == 3 and len(card["limitations"]) == 1
    card["claims"] = [copy.deepcopy(card["claims"][0]), copy.deepcopy(card["claims"][1])]
    card["limitations"] = [
        claim("limitation-1",
              "Original-paper zero-shot limits: weak fine-grained classification (car models, flower species, aircraft variants), counting (CLEVRCounts), near-random novel systematic tasks (KITTI distance); out-of-distribution brittleness (MNIST 88%, below a pixel baseline); ~1000x compute estimated to reach overall SOTA (infeasible on current hardware).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper §6 Limitations + §3.1.5 (arXiv:2103.00020v1).", subj),
    ]
    # Supersede the defect-carrying verification target (keep full-body target intact).
    tgts = card["verification"]["targets"]
    assert len(tgts) == 2 and tgts[1]["target"] == "bag-of-words limitation preserved"
    tgts[1] = {"target": "Targeted authority correction (CLIP BoW misattribution removed)",
               "status": "VERIFIED",
               "finding": REVERIFY + " The 2021 original paper contains no bag-of-words/compositionality limitation claim (BoW appears only for the Joulin et al. baseline method and the caption-prediction ablation in §2.3/Fig.2); the prior target is superseded and the limitation replaced with §6/§3.1.5 scope.",
               "subject_ids": [subj], "source_ids": ["src-1"]}
    staged["VM-D039"] = (tid, meta, card)

    # ---- VM-D116 pi-zero: horizon / rate / cadence separation ----
    tid, meta, card = load_card("VM-D116")
    subj = "ev-vmd116"
    old = {c["statement_id"]: c["text"] for c in card["claims"]}
    assert set(old) == {"claim-1", "claim-2", "claim-3"}, set(old)
    card["claims"] = [
        claim("claim-1",
              "Model output contract: PaliGemma VLM backbone (3B) + 300M flow-matching action expert (3.3B total); predicts continuous-action chunks with horizon H=50 (A_t=[a_t..a_{t+H-1}]); conditional flow-matching vector field integrated with 10 Euler steps; no temporal ensembling (open-loop chunk execution).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper §§I/IV + App.A-B/A-D (arXiv:2410.24164v4).", subj),
        copy.deepcopy(card["claims"][1]),
        copy.deepcopy(card["claims"][2]),
        claim("claim-4",
              "Control rates are platform-dependent: UR5e / Franka run at 20 Hz, other evaluated robots at 50 Hz; the paper describes control capability up to 50 Hz (not a uniform 50 Hz rate).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper §§I/II/V-C + App.A-D Inference (arXiv:2410.24164v4).", subj),
        claim("claim-5",
              "Re-inference cadence is separate from horizon: 20 Hz UR5e / Franka re-infer every 0.8 s (after 16 actions); 50 Hz robots every 0.5 s (after 25 actions); the full H=50 chunk need not execute before re-inference.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Paper App.A-D Inference (arXiv:2410.24164v4).", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted authority correction (pi-zero horizon/rate/cadence separation)",
         "status": "VERIFIED",
         "finding": REVERIFY + " Removed 'continuous 50Hz 50-step action chunks' conflation; horizon (H=50), control rate (20/50 Hz platform-dependent), and replan interval (16/25 actions) now carried as three distinct quantities.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D116"] = (tid, meta, card)

    # validate + write staged (canonical validator against the 121-task package basis)
    PKG = json.loads((EVROOT.parent / "package.json").read_text(encoding="utf-8"))
    TASKMETA = {m["evidence_task_id"]: m for m in PKG["tasks"]}
    report = {}
    for disc, (tid2, meta2, c) in staged.items():
        tm = TASKMETA[tid2]
        task = json.loads((EVROOT.parent / tm["path"]).read_text(encoding="utf-8"))
        errors = ev.validate_evidence_card(c, task, tm["sha256"], PKG, repo_root=ROOT)
        assert not errors, f"{disc} staged card invalid: {errors}"
        outp = OUTDIR / f"staged-{disc}-{meta2['filename']}"
        outp.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report[disc] = {"evidence_task_id": tid2, "staged_file": str(outp.relative_to(ROOT)),
                        "claims": len(c["claims"]), "metrics": len(c.get("metrics", [])),
                        "limitations": len(c.get("limitations", [])),
                        "status": c.get("status")}
    (OUTDIR.parent / "staging-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
