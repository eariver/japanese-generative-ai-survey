# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `OPERATOR BRIDGE MAINTENANCE / PRE-APPROVAL FULL-SYSTEM AUDIT BLOCKED / HUMAN-GATE CONTROL DEFECTS FOUND`

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

Current bridge allowlist before the pre-approval audit repair is:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`

Configured Retrospective initialization reuses the **existing `scripts/survey_period_v2.py`** Core helper. No second Retrospective builder survives in the candidate.

The pre-approval full-system audit later established that this four-operation bridge is incomplete for connector-only production after a Human Gate is reached. See `RVF-015` below. Do not treat the earlier fixed-head `6/6 PASS` as current acceptance evidence.

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

Status: `CONFIRMED / BRIDGE PARTIAL / HUMAN-GATE RECORDING GAP FOUND`

The connector runtime can research/edit GitHub but cannot necessarily execute canonical local Core over the exact branch. Manual imitation of machine authority is prohibited.

The pre-approval full-system audit confirmed that the same constraint also applies to deterministic recording of an explicit Human Gate decision. The current bridge reaches gates but does not yet expose canonical Human Gate recording mechanics.

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

Status: `IMPLEMENTED / PREVIOUS FIXED-HEAD CI PASSED / CURRENT CANDIDATE INVALIDATED BY RVF-015`

`tests/test_survey_core_execution_bridge_v2.py` exercises a temporary Thematic edition through:

```text
immutable INITIALIZE_THEMATIC request
-> canonical Profile/State/execution record
-> X NOT_REQUIRED manifest
-> Discovery acceptance
-> second immutable ADVANCE_STAGE request
-> DISCOVERY_COLLECTED + next_action=stage:screening
```

The first diagnostic CI attempt exposed only a sparse-checkout fixture assumption (`sources/` directory absent); the fixture was corrected before the earlier freeze.

### RVF-012 — final authority text synchronized to repository reality before the earlier freeze

Status: `REPAIRED / CROSS-CHECK COMPLETE / SUPERSEDED AS ACCEPTANCE EVIDENCE BY RVF-015`

After the duplicate Retrospective implementation was removed, two top-level authority documents still contained wording from the incorrect diagnosis: they described connector Retrospective cold start as binding a ChatGPT-authored scope through a new adapter.

Before the earlier freeze, the following were synchronized to the actual implementation:

- `docs/survey-production-core-v2-final-audit-rule.md` — commit `34d5583f8760c82bc709b3138b856f5b29fcce2e`;
- `docs/survey-production-core-v2-redesign-authority.md` — commit `b4dfec73a21b2deeadad6daa66d07881bc69c9e2`.

Current authority states that configured Retrospective cold start reuses the pre-existing `survey_period_v2.resolve_configured_period()` + `period_profile()` path and that the operator bridge must not create a second Retrospective schema/builder or cadence engine.

### RVF-013 — Retrospective request fixture is bound to the existing Period builder

Status: `IMPLEMENTED / PREVIOUS FIXED-HEAD CI PASSED / CURRENT CANDIDATE INVALIDATED BY RVF-015`

Commit `3a680764ab7c1b29f6e785a39cef64796c839fd6` adds a regression that resolves configured `2024-H1` through `survey_period_v2.resolve_configured_period()` and `period_profile()`, then requires the resulting `RETROSPECTIVE_PERIOD + LONGFORM_SPECIAL` Profile's `issue_id`, `source_root`, and `work_branch` to equal the operator request fixture exactly.

This complements the pre-existing monthly/half-year/annual Period tests and the Thematic init→Discovery bridge E2E test. It specifically protects the bridge/configured-period identity join without introducing a duplicate Retrospective execution path.

### RVF-014 — pre-freeze PR-wide candidate cross-check completed

Status: `HISTORICAL PASS FOR a65e714b... / INVALIDATED AS CURRENT ACCEPTANCE EVIDENCE BY RVF-015`

The earlier pre-freeze cross-check examined the complete PR scope and current authority vocabulary.

Results at that time:

- PR #447 changed exactly 14 files;
- no `sources/` or `surveys/` edition output was part of the maintenance diff;
- implementation exposed four operations: Weekly init, configured Retrospective init, Thematic init, and one-stage advance;
- configured Retrospective init used only existing `survey_period_v2` semantics plus the new generic bridge exposure;
- removed duplicate Retrospective adapter/schema/test names remained only where this worklog recorded the invalidated diagnosis;
- current authority consistently described seven workflows, not the superseded six-workflow maintenance surface;
- current tests bound the seven-workflow set, reviewed-main preflight, no-arbitrary-command boundary, existing Period builder join, and Thematic init→Discovery E2E glue.

The resulting frozen candidate was `a65e714b711e76006318a14b252aa0a4e9727b4f`. Its exact-head/PR-merge-candidate CI subsequently passed and a six-point audit reported 6/6 PASS. The pre-approval full-system audit in RVF-015 found material lifecycle gaps outside that audit's effective scope, so that PASS must not be used as final approval evidence.

### RVF-015 — pre-approval full-system audit found Human Gate control gaps

Status: `BLOCKING / a65e714b... CANDIDATE INVALIDATED / PR MUST RETURN TO DRAFT`

After the user requested an independent whole-system audit before approving PR #447, the review was expanded beyond the six fixed-head points' pre-gate focus to include **what happens after a real Human Gate is reached**.

The earlier candidate remains valuable regression evidence: its exact tree passed Core v2 CI and pipeline contract tests, and its bridge preflight/allowlist/generalization design is largely sound. However, two material gaps make the candidate incomplete as the connector-only production execution substrate it claims to provide.

#### HG-001 — explicit Human approval cannot be canonically recorded through the bridge

Existing Core already has deterministic, exact-byte functions:

- `survey_agent_control_v2.approve_architecture(...)`
- `survey_agent_control_v2.approve_publication_preview(...)`

They validate the pending gate, exact reviewed bytes, write the canonical approval record, bind provenance into Production State, and refresh lifecycle control. The Human decision remains external; these functions only **record** that explicit decision.

The current operator request schema exposes only:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`

