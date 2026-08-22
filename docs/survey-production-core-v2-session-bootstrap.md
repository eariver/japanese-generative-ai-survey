# Survey Production Core v2 — agent session bootstrap

Status: `PRE-MERGE CANONICAL CANDIDATE / AUDIT-STABLE PRE-AUDIT`  
Applies to: Weekly, Retrospective Period, standalone Thematic, and guided Special series work  
Primary operator: **ChatGPT**

## 1. Minimal user contract and stop discipline

A user may start or resume production with only a target and desired stopping Human Gate, for example:

```text
2026-W35をArchitecture Reviewまで編纂してください
Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください
2025-H2をPublication Previewまで進めてください
```

That instruction is sufficient. ChatGPT reconstructs pipeline mechanics from repository authority instead of asking the user to restate manifest paths, search tactics, stage order, quality rules or release mechanics.

After the request, **continue autonomously without routine confirmation prompts**. A production session may pause only for:

1. `ARCHITECTURE_REVIEW` Human Gate;
2. exact-byte `PUBLICATION_PREVIEW` Human Gate;
3. a genuine `EXCEPTION_GATE_REQUIRED` condition requiring Owner judgment;
4. unavoidable manual Grok instruction/result transport when the external Grok execution cannot be performed directly.

The fourth case is an operational transport boundary, not editorial approval and not a third Human Gate. Once the expected Grok result is present in the configured Google Drive run folder, import it and resume automatically.

Initialization, Source Intake, search expansion, Screening, Evidence, Completeness/materiality, Candidate Selection, Architecture preparation, drafting, synthesis, deterministic QA, ChatGPT semantic/visual review, Freeze preparation, CI retry and internally repairable defects are **not stop points**. Do not ask “continue?” between those stages.

## 2. Authority order at session start

Before changing an edition, read current `main` and at minimum:

1. `AGENTS.md`;
2. `docs/survey-production-core-v2-authority.md`;
3. this file;
4. `docs/survey-production-core-v2-issue-prevention-checklist.md`;
5. `docs/survey-production-core-v2-x-source-intake.md`;
6. the applicable Profile/period/thematic/series guide;
7. existing canonical Production Profile/State and stage artifacts, if any.

For Core-v2 implementation/review work, also read `docs/survey-production-core-v2-final-audit-rule.md`.

Repository state outranks chat history. A new session must be able to resume from repository state alone.

While PR #310 is unmerged, Core v2 production remains disabled: current `main` is still production source of truth and W33/SP001 must not be initialized from the improvement branch.

## 3. Resolve targets without user ceremony

### Weekly

For an explicit issue such as `2026-W35`, use the configured Weekly cutoff calendar. The issue must have completed its editorial cutoff. Initialize with the generic Weekly Profile and do not add issue-specific Core logic.

```text
python scripts/survey_production_v2.py init-weekly --issue-id 2026-W35 --target-gate ARCHITECTURE_REVIEW
```

If Profile/State already exists, resume it. Weekly Grok/X intake is required by Profile and cannot be bypassed because other collectors found many records.

### Retrospective Period

Monthly, half-year and annual configured Specials use one `RETROSPECTIVE_PERIOD` Profile through `scripts/survey_period_v2.py`:

```text
python scripts/survey_period_v2.py plan --special-slug 2025-H2
python scripts/survey_period_v2.py initialize --special-slug 2025-H2 --target-gate ARCHITECTURE_REVIEW
```

Custom bounded periods may use a repository-owned spec. A bounded Period cannot initialize until its period end has passed.

For X, ChatGPT records an explicit `REQUIRED` / `NOT_REQUIRED` decision with rationale.

### Standalone Thematic

Resolve research scope from canonical thematic planning authority. For SP001, the Pilot points to TS-001 in `docs/thematic-special-backlog.md`; detailed scope is not duplicated into Pilot configuration.

If a machine-readable scope file is absent, ChatGPT materializes it from planning authority. That is an internal action, not a Human Gate.

For Pilot planning:

```text
python scripts/survey_pilot_bootstrap_v2.py plan --pilot W33
python scripts/survey_pilot_bootstrap_v2.py plan --pilot SP001
```

`SP001` may return `MATERIALIZE_SCOPE`; perform that action and replan automatically.

For X, ChatGPT explicitly decides whether community/adoption/implementation signal is material to the thematic question.

### Guided series / Generative AI Foundations

