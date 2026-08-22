# Survey Production Core v2 — Pilot session bootstrap

Status: `PRE-PILOT CANONICAL BOOTSTRAP CANDIDATE`  
Applies to: W33 and SP001 first production validation  
Machine authority: `config/survey-production-v2-pilots.json` + `scripts/survey_pilot_bootstrap_v2.py`

## 1. Purpose and authority boundary

This document makes the first Core v2 production validations resumable across sessions without relying on chat history. Repository state is the authority for whether a Pilot is unstarted, resumable, at a Human Gate, at an Exception Gate, frozen, or released.

`docs/special-session-bootstrap.md` remains the bootstrap contract for the legacy Special pipeline. It does **not** define W33/SP001 Core v2 launch inputs or Core v2 lifecycle recovery.

The machine-readable W33/SP001 launch identities live in `config/survey-production-v2-pilots.json` and are schema-validated by `schemas/pilot-bootstrap-v2.schema.json`. Do not copy launch scope out of tests or prior conversations.

## 2. Precondition: do not start from the improvement branch

W33/SP001 external production is prohibited until the coherent Survey Production Core v2 candidate has completed full-candidate Human review and has been explicitly merged to `main`.

Before initialization, verify that current `main` contains:

- `config/survey-production-v2.json`;
- `config/survey-production-v2-pilots.json`;
- `scripts/survey_pilot_bootstrap_v2.py`;
- `.github/workflows/survey-production-v2-control.yml`;
- `.github/workflows/survey-production-v2-release.yml`;
- `.github/workflows/assistant-control-v2.yml`.

If those authorities are not on current `main`, stop. Do not initialize a Pilot from `refactor/survey-production-core-v2` or another unmerged implementation branch.

## 3. Canonical session entry

Every W33/SP001 production or continuation session begins with a side-effect-free plan from the current repository checkout:

```text
python scripts/survey_pilot_bootstrap_v2.py plan --pilot W33
python scripts/survey_pilot_bootstrap_v2.py plan --pilot SP001
```

An offset-aware `--recorded-at` may be supplied for deterministic testing. For actual first initialization, omit it or pass the actual session time.

The planner validates the Pilot registry and materializes the exact Production Profile without writing Production State. It returns one of three operations:

- `INITIALIZE`: neither canonical Production Profile nor Production State exists;
- `RESUME`: both exist and their immutable Pilot identity is valid;
- `EXCEPTION_GATE_REQUIRED`: only one of Profile/State exists, or another fail-closed inconsistency prevents safe continuation.

A planning command must never create `sources/2026-W33/production-state.json` or `sources/SP001/production-state.json`.

## 4. W33 identity

W33 is the **Weekly Profile First Production Validation**.

Its registry authority fixes:

```text
pilot_id: W33
issue_id: 2026-W33
research_profile: WEEKLY
publication_profile: WEEKLY_MAGAZINE
source_root: sources/2026-W33
survey_root: surveys/weekly/2026-W33
work_branch: weekly/2026-W33-v2-work
editorial cutoff: 2026-08-14T18:00:00-04:00
first requested Human Gate: ARCHITECTURE_REVIEW
```

The issue ID determines the completed Weekly editorial window. A later session date must not silently move W33 to W34 or another cutoff.

Legacy W33 artifacts are comparison/provenance fixtures only. They are not a migration target and are not acceptance authority for Core v2.

## 5. SP001 identity

SP001 is the **Thematic Profile First Production Validation**.

Its registry authority fixes:

```text
pilot_id: SP001
issue_id: SP001
research_profile: THEMATIC
publication_profile: LONGFORM_SPECIAL
source_root: sources/SP001
survey_root: surveys/special/SP001
work_branch: special/SP001-v2-work
temporal mode: OPEN_HISTORY_AS_OF
as_of policy: SET_AT_INITIALIZATION
first requested Human Gate: ARCHITECTURE_REVIEW
```

The thematic question, dimensions and initial obligations are defined only by `config/survey-production-v2-pilots.json`.

`SP001` `as_of` is set exactly once at first initialization. A later continuation session must read the existing Production Profile and preserve that original `as_of`; it must not rematerialize the thematic horizon from the new session time.

## 6. Initialization

When the planner returns `INITIALIZE`, create the exact `profile.paths.work_branch` from the reviewed Core v2 `main`, checkout that branch, and run:

```text
python scripts/survey_pilot_bootstrap_v2.py initialize --pilot <W33|SP001>
python scripts/survey_production_v2.py validate-state --state <source_root>/production-state.json
```

Initialization is deterministic control-state creation, not a Human Gate. A user request to start an authorized Pilot permits this initialization. It does not approve Architecture, Publication Preview, Freeze, or Release content.

Commit the generated `production-profile.json` and `production-state.json` on the canonical work branch before doing research work. Never initialize the same Pilot twice. The Core initializer is destructive-write protected and the bootstrap driver refuses any state other than cleanly uninitialized.

If branch or file state implies an ambiguous partial initialization, use an Exception Gate rather than deleting or recreating authority files ad hoc.

## 7. Resume

When the planner returns `RESUME`:

1. read the returned existing Production Profile and Production State;
2. use `profile.paths.work_branch` as the only production work branch;
3. validate the existing State against its pinned implementation/contract before changing stage artifacts;
4. inspect `lifecycle_state`, `next_action`, `terminal_reason`, checkpoint provenance, Human Gate provenance, and `orchestration/v2/` records;
5. continue from the current state only. Never replay a completed stage merely because a prior chat session ended.

