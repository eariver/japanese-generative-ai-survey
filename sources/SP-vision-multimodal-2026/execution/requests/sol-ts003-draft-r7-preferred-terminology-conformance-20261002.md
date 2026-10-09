# TS-003 execution instruction — Draft r7 preferred-terminology conformance repair

Status: `EXECUTION_AUTHORITY / SOL_READER_PUBLICATION_R1_REQUEST_CHANGES / FULL_PREFERRED_TERMINOLOGY_CONFORMANCE_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Reader / Publication Review r1:

`sources/SP-vision-multimodal-2026/execution/sol-reader-publication-review-r1.md`

Decision:

`REQUEST_CHANGES`

Rejected publication candidate authority:

`1f76b015c735f0164d97a67ab85d2da81948bf2f`

Rejected candidate tree:

`3129eb06ac34fadf211e6e9b1c2e57989b584fbc`

Rejected candidate PDF SHA-256:

`9f27aeaebb5297c253bb2f709b9b2084d6562c5fb06dcc218467c0863c2b7cf9`

Accepted factual Draft basis before terminology-only repair:

`a345358f568e5ab7b55798c1f8469378abbd5783`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Terminology authority update commit:

`23ed5ed1deab9f3275b1a343a419f74e1b174ccf`

Expected map blob SHA:

`4674bca4f8164fa9fd371b51410ea078160be93d`

Expected map status:

`DRAFT_R7_BINDING`

Expected map terminal:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R7_BINDING`

Human Architecture r2 remains APPROVED.

