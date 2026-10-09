#!/usr/bin/env python3
"""Build the VM-D074 Qwen3-VL-era license-history supplement (Core builder only).

Separates predecessor (2024-09-06, Qwen2-VL era) from Qwen3-VL-era authority
(f0ab724 cutover tree 2025-09-23 + ebd38f4 tree 2025-09-30, same Apache-2.0 bytes).
"""
from __future__ import annotations
import datetime
import hashlib
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
SNAP = f"{EDIR}/snapshots"
OUT = f"{EDIR}/evidence-authority-supplement-vm-d074-history.json"
SUPPLEMENT_ID = "ts003-late-cutoff-supplement-vm-d074-history-20261005"
TID074 = "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"

)

SPECS = [
    ("qwen3-vl-LICENSE-f0ab724.txt",
     "https://raw.githubusercontent.com/QwenLM/Qwen3-VL/f0ab7242ee0cdb24f07167b447b49bb76c7bd88d/LICENSE",
     "Qwen3-VL repo-root LICENSE at cutover commit f0ab724 (2025-09-23, Qwen3-VL era)",
     "Qwen3-VL-era authority: cutover tree lists LICENSE alongside Qwen3-VL README; pinned bytes identical Apache-2.0."),
    ("qwen3-vl-LICENSE-ebd38f4.txt",
     "https://raw.githubusercontent.com/QwenLM/Qwen3-VL/ebd38f447caaee6b85212e2751ca71e629d63fb4/LICENSE",
     "Qwen3-VL repo-root LICENSE at commit ebd38f4 (2025-09-30, pre-cutoff)",
     "Qwen3-VL-era authority: pre-cutoff tree lists LICENSE; pinned bytes identical Apache-2.0; 2024-09-06 commit is predecessor-era history, not the Qwen3-VL-era grant."),
]


def main() -> int:
    root = Path(".").resolve()
    state = core.load_json(root / f"{SRC}/production-state.json")
    profile = core.load_json(root / state["profile"]["path"])
    source_root = root / profile["paths"]["source_root"]
    discovery_path = source_root / "discovery/discovery-v2.jsonl"
    scr_acc = max((source_root / "screening/v2/accepted").glob("*/screening-accepted.json"),
                  key=lambda p: p.stat().st_mtime)
    sources = []
    for fname, locator, title, relation in SPECS:
        raw = root / SNAP / fname
        assert raw.is_file(), fname
        data = raw.read_bytes()
        assert len(data) > 0, fname
        sources.append({
            "supplement_source_id": "supplement-src-" + hashlib.sha256(locator.encode()).hexdigest()[:16],
            "discovery_id": "VM-D074",
            "evidence_task_id": TID074,
            "locator": locator,
            "source_type": "first_party_release_or_docs",
            "source_class": "PRIMARY_OFFICIAL",
            "title": title,
            "published_at": None,
            "accessed_at": NOW,
            "raw_path": f"{SNAP}/{fname}",
            "raw_sha256": hashlib.sha256(data).hexdigest(),
            "byte_count": len(data),
            "relation": relation,
        })
    assert len({s["supplement_source_id"] for s in sources}) == len(sources)
    from scripts import survey_agent_tool_v2 as agent_tool
    with agent_tool.current_stage_basis_override():
        out = evidence.build_evidence_authority_supplement(
            root, ISSUE_ID, source_root, discovery_path, scr_acc, sources,
            root / OUT, supplement_id=SUPPLEMENT_ID,
            implementation_sha=core.repository_commit_sha(root))
    print("supplement:", out.relative_to(root), core.sha256_file(out)[:12])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
