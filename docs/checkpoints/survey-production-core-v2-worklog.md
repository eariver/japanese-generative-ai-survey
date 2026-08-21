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

Last updated: **2026-08-22 JST — WU-006 closed; WU-007 started**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Current production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged since implementation start.
- Draft PR: `#310 Survey Production Core v2 implementation`; intentionally draft until WU-005–WU-011 form one coherent candidate.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**
- Active work unit: **WU-007 — Factual Evidence + Edition View + Materiality + Completeness**
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
| **WU-006** | **`COMPLETE`** | discovery-edge provenance + profile-neutral Screening v2; green v2 CI |
| **WU-007** | **`IN_PROGRESS`** | factual Evidence + Edition View + Materiality + Completeness |
| WU-008 | `PLANNED` | Matrix + internal Selection + generic Architecture |
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

A pre-existing branch-wide CI defect was isolated: a `main` test imported `pytest` while the workflow did not install it. The generic workflow dependency repair is isolated in commit `de9b87fe13e50f74a9574bb347b2c0e302d3af16`; it is not a v2 semantic repair.

## 6. WU-006 completion record

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

Key guarantees:
- expansion records bind parent/research obligation provenance;
- Weekly and Thematic share discovery mechanics without sharing completeness semantics;
- Screening decisions are exactly `KEEP|MAYBE|DROP|INSPECT` with free-form scope tags;
- Core Screening has no required `why_now` and no fixed A–L lane enum;
- exact Profile/State/discovery/prompt/result-contract/batch hashes are bound;
- missing, extra, duplicate, or Weekly-only result fields fail closed;
- accepted results are content-addressed and complete-only;
- v1 Screening remains untouched.

Primary commits:
- discovery schema `656e029cbe45e77385f065e0e8a6e6a32447786d`
- result schema `43a3e1f5a79bab6b3af34b91e7fb843e97d52a84`
- package schema `a611790adcf5c41a2680aede2e45dfba983412d6`
- prompt `4a8e87f697eb8e41fba5dbd28200ad7ddfd0e47f`
- implementation `63ed08ac522c2cce4853ac1e7aec50903e4d9221`
- contract binding `c7a6abf1ec067d686263321e9d10a4f8649831ab`
- tests `18e9f5539009d5dc3744321a4664ac4af51acbd9`
- CI sparse-checkout validation `d67e1134f2f5571fcb397dfea13a7eb13ee8539d`

Validation:
- v2 CI run `32509649193`, job `96857528724`: **SUCCESS**.
- checkout/setup/compile/WU-005+WU-006 unit tests/JSON contract parsing all passed.
- lifecycle mutation is intentionally not performed by the Screening acceptance helper; authoritative transition remains a single later dispatcher/state-API path rather than a second ad-hoc mutation path.

## 7. WU-007 active contract

Implement:

### Factual Evidence v2
- remove Weekly editorial significance from factual Evidence;
- retain artifact/source/temporal/claim/metric/limitation/verification facts;
- every concrete claim/metric/property that can be confused with comparator/related entities must bind an explicit subject entity;
- comparator/related subjects are represented explicitly rather than inferred from proximity;
- exact Screening acceptance/task/prompt/result contracts remain hash-bound and complete-only.

### Edition Evidence View
- bind exact factual Evidence SHA;
- own edition-specific significance/materiality annotations;
- Weekly annotations may include why-this-issue/window/carry-over semantics;
- Thematic annotations may include Core/Bridge/Context/Parallel/Competing/Counterexample, branch/transition IDs, inheritance/abandonment relevance, and historical-attribution caveats;
- these annotations are not factual Evidence.

### Materiality Ledger
- every discovery row has an explicit downstream disposition;
- Screening→Evidence/duplicate/exclusion/HOLD and Evidence→Edition View materiality are traceable;
- material discoveries cannot silently disappear;
- ledger is derived/validated, not an independent manually narrated database.

### Profile Completeness
- obligations are Profile-owned and exact-basis bound;
- no source-count minimum;
- Weekly completeness can encode current window/carry-over obligations;
- Thematic closure records expansion passes, final-pass new sources/material obligations, targeted gap-fill completion, open material obligations, limitations, and `COMPLETE|LIMITED|NEEDS_RESEARCH`;
- Thematic `COMPLETE/LIMITED` requires saturation evidence defined by the second audit.

### WU-007 P0 regressions
- #166: a material discovery with no explicit downstream disposition must fail validation even if collection volume is large and output looks coherent;
- #191: an unbound/incorrect subject metric or property must fail before reader-facing drafting.

WU-007 exit criteria:
1. Factual Evidence contains no required Weekly editorial significance.
2. Subject/entity binding is structural for concrete claims/metrics used downstream.
3. Edition Evidence View is the sole v2 authority for profile significance/materiality.
4. Materiality validation blocks silent material drop across implemented stages.
5. Weekly and Thematic completeness validators use different semantics on the same Core mechanism.
6. Thematic closure/saturation is mechanically validated without fixed source counts.
7. #166 and #191 generic fixtures fail before Architecture/Draft layers.

## 8. Cross-cutting CI status

Dedicated v2 CI is green through WU-006. Branch-wide existing workflows continue to run as cross-regression coverage. The isolated `pytest` dependency repair should remove the previously identified baseline failure; do not call the entire branch fully green until a current-head full-suite run completes successfully.

## 9. Resume rule

```text
read current main
-> read this worklog for status/next action
-> read docs/survey-production-core-v2-authority.md for semantic authority
-> verify repository reality
-> perform active WU + validation
-> update this ledger before declaring the WU complete
```

**Current action: implement and validate WU-007.**
