# W37 execution instruction — Sol Publication Preview r1 REQUEST_CHANGES, regenerate Draft through fresh Preview r2

Status: `EXECUTION_AUTHORITY / SOL_PUBLICATION_PREVIEW_R1_REQUEST_CHANGES / OPERATOR_INVALIDATE_UNPRESENTED_PREVIEW / REGENERATE_FROM_ARCHITECTURE_ESTABLISHED / BOUNDED_AT_FRESH_PUBLICATION_PREVIEW_R2`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W37-v2-work`

## 1. Authority and decision semantics

This request imports the actual independent Sol Publication Preview r1 review:

`sources/2026-W37/execution/reviews/sol-w37-publication-preview-r1-independent-review-20260919.md`

Sol verdict:

`REQUEST_CHANGES`

This is **not** a Human Publication Preview decision.

The r1 Publication Preview was not presented for Human judgment after independent Sol review found blocking defects.

Therefore:

- Human Publication Preview remains `PENDING`;
- do not create a Human `REQUEST_CHANGES` record;
- do not use `request-publication-preview-revision`;
- invalidate the unpresented pending r1 surface with the canonical operator pending-gate invalidation path;
- regenerate a fresh Publication Preview r2;
- stop with r2 still awaiting independent Sol review and Human judgment.

Human Architecture approval remains valid and immutable.

## 2. Invocation guard

The Muse invocation MUST supply the exact current remote HEAD/tree after this execution request is committed.

Before any write, read-only verify:

- remote `weekly/2026-W37-v2-work` HEAD == Exact Starting SHA supplied by invocation;
- remote W37 tree == Exact Starting Tree supplied by invocation;
- Exact Starting SHA parent == `39c0d27a1240258b950ae9d0897d5b7f3c346453`;
- parent tree == `abe85f6a88cccd6efd4fd543f3566cc6d7be5944`;
- remote `main` HEAD == `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
- remote main tree == `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- current Production State remains:
  - lifecycle `RELEASE_CANDIDATE`
  - next action `PUBLICATION_PREVIEW`
  - terminal `HUMAN_GATE_REACHED`
  - Architecture Review `approved`
  - Publication Preview `pending`;
- canonical Architecture approval remains:
  - review record `sources/2026-W37/gates/reviews/architecture-r1.json`
  - decision `APPROVED`
  - reviewed production commit `55e700a34765654cd2ced0c2a454d4fb3433dd4f`
  - Architecture SHA-256 `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`;
- Publication Preview r1 exact reviewed authority remains:
  - production commit `8057a468897f67d3a11bd9287f6f56f0485877ce`
  - PDF path `surveys/weekly/2026-W37/main.pdf`
  - PDF SHA-256 `08ceb5e9c90b2bf25541bb61e6b14e5b2cdc7fe48635d85c5ab798606b88fd4d`
  - bytes `301238`
  - pages `10`
  - candidate SHA-256 `1dfb87957cbab69e30c08a45c66e72b28c72d74d1272a3c3815ab6844445bef6`;
- independent Sol r1 review exists and still says `REQUEST_CHANGES`.

Any mismatch -> zero writes, report expected vs actual, STOP.

No alternate/fallback/repair/review/temp branch.

No force/reset/rebase/squash/history rewrite.

## 3. Mandatory read order

Read at minimum:

1. this request;
2. `sources/2026-W37/execution/reviews/sol-w37-publication-preview-r1-independent-review-20260919.md`;
3. `sources/2026-W37/execution/reviews/publication-preview-r1.md`;
4. `sources/2026-W37/execution/reviews/publication-preview-r1-dossier.md`;
5. `sources/2026-W37/gates/reviews/architecture-r1.json`;
6. `sources/2026-W37/gates/reviews/approvals/architecture-r1.json`;
7. `sources/2026-W37/architecture-v2.json`;
8. all current W37 Draft Results and profile synthesis result;
9. all current reader-facing W37 TeX/Bib sources;
10. current bodies/comments for:
   - Issue #501 — reader-facing Japanese technical-language semantic fidelity;
   - Issue #506 — reviewer attribution/provenance;
11. current `scripts/survey_human_gate_v2.py` CLI/help;
12. current Draft / reader-surface / publication-candidate / PDF validation CLIs;
13. W36 r1 Publication Preview language-repair precedent if useful.

Repository authority is controlling.

Do not access Google Drive.

## 4. Invalidate unpresented Publication Preview r1 without Human decision

Use canonical:

`survey_human_gate_v2.py invalidate-pending-gate`

for:

- gate: `PUBLICATION_PREVIEW`
- regeneration boundary: `ARCHITECTURE_ESTABLISHED`
- reason: Sol Publication Preview r1 REQUEST_CHANGES for Issue #501 recurrence and reviewer-provenance defect #506; r1 was unpresented to Human;
- operator reference: this request;
- expected work-branch head: Exact Starting SHA from invocation;
- invalidated commit SHA: use the exact invocation/start authority required by current CLI semantics; do not guess if the implementation requires a different identity.

Before execution, inspect current CLI/implementation semantics.

The required result must:

- create no Human decision;
- preserve canonical Human Architecture approval;
- preserve exact approved Architecture bytes;
- return the state to the canonical Draft regeneration point corresponding to `ARCHITECTURE_ESTABLISHED`;
- invalidate only Draft/downstream publication authority required for regeneration.

If the canonical operator invalidation would remove or reopen the already-approved Architecture Gate at this exact boundary, STOP and report the implementation behavior rather than bypassing it.

Preserve the r1 Publication Preview shell, dossier and independent Sol review as historical audit artifacts unless current canonical invalidation semantics explicitly supersede a canonical path. Do not rewrite history to hide the defect.

## 5. Frozen upstream authority

The following are frozen and must remain semantically unchanged:

- Grok/X intake;
- Discovery;
- Screening;
- Evidence and Evidence views;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Human Architecture approval.

Frozen counts:

- Discovery: `14`
- Screening: `13 KEEP / 1 DROP`
- Evidence: `11 VERIFIED / 2 PARTIAL`
- Materiality: `12 MATERIAL / 1 CONTEXT / 1 EXCLUDED`
- Selection: `12 SELECTED / 1 HOLD`
- Architecture: `7 packages`.

No fresh research is authorized.

## 6. Why regeneration starts at Architecture -> Draft

The r1 language defect is present in canonical Draft Results themselves, not only in TeX transformation.

Examples from r1 Draft authority include:

- `w37-voice-frontier/draft-result.json`:
  - 「背後の文章模型」
  - 「道具立て」
- `w37-harness-plane/draft-result.json`:
  - 「雲の上の代理人」
  - 「砂場」
  - 「開かれたCodexの符号」
- `w37-safety-bound/draft-result.json`:
  - 「対象の模型」
  - 「複数代理人」
  - 「検出子」
- profile synthesis:
  - 「模型ごとの数値」
  - 「許しの範囲」
  - 「符号の力」.

Therefore do not preserve r1 Draft Results as canonical r2 Draft authority.

Regenerate all seven Draft Packages/Results as required by current Core from the same approved Architecture and frozen accepted Evidence.

Do not change the Architecture to make the Japanese easier.

## 7. RC-P1 — natural Japanese technical prose, Issue #501

Classification:

`BLOCKING_READER_LANGUAGE_SEMANTIC_FIDELITY`

Issue #501 is OPEN again because W37 reproduced the defect.

The goal is not blanket katakana conversion.

Required transform:

`source/internal meaning -> semantic interpretation -> precise idiomatic Japanese technical prose`

A technically literate Japanese reader must be able to understand the intended mechanism, product behavior, metric, license, or limitation **without reconstructing the original English term from an unnatural literal translation**.

### Known r1 forced substitutions to eliminate contextually

Review the whole Draft and reader surface, not only this list.

Prefer established terminology where it preserves meaning:

- model:
  - use `モデル`
  - `言語モデル`
  - `テキストモデル`
  - another established context-specific term;
  - do not use `模型` for AI models.
- code / coding:
  - `コード`
  - `コーディング`;
  - do not use `符号` when source means software code.
- token:
  - `トークン`;
  - do not use `符号`.
- agent:
  - `エージェント`;
  - do not use `代理人` for AI agents.
- harness:
  - `ハーネス`
  - `エージェントハーネス`
  - natural contextual explanation where needed;
  - avoid vague `道具立て` where harness is the actual mechanism.
- tool:
  - `ツール` or a precise Japanese term according to source meaning.
- sandbox:
  - `サンドボックス`;
  - not `砂場`.
- serving:
  - `サービング`, `推論サービング`, `推論基盤` as context warrants;
  - not `給仕`.
- engine:
  - `エンジン`;
  - not `引擎`.
- license:
  - `ライセンス`, `利用条件`, etc.;
  - not `許し`.
- model card:
  - `モデルカード`;
  - not `札`.
- translation:
  - `翻訳`;
  - not `訳し` when naming a technical model/application domain.
- MoE:
  - `MoE`
  - `Mixture-of-Experts`
  - `混合エキスパート`;
  - avoid opaque `混合専門家`.
- judge model:
  - `評価用モデル`, `judge model`, or another clear technical expression.
- IOC / indicators:
  - `IOC`, `侵害指標`, or source-appropriate established terminology;
  - not vague `検出子`.

### Known r1 phrases requiring rewriting

At minimum fix the semantics behind:

- 「金融向けの整え」
- 「三つの出し分け」
- 「効率旗艦」
- 「声の層」
- 「読みの偏り付け」
- 「雲の上の代理人」
- 「公開試し」
- 「互換の経路」
- 「求めを振り替える」
- 「開かれた重みは縦に伸びる」
- 「安全の物差し」.

Do not merely replace one unusual noun with another unusual noun.

Use natural Japanese sentence structure.

### Terminology invariant

Technical precision is more important than avoiding katakana/English.

Conventional technical English or katakana is acceptable and often preferable.

Do not force:
- model
- code
- token
- agent
- harness
- sandbox
- serving
- engine
- license
- model card
- benchmark
- prompt
- repository
- dataset
- weights
- active parameters
into novel Japanese solely to reduce loanwords.

## 8. Claim/evidence invariants during language repair

The language rewrite must not change:

- claim strength;
- source attribution;
- vendor-report status;
- benchmark independence status;
- dates/times;
- ordinary/pre-window/Late Breaking/future-operation classification;
- model/product boundaries;
- license terms;
- Architecture package membership;
- HOLD/DROP semantic decisions;
- X/community technical-authority boundary.

Specifically preserve:

### OpenAI
- Financial Services uses Astra;
- GPT-Live-1 is a separate voice model/layer;
- Agents API is a separate harness;
- do not collapse them into one Astra surface.

### DeepSeek
- ahead-of-Pro remains DeepSeek/vendor-reported;
- unnamed parties are not independent reproduction;
- Sep 14 routing remains future/post-window;
- in-window pricing/economics are separate.

### Cognition
- Fusion published at `2026-09-11T17:00:00Z`;
- 39% is table maximum, not uniform;
- evaluation remains partnered/vendor-presented.

### Open weights
- MiniCPM/North/Ling benchmark claims remain card/vendor reported;
- North license and judge-model bounds remain exact;
- Ling timing precision remains bounded.

### Safety
- Threat cases remain vendor-reported investigation;
- full PDF/IOCs not consumed;
- late detail remains outside ordinary facts;
- resignation discourse remains non-architected;
- GLM rumor remains excluded.

## 9. Japanese-language QA before TeX/PDF

Before rendering r2, perform a dedicated whole-Draft language review.

This review must be separate from ordinary schema/coverage validation.

Minimum checks:

1. read all seven Draft Results plus synthesis as continuous Japanese prose;
2. flag any sentence whose intended technical term must be reverse-engineered from an unusual literal translation;
3. check headings/decks, not only body paragraphs;
4. check claim-boundary wording that will become reader-facing prose;
5. check frontmatter, Week in Review and Source Notes after TeX generation;
6. confirm the known r1 forced substitutions above are gone or contextually justified.

Create an edition-local Worker language-QA record.

It must identify reviewer as actual runner, for example:

`Worker/Agent (Muse Spark)`

not ChatGPT/Sol/Human.

A simple forbidden-word scan is insufficient; semantic reread is required.

## 10. RC-P2 — reviewer provenance, Issue #506

Classification:

`BLOCKING_REVIEW_PROVENANCE`

Do not repeat r1:

`reviewed_by: "ChatGPT (Muse Spark)"`

or session language such as:

`Genuine ChatGPT semantic/editorial QA`.

Worker-generated review artifacts must identify the actual worker.

Use a provenance such as:

`Worker/Agent (Muse Spark)`

for:

- language QA;
- reader-surface semantic review;
- semantic/editorial review;
- visual review;
- other Worker checks.

Do not claim:
- ChatGPT
- Sol
- Human
- independent reviewer
unless that reviewer actually produced the content and an external authority is explicitly bound.

Actual independent Sol review occurs only after remote push and is not performed in this Muse run.

## 11. Reader-facing X/public-citation behavior — preserve r1 success

Do not regress the successful W37 X citation design.

Preserve:

- direct public X status URLs;
- no repository-internal Raw path as reader citation;
- no internal GitHub blob citation;
- X as community/context only;
- ordinary-window timing;
- no X-only technical fact.

r1 had 19/19 resolved bibliography keys with 8 direct X citations. r2 need not preserve exactly the same count if natural drafting changes citation placement, but every reader-facing community claim must remain auditable and every technical claim must retain primary/authoritative support.

## 12. Publication Boundary / temporal discipline — preserve r1 success

Do not reintroduce W36 issues #434/#500.

No internal production state vocabulary in reader prose, including as reader-facing semantics:

- HOLD
- PARTIAL
- VERIFIED
- MATERIAL
- Screening
- Selection
- candidate
- blocker
- revision IDs
- internal paths.

Do not strengthen chronology:

- pre-window stays context;
- ordinary stays ordinary;
- Late Breaking stays outside ordinary facts;
- Sep 14 DeepSeek routing stays future operation.

## 13. Regeneration path

After operator invalidation to `ARCHITECTURE_ESTABLISHED`:

1. preserve approved Architecture and approval authority;
2. regenerate seven Draft Packages/Results and profile synthesis from frozen upstream;
3. run dedicated Worker language QA;
4. validate Draft canonically;
5. regenerate all reader-facing TeX sections/Bib from the new Draft;
6. run lexical Publication Boundary checks;
7. run semantic reader-language check;
8. build PDF through normal CI/build path;
9. pin exact PDF bytes;
10. rebuild reader manuscript;
11. rebuild deterministic quality checks/bundle;
12. regenerate reader-surface semantic review with correct Worker provenance;
13. regenerate semantic/editorial review with correct Worker provenance;
14. regenerate visual review with correct Worker provenance;
15. validate exact new PDF/source bundle;
16. create a new Publication Candidate;
17. advance to `RELEASE_CANDIDATE`;
18. create fresh Publication Preview r2 shell/dossier;
19. STOP.

Do not reuse r1 candidate/PDF/review SHA identities.

## 14. r2 Publication Preview dossier requirements

The fresh r2 dossier must report:

- approved Architecture authority unchanged;
- exact Draft r2 identity;
- language-QA record/path and actual reviewer identity;
- representative r1 -> r2 Japanese repairs;
- confirmation known forced substitutions were reviewed across full surface;
- section/package structure;
- exact PDF path/SHA/bytes/pages;
- X/public citation audit;
- vendor-claim boundary audit;
- temporal-boundary audit;
- Publication Boundary audit;
- semantic/editorial review with Worker provenance;
- visual review with Worker provenance;
- known residual nonblocking limitations;
- any deviation from approved Architecture;
- Human Preview decision = `PENDING`.

Do not say r2 is Sol-reviewed.

## 15. Shared-Core freeze

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

Issue #501 generic hardening and Issue #506 generic reviewer-provenance hardening remain separate Core concerns.

If current Core cannot perform the required operator invalidation/regeneration without a shared-Core change, record the exact blocker and STOP.

Do not implement an edition-local shared semantic workaround in Core.

## 16. Commit discipline

Use existing W37 branch only.

Normal commits, non-force pushes, remote read-back.

Before meaningful write groups, verify expected current remote HEAD.

No new branch, fallback, repair, review or temporary branch.

No history rewrite.

## 17. Normal successful endpoint

Expected endpoint:

- Architecture Human approval still `APPROVED`;
- exact approved Architecture unchanged;
- regenerated natural-Japanese Draft established;
- canonical validations passed;
- new reader-facing source/PDF/candidate established;
- lifecycle `RELEASE_CANDIDATE`;
- next action `PUBLICATION_PREVIEW`;
- terminal `HUMAN_GATE_REACHED`;
- fresh Publication Preview r2 `PENDING`;
- no Human Publication Preview decision;
- no Freeze;
- no Release;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0.

## 18. Final report

Report:

- Starting SHA/tree;
- operator invalidation record and boundary;
- confirmation no Human Preview decision created;
- Architecture approval identity preserved;
- frozen upstream counts;
- new Draft identity;
- language QA result;
- representative terminology/prose repairs;
- new TeX/Bib identity;
- X/public citation audit;
- new PDF path/SHA/bytes/pages;
- deterministic validation results;
- semantic/editorial review reviewer identity and status;
- visual review reviewer identity and status;
- new candidate identity;
- fresh Publication Preview r2 reviewed production commit/tree;
- ending HEAD/tree;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0;
- r2 Human decision = `PENDING`;
- exact stop reason.