No Human Publication Preview decision exists.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Frozen Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- terminology map blob == `4674bca4f8164fa9fd371b51410ea078160be93d`;
- terminology map status == `DRAFT_R7_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

Also confirm the rejected publication candidate exists but is not bound by a Human approval.

If any guard differs: perform zero writes, report expected vs actual, stop.

No new branch, fallback/repair/review branch, reset, rebase, squash, cherry-pick, force push, or history rewrite.

## 3. Mandatory read order

Read in this order:

1. this request;
2. `execution/sol-reader-publication-review-r1.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/sol-draft-review-r6.md`;
6. `execution/language-qa-ja-draft-r6.md`;
7. all 16 canonical Draft r6 Results;
8. profile synthesis input/result;
9. rejected publication candidate `main.tex` only as evidence of what became visible at publication scale;
10. approved Architecture r2;
11. unchanged Draft Packages.

Do not treat the rejected PDF's PASS-shaped worker artifacts as Sol editorial approval.

## 4. Mission

Produce Draft r7 as a terminology-only reader-surface repair.

This is not a research, architecture, selection, evidence, or factual-content revision.

The principal defect is that prior QA enforced the Avoid side of the Terminology Map much more strongly than the Preferred side. r7 must enforce **semantic preferred-form conformance** across all reader prose.

Revise:

- canonical Draft Results where terminology changes are required;
- profile synthesis only if affected reader terminology is present;
- cumulative map only if a genuinely new equivalent failure is discovered;
- r7 QA/report artifacts.

Do not regenerate publication/PDF during this execution.

The existing 38-page publication candidate becomes stale as soon as r7 reader prose changes.

## 5. Mandatory preferred-form repairs

### 5.1 Bounding boxes

Every technical CV use of `箱` that means a bounding box/box must become:

- `ボックス`; or
- at first use where useful, `バウンディングボックス（ボックス）`.

Audit all current hits, including headlines/decks.

Do not blindly replace literal boxes if any exist; classify every hit semantically.

### 5.2 Open vocabulary

Normalize:

- `開かれた語彙`;
- `開いた語彙`;
- equivalent domesticating paraphrases

to:

`オープンボキャブラリー`.

Do not alter ordinary descriptions of genuinely open-ended natural language that are not the open-vocabulary technical concept.

### 5.3 Decoder / calibration / scaling / open weights

Normalize technical contexts:

- `汎用復号` -> `汎用デコーダ`;
- `復号設計` -> `デコーダ設計`;
- calibration-free `較正なし` -> `キャリブレーション不要`;
- scaling `大規模化 / 規模化` -> `スケーリング` or source-accurate `大規模学習`;
- open-weights `開かれた重み` -> `オープンウェイト`.

### 5.4 Architecture components

Audit every `部品`.

When it names a model/software/architecture component:

- `構成要素`;
- `モジュール`;
- or the actual component name.

When it means body parts, use `部位`.

When it means UI/HTML components/elements, use `要素`.

P08 headline must not remain:

`凍結した部品をつなぐ橋`.

Use a direct technical title describing connection/integration of frozen vision and language components/models.

### 5.5 Technical transition metaphors

Audit `橋 / 橋渡し`.

When the phrase is the primary name of a technical transition/interface role, rewrite it directly:

- connection;
- integration;
- extension;
- transition;
- applicability expansion;
- predecessor role.

Do not introduce another metaphor.

Ordinary incidental explanatory metaphor may remain only with explicit technical concept in the same sentence and must be justified in QA.

### 5.6 Model-lineage chain metaphor

P13 uses:

- `一本の鎖`;
- `鎖のなか`;
- equivalent lineage-chain wording.

Replace with:

- `系譜`;
- `段階的な変化`;
- `連続する変化`;

as context requires.

Literal/coreference chains elsewhere are not targeted.

### 5.7 Attention

Technical attention mechanisms/maps must use:

- `アテンション`;
- `ウィンドウアテンション`;
- `アテンションマップ`.

Repair `窓注意` and technical mechanism uses of `注意`.

Ordinary caution/attention in prose remains ordinary Japanese.

### 5.8 Query

Q-Former/Transformer model queries must use:

- `クエリ`;
- `クエリベクトル`.

Repair:

- `問い合わせベクトル`;
- `問い合わせ選択`;
- `問い合わせ部`.

Ordinary user/system inquiry wording is not targeted.

### 5.9 ResNet shortcut

Repair ResNet mechanism sense:

`近道` -> `ショートカット接続`.

Ordinary shortcut/heuristic uses elsewhere remain contextually allowed.

### 5.10 one-stage / two-stage detector

Detector architecture terminology must use:

- `one-stage`;
- `two-stage`;

with a first-use explanatory Japanese gloss if desired.

Do not call the detector families simply `一段 / 二段`.

Ordinary 第一段階/第二段階 learning-process descriptions are unaffected.

### 5.11 Feature map

Technical feature-map terminology:

`特徴量地図 / 特徴地図` -> `特徴マップ`.

### 5.12 Dual encoder / two-tower

Architecture terminology:

`二塔 / 塔` -> `デュアルエンコーダ` or `two-tower`.

Choose one primary form and keep the volume consistent.

### 5.13 MoE / dense model

Normalize:

- `混合専門家` -> `Mixture-of-Experts（MoE）`, then `MoE`;
- dense-model `稠密` -> `denseモデル / dense構成`.

Do not alter ordinary dense prediction terminology already separately defined.

### 5.14 Cold start

`冷間始動` -> `コールドスタート`.

Preserve the limitation that the 234 ms number is theoretical, not a measured deployment latency.

### 5.15 Model checkpoint

`検査点` -> `チェックポイント` when referring to model checkpoints.

Do not expose internal production checkpoints.

### 5.16 Trainable parameters

`学習変数` -> `学習可能パラメータ` or first-use `trainable parameters`.

Preserve the exact quantitative relationship from the bound source.

### 5.17 Model/config variant

Model/configuration `変種` -> `バリアント` or `派生モデル`.

Ordinary biological/linguistic uses, if any, are unaffected.

### 5.18 Category

ML/CV taxonomy `範疇` -> `カテゴリ`.

Use precise forms where known:

- `ベースカテゴリ`;
- `novelカテゴリ`;
- `レアカテゴリ`;
- etc.

### 5.19 Masked labels

BEATs mechanism:

`覆った離散ラベル` -> `マスクされた離散ラベル`.

### 5.20 Speech / ASR

When `話し言葉` is serving as the primary technical label for the speech modality or ASR task, use:

- `音声`;
- `音声認識（ASR）`.

Preserve the important scope distinction between speech and general audio.

Do not broaden Whisper claims to general audio.

## 6. Full Section-2 conformance table is mandatory

The r7 QA must contain a row for **every Section 2 terminology-map concept**, not just concepts changed in r7.

For each concept record:

- preferred form;
- current canonical occurrence count if meaningful;
- nonpreferred candidate hits;
- semantic classification;
- exact retained exception sentence(s), if any;
- verdict.

A row cannot PASS merely because the literal Avoid strings are zero.

If the technical concept is expressed using a different synonym/paraphrase than the preferred form, classify it.

Headlines and decks must be included.

## 7. Full known-failure registry re-audit

Run the entire cumulative registry (§3.1 onward), not only the r7 additions.

For each hit classify:

- `TECHNICAL_SUBSTITUTION_BLOCKING`;
- `ORDINARY_JAPANESE_ALLOWED`;
- `SOURCE_QUOTE_OR_FIXED_NAME`;
- `NOT_APPLICABLE`.

Every `ORDINARY_JAPANESE_ALLOWED` entry must include exact sentence + reason.

## 8. Manual semantic pass

After automated scans, read all 16 r7 results + synthesis + boundaries as technical Japanese.

Specifically ask for every sentence/headline:

- Is a standard ML/CV/robotics/multimodal term being replaced by an everyday Japanese noun?
- Is a katakana/English technical term that the field normally uses translated into a literary kanji phrase?
- Is a metaphor acting as the primary name of a mechanism/architecture/interface/evaluator?
- Did a repair invent a new synonym instead of using the map's preferred term?

If a new failure is found:

1. add it to the cumulative map first;
2. repair all occurrences;
3. rerun the entire Section-2 table + registry audit;
4. record final map blob.

## 9. Preserve accepted substance

Must preserve:

- all factual claims;
- all Evidence bindings;
- all source/evaluator attribution;
- all comparison constraints;
- P07A vs P07B separation;
- P07B mechanism depth;
- P09 same-protocol/version-bound comparisons;
- P15 synthesis structure;
- CLAIM_BOUNDARY semantics;
- G01-G06/PARTIAL semantics;
- exact duplicate count 0;
- no padding.

No new research.

Do not add sources.

Do not change Architecture.

All Draft Packages must remain byte-identical.

## 10. Existing publication candidate

The current files under:

`surveys/special/vision-multimodal-2026`

and:

`sources/SP-vision-multimodal-2026/publication/v2`

belong to rejected publication candidate r1.

During r7 Draft repair:

- do not regenerate them;
- do not delete them;
- do not treat them as current publication authority after r7;
- record them as `STALE_AFTER_DRAFT_R7` in the r7 report.

A later execution will regenerate publication from Sol-accepted r7.

## 11. Core stage-contract blocker

Do not attempt to repair the Core checkpoint-staleness problem in this edition execution.

Do not:

- rewrite `ARCHITECTURE_ESTABLISHED.json`;
- modify historical checkpoint provenance;
- fake a validation PASS;
- use publication-surface revalidation at DRAFT_COMPLETE;
- advance lifecycle.

The Core blocker is a separate shared-Core issue to be handled after final reader prose is stable.

## 12. Language QA r7

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r7.md`

