#!/usr/bin/env python3
"""Build compact-input-fresh-121-r8-rev1.json: bounded closure repair from r8 spec.

- Exact replacements (each asserted to fire): §§5/6/8/9/10/13/18/19/20.
- Full-block rewrites: p04-b5 (narrowed GoldG + D047), p08-b1 (Flamingo scale),
  P12-B6 + P15-B04/B09 (D091 tuples), P09-B10/B11 (TODO removal),
  P07B-B10 (triad), p11-b10 (§16 wording kept, refs kept).
- discovery_ids: p04-b5 += VM-D047; P07B-B14 keeps D049; p08-b8 keeps D060.
- P11 must_cover_map remapped to r8 wording.
- draft_version fresh-121-r8-rev1. No upstream/Architecture change.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-draft-closure-rev1-20261007"
IN = SRC / "execution/r8-authority-binding-repair-20261007/compact-input-fresh-121-r8.json"
OUT = EDIR / "compact-input-fresh-121-r8-rev1.json"

REPLACEMENTS = [
    # §5 P08 Flamingo: data-volume axis, not model scale
    ("Flamingoは学習済みの視覚側と言語側をgated cross-attentionの重い層でつなぎ、",
     "Flamingoは学習済みの視覚側と言語側をgated cross-attention層でつなぎ、"),
    ("課題別に千倍規模で作り替えたモデルを上回ったと著者ら自身の測定は伝える。",
     "一部の評価では、課題固有データを数千倍多く用いてfine-tuneした専用モデルを上回ったと著者ら自身の測定は伝える。"),
    # §8 Grounding DINO triad + checkpoint + MDETR query
    ("Grounding DINOは特徴増強と言語誘導質問選択と相互様式復号器の3段階で",
     "Grounding DINOはfeature enhancer（特徴強化器）とlanguage-guided query selection（言語誘導型クエリ選択）とcross-modality decoder（クロスモダリティ・デコーダ）の3段階で"),
    ("検査点と推論コードが公開された。", "チェックポイントと推論コードが公開された。"),
    ("MDETRは自然文の質問でDETRを条件づけ、", "MDETRは自然言語クエリでDETRを条件づけ、"),
    # §9 P07A X01 label
    ("画像文対の大規模契約はX01の教師信号の系譜に位置づけられる。",
     "画像文対の大規模契約は、大規模画像テキスト対による教師信号の系譜に位置づけられる。"),
    # §11 P01 epistemic scope
    ("著者PDFの字体符号化の制約から本文の全体を機械で読み解くことはできず、抄録の外側の細部には踏み込まない。",
     "本節で用いるのは入手・確認できた一次資料の抄録水準の記述であり、細部には踏み込まない。"),
    # §20 資料/所管/委ね cleanup (dataset senses only; records senses kept)
    ("GLIPの資料実践再定式とは契約が異なり", "GLIPのデータ実践による再定式とは契約が異なり"),
    ("GLIPの資料実践か", "GLIPのデータ実践か"),
    ("ウェブ資料依存の限界を条件づける", "ウェブデータ依存の限界を条件づける"),
]

NEW_P04_B5 = ("関係構造の来歴として、Visual Genomeは領域記述データの先行形態にも位置づけられる。後の検出-接地統一学習（GLIPの語句接地への書き直し）が前提にする領域と言語の対応づけの原型を示す点に、ここへ置く理由がある。GoldGの構成の詳細や直接の来歴関係までは主張せず、本節では関係構造の限定事例として扱い、語彙拡張の系統史へは広げない。独立した第三者の再現ではなく原論文の測定として読む。")

NEW_P12_B6 = ("OSWorld 2.0は108件の長時間ワークフローから成り、中央値で1.6人間時間の作業を扱う到達点の事例である。流れの中の対話、動的環境、複数情報源にまたがる推論、暗黙状態の推定、視覚と空間の精密さを課題現象とし、真正な成果物と状態を持つ利用者像と安全性報告を備える。論文著者測定では、Claude Opus 4.7を用いた最大思考・単一行動設定で108課題平均318.4回のツール呼び出しとなり、OSWorld 1.0の約30回と桁が異なる。500段階バッチ構成ではClaude Opus 4.8の最大思考で二値20.6%・部分54.8%・481.8回と著者測定で示される。いずれもモデル・思考・ツール・手順・段数・公開条件を結びつけて読む。条件結合の厳密さが本巻で最も強い分野であり、名称と設定と手順を明示して読む。安全性報告は評価の付随情報として扱う。")

NEW_P15_B04_TAIL = None  # handled via targeted sentence replacements below

P15_B04_REPLACEMENTS = [
    ("OSWorld 2.0は単一行動設定で平均318.4回のツール呼び出しという状態管理費用を示し、OSWorld 1.0の約30回と桁が違う。",
     "OSWorld 2.0はClaude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回のツール呼び出しという状態管理費用を示し、OSWorld 1.0の約30回と桁が違う。"),
    ("GPT-5.5系は13%前後の効率頭打ちが著者測定として記される。",
     "GPT-5.5はトークン効率を重視した設定で二値完遂約13%のplateauを示すと著者測定で記される。"),
]

NEW_P15_B09_SENT = ("Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回ツール呼び出しがOSWorld 1.0約30回と桁違いの状態管理費用を示す。",)

P15_B09_OLD = "平均318.4回ツール呼び出しがOSWorld 1.0約30回と桁違いの状態管理費用を示す。"

NEW_P09_B10 = ("第二の系譜のオープン性はモデルの重みとデータの提供で示される。InternVLリポジトリはモデルの重みとInternVL-Dataの公開、1.0から3.5までの報告系譜と論文対応、3.5-GPT-OSS系の学習コード公開をREADME表層で示す。3.5系の存在は来歴注記に留める。ファイル水準の提供範囲は未確認であり、本節の主張はリポジトリ表層の確認範囲に留まる。molmo2リポジトリはデータ準備と事前学習やSFTや長文脈SFT、評価ツール群、vLLM推論、チェックポイント変換、MolmoPoint拡張をコード水準で確認する。")

P11_MC_OLD = "SAM 3 memory video tracking as supporting stored-timeline evidence"
P11_MC_NEW = ("SAM 3 concept-prompted video grounding and memory-based tracking are supporting "
              "temporal-grounding evidence; stored-timeline on-demand navigation remains the "
              "distinct VM-D112 contract.")


def main() -> int:
    EDIR.mkdir(parents=True, exist_ok=True)
    spec = json.loads(IN.read_text(encoding="utf-8"))
    fired = []
    missed = []
    for p in spec["packages"]:
        for field in ("headline", "deck"):
            if p.get(field):
                for old, new in REPLACEMENTS:
                    if old in p[field]:
                        p[field] = p[field].replace(old, new)
                        fired.append(f"{p['package_id']}:{field}:{old[:30]}")
        for b in p["blocks"]:
            if not b.get("text"):
                continue
            for old, new in REPLACEMENTS:
                if old in b["text"]:
                    b["text"] = b["text"].replace(old, new)
                    fired.append(f"{p['package_id']}/{b['block_id']}:{old[:30]}")
        if p.get("boundaries_text"):
            for old, new in REPLACEMENTS:
                if old in p["boundaries_text"]:
                    p["boundaries_text"] = p["boundaries_text"].replace(old, new)
                    fired.append(f"{p['package_id']}:boundaries:{old[:30]}")
    for old, _ in REPLACEMENTS:
        if not any(old[:30] in f for f in fired) and "7データセット群" not in old:
            missed.append(old[:60])
    print(f"replacements fired: {len(fired)}")
    if missed:
        print("MISSED (no-op):")
        for m in missed:
            print("  -", m)
        raise SystemExit("no-op replacements present; fix strings")

    def get_block(pid, bid):
        p = next(x for x in spec["packages"] if x["package_id"] == pid)
        return p, next(x for x in p["blocks"] if x.get("block_id") == bid)

    # P04-B5 narrowed + D047
    p04, b5 = get_block("P04", "p04-b5")
    assert "GoldG" in b5["text"], "P04-B5 GoldG context missing"
    b5["text"] = NEW_P04_B5
    b5["discovery_ids"] = ["VM-D021", "VM-D047"]
    # P12-B6 / P15-B04 / P15-B09 condition binding
    _, b6 = get_block("P12", "P12-B6")
    assert "318.4" in b6["text"]
    b6["text"] = NEW_P12_B6
    _, b04 = get_block("P15", "P15-B04")
    for old, new in P15_B04_REPLACEMENTS:
        assert old in b04["text"], old[:60]
        b04["text"] = b04["text"].replace(old, new)
    _, b09 = get_block("P15", "P15-B09")
    assert P15_B09_OLD in b09["text"], P15_B09_OLD[:60]
    b09["text"] = b09["text"].replace(P15_B09_OLD, NEW_P15_B09_SENT[0] if isinstance(NEW_P15_B09_SENT, tuple) else NEW_P15_B09_SENT)
    # P09-B10 trim (keep remainder) / P09-B11 delete TODO sentence
    _, b10 = get_block("P09", "p09-b10")
    idx = b10["text"].find("molmo2リポジトリはデータ準備")
    assert idx > 0
    b10["text"] = NEW_P09_B10 + b10["text"][idx:]
    _, b11 = get_block("P09", "p09-b11")
    todo = "LongVideoBenchの6,678問を含む行単位の対応づけと3.8 Flash行の確定は、公開版確定時に残された検証課題である。"
    assert todo in b11["text"]
    b11["text"] = b11["text"].replace(todo, "").rstrip()
    # P11 must_cover_map remap (r8 wording already in Architecture; map follows)
    p11 = next(x for x in spec["packages"] if x["package_id"] == "P11")
    mmap = p11.get("must_cover_map")
    assert mmap is not None, "P11 must_cover_map missing"
    if P11_MC_OLD in mmap:
        mmap[P11_MC_NEW] = mmap.pop(P11_MC_OLD)
    assert P11_MC_NEW in mmap, list(mmap)

    spec["draft_version"] = "fresh-121-r8-rev1"
    spec["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 Draft closure revision r8-rev1 from Architecture r8 APPROVED "
                       "(same authority; targeted reader-facing + binding repair: P04 GoldG/D047, "
                       "Flamingo scale, OSWorld conditions, P09 TODO removal, Grounding DINO terms, "
                       "Japanese/workflow cleanup; r8 authority unchanged; "
                       "no TeX/PDF; DRAFT_COMPLETE held for independent content review)"),
        "generated_at": "2026-10-07T08:00:00Z",
        "run_reference": None,
    }
    OUT.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"rev1 spec: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
