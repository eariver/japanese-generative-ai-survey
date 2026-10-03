#!/usr/bin/env python3
"""Build TS-003 edition-local reader/editorial authority r10 (Issue #559 bounded repair).

Revision chain: r9 (Sol-accepted) -> r10 (Issue #559 A-F only + provenance).
Canonical Draft authority remains checkpointed r1. r10 is publication-layer only,
never canonical Draft authority.

Primary sources read back before repair:
- Qwen3-Omni Technical Report §2.3/TM-RoPE https://arxiv.org/html/2509.17765
- QwenLM/Qwen3-Omni LICENSE https://github.com/QwenLM/Qwen3-Omni/blob/main/LICENSE
- LongVideoBench https://arxiv.org/html/2407.15754 (16->256 input frames)
- POPE https://arxiv.org/abs/2305.10355 (Polling-based Object Probing Evaluation)
- DETR accepted authority VM-D010 https://arxiv.org/abs/2005.12872 (300-epoch baseline 16xV100 ~3d vs 500-epoch comparison)
- docs/editorial/ja-technical-terminology-overtranslation-seed.md (contextual QA seed, not auto-dict)
"""
import copy
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
R9 = SRC / "publication/editorial/reader-editorial-authority-r9.json"
OUT = SRC / "publication/editorial/reader-editorial-authority-r10.json"

ISSUE = "SP-vision-multimodal-2026"


def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# (package, block, old, new, reason)
PATCHES = [
    # A. Qwen3-Omni 80ms temporal-ID granularity (p09-b5)
    ("P09", "p09-b5",
     "TM-RoPEで絶対時刻を合わせ、音声と映像のずれを80msに抑える。",
     "TM-RoPEで絶対時刻に結びつけた時間IDにより、音声・映像表現を約80msの共通時間分解能で並べる。音声表現の1フレームは原音声の約80msに対応し、音声の時間IDは80ms刻み、映像の時間IDは実際のタイムスタンプから動的に付与される。",
     "A: 80ms is temporal-ID granularity per Qwen3-Omni §2.3, not A/V error bound"),
    # A shorthand in p09-b6
    ("P09", "p09-b6",
     "80msの時刻合わせや234msの理論値",
     "約80msの時間ID分解能での時刻合わせや234msの理論値",
     "A: repair inherited false error-bound shorthand"),
    # B. Qwen3-Omni licensing categorical removal (p09-b6)
    ("P09", "p09-b6",
     "重みとコードの許諾は未確定のまま残り、確認済みと未確定を分けて記す。",
     "Qwen3-OmniのリポジトリはApache License 2.0のLICENSEを備え、技術報告はQwen3-Omni-30B-A3B／Qwen3-Omni-30B-A3B-Thinking／Qwen3-Omni-30B-A3B-Captionerの3者をApache 2.0で公開と記す。リポジトリ・コード面と名指しのモデルリリースの範囲で確認し、それを超える特定成果物の許諾は本稿の一次資料では確定しない。",
     "B: verified scope per repo LICENSE + report; no categorical unconfirmed"),
    # C. video frame 枠 -> フレーム (LongVideoBench input frames)
    ("P11", "p11-b3",
     "枠を増やして初めて点が伸び、枠数の効き方が明らかになった",
     "入力フレームを増やして初めて点が伸び、入力フレーム数の効き方が明らかになった",
     "C: LongVideoBench 16->256 input frames"),
    ("P11", "p11-b4",
     "枠数の効き方が鍵となる録りためた評価",
     "入力フレーム数の効き方が鍵となる録りためた評価",
     "C: retain recording-vs-streaming distinction, frame sense only"),
    ("P11", "p11-b5",
     "枠数の効き方はLongVideoBenchの側に記し",
     "入力フレーム数の効き方はLongVideoBenchの側に記し",
     "C: frame sense only"),
    ("P15", "p15-b4",
     "知見はコマを増やして初めて伸びることで、枠数の感受性が",
     "知見は入力フレームを増やして初めて伸びることで、入力フレーム数の感受性が",
     "C: normalize コマ+枠数 to input-frame meaning"),
    # D. POPE polling identity + stable/flexible
    ("P10", "p10-b2",
     "投票型のPOPEで安定にしなやかに測る。",
     "POPE (Polling-based Object Probing Evaluation)による問いかけ型の物体存在プロービングで、安定かつ柔軟に測る。",
     "D: polling identity + stable/flexible per POPE abstract"),
    ("P10", "p10-b2",
     "投票の範囲に限られ、開かれた応答の忠実さは制御ペアの道具が必要である。",
     "ポーリングによる問いかけの範囲に限られ、開かれた応答の忠実さは制御ペアの道具が必要である。",
     "D: polling scope, consequential"),
    ("P10", "p10-b3",
     "投票型評価はハルシネーションの一次検査",
     "POPEによる問いかけ型評価はハルシネーションの一次検査",
     "D: query-based, no voting"),
    ("P10", "P10-boundaries",
     "投票は投票の範囲に留まり",
     "ポーリングによる問いかけは問いかけの範囲に留まり",
     "D: boundary consequential to remove voting semantics"),
    ("P15", "p15-b3",
     "投票型のPOPEで安定にしなやかに測り",
     "POPE (Polling-based Object Probing Evaluation)による問いかけ型の物体存在プロービングで、安定かつ柔軟に測り",
     "D: same identity in synthesis-led section"),
    ("P15", "p15-b3",
     "ただし投票の射程にとどまり",
     "ただしポーリングによる問いかけの射程にとどまり",
     "D: polling scope"),
    ("P15", "p15-b3",
     "幅の測定と投票型評価と英語・中国語の評価範囲は別の契約",
     "幅の測定とPOPEによる問いかけ型評価と英語・中国語の評価範囲は別の契約",
     "D: no voting"),
    ("P15", "P15-boundaries",
     "投票で測ったことを自由な記述の忠実さとして語らず",
     "ポーリングによる問いかけで測ったことを自由な記述の忠実さとして語らず",
     "D: boundary consequential"),
    # E. ML baseline 基線 -> ベースライン
    ("P07B", "p07b-b2",
     "ゼロショット基線",
     "ゼロショットベースライン",
     "E: ML baseline identity"),
    ("P07B", "p07b-b5",
     "教師あり基線",
     "教師ありベースライン",
     "E: ML baseline identity"),
    # F. DETR schedule separation
    ("P02", "p02-b4",
     "代償として300〜500エポックのAdamW、16枚のV100で3日の日程、",
     "代償として300エポックの学習設定（AdamW、16枚のV100で約3日の学習期間）と、Faster R-CNN比較のための500エポックの長期設定、",
     "F: separate 300-epoch baseline (16xV100 ~3d) from 500-epoch comparison; 学習設定/学習期間 per DETR §4"),
]

