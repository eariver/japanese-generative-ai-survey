#!/usr/bin/env python3
"""Assemble compact-input-fresh-124-r9.json from staging files.

Fresh Draft from approved r9 + Evidence 124. Staging prose authored anew
(0 blocks identical to rev5), bindings re-derived from current matrix/evidence.
Normalizes ref_mode (AUTHOR_CLAIM->CLAIMS, missing->CLAIMS), preserves
CLAIMS/CLAIMS_AND_LIMITATIONS, validates banned terms, freshness, mandatory
corrections presence.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/fresh-draft-124-r9-20261009"
REV5 = SRC / "execution/r8-draft-closure-rev5-20261008/compact-input-fresh-121-r8-rev5.json"
OUT = EDIR / "compact-input-fresh-124-r9.json"

ORDER = ["P01","P02","P03","P04","P05","P06","P07A","P07B","P08","P09","P10","P11","P12","P13","P14","P15"]
BANNED = ["除去検証","思考の連鎖","頁面","一級の要素","ablation変形","完全オープン変形","文用言語モデル","使い回せる基盤"]

def load_staging():
    merged = {}
    synth = None
    for f in ["staging-p01-p04.json","staging-p05-p07b.json","staging-p08-p11.json","staging-p12-p15.json"]:
        d = json.loads((EDIR / f).read_text(encoding="utf-8"))
        for k,v in d.items():
            if k == "synthesis":
                synth = v
            else:
                assert k not in merged, k
                merged[k] = v
    assert set(merged) == set(ORDER), set(merged)
    assert synth and synth.get("profile_payload"), "synthesis missing"
    return merged, synth

def normalize(merged):
    for pid, pkg in merged.items():
        assert pkg.get("headline","").strip(), pid
        assert pkg.get("deck","").strip(), pid
        assert isinstance(pkg.get("deck_discovery_ids"), list) and pkg["deck_discovery_ids"], pid
        assert isinstance(pkg.get("blocks"), list) and pkg["blocks"], pid
        assert pkg.get("boundaries_text","").strip(), pid
        seen = set()
        for b in pkg["blocks"]:
            assert set(b) == {"block_id","block_type","discovery_ids","text"} or set(b) == {"block_id","block_type","discovery_ids","ref_mode","text"}, (pid, b.get("block_id"))
            assert b["block_id"] not in seen, (pid, b["block_id"])
            seen.add(b["block_id"])
            assert b["block_type"] == "PARAGRAPH", (pid, b["block_id"])
            assert isinstance(b["discovery_ids"], list) and b["discovery_ids"], (pid, b["block_id"])
            assert isinstance(b["text"], str) and len(b["text"]) > 100, (pid, b["block_id"])
            rm = b.get("ref_mode")
            if rm == "AUTHOR_CLAIM":
                b["ref_mode"] = "CLAIMS"
            elif rm is None:
                b["ref_mode"] = "CLAIMS"
            elif rm in ("CLAIMS","CLAIMS_AND_LIMITATIONS","LIMITATIONS","NONE"):
                pass
            else:
                raise ValueError(f"{pid}/{b['block_id']} invalid ref_mode {rm}")
            if b["ref_mode"] == "NONE":
                assert not b["discovery_ids"], pid
    return merged

def main() -> int:
    merged, synth = load_staging()
    merged = normalize(merged)
    # freshness vs rev5: 0 blocks identical
    rev5 = json.loads(REV5.read_text(encoding="utf-8"))
    rev5_texts = set()
    for p in rev5["packages"]:
        for b in p["blocks"]:
            rev5_texts.add(b["text"])
        rev5_texts.add(p["headline"])
        rev5_texts.add(p["deck"])
        if p.get("boundaries_text"):
            rev5_texts.add(p["boundaries_text"])
    identical = []
    for pid in ORDER:
        pkg = merged[pid]
        if pkg["headline"] in rev5_texts:
            identical.append(f"{pid}/headline")
        if pkg["deck"] in rev5_texts:
            identical.append(f"{pid}/deck")
        for b in pkg["blocks"]:
            if b["text"] in rev5_texts:
                identical.append(f"{pid}/{b['block_id']}")
        if pkg["boundaries_text"] in rev5_texts:
            identical.append(f"{pid}/boundaries")
    assert not identical, f"blocks identical to rev5 (not fresh): {identical}"
    # banned scan
    blob = json.dumps({"packages": merged, "synthesis": synth}, ensure_ascii=False)
    hits = [b for b in BANNED if b in blob]
    assert not hits, f"banned terms: {hits}"
    # mandatory corrections presence (spot checks)
    assert "Deformable" in blob or "Deformable DETR" in blob or "deformable" in blob.lower(), "P02 Deformable missing"
    # check Japanese-correct forms present
    for good in ["アブレーション","CoT","ページ上","明示的な構成要素"]:
        assert good in blob, f"correct form missing: {good}"
    # P15 four roles: check phrases
    assert "自己評価" in blob or "自己報告" in blob, "P15 role1 missing"
    assert "ベンダー" in blob, "P15 vendor missing"
    assert "第三者" in blob, "P15 third-party missing"
    # OSWorld proxy guard phrase
    assert "代理" in blob, "proxy framing missing"
    # DUSt3R editorial synthesis marker
    assert "比較判断" in blob or "編集上" in blob, "DUSt3R editorial marker missing"
    out_pkgs = []
    for pid in ORDER:
        p = merged[pid]
        out_pkgs.append({
            "package_id": pid,
            "headline": p["headline"],
            "deck": p["deck"],
            "deck_discovery_ids": p["deck_discovery_ids"],
            "blocks": [{"block_id": b["block_id"], "block_type": b["block_type"], "discovery_ids": b["discovery_ids"], "ref_mode": b["ref_mode"], "text": b["text"]} for b in p["blocks"]],
            "boundaries_text": p["boundaries_text"],
        })
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": "SP-vision-multimodal-2026",
        "draft_version": "fresh-124-r9",
        "runner": {
            "provider": "Muse",
            "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
            "invocation": ("TS-003 fresh 124-authority Draft from Architecture r9 APPROVED "
                           "(Evidence 124 VERIFIED 119/PARTIAL 5, Selection 124, 16 packages newly authored; "
                           "P02 DETR-successor lineage + attribution closure, P12 proxy framing, P15 four-role taxonomy, "
                           "DUSt3R editorial synthesis, Molmo scope, ResNet controlled comparison, Dreamer non-ancestry, "
                           "video role separation, P07A/B separation, Japanese terminology conformance; "
                           "rev5 as regression reference only, 0 blocks identical; no TeX/PDF; DRAFT_COMPLETE then STOP)"),
            "generated_at": "2026-10-09T00:00:00Z",
            "run_reference": None,
        },
        "packages": out_pkgs,
        "synthesis": synth,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total_chars = sum(len(b["text"]) for p in out_pkgs for b in p["blocks"])
    print(f"fresh input: {OUT.relative_to(ROOT)} | packages 16 | total block chars {total_chars} | identical-to-rev5 0")
    for p in out_pkgs:
        print(f" {p['package_id']}: {len(p['blocks'])} blocks")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
