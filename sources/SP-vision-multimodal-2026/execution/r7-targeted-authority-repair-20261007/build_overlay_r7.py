#!/usr/bin/env python3
"""Build cross-package synthesis overlay for r7: 30 carried entries (SHA re-verified
against the r7 authority) + new P07A/VM-D114 entry (§11). Frozen Core untouched.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
OLD = SRC / "execution/r6-final-authority-correction-20261006/cross-package-synthesis-authority-r6.json"
OUT = SRC / "execution/r7-targeted-authority-repair-20261007/cross-package-synthesis-authority-r7.json"


def main() -> int:
    old = json.loads(OLD.read_text(encoding="utf-8"))
    assert len(old["entries"]) == 30
    ev_acc = max((SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                 key=lambda p: p.stat().st_mtime)
    ev = json.loads(ev_acc.read_text(encoding="utf-8"))
    assert ev["result_count"] == 121
    by_task = {r["evidence_task_id"]: r for r in ev["results"]}
    arch = json.loads((SRC / "architecture-v2.json").read_text(encoding="utf-8"))
    approval = json.loads((SRC / "gates/architecture-approval.json").read_text(encoding="utf-8"))
    from scripts import survey_production_v2 as core
    arch_sha = core.sha256_file(SRC / "architecture-v2.json")
    appr_sha = core.sha256_file(SRC / "gates/architecture-approval.json")
    mx_sha = core.sha256_file(SRC / "candidate-matrix-v2.json")
    ev_sha = core.sha256_file(ev_acc)

    new_entries = []
    refreshed = []
    for e in old["entries"]:
        e2 = dict(e)
        meta = by_task[e["evidence_task_id"]]
        raw = (ev_acc.parent / "results" / meta["filename"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == meta["sha256"], e["evidence_task_id"]
        if e2["evidence_sha256"] != meta["sha256"]:
            # only the r7-corrected cards may differ (VM-D108 for P15; VM-D010 if referenced)
            assert e["discovery_id"] in ("VM-D108", "VM-D010"), e["discovery_id"]
            e2["evidence_sha256"] = meta["sha256"]
            refreshed.append(e["discovery_id"])
        for k in ("architecture_sha256", "architecture_approval_sha256",
                  "candidate_matrix_sha256", "evidence_acceptance_sha256"):
            e2[k] = {"architecture_sha256": arch_sha, "architecture_approval_sha256": appr_sha,
                     "candidate_matrix_sha256": mx_sha, "evidence_acceptance_sha256": ev_sha}[k]
        new_entries.append(e2)

    # New §11 entry: P07A consumer <- VM-D114 (canonical home P06 PRIMARY)
    meta114 = by_task["evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e"]
    card114 = json.loads((ev_acc.parent / "results" / meta114["filename"]).read_text(encoding="utf-8"))
    subj114 = card114["artifact"]["primary_subject_id"]
    assert meta114["discovery_ids"] == ["VM-D114"] and meta114["status"] == "VERIFIED"
    sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
    mx = json.loads((SRC / "candidate-matrix-v2.json").read_text(encoding="utf-8"))
    cand114 = next(r["candidate_id"] for r in mx["rows"] if r["discovery_ids"] == ["VM-D114"])
    disp114 = next(a["disposition"] for a in sel["assignments"] if a["candidate_id"] == cand114)
    assert disp114 == "SELECTED", disp114
    new_entries.append({
        "consumer_package": "P07A",
        "synthesis_axis": ["p07a_image_level_alignment_lineage"],
        "discovery_id": "VM-D114",
        "candidate_id": cand114,
        "canonical_home_package": "P06",
        "home_architecture_usage": "PRIMARY",
        "all_architecture_usages": [{"package_id": "P06", "usage": "PRIMARY"}],
        "evidence_task_id": "evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e",
        "evidence_sha256": meta114["sha256"],
        "evidence_filename": meta114["filename"],
        "evidence_subject_ids": [subj114],
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
    out["provenance"] = (f"r7 overlay: 30 entries carried from the r6 overlay (r7 authority SHAs "
                         f"re-verified; refreshed {refreshed}; all SELECTED) + new P07A/VM-D114 entry (§11: SigLIP-2 "
                         f"staged-recipe SUPPORTING authority for P07A; canonical home P06 PRIMARY; "
                         f"no Selection/destination change). r7 overlay: 30 entries carried from the r6 overlay (r7 authority SHAs "
                         "re-verified, all SELECTED) + new P07A/VM-D114 entry (§11: SigLIP-2 "
                         "staged-recipe SUPPORTING authority for P07A; canonical home P06 PRIMARY; "
                         "no Selection/destination change).")
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"overlay r7: {len(new_entries)} entries (30 carried + P07A/D114) -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
