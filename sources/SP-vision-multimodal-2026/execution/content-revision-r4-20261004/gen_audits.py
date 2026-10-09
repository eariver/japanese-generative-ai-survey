#!/usr/bin/env python3
"""Generate audit evidence files for content-revision-r4 (read-only inputs)."""
from __future__ import annotations
import json
import re
from pathlib import Path
from collections import Counter

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
INDIR = SRC / "execution/bounded-revision-112-20261004"
OUTDIR = SRC / "execution/content-revision-r4-20261004"


def load_compact(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def pkg_stats(data) -> dict:
    out = {}
    for p in data["packages"]:
        chars = sum(len(b["text"]) for b in p["blocks"]) + len(p.get("deck", "")) + len(p.get("headline", ""))
        sents = []
        for b in p["blocks"]:
            sents += [s for s in re.split(r"(?<=[。！？])", b["text"]) if s.strip()]
        exact_dup = len(sents) - len({s.strip() for s in sents})
        out[p["package_id"]] = {"blocks": len(p["blocks"]), "chars": chars,
                                "sentences": len(sents), "exact_dup_in_block_sum": exact_dup}
    return out


def count_pat(data, pat: str, regex: bool = False):
    n = 0
    locs = []
    for p in data["packages"]:
        for x in p["blocks"] + [{"text": p.get("deck", ""), "block_id": "@deck"},
                                {"text": p.get("headline", ""), "block_id": "@headline"}]:
            c = len(re.findall(pat, x["text"])) if regex else x["text"].count(pat)
            if c:
                n += c
                locs.append(f"{p['package_id']}/{x['block_id']}:{c}")
    # synthesis
    for k, v in data["synthesis"]["profile_payload"].items():
        c = len(re.findall(pat, v)) if regex else v.count(pat)
        if c:
            n += c
            locs.append(f"SYN/{k}:{c}")
    return n, locs


def main() -> int:
    before = load_compact(INDIR / "compact-input.json")
    after = load_compact(OUTDIR / "compact-input-revised.json")
    bs, ast = pkg_stats(before), pkg_stats(after)
    rows = []
    for pid in bs:
        rows.append({"package_id": pid, "before_chars": bs[pid]["chars"], "after_chars": ast[pid]["chars"],
                     "delta": ast[pid]["chars"] - bs[pid]["chars"],
                     "before_sentences": bs[pid]["sentences"], "after_sentences": ast[pid]["sentences"]})
    total_b = sum(r["before_chars"] for r in rows)
    total_a = sum(r["after_chars"] for r in rows)
    (OUTDIR / "before-after-stats.json").write_text(json.dumps(
        {"before_total_chars": total_b, "after_total_chars": total_a, "delta": total_a - total_b,
         "packages": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    terms = ["接地", "投票型", "框", "檔案系統", "文書物体模型", "言う側", "できる側", "言える側",
             "通貨の確認", "意味を言い当てる", "生徒側を尖らせ", "英語と中国語", "情報を落とさず",
             "について見ると", "定石", "伍する", "後の段階", "復号器", "符号化器"]
    en_pats = [r"(?<![A-Za-z])model(?![A-Za-z])", r"(?<![A-Za-z])token(?![A-Za-z])",
               r"(?<![A-Za-z])encoder(?![A-Za-z])", r"(?<![A-Za-z])decoder(?![A-Za-z])",
               r"(?<![A-Za-z])markup(?![A-Za-z])", r"(?<![A-Za-z])suite(?![A-Za-z])",
               r"(?<![A-Za-z])pair(?![A-Za-z])", r"(?<![A-Za-z])dataset(?![A-Za-z])",
               r"(?<![A-Za-z])benchmark(?![A-Za-z])", r"(?<![A-Za-z])mask(?![A-Za-z])",
               r"(?<![A-Za-z])frame(?![A-Za-z])", r"(?<![A-Za-z])interface(?![A-Za-z])",
               r"(?<![A-Za-z])grounding(?![A-Za-z])", r"(?<![A-Za-z])Model(?![A-Za-z])"]
    term_rows = []
    for t in terms:
        nb, lb = count_pat(before, t)
        na, la = count_pat(after, t)
        term_rows.append({"pattern": t, "before": nb, "after": na,
                          "before_locs": lb[:12], "after_locs": la[:12]})
    for t in en_pats:
        nb, lb = count_pat(before, t, True)
        na, la = count_pat(after, t, True)
        term_rows.append({"pattern": t, "before": nb, "after": na,
                          "before_locs": lb[:12], "after_locs": la[:12]})
    (OUTDIR / "terminology-audit.json").write_text(json.dumps(term_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    pads = ["について見ると", "別の欄に置く", "欄をまたいだ", "一面だけの結論は出さない",
            "一面だけを取り出して", "測ることは", "測っていないことは", "順序を変えない", "順序を守る", "範囲を守る"]
    pad_rows = []
    for t in pads:
        nb, lb = count_pat(before, t)
        na, la = count_pat(after, t)
        pad_rows.append({"pattern": t, "before": nb, "after": na,
                         "before_locs": lb[:16], "after_locs": la[:16]})
    (OUTDIR / "semantic-repetition-audit.json").write_text(json.dumps(pad_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # contamination wording scan (P15 + all)
    contam_pats = ["漏えいへの備えの根拠", "初めて測定の意味が立つ", "二段で固める", "証明",
                   "汚染がない", "一致があって初めて", "一致なしに漏えい"]
    crows = []
    for t in contam_pats:
        nb, lb = count_pat(before, t)
        na, la = count_pat(after, t)
        crows.append({"pattern": t, "before": nb, "after": na,
                      "before_locs": lb[:12], "after_locs": la[:12]})
    (OUTDIR / "contamination-wording-audit.json").write_text(json.dumps(crows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"chars": [total_b, total_a], "term_patterns": len(term_rows)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
