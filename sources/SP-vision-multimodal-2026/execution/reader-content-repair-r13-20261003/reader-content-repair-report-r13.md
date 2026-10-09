# TS-003 r13 Review Follow-up Bounded Repair — Repair Report

- Date: 2026-10-03 JST
- Basis: independent review on r12 (HEAD `103df2866`, `FRESH_CONTENT_REVIEW_REQUIRED`), verdict: fix-and-re-review (no full rewrite).
- Branch (existing only): `special/vision-multimodal-2026-work`
- Terminal: `FRESH_CONTENT_REVIEW_REQUIRED` (READER_JSON_ONLY, no TeX/PDF)
- Start guard: remote HEAD/tree matched `103df2866` / `e9027328e1e8c6ddd3a8fc24ec81056323d74fd0`, clean tree, no new branch.

## 1. What r13 changes vs r12 (r12 already carried the r12-turn corrections)

r13 reader: 135 → 139 blocks; 67,334 → 68,382 chars (+1,048). Per-package deltas: P02 −189 (b7 pointer rewrite), P07A +10 (edits), P07B −242 (b16 map rewrite), P09 +1,454 (4 supplement blocks), P13 −3 (terminology), P14 −92 (terminology), P15 −28 (X01 swap). P01/P03/P04/P05/P06/P08/P10/P11/P12 unchanged in count (P10–P12 keeps r12 merges).

