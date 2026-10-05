#!/usr/bin/env python3
"""Build (or verify) the replay union supplement manifest (22 entries).

Idempotent: if the manifest exists with the exact expected entry set and fresh
basis, it is reused as-is; otherwise it is (re)built via Core validation.
"""
from __future__ import annotations
import json
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
UNION = f"{EDIR}/evidence-authority-supplement-union-120.json"
UNION_ID = "ts003-late-cutoff-supplement-union-20261005"

SUPPLEMENT_FILES = [
    f"{SRC}/execution/architecture-r3-intake-20261003/evidence-authority-supplement-112.json",
    f"{SRC}/execution/vm-d077-authority-repair-20261004/evidence-authority-supplement-vm-d077.json",
    f"{SRC}/execution/license-authority-repair-r5-20261004/evidence-authority-supplement-vm-d074.json",
    f"{SRC}/execution/license-authority-repair-r5-20261004/evidence-authority-supplement-vm-d075.json",
    f"{EDIR}/evidence-authority-supplement-vm-d074-history.json",
    f"{EDIR}/evidence-authority-supplement-vm-d075-omni.json",
]


def build_union(root: Path) -> Path:
    state = core.load_json(root / f"{SRC}/production-state.json")
    profile = core.load_json(root / state["profile"]["path"])
    source_root = root / profile["paths"]["source_root"]
    discovery_path = source_root / "discovery/discovery-v2.jsonl"
    scr_acc = max((source_root / "screening/v2/accepted").glob("*/screening-accepted.json"),
                  key=lambda p: p.stat().st_mtime)
    union_sources = []
    for rel in SUPPLEMENT_FILES:
        m = core.load_json(root / rel)
        union_sources.extend(m["sources"])
    assert len(union_sources) == 26, len(union_sources)
    assert len({s["supplement_source_id"] for s in union_sources}) == 26
    payload = {
        "schema_version": "2.0-rc1",
        "supplement_id": UNION_ID,
        "issue_id": ISSUE_ID,
        "basis": {
            "source_root": SRC,
            "discovery_path": str((source_root / "discovery/discovery-v2.jsonl").relative_to(root)),
            "discovery_sha256": core.sha256_file(discovery_path),
            "screening_acceptance_path": str(scr_acc.relative_to(root)),
            "screening_acceptance_sha256": core.sha256_file(scr_acc),
        },
        "sources": union_sources,
    }
    out = root / UNION
    if out.exists():
        cur = core.load_json(out)
        if cur == payload:
            print("union manifest reused:", out.relative_to(root))
            return out
        raise ValueError("existing union manifest differs; refusing divergent overwrite")
    schema_gate.validate_instance(
        payload, root / "schemas/evidence-authority-supplement-v2.schema.json",
        label="Evidence Authority Supplement (union-120)")
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        from scripts import survey_agent_tool_v2 as agent_tool
        with agent_tool.current_stage_basis_override():
            evidence.validate_evidence_authority_supplement(
                root, out, core.repository_commit_sha(root), expected_issue_id=ISSUE_ID,
                expected_source_root=source_root,
                expected_discovery_path=discovery_path,
                expected_screening_acceptance_path=scr_acc)
    except Exception:
        out.unlink(missing_ok=True)
        raise
    print("union manifest built:", out.relative_to(root), core.sha256_file(out)[:12])
    return out


def main() -> int:
    root = Path(".").resolve()
    build_union(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
