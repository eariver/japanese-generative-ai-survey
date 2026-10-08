#!/usr/bin/env python3
"""Build evidence-authority-supplement-union-125.json for the P02 bridge intake.

Carries the r6final supplement's 23 authority sources verbatim, rebound to the
current Discovery (125) + Screening (125, cdf7a075) SHAs. No new supplement
sources: the 3 new cards cite Discovery-bounded src-1 locators only.
"""
from __future__ import annotations
import json
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
R6FINAL = f"{SRC}/execution/r6-final-authority-correction-20261006/evidence-authority-supplement-r6final.json"
OUT = f"{EDIR}/evidence-authority-supplement-union-125.json"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    impl = core.repository_commit_sha(root)
    base = core.load_json(root / R6FINAL)
    assert len(base["sources"]) == 23, len(base["sources"])

    scr_acc_path = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                       key=lambda p: p.stat().st_mtime)
    scr_acc = core.load_json(scr_acc_path)
    assert scr_acc["record_count"] == 125, scr_acc["record_count"]

    union = {
        "schema_version": "2.0-rc1",
        "supplement_id": "ts003-p02-bridge-supplement-union-20261008",
        "issue_id": ISSUE_ID,
        "basis": {
            "source_root": f"sources/{ISSUE_ID}",
            "discovery_path": f"sources/{ISSUE_ID}/discovery/discovery-v2.jsonl",
            "discovery_sha256": core.sha256_file(root / SRC / "discovery/discovery-v2.jsonl"),
            "screening_acceptance_path": str(scr_acc_path.relative_to(root)),
            "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
        },
        "sources": base["sources"],
    }
    out_path = root / OUT
    assert not out_path.exists()
    core.write_json(out_path, union)
    with agent_tool.current_stage_basis_override():
        evidence.validate_evidence_authority_supplement(
            root, out_path, impl, expected_issue_id=ISSUE_ID,
            expected_discovery_path=root / SRC / "discovery/discovery-v2.jsonl",
            expected_screening_acceptance_path=scr_acc_path)
    # every row must still point at an existing non-DROP task under the new acceptance
    dec = {d["discovery_id"]: d["decision"] for d in scr_acc["decisions"]}
    for s in union["sources"]:
        assert s["discovery_id"] in dec and dec[s["discovery_id"]] != "DROP", s["discovery_id"]
    print("union supplement:", out_path.relative_to(root), "| sources:", len(union["sources"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
