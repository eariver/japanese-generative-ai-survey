# W38 execution instruction — Human Architecture r2 APPROVED through fresh Publication Preview

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_R2_APPROVED / CONTINUE_TO_PUBLICATION_PREVIEW`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W38-v2-work`

## 1. Human decision authority

The Human Owner has explicitly reviewed the W38 Architecture r2 Human Review package and decided:

`APPROVED`

Human approval was explicitly communicated in the controlling conversation after the r2 review presentation. Independent Sol observed the conversation wall clock at:

- JST: `2026-09-19T14:33:23+09:00`
- UTC: `2026-09-19T05:33:23Z`

This observed conversation time establishes ordering/provenance of the explicit Human decision.

**Do not automatically copy this observed conversation timestamp into the canonical Human Gate `reviewed_at` field unless the current gate contract explicitly supports a distinct decision-observed timestamp.**

For the canonical Human Gate record itself, use the actual wall-clock time at approval-recording execution, obtained from the system clock, so the new record cannot become future-dated relative to its containing commit.

Exact Human-reviewed Architecture production authority:

- commit: `56b6d3d65c5b4105a410e61a22eb083e66fa344c`
- tree: `2360fc10c97f38e61c6bcc220b4cb1fd41e5de75`

Exact reviewed Architecture artifact:

`sources/2026-W38/architecture-v2.json`

SHA-256:

`c123f9af386d0c85e0abc41f4fd91ada7807b6a42816718f1c4e02a01ae5bc48`

Companion Architecture Review triple:

- `architecture-review-summary-v2.json`
  - SHA-256 `e286edc9817584c23996f160c0d6f8dbd3b6336e698976ce928e937dacd7969b`
- `architecture-review-attention-v2.json`
  - SHA-256 `044545e97c2e161144a5e78150a0d825573b6ccd229e13aac90aaa21b00e3e09`

Human-facing r2 review:

- `sources/2026-W38/execution/reviews/architecture-r2.md`
- `sources/2026-W38/execution/reviews/architecture-r2-dossier.md`

Timestamp correction authority:

`sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md`

The Human approval accepts the existing r2 Architecture bytes and seven-package editorial structure.

It does **not** authorize modifications to Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture before drafting.

The r1 Architecture review surface was superseded for Human decision because of invalid timestamp provenance. No Human decision was recorded on r1. Do not invent an r1 Human `REQUEST_CHANGES`.

## 2. Mission

1. record the explicit Human Architecture r2 approval using the canonical Human Gate protocol against exact reviewed production commit `56b6d3...`;
2. verify the immutable approval authority and resulting lifecycle state;
3. freeze all upstream research/Architecture semantic authority;
4. continue W38 through all current profile-required downstream stages:
   - Draft
   - Draft/schema/coverage validation
   - publication rendering
   - publication candidate authority
   - PDF generation/authority
   - lexical reader-surface validation
   - semantic/editorial/visual review required before Publication Preview
   - publication-profile/candidate validation
5. create a fresh Human Publication Preview review shell/dossier;
6. STOP with Human Publication Preview `PENDING`.

Do not Freeze.

Do not Release.

Do not record or infer a Publication Preview Human decision.

## 3. Invocation starting guard

The Muse invocation MUST provide the exact current remote W38 HEAD/tree corresponding to the commit containing this execution request.

Before any repository/GitHub write, read-only verify:

- remote `weekly/2026-W38-v2-work` HEAD == Exact Starting SHA supplied in invocation;
- remote W38 tree == Exact Starting Tree supplied in invocation;
- Exact Starting SHA parent == `eade15de1910943b31d204db749513d85e681df9`;
- parent tree == `af695cabe44d974c1ebf8ced7eb47e3e52e9c9e4`;
- remote `main` HEAD == `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- remote main tree == `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- Production State remains:
  - lifecycle `ARCHITECTURE_ESTABLISHED`;
  - next action `ARCHITECTURE_REVIEW`;
  - terminal reason `HUMAN_GATE_REACHED`;
  - Architecture Review pending;
  - Publication Preview pending;
