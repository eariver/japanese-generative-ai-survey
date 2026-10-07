#!/usr/bin/env python3
"""Build compact-input-fresh-121-r8.json from the r7-rev1 spec (same r8 authority).

- Base: every block/headline/deck carried from rev1 (correct prose reused per §12).
- Targeted rewrites: P07A CLIP unit; P07B new D114/D115 blocks + B14+D049;
  P05-B10 +D110; P11-b10 contract split; P12 application; P02 SSD augmentation;
  §20 Japanese/workflow pass; P11 must_cover_map remap (r8 wording).
- draft_version fresh-121-r8. No upstream/Architecture change.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-authority-binding-repair-20261007"
IN = SRC / "execution/r7-targeted-authority-repair-20261007/compact-input-fresh-121-r7-rev1.json"
OUT = EDIR / "compact-input-fresh-121-r8.json"

REPLACEMENTS = [
    # §13 P07A CLIP correction
    ("ImageNetの128万ラベルを使わず教師ありResNet-50に匹敵し",
     "ImageNetの約128万件の学習例（学習画像）を用いず教師ありResNet-50に匹敵し"),
    # §18 P12 application translation
    ("実際のウェブやデスクトップの利用画面、ファイル入出力、複数利用画面にまたがる作業を含む369の作業を備える。",
     "実際のWeb/デスクトップアプリケーション、ファイル入出力、複数アプリケーションにまたがるワークフローを含む369の作業を備える。"),
    # §19 P02 SSD augmentation binding (option B safe wording)
    ("SSD300でVOC 2007の精度が74.3%から77.2%へ上がり、Titan Xで毎秒59フレーム、SSD512で76.9%から79.8%に達してFaster R-CNNを上回りつつ3倍の速度であることが原論文の測定として示されている。",
     "SSD300はaugmentation条件の違いを含む原論文のablationで74.3〜77.2 mAP、SSD512は76.9〜79.8 mAPを報告している。Titan Xで毎秒59フレームとFaster R-CNNの3倍の速度であることが原論文の測定として示されている。"),
    # §20 reader-facing cleanup
    ("実展開の遅延の主張は体系側の資料に委ねる。", "実展開の遅延は本節の対象外とする。"),
    ("ただしクラウドソーシング由来の雑音と対応づけの限界が残り、GoldGへの下降の主張はGLIP側の資料に委ねられる。",
     "ただしクラウドソーシング由来の雑音と対応づけの限界が残り、GoldGとの直接の来歴関係までは主張しない。"),
    ("3.5系の存在は来歴注記であり、既存の収集範囲を置き換えるものではない。",
     "3.5系の存在は来歴注記に留める。"),
    ("LongVideoBenchの6,678問を含む行単位の対応づけと3.8 Flash行の確定は、版確定時の検証作業に委ねる。",
     "LongVideoBenchの6,678問を含む行単位の対応づけと3.8 Flash行の確定は、公開版確定時に残された検証課題である。"),
    ("方策機構の細部はRT-2側資料の所管である。", "方策機構の詳細はRT-2の説明で扱う。"),
    ("RGBのみ推論に伴うカメラ位置の鋭敏さや長期展開の誤差蓄積",
     "RGBのみ推論に伴うカメラ配置への感度や長期展開の誤差蓄積"),
    ("対象期間外に公開された記録は本稿の根拠に含めない。", ""),
    ("初の全範囲の映像評価である。", "初の広範な動画理解評価である。"),
    ("オンラインの問答のためのVStream-QAを伴い", "オンライン問答用のVStream-QAベンチマークを伴い"),
    ("伴走する問答の評価が流れを受け続ける仕組みの到達を確かめる軸になる。",
     "VStream-QAベンチマークが流れを受け続ける仕組みの到達を確かめる軸になる。"),
    ("接地正確さと長時間成功は別軸である。", "グラウンディングの正解率と長時間成功は別軸である。"),
    ("人間72.36%に対し最良モデル12.24%でGUI要素接地と操作知識に失敗する。",
     "人間72.36%に対し最良モデル12.24%でGUI要素のグラウンディングと操作知識に失敗する。"),
    # 資料 -> dataset/data where it stands in for data
    ("27M接地資料、すなわち人手3Mとウェブ対24Mから自己学習で起こした接地箱を用い",
     "27M件の接地データ、すなわち人手3Mとウェブ対24Mから自己学習で起こした接地箱を用い"),
    ("接地資料実践による検出の再定義が開かれた。", "接地データ実践による検出の再定義が果たされた。"),
    ("7資料群のオープンボキャブラリーで最先端とされる。", "7データセット群のオープンボキャブラリーで最先端とされる。"),
    ("細粒度分類を含む30超の資料群へゼロショット転移することが示され",
     "細粒度分類を含む30超のデータセット群へゼロショット転移することが示され"),
    ("MiDaSは互換性のない深度資料群、すなわち", "MiDaSは互換性のない深度データ群、すなわち"),
    ("既存の深度資料そのものが制約だという所見は", "既存の深度データそのものが制約だという所見は"),
    ("既存深度資料の不足が未解決である点にある", "既存深度データの不足が未解決である点にある"),
    ("Visual Genomeは領域記述の接地資料の先行形態にも位置づけられ、GLIP期のGoldG的実践の資料体制へ連なるものとして整理される。",
     "Visual Genomeは領域記述データの先行形態にも位置づけられ、GLIP期のGoldG的実践のデータ体制へ連なるものとして整理される。"),
    ("語句と対象の対応資料130万対の事前学習により", "語句と対象の対応データ130万対の事前学習により"),
    ("検出と接地と説明文の資料で事前学習する。", "検出と接地と説明文のデータで事前学習する。"),
    ("ウェブ資料依存が限界であり", "ウェブデータ依存が限界であり"),
    ("一部の資料で学習し、残りの未知資料で試すゼロショット横断にある。",
     "一部のデータで学習し、残りの未知データで試すゼロショット横断にある。"),
    ("を含む未見資料での転移を、実環境における汎化の代理として測る点",
     "を含む未知データでの転移を、実環境における汎化の代理として測る点"),
]

NEW_P07B_D114 = ("SigLIP 2の段階的手順（キャプション生成・自己蒸留・マスク予測の組合せ）は、画像と言葉の大規模対応づけが位置特定や密な転移へ伸びることを示した転換点である。RefCOCOの接地やOWL-ViTのオープンボキャブラリー検出での伸びが、開かれた語彙の知覚系譜への継承を裏づける。段階レシピやNaFlexの詳細はP06の範囲であり、ここでは転移の成立のみを扱う。")

NEW_P07B_D115 = ("SAM 3は言語・概念による指示を個体の検出・セグメンテーション・追跡へ直結させる後発の接地拡張である。単純な名詞句と画像例の正負ボックス、SAM 2型の視覚クリックで指示し、存在トークンの分離が認識と位置特定を分ける。SAM系の点指示と記憶機構を引き継ぎ、概念単位の全事例追跡を可能にする点が、開かれた語彙の知覚への遅い収束として位置づけられる。機構の詳細はP03の範囲であり、ここでは概念接地の拡張のみを扱う。")

NEW_P11_B10 = ("SAM 3は、概念プロンプトに基づく動画内の検出・セグメンテーション・追跡を扱い、memory-based trackerによって時間方向の対象対応を維持する。これはvideo concept grounding / trackingの補助例であり、保存済み動画から必要箇所をquery-drivenに取得する契約とは異なる。保存済みタイムラインのオンデマンドな移動・取得はVM-D112エージェント型理解の契約であり、本節の三契約の列を保つ。")

P11_MC_OLD = "SAM 3 memory video tracking as supporting stored-timeline evidence"
P11_MC_NEW = ("SAM 3 concept-prompted video grounding and memory-based tracking are supporting "
              "temporal-grounding evidence; stored-timeline on-demand navigation remains the "
              "distinct VM-D112 contract.")


def main() -> int:
    spec = json.loads(IN.read_text(encoding="utf-8"))
    n_replace = 0
    for p in spec["packages"]:
        for field in ("headline", "deck"):
            if p.get(field):
                for old, new in REPLACEMENTS:
                    if old in p[field]:
                        p[field] = p[field].replace(old, new)
                        n_replace += 1
        for b in p["blocks"]:
            if not b.get("text"):
                continue
            for old, new in REPLACEMENTS:
                if old in b["text"]:
                    b["text"] = b["text"].replace(old, new)
                    n_replace += 1
        if p.get("boundaries_text"):
            for old, new in REPLACEMENTS:
                if old in p["boundaries_text"]:
                    p["boundaries_text"] = p["boundaries_text"].replace(old, new)
                    n_replace += 1
    print(f"exact replacements applied: {n_replace}")

    def get_block(pid, bid):
        p = next(x for x in spec["packages"] if x["package_id"] == pid)
        return p, next(x for x in p["blocks"] if x.get("block_id") == bid)

    def set_block(pid, bid, text, discovery_ids=None):
        p, b = get_block(pid, bid)
        b["text"] = text
        if discovery_ids is not None:
            b["discovery_ids"] = discovery_ids
        return p, b

    set_block("P11", "p11-b10", NEW_P11_B10)  # discovery_ids already [VM-D115]
    # P07B: B14 += D049; new D114/D115 synthesis blocks appended
    p07b, b14 = get_block("P07B", "P07B-B14")
    assert sorted(b14["discovery_ids"]) == ["VM-D041", "VM-D044", "VM-D047", "VM-D048", "VM-D050", "VM-D056"], b14["discovery_ids"]
    if "VM-D049" not in b14["discovery_ids"]:
        b14["discovery_ids"] = sorted(b14["discovery_ids"] + ["VM-D049"])
    p07b_pkg = next(x for x in spec["packages"] if x["package_id"] == "P07B")
    existing = {b["block_id"] for b in p07b_pkg["blocks"]}
    assert "P07B-D114" not in existing and "P07B-D115" not in existing
    p07b_pkg["blocks"].append({"block_id": "P07B-D114", "block_type": "PARAGRAPH",
                               "discovery_ids": ["VM-D114"], "text": NEW_P07B_D114})
    p07b_pkg["blocks"].append({"block_id": "P07B-D115", "block_type": "PARAGRAPH",
                               "discovery_ids": ["VM-D115"], "text": NEW_P07B_D115})
    # P05-B10 += D110 (OCRBench specifics bound to evaluation authority)
    p05, _ = get_block("P05", "P05-B10")
    b10 = next(x for x in p05["blocks"] if x["block_id"] == "P05-B10")
    assert "OCRBench v2の23課題" in b10["text"], b10["text"][:120]
    if "VM-D110" not in b10["discovery_ids"]:
        b10["discovery_ids"] = sorted(b10["discovery_ids"] + ["VM-D110"])
    # P11 must_cover_map remap to r8 wording
    p11 = next(x for x in spec["packages"] if x["package_id"] == "P11")
    mmap = p11.get("must_cover_map")
    assert mmap is not None and P11_MC_OLD in mmap, list(mmap or {})
    mmap[P11_MC_NEW] = mmap.pop(P11_MC_OLD)

    spec["draft_version"] = "fresh-121-r8"
    spec["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 fresh 121-authority Draft from Architecture r8 APPROVED "
                       "(corrected D039 authority + P11 SAM3 wording + effective cross-package "
                       "map incl. D110->P05): 16 packages newly authored from the corrected chain; "
                       "fresh-121-r7-rev1 as regression reference only; "
                       "no TeX/PDF; DRAFT_COMPLETE then STOP for independent AI review"),
        "generated_at": "2026-10-07T07:00:00Z",
        "run_reference": None,
    }
    syn = spec["synthesis"]["profile_payload"]
    OUT.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"r8 spec: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
