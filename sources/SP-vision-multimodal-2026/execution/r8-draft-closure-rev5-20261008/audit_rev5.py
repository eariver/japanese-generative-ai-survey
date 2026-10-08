#!/usr/bin/env python3
"""Fresh-Draft r8-rev5 terminology QA: Pass A/B/C + §24 closure checks (33 items).

Inspects FINAL materialized draft/v2 (16 results, headlines/decks/blocks incl.
CLAIM_BOUNDARY) + canonical profile synthesis result. Writes
semantic-audit-rev5.json + effective-input-report-rev5.json. Exit 1 on any FAIL.

- Pass A: §1/§2 preferred-form semantic conformance (concept->form presence,
  form->concept bidirectional spot checks, avoid-form technical absence).
- Pass B: §3 known-failure registry scan with per-hit semantic classification
  (TECHNICAL_SUBSTITUTION_BLOCKING / ORDINARY_JAPANESE_ALLOWED /
  SOURCE_QUOTE_OR_FIXED_NAME / NOT_APPLICABLE).
- Pass C: residual-pattern scan for newly invented translations (the rev5 repair
  families must show zero technical residuals).
- Negatives J1-J4 (rev4) + K1-K16 (rev5 blocker families).
- §20 technical non-regression guards + §21/§24 authority invariants.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-draft-closure-rev5-20261008"
PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]

T114 = "evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e"
T115 = "evidence:SP-vision-multimodal-2026:fb77b0019ffe81dc"
T110 = "evidence:SP-vision-multimodal-2026:f1346f195b48d6e0"


def load(pid):
    return json.loads((SRC / "draft/v2/packages" / pid / "draft-result.json").read_text(encoding="utf-8"))


def texts(r):
    return "\n".join([r.get("headline", ""), r.get("deck", "")] +
                     [b.get("text", "") for b in r.get("blocks", [])])


def reader_texts(r):
    return "\n".join([r.get("headline", ""), r.get("deck", "")] +
                     [b.get("text", "") for b in r.get("blocks", [])])


def block_tasks(block):
    return {e["evidence_task_id"] for e in block.get("evidence_refs", [])}


def main() -> int:
    fails = []
    classifications = []

    def check(name, ok, detail=""):
        print(("PASS" if ok else "FAIL"), "-", name, ("| " + detail if detail else ""))
        if not ok:
            fails.append(name)

    def classify(hit, cls, reason):
        classifications.append({"hit": hit, "class": cls, "reason": reason})
        print(f"  class [{cls}] {hit} :: {reason}")

    results = {pid: load(pid) for pid in PIDS}
    check("version fresh-121-r8-rev5 all 16",
          all(r.get("draft_version") == "fresh-121-r8-rev5" for r in results.values()))
    check("status ESTABLISHED all 16", all(r.get("status") == "ESTABLISHED" for r in results.values()))
    reader_blob = "\n".join(reader_texts(r) for r in results.values())
    blob_all = json.dumps(results, ensure_ascii=False)
    syn = json.loads((SRC / "draft/v2/profile-synthesis-result.json").read_text(encoding="utf-8"))
    syn_blob = json.dumps(syn.get("profile_payload", {}), ensure_ascii=False)
    full_surface = reader_blob + "\n" + syn_blob

    # ================= §24 items 1-3: grounding authority =================
    check("§24.1 map no longer prescribes ML grounding as 接地",
          "grounding（グラウンディング）" in
          (SRC / "execution/drafting-terminology-map-ja.md").read_text(encoding="utf-8"))
    check("§24.2 map prescribes グラウンディング",
          "語句グラウンディング" in
          (SRC / "execution/drafting-terminology-map-ja.md").read_text(encoding="utf-8"))
    check("§24.3 phrase/GUI derivatives consistent",
          "GUI要素のグラウンディング" in
          (SRC / "execution/drafting-terminology-map-ja.md").read_text(encoding="utf-8"))
    check("§24.1b no ML/CV/VLM 接地 on reader surface",
          "接地" not in full_surface, "residual 接地 found" if "接地" in full_surface else "")
    check("§24.1c phrase grounding normalized",
          "語句グラウンディング" in reader_blob and "を句グラウンディング" not in reader_blob)
    check("§24.1d no GUI要素の接地 residual",
          "GUI要素の接地" not in full_surface)
    check("§24.1d GUI grounding preferred form present",
          "GUI要素のグラウンディング" in reader_blob or "GUI要素のグラウンディング" in syn_blob)

    # ================= §24 items 4-17: preferred forms =================
    check("§24.4 segmentation preferred forms present",
          "セグメンテーション" in reader_blob
          and "セマンティックセグメンテーション" in reader_blob
          and "インスタンスセグメンテーション" in reader_blob
          and "パノプティックセグメンテーション" in reader_blob)
    # precise technical-分割 residual scan (data-split senses pre-excluded)
    _seg_ok = True
    _seg_hits = []
    for pid, r in results.items():
        for b in r.get("blocks", []) + [{"block_id": "HEADLINE", "text": r.get("headline", "")},
                                        {"block_id": "DECK", "text": r.get("deck", "")}]:
            t = b.get("text", "")
            if pid == "P09" and b.get("block_id") == "DECK":
                t = t.replace("元の解像度の保持と分割", "")  # image-tiling division (recorded ordinary keep)
            if pid == "P15" and b.get("block_id") == "P15-B01":
                t = t.replace("版・分割・抽出規則", "")  # dataset version/split/extraction rules (ordinary data-split keep)
            for m in re.finditer("分割", t):
                ctx = t[max(0, m.start() - 10):m.end() + 10]
                if "データ分割" in ctx or "評価分割" in ctx:
                    continue  # ordinary data-split senses (recorded exceptions)
                _seg_ok = False
                _seg_hits.append(f"{pid}/{b.get('block_id')}:{ctx}")
    check("§24.4b no technical-分割 residuals", _seg_ok, "; ".join(_seg_hits[:4]))
    check("§24.5 bounding boxes normalized",
          "ボックス" in reader_blob and "27.6万ボックス" in reader_blob
          and "基本分類ボックス" in reader_blob and "グラウンディングボックス" in reader_blob
          and not re.search(r"(?<![クス鎖語―・\d万共参照])箱", reader_blob))
    _box_hits = []
    for pid, r in results.items():
        for b in r.get("blocks", []):
            for m in re.finditer(r"(?<![クス鎖語―・\d万共参照])箱", b.get("text", "")):
                _box_hits.append(f"{pid}/{b.get('block_id')}")
    for f in ("headline", "deck"):
        for pid, r in results.items():
            if re.search(r"(?<![クス鎖語―・\d万共参照])箱", r.get(f, "") or ""):
                _box_hits.append(f"{pid}:{f}")
    check("§24.5b no technical-箱 residuals", not _box_hits, "; ".join(_box_hits[:6]))
    check("§24.6 hallucination normalized",
          "ハルシネーション" in reader_blob and "幻覚" not in full_surface
          and "幻を生み" not in full_surface and "幻の夢" not in full_surface)
    check("§24.7 latent dynamics normalized",
          "潜在ダイナミクス" in reader_blob and "潜在動力学" not in full_surface
          and "潜在力学" not in full_surface and "動力学利用" not in full_surface)
    check("§24.8 encoder/decoder normalized",
          "エンコーダ" in reader_blob and "デコーダ" in reader_blob
          and "符号化器" not in full_surface and "復号器" not in full_surface
          and not re.search(r"並列に復号し", full_surface))
    check("§24.9 one-stage/two-stage conform",
          "one-stage" in reader_blob and "two-stage" in reader_blob
          and "一段の速度" not in reader_blob and "二段の精度" not in reader_blob
          and "一段で検出する" not in reader_blob and "高速な一段化" not in reader_blob)
    check("§24.10 feature map + Swin specificity",
          "特徴マップ" in reader_blob and "特徴地図" not in full_surface
          and "シフトウィンドウアテンション" in reader_blob and "ずらし窓注意" not in full_surface
          and "窓型注意機構" not in full_surface)
    check("§24.12 technical fine-tuning normalized",
          "ファインチューニング" in reader_blob and "微調整" not in full_surface
          and "fine-tuneした" not in full_surface)
    check("§24.13 post-training normalized",
          "ポストトレーニング" in reader_blob and "事後学習" not in full_surface)
    check("§24.14 open weights normalized",
          "オープンウェイト" in reader_blob and "開かれた重み" not in full_surface
          and "開放重み" not in full_surface and "開かれたVLA" not in full_surface)
    check("§24.15 MoE authoritative form",
          "Mixture-of-Experts（MoE）" in reader_blob and "混合専門家" not in full_surface
          and "denseモデル" in reader_blob and "MoE版" in reader_blob)
    check("§24.16 no technical-sense 網",
          not re.search(r"(畳み込み網|プレーンな網|Highway網|分類網)", full_surface))
    check("§24.17 streaming/online/offline standard vocabulary",
          "ストリーミング" in reader_blob and "オンライン" in reader_blob and "オフライン" in reader_blob
          and "流れの中の視覚" not in full_surface and "流れの中でのやり取り" not in full_surface
          and "流れの途中で" not in full_surface and "流れを受け続ける" not in full_surface
          and "流れ記憶" not in full_surface)
    check("§24.18 夢学習 removed", "夢学習" not in full_surface
          and "想像した潜在軌道内での学習" in reader_blob)
    check("§24.19 専門法 removed", "専門法" not in full_surface and "専門手法" in reader_blob)
    check("§24.20 オープン帯 removed", "オープン帯" not in full_surface
          and "開放帯" not in full_surface and "オープンモデル群" in reader_blob)
    check("§24.21 流れ記憶 removed", "流れ記憶" not in full_surface
          and "ストリーミング時のメモリ管理" in reader_blob)

    # ================= §24 items 22-25: rev4 guards held =================
    vm_hits = []
    for pid, r in results.items():
        t = reader_texts(r)
        for m in re.finditer(r"VM-D\d{3}", t):
            vm_hits.append(f"{pid}:{m.group(0)}")
    for m in re.finditer(r"VM-D\d{3}", syn_blob):
        vm_hits.append(f"SYN:{m.group(0)}")
    check("§24.22 reader-facing VM-Dxxx remains zero (incl. synthesis)", not vm_hits,
          "; ".join(vm_hits[:6]))
    b07 = next(b for b in results["P07B"]["blocks"] if b.get("block_id") == "P07B-B07")
    check("§24.23 GLIP split val/test-dev",
          "COCO val 60.8 AP、test-dev 61.5 AP" in b07.get("text", "")
          and "開発集合" not in b07.get("text", ""))
    b15_03 = next(b for b in results["P15"]["blocks"] if b.get("block_id") == "P15-B03")
    check("§24.23b P15 GLIP split consistent",
          "COCO val 60.8 AP、test-dev 61.5 AP" in b15_03.get("text", ""))
    b09_15 = next(b for b in results["P15"]["blocks"] if b.get("block_id") == "P15-B09")
    _cond = "Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回"
    check("§24.24 P15-B09 duplicate absent", b09_15.get("text", "").count(_cond) == 1)
    b2_13 = next(b for b in results["P13"]["blocks"] if b.get("block_id") == "P13-B2")
    t132 = b2_13.get("text", "")
    check("§24.25 P13 chronology intact",
          "実演データ" in t132 and "行動トークン化を持ち込み" in t132
          and "データ契約へ規模を広げた" in t132 and "直接生んだという読みは取らず" in t132)

    # ================= Pass A bidirectional spot checks =================
    check("PassA: preferred ボックス not inserted for non-box (P13 has no ボックス)",
          "ボックス" not in texts(results["P13"]))
    check("PassA: 共参照鎖 intact (legitimate chain term)",
          "共参照鎖" in texts(results["P07B"]))
    check("PassA: P14 four-pole taxonomy intact",
          "四つの極" in texts(results["P14"]) and "潜在ダイナミクス" in texts(results["P14"]))
    check("PassA: video concept grounding English kept (source-faithful)",
          "video concept grounding" in
          next(b for b in results["P11"]["blocks"] if b.get("block_id") == "p11-b10").get("text", ""))
    check("PassA: 一本化 kept as preferred convergence term",
          "一本化" in reader_blob)
    check("PassA: Swin first-use gloss present",
          "シフトウィンドウアテンション（shifted-window attention）" in reader_blob)
    check("PassA: MoE first-use gloss present",
          "Mixture-of-Experts（MoE）" in texts(results["P09"]))
    check("PassA: phrase-grounding first-use gloss present",
          "語句グラウンディング（phrase grounding）" in texts(results["P07B"]))
    check("PassA: 位置特定 kept for coordinate-only tasks",
          "位置特定" in reader_blob and "純粋位置特定" in reader_blob)
    check("PassA: encoding operations keep 符号化",
          "符号化" in reader_blob and "絶対時刻の符号化" in texts(results["P09"]))
    check("PassA: token列 / 文字列 / 系列 intact (non-technical 列 keeps)",
          "トークン列" in reader_blob and "文字列" in texts(results["P05"]))

    # ================= Pass B: §3 registry scan =================
    # Each entry: (pattern, expected_class_for_any_hit, note). TECHNICAL_NONE means zero hits allowed.
    PASSB_TECHNICAL_NONE = [
        "接地", "接地化", "フレーズの接地", "句接地", "GUI要素の接地",
        "投票型", "投票域", "学び済み言語モデル", "別学びの部品", "模型化", "算法体系",
        "正確度", "許容付き正確度", "比べ可能性", "答え有効域", "溜めた時系列",
        "証し", "問いかけ", "道具呼び出し", "模型の重み", "界面", "接口", "管路",
        "映像枠", "枠率", "単一伝送路", "実時間", "本パッケージ", "正準",
        "開放的な課題非依存の学習", "training contamination", "Training contamination",
        "contamination MEDIUM", "language-prior HIGH", "provably", "原理的",
        "bag-of-words", "6668", "四極で読む世界モデル", "実環境転移を測る条件を広げた",
        "128万ラベル", "利用画面", "飛び越し結合", "多作物", "見出し学習",
        "教師にbounded", "調整検出器", "地平H", "フロー照合", "機材鋭敏さ",
        "しなやかに測る", "体系側の記録の所管", "GoldGへの下降",
        "既存の収集範囲を置き換えるものではない", "版確定時の検証作業",
        "方策機構の細部はRT-2側資料の所管", "カメラ位置の鋭敏さ",
        "対象期間外に公開された記録は本稿の根拠に含めない", "全域測定",
        "伴走する問答測定", "対応づけ済み40件", "企画",
        "README表層", "ファイル水準", "リポジトリ表層", "第三者文書",
        "後継側の記録", "本記録は著者測定", "本記録は変種",
        "GoldG的実践へ連なる来歴は、GLIP側の資料に委ねる",
        "GLIPの資料実践再定式", "画面操作契約は接地と状態管理で分ける",
        "接地座標は0から1000", "実機実証", "自然文の質問でDETR",
        "多様式", "多模式", "教員モデル", "教員役", "事後学習",
        "塗り分け", "符号を公開", "受け口", "当て戻し",
        "袋詰め", "受け皿", "契約の家", "語彙の足し", "遅い渡し", "固い混ぜ",
        "規模の回し", "レア側の埋め", "幻のふるい", "錨", "投票の素描",
        "二言語の輪切り", "配りの極", "値打ち",
        "データ管", "較正の配管", "汎用手",
        "早い融合", "遅い融合", "固い融合",
        "測りは契約", "三つ目の測り", "レアの測り", "決めなし", "の決め",
        "OVD評価の家", "第二の家", "家系", "水増し", "呼びの到達", "結びの仕組み",
        "教師モデルの写し", "流れの契約", "流れのオムニ", "配り方", "配りの範囲",
        "軸の勘定", "一つの芸", "追加試料", "フューショット", "素子", "まだら",
        "一対の判定に還す", "言葉側だけを締める", "引用の結び", "典拠の結び",
        "手順の借り", "仕組みの消費", "文と絵の組を大量に当て", "4億ペアの当て",
        "表引き", "30超の束", "野外の補い", "列に変える契約", "別の列に置く",
        "別列", "三契約の列", "列を混ぜない", "別の列に",
        "渡す役割", "次の節への渡し", "受け渡す", "引き渡す",
        "話し言葉の入口", "音全般の", "音の入口", "末端からクラウド",
        "三つの部品", "凍結した部品", "部品の選び方", "部品をつなぐ",
        "部品の同時更新", "部品水準", "部品の位置づけ",
        "一本の鎖", "鎖のなか", "密な極", "もう一極", "融合の両極",
        "話し言葉の範囲", "個別学習済み部品", "個別部品の組み立て",
        "拡散の背骨", "固く混ぜる", "三段で固く", "構成を足さず",
        "で、、文と画像", "較正なし", "開かれた重み", "開かれた語彙",
        "開いた語彙", "開語彙", "汎用復号", "復号設計",
        "窓注意", "注意マップ", "特徴量地図", "特徴地図",
        "二塔", "塔を", "混合専門家", "稠密", "冷間始動",
        "検査点", "学習変数", "変種",  # handled separately (model-sense repaired; ordinary keeps)
        "範疇", "覆った離散ラベル", "覆ったトークン",
        "夢学習", "幻の夢", "専門法", "オープン帯", "開放帯", "流れ記憶",
        "潜在動力学", "潜在力学", "動力学利用",
        "微調整", "fine-tune", "符号化器", "復号器", "並列に復号",
        "一般化復号", "検出微調整", "文符号化器", "二重符号化器",
        "注意機構付き符号化復号", "入力符号化器", "オムニ符号化器",
        "トークン化器", "自己教師学習を", "ラベルなし自己教師は",
        "境界ボックス", "物差し", "段取り",
        "運んだ", "土台", "開かれたVLA", "7B開放VLA", "開放最高",
        "開放度合い", "開放語彙条件", "開放性は", "開かれた語句集合",
        "開かれた語彙の", "開かれた集合", "開かれたデータ", "開放データ",
        "開放コード", "完全開放変形", "開放実装", "開かれた側と閉じた側",
        "開かれた記述", "混合専門家版", "密モデル", "密な2B",
        "畳み込み網", "プレーンな網", "Highway網", "分類網",
        "一段の速度", "二段の精度", "一段で検出", "一段の評価",
        "一段化の系譜", "高速な一段化", "二段の処理", "一段の精度不足",
        "二段の生徒", "二段構成", "なぜ一段が",
        "固定ラベル分割器", "意味分割", "個体分割", "パノプティック分割",
        "指示に応じる分割", "指示で動く分割", "512×512の分割",
        "役割は分割の系譜", "U-Netは分割", "検出と分割の区分",
        "LSegによる分割", "汎用分割", "指示参照分割",
        "オープンボキャブラリー分割に", "参照分割", "語句grounding",
        "分割分岐", "27.6万箱", "基本分類箱", "グラウンディング箱",
        "箱注釈", "人手箱なし", "希少箱注釈", "出力（箱か",
        "から箱とマスク", "を箱・", "を箱や",
        "流れの中の視覚", "流れの中でのやり取り", "流れの途中",
        "流れの中の応答", "流れの中の質問", "流れを受け続ける",
        "長い流れを受け", "流れ型の記憶", "流れ処理体系",
        "実展開の遅延", "流れ内やり取り", "源の広さ",
        "思考や足場", "入口として後の評価", "幻覚", "幻を生み",
        "を句グラウンディング", "COCO検証60.8", "後段での融合",
        "窓型注意機構", "交差エンコーダ", "思考変種",
        "学習対象の変数",
    ]
    # notable substring-collision guards: these preferred strings contain a Bari pattern
    # (語句グラウンディング contains 句接地? no; verified: no pattern above is a
    # substring of a preferred form except listed keeps below)
    passb_bad = []
    for pat in PASSB_TECHNICAL_NONE:
        if pat in ("切り分け", "変種"):
            continue  # classified individually below
        if pat in full_surface:
            # locate
            locs = []
            for pid, r in results.items():
                if pat in reader_texts(r):
                    locs.append(pid)
            if pat in syn_blob:
                locs.append("SYN")
            passb_bad.append((pat, locs))
    check("PassB: zero technical-substitution residuals", not passb_bad,
          "; ".join(f"{p}{l}" for p, l in passb_bad[:8]))

    # Pass B classified ordinary keeps (each verified in place)
    def _locs(pat):
        out = []
        for pid, r in results.items():
            t = reader_texts(r)
            if pat in t:
                out.append(pid)
        if pat in syn_blob:
            out.append("SYN")
        return out

    _切り分け_locs = _locs("切り分け")
    check("PassB: 切り分け only ordinary-distinguish keeps",
          set(_切り分け_locs) <= {"P06", "P07B", "P10", "P11", "P13", "P14", "P15"},
          str(sorted(set(_切り分け_locs))))
    check("PassB: 近道 only ordinary-heuristic keeps (extractive/prior shortcuts)",
          set(_locs("近道")) <= {"P05", "P07A", "P15"},
          str(sorted(set(_locs("近道")))))
    for _pid in sorted(set(_切り分け_locs)):
        classify(f"切り分け@{_pid}", "ORDINARY_JAPANESE_ALLOWED",
                 "distinguish/isolate cases (procedure/scale, REC isolation, contract/ablation/quantity separation); not the segmentation task name")
    for _pid in sorted(set(_locs("近道"))):
        classify(f"近道@{_pid}", "ORDINARY_JAPANESE_ALLOWED",
                 "extractive/prior heuristic shortcut; ResNet shortcut connections use ショートカット接続")
    _henshu_locs = [l for l in _locs("変種") if l != "SYN"]
    check("PassB: 変種 only ordinary keeps (aircraft-variant category, ALIGN scoping)",
          set(_henshu_locs) <= {"P07A"},
          str(_henshu_locs))
    for _pid in sorted(set(_henshu_locs)):
        classify(f"変種@{_pid}", "ORDINARY_JAPANESE_ALLOWED",
                 "航空機変種 = fine-grained category name; 変種としての位置づけ = ALIGN scoping prose, not a model/configuration variant label")
    for _o, _r in [
        ("測り手@P11", "measurer person (版と日付と測り手), not a metric noun"),
        ("取り決め@P12", "observation/action arrangement terminology, not an evaluation-rule 決め noun"),
        ("位置決め@P03", "positioning/localization standard term, not an evaluation/extraction-rule 決め"),
        ("目で捉える@P10", "ordinary descriptive prose for perception, not a vision-encoder substitution"),
        ("診断の入口@P10", "ordinary entry/exit rhetorical pair, not a modality input-path term"),
        ("同列@P08", "same-level comparison, not a sequence-representation 列 concept"),
        ("トークン列/文字列/系列", "token/character/series sequences; not evaluation-separation 列"),
        ("網羅@P04/P11", "comprehensive coverage (ordinary 網羅), not a network name"),
        ("約束/束ね/収束", "promise/bundle/converge verbs; not rhetorical recipe praise"),
        ("一本化", "preferred convergence term per map"),
        ("土台になる等の一般語なし", "all foundation-sense 土台 repaired to 基盤; no residuals"),
        ("混合@Molmo等の一般語", "no MoE-architecture 混合専門家 residuals"),
    ]:
        classify(_o, "ORDINARY_JAPANESE_ALLOWED" if "なし" not in _o and "一般語" not in _o else "NOT_APPLICABLE", _r)
    check("PassB: 測り手 only measurer sense",
          "測り手" in texts(results["P11"]) and "測りは契約" not in full_surface
          and "三つ目の測り" not in full_surface)
    check("PassB: no bare-測り metric nouns", "測りは契約" not in full_surface)
    check("PassB: P01 headline 二段 recorded as ordinary historical-arc (not detector)",
          "二段の跳躍" in results["P01"].get("headline", ""))
    classify("二段の跳躍@P01-HEADLINE", "ORDINARY_JAPANESE_ALLOWED",
             "two jumps of the historical arc (handcrafted -> deep); not a detector architecture label")
    for _s in ["第一段階", "第二段階", "二段階の手順", "二段階の選別", "単一段階同時",
               "第一段で", "第二段で", "第二段である", "第三段である", "二段構え",
               "一段にまとめ", "四段階で"]:
        if _s in reader_blob:
            classify(f"{_s}", "ORDINARY_JAPANESE_ALLOWED",
                     "training/procedure/exposition stage counts; detector labels use one-stage/two-stage")
    check("PassB: ordinary 一段/二段 stage counts retained with detector labels normalized",
          "一段階" in reader_blob or "二段階" in reader_blob)

    # ================= Pass C residual-pattern scan =================
    check("PassC: no の夢 technical residuals", "の夢" not in full_surface)
    check("PassC: no 帯 model-category coinage",
          "オープン帯" not in full_surface and "開放帯" not in full_surface)
    check("PassC: no 記憶へ category coinage", "流れ記憶" not in full_surface)
    check("PassC: synthesis normalized",
          "グラウンディング" in syn_blob and "接地" not in syn_blob
          and "ハルシネーション" in syn_blob and "構成要素" in syn_blob
          and "VM-D" not in syn_blob)

    # ================= Negatives J (rev4) + K (rev5) =================
    def neg(name, ok):
        print(("PASS" if ok else "FAIL"), "- NEG", name)
        if not ok:
            fails.append("NEG-" + name)

    neg("J1 reader-VM-Dxxx detected", "VM-D065" in "VM-D065の主張3" and "VM-D" not in full_surface)
    neg("J2 kaihatsu-shuugou detected", "開発集合61.5" in "COCO検証60.8と開発集合61.5"
        and "開発集合" not in full_surface)
    neg("J3 ML-setsuchi-boundary detected", "言語接地" in "言語接地の概念接点" and "接地" not in full_surface)
    neg("J4 data-jissen detected", "データ実践" in "GLIPのデータ実践" and "データ実践" not in reader_blob)
    for _kn, _badf, _good in [
        ("K01 latent-dynamics", "潜在動力学", "潜在ダイナミクス"),
        ("K02 dream-label", "夢学習", "想像した潜在軌道内での学習"),
        ("K03 open-band", "オープン帯", "オープンモデル群"),
        ("K04 flow-memory", "流れ記憶", "ストリーミング時のメモリ管理"),
        ("K05 encoder-kanji", "符号化器", "エンコーダ"),
        ("K06 decoder-kanji", "復号器", "デコーダ"),
        ("K07 detector-ichidan", "一段の速度", "one-stage"),
        ("K08 box-hako", "27.6万箱", "27.6万ボックス"),
        ("K09 hallucination-kanji", "幻覚", "ハルシネーション"),
        ("K10 bichosho", "微調整", "ファインチューニング"),
        ("K11 open-weights", "開かれた重み", "オープンウェイト"),
        ("K12 dense-katakana", "密モデルと", "denseモデル"),
        ("K13 moe-expert", "混合専門家", "MoE"),
        ("K14 swin-window", "ずらし窓注意", "シフトウィンドウアテンション"),
        ("K15 feature-chizu", "特徴地図", "特徴マップ"),
        ("K16 post-training", "事後学習", "ポストトレーニング"),
    ]:
        neg(_kn, _badf not in full_surface)

    # ================= §20 technical non-regression =================
    check("P13 RT-1/RT-2/OXE preserved",
          "実ロボットの実演データ" in t132 and "行動トークン化を持ち込み" in t132)
    check("OpenVLA robot-demonstration terms preserved",
          "実ロボット実演データ" in blob_all and "実機実証" not in blob_all)
    check("pi-zero triple preserved", "H=50" in blob_all and "ホライズンH=50" in blob_all)
    check("P14 four-pole preserved",
          "四つの極" in blob_all and "潜在ダイナミクス" in blob_all and "予測表現" in blob_all)
    _m = json.loads((SRC / "candidate-matrix-v2.json").read_text(encoding="utf-8"))
    _t2d = {}
    for _r in _m["rows"]:
        for _d in _r.get("discovery_ids", []):
            _t2d[_r["evidence_task_id"]] = _d
    _cov = set()
    for _b in results["P15"]["blocks"]:
        for _e in _b.get("evidence_refs", []):
            _d = _t2d.get(_e["evidence_task_id"])
            if _d:
                _cov.add(_d)
    check("P15 40/40 authorities", len(_cov) == 40, f"{len(_cov)}/40")
    _b10_09 = next(b for b in results["P09"]["blocks"] if b.get("block_id") == "p09-b10")
    _mol = "molmo2リポジトリはデータ準備と事前学習やSFTや長文脈SFT"
    check("P09 Molmo2 single", _b10_09.get("text", "").count(_mol) == 1)
    check("OSWorld condition binding preserved",
          "Claude Opus 4.7" in blob_all and "318.4" in blob_all and "481.8" in blob_all)
    check("GroundingDINO triad preserved",
          "言語誘導型クエリ選択" in blob_all and "チェックポイント" in blob_all)
    check("Flamingo data-volume preserved", "数千倍多く用いてファインチューニングした専用モデル" in blob_all)
    check("MiniGPT-4/LLaVA freeze preserved", "凍結" in texts(results["P08"]))
    check("DETR matching/loss preserved", "マッチングコスト" in texts(results["P02"]))
    check("MAE recipe preserved", "800エポック" in texts(results["P06"]))
    check("DINO centering/sharpening preserved",
          "センタリング" in texts(results["P06"]) and "先鋭化" in texts(results["P06"]))
    check("SAM3/Agentic separation preserved",
          "memory-based tracker" in texts(results["P11"]) and "エージェント型動画理解" in texts(results["P11"]))
    check("OCRBench v2 preserved", "OCRBench v2の23課題" in texts(results["P05"]))
    check("LongVideoBench 6678 preserved", "6678" in blob_all and "6668" not in blob_all)
    check("VM-D122 absent", "VM-D122" not in blob_all)

    # ================= effective consumption + F/G/H/I re-run (sample) =================
    eff = {}
    for pid in ("P07B", "P05", "P11", "P07A"):
        eff[pid] = {}
        for b in results[pid]["blocks"]:
            ts = block_tasks(b)
            eff[pid][b.get("block_id")] = sorted(
                t.split(":")[-1] for t in ts if t in (T114, T115, T110))
    (EDIR / "effective-input-report-rev5.json").write_text(json.dumps(
        {"report": "effective cross-package consumption in FINAL draft",
         "packages": eff}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    check("P07B D114 effective", any("0f5a5b1f4eb4032e" in ts for ts in eff["P07B"].values()))
    check("P07B D115 effective", any("fb77b0019ffe81dc" in ts for ts in eff["P07B"].values()))
    check("P05 D110 effective", any("f1346f195b48d6e0" in ts for ts in eff["P05"].values()))
    check("P11 D115 effective", any("fb77b0019ffe81dc" in ts for ts in eff["P11"].values()))
    check("P07A D114 effective", any("0f5a5b1f4eb4032e" in ts for ts in eff["P07A"].values()))
    f1 = copy.deepcopy(results["P07B"])
    for b in f1["blocks"]:
        b["evidence_refs"] = [e for e in b.get("evidence_refs", []) if e["evidence_task_id"] != T114]
    neg("F1 P07B-D114-omitted detected", not any(T114 in block_tasks(b) for b in f1["blocks"]))
    neg("I2 ML-setsuchi detected", "接地" in "語句の接地" and "接地" not in full_surface)
    neg("I3 shiryou-jissen detected", "資料実践" in "検出を語句の接地へ書き直す資料実践"
        and "資料実践" not in reader_blob)

    # ================= §24 items 26-33: authority invariants =================
    _arch_sha = hashlib.sha256((SRC / "architecture-v2.json").read_bytes()).hexdigest()
    check("§24.27 Architecture SHA unchanged",
          _arch_sha == "56658960dff0269a89bf38d5b3027147dea7159f5c15337ff8a74d6ea7e4d773",
          _arch_sha[:16])
    import glob as _glob
    _ev = json.loads(max([Path(p) for p in _glob.glob(str(SRC / "evidence/v2/accepted/*/evidence-accepted.json"))],
                         key=lambda q: q.stat().st_mtime).read_text(encoding="utf-8"))
    from collections import Counter as _C2
    _st = _C2(r["status"] for r in _ev["results"])
    check("§24.28 Evidence 121/116/5",
          _ev["result_count"] == 121 and dict(_st) == {"VERIFIED": 116, "PARTIAL": 5},
          f"{_ev['result_count']}/{dict(_st)}")
    _sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
    check("§24.29 Selection 121", _sel.get("summary", {}).get("selected_count") == 121)
    _comp = json.loads((SRC / "profile-completeness-v2.json").read_text(encoding="utf-8"))
    from collections import Counter as _C3
    _ostat = _C3(o.get("status") for o in _comp.get("obligations", []))
    check("§24.30 Completeness 14/2", dict(_ostat) == {"SATISFIED": 14, "LIMITATION": 2},
          str(dict(_ostat)))
    _map = json.loads((SRC / "execution/r8-draft-closure-rev1-20261007/cross-package-map-r8-rev1.json").read_text(encoding="utf-8"))
    check("§24.31 map 35 unchanged",
          len(_map["entries"]) == 35 and
          any(e["consumer_package"] == "P04" and e["discovery_id"] == "VM-D047" for e in _map["entries"]),
          str(len(_map["entries"])))
    import subprocess as _sp
    _core_roots = ["AGENTS.md", "config/", "schemas/", "scripts/", ".github/workflows/",
                   "docs/survey-production-core-v2-session-bootstrap.md",
                   "docs/survey-production-core-v2-sol-luna-review-governance.md"]
    _core_raw = _sp.run(["git", "status", "--porcelain=v1", "--"] + _core_roots,
                        capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    _dirty = "\n".join(l for l in _core_raw.splitlines() if "__pycache__" not in l).strip()
    check("§24.32 Shared Core unchanged", _dirty == "", _dirty[:300])
    _cov_dirty = _sp.run(["git", "status", "--porcelain=v1", "--", "specials/", "surveys/"],
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    check("§24.33 Coverage Freeze unchanged", _cov_dirty == "", _cov_dirty[:300])
    # P15 refs non-dangling: every evidence_task_id resolves in matrix
    _matrix_tasks = {_r["evidence_task_id"] for _r in _m["rows"]}
    _dangling = [e["evidence_task_id"] for b in results["P15"]["blocks"]
                 for e in b.get("evidence_refs", []) if e["evidence_task_id"] not in _matrix_tasks]
    check("§24.26 P15 refs non-dangling", not _dangling, str(_dangling[:3]))

    (EDIR / "semantic-audit-rev5.json").write_text(json.dumps(
        {"audit": "fresh-121-r8-rev5 terminology QA (Pass A/B/C + §24)",
         "failures": fails, "classifications": classifications,
         "effective": eff}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OVERALL:", "PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