For `Generative AI Foundationsの次巻`, read `docs/generative-ai-foundations-special-series.md`, inspect completed/in-progress repository evidence, resolve the next volume, and materialize that volume's Thematic scope from the living series authority.

Do not ask the user for a volume number that repository authority can determine. Do not create a parallel machine Series engine solely for bootstrap convenience.

If multiple next volumes are genuinely equally valid and repository authority cannot decide, use an Exception Gate.

Each Foundations volume uses a normal `THEMATIC` Production Profile. If X is material, use `series_context = GENERATIVE_AI_FOUNDATIONS` so Drive handoff uses the dedicated category.

## 4. Initialization, resume and reviewed tool upgrades

The start request authorizes deterministic initialization and canonical work-branch creation. Initialization is not a Human Gate.

Initialization writes immutable launch provenance: Profile, State, issue/path identity and initialization implementation/contract identity.

Initialization implementation identity is historical provenance, not a permanent runtime pin. Later stages may use newer reviewed generic tooling only after the repair is actually integrated into the edition work branch.

Canonical upgrade loop:

```text
generic repair reviewed/merged on main
-> integrate it into edition work branch
-> validate State with integrated toolchain
-> revalidate/migrate only affected accepted boundaries
-> execute next stage from integrated branch head
-> record actual head + current contract in next Stage Checkpoint
-> continue automatically
```

Canonical resume validation:

```text
python scripts/survey_agent_control_v2.py validate-state --state <source_root>/production-state.json
```

Do not use legacy `survey_production_v2.py validate-state` as the canonical resume decision. Legacy Screening/Evidence helpers that retain historical pin checks may run through:

```text
python scripts/survey_agent_tool_v2.py <allowlisted screening/evidence helper arguments>
```

## 5. Source Intake and Grok/X Google Drive handoff

Read `docs/survey-production-core-v2-x-source-intake.md` before accepting Discovery.

### 5.1 Applicability

- `WEEKLY`: `REQUIRED`.
- `RETROSPECTIVE_PERIOD`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- `THEMATIC`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- Foundations: `THEMATIC` plus `series_context = GENERATIVE_AI_FOUNDATIONS` when required.

`NOT_REQUIRED` is a substantive research judgment, not a shortcut.

### 5.2 Build Grok run package

For each required run define purpose, research questions, coverage focus, time scope, stable run ID and expected result filename, then build:

```text
python scripts/survey_x_intake_v2.py build \
  --profile <source_root>/production-profile.json \
  --spec <run-spec.json>
```

This creates the X manifest plus exact Grok instruction/prompt under `<source_root>/external/x/<run-id>/`.

### 5.3 Provision Google Drive target

Resolve the connected Drive root named exactly:

`Grok_X_SourseIntake`

Persistent categories:

```text
Weekly
Retrospective_Special
Thematic_Special
Generative_AI_Foundations
```

Create the exact run folder before Grok runs:

```text
Grok_X_SourseIntake/<category>/<edition-folder>/<run-id>/
```

Do not commit account-specific Drive IDs/URLs.

### 5.4 External collection boundary

If Grok can be invoked directly, execute the collection and continue. If not, give the Human the exact generated instruction/prompt and Drive path for manual transport. **Do not ask for any additional approval or unrelated confirmation.**

If the result is absent, keep State in Source Intake with `AWAITING_GROK`. This is not a Human Gate. If the result already exists, continue immediately.

### 5.5 Import and disposition

Read the returned Drive Markdown and copy the **exact bytes** into repository Raw, preferably:

```text
<source_root>/external/x/<run-id>/raw/<actual-drive-filename>.md
```

Then record either:

```text
DISCOVERY_RECORDED
NO_MATERIAL_DISCOVERY
```

Material results must name Discovery record(s) that bind the imported Raw. Non-material results need a non-empty rationale. Technical facts still require normal authoritative Evidence verification.

### 5.6 Discovery Acceptance

Discovery Acceptance binds the completed X Source Intake manifest SHA. `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` cannot pass when Weekly skipped X, a required run is still awaiting output, imported Raw drifted, a result lacks disposition, or a named Discovery does not bind the imported Raw.

Conventional collectors, direct ChatGPT web research and Grok/X are all Source Intake surfaces. Collector success/count never proves completeness.

## 6. Autonomous research/editorial loop

For each internal stage:

