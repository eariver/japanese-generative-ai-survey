# TS-003 Sol Draft Review r4

Status: `SOL_DRAFT_REVIEW_R4 / REQUEST_CHANGES / FINAL_READER_SURFACE_CLEANUP`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed Draft r4 authority commit:

`f90f6000538437985b683edb1b2c4c33e2d067c5`

Reviewed tree:

`8807609dd8755cfdb7df6dc7b558c54822e5489e`

Decision:

`REQUEST_CHANGES`

Draft r4 closes the major r3 blocking set and preserves all prior structural and terminology gains. However, independent Sol review still found a small set of reader-facing expressions that violate the same cumulative anti-over-domestication rule, including one direct miss against the existing map in the P06 headline.

The cumulative terminology map has therefore been advanced for r5 at:

- commit `1b5184fda07afe4f8ffaff6124d09cfbfb364a1f`
- blob `45d8eb53a14ab9a50dd6eab7b74326ad7108dc5e`
- terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R5_BINDING`

## 1. What passed

- r4 start guard matched exactly:
  - work HEAD `98824312010983b5eaa9cfdce5de04ed02f33f63`
  - work tree `1f5595e41d7bbdb1cc62ba958f0b94360fb02d00`
- work branch advanced by one normal child commit to the reviewed r4 authority.
- main remained:
  - `d6381568cc897a47d6de992189e20339350342b7`
  - tree `83ce3a216d852a1c32d0138f9c56fadefa800666`
- Frozen Core remained:
  - `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
  - tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- lifecycle remains `DRAFT_COMPLETE`.
- Architecture Review remains approved.
- Publication Preview remains pending.
- validation/publication_preview/freeze/release remain pending.
- all 16 canonical Draft Results are `draft_version=r4`, `status=REVISED`.
- exact duplicate sentence scan independently confirms zero duplicates in all 16 packages.
- all previously enumerated r1-r3 regression strings checked by Sol are absent from canonical r4.
- technical segmentation in P07B is now rendered with the `セグメンテーション` family; retained `分割` uses are dataset split/partition uses.
- bare technical noun `測り`, technical `決め`, `評価の家`, model-family `家系/第二の家`, augmentation `水増し`, scaffold `足場`, technical `土台` in previously identified body positions, release `配り方`, `軸の勘定`, `一つの芸`, `追加試料`, `フューショット`, neural-unit `素子`, and openness `まだら` were materially repaired.
- preferred terms are now present, including `データ拡張`, `scaffold（補助的手順）`, `few-shot`, `ユニット`, `提供形態`, `提供範囲`.
- no internal workflow identifiers leak into reader prose.
- Draft Packages remain unchanged.
- no new research was performed.

These passes do not override the residual findings below.

## 2. Blocking finding F1 — P06 headline directly violates the current map

Canonical r4 headline:

`Transformerと自己教師の土台`

This contains two reader-surface defects.

First, the existing map already defines:

`self-supervised -> 自己教師あり`

Therefore `自己教師` is not the approved technical form.

Second, in this headline `土台` names the technical foundation/base representation theme, not an ordinary idiom. This is exactly the technical `土台` category added in the r4 map.

A direct form such as `Transformerと自己教師あり学習の基盤` or another Architecture-consistent established technical form is required.

This also shows that the r4 QA's statement that technical `土台` was repaired was incomplete because the headline was missed.

## 3. Blocking finding F2 — P06 still contains compressed everyday-language substitutes

Canonical r4 P06 contains:

- `視覚エンコーダを凍らせ、言葉側だけを締める調整である。`
- `正規化の大域性を捨てて一対の判定に還す点にある。`

These should name the actual technical operation directly.

Examples of acceptable direction, subject to bound Evidence:

- `視覚エンコーダを凍結し、テキスト側のみを調整する`;
- `各画像・テキスト対を独立に判定するシグモイド損失へ置き換える`.

Do not use `締める` or `還す` as the primary description of the mechanism.

## 4. Blocking finding F3 — source/citation language remains opaque

P06 still contains:

- `正確な引用の結びは残る`;
- `正確な典拠の結びのなさ`;
- `次の節の結びの話に渡す`.

The CLAIM_BOUNDARY is more problematic:

`DeiTは手順の借りでこれを緩和する。SigLIPの損失の仕組みの消費は抄録頁の水準に留まり、正確な典拠の結びは残る。`

