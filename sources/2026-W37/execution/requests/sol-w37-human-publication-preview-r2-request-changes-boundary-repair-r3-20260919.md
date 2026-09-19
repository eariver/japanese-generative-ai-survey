# W37 execution instruction — Human Publication Preview r2 REQUEST_CHANGES, narrow #434 repair through fresh Preview r3

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R2_REQUEST_CHANGES / CANONICAL_REVISION_PATH / NARROW_PUBLICATION_BOUNDARY_REPAIR / NO_CORE_CHANGE / BOUNDED_AT_FRESH_PUBLICATION_PREVIEW_R3`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W37-v2-work`

## 1. Human decision authority

The Human Owner has explicitly instructed that the W37 Publication Preview r2 Sol findings be repaired.

Record Publication Preview r2 as:

`REQUEST_CHANGES`

This is now a Human Publication Preview decision.

The requested change is narrowly bounded to the blocking finding in:

`sources/2026-W37/execution/reviews/sol-w37-publication-preview-r2-independent-review-20260919.md`

Blocking defect:

- Issue #434 semantic Publication Boundary leak: reader-facing Draft/TeX still narrates internal retrieval/production stopping behavior.

The Human does **not** request any new research, Architecture revision, evidence revision, package restructuring, or stylistic rollback.

Issue #507 timestamp provenance is already covered by the append-only correction ledger and is **not** an independent Draft/PDF regeneration reason.

## 2. Exact reviewed r2 authority

Publication Preview r2 reviewed production authority:

- reviewed production commit: `74400d716e703c12efee97707ff0ee97d47f98a8`
- publication candidate SHA-256: `8f74d379ccf7df181b8fbe0890d4774573f6c273c046ec44f15a80a184b3ab6b`
- PDF path: `surveys/weekly/2026-W37/main.pdf`
- PDF SHA-256: `c2298653e959388f359c5dadf0121e28684950343e874c2305179b4c0aa5f4fe`
- PDF bytes: `309850`
- PDF pages: `11`
- CI artifact: `10558181589`

Publication Preview r2 shell:

`sources/2026-W37/execution/reviews/publication-preview-r2.md`

Independent Sol r2 review:

`sources/2026-W37/execution/reviews/sol-w37-publication-preview-r2-independent-review-20260919.md`

Sol verdict:

`REQUEST_CHANGES`

## 3. Existing Human Gate history

Current canonical Human review index must remain historically intact:

1. Architecture Review r1:
   - `APPROVED`
   - reviewed production commit `55e700a34765654cd2ced0c2a454d4fb3433dd4f`
2. Publication Preview r1:
   - `REQUEST_CHANGES`
   - reviewed production commit `8057a468897f67d3a11bd9287f6f56f0485877ce`
   - regeneration boundary `ARCHITECTURE_ESTABLISHED`

The expected next Publication Preview Human review revision is therefore:

`2`

Verify from the actual review index before writing. Do not guess.

## 4. Invocation guard

The Muse invocation MUST provide the Exact Starting SHA/tree corresponding to the commit containing this request.

Before any write, read-only verify:

- remote W37 HEAD == Exact Starting SHA supplied by invocation;
- remote W37 tree == Exact Starting Tree supplied by invocation;
- Exact Starting SHA parent == `e207f329c132b461a12a26c65b891b739f664484`;
- parent tree == `ba6ed7d81b04e11c7a4746b4d375641b5290d8b4`;
- remote `main` HEAD == `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
- remote main tree == `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- Production State remains:
  - lifecycle `RELEASE_CANDIDATE`
  - next action `PUBLICATION_PREVIEW`
  - terminal `HUMAN_GATE_REACHED`
  - Architecture Review `approved`
  - Publication Preview `pending`;
- Architecture approval provenance remains byte-valid;
- Human Publication Preview r1 REQUEST_CHANGES record exists;
- no Human Publication Preview r2 review record exists yet;
- exact r2 candidate/PDF authority matches §2;
- independent Sol r2 review remains `REQUEST_CHANGES`;
- timestamp correction ledger exists:
  `sources/2026-W37/execution/provenance/w37-execution-time-correction-20260919.md`.

