#!/usr/bin/env python3
"""Stage 2 targeted Evidence authority corrections for r7 (STAGED ONLY).

- VM-D108 DocVQA: remove pseudo-quantitative `contamination MEDIUM` /
  `language-prior HIGH` grades from claim-2; keep bounded INFERENCE that
  public-source/extractive setup warrants a separate audit while the paper
  measures no prevalence and assigns no level. Limitation refined to
  source-fact vs audit-inference distinction.
- VM-D010 DETR: correct claim-3 NMS semantics from overstrong `provably
  unnecessary only from later decoder layers` to empirical layer-wise ablation;
  preserve the full design contract.
Staged outputs validated with canonical validate_evidence_card against the
current 81e3b75b package basis. Written only under staged-cards/.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
CURR = "81e3b75be5ac2b489512898dfe236a20b41a73617a8cb5b4b7783f868580764b"
EVROOT = SRC / "evidence/v2/accepted" / CURR / "results"
OUTDIR = SRC / "execution/r7-targeted-authority-repair-20261007/staged-cards"

REVERIFY = ("Bound primary paper re-verified read-only (already-bound locator; no new source).")


def claim(sid, text, role, cls, ctx, subj, srcs=None):
    return {"statement_id": sid, "text": text, "subject_id": subj, "subject_role": role,
            "evidence_class": cls, "source_ids": srcs or ["src-1"], "context": ctx}


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    OUTDIR.mkdir(parents=True, exist_ok=True)

    ACC = json.loads((EVROOT.parent / "evidence-accepted.json").read_text(encoding="utf-8"))
    BY_TASK = {r["evidence_task_id"]: r for r in ACC["results"]}
    staged = {}

    # ================= VM-D108 DocVQA =================
    tid108 = "evidence:SP-vision-multimodal-2026:70a2a554e22606a9"
    meta108 = BY_TASK[tid108]
    card108 = json.loads((EVROOT / meta108["filename"]).read_text(encoding="utf-8"))
    assert card108["evidence_task_id"] == tid108
    subj108 = "ev-vmd108"
    c1, c2, c3 = card108["claims"]
    assert c1["statement_id"] == "claim-1" and c2["statement_id"] == "claim-2" and c3["statement_id"] == "claim-3"
    assert "contamination MEDIUM" in c2["text"] and "language-prior HIGH" in c2["text"], c2["text"]
    card108["claims"] = [
        copy.deepcopy(c1),
        claim("claim-2",
              "Reporting discipline: ANLS, never bare accuracy alone (OCR-substring upper bounds inflate). "
              "Because DocVQA uses public-source documents and extractive answers, evaluation of later "
              "pretrained foundation models should separately audit possible pretraining overlap and "
              "shortcut behavior; the DocVQA paper itself does not measure contamination prevalence "
              "or assign a risk level.",
              "PRIMARY_SUBJECT", "INFERENCE",
              "Edition-level analytical synthesis by the Work operator (lineage/selection/boundary/contract judgment, not a literal statement of the cited source); structural home for edition rationale.",
              subj108),
        copy.deepcopy(c3),
    ]
    old_lim = card108["limitations"][0]["text"]
    assert old_lim == "Extractive-shortcut vulnerability; web-document contamination.", old_lim
    card108["limitations"] = [
        claim("limitation-1",
              "Extractive-shortcut vulnerability is a source-supported design concern; possible web-document "
              "pretraining overlap is an edition-level audit concern, not a paper-measured contamination rate.",
              "PRIMARY_SUBJECT", "INFERENCE",
              "Evidence boundary retained for downstream editorial use.",
              subj108),
    ]
    card108["verification"]["targets"].append(
        {"target": "Targeted authority correction (DocVQA pseudo-quantitative grades removed)",
         "status": "VERIFIED",
         "finding": REVERIFY + " Removed unmeasured pseudo-quantitative severity grades from claim-2; no replacement scale introduced. Bounded inference (public-source + extractive => separate audit warranted; paper measures no prevalence, assigns no level) kept as INFERENCE, not AUTHOR_CLAIM.",
         "subject_ids": [subj108], "source_ids": ["src-1"]})
    assert card108["status"] == "VERIFIED"
    staged["VM-D108"] = (tid108, meta108, card108)

    # ================= VM-D010 DETR =================
    tid010 = "evidence:SP-vision-multimodal-2026:b7de06e9d5276cc1"
    meta010 = BY_TASK[tid010]
    card010 = json.loads((EVROOT / meta010["filename"]).read_text(encoding="utf-8"))
    assert card010["evidence_task_id"] == tid010
    subj010 = "ev-vmd010"
    d1, d2, d3 = card010["claims"]
    assert d3["statement_id"] == "claim-3"
    assert "provably unnecessary only from later decoder layers" in d3["text"], d3["text"]
    card010["claims"] = [
        copy.deepcopy(d1),
        copy.deepcopy(d2),
        claim("claim-3",
              "Costs stated by the paper: 300-500-epoch AdamW schedules (3 days on 16 V100), auxiliary decoding "
              "losses as standard training recipe after each intermediate decoder layer (shared FFNs; helpful, "
              "not architecturally mandatory), object-query slot specialization. DETR is designed to omit NMS "
              "in the final set-prediction pipeline; layer-wise ablation shows that NMS can improve the first "
              "decoder layer, but its benefit decreases with depth and becomes harmful at the final output; "
              "the paper interprets this as duplicate suppression emerging through decoder "
              "interactions/self-attention.",
              "PRIMARY_SUBJECT", "AUTHOR_CLAIM",
              "Sections 4.1/4.2 ablations (encoder layers, decoder layers, FFN, positional encodings, NMS study) + conclusion challenges paragraph.",
              subj010),
    ]
    card010["verification"]["targets"].append(
        {"target": "Targeted authority correction (DETR NMS empirical-ablation semantics)",
         "status": "VERIFIED",
         "finding": REVERIFY + " Removed overstrong necessity wording from claim-3; "
         "NMS study recorded as empirical ablation (helps layer 1, decreasing benefit, harmful at final; "
         "duplicate suppression via decoder interactions/self-attention). No necessity-proof language. "
         "Design contract (set prediction, Hungarian, cost-vs-loss, queries, NMS-free final pipeline, aux losses as recipe) preserved.",
         "subject_ids": [subj010], "source_ids": ["src-1"]})
    assert card010["status"] == "VERIFIED"
    staged["VM-D010"] = (tid010, meta010, card010)

    # ---- guards ----
    for disc, (tid2, meta2, c) in staged.items():
        blob = json.dumps(c, ensure_ascii=False)
        assert "MEDIUM" not in blob and "HIGH" not in blob or disc == "VM-D010", disc
        assert "provably" not in blob and "原理的" not in blob, disc
    blob108 = json.dumps(staged["VM-D108"][2], ensure_ascii=False)
    assert "contamination MEDIUM" not in blob108 and "language-prior HIGH" not in blob108
    assert "does not measure contamination prevalence" in blob108
    assert "12K+" in blob108 and "ANLS" in blob108 and "94.36%" in blob108
    blob010 = json.dumps(staged["VM-D010"][2], ensure_ascii=False)
    assert "Hungarian" in blob010 and "object queries" in blob010.lower().replace("-", " ") or "object-query" in blob010

    # ---- canonical validation against current package basis ----
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
                        "claims": len(c["claims"]), "limitations": len(c.get("limitations", [])),
                        "status": c.get("status")}
    (OUTDIR.parent / "staging-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
