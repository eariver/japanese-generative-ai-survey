#!/usr/bin/env python3
"""Apply Draft r8 bidirectional terminology repairs to r8 spec copies.

Wording-only, concept-level repairs per map §3.8 + Sol r7 F1-F5.
Fails loudly on any mismatch.
"""
import json

D = "/home/eariver/git/japanese-generative-ai-survey/sources/SP-vision-multimodal-2026/execution/draft-r8-20261002/specs"

FIXES = [
# F1: P13 non-box ボックス -> architecture relations
("P13", "p13-b3",
 "見ることと考えることを別のボックスに閉じ込めず、一つの文の続きとして扱い",
 "視覚と推論を別系統に分離せず、一つの文の続きとして扱い"),
("P13", "p13-b5",
 "見ることと動かすことの間に別のボックスを置かず、一つのモデルで受けて出す",
 "視覚入力から行動出力までを一つのモデルで扱い、中間モジュールの分離を設けない"),
# F2: P13 lineage 鎖
("P13", "p13-b7",
 "鎖を通して見ると、表現と行動の界面が段階を追って変わった",
 "この系譜を通して見ると、表現と行動の界面が段階を追って変わった"),
# F3: non-P14 極
("P03", "p03-b2",
 "ボックスに依存した作りでありボックスなしの密な極はFCNやSAM側の資料に譲る",
 "ボックスに依存した作りでありボックスに依存しない密な予測はFCNやSAM側の資料に譲る"),
("P05", "p05-b5",
 "GOTはOCR-2.0という理論を掲げる特化型のもう一極である",
 "GOTはOCR-2.0という理論を掲げる別系統の特化型モデルである"),
("P07B", "p07b-b6",
 "融合の両極は、後段の最小構成と密な統一である",
 "融合方式は、後段融合の最小構成と密な融合に分かれる"),
("P07B", "p07b-b6",
 "足さない渡しと三段の混ぜの対置である",
 "追加構成なしの転移と三段階の融合の対比である"),
("P13", "p13-b6",
 "OpenVLAはオープンウェイトで確かめられる極だ",
 "OpenVLAはオープンウェイトで検証可能なVLAの事例である"),
("P15", "p15-b7",
 "Gemini 3.1 Proは100万のコンテキストをもつ当初からのマルチモーダルの極で",
 "Gemini 3.1 Proは100万のコンテキストをもつ当初からのマルチモーダルの代表例で、"),
]


def main() -> int:
    applied = 0
    for pid, bid, old, new in FIXES:
        p = f"{D}/{pid}.json"
        s = json.load(open(p))
        hits = [b for b in s["blocks"] if b["block_id"] == bid]
        assert len(hits) == 1, (pid, bid)
        assert old in hits[0]["text"], (pid, bid, old[:60])
        assert hits[0]["text"].count(old) == 1, (pid, bid, "multi")
        hits[0]["text"] = hits[0]["text"].replace(old, new)
        json.dump(s, open(p, "w"), ensure_ascii=False, indent=1)
        open(p, "a").write("\n")
        applied += 1
    print(f"applied {applied}/{len(FIXES)} repairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
