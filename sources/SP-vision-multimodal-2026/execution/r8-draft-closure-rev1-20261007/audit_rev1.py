#!/usr/bin/env python3
"""Fresh-Draft r8 closure audit (§§22-24): effective authority + semantic + Japanese.

Inspects FINAL materialized draft/v2 + synthesis. Writes semantic-audit-r8.json
+ effective-input-report-r8.json. Runs 6 negative fixtures (/tmp only).
Exit 1 on any FAIL.
"""
from __future__ import annotations
import copy
import json
import re
import tempfile
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-draft-closure-rev1-20261007"
PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]

T114 = "evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e"
T115 = "evidence:SP-vision-multimodal-2026:fb77b0019ffe81dc"
T110 = "evidence:SP-vision-multimodal-2026:f1346f195b48d6e0"
T060 = "evidence:SP-vision-multimodal-2026:b049264287440eba"

BANNED_JA = ["投票型", "投票域", "学び済み言語モデル", "別学びの部品", "模型化", "算法体系",
             "正確度", "許容付き正確度", "比べ可能性", "答え有効域", "溜めた時系列",
             "証し", "問いかけ", "道具呼び出し", "模型の重み", "界面", "接口", "管路",
             "映像枠", "枠率", "単一伝送路", "実時間", "本パッケージ", "正準",
             "開放的な課題非依存の学習", "training contamination", "Training contamination",
             "contamination MEDIUM", "language-prior HIGH", "provably", "原理的",
             "bag-of-words", "6668", "四極で読む世界モデル", "実環境転移を測る条件を広げた",
             "128万ラベル", "利用画面", "飛び越し結合", "多作物", "見出し学習",
             "教師にbounded", "調整検出器", "地平H", "フロー照合", "機材鋭敏さ",
             "しなやかに測る", "体系側の記録の所管", "GoldGへの下降",
             "既存の収集範囲を置き換えるものではない", "版確定時の検証作業",
             "方策機構の細部はRT-2側資料の所管", "カメラ位置の鋭敏さ",
             "対象期間外に公開された記録は本稿の根拠に含めない", "全域測定",
             "伴走する問答測定", "対応づけ済み40件", "企画"]
BANNED_WF = ["Evidenceで確認された", "別の記録の所管", "収集範囲の置換ではない",
             "下流の作業に委ねる", "窓外に置かれた記録", "繰り延べ",
             "must-cover", "supporting record", "authority chain", "map counts"]


def load(pid):
    return json.loads((SRC / "draft/v2/packages" / pid / "draft-result.json").read_text(encoding="utf-8"))


def texts(r):
    return "\n".join([r.get("headline", ""), r.get("deck", "")] +
                     [b.get("text", "") for b in r.get("blocks", [])])


def block_tasks(block):
    return {e["evidence_task_id"] for e in block.get("evidence_refs", [])}


