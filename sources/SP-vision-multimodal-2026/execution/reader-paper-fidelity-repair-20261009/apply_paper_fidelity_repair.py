#!/usr/bin/env python3
"""Bounded paper-review technical-fidelity repair (Sol TS-003 PR-01/02/03).

Immutable basis: prior corrected staging
  sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009/main.tex
read read-only with commit-fixed SHA pin. Applies exactly the 4 Sol-authorized
exact replacements (PR-01 x1 on L86, PR-02 x1 + PR-03 x2 on L391) and writes
ONLY into the new edition-local staging directory:
  sources/SP-vision-multimodal-2026/execution/reader-paper-fidelity-repair-20261009/

Never modifies: prior staging, canonical publication artifacts, Draft
authority (fresh-124-r9), Evidence 124, Architecture r9, checkpoints, gates,
or shared Core v2. Never re-runs the canonical 9-occurrence reader repair.

Authorized scope (4 replacements, 2 lines):
  PR-01 L86 : DETR training-schedule conflation -> 300ep base + 3 days + 500ep comparison split
  PR-02 L391: 'POPEは投票型...' -> yes/no polling wording
  PR-03 L391: 'MMBenchは3000件超の日英設問...' -> EN/ZH wording
  PR-03 L391: '判定依存と英中の言語範囲...' -> dependence + bilingual-range wording

Usage:
  python3 apply_paper_fidelity_repair.py [--check-only]

Outputs (all inside STAGING):
  main.tex, references.bib (byte-identical copy of basis), before-after.json
"""

import argparse
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
BASIS_TEX = REPO / "sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009/main.tex"
BASIS_BIB = REPO / "sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009/references.bib"
STAGING = REPO / "sources/SP-vision-multimodal-2026/execution/reader-paper-fidelity-repair-20261009"

# Immutable repair basis pins (R02-01-final staged authority).
BASIS_TEX_SHA256 = "f09a808d1ed8ec7b18713e64dadafe6fbb0925d585df22881d0d27df37577342"
BASIS_BIB_SHA256 = "9c1e60fbefa4c2679f6a6cc465f803efc24f891ac215ef87782e4f636aeb3c1a"

# (rule_id, finding, old, new, expected_count)
RULES = [
    ("PR-01-DETR-L86", "PR-01",
     "小物体の5.5ポイント不足と300から500エポックに及ぶAdamW日程、16枚のV100で3日という訓練負担が論文自身の開かれた課題である。",
     "小物体の5.5ポイント不足と長い学習期間が、論文自身の挙げる課題である。AdamWを用いた基準設定は300エポックで、16枚のV100による学習に約3日を要する。Faster R-CNNとの比較には500エポックの長期設定を用いている。", 1),
    ("PR-02-POPE-L391", "PR-02",
     "POPEは投票型の設問で物体ハルシネーションを安定に測る範囲に属し、",
     "POPEは物体の有無をyes/no形式で問うポーリング方式により、物体ハルシネーションを安定的に評価し、", 1),
    ("PR-03-MMBENCH-L391a", "PR-03",
     "MMBenchは3000件超の日英設問を20能力軸で整え、",
     "MMBenchは3000件超の英語・中国語の選択式設問を20の能力軸で整え、", 1),
    ("PR-03-MMBENCH-L391b", "PR-03",
     "判定依存と英中の言語範囲が条件として残る。",
     "判定方法への依存と英語・中国語という二言語の評価範囲が条件として残る。", 1),
]

FORBIDDEN_AFTER = [
    "300から500エポックに及ぶAdamW日程",
    "POPEは投票型",
    "MMBenchは3000件超の日英設問",
    "判定依存と英中の言語範囲",
]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    tex = BASIS_TEX.read_text(encoding="utf-8")
    bib = BASIS_BIB.read_bytes()
    assert sha256(BASIS_TEX) == BASIS_TEX_SHA256, "basis main.tex pin mismatch"
    assert sha256(BASIS_BIB) == BASIS_BIB_SHA256, "basis references.bib pin mismatch"

    before_after = []
    total = 0
    for rule_id, finding, old, new, expected in RULES:
        got = tex.count(old)
        assert got == expected, (rule_id, expected, got)
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
    assert total == 4, total

    for frag in FORBIDDEN_AFTER:
        assert tex.count(frag) == 0, ("residual forbidden fragment", frag)

    # R02/R04/R05 non-regression (basis carried the closed repair forward).
    assert tex.count("exhibits") == 0
    assert tex.count("残差 reformulation") == 0
    assert tex.count("IDは受入時に修正済みである。") == 0
    assert tex.count("三次元持ち上げは本節の対象外として扱わず") == 0
    import re
    assert len(re.findall(r"(?<![\wぁ-んァ-ン一-鿿])cap(?![\w])", tex)) == 0
    assert tex.count("残差としての再定式化") == 2
    assert tex.count("三次元への持ち上げは本節の対象外とし") == 1
    assert tex.count("本節の対象外") == 4

    # PR presence.
    assert tex.count("AdamWを用いた基準設定は300エポックで") == 1
    assert tex.count("500エポックの長期設定を用いている") == 1
    assert tex.count("POPEは物体の有無をyes/no形式で問うポーリング方式により") == 1
    assert tex.count("MMBenchは3000件超の英語・中国語の選択式設問を20の能力軸で整え") == 1
    assert tex.count("判定方法への依存と英語・中国語という二言語の評価範囲が条件として残る") == 1

    if args.check_only:
        print(json.dumps({"rules": len(RULES), "occurrences": total,
                          "forbidden_residual": 0}, ensure_ascii=False, indent=1))
        return 0

    STAGING.mkdir(parents=True, exist_ok=True)
    (STAGING / "main.tex").write_text(tex, encoding="utf-8")
    (STAGING / "references.bib").write_bytes(bib)
    (STAGING / "before-after.json").write_text(
        json.dumps({
            "decision": "PAPER_REVIEW_TECHNICAL_FIDELITY_REPAIR",
            "blocking_scope": ["PR-01", "PR-02", "PR-03"],
            "prior_closed": ["R02", "R04", "R05"],
            "repair_basis": {
                "basis": "sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009/main.tex",
                "main_tex_sha256": BASIS_TEX_SHA256,
                "references_bib_sha256": BASIS_BIB_SHA256,
            },
            "rules": before_after,
            "total_occurrences": total,
            "outputs_confined_to": str(STAGING),
            "basis_untouched": True,
            "canonical_untouched": True,
        }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"staged_main_tex_sha256": sha256(STAGING / "main.tex"),
                      "staged_references_bib_sha256": sha256(STAGING / "references.bib"),
                      "total_occurrences": total}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
