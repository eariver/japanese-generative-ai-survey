#!/usr/bin/env python3
"""W41 edition-local derived r2 Evidence package builder, r5 guarded revision.

SC-E41-05 hardening of build_r2_package.py: enforces the EXACT nine
(Discovery ID, Evidence Task ID, original source_type) allowlist from the
reviewed r4 projection ledger. Aborts (before any authoritative write) on:
 - a tenth/unexpected SECONDARY_OBSERVATION source,
 - a missing expected allowlist member,
 - any derived-vs-original Task diff beyond (a) the nine source_type
   projections and (b) the eight supplement-binding attachments recorded in
   the r4 supplement manifest,
 - unknown source_type values.
Original r4 builder SHA remains in git history. No shared-Core modification.
Deterministic double-build required.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO))
from scripts import survey_production_v2 as core  # noqa: E402 read-only use

import os as _os
R1 = Path(_os.environ.get("R5_R1", REPO / "sources/2026-W41/evidence/v2/packages/r1"))
R2 = REPO / "sources/2026-W41/evidence/v2/packages/r2"
SUPP = REPO / "sources/2026-W41/external/evidence-supplement/evidence-authority-supplement-r4.json"
SUPPLEMENT_SCHEMA = Path("schemas/evidence-authority-supplement-v2.schema.json")
LEDGER = Path(_os.environ.get("R5_LEDGER", REPO / "sources/2026-W41/execution/compat/evidence-source-class-projection-r4/projection-ledger.json"))

def _task_diff_keys(orig: dict, new: dict, path: str = "") -> list[str]:
    """Field paths that differ between original and derived task JSON."""
    diffs: list[str] = []
    if isinstance(orig, dict) and isinstance(new, dict):
        for k in set(orig) | set(new):
            diffs.extend(_task_diff_keys(orig.get(k), new.get(k), f"{path}.{k}" if path else k))
    elif isinstance(orig, list) and isinstance(new, list):
        if len(orig) != len(new):
            diffs.append(f"{path}[len {len(orig)}->{len(new)}]")
        else:
            for i, (a, b) in enumerate(zip(orig, new)):
                diffs.extend(_task_diff_keys(a, b, f"{path}[{i}]"))
    elif orig != new:
        diffs.append(path)
    return diffs

def main(out_dir: Path = R2) -> dict:
    ledger = json.loads(LEDGER.read_bytes())
    allow = {(r["discovery_id"], r["evidence_task_id"], r["original_source_type"]) for r in ledger["rows"]
             if r["projection_rule"] != "W41MAP:passthrough"}
    assert len(allow) == 9, f"ledger must authorize exactly nine, found {len(allow)}"
    r1pkg = json.loads((R1 / "package.json").read_bytes())
    supp = json.loads(SUPP.read_bytes())
    by_task: dict[str, list[str]] = {}
    for e in supp["sources"]:
        by_task.setdefault(e["evidence_task_id"], []).append(e["supplement_source_id"])
    for v in by_task.values():
        v.sort()
    seen_allow: set[tuple[str, str, str]] = set()
    task_metas = []
    for meta in r1pkg["tasks"]:
        task = json.loads((R1 / meta["path"]).read_bytes())
        did = task["discovery_ids"][0]
        tid = task["evidence_task_id"]
        st = task["source_records"][0]["source_type"]
        if st == "SECONDARY_OBSERVATION":
            key = (did, tid, st)
            if key not in allow:
                raise ValueError(f"SC-E41-05 GUARD: unexpected tenth/unlisted SECONDARY_OBSERVATION {did}/{tid}; STOP")
            seen_allow.add(key)
            task["source_records"][0]["source_type"] = "SECONDARY"
        elif st not in ("PRIMARY_OFFICIAL", "SECONDARY", "x-community-signal"):
            raise ValueError(f"SC-E41-05 GUARD: unrecognized source_type {st!r} on {did}; STOP")
        tids = by_task.get(tid)
        if tids:
            task["authority_supplement_source_ids"] = tids
        # allowed-diff audit: only projection + supplement attachment may differ
        orig = json.loads((R1 / meta["path"]).read_bytes())
        diffs = _task_diff_keys(orig, task)
        allowed_prefixes = {"source_records[0].source_type", "authority_supplement_source_ids"}
        bad = [d for d in diffs if d not in allowed_prefixes]
        if bad:
            raise ValueError(f"SC-E41-05 GUARD: non-authority Task change on {did}: {bad}; STOP")
        blob = core.json_bytes(task)
        dest = out_dir / meta["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
        m2 = {"evidence_task_id": tid, "path": meta["path"],
              "sha256": hashlib.sha256(blob).hexdigest(), "discovery_ids": list(meta["discovery_ids"])}
        if tids:
            m2["authority_supplement_source_ids"] = tids
        task_metas.append(m2)
    if seen_allow != allow:
        raise ValueError(f"SC-E41-05 GUARD: allowlist members missing: {sorted(allow - seen_allow)}; STOP")
    pkg = dict(r1pkg)
    pkg["tasks"] = task_metas
    pkg["authority_supplement"] = {"path": "sources/2026-W41/external/evidence-supplement/evidence-authority-supplement-r4.json",
                                   "sha256": core.sha256_file(SUPP)}
    contracts = dict(pkg["contracts"])
    contracts["supplement"] = {"path": str(SUPPLEMENT_SCHEMA), "sha256": core.sha256_file(REPO / SUPPLEMENT_SCHEMA)}
    pkg["contracts"] = contracts
    pkg["rules"] = list(r1pkg["rules"]) + ["Post-Screening authority is eligible only through an exact validated Evidence Authority Supplement source ID bound to this task."]
    (out_dir / "package.json").write_bytes(core.json_bytes(pkg))
    return {"tasks": len(task_metas)}

if __name__ == "__main__":
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else R2
    print(main(dest))
