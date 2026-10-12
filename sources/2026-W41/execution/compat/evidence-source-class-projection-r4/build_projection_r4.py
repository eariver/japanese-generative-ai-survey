#!/usr/bin/env python3
"""W41 edition-local Evidence source-class projection builder (r4).

Derives a compat task package from r1 package bytes: for EXACTLY the nine
known SECONDARY_OBSERVATION tasks, projects source_records[0].source_type to
SECONDARY (identical secondary strength; sibling classes carryover_recheck /
sol_working_set_observation / prior-week-authority already map there).
All other bytes preserved. No shared-Core modification. Deterministic
double-build required; unknown types fail closed (never projected).
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO))
from scripts import survey_production_v2 as core  # noqa: E402  (read-only use: json_bytes/sha)

R1 = REPO / "sources/2026-W41/evidence/v2/packages/r1"
OUT = REPO / "sources/2026-W41/execution/compat/evidence-source-class-projection-r4/compat-package"
KNOWN_NINE = {
    "w41-dailyx-agr-20261006", "w41-dailyx-nemotron-hf-20261006",
    "w41-dailyx-nace-drex-20261010", "w41-dailyx-nace-ndi-20261010",
    "w41-dailyx-elevenlabs-20261010", "w41-hold-tencent-20261011",
    "w41-hold-pixelcanary-20261011", "w41-hold-tbcvideo-20261011",
    "w41-weak-elyza-rsi-20261002",
}

def main(out_dir: Path = OUT) -> dict:
    r1_pkg = json.loads((R1 / "package.json").read_bytes())
    rows = []
    for meta in r1_pkg["tasks"]:
        did = meta["discovery_ids"][0]
        src = R1 / meta["path"]
        orig_bytes = src.read_bytes()
        task = json.loads(orig_bytes)
        st = task["source_records"][0]["source_type"]
        if did in KNOWN_NINE:
            if st != "SECONDARY_OBSERVATION":
                raise ValueError(f"known-nine task {did} has unexpected source_type {st!r}; STOP")
            task["source_records"][0]["source_type"] = "SECONDARY"
            new_bytes = core.json_bytes(task)
            rule = "W41MAP:SECONDARY_OBSERVATION->SECONDARY"
        else:
            if st == "SECONDARY_OBSERVATION":
                raise ValueError(f"unlisted SECONDARY_OBSERVATION task {did}; STOP (closed set violated)")
            new_bytes = orig_bytes
            rule = "W41MAP:passthrough"
        dest = out_dir / meta["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(new_bytes)
        rows.append({
            "discovery_id": did,
            "evidence_task_id": meta["evidence_task_id"],
            "original_source_type": st,
            "projected_source_type": task["source_records"][0]["source_type"] if did in KNOWN_NINE else st,
            "original_task_sha256": hashlib.sha256(orig_bytes).hexdigest(),
            "projected_task_sha256": hashlib.sha256(new_bytes).hexdigest(),
            "locator": task["source_records"][0]["locator"],
            "projection_rule": rule,
            "role_note": ("identical secondary strength; sibling classes carryover_recheck/sol_working_set_observation already SECONDARY"
                          if did in KNOWN_NINE else "natively supported frozen Core class"),
        })
    return {"rows": rows,
            "projected": sum(1 for r in rows if r["projection_rule"] != "W41MAP:passthrough"),
            "passthrough": sum(1 for r in rows if r["projection_rule"] == "W41MAP:passthrough")}

if __name__ == "__main__":
    import sys as _s
    dest = Path(_s.argv[1]) if len(_s.argv) > 1 else OUT
    info = main(dest)
    print(f"tasks={len(info['rows'])} projected={info['projected']} passthrough={info['passthrough']}")
