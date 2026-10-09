# TS-003 execution instruction — Draft r5 to Draft r6 P09 terminology closure

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R5_REQUEST_CHANGES / P09_TERMINOLOGY_CLOSURE_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r5:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r5.md`

Decision:

`REQUEST_CHANGES`

Reviewed Draft r5 authority commit:

`2979026987e11cd52cf278432d111e83a64c573b`

Reviewed tree:

`101dead5e620698006647df7dab4d5479f7dc824`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Authority update commit:

`dec8b7c28efe5e224778222ffef5dc5155ccd09d`

Expected map blob SHA:

`bad61f051146b0ec0c3fd25d72d816b2de41c53b`

Expected map terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R6_BINDING`

Human Architecture r2 remains APPROVED.

This request does not reopen Architecture and is not a new Human gate.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- cumulative terminology map blob == `bad61f051146b0ec0c3fd25d72d816b2de41c53b`;
- cumulative terminology map terminal state == `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R6_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- current Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, squash, force push, or history rewrite is authorized.

## 3. Mandatory read order

Read:

1. this request;
2. `execution/sol-draft-review-r5.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r5.md`;
6. `execution/draft-r5-20261002/draft-r5-review-report.md`;
7. canonical Draft r5 P09 result;
8. all other canonical Draft r5 Results for regression-only verification;
9. current profile synthesis;
10. approved Architecture r2;
11. unchanged Draft Packages;
12. frozen Core Draft schema/prompt/non-mutating validators.

Do not treat Worker r5 `PASS_WITH_NOTES` as Sol approval.

## 4. Mission

Produce Draft r6 as a narrowly bounded P09 terminology closure.

Do not rewrite the volume globally.

Primary editing scope:

- P09 Draft Result;
- synthesis inputs/results only as mechanically required by canonical regeneration;
- QA/report artifacts;
- cumulative map only if a genuinely new failure is discovered.

Other Draft Results should remain semantically and textually unchanged unless canonical tooling necessarily regenerates metadata. If any non-P09 reader text changes, report the exact reason and diff.

Do not rerun or modify:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Architecture approval.

No new sources or facts from memory/web.

Keep all 16 Draft Package files byte-identical.

Preserve r1-r5 as immutable Git history.

## 5. Mandatory P09 repairs

### 5.1 self-supervised terminology

Repair:

- `BEATsは音全般の自己教師の入口を担う`;
- `音響トークナイザと音の自己教師を交互に鍛え`.

Use `自己教師あり学習` / `自己教師あり` according to source context.

Do not alter correct `自己教師あり` occurrences elsewhere.

### 5.2 model family

Repair:

`1Bから78Bの家族を用意し`

to direct technical wording such as:

- `1Bから78Bのモデル群`;
- `モデルファミリー`;
- `モデル系列`.

Use the form best supported by bound Evidence and volume terminology.

### 5.3 modality/input role

Repair modality/input-pipeline uses of `入口`, including:

- `Whisperは話し言葉の入口の前例である`;
- `BEATsは音全般の…入口を担う`;
- `音の入口を組み合わせて時刻で合わせるのがQwen3-Omni`.

State the actual technical role directly:

- speech/audio input processing;
- audio representation learning;
- audio encoder;
- modality input path;
- temporal synchronization.

Do not replace `入口` with another metaphor.

### 5.4 deployment/architecture wording

Repair:

- deployment sense `末端からクラウドまで` -> `エッジデバイスからクラウドまで` or equivalent established terminology;
- architecture sense `三つの部品の積み重ね` -> `三つの構成要素` / `アーキテクチャ構成`.

## 6. Full cumulative-map re-audit

Even though editing is P09-centered, rerun full map Pass A/B/C on all 16 canonical r6 reader surfaces after regeneration.

Important self-supervised audit:

- search bare `自己教師` semantically;
- classify `自己教師あり` as approved, not blocking;
- ensure no bare self-supervised-sense `自己教師` remains anywhere.

If a genuinely new failure is found:

1. add it to the cumulative map first;
2. repair all occurrences;
3. rerun Pass A/B/C;
4. report the final map blob SHA.

Do not silently fix without map update.

## 7. Preserve prior gains

Preserve:

- zero exact duplicates;
- no re-padding;
- all r1-r5 repairs;
- P06 direct headline/mechanism/boundary wording;
- P07A direct contrastive-learning wording;
- P07B segmentation and ODinW wording;
- P11 distinct evaluation-axis wording;
- source/evaluator roles;
- CLAIM_BOUNDARY semantics;
- P07B grouping;
- P09 sanctioned same-protocol comparisons;
- P15 synthesis density;
- G01-G06/PARTIAL semantics.

## 8. Language QA r6

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r6.md`

Include:

- map authority path/blob/status;
- exact duplicate scan by package and cross-package;
- full cumulative-map conformance;
- exact bare-`自己教師` semantic audit across all packages;
- P09 model-family audit;
- P09 modality/input-`入口` audit;
- P09 edge/cloud terminology audit;
- P09 architecture-component terminology audit;
- any non-P09 reader-text changes and rationale;
- source-role and CLAIM_BOUNDARY audit;
- new failures discovered, if any, plus map update.

## 9. Deterministic validation

Run available canonical non-mutating Draft Result and synthesis validators at `DRAFT_COMPLETE`.

Do not fake lifecycle rollback.

Do not call reader-publication validation.

## 10. Required r6 review report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r6-20261002/draft-r6-review-report.md`

Report:

- startup guards;
- reviewed r5 commit/tree;
- Sol r5 review authority;
- map starting blob/status;
- map changes if any + final blob;
- unchanged Draft Package hashes;
- Draft Result hashes;
- exact P09 reader-text changes;
- any non-P09 reader-text changes;
- duplicate scan;
- cumulative terminology audit;
- self-supervised audit;
- source-role/CLAIM_BOUNDARY preservation;
- G01-G06/PARTIAL preservation;
- QA r6 path/hash/status;
- deterministic validation result;
- lifecycle/next_action;
- Publication Preview pending;
- main/Core unchanged;
- final HEAD/tree.

## 11. Lifecycle boundary

Keep `DRAFT_COMPLETE`.

Do not:

- call reader-publication validation;
- create Publication Preview;
- record Human Publication Preview decision;
- Freeze;
- Release.

## 12. Terminal condition

`TS-003 DRAFT_R6_P09_TERMINOLOGY_CLOSURE_COMPLETE`

`TS-003 LANGUAGE_QA_R6_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R6`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
