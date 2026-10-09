#!/usr/bin/env python3
"""Stage the VM-D075 scope-wording correction (STAGED ONLY).

- limitation-2: unscoped -> candidate-scoped semantically-equivalent wording.
- Everything else identical (status VERIFIED, claims, sources, limitation-1,
  unresolved_questions, materiality-relevant fields).
- Validated with canonical validate_evidence_card against exact task/package basis.
- Canonical files untouched.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/blocker-repair-r5-20261004"
CURR = "8d79dce3a71f97db855474b60aebbd66a3b497914db6fac523097813641e4ced"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"

OLD = "Weight/code licenses remain unresolved in canonical Evidence."
NEW = "Qwen3-Omni repository (VM-D075): weight/code license status remains unresolved in canonical Evidence."


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    from scripts import survey_production_v2 as core

    acc = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/evidence-accepted.json")
    meta = next(r for r in acc["results"] if r["evidence_task_id"] == TID075)
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    lims = {l["statement_id"]: l for l in card["limitations"]}
    assert set(lims) == {"limitation-1", "limitation-2"}, set(lims)
    assert lims["limitation-2"]["text"] == OLD
    lims["limitation-2"]["text"] = NEW
    card["verification"]["targets"].append(
        {"target": "Narrow scope-wording correction (VM-D075 limitation-2)",
         "status": "VERIFIED",
         "finding": "Subject/candidate made explicit; no new license fact; status/claims/sources/materiality unchanged.",
         "subject_ids": ["ev-vmd075"], "source_ids": ["src-1"]})

    pkg = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/package.json")
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID075)
    task = core.load_json(SRC / "evidence/v2/accepted" / CURR / tm["path"])
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, errors
    outp = EDIR / "staged-vm-d075-scoped.json"
    outp.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged VM-D075 VALID:", outp.relative_to(ROOT), "| status:", card["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
