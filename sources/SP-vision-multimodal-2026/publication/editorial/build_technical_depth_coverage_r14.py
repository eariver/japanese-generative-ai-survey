#!/usr/bin/env python3
"""Build technical-depth-coverage-r14.json: r13 audit re-derived from r14 bytes.

- No node reclassification (dispositions carried; no auto-promotion).
- Evidence bindings re-derived from r14 blocks (picks up p15-b3/b15 ev-vmd080
  cross-binding + all r14 ref sets).
- Generation-path guard: banned/stale phrases fail the build (same list as r13).
"""
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R14 = ED / "reader-editorial-authority-r14.json"
ARCH = SRC / "architecture-v2.json"
OUT = ED / "technical-depth-coverage-r14.json"
R13COV = ED / "technical-depth-coverage-r13.json"

BANNED = ["物の輪郭", "代表値の敷き詰め", "代表値敷詰め", "重なりの後始末",
          "描き直し→言い当て", "教示→潜ませ", "潜ませ動き", "潜動画",
          "110億級", "無ラベル動画110億級", "算法", "绑定", "私傾",
          "吸い上げ", "夢の中で育てた", "夢で育てて", "言い当て", "変種",
          "文字の理論", "設計の選び", "埋め込み評価", "教師モデルなしに教師の役割",
          "端から端まで一緒に調整", "キャプション予測の事前学習",
          "ずれを80msに抑える", "300〜500エポックのAdamW", "投票型",
          "幻覚", "基線", "日程", "教員", "文節", "行動の言語化",
          "呼び出し可能性", "三つの評価指標"]


def main() -> int:
    r14 = json.loads(R14.read_text(encoding="utf-8"))
    arch = json.loads(ARCH.read_text(encoding="utf-8"))
    r13cov = json.loads(R13COV.read_text(encoding="utf-8"))
    assert r14["reader_editorial_revision"] == "r14"

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
    for p in r14["reader_packages"]:
        for b in p["ordered_blocks"]:
            blocks[(p["package_id"], b["block_id"])] = b

    entries = []
    seen = set()
    for e in r13cov["nodes"]:
        pid, nid = e["package_id"], e["node_id"]
        key = (pid, nid)
        assert key not in seen
        seen.add(key)
        assert arch_nodes[pid][nid] == e["depth_class"], key
        refs, rids = [], []
        for bid in e["reader_block_ids"]:
            b = blocks.get((pid, bid))
            assert b is not None, f"block miss {pid} {bid}"
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
        "reader_authority": "reader-editorial-authority-r14.json",
        "reader_authority_sha256": hashlib.sha256(R14.read_bytes()).hexdigest(),
        "parent_coverage": "technical-depth-coverage-r13.json",
        "parent_coverage_sha256": hashlib.sha256(R13COV.read_bytes()).hexdigest(),
        "status": "CONTENT_CONVERGENCE_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED",
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
        "package_level_gaps": r13cov["package_level_gaps"],
        "nodes": entries,
    }
    text = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    for kw in BANNED:
        assert kw not in text, f"banned phrase in coverage r14: {kw}"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} nodes={len(entries)}")
    print(json.dumps(out["summary"], indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