and the bridge design explicitly excludes Architecture/Publication Preview approval operations.

That distinction is too coarse for the connector-only runtime. It is correct that Actions must never *decide* Human approval, but after the Human explicitly approves, ChatGPT still needs an exact checkout/CLI substrate to run the deterministic approval recorder. Manually hand-authoring approval JSON or mutating State through the GitHub connector would violate RVF-006 and bypass canonical validators.

Therefore the bridge can reach `ARCHITECTURE_REVIEW` but cannot, in the same runtime model, resume normal production after an approval.

Required repair direction: expose only deterministic **Human-decision recording** operations that call the existing canonical approval functions and require explicit Human decision provenance. Do not let Actions infer or create the decision.

#### HG-002 — ordinary Human revision/rejection has no coherent canonical lifecycle path

The Production State schema permits `pending`, `approved`, and `rejected` for both normal Human Gates. Core control maps a rejected Human Gate to `EXCEPTION_GATE_REQUIRED`.

However:

- `architecture-approval-record-v2.schema.json` accepts only `decision: APPROVED`;
- `publication-preview-approval-v2.schema.json` accepts only `decision: APPROVED`;
- no canonical rejection/revision recorder was found in `survey_agent_control_v2.py` or the retained orchestration path;
- edition execution-record policy explicitly expects `architecture-r1.md`, `architecture-r2.md`, `publication-r1.md`, `publication-r2.md` and requires `Requested changes` plus a `Regeneration boundary`, so routine Human revision is clearly part of the intended operating model;
- completed Stage Checkpoints pin exact artifact SHA-256 values, and `validate_agent_state()` fails closed on `Stage Checkpoint artifact drift`.

Consequently, after the Human requests changes at Architecture Review, editing `architecture-v2.json` in place would invalidate the already-passed Architecture checkpoint, while no reverse/invalidation/revision transition exists to return safely to Selection/Architecture generation. Publication Preview has the same structural issue: changing reader source/PDF after validation invalidates pinned Stage Checkpoint bytes, but no canonical lifecycle path returns to drafting/validation and establishes a new candidate revision.

A Human review that requests ordinary corrections must not be forced into an Owner-level Exception Gate merely because the machine lifecycle lacks revision semantics.

Required repair direction: define an explicit fail-closed Human revision path that records the reviewed revision and requested regeneration boundary, invalidates only downstream authority, returns to the correct lifecycle boundary, and permits a new exact candidate to reach the same Human Gate again. Architecture and Publication Preview need equivalent semantics appropriate to their different downstream authorities.

