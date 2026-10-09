#!/usr/bin/env python3
"""Apply Draft r6 P09 terminology closure repairs to r6 spec copy.

Wording-only, concept-level repairs per map §3.6 + Sol r5 F1-F4.
Fails loudly on any mismatch.
"""
import json

D = "/home/eariver/git/japanese-generative-ai-survey/sources/SP-vision-multimodal-2026/execution/draft-r6-20261002/specs"

FIXES = [
# F1: bare self-supervised -> approved forms
("P09", "p09-b4", "BEATsは音全般の自己教師の入口を担う",
 "BEATsは音全般の自己教師あり学習の入口を担う"),
("P09", "p09-b4", "音響トークナイザと音の自己教師を交互に鍛え",
 "音響トークナイザと音の自己教師あり学習を交互に鍛え"),
# F2: model family
("P09", "p09-b2", "1Bから78Bの家族を用意し", "1Bから78Bのモデル群を用意し"),
# F3: modality/input roles
("P09", "p09-b4", "Whisperは話し言葉の入口の前例である",
 "Whisperは話し言葉の音声入力処理の前例である"),
("P09", "p09-b4", "BEATsは音全般の自己教師あり学習の入口を担う",
 "BEATsは音全般の自己教師あり学習による音響表現学習を担う"),
("P09", "p09-b5", "音の入口を組み合わせて時刻で合わせるのがQwen3-Omniである",
 "音声入力を組み合わせて時刻で合わせるのがQwen3-Omniである"),
# F4: deployment + architecture
("P09", "p09-b2", "稠密と混合専門家で末端からクラウドまで",
 "稠密と混合専門家でエッジデバイスからクラウドまで"),
("P09", "p09-b2", "三つの部品の積み重ねはコードの上で確かめられるが",
 "三つの構成要素の積み重ねはコードの上で確かめられるが"),
]


def main() -> int:
    applied = 0
    for pid, bid, old, new in FIXES:
        p = f"{D}/{pid}.json"
        s = json.load(open(p))
        hits = [b for b in s["blocks"] if b["block_id"] == bid]
        assert len(hits) == 1, (pid, bid)
        assert old in hits[0]["text"], (pid, bid, old[:50])
        assert hits[0]["text"].count(old) == 1, (pid, bid, "multi")
        hits[0]["text"] = hits[0]["text"].replace(old, new)
        json.dump(s, open(p, "w"), ensure_ascii=False, indent=1)
        open(p, "a").write("\n")
        applied += 1
    print(f"applied {applied}/{len(FIXES)} repairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