Any mismatch -> zero writes, report expected vs actual, STOP.

No new/fallback/repair/review/temp branch.
No force/reset/rebase/squash/history rewrite.

## 5. Core path — use canonical Human revision, no operator invalidation

Do not use:

`invalidate-pending-gate`

Do not use:

`revalidate-publication-surface`

Do not modify shared Core.

Use current canonical:

`survey_human_gate_v2.py request-publication-preview-revision`

with:

- gate: `PUBLICATION_PREVIEW`
- expected revision: `2`
- regeneration boundary: `ARCHITECTURE_ESTABLISHED`
- reviewed_by: `Human Owner`
- reviewed repository commit: `74400d716e703c12efee97707ff0ee97d47f98a8`
- requested changes:
  - remove reader-facing internal retrieval/production stopping narration under Issue #434;
  - preserve all r2 content/citation/language/provenance successes;
- review references:
  - this execution request;
  - `publication-preview-r2.md`;
  - `sol-w37-publication-preview-r2-independent-review-20260919.md`.

Use the **actual timezone-aware execution time** for the Human review record.

Do not supply a synthetic future timestamp.

A `Z` suffix may be used only for actual UTC.

After recording the Human decision, immediately read back:

- Publication Preview r2 Human review record;
- review index;
- Production State;
- Architecture approval record and provenance.

Required state:

- lifecycle `ARCHITECTURE_ESTABLISHED`;
- Architecture Review still `approved`;
- Publication Preview `pending`;
- Draft and downstream checkpoints reset to pending according to current Core;
- Human Preview r2 `REQUEST_CHANGES` preserved as revision 2;
- no Architecture reopen.

If Architecture approval is removed/reopened, STOP.

## 6. Frozen upstream authority

Do not modify or rerun:

- Grok/X;
- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Human Architecture approval.

Frozen values:

- Discovery: `14`
- Screening: `13 KEEP / 1 DROP`
- Evidence: `11 VERIFIED / 2 PARTIAL`
- Materiality: `12 MATERIAL / 1 CONTEXT / 1 EXCLUDED`
- Selection: `12 SELECTED / 1 HOLD`
- Architecture: `7 packages`
- Architecture SHA-256:
  `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`.

No fresh research.

## 7. Preserve all r2 repairs

Publication Preview r2 passed independent Sol review on all of the following and these must not regress:

### Natural technical Japanese — Issue #501

Preserve the r2 terminology and prose quality.

Do not reintroduce technical-use expressions such as:

- 模型 for AI model
- 符号 for code/token
- 道具立て for harness
- 代理人 for agent
- 砂場 for sandbox
- 給仕 for serving
- 引擎 for engine
- 許し for license
- 札 for model card
- 訳し for translation
- 混合専門家 for MoE
- 検出子 for IOC.

Continue using established technical terms:

- モデル
- コード / コーディング
- トークン
- エージェント
- エージェントハーネス
- サンドボックス
- サービング / 推論基盤
- エンジン
- ライセンス
- モデルカード
- 翻訳
- MoE / Mixture-of-Experts
- 評価用モデル
- IOC / 侵害指標.

### Reviewer provenance — Issue #506

All Worker-generated reviews remain truthfully attributed to:

`Worker/Agent (Muse Spark)`

or equivalent actual-runner identity.

Do not use:

- ChatGPT
- Sol
- Human
- independent reviewer

as worker identity.

### Citation / X behavior

Preserve:

- 19/19 cited bibliography integrity unless a legitimate wording edit changes citation placement;
- zero missing citation keys;
- zero unused bibliography records;
- 8 direct public X status URLs unless a legitimate reader edit changes the exact count;
- no internal GitHub blob URL;
- no repository-internal reader path;
- X as community/context only.

### Evidence / Architecture boundaries

Preserve:

- Financial Services / GPT-Live-1 / Agents API as distinct layers;
- DeepSeek comparison as vendor-reported;
- Sep 14 routing as future/post-window;
- Fusion exact publication time `2026-09-11T17:00:00Z`;
- Fusion 39% as maximum, not uniform;
- MiniCPM/North/Ling as vendor/card bounded;
- North license/judge boundary;
- Anthropic cases as vendor investigations;
- resignation discourse outside Architecture weight;
- GLM rumor excluded.

## 8. Narrow blocking repair — Issue #434

The r2 reader surface incorrectly exposes internal production/retrieval stopping mechanics.

### Known blocking example 1 — canonical Draft + TeX

Current r2 DeepSeek Draft/reader wording includes:

`ベンチマーク表や図の詳細は取得の打ち切りでたどり切れておらず`

This is not reader-relevant.

Required semantic meaning:

- benchmark table/figure detail was not independently or fully verified/covered by this edition;
- therefore conclusions remain bounded to the vendor summary.

Rewrite in natural reader-facing language without describing an internal retrieval cutoff.

Acceptable direction:

`本号ではベンチマーク表・図の詳細な検証までは行っておらず、評価手法はベンダー側の説明の範囲で扱う。`

Exact wording is editorial choice.

Do not falsely claim the detailed material does not exist.

### Known blocking example 2 — Sources & Limitations

Current wording includes:

`全文PDFやIOC、ベンチマーク手法の詳細、図表の値は参照の打ち切りで取り切れていない`

Rewrite as publication scope, for example:

`本号では全文PDFやIOC、ベンチマーク手法・図表の詳細までは扱わず、その範囲を超える主張は行わない。`

Again, exact wording is editorial choice.

### Whole-surface semantic sweep

Do not stop after replacing these two phrases.

Read all seven Draft Results, profile synthesis, frontmatter, Week in Review, Sources & Limitations, and reader-facing TeX for equivalent production-process narration.

Flag and remove reader-facing language that reveals:

- retrieval was stopped;
- collection was cut short;
- token/tool/time budget;
- source-consumption mechanics;
- internal execution limits;
- agent/tool failure;
- process-stage vocabulary.

Examples of semantic forms to examine:

- `取得の打ち切り`
- `参照の打ち切り`
- `途中で取得を止めた`
- `時間の都合で`
- `ツール制約で`
- `取り切れなかった` when it means internal process rather than an actual source limitation.

Allowed reader-facing expression:

- what was verified;
- what was not verified;
- what this edition covers/does not cover;
- source-specific uncertainty;
- independent reproduction status;
- evidence limitation.

The reader needs the **scope of verification**, not the internal reason production stopped.

## 9. Draft regeneration

Because the DeepSeek wording exists in canonical Draft r2, regenerate Draft from the unchanged approved Architecture.

Regenerate all seven Draft Results plus profile synthesis through the normal canonical Draft path.

This regeneration must be semantically conservative.

Expected differences should be narrowly limited to:

- #434 process-narration repair;
- incidental grammar/flow changes strictly necessary for natural Japanese.

Do not rephrase unrelated sections merely for variety.

Record representative r2 -> r3 wording changes in an edition-local Worker QA artifact.

## 10. Reader-boundary QA

Before TeX/PDF rendering, perform a dedicated Worker semantic Publication Boundary review.

Reviewer identity:

`Worker/Agent (Muse Spark)`

The review must explicitly answer:

1. Does the Draft expose internal pipeline states?
2. Does it narrate retrieval/collection stopping mechanics?
3. Does it expose tool/budget/time constraints?
4. Does it confuse “not verified by this edition” with “not present in the source”?
5. Does it preserve all genuine evidence limitations without internal-process narration?
6. Did #501 natural technical Japanese remain intact?
7. Did #506 reviewer provenance remain intact?

A lexical scan alone is insufficient.

Store the QA artifact edition-locally.

Do not claim it is Sol review.

## 11. Timestamp provenance — Issue #507

Read:

`sources/2026-W37/execution/provenance/w37-execution-time-correction-20260919.md`

Do not modify historical future-dated records merely to hide them.

For all **new** r3 records:

- use actual wall-clock time;
- use timezone-aware ISO-8601;
- if serializing with `Z`, convert actual time to UTC;
- do not use synthetic schedule-like round times;
- do not write a timestamp later than actual execution time.