- r2 review binds reviewed commit `56b6d3d65c5b4105a410e61a22eb083e66fa344c`;
- Architecture triple SHAs exactly match §1;
- current research-stage counts remain:
  - Discovery 13;
  - Screening 12 KEEP / 1 DROP;
  - Evidence 9 VERIFIED / 3 PARTIAL;
  - Materiality 11 MATERIAL / 1 CONTEXT / 1 EXCLUDED;
  - Selection 11 SELECTED / 1 HOLD;
  - Architecture 7 packages.

Any mismatch -> zero production writes, report expected vs actual, STOP.

If the local clone is stale, use the bounded fetch + fast-forward-only sync authority already established in:

`sources/2026-W38/execution/requests/sol-w38-stale-local-sync-and-resume-20260919.md`

Do not use stale local `main` as reviewed authority.

No new/fallback/repair/review/temporary branch.

No force/reset/rebase/squash/history rewrite.

## 4. Mandatory read order

Read at minimum:

1. this execution request;
2. `sources/2026-W38/execution/reviews/architecture-r2.md`;
3. `sources/2026-W38/execution/reviews/architecture-r2-dossier.md`;
4. `sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md`;
5. `sources/2026-W38/architecture-v2.json`;
6. `sources/2026-W38/architecture-review-summary-v2.json`;
7. `sources/2026-W38/architecture-review-attention-v2.json`;
8. `sources/2026-W38/candidate-selection-v2.json`;
9. `sources/2026-W38/profile-completeness-v2.json`;
10. `sources/2026-W38/production-state.json`;
11. current Human Gate implementation/CLI help;
12. current Draft/publication/reader-surface/publication-candidate/PDF pipeline authority and CLI help;
13. W37 approved-through-Publication-Preview execution precedent where useful.

Repository-local reviewed Core behavior is authoritative.

Do not access Google Drive.

## 5. Canonically record Human Architecture approval

Use the current canonical Human Gate protocol.

Required semantics:

- gate: `ARCHITECTURE_REVIEW`
- decision: `APPROVED`
- reviewed repository commit SHA: `56b6d3d65c5b4105a410e61a22eb083e66fa344c`
- reviewed_by: `Human Owner`
- review reference must bind:
  - this execution request;
  - `architecture-r2.md`;
  - `architecture-r2-dossier.md`;
  - W38 timestamp correction ledger;
  - explicit Human decision authority in §1.
- requested changes: none
- regeneration boundary: none

Determine the canonical next Human review revision from current repository state. Do not infer revision solely from filenames.

Use **actual execution wall-clock time** for the canonical review record.

Before saving the canonical Human decision:

```bash
date --iso-8601=seconds
date -u --iso-8601=seconds
```

or equivalent actual system-clock authority.

After canonical recording:

- read back the Human review record;
- read back Human review index;
- verify exact reviewed commit;
- verify immutable approval snapshot/authority produced by current Core;
- verify Production State transition produced by canonical approval logic;
- verify new `reviewed_at` is not future-dated relative to actual wall clock;
- after commit/read-back, verify the new `reviewed_at` does not post-date its containing commit.

If timestamp, revision, reviewed commit, state, or canonical gate protocol does not match, STOP. Do not bypass.

## 6. Timestamp provenance discipline for all downstream records

Issue #507 recurrence remains active as a known generic Core defect.

Existing invalid historical timestamp fields remain governed by:

`sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md`

Do not rewrite those old records.

For every **new** record created after Human approval:

- use actual wall-clock time;
- timezone-aware only;
- never synthesize rounded future stage times;
- never advance timestamps merely to preserve monotonicity with invalid historical State times;
- if current Core attempts to force a future timestamp, record the lifecycle result separately and append a provenance correction rather than presenting the future value as actual wall time;
- new Human/Worker review timestamps must not post-date their containing commit.

### Nonbinding r2 repair-session typo

The prior session note:

`sources/2026-W38/execution/sessions/w38-timestamp-provenance-repair-20260919-r1.md`

contains a nonbinding parenthetical statement referring to a HEAD commit clock of `14:06:15+09:00`.

Actual Git authority for the containing r2 repair commit is:

- commit `eade15de1910943b31d204db749513d85e681df9`
- commit time `2026-09-19T05:14:40Z` = `2026-09-19T14:14:40+09:00`

Do not rewrite the historical session note.

Treat the parenthetical clock text as a provenance typo and use immutable Git commit metadata for ordering.

This typo does not affect the r2 review generation timestamp `14:13:35+09:00`, which correctly precedes the containing commit.

