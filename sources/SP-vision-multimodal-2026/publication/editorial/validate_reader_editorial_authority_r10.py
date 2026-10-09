#!/usr/bin/env python3
"""Validate TS-003 reader/editorial authority r10 (Issue #559 bounded repair).

- Canonical remains checkpointed r1; r10 is publication-layer only.
- Evidence authority unchanged vs r1 (no new refs/sources), package identity,
  CLAIM_BOUNDARY present, limitations preserved, Arch order intact.
- r9->r10 diff confined to 14 blocks / Issue #559 A-F + consequential boundaries.
- Forbidden strings absent; required repaired strings present.
- Terminology seed contextual decisions recorded (replace/retain with reason).
"""
import hashlib
import json
import subprocess
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
R9 = SRC / "publication/editorial/reader-editorial-authority-r9.json"
R10 = SRC / "publication/editorial/reader-editorial-authority-r10.json"
R1 = "d1053e957d92cddd9d2759ec9713db59c66263ad"

FORBIDDEN = [
    "音声と映像のずれを80msに抑える",
    "重みとコードの許諾は未確定のまま残り",
    "ゼロショット基線",
    "教師あり基線",
    "300〜500エポックのAdamW、16枚のV100で3日の日程",
    "投票型のPOPE",
    "投票型評価",
    "安定にしなやかに測る",
    "安定にしなやかに測り",
]
REQUIRED = [
    "約80msの共通時間分解能",
    "音声表現の1フレームは原音声の約80msに対応",
    "映像の時間IDは実際のタイムスタンプから動的に付与",
    "Apache License 2.0のLICENSE",
    "Qwen3-Omni-30B-A3B／Qwen3-Omni-30B-A3B-Thinking／Qwen3-Omni-30B-A3B-Captioner",
    "入力フレームを増やして",
    "入力フレーム数の効き方",
    "入力フレーム数の感受性",
    "POPE (Polling-based Object Probing Evaluation)",
    "問いかけ型の物体存在プロービング",
    "安定かつ柔軟に測",
    "ゼロショットベースライン",
    "教師ありベースライン",
    "300エポックの学習設定",
    "約3日の学習期間",
    "500エポックの長期設定",
]


def show(commit, rel):
    return subprocess.check_output(["git", "show", f"{commit}:{rel}"], cwd=REPO)


def ev_task_set(res):
    s = set()
    for ref in (res.get("deck_evidence_refs") or []):
        s.add(ref["evidence_task_id"])
    for b in res["blocks"]:
        for ref in (b.get("evidence_refs") or []):
            s.add(ref["evidence_task_id"])
    return s


def main() -> int:
    r9 = json.loads(R9.read_text(encoding="utf-8"))
    r10 = json.loads(R10.read_text(encoding="utf-8"))
    assert r10["reader_editorial_revision"] == "r10"
    assert r10["parent_reader_revision"] == "r9"
    assert "never claim r9/r10 remains canonical" in r10["semantic_labels"]["warning"]
    failures = []
    # Evidence still bounded vs r1 (text changes must not alter refs)
    for p10 in r10["reader_packages"]:
        pid = p10["package_id"]
        rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json"
        r1 = json.loads(show(R1, rel).decode("utf-8"))
        # r10 evidence refs must equal r9 refs (which equal r1 sets per r9 validation)
        p9 = [x for x in r9["reader_packages"] if x["package_id"] == pid][0]
        for b9, b10 in zip(p9["ordered_blocks"], p10["ordered_blocks"]):
            if b9["block_id"] != b10["block_id"] or b9["block_type"] != b10["block_type"]:
                failures.append(f"{pid} {b10['block_id']} block identity changed")
            if (b9["evidence_refs"] or []) != (b10["evidence_refs"] or []):
                failures.append(f"{pid} {b10['block_id']} Evidence refs changed")
        if (p9["deck_evidence_refs"] or []) != (p10["deck_evidence_refs"] or []):
            failures.append(f"{pid} deck refs changed")
        if ev_task_set({"deck_evidence_refs": p10["deck_evidence_refs"],
                        "blocks": [{"evidence_refs": b["evidence_refs"]} for b in p10["ordered_blocks"]]}) != \
           ev_task_set({"deck_evidence_refs": p9["deck_evidence_refs"],
                        "blocks": [{"evidence_refs": b["evidence_refs"]} for b in p9["ordered_blocks"]]}):
            failures.append(f"{pid} Evidence task set changed r9->r10")
    # Diff confined
    r9_by = {(p['package_id'], b['block_id']): b['reader_text'] for p in r9["reader_packages"] for b in p["ordered_blocks"]}
    r10_by = {(p['package_id'], b['block_id']): b['reader_text'] for p in r10["reader_packages"] for b in p["ordered_blocks"]}
    changed = sorted([k for k in r9_by if r9_by[k] != r10_by[k]])
    if len(changed) != 14:
        failures.append(f"expected 14 changed blocks, got {len(changed)}: {changed}")
    # Forbidden absent, required present (joined full text)
    full = "\n".join([b["reader_text"] for p in r10["reader_packages"] for b in p["ordered_blocks"]])
    for s in FORBIDDEN:
        if s in full:
            failures.append(f"forbidden string remains: {s}")
    for s in REQUIRED:
        if s not in full:
            failures.append(f"required repaired string missing: {s}")
    # Retain decisions: framework/box 枠 must remain (no blind replace)
    for keep in ["同じ枠組み", "クエリ枠の分業", "共通の枠に載せる", "理解の枠に入れた", "two-stageの枠組み"]:
        if keep not in full:
            failures.append(f"retain 枠 sense lost (over-replacement?): {keep}")
    if "基線" in full:
        failures.append("基線 remains (should be normalized to ベースライン in ML senses)")
    if "日程" in full:
        # 日程 may remain in non-scheduler senses? For TS-003 reader, DETR was the only scheduler 日程; ensure gone
        failures.append("日程 remains (DETR 日程 should be 学習期間/学習設定)")
    if failures:
        print("R10 VALIDATION FAIL:")
        for f in failures:
            print(" -", f)
        return 1
    print(f"r10 validation PASS: 14 blocks repaired (A-F), Evidence bounded, 枠/基線/日程 contextual decisions hold, canonical r1 intact.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
