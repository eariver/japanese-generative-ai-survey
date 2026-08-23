# Survey Production Core v2 — Post-Merge Production Feedback Backlog

Status: `REDESIGN INTEGRATED / CLEAN REVALIDATION EXPOSED OPERATOR-RUNTIME GAP / PFB-014 MAINTENANCE IN PROGRESS`  
Established: 2026-08-23 JST  
Initial review closed: 2026-08-23 JST  
Last updated: 2026-08-23 JST

Current maintenance branch: `maintenance/core-v2-operator-execution-bridge`

## Current authority

The initial W33/SP001 production feedback drove the Core v2 redesign that was reviewed and integrated. Subsequent clean post-merge W33/SP001 revalidation exposed one additional dependency: the normal ChatGPT connector runtime can research/edit the repository but cannot necessarily mount the exact work branch and execute the canonical local Core CLI.

Cross-edition revalidation: `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`  
Operator-bridge design: `docs/survey-production-core-v2-operator-execution-bridge.md`

PFB-001 through PFB-013 remain applicable. PFB-014 is the new post-integration finding.

## PFB-001 — one self-contained Grok task file in Google Drive

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

Use one run-specific Markdown task file. Repository provenance hash-binds exact task/result bytes.

## PFB-002 — Human passes the exact Drive task-file path; do not search for a Grok connector

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

PFB-014 follows this rule: W33/SP001 were paused and bridge work moved to separate Core maintenance.

## PFB-006 — reduce Actions from production author to narrow deterministic infrastructure

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT / PFB-014 NARROW FALLBACK UNDER REVIEW`

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.**

PFB-014 does not reverse the redesign. The operator bridge is admissible only as a constrained deterministic execution substrate because the connector runtime lacks an exact checked-out CLI environment.

If accepted, current Actions surface is seven workflows. The prior six-workflow audit is historical only.

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

Candidate readiness requires deterministic QA + ChatGPT semantic/editorial QA + exact-PDF visual QA. The bridge owns none of the agent/Human judgments.

## PFB-011 — atomic publication revision/candidate authority

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Reader Manuscript, exact source/PDF, deterministic QA, semantic/editorial review and visual review bind atomically. Source/PDF revision invalidates downstream authority.

## PFB-012 — standardized edition-local execution records

Status: `IMPLEMENTED / PFB-014 EXTENDS EXECUTION TRANSPORT`

Canonical execution tree may add:

```text
requests/
bridge-runs/
```

These are transport/provenance, not a second lifecycle state machine.

## PFB-013 — real cold-start profile trials required after Core repair

Status: `PARTIALLY EXERCISED / NOT PASSED`

Required acceptance remains:

- clean Weekly;
- clean Thematic/LONGFORM with SP001 regression;
- representative configured `RETROSPECTIVE_PERIOD`;
- Foundations-guided Thematic/Longform;
- structural monthly/half-year/annual compatibility through one generic period Profile.

The first post-merge attempts did real operator work but could not begin canonical lifecycle execution before bridge maintenance.

A maintenance fixed-head audit also found that the initial bridge did not expose the existing Retrospective initializer. The candidate was invalidated rather than weakening the cross-profile validation requirement.

PFB-013 remains open until reviewed integration and clean real-production validation.

## PFB-014 — deterministic Core execution fallback for connector-only runtimes

Status: `IMPLEMENTATION CANDIDATE / RETROSPECTIVE BRIDGE EXPOSURE REPAIRED / NOT VALIDATED`

### Observation

The integrated redesign assumes ChatGPT can invoke local deterministic Core scripts. In the normal connector runtime, ChatGPT can read/write exact repository content but cannot necessarily obtain a mounted checkout or run the canonical Core CLI on the exact work branch.

Manual creation of plausible Profile/State/checkpoint/acceptance artifacts is prohibited.

A later fixed-head audit established that the bridge also needed to expose Retrospective initialization for the required cross-profile matrix.

### Corrected Retrospective diagnosis

Deeper pre-freeze inspection established that Core **already contained** canonical generic Retrospective support on the maintenance base:

- `scripts/survey_period_v2.py`
- `tests/test_survey_period_v2.py`

That helper already resolves configured monthly/half-year/annual periods and builds `RETROSPECTIVE_PERIOD + LONGFORM_SPECIAL`, including bounded-period and resume safeguards.

Therefore the true maintenance defect is:

> **The operator bridge did not expose the existing `survey_period_v2` deterministic initializer.**

Temporary duplicate Retrospective adapter/schema/tests created under the earlier diagnosis were removed before final candidate freeze.

### Required behavior

```text
ChatGPT commits edition artifacts
-> ChatGPT commits one immutable request-only commit
-> runner checks out exact commit
-> runner proves protected Core/contract bytes equal reviewed main
-> runner executes only allowlisted canonical Core mechanics
-> runner commits only edition-local authorities/receipts
-> ChatGPT resumes from canonical State
```

Configured Retrospective bridge path is now simply:

```text
request special_slug
-> existing survey_period_v2.resolve_configured_period(...)
-> existing survey_period_v2.period_profile(...)
-> exact request/Profile identity check
-> canonical initialize(...)
```

There is no new Retrospective scope schema, no second Profile builder and no separate monthly/half-year/annual bridge engine.

### Current implementation candidate

Maintenance branch: `maintenance/core-v2-operator-execution-bridge`

Candidate-specific files include:

- `docs/survey-production-core-v2-operator-execution-bridge.md`
- `schemas/operator-execution-request-v2.schema.json`
- `scripts/survey_core_execution_bridge_v2.py`
- `.github/workflows/survey-production-v2-operator-bridge.yml`
- `tests/test_survey_core_execution_bridge_v2.py`
- synchronized config/authority/policy/worklog files.

Existing `scripts/survey_period_v2.py` and `tests/test_survey_period_v2.py` remain the canonical Retrospective Core implementation and are not duplicated by this PR.

Current allowlist:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`

