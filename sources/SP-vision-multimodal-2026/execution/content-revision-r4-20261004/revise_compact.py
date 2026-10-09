#!/usr/bin/env python3
"""Revise compact Draft input per supplied fresh independent content review.

Reads bounded-revision compact-input.json, applies Evidence-bounded repairs +
terminology normalization + semantic-padding reduction + P15 overlay refs,
writes content-revision-r4-20261004/compact-input-revised.json with audit counts.
No upstream (Matrix/Selection/Evidence/Architecture) changes. No Core changes.
"""
from __future__ import annotations
import copy
import json
import re
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
INDIR = SRC / "execution/bounded-revision-112-20261004"
OUTDIR = SRC / "execution/content-revision-r4-20261004"

counts: dict[str, int] = {}


def bump(key: str, n: int = 1):
    counts[key] = counts.get(key, 0) + n


def sub_once(text: str, old: str, new: str, key: str) -> str:
    if old in text:
        bump(key, text.count(old))
        return text.replace(old, new)
    return text


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[。！？])", text)
    return [p for p in parts if p.strip()]


def join_sentences(sents: list[str]) -> str:
    return "".join(sents)


def drop_containing(sents: list[str], substrs: list[str], key: str) -> list[str]:
    out = []
    for s in sents:
        if any(u in s for u in substrs):
            bump(key)
            continue
        out.append(s)
    return out


