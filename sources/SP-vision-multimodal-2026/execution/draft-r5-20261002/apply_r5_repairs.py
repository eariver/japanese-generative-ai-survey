#!/usr/bin/env python3
"""Apply Draft r5 final reader-surface cleanup repairs to r5 spec copies.

Wording-only, concept-level repairs per map §3.5 + Sol r4 F1-F5.
Fails loudly on any mismatch.
"""
import json

D = "/home/eariver/git/japanese-generative-ai-survey/sources/SP-vision-multimodal-2026/execution/draft-r5-20261002/specs"

FIXES = [
# 5.1 P06 headline
("P06", "headline", "Transformerと自己教師の土台", "Transformerと自己教師あり学習の基盤"),
# 5.2 P06 mechanism wording
("P06", "p06-b4", "視覚エンコーダを凍らせ、言葉側だけを締める調整である",
 "視覚エンコーダを凍結し、テキスト側のみを調整するものである"),
("P06", "p06-b4", "仕組みの要点は、正規化の大域性を捨てて一対の判定に還す点にある",
 "仕組みの要点は、正規化の大域性を捨て、各画像・テキスト対を独立に判定するシグモイド損失に置き換える点にある"),
# 5.3 P06 source/citation boundary wording (prose)
("P06", "p06-b4", "ただし正確な引用の結びは残る", "ただし正確な引用対応は未確定のまま残る"),
("P06", "p06-b5", "正確な典拠の結びのなさも同時に記す", "正確な典拠との対応のなさも同時に記す"),
("P06", "p06-b5", "正確な典拠の結びのなさであり、次の節の結びの話に渡す",
 "正確な典拠との対応のなさであり、次の節では接地の話を扱う"),
("P06", "p06-b5", "分けた整理が、結びの節の入口になる", "分けた整理が、次の節の入口になる"),
# 5.4 P07A contrastive-learning wording
("P07A", "deck", "語の並びや帰属の読みが落ちる画像全体のアライメントの限界を次の節へ渡す",
 "語の並びや帰属の読みが落ちる画像全体のアライメントの限界を次の節で扱う"),
("P07A", "p07a-b1", "文と絵の組を大量に当て、言葉を概念への言及の界面に育てる",
 "文と絵の大量の組を対照学習し、言葉を概念への言及の界面に育てる"),
("P07A", "p07a-b1", "決まった範疇の表引きから、言葉の開いた呼び出しへの転換である",
 "決まった範疇の固定クラス分類から、言葉の開いた呼び出しへの転換である"),
("P07A", "p07a-b3", "4億ペアの当てが、30超の束への転送を生んだ",
 "4億ペアの対照学習が、30以上のデータセットへの転送を生んだ"),
("P07A", "p07a-b3", "アライメントの到達の上に接地の仕組みを積むことが、次の節への渡しである",
 "アライメントの到達を起点に接地の仕組みを扱うのが次の節である"),
# 5.5 other residual shorthand
("P07B", "p07b-b1", "ODinWを野外の補いとして添える",
 "ODinWを実世界・多様ドメインの補完的評価として添える"),
("P09", "p09-b4", "ここでは受け止めて列に変える契約だけを扱う",
 "ここでは受け止めてトークン列へ変換する契約だけを扱う"),
("P11", "p11-b2", "流れる映像への即応とは別の列に置く",
 "流れる映像への即応とは別の評価軸として扱う"),
("P06", "p06-b1", "階層を要する検出や密な予測にTransformerを渡す役割であり、本節では短く置く",
 "階層を要する検出や密な予測へTransformerの適用範囲を広げる役割であり、本節では短く置く"),
]


def main() -> int:
    applied = 0
    for pid, bid, old, new in FIXES:
        p = f"{D}/{pid}.json"
        s = json.load(open(p))
        if bid in ("deck", "headline"):
            assert old in s[bid], (pid, bid, old[:50])
            assert s[bid].count(old) == 1, (pid, bid, "multi")
            s[bid] = s[bid].replace(old, new)
        else:
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