# Deck patches (directly consequential: decks inherit same false meanings)
DECK_PATCHES = [
    ("P10",
     "投票と回転と視覚数学の道具の違い",
     "POPEによる問いかけ型評価と回転と視覚数学の道具の違い",
     "D-deck: polling identity in deck"),
    ("P11",
     "枠数の効き方と未確定の部分を正直に残す",
     "入力フレーム数の効き方と未確定の部分を正直に残す",
     "C-deck: input-frame sense in deck"),
]


def main() -> int:
    r9 = json.loads(R9.read_text(encoding="utf-8"))
    assert r9["issue_id"] == ISSUE
    r10 = copy.deepcopy(r9)
    by_pid = {p["package_id"]: p for p in r10["reader_packages"]}
    applied = []
    for pid, bid, old, new, reason in PATCHES:
        blk = [b for b in by_pid[pid]["ordered_blocks"] if b["block_id"] == bid]
        assert len(blk) == 1, (pid, bid)
        b = blk[0]
        assert old in b["reader_text"], f"patch miss {pid} {bid}: {old[:40]}"
        assert b["reader_text"].count(old) == 1, f"ambiguous {pid} {bid}"
        b["reader_text"] = b["reader_text"].replace(old, new)
        b["reader_text_sha256"] = sha_text(b["reader_text"])
        applied.append({"package_id": pid, "block_id": bid, "reason": reason,
                        "old": old, "new": new})
    for pid, old, new, reason in DECK_PATCHES:
        p = by_pid[pid]
        assert old in p["deck"], f"deck patch miss {pid}: {old[:40]}"
        assert p["deck"].count(old) == 1, f"ambiguous deck {pid}"
        p["deck"] = p["deck"].replace(old, new)
        p["deck_sha256"] = sha_text(p["deck"])
        applied.append({"package_id": pid, "block_id": "deck", "reason": reason,
                        "old": old, "new": new})
    # Update package file SHAs (r10 derived, not canonical)
    for p in r10["reader_packages"]:
        payload = json.dumps({"package_id": p["package_id"], "headline": p["headline"],
                              "deck": p["deck"], "blocks": p["ordered_blocks"]},
                             ensure_ascii=False, sort_keys=True).encode("utf-8")
        p["r10_derived_sha256"] = hashlib.sha256(payload).hexdigest()
    # Provenance: r10 revision
    r10["semantic_labels"] = {
        "CANONICAL_DRAFT_AUTHORITY": "checkpointed r1 via ARCHITECTURE_ESTABLISHED.json (DRAFT_COMPLETE checkpoint, immutable)",
        "READER_EDITORIAL_AUTHORITY": "Sol-accepted r9 refinement + Issue #559 bounded r10 repair, publication layer only",
        "warning": "r9/r10 wording must be consumed only via reader/editorial authority after canonical restore; never claim r9/r10 remains canonical Draft authority.",
    }
    r10["reader_editorial_revision"] = "r10"
    r10["parent_reader_revision"] = "r9"
    r10["parent_reader_sha256"] = hashlib.sha256(R9.read_bytes()).hexdigest()
    r10["issue_559"] = {
        "issue": "#559 [Publication][TS-003] Publication Preview REQUEST_CHANGES — Qwen3-Omni source fidelity + terminology repair",
        "primary_sources": [
            "Qwen3-Omni Technical Report §2.3/TM-RoPE https://arxiv.org/html/2509.17765",
            "QwenLM/Qwen3-Omni LICENSE https://github.com/QwenLM/Qwen3-Omni/blob/main/LICENSE",
            "LongVideoBench https://arxiv.org/html/2407.15754",
            "POPE https://arxiv.org/abs/2305.10355",
            "DETR accepted VM-D010 https://arxiv.org/abs/2005.12872",
            "docs/editorial/ja-technical-terminology-overtranslation-seed.md (contextual QA seed)",
        ],
        "patches": applied,
        "traceability": "r9 -> r10 contains only Issue #559 A-F repairs + provenance updates; Evidence refs unchanged; package/block order unchanged except P07A/P15 consolidation already in r9 (unchanged here).",
    }
    r10["provenance"] = {
        "built_from": f"reader-editorial-authority-r9.json@{r10['parent_reader_sha256'][:12]} + Issue #559 bounded patches",
        "reproducible": "re-run this script; r9 bytes + explicit PATCHES only",
        "generator": "sources/SP-vision-multimodal-2026/publication/editorial/build_reader_editorial_authority_r10.py",
    }
    # Keep renderer binding but point to r10
    r10["renderer_binding"] = {
        "canonical_provenance_source": "checkpointed r1 bytes (integrity/provenance only, never reader wording)",
        "reader_wording_source": "this authority (reader-editorial-authority-r10.json) + accepted Evidence for bibliography/citation resolution + approved Architecture/Profile",
        "forbidden": "must not read restored r1 Draft Result prose as final reader wording; must not claim TeX identical to canonical Draft r9/r10",
    }
    OUT.write_text(json.dumps(r10, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} patches={len(applied)}")
    # Verify only expected blocks + decks changed
    r9_by = {(p['package_id'], b['block_id']): b['reader_text']
             for p in r9["reader_packages"] for b in p["ordered_blocks"]}
    r10_by = {(p['package_id'], b['block_id']): b['reader_text']
              for p in r10["reader_packages"] for b in p["ordered_blocks"]}
    changed = [(k) for k in r9_by if r9_by[k] != r10_by[k]]
    print(f"changed blocks: {sorted(changed)}")
    r9_deck = {p['package_id']: p['deck'] for p in r9["reader_packages"]}
    r10_deck = {p['package_id']: p['deck'] for p in r10["reader_packages"]}
    changed_decks = sorted([k for k in r9_deck if r9_deck[k] != r10_deck[k]])
    print(f"changed decks: {changed_decks}")
    assert len(changed) == 14, changed
    assert changed_decks == ["P10", "P11"], changed_decks
    assert len(applied) == 20, len(applied)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