## 7. Approved W38 editorial thesis

Preserve the approved semantic thesis:

**W38 shows the frontier moving from generic model competition toward verticalization, verification, and operationalization.**

The Architecture frames the week through seven packages:

1. `w38-law-vertical` — Astra goes vertical: Law
2. `w38-voice-frontier` — The live voice frontier
3. `w38-biology-access` — Biology access, verified
4. `w38-pacing-operational` — Pacing, operationalized
5. `w38-decision-models` — Decisions without generation
6. `w38-agent-harness` — Harness efficiency: codebase investigation
7. `w38-image-production` — Image goes production

Do not add, remove, merge, split, or materially reorder packages in a way that changes the approved thesis without stopping for new Human authority.

Page allocation is downstream drafting/layout concern; it may be adjusted without changing semantic package structure.

## 8. Frozen upstream research authority

After Human approval is canonically recorded, do not rerun or semantically modify:

- Grok/X intake;
- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture.

Expected frozen authority:

- Grok r2 Raw exact SHA/bytes unchanged;
- Discovery 13;
- Screening 12 KEEP / 1 DROP;
- Evidence 9 VERIFIED / 3 PARTIAL;
- Materiality 11 MATERIAL / 1 CONTEXT / 1 EXCLUDED;
- Selection 11 SELECTED / 1 HOLD;
- Architecture 7 packages.

If drafting exposes a genuine contradiction that invalidates approved Architecture, STOP at the smallest canonical boundary. Do not silently repair upstream semantic authority.

## 9. Draft evidence boundaries — Astra for Law

Preserve:

- Astra for Law is a legal-vertical configuration, not a new base model;
- 230M-URL index / CourtListener statements only within first-party wording;
- Vals 54.0/38.7 figures are vendor-reported;
- Trusted Access/ZDR/plugins are bounded to the stated product surface;
- X C1 is community signal only.

Do not claim:

- independent benchmark reproduction;
- universal legal superiority;
- unstated pricing/limits;
- legal privilege/security conclusions from one X counter-signal.

## 10. Draft evidence boundaries — Gemini 3.8 Live

Preserve:

- separate Live / Extended Thinking positioning as first-party stated;
- native speech-to-speech framing;
- 97-language/background execution claims as vendor-stated;
- S2S/tau-Voice/BBA figures as publisher/vendor claims;
- @tetumemo observations as independent/community integration context only.

Do not convert X integration anecdotes into official technical facts.

Gemini Live API docs retrieval failed during gap-fill; do not imply those docs were semantically consumed.

## 11. Draft evidence boundaries — LSVP

Preserve:

- LSVP beta as a verified-access life-sciences regime;
- Standard vs High-risk access mechanics as stated;
- monitoring/retention design as first-party stated;
- dual-use framing as vendor context.

Do not use LSVP as evidence of a Mythos 5.1 release date or independent biology capability benchmark.

## 12. Draft evidence boundaries — pacing / R&D / Accenture arc

The Human approval accepts the Architecture grouping:

`Amodei essay -> R&D metrics -> Accenture embedded evaluation`

as an editorial governance arc.

This is **editorial synthesis**, not a causal claim that the essay caused the deal.

Preserve:

- essay as policy/pacing commitment;
- incident account as the author's stated account unless independently sourced;
- Anthropic R&D metrics as first-party reported snapshots with methodology;
- Accenture partnership within first-party terms;
- `$1B` figures as stated mutual expectations, not audited spending;
- non-exclusive/operational details only where source-supported.

Do not:

- generalize August R&D measurements into current industry-wide facts;
- claim the missing biomolecular optimization repo/report;
- claim causation from essay to deal.

## 13. Draft evidence boundaries — Jev

Preserve:

- System One / Jev as non-generative structured decision framing;
- RLCD as vendor-described;
- speed/cost/eval figures as vendor-stated;
- schema-bound guarantee scope only;
- commercial/early-access terms only where stated.

Do not invent:

- parameter count;
- topology;
- loss/training architecture beyond sources;
- independent performance superiority.

X community summaries must not become architecture facts.

## 14. Draft evidence boundaries — Devin Code Scans

Preserve:

- goal-to-PR/codebase investigation product framing;
- Agentic MapReduce as Cognition-described architecture;
- pilot metrics as first-party stated outcomes;
- /scan/docs product surface as stated.