For SP001, the existing Profile's initialization-time `as_of` is authoritative. For W33, the fixed completed issue window is authoritative.

## 8. One-stage production adoption

All executable Core v2 stages require a canonical Stage Handoff. The production session prepares the stage's explicit external/model outputs and a schema-valid canonical request at:

```text
<source_root>/orchestration/v2/handoff-requests/<LIFECYCLE_STATE>.json
```

The request must name every explicit input/output path and must match `schemas/stage-handoff-request-v2.schema.json` and the current stage output contract. Do not use a "latest artifact" search or an unpinned external run.

After committing the request and its referenced stage artifacts to the canonical work branch, compute the exact request SHA-256 and dispatch **the `main` copy** of `survey-production-v2-control.yml` with:

```text
operation = adopt-stage
issue_id = <Production State issue_id>
work_branch = <Production Profile work_branch>
request_sha256 = <exact canonical request SHA-256>
human_gate_authorized = false
```

The workflow must:

- require the dispatched main workflow bytes to equal the State-pinned worktree workflow;
- execute the worktree-pinned Core implementation;
- build the exact canonical Stage Handoff from the request;
- execute at most one deterministic stage;
- run the implementation-controlled semantic validator;
- create/pin Validation Attestations and State transition provenance;
- if that one transition reaches a terminal Human/Exception/Complete plan, persist the exact terminal Action Spec without executing the next deterministic stage;
- commit all resulting control records to the canonical work branch.

`FROZEN` is not adoptable through this generic operation. Release uses the dedicated release workflow.

## 9. Architecture Review Human Gate

After the Architecture stage is adopted, canonical control must leave State at:

```text
lifecycle_state = ARCHITECTURE_ESTABLISHED
terminal_reason = HUMAN_GATE_REACHED
next_action = ARCHITECTURE_REVIEW
human_gates.architecture_review = pending
```

The same control commit must contain the current `HUMAN_GATE` Action Spec bound to the exact reviewed inputs.

Present the repository-backed Architecture Review package to the human reviewer. Do not infer approval from silence, prior editions, or a previous chat.

Only after explicit approval dispatch `survey-production-v2-control.yml` with:

```text
operation = approve-architecture
issue_id = <issue>
work_branch = <canonical work branch>
human_gate_authorized = true
reviewed_by = <explicit reviewer identity>
reviewed_at = <offset-aware review time>
review_reference = <durable review reference>
```

The workflow resolves and consumes the exact current Architecture Human Gate Action Spec and writes an independent Approval Record. Architecture proposal bytes remain immutable.

## 10. Publication Preview Human Gate

After Architecture approval, continue one stage at a time through Drafting/Synthesis, semantic/quality validation, and Publication Candidate creation.

When State reaches `RELEASE_CANDIDATE`, the same rule applies: the control commit must persist the current `human:publication-preview` Action Spec. The exact Publication Candidate binds the PDF durable authority and source/quality identities.

Do not approve a rebuilt or visually similar PDF. Publication Preview approval is exact-byte authority.

Only after explicit human approval dispatch:

```text
operation = approve-publication-preview
issue_id = <issue>
work_branch = <canonical work branch>
human_gate_authorized = true
reviewed_by = <explicit reviewer identity>
reviewed_at = <offset-aware review time>
review_reference = <durable review reference>
```

## 11. Freeze, merge verification and Release

After Publication Preview approval, prepare/adopt the Freeze stage through the canonical Stage Handoff path. The Freeze stage must produce the exact Visual Review Record, Freeze Record and Release Manifest and transition State to `FROZEN`.

Before public Release, the frozen production changes must be merged through the reviewed repository path so that current `main` contains the exact FROZEN Production State and Release Manifest. Do not dispatch Release against an unmerged work-branch-only freeze.

Then dispatch `survey-production-v2-release.yml` using the exact authorized values from current `main`:

```text
issue_id = <issue>
production_state_sha256 = <SHA-256 of current main Production State>
release_manifest_sha256 = <SHA-256 of current main Release Manifest>
confirmation = release:<issue>
```

The Release workflow revalidates State-pinned implementation identity, Publication Candidate authority, durable PDF bytes, merge identity and release identity before side effects.

If an issue-only GitHub Release with the same identity already exists after a partial prior attempt, reconciliation is allowed only when tag/title/target and released asset SHA-256/byte count exactly match the authorized Release Manifest/Candidate. Divergence fails closed.

## 12. Exception Gate rules

Use an Exception Gate instead of improvising when any of the following occurs:

- Pilot registry target cannot be resolved;
- only one of canonical Profile/State exists;
- existing Profile differs from fixed registry identity;
- State semantic/provenance validation fails;
- State-pinned implementation differs from executable control roots;
- canonical Stage Handoff Request cannot represent the actual stage inputs/outputs;
- external artifact identity or accepted Raw byte identity cannot be proven;
- Human Gate reviewed bytes differ from the current Action Spec;
- frozen/release exact-byte identity diverges;
- recovery would require changing editorial scope or manufacturing a Human approval.

Deterministic CI/network/retry failures are not automatically Human Gates. Recover only within the action's configured retry/idempotency authority.

## 13. Session handoff rule

At the end of any production session, repository state must be enough for the next session. Commit all authoritative work-branch records before stopping and report the current:

```text
Pilot / issue_id
work_branch
Production State SHA-256
lifecycle_state
next_action / terminal_reason
latest canonical Action Spec
open Human/Exception Gate, if any
```

A later session must start again with `survey_pilot_bootstrap_v2.py plan --pilot ...` and reconstruct continuation from repository state. Conversation history is supplementary context only.
