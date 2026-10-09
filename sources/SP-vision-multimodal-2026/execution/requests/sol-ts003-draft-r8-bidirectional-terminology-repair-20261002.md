# TS-003 execution instruction — Draft r8 bidirectional terminology repair

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R7_REQUEST_CHANGES / BOUNDED_BIDIRECTIONAL_TERMINOLOGY_REPAIR`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r7:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r7.md`

Decision:

`REQUEST_CHANGES`

Reviewed r7 worker commit:

`59f841121271d68154f9173d0826791215b261d4`

Reviewed r7 worker tree:

`d57d7e028fd316926fb63716c2e43d896a5a3638`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Expected map blob:

`fcc0c6224ac400a3f0f3ba42016d66190a67bfc9`

Expected map status:

`DRAFT_R8_BINDING`

Expected map terminal:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R8_BINDING`

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
- terminology map blob == `fcc0c6224ac400a3f0f3ba42016d66190a67bfc9`;
- terminology map status == `DRAFT_R8_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs: perform zero writes, report expected vs actual, stop.

No new branch, fallback/repair/review branch, reset, rebase, squash, cherry-pick, force push, or history rewrite.

## 3. Mandatory read order

Read:

1. this request;
2. `execution/sol-draft-review-r7.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r7.md`;
6. `execution/draft-r7-20261002/draft-r7-review-report.md`;
7. all 16 canonical r7 Draft Results;
8. canonical `draft/v2/profile-synthesis-result.json`;
9. canonical `draft/v2/profile-synthesis-input.json`;
10. unchanged Draft Packages;
11. approved Architecture r2.

Do not use the stale PDF/publication candidate as current reader authority.

## 4. Mission

Produce Draft r8 as a **minimal semantic terminology cleanup**.

Do not reopen research, selection, architecture, package design, depth allocation, or factual content.

Repair only:

- P13 blind `ボックス` replacements that are not bounding boxes;
- P13 lineage `鎖`;
- non-P14 technical-organizer `極 / 両極`;
- P09 technical `話し言葉` boundary;
- stale component/bridge metaphors in canonical profile synthesis;
- any exactly equivalent residual exposed by the required bidirectional audit.

No publication/PDF regeneration.

## 5. Required exact repairs

### 5.1 P13 non-box `ボックス`

Current wrong sentences include:

`見ることと考えることを別のボックスに閉じ込めず、一つの文の続きとして扱い…`

and:

`見ることと動かすことの間に別のボックスを置かず、一つのモデルで受けて出す。`

These are not bounding boxes.

Rewrite architecture relations directly.

Preferred direction:

- `視覚と推論を別系統に分離せず…`;
- `視覚入力から行動出力までを一つのモデルで扱う…`.

Preserve factual meaning.

### 5.2 P13 lineage `鎖`

Repair:

`鎖を通して見ると…`

to:

`この系譜を通して見ると…`

or direct equivalent.

Do not alter `共参照鎖` or ordinary causal `連鎖`.

### 5.3 Non-P14 `極 / 両極`

Repair these technical-organizer uses:

- P03: `ボックスなしの密な極`;
- P03 CLAIM_BOUNDARY same expression;
- P05: `特化型のもう一極`;
- P07B: `融合の両極`;
- P13: `OpenVLAはオープンウェイトで確かめられる極`;
- P15: `マルチモーダルの極`.

Name actual technical classification directly.

Examples:

- `ボックスに依存しない密な予測`;
- `別系統の特化型モデル`;
- `二つの融合方式`;
- `オープンウェイトで検証可能なVLAの事例`;
- `長いコンテキストを備えたマルチモーダルモデルの事例`.

P14 Architecture-defined `四つの極 / 四極` remains allowed.

Do not alter ordinary `極端` or `極めて`.

### 5.4 P09 speech/ASR boundary

Repair:

`Whisperの話は話し言葉の範囲に留まり、音全般の主張はしない。`

to a direct technical form such as:

`Whisperの話は音声認識の範囲に留まり、音全般の主張はしない。`

