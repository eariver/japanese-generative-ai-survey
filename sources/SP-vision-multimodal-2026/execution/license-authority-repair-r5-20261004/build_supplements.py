#!/usr/bin/env python3
"""Build VM-D074 + VM-D075 dedicated Evidence Authority Supplements (Core builder only).

Snapshots: exact first-party bytes (repo LICENSE current + pinned historical;
model-card README current + pinned initial), hash-bound. No VM-D112 supplement reuse.
Staged under execution/license-authority-repair-r5-20261004/.
"""
from __future__ import annotations
import datetime
import hashlib
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/license-authority-repair-r5-20261004"
SNAP = f"{EDIR}/snapshots"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

TID074 = "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"

SPECS074 = [
    ("qwen3-vl-LICENSE-main.txt", "https://raw.githubusercontent.com/QwenLM/Qwen3-VL/main/LICENSE",
     "Qwen3-VL repo-root LICENSE (current; Apache-2.0)",
     "Code license bucket: repo-root LICENSE full Apache-2.0 text as served today."),
    ("qwen3-vl-LICENSE-e8c6dfb.txt", "https://raw.githubusercontent.com/QwenLM/Qwen3-VL/e8c6dfbe0472e567b1bedc7640f550e0e506429f/LICENSE",
     "Qwen3-VL repo-root LICENSE at commit e8c6dfb (2024-09-06, single LICENSE commit)",
     "Code license pre-cutoff proof: byte-identical Apache-2.0 text since 2024-09-06, ~2y before 2026-09-30."),
    ("qwen3-vl-8b-readme-main.md", "https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/raw/main/README.md",
     "Qwen3-VL-8B-Instruct model-card README (current; license apache-2.0)",
     "Weight license bucket: card frontmatter license apache-2.0 for the released 8B-Instruct artifact."),
    ("qwen3-vl-8b-readme-fe33404.md", "https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/resolve/fe3340460dc1b2245a90d1b3b608bc86ffb3bfd6/README.md",
     "Qwen3-VL-8B-Instruct model-card README at commit fe33404 (2025-10-11 weight upload)",
     "Weight license pre-cutoff proof: license apache-2.0 declared from creation, ~11.5mo before cutoff; 4B sibling mirrors."),
]

SPECS075 = [
    ("qwen3-omni-LICENSE-main.txt", "https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/main/LICENSE",
     "Qwen3-Omni repo-root LICENSE (current; Apache-2.0)",
     "Code license bucket: repo-root LICENSE full Apache-2.0 text as served today."),
    ("qwen3-omni-LICENSE-ae5dbf9.txt", "https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/ae5dbf9e734b7c72c1a70805cfb321b5fa3e9615/LICENSE",
     "Qwen3-Omni repo-root LICENSE at commit ae5dbf9 (2025-09-22 inception)",
     "Code license pre-cutoff proof: byte-identical Apache-2.0 text since repo inception, ~1y before cutoff."),
    ("qwen3-omni-30b-readme-main.md", "https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/main/README.md",
     "Qwen3-Omni-30B-A3B-Instruct model-card README (current; license_name apache-2.0)",
     "Weight license bucket: current header license_name apache-2.0 for the released 30B-A3B-Instruct artifact."),
    ("qwen3-omni-30b-readme-302ffa9.md", "https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/302ffa9/README.md",
     "Qwen3-Omni-30B-A3B-Instruct model-card README at commit 302ffa9 (2025-09-20 initial)",
     "Weight license pre-cutoff proof: license apache-2.0 from Sep 20 2025 release; bound artifact model-00001-of-00015.safetensors; no generalization beyond checked card."),
]


def build(root: Path, did: str, tid: str, specs: list, out_name: str, supp_id: str,
          source_root: Path, discovery_path: Path, scr_acc: Path) -> Path:
    from scripts import survey_agent_tool_v2 as agent_tool
    sources = []
    for fname, locator, title, relation in specs:
        raw = root / SNAP / fname
        assert raw.is_file(), fname
        data = raw.read_bytes()
        assert len(data) > 0, fname
        sources.append({
            "supplement_source_id": "supplement-src-" + hashlib.sha256(locator.encode()).hexdigest()[:16],
            "discovery_id": did,
            "evidence_task_id": tid,
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
    with agent_tool.current_stage_basis_override():
        out = evidence.build_evidence_authority_supplement(
            root, ISSUE_ID, source_root, discovery_path, scr_acc, sources,
            root / EDIR / out_name, supplement_id=supp_id,
            implementation_sha=core.repository_commit_sha(root))
    print("supplement:", out.relative_to(root), core.sha256_file(out)[:12], "| sources:", len(sources))
    return out


def main() -> int:
    root = Path(".").resolve()
    state = core.load_json(root / f"{SRC}/production-state.json")
    profile = core.load_json(root / state["profile"]["path"])
    source_root = root / profile["paths"]["source_root"]
    discovery_path = source_root / "discovery/discovery-v2.jsonl"
    scr_acc = max((source_root / "screening/v2/accepted").glob("*/screening-accepted.json"),
                  key=lambda p: p.stat().st_mtime)
    build(root, "VM-D074", TID074, SPECS074,
          "evidence-authority-supplement-vm-d074.json",
          "ts003-license-repair-supplement-vm-d074-20261005",
          source_root, discovery_path, scr_acc)
    build(root, "VM-D075", TID075, SPECS075,
          "evidence-authority-supplement-vm-d075.json",
          "ts003-license-repair-supplement-vm-d075-20261005",
          source_root, discovery_path, scr_acc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
