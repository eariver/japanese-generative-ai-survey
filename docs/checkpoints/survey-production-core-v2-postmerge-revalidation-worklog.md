# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `OPERATOR BRIDGE MAINTENANCE IN PROGRESS / W33 + SP001 COLD REVALIDATION PAUSED UNTIL REVIEWED INTEGRATION`

Established: 2026-08-23 JST  
Last updated: 2026-08-23 JST

Integrated Core baseline that exposed the gap: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`

Current `main` at maintenance start: `2bcaa7d1df1826ab8848c25de8bf2373d85a8e75`

Current shared-Core maintenance branch:

`maintenance/core-v2-operator-execution-bridge`

Validation editions retained as non-PASS evidence while maintenance is in progress:

- Weekly: `weekly/2026-W33-v2-work`
- Thematic/LONGFORM regression: `special/SP001-v2-work`

Historical failed pre-redesign editions remain archived separately and are not acceptance evidence.

## Resume checkpoint — read this first

The post-merge clean W33/SP001 trials successfully exercised real ChatGPT research/editorial work, including the actual Human-mediated Grok/Google Drive boundary for W33, but could not begin canonical Core lifecycle execution because the ChatGPT connector runtime had no exact repository checkout/CLI bridge.

That blocker is now being handled as **shared operator/Core maintenance**, not by fabricating machine artifacts and not by adding edition-specific temporary workflows.

Current position:

1. W33 and SP001 production branches are intentionally paused.
2. A generic deterministic operator bridge is being implemented on `maintenance/core-v2-operator-execution-bridge`.
3. The bridge is intended to execute only canonical deterministic Core mechanics from one immutable edition-local request commit.
4. After bridge exact-head CI/audit and Human-reviewed integration, W33/SP001 must be cleanly restarted/rebased from the reviewed `main` and rerun canonically.
5. Neither existing trial may be relabeled as PASS.

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

Status: `CONFIRMED / MAINTENANCE IMPLEMENTATION UNDERWAY`

The connector runtime can research and mutate GitHub but cannot necessarily mount the exact repository branch and execute the canonical local Core CLI. Manually imitating Profile/State/checkpoint output is prohibited.

The accepted maintenance direction is a generic **deterministic operator execution bridge** that preserves ChatGPT authorship and uses Actions only as the missing checked-out execution substrate.

### RVF-006 — do not fabricate machine acceptance

Status: `CONFIRMED OPERATIONAL RULE`

If canonical deterministic execution is unavailable, preserve research/provenance and stop before machine acceptance rather than hand-authoring plausible validator output.

### RVF-007 — edition-local human-readable resume records remain useful

Status: `CONFIRMED / MIGRATION PRACTICE`

Before canonical `execution/` bootstrap is available, concise edition-local resume files are acceptable migration evidence. Once canonical Profile/State is initialized, `sources/<issue>/execution/` becomes the preferred operational record.

### RVF-008 — old failed artifacts remain visibly non-authoritative

Status: `CONFIRMED`

W33's historical `pipeline-state.json` remains `NON_AUTHORITATIVE_READ_ONLY`; SP001 failed accepted artifacts remain on the archived branch only.

## Current maintenance design

Authority/plan document:

`docs/survey-production-core-v2-operator-execution-bridge.md`

Maintenance branch:

`maintenance/core-v2-operator-execution-bridge`

Current implementation candidate adds:

- `schemas/operator-execution-request-v2.schema.json`
- `scripts/survey_core_execution_bridge_v2.py`
- `.github/workflows/survey-production-v2-operator-bridge.yml`
- `tests/test_survey_core_execution_bridge_v2.py`
- regression update to `tests/test_survey_pilot_bootstrap_v2.py`

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
2. `INITIALIZE_THEMATIC`;
3. `ADVANCE_STAGE` over already-authored exact artifacts.

The bridge does not expose arbitrary commands, shell snippets, module names, Architecture approval, Publication Preview approval or Release.

### Request/receipt shape

Request authority:

```text
sources/<issue-id>/execution/requests/<request-id>.json
```

Bridge result/receipt authority:

```text
sources/<issue-id>/execution/bridge-runs/<request-id>/
```

Workflow trigger rules currently require:

- one newly added request;
- request-only triggering commit;
- edition work branch (`weekly/**` or `special/**`);
- non-bot actor;
- generated writes only under the target edition source root;
- no mutation of immutable request authority.

The bot output commit does not change a request file and therefore does not recursively retrigger the bridge.

## Why this is not a return to the old Actions-heavy pipeline

The failed pre-redesign topology used Actions to author/mutate editorial and publication content, choose repairs, chain state changes and create bot-driven production loops.

The bridge instead supplies one missing execution property: an exact repository checkout capable of running already-existing deterministic Core code. It neither selects content nor creates semantic judgments.

This is consistent with the Actions admission principle only if the implementation remains narrow and fail-closed.

## PFB-013 status

Existing requirement: real cold-start Weekly + SP001/LONGFORM validation after reviewed Core integration.

Current verdict:

`PARTIALLY EXERCISED / NOT PASSED`

PFB-013 cannot close until the bridge (or another equivalent execution path) is reviewed/integrated and new clean W33/SP001 runs reach pending `ARCHITECTURE_REVIEW` with canonical State and no in-run shared-Core repair.

## PFB-014 candidate

Proposed new maintenance feedback item:

**Operator runtime requires a generic deterministic Core execution fallback when direct local checkout/CLI execution is unavailable.**

Acceptance criteria:

- no arbitrary command surface;
- exact request commit identity;
- immutable one-request trigger;
- edition-local write scope;
- canonical Core code, not duplicated semantics;
- no research/editorial/visual/Human decision ownership in Actions;
- no bot recursion;
- stage/state provenance binds exact implementation commit;
- direct-local CLI remains preferred when available;
- bridge path is proven by clean W33 and SP001 production revalidation.

Do not mark PFB-014 closed merely because unit tests pass; real edition use is required.

## Next actions

### Shared Core maintenance

```text
finish operator bridge implementation
-> update affected policy/feedback docs
-> open maintenance PR
-> run exact-head Core CI + pipeline contract tests
-> inspect failures and repair generically
-> freeze one exact maintenance head
-> rerun the six-point Core audit from zero for changed scope
-> Human review/integration
```

Any maintenance-tree change after a frozen audit invalidates that audit and requires a fresh exact-head rerun.

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
| W33 current position / plan | `weekly/2026-W33-v2-work` | `sources/2026-W33/postmerge-validation-status.md` |
| W33 research / Architecture preparation | `weekly/2026-W33-v2-work` | `sources/2026-W33/postmerge-research-intake.md` |
| W33 exact Grok Raw | `weekly/2026-W33-v2-work` | `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md` |
| SP001 current position / plan | `special/SP001-v2-work` | `sources/SP001/postmerge-validation-status.md` |
| SP001 research scope | `special/SP001-v2-work` | `sources/SP001/research-scope-v2.json` |
| SP001 research intake | `special/SP001-v2-work` | `sources/SP001/intake/postmerge-primary-source-intake.md` |
| SP001 Architecture preparation | `special/SP001-v2-work` | `sources/SP001/architecture-preparation.md` |
| Pre-bridge feedback backlog | `main` | `docs/survey-production-core-v2-production-feedback-backlog.md` |

Repository reality and canonical Production State, once created, outrank this human-readable summary.