def main() -> int:
    data = json.loads((INDIR / "compact-input.json").read_text(encoding="utf-8"))
    data = copy.deepcopy(data)
    data["draft_version"] = "content-revision-r4-20261004"
    pkgs = {p["package_id"]: p for p in data["packages"]}

    # ---------------- P06 DINO ----------------
    b = next(x for x in pkgs["P06"]["blocks"] if x["block_id"] == "p06-b4")
    t = b["text"]
    # Delete 4 unsupported temperature/centering sentences (exact strings from audit)
    for old in [
        "崩壊の回避は中心化と鋭化の二点にあり、前者は出力の平均を引いて一様解を防ぎ、後者は温度で分布を尖らせて余白を保つ。",
        "温度の二重設計は、生徒側を尖らせ教師側を滑らかにする非対称にあり、崩壊の回避と学習の進行を両立させる。",
        "中心化の更新は指数移動平均でゆっくり行い、急な変化が学習を壊さないようにする。",
        "手順の具体は、生徒と教師の二役を一つの系列に担わせ、教師側を生徒の指数移動平均でゆっくり動かす点にある。",
    ]:
        if old in t:
            bump("P06-DINO-temperature-removed")
            t = t.replace(old, "")
    # Insert one Evidence-bounded momentum-encoder sentence at the anchor point
    anchor = "人手の教師を要さず、教師の役割が学習の進行とともに育つ。"
    if anchor in t:
        t = t.replace(anchor, anchor + "学習の安定には教師側を生徒の指数移動平均で緩やかに更新する仕組みが用いられる。", 1)
        bump("P06-momentum-kept")
    b["text"] = t

    # ---------------- P02 RetinaNet ----------------
    b = next(x for x in pkgs["P02"]["blocks"] if x["block_id"] == "p02-b05")
    t = b["text"]
    t = sub_once(t, "入力や骨格を変えず目的関数の重みづけを変えた点が、前任との技術的な差である。",
                 "目的関数の重みづけを変えた点が、損失側の診断としての技術的な差である。", "P02-invariant-softened")
    t = sub_once(t, "骨格や解像度を変えずに目的関数のみで精度を引き上げた点に、形状と損失の切り分けの意義がある。",
                 "不均衡の診断を損失の重みづけで解く点に、この記録の意義がある。", "P02-invariant-removed")
    b["text"] = t

    # ---------------- P07A ----------------
    b = next(x for x in pkgs["P07A"]["blocks"] if x["block_id"] == "p07a-b4")
    t = b["text"]
    for old in [
        "全体照合の限界は、語の並びや帰属の読みの落ちに現れる。",
        "どの語がどの物に掛かるかの構造が一括の照合では抜け落ち、語順を入れ替えても点が動かない振る舞いが後の診断で暴かれる。",
        "属性の結びつけの失敗も同根であり、色や形や位置の帰属が全体の類似では解けない。",
        "数え上げや空間関係の弱さも同じ一括性の帰結である。",
        "後の診断の顔ぶれは、語順の入れ替えや属性の付け替えの制御pairに及び、一括照合の弱さを暴く方向に進む。",
    ]:
        if old in t:
            bump("P07A-beyond-card-removed")
            t = t.replace(old, "")
    b["text"] = t
    b = next(x for x in pkgs["P07A"]["blocks"] if x["block_id"] == "p07a-b6")
    t = b["text"]
    t = sub_once(t, "言語先行の近道は応答の課題で暴かれ、語順や帰属の落ちは照合の限界として残り、二つの残りが接地への動機になる。",
                 "言語先行の近道は応答の課題で確かめられ、一括照合では語と物の対応の構造が抜け落ちる点がグラウンディングへの動機になる。", "P07A-b6-bounded")
    t = sub_once(t, "接地への動機の二点は、一括照合の語順や帰属の落ちと、決まった区分を超える言葉の要請であり、前者が構成の動機、後者が語彙の動機になる。",
                 "グラウンディングへの動機の二点は、一括照合での対応構造の欠落と、決まった区分を超える言葉の要請であり、前者が構成の動機、後者が語彙の動機になる。", "P07A-b6-bounded2")
    b["text"] = t

    # ---------------- P07B linear -> branching ----------------
    b = next(x for x in pkgs["P07B"]["blocks"] if x["block_id"] == "p07b-b13")
    t = b["text"]
    t = sub_once(t, "読み筋の要点は、定式から蒸留へ、蒸留から語彙拡張へ、語彙拡張から言い換えへ、言い換えから融合へ、融合から規模化へ、規模化から分割枝への六段にあり、段の順序が lineage の理解になる。",
                 "読み筋の要点は、定式の起点と蒸留による転移と語彙拡張と融合の二系統と規模化と分割枝の六群の並立にあり、群の違いが系譜の理解になる。", "P07B-linear-removed")
    b["text"] = t

    # ---------------- P10 POPE ----------------
    for bid in ("p10-b3", "p10-b5", "p10-b2", "p10-b4"):
        for x in pkgs["P10"]["blocks"]:
            if x["block_id"] == bid:
                t = x["text"]
                # First-use full operation phrase only in p10-b3 first occurrence
                if bid == "p10-b3" and "投票型の問いかけで安定にしなやかに測る" in t:
                    t = t.replace("投票型の問いかけで安定にしなやかに測る",
                                  "反復的な二値質問によるobject probing（polling-based query）で安定に測る", 1)
                    bump("P10-polling-full-phrase")
                t = t.replace("投票型評価", "POPEの質問方式による評価")
                t = t.replace("投票型の測定", "POPEの質問方式による測定")
                t = t.replace("投票型", "POPEの質問方式")
                if "投票型" in x["text"]:
                    bump("P10-投票型-removed", x["text"].count("投票型"))
                # 定石 removal
                t = sub_once(t, "一次検査で疑わしい箇所を見つけ、制御ペアで原因を切り分ける順序が、失敗の分解の定石になる。",
                             "一次検査で疑わしい箇所を見つけ、制御ペアで原因を切り分ける順序で調べる。", "P10-定石-removed")
                t = sub_once(t, "という段取りが、費用と精度の配分の定石になる。",
                             "という段取りで費用と精度の配分を調整する。", "P10-定石-removed2")
                x["text"] = t

    # ---------------- P09 ----------------
    b = next(x for x in pkgs["P09"]["blocks"] if x["block_id"] == "p09-b2")
    t = b["text"]
    t = sub_once(t, "画素を捨てるのではなく並べ替えてまとめる手順であり、情報を落とさずに数を減らす点が単純な間引きとの違いである。",
                 "画素を捨てるのではなく空間情報をチャネル方向へ再配置してまとめる手順であり、単純な縮小とは異なる形で高解像度情報を保持する点が単純な間引きとの違いである。", "P09-pixel-unshuffle-softened")
    b["text"] = t
    # 通貨的 -> 時間的な (P09 b10 x2)
    for x in pkgs["P09"]["blocks"]:
        if "通貨的" in x["text"]:
            x["text"] = x["text"].replace("通貨的な新しさ", "時間的な新しさ")
            bump("P09-通貨的-fixed", 1)

    # ---------------- P12 ----------------
    for x in pkgs["P12"]["blocks"]:
        if x["block_id"] == "p12-b7" and "通貨の確認が必要" in x["text"]:
            x["text"] = x["text"].replace("通貨の確認が必要", "鮮度の確認が必要")
            bump("P12-通貨の確認-fixed")

    # ---------------- P13 言う側/できる側 ----------------
    for x in pkgs["P13"]["blocks"]:
        t = x["text"]
        n1, n2 = t.count("言う側"), t.count("できる側")
        n3 = t.count("言える側")
        t = t.replace("言う側", "言語側").replace("できる側", "行動側").replace("言える側", "言語側")
        if n1 or n2 or n3:
            bump("P13-言う側できる側-replaced", n1 + n2 + n3)
        x["text"] = t

    # ---------------- P14 ----------------
    b = next(x for x in pkgs["P14"]["blocks"] if x["block_id"] == "p14-b3")
    t = b["text"]
    t = sub_once(t, "絵を描き直す力を育てるのではなく絵の意味を言い当てる力を育てる。",
                 "絵を描き直す力を育てるのではなく潜在表現を予測する力を育てる。", "P14-言い当てる-fixed")
    t = sub_once(t, "見えている断片から見えていない部分の意味を言い当てる。",
                 "見えている断片から見えていない部分の潜在表現を予測する。", "P14-言い当てる-fixed2")
    t = sub_once(t, "描き直しと意味の言い当ての区別が、設計の出発点になる。",
                 "描き直しと潜在表現の予測の区別が、設計の出発点になる。", "P14-言い当てる-fixed3")
    b["text"] = t
    b = next(x for x in pkgs["P14"]["blocks"] if x["block_id"] == "p14-b4")
    t = b["text"]
    t = sub_once(t, "拡散型の画素復号器は符号化器を凍結したまま後から接地を確かめる調べにすぎず、生成の主張ではない。",
                 "拡散型の画素デコーダはエンコーダを凍結したまま後から獲得された特徴の内容を確かめる調べにすぎず、生成の主張ではない。", "P14-VJEPA-接地-fixed")
    b["text"] = t

    # ---------------- P04 tokenization reframe ----------------
    b = next(x for x in pkgs["P04"]["blocks"] if x["block_id"] == "p04-b5")
    t = b["text"]
    t = sub_once(t, "ここでトークンに刻むときの得失を整理する。",
                 "ここで系列に載せる際の得失を編集上の整理としてまとめる。", "P04-reframe")
    t = sub_once(t, "画像をトークン列に変換する際、奥行きの順序や配置の細部をどこまで保てるかは設計に依存する。",
                 "画像を系列に変換する際に奥行きの順序や配置の細部がどこまで保てるかは設計に依存し、本節の四件はその定量を扱わない。", "P04-reframe2")
    t = sub_once(t, "一般に解像度を上げればトークン数と計算の負担が増す交換が生じるが、本節の四件はこの交換の定量を扱わない。",
                 "解像度と系列長や計算の負担の交換は本節の記録からは断定せず、一般的な得失の見方は編集上の推論として弱めて読む。", "P04-reframe3")
    t = sub_once(t, "得る側は、順序と配置の状態をトークンの列に載せて後の推論の素材にできる点であり、失う側は、画素の細部の切り捨てとトークン増大の負荷の交換である。",
                 "得る側の見方は、順序と配置の状態を系列に載せて後の推論の素材にできる点であり、失う側の見方は細部の切り捨てと系列増大の負荷の交換であるが、いずれも本節の記録を超える断定ではなく編集上の推論として読む。系列化の契約の詳細はP06の系列化とP09の解像度・融合の記録を参照する。", "P04-reframe4")
    t = sub_once(t, "残すべきは順序と配置という状態であり、画素のすべてではないという整理が本節前半のまとめである。",
                 "残すべきは順序と配置という状態であるという整理が本節前半のまとめであり、画素の扱いの断定には別の記録が要る。", "P04-reframe5")
    b["text"] = t
    b = next(x for x in pkgs["P04"]["blocks"] if x["block_id"] == "p04-b6")
    t = b["text"]
    t = sub_once(t, "トークン化の得失の整理として、関係の三つ組や対応の組は離散の記号に切り分けやすい性質を持つ一方、尺度の不定は記号化で解消せず、人手の揺れも正準化の完全さを欠くため、正確さの根拠には独立した確かめが要る。",
                 "系列化の得失の整理として、関係の記述が記号に切り分けやすい面的な見方は編集上の推論であり、尺度の不定は記号化で解消せず人手の揺れも残るため、正確さの根拠には独立した確かめが要る。", "P04-b6-reframe")
    t = sub_once(t, "載せやすいのは、関係の三つ組や対応の組が離散の記号に切り分けやすいためであり、消えないのは、尺度の不定が記号化で解消せず、人手の揺れが正準化の完全さを欠くためである。",
                 "載せやすい面の見方は編集上の推論に留め、尺度の不定と人手の揺れが残る点は記録の限りとして読む。", "P04-b6-reframe2")
    b["text"] = t

    # ---------------- P05 ----------------
    b = next(x for x in pkgs["P05"]["blocks"] if x["block_id"] == "p05-b8")
    t = b["text"]
    for old in [
        "九種の推論型は、抜き出しで解ける問いと表や欄の対応を要する問いを分け、構造を読む力の測定を可能にする。",
        "問いの九類型は、図版と書式と表や箇条と配置と本文と写真と手書きと肯定否定とその他に分かれ、体裁ごとの読みを切り分ける。",
    ]:
        if old in t:
            bump("P05-9taxonomy-removed")
            t = t.replace(old, "")
    for old in [
        "汚染は中程度、言語先行の危うさは高いとされ、抜き出しの近道が残り、ウェブ文書の混入も避けがたい。",
        "言語先行の危うさは、問い文の癖だけで答えが当たる近道の存在であり、制御pairによる診断の起点を共有する。",
        "ウェブ文書の混入は学習と試験の隔たりの管理に属し、混入の有無の開示が測定の誠実さを保つ。",
    ]:
        if old in t:
            bump("P05-contamination-as-fact-removed")
            t = t.replace(old, "")
    # Insert one bounded replacement sentence
    anchor = "構造を読む問いと抜き出しで解ける問いの区別が、文書理解の測定の要点である。"
    if anchor in t:
        t = t.replace(anchor, anchor + "抜き出しの近道への弱さやウェブ文書の混入のおそれは、測定条件の開示と一緒に読む。", 1)
        bump("P05-bounded-insert")
    b["text"] = t

    b = next(x for x in pkgs["P05"]["blocks"] if x["block_id"] == "p05-b5")
    t = b["text"]
    for old in [
        "機構はDonutの系譜を引くSwin encoderとdecoderが配置と数式と表構造を文字起こしの延長で直列化する点にあり、数式の添字や表の桁揃えを系列生成で書き出す。",
        "直列化の具体は、頁画像をSwin系encoderで特徴化し、系列decoderが軽量markupを自己回帰に起こす点にある。",
        "本文の段落と見出し、LaTeX数式の添字や分数や行列、表の行列と結合セルを一つの記号列に載せる。",
        "読み順の復元は二段組や割り込み図版の回り込みを含み、頁の幾何から論理順序への変換を担う。",
        "体裁の内訳は、二段組の回り込みや割り込み図版や脚注や引用文献の扱いを含み、頁の幾何から論理順序への変換が読みの本体になる。",
        "図表の caption や表の罫線や数式番号の扱いが、markup復元の正確さを左右する。",
        "頁の幾何から論理順序への変換は、段組みの検出と図版の回避と脚注の分離を含み、幾何の読み違えが順序の崩れに直結する。",
        "幾何の正確さが直列化の前提であり、前提の崩れがmarkup全体の崩れになる。",
    ]:
        if old in t:
            bump("P05-Nougat-beyond-card-removed")
            t = t.replace(old, "")
    anchor = "科学論文PDFをmarkupに変換し、本文とLaTeX数式と表を一つの出力に載せる点にある。"
    if anchor in t:
        t = t.replace(anchor, "科学論文PDFをマークアップに変換し、本文と数式と表を一つの出力に載せる点にある。出力の内訳の細部は記録の範囲を超えるため、本書では変換の契約と限界の三点の範囲で読む。", 1)
        bump("P05-Nougat-bounded-insert")
    b["text"] = t

    b = next(x for x in pkgs["P05"]["blocks"] if x["block_id"] == "p05-b6")
    t = b["text"]
    for old in [
        "圧縮の具体は、80M級encoderが1024画素級の入力を256 token級に畳み、長いcontextのdecoderが受ける点にある。",
        "この圧縮により長い文書を一つのmodelで受ける。",
        "読みの三様式は、素の文字起こしと用途別の整形出力、領域指定の対話的読み、解像度を動かす読みと複数頁の読みであり、同じ頁画像からmarkdownや数式や表や図中記号を取り分ける。",
        "整形の切替は指示で制御し、用途ごとに出力の文法を変える。",
        "出力の文法は三層に分かれる。",
        "素の文字起こしは頁の全文を順序通りに起こし、整形出力は用途別の文法で構造を起こし、細粒度読みは框や座標で指した範囲だけを起こす。",
        "領域指定の読みは、框で指した範囲だけを起こすことで長文書の狙い読みを可能にし、token配分の実務に接続する。",
        "動的解像度は、細字の頁では細かく、粗い頁では粗く受ける配分であり、固定解像度の一律処理との違いである。",
        "複数切断の読みは頁を割りて細かく受け、複数頁の読みは頁を連ねて受ける。",
    ]:
        if old in t:
            bump("P05-GOT-beyond-card-removed")
            t = t.replace(old, "")
    anchor = "領域を指定して対話的に読むOCRと解像度を動かす読みと複数ページの読みを備えると、model論文の著者測定として報告している。"
    if anchor in t:
        t = t.replace(anchor, "領域を指定して対話的に読む機能と解像度を動かす読みと複数ページの読みを備えると、モデル論文の著者測定として報告している。圧縮率や出力文法の細部は記録の範囲を超えるため、本書では単一モデルで信号一般を解く理論と自前評価の範囲の二点で読む。領域指定の読みはバウンディングボックスで指した範囲だけを起こすことで長文書の狙い読みを可能にする。領域分割の読みは頁を区分して受け、複数頁の読みは頁を連ねて受ける。", 1)
        bump("P05-GOT-bounded-insert")
    b["text"] = t

    # ---------------- P15 ----------------
    p15 = pkgs["P15"]
    blk = {x["block_id"]: x for x in p15["blocks"]}

    # b4 MMMU: remove bilingual contamination (2 sentences)
    t = blk["p15-b4"]["text"]
    for old in [
        "英語と中国語の範囲の二言語であり、他の言葉への広がりはこの記録では語らない。",
        "英語と中国語の範囲での二言語として読み、他の言葉への広がりは語らない。",
    ]:
        if old in t:
            bump("P15-MMMU-bilingual-removed")
            t = t.replace(old, "")
    anchor = "試験や教科書の問いの教師が中心であり、専門の幅を集める資料の契約として読む。"
    if anchor in t:
        t = t.replace(anchor, anchor + "言語範囲の条件はこの記録では言語の広がりの主張に使わず、多肢選択の正誤の範囲での姿として読む。対の調べとの使い分けは別契約の仕事であり、幅の点数を確かさに格上げしない。", 1)
        bump("P15-b4-HallusionBench-synthesis")
    blk["p15-b4"]["text"] = t
    blk["p15-b4"]["discovery_ids"] = ["VM-D078", "VM-D080"]

    # b1 OCRBench: contamination-proof rewrite (targeted sentence replacements)
    t = blk["p15-b1"]["text"]
    t = sub_once(t, "公開と非公開の傾向が一致することが、漏えいへの備えの根拠になる。",
                 "公開と非公開の傾向の一致は、公開ベンチマークへの過適合や既知問題の影響を緩和・検出するための補助的な手がかりになる。", "P15-private-rewritten")
    t = sub_once(t, "公開だけでは覚えていたのか解いたのかが分からず、非公開の一致があって初めて測定の意味が立つ。",
                 "公開だけでは記憶していたのか解いたのかの切り分けが難しく、非公開の傾向の一致は測定の読みを助ける補助になる。", "P15-private-rewritten2")
    t = sub_once(t, "一致の有無が、測定の誠実さを分ける。",
                 "一致の有無は測定条件の開示と一緒に読む。", "P15-private-rewritten3")
    t = sub_once(t, "公開と非公開の傾向の一致が測定の意味を支え、一致なしに漏えいへの備えは語れない。",
                 "公開と非公開の傾向の一致は測定の読みを助けるが、汚染がないことの証明にはならない。", "P15-private-rewritten4")
    t = sub_once(t, "明かさないことが備えの条件である。",
                 "中身を明かさない設計は補助的な備えであり、証明ではない。", "P15-private-rewritten5")
    blk["p15-b1"]["text"] = t

    # b10 contamination section rewrite
    t = blk["p15-b10"]["text"]
    t = sub_once(t, "汚染への備えは公開と非公開の二段で固める。",
                 "汚染への備えは公開と非公開の二段の補助で緩和・検出を図る。", "P15-b10-rewritten")
    t = sub_once(t, "公開と非公開の傾向の一致で測定の意味を支える。",
                 "公開と非公開の傾向の一致で測定の読みを助ける。", "P15-b10-rewritten2")
    t = sub_once(t, "公開だけでは記憶していたのか解いたのかが分からず、非公開の一致があって初めて測定の意味が立つ。",
                 "公開だけでは記憶していたのか解いたのかの切り分けが難しく、非公開の傾向の一致は補助になる。", "P15-b10-rewritten3")
    t = sub_once(t, "二段の備えについて見ると、公開と非公開の傾向の一致が測定の意味を支え、中身を明かさないことが備えの条件になる。",
                 "公開と非公開の二段は過適合や既知問題の影響を緩和・検出するための補助的な手段であり、汚染がないことの証明にはならない。", "P15-b10-rewritten4")
    t = sub_once(t, "測ることは公開と非公開の傾向の一致であり、測っていないことは非公開の中身の詳細である。",
                 "測ることは公開と非公開の傾向の一致の範囲であり、測っていないことは汚染の有無の断定である。", "P15-b10-rewritten5")
    t = sub_once(t, "中身は設計上明かされず、明かさないことが備えの条件である。",
                 "中身は設計上明かされず、明かさない設計は補助的な備えに留まる。", "P15-b10-rewritten6")
    blk["p15-b10"]["text"] = t

    # b5 POPE voting fix
    t = blk["p15-b5"]["text"]
    if "投票型の測定で安定にしなやかに測り" in t:
        t = t.replace("投票型の測定で安定にしなやかに測り",
                      "反復的な二値質問によるobject probing（polling-based query）で安定に測り", 1)
        bump("P15-polling-full-phrase")
    t = t.replace("投票型の測定", "POPEの質問方式による測定").replace("投票型評価", "POPEの質問方式による評価").replace("投票型", "POPEの質問方式")
    t = sub_once(t, "投票で測れることと対で測れることは別の事柄であり、投票の結果を記述の忠実さに読み替えない。",
                 "POPEの質問方式で測れることと対で測れることは別の事柄であり、POPEの結果を記述の忠実さに読み替えない。", "P15-b5-vote-noun")
    blk["p15-b5"]["text"] = t
    blk["p15-b5"]["discovery_ids"] = ["VM-D079", "VM-D080"]

    # b6 MMBench polling fix (keep bilingual - correct home)
    t = blk["p15-b6"]["text"]
    t = t.replace("投票型評価", "POPEの質問方式による評価").replace("投票型", "POPEの質問方式")
    blk["p15-b6"]["text"] = t

    # b9 full rewrite: contract differences only, no VM-D112 mechanism
    blk["p15-b9"]["text"] = (
        "長さの幅と指示文脈の想起と実時間の応答は、それぞれ別の評価契約である。"
        "幅の契約は録りためた動画の長さと広さを測り、想起の契約は指示された長い文脈を取り出して考える過程を測り、"
        "実時間の契約は流れる映像への即応を測る。条件をまたいで結論を移さず、幅の値を想起の証拠にせず、想起の値を実時間の証拠にしない。"
        "蓄積された時系列への問い合わせは、オンラインの流れへの応答とは別の契約としてP11で扱われる。本節では三つの契約の区別に留め、"
        "具体的な取得方式や到達の値は動画理解の節に譲る。第三の契約を実時間の特殊例に読み替えない。"
    )
    blk["p15-b9"]["discovery_ids"] = ["VM-D086", "VM-D087", "VM-D088", "VM-D089"]
    bump("P15-b9-rewritten")

    # b2: add P05 specialist refs
    t = blk["p15-b2"]["text"]
    anchor = "特化と汎用の直接対決の不在を順位なしに残すことが、二契約への向き合い方になる。"
    if anchor in t:
        t = t.replace(anchor, anchor + "科学論文の変換に特化した記録と汎用の読みの記録の向き合い方の違いも順位なしに残し、特化の崩れ方の記録を汎用設計への反面教師として読む。", 1)
        bump("P15-b2-P05-synthesis")
    blk["p15-b2"]["text"] = t
    blk["p15-b2"]["discovery_ids"] = ["VM-D108", "VM-D027", "VM-D028"]

    # b3: chart side (keep VM-D109; no overlay add needed - P05 covered via b2; add nothing)
    # b7: add streaming refs
    t = blk["p15-b7"]["text"]
    anchor = "商用モデルの数値は著者らが測定したものとして読み、独立した第三者の再現とは分けて置く。"
    if anchor in t:
        t = t.replace(anchor, anchor + "流れる映像への即応の契約は別にあり、幅の値を実時間の証拠にしない。", 1)
        bump("P15-b7-streaming-synthesis")
    blk["p15-b7"]["text"] = t
    blk["p15-b7"]["discovery_ids"] = ["VM-D086", "VM-D088", "VM-D089"]

    # b8: referred-context (already VM-D087); add nothing (VM-D088/089 in b9)
    # b11: add P09 vendor poles
    t = blk["p15-b11"]["text"]
    anchor = "ベンダーの言い分として受け取ることが、出所の見分けの条件である。"
    if anchor in t:
        t = t.replace(anchor, anchor + "当初からのマルチモーダルの代表例同士でも、長いものを一度に見る力と効率軸の配置は別の評価軸であり、版と日付と条件に縛って読む。", 1)
        bump("P15-b11-P09-synthesis")
    blk["p15-b11"]["text"] = t
    blk["p15-b11"]["discovery_ids"] = ["VM-D072", "VM-D073", "VM-D065", "VM-D070", "VM-D071"]

    # b12: cost/context/memory/latency + P12 OSWorld formal refs
    t = blk["p15-b12"]["text"]
    anchor = "正確さと費用の両方を見て動作点を選ぶ。"
    if anchor in t:
        t = t.replace(anchor, "正確さと費用の両方を見て動作点を選ぶ。画面操作の契約では短い射程の成否と長い手順の状態維持が別の指標になり、"
                      "トークン数と費用と待ち時間の増え方は条件と一緒に読む。手順数からの倍率の推定はしない。", 1)
        bump("P15-b12-P12-X03-synthesis")
    blk["p15-b12"]["text"] = t
    blk["p15-b12"]["discovery_ids"] = ["VM-D072", "VM-D073", "VM-D090", "VM-D091", "VM-D092", "VM-D089", "VM-D100"]

    # b13: add OpenVLA limitation ref
    t = blk["p15-b13"]["text"]
    t = t + "独立した評価の希薄さは限りとして残し、到達の記録を構成の根拠にしない。"
    bump("P15-b13-gap")
    blk["p15-b13"]["text"] = t
    blk["p15-b13"]["discovery_ids"] = ["VM-D099", "VM-D100", "VM-D098", "VM-D096"]

    # b14: add I-JEPA/V-JEPA/Genie refs (4-pole)
    t = blk["p15-b14"]["text"]
    t = t + "歴史的定式と潜在力学と予測表現と生成的環境の四つの極の区別は、状態と目標と条件づけと画素と潜在と報酬と使い道の対応で読む。"
    bump("P15-b14-4pole")
    blk["p15-b14"]["text"] = t
    blk["p15-b14"]["discovery_ids"] = ["VM-D106", "VM-D107", "VM-D103", "VM-D104", "VM-D105"]

    # b15 editorial synthesis (NONE, no refs): rewrite X01-X04 threads without new facts
    blk["p15-b15"]["text"] = (
        "横断的に整理すると、教師信号の出所と入出力の約束の変化が全巻の筋になる。編集上の整理として述べれば、"
        "分類のラベルから対照や再構成や蒸留を経て指示への仕上げへという育て方の変化と、実演の軌道の集め方と機体をまたぐ整備という集め方の変化が並走し、"
        "どちらか一方の年表に畳まない。集める内容が変わるたびに測り方が定め直され、許容の指標の意味や選択の手続きや想起の条件や行動の書式や特徴の予測という定め直しが、能力の伸びと同じだけの内容だったという見方が要る。"
        "教師信号の出所（X01）と入出力の約束（X02）と系列・記憶・待ち時間の経済（X03）と主張の強さの見分け（X04）の四つの筋は、契約ごとの指標で読む。"
    )
    bump("P15-b15-rewritten")

    # b16 convergence: add X-thread anchors
    t = blk["p15-b16"]["text"]
    t = t + "教師信号の出所の変化（ラベル付き分類から対照・蒸留・指示仕上げへ）と入出力の約束の変化（言葉の指示から行動の書式へ）と資料の契約の変化（機体をまたぐ整備へ）は、どちらが勝つかの断定には届かず、未決の問いとして残す。開かれた語彙の検出の系譜の変化も、断定には届かず未決の問いとして残す."
    bump("P15-b16-Xthreads")
    blk["p15-b16"]["text"] = t
    blk["p15-b16"]["discovery_ids"] = ["VM-D072", "VM-D073", "VM-D099", "VM-D100",
                                      "VM-D003", "VM-D035", "VM-D051", "VM-D059", "VM-D062",
                                      "VM-D010", "VM-D047", "VM-D056",
                                      "VM-D096", "VM-D097", "VM-D104"]

    # deck: extend slightly to bind vendor pole? keep stable (deck refs must resolve; keep as-is)
    # P15 headline/deck text: terminology sweep later; fix 投票 in deck later

    # b10 near-dup order closings -> keep the fuller one
    t = blk["p15-b10"]["text"]
    if t.count("置き換えの順序を守る。") > 1:
        t = t.replace("置き換えの順序を守る。", "", 1)
        bump("P15-b10-dedup-order")
    blk["p15-b10"]["text"] = t

    # ---------------- Global terminology normalization (prose only) ----------------
    for p in data["packages"]:
        # headline/deck
        for field in ("headline", "deck"):
            t = p.get(field, "")
            orig = t
            t = t.replace("接地", "グラウンディング")
            t = t.replace("投票型", "POPEの質問方式")
            if t != orig:
                bump("term-headline-deck")
            p[field] = t
        for x in p["blocks"]:
            t = x["text"]
            # Order matters: specific fixes first already done; now generic
            # 接地 -> グラウンディング (P14 b4 diffusion already fixed; remaining are grounding sense)
            if "接地" in t:
                # avoid touching グラウンディング substrings (they don't contain 接地, safe)
                n = t.count("接地")
                t = t.replace("接地", "グラウンディング")
                bump("term-接地", n)
            # 投票型 -> POPEの質問方式 (remaining)
            if "投票型" in t:
                n = t.count("投票型")
                t = t.replace("投票型", "POPEの質問方式")
                bump("term-投票型", n)
            # 框 -> バウンディングボックス
            if "框" in t:
                n = t.count("框")
                t = t.replace("框", "バウンディングボックス")
                bump("term-框", n)
            # generic English tokens (ASCII-letter boundaries; CJK-safe).
            # Protect the DOM first-use English explanation from replacement.
            t = t.replace("Document Object Model", "＿＿DOMEXP＿＿")
            repls = [
                (r"(?<![A-Za-z])model(?![A-Za-z])", "モデル"), (r"(?<![A-Za-z])Model(?![A-Za-z])", "モデル"),
                (r"(?<![A-Za-z])token(?![A-Za-z])", "トークン"), (r"(?<![A-Za-z])encoder(?![A-Za-z])", "エンコーダ"),
                (r"(?<![A-Za-z])decoder(?![A-Za-z])", "デコーダ"),
                (r"(?<![A-Za-z])markup(?![A-Za-z])", "マークアップ"), (r"(?<![A-Za-z])suite(?![A-Za-z])", "スイート"),
                (r"(?<![A-Za-z])pair(?![A-Za-z])", "ペア"),
                (r"(?<![A-Za-z])dataset(?![A-Za-z])", "データセット"), (r"(?<![A-Za-z])benchmark(?![A-Za-z])", "ベンチマーク"),
                (r"(?<![A-Za-z])mask(?![A-Za-z])", "マスク"), (r"(?<![A-Za-z])frame(?![A-Za-z])", "フレーム"),
                (r"(?<![A-Za-z])interface(?![A-Za-z])", "インターフェース"),
                (r"(?<![A-Za-z])grounding(?![A-Za-z])", "グラウンディング"),
                (r"(?<![A-Za-z])code(?![A-Za-z])", "コード"),
                (r"(?<![A-Za-z])data(?![A-Za-z])", "データ"),
                (r"(?<![A-Za-z])leaderboard(?![A-Za-z])", "リーダーボード"),
            ]
            for pat, rep in repls:
                t2, n = re.subn(pat, rep, t)
                if n:
                    bump(f"term-{pat}", n)
                    t = t2
            t = t.replace("＿＿DOMEXP＿＿", "Document Object Model")
            # bounding box phrase
            if "bounding box" in t.lower() and "バウンディングボックス" not in t:
                t = re.sub(r"[Bb]ounding [Bb]ox", "バウンディングボックス", t)
                bump("term-bounding-box")
            # DOM first-use explanation
            if "DOM" in t and "Document Object Model" not in t and p["package_id"] == "P12":
                pass  # P12 b5 already has explanation; leave
            # 復号器 -> デコーダ (remaining, esp. P14)
            if "復号器" in t:
                n = t.count("復号器")
                t = t.replace("復号器", "デコーダ")
                bump("term-復号器", n)
            # 符号化器 -> エンコーダ (P14 has 符号化器; standardize? keep? terminology says encoder->エンコーダ.
            # 符号化器 is a legitimate Japanese term for encoder; but map prefers エンコーダ. Replace.)
            if "符号化器" in t:
                n = t.count("符号化器")
                t = t.replace("符号化器", "エンコーダ")
                bump("term-符号化器", n)
            # 檔案系統 / 文書物体模型 (legacy; likely 0 but sweep)
            if "檔案系統" in t:
                t = t.replace("檔案系統", "ファイルシステム")
                bump("term-檔案系統")
            if "文書物体模型" in t:
                t = t.replace("文書物体模型", "DOM（Document Object Model）")
                bump("term-文書物体模型")
            # 後の段階 pledge -> bounded scope statement
            if "3.5系の後継確認は後の段階に譲る。" in t:
                t = t.replace("3.5系の後継確認は後の段階に譲る。",
                              "3.5系の後継確認は記録の範囲を超えるため本書では扱わない。")
                bump("pledge-後の段階-removed")
            if "伍する開かれた符号化の不在" in t:
                n = t.count("伍する開かれた符号化の不在")
                t = t.replace("伍する開かれた符号化の不在", "匹敵する開かれた符号化の不在")
                bump("term-伍する", n)
            if "通貨の確認" in t:
                t = t.replace("通貨の確認が必要", "鮮度の確認が必要")
                bump("term-通貨の確認")
            x["text"] = t

    # ---------------- Semantic padding reduction ----------------
    for p in data["packages"]:
        for x in p["blocks"]:
            sents = split_sentences(x["text"])
            # 1. drop recap boilerplate sentences
            sents = drop_containing(sents, ["について見ると"], "pad-について見ると")
            # 2. exact-duplicate sentences within block (keep first)
            seen: set[str] = set()
            out = []
            for s in sents:
                k = s.strip()
                if k in seen and len(k) > 8:
                    bump("pad-exact-dup-in-block")
                    continue
                seen.add(k)
                out.append(s)
            sents = out
            # 3. generic closing paddings (keep block >= 3 sentences)
            closings = ["一面だけの結論は出さない", "順序を変えない", "順序を守ることで",
                        "範囲を守る", "見積もらない範囲を守る"]
            filtered = []
            for s in sents:
                if len(sents) - (len(sents) - len(filtered)) <= 0:
                    filtered.append(s)
                    continue
                if any(c in s for c in closings) and len(s) < 60 and len(sents) > 3:
                    # keep 測ることは contract sentences even if they contain 範囲
                    if s.strip().startswith("測ることは") or s.strip().startswith("測っていないことは"):
                        filtered.append(s)
                        continue
                    bump("pad-closing")
                    # remove only the closing clause if sentence is longer? No: drop whole short sentence
                    continue
                filtered.append(s)
            # Recompute properly: simpler second pass
            x["text"] = join_sentences(filtered)

    # Ensure no empty blocks
    for p in data["packages"]:
        for x in p["blocks"]:
            assert x["text"].strip(), f"empty block {p['package_id']} {x['block_id']}"
            assert x["text"].count("VM-D") == 0, "internal ID leak check (VM-D in prose unexpected)"

    # ---------------- Synthesis fresh regeneration ----------------
    data["synthesis"] = {
        "profile_payload": {
            "branch_transition_synthesis": (
                "表現の学習と転移を起点に、検出の枠組み、密な構造化と指示応答、文書の構造理解、"
                "系列としての視覚と自己教師あり学習、画像全体の対応づけから開かれたグラウンディングへ、"
                "個別に事前学習した構成要素の接続、解像度と融合と時刻の統合、幻覚と根拠利用の診断、"
                "オフラインの幅と想起と実時間の応答の分離、画面操作のグラウンディングと状態維持、"
                "身体をもつ行動のインターフェース、歴史的定式と潜在力学と予測表現と生成的環境の四つの極へと系譜が分かれ、"
                "評価の契約ごとの方法の整理へ集まる。起点では分類のラベルから対照やマスク再構成や蒸留や指示仕上げへと見る力の育て方が積み重なり、"
                "身体の側では実演の軌道と機体をまたぐ整備へと集める内容が並走し、どちらか一方の年表に畳まない。"
                "文書の構造読みではANLSの許容と抜き出しの弱さの開示が契約になり、図表では緩めた正確さの許容が数値の意味を決める。"
                "系列の視覚では軽さと転移の広さが到達になり、開かれたグラウンディングでは見つける力と指す力の層の違いを分ける。"
                "言語モデル側の計画と行動方策側の実行の分業から一体の文へのまとめと行動の言語化と開かれた確かめへ進み、"
                "四つの極では状態と目標と条件づけの対応を記録ごとに分ける。閉じた製品の記録は能力と運用の範囲に留め、構成の根拠にはしない。"
                "一本化か分業かは未決の問いとして残す。"
            ),
            "parallel_competing_relations": (
                "一体の事前学習と部品の併用、特化型と汎用型、密な注釈とウェブ規模の弱い教師信号、早期と後段と密な融合、"
                "凍結の再利用と共同学習、オフラインの幅と想起と実時間の応答、言語モデル側の計画と一体の行動表現、"
                "潜在力学と予測表現と生成的環境、ベンダー測定と独立測定が並行する競合関係にある。"
                "いずれも万能ではなく、条件と装置と費用と対象で損得が変わる。"
                "文書の構造読みと図表の見た目と筋道読みでは向き合い方の違いを順位なしに残し、"
                "幅の点数とPOPEの質問方式の傾向と回転の一致では指標の違いを分ける。"
                "ベンダーの測定と著者らの測定と独立再現の三段階を分け、開示と測定の区別を置く。"
                "どちらが勝つかの断定には全巻の結果は届かず、未決の問いとして残す。"
            ),
            "unresolved_lineage_questions": (
                "身体の行動については独立機関による横断評価が限られ、制御に使える生成世界の共有測定がなく、"
                "特化型と汎用型の同一条件での直接対決がなく、実運用の遅延と記憶量の根拠が不足し、"
                "最新ベンダー報告の独立再現が残された課題である。概要水準の記録は概要の範囲に留め、語りで格上げしない。"
                "問いに応じて調べる動画方式の上限は動画理解の節の範囲で読み、到達の証拠にはしない。"
                "版と日付の範囲で読む。"
            ),
            "historical_attribution_boundaries": (
                "概要や断片水準の記録は概要の範囲に留め、語りで格上げしない。閉じた製品は能力と運用のみで扱い、構成を推測しない。"
                "条件の異なる数値の横断順位づけはしない。ベンダーの主張は帰属づきで引用し、独立再現を待つ。"
                "歴史的定式から生成環境への直接継承は主張しない。似ていることと受け継いだことの区別を置く。"
                "測ったことだけを語り、測っていないことは語らない。版と日付と所在の範囲で読む。"
                "公開と非公開の傾向の一致は過適合や既知問題の影響を緩和・検出するための補助的な手段であり、汚染がないことの証明にはならない。"
                "助けの切り分けと混入の宣言と借りの表示を数値と一緒に示す。未決を未決として残す。"
            ),
        },
        "publication_payload": {},
    }
    bump("synthesis-regenerated")

    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "compact-input-revised.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTDIR / "revision-counts.json").write_text(
        json.dumps(counts, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
