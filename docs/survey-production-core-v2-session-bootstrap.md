# Survey Production Core v2 — agent session bootstrap

Status: `REDESIGN + HUMAN-GATE ROUNDTRIP + REVIEW-COMMIT PROVENANCE MAINTENANCE CANDIDATE`  
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
5. a recorded shared-Core defect that makes correct production impossible under reviewed Core.

Before presenting either normal Human Gate, commit the exact current Production State and every configured Gate input that the Human will review. The Human decision binds that exact repository commit, not an uncommitted working-tree view. Canonical `survey_human_gate_v2` proves the named reviewed commit exists and contains those exact State/Gate-input bytes before recording either `APPROVED` or `REQUEST_CHANGES`. When connector-safe bridge execution is used, the immutable request additionally binds the same reviewed commit as its request-only parent; the later request/event commit is separate execution provenance.

At either normal Human Gate, the Human may explicitly choose `APPROVED` or routine `REQUEST_CHANGES`. `REQUEST_CHANGES` is not an Exception Gate: record the Human decision/review provenance, validate the Human-supplied allowed regeneration boundary, selectively invalidate affected downstream machine authority, apply the requested edition-local repair, and resume automatically toward the same Gate as the next revision.

Grok handoff is operational transport, not editorial approval or a third Human Gate. Once the expected Grok result is present, import it and resume automatically.

Initialization, Source Intake, search expansion, Screening, Evidence, Completeness/materiality, Candidate Selection, Architecture preparation, reader-facing authorship, deterministic QA, ChatGPT semantic/editorial review, PDF build, ChatGPT visual review, Freeze preparation, transient retry and edition-local repair are **not stop points**. Continue immediately unless a Human/Exception Gate or blocking shared-Core defect is reached.

## 2. Authority order at session start

Before changing an edition, read current reviewed `main` and at minimum:

1. `AGENTS.md`;
2. `docs/survey-production-core-v2-authority.md` plus the current redesign overlay when applicable;
3. this file;
4. `docs/survey-production-core-v2-issue-prevention-checklist.md`;
5. `docs/survey-production-core-v2-x-source-intake.md`;
6. `docs/survey-production-core-v2-execution-record-policy.md`;
7. the applicable Profile/period/thematic/series guide;
8. existing canonical Production Profile/State, Human-review index and edition execution index, if any.

For Core-maintenance implementation/review work, also read `docs/survey-production-core-v2-redesign-authority.md` and `docs/survey-production-core-v2-final-audit-rule.md`.

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

A production run that edits shared Core to make itself pass is not valid evidence that reviewed Core worked. A newer Core revision may be consumed only after separately reviewed/integrated repair.

## 4. Resolve targets without user ceremony

### Weekly

For an explicit issue such as `2026-W35`, use the configured Weekly cutoff calendar. The issue must have completed its editorial cutoff. Initialize with the generic Weekly Profile and do not add issue-specific Core logic.

If Profile/State already exists, resume it. Weekly Grok/X intake is required by Profile and cannot be bypassed because other collectors found many records.

### Retrospective Period

Monthly, half-year and annual configured Specials use one `RETROSPECTIVE_PERIOD` Profile through `scripts/survey_period_v2.py`. Custom bounded periods may use a repository-owned spec. A bounded Period cannot initialize until its period end has passed. ChatGPT records an explicit X `REQUIRED` / `NOT_REQUIRED` decision with rationale.

### Standalone Thematic

Resolve research scope from canonical thematic planning authority. If a machine-readable scope file is absent, ChatGPT materializes it from that authority; this is internal work, not a Human Gate.

### Guided series / Generative AI Foundations

Read `docs/generative-ai-foundations-special-series.md`, inspect completed/in-progress repository evidence, resolve the next volume, and materialize that volume's Thematic scope from living series authority. Do not build a parallel machine Series engine solely for bootstrap convenience.

## 5. Initialization, resume and deterministic execution mode

The start request authorizes deterministic initialization and canonical work-branch/state creation. Initialization is not a Human Gate.

If an exact local checkout/CLI is available, use canonical repository scripts directly. If the connector-only runtime cannot execute exact local Core, use the reviewed operator bridge described in `docs/survey-production-core-v2-operator-execution-bridge.md`.

