# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `OPERATOR BRIDGE MAINTENANCE / FINAL CANDIDATE PREPARATION / W33 + SP001 COLD REVALIDATION PAUSED UNTIL REVIEWED INTEGRATION`

Established: 2026-08-23 JST  
Last updated: 2026-08-23 JST

Integrated Core baseline that exposed the operator gap: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`

Current `main` at maintenance start: `2bcaa7d1df1826ab8848c25de8bf2373d85a8e75`

Current shared-Core maintenance branch:

`maintenance/core-v2-operator-execution-bridge`

Maintenance PR:

`#447 Core v2: add deterministic operator execution bridge`

Validation editions retained as non-PASS evidence while maintenance is in progress:

- Weekly: `weekly/2026-W33-v2-work`
- Thematic/LONGFORM regression: `special/SP001-v2-work`

Historical failed pre-redesign editions remain archived separately and are not acceptance evidence.

## Resume checkpoint — read this first

The post-merge clean W33/SP001 trials successfully exercised real ChatGPT research/editorial work, including the actual Human-mediated Grok/Google Drive boundary for W33, but could not begin canonical Core lifecycle execution because the ChatGPT connector runtime had no exact repository checkout/CLI bridge.

That blocker is handled as **shared operator/Core maintenance**, not by fabricating machine artifacts and not by adding edition-specific temporary workflows.

Current position:

1. W33 and SP001 production branches remain intentionally paused.
2. A generic deterministic operator bridge is implemented on `maintenance/core-v2-operator-execution-bridge`.
3. The bridge executes only canonical deterministic Core mechanics from one immutable edition-local request-only commit.
4. The bridge now supports canonical cold-start initialization for all three Research Profile families that have repository-owned initialization authority:
   - `WEEKLY`;
   - configured `RETROSPECTIVE_PERIOD`;
   - `THEMATIC`.
5. After exact-head CI, fixed-head six-point audit, Human review, and unchanged integration, W33/SP001 must be cleanly restarted/rebased from reviewed `main` and rerun canonically.
6. Neither existing production trial may be relabeled as PASS.

## Edition-local resume authorities

### W33

Branch:

`weekly/2026-W33-v2-work`

Primary resume file:

`sources/2026-W33/postmerge-validation-status.md`

Completed preparation:

- canonical Weekly window resolved;
- one self-contained Drive `grok-task.md` created and executed by Grok;
- exact returned Raw bytes imported;
- X/community signal disposition performed;
- primary-source follow-up performed;
- fresh editorial Architecture preparation written.

Important exact Raw authority:

`sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md`

SHA-256:

`93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`

Do not rerun Grok unless the exact existing Raw is later proven unusable by canonical validation.

### SP001

Branch:

`special/SP001-v2-work`

Primary resume file:

`sources/SP001/postmerge-validation-status.md`

Completed preparation:

- current Thematic backlog scope materialized;
- X/Grok applicability prepared as `NOT_REQUIRED`;
- primary-source research across the major Chinese model families completed to Architecture-preparation depth;
- licensing/open-weight/runtime boundaries explicitly separated;
- seven scope obligations mapped;
- six-package editorial Architecture preparation written.

Prepared files:

- `sources/SP001/research-scope-v2.json`
- `sources/SP001/intake/postmerge-primary-source-intake.md`
- `sources/SP001/architecture-preparation.md`

Do not copy failed pre-redesign accepted artifacts into the clean rerun.

## Revalidation findings retained

### RVF-001 — Human-mediated Grok/Drive transport works

Status: `CONFIRMED BY REAL W33 OPERATION`

The single-task-file boundary worked:

```text
ChatGPT prepares exact grok-task.md
-> Human passes only that Drive path/reference to Grok
-> Grok writes result in instructed run folder
-> ChatGPT retrieves exact bytes
-> ChatGPT imports Raw and resumes
```

No Grok connector is required for the normal boundary.

### RVF-002 — X/community and technical Evidence separation works editorially

Status: `CONFIRMED EDITORIALLY / CANONICAL MANIFEST VALIDATION STILL PENDING`

Grok/X is useful for salience, hands-on behavior, disagreement, practical friction and community movement. Technical facts still require authoritative verification before entering Evidence.

### RVF-003 — fresh X can materially change Weekly Architecture

Status: `CONFIRMED BY W33`

The Aug. 12–14 model-release wave materially changed W33 package selection and synthesis after primary-source follow-up. Weekly X intake is therefore not merely decorative.

