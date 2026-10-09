#!/usr/bin/env python3
"""TS-003 Draft r8 driver: canonical per-package derivation + F5 boundary repair.

Documented §16 limitation: the canonical interactive runner gates on
ARCHITECTURE_ESTABLISHED, but this repair runs at DRAFT_COMPLETE (no rollback
faked). This driver performs the runner's exact per-package steps using the same
canonical Core functions (derive_draft_package, runner _draft_result,
validate_draft_result, build_synthesis_input, validate_synthesis_result) with an
upstream resolver identical to the runner's except that it admits DRAFT_COMPLETE
with an approved Architecture Review. Every validation below is canonical Core.
"""
import copy
import json
import shutil
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
sys.path.insert(0, str(REPO))

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
from scripts import run_drafting_synthesis_v2_interactive as irunner

SRC = REPO / "sources/SP-vision-multimodal-2026"
STATE_PATH = SRC / "production-state.json"
R8DIR = SRC / "execution/draft-r8-20261002"
INPUT_PATH = R8DIR / "interactive-drafting-synthesis-input-r8.json"

# --- F5 boundary repair table: exact Architecture boundary string -> (handling, ) ---
# EXPLICIT boundaries get concise Japanese reader text (one block per package);
# all others RESPECTED_BY_OMISSION. Sets must exactly partition each package.
JP = {
"P01": ("本節の転移の主張はImageNetという一つのデータの範囲に留まる。別課題への転換は後継の記録が担う。検出の伸びは2015年当時の条件の上での報告であり、現在の基準での優劣ではない。LeNetの機構の細部は抄録水準に留める。",
 ["Single-dataset (ImageNet) scope; transfer claims require successor sources (ResNet record).",
  "Detection gains use Faster R-CNN baselines of 2015 vintage.",
  "Full-text body behind paywall; mechanism detail stays at abstract level by D01 cap design."]),
"P02": ("R-CNNの多段処理の重さは後の課題として残され、後の基準では遅い仕組みである。YOLOの精度は当時の最上位に届かないと論文自身が認めており、後の各版は別製品として扱う。版を外した主張はしない。端末搭載の負担は動機の記録であり、確かめた成果ではない。",
 ["Multi-stage pipeline speed addressed only as future work; R-CNN itself is slow by later standards.",
  "Accuracy lags state-of-the-art systems of its generation by the paper's own account; later YOLO versions are distinct products.",
  "YOLO product-line confusion risk; version-bound claims only; edge-deployment burden noted as motivation, not established result."]),
"P03": ("輪郭の粗さは後の基準での留保であり、磨き上げは後継に譲る。Mask R-CNNはボックスを前提とする作りのため、ボックスに依存しない密な予測は別の記録が担う。U-Netの話は医療画像の範囲に留まり、一般の情景への転移は語らない。",
 ["Coarse boundaries by later standards; refinement needs successor sources.",
  "Box-dependent by construction; box-free dense pole needs FCN/SAM-side sources.",
  "Biomedical-image domain; general-scene transfer requires other sources."]),
"P04": ("深さは相対の範囲に留まり、尺度つきの主張はしない。姿勢は2次元の範囲に留まり、3次元への持ち上げは扱わない。いずれも2019年当時の条件の上での記録である。",
 ["Relative-depth scope; metric-depth claims need other sources; 2019-vintage baselines.",
  "2D pose scope; 3D lifting excluded by cap; 2019-vintage runtime hardware baseline."]),
"P05": ("NougatとGOTの評価は自前の試験の範囲に留まる。Nougatの繰り返し・言語・構造の偏りは論文自身の申告であり、GOTと汎用モデルの同一条件での直接対決は見つかっていないため優劣は決めない。検索モデルの順位は著者測定のプレプリント時点の主張であり、独立した再現はない。図表の数値は緩めた正確さの許容と組で読む。",
 ["Own-suite evaluation only; repetition + language + structure biases paper-stated.",
  "Own-suite evaluation; same-protocol generalist head-to-head not found (gap G03 preserved).",
  "Author-measured leaderboard; preprint status confirmed at intake; independent reproduction pending (G05).",
  "Relaxed-accuracy tolerance semantics must travel with scores; synthetic predecessors are context."]),
"P06": ("ViTの到達は大規模な事前学習への依存の上にあり、DeiTは学習手順の改善と蒸留でこの依存を緩和する。SigLIPの損失の仕組みの記述は抄録頁の水準に留まり、正確な引用対応は未確定のまま残る。",
 ["Large-scale pre-training dependence (DeiT qualifies); 100B-parameter era context noted in intro.",
  "Abs-page-level consumption for the loss mechanism (HTML extraction thin); SigLIP2 citation unbound (G06).",
  "G06 SigLIP2 citation binding: SigLIP2 exact citation unbound; G06 gap preserved."]),
"P07A": ("VQAの素の正確度は、学習分割の混入と言葉の癖で当たる問いの混入のため、そのまま読めたことにはならない。学習分割と答えの取り出し規則と組で読む。画像全体の照合は語の並びや掛かりの読みを落とし、この限界が次の接地の節への動機になる。",
 ["VQA-v2 training contamination and prior-exploitability qualify naive accuracy readings; bind split + extraction rule.",
  "Bag-of-words alignment limits; efficiency/scale critiques need successor sources (SigLIP record)."]),
"P07B": ("ウェブ由来の教師モデルやデータを使う以上、未見の言い方はラベル空間と学習分割の定義に縛られる。機械の空間での未見と人手の空間での未見は別物であり、数値はその定義と組で読む。レア分割の数値も分割の取り方の下での記録である。ファインチューニング後の言い分けとゼロショットの言い分けは同じ契約の別の手順であり、新しい節ではない。",
 ["Web-data dependence; label-space qualification travels with every number.",
  "Rare-split protocol must be bound per use; web-pretraining adjacency affects 'unseen' readings.",
  "Fine-tuned vs zero-shot REC is a protocol difference, not a new node; game-collected expressions carry collection bias.",
  "Fine-tuned REC vs zero-shot REC is a protocol difference, not a new node."]),
"P08": ("Flamingoの学習データは非公開の体制であり、閉じた条件の記録として読む。Frozenの記録は概念実証の範囲に留まり、前駆としての位置づけを超えない。",
 ["Closed training-data regime; resampling predecessor role noted for D09, not duplicated.",
  "Proof-of-concept scope per the paper's own discussion; precursor depth only."]),
"P09": ("ベンチマークの主張はベンダー測定であり、トークンや設定の数値は設定に結びつく読みに留め、独立した再現は今後の課題として残す。234msは理論上のコールドスタートであり、実測のデプロイ値ではない。Whisperの話は音声認識の範囲に留まり、音全般の主張はしない。BEATsの分類の強さは分類の範囲の記録であり、融合の振る舞いの根拠にはしない。",
 ["All benchmark claims vendor-measured (G05); token/config figures config-bound (CV2-DM-020); independent reproduction pending; repo commit binding at later stages.",
  "No-degradation and leaderboard claims vendor-measured (G05); 234ms is theoretical cold-start; generation-side excluded by boundary.",
  "Speech-domain scope; general-audio needs BEATs-side sources.",
  "Classification-benchmark scope; fusion behavior needs omni-side sources."]),
"P10": ("合成点をもって賢さ一般を語らない。使うたびに補助手順の切り分けと汚染の不透明さを添える。制御ペアの診断は手作りの小さな規模であり、厳しい指標の診断として読む。投票は投票の範囲に留まり、自由な記述の忠実さは制御ペアの道具が担う。判定への依存は点と組で読み、英中の範囲を超えない。",
 ["Composite score must not stand as general intelligence; scaffold ablations and contamination opacity (closed models) required per use.",
  "Handcrafted small scale; pair-accuracy is a strict metric — report as diagnostic, not leaderboard.",
  "Polling scope only; open-ended faithfulness needs control-pair instruments (HallusionBench).",
  "Judge/choice-extraction dependence (GPT-4) must travel with every score; bilingual scope is EN/CN only."]),
"P11": ("多くのモデルはオフライン変換で測られており、真のオンラインの点は実時間の仕組み側の記録が担う。遅延とメモリの数値は著者の報告に留まり、それを超えるデプロイの数値は未確定として残す。空間知能の評価の読みは要旨の深さに留まり、偏りを除いた分析は後に譲る。",
 ["Most models evaluated via offline conversion; true online-system scores need Flash-VStream-side sources.",
  "Author-reported latency/VRAM; deployment figures beyond that are G04 gap.",
  "PARTIAL: paper body at abstract depth (not full-paper read); debiased-subset analysis deferred."]),
"P12": ("OSWorldの記録は短い射程に留まり、長い作業の結論は2.0側の記録が担う。数値はモデルと設定と道具と手順数と版に結びつけて読む。",
 ["Short-horizon scope; long-horizon thesis needs 2.0-side sources.",
  "Author-measured model results; strictest binding in volume required per use (model+thinking+tool+steps+release)."]),
"P13": ("独立した評価の指標の乏しさは残り、オープンウェイトがあっても独立に測られたことにはならない。仕組みの中身や遅延や価格やトークンの事実は公開されておらず、書かれていないものは補わない。到達点の記録はモデルカードの範囲に留まり、日付と結びつけて読む。",
 ["G01 gap preserved; fine-tuning-efficiency claims are paper-reported.",
  "No mechanism disclosure; no latency/price/token facts published.",
  "Card-scoped eval only; OOD/whole-body outside stated scope; card may update (bind date)."]),
"P14": ("Genie 3は能力と運用の到達点としてだけ読み、ベンダーが示す五つの限りと組で読む。仕組みは公開されておらず、整合性やエージェント学習の主張はベンダーの言い分であり、ダイナミクス利用の独立した評価は結びついていない。潜在ダイナミクスの記録は強化学習の指標の範囲に留まり、見栄えの結論は盛らない。運転支援の参照は一次資料待ちであり、機構の根拠にはしない。",
 ["Genie 3 capability-capped with 5 stated limits; Waymo pointer pending primary source",
  "RL-benchmark scope; visual-fidelity readings are out of contract.",
  "Architecture undisclosed; consistency/SIMA claims vendor-stated; no independent dynamics-use eval (G02)."]),
"P15": ("合成点をもって賢さ一般を語らず、使うたびに補助手順の切り分けと汚染の不透明さを添える。投票で測ったことを自由な記述の忠実さとして語らず、判定を借りた分は借りた分として残す。英中の範囲を超えず、版と日付と測り手を外さない。ベンダーが測った値は作り手の言い分として受け取り、独立の根拠と分け、変わりうる頁の断定を動かない事実にしない。ダイナミクス利用の独立した評価の不在など、測られていないことは語らず、収束の断定は出さない。",
 ["Composite score must not stand as general intelligence; scaffold ablations and contamination opacity (closed models) required per use.",
  "Polling scope only; open-ended faithfulness needs control-pair instruments (HallusionBench).",
  "Judge/choice-extraction dependence (GPT-4) must travel with every score; bilingual scope is EN/CN only.",
  "Version-bind at Evidence (v3); commercial-model numbers author-measured.",
  "No mechanism disclosure; scores vendor-measured; card content may drift (bind date).",
  "Card-scoped eval only; OOD/whole-body outside stated scope; card may update (bind date).",
  "Architecture undisclosed; consistency/SIMA claims vendor-stated; no independent dynamics-use eval (G02).",
  "Author-benchmarked model scores; private-set details undisclosed by design."]),
}


