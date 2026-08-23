# Survey Production Core v2 — agent session bootstrap

Status: `REDESIGN IMPLEMENTATION CANDIDATE`  
Applies to: Weekly, Retrospective Period, standalone Thematic, and guided Special series work  
Primary operator: **ChatGPT**

## 1. Minimal user contract and stop discipline

A user may start or resume production with only a target and desired stopping Human Gate, for example:

```text
2026-W35をArchitecture Reviewまで編纂してください
Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください
2025-H2をPublication Previewまで進めてください
```

That instruction is sufficient. ChatGPT reconstructs production mechanics from repository authority instead of asking the user to restate manifest paths, search tactics, stage order, quality rules or release mechanics.

After the request, **continue autonomously without routine confirmation prompts**. A production session may pause only for:

1. `ARCHITECTURE_REVIEW` Human Gate;
2. exact-byte `PUBLICATION_PREVIEW` Human Gate;
3. a genuine `EXCEPTION_GATE_REQUIRED` condition requiring Owner judgment;
4. the permitted Human-mediated Grok Drive task-file path handoff;
5. a recorded shared-Core defect that makes correct production impossible under the reviewed Core.

Grok handoff is operational transport, not editorial approval or a third Human Gate. Once the expected Grok result is present, import it and resume automatically.

Initialization, Source Intake, search expansion, Screening, Evidence, Completeness/materiality, Candidate Selection, Architecture preparation, reader-facing authorship, deterministic QA, ChatGPT semantic/editorial review, PDF build, ChatGPT visual review, Freeze preparation, transient retry and edition-local repair are **not stop points**. Continue immediately unless a Human/Exception Gate or blocking shared-Core defect is reached.

## 2. Authority order at session start

Before changing an edition, read current reviewed `main` and at minimum:

1. `AGENTS.md`;
2. `docs/survey-production-core-v2-authority.md`;
3. this file;
4. `docs/survey-production-core-v2-issue-prevention-checklist.md`;
5. `docs/survey-production-core-v2-x-source-intake.md`;
6. `docs/survey-production-core-v2-execution-record-policy.md`;
7. the applicable Profile/period/thematic/series guide;
8. existing canonical Production Profile/State and edition execution index, if any.

For Core-maintenance implementation/review work, also read the redesign authority and `docs/survey-production-core-v2-final-audit-rule.md`.

Repository state outranks chat history. A new production conversation must be able to resume from repository state alone.

## 3. Production versus Core-maintenance boundary

Production sessions own edition-local work. Core-maintenance sessions own shared implementation.

During an edition run, do not author generic changes under:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

If a shared-Core defect is observed:

```text
record symptom / reproduction / impact
-> classify SHARED_CORE_DEFECT
-> record sources/<issue>/execution/defects/<id>.md
-> continue only if a semantically safe edition-local workaround exists
-> otherwise mark BLOCKED_CORE_DEFECT and stop the edition
-> repair Core separately through normal review/CI
```

A production run that edits shared Core to make itself pass is not valid evidence that the reviewed Core worked.

A newer Core revision may be consumed only after it is separately reviewed and integrated. Revalidate affected accepted boundaries and record the new integrated revision; do not author the generic repair in the edition conversation.

## 4. Resolve targets without user ceremony

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

Custom bounded periods may use a repository-owned spec. A bounded Period cannot initialize until its period end has passed. ChatGPT records an explicit X `REQUIRED` / `NOT_REQUIRED` decision with rationale.

### Standalone Thematic

Resolve research scope from canonical thematic planning authority. If a machine-readable scope file is absent, ChatGPT materializes it from that authority; this is internal work, not a Human Gate.

Thematic X applicability is a ChatGPT research judgment based on whether community/adoption/implementation signal is material to the question.

### Guided series / Generative AI Foundations

For `Generative AI Foundationsの次巻`, read `docs/generative-ai-foundations-special-series.md`, inspect completed/in-progress repository evidence, resolve the next volume, and materialize that volume's Thematic scope from the living series authority.

Do not ask for a volume number that repository authority can determine. Do not build a parallel machine Series engine solely for bootstrap convenience.

Each volume uses normal `THEMATIC` + applicable Publication Profile contracts. When X is material, use the dedicated Foundations Drive category.

## 5. Initialization, resume and execution record

