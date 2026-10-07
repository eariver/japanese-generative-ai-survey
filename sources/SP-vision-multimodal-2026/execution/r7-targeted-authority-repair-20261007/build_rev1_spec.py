#!/usr/bin/env python3
"""Build compact-input-fresh-121-r7-rev1.json: targeted semantic/editorial repair.

- Exact-string replacements (asserted found): §7 terminology, §8 workflow,
  P07B rhythm openers/closers, P06/P07A captioning terms.
- Full-block rewrites (asserted by block_id): p11-b2, p08-b8 (+VM-D060 binding),
  P07B-B14, P07A-B05 trim, p10-b7/p11-b9/p11-b8/p11-b10 trims.
- Synthesis payload: 計画側 -> プランニング側.
- draft_version fresh-121-r7-rev1. No upstream/Architecture change.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r7-targeted-authority-repair-20261007"
IN = EDIR / "compact-input-fresh-121-r7.json"
OUT = EDIR / "compact-input-fresh-121-r7-rev1.json"

REPLACEMENTS = [
    # §7 terminology
    ("飛び越し結合", "スキップ接続"),
    ("多作物と小パッチ", "マルチクロップと小パッチ"),
    ("説明復号器LocCaによる見出し学習", "説明デコーダLocCaによるキャプション生成学習"),
    ("説明デコーダLocCaによる見出し学習", "説明デコーダLocCaによるキャプション生成学習"),
    ("限界は教師にboundedすることであり", "限界は教師モデルに制約されることであり"),
    ("端到端の調整検出器を構成した", "端到端の条件付き検出器を構成した"),
    ("企画側接地を示す分岐点", "プランニング側の接地を示す分岐点"),
    ("言語モデルが企画を担い", "言語モデルがプランニングを担い"),
    ("企画側に留まり知覚と言語を束ねない点", "プランニング側に留まり知覚と言語を束ねない点"),
    ("操作企画と視覚質問応答と説明生成にまたがり", "操作のプランニングと視覚質問応答と説明生成にまたがり"),
    ("企画分離と統合を混ぜず", "プランニングの分離と統合を混ぜず"),
    ("難関長期課題は調整と上位言語企画を要し、規模と機材鋭敏さと推論負担が残る。",
     "難関長期課題は調整と上位の言語プランニングを要し、規模とハードウェア構成への感度と推論負担が残る。"),
    ("実世界理解と多段企画を担うER 2", "実世界理解と多段プランニングを担うER 2"),
    ("実世界理解・多段企画の分業", "実世界理解・多段プランニングの分業"),
    ("企画と方策の分業を能力段階で示す", "プランニングと方策の分業を能力段階で示す"),
    ("効率と転移の両立が読みどころであり、企画への利用は主張しない。",
     "効率と転移の両立が読みどころであり、プランニングへの利用は主張しない。"),
    ("ここでは行動なし事前学習と固定評価が要点であり、企画への利用は次段の記録が担う。",
     "ここでは行動なし事前学習と固定評価が要点であり、プランニングへの利用は次段の記録が担う。"),
    ("新味は3D-RoPE安定化と規模と行動条件づけ追加学習と企画利用とVideoQA言語結合にある。",
     "新味は3D-RoPE安定化と規模と行動条件づけ追加学習とプランニング利用とVideoQA言語結合にある。"),
    ("地平H=50の系列をフロー照合の場を10段Eulerで解いて生成し",
     "ホライズンH=50の系列をflow matching（フローマッチング）のベクトル場を10段Eulerで解いて生成し"),
    ("安定してしなやかに測る道を開いた", "安定した評価の道を開いた"),
    # §8 + §11 workflow/scope
    ("一般場面への持ち込みは別の記録の所管である。", "一般場面への展開は本節では扱わない。"),
    ("既存の収集範囲の置換ではない。", "既存の収集範囲を置き換えるものではない。"),
    ("LongVideoBenchの6,678問を含む行単位の対応づけと3.8 Flash行の確定は下流の作業に委ねる。",
     "LongVideoBenchの6,678問を含む行単位の対応づけと3.8 Flash行の確定は、版確定時の検証作業に委ねる。"),
    ("窓外に置かれた記録は本文根拠に用いず繰り延べとし、方策利用の記録も表現十分性の観点からは取り込まずにおく。",
     "対象期間外に公開された記録は本稿の根拠に含めない。方策利用の記録は、表現の十分性を論じる限りでは取り込まない。"),
    ("対応づけ済み40件を過不足なく配し、後続の各群はこの共通語彙からの差分だけを記す。",
     "後続の各群はこの共通語彙からの差分だけを記す。"),
    ("transferはResNetのEvidenceで確認された検出・セグメンテーション条件までを扱い、それを超える一般的なtransfer claimへ拡張しない。",
     "transferはResNetの検出・セグメンテーション転移の報告で確認された条件までを扱い、それを超える一般的なtransfer claimへ拡張しない。"),
    # P07B rhythm: axis-framed openers
    ("接地から検出への定式がなかった局面で、オープンボキャブラリー検出が命名された。",
     "認識と位置特定の教師を分けて検出を組み立てる方式として、オープンボキャブラリー検出が命名された。"),
    ("画像水準の教師を検出器へ移す手段がなかった局面で、蒸留によるOVDが示された。",
     "画像水準の教師を蒸留で検出器へ移す方式として、ViLDによるOVDが示された。"),
    ("CLIPを領域にそのまま当てはめる段階では、画像全体の照合が領域に適合しない不足が残った。",
     "画像全体の照合では領域水準の対応が足りない。疑似領域文対で領域表現を学ぶ方式として、RegionCLIPが示された。"),
    ("箱注釈なしに検出器をオープンボキャブラリー化するには、画像水準教師の割当てが要った。",
     "箱注釈なしの語彙拡張を画像水準教師の素朴な割当てで果たす方式として、Deticが示された。"),
    ("検出と接地を別課題とする枠組みでは、両者を一つの学習にまとめる再定式が要った。",
     "検出と接地を一つの学習にまとめる再定式として、GLIPは検出を語句の接地へ書き直した。"),
    ("質問と画像の早期融合がなかった局面で、言語条件づけの検出器が示された。MDETRは生文質問でDETRを条件づけ、",
     "文と画像を早期に融合させる言語条件づけの方式として、MDETRは自然文の質問でDETRを条件づけ、"),
    ("密な融合を前提としない最小構成がなかった局面で、素朴な転移手順が示された。",
     "密な融合を足さない最小構成の転移手順として、OWL-ViTが示された。"),
    ("接地事前学習と検出器の密な結合がなかった局面で、3段階の密な融合が示された。",
     "接地学習と検出器を三段階で密に結ぶ融合設計として、Grounding DINOが示された。"),
    ("人手箱なしの拡張がなかった局面で、ウェブ規模の自己学習手順が示された。",
     "人手箱なしの拡張をウェブ規模の自己学習で果たす手順として、OWL-STとOWLv2が示された。"),
    ("固定ラベルに縛られない密な予測がなかった局面で、言語埋め込みによる分割が示された。",
     "固定ラベルに縛られない密な予測を言語埋め込みで果たす方式として、LSegによる分割が示された。"),
    ("汎用と指示参照の分割を一つの復号にまとめる手段と、生成基盤の転用が足りなかった。",
     "汎用分割と指示参照分割を一般化復号で統合する方式として、X-Decoderが示された。"),
    # P07B rhythm: varied closers
    ("固定分類から開かれた語句集合への局在化が開かれた。", "固定分類から開かれた語句集合への局在化が可能になった。"),
    ("語彙を埋め込みに開いた検出の定式化が開かれた。", "語彙を埋め込みに開いた検出の定式化が与えられた。"),
    ("教師に縛られた検出器のオープンボキャブラリー化が開かれ、", "教師に縛られた検出器のオープンボキャブラリー化が果たされ、"),
    ("領域水準の事前学習によるOVD基盤の強化が開かれた。", "領域水準の事前学習によるOVD基盤の強化が図られた。"),
    ("込み入った割当てを要しない語彙拡張が開かれた。", "込み入った割当てを要しない語彙拡張が果たされた。"),
    ("追加要素なしの検出適応が開かれた。", "追加要素なしの検出適応が可能になった。"),
    ("密な融合によるオープンボキャブラリー検出が開かれた。", "密な融合によるオープンボキャブラリー検出が実現された。"),
    ("希少区分の自己学習による拡張が開かれた。", "希少区分の自己学習による拡張が果たされた。"),
]

NEW_P11_B2 = ("Something-Something V1は、108,499本の群衆実演動画を174種類のcaption-template action classへ分類するデータセットである。物体操作の時間的な進行を区別する必要があり、静的な外観だけでは捉えにくい時間順序への感度を評価する。雛形の区分の範囲での扱いに留め、短い振る舞いの分類を超える時間の推論一般の主張はしない。Kineticsの分類の広さと比べると、時間順序への感度が要点になる。")

NEW_P08_B8 = ("系譜を通覧すると、別々に事前学習されたコンポーネントの結合は段階を追って収束する。Frozenの前置きを起点にFlamingoのgated cross-attentionと交互配置集合が少数例での汎化を切り開き、BLIP-2の二段階が凍結の節約を定式化した。InstructBLIPは既存の公開視覚言語データセット26件を指示形式へ変換し、指示を読み取るQ-Formerで調整する。26件の指示化と13のheld-out集合でのゼロショット首位、画像付きScienceQA 90.7%が著者測定として示される。核はBLIP-2土台の指示形式変換であり、GPT-4による合成指示生成ではない。LLaVAは対照的に、画像を見ない言語専用GPT-4が記号化した説明とボックスから15万8000件の合成指示集合を生成し、第一段で視覚と言語モデルを凍結してprojectionのみ、第二段で視覚を凍結したままprojectionと大規模言語モデルを学ぶ。両者は指示追従へ向かうが、データ生成（既存公開集合の指示化かGPT-4合成か）と学習対象（指示読み取りQ-Formerか段階的projection/LLMか）の契約が異なる。MolmoとPixMoは外部蒸留なしの開かれた集合で同列の到達を示し、pointingを含む評価の幅と開放データおよびコードによる確認可能性を押し広げた。少数例対応や指示追従の欠落は順に計算可能となったが、言語事前分布に由来する幻覚や合成依存、高解像度知覚の限界は残存する。")

NEW_P07B_B14 = ("本節の系譜は、語句と領域の対応づけを担う資料（Flickr30k Entitiesの24.4万共参照鎖・27.6万箱）から、検出を語句の接地へ書き直す資料実践（GLIPの27M接地集合：人手3Mとウェブ由来24M）、検出器と接地学習を三段階で結ぶ密な融合（Grounding DINO）へ進んだ。教師の置き方（ViLDの蒸留かGLIPの資料実践か）と融合の位置（MDETRの早期融合か後段での融合）と出力（箱か語句接地か）で系統が分かれる。LVIS-rareのAPと語句接地のRecallを別指標で測り、画像水準のゼロショットや検索Recall@Kとも混ぜない点が共通の約束である。希少区分の手順は利用ごとに明示し、ウェブ資料依存の限界を条件づける。単一構成の勝利ではなく、粒度と代償の未解決を残す。")

NEW_P07A_B05 = ("SigLIP 2は、CLIPが開いた画像文対応の系譜を段階的な教師で強める。対ごとシグモイド損失を保ったまま、キャプション生成（説明デコーダLocCa）、自己蒸留（SILCの局所全体間）、マスク予測を組み合わせ、WebLIの109言語混合とNaFlexの縦横比保持で学ぶ。RefCOCOの接地やOWL-ViTの検出や密な探索、PaliGemma型凍結転移の伸びは、画像水準の対応の延長として読む。NaFlexの外挿の弱さや多言語の代償など限界は原論文の範囲に残る。位置や領域への接地そのものは次節の契約であり、指標を混ぜない。")

NEW_P10_B7 = ("知覚を道具で助ける循環は、保存済み映像を問いに応じて探す第三の方式である。エージェント型理解は全時間軸の事前取り込みをやめ、問いごとの区間取り寄せと関心窓の取り直しで費用を変える。効率値（長尺で最大88%少ないトークン等）は提供元測定の上限であり、対象は蓄積済み投稿とYouTubeの時間軸に限る。自律的推論一般の根拠でも、オンライン状態の根拠でもない。素の知覚から補助手順を経て道具利用へ至り、誤りの帰属を定める第三段である。")

NEW_P11_B9 = ("Agentic Video Understandingは蓄積済み動画とYouTubeの時間軸を問いに応じてたどる第三の契約であり、オンラインの流れを受け続ける状態とは別の列に置く。静止処理（毎秒1フレーム・単一音声チャンネル毎秒1キロビット）では速い動きの細部が落ちる場合があり、道具利用の処理は問いごとの区間取り寄せと関心窓の取り直しで費用を変える。長尺で最大88%少ないトークン等の効率値は提供元測定の上限である。対象はオフライン時系列であり、連続取り込みのオンライン状態ではない。")

NEW_P11_B8 = ("空間の理解を助ける手順の効果は、VSI-Benchが288本の一人称映像と5131の質問で示す。思考の連鎖で下がり認知地図で上がる所見は、補助手順の切り分けが本節の契約とは別の列にあることを示す。記述は論文要旨の水準に留め、偏り除去の部分集合分析には踏み込まない。")

NEW_P11_B10 = ("保存済みタイムラインへの概念指示として、SAM 3のPromptable Concept Segmentationを補助的根拠に置く。単純な名詞句と画像例の正負ボックス、SAM 2型の視覚クリックで指示し、存在トークンの分離が認識と位置特定を分ける。言語接地の概念インターフェースという新規性と細粒度ゼロショットの弱さ等の限定はP03の範囲であり、ここでは保存済み時間軸の契約として位置づける。")


def main() -> int:
    spec = json.loads(IN.read_text(encoding="utf-8"))
    n_replace = 0
    for pid in [p["package_id"] for p in spec["packages"]]:
        pass
    for p in spec["packages"]:
        for b in p["blocks"]:
            for old, new in REPLACEMENTS:
                if old in b.get("text", ""):
                    b["text"] = b["text"].replace(old, new)
                    n_replace += 1
        if p.get("boundaries_text"):
            for old, new in REPLACEMENTS:
                if old in p["boundaries_text"]:
                    p["boundaries_text"] = p["boundaries_text"].replace(old, new)
                    n_replace += 1
        if p.get("headline"):
            for old, new in REPLACEMENTS:
                if old in p["headline"]:
                    p["headline"] = p["headline"].replace(old, new)
                    n_replace += 1
        if p.get("deck"):
            for old, new in REPLACEMENTS:
                if old in p["deck"]:
                    p["deck"] = p["deck"].replace(old, new)
                    n_replace += 1
    print(f"exact replacements applied: {n_replace} (hits across blocks/boundaries/headlines/decks)")

    def set_block(pid, bid, text, discovery_ids=None):
        p = next(x for x in spec["packages"] if x["package_id"] == pid)
        b = next(x for x in p["blocks"] if x["block_id"] == bid)
        b["text"] = text
        if discovery_ids is not None:
            b["discovery_ids"] = discovery_ids
        return b

    set_block("P11", "p11-b2", NEW_P11_B2)
    b8 = set_block("P08", "p08-b8", NEW_P08_B8, ["VM-D058", "VM-D060", "VM-D062", "VM-D063"])
    b14 = set_block("P07B", "P07B-B14", NEW_P07B_B14,
                    ["VM-D041", "VM-D044", "VM-D047", "VM-D048", "VM-D050", "VM-D056"])
    set_block("P07A", "P07A-B05", NEW_P07A_B05, ["VM-D039", "VM-D114"])
    set_block("P10", "p10-b7", NEW_P10_B7)
    set_block("P11", "p11-b9", NEW_P11_B9)
    set_block("P11", "p11-b8", NEW_P11_B8)
    set_block("P11", "p11-b10", NEW_P11_B10)
    print("8 blocks rewritten")

    syn = spec["synthesis"]["profile_payload"]
    assert "計画側の分業" in syn["parallel_competing_relations"]
    syn["parallel_competing_relations"] = syn["parallel_competing_relations"].replace(
        "計画側の分業と一体の行動表現", "プランニング側の分業と一体の行動表現")

    spec["draft_version"] = "fresh-121-r7-rev1"
    spec["runner"]["invocation"] = ("TS-003 Draft closure revision r7-rev1 from Architecture r7 APPROVED "
                                    "(same authority; targeted semantic/editorial repair: SSv1 task identity, "
                                    "InstructBLIP/LLaVA contracts, P07B synthesis granularity + rhythm, "
                                    "technical Japanese, workflow-vocabulary purge, SigLIP2/P07A role split, "
                                    "cross-package dedup, reader-scope cleanup; r7 authority unchanged; "
                                    "no TeX/PDF; DRAFT_COMPLETE held for final AI closure review)")
    spec["runner"]["generated_at"] = "2026-10-07T05:00:00Z"
    OUT.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"rev1 spec: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
