# Survey Production Core v2 — Post-Merge Production Feedback Backlog

Status: `REDESIGN INTEGRATED / CLEAN REVALIDATION EXPOSED OPERATOR-RUNTIME GAP / PFB-014 MAINTENANCE IN PROGRESS`  
Established: 2026-08-23 JST  
Initial review closed: 2026-08-23 JST  
Last updated: 2026-08-23 JST

Current maintenance branch for the new finding:

`maintenance/core-v2-operator-execution-bridge`

## Current authority

The initial W33/SP001 production feedback drove the Core v2 redesign that was reviewed and integrated. Subsequent clean post-merge W33/SP001 revalidation then exposed one additional operational dependency: the normal ChatGPT connector runtime can research and edit the repository but cannot necessarily mount the exact work branch and execute the canonical local Core CLI.

The cross-edition revalidation record is:

`docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`

The operator-bridge maintenance design is:

`docs/survey-production-core-v2-operator-execution-bridge.md`

The original feedback items PFB-001 through PFB-013 remain applicable. PFB-014 is the new post-integration finding.

## Feedback item PFB-001 — Use one self-contained Grok task file in Google Drive

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

Use one run-specific Markdown file in Google Drive containing the complete Grok/X task: role, scope, research questions, evidence boundary, output format, and result destination.

Operational shape:

```text
Grok_X_SourseIntake/
  <category>/<edition>/<run-id>/
    grok-task.md
    <result>.md
```

Repository provenance hash-binds the exact task bytes and imported result bytes.

The clean W33 revalidation successfully exercised this exact Human-mediated boundary.

## Feedback item PFB-002 — Human passes the exact Drive task-file path to Grok; do not search for a Grok connector

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

Normal boundary:

```text
ChatGPT prepares one self-contained task file in Drive
-> ChatGPT gives Human the exact Drive file path/reference
-> Human gives that file path/reference to Grok
-> Grok reads it and writes the instructed result
-> ChatGPT imports/dispositions the result and resumes automatically
```

Absence of a Grok connector is not an Exception Gate or dependency failure.

## Feedback item PFB-003 — Require a concluding synthesis in every Weekly and Special

Status: `IMPLEMENTED`

Every reader-facing Weekly and Special requires a final substantive `総括` or explicitly equivalent section before non-editorial back matter. ChatGPT judges synthesis quality; deterministic checks may verify only reliable structural presence/order.

## Feedback item PFB-004 — Weekly must always publish an explicit community-movement view informed by Grok/X

Status: `IMPLEMENTED / CLEAN W33 EDITORIAL VALUE CONFIRMED`

Every Weekly requires a reader-facing `コミュニティの動き` component. The completed Grok/X result receives editorial disposition, not merely technical import/disposition. Material observations are reflected in the issue or carry an internal exclusion reason; a quiet week is an explicit reader-facing finding rather than silent omission.

Grok/X remains Discovery/community-signal authority, not final technical Evidence authority.

The clean W33 trial additionally confirmed that fresh X signal can materially change Weekly package selection and synthesis after primary-source verification.

## Feedback item PFB-005 — Production sessions repair editions, not shared Core v2

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

> **A Production session repairs the edition. It does not repair shared Core v2.**

A shared Core defect or operator/Core infrastructure gap is recorded and returned to Core maintenance. If there is no semantically safe edition-local workaround, the acceptance production attempt remains failed/non-validating and is later restarted from the appropriate clean boundary after reviewed Core repair.

The current PFB-014 work follows this rule: W33/SP001 were paused, and the execution bridge is being implemented on a separate shared-Core maintenance branch.