```text
read Profile + State + applicable guide/checklist
-> plan work appropriate to the actual edition
-> perform applicable Source Intake
-> produce/update canonical artifacts
-> run genuinely applicable deterministic checks
-> perform required ChatGPT research/editorial/visual reviews
-> repair ordinary findings and re-check
-> validate exact intended stage artifacts with scripts/survey_stage_validation_v2.py
-> include exact CORE_STAGE_CONTRACT in checkpoint review set
-> write one compact Stage Checkpoint
-> advance Production State exactly one lifecycle step
-> continue immediately unless a Human/Exception Gate is reached
```

The compact checkpoint lives under:

```text
<source_root>/orchestration/v2/checkpoints/<FROM_STATE>.json
```

It binds lifecycle transition, canonical artifact hashes, exact semantic validation, applicable ChatGPT review, implementation commit, current contract identity and readiness summary.

A canonical filename or ChatGPT PASS statement is not enough. Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery remains compatibility/audit code, not the hot path.

A semantic/visual or deterministic finding is normally repaired and re-run autonomously. Do not stop merely because a check failed when a safe local repair exists.

## 7. Human Gates

### Human Gate 1 — Architecture Review

The first normal stop is at:

```text
lifecycle_state = ARCHITECTURE_ESTABLISHED
terminal_reason = HUMAN_GATE_REACHED
next_action = ARCHITECTURE_REVIEW
```

Present the exact Architecture package, research limitations and material unresolved questions. Never infer approval from silence.

After explicit approval, record exact Architecture approval and continue autonomously toward Publication Preview unless the user explicitly requested to stop after Architecture approval.

### Human Gate 2 — Publication Preview

After Architecture approval, continue through drafting/synthesis, deterministic validation, semantic review, rendering and agent visual review.

Quality rows are `DETERMINISTIC`, `AGENT_SEMANTIC` or `AGENT_VISUAL`; applicability derives from the exact Production Profile.

At `RELEASE_CANDIDATE`, stop for approval of one exact Publication Candidate/PDF byte identity. A rebuilt or similar PDF is not the approved artifact.

## 8. Freeze and Release

After Publication Preview approval, continue without another routine Human Gate:

1. record exact approved-PDF visual review;
2. build Freeze Record and Release Manifest with `scripts/survey_profiled_freeze_v2.py`;
3. transition to `FROZEN` after exact stage validation;
4. merge frozen production changes through the normal reviewed repository path;
5. run dedicated Release workflow against current `main`;
6. create/reconcile issue-only GitHub Release;
7. recheck released asset SHA-256/byte count;
8. record Merge Verification, Release Record and compact `FROZEN -> RELEASED` checkpoint.

Public identity derives from exact Production Profile `paths.survey_root` basename. Release reconciliation remains fail-closed and idempotent.

## 9. Exception Gate

Use an Exception Gate only when safe continuation genuinely needs Owner judgment, including unresolved scope ambiguity, irreconstructible partial initialization, inability to establish accepted Raw/external artifact identity, incompatible accepted-contract migration, changed already-approved bytes, or frozen/release identity divergence.

Do **not** stop for ordinary search refinement, weak-source replacement, local QA failure, CI retry, wording/layout repair, ordinary Grok result transport, or a generic defect that can be repaired safely.

A missing Grok result is not an Exception Gate when task and Drive target are valid; it is incomplete Source Intake.

## 10. Session handoff

If the conversation ends before the requested Gate, persist enough repository state for another session to resume:

```text
issue_id / resolved target
work_branch
Production State path + SHA-256
lifecycle_state
next_action / terminal_reason
latest Stage Checkpoint
X Source Intake manifest/status if active
pending Grok run-id + Drive path if AWAITING_GROK
open Human/Exception Gate if any
known research limitations
```

A later session validates repository state and **continues**, rather than replaying already completed work or asking the user to restate it.

## 11. Core-v2 candidate review rule

For Survey Production Core v2 changes, follow `docs/survey-production-core-v2-final-audit-rule.md`:

```text
complete every code/config/schema/workflow/test/doc/Finding/Repair-Set change
-> obtain all five CI cross-regression families green on one head
-> freeze that candidate head SHA
-> audit all six acceptance priorities from zero on that exact head
-> make no candidate-tree changes during the audit
```

The six points are Weekly viability, Special viability, generality, recurrence prevention, control proportionality, and **autonomous progression / stop discipline**.

If any finding requires a repository change, invalidate the entire audit, complete repairs, freeze a new head and rerun **all six points from point 1**. The final PASS is recorded against the exact audited SHA in PR/Human-review metadata rather than committed into the audited tree.
