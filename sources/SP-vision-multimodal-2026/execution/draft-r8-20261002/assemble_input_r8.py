#!/usr/bin/env python3
"""Assemble TS-003 Draft r2 interactive input from rewritten r2 spec files."""
import json
import os
from datetime import datetime, timezone

REPO = "/home/eariver/git/japanese-generative-ai-survey"
SPECDIR = f"{REPO}/sources/SP-vision-multimodal-2026/execution/draft-r8-20261002/specs"
OUT = f"{REPO}/sources/SP-vision-multimodal-2026/execution/draft-r8-20261002/interactive-drafting-synthesis-input-r8.json"

PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B",
        "P08", "P09", "P10", "P11", "P12", "P13", "P14", "P15"]

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
runner = {
    "provider": "Muse",
    "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
    "invocation": ("TS-003 Draft r8 bidirectional terminology repair from approved Architecture r2 "
                   "(Human APPROVED r2, Sol Draft Review r1 REQUEST_CHANGES F1-F5): full-volume "
                   "prose rewrite, zero duplicate sentences, metaphor-substitution eliminated, "
                   "evaluator classes explicit, boundary reader surface repaired; "
                   "G01-G06 and 5 PARTIAL preserved semantically; no cross-task ranking; no new research"),
    "generated_at": now,
    "run_reference": "ts003-draft-r8-20261002",
}

packages = []
total = 0
for pid in PIDS:
    with open(f"{SPECDIR}/{pid}.json") as f:
        spec = json.load(f)
    assert spec["package_id"] == pid, pid
    assert set(spec) == {"package_id", "headline", "deck", "deck_discovery_ids", "blocks"}, (pid, set(spec))
    for b in spec["blocks"]:
        assert set(b) in ({"block_id", "block_type", "discovery_ids", "text"},
                          {"block_id", "block_type", "discovery_ids", "text", "ref_mode"}), (pid, set(b))
    n = len(spec["deck"]) + sum(len(b["text"]) for b in spec["blocks"])
    total += n
    packages.append(spec)
    print(pid, "chars:", n, "blocks:", len(spec["blocks"]))
print("TOTAL chars:", total)

doc = {
    "schema_version": "2.0-rc1",
    "issue_id": "SP-vision-multimodal-2026",
    "draft_version": "r8",
    "runner": runner,
    "packages": packages,
    "synthesis": {
        "profile_payload": {
            "branch_transition_synthesis": ("表現の学習と転移を起点に、検出の枠組み（提案・一点予測・集合予測）、密な構造化とプロンプト指示、文書の構造理解、系列としての視覚と自己教師あり学習、画像全体のアライメントから開かれた接地へ、個別学習済み部品の橋渡し、解像度・融合・時刻の統合、ハルシネーションと根拠利用の診断、オフライン長文脈とオンラインストリーミングの分離、画面操作の接地と状態管理、身体をもつ行動の界面、予測表現と生成的環境の四極へと系譜が分かれ、評価の契約ごとに収束の問いへ集まる。閉じた製品は能力・デプロイの文脈に留め、機構の根拠にはしない。"),
            "parallel_competing_relations": ("個別部品の組み立てと一体の事前学習、専門家と汎用モデル、密な注釈とウェブ規模の弱い教師信号、早期・後期・密な融合、凍結と共同学習、オフライン長文脈とオンライン状態保持、計画側の接地と一体の行動表現、潜在ダイナミクスと予測表現と生成的環境、ベンダー報告と独立評価が並行する競合関係にある。いずれも万能ではなく、条件・装置・予算・母集団で損得が変わる。"),
            "unresolved_lineage_questions": ("VLAの独立評価の不足、制御に使えるワールドモデルの評価の不在、同一条件での専門家・汎用モデル比較の不在、実デプロイの遅延・メモリ根拠の不足、最新ベンダー報告の独立再現の不足、SigLIP2引用の特定の弱さは残る。概要水準の5件は概要の範囲に留める。運転支援の参照は一次資料待ちであり、機構の根拠にはしない。"),
            "historical_attribution_boundaries": ("概要・断片水準の5件は概要の範囲に留め、語りで格上げしない。閉じた製品は能力・デプロイのみで機構推論しない。条件の異なる数値の横断順位づけはしない。ベンダー主張は帰属づきで引用し独立再現を待つ。要旨・断片の事実はその水準でのみ用いる。内部の作業用語は読者文に出さない。"),
        },
        "publication_payload": {},
    },
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("wrote:", OUT)