## Feedback item PFB-006 — Reduce GitHub Actions from production author to narrow deterministic infrastructure

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT / PFB-014 NARROW FALLBACK UNDER REVIEW`

The governing principle remains:

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.**

The integrated redesign reduced the normal Actions surface to contract/Core CI, reproducible Weekly/Special builds, exact-byte Publication Preview transport, and release.

PFB-014 does **not** reverse that direction. The proposed operator bridge is admissible only as a narrowly scoped deterministic execution substrate because the normal ChatGPT connector runtime lacks an exact checked-out CLI environment. The bridge must not perform research, Evidence/Selection/Architecture authorship, drafting, semantic/visual judgment, layout repair, Human approval, or arbitrary request-driven command execution.

If PFB-014 is reviewed and integrated, the Actions surface gains one additional constrained operator-bridge workflow. That change requires a fresh exact-head audit; the prior six-workflow audit cannot be reused as current evidence.

## Feedback item PFB-007 — Retain failed W33/SP001 trials as non-validating evidence

Status: `RESOLVED / HISTORICAL FAILED EVIDENCE PRESERVED`

The pre-redesign W33/SP001 runs and SP001 salvage revision remain useful failure evidence but not cold-start validation. Archived failed branches must not be copied into later clean accepted State.

The first post-merge clean attempts also remain non-PASS because canonical lifecycle execution could not begin before PFB-014 maintenance.

## Feedback item PFB-008 — Make the reader-facing Publication Boundary structural, not stylistic

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Implemented direction:

- explicit internal editorial/provenance layer;
- explicit Reader Manuscript / reader-facing publication layer;
- internal fields are not legal fallback render inputs;
- no fallback from missing reader-facing fields to Architecture/Profile/Evidence text;
- missing required publication content fails closed back to ChatGPT authoring.

Known-token lint remains defense-in-depth only.

## Feedback item PFB-009 — Architecture fidelity means reader-facing content fulfillment

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

The Reader Manuscript and semantic/editorial review retain lightweight traceability:

```text
requirement
-> accepted Evidence/Observation
-> actual reader-facing section/block
-> ChatGPT fulfillment judgment
```

Page quotas or string-presence checks do not substitute for editorial fulfillment judgment.

## Feedback item PFB-010 — Separate deterministic QA from semantic/editorial and visual QA

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Candidate readiness requires separate evidence for:

1. deterministic QA;
2. ChatGPT semantic/editorial QA;
3. ChatGPT exact-PDF visual QA.

The operator bridge belongs only to deterministic Core mechanics. It cannot manufacture AGENT_SEMANTIC/AGENT_EDITORIAL/AGENT_VISUAL judgments or Human decisions.

## Feedback item PFB-011 — Publication revision/candidate authority must be atomic

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Reader Manuscript, exact source, exact repository-resident PDF, deterministic QA, semantic/editorial review and visual review bind atomically into one Publication Candidate. Source/PDF revision invalidates downstream Candidate/Preview/Freeze identity.

## Feedback item PFB-012 — Standardize edition-local execution records

Status: `IMPLEMENTED / PFB-014 EXTENDS EXECUTION TRANSPORT`

Canonical location remains:

```text
sources/<issue-id>/execution/
  index.md
  sessions/
  reviews/
  defects/
```

PFB-014 adds transport/provenance subpaths for immutable deterministic execution requests and receipts:

```text
  requests/
  bridge-runs/
```

These additions are execution provenance, not a second lifecycle state machine.

## Feedback item PFB-013 — Real cold-start profile trials are required after Core repair

Status: `PARTIALLY EXERCISED / NOT PASSED`

Required acceptance remains:

- one clean Weekly trial with no in-run shared-Core repair;
- one clean LONGFORM_SPECIAL/SP001 regression trial with no in-run shared-Core repair;
- one representative configured `RETROSPECTIVE_PERIOD` trial with no in-run shared-Core repair;
- one Foundations-guided Thematic/Longform scenario through at least Architecture Review;
- structural confirmation that monthly, half-year and annual Retrospective guidance use one generic period Profile rather than separate engines.

The first post-merge clean attempts performed substantial real operator work, and W33 successfully exercised the actual Grok/Drive handoff. They did not reach canonical Profile/State lifecycle execution because the operator runtime lacked an execution bridge.

The first PFB-014 fixed-head audit also exposed a second execution-coverage gap: the bridge could cold-start Weekly and Thematic work but not the required Retrospective validation matrix. That candidate was invalidated rather than treating structural Profile support as executable production support.

Therefore PFB-013 remains open until reviewed Core integration and clean validation.

## Feedback item PFB-014 — Provide a generic deterministic Core execution fallback for connector-only operator runtimes

Status: `IMPLEMENTATION CANDIDATE / RETROSPECTIVE GAP REPAIRED / NOT VALIDATED`

### Observation

The integrated redesign assumes ChatGPT can invoke local deterministic Core scripts. In the normal connector runtime used for clean W33/SP001 revalidation, ChatGPT can read/write exact repository content through GitHub but cannot necessarily obtain a mounted checkout or execute the canonical Core CLI on the exact work branch.

Manual creation of plausible `production-profile.json`, `production-state.json`, checkpoint or acceptance artifacts is prohibited because it bypasses the validators being tested.

A later fixed-head audit showed that a fallback which initialized only Weekly/Thematic work was also insufficient: the mandated post-integration matrix includes Retrospective Period production, and connector-only execution had no canonical cold-start path for that Profile.

### Required behavior

When direct local CLI execution is unavailable, Core may provide a generic fallback that:

```text
ChatGPT commits already-authored edition artifacts / required scope materialization
-> ChatGPT commits one immutable request-only commit
-> deterministic remote runner checks out that exact commit
-> runner proves shared Core/contract bytes match reviewed main
-> runner executes only allowlisted canonical Core mechanics
-> runner commits only edition-local generated authorities/receipts
-> ChatGPT resumes from canonical State
```

Retrospective initialization additionally follows:

```text
configured slug
-> existing config/special-pipeline.json + special_pipeline.bootstrap_plan authority
-> ChatGPT reads applicable period guide and materializes edition-local research scope
-> one deterministic RETROSPECTIVE_PERIOD Profile adapter binds exact period/identity/paths + authored scope
-> Core initializes canonical Profile/State
```

This is one adapter for `MONTHLY`, `HALF_YEAR`, and `ANNUAL`; it is not three cadence engines.

### Current implementation candidate

Maintenance branch:

`maintenance/core-v2-operator-execution-bridge`

Candidate files include:

- `docs/survey-production-core-v2-operator-execution-bridge.md`
- `schemas/operator-execution-request-v2.schema.json`
- `schemas/retrospective-scope-spec-v2.schema.json`
- `scripts/survey_core_execution_bridge_v2.py`
- `scripts/survey_retrospective_profile_v2.py`
- `.github/workflows/survey-production-v2-operator-bridge.yml`
- `tests/test_survey_core_execution_bridge_v2.py`
- `tests/test_survey_retrospective_profile_v2.py`

Current allowlisted operations:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`