Preserve speech-vs-general-audio scope exactly.

### 5.5 Canonical profile synthesis

Canonical `profile-synthesis-result.json` currently contains:

- `個別学習済み部品の橋渡し`;
- `個別部品の組み立て`.

Repair to direct technical language, e.g.:

- `個別に事前学習した構成要素の接続`;
- `モジュール構成`.

Do not change synthesis claims beyond terminology.

If `四極` is retained in synthesis, confirm it is explicitly and correctly referring to P14's approved Architecture-defined four-pole classification. Otherwise rewrite to direct classification wording.

## 6. Bidirectional semantic audit

This is mandatory.

For each Section-2 preferred concept:

### Direction A — concept -> preferred form

Verify the concept uses the preferred term.

### Direction B — preferred form -> correct concept

Verify every occurrence of the preferred token actually represents that concept.

Examples:

- every bounding-box concept -> `ボックス`;
- every `ボックス` -> actually bounding-box/box semantics;
- every `アテンション` -> actually attention mechanism/map semantics;
- every `クエリ` -> actually model-query semantics;
- every `チェックポイント` -> model checkpoint, not internal pipeline checkpoint.

Do not infer correctness from string replacement alone.

## 7. Mandatory residual classifications

Explicitly enumerate and classify every remaining occurrence of:

- `ボックス`;
- `箱`;
- `鎖`;
- `極`;
- `話し言葉`;
- `部品`;
- `橋`;
- `橋渡し`.

For every occurrence, record:

- package/synthesis field;
- exact sentence;
- semantic class;
- allowed/blocking decision;
- reason.

Expected allowed examples include:

- P07B `共参照鎖`;
- P05 causal `連鎖`;
- P14 approved `四つの極`;
- ordinary `極端` / `極めて`.

There must be no unclassified hit.

## 8. Full cumulative registry audit

Re-run all known failures in the cumulative terminology map across:

- 16 canonical Draft Results;
- canonical profile synthesis result;
- headline/deck/body/CLAIM_BOUNDARY.

A PASS requires 0 blocking hits.

## 9. Preserve accepted substance

Must preserve:

- all factual claims;
- Evidence bindings;
- source/evaluator attribution;
- comparison constraints;
- P07A/P07B separation;
- P07B grouping/depth;
- P09 same-protocol/version-bound comparisons;
- P15 synthesis structure;
- CLAIM_BOUNDARY meaning;
- G01-G06/PARTIAL meaning;
- zero exact duplicates;
- no padding.

All Draft Packages byte-identical.

No new research or source additions.

## 10. QA r8

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r8.md`

Required:

- map authority blob/status;
- bidirectional Section-2 audit;
- exact residual classification table for `ボックス/箱/鎖/極/話し言葉/部品/橋/橋渡し`;
- full cumulative registry audit;
- package + synthesis scope proof;
- duplicate scan;
- source-role/boundary preservation;
- exact retained context exceptions;
- explicit statement that no preferred token is being used for a different underlying concept.

## 11. r8 execution report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r8-20261002/draft-r8-review-report.md`

Report:

- startup guards;
- Sol r7 review authority;
- map start/final blob;
- unchanged Draft Package hashes;
- exact changed Draft Results;
- exact changed synthesis fields;
- before/after sentences for every r8 repair;
- bidirectional audit result;
- residual occurrence classifications;
- duplicate result;
- source-role/boundary preservation;
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
- run advance-stage;
- create Human Publication Preview approval;
- Freeze;
- Release;
- modify historical Stage Checkpoints;
- attempt to work around Core checkpoint staleness.

## 13. Terminal

`TS-003 DRAFT_R8_BIDIRECTIONAL_TERMINOLOGY_REPAIR_COMPLETE`

`TS-003 LANGUAGE_QA_R8_COMPLETE`

`PUBLICATION_CANDIDATE_R1_REMAINS_STALE`

`CORE_CHECKPOINT_STALENESS_UNCHANGED`

`AWAITING_SOL_DRAFT_REVIEW_R8`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
