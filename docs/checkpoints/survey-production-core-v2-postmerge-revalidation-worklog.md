# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `OPERATOR BRIDGE MAINTENANCE / FINAL CANDIDATE PREPARATION / W33 + SP001 COLD REVALIDATION PAUSED UNTIL REVIEWED INTEGRATION`

Established: 2026-08-23 JST  
Last updated: 2026-08-23 JST

Integrated Core baseline that exposed the operator gap: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`  
Maintenance-start `main`: `2bcaa7d1df1826ab8848c25de8bf2373d85a8e75`  
Maintenance branch: `maintenance/core-v2-operator-execution-bridge`  
Maintenance PR: `#447 Core v2: add deterministic operator execution bridge`

W33/SP001 remain paused non-PASS production-validation evidence until reviewed unchanged bridge integration.

## Resume checkpoint

The post-merge clean W33/SP001 trials exercised real ChatGPT research/editorial work and the real W33 Human-mediated Grok/Drive handoff, but could not begin canonical Core lifecycle execution because the connector runtime had no exact checkout/CLI execution substrate.

The response is shared operator/Core maintenance, not fabricated Profile/State/checkpoint authority and not an edition-specific temporary workflow.

Current bridge allowlist:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`

Configured Retrospective initialization reuses the **existing `scripts/survey_period_v2.py`** Core helper. No second Retrospective builder survives in the candidate.

## Edition-local resume authority

### W33

Branch: `weekly/2026-W33-v2-work`  
Resume file: `sources/2026-W33/postmerge-validation-status.md`

Completed preparation includes canonical Weekly window resolution, real one-file Grok/Drive execution, exact Raw import, X/community disposition, primary-source follow-up and editorial Architecture preparation.

Exact Raw:

`sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md`

SHA-256: `93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`

Do not rerun Grok unless canonical validation later proves those exact bytes unusable.

### SP001

Branch: `special/SP001-v2-work`  
Resume file: `sources/SP001/postmerge-validation-status.md`

Prepared authority/research:

- `sources/SP001/research-scope-v2.json`
- `sources/SP001/intake/postmerge-primary-source-intake.md`
- `sources/SP001/architecture-preparation.md`

X/Grok applicability is prepared as `NOT_REQUIRED`. Do not copy failed pre-redesign accepted artifacts into the clean rerun.

## Revalidation findings

### RVF-001 — Human-mediated Grok/Drive transport works

Status: `CONFIRMED BY REAL W33 OPERATION`

```text
ChatGPT prepares exact grok-task.md
-> Human passes only that Drive path/reference to Grok
-> Grok writes result in instructed run folder
-> ChatGPT retrieves/imports exact Raw
-> ChatGPT resumes
```

No Grok connector is required.

### RVF-002 — X/community and technical Evidence separation works

Status: `CONFIRMED EDITORIALLY / CANONICAL MANIFEST VALIDATION PENDING`

Grok/X supplies salience/community signal. Technical claims still require authoritative verification before Evidence acceptance.

### RVF-003 — fresh X can materially change Weekly Architecture

Status: `CONFIRMED BY W33`

W33's Aug. 12–14 model-release wave materially changed package selection and synthesis after primary-source verification.

### RVF-004 — Thematic X may legitimately be `NOT_REQUIRED`

Status: `CONFIRMED EDITORIALLY BY SP001 / CANONICAL RECORD PENDING`

### RVF-005 — operator execution path was the blocking dependency

Status: `CONFIRMED / BRIDGE IMPLEMENTED / FINAL AUDIT PENDING`

The connector runtime can research/edit GitHub but cannot necessarily execute canonical local Core over the exact branch. Manual imitation of machine authority is prohibited.

### RVF-006 — do not fabricate machine acceptance

Status: `CONFIRMED OPERATIONAL RULE`

If canonical deterministic execution is unavailable, preserve preparation/provenance and stop before machine acceptance.

### RVF-007 — edition-local human-readable resume records remain useful

Status: `CONFIRMED / MIGRATION PRACTICE`

Once canonical Profile/State exists, `{source_root}/execution/` becomes the preferred operational record.

### RVF-008 — old failed artifacts remain non-authoritative

Status: `CONFIRMED`

W33 historical `pipeline-state.json` remains `NON_AUTHORITATIVE_READ_ONLY`; SP001 failed accepted artifacts remain archived only.

### RVF-009 — first fixed-head audit found stale workflow-count authority

Status: `FOUND / REPAIRED / AUDIT INVALIDATED`

Candidate: `89b0a02c8699c957dc8ca09d0228e9d8b4ce7287`

The current audit rule still said six workflows while PFB-014 correctly introduced a seventh operator-bridge workflow. The candidate changed, so the complete audit was invalidated. No PASS from that audit is reusable.

### RVF-010 — second fixed-head audit found Retrospective bridge exposure missing

Status: `FOUND / REPAIRED / AUDIT INVALIDATED / DIAGNOSIS CORRECTED BEFORE FINAL FREEZE`

Candidate: `0caa2c4f9ed87a32e50cf7813990b916489581bc`

Point 2 (`Special viability`) correctly established that a bridge exposing only Weekly/Thematic could not execute the mandated connector-runtime Retrospective validation.

Initial diagnosis incorrectly concluded that Core v2 lacked a canonical configured-period Profile adapter. Deeper pre-freeze inspection later found that the maintenance base already contained:

- `scripts/survey_period_v2.py`
- `tests/test_survey_period_v2.py`

That existing Core helper already supports generic configured monthly/half-year/annual `RETROSPECTIVE_PERIOD + LONGFORM_SPECIAL`, custom bounded periods, pre-period-end rejection, unknown-slug rejection and resume semantics.

Therefore the true defect was narrower:

> **The operator bridge did not expose the already-existing canonical `survey_period_v2` initializer.**

Temporary duplicate files created under the incorrect diagnosis were removed before final candidate freeze:

- `scripts/survey_retrospective_profile_v2.py`
- `schemas/retrospective-scope-spec-v2.schema.json`
- `tests/test_survey_retrospective_profile_v2.py`

Final Retrospective bridge semantics are:

```text
request special_slug
-> survey_period_v2.resolve_configured_period(...)
-> survey_period_v2.period_profile(...)
-> exact request/Profile identity check
-> canonical Core initialize(...)
```

No PASS from the `0caa2c4f...` audit is reusable.

### RVF-011 — bridge glue has an end-to-end regression

Status: `IMPLEMENTED / FINAL EXACT-HEAD CI PENDING`

`tests/test_survey_core_execution_bridge_v2.py` exercises a temporary Thematic edition through:

```text
immutable INITIALIZE_THEMATIC request
-> canonical Profile/State/execution record
-> X NOT_REQUIRED manifest
-> Discovery acceptance
-> second immutable ADVANCE_STAGE request
-> DISCOVERY_COLLECTED + next_action=stage:screening
```

The first diagnostic CI attempt exposed only a sparse-checkout fixture assumption (`sources/` directory absent); the fixture was corrected before final freeze.

## Current maintenance design

Candidate scope contains bridge/authority changes, not a duplicate Retrospective implementation:

- `.github/workflows/survey-production-v2-operator-bridge.yml`
- `schemas/operator-execution-request-v2.schema.json`
- `scripts/survey_core_execution_bridge_v2.py`
- `tests/test_survey_core_execution_bridge_v2.py`
- workflow/config/authority/regression synchronization.

Existing `scripts/survey_period_v2.py` remains the Retrospective builder and is unchanged by the maintenance PR.

### Reviewed-main preflight

Every request binds exact lowercase 40-hex `reviewed_main_sha`. Before dependency installation/Core execution, the workflow requires reviewed SHA on current `main` history, request-parent descent, initialization execution-record baseline equality, and byte equality for fixed shared implementation roots plus configured contract files.

### Request/receipt

```text
{source_root}/execution/requests/<request-id>.json
{source_root}/execution/bridge-runs/<request-id>/
```

Trigger is request-only; generated writes are Profile-source-root-bound; immutable requests cannot be mutated; bot output cannot recursively retrigger.

## Why this is not a return to Actions-heavy production

The bridge supplies only the missing exact checked-out deterministic execution substrate. It neither chooses content nor creates research/editorial/visual/Human judgments.

Current Actions surface is exactly seven workflows. A new eighth workflow requires separate Actions-policy review.

## Diagnostic CI evidence before final freeze

Diagnostic runs are not final acceptance evidence if the candidate tree changes afterward.

- head `6ba6748a4e06e63a24ddac34173a7a2534b7e370`: Core v2 CI PASS and Pipeline contract tests PASS;
- head `4088bcfc63aafa440f1966c5393f6aae912eee30`: E2E fixture FAIL before bridge execution because sparse checkout lacked `sources/`;
- head `08328d8babcb60b00be22d87a69289fd0e751ace`: Core v2 CI PASS after fixture correction.

All are pre-freeze diagnostics only.

## PFB-013 status

`PARTIALLY EXERCISED / NOT PASSED`

Real cold-start Weekly, SP001/LONGFORM, representative Retrospective and Foundations-guided validation remain required after reviewed unchanged integration.

## PFB-014 status

`IMPLEMENTED CANDIDATE / EXACT-HEAD REAUDIT PENDING`

Acceptance requires no arbitrary executable surface, exact request identity, reviewed-main preflight, Profile-bound writes, immutable requests, stale-state refusal, deterministic result ownership by Core, no deterministic-review impersonation, no recursive bot chain, exact provenance, direct local CLI preference, Weekly/configured Retrospective/Thematic exposure through existing Core builders, exact-head CI, complete six-point audit, and clean post-integration trials.

Do not close PFB-014 merely because unit tests pass.

## Next actions

```text
finish authority/implementation cross-check
-> freeze exact maintenance candidate SHA
-> exact-head Core CI + pipeline contract tests
-> complete six-point audit from point 1 on unchanged SHA
-> any required tree change invalidates and restarts audit
-> 6/6 PASS: record result outside candidate tree in PR #447
-> mark PR #447 ready for Human full-candidate review
```

After Human-reviewed unchanged integration, reset/rebase clean W33/SP001 validation branches from reviewed main, restore only legitimate Raw/research preparation, then run the canonical Weekly / SP001 / representative Retrospective / Foundations validation matrix.

Repository reality and canonical Production State, once created, outrank this human-readable summary.
