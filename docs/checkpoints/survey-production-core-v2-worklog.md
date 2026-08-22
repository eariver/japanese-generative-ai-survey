# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, commits, unresolved execution issues, and the exact next action. It does **not** override semantic/design contracts; those are governed by the authority index and current amendments.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and explicitly merged. No frozen historical release may be rewritten by this improvement work.

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-007 closed after post-implementation audit; WU-008 started**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Current production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — rechecked after WU-007 and unchanged.
- WU-007 audited head: `bf87f451b2e96c9b92d66c685f946cd3d062b44b`.
- Draft PR: `#310 Survey Production Core v2 implementation`; intentionally draft until WU-005–WU-011 form one coherent candidate.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**
- Active work unit: **WU-008 — Candidate Matrix + internal Selection + generic Architecture**
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED until full candidate is merged to main**.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**.
- Legacy `weekly/2026-W33-work` = optional benchmark/provenance fixture only; migration/reuse is never a Pilot acceptance criterion.
- SP001 = first true Thematic Profile production validation; no fabricated Weekly fields or fake bounded historical window.
- W34 follows W33 finding consolidation; SP002/SP003 follow SP001 finding consolidation.
- Normal Human Gates: Architecture Review, then exact-byte Publication Preview. Candidate Selection is internal.
- First external Pilots start only after a full production-capable v2 path through Publication Preview/Freeze/Release is merged to `main`.

## 4. Phase / work-unit status

| Work unit | Status | Exit / primary evidence |
|---|---|---|
| WU-000 | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement plan + persistent checkpoint |
| WU-001 / WU-001A | `COMPLETE / AMENDED` | component inventory + profile-pollution audit through Synthesis |
| WU-002 | `COMPLETE / AMENDED` | normalized Core/Profile/Human-Gate/temporal/release contracts |
| WU-003 / WU-003B / WU-003C | `COMPLETE` | historical invariants + all-15 production deep audit |
| WU-004 / WU-004B | `COMPLETE / SUPERSEDED IN PART` | authoritative second-audit vertical-slice amendment |
| WU-005 | `COMPLETE` | Profile/State/contract+implementation identity/anti-divergence foundation |
| WU-006 | `COMPLETE / POST-AUDIT HARDENED` | discovery-edge provenance + profile-neutral Screening v2 + self-contained accepted archive |
| **WU-007** | **`COMPLETE / POST-AUDIT HARDENED`** | factual Evidence + Edition View + Materiality + Completeness; all cross-regression CI green |
| **WU-008** | **`IN_PROGRESS`** | Matrix + internal Selection + generic Architecture |
| WU-009 | `PLANNED` | generic Drafting + Profile Synthesis |
| WU-010 | `PLANNED` | executable orchestration + Finding/Repair Set |
| WU-011 | `PLANNED` | P0 quality integration + full Pilot bootstrap |

## 5. WU-005 completion record

Implemented:
- `config/survey-production-v2.json`;
- `schemas/survey-production-profile.schema.json`;
- `schemas/survey-production-state.schema.json`;
- `scripts/survey_production_v2.py`;
- `tests/test_survey_production_v2.py`;
- dedicated v2 CI.

Key guarantees:
- Weekly calendar reuses tested cutoff-to-cutoff logic;
- Thematic open-history/current-state profiles have no fake bounded window;
- `production-state.json` is sole v2 authority;
- Profile bytes, semantic contract, implementation commit/orchestrator, and legacy fixture bytes are independently drift-checked;
- state initialization is non-destructive and lifecycle transition is monotonic/authoritative.

Primary implementation commits:
`7e081eb4`, `d7b335fd`, `2c31558d`, `591369ba`, `f5938e79`, `b2e0d8e5`.

## 6. WU-006 completion + audit-hardening record

Implemented:
- `schemas/survey-discovery-record.schema.json`;
- `schemas/screening-v2-run-package.schema.json`;
- `schemas/screening-v2-batch-result.schema.json`;
- `config/prompts/source-screening-v2.md`;
- `scripts/survey_screening_v2.py`;
- `tests/test_survey_screening_v2.py`;
- screening contract files added to pipeline-contract hash basis;
- v2 CI extended through Screening and changed to sparse checkout for fast deterministic validation.

