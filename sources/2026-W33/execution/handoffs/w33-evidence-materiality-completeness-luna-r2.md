# 2026-W33 Sol→Luna handoff — Evidence / Materiality / Completeness candidate r2

Status: `READY_FOR_LUNA / EVIDENCE_MATERIALITY_COMPLETENESS_CANDIDATE / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Base detailed handoff: `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`  
Sol/Luna policy authority: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`  
Screening advancement review: `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`  
Current lifecycle at handoff creation: `CANDIDATES_NORMALIZED`  
Current machine next action: `stage:evidence-materiality-completeness`  
Requested stop: Sol review before any `ADVANCE_STAGE`

The caller must give Luna the exact branch commit SHA containing this r2 handoff and the recovery-index update that points to it. Luna must start from that exact SHA and must not silently rebase, merge, force-push, or choose a newer basis. If the branch has moved before execution starts, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 1. Authority relationship to r1

This file is a **corrective authority overlay** for r1. It exists because Sol's post-commit audit found that r1 section 9 incorrectly described W33 Production Profile dimensions.

Execution authority is:

`r1 detailed procedure + r2 corrections below`, with **r2 winning on every conflict**.

Do not execute r1 standalone. Read r1 for the full bounded procedure, then apply this r2 before any production-artifact write.

All r1 rules remain in force except where this r2 explicitly replaces or clarifies them.

## 2. Defect corrected by r2

The actual committed W33 Production Profile is:

`sources/2026-W33/production-profile.json`

Its exact `research_scope.scope_dimensions` values are:

- `current relevance`
- `technical significance`
- `carry-over obligations`

Its exact `research_scope.initial_obligations` are:

1. `weekly:current-relevance`
   - dimension: `current relevance`
   - establish which developments materially belong in the completed Weekly issue and why they matter to the issue;
2. `weekly:technical-significance`
   - dimension: `technical significance`
   - verify and prioritize technical significance without relying on Weekly timing alone;
3. `weekly:carry-over`
   - dimension: `carry-over obligations`
   - explicitly dispose every carry-over obligation inherited from prior Weekly work.

The r1 statements naming `originality`, `independent-verification`, and `ecosystem-impact` as W33 Profile scope dimensions are **incorrect and superseded**. Those concepts may be useful analytical considerations when the evidence supports them, but they are not legal values for W33 `scope_dimensions` and they must not be invented as Profile Completeness dimensions or obligations.

The r1 statement that only `weekly:current-relevance` and `weekly:technical-significance` are the current W33 blocking obligations is also incomplete. `weekly:carry-over` is an explicit initial obligation and must be retained and disposed by Profile Completeness.

## 3. Corrected Profile Completeness policy

Replace r1 section 9 with this section.

### Exact Profile dimensions

Every Edition Evidence View `scope_dimensions` value must come only from the exact committed Profile values:

- `current relevance`
- `technical significance`
- `carry-over obligations`

Do not normalize these strings to hyphenated spellings. Do not add adjacent analytical concepts as dimensions.

### Exact initial obligations

Profile Completeness must preserve all three initial obligations exactly by obligation ID and dimension:

- `weekly:current-relevance` → `current relevance`
- `weekly:technical-significance` → `technical significance`
- `weekly:carry-over` → `carry-over obligations`

Current `survey_completeness_v2.py` requires Profile initial obligations to be retained; silent omission is a validation failure.

### Carry-over obligation treatment

The `weekly:carry-over` obligation is not a cosmetic annotation. Luna must explicitly account for every inherited carry-over record/obligation that is represented in the accepted W33 Discovery provenance.

For each active carry-over item:

- establish whether a distinct W33 delta exists;
- set Weekly `window_relation` and `carry_over` from factual chronology;
- propose Materiality under the r1 rubric;
- preserve unresolved timing/source gaps rather than guessing;
- ensure the relevant carry-over Discovery/Evidence references are available to the Completeness obligation row as current Core requires.

For prior carry-over obligations that are represented only by records already disposed at Screening, preserve the machine-readable downstream disposition rather than silently dropping the obligation.

### Completeness status

Build and validate Profile Completeness from the exact committed:

