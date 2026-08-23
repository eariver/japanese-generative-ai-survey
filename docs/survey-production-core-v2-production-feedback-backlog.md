# Survey Production Core v2 — Post-Merge Production Feedback Backlog

Status: `REDESIGN INTEGRATED / PFB-014 HUMAN-GATE ROUNDTRIP IMPLEMENTATION CANDIDATE / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Initial review closed: 2026-08-23 JST  
Last updated: 2026-08-24 JST

Current maintenance branch: `maintenance/core-v2-operator-execution-bridge`

## Current authority

The initial W33/SP001 production feedback drove the Core v2 redesign that was reviewed and integrated. Subsequent clean post-merge W33/SP001 revalidation exposed an additional dependency: the normal ChatGPT connector runtime can research/edit the repository but cannot necessarily mount the exact work branch and execute the canonical local Core CLI.

A later pre-approval full-system audit found a second consequence of the same operator-runtime constraint: the first bridge could reach a normal Human Gate but could not canonically record an already explicit Human approval or ordinary requested-revision cycle. PFB-014 therefore now covers the complete connector-safe deterministic execution boundary, including Human Gate round trips.

Cross-edition revalidation: `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`  
Operator-bridge design: `docs/survey-production-core-v2-operator-execution-bridge.md`

PFB-001 through PFB-013 remain applicable. PFB-014 is the open post-integration maintenance finding.

## PFB-001 — one self-contained Grok task file in Google Drive

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

Use one run-specific Markdown task file. Repository provenance hash-binds exact task/result bytes.

## PFB-002 — Human passes exact Drive task-file path; do not search for a Grok connector

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

```text
ChatGPT prepares one self-contained task file
-> Human passes exact Drive path/reference to Grok
-> Grok reads/writes instructed result
-> ChatGPT imports/dispositions result and resumes
```

Absence of a Grok connector is not an Exception Gate.

## PFB-003 — concluding synthesis in every Weekly and Special

Status: `IMPLEMENTED`

Every reader-facing Weekly/Special requires substantive `総括` or equivalent. ChatGPT judges quality; deterministic checks only protect crisp structure.

## PFB-004 — Weekly always has explicit community movement informed by Grok/X

Status: `IMPLEMENTED / CLEAN W33 EDITORIAL VALUE CONFIRMED`

Every Weekly requires reader-facing `コミュニティの動き`; Grok/X remains Discovery/community-signal rather than final technical Evidence authority.

## PFB-005 — Production sessions repair editions, not shared Core

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

> **A Production session repairs the edition. It does not repair shared Core v2.**

PFB-014 follows this rule: W33/SP001 remain paused while shared bridge/Human-Gate work is repaired in Core maintenance.

## PFB-006 — reduce Actions from production author to narrow deterministic infrastructure

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT / PFB-014 NARROW FALLBACK UNDER REVIEW`

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, Human-decision, or publication-authoring agent.**

PFB-014 does not reverse the redesign. The operator bridge is admissible only as a constrained deterministic execution substrate because the connector runtime lacks an exact checked-out CLI environment. It may record an already explicit Human decision but may not choose one.

The current intended Actions surface remains exactly seven workflows. Earlier six-workflow/six-point evidence is historical only.

## PFB-007 — retain failed W33/SP001 trials as non-validating evidence

Status: `RESOLVED / HISTORICAL FAILED EVIDENCE PRESERVED`

Pre-redesign failures and first post-merge blocked attempts remain non-PASS evidence.

## PFB-008 — structural reader-facing Publication Boundary

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Internal editorial/provenance state is not legal fallback reader prose. Missing reader content fails closed to ChatGPT authoring. Known-token lint remains defense-in-depth.

## PFB-009 — Architecture fidelity means reader-facing content fulfillment

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

```text
requirement
-> accepted Evidence/Observation
-> actual reader-facing location
-> ChatGPT fulfillment judgment
```

## PFB-010 — separate deterministic QA from semantic/editorial and visual QA

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Candidate readiness requires deterministic QA + ChatGPT semantic/editorial QA + exact-PDF visual QA. The bridge owns none of these judgments.