Discovery origins:
`BASE`, `CARRY_OVER`, `REFERENCE_EXPANSION`, `SUCCESSOR_EXPANSION`, `PARALLEL_EXPANSION`, `COMPETING_EXPANSION`, `BRIDGE_EXPANSION`, `GAP_FILL`.

Post-WU-007 audit hardening additionally established:
- accepted Screening runs preserve exact `package.json`, exact input batches, exact result batches, and flattened decisions;
- content-addressed run identity is recomputed during revalidation;
- accepted archive byte tampering fails both direct Screening validation and downstream Evidence preparation;
- acceptance is idempotent only when an existing content-addressed archive fully revalidates.

Primary hardening commits:
- archive validation/retention `011685ac53cb1b525f1f3bf81d7bcc5a7d8d532b`
- archive regression tests `f4118a55c503300aab77f83ff9336888045d5db9`
- test harness corrections `2a026a4dbec28b6c2219eb5afb9722137352a5a6`, `bf87f451b2e96c9b92d66c685f946cd3d062b44b`

## 7. WU-007 completion record

Implemented:
- `config/prompts/evidence-verification-v2.md`;
- `schemas/evidence-v2-run-package.schema.json`;
- `schemas/evidence-v2-task.schema.json`;
- `schemas/evidence-v2-card.schema.json`;
- `schemas/edition-evidence-view.schema.json`;
- `schemas/materiality-ledger.schema.json`;
- `schemas/profile-completeness-result.schema.json`;
- `scripts/survey_evidence_v2.py`;
- `scripts/survey_completeness_v2.py`;
- `tests/test_survey_evidence_v2.py`;
- `tests/test_survey_completeness_v2.py`;
- v2 pipeline-contract identity extended to include WU-007 semantic contracts;
- dedicated CI extended through Evidence/Edition View/Materiality/Completeness.

Key guarantees:
- factual Evidence has no required Weekly editorial significance;
- Edition Evidence View is the edition-specific significance/materiality authority;
- every event/claim/metric/limitation has explicit subject binding;
- entity roles distinguish `PRIMARY_SUBJECT`, `COMPARATOR`, and `RELATED` so comparator-owned values cannot be silently attached to the primary subject;
- Evidence sources are constrained to supplied Screening-derived source records;
- accepted Evidence preserves exact Task bytes and exact result bytes and revalidates package/task/result identity;
- Materiality Ledger preserves `MATERIAL`, `CONTEXT`, `NON_MATERIAL`, `HOLD`, `DUPLICATE`, and `EXCLUDED` rather than collapsing semantically distinct outcomes;
- exactly one Materiality row exists per Discovery record;
- `REJECTED` / `NEEDS_MORE` Evidence cannot masquerade as settled material Evidence;
- Profile Completeness is exact-basis-bound and covers every Profile scope dimension;
- Discovery `obligation_ids` must appear as named completeness obligations and reference every Discovery that declared them;
- Thematic closure requires saturation/gap-fill evidence and cannot close while material obligations remain open;
- Weekly uses the same generic completeness mechanism without a fabricated Thematic closure payload.

### WU-007 P0 regression outcome

- **Issue #166**: silent material disappearance is structurally rejected by exact Discovery↔Screening↔Evidence↔Edition View↔Materiality correspondence and named-obligation closure.
- **Issue #191**: comparator-owned metric/property values fail subject-role validation before Architecture/Drafting.

### WU-007 audit findings repaired before closure

The completion audit found and repaired:
1. one legacy `pytest` dependency inconsistency in repository-wide `unittest` execution; the test was normalized to `unittest` rather than spreading a pytest runtime dependency across workflows;
2. Evidence package result-filename contract/implementation mismatch;
3. accepted Evidence missing exact Task bytes;
4. insufficient revalidation of accepted Screening/Evidence content-addressed identities;
5. insufficient comparator/related-subject structural distinction;
6. Materiality state collapse of material/context/non-material outcomes;
7. missing explicit closure of Discovery-originated named research obligations;
8. WU-006 accepted Screening archive not retaining exact batch/result bytes.

