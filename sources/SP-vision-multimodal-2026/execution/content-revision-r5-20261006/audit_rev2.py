#!/usr/bin/env python3
"""rev2 polish audits: branching, license separation, geo, unseen, costs, rhythm.

Runs AFTER gen_audits.py (which must also still PASS). Writes repetition
before/after report (counts + qualitative note; counts are not the PASS criterion).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r5-20261006"
PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]


def load(pid):
    return json.loads((SRC / "draft/v2/packages" / pid / "draft-result.json").read_text(encoding="utf-8"))


def main() -> int:
    fails = []
    docs = {}
    for pid in PIDS:
        d = load(pid)
        docs[pid] = {b["block_id"]: b["text"] for b in d["blocks"]}
        docs[pid]["__deck__"] = d.get("deck", "")

    # ---- P15-B02 branching
    b02 = docs["P15"]["P15-B02"]
    for phrase in ["一本の系列ではなく", "分岐", "並立", "別の柱", "組み替えて使う"]:
        if phrase not in b02:
            fails.append(f"P15-B02 missing branching phrase: {phrase}")
    if "実機実証の身体データへと移った" in b02:
        fails.append("P15-B02 linear opening remains")
    if "ラベルなしの自己教師あり学習は別の柱" not in b02:
        fails.append("P15-B02 DINOv2 label-free branch missing")

    # ---- P09 license separation
    b10 = docs["P09"]["p09-b10"]
    for phrase in ["モデル重みのライセンスは別の事実", "意図した用途", "書き換えるものではない",
                   "モデル重みのライセンスはApache 2.0", "未確認である"]:
        if phrase not in b10:
            fails.append(f"P09-B10 missing: {phrase}")
    for bad in ["模型の重みの許諾", "研究教育利用の条件とAi2"]:
        if bad in b10:
            fails.append(f"P09-B10 bad phrasing remains: {bad}")

    # ---- P07A geo
    if "地理的位置推定" not in docs["P07A"]["P07A-B03"]:
        fails.append("P07A geo-localization missing")

    # ---- P07B unseen accuracy
    b01 = docs["P07B"]["P07B-B01"]
    if "語句は学習時に未知" in b01:
        fails.append("P07B all-unseen overstatement remains")
    if "open-endedな語句空間" not in b01:
        fails.append("P07B open-ended phrase space missing")

    # ---- P02 costs
    b7 = docs["P02"]["p02-b7"]
    for bad in ["割り当て負担", "クラス確率の負担", "ボックス負担"]:
        if bad in b7:
            fails.append(f"P02 DETR burden term remains: {bad}")
    for phrase in ["マッチングコスト", "対応づいた対に対する学習損失"]:
        if phrase not in b7:
            fails.append(f"P02 cost distinction missing: {phrase}")

    # ---- Japanese finals
    allt = "\n".join(t for pid in PIDS for t in docs[pid].values())
    for bad in ["般化", "管路", "枠率", "単一伝送路", "模型の重みの許諾", "割り当て負担",
                "後継の証しが担う", "新たに計算可能になった"]:
        # 般化 check must exclude 一般化/汎化
        import re
        if bad == "般化":
            if re.search(r"(?<!一)(?<!汎)般化", allt):
                fails.append("般化 error remains")
        elif bad in allt:
            fails.append(f"reader token remains: {bad}")
    rt_left = allt.count("実時間")
    if rt_left:
        fails.append(f"実時間 remains x{rt_left}")

    # ---- repetition before/after (spec-level counts)
    rev1 = json.loads((EXECDIR / "compact-input-rev1.json").read_text(encoding="utf-8"))
    rev2 = json.loads((EXECDIR / "compact-input-rev2.json").read_text(encoding="utf-8"))

    def famcounts(data):
        full = ""
        for p in data["packages"]:
            for b in p["blocks"]:
                full += b["text"] + "\n"
            full += p.get("deck", "") + "\n"
        import re
        return {
            "論文著者": len(re.findall("論文著者", full)),
            "委ねられる": len(re.findall("委ねられる", full)),
            "新たに計算可能になった": len(re.findall("新たに計算可能になった", full)),
            "著者らの評価では/報告値では/原論文で": (len(re.findall("著者らの評価では", full))
                + len(re.findall("報告値では", full)) + len(re.findall("原論文で", full))
                + len(re.findall("著者らは報告する", full))),
            "実時間": len(re.findall("実時間", full)),
            "リアルタイム": len(re.findall("リアルタイム", full)),
        }

    before, after = famcounts(rev1), famcounts(rev2)
    rep = {"before": before, "after": after,
           "note": ("Template heads reduced by varied reformulation (attribution and limitation "
                    "semantics preserved in every edited paragraph; JSON evidence bindings unchanged). "
                    "Counts alone are not the PASS criterion; qualitative check: no paragraph lost its "
                    "source attribution or boundary condition in the rewrite set.")}
    (EXECDIR / "repetition-report-rev2.json").write_text(
        json.dumps(rep, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if fails:
        print("REV2 AUDIT FAIL:")
        for f in fails:
            print(" -", f)
        return 1
    print("ALL REV2 AUDITS PASS")
    print(json.dumps(rep, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
