#!/usr/bin/env python3
"""Assemble compact-input-fresh-121-r6.json: rev2 skeleton + fresh prose.

Preserves rev2 structure (deck_discovery_ids, block ids/types/discovery_ids/
ref_modes/only_claims, must_cover_map) and injects fresh headline/deck/text/
boundaries. Validates banned terms + freshness (zero block texts identical to rev2).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
REV2 = SRC / "execution/content-revision-r5-20261006/compact-input-rev2.json"
EDIR = SRC / "execution/r6-final-authority-correction-20261006"
OUT = EDIR / "compact-input-fresh-121-r6.json"

BANNED = ["証し", "問いかけ", "道具呼び出し", "模型の重み", "般化", "界面",
          "開放的な課題非依存の学習", "学習汚染", "training contamination",
          "Training contamination", "本パッケージ", "正準", "管路", "枠率", "映像枠",
          "単一伝送路", "実時間", "6668"]
BANNED_EN = []  # checked contextually elsewhere


def main() -> int:
    rev2 = json.loads(REV2.read_text(encoding="utf-8"))
    fresh = {}
    for f in ("fresh-prose-p01-p04.json", "fresh-prose-p05-p07b.json",
              "fresh-prose-p09-p12.json", "fresh-prose-p08-p13-p15.json"):
        fresh.update(json.loads((EDIR / f).read_text(encoding="utf-8")))
    assert set(fresh) == {p["package_id"] for p in rev2["packages"]}, set(fresh)
    out_pkgs = []
    identical = []
    for rp in rev2["packages"]:
        pid = rp["package_id"]
        fp = fresh[pid]
        blocks = []
        for rb in rp["blocks"]:
            fb = next(b for b in fp["blocks"] if b["block_id"] == rb["block_id"])
            if fb["text"] == rb["text"]:
                identical.append(f"{pid}/{rb['block_id']}")
            nb = dict(rb)
            nb["text"] = fb["text"]
            blocks.append(nb)
        out_pkgs.append({
            "package_id": pid,
            "headline": fp["headline"],
            "deck": fp["deck"],
            "deck_discovery_ids": rp["deck_discovery_ids"],
            **({"deck_ref_mode": rp["deck_ref_mode"]} if "deck_ref_mode" in rp else {}),
            "blocks": blocks,
            **({"must_cover_map": rp["must_cover_map"]} if "must_cover_map" in rp else {}),
            **({"only_claims": rp["only_claims"]} if "only_claims" in rp else {}),
            "boundaries_text": fp["boundaries_text"],
        })
    assert not identical, f"blocks identical to rev2 (not fresh): {identical}"
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": "SP-vision-multimodal-2026",
        "draft_version": "fresh-121-r6",
        "runner": {
            "provider": "Muse",
            "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
            "invocation": ("TS-003 fresh 121-authority Draft from Architecture r6 APPROVED "
                           "(corrected VQA-v2 + three-way provenance authority): 16 packages newly "
                           "authored from the corrected chain; r5-rev2 as negative regression only; "
                           "no TeX/PDF; DRAFT_COMPLETE then STOP for independent AI review"),
            "generated_at": "2026-10-07T02:00:00Z",
            "run_reference": None,
        },
        "packages": out_pkgs,
        "synthesis": {
            "profile_payload": {
                "branch_transition_synthesis": ("本巻の系譜は一本の前進ではなく、並立する枝の移行の束である。学習表現と転移を起点に、検出の枠組み、密な構造化と指示応答、文書の構造理解、系列としての視覚と自己教師あり学習、画像全体の対応づけから開かれた接地へ、個別に事前学習した構成要素の接続、解像度と融合と時刻の統合、幻覚と根拠利用の診断、溜めた時系列の幅と想起とオンライン状態の保持の分離、画面操作の接地と状態維持、身体をもつ行動のインターフェース、歴史的定式と潜在ダイナミクスと予測表現と生成的環境の四極へと系譜が分かれ、評価の契約ごとの方法の整理へ集まる。教師信号の出所と入出力の約束の変化が全巻の流れをなす。版と日付と所在の結びつけを保ち、条件を外した順位づけはしない。未決を未決として残す。"),
                "parallel_competing_relations": ("一体の事前学習と部品の組み合わせ、特化型と汎用型、密な注釈とウェブ規模の弱い教師信号、早期と後段と密な融合、凍結の再利用と共同学習、溜めた時系列の幅と想起とオンライン状態の保持、計画側の分業と一体の行動表現、潜在ダイナミクスと予測表現と生成的環境、著者・開発者の自己報告と提供者・ベンダーの報告と独立第三者の測定が並行する競合関係にある。いずれも万能ではなく、条件と装置と費用と対象で損得が変わる。一本化の圧力と分業の圧力を両方残す。特化と汎用の直接対決の不在を順位なしに残し、不在を優劣に読み替えない。著者・開発者の報告と提供者・ベンダーの測定と独立第三者の測定の区別を保ち、開かれていることと独立に測られていることの区別を保つ。どちらが勝つかの断定には全巻の結果は届かず、未決を未決として残す。"),
                "unresolved_lineage_questions": ("身体の行動の独立評価の不足をG01、制御に使える生成世界の共有測定の不在をG02、同一条件での特化型と汎用型の直接対決の不在をG03、実運用の遅延と記憶量の根拠の不足をG04、最新第一者報告の独立再現の不足をG05として残す。概要水準の五件はPARTIALとして概要の範囲に留める。要求に応じて調べる動画方式の上限はVM-D112として提供者・ベンダー側の示値であり行単位の結びつけを残す。六つのGのうちG06は解決済みとして引き継がず、G01からG05を組で引き継ぎ、全巻の測定の章への接続を欠かさない。未決を未決として残す。"),
                "historical_attribution_boundaries": ("概要や断片水準の記録は概要の範囲に留め、語りで格上げしない。閉じた製品は能力と運用のみで構成を推測しない。条件の異なる数値の横断順位づけはしない。著者・開発者と提供者・ベンダーの主張は帰属づきで引用し独立再現を待つ。要旨水準の事実はその水準でのみ用いる。歴史的定式から生成環境への直接継承は主張しない。似ていることと受け継いだことの区別を保ち、名指しや類似を継承に読み替えない。内部の作業用語は読者文に出さない。測ったことだけを語り、測っていないことは語らない。測り方の違う数値を一つの順位に混ぜず、版と日付と所在の結びつけを保つ。開かれていることと独立に測られていることの区別を保ち、重みの公開を測定の存在に読み替えない。未決を未決として残す。"),
            },
            "publication_payload": {},
        },
    }
    # banned-term scan on reader prose (headline/deck/blocks/boundaries + fresh synthesis;
    # standalone 般化 only — 一般化 (generalize) is legitimate and excluded)
    import re
    blob = json.dumps(payload, ensure_ascii=False)
    hits = [b for b in BANNED if b in blob]
    hits = [h for h in hits if not (h == "般化" and "般化" in blob and blob.count("一般化") * 2 >= blob.count("般化"))]
    # precise standalone-般化 check (not part of 一般化)
    standalone_ipan = [m for m in re.finditer(r"般化", blob) if not (m.start() > 0 and blob[m.start()-1] == "一")]
    if standalone_ipan:
        hits.append("般化(standalone)")
    assert not hits, f"banned terms in fresh input: {hits}"
    assert "bag-of-words" not in blob, "BoW survives in fresh input"
    # corrected-semantics presence
    assert "補完的" in blob and "事前分布" in blob, "VQA complementary/prior semantics missing"
    assert "著者" in blob and ("提供元" in blob or "ベンダー" in blob), "three-way taxonomy missing"
    assert "6678" in blob and "6668" not in blob
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"fresh input: {OUT.relative_to(ROOT)} | packages 16 | identical-to-rev2 blocks: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