- Production Profile;
- Discovery;
- Screening acceptance;
- Evidence acceptance;
- Edition Evidence View acceptance;
- deterministic Materiality Ledger;
- current implementation identity.

Do not force `READY`, `LIMITED`, or `INCOMPLETE`. Preserve the Core-derived status and exact residual limitations.

If any of the three initial obligations cannot be safely closed under the accepted Evidence source authority, stop for Sol review with the actual limitation or `NEEDS_RESEARCH` state. Do not mutate Discovery/Screening or broaden source authority in this candidate task.

## 4. Materiality rubric clarification

The r1 Materiality rubric remains authoritative, with this exact Profile alignment:

- `current relevance`: whether the development materially belongs to W33 under the committed rolling window / explicit carry-over policy;
- `technical significance`: whether the verified change is technically meaningful enough to matter for the Weekly issue, rather than merely fresh;
- `carry-over obligations`: whether inherited prior-week obligations have been explicitly resolved, retained as current delta/context, rejected as stale continuity, or held because the frozen source authority cannot resolve them.

`originality`, `independent verification`, and `ecosystem impact` may inform Luna's reasoning when directly supported, but Luna must not treat them as separately required Profile dimensions or create Completeness obligations for them unless repository authority independently introduces them.

## 5. Corrected required read order

Before any production-artifact write, Luna must read in order:

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
11. canonical Screening acceptance `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json`
12. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
13. `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
14. `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`
15. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
16. this r2 handoff

If r1 and r2 differ, r2 wins. If either handoff differs from the exact committed Production Profile or current Core schema/invariants, the exact repository artifact/Core contract wins for machine shape and Luna must stop and report the semantic conflict instead of inventing a repair.

## 6. Execution scope retained from r1

All other r1 execution requirements remain unchanged, including:

- exactly 37 Evidence tasks for the 37 non-DROP Screening records;
- no Evidence tasks for the four DROP records;
- source authority frozen to each generated task's accepted Discovery source record;
- factual Evidence Card separated from Weekly Edition Evidence View;
- Luna may produce first-pass factual status and Materiality proposals under the Sol rubric;
- `KEEP` does not imply `MATERIAL`;
- the 8 INSPECT + 3 MAYBE records must receive explicit first-pass resolutions;
- active carry-over records must receive explicit W33-delta analysis;
- duplicate groups remain uncollapsed during Evidence;
- X/community remains discovery/context and cannot become technical authority;
- Evidence/View accepted runs must use current Core content-addressed acceptance;
- Materiality Ledger must be deterministic Core derivation with exactly 41 Discovery rows;
- Profile Completeness must validate under current `survey_completeness_v2.py`;
- candidate commit must leave Production State unchanged at `CANDIDATES_NORMALIZED`;
- no Evidence/Materiality/Completeness checkpoint or `ADVANCE_STAGE` in this task;
- no Selection, Architecture, Draft, publication, or Human Gate work;
- Luna commits candidate artifacts plus one session record and stops for Sol review.

## 7. Additional validation required by r2

Before commit, Luna must add these checks to r1 E7 validation:

1. Production Profile scope dimensions read back exactly as `current relevance`, `technical significance`, `carry-over obligations`;
2. every Edition View `scope_dimensions` value is one of those exact three strings;
3. Profile Completeness contains and preserves all three initial obligation IDs;
4. `weekly:carry-over` uses dimension `carry-over obligations` and is not silently omitted;
5. no Completeness row invents `originality`, `independent-verification`, or `ecosystem-impact` as a W33 Profile dimension;
6. the Luna session report explicitly records the disposition/status of `weekly:carry-over` and any residual carry-over limitation.

Failure of any of these checks is `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW` unless the root cause is a genuine repository-authority conflict, in which case use `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 8. Stop condition

The endpoint remains:

`EVIDENCE + MATERIALITY + COMPLETENESS CANDIDATE COMMITTED -> STOP FOR SOL REVIEW`

Allowed stop statuses remain those defined by r1:

- `READY_FOR_SOL_REVIEW`
- `COMPLETENESS_INCOMPLETE_NEEDS_SOL_REVIEW`
- `SOURCE_GAP_NEEDS_SOL_REVIEW`
- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`

Do not advance to `EVIDENCE_REVIEWED`. Sol must review the exact committed candidate first.