Before committing any new Human/Worker review record, compare the timestamp against the actual current environment time.

After commit, verify the record timestamp is not later than the commit timestamp.

If this invariant cannot be met with current tooling, STOP before creating false provenance.

## 12. Rebuild downstream authority

After Draft r3:

1. canonical Draft validation;
2. regenerate reader-facing TeX/Bib;
3. lexical Publication Boundary check;
4. semantic Publication Boundary review;
5. Japanese-language QA;
6. CI PDF build;
7. pin exact PDF bytes;
8. rebuild reader manuscript;
9. deterministic checks/bundle;
10. reader-surface semantic review with truthful Worker provenance;
11. semantic/editorial review with truthful Worker provenance;
12. visual review with truthful Worker provenance;
13. stage validation;
14. create new Publication Candidate;
15. advance to `RELEASE_CANDIDATE`;
16. create fresh Publication Preview r3 shell/dossier;
17. STOP.

Do not reuse r2 PDF/candidate/review identities.

## 13. Publication Preview r3 dossier requirements

Report:

- Human Preview r2 REQUEST_CHANGES record path/revision/hash;
- actual Human decision timestamp and its timezone;
- Architecture approval preserved;
- Draft r3 identity;
- exact list of #434 semantic wording changes;
- whole-surface process-narration sweep result;
- confirmation #501 repairs remain;
- confirmation #506 Worker provenance remains;
- new timestamps are not future-dated;
- TeX/Bib identity;
- citation audit;
- X/public auditability;
- vendor/temporal boundary audit;
- new PDF path/SHA/bytes/pages;
- Worker semantic/editorial reviewer identity/result;
- Worker visual reviewer identity/result;
- Publication Candidate identity;
- current lifecycle/state;
- Human Preview r3 = `PENDING`;
- deviations from approved Architecture = none, unless STOP is required.

## 14. Shared-Core freeze — absolute

No changes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`.

Do not modify:

- `main`;
- `production/survey-core-v2`.

Generic issues:

- #434 semantic Publication Boundary hardening;
- #501 natural technical Japanese QA;
- #506 reviewer provenance;
- #507 timestamp provenance

remain future shared-Core concerns.

W37 repair is edition-local only.

## 15. Commit discipline

Existing W37 branch only.

Normal commits, non-force push, remote read-back.

No new branch.

No reset/rebase/squash/history rewrite.

Verify expected current remote HEAD before each meaningful write group.

## 16. Normal endpoint

Successful endpoint:

- Architecture Human Review remains APPROVED;
- Human Publication Preview r1 REQUEST_CHANGES preserved;
- Human Publication Preview r2 REQUEST_CHANGES preserved as revision 2;
- Draft r3 regenerated narrowly;
- semantic Publication Boundary leak removed;
- #501 natural Japanese still PASS;
- #506 reviewer provenance still PASS;
- new timestamps satisfy #507 invariant;
- new exact PDF/candidate established;
- lifecycle `RELEASE_CANDIDATE`;
- next action `PUBLICATION_PREVIEW`;
- terminal `HUMAN_GATE_REACHED`;
- fresh Publication Preview r3 = `PENDING`;
- no Human r3 decision;
- no Freeze;
- no Release;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0.

STOP there.

## 17. Final report

Report at least:

- Starting SHA/tree;
- Human Preview r2 REQUEST_CHANGES revision/path/hash;
- actual reviewed_at value + timezone validation;
- regeneration boundary;
- Architecture approval path/hash preserved;
- frozen upstream counts;
- Draft r3 identity;
- #434 before/after examples;
- process-narration sweep result;
- #501 regression check;
- #506 provenance check;
- #507 timestamp check;
- TeX/Bib identity;
- citation/X audit;
- PDF path/SHA/bytes/pages;
- semantic/editorial review identity/result;
- visual review identity/result;
- candidate SHA;
- fresh Preview r3 reviewed production commit/tree;
- ending HEAD/tree;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0;
- Human Preview r3 decision = PENDING;
- exact stop reason.
