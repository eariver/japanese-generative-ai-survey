#!/usr/bin/env python3
"""W41 edition-local derived r2 Evidence package builder (r4).

Inputs: r1 package (immutable), projection ledger (W41MAP), r4 supplement manifest.
Output: evidence/v2/packages/r2 with 36 derived task copies:
 - exactly-nine source_records[0].source_type projection (SECONDARY_OBSERVATION->SECONDARY);
 - authority_supplement_source_ids attached per supplement manifest bindings;
 - package authority_supplement + contracts.supplement; recomputed task SHAs.
No shared-Core modification. Deterministic double-build required.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO))
from scripts import survey_production_v2 as core  # noqa: E402 read-only use

R1 = REPO / "sources/2026-W41/evidence/v2/packages/r1"
R2 = REPO / "sources/2026-W41/evidence/v2/packages/r2"
SUPP = REPO / "sources/2026-W41/external/evidence-supplement/evidence-authority-supplement-r4.json"
SUPPLEMENT_SCHEMA = Path("schemas/evidence-authority-supplement-v2.schema.json")

def main(out_dir: Path = R2) -> dict:
    r1pkg = json.loads((R1 / "package.json").read_bytes())
    supp = json.loads(SUPP.read_bytes())
    by_task: dict[str, list[str]] = {}
    for e in supp["sources"]:
        by_task.setdefault(e["evidence_task_id"], []).append(e["supplement_source_id"])
    for v in by_task.values():
        v.sort()
    task_metas = []
    for meta in r1pkg["tasks"]:
        src = R1 / meta["path"]
        task = json.loads(src.read_bytes())
        did = task["discovery_ids"][0]
        st = task["source_records"][0]["source_type"]
        if st == "SECONDARY_OBSERVATION":
            task["source_records"][0]["source_type"] = "SECONDARY"
        tids = by_task.get(task["evidence_task_id"])
        if tids:
            task["authority_supplement_source_ids"] = tids
        blob = core.json_bytes(task)
        dest = out_dir / meta["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
        m2 = {"evidence_task_id": meta["evidence_task_id"], "path": meta["path"],
              "sha256": hashlib.sha256(blob).hexdigest(), "discovery_ids": list(meta["discovery_ids"])}
        if tids:
            m2["authority_supplement_source_ids"] = tids
        task_metas.append(m2)
    pkg = dict(r1pkg)
    pkg["tasks"] = task_metas
    pkg["authority_supplement"] = {"path": "sources/2026-W41/external/evidence-supplement/evidence-authority-supplement-r4.json",
                                   "sha256": core.sha256_file(SUPP)}
    contracts = dict(pkg["contracts"])
    contracts["supplement"] = {"path": str(SUPPLEMENT_SCHEMA), "sha256": core.sha256_file(REPO / SUPPLEMENT_SCHEMA)}
    pkg["contracts"] = contracts
    pkg["rules"] = list(r1pkg["rules"]) + ["Post-Screening authority is eligible only through an exact validated Evidence Authority Supplement source ID bound to this task."]
    (out_dir / "package.json").write_bytes(core.json_bytes(pkg))
    return {"tasks": len(task_metas),
            "projected": sum(1 for m in task_metas if json.loads((out_dir / m["path"]).read_bytes())["source_records"][0]["source_type"] == "SECONDARY"
                             and json.loads((R1 / m["path"]).read_bytes())["source_records"][0]["source_type"] == "SECONDARY_OBSERVATION"),
            "supplemented": sum(1 for m in task_metas if "authority_supplement_source_ids" in m)}

if __name__ == "__main__":
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else R2
    print(main(dest))
