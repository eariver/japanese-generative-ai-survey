#!/usr/bin/env python3
"""Apply Language QA prose-only fixes to TS-003 Draft r1 spec files.

All fixes are wording-only: no meaning/evidence/binding/coverage changes.
After this, draft/v2 outputs must be deleted and the runner re-executed.
"""
import json
import re

D = "/home/eariver/git/japanese-generative-ai-survey/sources/SP-vision-multimodal-2026/execution/draft-r1-20261001/specs"

# 0. Repair モデル pile-ups from an earlier overlapping-replace bug, then verify none remain.
for pid in ["P01","P02","P03","P04","P05","P06","P07A","P07B","P08","P09","P10","P11","P12","P13","P14","P15"]:
    p = f"{D}/{pid}.json"
    s = json.load(open(p))
    changed = False
    for key in ("headline", "deck"):
        new = s[key]
        while "モデルモデル" in new:
            new = new.replace("モデルモデル", "モデル")
        if new != s[key]:
            s[key] = new
            changed = True
    for b in s["blocks"]:
        new = b["text"]
        while "モデルモデル" in new:
            new = new.replace("モデルモデル", "モデル")
        if new != b["text"]:
            b["text"] = new
            changed = True
    if changed:
        print(pid, "pile-up repaired")
        json.dump(s, open(p, "w"), ensure_ascii=False, indent=1)
        open(p, "a").write("\n")

def load(pid):
    p = f"{D}/{pid}.json"
    s = json.load(open(p))
    return p, s

def save(p, s):
    json.dump(s, open(p, "w"), ensure_ascii=False, indent=1)
    open(p, "a").write("\n")

def sub_all(s, old, new):
    """Replace in headline/deck/all block texts. Returns count."""
    n = 0
    for key in ("headline", "deck"):
        if old in s[key]:
            n += s[key].count(old)
            s[key] = s[key].replace(old, new)
    for b in s["blocks"]:
        if old in b["text"]:
            n += b["text"].count(old)
            b["text"] = b["text"].replace(old, new)
    return n

def sub_block(s, block_id, old, new):
    for b in s["blocks"]:
        if b["block_id"] == block_id:
            if new in b["text"]:
                return "already"
            if old in b["text"]:
                b["text"] = b["text"].replace(old, new)
                return "fixed"
            raise AssertionError((block_id, old))
    raise AssertionError(block_id)

total = {}
# 1. Global: 模型 -> モデル (all reader prose; model sense everywhere)
for pid in ["P01","P02","P03","P04","P05","P06","P07A","P07B","P08","P09","P10","P11","P12","P13","P14","P15"]:
    p, s = load(pid)
    n = sub_all(s, "模型", "モデル")
    total[pid] = n
    save(p, s)
print("模型->モデル:", total)

# 2. Global: supervision -> 教師信号 (map disposition), except code-ish contexts (none present)
for pid in ["P07A", "P07B"]:
    p, s = load(pid)
    n = sub_all(s, "supervision", "教師信号")
    print(pid, "supervision->教師信号:", n)
    save(p, s)

# P07B-b4 specific: 語彙の教師信号の群 reads awkward after global replace; fix phrasing
p, s = load("P07B")
sub_block(s, "p07b-b4", "語彙 教師信号 の群は、", "語彙への教師信号の群は、")
sub_block(s, "p07b-b4", "同じ領域へ 教師信号 する点が", "同じ領域へ教師信号を与える点が")
sub_block(s, "p07b-b4", "Deticは、語彙の 教師信号 を画像水準ラベルで賄う", "Deticは、語彙への教師信号を画像水準ラベルで賄う")
sub_block(s, "p07b-b1", "という 教師信号 の知見も置く", "という教師信号の知見も置く")
sub_block(s, "p07b-b7", "語彙 教師信号 や融合設計とは別の群", "語彙への教師信号や融合設計とは別の群")
sub_block(s, "p07b-b8", "キャプション規模の 教師信号 を可能にし", "キャプション規模の教師信号を可能にし")
save(p, s)

# 3. P04 lane-code leaks -> section names
p, s = load("P04")
sub_block(s, "p04-b3", "後のD10やD12、D13の節に流れ込む", "後の推論や画面操作、行動の節に流れ込む")
sub_block(s, "p04-b3", "D10やD12、D13の節では、この契約が前提として働く", "推論や画面操作、行動の節では、この契約が前提として働く")
sub_block(s, "p04-b4", "D09やD13の節への橋になる", "統合や行動の節への橋になる")
save(p, s)
print("P04 D-codes fixed")

# 4. P06 百B級 -> 100B級
p, s = load("P06")
n = sub_all(s, "百B級", "100B級")
save(p, s)
print("P06:", n)

