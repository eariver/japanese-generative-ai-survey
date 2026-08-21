# Survey Production Core v2 — Minimum Vertical Slice Audit Amendment

Status: `PHASE 3 CORRECTION / authoritative implementation amendment`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Base design: `docs/survey-production-core-v2-minimum-vertical-slice.md`  
Companions:
- `docs/survey-production-core-v2-component-inventory-audit-amendment.md`
- `docs/survey-production-core-v2-historical-production-pattern-matrix.md`
- `docs/survey-production-core-v2-w33-artifact-disposition.md`

## 1. Authority and reason for amendment

A pre-implementation audit found that the original minimum vertical slice correctly identified Weekly semantic pollution in Screening/Evidence/Selection, but did not carry that finding far enough through Architecture, Drafting and Issue Synthesis. It also omitted Pilot-critical thematic research expansion, machine-readable Pilot finding capture, state anti-divergence, and an executable liveness layer.

Where this document conflicts with the original minimum vertical slice, **this amendment controls** until the documents are consolidated after Pilot stabilization.

The target architecture itself is unchanged:

```text
Survey Production Core v2
  + Research / Editorial Profile
  + Publication Profile
  + optional Series Research Layer
```

The correction changes the implementation boundary, not the architectural direction.

## 2. Corrected Pilot objective

The first coherent candidate merged to `main` must let separate sessions demonstrate:

### W33

A real Weekly issue can enter v2 while preserving useful legacy factual/provenance work through explicit artifact-level revalidation, without inheriting legacy editorial/gate semantics.

### SP001

A real Thematic Special can reach Architecture Review through:
- open/current-as-of research scope;
- thematic research expansion beyond base collectors;
- profile-neutral Screening and factual Evidence;
- thematic materiality/completeness;
- generic Selection/Architecture contracts;
- no fabricated Weekly `why_now`, `late_breaking`, `this_week`, or rolling-window fields.

Both must use the same Core Human Gate/state/traceability mechanics.

## 3. Pilot-critical semantic path

The v2 candidate must cover the following path coherently:

```text
Production Profile / contract identity
        ↓
Research discovery / expansion
        ↓
Raw provenance
        ↓
Screening v2
        ↓
Factual Evidence
        ↓
Edition Evidence View
        ↓
Materiality Ledger
        ↓
Profile Completeness
        ↓
Candidate Matrix v2
        ↓
Internal Selection v2
        ↓
Architecture v2
        ↓
Architecture Review Summary
        ↓
HUMAN GATE 1 — Architecture Review
        ↓
Draft Packages v2 / Draft Results v2
        ↓
Profile Synthesis
        ↓
semantic/publication validation
        ↓
Publication candidate / PDF / preflight
        ↓
HUMAN GATE 2 — Publication Preview
        ↓
Visual Review record / Freeze / Merge / Release
```

First Pilot validation may stop at Architecture Review in the external production sessions initially, but the implementation plan must not create a semantic dead end that later forces Thematic production back into Weekly-shaped Draft/Synthesis contracts.

## 4. Foundation Profile and Production State

The original profile/state direction remains valid with a stricter compatibility rule.

### 4.1 Authoritative v2 state

For a v2-initialized edition:

```text
sources/<issue-id>/production-state.json
```

is the **only authoritative lifecycle/gate state**.

It binds:
- Production Profile SHA;
- pipeline/quality/profile/publication contract identity;
- lifecycle state;
- Human Gate state;
- requested target gate;
- next action / terminal reason;
- artifact/checkpoint provenance;
- Exception Gate state.

### 4.2 Legacy state compatibility is one-way and preferably ephemeral

Some proven v1 primitives currently expect `pipeline-state.json`. The preferred adapter is:

```text
production-state.json
     ↓ deterministic projection
scratch/staging compatibility pipeline-state.json
     ↓ legacy primitive
result artifact
     ↓ v2 validator bound to original production-state/profile/contract SHAs
v2 state transition
```

Rules:

1. `pipeline-state.json` generated for compatibility is **not** authoritative.
2. Legacy code may not directly advance canonical `production-state.json`.
3. Mutations made by a legacy primitive to its compatibility state are discarded unless represented as an independently validated result/artifact and applied through the v2 transition API.
4. If a persistent compatibility state ever has to be committed, it must contain/associate an exact `generated_from` v2-state SHA and validation must fail on divergence. Ephemeral compatibility projection is preferred because legacy schemas may not allow new metadata fields.
5. A v2 state transition must verify that the profile/contract/state basis has not changed since the action was planned.