Human Architecture approval, Publication Preview approval and Release are deliberately outside this bridge operation set.

### Acceptance criteria

PFB-014 cannot close until all of the following hold:

1. no arbitrary command/module/script surface from request data;
2. request path/id/branch/source-root are exact and fail closed;
3. every operation binds one exact reviewed-main SHA and initialization execution records bind the same SHA;
4. before dependency installation/execution, the request parent must descend from reviewed main and protected shared Core/contract bytes must match it exactly;
5. triggering commit adds exactly one immutable request and changes nothing else;
6. generated writes are constrained to the Profile-bound edition source root;
7. immutable request bytes are never mutated by the runner;
8. `ADVANCE_STAGE` requires an exact expected current lifecycle state;
9. deterministic `CORE_STAGE_CONTRACT` is generated by canonical Core code, not supplied by ChatGPT;
10. ChatGPT agent review rows cannot impersonate deterministic results;
11. output commits do not recursively retrigger the workflow;
12. exact implementation/request/State provenance is recorded;
13. direct-local CLI remains preferred when available;
14. Retrospective initialization reuses configured-period authority, rejects unconfigured/pre-period-end targets, and one builder covers monthly/half-year/annual without fixed editorial taxonomy;
15. bridge exact-head CI and changed-scope six-point audit pass;
16. after reviewed integration, fresh W33 and SP001 clean production trials plus representative Retrospective and Foundations-guided trials reach their required gate without shared-Core repair.

### Classification

This began as `TRANSIENT_EXECUTION / OPERATOR-RUNTIME CAPABILITY`. Because the repository's production model must work in the actual ChatGPT operator runtime used for this project, the missing generic execution fallback is now being treated as a **shared operator/Core integration maintenance requirement** rather than an edition-local defect.

The missing Retrospective cold-start adapter found during fixed-head audit is part of the same integration requirement, not an edition-specific Retrospective defect: the Core contract already defined `RETROSPECTIVE_PERIOD`, and the adapter now binds that existing Profile to the repository's already-canonical configured-period authority.

## Current next step

Do not resume W33/SP001/Retrospective canonical acceptance execution on a pre-PFB-014 integrated baseline.

Maintenance sequence:

```text
finish PFB-014 bridge + Retrospective adapter implementation/documentation
-> run exact-head Core CI + pipeline contract tests
-> repair generic regressions only
-> freeze one exact maintenance candidate SHA
-> rerun changed-scope six-point Core audit from zero
-> Human full-candidate review
-> integrate unchanged accepted head
-> recreate/reset clean validation branches from reviewed main
-> reapply only legitimate Raw/research preparation
-> execute PFB-013 cold-start validation canonically across Weekly / Thematic-SP001 / Retrospective / Foundations-guided scenarios
```

Any maintenance-tree change after a frozen audit invalidates that audit and requires a new exact head plus a complete rerun.
