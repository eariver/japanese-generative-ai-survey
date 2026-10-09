#!/usr/bin/env python3
"""Stage the single VM-D039 CLIP correction for r8 (STAGED ONLY).

claim-1: `zero of its 1.28M labels` -> `without using any of its 1.28M training
examples` (source-faithful unit fix). Everything else preserved. Canonical
validation against the 66c9932e package basis.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
CURR = "66c9932ebc23a3c04df6c1dd2ba65fb300c7e090343e5062487160f00682c77f"
EVROOT = SRC / "evidence/v2/accepted" / CURR / "results"
OUTDIR = SRC / "execution/r8-authority-binding-repair-20261007/staged-cards"


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    OUTDIR.mkdir(parents=True, exist_ok=True)

    ACC = json.loads((EVROOT.parent / "evidence-accepted.json").read_text(encoding="utf-8"))
    BY_TASK = {r["evidence_task_id"]: r for r in ACC["results"]}
    tid = "evidence:SP-vision-multimodal-2026:20d1ebc2759ddd61"
    meta = BY_TASK[tid]
    assert meta["discovery_ids"] == ["VM-D039"] and meta["sha256"][:12] == "0efcc94502a2"
    card = json.loads((EVROOT / meta["filename"]).read_text(encoding="utf-8"))
    c1 = next(c for c in card["claims"] if c["statement_id"] == "claim-1")
    assert "zero of its 1.28M labels" in c1["text"], c1["text"]
    new_text = c1["text"].replace(
        "matches supervised ResNet-50 on ImageNet with zero of its 1.28M labels",
        "matches the supervised ResNet-50 baseline on ImageNet without using any of its 1.28M training examples")
    assert "1.28M labels" not in new_text
    assert "1.28M training examples" in new_text
    card["claims"] = [dict(c1, text=new_text) if c["statement_id"] == "claim-1" else copy.deepcopy(c)
                      for c in card["claims"]]
    card["verification"]["targets"].append(
        {"target": "Targeted authority correction (CLIP 1.28M unit fix)",
         "status": "VERIFIED",
         "finding": ("Bound primary paper re-verified read-only (already-bound locator; no new "
                     "source). Corrected the claim unit from labels to training examples per the "
                     "original CLIP paper; all other corrected semantics preserved (400M pairs, "
                     "addressability, zero-shot, limitation scope, no BoW misattribution)."),
         "subject_ids": ["ev-vmd039"], "source_ids": ["src-1"]})
    assert card["status"] == "VERIFIED"
    blob = json.dumps(card, ensure_ascii=False)
    assert "1.28M labels" not in blob and "400M" in blob

    PKG = json.loads((EVROOT.parent / "package.json").read_text(encoding="utf-8"))
    tm = next(m for m in PKG["tasks"] if m["evidence_task_id"] == tid)
    task = json.loads((EVROOT.parent / tm["path"]).read_text(encoding="utf-8"))
    errors = ev.validate_evidence_card(card, task, tm["sha256"], PKG, repo_root=ROOT)
    assert not errors, errors
    outp = OUTDIR / f"staged-VM-D039-{meta['filename']}"
    outp.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTDIR.parent / "staging-report.json").write_text(json.dumps(
        {"VM-D039": {"evidence_task_id": tid, "staged_file": str(outp.relative_to(ROOT)),
                     "claims": len(card["claims"]), "status": card["status"]}},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"VM-D039": tid, "staged": str(outp.relative_to(ROOT))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