### RVF-004 — Thematic X applicability can legitimately be `NOT_REQUIRED`

Status: `CONFIRMED EDITORIALLY BY SP001 / CANONICAL RECORD PENDING`

SP001's technical-history question can be closed with first-party technical/distribution/license authorities without mandatory X transport.

### RVF-005 — operator execution path was the blocking dependency

Status: `CONFIRMED / BRIDGE IMPLEMENTED / FINAL AUDIT PENDING`

The connector runtime can research and mutate GitHub but cannot necessarily mount the exact repository branch and execute the canonical local Core CLI. Manually imitating Profile/State/checkpoint output is prohibited.

The maintenance direction is a generic **deterministic operator execution bridge** that preserves ChatGPT authorship and uses Actions only as the missing checked-out execution substrate.

### RVF-006 — do not fabricate machine acceptance

Status: `CONFIRMED OPERATIONAL RULE`

If canonical deterministic execution is unavailable, preserve research/provenance and stop before machine acceptance rather than hand-authoring plausible validator output.

### RVF-007 — edition-local human-readable resume records remain useful

Status: `CONFIRMED / MIGRATION PRACTICE`

Before canonical `execution/` bootstrap is available, concise edition-local resume files are acceptable migration evidence. Once canonical Profile/State is initialized, `{source_root}/execution/` becomes the preferred operational record.

### RVF-008 — old failed artifacts remain visibly non-authoritative

Status: `CONFIRMED`

W33's historical `pipeline-state.json` remains `NON_AUTHORITATIVE_READ_ONLY`; SP001 failed accepted artifacts remain on the archived branch only.

### RVF-009 — fixed-head audit itself found stale workflow-count authority

Status: `FOUND / REPAIRED / ORIGINAL AUDIT INVALIDATED`

First frozen maintenance candidate:

`89b0a02c8699c957dc8ca09d0228e9d8b4ce7287`

Fresh six-point audit discovered that `docs/survey-production-core-v2-final-audit-rule.md` still required the pre-PFB-014 six-workflow surface, while the current redesign authority correctly admitted seven workflows including the operator bridge.

Per the fixed-head invalidation rule:

```text
finding requires repository change
-> candidate audit invalidated
-> authority synchronized to seven workflows
-> regression added
-> freeze a new candidate and restart from point 1
```

No PASS from the `89b0a02c...` audit is reusable.

### RVF-010 — Retrospective cold-start path was missing from the bridge/Core-v2 adapter surface

Status: `FOUND / REPAIRED / SECOND AUDIT INVALIDATED`

Second frozen maintenance candidate:

`0caa2c4f9ed87a32e50cf7813990b916489581bc`

Fresh Point 2 (`Special viability`) inspection established:

- Core v2 already declared `RETROSPECTIVE_PERIOD + LONGFORM_SPECIAL + BOUNDED_PERIOD` as a canonical profile family;
- existing Special authority already provided configured monthly/half-year/annual slugs, exact coverage windows, canonical identities, required guides and canonical paths through `config/special-pipeline.json` + `scripts/special_pipeline.py bootstrap-plan`;
- but Core v2 had no canonical adapter that materialized those configured-period authorities into a v2 Production Profile;
- therefore the connector-only runtime could not start the required post-integration Retrospective validation through the bridge.

The candidate audit was invalidated rather than weakening Point 2.

Repair deliberately did **not** add separate monthly/half-year/annual engines. It added one configured-period adapter:

- `schemas/retrospective-scope-spec-v2.schema.json`
- `scripts/survey_retrospective_profile_v2.py`
- bridge operation `INITIALIZE_RETROSPECTIVE`
- contract registration and regression coverage.

Configured period identity, tier, coverage, required guides and paths remain owned by existing `special_pipeline.bootstrap_plan`. ChatGPT materializes only the edition-local research question, inclusion/exclusion, dimensions and initial obligations after reading the required period guides.

Representative regression covers the same builder across:

- monthly `2026-M07`;
- half-year `2024-H1`;
- annual `2023-Y`.

The adapter fail-closes on unconfigured slugs, planning-authority SHA drift, issue-id drift, scope materialized after initialization, and initialization before period end.

No PASS from the `0caa2c4f...` audit is reusable.

## Current maintenance design

Authority/plan document:

`docs/survey-production-core-v2-operator-execution-bridge.md`

Maintenance branch:

`maintenance/core-v2-operator-execution-bridge`

Current implementation candidate includes:

- `schemas/operator-execution-request-v2.schema.json`
- `schemas/retrospective-scope-spec-v2.schema.json`
- `scripts/survey_core_execution_bridge_v2.py`
- `scripts/survey_retrospective_profile_v2.py`
- `.github/workflows/survey-production-v2-operator-bridge.yml`
- `tests/test_survey_core_execution_bridge_v2.py`
- `tests/test_survey_retrospective_profile_v2.py`
- regression updates to `tests/test_survey_pilot_bootstrap_v2.py`
- synchronized Core authority/policy/worklog/config documents.

### Bridge responsibility boundary

ChatGPT still owns:

- research/source strategy;
- Evidence/materiality/completeness judgment;
- Selection;
- Architecture;
- drafting/synthesis;
- semantic/editorial review;
- exact-PDF visual review;
- Human-Gate preparation.

The bridge may execute only:

1. `INITIALIZE_WEEKLY`;
2. `INITIALIZE_RETROSPECTIVE` using the existing configured-period Special authority plus a ChatGPT-authored edition-local scope spec;
3. `INITIALIZE_THEMATIC`;
4. `ADVANCE_STAGE` over already-authored exact artifacts.

The bridge does not expose arbitrary commands, shell snippets, module names, Architecture approval, Publication Preview approval or Release.

### Reviewed-main preflight

Every request binds one exact lowercase 40-hex `reviewed_main_sha`.

Before dependency installation or Core execution, the workflow requires:

- the SHA to exist on current `main` history;
- the request parent to descend from it;
- initialization execution-record SHA to match it;
- fixed minimum shared roots `.github/workflows`, `config`, `schemas`, `scripts` plus configured contract paths to be byte-identical between the reviewed-main baseline and request parent.

This prevents an edition branch from silently running drifted/shared-Core code while claiming reviewed-main provenance.

### Request/receipt shape

Request authority:

```text
{source_root}/execution/requests/<request-id>.json
```

Bridge result/receipt authority:

```text
{source_root}/execution/bridge-runs/<request-id>/
```

Workflow trigger rules require:

- one newly added request;
- request-only triggering commit;
- exact request work-branch/ref match rather than hardcoded cadence branch prefixes;
- non-bot actor;
- reviewed-main Core preflight;
- generated writes only under the Profile-bound source root;
- no mutation of immutable request authority.

The bot output commit does not add a request file and is also actor-guarded, so it cannot recursively chain bridge execution.

## Why this is not a return to the old Actions-heavy pipeline

The failed pre-redesign topology used Actions to author/mutate editorial and publication content, choose repairs, chain state changes and create bot-driven production loops.

The bridge instead supplies one missing execution property: an exact repository checkout capable of running already-existing deterministic Core code. It neither selects content nor creates semantic judgments.

This remains consistent with the Actions admission principle only while the implementation stays narrow and fail-closed.

Current Actions surface is exactly seven workflows. A new eighth workflow is prima facie architectural regression unless separately reviewed against the same admission rule.

## Diagnostic CI evidence before final freeze

These runs are useful diagnostics but are **not final fixed-head acceptance evidence** if the branch changes afterward.

At maintenance head `6ba6748a4e06e63a24ddac34173a7a2534b7e370`:

- Survey Production Core v2 CI run `32644491998`: PASS;
- Pipeline contract tests run `32644492001`: PASS.

Subsequent candidate-preparation changes include only the planned Retrospective CLI fail-closed timestamp handling, its regression test, and this worklog/authority synchronization. Exact-head CI must be rerun after the final candidate SHA is frozen.

## PFB-013 status

Existing requirement: real cold-start Weekly + SP001/LONGFORM validation after reviewed Core integration, plus representative Retrospective and Foundations-guided validation under the current final-audit rule.

Current verdict:

`PARTIALLY EXERCISED / NOT PASSED`

The first post-merge clean attempts performed substantial real operator work, and W33 successfully exercised the actual Grok/Drive handoff. They did not reach canonical Profile/State lifecycle execution because the operator runtime lacked an execution bridge.

PFB-013 remains open until reviewed integration and clean post-integration runs.

## PFB-014 status

Feedback item:

**Operator runtime requires a generic deterministic Core execution fallback when direct local checkout/CLI execution is unavailable.**

Status:

`IMPLEMENTED CANDIDATE / EXACT-HEAD REAUDIT PENDING`

Acceptance criteria include:

1. no arbitrary command/module/script surface from request data;
2. request path/id/branch are exact and fail closed;
3. triggering commit adds exactly one immutable request and changes nothing else;
4. reviewed-main shared-Core preflight runs before dependency installation/execution;
5. generated writes are constrained to the Profile-bound edition source root;
6. immutable request bytes are never mutated by the runner;
7. `ADVANCE_STAGE` requires an exact expected current lifecycle state;
8. deterministic `CORE_STAGE_CONTRACT` is generated by canonical Core code, not supplied by ChatGPT;
9. ChatGPT agent review rows cannot impersonate deterministic results;
10. output commits do not recursively retrigger the workflow;
11. exact implementation/request/State provenance is recorded;
12. direct-local CLI remains preferred when available;
13. canonical cold-start initialization is structurally available for Weekly, configured Retrospective Period and Thematic without cadence/topic-specific authoring workflows;
14. bridge exact-head CI and complete six-point fixed-head audit pass;
15. after reviewed integration, fresh representative production trials reach their requested Human Gate without in-run shared-Core repair.

Do not mark PFB-014 closed merely because unit tests pass; real edition use is still required.

## Next actions

### Shared Core maintenance

```text
finish final authority/implementation cross-check
-> freeze one exact maintenance candidate SHA
-> run exact-head Core CI + pipeline contract tests
-> rerun the complete six-point Core audit from point 1 on that exact unchanged SHA
-> if any repository change is required, invalidate and restart
-> if 6/6 PASS, record the result outside the candidate tree in PR #447
-> mark PR #447 ready for Human full-candidate review
```

### After reviewed unchanged integration

```text
reset/rebase clean validation branches from reviewed main
-> restore only legitimate edition-local Raw/research preparation
-> execute canonical cold-start matrix through the bridge/direct local Core as available:
   Weekly
   standalone Thematic/LONGFORM (SP001 regression)
   representative Retrospective Period
   Foundations-guided scenario
-> stop at the requested Human Gates
-> preserve any shared-Core defect as failed evidence and repair separately
```

### W33 after reviewed integration

```text
reset/rebase clean W33 validation branch from reviewed main
-> restore only legitimate exact Raw + editorial preparation
-> commit INITIALIZE_WEEKLY bridge request
-> verify canonical Profile/State/execution record
-> canonical X manifest binding of existing Raw
-> Discovery
-> Screening
-> Evidence / Materiality / Completeness
-> Candidate Matrix / Selection
-> Architecture
-> ARCHITECTURE_REVIEW
```

### SP001 after reviewed integration

```text
reset/rebase clean SP001 validation branch from reviewed main
-> restore current scope + legitimate research/Architecture preparation only
-> commit INITIALIZE_THEMATIC bridge request
-> verify canonical Profile/State/execution record
-> canonical X NOT_REQUIRED disposition
-> Discovery
-> Screening
-> Evidence / Materiality / Completeness
-> Candidate Matrix / Selection
-> Architecture
-> ARCHITECTURE_REVIEW
```

## Files to use when resuming

| Purpose | Branch | File |
|---|---|---|
| Shared bridge maintenance current position | `maintenance/core-v2-operator-execution-bridge` | `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md` |
| Bridge design/boundary | `maintenance/core-v2-operator-execution-bridge` | `docs/survey-production-core-v2-operator-execution-bridge.md` |
| Current redesign authority overlay | `maintenance/core-v2-operator-execution-bridge` | `docs/survey-production-core-v2-redesign-authority.md` |
| Current final audit rule | `maintenance/core-v2-operator-execution-bridge` | `docs/survey-production-core-v2-final-audit-rule.md` |
| W33 current position / plan | `weekly/2026-W33-v2-work` | `sources/2026-W33/postmerge-validation-status.md` |
| W33 research / Architecture preparation | `weekly/2026-W33-v2-work` | `sources/2026-W33/postmerge-research-intake.md` |
| W33 exact Grok Raw | `weekly/2026-W33-v2-work` | `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md` |
| SP001 current position / plan | `special/SP001-v2-work` | `sources/SP001/postmerge-validation-status.md` |
| SP001 research scope | `special/SP001-v2-work` | `sources/SP001/research-scope-v2.json` |
| SP001 research intake | `special/SP001-v2-work` | `sources/SP001/intake/postmerge-primary-source-intake.md` |
| SP001 Architecture preparation | `special/SP001-v2-work` | `sources/SP001/architecture-preparation.md` |

Repository reality and canonical Production State, once created, outrank this human-readable summary.