Required sections:

- map authority path/blob/status;
- full Section-2 preferred-form semantic conformance table;
- full cumulative known-failure registry audit;
- headline/deck-specific audit;
- box/open-vocabulary audit;
- decoder/calibration/scaling/open-weights audit;
- component/bridge/lineage audit;
- attention/query/shortcut audit;
- one-stage/two-stage audit;
- feature-map/dual-encoder audit;
- MoE/dense audit;
- cold-start/checkpoint/trainable-parameter audit;
- variant/category audit;
- masked-label/speech audit;
- exact duplicate scan by package and cross-package;
- source-role and boundary audit;
- new failures discovered + map updates;
- exact retained exceptions.

Regex counts alone are insufficient.

## 13. Required r7 execution report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r7-20261002/draft-r7-review-report.md`

Report:

- startup guards;
- Sol publication review authority;
- map start/final blob and status;
- unchanged Draft Package hashes;
- changed Draft Result inventory;
- exact reader-text changes by package;
- synthesis changes;
- full terminology-conformance result;
- duplicate scan;
- source-role/boundary preservation;
- G01-G06/PARTIAL preservation;
- existing publication candidate marked stale;
- Core blocker left untouched;
- production state unchanged;
- main/Core unchanged;
- final HEAD/tree.

## 14. Lifecycle boundary

Keep production state byte-identical at:

`DRAFT_COMPLETE`.

Do not run reader-publication regeneration.

Do not run DRAFT_COMPLETE -> VALIDATED_DRAFT validation.

Do not advance stage.

Do not create Human Publication Preview.

Do not Freeze/Release.

## 15. Terminal condition

`TS-003 DRAFT_R7_PREFERRED_TERMINOLOGY_CONFORMANCE_COMPLETE`

`TS-003 LANGUAGE_QA_R7_COMPLETE`

`PUBLICATION_CANDIDATE_R1_STALE_AFTER_DRAFT_R7`

`CORE_CHECKPOINT_STALENESS_UNCHANGED`

`AWAITING_SOL_DRAFT_REVIEW_R7`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