This prevents silent dual-authority drift.

## 5. Research Discovery / Expansion contract

The original vertical slice under-specified this stage. SP001 requires a first-class research-expansion mechanism.

### 5.1 Generic discovery graph

The Core records discovered source nodes and why each entered the research corpus. Example origin/edge vocabulary:

- `BASE_COLLECTOR`
- `SEED`
- `BACKWARD_REFERENCE`
- `FORWARD_CITATION`
- `SUCCESSOR`
- `PARALLEL_APPROACH`
- `COMPETING_APPROACH`
- `BRIDGE_SOURCE`
- `COUNTEREXAMPLE`
- `SUPPLEMENTAL_GAP_FILL`
- `CARRY_OVER` (Weekly profile use)

The exact enum may be refined, but every non-base discovery must retain:
- parent/trigger source or completeness obligation;
- discovery method/query/reference;
- retrieval provenance;
- accepted Raw identity;
- downstream Screening disposition.

### 5.2 Thematic Research Expansion

Thematic Profile supplies research-question obligations and expansion policy. A generic iteration is:

```text
initial seeds + base discovery
  -> identify canonical/original sources
  -> backward-reference expansion
  -> forward/successor expansion
  -> parallel/competing branch search
  -> bridge/counterexample search where material
  -> update branch/transition completeness obligations
  -> targeted gap fill
  -> repeat until obligations are SATISFIED, explicit LIMITATION, or NEEDS_RESEARCH
```

No fixed citation depth or minimum source count proves completeness. Stop condition is Profile Completeness closure, not “N sources collected”.

### 5.3 SP001-specific data, not code

SP001 may define dimensions such as model families/ecosystems, reasoning/coding/agent/runtime/deployment/open-weight branches and major transitions. Those obligations live in the Production Profile/completeness data.

The implementation must not contain `if SP001` or topic-named production scripts.

### 5.4 Weekly discovery

Weekly still uses rolling collectors, carry-over and current-trend inputs. It may use reference expansion for a specific technical development, but it is not required to perform open-ended lineage traversal for every current item.

Research expansion is therefore a Core mechanism invoked according to Profile policy.

## 6. Screening v2

Retain the original corrected direction:
- one explicit decision per accepted discovery;
- `KEEP | MAYBE | DROP | INSPECT`;
- reason;
- generic scope tags;
- duplicate linkage;
- verification targets;
- confidence;
- exact prompt/input SHA binding.

Core Screening does not require:
- `why_now`;
- A–L topic lane constants;
- rolling-window classification.

Weekly relevance is produced later in Edition Evidence View/Profile annotations.

## 7. Factual Evidence + Edition Evidence View

### 7.1 Factual Evidence

The v2 Evidence contract retains the mature primitives:
- source references;
- objective events;
- claims with attribution class;
- metrics;
- limitations;
- exact task/prompt/source binding;
- unknowns remain unknown;
- stable IDs.

It must not require Weekly editorial recommendation or `why_now_confirmed` as factual truth.

### 7.2 Subject/entity binding

A concrete technical attribute must carry enough structure to identify:
- subject entity/artifact;
- value/attribute;
- source support;
- comparator/related entity where applicable.

Comparator values must not become target attributes by source-page proximity. Historical Mistral/Jamba/Ministral failures become P0 regression fixtures.

### 7.3 Edition Evidence View

This owns edition-specific interpretation:
- materiality status/rationale;
- scope dimensions;
- profile annotations.

Weekly examples:
- why this issue;
- window/carry-over relation;
- late-breaking/watchlist suitability.

Thematic examples:
- Core/Bridge/Context/Parallel/Competing/Counterexample lineage role;
- branch/transition IDs;
- inheritance/abandonment hypothesis;
- historical-attribution caveat.

Reusable factual Evidence and edition-specific significance remain distinct authorities.

## 8. Materiality Ledger and Profile Completeness

Original design remains, with discovery expansion integrated.

Materiality Ledger rows must record intake origin/edge and downstream disposition. Any source discovered through backward/forward/parallel/competing/gap-fill research has the same no-silent-drop obligation as base collector input.

Profile Completeness is evaluated against:
- profile-defined initial obligations;
- obligations discovered during research expansion;
- residual limitations.

Architecture Review is not ready while a required obligation remains `NEEDS_RESEARCH` unless a genuine Exception Gate records an explicit editorial decision.

## 9. Candidate Matrix and internal Selection v2

The common Matrix is evidence/materiality/comparison data, not a Weekly timing table.