def upstream(root, state_path):
    """Runner _upstream with lifecycle gate extended to DRAFT_COMPLETE (documented §16)."""
    state = core.load_json(state_path)
    if state.get("lifecycle_state") != "DRAFT_COMPLETE":
        raise ValueError("r2 driver requires DRAFT_COMPLETE State")
    if state.get("human_gates", {}).get("architecture_review") != "approved":
        raise ValueError("r2 driver requires approved Architecture Review")
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    errs = agent.validate_agent_state(root, cfg, state)
    if errs:
        raise ValueError("Production State invalid: " + "; ".join(errs))
    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = root / profile["paths"]["source_root"]
    accepted = core.load_json(source_root / "discovery/discovery-accepted-v2.json")
    discovery_path = (root / accepted["discovery_path"]).resolve()
    matrix_path = source_root / "candidate-matrix-v2.json"
    matrix = core.load_json(matrix_path)
    active = agent.resolve_active_evidence_views(root, cfg, state)
    evidence_path, views_path = active["evidence_path"], active["views_path"]
    if matrix.get("basis", {}).get("evidence_acceptance_sha256") != core.sha256_file(evidence_path):
        raise ValueError("Candidate Matrix does not bind checkpoint-bound Evidence acceptance")
    if matrix.get("basis", {}).get("edition_views_acceptance_sha256") != core.sha256_file(views_path):
        raise ValueError("Candidate Matrix does not bind checkpoint-bound Edition Views acceptance")
    approval_ref = state.get("human_gate_provenance", {}).get("architecture_review")
    approval_path = root / approval_ref["path"]
    attention = core.load_json(source_root / "architecture-review-attention-v2.json")
    screening_path = (root / attention["basis"]["screening_acceptance_path"]).resolve()
    return {
        "profile": profile_path, "source_root": source_root, "discovery": discovery_path,
        "screening": screening_path, "evidence": evidence_path, "views": views_path,
        "ledger": source_root / "materiality-ledger-v2.json",
        "completeness": source_root / "profile-completeness-v2.json",
        "matrix": matrix_path, "selection": source_root / "candidate-selection-v2.json",
        "architecture": source_root / "architecture-v2.json",
        "review": source_root / "architecture-review-summary-v2.json",
        "approval": approval_path,
    }


