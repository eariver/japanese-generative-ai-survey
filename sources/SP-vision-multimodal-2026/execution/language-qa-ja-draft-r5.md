# TS-003 Language QA r5 — final reader-surface cleanup

Status: `PASS_WITH_NOTES / MAP_R5_APPLIED / SOL_R5_PENDING`

Date: `2026-10-02`

Authority: `execution/drafting-terminology-map-ja.md`
(starting blob `45d8eb53a14ab9a50dd6eab7b74326ad7108dc5e`,
status `DRAFT_R5_BINDING`,
terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R5_BINDING`).

Scope: all 16 r5 Draft Results (headline + deck + PARAGRAPH + CLAIM_BOUNDARY) +
profile synthesis payload. Reader text ~52.8k chars.

## 1. Exact duplicate sentences

Zero per package and cross-package (re-verified post-regeneration).
No re-padding (52.2k r4 → 52.8k r5; delta is repairs only).

## 2. Pass A — preferred/avoid conformance (full map §§1–2)

Prior gains hold (r1–r4 lexicon, teacher/student, code/encoding, multimodal,
hallucination, segmentation-family, deployment, fusion terms all clean).
No regressions introduced by r5 repairs (verified by re-scan).

## 3. Pass B — §3.5 closure + full registry re-audit

- P06 headline now `Transformerと自己教師あり学習の基盤` (map-conformant).
- P06 mechanism: テキスト側のみを調整 / 各画像・テキスト対を独立に判定する
  シグモイド損失. P06 boundary states all three F3 points directly
  (DeiT training-recipe mitigation; abstract-level-only mechanism support;
  citation correspondence unresolved); no production-consumption language.
- P07A contrastive prose: 対照学習 / 固定クラス分類 / 30以上のデータセット.
- P07B ODinW: 実世界・多様ドメインの補完的評価.
- P09 token-sequence contract / P11 separate evaluation axis / P06 適用範囲 /
  P07A 次節扱い: all direct.
- Full registry (§§3.1–3.4) re-scanned on canonical r5: zero BLOCKING residue
  (one apparent hit is the repaired headline itself, confirmed present-by-design).

## 4. Pass C — full-text read (P06/P07A complete + connective-tissue triage)

- Repaired regions read in final form: direct technical wording, attribution and
  Evidence scope intact, no new metaphors introduced.
- Triaged and retained with rationale (ordinary/clear-in-context or
  Architecture-owned): 例 chains, 装置, literal 箱, non-box 枠, 四極 +
  axis-defined 極, 共参照鎖, 版/ID/日付の結びつけ (version binding),
  損失の結びを解く (decoupling), 測り方/測り手/測る verbs, dataset-split 分割,
  決める verbs + 位置決め, inflation 水増し, idiom 読みの土台, 二塔
  (two-tower direct translation), 呼び出し可能性 (consistent volume term),
  手足と目 (explained), まだら-ordinary, 家系-lineage note, merged-sentence
  損失の結び variants, 流れ ordinary noun, 三つ組 grouping.
- Deck-level 渡す (P07A deck) repaired alongside the flagged b3 instance
  (same failure class, found during Pass C).

## 5. New failures in r5

None beyond §3.5. Map-first rule had nothing to trigger; map unchanged
(final blob == starting blob, recorded in r5 report §13).

## 6. Preserved gains + integrity

Zero duplicates; no padding; r1–r4 repairs intact; boundary sets unchanged
(53 EXPLICIT concise Japanese + 104 OMISSION); evaluator roles explicit;
P07B grouped, P09 protocol-bound, P15 synthesis-led; G01–G06/PARTIAL semantics
intact; no cross-task ranking; packages byte-identical; no new research.

Terminal QA state: `TS-003_LANGUAGE_QA_R5_COMPLETE / PASS_WITH_NOTES`
