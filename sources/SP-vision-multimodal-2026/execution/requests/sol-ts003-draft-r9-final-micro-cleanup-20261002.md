# TS-003 execution instruction — Draft r9 final micro-cleanup

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R8_REQUEST_CHANGES / FOUR_EDIT_MICRO_CLEANUP_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r8:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r8.md`

Decision:

`REQUEST_CHANGES`

Reviewed r8 worker commit:

`45e1aae18883983bfb852ac95bfd78d6a4d2fcf1`

Reviewed r8 worker tree:

`d5113b2a2d58e8b016a2e3e74fc596c297625fd4`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Expected map blob:

`cf39a5860d64b5d85a3a382911680dcadaa954a1`

Expected map status:

`DRAFT_R9_BINDING`

Expected map terminal:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R9_BINDING`

Human Architecture r2 remains approved.

Publication candidate r1 remains stale.

No Human Publication Preview decision exists.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Frozen Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- terminology map blob == `cf39a5860d64b5d85a3a382911680dcadaa954a1`;
- terminology map status == `DRAFT_R9_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs: zero writes, report expected vs actual, stop.

No new branch, fallback/repair/review branch, reset, rebase, squash, cherry-pick, force push, or history rewrite.

## 3. Mandatory read order

1. this request;
2. `execution/sol-draft-review-r8.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r8.md`;
6. `execution/draft-r8-20261002/draft-r8-review-report.md`;
7. canonical r8 P03, P07B, P15 Draft Results;
8. all other canonical r8 Draft Results for regression-only verification;
9. canonical profile synthesis result;
10. unchanged Draft Packages;
11. approved Architecture r2.

## 4. Mission

Produce Draft r9 as a four-edit micro-cleanup.

Do not rewrite the volume.

Authorized reader-prose edits are only:

1. P03 b1 technical backbone wording;
2. P07B b6 tight/deep fusion wording;
3. P07B b6 detection-adaptation wording;
4. P15 b7 punctuation.

If another substantive terminology defect is discovered during the mandatory regression scan, do not broaden the repair silently. Add it to the cumulative map and stop for Sol unless it is an exact morphological/contextual equivalent of one of the four authorized defects.

## 5. Exact repair A — P03 backbone

Current:

`拡散の背骨としての来歴はTS-002の範囲として本書では扱わない。`

Repair the technical backbone concept using the preferred term.

Acceptable direction:

`拡散モデルのバックボーンとしての来歴はTS-002の範囲として本書では扱わない。`

Preserve the scope boundary exactly.

## 6. Exact repair B — P07B fusion mechanism

Current:

`特徴増強と言語誘導クエリ選択とcross-modalityデコーダの三段で固く混ぜる。`

Repair to direct fusion terminology.

Acceptable direction:

`特徴増強、言語誘導クエリ選択、cross-modalityデコーダの三段階で密に融合する。`

Use source-supported wording only.

Do not use `混ぜる / 固く混ぜる / 固い融合` as the mechanism name.

## 7. Exact repair C — P07B detection adaptation

Current:

`構成を足さず、学習手順で検出に渡す。`

Repair to direct adaptation/fine-tuning language.

Acceptable direction:

`追加モジュールなしで、学習手順のみを調整して検出へ適応させる。`

or, if more faithful to the source:

`追加モジュールなしで検出へファインチューニングする。`

Do not use `渡す` as the technical relation.

## 8. Exact repair D — P15 punctuation

Current:

`マルチモーダルの代表例で、、文と画像と音声と動画を入力し…`

Repair only the punctuation:

`マルチモーダルの代表例で、文と画像と音声と動画を入力し…`

Do not otherwise rewrite P15 b7.

## 9. Regression verification

After regeneration, verify:

- all other r8 reader prose is textually identical except the four authorized edits;
- canonical profile synthesis prose is textually identical to r8;
- all Draft Packages remain byte-identical;
- exact duplicate sentences remain 0 per package and cross-package;
- no internal workflow labels;
- all r8 bidirectional terminology classifications remain valid;
- all remaining `ボックス` are box/bounding-box semantics;
- all remaining `鎖` are allowed causal/coreference senses;
- all remaining `極` are ordinary adjective/adverb or approved P14 classification;
- `話し言葉 / 部品 / 橋 / 橋渡し` remain absent as blocking technical labels;
- technical backbone `背骨` = 0;
- fusion-mechanism `固く混ぜる / 固い混ぜ / 固い融合` = 0;
- technical `検出に渡す` = 0;
- punctuation anomalies `、、 / 。。 / ，， / ,,` = 0.

## 10. QA r9

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r9.md`

Include:

- map authority blob/status;
- exact four before/after repairs;
- proof that no other reader prose changed;
- duplicate scan;
- bidirectional terminology regression result;
- exact residual classification for box/chain/pole categories;
- punctuation-anomaly scan;
- source-role/boundary preservation;
- exact statement that synthesis prose remained unchanged.

## 11. r9 execution report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r9-20261002/draft-r9-review-report.md`

Report:

- startup guards;
- Sol r8 review authority;
- map start/final blob;
- unchanged Draft Package hashes;
- exact changed Draft Results and blocks;
- proof all other prose unchanged;
- synthesis hash/prose identity;
- terminology regression result;
- punctuation scan;
- duplicate scan;
- production state unchanged;
- stale publication candidate unchanged;
- Core blocker untouched;
- main/Core unchanged;
- final HEAD/tree.

## 12. Lifecycle boundary

Keep production state byte-identical at `DRAFT_COMPLETE`.

Do not:

- regenerate publication/PDF;
- run reader-publication validation;
- run stage validation;
- advance stage;
- create Human Publication Preview;
- Freeze;
- Release;
- modify historical checkpoints;
- attempt to repair Core checkpoint staleness.

## 13. Terminal

`TS-003 DRAFT_R9_FINAL_MICRO_CLEANUP_COMPLETE`

`TS-003 LANGUAGE_QA_R9_COMPLETE`

`PUBLICATION_CANDIDATE_R1_REMAINS_STALE`

`CORE_CHECKPOINT_STALENESS_UNCHANGED`

`AWAITING_SOL_DRAFT_REVIEW_R9`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