All identified blockers were repaired before closure. No known WU-007 semantic blocker remains.

### WU-007 validation and post-implementation audit

Audited head: `bf87f451b2e96c9b92d66c685f946cd3d062b44b`.

Dedicated v2 CI:
- run `32512736980`: **SUCCESS**;
- 28 v2 tests: **PASS**;
- compile and all v2 JSON contract parse steps: **PASS**.

Cross-regression workflows on the same head:
- Evidence contract CI `32512737031`: **SUCCESS**;
- Screening contract CI `32512736967`: **SUCCESS**;
- Pipeline contract tests `32512736997`: **SUCCESS**;
- Weekly pipeline spine `32512736957`: **SUCCESS**, including committed Raw integrity.

Repository revalidation:
- production `main` rechecked after WU-007: still `2086b396d2f30103d9292b722891be436cd28db5`;
- Draft PR remained mergeable/draft;
- W33/SP001 Pilot production remains intentionally blocked until WU-011/full candidate review/merge.

**WU-007 exit criteria are satisfied.**

## 8. WU-008 active contract

Authoritative guidance: `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` §9–10, as constrained by the second-audit amendment.

Implement:

### Candidate Matrix v2
- consume exact accepted Evidence, Edition Evidence View, Materiality Ledger, and Profile Completeness basis;
- expose shared evidence/materiality/comparison data without turning the Core matrix into a Weekly timing table;
- allow Profile-owned extensions without making them generic mandatory fields;
- preserve traceability from matrix rows to Evidence Task / Discovery / materiality state;
- fail closed if material/context Evidence disappears before Selection.

### Internal Selection v2
- remain an internal SHA-bound editorial checkpoint, not a Human Gate;
- remove generic human-approval fields;
- assign every matrix candidate an explicit selected/hold/reject/inspect disposition and rationale;
- require selected candidates to identify proposed publication/architecture role through Profile/Publication-owned values rather than a global Weekly role enum;
- preserve explicit omission rationale for material/context candidates that are not selected.

### Architecture v2
- generic envelope binds exact Profile, Completeness, Materiality, Matrix, and Selection hashes;
- owns editorial thesis, architecture goals, package list, Evidence assignments, must-cover requirements, boundaries, drafting order, and Profile/Publication extensions;
- Core does not require Weekly-only package vocabulary such as `LATE_BREAKING`, `X_COMMUNITY`, `WATCHLIST_CHRONOLOGY`, or `this_week_summary_written_last`;
- selected non-support Evidence receives one explicit Architecture destination or an explicit structured exception/omission reason;
- Architecture Review summary makes the compression from research breadth to proposed structure auditable.

### WU-008 exit criteria
1. Matrix is profile-neutral at Core level and exact-basis-bound.
2. Every material/context candidate is traceable through Matrix and Selection with no silent disappearance.
3. Selection is internal and contains no Human approval semantics.
4. Publication/package roles are Profile/Publication-owned, not a universal Weekly enum.
5. Architecture is profile-neutral at Core level and binds exact upstream artifacts.
6. Architecture Review summary exposes source/disposition/completeness/selection/destination evidence sufficient to audit Issue #166-style compression.
7. Weekly and Thematic fixtures can both produce valid Matrix/Selection/Architecture without dummy fields from the other Profile.

## 9. Cross-cutting CI status

Current audited baseline entering WU-008 is fully green on the WU-007 head:
- Survey Production Core v2 CI: SUCCESS;
- Evidence contract CI: SUCCESS;
- Screening contract CI: SUCCESS;
- Pipeline contract tests: SUCCESS;
- Weekly pipeline spine: SUCCESS.

The earlier pytest baseline defect is considered resolved by test normalization, not by adding a permanent pytest dependency to every workflow.

## 10. Resume rule

```text
read current main
-> read this worklog for status/next action
-> read docs/survey-production-core-v2-authority.md for semantic authority
-> verify repository reality
-> perform active WU + validation
-> update this ledger before declaring the WU complete
```

**Current action: implement and validate WU-008.**