The bridge is a deterministic execution substrate, not an editorial agent. Its current request surface is exactly:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`
- `RECORD_ARCHITECTURE_APPROVAL`
- `REQUEST_ARCHITECTURE_REVISION`
- `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- `REQUEST_PUBLICATION_PREVIEW_REVISION`

Human Gate operations only record an already explicit Human decision and deterministic consequence; Actions/Core never choose the decision, requested changes or regeneration boundary.

For Human Gate operations, direct-local and bridge-backed execution share the same canonical review-commit check: `reviewed_repository_commit_sha` must resolve to a real Git commit and its tree must contain exact current reviewed Production State and Gate-input bytes. Connector-safe execution additionally requires that reviewed commit to equal the immutable request-only commit parent. Do not substitute the request/event commit for the Human-reviewed commit.

After State, read or create `<source_root>/execution/index.md` and a concise session record. If Human review history exists, read `<source_root>/gates/review-index.json` and the latest referenced rN record before continuing.

## 6. Source Intake and Grok/X Google Drive handoff

Read `docs/survey-production-core-v2-x-source-intake.md` before Discovery Acceptance.

Applicability:

- `WEEKLY`: `REQUIRED`.
- `RETROSPECTIVE_PERIOD`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- `THEMATIC`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- Foundations: use the dedicated series Drive category when required.

For each required run, prepare one self-contained task file:

```text
Grok_X_SourseIntake/<category>/<edition>/<run-id>/grok-task.md
```

Give the Human only the exact Drive task-file path/reference. The Human gives it to Grok. Do **not** search for, install or configure a Grok connector.

Import returned Markdown as **exact bytes** into repository Raw and record `DISCOVERY_RECORDED` or `NO_MATERIAL_DISCOVERY` with rationale. X remains discovery/community signal; technical claims still require authoritative Evidence verification. Then resume automatically.

## 7. Research and Architecture loop

ChatGPT owns research/editorial judgment. Deterministic helpers validate exact structures/invariants; they do not decide what the edition should say.

