# TS-003 Language QA r7 — preferred-terminology conformance

Status: `PASS_WITH_NOTES / MAP_R7_APPLIED / SOL_R7_PENDING`

Date: `2026-10-02`

Authority: `execution/drafting-terminology-map-ja.md`
(starting blob `4674bca4f8164fa9fd371b51410ea078160be93d`,
status `DRAFT_R7_BINDING`,
terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R7_BINDING`).

Scope: all 16 r7 Draft Results (headline + deck + PARAGRAPH + CLAIM_BOUNDARY) +
profile synthesis payload. Reader text ~53.2k chars.

## 1. Exact duplicate sentences

Zero per package and cross-package (re-verified post-regeneration, incl. after
follow-up fixes). No re-padding.

## 2. Section-2 preferred-form semantic conformance table (every row)

Method: for each Section-2 row, preferred presence + nonpreferred scan across
headline/deck/all blocks/boundaries, then semantic classification of every hit.
`n(pref)` = packages/blocks with preferred form; verdict PASS unless stated.

| # | Concept | Preferred (present) | Nonpreferred hits | Classification / retained exception | Verdict |
|---|---|---|---|---|---|
| 1 | model | モデル 81 | 模型 0 | — | PASS |
| 2 | neural network | ニューラルネットワーク 1 | 網 0 | — | PASS |
| 3 | CNN | CNN 15 | 畳み込み網/基幹網 0 | — | PASS |
| 4 | multimodal | マルチモーダル 7 | 多様式 0 | — | PASS |
| 5 | modality | モダリティ 4 | 様式 0 (excl. fixed phrases) | — | PASS |
| 6 | VLM | VLM/視覚言語モデル 13 | 視覚言語模型 0 | — | PASS |
| 7 | VLA | VLA 5 | 視覚言語行動模型 0 | — | PASS |
| 8 | Computer Use | Computer Use 1 | 計算機利用/電脳使用 0 | — | PASS |
| 9 | open-vocabulary | オープンボキャブラリー 7 | 開かれた語彙/開いた語彙 0 | repaired P02/H/deck/b5, P07B/H/b1/b2/b4/b8 | PASS |
| 10 | referring expression | 指示表現 1 | 参照表現 0 | — | PASS |
| 11 | phrase grounding | フレーズの接地 1 | 句接地 0 | — | PASS |
| 12 | REC/OVD/OVS | 3 acronyms present | none coined | — | PASS |
| 13 | zero-shot | ゼロショット 20 | 無学習推論 0 | — | PASS |
| 14 | prompt | プロンプト 3 | プロンプト可能 0 | — | PASS |
| 15 | instruction tuning | 指示チューニング 2 | 命令調整 0 | — | PASS |
| 16 | self-supervised | 自己教師あり 8 | bare自己教師 0, 自己統制 0 | — | PASS |
| 17 | contrastive/masked | 対照系 10, MAE系 2 | 対比化/仮面化/当て戻し 0 | — | PASS |
| 18 | teacher/student | 教師モデル17/生徒モデル3/教師信号22 | 教員/教員役/bare生徒 0 | 生徒 hits only inside 生徒モデル | PASS |
| 19 | distillation/fine-tuning/pretraining | 蒸留14/ファインチューニング/事前学習/ポストトレーニング | 抽出化/事後学習 0; 微調整 0 | 6×微調整→ファインチューニング incl. P07B boundary + P03 boundary check | PASS |
| 20 | encoder/decoder/backbone | 23 | 符号器/復号器/汎用復号/復号設計/基幹網 0 | repaired P07B b8 ×2 | PASS |
| 21 | resampler/attention/query | 10 (incl. アテンション/クエリ) | 交差注意/窓注意/注意マップ 0; model問い合わせ 0 | repaired P06 b1/b3, P02 b2, P08 ×4; retained: 注意を促す/要する (caution, P07B b6), 判定と汚染の注意 (P10 b3) with sentences | PASS |
| 22 | shortcut/stage/featmap | ショートカット接続1/one-stage4/two-stage/特徴マップ1 | ResNet近道 0; detector一段/二段 0; 特徴量地図 0 | repaired P01 b2, P02 deck/b2/b3, P07B b2; retained: 一段階手順/学習 (P09 b2), 二段階の読み (P15 b4), 第一段階/第二段階 (P08), 抜き出し/言語先行の近道 heuristic (P05 b4, P07A b2, P15 b2) with sentences | PASS |
| 23 | dual-encoder/MoE/dense | デュアルエンコーダ2/two-tower/MoE3/dense1 | 二塔/混合専門家/稠密-model 0 | repaired P07A b3 ×2, P09 b1/b2/b5; no bare-塔 remains | PASS |
| 24 | checkpoint/params/variant | チェックポイント2/学習可能パラメータ1/バリアント7/派生 | 検査点/学習変数/変種-model 0 | repaired P08 b2 ×2, P09 b7, P02/P07A/P07B/P08/P09 変種9 | PASS |
| 25 | category/cold/masked-label | カテゴリ8/コールドスタート1/マスクされた離散1 | 範疇/冷間始動/覆った離散 0 | repaired P07A b1 ×2, P07B b1/b2/b4/b5/b7/b8, P09 b5/b7, P09 b4 | PASS |
| 26 | speech/component | 音声系/構成要素/モジュール/部位/要素名 | label話し言葉 0; arch部品 0 | repaired P09 b4 ×4/b5 ×2 (kept speech-vs-audio scope), P03 b3→構成要素, P04 b2→部位, P05 b3→要素名, P08 H/b5 →接続/構成要素 | PASS |
| 27 | frozen/token/code | 凍結57/トークン/コード/符号化 | 固定化/字句化/符号-code 0 | — | PASS |
| 28 | box/mask/coord | ボックス27/マスク/座標 | technical箱 0 | repaired P02 H/deck/b2/b3/b4/b5, P03 deck/b2/b3, P04 deck/b1/b3, P07B H/b1/b4/b7/b9, P13 b3/b5, P03 boundary | PASS |
| 29 | calibration/hallucination | キャリブレーション不要3/ハルシネーション5 | 較正なし/幻覚 0 | repaired P04 deck/b1/b4 | PASS |
| 30 | CoT/scaffold/contam/ablation | 17 | 思考連鎖/審査員/足場/混入化 0 | — | PASS |
| 31 | latency/stream/ts/omni/shot | 20 | 潜時/実時間化/先回り化/全様式/画面撮影化 0 | — | PASS |
| 32 | traj/planner/RL/embodiment | 23 (軌道/プランナ/計画/方策/身体/機体系) | 軌跡/具現化/機体横断化/潜在力学化 0; 方針 hits are 記憶の方針/運用方針 (non-RL) | retained with sentences | PASS |
| 33 | sim/action/open-weights | 10 | 模擬器/動作符号化/開かれた重み 0 | repaired P09 b7, P13 b6/b7/boundary | PASS |
| 34 | vendor/card/OCR/objective | 37 | 供給者説/模型証/目的化 0 | — | PASS |
| 35 | interface/contract | 13 | 受け口/契約化 0 | — | PASS |
| 36 | strength/provenance/convergence | 21 | 主張強度化/来歴化/融合化 0 | — | PASS |
| 37 | lineage/capstone/op/trade/recipe | 60 | 系統化/集大成化/稼働点化/交換化/処方 0 | — | PASS |
| 38 | scaling/discipline | スケーリング3/大規模学習/規律19 | 躾/規模化/大規模化 0 | repaired P06 b3 | PASS |
| 39 | metric/preserve | 52 | 物差し 0 | — | PASS |
| 40 | reliability/temporal/ego/doc/point | 8 (incl. 一人称視点/文書理解/指さし) | 時間状態化/自己中心化/文書知能化/点示化 0; 信頼性 absent | reliability concept carried by 出所/由来/独立測定; no nonpreferred substitute used | PASS |
| 41 | grounding/align/perception | 47+27 | 接地化/整列化/整合化/知覚化 0; P07A zero接地 | — | PASS |
| 42 | detection/segment/bench/world | 84 | 検知 0 | — | PASS |
| 43 | capability/arch | 52 | 証し/配備化/展開化 0 | — | PASS |
| 44 | evaluator roles | ベンダー測定/著者測定/第三者 53 | 供給者 0; bare著者-as-independence 0 | — | PASS |

Retained-exception sentences (exact):
- P11 deck: 「順序と記憶と問い合わせの違いをたどり」 — system/user inquiry to streaming video, not model queries.
- P07B b6 ×2: 「注意を促す」「注意を要する」 — caution senses.
- P10 b3: 「判定と汚染の注意を合わせて記し」 — caution sense.
- P05 b4 / P07A b2 / P15 b2: 「抜き出しの近道」「言語先行の近道」 — heuristic-bypass senses (map allows heuristic 近道).
- P08 b2/b3: 「第一段階/第二段階/二段階」 — learning/procedure stages (map exception).
- P09 b2: 「一段階の手順/学習」 — single-stage training procedure (same exception family).
- P15 b4: 「二段階の読み」 — two-step reading procedure (not detector naming).

## 3. Full registry re-audit (§§3.1–3.7)

Zero TECHNICAL_SUBSTITUTION_BLOCKING hits on canonical r7 (programmatic scan
over headline/deck/all blocks/boundaries, with 生徒モデル/符号化 disambiguation).
Prior-round gains intact.

## 4. Headline/deck audit

All 16 headlines + decks scanned in the Section-2 pass above. Changed: P02
headline (ボックス/オープンボキャブラリー), P07B headline (ボックス),
P08 headline (接続する direct title). No relaxed standard applied.

## 5. Targeted audits (§5.1–5.20 + Sol F1–F5)

Box/open-vocab/decoder/calibration/scaling/open-weights/component/bridge/lineage/
attention/query/shortcut/stage/featmap/dual-encoder/MoE/dense/cold-start/
checkpoint/params/variant/category/masked-label/speech: all repaired and
verified present-in-canonical-bytes (§2 rows 9, 20–28, 33). P06 headline/
mechanism/boundary, P07A contrastive set, P07B ODinW+segmentation, P11 axis,
P13 chain→系譜, P08 connection headline: verified.

## 6. Duplicates / integrity

Zero exact duplicates (per-package + cross-package). No padding (53.0k→53.2k chars,
delta is repairs only). Evidence refs, attribution, boundary sets (53+104),
G01–G06/PARTIAL intact. Packages byte-identical. No new research.

## 7. New failures in r7

Follow-up finds during r7 audit (CLS注意マップ/注意 mechanism uses, 一段階/
二段階 procedure forms, P03-boundary 箱) were all repaired and re-audited;
no map addition needed (all covered by existing §2 preferred forms). Map unchanged.

Terminal QA state: `TS-003_LANGUAGE_QA_R7_COMPLETE / PASS_WITH_NOTES`
