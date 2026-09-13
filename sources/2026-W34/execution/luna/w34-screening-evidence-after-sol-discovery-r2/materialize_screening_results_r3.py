#!/usr/bin/env python3
"""Materialize Screening batch results for r3 from fresh decisions."""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(".").resolve()
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
DECISIONS_PATH = REPO / EXEC_REL / "screening-basis/fresh-screening-decisions.json"
PACKAGE_PATH = REPO / "sources/2026-W34/screening/v2/prepared/w34-event-screening-r3/package.json"
RESULTS_DIR = REPO / "sources/2026-W34/screening/v2/prepared/w34-event-screening-r3/results"

def load_json(p): return json.loads(p.read_text(encoding="utf-8"))
def read_jsonl(p): return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]

def main():
    from scripts import survey_screening_v2 as screening
    from scripts import survey_production_v2 as core
    package = load_json(PACKAGE_PATH)
    doc = load_json(DECISIONS_PATH)
    by_id = {d["discovery_id"]: d for d in doc["decisions"]}
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    for batch in package["input"]["batches"]:
        batch_id = batch["batch_id"]
        batch_path = PACKAGE_PATH.parent / batch["path"]
        records = read_jsonl(REPO / batch_path.relative_to(REPO) if not batch_path.is_absolute() else batch_path)
        # Actually batch path is relative to package dir: input/batches/...
        # PACKAGE_PATH.parent / batch["path"] is correct
        rows = []
        for rec in records:
            did = rec["discovery_id"]
            if did not in by_id:
                raise ValueError(f"missing decision {did}")
            rows.append(by_id[did])
        basis = screening.expected_result_basis(REPO, PACKAGE_PATH, package, batch)
        result = {
            "schema_version": "2.0-rc1",
            "issue_id": package["issue_id"],
            "batch_id": batch_id,
            "basis": basis,
            "decisions": rows,
        }
        out = RESULTS_DIR / f"{batch_id}.json"
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {out} {len(rows)} decisions")
    print("done")

if __name__ == "__main__":
    raise SystemExit(main())
