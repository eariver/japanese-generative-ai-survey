#!/usr/bin/env python3
"""Build source-body-access-ledger.json for TS-002 Evidence r2.

One row per Evidence task: discovery ID, task ID, source type, locator,
access status, body sections consumed, source-body vs summary-only flag,
final verification status, access barrier if any.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(".").resolve()
OUTDIR = ROOT / "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2"
COMPAT = ROOT / "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat/compat-package/package.json"
DISC = ROOT / "sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl"


def load_data():
    spec = importlib.util.spec_from_file_location(
        "r2input", ROOT / "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/make_evidence_input_r2.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DATA


def main() -> None:
    package = json.loads((ROOT / COMPAT).read_text(encoding="utf-8"))
    task_by_disc = {m["discovery_ids"][0]: m for m in package["tasks"]}
    recs = {}
    for line in DISC.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            recs[r["discovery_id"]] = r
    r2in = json.loads((OUTDIR / "evidence-interactive-input-r2.json").read_text(encoding="utf-8"))
    ver_by_disc = {}
    for row in r2in["records"]:
        fb = [v for v in row["verification"] if v["target"] == "Evidence-stage full-body verification"]
        ver_by_disc[row["discovery_id"]] = (row["status"], fb[0] if fb else None)
    DATA = load_data()
    rows = []
    for did in sorted(recs):
        rd = DATA[did]
        rec = recs[did]
        status, fb = ver_by_disc[did]
        body_flag = rd["access"] == "FULL"
        barrier = None
        if rd["access"] != "FULL":
            barrier = rd["sections"]
        rows.append({
            "discovery_id": did,
            "evidence_task_id": task_by_disc[did]["evidence_task_id"],
            "source_type": rec["source"]["source_type"],
            "locator": rec["source"]["locator"],
            "corrected_body_id": rd.get("corrected"),
            "access_status": rd["access"],
            "body_sections_consumed": rd["sections"],
            "source_body_consumed": body_flag,
            "summary_only": not body_flag,
            "final_status": status,
            "full_body_verification": fb["status"] if fb else None,
            "access_barrier": barrier,
        })
    (OUTDIR / "source-body-access-ledger.json").write_text(
        json.dumps({"schema_version": "1.0", "issue_id": "SP-beyond-text-2026",
                    "rows": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(json.dumps({"rows": len(rows),
                      "access": dict(Counter(r["access_status"] for r in rows)),
                      "body_consumed": sum(1 for r in rows if r["source_body_consumed"]),
                      "final": dict(Counter(r["final_status"] for r in rows))}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
