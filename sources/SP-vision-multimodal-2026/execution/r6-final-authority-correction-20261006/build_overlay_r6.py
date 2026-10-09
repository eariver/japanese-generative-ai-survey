#!/usr/bin/env python3
"""Rebuild cross-package synthesis overlay for r6 (refresh 4 stale evidence SHAs).

Same 30 entries / same consumers / same Discovery IDs as the r5 overlay; only
evidence_sha256 refreshed for VM-D065/D070/D071 to the r6 corrected card bytes
(all SELECTED, all SHA-verified). Role CROSS_PACKAGE_SYNTHESIS_REFERENCE.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
OLD = SRC / "execution/content-revision-r5-20261006/cross-package-synthesis-authority.json"
OUT = SRC / "execution/r6-final-authority-correction-20261006/cross-package-synthesis-authority-r6.json"


def main() -> int:
    old = json.loads(OLD.read_text(encoding="utf-8"))
    assert len(old["entries"]) == 30
    ev_acc = max((SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                 key=lambda p: p.stat().st_mtime)
    ev = json.loads(ev_acc.read_text(encoding="utf-8"))
    assert ev_acc.parent.name.startswith("81e3b75b")
    by_task = {r["evidence_task_id"]: r for r in ev["results"]}
    new_entries = []
    refreshed = 0
    for e in old["entries"]:
        e2 = dict(e)
        meta = by_task[e["evidence_task_id"]]
        assert meta["sha256"] == hashlib.sha256(
            (ev_acc.parent / "results" / meta["filename"]).read_bytes()).hexdigest()
        if e2["evidence_sha256"] != meta["sha256"]:
            e2["evidence_sha256"] = meta["sha256"]
            refreshed += 1
        # verify raw bytes + selection role unchanged
        p = ev_acc.parent / "results" / meta["filename"]
        assert hashlib.sha256(p.read_bytes()).hexdigest() == e2["evidence_sha256"]
        new_entries.append(e2)
    assert refreshed == 4, refreshed
    out = dict(old)
    out["entries"] = new_entries
    out["provenance"] = ("r6 refresh of the r5 overlay: identical 30 entries / consumers / Discovery IDs; "
                         "evidence_sha256 refreshed for VM-D065 (P06+P15), VM-D070 (P15), VM-D071 (P15) "
                         "to corrected r6 card bytes; all SELECTED + SHA-verified; no Selection change.")
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"overlay r6: 30 entries, {refreshed} SHAs refreshed -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
