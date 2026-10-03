#!/usr/bin/env python3
"""Build technical-depth-coverage-r12.json: r11 audit + r12 overlay.

Re-derives evidence bindings from r12 bytes; asserts every Architecture node
bound; dispositions carried from r11 unless overlayed (no auto-promotion).
Supports ADEQUATE / PARTIAL / DEPTH_EVIDENCE_GAP / PUBLIC_SOURCE_DISCLOSURE_LIMIT.
"""
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R12 = ED / "reader-editorial-authority-r12.json"
ARCH = SRC / "architecture-v2.json"
OUT = ED / "technical-depth-coverage-r12.json"
R11COV = ED / "technical-depth-coverage-r11.json"
OVERLAY = ED / "r12-coverage-overlay.json"

STATES = ("ADEQUATE", "PARTIAL", "DEPTH_EVIDENCE_GAP", "PUBLIC_SOURCE_DISCLOSURE_LIMIT")


def main() -> int:
    r12 = json.loads(R12.read_text(encoding="utf-8"))
    arch = json.loads(ARCH.read_text(encoding="utf-8"))
    r11cov = json.loads(R11COV.read_text(encoding="utf-8"))
    ov = json.loads(OVERLAY.read_text(encoding="utf-8"))
    assert r12["reader_editorial_revision"] == "r12"

    arch_nodes = {}
    for p in arch["packages"]:
        dc = p.get("publication_extensions", {}).get("depth_classes", {})
        inv = {}
        for cls in ("FULL_MECHANISM_TREATMENT", "TRANSITION_NODE_TREATMENT",
                    "BRIEF_CONTEXT_OR_AUTHORITY"):
            for n in dc.get(cls, []):
                inv[n] = cls
        arch_nodes[p["package_id"]] = inv

    blocks = {}
    for p in r12["reader_packages"]:
        for b in p["ordered_blocks"]:
            blocks[(p["package_id"], b["block_id"])] = b

    entries = []
    seen = set()
    for e in r11cov["nodes"]:
        pid, nid = e["package_id"], e["node_id"]
        key = (pid, nid)
        assert key not in seen
        seen.add(key)
        assert arch_nodes[pid][nid] == e["depth_class"], key
        okey = f"{pid}:{nid}"
        if okey in ov["reader_block_ids"]:
            e = dict(e, reader_block_ids=ov["reader_block_ids"][okey])
        if okey in ov["notes"]:
            e = dict(e, notes=ov["notes"][okey])
        assert e["disposition"] in STATES, key
        refs, rids = [], []
        for bid in e["reader_block_ids"]:
            b = blocks.get((pid, bid))
            assert b is not None, f"block miss {pid} {bid}"
            assert b["block_type"] == "PARAGRAPH", f"non-paragraph {pid} {bid}"
            for r in b.get("evidence_refs", []) or []:
                if r["evidence_task_id"] not in rids:
                    rids.append(r["evidence_task_id"])
                    refs.append(r)
        assert rids, f"{pid} {nid} binds no evidence"
        e = dict(e, evidence_refs=refs)
        entries.append(e)
    for pid, inv in arch_nodes.items():
        missing = [x for x in inv if (pid, x) not in seen]
        assert not missing, f"{pid} missing {missing}"

    def count(cls, disp):
        return sum(1 for e in entries if e["depth_class"] == cls and e["disposition"] == disp)

    doc = {
        "schema_version": "1.0",
        "issue_id": "SP-vision-multimodal-2026",
        "reader_authority": "reader-editorial-authority-r12.json",
        "reader_authority_sha256": hashlib.sha256(R12.read_bytes()).hexdigest(),
        "parent_coverage": "technical-depth-coverage-r11.json",
        "parent_coverage_sha256": hashlib.sha256(
            (ED / "technical-depth-coverage-r11.json").read_bytes()).hexdigest(),
        "status": "BOUNDED_CONTENT_REPAIR_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED",
        "summary": {
            "total_nodes": len(entries),
            "FULL_MECHANISM_TREATMENT": {
                "ADEQUATE": count("FULL_MECHANISM_TREATMENT", "ADEQUATE"),
                "PARTIAL": count("FULL_MECHANISM_TREATMENT", "PARTIAL"),
                "DEPTH_EVIDENCE_GAP": count("FULL_MECHANISM_TREATMENT", "DEPTH_EVIDENCE_GAP"),
                "PUBLIC_SOURCE_DISCLOSURE_LIMIT": count(
                    "FULL_MECHANISM_TREATMENT", "PUBLIC_SOURCE_DISCLOSURE_LIMIT")},
            "TRANSITION_NODE_TREATMENT": {
                "ADEQUATE": count("TRANSITION_NODE_TREATMENT", "ADEQUATE"),
                "PARTIAL": count("TRANSITION_NODE_TREATMENT", "PARTIAL"),
                "DEPTH_EVIDENCE_GAP": count("TRANSITION_NODE_TREATMENT", "DEPTH_EVIDENCE_GAP"),
                "PUBLIC_SOURCE_DISCLOSURE_LIMIT": count(
                    "TRANSITION_NODE_TREATMENT", "PUBLIC_SOURCE_DISCLOSURE_LIMIT")},
            "BRIEF_CONTEXT_OR_AUTHORITY": {
                "ADEQUATE": count("BRIEF_CONTEXT_OR_AUTHORITY", "ADEQUATE"),
                "PARTIAL": count("BRIEF_CONTEXT_OR_AUTHORITY", "PARTIAL"),
                "DEPTH_EVIDENCE_GAP": count("BRIEF_CONTEXT_OR_AUTHORITY", "DEPTH_EVIDENCE_GAP"),
                "PUBLIC_SOURCE_DISCLOSURE_LIMIT": count(
                    "BRIEF_CONTEXT_OR_AUTHORITY", "PUBLIC_SOURCE_DISCLOSURE_LIMIT")},
        },
        "package_level_gaps": [
            {"gap": "X01 training-side supervision timeline: no P15 evidence; r12 p15-b9 "
                    "declares absence as pure editorial synthesis (refs legitimately empty). "
                    "Evaluation timeline lives in p15-b13 as contract taxonomy.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
            {"gap": "P15 screen-operation contracts now bound via Architecture-sanctioned "
                    "P15<-P12 cross-package provenance (PRIMARY home stays P12).",
             "disposition": "ADEQUATE"},
            {"gap": "P09 tiling/token-reduction/projector/layer-fusion/KV/latency axes: "
                    "concrete items need canonical Evidence repair first (EVIDENCE_GAP); "
                    "undisclosed internals stay at LIMIT (PUBLIC_SOURCE_DISCLOSURE_LIMIT). "
                    "Reader LIMIT sentences retained; nothing inserted by conjecture.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
            {"gap": "OpenVLA Evidence claim text '29 tasks/embeddings' contradicts the "
                    "primary abstract ('multiple robot embodiments'); r12 reader follows "
                    "the primary (機体にわたる実機評価). Evidence repair recorded as "
                    "follow-up need, reader not blocked.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
        ],
        "nodes": entries,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} nodes={len(entries)}")
    print(json.dumps(doc["summary"], indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
