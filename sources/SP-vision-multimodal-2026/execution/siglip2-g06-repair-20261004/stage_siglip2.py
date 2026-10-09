#!/usr/bin/env python3
"""Stage the VM-D036 G06-resolution card update (STAGED ONLY).

- limitation-1: keep own-scope first clause; replace stale G06-unbound tail with the
  resolved binding pointer (VM-D065 claim-3, already canonical). Class INFERENCE kept
  (edition-level authority-linkage statement), src-1 kept.
- verification.unresolved_questions: the single G06 entry is resolved -> [].
- Status VERIFIED kept. Canonical validate_evidence_card against exact task/package
  basis (no supplement involved). Canonical files untouched.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/siglip2-g06-repair-20261004"
CURR = "bd31c88ce4a41762e8182b4939fe0b836a95796cb6e3d99cb7eee8894ad32aa9"
TID036 = "evidence:SP-vision-multimodal-2026:0eb3420fb03f017e"

OLD_LIM = "Abs-page-level consumption for the loss mechanism (HTML extraction thin); SigLIP2 citation unbound (G06)."
NEW_LIM = "Abs-page-level consumption for the loss mechanism (HTML extraction thin); SigLIP2 citation bound via VM-D065 claim-3 (G06 resolved)."
OLD_UNRESOLVED = ["G06 SigLIP2 citation binding: SigLIP2 exact citation unbound; G06 gap preserved."]


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    from scripts import survey_production_v2 as core

    acc = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/evidence-accepted.json")
    meta = next(r for r in acc["results"] if r["evidence_task_id"] == TID036)
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    lims = card["limitations"]
    assert len(lims) == 1 and lims[0]["text"] == OLD_LIM, lims
    assert card["verification"]["unresolved_questions"] == OLD_UNRESOLVED
    lims[0]["text"] = NEW_LIM
    card["verification"]["unresolved_questions"] = []
    card["verification"]["targets"].append(
        {"target": "Narrow authority repair: G06 SigLIP2 binding resolved",
         "status": "VERIFIED",
         "finding": "SigLIP-2 vision-encoder citation bound via canonical VM-D065 claim-3 (no new source; existing Evidence sufficient); obsolete G06-unbound language superseded.",
         "subject_ids": ["ev-vmd036"], "source_ids": ["src-1"]})

    pkg = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/package.json")
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID036)
    task = core.load_json(SRC / "evidence/v2/accepted" / CURR / tm["path"])
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, errors
    outp = EDIR / "staged-vm-d036-g06-resolved.json"
    outp.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged VM-D036 VALID:", outp.relative_to(ROOT), "| status:", card["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