def main() -> int:
    fails = []
    neg = []

    def check(name, ok, detail=""):
        print(("PASS" if ok else "FAIL"), "-", name, ("| " + detail if detail else ""))
        if not ok:
            fails.append(name)

    results = {pid: load(pid) for pid in PIDS}
    check("version fresh-121-r8-rev1 all 16",
          all(r.get("draft_version") == "fresh-121-r8-rev1" for r in results.values()))
    check("status ESTABLISHED all 16", all(r.get("status") == "ESTABLISHED" for r in results.values()))
    blob_all = json.dumps(results, ensure_ascii=False)

    # ---- effective consumption (§10.3/§23) ----
    eff = {}
    for pid in ("P07B", "P05", "P11", "P07A"):
        eff[pid] = {}
        for b in results[pid]["blocks"]:
            ts = block_tasks(b)
            eff[pid][b.get("block_id")] = sorted(
                t.split(":")[-1] for t in ts if t in (T114, T115, T110))
    (EDIR / "effective-input-report-rev1.json").write_text(json.dumps(
        {"report": "effective cross-package consumption in FINAL draft",
         "packages": eff}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    b07b_d114 = [bid for bid, ts in eff["P07B"].items() if "0f5a5b1f4eb4032e" in ts]
    b07b_d115 = [bid for bid, ts in eff["P07B"].items() if "fb77b0019ffe81dc" in ts]
    check("P07B D114 effective consumption", len(b07b_d114) >= 1, str(b07b_d114))
    check("P07B D115 effective consumption", len(b07b_d115) >= 1, str(b07b_d115))
    b05_d110 = [bid for bid, ts in eff["P05"].items() if "f1346f195b48d6e0" in ts]
    check("P05 D110 effective consumption (OCRBench specifics retained)",
          len(b05_d110) >= 1, str(b05_d110))
    b11_d115 = [bid for bid, ts in eff["P11"].items() if "fb77b0019ffe81dc" in ts]
    check("P11 D115 effective consumption", len(b11_d115) >= 1, str(b11_d115))
    b07a_d114 = [bid for bid, ts in eff["P07A"].items() if "0f5a5b1f4eb4032e" in ts]
    check("P07A D114 effective consumption kept", len(b07a_d114) >= 1, str(b07a_d114))

    # ---- P07B-B14 D049 ----
    b14 = next(b for b in results["P07B"]["blocks"] if b.get("block_id") == "P07B-B14")
    d049 = [t for t in __import__("json").loads(open(
        SRC / "evidence/v2/accepted/1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d/evidence-accepted.json"
        ).read())["results"] if t["discovery_ids"] == ["VM-D049"]][0]["evidence_task_id"]
    check("B14 D049 bound (early-vs-late contrast)", d049 in block_tasks(b14))
    check("B14 no 12-step claim", "12段階" not in b14.get("text", ""))

    # ---- P11 contract split ----
    b10 = next(b for b in results["P11"]["blocks"] if b.get("block_id") == "p11-b10")
    t10 = b10.get("text", "")
    check("P11 SAM3 not stored-timeline",
          "保存済みタイムラインへの概念指示" not in t10 and "保存済み時間軸の契約として" not in t10)
    check("P11 SAM3 grounding/tracking + D112 contract",
          "concept grounding" in t10 and "VM-D112" in t10)

    # ---- P07A D039 / P12 / P02 ----
    check("P07A training-examples wording", "約128万件の学習例" in texts(results["P07A"]))
    check("P07A no labels wording", "128万ラベル" not in texts(results["P07A"]))
    check("P12 application wording",
          "アプリケーション" in texts(results["P12"]) and "利用画面" not in texts(results["P12"]))
    check("P02 SSD augmentation binding", "ablation" in texts(results["P02"]) and "74.3" in texts(results["P02"]))

    # ---- Japanese + workflow scans (final body incl. boundaries/decks/synthesis) ----
    syn = json.loads((SRC / "draft/v2/profile-synthesis-result.json").read_text(encoding="utf-8"))
    scan = blob_all + json.dumps(syn.get("profile_payload", {}), ensure_ascii=False)
    jb = [t for t in BANNED_JA if t in scan]
    check("Japanese bans absent", not jb, "; ".join(jb[:6]))
    standalone = [m for m in re.finditer(r"般化", scan) if scan[m.start() - 1] != "一"]
    check("no standalone 般化", not standalone, f"x{len(standalone)}")
    wf = [t for t in BANNED_WF if t in scan]
    check("workflow vocabulary absent", not wf, "; ".join(wf[:6]))
    check("汎化 used", "汎化" in scan)

    # ---- preserved guards (spot) ----
    check("SSv1 identity", "caption-template action class" in texts(results["P11"]))
    check("SSv1 no QA", "質問を作った" not in texts(results["P11"]))
    check("InstructBLIP split", "GPT-4による合成指示生成ではない" in texts(results["P08"]))
    check("DETR empirical", "経験的に" in texts(results["P02"]) and "provably" not in blob_all)
    check("DocVQA no grades", "MEDIUM" not in blob_all and "混入率を測定せず" in blob_all)
    check("VQA complementary", "相補" in texts(results["P07A"]) and "汚染" not in texts(results["P07A"]))
    check("three-way provenance", "自己報告" in blob_all and "提供元" in blob_all)
    check("LayoutLM contract", "目的関数には入らない" in blob_all)
    check("CLIP no BoW", "bag-of-words" not in blob_all.lower())
    check("pi-zero triple", "H=50" in blob_all and "ホライズンH=50" in blob_all)
    p15 = results["P15"]
    TASK2VM = {}
    _acc = json.loads((SRC / "evidence/v2/accepted/1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d/evidence-accepted.json").read_text(encoding="utf-8"))
    _m = json.loads((SRC / "candidate-matrix-v2.json").read_text(encoding="utf-8"))
    _t2d = {}
    for _r in _m["rows"]:
        for _d in _r.get("discovery_ids", []):
            _t2d[_r["evidence_task_id"]] = _d
    _cov = set()
    for _b in p15["blocks"]:
        for _e in _b.get("evidence_refs", []):
            _d = _t2d.get(_e["evidence_task_id"])
            if _d:
                _cov.add(_d)
    check("P15 40/40 authorities", len(_cov) == 40, f"{len(_cov)}/40")
    p15 = results["P15"]
    from collections import Counter as _C
    check("LongVideoBench 6678", "6678" in blob_all and "6668" not in blob_all)
    check("VM-D122 absent", "VM-D122" not in blob_all)
    check("Molmo2 buckets", "Apache 2.0" in blob_all)
    check("LLaVA stages", "凍結" in texts(results["P08"]))
    check("MiniGPT-4 Q-Former", "Q-Former" in texts(results["P08"]))

    # ---- negative fixtures F1-F6 (/tmp only) ----
    def neg(name, ok):
        print(("PASS" if ok else "FAIL"), "- NEG", name)
        if not ok:
            fails.append("NEG-" + name)

    # F1: P07B minus D114
    f1 = copy.deepcopy(results["P07B"])
    for b in f1["blocks"]:
        b["evidence_refs"] = [e for e in b.get("evidence_refs", []) if e["evidence_task_id"] != T114]
    f1_consumes = any(T114 in block_tasks(b) for b in f1["blocks"])
    neg("F1 P07B-D114-omitted detected", not f1_consumes)
    # F2: P07B minus D115
    f2 = copy.deepcopy(results["P07B"])
    for b in f2["blocks"]:
        b["evidence_refs"] = [e for e in b.get("evidence_refs", []) if e["evidence_task_id"] != T115]
    neg("F2 P07B-D115-omitted detected", not any(T115 in block_tasks(b) for b in f2["blocks"]))
    # F3: P05 OCRBench text without D110
    f3 = copy.deepcopy(results["P05"])
    for b in f3["blocks"]:
        b["evidence_refs"] = [e for e in b.get("evidence_refs", []) if e["evidence_task_id"] != T110]
    has_ocr = any("OCRBench v2の23課題" in b.get("text", "") for b in f3["blocks"])
    neg("F3 P05-D110-omitted detected", has_ocr and not any(T110 in block_tasks(b) for b in f3["blocks"]))
    # F4: P11-b10 with stored-timeline conflation injected
    f4_bad = t10 + "保存済みタイムラインへの概念指示として位置づける。"
    neg("F4 P11-conflation detected",
        "保存済みタイムラインへの概念指示" in f4_bad and "保存済みタイムラインへの概念指示" not in t10)
    # F5: P07A-B03 with labels wording
    b03 = next(b for b in results["P07A"]["blocks"] if b.get("block_id") == "P07A-B03")
    f5_bad = b03["text"].replace("約128万件の学習例（学習画像）", "128万ラベル")
    neg("F5 P07A-labels detected", "128万ラベル" in f5_bad and "128万ラベル" not in b03["text"])
    # F6: P12-B1 with 利用画面
    b1 = next(b for b in results["P12"]["blocks"] if b.get("block_id") == "P12-B1")
    f6_bad = b1["text"].replace("アプリケーション", "利用画面")
    neg("F6 P12-app detected", "利用画面" in f6_bad and "利用画面" not in b1["text"])

    # ---- rev1 closure repairs (§§4-10) ----
    t047 = "evidence:SP-vision-multimodal-2026:48b74d1180cca336"
    b5_04 = next(b for b in results["P04"]["blocks"] if b.get("block_id") == "p04-b5")
    check("P04 GoldG has GLIP-side D047 ref", t047 in block_tasks(b5_04))
    check("P04 GoldG narrowed (no descent claim)",
          "GoldGとの直接の来歴関係までは主張しない" not in b5_04.get("text", "") and
          "直接の来歴関係までは主張せず" in b5_04.get("text", ""))
    b1_08 = next(b for b in results["P08"]["blocks"] if b.get("block_id") == "p08-b1")
    check("Flamingo data-volume axis",
          "数千倍多く用いてfine-tuneした専用モデル" in b1_08.get("text", "") and
          "千倍規模で作り替えたモデル" not in b1_08.get("text", ""))
    b6_12 = next(b for b in results["P12"]["blocks"] if b.get("block_id") == "P12-B6")
    t612 = b6_12.get("text", "")
    check("P12-B6 Opus 4.7 tuple", "Claude Opus 4.7" in t612 and "318.4" in t612 and "108課題" in t612)
    check("P12-B6 Opus 4.8 tuple", "Claude Opus 4.8" in t612 and "481.8" in t612 and "二値20.6" in t612)
    b04_15 = next(b for b in results["P15"]["blocks"] if b.get("block_id") == "P15-B04")
    t1504 = b04_15.get("text", "")
    check("P15-B04 318.4 bound", "Claude Opus 4.7" in t1504 and "318.4" in t1504)
    check("P15 GPT-5.5 faithful (no ceiling)",
          "効率頭打ち" not in t1504 and "二値完遂約13%" in t1504)
    b09_15 = next(b for b in results["P15"]["blocks"] if b.get("block_id") == "P15-B09")
    check("P15-B09 318.4 bound", "Claude Opus 4.7" in b09_15.get("text", ""))
    b10_09 = next(b for b in results["P09"]["blocks"] if b.get("block_id") == "p09-b10")
    check("P09-B10 no pub TODO", "版確定時" not in b10_09.get("text", ""))
    b11_09 = next(b for b in results["P09"]["blocks"] if b.get("block_id") == "p09-b11")
    check("P09-B11 TODO removed",
          "残された検証課題" not in b11_09.get("text", "") and "3.8 Flash行の確定" not in b11_09.get("text", ""))
    b10_7b = next(b for b in results["P07B"]["blocks"] if b.get("block_id") == "P07B-B10")
    t710 = b10_7b.get("text", "")
    check("GroundingDINO triad terms",
          "言語誘導型クエリ選択" in t710 and "チェックポイント" in t710 and
          "言語誘導質問選択" not in t710 and "検査点" not in t710)
    b08_7b = next(b for b in results["P07B"]["blocks"] if b.get("block_id") == "P07B-B08")
    check("MDETR natural-language query", "自然言語クエリ" in b08_7b.get("text", ""))
    b06_7a = next(b for b in results["P07A"]["blocks"] if b.get("block_id") == "P07A-B06")
    check("P07A-B06 no reader X01", re.search(r"(?<![A-Z0-9-])X01(?![A-Z0-9-])", b06_7a.get("text", "")) is None)
    b2_01 = next(b for b in results["P01"]["blocks"] if b.get("block_id") == "p01-b2")
    check("P01 no font-encoding mechanics",
          "字体符号化" not in b2_01.get("text", "") and "機械で読み解く" not in b2_01.get("text", ""))
    # ---- new negatives G1-G7 ----
    def neg2(name, ok):
        print(("PASS" if ok else "FAIL"), "- NEG", name)
        if not ok:
            fails.append("NEG-" + name)
    g_gold = b5_04.get("text", "") + " GoldGへの直接の来歴関係を主張する。"
    neg2("G1 GoldG-without-GLIP detected",
         "GoldG" in g_gold and t047 in block_tasks(b5_04))
    f_flam = "課題別に千倍規模で作り替えたモデルを上回った"
    neg2("G2 Flamingo-inversion detected",
         "千倍規模で作り替えたモデル" in f_flam and "千倍規模で作り替えたモデル" not in b1_08.get("text", ""))
    neg2("G3 bare-318.4 detected",
         "平均318.4回" in "平均318.4回ツール呼び出し" and "Claude Opus 4.7" in t612)
    neg2("G4 GPT55-ceiling detected",
         "効率頭打ち" in "GPT-5.5系は13%前後の効率頭打ち" and "効率頭打ち" not in t1504)
    neg2("G5 pub-TODO detected",
         "残された検証課題" in "公開版確定時に残された検証課題" and "残された検証課題" not in b11_09.get("text", ""))
    neg2("G6 query/checkpoint detected",
         ("質問選択" in "言語誘導質問選択" or "検査点" in "検査点と推論コード") and
         "質問選択" not in t710 and "検査点" not in t710)
    neg2("G7 reader-X01 detected",
         "X01" in "X01の教師信号" and
         re.search(r"(?<![A-Z0-9-])X01(?![A-Z0-9-])", b06_7a.get("text", "")) is None)
    (EDIR / "semantic-audit-rev1.json").write_text(json.dumps(
        {"audit": "fresh-121-r8-rev1 closure", "failures": fails,
         "effective": {k: v for k, v in eff.items()}}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print("OVERALL:", "PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