Genuine r13 value-add (r12 already held Agent-A/B corrections, r12 merges, #559 guards):

1. **Evidence r6 batch** (review priority 1+3): append-only acceptance `5b8d4ba6` (ae485bd4) + views `e8373be3` (e413a7b9), 111 cards (105 byte-identical hash-proven, 6 rebuilt), all canonical validators PASS. VM-D098 embeddings→embodiments micro-fix; VM-D105 11B-parameter clarification; 12 P09 supplement AUTHOR_CLAIMs from bound reports (Qwen3-VL merger/DeepStack-map/timestamps/S0-S3; Omni AuT-12.5Hz/TM-RoPE-24-20-20/theoretical-latency-table; InternVL3 448-256/MLP/V2PE-δ/SFT-MPO-32K; Molmo2 K-crop/connector-layers/training-packing). All 14 claim texts primary-verified section-level (Omni + Qwen3-VL + InternVL3 + Molmo full-text HTML). Timestamps preserved per Sol r4/r5 rule. See `execution/evidence-semantic-repair-r6-20261003/repair-report-r5-to-r6.md`.
2. **X01 supervision timeline implemented** (priority 2): r12 p15-b9 gap declaration REPLACED with real timeline binding 8 named already-selected supervision authorities (ImageNet labels / CLIP pairs / RegionCLIP pseudo-pairs / DINO self-distillation / MAE masked objectives / InstructBLIP tuning / LLaVA synthetic instruction / RT-1 demonstrations) + provenance record #2 (Architecture X01-X04 clause cited; PRIMARY homes unchanged; P15-native absence fenced in prose).
3. **Coverage resync + generation-path guard** (priority 4): field-level sync (輪郭→objectness+offset, 描き直し→予測, 潜ませ→潜在行動表現, 110億級→11B-parameter, 绑定→との結びつけ ×24, 私傾→傾向, 代表値→アンカー配置); 13 notes rewritten positive-only; builder now FAILS on any banned/stale phrase in coverage output. FULL 20→24 ADEQUATE (P09 four promoted on new evidence, documented), PARTIAL 13→9.
4. **Currency sweep + materiality** (priority 5): `execution/currency-sweep-r13-20261003/currency-sweep-record.md`. 3.7 Flash EXCLUDE, 3.8 Flash EXCLUDE, agentic video understanding INSPECT (pipeline referral, NOT admitted), Omni Flash EXCLUDE. No new candidates/Discovery/Evidence.
5. **Residual dedup pointer-rewrites** (priority 6 subset): p07b-b16 (branch map), p14-b10 (separation lens), p09-b11 (problem+quarantine), p02-b7 (reference table). 5-char n-gram vs fronts: 0.461→0.036, 0.418→0.020, 0.413→0.018, 0.360→0.045. p15-b13 verified spec-free (names + comparison only). Zero exact-duplicate sentences in r13 (machine-verified).
6. **Terminology standardization** (priority 7): 文節→埋め込み系列写像 (p13-b3), 行動の言語化→行動テキストトークン化 (p13-b7), RT-1 trajectory≠token-unit (p13-b2; 11-dim/256-bin/130k/700+ recorded as Evidence gap, not inserted), 見せ場/ casual 極→評価軸/分類上 (p14-b2/b3/b4), 呼び出し可能性→言語による指定可能性 (p07a-b2/b3/b5), 一手/受け持つ (p13-b1/b5), 11B-parameter (p14-b5). 起点/到達点 kept (review-allowed lineage terms); 四つの極 kept (Architecture-mandated).
7. **P09 supplement prose** p09-b13–b16 binding new claims (each ~430–550 chars, claim-bound, #559-safe: 80ms granularity-only, 234/547ms theoretical-only with setup, no license claims).

## 2. Technical correction matrix (r13 slice; r12 corrections retained)

- OpenVLA: Evidence repaired (r6) + reader already correct since r12 → chain realigned. Follow-up need CLOSED.
- Genie 11B: Evidence clarified (r6) + reader p14-b5 + coverage fields → explicit 11B-parameter. D105 stays PARTIAL (extraction internals gap).
- RT-1: conceptual split without unevidenced numbers; specifics recorded as Evidence gap (not inserted per source-fidelity rule).
- CLIP/LLaVA/DINO/RPN/DETR/RT-2/DreamerV3/Genie-separation: r12 corrections retained byte-identical (builders assert); no regression (fix-marker scan all present).
- P09 axes: supplemented items now ADEQUATE-bound; undisclosed axes stay LIMIT (KV measured, non-theoretical latency, unpublished internals) — unknown kept unknown.
- P15: b5 bound (r12) + b9 timeline implemented + b13 taxonomy kept + b16 capability/architecture split kept; training/eval never merged.
- P06 SigLIP2 lineage: confirmed since r12 via Qwen reports; unchanged.

## 3. Evidence gaps ledger

- RESOLVED by r6: OpenVLA embodiments wording; Genie 11B ambiguity; 12 P09 mechanism axes (merger, DeepStack map, timestamps, S0-S3, AuT rates, TM-RoPE split, latency table, 448/256, V2PE δ, SFT/MPO/32K, K-crops, connector layers, training/packing).
- Still PARTIAL (node-level, documented): D006/D011/D012/D051/D089/D095/D097/D103/D105 (full list with per-axis reasons in coverage-r13).
- LIMIT (axis-level, by design): measured KV-cache, non-theoretical latency, unpublished internals, layer indices beyond disclosed, per-image tile caps, training throughputs.
- DEFERRED (pipeline referral, not admitted): agentic video understanding (INSPECT); RT-1 discretization specifics; P09 items beyond bound-report disclosure.
- STALE PINS (by design, Human-gated path owed): candidate-matrix basis 5cc951bd, draft-package evidence_acceptance pins, views 78a08d3c — those files truthfully record their build inputs; rebind needs Architecture rN+1 per dependency-aware revision. No lifecycle artifact rewritten; no approval fabricated. Sol re-review of the r6 batch requested with this fresh review.

## 4. Language QA

- Banned/metaphor scan over r13 bytes: zero hits (文節/行動の言語化/見せ場-casual/極-casual/一手/受け持つ/呼び出し可能性/绑定/算法/変種/文字の理論/設計の選び/投票型/幻覚/基線/日程/教員/埋め込み評価/物の輪郭/代表値/後始末/吸い上げ/夢/潜ませ/言い当て).
- Contextual retains: 生徒モデル (prescribed), 教師信号/教師あり/教師モデル/教師ネットワーク (standard/descriptive), 枠組み/クエリ枠 (retained), コマ (detector-fps + interactive-frame package usage; video input frames are フレーム/入力フレーム), 四つの極 (Architecture term), 起点/到達点 (allowed lineage).
- #559: 9 forbidden absent, 16 required present, retains intact.

## 5. Files

New (edition-local only): reader-editorial-authority-r13.json; technical-depth-coverage-r13.json; build_reader_editorial_authority_r13.py; build_technical_depth_coverage_r13.py; r13-ops-a/b.json; r13-coverage-overlay.json; evidence/v2/accepted/5b8d4ba6…/ + views/e8373be3…/; execution/evidence-semantic-repair-r6-20261003/ (builder, card-edits, input, repair report); execution/currency-sweep-r13-20261003/; this report.
Untouched: main.tex/pdf, references.bib, historical candidates, r10/r11/r12 authorities, Architecture approval/Architecture/Selection, checkpoints, production-state.json, Shared Core, candidate-matrix, draft packages, materiality/completeness. Issue #559 left open. No Human decision inferred. No freeze/release.
