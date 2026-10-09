#!/usr/bin/env python3
"""Bounded reader-only repair wrapper (Sol execution decision TS-003 R02/R04/R05).

Reads canonical VALIDATED_DRAFT bytes read-only, applies exactly the 9
Sol-authorized reader corrections, writes ONLY into the edition-local staging
directory. Never modifies canonical publication artifacts, Draft authority,
Evidence, Architecture, checkpoints, gates, or shared Core v2.

Authorized scope (9 occurrences, 7 lines):
  R05 P01 : '残差 reformulation' x2 -> '残差としての再定式化' (meaning preserved)
  R02 P04 : 'exhibits' x3 -> natural Japanese per context (3 distinct rules)
  R02 P04 : 'cap' x3 -> natural scope-limiting wording ('本節の対象外' family)
  R04 P07B: 'IDは受入時に修正済みである。' x1 -> deleted (mechanism/eval/source kept)

DUSt3R downstream linkage stays Survey/editorial synthesis; the existing
explicit disclaimer sentence in P04 is preserved byte-identically.

Usage:
  python3 apply_reader_repair_r02_r04_r05.py [--check-only]

Outputs (all inside STAGING):
  main.tex, references.bib (byte-identical copy), before-after.json
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
CANON_TEX = REPO / "surveys/special/vision-multimodal-2026/main.tex"
CANON_BIB = REPO / "surveys/special/vision-multimodal-2026/references.bib"
STAGING = REPO / "sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009"

# Canonical VALIDATED_DRAFT base pins (fresh-124-r9 validation, exact 39pp PDF).
CANON_TEX_SHA256 = "edcf8ef982a63ac9dc65881aae1963a7daf64fa7fc16de67fbf97825cba090cb"
CANON_BIB_SHA256 = "9c1e60fbefa4c2679f6a6cc465f803efc24f891ac215ef87782e4f636aeb3c1a"

# (rule_id, finding, old, new, expected_count)
RULES = [
    ("R05-P01-1", "R05", "残差 reformulation が超深度の最適化を切り開いた",
     "残差としての再定式化が超深度の最適化を切り開いた", 1),
    ("R05-P01-2", "R05", "学ぶ残差 reformulation へ切り替えた",
     "学ぶ残差としての再定式化へ切り替えた", 1),
    ("R02-P04-exhibits-1", "R02", "頑健さ測定の exhibits として示されている",
     "頑健さ測定の評価事例として示されている", 1),
    ("R02-P04-exhibits-2", "R02", "対応づけ自体の表現化を示す exhibits である",
     "対応づけ自体の表現化を示す技術的な比較例である", 1),
    ("R02-P04-exhibits-3", "R02", "後の融合や身体系への受け渡し exhibits になる",
     "後の融合や身体系への受け渡しを考える編集上の比較例になる", 1),
    ("R02-P04-cap-1", "R02", "後継の追加は新しい契約を生まないものとして cap の外に置く。",
     "後継の追加は新しい契約を生まないものとして本節の対象外に置く。", 2),
    ("R02-P04-cap-2", "R02", "三次元持ち上げは cap により扱わず",
     "三次元への持ち上げは本節の対象外とし", 1),
    ("R04-P07B-1", "R04", "範囲として記録する。IDは受入時に修正済みである。",
     "範囲として記録する。", 1),
]

FORBIDDEN_AFTER = ["exhibits", "残差 reformulation", "IDは受入時に修正済みである。",
                   " cap ", " cap の", "cap により", "として cap "]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    tex = CANON_TEX.read_text(encoding="utf-8")
    bib = CANON_BIB.read_bytes()
    assert sha256(CANON_TEX) == CANON_TEX_SHA256, "canonical main.tex pin mismatch"
    assert sha256(CANON_BIB) == CANON_BIB_SHA256, "canonical references.bib pin mismatch"

    before_after = []
    total = 0
    for rule_id, finding, old, new, expected in RULES:
        got = tex.count(old)
        assert got == expected, (rule_id, expected, got)
        # capture one context window per rule for the record
        idx = tex.find(old)
        ctx_before = tex[max(0, idx - 60):idx + len(old) + 60].replace("\n", " / ")
        tex = tex.replace(old, new)
        idx2 = tex.find(new)
        ctx_after = tex[max(0, idx2 - 60):idx2 + len(new) + 60].replace("\n", " / ")
        total += got
        before_after.append({
            "rule_id": rule_id,
            "finding": finding,
            "occurrences": got,
            "before": old,
            "after": new,
            "context_before": ctx_before,
            "context_after": ctx_after,
        })
    assert total == 9, total

    for frag in FORBIDDEN_AFTER:
        assert tex.count(frag) == 0, ("residual forbidden fragment", frag)

    # word-boundary sweep for stray 'cap' tokens outside known-safe words
    import re
    strays = [m.start() for m in re.finditer(r"(?<![\wぁ-んァ-ン一-鿿])cap(?![\w])", tex)]
    assert strays == [], strays

    assert tex.count("残差としての再定式化") == 2
    # Canonical base already carries 1x '本節の対象外'; repair adds exactly 3.
    assert tex.count("本節の対象外") == 4

    if args.check_only:
        print(json.dumps({"rules": len(RULES), "occurrences": total,
                          "forbidden_residual": 0}, ensure_ascii=False, indent=1))
        return 0

    STAGING.mkdir(parents=True, exist_ok=True)
    (STAGING / "main.tex").write_text(tex, encoding="utf-8")
    (STAGING / "references.bib").write_bytes(bib)
    (STAGING / "before-after.json").write_text(
        json.dumps({
            "decision": "READER_PUBLICATION_REVISION_REQUIRED",
            "blocking_scope": ["R02", "R04", "R05"],
            "canonical_base": {
                "main_tex_sha256": CANON_TEX_SHA256,
                "references_bib_sha256": CANON_BIB_SHA256,
            },
            "rules": before_after,
            "total_occurrences": total,
            "outputs_confined_to": str(STAGING),
            "canonical_untouched": True,
        }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"staged_main_tex_sha256": sha256(STAGING / "main.tex"),
                      "staged_references_bib_sha256": sha256(STAGING / "references.bib"),
                      "total_occurrences": total}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
