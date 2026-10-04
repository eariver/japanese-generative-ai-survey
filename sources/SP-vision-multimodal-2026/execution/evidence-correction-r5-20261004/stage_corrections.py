#!/usr/bin/env python3
"""Stage targeted Evidence corrections (STAGED ONLY - no acceptance, no state change).

Targets: VM-D062 LLaVA (correction), VM-D061 MiniGPT-4 (depth), VM-D034 DINO (operators),
VM-D033 MAE (recipe), VM-D024 LayoutLMv3 (1 line), VM-D028 GOT (1 line),
VM-D108 DocVQA (1 line), VM-D077 molmo2 repo (currentness buckets).
All other 104 cards untouched. Staged outputs validated with canonical
survey_evidence_v2.validate_evidence_card; written only under execution/
evidence-correction-r5-20261004/staged-cards/. Canonical accepted store read-only.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EVROOT = SRC / "evidence/v2/accepted/33ec63cbd5bbe776fb106f57fa64ca448061dfe92cbbfe3684848ddb17010b69/results"
OUTDIR = SRC / "execution/evidence-correction-r5-20261004/staged-cards"
ACC = json.loads((EVROOT.parent / "evidence-accepted.json").read_text(encoding="utf-8"))
BY_TASK = {r["evidence_task_id"]: r for r in ACC["results"]}
MX = json.load(open(SRC / "candidate-matrix-v2.json"))
DISC2TASK = {}
for row in MX["rows"]:
    for d in row.get("discovery_ids", []):
        DISC2TASK[d] = row["evidence_task_id"]

REVERIFY = "Primary full-body re-verified 2026-10-04 against bound locator (read-only web fetch of arXiv HTML); pinpoints recorded per claim context."


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

    # ---- VM-D062 LLaVA: full correction ----
    tid, meta, card = load_card("VM-D062")
    subj = "ev-vmd062"
    card["claims"] = [
        claim("claim-1", "Language-only GPT-4 instruction-data generation: image unseen by teacher; image encoded as symbolic sequences of multi-perspective captions plus bounding boxes [x1,y1,x2,y2]; COCO-sourced; 158K unique samples (58K conversation + 23K detailed description + 77K complex reasoning); seed examples are the only human annotations.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §3 + Tables 1/14 + App.F Tables 13/15/16.", subj),
        claim("claim-2", "Architecture/interface: CLIP ViT-L/14 visual encoder connected to Vicuna LLM through a single trainable projection matrix W (system described as end-to-end trained large multimodal model at the whole-system level).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §4.1 + Abstract/contributions.", subj),
        claim("claim-3", "Stage 1 feature-alignment pre-training: visual encoder FROZEN and LLM FROZEN; ONLY the projection matrix W trainable (theta=W); 595K CC3M-derived pairs; single-turn naive-expansion format.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §4.2 Stage 1 + Eq.(3) + App.E (CC3M/Fig.7/Table 11).", subj),
        claim("claim-4", "Stage 2 instruction tuning: visual encoder REMAINS FROZEN (always); projection layer AND LLM updated (theta={W,phi}); 158K instruction-following (multi-turn conversation + detailed + complex, uniformly sampled) or ScienceQA single-turn variant. The vision encoder is nowhere updated end-to-end; end-to-end phrasing is system-level (vs coordination systems), not component-level.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §4.2 Stage 2 + Eq.(3) + §5/App.C hyperparams; system-vs-component distinction per §1/§2/§4.1/App.B Fig.6.", subj),
        claim("claim-5", "Evaluation conditions: LLaVA-Bench (COCO) 85.1% All relative to text-only GPT-4 reference under the triplet/judge protocol (30 images x 3 types); In-the-Wild 67.3 vs BLIP-2 38.1; ScienceQA 90.92% alone and 92.53% ensemble with GPT-4-as-judge (reasoning-first, visual features before last layer, 12 epochs); LLaVA-Bench limits paper-acknowledged (knowledge/multilingual/retrieval/high-resolution/bag-of-patches failures incl. yogurt case).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §5.1 Tables 4/5/6 + §5.2 Tables 7/8 + Limitations + App.A/B.", subj),
        claim("claim-6", "X01 exhibit: machine-generated instruction-following data as a supervision contract — the data-composition claim Evidence must carry (caption+box proxy symbols; 158K composition; 595K alignment subset).",
              "PRIMARY_SUBJECT", "INFERENCE", "Edition synthesis over claims 1/3/4; X01 supervision-timeline role.", subj),
    ]
    card["limitations"] = [
        claim("limitation-1", "Synthetic instruction-data dependence; failure cases paper-acknowledged via LLaVA-Bench; knowledge/multilingual/internet-retrieval/high-resolution perception bounds per paper Limitations.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §5.1 Limitations + App.A/B.", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence correction re-verification (LLaVA topology)", "status": "VERIFIED",
         "finding": REVERIFY + " Old end-to-end vision-encoder+LLM tuning claim removed as factually wrong.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D062"] = (tid, meta, card)

    # ---- VM-D061 MiniGPT-4: depth ----
    tid, meta, card = load_card("VM-D061")
    subj = "ev-vmd061"
    c1 = copy.deepcopy(card["claims"][0])
    card["claims"] = [c1,
        claim("claim-2", "Visual stack provenance: BLIP-2-derived ViT-G/14 (EVA-CLIP) plus pretrained Q-Former, BOTH frozen throughout all MiniGPT-4 training; querying happens inside the reused frozen Q-Former; MiniGPT-4's own trainable path is only the linear map of Q-Former output into Vicuna space (no own query selection, no dense cross-attention).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper Abstract/§1/§3/§3.1/Fig.1 (freezes all other vision and language components).", subj),
        claim("claim-3", "Two-stage data: ~5M Conceptual-Captions/SBU/LAION pairs (20k steps x batch 256) for alignment pre-training; ~3.5K/5K ChatGPT-refined detailed descriptions (400 steps x batch 12) for curation finetuning.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §1/§3.1/§3.2/§3.3.", subj),
        claim("claim-4", "Q-Former removal is an ablation variant (MiniGPT-4 w/o Q-Former maps ViT output directly; AOK-VQA/GQA near-parity, paper concludes non-critical for advanced skills); 3-linear-layer and finetune-Q-Former variants are worse. Vicuna-vs-Flan-T5 control shows weaker LLM benefits less.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §4.4(a)(b)(c)/Tables 3-4/Figs.4-5 + §4.1/§4.3.", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence depth repair (MiniGPT-4 stack provenance)", "status": "VERIFIED",
         "finding": REVERIFY, "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D061"] = (tid, meta, card)

    # ---- VM-D034 DINO: operators ----
    tid, meta, card = load_card("VM-D034")
    subj = "ev-vmd034"
    card["claims"] = card["claims"] + [
        claim("claim-3", "Collapse avoidance requires BOTH centering (bias on teacher output only, EMA-updated) and sharpening (low teacher temperature); either missing collapses (KL->0 or dominated-dimension/uniform per H = h + D_KL decomposition).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §3.1 Eq.4/Alg.1 + §5.3/Fig.7 + App.D.", subj),
        claim("claim-4", "Temperature direction: TEACHER is centered+sharpened with the SMALLER temperature (student tau_s=0.1 fixed; teacher tau_t linear warmup 0.04->0.07); momentum teacher lambda cosine 0.996->1 with stop-gradient (student-only SGD). The reverse (student sharpened, teacher smoothed) is factually wrong.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §3.1 Eq.1/Alg.1 + §3.2 Implementation details + §5.2/Fig.6 + App.D.", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence depth repair (DINO operators, direction-correct)", "status": "VERIFIED",
         "finding": REVERIFY, "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D034"] = (tid, meta, card)

    # ---- VM-D033 MAE: recipe ----
    tid, meta, card = load_card("VM-D033")
    subj = "ev-vmd033"
    card["claims"] = card["claims"] + [
        claim("claim-2", "Reconstruction target: per-patch pixel MSE on masked patches only; FINAL recipe uses per-patch NORMALIZED pixels (default ablations use unnormalized; PCA/dVAE-token variants near-parity, tokenization unnecessary).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §3 Reconstruction target + Table 1(d)/Table 3 caption/Table 7.", subj),
        claim("claim-3", "Ablations: decoder depth 1->8 raises linear probe 65.5->73.5 while fine-tune stays ~84.9 (width default 512-d); mask ratio optimum 75% under both protocols (linear sensitive ~20pp gap, fine-tune flat 40-80%).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper Tables 1(a)(b)/2 + Fig.5/§4.1.", subj),
        claim("claim-4", "Linear-vs-finetune sensitivity and recipe versions: modest linear (73.5) but strong partial/full tuning; DEFAULT recipe = 8x512 decoder, unnormalized pixels, 800 epochs; FINAL recipe = normalized pixels, 1600 epochs (no saturation to 1600).",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §4.3/Fig.9/Table 12 + Table 1 caption/Table 3/Fig.7.", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence depth repair (MAE recipe, default-vs-final distinguished)", "status": "VERIFIED",
         "finding": REVERIFY, "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D033"] = (tid, meta, card)

    # ---- VM-D024 LayoutLMv3: 1 line ----
    tid, meta, card = load_card("VM-D024")
    subj = "ev-vmd024"
    card["claims"] = card["claims"] + [
        claim("claim-3", "MIM target is discrete image tokens from a codebook tokenizer (8,192 visual vocabulary, DiT-initialized), reconstructed with cross-entropy under ~40% blockwise masking — high-level layout structures, not raw pixels or region features.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §§1/2.2/3.2 + Fig.2/Fig.3/Eq.(2) (arXiv:2204.08387).", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence depth repair (LayoutLMv3 discrete-token target)", "status": "VERIFIED",
         "finding": REVERIFY + " Correct locator arXiv:2204.08387 (not 2204.08374).", "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D024"] = (tid, meta, card)

    # ---- VM-D028 GOT: 1 line ----
    tid, meta, card = load_card("VM-D028")
    subj = "ev-vmd028"
    card["claims"] = card["claims"] + [
        claim("claim-3", "Training is predominantly synthetic data-engine centered (PaddleOCR pseudo ground truth, six rendering tools for formulas/tables/music/geometry/charts, Nougat-method plus Chinese markdown pairs) with Common-Crawl PDF extraction alongside — rendered/pseudo-centered, not exclusively synthetic.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "Paper §§1/3.2.2/3.3.2/Fig.3 (arXiv:2409.01704; not 2403.05511).", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence depth repair (GOT synthetic data-engine composition)", "status": "VERIFIED",
         "finding": REVERIFY + " Correct locator arXiv:2409.01704 (not 2403.05511).", "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D028"] = (tid, meta, card)

    # ---- VM-D108 DocVQA: 1 line ----
    tid, meta, card = load_card("VM-D108")
    subj = "ev-vmd108"
    card["claims"] = card["claims"] + [
        claim("claim-3", "ANLS (Average Normalized Levenshtein Similarity, adopted from ST-VQA) is the primary metric so minor OCR-error mismatches are not severely penalized; used alongside Accuracy.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM", "DocVQA paper §5.1 Evaluation Metrics. No threshold/case-folding claim (ST-VQA-side detail, not DocVQA).", subj),
    ]
    card["verification"]["targets"].append(
        {"target": "Targeted Evidence depth repair (DocVQA ANLS definition line)", "status": "VERIFIED",
         "finding": REVERIFY, "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D108"] = (tid, meta, card)

    # ---- VM-D077 molmo2 repo: currentness buckets (PARTIAL kept) ----
    tid, meta, card = load_card("VM-D077")
    subj = "ev-vmd077"
    card["claims"] = card["claims"] + [
        claim("claim-3", "Model-weight license bucket (repo-linked first-party): Apache-2.0 on HuggingFace model cards (e.g., Molmo2-8B/O-7B) for research/educational use under Ai2 Responsible Use; trained on third-party datasets subject to academic and non-commercial research use only. Weight license must not be conflated with mixture-dataset licenses.",
              "PRIMARY_SUBJECT", "PROJECT_CLAIM", "Repo-linked first-party: HF allenai/Molmo2-8B + Molmo2-O-7B License-and-Use sections; allenai.org/blog/molmo2 footer; verified 2026-10-04.", subj),
        claim("claim-4", "Released-dataset availability bucket (repo-linked first-party collection): 9-dataset family plus eval splits served with live viewers (Molmo2-Cap/CapEval/VideoCapQA/VideoSubtitleQA/AskModelAnything/VideoPoint(+Eval/CountEval)/VideoTrack(+Eval)/MultiImageQA/SynMultiImageQA/MultiImagePoint); per-dataset ODC-BY with GPT-4.1/GPT-5 output Terms and Anthropic ToS where synthetic, CC BY-4.0 video subset via GCS, YouTube-ID separate download.",
              "PRIMARY_SUBJECT", "PROJECT_CLAIM", "Repo-linked first-party: HF allenai/molmo2-data collection + per-dataset License sections; blog data-curation table; verified 2026-10-04.", subj),
    ]
    lims = card.get("limitations", [])
    lims[0]["text"] = ("PARTIAL: training-data license mix bound at bucket level (academic/non-commercial third-party; "
                       "manual-license items DocQA/InfoQA/SceneText, LVBench, MLVU/LongVideoBench agreements, manual-download "
                       "tracking sets) — individual third-party license texts and Source Attribution contents remain unbound (INSPECT target).")
    card["limitations"] = lims
    card["verification"]["targets"].append(
        {"target": "Targeted currentness refresh (VM-D077 buckets, no Discovery mutation)", "status": "VERIFIED",
         "finding": "First-party current sources only (repo README badges -> HF collections/model cards, AllenAI blog), verified 2026-10-04. Status kept PARTIAL: individual third-party texts unbound; no new Discovery created.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    staged["VM-D077"] = (tid, meta, card)

    # validate + write staged (canonical validator with exact task/package basis)
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
                        "limitations": len(c.get("limitations", []))}
    (OUTDIR.parent / "staging-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
