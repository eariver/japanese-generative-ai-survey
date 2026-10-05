#!/usr/bin/env python3
"""Stage VM-D074 + VM-D075 license-authority corrections (STAGED ONLY).

VM-D074 (VERIFIED kept): claim-3 -> code-only (supplement-bound); NEW claim-4 weights
(supplement-bound, checked-cards scope); obsolete unresolved tail removed; lim-1 kept.
VM-D075 (VERIFIED kept): claim-1 tail resolved buckets; NEW claim-2 weights;
limitation-2 (scoped unresolved) DELETED as resolved; lim-1 + unresolved kept.
No new facts beyond supplement bytes. Canonical validation with in-memory
supplement binding (mirrors replay mechanics; canonical files untouched).
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/license-authority-repair-r5-20261004"
CURR = "446f359c726546411244389d66c60dd5037d9d16a671cb5842accc02a10fa2da"
TID074 = "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"


def sid(url: str) -> str:
    return "supplement-src-" + hashlib.sha256(url.encode()).hexdigest()[:16]


SUP = {
    "vl_lic": sid("https://raw.githubusercontent.com/QwenLM/Qwen3-VL/main/LICENSE"),
    "vl_lic_hist": sid("https://raw.githubusercontent.com/QwenLM/Qwen3-VL/e8c6dfbe0472e567b1bedc7640f550e0e506429f/LICENSE"),
    "vl_card": sid("https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/raw/main/README.md"),
    "vl_card_hist": sid("https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/resolve/fe3340460dc1b2245a90d1b3b608bc86ffb3bfd6/README.md"),
    "om_lic": sid("https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/main/LICENSE"),
    "om_lic_hist": sid("https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/ae5dbf9e734b7c72c1a70805cfb321b5fa3e9615/LICENSE"),
    "om_card": sid("https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/main/README.md"),
    "om_card_hist": sid("https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/302ffa9/README.md"),
}


def register_sources(card: dict, supp: dict, keys: list) -> None:
    have = {s["source_id"] for s in card["sources"]}
    by_id = {s["supplement_source_id"]: s for s in supp["sources"]}
    for k in keys:
        s = by_id[SUP[k]]
        assert s["supplement_source_id"] not in have, k
        card["sources"].append({
            "source_id": s["supplement_source_id"], "url": s["locator"],
            "source_class": s["source_class"], "title": s["title"],
            "published_at": s["published_at"], "accessed_at": s["accessed_at"],
            "role": s["relation"],
        })


def validate(card: dict, tid: str, ev, core, supp_path: Path) -> None:
    supp = core.load_json(supp_path)
    pkg = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/package.json")
    pkg = copy.deepcopy(pkg)
    pkg["authority_supplement"] = {"path": str(supp_path.relative_to(ROOT)),
                                   "sha256": core.sha256_file(supp_path)}
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == tid)
    task = core.load_json(SRC / "evidence/v2/accepted" / CURR / tm["path"])
    task = copy.deepcopy(task)
    task["authority_supplement_source_ids"] = sorted(
        s["supplement_source_id"] for s in supp["sources"])
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, errors


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    from scripts import survey_production_v2 as core

    acc = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/evidence-accepted.json")
    by_task = {r["evidence_task_id"]: r for r in acc["results"]}

    # ---------- VM-D074 ----------
    meta = by_task[TID074]
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    claims = {c["statement_id"]: c for c in card["claims"]}
    assert set(claims) == {"claim-1", "claim-2", "claim-3"}, set(claims)
    assert claims["claim-3"]["text"].endswith("Model-weight license remains unresolved in canonical Evidence.")
    subj = "ev-vmd074"
    c3 = copy.deepcopy(claims["claim-3"])
    c3["text"] = ("Code license: Apache 2.0 (repo-root LICENSE file, present since the 2024-09-06 "
                   "LICENSE commit; cutoff-bound first-party authority).")
    c3["source_ids"] = ["src-1", SUP["vl_lic"], SUP["vl_lic_hist"]]
    c3["context"] = "Repo LICENSE current + pinned historical bytes."
    c4 = {"statement_id": "claim-4",
          "text": ("Selected released weights Apache 2.0 within bound model-card scope "
                   "(Qwen3-VL-8B-Instruct card apache-2.0 since 2025-10-11 creation; 4B sibling "
                   "verified; safetensors artifacts enumerated; no generalization beyond checked cards)."),
          "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
          "evidence_class": "PROJECT_CLAIM",
          "source_ids": [SUP["vl_card"], SUP["vl_card_hist"]],
          "context": "Model-card frontmatter current + pinned initial bytes."}
    card["claims"] = [claims["claim-1"], claims["claim-2"], c3, c4]
    supp074 = core.load_json(EDIR / "evidence-authority-supplement-vm-d074.json")
    register_sources(card, supp074, ["vl_lic", "vl_lic_hist", "vl_card", "vl_card_hist"])
    card["verification"]["targets"].append(
        {"target": "License authority repair (code + selected weights)",
         "status": "VERIFIED",
         "finding": "First-party repo LICENSE (current + 2024-09-06 pinned) and model-card README (current + 2025-10-11 pinned) exact bytes bound; obsolete unresolved tail removed; buckets separated.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    validate(card, TID074, ev, core, EDIR / "evidence-authority-supplement-vm-d074.json")
    (EDIR / "staged-vm-d074-license.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged VM-D074 VALID | claims:", len(card["claims"]), "| status:", card["status"])

    # ---------- VM-D075 ----------
    meta = by_task[TID075]
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    claims = {c["statement_id"]: c for c in card["claims"]}
    assert set(claims) == {"claim-1"}, set(claims)
    lims = {l["statement_id"]: l for l in card["limitations"]}
    assert set(lims) == {"limitation-1", "limitation-2"}, set(lims)
    subj = "ev-vmd075"
    c1 = copy.deepcopy(claims["claim-1"])
    old_tail = "Weights license and code license remain unresolved in canonical Evidence."
    assert c1["text"].endswith(old_tail), c1["text"][-120:]
    c1["text"] = c1["text"][: -len(old_tail)] + ("Code license Apache 2.0 (repo LICENSE since "
          "2025-09-22 inception); selected weights Apache 2.0 within bound model-card scope "
          "(30B-A3B-Instruct).")
    c1["source_ids"] = ["src-1", SUP["om_lic"], SUP["om_lic_hist"], SUP["om_card"], SUP["om_card_hist"]]
    c1["context"] = "Deployment surface per repo; license buckets per supplement bytes."
    c2 = {"statement_id": "claim-2",
          "text": ("Selected released weights Apache 2.0 within bound model-card scope "
                   "(Qwen3-Omni-30B-A3B-Instruct card apache-2.0 since 2025-09-20 initial commits; "
                   "bound artifact model-00001-of-00015.safetensors; no generalization beyond the checked card)."),
          "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
          "evidence_class": "PROJECT_CLAIM",
          "source_ids": [SUP["om_card"], SUP["om_card_hist"]],
          "context": "Model-card frontmatter current + pinned initial bytes."}
    card["claims"] = [c1, c2]
    card["limitations"] = [lims["limitation-1"]]  # limitation-2 (scoped unresolved) RESOLVED -> removed
    supp075 = core.load_json(EDIR / "evidence-authority-supplement-vm-d075.json")
    register_sources(card, supp075, ["om_lic", "om_lic_hist", "om_card", "om_card_hist"])
    card["verification"]["targets"].append(
        {"target": "License authority repair (code + selected weights)",
         "status": "VERIFIED",
         "finding": "First-party repo LICENSE (current + 2025-09-22 pinned) and model-card README (current + 2025-09-20 pinned) exact bytes bound; obsolete unresolved tail/limitation removed; Discovery contradiction repaired at source.",
         "subject_ids": [subj], "source_ids": ["src-1"]})
    validate(card, TID075, ev, core, EDIR / "evidence-authority-supplement-vm-d075.json")
    (EDIR / "staged-vm-d075-license.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged VM-D075 VALID | claims:", len(card["claims"]),
          "| limitations:", len(card["limitations"]), "| status:", card["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
