#!/usr/bin/env python3
"""Build compact-input-fresh-121-r8-rev4.json: minimal publication-blocker closure.

Scope (TS-003 fresh-121-r8-rev4):
  A. P06-B06 + P06-boundaries: remove internal VM-D065 / claim-number leakage.
  B. p11-b10: remove internal VM-D112 leakage, keep SAM3 vs Agentic split.
  C. P07B-B07: COCO val / test-dev split identity fix.
  D. P03-boundaries + P07A-boundaries: final two ML grounding 接地 -> reader terms.
  E. P07B-B07/B08 residual データ実践 cleanup (adjacent to GLIP repair).

No general rewrite. No upstream/Architecture/Evidence/Selection/map change.
discovery_ids/must_cover_map/only_claims untouched. draft_version rev4.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-draft-closure-rev4-20261008"
IN = SRC / "execution/r8-draft-closure-rev3-20261007/compact-input-fresh-121-r8-rev3.json"
OUT = EDIR / "compact-input-fresh-121-r8-rev4.json"

# (old, new, expected_hits) — each asserts exact count in INPUT spec
REPLACEMENTS = [
    # BLOCKER A — P06-B06 internal authority leakage
    ("Qwen3-VLへの継承はQwen側の報告による事実としてのみ扱い、VM-D065の主張3に限定して結びつける。",
     "Qwen3-VLとの接続は、Qwen3-VL技術報告が明示する視覚エンコーダ、merger、DeepStackの構成に限って扱う。", 1),
    # BLOCKER A — P06-boundaries claim-number leakage
    ("Qwen3-VLへの継承はQwen側の報告の主張3に限定して結びつけ、検出器のDINOと自己教師ありDINOを混ぜない。",
     "Qwen3-VLとの接続は、Qwen3-VL技術報告が明示する視覚エンコーダ、merger、DeepStackの構成に限って扱い、検出器のDINOと自己教師ありDINOを混ぜない。", 1),
    # BLOCKER B — p11-b10 VM-D112 leakage (keep SAM3 vs Agentic split)
    ("保存済みタイムラインのオンデマンドな移動・取得はVM-D112エージェント型理解の契約であり、本節の三契約の列を保つ。",
     "保存済みタイムラインのオンデマンドな移動・取得はGoogleが報告するエージェント型動画理解の契約であり、本節の三契約の列を保つ。", 1),
    # BLOCKER C — P07B-B07 COCO split identity
    ("微調整でCOCO検証60.8と開発集合61.5",
     "微調整でCOCO val 60.8 AP、test-dev 61.5 AP", 1),
    # Residual grounding normalization — P03-boundaries
    ("SAM 3は言語接地の概念接点の範囲である",
     "SAM 3は言語グラウンディングの概念接点の範囲である", 1),
    # Residual grounding normalization — P07A-boundaries
    ("位置への接地とは別の評価で測る",
     "領域グラウンディングや位置特定とは別の評価で測る", 1),
    # P07B-B07 residual データ実践 (adjacent to GLIP repair)
    ("グラウンディングデータ実践による検出の再定義が果たされた。",
     "大規模グラウンディングデータを用いた統一事前学習が検出の再定式化を支えた。", 1),
    # P07B-B08 residual データ実践 (names actual technical distinction)
    ("GLIPのデータ実践による再定式とは契約が異なり",
     "GLIPの大規模グラウンディングデータと統一事前学習による再定式化とは異なり", 1),
]


def main() -> int:
    EDIR.mkdir(parents=True, exist_ok=True)
    spec = json.loads(IN.read_text(encoding="utf-8"))
    assert spec.get("draft_version") == "fresh-121-r8-rev3", spec.get("draft_version")
    fired = []
    for p in spec["packages"]:
        for field in ("headline", "deck"):
            if p.get(field):
                for old, new, expected in REPLACEMENTS:
                    if old in p[field]:
                        p[field] = p[field].replace(old, new)
                        fired.append((p["package_id"], field, old[:40]))
        for b in p["blocks"]:
            if not b.get("text"):
                continue
            for old, new, expected in REPLACEMENTS:
                if old in b["text"]:
                    b["text"] = b["text"].replace(old, new)
                    fired.append((p["package_id"], b["block_id"], old[:40]))
        if p.get("boundaries_text"):
            for old, new, expected in REPLACEMENTS:
                if old in p["boundaries_text"]:
                    p["boundaries_text"] = p["boundaries_text"].replace(old, new)
                    fired.append((p["package_id"], "boundaries", old[:40]))
    from collections import Counter as _C
    counts = _C(o for _, _, o in fired)
    missed = []
    for old, _, expected in REPLACEMENTS:
        got = sum(1 for _, _, o in fired if o == old[:40])
        if got != expected:
            missed.append((old[:70], expected, got))
    print(f"replacements fired: {len(fired)}")
    for pid, field, prefix in fired:
        print(f"  - {pid}/{field}: {prefix!r}")
    if missed:
        print("COUNT MISMATCH:")
        for m in missed:
            print("  -", m)
        raise SystemExit("replacement count mismatch")
    # discovery_ids / only_claims / must_cover_map must be untouched vs rev3 input
    rev3 = json.loads(IN.read_text(encoding="utf-8"))
    for p_new in spec["packages"]:
        p_old = next(x for x in rev3["packages"] if x["package_id"] == p_new["package_id"])
        assert p_new.get("deck_discovery_ids") == p_old.get("deck_discovery_ids"), p_new["package_id"]
        assert p_new.get("must_cover_map") == p_old.get("must_cover_map"), p_new["package_id"]
        for b_new in p_new["blocks"]:
            b_old = next(x for x in p_old["blocks"] if x["block_id"] == b_new["block_id"])
            assert b_new.get("discovery_ids") == b_old.get("discovery_ids"), (p_new["package_id"], b_new["block_id"])
            assert b_new.get("only_claims") == b_old.get("only_claims"), (p_new["package_id"], b_new["block_id"])
            assert b_new.get("ref_mode") == b_old.get("ref_mode"), (p_new["package_id"], b_new["block_id"])

    spec["draft_version"] = "fresh-121-r8-rev4"
    spec["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 Draft closure revision r8-rev4 from Architecture r8 APPROVED "
                       "(same authority; minimal publication-blocker closure: P06 VM-D065/claim-3 "
                       "purge, P11 VM-D112 purge, P07B val/test-dev split fix, final two ML 接地 "
                       "normalizations, adjacent データ実践 cleanup; r8 authority unchanged; "
                       "no TeX/PDF; DRAFT_COMPLETE held for final differential content review)"),
        "generated_at": "2026-10-08T00:00:00Z",
        "run_reference": None,
    }
    OUT.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blob = OUT.read_text(encoding="utf-8")
    must_be_gone = [
        "VM-D065の主張3",
        "Qwen側の報告の主張3に限定",
        "VM-D112エージェント型理解",
        "COCO検証60.8と開発集合61.5",
        "開発集合61.5",
        "言語接地の概念接点",
        "位置への接地とは別の評価",
        "グラウンディングデータ実践",
        "GLIPのデータ実践",
    ]
    bad = [s for s in must_be_gone if s in blob]
    assert not bad, bad
    must_be_present = [
        "Qwen3-VL技術報告が明示する視覚エンコーダ、merger、DeepStackの構成に限って扱う",
        "Googleが報告するエージェント型動画理解の契約",
        "COCO val 60.8 AP、test-dev 61.5 AP",
        "言語グラウンディングの概念接点",
        "領域グラウンディングや位置特定とは別の評価で測る",
        "大規模グラウンディングデータを用いた統一事前学習が検出の再定式化を支えた",
        "GLIPの大規模グラウンディングデータと統一事前学習による再定式化とは異なり",
    ]
    missing = [s for s in must_be_present if s not in blob]
    assert not missing, missing
    # test-dev must not be translated
    assert "test-dev 61.5 AP" in blob
    print(f"rev4 spec verified clean: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