Do not present 96% / 700h / Dioxus / SEO or similar pilot metrics as independently reproduced facts.

Secondary Copilot/Zed/xAI-memory leads remain outside this package unless existing approved Evidence explicitly binds them.

## 15. Draft evidence boundaries — production image

Preserve:

- CAI-Image family as Character.ai's production/open-lineage image direction;
- Tsubaki.3 + Tsubaki Video as creator-production tooling;
- comparative imagery/quality as vendor-presented;
- explicit distinction between creator tooling and foundation video-model releases.

Do not rank creator tools against foundation video models.

Do not convert marketing superlatives into measured fact.

## 16. HOLD / DROP handling

### DeepSeek routing

Current disposition:

`HOLD / CONTEXT / NOT_SELECTED`

Reason:

secondary-only occurrence with open primary gap.

Do not make it an eighth package or a technical release claim.

It may appear only as narrowly bounded context/sidebar material if current downstream contract allows and primary gap remains explicit.

### GLM-5.5

Current disposition:

`DROP / EXCLUDED`

Rumor-only with absence re-verified.

Do not surface GLM-5.5 as a W38 technical development.

## 17. X / community provenance

W38 Grok/X r2 remains Raw Observation/community signal.

Accepted corrected accounting:

- 25 total direct X status IDs;
- 23 ordinary;
- 2 late-breaking;
- 15 ordinary accounts;
- 7 INDEPENDENT;
- 3 OFFICIAL;
- 5 COMMUNITY.

Use the row-level ledger + Sol correction record, not inconsistent r2 prose summaries.

For reader-facing X/community statements:

- use auditable public direct X status URLs where citation is appropriate;
- do not cite internal repository paths as reader-facing public sources;
- preserve ordinary vs late-breaking distinction;
- technical facts must cite primary/authoritative sources separately;
- do not imply X corroboration where C3 is OFFICIAL_ONLY_X.

## 18. Reader-facing Japanese and process-language discipline

The finished W38 magazine must read as natural technical Japanese.

Do not leak internal pipeline terminology into the reader-facing magazine, including context-dependent terms such as:

- HOLD
- PARTIAL
- VERIFIED
- Screening
- Selection
- Materiality
- candidate
- blocker
- unresolved authority
- internal repository paths
- review-stage vocabulary

unless the publication explicitly discusses methodology.

Avoid:

- English noun-stack calques;
- mechanical translation of Architecture titles;
- repeated `〜として位置づけられる` patterns;
- qualifier dumps that make main prose unreadable;
- prose that sounds like an audit report rather than a magazine.

Preserve technical qualification naturally in Japanese.

## 19. Time-window language

Canonical W38 ordinary window remains:

`[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`

Do not transform:

- pre-window context;
- post-cutoff Late Breaking;
- future-announced operations;
- uncertain-day/hour events

into an unqualified `今週発表された` claim.

Use exact date or bounded wording where material.

## 20. Drafting and volume policy

Use the approved seven-package Architecture as controlling structure.

Do not impose a page target by deleting selected material or required caveats.

Optimize for:

- coherent synthesis;
- natural Japanese;
- clear evidence boundaries without process leakage;
- balanced package density;
- source auditability;
- readable charts/tables/callouts only when they materially improve the magazine.

Moderate length is acceptable.

If layout becomes overly long, compress prose/repetition before dropping approved semantic content.

## 21. Reviewer attribution discipline

Independent Sol / Human provenance must remain distinct from Worker/Agent analysis.

Worker may create:

- Worker pre-gate analysis;
- deterministic validation output;
- Worker semantic/editorial/visual review if current pipeline requires it;
- Worker dossier inputs.

Worker must not self-author:

- Independent Sol review;
- Human review decision;
- Sol PASS / REQUEST_CHANGES;
- Human APPROVED / REQUEST_CHANGES beyond the explicit Architecture decision being canonically recorded from this request.

The fresh Publication Preview must remain pending independent Sol/Human review.

## 22. Canonical downstream pipeline

Use current repository CLI/help rather than remembered syntax.

Run every profile-required stage/check before Publication Preview.

At minimum cover:

