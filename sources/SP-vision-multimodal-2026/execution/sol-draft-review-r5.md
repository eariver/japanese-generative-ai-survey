# TS-003 Sol Draft Review r5

Status: `SOL_DRAFT_REVIEW_R5 / REQUEST_CHANGES / P09_FINAL_TERMINOLOGY_CLOSURE`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed Draft r5 authority commit:

`2979026987e11cd52cf278432d111e83a64c573b`

Reviewed tree:

`101dead5e620698006647df7dab4d5479f7dc824`

Decision:

`REQUEST_CHANGES`

Draft r5 successfully closes the r4 findings in P06/P07A/P07B/P09/P11 and preserves all prior gains, but independent Sol review found a direct terminology-map miss in P09 plus a small cluster of related modality/deployment wording defects. Because these are reader-facing technical terms and one is an explicit existing-map violation, reader-publication validation must remain blocked.

The cumulative terminology map has been advanced for r6 at:

- commit `dec8b7c28efe5e224778222ffef5dc5155ccd09d`
- blob `bad61f051146b0ec0c3fd25d72d816b2de41c53b`
- terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R6_BINDING`

## 1. What passed

- r5 launch guards matched exactly.
- work branch advanced by one normal child commit.
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`.
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- lifecycle remains `DRAFT_COMPLETE`; Architecture Review approved; Publication Preview pending.
- all 16 canonical Draft Results are r5 / REVISED.
- exact duplicate sentence scan independently confirms zero duplicates in every package.
- all r4-targeted phrases were repaired:
  - P06 headline -> `Transformerと自己教師あり学習の基盤`;
  - P06 text-side tuning and sigmoid objective wording are direct;
  - P06 CLAIM_BOUNDARY no longer uses `手順の借り / 仕組みの消費 / 典拠の結び`;
  - P07A uses `対照学習 / 固定クラス分類 / 30以上のデータセット`;
  - P07B ODinW wording is direct;
  - P09 token-sequence wording is direct;
  - P11 uses a distinct evaluation axis rather than `別の列`.
- prior r1-r4 regression terms remain absent.
- Draft Packages remained unchanged.
- no new research was performed.

## 2. Blocking finding F1 — existing self-supervised terminology rule is still violated in P09

The map already defines:

`self-supervised -> 自己教師あり`

Canonical r5 P09 b4 still says:

- `BEATsは音全般の自己教師の入口を担う。`
- `音響トークナイザと音の自己教師を交互に鍛え`

These are not substring false positives from `自己教師あり`; they are bare `自己教師` used as the technical concept.

Required repair: use `自己教師あり学習` or another source-accurate established form.

This direct map miss is sufficient to block publication validation.

## 3. Blocking finding F2 — model family is rendered as 家族

Canonical r5 P09 b2 says:

`1Bから78Bの家族を用意し`

The intended concept is a model family / model series.

Required repair:

- `1Bから78Bのモデル群`;
- `1Bから78Bのモデルファミリー`;
- or `1Bから78Bのモデル系列`

as best supported by the bound Evidence.

Do not use human-family metaphor as the technical noun.

## 4. Blocking finding F3 — P09 still uses modality/input role as 入口

Canonical r5 P09 uses expressions such as:

- `Whisperは話し言葉の入口の前例である`;
- `BEATsは音全般の自己教師の入口を担う`;
- `音の入口を組み合わせて時刻で合わせるのがQwen3-Omniである`.

These are understandable but continue the same over-domestication pattern: the actual role is speech/audio input processing, representation learning, or an audio encoder path.

Required repair: name the actual modality/input role directly.

## 5. Blocking finding F4 — minor P09 technical shorthand

P09 b2 still contains:

- `稠密と混合専門家で末端からクラウドまで`;
- `三つの部品の積み重ねはコードの上で確かめられる`.

For the intended deployment range and architecture composition, prefer direct technical wording:

- `エッジデバイスからクラウドまで`;
- `三つの構成要素` / `アーキテクチャ構成`.

These are small, but r6 should close them while P09 is already being edited.

## 6. Non-blocking observations

- `自己教師あり` occurrences in P02/P05/P06/P14 are correct and must not be changed.
- ordinary literal `入口` is not globally prohibited; only modality/input-pipeline uses are targeted.
- P06 residual editorial language such as `橋渡し` or `柱` is not acting as the primary name of a technical mechanism in the reviewed contexts and is non-blocking.
- ordinary `流れ`, `枝`, `鎖` may remain when used for narrative organization rather than replacing a technical term.
- r5 length and zero-duplicate state are acceptable; do not re-pad.

## 7. Cumulative map update

The new explicit regression cases were added to:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

at commit:

`dec8b7c28efe5e224778222ffef5dc5155ccd09d`

with blob:

`bad61f051146b0ec0c3fd25d72d816b2de41c53b`

and terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R6_BINDING`.

## 8. Required Draft r6 boundary

This is a very small P09-centered Draft-only terminology closure.

Immutable:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Human Architecture approval;
- Draft Packages;
- source set;
- main;
- Frozen Core.

No new research.

Only Draft Results / synthesis / QA / r6 report / cumulative map if genuinely new failures are discovered may change.

## 9. Draft r6 acceptance criteria

Before returning to Sol:

1. no bare self-supervised-sense `自己教師`; approved `自己教師あり` remains;
2. model-family sense `家族` removed;
3. modality/input technical role is not named `入口`;
4. deployment sense `末端` normalized to edge terminology;
5. architecture-component sense `部品` normalized;
6. all cumulative R6 map blocking cases clean;
7. exact duplicates remain zero;
8. no re-padding;
9. source roles, Evidence refs, CLAIM_BOUNDARY semantics, G01-G06/PARTIAL limitations unchanged;
10. no reader-publication validation / Publication Preview / Freeze / Release.

## 10. State boundary

Keep `DRAFT_COMPLETE`.

Terminal target:

`TS-003 DRAFT_R5_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R6_P09_TERMINOLOGY_CLOSURE_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R6`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
