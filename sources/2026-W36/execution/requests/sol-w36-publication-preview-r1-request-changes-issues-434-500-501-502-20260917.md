# W36 execution instruction — Publication Preview r1 REQUEST_CHANGES for #434 / #500 / #501 / #502

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R1_REQUEST_CHANGES / BOUNDED_DRAFT_COMPLETE_REGEN`

Date: `2026-09-17 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W36-v2-work`

## 1. Human decision authority

The Human has reviewed the W36 Publication Preview r1 and requires the defects tracked by GitHub Issues #434, #500, #501 and #502 to be addressed before approval.

Publication Preview r1 decision for this execution:

`REQUEST_CHANGES`

Exact reviewed production authority:

`c4ab045548ebf279209862bf62bd6f9725082fb8`

Publication Preview r1 presentation shell currently bound above it:

`acb82cdcc4d09820ce4a30c9984ee66d18df759b`

Reviewed PDF authority:

- path: `surveys/weekly/2026-W36/main.pdf`
- SHA-256: `b5893f4809a7004fa7890e7817e3e8ca08056f401f699562ece3607f67111dc0`
- bytes: `360121`
- pages: `12`
- candidate SHA-256: `0c4ea8733d9c7c682db5770c6e8e690750bd479d10b0440c38ce4767b07a60b8`

The allowed regeneration boundary is:

`DRAFT_COMPLETE`

This is the smallest valid boundary because the accepted Draft authority remains usable, while the reader-facing TeX/Bibliography/publication validation and PDF must be regenerated.

Do not reopen or alter Discovery, Screening, Evidence, Materiality, Completeness, Selection, Architecture, or canonical Draft Results.

## 2. Starting guard

The Muse invocation will supply the Exact Starting SHA equal to the commit containing this execution request.

Before any repository/GitHub write, read-only verify:

- remote `weekly/2026-W36-v2-work` HEAD == Exact Starting SHA supplied by invocation;
- Exact Starting SHA parent == `acb82cdcc4d09820ce4a30c9984ee66d18df759b`;
- remote `main` HEAD == `5acbff8528890ed9fc324c0227e6c4e43067c438`;
- remote `main` tree == `451fd7c6c6a9fcda59daa81fe484c62291e7d018`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote `production/survey-core-v2` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- current W36 state is `RELEASE_CANDIDATE`, next action `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`;
- Architecture Review r2 remains `APPROVED` against `3e1e0fc3b802bf388e56486c638acba35b7bc2ae`;
- Publication Preview r1 remains `PENDING` before this decision is recorded;
- reviewed PDF/candidate identity exactly matches §1.

If any guard differs, perform no repository/GitHub write. Report expected versus actual and STOP.

No force push, reset, rebase, history rewrite, fallback branch, alternate W36 branch, Core repair branch, or merge to `main` is authorized.

## 3. Mandatory issue read

Read the current bodies and relevant comments for:

- #434 — Publication Boundary / internal state leakage
- #500 — GLM-5.3 temporal-confidence preservation
- #501 — reader-facing Japanese technical-language semantic quality
- #502 — reader-auditable community-observation citation

Treat those issues as Human review requirements for this revision.

Do not silently reinterpret or narrow them to only the representative examples.

## 4. Record Publication Preview r1 REQUEST_CHANGES

Use the canonical Human Gate implementation to record:

- gate: `PUBLICATION_PREVIEW`
- revision: `1`
- decision: `REQUEST_CHANGES`
- reviewed repository commit: `c4ab045548ebf279209862bf62bd6f9725082fb8`
- reviewed_by: `Human Owner`
- review_reference: this execution request plus `sources/2026-W36/execution/reviews/publication-preview-r1.md`
- regeneration boundary: `DRAFT_COMPLETE`
- requested changes: #434, #500, #501, #502 as specified below

Use the actual canonical tool timestamp. Do not invent a historical timestamp.

After recording the decision, verify that the canonical lifecycle rollback/invalidation matches current Core semantics for `DRAFT_COMPLETE`.

If Core refuses the requested revision because of identity/state/provenance mismatch, STOP rather than bypassing it.

## 5. Frozen upstream authority

This run must not rerun or semantically alter:

- Grok/X intake
- Discovery
- Screening
- Evidence or Evidence views
- Materiality
- Completeness
- Selection
- Architecture
- Architecture approval
- Draft Packages / Draft Results / profile synthesis authority

Expected frozen counts remain:

- Discovery: `19`
- Screening: `19 KEEP / 0 DROP`
- Evidence: `13 VERIFIED / 6 PARTIAL`
- Materiality: `18 MATERIAL / 1 CONTEXT`
- Selection: `18 SELECTED / 1 HOLD`

The internal statuses above remain repository authority; the point of #434 is that they must not be serialized into reader-facing prose.

## 6. RC-P1 — Issue #434: Publication Boundary regression

Classification: `BLOCKING_READER_SURFACE_BOUNDARY`

W36 r1 demonstrates a false negative in the current reader-surface gate. Reader-facing TeX/Bibliography contains internal Evidence/Selection state even though the gate reports zero findings.

Known examples include, but are not limited to:

- `sections/55-ecosystem-spatial-media.tex`: `PARTIALの札のまま本文に格上げしない。`
- `sections/40-frontier-coding.tex`: `...HOLDの文脈資料に留め...`
- `sections/99-source-notes.tex`: `HOLDの模型札の細目は別候補として持ち上げていない。`
- `references.bib`: `Model-card detail stays HOLD context companion.`
- `references.bib`: `Vendor-via-PR authority, PARTIAL; ...`
- `sections/10-astra-critical-cyber.tex`: internal revision/process wording such as `r4で...`

Required artifact repair:

1. Perform a full semantic Publication Boundary pass over every reader-facing W36 source:
   - `surveys/weekly/2026-W36/main.tex`
   - all `surveys/weekly/2026-W36/sections/*.tex`
   - `surveys/weekly/2026-W36/references.bib`
   - the new publication-facing community note required by #502
2. Remove internal workflow/review semantics, not only literal tokens.
3. Reader-facing text must not expose internal states or operations such as:
   - `HOLD`, `PARTIAL`, `VERIFIED`, `MATERIAL`, `CONTEXT`
   - Screening/Selection/Candidate disposition
   - revision IDs such as `r4`
   - promotion/demotion language such as `格上げ`, `別候補として持ち上げない`
   - internal source-consumption/process wording when a reader-facing factual limitation can express the same boundary
   - raw internal paths/IDs/provenance labels
4. Preserve the underlying reader-relevant limitation. Examples:
   - instead of `PARTIAL`, state that the H3 Max ranking evidence comes from a vendor-via-PR source and was not independently reproduced;
   - instead of `HOLD`, state that the additional Gemini model-card details are not used as separate factual support in this edition;
   - instead of `r4`, describe only the published observation set and its scope.
5. Do not weaken any factual uncertainty or attribution boundary while removing internal terminology.

The current Core gate false negative is a generic #434 regression. **Do not modify shared Core in this run.** #434 has been reopened separately with W36 regression evidence. The W36 run repairs the artifact only.

Create an edition-local Worker/Operator Publication Boundary audit record if useful, but do not mislabel it as a Core fix or independent Human/Sol review.

## 7. RC-P2 — Issue #500: GLM-5.3 temporal-confidence preservation

Classification: `BLOCKING_TEMPORAL_CONFIDENCE`

Current accepted authority says:

- GLM-5.3 is associated with `2026-08-28`,
- the exact UTC publication hour is unresolved,
- therefore relation to the W36 start boundary (`2026-08-28T22:00:00Z`) is medium-confidence / boundary placement.

Current `Week in Review` incorrectly strengthens this to:

`K2 Horizon ... とGLM-5.3 ... が同じ週に現れた。`

For this run, **do not perform new research merely to resolve the timestamp**. Use Issue #500 option 2: preserve GLM-5.3 as a boundary item.

Required repair:

- `sections/30-open-efficient.tex`: rewrite the temporal explanation into precise natural Japanese. State that the 28 Aug date is visible but the publication time is unresolved, so whether it falls inside the W36 window cannot be established at hour precision.
- `sections/60-week-in-review.tex`: remove any definite `same week` claim for GLM-5.3. Distinguish K2 as an in-window event from GLM as a boundary/carry-in item.
- `sections/99-source-notes.tex` and any frontmatter/synthesis wording: maintain the same confidence.
- bibliography note for `glm53weights`: preserve the same boundary semantics.

No downstream sentence may express stronger temporal certainty than the accepted source/event authority.

Do not remove GLM from the approved Architecture or Selection. This is a chronology/reader-surface correction only.

## 8. RC-P3 — Issue #501: natural technical Japanese semantic pass

Classification: `BLOCKING_READER_LANGUAGE_SEMANTIC_FIDELITY`

Perform a bounded language-quality pass across the complete reader-facing W36 publication source, not only the examples in #501.

The goal is **not** blanket katakana conversion. The rule is:

`source/internal term -> semantic interpretation -> precise, idiomatic technical Japanese`

A technically literate Japanese reader should not need to reconstruct the English source phrase to understand the mechanism, product behavior, metric, or limitation.

Known examples that must be corrected contextually include:

- `全物公開の連なり`
- `守りの段違い`
- `協定時単位`
- `落としや好みの数は基盤の遠隔測定`
- `一押しの全枠debug`
- `物切り分けと狙い文指示の直しや束ね直し`
- `自家対面試験`

Also review recurring forced lexical substitutions throughout all sections, including context-dependent uses of:

- `模型` where `モデル` is the established technical term
- `符号` where `コード` is intended
- `番付` where `ランキング` / `順位` is intended
- `許し` where `ライセンス` / `利用条件` is intended
- `給仕` where `サービング` / `推論提供` is intended
- `札` where `モデルカード` is intended
- `道具` where `ツール` / `エージェント` is intended
- `仕事` where `タスク` / `ワークフロー` is intended
- `砂場` where `サンドボックス` is intended
- `枝` / `未投入差分` where Git terminology (`ブランチ`, `未コミット差分`) is intended
- technical terms such as prompt/debug/telemetry/repository/dataset/weights/active parameters when forced Japanese wording obscures meaning.

These are examples, not mandatory global replacements. Choose terminology by actual source meaning and conventional Japanese technical usage.

Preserve:

- exact claim strength
- source attribution
- vendor-report boundaries
- temporal uncertainty
- licensing nuance
- GA/preview distinctions
- benchmark methodology limitations
- all r2 Architecture semantics.

Do not introduce new facts or fresh research.

The Draft authority remains frozen; this is a reader-facing publication-language transform.

## 9. RC-P4 — Issue #502: reader-auditable community observation citation

Classification: `BLOCKING_READER_AUDITABILITY`

Current `w36community` bibliography entry has no URL even though it is cited from reader-facing prose.

Create a dedicated publication-facing community observation artifact at:

`surveys/weekly/2026-W36/community-observation.md`

Required content:

- clear title and W36 observation scope;
- canonical W36 ordinary window and explicit Late Breaking distinction;
- the exact 15 accepted public X URLs from the canonical W36 accepted observation source;
- for each entry, only reader-auditable public metadata useful for understanding the observation (for example account, timestamp, ordinary vs late-breaking, short neutral observation summary);
- an explicit statement that the observation set is **context only** and cannot establish specifications, benchmarks, licenses, release dates, availability, pricing, architecture, autonomy, transaction terms, or other technical facts;
- no candidate IDs;
- no Screening/Selection/Evidence status;
- no internal revision IDs (`r1/r2/r3/r4`);
- no raw production paths;
- no private provenance.

Do not reconstruct or guess X URLs. Read them from the accepted repository-local W36 authority and preserve exact URLs.

### Immutable reader-facing URL procedure

To avoid a branch-dependent citation:

1. create the publication-facing `community-observation.md`;
2. commit and non-force push it as a distinct normal commit;
3. read back that commit SHA;
4. use an immutable GitHub commit permalink in `references.bib`, of the form:

`https://github.com/eariver/japanese-generative-ai-survey/blob/<MANIFEST_COMMIT_SHA>/surveys/weekly/2026-W36/community-observation.md`

5. only after that immutable URL exists, regenerate the reader-facing source/PDF/candidate.

Update `w36community` so it has a reader-followable URL and a context-only note with no internal state leakage.

Use the same public observation surface consistently from Astra/community prose, Week in Review, Source Notes and bibliography where referenced.

Edition-local validation must verify there is no reader-facing `@online` bibliography record without a URL unless an explicit publication policy exception exists. For W36, `w36community` must have a URL.

Do not modify Core to add this generic validator in this run; the generic pipeline acceptance criterion remains tracked by #502.

## 10. Reader-facing semantic pass beyond the named defects

Because #434 and #501 are semantic rather than token-only failures, review the whole publication after edits.

At minimum inspect:

- cover title/deck
- frontmatter
- all six package sections
- Week in Review
- Sources & limitations
- References
- community-observation.md

Check for:

- production/editorial process language;
- unnatural machine-like Japanese;
- stronger chronology than source confidence;
- vendor claims written as independent facts;
- cross-model generalization;
- stale r1 NVIDIA/Hugging Face completed-ownership implication;
- any accidental promotion of the Gemini companion model-card detail;
- any use of community observation as technical authority.

Do not expand scope into new research or new editorial themes.

## 11. Canonical regeneration path

After recording r1 REQUEST_CHANGES and returning to the canonical `DRAFT_COMPLETE` boundary:

1. preserve existing canonical Draft Results byte-identical;
2. create and commit the #502 publication-facing community observation artifact first;
3. perform the bounded reader-facing source/Bibliography corrections for #434/#500/#501/#502;
4. regenerate/rebind every downstream artifact required by current Core from `DRAFT_COMPLETE` onward;
5. rebuild PDF through the normal CI/build path;
6. rebuild reader manuscript and deterministic checks;
7. rerun reader-surface lexical + persisted semantic review;
8. rerun semantic/editorial and visual review against exact new PDF;
9. rerun stage validation;
10. construct a fresh Publication Candidate;
11. create a fresh Human Publication Preview r2 surface;
12. STOP with r2 Human decision `PENDING`.

Do not reuse r1 PDF hashes or candidate identity after any reader-source change.

## 12. Required validation supplement

Current Core may still falsely PASS #434/#501/#502 patterns because shared Core is frozen. Therefore, in addition to canonical validation, create edition-local Worker/Operator audit records documenting at least:

- no literal internal disposition/status tokens remain in reader-facing TeX/Bib/Markdown (`HOLD`, `PARTIAL`, `VERIFIED`, `MATERIAL`, `CONTEXT`, Screening/Selection/Candidate-state usage);
- no semantic promotion/demotion/process language remains;
- GLM temporal confidence is consistent across article/synthesis/source notes/bibliography;
- all representative #501 phrases are gone and the complete reader surface received a language-quality read;
- `w36community` resolves to the immutable public manifest URL;
- all `@online` references are reader-followable or explicitly allowed by publication policy;
- new PDF text extraction does not reintroduce the above defects.

These are Worker/Operator checks, not independent Sol/Human approval.

## 13. Shared Core freeze — mandatory

No changes are authorized under shared Core paths, including:

`.github/**`
`config/**`
`schemas/**`
`scripts/**`
`templates/**`
`tests/**`

Do not modify:

`production/survey-core-v2`

Do not modify:

`main`

Do not repair #434, #500, #501 or #502 generically in Core during this W36 production run.

#434 has been reopened because W36 proves the existing gate still has a false negative. The generic Core improvements requested by #434/#500/#501/#502 must wait for the separate Core-refactor/repair program.

If any necessary artifact repair cannot be completed without shared-Core modification, record the exact blocker and STOP. Do not patch around it in shared code.

## 14. Issue state discipline

Do not close #434, #500, #501 or #502 merely because the W36 artifact is repaired.

The W36 revision can satisfy each issue's artifact-specific acceptance portion, but generic regression/gate acceptance remains a separate Core concern while Core is pinned.

At the end, report exact evidence showing which W36 acceptance criteria are satisfied so Sol/Human can decide whether to add issue comments or split/close artifact-specific portions later.

## 15. Commit/push discipline

Use only:

`weekly/2026-W36-v2-work`

Normal commits and non-force pushes only.

No new branch, force push, reset, rebase, squash, history rewrite, or fallback branch.

Before every write sequence, confirm remote HEAD is the expected parent.

After each push, read back remote HEAD/tree.

The dedicated #502 manifest commit must remain in history because its SHA becomes the immutable reader-facing citation URL.

## 16. Normal endpoint

Successful completion must end at a fresh Publication Preview r2 Human Gate:

- Architecture Review r2 remains `APPROVED`;
- Draft authority unchanged;
- revised reader-facing publication source validated;
- new exact PDF generated;
- new publication candidate generated;
- lifecycle `RELEASE_CANDIDATE`;
- next action `PUBLICATION_PREVIEW`;
- terminal reason `HUMAN_GATE_REACHED`;
- Publication Preview r1 = `REQUEST_CHANGES` preserved historically;
- Publication Preview r2 = `PENDING`;
- Freeze = not started;
- Release = not started;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0.

STOP there.

## 17. Final report

Report:

- Exact Starting SHA/tree
- r1 reviewed production commit/PDF/candidate identity
- canonical r1 REQUEST_CHANGES record identity
- regeneration boundary actually used
- #434 W36 artifact repairs and remaining generic Core implication
- #500 temporal wording before/after semantics
- #501 representative and broader language repairs
- #502 manifest path, manifest commit SHA, immutable bibliography URL, URL count
- confirmation Draft/Architecture/Evidence/Selection unchanged
- canonical validation results
- edition-local supplemental audit results
- new PDF path/SHA/bytes/pages
- new candidate SHA
- fresh Publication Preview r2 reviewed production commit/tree
- ending remote HEAD/tree
- main guard result
- Production Line guard result
- shared-Core changed paths count
- r2 Human decision status
- exact stop reason.