## PFB-011 — atomic publication revision/candidate authority

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT / HUMAN-GATE REVISION PATH ADDED`

Reader Manuscript, exact source/PDF, deterministic QA, semantic/editorial review and visual review bind atomically. Source/PDF revision invalidates downstream authority. Publication Preview `REQUEST_CHANGES` now also resets affected Validation/Candidate authority before a new candidate can return to the gate.

## PFB-012 — standardized edition-local execution records

Status: `IMPLEMENTED / PFB-014 EXTENDS EXECUTION + HUMAN-REVIEW PROVENANCE`

Canonical execution tree may add `requests/` and `bridge-runs/` when bridge transport is used. Human-readable `execution/reviews/*-rN.md` points to exact machine Human-review authority under `{source_root}/gates/reviews/` and `gates/review-index.json`.

These are provenance layers, not second lifecycle state machines.

## PFB-013 — real cold-start profile trials required after Core repair

Status: `PARTIALLY EXERCISED / NOT PASSED`

Required post-integration acceptance remains:

- clean Weekly;
- clean Thematic/LONGFORM with SP001 regression;
- representative configured `RETROSPECTIVE_PERIOD`;
- Foundations-guided Thematic/Longform;
- structural monthly/half-year/annual compatibility through one generic period Profile.

The first post-merge attempts did real operator work but could not begin canonical lifecycle execution before bridge maintenance. PFB-013 remains open until reviewed integration and clean real-production validation.

## PFB-014 — deterministic Core execution fallback for connector-only runtimes

Status: `IMPLEMENTATION CANDIDATE / HUMAN-GATE ROUNDTRIP IMPLEMENTED / SEVEN-POINT REAUDIT PENDING`

### Observation

The integrated redesign assumes ChatGPT can invoke local deterministic Core scripts. In the normal connector runtime, ChatGPT can read/write exact repository content but cannot necessarily obtain a mounted checkout or run canonical Core CLI on the exact work branch.

Manual creation of plausible Profile/State/checkpoint/approval/review authority is prohibited.

The first bridge candidate addressed initialization and one-stage advancement but a pre-approval audit exposed two blocking continuation gaps:

- **HG-001:** connector-only operation could reach a Human Gate but could not canonically record the Human's explicit approval;
- **HG-002:** routine Human `REQUEST_CHANGES` had no canonical selective invalidation/revision path, so ordinary correction risked becoming an inappropriate Exception Gate or causing pinned checkpoint drift.

A later freeze-preparation audit also found a provenance precision defect: the bridge originally recorded the request/event commit as `reviewed_repository_commit_sha`, although the Human had actually reviewed the edition bytes in the request-only commit's parent. The candidate now requires an explicit Human-reviewed commit SHA and the workflow proves it equals the request parent before execution.

### Retrospective diagnosis

Core already contained canonical generic Retrospective support:

- `scripts/survey_period_v2.py`
- `tests/test_survey_period_v2.py`

The bridge therefore exposes that existing initializer; it does not create a second Retrospective builder, scope schema or monthly/half-year/annual engine.

### Current required behavior

```text
ChatGPT commits edition artifacts
-> Human reviews the exact current edition commit when a Human Gate is reached
-> ChatGPT commits one immutable request-only commit that names that reviewed parent SHA
-> runner checks out exact request commit
-> runner proves reviewed_repository_commit_sha == request-only commit parent
-> runner proves protected Core/contract bytes equal reviewed main
-> runner executes only allowlisted canonical deterministic mechanics
-> runner commits only edition-local authorities/receipts
-> ChatGPT resumes from canonical State
```

At a Human Gate:

```text
Human explicitly decides APPROVED
  or REQUEST_CHANGES + requested changes + regeneration boundary
-> ChatGPT encodes only that explicit decision/provenance in immutable request
-> bridge/Core validates exact pending gate/current bytes/revision
-> workflow binds Human-reviewed commit to request parent
-> Core records approval or immutable rN review record
-> APPROVED resumes lifecycle
   OR REQUEST_CHANGES selectively invalidates downstream authority
-> ChatGPT performs actual requested repair and revalidates to rN+1
```

Actions/Core never choose the Human decision, requested changes or regeneration boundary.

### Current implementation candidate

Maintenance branch: `maintenance/core-v2-operator-execution-bridge`

Key candidate files include:

- `docs/survey-production-core-v2-operator-execution-bridge.md`
- `docs/survey-production-core-v2-github-actions-policy.md`
- `docs/survey-production-core-v2-final-audit-rule.md`
- `schemas/operator-execution-request-v2.schema.json`
- `schemas/human-gate-review-record-v2.schema.json`
- `schemas/human-gate-review-index-v2.schema.json`
- `scripts/survey_core_execution_bridge_v2.py`
- `scripts/survey_human_gate_v2.py`
- `.github/workflows/survey-production-v2-operator-bridge.yml`
- `tests/test_survey_core_execution_bridge_v2.py`
- `tests/test_survey_core_execution_bridge_human_gate_v2.py`
- `tests/test_survey_human_gate_v2.py`
- synchronized config/authority/policy/worklog files.

Existing `scripts/survey_period_v2.py` and `tests/test_survey_period_v2.py` remain canonical Retrospective implementation and are not duplicated.

Current bridge allowlist is exactly eight request kinds:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

Release remains outside the bridge and owned by the dedicated release workflow.

### Human Gate machine authority

The canonical machine review history is:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

Each rN binds exact reviewed State/artifact SHA-256 values, the exact Human-reviewed repository commit, Human provenance, decision, and requested revision boundary where applicable. In connector-safe execution that reviewed commit is exactly the request-only commit parent; the bridge receipt separately retains the request/event commit. Prior reviewed bytes remain reconstructable; current Production State/checkpoint/gate provenance determines current authority.

### Regression evidence implemented before final freeze

The candidate now includes positive/negative direct and bridge-backed Human Gate coverage:

- Architecture r1 `REQUEST_CHANGES` -> selective invalidation -> r2 -> approval;
- stale r1 approval after r2 refusal;
- changed reviewed Architecture bytes refusal;
- Publication Preview r1 `REQUEST_CHANGES` -> Validation/Candidate regeneration -> r2 -> approval;
- invalid cross-gate regeneration boundary refusal;
- current r2 approval binds current Candidate/PDF;
- generic Human-decision/rejection operation surface absent;
- request/event SHA and Human-reviewed commit SHA are intentionally distinct in bridge E2E and remain distinct in the review record/receipt;
- workflow refuses a Human Gate request unless its reviewed commit is the exact request-only parent;
- request-only bridge transport, reviewed-main preflight, bot-recursion protection and no arbitrary execution remain protected.

These are candidate regressions, not substitutes for post-integration real-production validation.

### Acceptance criteria

PFB-014 cannot close until all conditions below hold:

1. no arbitrary executable surface from request data;
2. request path/id/branch/source-root exact and fail closed;
3. exact reviewed-main SHA on every operation and initialization execution-record equality;
4. protected shared Core/contract bytes match reviewed main before dependency installation/execution;
5. triggering commit adds exactly one immutable request and nothing else;
6. generated writes stay under Profile-bound source root;
7. immutable request bytes are not mutated;
8. `ADVANCE_STAGE` requires exact current lifecycle state;
9. deterministic `CORE_STAGE_CONTRACT` is generated by Core;
10. ChatGPT reviews cannot impersonate deterministic results;
11. bot output cannot recursively retrigger;
12. exact request/event/State provenance is recorded, and Human Gate provenance separately binds the exact reviewed parent commit rather than conflating it with the request/event commit;
13. direct-local CLI remains preferred;
14. Retrospective request reuses existing `survey_period_v2`, rejects unknown/pre-period-end targets through existing Core semantics, and adds no cadence-specific engine;
15. bridge glue has init -> stage-advance E2E coverage;
16. HG-001: explicit Architecture and Publication Preview approval can be canonically recorded from connector-only operation without Actions/Core making the decision;
17. HG-002: both normal gates support explicit `REQUEST_CHANGES`, contiguous rN history, allowed selective invalidation and return to the same gate;
18. stale review revision, changed reviewed bytes, invalid regeneration boundaries and reviewed-parent mismatch fail closed;
19. prior review revisions remain reconstructable while only current State/gate/checkpoint authority is active;
20. direct canonical and bridge-backed Human Gate round-trip regressions pass;
21. exact-head Core CI + Pipeline contract tests pass on the final unchanged candidate;
22. complete **seven-point** fixed-head audit, including Point 7 Human Gate round-trip viability, passes from Point 1 on one unchanged candidate SHA;
23. after reviewed unchanged integration, clean Weekly/SP001/Retrospective/Foundations trials reach required gates without in-run shared-Core repair.

### Classification

The missing execution fallback began as `TRANSIENT_EXECUTION / OPERATOR-RUNTIME CAPABILITY`. Because the production model must work in the actual ChatGPT runtime used by this project, it is a **shared operator/Core integration maintenance requirement**.

Retrospective exposure and Human Gate deterministic recording/revision are parts of that same integration boundary, not new editorial subsystems.

## Current next step

Do not resume canonical W33/SP001 acceptance on a pre-PFB-014 baseline.

```text
finish authority/worklog synchronization and pre-freeze consistency audit
-> resolve any remaining shared-Core consistency finding
-> freeze one exact maintenance candidate SHA
-> exact-head Core CI + Pipeline contract tests
-> complete seven-point audit from Point 1 on unchanged SHA
-> Human full-candidate review
-> integrate unchanged accepted head
-> reset clean validation branches from reviewed main
-> execute Weekly / Thematic-SP001 / Retrospective / Foundations validation matrix
```

Any candidate-tree change after freeze invalidates all seven fixed-head audit verdicts.
