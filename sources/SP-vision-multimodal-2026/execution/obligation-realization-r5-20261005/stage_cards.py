#!/usr/bin/env python3
"""Stage VM-D075/VM-D090/VM-D092 corrections (STAGED ONLY - no acceptance/state change).

- VM-D075: reuse the verified staged license card content
  (execution/license-authority-repair-r5-20261004/staged-vm-d075-license.json):
  claim-1 tail resolved buckets + claim-2 weights + limitation-2 removed.
- VM-D090: deepen interface contract from the bound OSWorld paper (src-1 only):
  +claim-2 observation contract (screenshot/a11y-tree/terminal streams, §2.3/App A.2),
  +claim-3 action contract (pyautogui mouse/keyboard code + COMPUTER_13 structured
  space, §2.4/App A.3). Existing claim-1/limitation untouched.
- VM-D092: limitation reword — ScreenSpot-Pro acknowledged as separately admitted
  D120; still-unreviewed successors remain deferred. Claims untouched.
All staged cards validated with canonical validate_evidence_card against exact
task/package basis. Canonical files untouched.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/obligation-realization-r5-20261005"
CURR = "caab11b84274a4f4073b77042ca46d6154fbec473de5bce9b1c2644314e9b8c7"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"
TID090 = "evidence:SP-vision-multimodal-2026:85268ad1dbd5f285"
TID092 = "evidence:SP-vision-multimodal-2026:3d4f179a082773fd"

D075_OLD_LIM2 = "Qwen3-Omni repository (VM-D075): weight/code license status remains unresolved in canonical Evidence."
D092_OLD_LIM = "Successor currency check at later stages (v2/Pro-class named as check, not entries)."
D092_NEW_LIM = ("ScreenSpot-Pro is separately admitted as canonical VM-D120; any still-unreviewed "
                "successor remains correctly deferred (check, not entry).")


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    from scripts import survey_production_v2 as core

    acc = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/evidence-accepted.json")
    by_task = {r["evidence_task_id"]: r for r in acc["results"]}
    pkg = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/package.json")
    staged = {}

    # ---- VM-D075: reuse verified staged content ----
    meta = by_task[TID075]
    cur = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert any(l["text"] == D075_OLD_LIM2 for l in cur.get("limitations", [])), "D075 regression not present?"
    staged075 = core.load_json(
        SRC / "execution/license-authority-repair-r5-20261004/staged-vm-d075-license.json")
    card = copy.deepcopy(staged075)
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID075)
    task = core.load_json(SRC / "evidence/v2/accepted" / CURR / tm["path"])
    card["basis"] = {
        "task_sha256": tm["sha256"],
        "screening_acceptance_sha256": task["screening_basis"]["screening_acceptance_sha256"],
        "prompt_sha256": pkg["prompt"]["sha256"],
        "result_contract_sha256": pkg["contracts"]["card"]["sha256"],
    }
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, ("VM-D075", errors)
    staged["VM-D075"] = (TID075, meta, card)

    # ---- VM-D090: interface-contract depth ----
    meta = by_task[TID090]
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    assert {c["statement_id"] for c in card["claims"]} == {"claim-1"}, {c["statement_id"] for c in card["claims"]}
    assert len(card.get("limitations", [])) == 1
    subj = "ev-vmd090"
    card["claims"] = card["claims"] + [
        {"statement_id": "claim-2",
         "text": ("Observation contract: complete desktop screenshot (with mouse position/shape) plus "
                  "XML-format accessibility tree (ATSPI/PyWinAuto) plus customized streams including "
                  "terminal outputs; screenshot-only, a11y-only, combined and Set-of-Marks variants compared."),
         "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
         "evidence_class": "AUTHOR_CLAIM", "source_ids": ["src-1"],
         "context": "Paper §2.3 Observation Space + App A.2 (A.2.1 screenshot, A.2.2 accessibility tree) + §4.1 baseline variants."},
        {"statement_id": "claim-3",
         "text": ("Action contract: pyautogui mouse/keyboard code actions (moveTo/click/write/press/hotkey/"
                  "scroll/dragTo/keyDown/keyUp plus WAIT/FAIL/DONE) and the COMPUTER_13 structured action "
                  "space; syntax-correct code prediction required, composable in program structures."),
         "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
         "evidence_class": "AUTHOR_CLAIM", "source_ids": ["src-1"],
         "context": "Paper §2.4 Action Space + Table 2 + App A.3 (A.3.1 pyautogui, A.3.2 COMPUTER_13)."},
    ]
    card["verification"]["targets"].append(
        {"target": "Interface-contract depth repair (observation/action spaces)",
         "status": "VERIFIED",
         "finding": "Observation/action contract claims verified against bound OSWorld paper §§2.3–2.4 + App A.2/A.3; no DOM/API detail beyond source-accurate structured tool/action interface language.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID090)
    task = core.load_json(SRC / "evidence/v2/accepted" / CURR / tm["path"])
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, ("VM-D090", errors)
    staged["VM-D090"] = (TID090, meta, card)

    # ---- VM-D092: stale successor boundary ----
    meta = by_task[TID092]
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    lims = {l["statement_id"]: l for l in card["limitations"]}
    assert "limitation-1" in lims and lims["limitation-1"]["text"] == D092_OLD_LIM, lims
    lims["limitation-1"]["text"] = D092_NEW_LIM
    card["verification"]["targets"].append(
        {"target": "Stale successor-boundary correction (ScreenSpot-Pro admitted as D120)",
         "status": "VERIFIED",
         "finding": "Limitation reworded to acknowledge canonical D120; unreviewed-successor deferral preserved.",
         "subject_ids": ["ev-vmd092"], "source_ids": ["src-1"]})
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID092)
    task = core.load_json(SRC / "evidence/v2/accepted" / CURR / tm["path"])
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, ("VM-D092", errors)
    staged["VM-D092"] = (TID092, meta, card)

    for disc, (tid, m, c) in staged.items():
        outp = EDIR / f"staged-{disc.lower()}-card.json"
        outp.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"staged {disc} VALID | claims: {len(c['claims'])} | limitations: {len(c.get('limitations', []))}")
    report = {disc: {"evidence_task_id": tid, "claims": len(c["claims"]),
                     "limitations": len(c.get("limitations", []))}
              for disc, (tid, m, c) in staged.items()}
    (EDIR / "staging-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
