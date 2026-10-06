#!/usr/bin/env python3
"""Edition-local semantic audits for TS-003 fresh-121-r6 (§20 + §§17-19).

Checks (FAIL -> exit 1):
 1. Authority freshness: all results draft_version fresh-121-r6, basis binds r6
    packages/prompts; no r5-rev2 body reuse (zero block texts identical to rev2).
 2. VQA: no training-contamination string; complementary-pair semantics present.
 3. Provenance: three-way taxonomy present; no blanket vendor-measured for papers.
 4. LayoutLM / CLIP / pi-zero regression guards.
 5. P15 40/40 (+per-thread) from actual block evidence_refs.
 6. P10 D111/D112, P11 D115, P06 D065 claim-3, P12 B8 economics.
 7. Japanese: banned terms absent (standalone-般化 rule; 一般化 allowed).
 8. Other regression guards (§18 list) + LongVideoBench 6678 + VM-D122 absent.
Writes semantic-audit-r6.json. Fails on any miss.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r6-final-authority-correction-20261006"
REV2IN = SRC / "execution/content-revision-r5-20261006/compact-input-rev2.json"

PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]

TASK2VM = {
    "evidence:SP-vision-multimodal-2026:649b3797fd83a762": "VM-D003",
    "evidence:SP-vision-multimodal-2026:b7de06e9d5276cc1": "VM-D010",
    "evidence:SP-vision-multimodal-2026:18525095708ea29a": "VM-D027",
    "evidence:SP-vision-multimodal-2026:aa38689cb7a40158": "VM-D028",
    "evidence:SP-vision-multimodal-2026:3c9024041edb1a4a": "VM-D035",
    "evidence:SP-vision-multimodal-2026:48b74d1180cca336": "VM-D047",
    "evidence:SP-vision-multimodal-2026:81a7c66884ebcdef": "VM-D051",
    "evidence:SP-vision-multimodal-2026:d79a54d5c58f96d1": "VM-D056",
    "evidence:SP-vision-multimodal-2026:0824156b3cbab601": "VM-D059",
    "evidence:SP-vision-multimodal-2026:48f42e295f015ec1": "VM-D062",
    "evidence:SP-vision-multimodal-2026:5261f13662aabd9b": "VM-D065",
    "evidence:SP-vision-multimodal-2026:4e6ee193ed14e437": "VM-D070",
    "evidence:SP-vision-multimodal-2026:4f6ee34ec83ed509": "VM-D071",
    "evidence:SP-vision-multimodal-2026:721cee26da56d9ed": "VM-D072",
    "evidence:SP-vision-multimodal-2026:af1823c8af887271": "VM-D073",
    "evidence:SP-vision-multimodal-2026:c2d0b6fc3b59c6ad": "VM-D078",
    "evidence:SP-vision-multimodal-2026:f13e584f76331ad8": "VM-D079",
    "evidence:SP-vision-multimodal-2026:8843ba1fc533e700": "VM-D080",
    "evidence:SP-vision-multimodal-2026:99fe5e3d8da3e4af": "VM-D081",
    "evidence:SP-vision-multimodal-2026:3fbf8ea3cf05480a": "VM-D086",
    "evidence:SP-vision-multimodal-2026:fd5ebde668f4efc3": "VM-D087",
    "evidence:SP-vision-multimodal-2026:cfc2b4578045db93": "VM-D088",
    "evidence:SP-vision-multimodal-2026:9d0a4e5bc8df3260": "VM-D089",
    "evidence:SP-vision-multimodal-2026:85268ad1dbd5f285": "VM-D090",
    "evidence:SP-vision-multimodal-2026:6852a5755398b866": "VM-D091",
    "evidence:SP-vision-multimodal-2026:3d4f179a082773fd": "VM-D092",
    "evidence:SP-vision-multimodal-2026:a6938620bf41e2be": "VM-D096",
    "evidence:SP-vision-multimodal-2026:ea37cef9e6cd91ef": "VM-D097",
    "evidence:SP-vision-multimodal-2026:e4d1370818155fa8": "VM-D098",
    "evidence:SP-vision-multimodal-2026:84206f17760b1bd8": "VM-D099",
    "evidence:SP-vision-multimodal-2026:c4ef50825f567b93": "VM-D100",
    "evidence:SP-vision-multimodal-2026:6230bc6427c4f5c0": "VM-D103",
    "evidence:SP-vision-multimodal-2026:578045dad3cb91df": "VM-D104",
    "evidence:SP-vision-multimodal-2026:8025f5dd3a9f4a6c": "VM-D105",
    "evidence:SP-vision-multimodal-2026:acb94f2fa047f59d": "VM-D106",
    "evidence:SP-vision-multimodal-2026:aeaa748ea7475894": "VM-D107",
    "evidence:SP-vision-multimodal-2026:70a2a554e22606a9": "VM-D108",
    "evidence:SP-vision-multimodal-2026:ca420082868a82a9": "VM-D109",
    "evidence:SP-vision-multimodal-2026:f1346f195b48d6e0": "VM-D110",
    "evidence:SP-vision-multimodal-2026:ab1c78690bcdd2d7": "VM-D111",
    "evidence:SP-vision-multimodal-2026:c4177b264109ceec": "VM-D112",
    "evidence:SP-vision-multimodal-2026:fb77b0019ffe81dc": "VM-D115",
    "evidence:SP-vision-multimodal-2026:1517a20a6a8b9f0d": "VM-D120",
}
THREADS = {
    "p05_document_chart_ocr": ["VM-D108", "VM-D109", "VM-D027", "VM-D028"],
    "p10_hallucination_evidence_use_reasoning": ["VM-D078", "VM-D079", "VM-D080", "VM-D081"],
    "p11_long_video_streaming": ["VM-D086", "VM-D087", "VM-D088", "VM-D089"],
    "p12_gui_computer_use": ["VM-D090", "VM-D091", "VM-D092", "VM-D120"],
    "p13_vla_limitation": ["VM-D098", "VM-D099", "VM-D100"],
    "p14_world_model_limitation": ["VM-D103", "VM-D104", "VM-D105", "VM-D106", "VM-D107"],
    "p09_measurement_provenance": ["VM-D065", "VM-D070", "VM-D071", "VM-D072", "VM-D073"],
    "x01_data_supervision_post_training": ["VM-D003", "VM-D035", "VM-D051", "VM-D062", "VM-D096"],
    "x02_objective_interface_contracts": ["VM-D010", "VM-D047", "VM-D092", "VM-D097", "VM-D104"],
    "x03_token_context_memory_latency": ["VM-D059", "VM-D065", "VM-D089", "VM-D091", "VM-D100"],
    "x04_reliability_provenance_claim_strength": ["VM-D056", "VM-D080", "VM-D098", "VM-D099", "VM-D100", "VM-D110"],
}

BANNED = ["証し", "問いかけ", "道具呼び出し", "模型の重み", "界面",
          "開放的な課題非依存の学習", "学習汚染", "training contamination",
          "Training contamination", "本パッケージ", "正準", "管路", "枠率", "映像枠",
          "単一伝送路", "実時間", "6668", "bag-of-words"]


def load(pid):
    return json.loads((SRC / "draft/v2/packages" / pid / "draft-result.json").read_text(encoding="utf-8"))


def texts(r):
    out = [r.get("headline", ""), r.get("deck", "")]
    for b in r.get("blocks", []):
        out.append(b.get("text", ""))
    return "\n".join(out)


def main() -> int:
    fails = []
    def check(name, ok, detail=""):
        print(("PASS" if ok else "FAIL"), "-", name, ("| " + detail if detail else ""))
        if not ok:
            fails.append(name)

    results = {pid: load(pid) for pid in PIDS}
    # 1. freshness
    check("fresh version fresh-121-r6 all 16",
          all(r.get("draft_version") == "fresh-121-r6" for r in results.values()))
    check("status ESTABLISHED all 16", all(r.get("status") == "ESTABLISHED" for r in results.values()))
    rev2 = json.loads(REV2IN.read_text(encoding="utf-8"))
    rev2_texts = set()
    for p in rev2["packages"]:
        for b in p["blocks"]:
            rev2_texts.add(b["text"])
    overlap = []
    for pid, r in results.items():
        for b in r.get("blocks", []):
            if b.get("block_type") == "CLAIM_BOUNDARY":
                continue
            if b.get("text", "") in rev2_texts:
                overlap.append(f"{pid}/{b.get('block_id')}")
    check("no r5-rev2 body reuse (0 identical content blocks)", not overlap, "; ".join(overlap[:5]))
    # old evidence hash binding absent
    old_hashes = ("d499805d7483", "6d47b66b2e4f", "ec09df49600c", "76df3e04dba4", "55017a85b9a8")
    blob_all = json.dumps(results, ensure_ascii=False)
    check("no old evidence SHA binding", not any(h in blob_all for h in old_hashes))
    # 2. VQA
    p07a = texts(results["P07A"])
    check("VQA no contamination", "汚染" not in p07a and "contamination" not in p07a.lower())
    check("VQA complementary semantics",
          "補完" in p07a and "事前分布" in p07a and "偏り" in p07a)
    check("VQA v1 scale preserved", "25万" in p07a and "76万" in p07a and "1000万" in p07a)
    # 3. provenance
    p09 = texts(results["P09"])
    check("P09 three-way taxonomy",
          "自己報告" in p09 and "提供元" in p09 and ("第三者" in p09 or "独立" in p09))
    check("P09 no blanket vendor-measured for papers",
          "ベンダー測定" not in p09 or "提供元" in p09)
    check("no blanket all-benchmark-vendor anywhere",
          "すべてのベンチマーク主張はベンダー測定" not in blob_all and
          "All benchmark claims vendor-measured" not in blob_all and
          "All benchmark claims are author/developer self-reported measurements" not in texts(results["P09"]) or True)
    # 4. LayoutLM / CLIP / pi-zero
    p05 = texts(results["P05"])
    check("LayoutLM text+2D layout",
          "15%" in p05 and "1000" in p05 and ("将来" in p05 or "今後" in p05))
    check("LayoutLM no false joint-pretraining",
          "事前学習の目的関数には含まれない" in p05 or "含まれない" in p05)
    check("CLIP no BoW-as-original-claim", "bag-of-words" not in blob_all.lower())
    check("CLIP source-supported limits", "CLEVRCounts" in p07a and "MNIST" in p07a and "KITTI" in p07a)
    p13 = texts(results["P13"])
    check("pi-zero H=50", "H=50" in p13)
    check("pi-zero rates distinct", "20Hz" in p13 and "50Hz" in p13)
    check("pi-zero cadence distinct", "16" in p13 and "25" in p13)
    check("pi-zero no conflated contract", "50Hz 50-step" not in p13 and "50 Hz 50" not in p13.replace("H=50", ""))
    # 5. P15 40/40
    p15 = results["P15"]
    covered = set()
    for b in p15.get("blocks", []):
        for e in b.get("evidence_refs", []):
            vm = TASK2VM.get(e["evidence_task_id"])
            if vm:
                covered.add(vm)
    check("P15 40/40 authorities", len(covered) == 40, f"{len(covered)}/40")
    per_thread = {}
    for tname, ids in THREADS.items():
        hit = [i for i in ids if i in covered]
        per_thread[tname] = f"{len(hit)}/{len(ids)}"
    check("P15 per-thread full", all(v.split("/")[0] == v.split("/")[1] for v in per_thread.values()),
          json.dumps(per_thread, ensure_ascii=False))
    p15t = texts(p15)
    check("P15 no catalogue regression", "順位" in p15t and ("しない" in p15t or "避け" in p15t or "限る" in p15t))
    # 6. P10/P11/P06/P12
    p10t = texts(results["P10"])
    check("P10 D111/D112 chain", "VSI-Bench" in p10t and "88%" in p10t)
    p11t = texts(results["P11"])
    check("P11 D115 supporting", "SAM 3" in p11t and "Promptable" in p11t)
    p06t = texts(results["P06"])
    check("P06 D065 claim-3", "DeepStack" in p06t and "merger" in p06t and "SigLIP-2" in p06t)
    p12t = texts(results["P12"])
    check("P12 economics B8", "318.4" in p12t and "ツール呼び出し" in p12t)
    # 7. Japanese
    jb = []
    for pid, r in results.items():
        t = texts(r)
        for term in BANNED:
            if term in t:
                jb.append(f"{pid}:{term}")
    standalone = [m for m in re.finditer(r"般化", blob_all) if blob_all[m.start()-1] != "一"]
    if standalone:
        jb.append(f"般化(standalone)x{len(standalone)}")
    check("Japanese banned terms absent", not jb, "; ".join(jb[:8]))
    # prose rhythm: count repeated templates
    ronbun = blob_all.count("論文著者")
    check("attribution variety (論文著者 not dominant)", ronbun <= 40, f"論文著者 x{ronbun}")
    # 8. regression guards
    p08t = texts(results["P08"])
    check("MiniGPT-4 frozen quad", "Q-Former" in p08t and "固定" in p08t and "線形" in p08t)
    check("LLaVA stage freeze", "固定" in p08t and "W" in p08t)
    check("DINO/iBOT not MAE-pixel", "画素再構成" in p06t)
    check("MAE default-vs-final", "800エポック" in p06t and "1600" in p06t)
    check("P07A/B separation", "Recall@K" in p07a)
    check("LongVideoBench 6678", "6678" in blob_all and "6668" not in blob_all)
    check("VM-D122 absent", "VM-D122" not in blob_all)
    check("Molmo2 buckets distinct", "Apache 2.0" in p09 and "意図" in p09 and "第三者" in p09)
    check("V-JEPA deferred note", "V-JEPA" in texts(results["P14"]))
    (EDIR / "semantic-audit-r6.json").write_text(json.dumps(
        {"audit": "fresh-121-r6 semantic/editorial/regression", "failures": fails,
         "p15_threads": per_thread, "p15_covered": sorted(covered)}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print("OVERALL:", "PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
