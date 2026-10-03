#!/usr/bin/env python3
"""Build technical-depth-coverage-r11.json from hand-audited node data + r11 blocks.

Machine-readable audit: per Architecture node depth class, reader block binding,
Evidence binding (derived from actual r11 block refs), 8-field coverage, disposition.
"""
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R11 = ED / "reader-editorial-authority-r11.json"
ARCH = SRC / "architecture-v2.json"
OUT = ED / "technical-depth-coverage-r11.json"
DATA = [ED / "r11-coverage-data-a.json", ED / "r11-coverage-data-b.json"]


def main() -> int:
    r11 = json.loads(R11.read_text(encoding="utf-8"))
    arch = json.loads(ARCH.read_text(encoding="utf-8"))
    assert r11["reader_editorial_revision"] == "r11"

    # Architecture node inventory per package.
    arch_nodes = {}
    for p in arch["packages"]:
        dc = p.get("publication_extensions", {}).get("depth_classes", {})
        inv = {}
        for cls in ("FULL_MECHANISM_TREATMENT", "TRANSITION_NODE_TREATMENT",
                    "BRIEF_CONTEXT_OR_AUTHORITY"):
            for n in dc.get(cls, []):
                inv[n] = cls
        arch_nodes[p["package_id"]] = inv

    # r11 block index.
    blocks = {}
    for p in r11["reader_packages"]:
        for b in p["ordered_blocks"]:
            blocks[(p["package_id"], b["block_id"])] = b

    nodes = []
    for df in DATA:
        nodes.extend(json.loads(df.read_text(encoding="utf-8"))["nodes"])

    # Completeness: every Architecture node covered exactly once.
    seen = {}
    for n in nodes:
        key = (n["package_id"], n["node_id"])
        assert key not in seen, f"dup {key}"
        seen[key] = n
        assert n["node_id"] in arch_nodes[n["package_id"]], f"unknown node {key}"
        assert arch_nodes[n["package_id"]][n["node_id"]] == n["depth_class"], \
            f"class mismatch {key}"
    for pid, inv in arch_nodes.items():
        missing = [x for x in inv if (pid, x) not in seen]
        assert not missing, f"{pid} missing {missing}"

    entries = []
    for n in nodes:
        pid = n["package_id"]
        assert len(n["coverage"]) == 8, n["node_id"]
        refs, rids = [], []
        for bid in n["reader_block_ids"]:
            b = blocks.get((pid, bid))
            assert b is not None, f"block miss {pid} {bid}"
            assert b["block_type"] == "PARAGRAPH", f"non-paragraph {pid} {bid}"
            for r in b.get("evidence_refs", []) or []:
                if r["evidence_task_id"] not in rids:
                    rids.append(r["evidence_task_id"])
                    refs.append(r)
        assert rids, f"{pid} {n['node_id']} binds no evidence"
        assert n["disposition"] in ("ADEQUATE", "PARTIAL", "DEPTH_EVIDENCE_GAP"), n
        entries.append({
            "package_id": pid,
            "node_id": n["node_id"],
            "technique": n["technique"],
            "depth_class": n["depth_class"],
            "reader_block_ids": n["reader_block_ids"],
            "evidence_refs": refs,
            "coverage": n["coverage"],
            "disposition": n["disposition"],
            "notes": n["notes"],
        })

    def count(cls, disp):
        return sum(1 for e in entries if e["depth_class"] == cls and e["disposition"] == disp)

    doc = {
        "schema_version": "1.0",
        "issue_id": "SP-vision-multimodal-2026",
        "reader_authority": "reader-editorial-authority-r11.json",
        "reader_authority_sha256": hashlib.sha256(R11.read_bytes()).hexdigest(),
        "status": "TECHNICAL_DEPTH_RESTORATION_CANDIDATE / SOL_REVIEW_REQUIRED",
        "summary": {
            "total_nodes": len(entries),
            "FULL_MECHANISM_TREATMENT": {
                "ADEQUATE": count("FULL_MECHANISM_TREATMENT", "ADEQUATE"),
                "PARTIAL": count("FULL_MECHANISM_TREATMENT", "PARTIAL"),
                "DEPTH_EVIDENCE_GAP": count("FULL_MECHANISM_TREATMENT", "DEPTH_EVIDENCE_GAP")},
            "TRANSITION_NODE_TREATMENT": {
                "ADEQUATE": count("TRANSITION_NODE_TREATMENT", "ADEQUATE"),
                "PARTIAL": count("TRANSITION_NODE_TREATMENT", "PARTIAL"),
                "DEPTH_EVIDENCE_GAP": count("TRANSITION_NODE_TREATMENT", "DEPTH_EVIDENCE_GAP")},
            "BRIEF_CONTEXT_OR_AUTHORITY": {
                "ADEQUATE": count("BRIEF_CONTEXT_OR_AUTHORITY", "ADEQUATE"),
                "PARTIAL": count("BRIEF_CONTEXT_OR_AUTHORITY", "PARTIAL"),
                "DEPTH_EVIDENCE_GAP": count("BRIEF_CONTEXT_OR_AUTHORITY", "DEPTH_EVIDENCE_GAP")},
        },
        "package_level_gaps": [
            {"gap": "X01 supervision timeline has no direct P15 evidence_task_id "
                    "(pair-pretraining / instruction-data / action-data); r11 p15-b13 marks "
                    "timeline ordering as explicit editorial inference grounded in "
                    "DocVQA/ChartQA/MMMU; not promoted to measured synthesis.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
            {"gap": "P15 screen-operation layer contracts (OSWorld 1.0/2.0, SeeClick/"
                    "ScreenSpot) and HallusionBench control-pair have no P15 evidence_task_id; "
                    "r11 p15-b5/p15-b9 keep method-principle scope with OCRBench-gap analogy; "
                    "numeric screen claims not inserted into P15.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
            {"gap": "P09 tiling/patch internals, resampling/token-reduction widths, "
                    "KV/memory and measured-latency consequences, cross-attention vs "
                    "unified-sequence layer distinction, multi-image binding: no P09 primary "
                    "source; r11 p09-b9/b10/b12 state gaps explicitly in prose.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
        ],
        "nodes": entries,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} nodes={len(entries)}")
    print(json.dumps(doc["summary"], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
