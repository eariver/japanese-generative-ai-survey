# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, commits, unresolved execution issues, and the exact next action. It does **not** override semantic/design contracts; those are governed by the authority index and current amendments.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and explicitly merged.

No frozen historical release may be rewritten by this improvement work.

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-005 closed; WU-006 started**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Current production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — revalidated before WU-005 and unchanged.
- Draft PR: `#310 Survey Production Core v2 implementation`; intentionally draft until WU-005–WU-011 form one coherent candidate.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**
- Active work unit: **WU-006 — Research discovery expansion + Screening v2**
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED until full candidate is merged to main**.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**.
- Legacy `weekly/2026-W33-work` = optional benchmark/provenance fixture only; migration/reuse is never a Pilot acceptance criterion.
- SP001 = first true Thematic Profile production validation; no fabricated Weekly fields or fake bounded historical window.
- W34 follows W33 finding consolidation.
- SP002/SP003 follow SP001 finding consolidation.
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
| **WU-005** | **`COMPLETE`** | v2 Profile/State/contract identity/implementation identity/anti-divergence foundation |
| **WU-006** | **`IN_PROGRESS`** | discovery-edge provenance + profile-neutral Screening v2 |
| WU-007 | `PLANNED` | factual Evidence + Edition View + Materiality + Completeness |
| WU-008 | `PLANNED` | Matrix + internal Selection + generic Architecture |
| WU-009 | `PLANNED` | generic Drafting + Profile Synthesis |
| WU-010 | `PLANNED` | executable orchestration + Finding/Repair Set |
| WU-011 | `PLANNED` | P0 quality integration + full Pilot bootstrap |

## 5. WU-005 completion record

### Implemented

- `config/survey-production-v2.json`
  - contract/schema/orchestrator versions;
  - research/publication Profile registry;
  - only two normal Human Gates;
  - v2 state authority and read-only legacy mode.
- `schemas/survey-production-profile.schema.json`
  - `ROLLING_WINDOW`, `BOUNDED_PERIOD`, `OPEN_HISTORY_AS_OF`, `CURRENT_STATE_AS_OF` separated;
  - Thematic open-history modes require no fake start/end.
- `schemas/survey-production-state.schema.json`
  - profile SHA, semantic contract SHAs, executable repository SHA, orchestrator version;
  - Human Gate state, lifecycle, machine checkpoints, read-only legacy reference/history.
- `scripts/survey_production_v2.py`
  - Weekly Profile resolver reuses tested `weekly_pipeline.latest_cutoff` / cutoff-to-cutoff window;
  - Thematic Profile resolver;
  - deterministic contract hashing;
  - non-destructive initialization;
  - one authoritative v2 transition API;
  - profile/contract/implementation/legacy-byte anti-divergence checks.
- `tests/test_survey_production_v2.py`
  - W33 fixed-time cutoff resolution;
  - future issue rejection;
  - Thematic no-window fiction;
  - non-destructive initialization;
  - monotonic one-step transition;
  - implementation/profile/contract/legacy drift rejection.
- `.github/workflows/survey-production-v2-ci.yml`
  - v2 compile/test/JSON-contract CI.

### Commits

- documentation authority hardening: `450e885ede830742f02fe64015f2dec8a579f94d`
- WU-005 start checkpoint: `8e767071b2902bf6661b6f6d7776a04b04c4d082`
- v2 contract manifest: `7e081eb4bf69659150e1601397eb70b34fc84fd8`
- Profile schema: `d7b335fd8ceb398db0fd50a4752a2727cf281b23`
- State schema: `2c31558de7b0e81b2391492ce45d80eb3807847e`
- Profile/state implementation: `591369bac56439883484db550ff3f683cc743c51`
- WU-005 tests: `f5938e79c6fc4a8e824baa06dc9bb4b8de4b786a`
- v2 CI: `b2e0d8e53c964cb90b781f83945fc89a777df0b6`

### Validation

The first full repository `Pipeline contract tests` run compiled the new implementation and executed 455 discovered tests. **All nine WU-005 tests passed.** The sole suite error was an unrelated pre-existing baseline defect: `tests/test_prepare_annual_reader_notes_ja_overrides.py` imports `pytest`, while `main`'s `pipeline-contract-tests.yml` did not install pytest.

The defect was verified directly on `main` and repaired independently on this branch:

- baseline CI dependency repair: `de9b87fe13e50f74a9574bb347b2c0e302d3af16`

The CI rerun remains a branch-wide regression check; it is not evidence of a WU-005 semantic failure. WU-005 exit criteria are satisfied by the executed tests and exact failure isolation.

## 6. WU-006 active contract

Implement while preserving the mature v1 mechanical guarantees below their valid semantic boundary:

### Reuse

- immutable/hash-bound input packages;
- exact prompt/result-contract/input hashes;
- bounded deterministic batches;
- one result per batch;
- exactly one decision per discovered record;
- no missing/extra/duplicate decisions;
- content-addressed accepted result sets;
- acceptance revalidation before lifecycle progress.

### Generalize

Add common discovery provenance:

```text
BASE
CARRY_OVER
REFERENCE_EXPANSION
SUCCESSOR_EXPANSION
PARALLEL_EXPANSION
COMPETING_EXPANSION
BRIDGE_EXPANSION
GAP_FILL
```

Thematic records may form traceable parent/edge graphs. Weekly may use `BASE` and `CARRY_OVER` without inheriting Thematic completeness semantics.

Add profile-neutral Screening v2 decisions with fields conceptually:

```yaml
discovery_id:
decision: KEEP | MAYBE | DROP | INSPECT
reason:
scope_tags: []
duplicate_group:
verification_targets: []
confidence: low | medium | high
```

Core Screening must not require:
- Weekly `why_now`;
- fixed A–L topic lanes;
- Weekly issue-id regex monkey-patching for Special/Thematic operation.

### WU-006 exit criteria

1. Weekly and Thematic discovery records share provenance mechanics but can use different origins/relations.
2. Thematic successor/reference/parallel/competing/bridge/gap-fill records remain traceable to a parent/research reason where applicable.
3. Screening v2 has no required Weekly `why_now` or A–L lane vocabulary.
4. Every accepted discovery record receives exactly one Screening disposition; missing/extra/duplicate decisions fail closed.
5. Screening packages bind exact Profile/State/prompt/result-contract/input hashes.
6. Existing v1 Screening remains untouched for frozen/legacy replay.
7. Tests demonstrate an SP001-like expansion and a Weekly carry-over path without issue-regex monkey-patching.

## 7. Cross-cutting validation issue currently tracked

`Pipeline contract tests` had a pre-existing missing-`pytest` dependency on current `main`. The improvement branch fixes this in one isolated CI commit. Until its rerun is green, branch-wide CI should be reported as **rerun pending**, not as fully green.

This is a baseline CI quality issue, not a v2 semantic exception and not a Human Gate.

## 8. Resume rule

```text
read current main
-> read this worklog for status/next action
-> read docs/survey-production-core-v2-authority.md for semantic authority
-> verify repository reality
-> perform active WU + validation
-> update this ledger before declaring the WU complete
```

**Current action: implement and validate WU-006, while continuing to observe the repaired branch-wide CI rerun.**