`手順の借り`, `仕組みの消費`, and `典拠の結び` are not suitable technical-survey wording.

Required repair:

- state that DeiT mitigates the data dependency through its training recipe / training procedure;
- state that the mechanism claim is supported only to the abstract-level evidence currently bound;
- state that precise source/citation correspondence remains unresolved.

Do not expose production-side “consumption” language to readers.

## 5. Blocking finding F4 — P07A still uses nontechnical shorthand for contrastive learning and datasets

Representative r4 prose:

- `文と絵の組を大量に当て`;
- `決まった範疇の表引きから`;
- `4億ペアの当てが、30超の束への転送を生んだ`.

These are semantically recoverable, but they are the same reader-surface failure class as prior rounds.

Use direct established wording:

- image-text pairs;
- contrastive learning / alignment;
- fixed-class classification;
- 30+ datasets or evaluation tasks;
- zero-shot transfer.

Do not use `当て`, `表引き`, or `束` as substitutes for those technical concepts.

## 6. Blocking finding F5 — a few additional shorthand metaphors remain

Examples found in independent scan:

- P07B: `ODinWを野外の補いとして添える`;
- P09: `受け止めて列に変える契約`;
- P11: `流れる映像への即応とは別の列に置く`;
- P06: `階層を要する検出や密な予測にTransformerを渡す役割`;
- P07A: `次の節への渡し`.

These should be rewritten with the actual role:

- ODinW as supplementary in-the-wild/diverse-domain evaluation;
- audio/speech input converted into token/sequence representation;
- offline long-context evaluation treated on a separate evaluation axis from streaming response;
- Swin extending Transformer use to hierarchical detection/dense prediction;
- the next section extending global alignment to grounding/localization.

This is a small set, but the volume is now close enough to publication that leaving these generated shorthand expressions would be visible.

## 7. QA process finding

The r4 QA is much stronger than r2/r3 and correctly classified many context-sensitive forms.

However, its Pass C conclusion:

`No genuinely new technical-substitution failure found beyond §3.4`

is not supported by the canonical r4 text because:

- the P06 headline still contains technical `土台`;
- the headline still has `自己教師`;
- P06 boundary contains `仕組みの消費`;
- P07A retains `30超の束`;
- additional shorthand listed above remains.

Thus r4 QA cannot yet support reader-publication validation.

## 8. Cumulative map update

Per the cumulative-map rule, the residual failures above have been added to the terminology authority.

New authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Map update commit:

`1b5184fda07afe4f8ffaff6124d09cfbfb364a1f`

Map blob:

`45d8eb53a14ab9a50dd6eab7b74326ad7108dc5e`

Terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R5_BINDING`

## 9. Required Draft r5 boundary

This remains a bounded Draft-only reader-surface cleanup.

Immutable:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Human Architecture r2 approval;
- Draft Packages;
- source set;
- main;
- Frozen Core.

Do not perform new research.

Revise only Draft Results / synthesis / language QA / r5 report / cumulative map if genuinely new failures are discovered.

## 10. Draft r5 acceptance criteria

Before returning to Sol:

1. P06 headline conforms to `self-supervised -> 自己教師あり` and no technical `土台`;
2. `言葉側だけを締める` is replaced by explicit tuning terminology;
3. `一対の判定に還す` is replaced by direct pairwise-objective wording;
4. `引用の結び / 典拠の結び / 手順の借り / 仕組みの消費` are rewritten directly;
5. contrastive-learning prose does not use `大量に当て / ペアの当て`;
6. fixed-class classification is not called `表引き`;
7. datasets/tasks are not called `束`;
8. `野外の補い`, sequence-`列に変える契約`, evaluation-`別の列`, and technical `渡し` shorthand are removed;
9. all cumulative-map blocking forms remain clean;
10. exact duplicates remain zero;
11. no re-padding;
12. source roles, Evidence refs, CLAIM_BOUNDARY semantics, and G01-G06/PARTIAL limitations remain intact;
13. no reader-publication validation / Publication Preview / Freeze / Release.

## 11. State boundary

Keep `DRAFT_COMPLETE`.

Terminal target:

`TS-003 DRAFT_R4_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R5_FINAL_READER_SURFACE_CLEANUP_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R5`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
