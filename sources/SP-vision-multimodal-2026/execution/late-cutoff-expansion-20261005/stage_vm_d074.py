#!/usr/bin/env python3
"""Build the merged VM-D074 staged card (STAGED ONLY).

Base: license-run staged card (code + weights authority, supplement-bound).
Change: claim-3 era-separation reword (§11) + register the 2 history supplement
sources + extend claim-3 source_ids. License conclusion unchanged.
Validated with canonical validate_evidence_card (in-memory supplement binding).
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/late-cutoff-expansion-20261005"
TID074 = "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c"


def main() -> int:
    root = Path(".").resolve()
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    from scripts import survey_production_v2 as core

    base = core.load_json(
        SRC / "execution/license-authority-repair-r5-20261004/staged-vm-d074-license.json")
    hist = core.load_json(EDIR / "evidence-authority-supplement-vm-d074-history.json")
    assert len(hist["sources"]) == 2
    card = copy.deepcopy(base)
    claims = {c["statement_id"]: c for c in card["claims"]}
    assert set(claims) == {"claim-1", "claim-2", "claim-3", "claim-4"}, set(claims)
    assert "2024-09-06 LICENSE commit" in claims["claim-3"]["text"]
    claims["claim-3"]["text"] = (
        "Code license: Apache 2.0 (repo-root LICENSE file; the 2024-09-06 commit is "
        "Qwen2-VL-era predecessor history; Qwen3-VL-era authority is the unchanged Apache-2.0 "
        "text in the 2025-09-23 cutover and 2025-09-30 pre-cutoff trees).")
    claims["claim-3"]["context"] = (
        "Qwen3-VL-era pinned trees f0ab724/ebd38f4 (same Apache-2.0 bytes, hash-bound); "
        "predecessor history separated, not cited as the grant.")
    have = {s["source_id"] for s in card["sources"]}
    hist_ids = []
    for s in hist["sources"]:
        assert s["supplement_source_id"] not in have, s["supplement_source_id"]
        card["sources"].append({
            "source_id": s["supplement_source_id"], "url": s["locator"],
            "source_class": s["source_class"], "title": s["title"],
            "published_at": s["published_at"], "accessed_at": s["accessed_at"],
            "role": s["relation"],
        })
        hist_ids.append(s["supplement_source_id"])
    claims["claim-3"]["source_ids"] = list(dict.fromkeys(
        claims["claim-3"]["source_ids"] + hist_ids))
    card["verification"]["targets"].append(
        {"target": "Qwen3-VL-era license authority separation",
         "status": "VERIFIED",
         "finding": "Predecessor 2024-09-06 history separated from Qwen3-VL-era f0ab724/ebd38f4 tree authority (identical Apache-2.0 bytes); conclusion unchanged.",
         "subject_ids": ["ev-vmd074"], "source_ids": ["src-1"]})

    # Validate with the REAL union manifest + real package/task copies in memory
    # (mirrors replay mechanics; canonical files untouched).
    import build_union as _bu
    union_path = _bu.build_union(ROOT)
    union = core.load_json(union_path)
    import build_package as _bp
    _, pkg = _bp.build_package(ROOT)
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID074)
    task = core.load_json(ROOT / "sources/SP-vision-multimodal-2026/execution/late-cutoff-expansion-20261005" / "evidence-package-120" / tm["path"])
    # Rebind basis to the fresh package (deterministic metadata-only change).
    probe = core.load_json(ROOT / "sources/SP-vision-multimodal-2026/evidence/v2/accepted/446f359c726546411244389d66c60dd5037d9d16a671cb5842accc02a10fa2da/results/task-0202917391a980c0420f.json")
    scr_acc_path = max((ROOT / "sources/SP-vision-multimodal-2026/screening/v2/accepted").glob("*/screening-accepted.json"), key=lambda p: p.stat().st_mtime)
    card["basis"] = {
        "task_sha256": tm["sha256"],
        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
        "prompt_sha256": probe["basis"]["prompt_sha256"],
        "result_contract_sha256": probe["basis"]["result_contract_sha256"],
    }
    task["authority_supplement_source_ids"] = sorted(
        s["supplement_source_id"] for s in union["sources"] if s["evidence_task_id"] == TID074)
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=ROOT)
    assert not errors, errors
    (EDIR / "staged-vm-d074-merged.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged VM-D074 merged VALID | claims:", len(card["claims"]),
          "| claim-3 src:", len(claims["claim-3"]["source_ids"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
