#!/usr/bin/env python3
"""Build technical-depth-coverage-r13.json: r12 audit + r13 overlay.

- Applies field_fixes (exact-count asserted), node updates (blocks/disposition/
  notes), package-gap updates.
- Re-derives evidence bindings from r13 bytes; asserts every Architecture node.
- Generation-path guard: asserts NO banned/stale phrase anywhere in the
  resulting coverage JSON (reader-body sync regressions fail the build).
"""
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R13 = ED / "reader-editorial-authority-r13.json"
ARCH = SRC / "architecture-v2.json"
OUT = ED / "technical-depth-coverage-r13.json"
R12COV = ED / "technical-depth-coverage-r12.json"
OVERLAY = ED / "r13-coverage-overlay.json"

STATES = ("ADEQUATE", "PARTIAL", "DEPTH_EVIDENCE_GAP", "PUBLIC_SOURCE_DISCLOSURE_LIMIT")
BANNED = ["物の輪郭", "代表値の敷き詰め", "代表値敷詰め", "重なりの後始末",
          "描き直し→言い当て", "教示→潜ませ", "潜ませ動き", "潜動画",
          "110億級", "無ラベル動画110億級", "算法", "绑定", "私傾",
          "吸い上げ", "夢の中で育てた", "夢で育てて", "言い当て", "変種",
          "文字の理論", "設計の選び", "埋め込み評価", "教師モデルなしに教師の役割",
          "端から端まで一緒に調整", "キャプション予測の事前学習",
          "ずれを80msに抑える", "300〜500エポックのAdamW", "投票型",
          "幻覚", "基線", "日程", "教員"]


def main() -> int:
    r13 = json.loads(R13.read_text(encoding="utf-8"))
    arch = json.loads(ARCH.read_text(encoding="utf-8"))
    r12cov = json.loads(R12COV.read_text(encoding="utf-8"))
    ov = json.loads(OVERLAY.read_text(encoding="utf-8"))
    assert r13["reader_editorial_revision"] == "r13"

    raw = R12COV.read_text(encoding="utf-8")
    for fx in ov["field_fixes"]:
        n = raw.count(fx["old"])
        assert n == fx["count"], f"field fix count {fx['old']}: {n} != {fx['count']}"
        raw = raw.replace(fx["old"], fx["new"])
    doc = json.loads(raw)

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
    for p in r13["reader_packages"]:
        for b in p["ordered_blocks"]:
            blocks[(p["package_id"], b["block_id"])] = b

    entries = []
    seen = set()
    for e in doc["nodes"]:
        pid, nid = e["package_id"], e["node_id"]
        key = (pid, nid)
        assert key not in seen
        seen.add(key)
        assert arch_nodes[pid][nid] == e["depth_class"], key
        okey = f"{pid}:{nid}"
        if okey in ov["node_updates"]:
            u = ov["node_updates"][okey]
            for fld in ("reader_block_ids", "disposition", "notes"):
                if fld in u:
                    e = dict(e, **{fld: u[fld]})
        assert e["disposition"] in STATES, key
        assert len(e["coverage"]) == 8, key
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

    out = {
        "schema_version": "1.0",
        "issue_id": "SP-vision-multimodal-2026",
        "reader_authority": "reader-editorial-authority-r13.json",
        "reader_authority_sha256": hashlib.sha256(R13.read_bytes()).hexdigest(),
        "parent_coverage": "technical-depth-coverage-r12.json",
        "parent_coverage_sha256": hashlib.sha256(R12COV.read_bytes()).hexdigest(),
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
            {"gap": "X01 training-side supervision timeline: IMPLEMENTED in r13 p15-b9 "
                    "via Architecture-sanctioned cross-package synthesis (8 named "
                    "already-selected supervision authorities; PRIMARY homes unchanged; "
                    "P15-native absence explicitly fenced in prose).",
             "disposition": "ADEQUATE"},
            {"gap": "P15 screen-operation contracts bound via Architecture-sanctioned "
                    "P15<-P12 cross-package provenance (PRIMARY home stays P12).",
             "disposition": "ADEQUATE"},
            {"gap": "P09 mechanism axes supplemented in Evidence r6 batch (12 claims, "
                    "bound-report pinpoints, Sol re-review required); reader prose added "
                    "as p09-b13/b14/b15/b16. Undisclosed internals (measured KV/latency, "
                    "unpublished internals) stay at PUBLIC_SOURCE_DISCLOSURE_LIMIT, "
                    "recorded per-axis in node notes; nothing inserted by conjecture.",
             "disposition": "ADEQUATE"},
            {"gap": "OpenVLA Evidence claim repaired in r6 batch (embodiments); reader "
                    "already correct since r12; provenance chain realigned. Canonical "
                    "Evidence repair recorded as follow-up need: CLOSED by this batch.",
             "disposition": "ADEQUATE"},
            {"gap": "Downstream SHA pins now stale by design (candidate-matrix basis "
                    "5cc951bd, draft-package evidence_acceptance pins, views 78a08d3c): "
                    "those files truthfully record what they were built from; rebind "
                    "requires the Human-gated dependency-aware path (Architecture rN+1). "
                    "No lifecycle artifact rewritten in this pass; no approval fabricated.",
             "disposition": "DEPTH_EVIDENCE_GAP"},
        ],
        "nodes": entries,
    }
    text = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    for kw in BANNED:
        assert kw not in text, f"banned phrase in coverage r13: {kw}"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} nodes={len(entries)}")
    print(json.dumps(out["summary"], indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