Normal progression:

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
-> ARCHITECTURE_REVIEW
```

Repair edition-local findings autonomously. If repair would change shared Core, use §3 instead.

Before a Stage Checkpoint is adopted, run the exact intended artifact set through `scripts/survey_stage_validation_v2.py` and include exact `CORE_STAGE_CONTRACT` authority.

## 8. Human Gate 1 — Architecture Review

The first normal stop is:

```text
lifecycle_state = ARCHITECTURE_ESTABLISHED
terminal_reason = HUMAN_GATE_REACHED
next_action = ARCHITECTURE_REVIEW
```

Before presenting the Gate, commit the exact canonical Production State and all configured Architecture Review inputs, including the current Architecture, review summary and review-attention authority. Record that exact commit SHA as the Human review surface. Present the exact Architecture package, research limitations and material unresolved questions from that committed state. Never infer approval from silence and never record approval against an uncommitted or different commit.

If Human says `APPROVED`, use that reviewed commit SHA when recording exact approval plus machine review rN and continue to drafting unless the user explicitly requested to stop after approval.

If Human says `REQUEST_CHANGES`, use the same reviewed commit SHA and require explicit requested changes plus one allowed Architecture regeneration boundary. Canonical Core first proves that commit still reconstructs the exact reviewed State/Gate inputs, then records `gates/reviews/architecture-rN.json`, updates `gates/review-index.json`, resets only downstream State/checkpoint/gate authority, and removes superseded canonical Stage Checkpoints. ChatGPT then performs the requested edition-local repair and revalidates to Architecture Review rN+1. A stale rN approval must fail.

## 9. Reader-facing authorship and QA

After Architecture approval, internal Draft/Synthesis artifacts may support ChatGPT's work but are not publication prose.

ChatGPT explicitly authors canonical reader-facing files under bound `survey_root`, normally `main.tex` and `references.bib`, then creates a Reader Manuscript Manifest binding exact source and Architecture coverage.

For one exact source/PDF revision complete three separate QA layers:

1. **Deterministic QA** — Quality Bundle with applicable deterministic checks and exact source/PDF authority.
2. **Semantic/Editorial QA** — ChatGPT review of exact manuscript/source/PDF.
3. **Visual QA** — ChatGPT visual review of the exact rendered PDF.

Normal edition-local findings cause source revision, rebuild, stale QA invalidation and affected-layer rerun. Do not patch shared Core in production.

## 10. Human Gate 2 — Publication Preview

Finalize one Publication Candidate only after all three QA layers pass on the same source/PDF bytes. The Candidate atomically binds Reader Manuscript, exact source, exact PDF/page count, deterministic bundle, Semantic/Editorial Review and Visual Review.

At `RELEASE_CANDIDATE`, first commit the exact canonical Production State, Publication Candidate and Candidate-bound PDF that will be presented. Record that exact repository commit SHA as the Human review surface, then stop for Human review of that exact committed Candidate/PDF identity. A rebuilt, changed or merely similar PDF is not the reviewed artifact.

If Human says `APPROVED`, use that reviewed commit SHA to record exact Publication Preview approval plus machine review rN and continue to Freeze.

If Human says `REQUEST_CHANGES`, use the same reviewed commit SHA and require explicit requested changes plus one allowed Publication Preview regeneration boundary. Canonical Core first proves the reviewed commit contains the exact current reviewed State, Candidate and Candidate-bound PDF, then records `gates/reviews/publication-rN.json`, preserves approved Architecture when valid, resets affected downstream Validation/Candidate/gate authority and removes superseded Stage Checkpoints. ChatGPT repairs/rebuilds/reviews exact bytes and returns with Publication Preview rN+1. Rebuilt or changed bytes cannot reuse old approval.

## 11. Freeze and Release

After Publication Preview approval, continue without another routine Human Gate:

1. verify approval binds exact already-reviewed Candidate/PDF;
2. build Freeze Record and Release Manifest from that Candidate and approval;
3. transition to `FROZEN` after exact stage validation;
4. merge frozen production changes through normal reviewed repository path;
5. use dedicated mechanical Release workflow against current `main`;
6. create/reconcile issue-only GitHub Release;
7. verify released asset SHA-256/byte count;
8. record Merge Verification, Release Record and compact `FROZEN -> RELEASED` checkpoint.

Do **not** insert a second post-approval semantic/visual quality gate.

## 12. GitHub Actions responsibility

GitHub Actions are retained only where they add independent mechanical value: CI/regression, reproducible build, deterministic checks, exact-byte Preview transport, credential-isolated Release, and the narrow operator execution bridge when exact local CLI is unavailable.

Do not use Actions as Screening/Evidence/Selection/Drafting/Semantic Revision/Visual Repair author or as Human decision-maker. Follow `docs/survey-production-core-v2-workflow-responsibility-inventory.md`.

## 13. Exception Gate

Use an Exception Gate only when safe continuation genuinely needs Owner judgment, including unresolved scope ambiguity, irreconstructible accepted authority, incompatible accepted-contract migration, changed already-approved bytes outside a normal requested-revision cycle, or frozen/release identity divergence.

Do not stop for ordinary search refinement, weak-source replacement, local QA failure, wording/layout repair, CI retry, Grok handoff, or routine Human `REQUEST_CHANGES`.

A shared-Core defect that makes production impossible is `BLOCKED_CORE_DEFECT`; repair occurs in separate Core maintenance.

## 14. Session handoff

If the conversation ends before the requested Gate, update edition execution records with issue/target, work branch, Production State path/SHA, lifecycle, next action/stop reason, latest Stage Checkpoint, latest Human-review rN/index when applicable, exact `reviewed_repository_commit_sha` for any presented/recorded Human Gate, X task/result disposition, shared-Core defect pointer and exact candidate/PDF SHA where applicable. When bridge transport was used, keep the Human-reviewed commit distinct from the later request/event commit.

A later session validates repository state and continues rather than replaying completed work or asking the user to reconstruct it.

## 15. Core-v2 candidate review rule

Core-maintenance candidates follow `docs/survey-production-core-v2-final-audit-rule.md`:

```text
complete every intended code/config/schema/workflow/test/doc/Finding/Repair-Set change
-> obtain required regression/CI evidence on one head
-> synchronize all Core authority/docs
-> freeze that candidate head SHA
-> audit all seven acceptance priorities from zero on that exact head
-> make no candidate-tree changes during the audit
```

The seventh priority is `Human Gate round-trip viability` and explicitly covers approve/revise continuation for both normal gates, direct-local reviewed-commit tree-byte proof, and connector-safe request-parent binding where required.

If any finding requires repository mutation, invalidate the entire audit, repair Core, freeze a new head and rerun all seven points from point 1. Final PASS is PR/Human-review metadata bound to the exact audited SHA.
