#!/usr/bin/env python3
"""Build the r6-final authority supplement: union-121 (22 entries) + VQA-v2 (1 entry).

Frozen Core only. Validates via canonical build_evidence_authority_supplement.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
OLD = SRC / "execution/obligation-realization-r5-20261005/evidence-authority-supplement-union-121.json"
OUT = SRC / "execution/r6-final-authority-correction-20261006/evidence-authority-supplement-r6final.json"
RAW_REL = "sources/SP-vision-multimodal-2026/execution/r6-final-authority-correction-20261006/snapshots/arxiv-1612.00837-v3.html"


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as evidence
    from scripts import survey_agent_tool_v2 as agent_tool
    from scripts import survey_production_v2 as core

    old = core.load_json(OLD)
    assert len(old["sources"]) == 22, len(old["sources"])
    existing_ids = {s["supplement_source_id"] for s in old["sources"]}
    new_id = "supplement-src-2931815e4c48399b"
    assert new_id not in existing_ids

    raw_path = ROOT / RAW_REL
    assert raw_path.is_file() and not raw_path.is_symlink()
    raw_sha = core.sha256_file(raw_path)
    byte_count = raw_path.stat().st_size
    assert byte_count == 216781, byte_count
    print("raw:", RAW_REL, byte_count, raw_sha[:12])

    new_entry = {
        "supplement_source_id": new_id,
        "discovery_id": "VM-D038",
        "evidence_task_id": "evidence:SP-vision-multimodal-2026:25a1e7517b74ec98",
        "locator": "https://arxiv.org/abs/1612.00837",
        "source_type": "arxiv_primary",
        "source_class": "PRIMARY_PAPER",
        "title": "Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering (Goyal et al.)",
        "published_at": "2016-12-02T00:00:00Z",
        "accessed_at": "2026-10-07T01:30:00Z",
        "raw_path": RAW_REL,
        "raw_sha256": raw_sha,
        "byte_count": byte_count,
        "relation": "VQA-v2 balancing authority for VM-D038 source enrichment (existing candidate, NOT new Discovery): language priors / answer-prior bias mitigation via complementary image pairs (same question + similar images + different answers); balanced-dataset construction.",
    }
    sources = list(old["sources"]) + [new_entry]

    state_path = SRC / "production-state.json"
    state = core.load_json(state_path)
    assert state["lifecycle_state"] == "CANDIDATES_NORMALIZED"
    profile = core.load_json(SRC / "production-profile.json")
    source_root = ROOT / profile["paths"]["source_root"]
    disc_path = ROOT / "sources/SP-vision-multimodal-2026/discovery/discovery-v2.jsonl"
    # screening acceptance is pinned by the last accepted evidence package basis (deterministic)
    curr_pkg = core.load_json(ROOT / "sources/SP-vision-multimodal-2026/evidence/v2/accepted/68be75fd39fc35df04abe32757d7dbe3f6d8b6a23418007c78e9688e003da2e3/package.json")
    scr_acc = ROOT / curr_pkg["basis"]["screening_acceptance_path"]
    impl = core.repository_commit_sha(ROOT)

    out = None
    with agent_tool.current_stage_basis_override():
        out = evidence.build_evidence_authority_supplement(
            ROOT, "SP-vision-multimodal-2026", source_root, disc_path, scr_acc,
            sources, OUT,
            supplement_id="ts003-r6final-authority-supplement-20261006",
            implementation_sha=impl,
        )
    print("supplement built:", out.relative_to(ROOT))
    manifest = core.load_json(out)
    assert len(manifest["sources"]) == 23
    print("entries: 23 (22 carried + 1 VQA-v2)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
