# TS-003 Sol Reader / Publication Review r1

Status: `SOL_READER_PUBLICATION_REVIEW_R1 / REQUEST_CHANGES / PREFERRED_TERMINOLOGY_CONFORMANCE_REPAIR`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed publication-candidate commit:

`1f76b015c735f0164d97a67ab85d2da81948bf2f`

Reviewed tree:

`3129eb06ac34fadf211e6e9b1c2e57989b584fbc`

Candidate PDF:

`surveys/special/vision-multimodal-2026/main.pdf`

Candidate PDF SHA-256:

`9f27aeaebb5297c253bb2f709b9b2084d6562c5fb06dcc218467c0863c2b7cf9`

Candidate PDF size/page count:

`687583 bytes / 38 pages`

Decision:

`REQUEST_CHANGES`

The first publication materialization exposed a terminology-QA defect that was not sufficiently visible during Draft-only review. The problem is not research depth or architecture; it is failure to enforce the preferred-form side of the already binding Terminology Map, plus several additional technical calques discovered while auditing the publication surface.

The candidate PDF must not be presented as Human Publication Preview.

The cumulative terminology map has been strengthened for r7 at:

- commit `23ed5ed1deab9f3275b1a343a419f74e1b174ccf`
- blob `4674bca4f8164fa9fd371b51410ea078160be93d`
- terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R7_BINDING`

## 1. What passed

Independent checks confirm:

- candidate branch is one normal child of the authorized publication-validation start;
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- production state remains byte-identical at `DRAFT_COMPLETE`;
- Architecture Review remains approved;
- Publication Preview remains pending;
- no Freeze/Release/Human decision was created;
- reader manuscript / reader-surface gate / semantic review / deterministic quality bundle were generated;
- bibliography reports 111/111 accepted sources bound with no missing or unused citation;
- deterministic PDF preflight reports PASS;
- worker visual review reports all 38 pages inspected with no clipping, missing glyphs, collisions, broken tables, stranded headings, or blank pages;
- candidate build has no undefined citations/references or TeX layout warnings;
- Draft r6 content was transformed without factual expansion or new research.

These passes do not override the terminology defects below.

The exact PDF has not received independent Sol pixel-level acceptance because the current candidate is already editorially rejected on source-text grounds; its worker visual review remains evidence, not Human approval.

## 2. Blocking F1 — existing preferred terminology was not enforced

The binding map already states preferred forms, but canonical r6/publication prose uses nonpreferred domesticating synonyms.

### 2.1 box -> ボックス

Map:

`box / mask / coordinate -> ボックス / マスク / 座標`

Canonical reader prose contains technical `箱` 35 times, including:

- P02 headline: `箱から集合予測、開かれた語彙へ`;
- P02 deck/body detection boxes;
- P03 box/mask transition prose;
- P07B grounding/detection prose.

These are bounding-box concepts, not literal boxes.

Required repair: `ボックス`; first-use `バウンディングボックス（ボックス）` is allowed when it improves clarity.

### 2.2 open-vocabulary -> オープンボキャブラリー

Map:

`open-vocabulary -> オープンボキャブラリー`

Canonical prose contains:

- `開かれた語彙` ×4;
- `開いた語彙` ×6.

Required repair: `オープンボキャブラリー`.

### 2.3 decoder -> デコーダ

P07B still contains:

- `汎用復号`;
- `復号設計`.

In architecture/component context these mean decoder / decoder design.

Required repair: `汎用デコーダ`, `デコーダ設計`.

### 2.4 calibration-free -> キャリブレーション不要

P04 repeatedly uses `較正なし` as the technical label for DUSt3R's calibration-free property.

Required repair: `キャリブレーション不要` and direct `キャリブレーション` wording where needed.

### 2.5 scaling -> スケーリング

P06 uses `大規模化` for model/data scaling.

Required repair: `スケーリング` / evidence-accurate `大規模学習`.

### 2.6 open weights -> オープンウェイト

P09/P13 contain `開かれた重み` in the technical open-weights sense.

Required repair: `オープンウェイト`.

## 3. Blocking F2 — architecture/components still use domesticating nouns

The map already classified architecture-sense `部品` as a failure, yet six hits remain.

The most visible is the P08 headline:

`凍結した部品をつなぐ橋`

P08 also says:

- `部品の選び方`;
- `凍結した部品を使い回す考え方`.

Other technical `部品` occurrences need semantic repair, e.g. a model component should be `構成要素 / モジュール`, body parts should be `部位`, UI/HTML elements should be `要素`.

P08 headline additionally uses `橋` as the primary name of a technical transition. This conflicts with the anti-metaphor rule.

Required direction:

- name the actual connection/integration mechanism;
- e.g. a headline such as `凍結した視覚・言語モデルを接続する` or another Architecture-consistent direct form;
- do not merely replace `橋` with another metaphor.

## 4. Blocking F3 — unregistered but standard technical terms are still calqued/domesticated

The publication audit identified the following concepts that must now use established technical forms.

### 4.1 attention

- P09: `窓注意` -> `ウィンドウアテンション`;
- P06 technical attention map/mechanism -> `アテンション / アテンションマップ`.

Ordinary Japanese `注意` meaning caution remains valid.

### 4.2 query

Q-Former model queries are written as:

- `問い合わせベクトル`;
- `問い合わせ選択`;
- `問い合わせ部`.

Required: `クエリベクトル / クエリ`.

Ordinary user/system inquiries remain `問い合わせ`.

### 4.3 ResNet shortcut

P01:

`次元が一致する箇所の近道`

Required: `ショートカット接続`.

Other ordinary shortcut/heuristic uses of `近道` are contextually allowed.

### 4.4 detector one-stage/two-stage

P02/P07B use `一段 / 二段` as detector architecture names.

Required: `one-stage / two-stage` with an optional first-use Japanese explanation.

Learning stage descriptions such as 第一段階/第二段階 are unaffected.

### 4.5 feature map

P02 uses `特徴量地図`.

Required: `特徴マップ`.

### 4.6 dual encoder / two-tower

P07A/P09 use `二塔 / 塔` as the architecture name.

Required: `デュアルエンコーダ` or `two-tower`, consistently.

### 4.7 Mixture-of-Experts / dense model

P09 contains:

- `混合専門家`;
- `稠密と混合専門家`.

Required:

- `Mixture-of-Experts（MoE）` then `MoE`;
- `denseモデル / dense構成` for the dense counterpart.

### 4.8 cold start

P09 uses `冷間始動`.

Required: `コールドスタート`.

### 4.9 model checkpoint

P09 uses `検査点の変換`.

Required: `チェックポイントの変換`.

### 4.10 trainable parameters

P08 uses `学習変数`.

Required: `学習可能パラメータ` or `trainable parameters` on first use.

### 4.11 model/configuration variant

Technical `変種` is used repeatedly for model/configuration variants.

Required: `バリアント` or source-accurate `派生モデル`.

### 4.12 category

P07A/P07B use `範疇` for ML/CV category.

Required: `カテゴリ`, `ベースカテゴリ`, `novelカテゴリ`, etc.

### 4.13 masked labels

P09 BEATs uses:

`覆った離散ラベル`

Required: `マスクされた離散ラベル`.

### 4.14 speech/ASR

P09 repeatedly uses `話し言葉` as the primary technical label for speech/ASR.

Use `音声` / `音声認識（ASR）` where the concept is the speech modality or recognition task. Ordinary prose describing spoken language remains allowed when it is semantically needed.

## 5. Blocking F4 — transition/lineage metaphors remain primary organizers

A small number of repeated metaphors still act as primary technical labels:

- P02/P03/P04/P08: technical transition as `橋 / 橋渡し`;
- P13: `七つの記録を一本の鎖として読む`, repeated `鎖のなか`.

These should be replaced with direct terms such as:

- connection;
- integration;
- extension;
- transition;
- lineage;
- staged progression;

rendered in established Japanese technical prose.

Literal bridges/chains or ordinary incidental metaphor are not globally banned.

P14's Architecture-defined `四つの極` remains an explicit exception.

## 6. Blocking F5 — QA methodology defect

r6 QA claimed full map conformance, but the reader surface still contained dozens of nonpreferred forms for concepts already listed in Section 2.

Therefore:

`zero known Avoid strings != terminology conformance`.

The cumulative map now makes the rule explicit:

- preferred form is normative;
- Pass A is semantic concept-level conformance, not a blacklist scan;
- headlines/decks have the same terminology authority as body text;
- any retained nonpreferred form needs exact-sentence context-exception justification.

The next QA must produce a full Section-2 conformance table, not only regression-string counts.

## 7. Separate blocker F6 — Core checkpoint staleness

The worker correctly reported a separate fail-closed Core issue.

Stage validation stopped with:

`Stage Checkpoint artifact drift: draft-result:P01 ... P15, synthesis-input, synthesis-result`.

Independent Sol code inspection confirms why:

- the historical Draft checkpoint binds r1 Draft Result/synthesis bytes;
- r2-r6 were Sol-authorized bounded repairs while lifecycle remained `DRAFT_COMPLETE`;
- Frozen Core validates historical checkpoint-bound artifacts as byte-identical;
- the only implemented supersession mechanism is publication-surface revalidation;
- that mechanism explicitly requires `VALIDATED_DRAFT` and only supersedes publication-surface roles.

Therefore no sanctioned current-Core operation can rebind reviewed r6/r7 Draft Results while still at `DRAFT_COMPLETE`.

Do not rewrite or overwrite the historical `ARCHITECTURE_ESTABLISHED.json` checkpoint.

Do not fake stage-contract PASS.

This shared-Core defect will be handled separately after the reader prose is stable.

## 8. Candidate PDF status

The 38-page PDF candidate is a useful build/formatting proof, but it is superseded for editorial review by this REQUEST_CHANGES decision.

Its deterministic and worker visual checks may be reused only as historical evidence, not as approval of future PDF bytes.

No Human Publication Preview decision may be recorded from this candidate.

## 9. Required r7 boundary

Draft r7 is a terminology-only conformance repair.

Immutable:

- research/source set;
- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Human Architecture approval;
- all Draft Packages;
- factual claims;
- source/evaluator attribution;
- CLAIM_BOUNDARY semantics;
- G01-G06/PARTIAL semantics;
- main;
- Frozen Core.

No new research.

Revise reader wording only.

Existing publication candidate r1 is stale after r7 and must not be treated as current authority.

Do not regenerate publication in the r7 Draft repair execution; return first for Sol Draft r7 review.

## 10. r7 acceptance criteria

Before returning to Sol:

1. full Section-2 preferred-form semantic audit completed for all 16 results + synthesis;
2. technical `箱` eliminated in favor of `ボックス`;
3. open-vocabulary paraphrases normalized to `オープンボキャブラリー`;
4. decoder/calibration/scaling/open-weights direct violations repaired;
5. architecture-sense `部品` repaired;
6. primary technical `橋 / 鎖` metaphors removed;
7. attention/query/shortcut/detector-stage/feature-map/dual-encoder/MoE/dense/cold-start/checkpoint/trainable-parameter/category/masked-label/speech terminology normalized;
8. every retained nonpreferred-looking hit has exact-sentence context-exception evidence;
9. no new metaphorical synonym is introduced;
10. zero exact duplicates remains true;
11. no padding;
12. source roles/boundaries/comparisons remain intact;
13. no publication regeneration;
14. no stage validation/advance;
15. no Human Preview/Freeze/Release.

Terminal:

`TS-003 READER_PUBLICATION_R1_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R7_PREFERRED_TERMINOLOGY_CONFORMANCE_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R7`

`PUBLICATION_CANDIDATE_R1_STALE`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