Weekly Profile may append:
- current window relation;
- carry-over relation;
- why-this-issue relevance.

Thematic Profile may append:
- lineage branch/transition;
- parallel/competing relation;
- unresolved historical significance.

Selection remains an internal SHA-bound editorial checkpoint. Human approval fields are removed from the generic selection record. Publication roles are validated by the Profile/Publication contract rather than one global Weekly enum.

## 10. Architecture v2

The original vertical slice did not explicitly replace the Weekly-shaped Architecture schema. The corrected candidate must.

### 10.1 Generic Architecture envelope

Common fields include:
- issue/profile identity;
- exact basis hashes: Profile, Completeness, Materiality, Matrix, Selection;
- editorial thesis;
- architecture goals;
- package list;
- primary/supporting Evidence assignments;
- must-cover requirements;
- boundaries;
- drafting order;
- Profile/Publication extensions;
- proposed/approved status and Human Architecture approval reference.

### 10.2 No universal Weekly package vocabulary

Core does not require:
- `LATE_BREAKING`;
- `X_COMMUNITY`;
- `WATCHLIST_CHRONOLOGY`;
- `this_week_summary_written_last`.

Weekly Profile/Publication Profile may define these roles/extensions.

Thematic Profile may define long-form chapter/research roles without pretending they are Weekly packages.

### 10.3 Architecture Review Summary

The Human Gate surface binds exact hashes and exposes:
- source counts by discovery origin;
- expansion graph/coverage summary where relevant;
- Screening dispositions;
- Evidence/materiality counts;
- holds/exclusions;
- Selection assignments;
- completeness obligations/status;
- major material discoveries and destinations;
- residual limitations;
- proposed thesis/packages/page planning.

This is the v2 solution to Issue #166’s “how did wide research compress into this architecture?” review problem.

## 11. Draft Package / Draft Result v2

The audit found that current Draft contracts still contain Weekly semantics. Pilot implementation must establish a clean boundary before publication validation.

### 11.1 Generic Draft Package

Retain:
- exact Architecture/Evidence basis hashes;
- package title/type supplied by approved Architecture;
- primary/supporting factual Evidence;
- must-cover/boundary constraints;
- language;
- raw sources forbidden;
- unknowns remain unknown;
- citation granularity;
- drafting order.

Do not require generic fields named:
- `late_breaking`;
- `this_week_summary_forbidden`.

Weekly Profile may supply an extension requiring a Late Breaking note or prohibiting issue-level synthesis during article drafting.

### 11.2 Draft Result

Retain:
- headline/deck/blocks;
- evidence refs;
- attribution modes;
- must-cover/boundary coverage;
- exact Draft Package/prompt binding.

A generic draft result does not require `late_breaking_acknowledged`. Weekly extension validation may require it only for a Weekly Late Breaking package.

### 11.3 Generic vs extension validation

Validation layers:

```text
Core Draft Validator
  - exact basis
  - evidence reference validity
  - attribution correctness
  - requirement coverage
  - architecture-included Evidence use
  - identifier/subject correctness hooks

Profile Draft Validator
  - Weekly Late Breaking / Watchlist semantics
  - Period synthesis/chronology requirements
  - Thematic historical-attribution/lineage boundaries

Publication Validator
  - reader/internal prose separation
  - layout/render rules later
```

## 12. Profile Synthesis v2

Current shared Synthesis contract is Weekly-shaped because `this_week_signals` is mandatory.

v2 introduces:

```text
Synthesis Envelope
  - issue/profile identity
  - exact input/prompt/runner provenance
  - cover/frontmatter data where Publication Profile requests it
  - profile_payload
```

Profile payload examples:

### Weekly
- This Week signals;
- late-breaking/current interpretation;
- carry-over-facing summary.

### Monthly Period
- issue-level retrospective synthesis;
- cross-feature relationships and unresolved boundaries.

### Half-year
- cross-month comparison;
- half-year reclassification;
- cross-layer synthesis;
- half-year synthesis.

### Annual
- Story units;
- Annual trajectories;
- Annual thesis/phase synthesis.

### Thematic
- branch/transition synthesis;
- competing/parallel approach relation;
- unresolved lineage questions;
- historical-attribution boundaries.

No Profile is forced to emit `this_week_signals` as dummy data.

## 13. W33 artifact compatibility

`docs/survey-production-core-v2-w33-artifact-disposition.md` is normative for the Pilot.