- canonical Human Architecture approval record;
- Draft generation;
- Draft/schema validation;
- Architecture-to-Draft coverage;
- citation/source binding;
- publication rendering;
- durable publication candidate authority;
- TeX/PDF generation;
- PDF authority recording;
- lexical reader-surface validation;
- semantic/editorial reader-surface review;
- visual/layout review required by current profile;
- publication-candidate validation;
- state/checkpoint advancement;
- fresh Human Publication Preview shell/dossier.

Do not manufacture semantic PASS states in production code.

If current Core requires a generic repair to proceed, STOP and document the defect rather than modifying shared Core.

## 23. Publication Preview deliverables

Before normal stop, produce durable canonical authority for:

- final Draft;
- publication candidate;
- final rendered PDF;
- exact PDF path;
- PDF SHA-256;
- byte count;
- page count;
- lexical reader-surface result;
- semantic/editorial reader-surface result;
- visual/layout review result if profile-required;
- publication-profile validation;
- current Production State;
- fresh Human Publication Preview review shell;
- fresh Publication Preview dossier.

The Human-facing dossier must allow independent review of:

- Architecture approval provenance;
- actual seven-package/section structure;
- any drafting compression;
- exact source/citation behavior;
- X/community public auditability;
- vendor-claim qualification;
- PARTIAL/HOLD/EXCLUDED handling without internal terms leaking to readers;
- Japanese prose quality;
- PDF pagination/layout;
- remaining non-blocking limitations;
- deviations from approved Architecture, if any.

Publication Preview Human decision must remain absent.

## 24. Publication Preview timestamp requirements

The fresh Publication Preview shell/dossier must use actual wall-clock timestamps.

Before generating any Worker review or Human-facing preview surface, capture actual time from the system clock.

After commit/read-back:

- verify review timestamp <= containing commit timestamp;
- verify timestamp <= actual current wall clock;
- if not, the surface is NOT PRESENTABLE and must be corrected append-only before Human review.

Do not reuse invalid historical Production State times for Human-facing chronology.

## 25. Shared-Core freeze

No writes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Do not modify:

- `main`
- `production/survey-core-v2`

Known generic issues remain out of scope, including:

- #507 timestamp provenance defect;
- #508 generic Weekly trailing-box/pagination hardening;
- known Freeze schema incompatibility;
- known Freeze-stage Human Gate provenance misclassification;
- known Release workflow nonexistent `validate-state` command;
- #505 future generic X-intake hardening.

This run stops before Freeze/Release.

## 26. Commit/push discipline

Stay on existing W38 branch.

Use:

- normal commits;
- non-force push;
- remote read-back;
- expected prior SHA verification before meaningful write groups.

Do not:

- create another branch;
- force push;
- reset;
- rebase;
- squash;
- rewrite history.

Do not rewrite r1/r2 review provenance.

## 27. Normal STOP condition

Successful endpoint:

- Human Architecture Review canonically `APPROVED`;
- reviewed commit exactly `56b6d3d...`;
- Draft generated;
- required validations passed;
- durable publication candidate exists;
- durable PDF exists;
- lifecycle at current Core-defined Publication Preview gate, normally `RELEASE_CANDIDATE`;
- `PUBLICATION_PREVIEW = PENDING`;
- fresh Human Publication Preview shell/dossier exists;
- no Freeze;
- no Release;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0.

Then STOP.

## 28. Final report

Report at least:

- invocation Starting SHA/tree;
- canonical Human Architecture approval:
  - review revision;
  - review record path/hash;
  - canonical reviewed_at;
  - explicit Human decision authority source;
  - immutable approval/snapshot authority;
  - reviewed production SHA/tree;
- frozen upstream counts;
- Draft identity;
- final seven-package/section structure;
- publication candidate identity;
- PDF path/SHA/bytes/pages;
- lexical reader-surface result;
- semantic/editorial result;
- visual/layout result;
- X/community citation/public-auditability status;
- vendor-claim boundary status;
- Japanese prose quality status;
- timestamp-provenance checks for all newly created review surfaces;
- any downstream edition-local repairs;
- deviations from approved Architecture, if any;
- ending HEAD/tree;
- lifecycle / next action / terminal reason;
- Publication Preview review path;
- Publication Preview Human status = `PENDING`;
- shared-Core changed paths = 0;
- main unchanged;
- Production Line unchanged;
- exact stop reason.

Human Publication Preview decision must remain absent.