# 5. P07B micro-fixes
p, s = load("P07B")
sub_block(s, "p07b-b1", "開世界検出の話題は脚注に留める", "開世界検出の話題は脇に置く")
sub_block(s, "p07b-b2", "V2L投影と接地", "V2L投影（視覚から言語への投影）と接地")
sub_block(s, "p07b-b7", "ウェブ規模の自己学習で rare を押し上げた", "ウェブ規模の自己学習でレアを押し上げた")
sub_block(s, "p07b-b7", "LVIS-rare 31.2から44.6%へ上げ", "LVIS-rare 31.2%から44.6%へ上げ")
sub_block(s, "p07b-b7", "人手の箱注釈なしに rare 範疇で", "人手の箱注釈なしにレア範疇で")
sub_block(s, "p07b-b9", "自己学習がウェブの量で rare の裾を埋める", "自己学習がウェブの量でレアの裾を埋める")
sub_block(s, "p07b-b7", "ウェブの量で rare の裾を埋める", "ウェブの量でレアの裾を埋める")
sub_block(s, "p07b-b9", "人手の箱なしに機械ラベル空間と弱い選別で rare を押し上げた", "人手の箱なしに機械ラベル空間と弱い選別でレアを押し上げた")
sub_block(s, "p07b-b7", "LVIS-rare 31.2から44.6%へ上げ", "LVIS-rare 31.2%から44.6%へ上げ")
save(p, s)
print("P07B micro fixed")

# 6. P03 本カード -> 本節
p, s = load("P03")
sub_block(s, "p03-b3", "本カードでは二重の読みを運び", "本節では二重の読みを運び")
save(p, s)

# 7. P11 workflow leaks
p, s = load("P11")
sub_block(s, "p11-b2", "版の結びつけはEvidenceのv3に置き", "版の結びつけはv3の記録に置き")
sub_block(s, "p11-b5", "受け入れ時のIDの結びつけは、動かさない所在である", "記録の範囲でのIDの結びつけは、動かさない所在である")
sub_block(s, "p11-b5", "正準の範囲の外に置く", "記録の範囲の外に置く")
save(p, s)
print("P11 leaks fixed")

# 8. P13 カード -> モデルカード
p, s = load("P13")
sub_block(s, "p13-b5", "運用の話はカードの範囲でだけ語る", "運用の話はモデルカードの記載範囲でだけ語る")
sub_block(s, "p13-b6", "カードが示す限りでは", "モデルカードが示す限りでは")
sub_block(s, "p13-b6", "カードは更新されうるため", "モデルカードは更新されうるため")
save(p, s)
print("P13 cards fixed")

# 9. P14 fixes
p, s = load("P14")
sub_block(s, "p14-b1", "この版の修復の射程の外に置く", "本節の射程の外に置く")
sub_block(s, "p14-b4", "2026年8月24日時点の対応版で読む", "2026年8月24日時点の版で読む")
save(p, s)
print("P14 fixed")

# 10. P15 fixes
p, s = load("P15")
sub_block(s, "p15-b4", "版は証拠時点のv3で縛り", "版はv3の記録で縛り")
sub_block(s, "p15-b4", "Gemini 1.5 Proが商業の最良で平均75%", "Gemini 1.5 Proが商用モデルの最良で平均75%")
sub_block(s, "p15-b6", "カードが示す限りでは", "モデルカードが示す限りでは")
sub_block(s, "p15-b6", "カードは更新されうるため", "モデルカードは更新されうるため")
sub_block(s, "p15-b6", "いつのカードかを外して能力を語ることはできない", "いつのモデルカードかを外して能力を語ることはできない")
sub_block(s, "p15-b7", "生まれながらのマルチモーダルの極で", "当初からのマルチモーダルの極で")
sub_block(s, "p15-b7", "2026年2月のカードで読む", "2026年2月のモデルカードで読む")
sub_block(s, "p15-b7", "カードの中身は変わりうる", "モデルカードの中身は変わりうる")
sub_block(s, "p15-b7", "生来のマルチモーダルモデルで", "当初からのマルチモーダルモデルで")
sub_block(s, "p15-b7", "2026年7月のカードで読む", "2026年7月のモデルカードで読む")
# duplicate sentence removal (exact repeat within b1)
for b in s["blocks"]:
    if b["block_id"] == "p15-b1":
        dup = "設計があることが、測定の信頼になる。"
        if b["text"].count(dup) == 2:
            b["text"] = b["text"].replace("結びがあることが、巻の区切りだ。" + dup, "結びがあることが、巻の区切りだ。", 1)
save(p, s)
print("P15 fixed")
print("ALL REPAIRS APPLIED")