Summary:
- collector Raw/provenance → `REVALIDATE`;
- carry-over/current-context Raw → `REVALIDATE`;
- v1 Screening → `REGENERATE`;
- Evidence factual subset → `REVALIDATE`, Edition View regenerated;
- Matrix/Selection → `REGENERATE`;
- Architecture → `REGENERATE`;
- Draft/Synthesis/claim review → `REGENERATE` as canonical v2 artifacts;
- legacy TeX/PDF/Visual Review → comparison fixture, not v2 release authority;
- legacy state → immutable fixture, not v2 authority.

This intentionally tests compatibility boundaries without creating a universal state migrator.

## 14. Machine-readable Review Finding and Repair Set

The first external Pilots must not recreate an ad hoc `revise_*_v35` process.

### 14.1 Finding schema

Add a machine-readable schema roughly covering:

```yaml
finding_id:
edition:
stage:
observed_problem:
expected_behavior:
actual_behavior:
production_workaround:
classification:
  scope: EDITION_LOCAL | WEEKLY_PROFILE | PERIOD_PROFILE | THEMATIC_PROFILE | CORE | PUBLICATION_PROFILE | QUALITY_CONTRACT | SERIES_LAYER | UNCLASSIFIED
  confidence:
provenance:
  source_commit:
  relevant_artifacts: []
  human_review_reference:
improvement_action:
regression_fixture:
status: OPEN | CLASSIFIED | FIXED_LOCAL | FIXED_GENERIC | DEFERRED | CLOSED
```

### 14.2 Repair Set schema

A Repair Set groups one or more findings into a proposed coherent change:
- affected contract/component;
- findings addressed;
- generic vs profile/local classification;
- implementation commits;
- required regression fixtures;
- compatibility impact;
- validation results;
- Pilot edition(s) that must verify the fix.

Rule:

> A production workaround is evidence about a defect, not automatic authorization to promote the workaround into Core.

## 15. Executable `advance-to-gate`

A planner alone is not sufficient liveness.

### 15.1 Planner

Reads:
- Production State/Profile;
- artifact validity;
- target Human Gate;
- contract identity.

Returns an Action Spec:

```yaml
action_id:
current_stage:
action_kind: LOCAL_SCRIPT | WORKFLOW_DISPATCH | HUMAN_GATE | COMPLETE | EXCEPTION
handler:
required_inputs: []
expected_outputs: []
basis_hashes: {}
retry_policy:
next_terminal_reason:
```

### 15.2 Executor / dispatcher

A registered dispatcher executes deterministic Action Specs:
- local script handler;
- GitHub workflow dispatch/control handler;
- artifact import/validation handler where necessary.

After each action it:
1. verifies expected outputs/basis;
2. transitions v2 state through one authoritative API;
3. records action/result provenance;
4. replans;
5. continues until terminal.

Normal terminals:
- `HUMAN_GATE_REACHED`;
- `EXCEPTION_GATE_REQUIRED`;
- `COMPLETE`.

A recoverable collector/CI/build failure is retried or repaired under configured policy and does not automatically become a user interaction gate.

The first candidate need not replace every YAML workflow, but it must be able to *execute* the registered existing wrappers rather than merely tell a chat session which one to run next.

## 16. Revised implementation work units

The original WU-005–010 sequence is superseded by the following reviewable sequence.

### WU-005 — Foundation contracts, state and anti-divergence

Implement:
- `config/survey-production-v2.json`;
- Production Profile schema/resolver;
- Production State schema/transition API;
- temporal policies;
- contract SHA binding;
- ephemeral/one-way legacy state projection;
- divergence tests;
- W33/SP001 initialization fixtures.

Exit:
- W33 and synthetic Thematic profile initialize under one Core;
- Thematic requires no fake bounded window;
- no legacy state can silently become v2 authority.

### WU-006 — Research discovery expansion + Screening v2

Implement:
- common discovery-origin/edge provenance;
- Thematic seed/reference/successor/parallel/competing/bridge/gap-fill expansion interface;
- Weekly discovery/carry-over hooks;
- Screening v2 schema/prompt/package/acceptance;
- tests for one decision per discovered record and no regex monkey-patching.

Exit:
- SP001-like thematic research can expand beyond base collectors with traceable reasons;
- Weekly and Thematic share mechanics without sharing completeness semantics.

### WU-007 — Factual Evidence, Edition View, Materiality, Completeness

Implement:
- profile-neutral Evidence v2 or bounded adapter path;
- subject/entity-bound facts;
- Edition Evidence View;
- Materiality Ledger;
- Profile Completeness Result;
- Weekly/Thematic validators;
- Issue #166 and #191 P0 regressions.