Human Architecture approval, Publication Preview approval and Release are outside the bridge.

### Acceptance criteria

PFB-014 cannot close until:

1. no arbitrary executable surface from request data;
2. request path/id/branch/source-root exact and fail closed;
3. exact reviewed-main SHA on every operation and equality with initialization execution record;
4. protected shared Core/contract bytes match reviewed main before dependency installation/execution;
5. triggering commit adds exactly one immutable request and nothing else;
6. generated writes stay under Profile-bound source root;
7. immutable request bytes are not mutated;
8. `ADVANCE_STAGE` requires exact current lifecycle state;
9. deterministic `CORE_STAGE_CONTRACT` is generated by Core;
10. ChatGPT reviews cannot impersonate deterministic results;
11. bot output cannot recursively retrigger;
12. exact request/event/State provenance is recorded;
13. direct-local CLI remains preferred;
14. Retrospective request reuses existing `survey_period_v2`, rejects unknown/pre-period-end targets through existing Core semantics, and adds no cadence-specific engine;
15. bridge glue has an end-to-end init -> stage-advance regression;
16. exact-head CI + complete six-point fixed-head audit pass;
17. after reviewed unchanged integration, clean Weekly/SP001/Retrospective/Foundations trials reach required gates without in-run shared-Core repair.

### Classification

This began as `TRANSIENT_EXECUTION / OPERATOR-RUNTIME CAPABILITY`. Because the production model must work in the actual ChatGPT runtime used by this project, the missing execution fallback is treated as a **shared operator/Core integration maintenance requirement**.

Retrospective exposure is part of that same integration requirement, not a new Retrospective subsystem.

## Current next step

Do not resume canonical W33/SP001 acceptance on a pre-PFB-014 baseline.

```text
finish bridge documentation/implementation synchronization
-> exact-head Core CI + pipeline contract tests
-> freeze one exact maintenance candidate SHA
-> complete six-point audit from zero on unchanged SHA
-> Human full-candidate review
-> integrate unchanged accepted head
-> reset clean validation branches from reviewed main
-> execute Weekly / Thematic-SP001 / Retrospective / Foundations validation matrix
```

Any candidate-tree change after freeze invalidates the fixed-head audit.
