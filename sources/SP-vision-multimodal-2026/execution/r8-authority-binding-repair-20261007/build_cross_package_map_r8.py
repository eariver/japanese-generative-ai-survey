#!/usr/bin/env python3
"""Build the r8 effective cross-package map (32 entries): r7 overlay 31 carried
(SHAs refreshed to r8 authority) + new VM-D110 P15->P05 SUPPORTING entry (§10.2).

This file is BOTH the intent record AND the generation-time overlay consumed by
the r8 Draft generator (no divergent sidecars). Frozen Core untouched.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
OLD = SRC / "execution/r7-targeted-authority-repair-20261007/cross-package-synthesis-authority-r7.json"
OUT = SRC / "execution/r8-authority-binding-repair-20261007/cross-package-map-r8.json"


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_production_v2 as core

    old = json.loads(OLD.read_text(encoding="utf-8"))
    assert len(old["entries"]) == 31, len(old["entries"])
    ev_acc = max((SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                 key=lambda p: p.stat().st_mtime)
    ev = json.loads(ev_acc.read_text(encoding="utf-8"))
    assert ev["result_count"] == 121
    by_task = {r["evidence_task_id"]: r for r in ev["results"]}
    arch_sha = core.sha256_file(SRC / "architecture-v2.json")
    appr_sha = core.sha256_file(SRC / "gates/architecture-approval.json")
    mx_sha = core.sha256_file(SRC / "candidate-matrix-v2.json")
    ev_sha = core.sha256_file(ev_acc)

    new_entries = []
    for e in old["entries"]:
        e2 = dict(e)
        meta = by_task[e["evidence_task_id"]]
        raw = (ev_acc.parent / "results" / meta["filename"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == meta["sha256"], e["evidence_task_id"]
        assert e2["evidence_sha256"] == meta["sha256"], e["evidence_task_id"]  # no card drift r7->r8
        for k, v in (("architecture_sha256", arch_sha),
                     ("architecture_approval_sha256", appr_sha),
                     ("candidate_matrix_sha256", mx_sha),
                     ("evidence_acceptance_sha256", ev_sha)):
            e2[k] = v
        new_entries.append(e2)

    def _entry(consumer, axis, did, home, home_usage, tid):
        meta = by_task[tid]
        card = json.loads((ev_acc.parent / "results" / meta["filename"]).read_text(encoding="utf-8"))
        mx = json.loads((SRC / "candidate-matrix-v2.json").read_text(encoding="utf-8"))
        cand = next(r["candidate_id"] for r in mx["rows"] if r["evidence_task_id"] == tid)
        sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
        disp = next(a["disposition"] for a in sel["assignments"] if a["candidate_id"] == cand)
        assert disp == "SELECTED", (did, disp)
        return {
            "consumer_package": consumer,
            "synthesis_axis": [axis],
            "discovery_id": did,
            "candidate_id": cand,
            "canonical_home_package": home,
            "home_architecture_usage": home_usage,
            "all_architecture_usages": [{"package_id": home, "usage": home_usage}],
            "evidence_task_id": tid,
            "evidence_sha256": meta["sha256"],
            "evidence_filename": meta["filename"],
            "evidence_subject_ids": [card["artifact"]["primary_subject_id"]],
            "selection_disposition": "SELECTED",
            "reference_role": "CROSS_PACKAGE_SYNTHESIS_REFERENCE",
            "architecture_sha256": arch_sha,
            "architecture_approval_sha256": appr_sha,
            "candidate_matrix_sha256": mx_sha,
            "evidence_acceptance_sha256": ev_sha,
        }

    # Retained §10.1 mappings missing from the generation overlay: D114/D115 -> P07B
    new_entries.append(_entry("P07B", "localization-transfer scope", "VM-D114", "P06", "PRIMARY",
                              "evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e"))
    new_entries.append(_entry("P07B", "concept-grounding scope", "VM-D115", "P03", "PRIMARY",
                              "evidence:SP-vision-multimodal-2026:fb77b0019ffe81dc"))
    # New §10.2 entry: VM-D110 P15(PRIMARY home) -> P05 SUPPORTING evaluation authority
    tid110 = "evidence:SP-vision-multimodal-2026:f1346f195b48d6e0"
    meta110 = by_task[tid110]
    assert meta110["discovery_ids"] == ["VM-D110"] and meta110["status"] == "VERIFIED"
    card110 = json.loads((ev_acc.parent / "results" / meta110["filename"]).read_text(encoding="utf-8"))
    new_entries.append({
        "consumer_package": "P05",
        "synthesis_axis": ["p05_document_ocr_evaluation_contract"],
        "discovery_id": "VM-D110",
        "candidate_id": "candidate:SP-vision-multimodal-2026:0202917391a980c0",
        "canonical_home_package": "P15",
        "home_architecture_usage": "PRIMARY",
        "all_architecture_usages": [{"package_id": "P15", "usage": "PRIMARY"}],
        "evidence_task_id": tid110,
        "evidence_sha256": meta110["sha256"],
        "evidence_filename": meta110["filename"],
        "evidence_subject_ids": [card110["artifact"]["primary_subject_id"]],
        "selection_disposition": "SELECTED",
        "reference_role": "CROSS_PACKAGE_SYNTHESIS_REFERENCE",
        "architecture_sha256": arch_sha,
        "architecture_approval_sha256": appr_sha,
        "candidate_matrix_sha256": mx_sha,
        "evidence_acceptance_sha256": ev_sha,
    })
    out = dict(old)
    out["entries"] = new_entries
    out["entry_count"] = len(new_entries)
    out["unique_discovery_count"] = len({e["discovery_id"] for e in new_entries})
    out["architecture_sha256"] = arch_sha
    out["architecture_approval_sha256"] = appr_sha
    out["candidate_matrix_sha256"] = mx_sha
    out["evidence_acceptance_sha256"] = ev_sha
    out["provenance"] = ("r8 effective map: 31 entries carried from the r7 overlay (card SHAs "
                         "re-verified identical, authority SHAs rebound to r8) + new VM-D110 "
                         "P15->P05 SUPPORTING evaluation-authority entry (§10.2; no PRIMARY "
                         "relocation; P15 remains the synthesis home). This file is the "
                         "generation-time overlay: the r8 generator consumes it and the "
                         "effective-input report + semantic validator check FINAL block refs.")
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(f"map r8: {len(new_entries)} entries -> {OUT.relative_to(ROOT)}")
    print(Counter((e["consumer_package"], e["discovery_id"]) for e in new_entries if e["consumer_package"] in ("P07B", "P05", "P11")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
