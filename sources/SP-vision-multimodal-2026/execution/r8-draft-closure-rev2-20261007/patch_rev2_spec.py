#!/usr/bin/env python3
"""Patch rev2 spec with remaining closure fixes. Fully idempotent: every edit
applies only when its old-form is present and its new-form absent.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SPEC = ROOT / "sources/SP-vision-multimodal-2026/execution/r8-draft-closure-rev2-20261007/compact-input-fresh-121-r8-rev2.json"

NEW_P12_B6 = ("OSWorld 2.0は108件の長時間ワークフローから成り、中央値で1.6人間時間の作業を扱う到達点の事例である。流れの中の対話、動的環境、複数情報源にまたがる推論、暗黙状態の推定、視覚と空間の精密さを課題現象とし、真正な成果物と状態を持つ利用者像と安全性報告を備える。論文著者測定では、Claude Opus 4.7を用いた最大思考・単一行動設定で108課題平均318.4回のツール呼び出しとなり、OSWorld 1.0の約30回と桁が異なる。500段階バッチ構成ではClaude Opus 4.8の最大思考で二値20.6%・部分54.8%・481.8回と著者測定で示される。いずれもモデル・思考・ツール・手順・段数・公開条件を結びつけて読む。条件結合の厳密さが本巻で最も強い分野であり、名称と設定と手順を明示して読む。安全性報告は評価の付随情報として扱う。")

NEW_3184_B04 = "OSWorld 2.0はClaude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回のツール呼び出しという状態管理費用を示し、OSWorld 1.0の約30回と桁が違う。"
OLD_3184_B04 = "OSWorld 2.0は単一行動設定で平均318.4回のツール呼び出しという状態管理費用を示し、OSWorld 1.0の約30回と桁が違う."
NEW_3184_B09 = "Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回ツール呼び出しがOSWorld 1.0約30回と桁違いの状態管理費用を示す。"
OLD_3184_B09 = "平均318.4回ツール呼び出しがOSWorld 1.0約30回と桁違いの状態管理費用を示す。"


def main() -> int:
    d = json.loads(SPEC.read_text(encoding="utf-8"))

    def get(pid, bid):
        p = next(x for x in d["packages"] if x["package_id"] == pid)
        return p, next(x for x in p["blocks"] if x.get("block_id") == bid)

    _, b6 = get("P12", "P12-B6")
    if "Claude Opus 4.7を用いた最大思考" not in b6["text"]:
        b6["text"] = NEW_P12_B6

    _, b04 = get("P15", "P15-B04")
    if OLD_3184_B04 in b04["text"]:
        b04["text"] = b04["text"].replace(OLD_3184_B04, NEW_3184_B04)

    _, b09 = get("P15", "P15-B09")
    if OLD_3184_B09 in b09["text"]:
        b09["text"] = b09["text"].replace(OLD_3184_B09, NEW_3184_B09)

    _, b11 = get("P09", "p09-b11")
    parts = [s for s in b11["text"].split("。") if s]
    dropped = [s for s in parts if "残された検証課題" in s or "3.8 Flash行の確定" in s]
    assert len(dropped) <= 1, [s[:60] for s in dropped]
    if dropped:
        b11["text"] = "。".join(s for s in parts if s not in dropped) + "。"

    _, b10 = get("P09", "p09-b10")
    old3 = "ファイル水準の提供範囲は未確認であり、本節の主張は公開リポジトリで確認できる範囲に留まる。"
    if old3 in b10["text"]:
        b10["text"] = b10["text"].replace(
            old3, "公開範囲を超える提供内容までは確認できないため、本節の主張は公開リポジトリで確認できる範囲に留まる。")
    p09 = next(x for x in d["packages"] if x["package_id"] == "P09")
    if "第三者文書" in b10["text"]:
        b10["text"] = b10["text"].replace("第三者文書", "第三者データ")
    if "第三者文書" in (p09.get("boundaries_text") or ""):
        p09["boundaries_text"] = p09["boundaries_text"].replace("第三者文書", "第三者データ")

    SPEC.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blob = SPEC.read_text(encoding="utf-8")
    must_gone = ["残された検証課題", "3.8 Flash行の確定", "ファイル水準", "第三者文書",
                 "単一行動設定で平均318.4回"]
    bad = [s for s in must_gone if s in blob]
    assert not bad, bad
    bare = [m.group(0) for m in re.finditer(r"(?<!108課題)平均318\.4回ツール呼び出しがOSWorld 1\.0約30回と桁違い", blob)]
    assert not bare, bare
    must_have = ["Claude Opus 4.7を用いた最大思考・単一行動設定で108課題平均318.4回",
                 "Claude Opus 4.8の最大思考で二値20.6%・部分54.8%・481.8回",
                 "Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回",
                 "公開範囲を超える提供内容までは確認できない",
                 "第三者データの許諾文"]
    missing = [s for s in must_have if s not in blob]
    assert not missing, missing
    print("rev2 spec patched + verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