#### Audit consequence

The prior fixed candidate `a65e714b711e76006318a14b252aa0a4e9727b4f` is **not approved for integration**.

The previous `6/6 PASS` was not fabricated: it was valid for the six checks as they were then applied and for the unchanged candidate tree. The failure was **audit-scope incompleteness**: it established that the system could reach the requested Human Gate and preserve role boundaries, but did not prove that the connector-only operator path could record an explicit Human decision or execute a normal Human-requested revision cycle afterward.

Any repair changes the candidate tree. Therefore:

1. PR #447 returns to Draft;
2. update bridge/Core authority and tests for HG-001/HG-002;
3. add end-to-end regression for at least:
   - reach Architecture Review → explicit Human approval record → resume drafting;
   - reach Architecture Review → requested revision → regenerate/revalidate → Architecture Review r2;
   - reach Publication Preview → explicit approval record → freeze path;
   - reach Publication Preview → requested revision → regenerate/revalidate → Publication Preview r2;
4. freeze a new exact head;
5. rerun Core CI + pipeline contracts;
6. rerun the complete six-point audit **plus explicit Human Gate continuation/revision coverage** from zero;
7. only then return PR #447 to Human full-candidate review.

## Current maintenance design

The pre-RVF-015 bridge candidate scope contains bridge/authority changes, not a duplicate Retrospective implementation:

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

Current pre-repair Actions surface is exactly seven workflows. A new workflow is not required merely to solve HG-001/HG-002: prefer extending the existing enum-constrained bridge with deterministic recording/revision mechanics unless a separate Actions-specific advantage is demonstrated.

## Diagnostic CI evidence before the invalidated freeze

Diagnostic runs are not final acceptance evidence if the candidate tree changes afterward.

- head `6ba6748a4e06e63a24ddac34173a7a2534b7e370`: Core v2 CI PASS and Pipeline contract tests PASS;
- head `4088bcfc63aafa440f1966c5393f6aae912eee30`: E2E fixture FAIL before bridge execution because sparse checkout lacked `sources/`;
- head `08328d8babcb60b00be22d87a69289fd0e751ace`: Core v2 CI PASS after fixture correction;
- frozen head `a65e714b711e76006318a14b252aa0a4e9727b4f`: Core v2 CI PASS and Pipeline contract tests PASS; PR merge-candidate tree matched the exact frozen head tree.

All are now historical/diagnostic evidence because RVF-015 requires a new candidate tree.

## PFB-013 status

`PARTIALLY EXERCISED / NOT PASSED`

Real cold-start Weekly, SP001/LONGFORM, representative Retrospective and Foundations-guided validation remain required after reviewed unchanged integration.

## PFB-014 status

`IMPLEMENTED PARTIALLY / PRE-APPROVAL FULL-SYSTEM AUDIT FAILED / REPAIR REQUIRED`

The current bridge successfully addresses initialization and ordinary stage execution, with reviewed-main preflight, Profile-bound writes, immutable requests, no arbitrary executable surface, stale-state refusal, deterministic result ownership by Core, no deterministic-review impersonation, no recursive bot chain, exact provenance, direct-local preference, and Weekly/configured-Retrospective/Thematic support.

It does **not** yet close the connector-only execution gap across Human Gate approval/revision boundaries. Do not close PFB-014 and do not merge PR #447 until RVF-015 is repaired and reaudited.

## Next actions after the pre-approval full-system audit

```text
keep PR #447 in Draft
-> design the narrow HG-001 Human-decision recording bridge operations using existing canonical approval functions
-> design HG-002 fail-closed revision/invalidation semantics for Architecture Review and Publication Preview
-> update Core authority + execution-record policy + bridge request contract + regression tests
-> record repair in this worklog
-> freeze a new candidate head
-> exact-head Core CI + pipeline contract tests
-> complete six-point audit from point 1
-> explicitly audit Human Gate approve + revise/r2 paths
-> any required tree change invalidates and restarts audit
-> only after PASS: record result outside candidate tree and mark PR #447 ready for Human full-candidate review
```

W33/SP001 production validation remains paused. Do not restart those editions until the shared Core maintenance candidate is reviewed and integrated unchanged.

Repository reality and canonical Production State, once created, outrank this human-readable summary.