Exit:
- silent material drop is mechanically blocked across covered stages;
- profile significance is not stored as universal factual Evidence.

### WU-008 — Candidate Matrix, internal Selection, Architecture, W33 disposition support

Implement:
- profile-aware matrix;
- generic internal Selection;
- generic Architecture envelope;
- Profile/Publication extensions;
- Architecture Review Summary/readiness validator;
- W33 artifact disposition/import/revalidation records where needed.

Exit:
- W33 and SP001 can reach the same Human Gate 1 using different profile semantics;
- legacy W33 semantic artifacts are not silently inherited.

### WU-009 — Drafting and Synthesis semantic generalization

Implement:
- generic Draft Package/Draft Result contracts;
- generic Draft validator + Profile validators;
- Weekly extension for Late Breaking/Watchlist;
- profile Synthesis envelope + Weekly/Period/Thematic payload validators;
- reader/internal prose boundary;
- identifier preservation integration.

Exit:
- both Weekly and Thematic have a valid post-Architecture semantic path without dummy Weekly fields.

### WU-010 — Executable orchestration + Pilot findings/Repair Sets

Implement:
- planner;
- deterministic Action Spec;
- executor/dispatcher registry;
- authoritative state transition/logging;
- target gate/terminal behavior;
- Finding schema/validator;
- Repair Set schema/validator;
- Pilot handoff tooling.

Exit:
- a separate session can advance a configured issue to its requested Human Gate from repository state without reconstructing stage order from chat;
- Pilot findings return in a reusable structured form.

### WU-011 — P0 quality integration and Pilot bootstrap

Implement/verify:
- identifier preservation;
- subject/entity binding;
- reader/internal separation;
- exact-byte Publication Preview/Freeze/Release integration;
- frozen historical immutability;
- regression suite including coupled repairs;
- W33/SP001 startup docs;
- assistant-control/workflow allowlist updates only for settled canonical entrypoints.

Exit:
- candidate is review/merge-ready for external W33/SP001 production validation.

## 17. Pilot acceptance criteria — corrected

### W33

Must demonstrate:
- correct Weekly rolling window/carry-over semantics;
- explicit legacy artifact disposition;
- verified factual/provenance reuse where safe;
- regeneration of legacy semantic artifacts where contracts changed;
- broad/current intake + explicit completeness status;
- no silent material drop;
- internal Selection, not a standalone Human Gate;
- Architecture Review Summary exposes compression/limitations;
- no generic automatic migration requirement was introduced solely for W33.

### SP001

Must demonstrate:
- no fake bounded historical coverage;
- explicit research question/inclusion/exclusion;
- thematic research expansion with source-origin graph;
- backward/forward/successor/parallel/competing/bridge/gap-fill research as materially required;
- completeness closure by obligations, not source count;
- materiality based on thematic significance, not Weekly `why_now`;
- common factual Evidence/Selection/Architecture traceability;
- no dummy Weekly fields in Architecture/Draft/Synthesis path;
- same Human Gate mechanics as W33.

### Both

Before external Pilot starts:
- Finding/Repair Set contract exists;
- executable advance-to-gate exists for required deterministic stages;
- contract/profile/state hashes are recorded;
- frozen historical artifacts are unchanged.

## 18. Deferred work remains deferred

The correction does not turn Pilot 1 into a complete rewrite. Still deferred unless Pilot findings promote them:
- removal of every v1 workflow wrapper;
- deletion/archive of all historical repair scripts;
- full Series Research Layer/shared corpus implementation;
- perfect migration of arbitrary active v1 editions;
- total unification of Weekly/long-form TeX templates;
- cleanup of every P1 historical layout invariant.

The difference is that no deferred item may be required to fake a valid W33/SP001 semantic path.

## 19. Corrected WU-004 exit decision

WU-004 may close only when all of the following are recorded:

- Phase 0 amendment maps profile pollution through Synthesis;
- Phase 2B covers all 15 completed Specials with positive and negative patterns;
- W33 has explicit artifact-level disposition;
- Thematic Research Expansion is a Pilot-critical component;
- Architecture/Draft/Synthesis v2 boundaries are explicit;
- state anti-divergence is explicit;
- Review Finding/Repair Set is scheduled before Pilot;
- `advance-to-gate` includes executable dispatch/control;
- revised implementation WUs have concrete exits;
- no design relies on automatic legacy migration or dummy Weekly fields.

With this amendment committed and cross-checked against the companion correction artifacts, the next implementation unit is **WU-005 — Foundation contracts, state and anti-divergence**.
