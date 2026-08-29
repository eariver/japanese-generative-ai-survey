# 2026-W33 Sol→Luna handoff — Evidence / Materiality / Completeness candidate r1

Status: `READY_FOR_LUNA / EVIDENCE_MATERIALITY_COMPLETENESS_CANDIDATE / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Sol/Luna policy authority: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`  
Screening advancement review: `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`  
Current lifecycle at handoff creation: `CANDIDATES_NORMALIZED`  
Current machine next action: `stage:evidence-materiality-completeness`  
Requested stop: Sol review before any `ADVANCE_STAGE`

The caller must give Luna the exact branch commit SHA containing this handoff. Luna must start from that exact SHA and must not silently rebase, merge, force-push, or choose a newer basis. If the branch has moved before execution starts, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 1. Objective

Produce the complete **candidate** Evidence / Edition Evidence View / Materiality Ledger / Profile Completeness package for W33 under the current Core v2 contract, then stop for Sol semantic review.

This task includes bounded research and first-pass semantic proposals under the policy below. Luna may propose factual Evidence status and edition Materiality outcomes; those proposals are **not authority until Sol reviews the committed bytes**.

Successful endpoint:

`EVIDENCE + MATERIALITY + COMPLETENESS CANDIDATE COMMITTED -> STOP FOR SOL REVIEW`

Do not run the lifecycle transition to `EVIDENCE_REVIEWED` in this task.

## 2. Frozen upstream authority

### Production State

At task start, verify:

- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- Screening checkpoint: `passed`
- Evidence / Materiality / Completeness checkpoints: `pending`
- terminal reason: none

Canonical State path:

`sources/2026-W33/production-state.json`

### Discovery

- path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- record count: 41
- SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`

### Screening

Canonical accepted Screening run:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`

- acceptance file: `screening-accepted.json`
- result-set SHA-256: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- acceptance SHA-256: `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`
- total: 41
- KEEP: 26
- INSPECT: 8
- MAYBE: 3
- DROP: 4

The 37 non-DROP records are the exact active Evidence task set. The four DROP records must not receive Evidence tasks.

### Core implementation / contracts

Use the current repository Core exactly as reviewed from main `6267de3f6876f491950139757bfdf1085fc07bdc`, including:

- `scripts/survey_evidence_v2.py`
- `scripts/survey_completeness_v2.py`
- `scripts/survey_stage_validation_v2.py`
- `config/prompts/evidence-verification-v2.md`
- current schemas referenced by those modules

Do not patch shared Core in this task. If the current Core cannot materialize a valid candidate, stop with a deterministic failure record for Sol.

## 3. Required read order

Before writing production artifacts, read in order:

1. `sources/2026-W33/production-state.json`
2. `sources/2026-W33/production-profile.json`
3. `sources/2026-W33/execution/index.md`
4. `config/survey-production-v2.json`
5. `config/prompts/evidence-verification-v2.md`
6. `scripts/survey_evidence_v2.py`
7. `scripts/survey_completeness_v2.py`
8. `scripts/survey_stage_validation_v2.py`
9. `sources/2026-W33/discovery/discovery-accepted-v2.json`
10. `sources/2026-W33/discovery/discovery-v2.jsonl`
11. canonical Screening acceptance above
12. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
13. `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
14. `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`
15. this handoff

If repository authority materially disagrees with this handoff, stop before candidate writes.

## 4. Current Core semantic structure

Do not collapse these layers:

`Discovery / Screening -> Evidence Task -> factual Evidence Card -> Edition Evidence View -> deterministic Materiality Ledger -> Profile Completeness`

### Evidence Tasks

Current Core creates one task for each non-DROP Discovery record. For W33 the expected task count is **37**.

Each task is bound to exactly one accepted Discovery source record and inherits the Screening verification targets. Do not create Evidence tasks for DROP records.

### Evidence Cards

Evidence Cards are reusable factual authority. They must not contain article-selection or issue-architecture decisions.

Every factual claim, event, metric, limitation, entity, and role must conform to the current Evidence Card contract and exact task basis.

### Edition Evidence Views

Weekly significance belongs here. Each accepted Evidence Card receives one Edition Evidence View binding the exact Evidence bytes and proposing one materiality status:

- `MATERIAL`
- `CONTEXT`
- `NON_MATERIAL`
- `HOLD`

Weekly annotations must follow the current schema, including `why_this_issue`, `window_relation`, and `carry_over`.

### Materiality Ledger

The Materiality Ledger is a **deterministic Core derivation** from Discovery + Screening + accepted Evidence + accepted Edition Views. Do not hand-edit its per-record disposition.

The Ledger must contain exactly one row for every one of the 41 Discovery records. DROP records receive the Core-defined downstream treatment without an Evidence task; non-DROP records must have exactly one Evidence task and one Edition View.

### Profile Completeness

Build and validate Profile Completeness from the exact Profile, Ledger, and accepted upstream artifacts using current Core. Do not manually force `READY`, `LIMITED`, or `INCOMPLETE`.

## 5. Source authority and research boundary

### Binding rule

The Evidence Card source set is frozen by the generated Evidence Task. Current Core requires Evidence sources to already be represented by that task's accepted Discovery source record.

Therefore Luna may:

- read the exact bound Raw captures;
- retrieve/read the exact bound source locator when necessary to understand the source;
- extract source-local facts, chronology, limitations, claims, metrics, authorship/publisher information, and technical details;
- use the current accepted Discovery provenance to understand why the task exists.

Luna must not:

- add an arbitrary new URL/source to an Evidence Card;
- mutate Discovery or Screening to make a new source fit;
- substitute a secondary source for missing first-party evidence;
- promote an unbound web search result into Evidence authority;
- use X/community material as technical-claim authority.

If the bound source is insufficient and a materially different source would be required, record a `SOURCE_GAP` in the Luna session report and keep the factual/materiality result appropriately unresolved under the Core contract. Do not silently expand source authority.

### Source hierarchy within the bound task source

Interpret bound sources according to their nature:

1. first-party official release, product page, documentation, repository release, changelog, or event page — primary for facts that page actually states;
2. authored paper / project primary source — primary for the authors' method, experiment, and reported result claims;
3. official index/changelog — strong for chronology and index-level statements, but do not infer event details absent from the source;
4. X/social/community — discovery/context signal only, never technical authority;
5. Raw capture — exact provenance copy of its originating source; Raw storage does not upgrade the authority class of the underlying source.

Do not infer independent verification where only vendor/project/author claims exist.

## 6. Factual Evidence policy

Evidence sufficiency and weekly Materiality are different judgments.

For each task, resolve every current Core verification target explicitly. Use the current Evidence Card status contract and source bindings exactly as implemented.

Policy meaning:

- `VERIFIED`: the exact allowed source supports every required factual verification strongly enough for the card to close under current Core.
- `PARTIAL`: useful factual evidence exists, but one or more verification targets remain unresolved or bounded. A PARTIAL card may still support a non-HOLD Materiality proposal only when the unresolved point does not materially affect that proposal.
- `NEEDS_MORE`: the decision materially depends on evidence unavailable from the accepted task source set, or access/source limitations prevent safe resolution.
- `REJECTED`: the allowed evidence directly defeats the substantive premise that the task was expected to verify, or the factual target is otherwise invalid under the Core contract.

Use the actual current schema/status values and validation rules if they differ in naming detail; do not patch Core to match prose in this handoff.

General rules:

- positive factual claims require explicit source binding;
- every required verification target must be represented exactly as Core requires;
- preserve `ACCESS_LIMITED` where access is actually limited;
- label performance/benchmark claims as vendor-, project-, or author-reported unless the bound source itself supplies independent verification;
- distinguish publication date, announcement date, release availability date, and observation date;
- distinguish a model/product identity from a surrounding index or distribution event;
- do not convert Screening KEEP into assumed factual verification.

## 7. Weekly Materiality rubric

Luna is explicitly authorized to make a **first-pass Materiality proposal** in each Edition Evidence View under this rubric. Sol retains semantic acceptance authority.

### `MATERIAL`

Propose `MATERIAL` when the reviewed factual evidence establishes a distinct development relevant to W33 and the development has meaningful issue-level significance, especially under the Profile's `current-relevance` and `technical-significance` dimensions.

Typical qualifying characteristics include one or more of:

- a substantive model/release/API/runtime capability change;
- a meaningful deployment, availability, distribution, or lifecycle change;
- a technically significant open-source/runtime/framework release;
- research with a materially new method, empirical result, benchmark, systems contribution, or diagnostic insight relevant to current generative AI;
- a development with ecosystem impact beyond routine maintenance or a mere index listing.

Do not propose `MATERIAL` solely because Screening said KEEP. Current Core restrictions on Evidence status/direct support always win.

### `CONTEXT`

Propose `CONTEXT` when the item is factual and useful to the issue but is primarily:

- chronology or corroboration;
- a secondary distribution/partner dimension of a larger event;
- ecosystem/background context;
- a community/discovery signal;
- a useful related detail that should inform interpretation but does not merit treatment as an independent main development.

### `NON_MATERIAL`

Propose `NON_MATERIAL` when evidence establishes that the item should not contribute as a meaningful W33 development, for example:

- no qualifying W33 event is established;
- the item is stale or purely prior-window continuity with no W33 delta;
- a dedicated source supersedes an index/process record and the residual record adds no useful issue context;
- the change is routine and lacks meaningful technical/current significance;
- the factual premise is rejected.

A current Core `REJECTED` Evidence result must map to the Core-required `NON_MATERIAL` treatment.

### `HOLD`

Propose `HOLD` only for a real evidence insufficiency that prevents a safe materiality decision, not merely because the worker is uncertain.

Use `HOLD` when:

- chronology/event identity remains materially unresolved;
- a required first-party fact is inaccessible;
- the accepted task source cannot resolve a verification target that changes whether the item is material;
- a new source would be required but is outside this phase's accepted Discovery authority.

A current Core `NEEDS_MORE` Evidence result must remain `HOLD` as required by Core.

## 8. Candidate-specific policy

### KEEP records

KEEP means “worthy of factual Evidence work,” not “automatically MATERIAL.” Luna may propose MATERIAL, CONTEXT, NON_MATERIAL, or HOLD according to reviewed evidence and this rubric.

### INSPECT and MAYBE

The 8 INSPECT and 3 MAYBE records are specifically delegated to Luna for first-pass resolution under this policy.

For each of these 11 records, the Luna session report must state:

- discovery ID;
- factual Evidence status;
- proposed Materiality;
- decisive verification target(s);
- evidence basis;
- remaining uncertainty/source gap;
- why the proposal follows this rubric.

Do not preserve MAYBE/INSPECT merely because Screening used those labels; resolve them as far as the frozen Evidence source permits.

### Carry-over

For a carry-over record, establish whether there is a **distinct W33 delta**: new availability, distribution, lifecycle change, release event, or other current change.

- distinct W33 delta established -> evaluate normally for MATERIAL/CONTEXT;
- only W32/prior continuity or an old event -> normally NON_MATERIAL;
- W33 applicability cannot be safely resolved from the bound source -> HOLD.

`carry_over` and `window_relation` in the Weekly Edition View must reflect the factual chronology, not the desired editorial outcome.

### Duplicate groups

Do not collapse duplicate groups during Evidence.

Evaluate every non-DROP record source-locally and preserve overlap in the Edition View rationale. Selection will later decide canonical representative/single-home treatment.

Important current groups include, but are not limited to:

- `openai-daybreak`
- `grok-4.6`
- `gemini-3.7-flash`
- `glm-5.3`
- `qwen3.8-27b`

Do not turn a duplicate relationship into unsupported factual equivalence.

### `x-weekly-signal-wave`

X/community evidence is non-authoritative for technical claims. This item may normally support `CONTEXT` if its community/discovery role is factually established. It must not become `MATERIAL` solely on the basis of X/social assertions.

### Official index records

An official index may be useful chronology/context. If the same substantive event has a dedicated first-party event record, the index will often be CONTEXT or NON_MATERIAL depending on whether it adds useful issue information.

Do not hard-code all indexes as non-material. If an index itself directly establishes a distinct W33 event not otherwise represented, Luna may propose MATERIAL, but must flag overlap/dedup implications for Sol.

### Research papers

For papers:

- establish current relevance from the accepted chronology;
- assess technical significance/novelty from the paper itself;
- preserve authorship attribution;
- report benchmark/performance conclusions as author-reported unless independent evidence is actually bound;
- inspect whether a journal extension meaningfully adds to earlier work when Screening specifically requests that check.

### Software/runtime releases

Separate:

- user-visible or architectural feature changes;
- compatibility/model-support changes;
- fixes/maintenance;
- project-reported performance claims.

Routine maintenance alone should not be elevated to MATERIAL merely because it is a fresh release.

## 9. Profile Completeness policy

The current W33 Profile includes blocking research obligations for:

- `weekly:current-relevance`
- `weekly:technical-significance`

and scope dimensions including:

- `current-relevance`
- `technical-significance`
- `originality`
- `independent-verification`
- `ecosystem-impact`

The existing required X Source Intake remains bound as Discovery/context authority; do not recollect X in this task.

Use current `survey_completeness_v2` / current Core derivation and validation to create Profile Completeness from the exact accepted Evidence/Edition Views/Materiality Ledger.

Do not manufacture `READY`. If the Core result is `LIMITED` or `INCOMPLETE`, preserve it and explain the exact obligation/source gap.

A genuine unresolved completeness result is not permission to mutate Discovery or Screening in this task. Stop for Sol review. Sol will decide whether a bounded upstream repair, additional source authority, or Exception Gate is required.

## 10. Required execution sequence

### E1 — Preflight

Verify and record:

- exact caller-supplied branch SHA;
- reviewed main unchanged unless Sol explicitly supplies a newer authority;
- State is `CANDIDATES_NORMALIZED` / `stage:evidence-materiality-completeness`;
- Discovery acceptance and Screening acceptance validate;
- 41 Screening records exist;
- exact aggregate remains 26 / 8 / 3 / 4;
- generated Evidence package contains exactly 37 tasks and excludes exactly the 4 DROP records;
- no pre-existing conflicting incomplete Evidence/View accepted run exists.

### E2 — Generate current-Core Evidence package

Use current `survey_evidence_v2.prepare_evidence_package` or the repository-prescribed equivalent.

The generated package must bind the exact:

- Production Profile;
- Production State;
- Discovery;
- Screening acceptance;
- Evidence prompt/contracts.

Do not manually invent task IDs or task source sets when Core can generate them.

### E3 — Source-local factual research and Evidence Cards

For every one of the 37 tasks:

1. read its exact source record and verification targets;
2. inspect bound Raw capture(s) and/or exact bound locator as needed;
3. build one schema-valid Evidence Card using only allowed source binding;
4. resolve verification targets as far as the source supports;
5. preserve attribution, access limitation, and claim class accurately;
6. do not include Selection or Architecture recommendations in the factual card.

Materialize the complete exact one-result-per-task set and accept it through current Core into the canonical content-addressed Evidence accepted run.

### E4 — Edition Evidence Views / Materiality proposals

For every accepted Evidence task, create one Weekly Edition Evidence View that:

- binds the exact Evidence Card SHA;
- proposes `MATERIAL`, `CONTEXT`, `NON_MATERIAL`, or `HOLD` under this handoff;
- supplies a concise but decision-useful rationale;
- assigns only Production Profile scope dimensions;
- fills Weekly annotations accurately;
- respects current Core Evidence-status/materiality restrictions.

Accept the complete View set through current Core into its canonical content-addressed accepted run.

### E5 — Materiality Ledger

Call current Core `build_materiality_ledger(...)` against the exact accepted artifacts and write the canonical ledger expected by the current edition workflow.

Do not manually alter a derived row. Independently validate that the stored Ledger equals the current Core derivation.

The Ledger must contain exactly 41 Discovery rows with no silent drop.

### E6 — Profile Completeness

Build the current Profile Completeness result using current Core and validate it against:

- Production Profile;
- Discovery;
- Screening acceptance;
- Evidence acceptance;
- Edition View acceptance;
- Materiality Ledger;
- current implementation identity.

Preserve the resulting status and limitations exactly.

### E7 — Candidate validation and commit

Before commit, independently validate:

- 37 Evidence tasks exactly;
- one valid Evidence Card per task;
- one Edition View per accepted Evidence result;
- every View binds exact Evidence bytes;
- all required verification targets are accounted for;
- no technical claim depends only on X/community evidence;
- Materiality Ledger equals deterministic Core derivation and contains all 41 Discovery IDs;
- Profile Completeness validates;
- Production State bytes/hash are unchanged from task start;
- no Evidence/Materiality/Completeness checkpoint was created;
- no Selection/Architecture artifact exists because of this task.

Commit candidate artifacts plus one Luna session record and stop for Sol review.

## 11. Allowed repository writes

Luna may write only the edition-local candidate artifacts required by current Core for this stage, including as applicable:

- current-Core Evidence package/tasks/results/accepted content-addressed run under `sources/2026-W33/**`;
- current-Core accepted Edition Evidence View set under `sources/2026-W33/**`;
- canonical W33 Materiality Ledger generated by current Core;
- canonical W33 Profile Completeness result generated by current Core;
- one Luna session record under `sources/2026-W33/execution/sessions/`.

Use the exact paths produced or required by current Core. Record every path in the Luna session report.

Execution-local scratch inputs may be created outside the repository and must not be committed.

Do not modify:

- `sources/2026-W33/production-state.json`
- `sources/2026-W33/production-profile.json`
- `sources/2026-W33/discovery/**`
- `sources/2026-W33/screening/**`
- prior checkpoint/bridge-run/request/review/handoff history
- shared `config/**`, `schemas/**`, `scripts/**`, workflows
- Selection paths
- Architecture paths
- Draft/publication paths

Do not update `execution/index.md` in this candidate task unless repository execution policy strictly requires it; Sol will update the recovery index after review.

## 12. Explicit prohibitions

Luna must not:

- run `ADVANCE_STAGE`;
- create the CANDIDATES_NORMALIZED Stage Checkpoint by hand or through the operator bridge;
- mark Evidence/Materiality/Completeness machine checkpoints passed;
- change Screening decisions;
- turn Evidence research into Selection decisions;
- collapse duplicate groups;
- decide final single-home/carry-over disposition for publication;
- propose issue Architecture yet;
- draft article prose;
- broaden accepted source authority without returning to Sol;
- use X/social as technical authority;
- guess unresolved chronology, identity, or factual conflicts;
- modify shared Core to get a desired result;
- infer Human approval.

## 13. Luna session record requirements

Create one stable session record such as:

`sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-20260830-r1.md`

It must contain at minimum:

### Authority / Git

- exact caller-supplied starting SHA;
- exact local ending SHA and canonical GitHub ending SHA if transport reconstruction causes divergence;
- reviewed-main SHA;
- starting and ending Production State SHA-256;
- exact changed paths;
- fast-forward / force status;
- any local↔remote SHA mapping caused by transport.

### Evidence

- Evidence package path/SHA-256;
- task count: expected 37;
- Evidence acceptance path/result-set SHA-256/acceptance SHA-256;
- Evidence status distribution;
- source-access limitations;
- `SOURCE_GAP` list;
- confirmation that every technical claim uses an allowed bound source.

### Materiality / Edition Views

- Edition View acceptance path/view-set SHA-256/acceptance SHA-256;
- Materiality distribution across the 37 active tasks;
- detailed proposal table for all 8 INSPECT + 3 MAYBE records;
- detailed proposal table for all active carry-over records;
- every `HOLD` record and why it is held;
- every `NON_MATERIAL` record and why;
- duplicate-group implications that Selection must later resolve;
- X/community boundary confirmation.

### Derived authorities

- Materiality Ledger path/SHA-256;
- proof that stored Ledger equals current Core derivation;
- Ledger row count: expected 41;
- Profile Completeness path/SHA-256;
- Completeness overall status;
- obligation status summary;
- residual limitations.

### Validation / stop

- commands/validators run and result;
- confirmation Production State was not modified;
- confirmation no checkpoint/advance occurred;
- unresolved issues;
- exact stop reason.

Use one of these stop statuses:

- `READY_FOR_SOL_REVIEW`
- `COMPLETENESS_INCOMPLETE_NEEDS_SOL_REVIEW`
- `SOURCE_GAP_NEEDS_SOL_REVIEW`
- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`

A non-blocking source limitation may be recorded while still using `READY_FOR_SOL_REVIEW`; use `SOURCE_GAP_NEEDS_SOL_REVIEW` when the gap materially prevents a required candidate result.

## 14. Sol review criteria after Luna stops

Sol will review the exact committed candidate for:

1. exact 37-task coverage and exclusion of the four DROP records;
2. factual claim/source binding and attribution;
3. verification-target completeness;
4. correct source-authority and X/community boundary;
5. factual Evidence status appropriateness;
6. all 11 INSPECT/MAYBE resolutions;
7. carry-over chronology and W33-delta reasoning;
8. duplicate-group treatment without premature collapse;
9. Weekly Materiality rubric fidelity;
10. Edition View rationale/annotations;
11. deterministic 41-row Materiality Ledger equality;
12. Profile Completeness correctness;
13. changed-path boundary and unchanged Production State;
14. absence of Selection/Architecture work.

If Sol passes the candidate, a **separate** advancement handoff will authorize the deterministic Evidence/Materiality/Completeness checkpoint and transition:

`CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED`

Only after that transition may Selection begin.
