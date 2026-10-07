#!/usr/bin/env python3
"""Build compact-input-fresh-121-r8-rev1.json: bounded closure repair from r8 spec.

Complete fix list with strict post-verification: every old-string must reach
zero occurrences in the output spec, and every new-form must be present.
Block rewrites: P13-B2 (lineage split +D097), P15-B04 (GPT-5.5),
P09-B10 (single molmo2 sentence + TODO removal), P11-b10 (contract split),
P04-B5 (narrowed GoldG +D047), P08-B8 (+D060 already in r8; text kept).
draft_version fresh-121-r8-rev1. No upstream/Architecture/map change.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-draft-closure-rev2-20261007"
IN = SRC / "execution/r8-authority-binding-repair-20261007/compact-input-fresh-121-r8.json"
OUT = EDIR / "compact-input-fresh-121-r8-rev2.json"

# (old, new, must_fire_count_or_None)
REPLACEMENTS = [
    # §5 P08 Flamingo: data-volume axis
    ("Flamingoは学習済みの視覚側と言語側をgated cross-attentionの重い層でつなぎ、",
     "Flamingoは学習済みの視覚側と言語側をgated cross-attention層でつなぎ、", 1),
    ("課題別に千倍規模で作り替えたモデルを上回ったと著者ら自身の測定は伝える。",
     "一部の評価では、課題固有データを数千倍多く用いてfine-tuneした専用モデルを上回ったと著者ら自身の測定は伝える。", 1),
    # §8 Grounding DINO triad + checkpoint + MDETR query
    ("Grounding DINOは特徴増強と言語誘導質問選択と相互様式復号器の3段階で",
     "Grounding DINOはfeature enhancer（特徴強化器）とlanguage-guided query selection（言語誘導型クエリ選択）とcross-modality decoder（クロスモダリティ・デコーダ）の3段階で", 1),
    ("検査点と推論コードが公開された。", "チェックポイントと推論コードが公開された。", 1),
    ("MDETRは自然文の質問でDETRを条件づけ、", "MDETRは自然言語クエリでDETRを条件づけ、", 1),
    # §9 P07A X01 label
    ("画像文対の大規模契約はX01の教師信号の系譜に位置づけられる。",
     "画像文対の大規模契約は、大規模画像テキスト対による教師信号の系譜に位置づけられる。", 1),
    # §11 P01 epistemic scope
    ("著者PDFの字体符号化の制約から本文の全体を機械で読み解くことはできず、抄録の外側の細部には踏み込まない。",
     "本節で用いるのは入手・確認できた一次資料の抄録水準の記述であり、細部には踏み込まない。", 1),
    # §9 editorial cleanup
    ("README表層で示す。", "公開リポジトリで確認できる範囲では示す。", 1),
    ("ファイル水準の提供範囲は未確認であり、版確定時の結びつけに委ねる。",
     "ファイル水準の提供範囲は未確認であり、本節の主張は公開リポジトリで確認できる範囲に留まる。", 1),
    ("第三者文書の許諾文や帰属記載", "第三者データの許諾文や帰属記載", None),
    ("性能の主張は後継側の記録に譲り、本節では機構の来歴に範囲を限って数値の優劣には立ち入らない。",
     "性能の主張はQwen3-VLの評価に譲り、本節では機構の来歴に範囲を限って数値の優劣には立ち入らない。", 1),
    ("本記録は著者測定でプレプリント段階であり、独立した第三者再現は未確認である。",
     "本節の記録は著者測定でプレプリント段階であり、独立した第三者再現は未確認である。", 1),
    ("本記録は変種としての位置であり、記述は簡潔に留める。",
     "本節では変種としての位置づけに留め、記述は簡潔にする。", 1),
    ("Visual Genomeの領域記述体制がGoldG的実践へ連なる来歴は、GLIP側の資料に委ねる範囲として添える。",
     "Visual Genomeの領域記述データの蓄積がGoldGのデータ体制へつながる来歴は、GLIPの節で扱う範囲として添える。", 1),
    ("GLIPの資料実践再定式とは契約が異なり", "GLIPのデータ実践による再定式とは契約が異なり", 1),
    # §7 grounding normalization (ambiguous/mixed spots)
    ("画面操作契約は接地と状態管理で分ける。", "画面操作契約はグラウンディングと状態管理で分ける。", 1),
    ("接地座標は0から1000へ正規化される。", "位置座標は0から1000へ正規化される。", 1),
    ("接地座標は0から1000に正規化され、", "位置座標は0から1000に正規化され、", 1),
    # §6 robot demonstrations
    ("97万件の実機実証で学ぶ。", "97万件の実ロボット実演データで学ぶ。", 1),
    ("97万件の実機実証で29課題の実機成功を測り", "97万件の実ロボット実演データで29課題の実機成功を測り", 1),
    ("97万件実機実証で29課題実機成功を測り", "97万件の実ロボット実演データで29課題実機成功を測り", 1),
]

NEW_P13_B2 = ("RT-1は実ロボットの実演データを大規模に集めて方策学習の規模化を進めたRobotics Transformerである。実働ロボットを用い、量と規模と多様性の関数として実環境での汎化を調べ、軌道条件づけを規模で学ばせる実演データの集積という位置にある。方策機構の詳細はRT-2の説明で扱う。RT-2はこの系譜に行動トークン化を持ち込み、視覚言語モデルの出力空間へ行動をテキストトークンとして組み込むVLA定式を導入した。その後、Open X-Embodimentは22機種と527技能と16万件超の課題を21機関から集め、多数の機体・技能・機関をまたぐデータ契約へ規模を広げた。RT-Xは複数機種で正の転移を示したと論文著者らは述べる。データ契約の主張であって方策の主張ではなく、操作域を扱う。実演データの集積が後の定式を直接生んだという読みは取らず、条件違いの数値を並べて順位づけない。")

NEW_P09_B10_HEAD = ("第二の系譜のオープン性はモデルの重みとデータの提供で示される。InternVLリポジトリはモデルの重みとInternVL-Dataの公開、1.0から3.5までの報告系譜と論文対応、3.5-GPT-OSS系の学習コード公開を公開リポジトリで確認できる範囲では示す。3.5系の存在は来歴注記に留める。ファイル水準の提供範囲は未確認であり、本節の主張は公開リポジトリで確認できる範囲に留まる。")

NEW_P11_B10 = ("SAM 3は、概念プロンプトに基づく動画内の検出・セグメンテーション・追跡を扱い、memory-based trackerによって時間方向の対象対応を維持する。これはvideo concept grounding / trackingの補助例であり、保存済み動画から必要箇所をquery-drivenに取得する契約とは異なる。保存済みタイムラインのオンデマンドな移動・取得はVM-D112エージェント型理解の契約であり、本節の三契約の列を保つ。")

NEW_P15_B04_GPT = ("GPT-5.5はトークン効率に優れた到達として二値完遂で約13%に頭打ちになると報告され、課題成功と部分完遂とツール呼び出しと出力トークン量とステップ予算は別の軸で読む。")
OLD_P15_B04_GPT = "GPT-5.5系は13%前後の効率頭打ちが著者測定として記される。"

P11_MC_OLD = "SAM 3 memory video tracking as supporting stored-timeline evidence"
P11_MC_NEW = ("SAM 3 concept-prompted video grounding and memory-based tracking are supporting "
              "temporal-grounding evidence; stored-timeline on-demand navigation remains the "
              "distinct VM-D112 contract.")

MOLMO2 = "molmo2リポジトリはデータ準備と事前学習やSFTや長文脈SFT、評価ツール群、vLLM推論、チェックポイント変換、MolmoPoint拡張をコード水準で確認する。"


def main() -> int:
    spec = json.loads(IN.read_text(encoding="utf-8"))

    def all_texts():
        for p in spec["packages"]:
            for f in ("headline", "deck"):
                if p.get(f):
                    yield p["package_id"], f, p[f]
            for b in p["blocks"]:
                if b.get("text"):
                    yield p["package_id"], b["block_id"], b["text"]
            if p.get("boundaries_text"):
                yield p["package_id"], "boundaries", p["boundaries_text"]

    for old, new, expected in REPLACEMENTS:
        hits = 0
        for pid, field, text in all_texts():
            if old in text:
                hits += text.count(old)
        if expected is not None:
            assert hits == expected, f"expected {expected} hits for {old[:50]!r}, found {hits}"
        else:
            print(f"info: {old[:45]!r} hits={hits}")

    for p in spec["packages"]:
        for field in ("headline", "deck"):
            if p.get(field):
                for old, new, _ in REPLACEMENTS:
                    if old in p[field]:
                        p[field] = p[field].replace(old, new)
        for b in p["blocks"]:
            if not b.get("text"):
                continue
            for old, new, _ in REPLACEMENTS:
                if old in b["text"]:
                    b["text"] = b["text"].replace(old, new)
        if p.get("boundaries_text"):
            for old, new, _ in REPLACEMENTS:
                if old in p["boundaries_text"]:
                    p["boundaries_text"] = p["boundaries_text"].replace(old, new)

    def get_block(pid, bid):
        p = next(x for x in spec["packages"] if x["package_id"] == pid)
        return p, next(x for x in p["blocks"] if x.get("block_id") == bid)

    _, b2 = get_block("P13", "P13-B2")
    assert "後の行動トークン化を可能にした" in b2["text"]
    b2["text"] = NEW_P13_B2
    b2["discovery_ids"] = ["VM-D094", "VM-D096", "VM-D097"]

    _, b04 = get_block("P15", "P15-B04")
    assert OLD_P15_B04_GPT in b04["text"]
    b04["text"] = b04["text"].replace(OLD_P15_B04_GPT, NEW_P15_B04_GPT)

    _, b10 = get_block("P09", "p09-b10")
    idx = b10["text"].find(MOLMO2)
    assert idx > 0, "molmo2 anchor missing in P09-B10"
    b10["text"] = NEW_P09_B10_HEAD + b10["text"][idx:]

    set_block_p11 = get_block("P11", "p11-b10")
    set_block_p11[1]["text"] = NEW_P11_B10

    # P04-B5 narrowed + D047 (re-assert; idempotent rebuild from r8 spec)
    p04, b5 = get_block("P04", "p04-b5")
    assert "GoldG" in b5["text"]
    b5["text"] = ("関係構造の来歴として、Visual Genomeは領域記述データの先行形態にも位置づけられる。後の検出-接地統一学習（GLIPの語句接地への書き直し）が前提にする領域と言語の対応づけの原型を示す点に、ここへ置く理由がある。GoldGの構成の詳細や直接の来歴関係までは主張せず、本節では関係構造の限定事例として扱い、語彙拡張の系統史へは広げない。独立した第三者の再現ではなく原論文の測定として読む。")
    b5["discovery_ids"] = ["VM-D021", "VM-D047"]
    # P08-B8 += D060 (re-assert)
    p08, b8 = get_block("P08", "p08-b8")
    if "VM-D060" not in b8["discovery_ids"]:
        b8["discovery_ids"] = sorted(b8["discovery_ids"] + ["VM-D060"])
    # P07B-B14 += D049 (re-assert)
    p7b, b14 = get_block("P07B", "P07B-B14")
    if "VM-D049" not in b14["discovery_ids"]:
        b14["discovery_ids"] = sorted(b14["discovery_ids"] + ["VM-D049"])
    # P05-B10 += D110 (re-assert)
    p05, b10_05 = get_block("P05", "P05-B10")
    assert "OCRBench v2の23課題" in b10_05["text"]
    if "VM-D110" not in b10_05["discovery_ids"]:
        b10_05["discovery_ids"] = sorted(b10_05["discovery_ids"] + ["VM-D110"])
    # P11 must_cover_map (r8 wording)
    p11 = next(x for x in spec["packages"] if x["package_id"] == "P11")
    mmap = p11.get("must_cover_map")
    assert mmap is not None
    if P11_MC_OLD in mmap:
        mmap[P11_MC_NEW] = mmap.pop(P11_MC_OLD)
    assert P11_MC_NEW in mmap

    spec["draft_version"] = "fresh-121-r8-rev2"
    spec["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 Draft closure revision r8-rev2 from Architecture r8 APPROVED "
                       "(same authority; final targeted reader-facing repair: P13 VLA lineage split, "
                       "P15 GPT-5.5 wording, robot-demonstration terms, grounding normalization, P09 "
                       "duplicate removal, editorial/workflow cleanup; r8 authority unchanged; "
                       "no TeX/PDF; DRAFT_COMPLETE held for independent content review)"),
        "generated_at": "2026-10-07T10:00:00Z",
        "run_reference": None,
    }
    OUT.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # STRICT post-verification on the OUTPUT spec
    blob = OUT.read_text(encoding="utf-8")
    must_be_gone = [o for o, _, _ in REPLACEMENTS] + [
        "対象期間外に公開された記録は本稿の根拠に含めない",
        "初の全範囲の映像評価", "全域測定", "伴走する問答",
        "体系側の記録の所管", "既存の収集範囲を置き換えるものではない",
        "版確定時の検証作業", "方策機構の細部はRT-2側資料の所管",
        "カメラ位置の鋭敏さ", "対応づけ済み40件",
        "後の行動トークン化を可能にした",
        "実機実証", "利用画面", "128万ラベル",
    ]
    bad = [(s, blob.count(s)) for s in must_be_gone if s in blob]
    assert not bad, f"old strings survive in output spec: {bad}"
    assert blob.count(MOLMO2) == 1, f"molmo2 sentence count != 1: {blob.count(MOLMO2)}"
    must_be_present = ["数千倍多く用いてfine-tuneした専用モデル",
                       "language-guided query selection（言語誘導型クエリ選択）",
                       "自然言語クエリでDETRを条件づけ",
                       "大規模画像テキスト対による教師信号",
                       "入手・確認できた一次資料の抄録水準",
                       "公開リポジトリで確認できる範囲では示す",
                       "第三者データの許諾文",
                       "Qwen3-VLの評価に譲り",
                       "本節の記録は著者測定でプレプリント段階",
                       "本節では変種としての位置づけに留め",
                       "GoldGのデータ体制へつながる来歴は、GLIPの節で扱う",
                       "GLIPのデータ実践による再定式",
                       "グラウンディングと状態管理で分ける",
                       "位置座標は0から1000",
                       "実ロボット実演データ",
                       "二値完遂で約13%に頭打ち",
                       "query-drivenに取得する契約とは異なる"]
    missing = [s for s in must_be_present if s not in blob]
    assert not missing, f"new forms missing: {missing}"
    print(f"rev2 spec verified clean: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
