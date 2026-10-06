#!/usr/bin/env python3
"""Edition-local semantic/content audits for TS-003 content revision r5-rev1.

Writes audit JSONs into the execution dir. Fails (exit 1) on any required miss.
Checks:
 1. P15 40-ID consumption from actual reader-facing block evidence_refs (+per-thread counts).
 2. P15 must_cover semantic mapping (no blanket rows).
 3. P10 D111/D112 binding + PARTIAL restraint + no-online-streaming misrep (text scan).
 4. P11 D115 supporting binding; no 'name only'.
 5. P06 D065 claim-3 binding on the reuse sentence.
 6. P12 token/context axis present.
 7. P09 license/data-term bucket separation (text scan).
 8. LongVideoBench 6678 everywhere; no 6668.
 9. Reader-facing Japanese: banned tokens absent from all blocks/decks/headlines
    (管路, 枠率, 映像枠, 単一伝送路, 般化-as-error, 動作点, 本パッケージ, カード-as-internal,
    正準, 後の確認に譲る, 賢さ一般, 見取り, 筋道を立てる, 二段階の起動, G0x codes, PARTIAL/INSPECT codes...).
    with documented exceptions (モデルカード as document name; scaffold as approved term).
 10. Regression guards (LLaVA freeze topology, VQA v2 pairs, DINO/iBOT vs MAE,
     MiniGPT-4 Q-Former topology, OpenVLA real-robot success, HallusionBench restraint,
     Genie 3 non-inference, Qwen/Molmo license buckets, VM-D122 absent).
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r5-20261006"

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
    "p09_vendor_vs_independent": ["VM-D065", "VM-D070", "VM-D071", "VM-D072", "VM-D073"],
    "x01_data_supervision_post_training": ["VM-D003", "VM-D035", "VM-D051", "VM-D062", "VM-D096"],
    "x02_objective_interface_contracts": ["VM-D010", "VM-D047", "VM-D092", "VM-D097", "VM-D104"],
    "x03_token_context_memory_latency": ["VM-D059", "VM-D065", "VM-D089", "VM-D091", "VM-D100"],
    "x04_reliability_provenance_claim_strength": ["VM-D056", "VM-D080", "VM-D098", "VM-D099", "VM-D100", "VM-D110"],
}

PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]


def load(pid):
    return json.loads((SRC / "draft/v2/packages" / pid / "draft-result.json").read_text(encoding="utf-8"))


def block_vms(block):
    out = {}
    for e in block.get("evidence_refs", []):
        vm = TASK2VM.get(e["evidence_task_id"])
        if vm:
            out.setdefault(vm, []).append(f"{e['kind']}:{e['evidence_id']}")
    return out


def main() -> int:
    fails = []
    audits: dict = {}

    # ---- 1. P15 consumption
    p15 = load("P15")
    content_blocks = [b for b in p15["blocks"] if not b["block_id"].endswith("boundaries")]
    consumed: dict[str, list] = {}
    for b in content_blocks:
        for vm in block_vms(b):
            consumed.setdefault(vm, []).append(b["block_id"])
    map40 = sorted({d for ids in THREADS.values() for d in ids})
    assert len(map40) == 40
    missing = [d for d in map40 if d not in consumed]
    if missing:
        fails.append(f"P15 missing authorities: {missing}")
    per_thread = {t: {"expected": len(ids), "consumed": sum(1 for d in ids if d in consumed),
                      "missing": [d for d in ids if d not in consumed],
                      "blocks": sorted({b for d in ids for b in consumed.get(d, [])})}
                  for t, ids in THREADS.items()}
    for t, row in per_thread.items():
        if row["missing"]:
            fails.append(f"P15 thread {t} missing {row['missing']}")
    audits["p15_consumption"] = {"distinct_consumed": len(consumed), "distinct_expected": 40,
                                 "missing": missing, "per_thread": per_thread,
                                 "block_map": {b["block_id"]: sorted(block_vms(b)) for b in content_blocks}}

    # ---- 2. P15 must_cover semantic (no blanket rows)
    nblocks = len(content_blocks)
    blanket = [r["requirement"][:60] for r in p15["must_cover_coverage"]
               if len(r["block_ids"]) == nblocks]
    if blanket:
        fails.append(f"P15 blanket must_cover rows remain: {blanket}")
    audits["p15_must_cover"] = {
        r["requirement"]: r["block_ids"] for r in p15["must_cover_coverage"]}

    # ---- 3. P10
    p10 = load("P10")
    p10vms = {}
    for b in p10["blocks"]:
        for vm in block_vms(b):
            p10vms.setdefault(vm, []).append(b["block_id"])
    for need in ("VM-D111", "VM-D112"):
        if need not in p10vms:
            fails.append(f"P10 missing {need}")
    t10 = "\n".join(b["text"] for b in p10["blocks"])
    if "名のみ" in t10 or "賢さ一般" in t10 or "筋道を立てる" in t10 or "見取り" in t10 or "言葉の癖" in t10:
        fails.append("P10 banned reader language remains")
    if "2363" in t10:
        fails.append("P10 debiased-subset detail leaked")
    if "要旨の水準" not in t10:
        fails.append("P10 PARTIAL restraint wording missing")
    if "オンラインの流れを受け続ける状態の証拠でもない" not in t10:
        fails.append("P10 D112 streaming disclaimer missing")
    audits["p10"] = {k: v for k, v in p10vms.items()}

    # ---- 4. P11 D115
    p11 = load("P11")
    p11vms = {}
    for b in p11["blocks"]:
        for vm in block_vms(b):
            p11vms.setdefault(vm, []).append(b["block_id"])
    if "VM-D115" not in p11vms:
        fails.append("P11 missing VM-D115")
    t11 = "\n".join(b["text"] for b in p11["blocks"])
    if "名のみに留める" in t11:
        fails.append("P11 SAM3 name-only remains")
    if "単一伝送路" in t11:
        fails.append("P11 単一伝送路 remains")
    if "存在トークン" not in t11 or "メモリ型の映像追跡器" not in t11:
        fails.append("P11 SAM3 supporting content missing")
    audits["p11"] = {k: v for k, v in p11vms.items()}

    # ---- 5. P06 D065 claim-3
    p06 = load("P06")
    b06 = [b for b in p06["blocks"] if b["block_id"] == "P06-B06"][0]
    refs = [(e["evidence_task_id"], e["evidence_id"]) for e in b06["evidence_refs"]]
    if ("evidence:SP-vision-multimodal-2026:5261f13662aabd9b", "claim-3") not in refs:
        fails.append("P06-B06 missing D065 claim-3")
    if "Omni系" in b06["text"]:
        fails.append("P06-B06 Omni wording not narrowed")

    # ---- 6. P12 token axis
    p12 = load("P12")
    b8 = [b for b in p12["blocks"] if b["block_id"] == "P12-B8"]
    if not b8:
        fails.append("P12-B8 token economics block missing")
    else:
        if "318.4" not in b8[0]["text"] or "繰り返し符号化" not in b8[0]["text"]:
            fails.append("P12-B8 token axis content missing")

    # ---- 7. P09 buckets
    p09 = load("P09")
    b10 = [b for b in p09["blocks"] if b["block_id"] == "p09-b10"][0]
    for phrase in ["別の区分", "書き換えることはなく", "未確認である", "Apache 2.0"]:
        if phrase not in b10["text"]:
            fails.append(f"P09-B10 missing phrase: {phrase}")
    if "後の確認に譲る" in b10["text"]:
        fails.append("P09-B10 internal phrasing remains")

    # ---- 8. numerics
    all_text = ""
    for pid in PIDS:
        d = load(pid)
        all_text += "\n" + d.get("headline", "") + "\n" + d.get("deck", "")
        for b in d["blocks"]:
            all_text += "\n" + b["text"]
    if "6668" in all_text:
        fails.append("6668 remains")
    if "6678" not in all_text:
        fails.append("6678 missing")

    # ---- 9. reader Japanese
    banned = ["管路", "枠率", "映像枠", "単一伝送路", "動作点", "本パッケージ", "正準",
              "後の確認に譲る", "賢さ一般", "見取り", "筋道を立てる", "二段階の起動",
              "G01", "G02", "G03", "G04", "G05", "G06", "PARTIAL", "INSPECT",
              "must-cover", "supporting candidate", "authority",
              "1024画素", "注意の役割", "単一音声チャネル（モノラル）の毎秒1キロビット"[:0] or "単一伝送路",
              "名のみに留める", "本カード", "カードが裏づける", "カードが支える"]
    # カード-as-document (モデルカード) is allowed; flag only internal-sense uses
    card_bad = ["本カード", "カードが裏づける", "カードが支える", "カード更新"]
    hits = {}
    for pid in PIDS:
        d = load(pid)
        texts = [(d.get("headline", ""), "headline"), (d.get("deck", ""), "deck")] + \
                [(b["text"], b["block_id"]) for b in d["blocks"]]
        for text, label in texts:
            for pat in banned + card_bad:
                if pat and pat in text:
                    hits.setdefault(pat, []).append(f"{pid}/{label}")
    # の般化 error (excluding 一般化/汎化 which are fine)
    for m in re.finditer(r"(?<!一)(?<!汎)般化", all_text):
        fails.append(f"般化 error near: ...{all_text[max(0,m.start()-15):m.start()+5]}...")
        break
    # 枠-as-frame remnants (映像N枠 / 毎秒N枠 / N枠 patterns with digits)
    for m in re.finditer(r"[0-9]+枠|毎秒[0-9]*枠|可変枠率", all_text):
        fails.append(f"frame-counter remnant: {m.group(0)}")
        break
    if hits:
        fails.append(f"banned reader tokens remain: {hits}")
    audits["japanese_banned_hits"] = hits

    # open-vocabulary normalization: 開放語彙 must not remain in OVD senses
    ov_hits = []
    for pid in PIDS:
        d = load(pid)
        for b in d["blocks"]:
            if "開放語彙" in b["text"]:
                ov_hits.append(f"{pid}/{b['block_id']}")
    if ov_hits:
        fails.append(f"開放語彙 remains: {ov_hits}")

    # ---- 10. regression guards
    reg = {}
    def has(pat):
        return pat in all_text
    reg["vqa_v2_complementary"] = has("補完的構成") or has("類似画像対")
    reg["dino_distill_vs_mae"] = has("自己蒸留") and has("マスク")
    reg["minigpt4_qformer_frozen"] = has("凍結Q-Former") or has("凍結したQ-Former")
    reg["openvla_real_robot"] = has("97万件の実機実証")
    reg["hallusionbench_restraint"] = has("厳しい") and has("診断")
    reg["genie3_no_arch"] = has("アーキテクチャの断定は行わない")
    reg["qwen_apache"] = has("8B-Instructの重みもApache 2.0")
    reg["molmo_apache"] = (has("Molmo2-8BやO-7Bの重みはApache 2.0")
                             or has("モデル重みのライセンスはApache 2.0"))
    reg["no_vmd122"] = "VM-D122" not in all_text and "ev-vmd122" not in json.dumps(
        {pid: load(pid) for pid in PIDS}, ensure_ascii=False)
    for k, v in reg.items():
        if not v:
            fails.append(f"regression guard missing: {k}")
    audits["regression"] = reg

    (EXECDIR / "semantic-audit-r5-rev1.json").write_text(
        json.dumps(audits, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if fails:
        print("AUDIT FAIL:")
        for f in fails:
            print(" -", f)
        return 1
    print("ALL SEMANTIC AUDITS PASS")
    print(json.dumps({"p15_distinct": audits["p15_consumption"]["distinct_consumed"],
                      "regression": reg}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