def main() -> int:
    root = REPO
    data = core.load_json(INPUT_PATH)
    up = upstream(root, STATE_PATH)
    state = core.load_json(STATE_PATH)
    assert data["schema_version"] == "2.0-rc1" and data["issue_id"] == state["issue_id"]
    assert set(data) == {"schema_version", "issue_id", "draft_version", "runner", "packages", "synthesis"}
    assert data["draft_version"] == "r8"
    plan = core.load_json(up["architecture"])
    specs = data["packages"]
    assert {r["package_id"] for r in specs} == {r["package_id"] for r in plan["packages"]}
    spec_by_id = {r["package_id"]: r for r in specs}
    draft_root = up["source_root"] / "draft/v2"
    # State validates only while r1 bytes are present (checkpoint-bound), but
    # derivation must not overwrite them in place. Derive into staging while
    # r1 keeps the state valid, then atomically swap. r1 bytes are preserved
    # in snapshot-r1/ + git regardless.
    staging_root = up["source_root"] / "draft/v2-r8-staging"
    if staging_root.exists():
        shutil.rmtree(staging_root)
    pairs, outputs = [], []
    implementation_sha = core.repository_commit_sha(root)
    with runtime_tool.current_stage_basis_override():
        for plan_row in sorted(plan["packages"], key=lambda r: (r["drafting_order"], r["package_id"])):
            pid = plan_row["package_id"]
            spec = spec_by_id[pid]
            assert set(spec) == {"package_id", "headline", "deck", "deck_discovery_ids", "blocks"}, pid
            package = drafting.derive_draft_package(
                root, up["profile"], up["discovery"], up["screening"], up["evidence"], up["views"],
                up["ledger"], up["completeness"], up["matrix"], up["selection"],
                up["architecture"], up["review"], up["approval"], pid, implementation_sha)
            package_dir = staging_root / "packages" / pid
            package_dir.mkdir(parents=True)
            package_path = package_dir / "draft-package.json"
            result_path = package_dir / "draft-result.json"
            core.write_json(package_path, package)
            result = irunner._draft_result(root, package_path, package, spec, data["runner"], "r8")
            errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
            if errors:
                raise SystemExit(f"{pid} Draft Result invalid: " + "; ".join(errors))
            core.write_json(result_path, result)
            pairs.append((package_path, result_path))
            outputs.append(pid)
    print("packages derived + runner-validated:", outputs)
    # F5 boundary repair
    from scripts import survey_draft_profile_v2 as draft_profile
    for package_path, result_path in pairs:
        package = core.load_json(package_path)
        result = core.load_json(result_path)
        pid = package["package_id"]
        jp_text, explicit = JP[pid]
        assert set(explicit) <= set(package["package"]["boundaries"]), pid
        assert len(set(explicit)) == len(explicit), pid
        assert len(explicit) >= 1, pid
        # find runner boundary block, replace text only (refs/attribution preserved)
        bblocks = [b for b in result["blocks"] if b["block_type"] == "CLAIM_BOUNDARY"]
        assert len(bblocks) == 1, pid
        bblocks[0]["text"] = "この節の読解上の境界: " + jp_text
        new_disp = []
        for row in result["boundary_dispositions"]:
            if row["boundary"] in explicit:
                new_disp.append({"boundary": row["boundary"], "handling": "EXPLICITLY_STATED",
                                 "block_ids": [bblocks[0]["block_id"]],
                                 "rationale": "Reader-facing limitation; concise Japanese limitation text carries it."})
            else:
                new_disp.append({"boundary": row["boundary"], "handling": "RESPECTED_BY_OMISSION",
                                 "block_ids": [],
                                 "rationale": "Internal drafting guard; omission of the unsupported claim suffices."})
        result["boundary_dispositions"] = new_disp
        result["status"] = "REVISED"
        errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
        if errors:
            raise SystemExit(f"{pid} post-repair invalid: " + "; ".join(errors))
        errors = draft_profile.validate_extension_propagation(result, package)
        if errors:
            raise SystemExit(f"{pid} extension propagation invalid: " + "; ".join(errors))
        core.write_json(result_path, result)
    print("F5 boundary repair applied + re-validated (status REVISED)")
    # synthesis rebuild
    with runtime_tool.current_stage_basis_override():
        synthesis_input = drafting.build_synthesis_input(
            root, up["profile"], up["architecture"], up["review"], up["approval"], pairs)
    synthesis_input_path = staging_root / "profile-synthesis-input.json"
    synthesis_result_path = staging_root / "profile-synthesis-result.json"
    core.write_json(synthesis_input_path, synthesis_input)
    syn = data["synthesis"]
    assert set(syn) == {"profile_payload", "publication_payload"}
    synthesis_result = {
        "schema_version": "2.0-rc1", "issue_id": state["issue_id"],
        "research_profile": state["research_profile"], "publication_profile": state["publication_profile"],
        "synthesis_version": "v1.0", "status": "REVISED",
        "basis": {"synthesis_input_sha256": core.sha256_file(synthesis_input_path),
                  "prompt_id": "profile-synthesis-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.SYNTHESIS_PROMPT)},
        "runner": data["runner"], "profile_payload": syn["profile_payload"],
        "publication_payload": syn["publication_payload"],
    }
    errors = drafting.validate_synthesis_result(synthesis_result, synthesis_input_path, root / drafting.SYNTHESIS_PROMPT)
    if errors:
        raise SystemExit("Profile Synthesis Result invalid: " + "; ".join(errors))
    core.write_json(synthesis_result_path, synthesis_result)
    archive = staging_root / "interactive-drafting-synthesis-input.json"
    core.write_json(archive, data)
    print("synthesis rebuilt + validated (status REVISED)")
    # Atomic swap: staging becomes canonical draft/v2. r1 lives on in snapshot-r1/ + git.
    # Note: whole-state re-validation is impossible after the swap without a
    # rollback (documented §16 limitation); every per-artifact canonical
    # validator above has passed on the exact bytes being installed.
    shutil.rmtree(draft_root)
    staging_root.rename(draft_root)
    print("swapped staging -> draft/v2")
    print(json.dumps({"packages": outputs, "draft_version": "r8"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