The start request authorizes deterministic initialization and canonical work-branch/state creation. Initialization is not a Human Gate.

Canonical resume validation:

```text
python scripts/survey_agent_control_v2.py validate-state --state <source_root>/production-state.json
```

After State, read or create:

```text
<source_root>/execution/index.md
<source_root>/execution/sessions/<session-id>.md
```

Follow `docs/survey-production-core-v2-execution-record-policy.md`. Log material actions/decisions and authority pointers, not every tool invocation.

At session close, persist the exact end state, next action, relevant candidate/Grok/Human Gate identity, and any defect/deviation. This logging is internal production work and never requires routine approval.

## 6. Source Intake and Grok/X Google Drive handoff

Read `docs/survey-production-core-v2-x-source-intake.md` before Discovery Acceptance.

### 6.1 Applicability

- `WEEKLY`: `REQUIRED`.
- `RETROSPECTIVE_PERIOD`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- `THEMATIC`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- Foundations: use the dedicated series Drive category when required.

`NOT_REQUIRED` is a substantive research judgment, not a shortcut.

### 6.2 One self-contained Drive task

For each required run, define purpose, research questions, time/scope constraints, expected output format, stable run ID and expected result filename. Prepare one self-contained task file:

```text
Grok_X_SourseIntake/<category>/<edition>/<run-id>/grok-task.md
```

The repository-side X manifest must bind the exact task bytes/hash and expected Drive location. Account-specific Drive IDs/URLs are operational metadata and must not be committed when they contain private identity.

### 6.3 Human-mediated path handoff

Give the Human only the exact Google Drive **task-file path/reference**. The Human gives that path/reference to Grok. The Human is not expected to copy/paste instruction or prompt contents.

Do **not** search for, install, discover or configure a Grok connector. Connector absence is not a missing dependency or Exception Gate.

Grok reads `grok-task.md` and writes the instructed result into the same run folder. If the result is not present yet, Source Intake is incomplete; do not reinterpret that as Human approval or Core failure.

### 6.4 Import and disposition

Read the returned Markdown and import its **exact bytes** into repository Raw, for example:

```text
<source_root>/external/x/<run-id>/raw/<actual-drive-filename>.md
```

Then record either:

```text
DISCOVERY_RECORDED
NO_MATERIAL_DISCOVERY
```

Material results link Discovery records to imported Raw. Non-material results require rationale. X remains discovery/community signal; technical claims still require normal authoritative Evidence verification.

After import/disposition, resume automatically toward the requested Gate.

## 7. Research and Architecture loop

ChatGPT owns research/editorial judgment. Deterministic helpers validate exact structures/invariants; they do not decide what the edition should say.

Normal internal progression:

```text
Profile + State + guide/checklist
-> Source Intake and research expansion
-> Screening
-> Evidence verification
-> materiality/completeness closure
-> Candidate Selection
-> Architecture
-> exact stage validation
-> compact Stage Checkpoint
-> next lifecycle state
```

Repair edition-local research/evidence/architecture findings autonomously. If the required repair would change shared Core, use the responsibility rule in §3 instead.

Before a Stage Checkpoint is adopted, run the exact intended artifact set through `scripts/survey_stage_validation_v2.py` and include the exact `CORE_STAGE_CONTRACT` result.

Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery is compatibility/audit code, not the canonical hot path.

## 8. Human Gate 1 — Architecture Review

The first normal stop is:

```text
lifecycle_state = ARCHITECTURE_ESTABLISHED
terminal_reason = HUMAN_GATE_REACHED
next_action = ARCHITECTURE_REVIEW
```

Present the exact Architecture package, research limitations and material unresolved questions. Never infer approval from silence.

After explicit approval, record exact Architecture approval and continue autonomously toward Publication Preview unless the user explicitly requested to stop after Architecture approval.

## 9. Reader-facing authorship and QA

After Architecture approval, internal Draft Package/Result and Synthesis artifacts may support ChatGPT's work, but they are not publication prose and are never a legal fallback source for publication assembly.

ChatGPT explicitly authors canonical reader-facing files under the bound `survey_root`, normally:

```text
<survey_root>/main.tex
<survey_root>/references.bib
```

Create a Reader Manuscript Manifest binding the exact reader source and complete Architecture must-cover mapping.

For one exact source/PDF revision, complete these separate QA layers:

1. **Deterministic QA** — Quality Bundle containing only applicable deterministic checks and exact build/source/PDF authority.
2. **Semantic/Editorial QA** — ChatGPT review record of the exact manuscript/source/PDF, including Publication Boundary, Architecture content fidelity and Profile-specific semantics.
3. **Visual QA** — ChatGPT visual review record of the exact rendered PDF and applicable Publication Profile visual checks.

If any layer finds a normal edition-local issue, revise the reader-facing source, rebuild the PDF, invalidate stale QA records and rerun all affected layers. Do not patch shared renderer/Core code in the production session.

## 10. Human Gate 2 — Publication Preview

Finalize one Publication Candidate only after the three QA layers pass on the same source/PDF bytes.

The Candidate atomically binds:

- Reader Manuscript;
- exact source;
- exact PDF + page count;
- deterministic Quality Bundle;
- Semantic/Editorial Review;
- Visual Review.

At `RELEASE_CANDIDATE`, stop for Human approval of that exact Candidate/PDF identity. Rebuilt or changed bytes require a new candidate and new review.

## 11. Freeze and Release

After Publication Preview approval, continue without another routine Human Gate:

1. verify the approval binds the exact already-reviewed Candidate/PDF;
2. build Freeze Record and Release Manifest from that Candidate and approval;
3. transition to `FROZEN` after exact stage validation;
4. merge frozen production changes through the normal reviewed repository path;
5. use the dedicated mechanical Release workflow against current `main`;
6. create/reconcile the issue-only GitHub Release;
7. verify released asset SHA-256/byte count;
8. record Merge Verification, Release Record and compact `FROZEN -> RELEASED` checkpoint.

Do **not** insert a second post-approval semantic/visual quality gate. Human approval is followed by exact-byte integrity work, not new editorial judgment.

Public identity derives from the exact Production Profile `paths.survey_root` basename. Release reconciliation remains fail-closed and idempotent.

## 12. GitHub Actions responsibility

GitHub Actions are retained where they add independent mechanical value:

- CI/regression;
- reproducible/pinned PDF build;
- deterministic checks that benefit from clean-environment execution;
- exact-byte preview export where needed;
- credential-isolated Freeze/Release/reconciliation.

Do not use Actions as the normal Screening/Evidence/Selection/Drafting/Semantic Revision/Visual Repair author. ChatGPT performs those decisions directly and records the resulting edition artifacts.

If a legacy production-mutation workflow still exists in the repository, its existence does not make it canonical. Follow the current Core contract and workflow responsibility inventory.

## 13. Exception Gate

Use an Exception Gate only when safe continuation genuinely needs Owner judgment, including unresolved scope ambiguity, irreconstructible accepted authority, incompatible accepted-contract migration, changed already-approved bytes, or frozen/release identity divergence.

Do not stop for ordinary search refinement, weak-source replacement, local QA failure, wording/layout repair, CI retry, Grok path handoff, or a defect that is clearly edition-local.

A shared-Core defect that makes production impossible is recorded as `BLOCKED_CORE_DEFECT`; repair occurs in the separate Core-maintenance flow. Use an Owner Exception Gate only when Owner judgment—not merely Core engineering—is actually required.

## 14. Session handoff

If the conversation ends before the requested Gate, update the edition execution record with:

```text
issue_id / resolved target
work_branch
Production State path + SHA-256
lifecycle_state
next_action / stop reason
latest Stage Checkpoint
latest execution session record
X task-file path/result disposition if active
open Human/Exception Gate if any
shared-Core defect pointer if any
exact candidate/PDF SHA if applicable
```

A later session validates repository state and continues rather than replaying completed work or asking the user to reconstruct it.

## 15. Core-v2 candidate review rule

Core-maintenance candidates follow `docs/survey-production-core-v2-final-audit-rule.md`:

```text
complete every intended code/config/schema/workflow/test/doc/Finding/Repair-Set change
-> obtain required regression/CI evidence on one head
-> synchronize all Core authority/docs
-> freeze that candidate head SHA
-> audit all six acceptance priorities from zero on that exact head
-> make no candidate-tree changes during the audit
```

If any finding requires repository mutation, invalidate the audit, repair Core, freeze a new head and rerun all six points from point 1. Final PASS is PR/Human-review metadata bound to the exact audited SHA.
