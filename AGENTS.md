# Repository agent instructions

## Survey Production Core v2 bootstrap

When a user asks to start, resume, or continue a Weekly or Special edition, treat the current reviewed `main` branch as the production source of truth and read `docs/survey-production-core-v2-session-bootstrap.md` plus the applicable Profile/period/thematic/series guide before editorial work.

The user only needs to identify the target and, when relevant, the Human Gate at which to stop. Do **not** require the user to restate manifest paths, pipeline stages, search tactics, Human Gate rules, taxonomy policy, quality checks, external-source mechanics, or release mechanics that the repository already owns.

Examples of sufficient requests are:

> `2026-W35をArchitecture Reviewまで編纂してください。`

> `Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください。`

ChatGPT is the primary research, editorial and publication operator. It resolves the target from repository authority, initializes or resumes canonical Production Profile/State, plans research, performs source/evidence work, authors the reader-facing manuscript, performs semantic/editorial review, reviews the exact rendered PDF visually, and proceeds autonomously toward the requested Gate.

Deterministic scripts and GitHub Actions are support infrastructure. They protect exact identities, provenance, crisp invariants, reproducible builds, CI and release integrity. They do **not** replace ChatGPT research/editorial judgment and do not make Human Gate decisions.

## Continuous production progression

**Do not stop for ordinary internal work.** Source Intake, search expansion, Screening, Evidence work, Completeness/materiality review, Candidate Selection, Architecture preparation, reader-facing authorship, synthesis, deterministic QA, semantic/editorial review, PDF build, ChatGPT visual review, Freeze preparation, retryable transient tool/CI failures, and edition-local repairs that do not alter approved authority are not user decision points.

The operating default is continuous progression toward the requested Gate. Do not ask the user to confirm routine next steps, approve internal transitions, choose repository-resolvable mechanics, or authorize ordinary retries.

The only normal Human Gates are:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`.

Before presenting either Human Gate, commit the exact current Production State and every Gate input that the Human will review, and retain that exact repository commit SHA as the review surface. `ARCHITECTURE_REVIEW` therefore reviews committed Architecture gate inputs; `PUBLICATION_PREVIEW` reviews the committed Publication Candidate and its exact Candidate-bound PDF. Do not ask the Human to approve an uncommitted working-tree state. Canonical Human Gate Core will require `reviewed_repository_commit_sha` to exist and contain those exact bytes before recording either decision; connector-safe bridge execution additionally binds that SHA to the request-only commit parent.

At either normal Gate, the Human may explicitly choose `APPROVED` or routine `REQUEST_CHANGES`. For `REQUEST_CHANGES`, the Human supplies the requested changes and an allowed regeneration boundary. Deterministic Core records the review revision and invalidates only affected downstream authority; ChatGPT then applies the requested edition-local repair and resumes automatically toward the same Gate as rN+1. Routine requested changes are **not** an Exception Gate.

Raise an Exception Gate only when safe continuation genuinely requires Owner judgment. Do not turn routine research refinement, edition-local QA repair, network/tool retry, a normal Human revision, or a missing-but-valid Grok result into an Exception Gate.

## Production versus Core-maintenance responsibility

A production session repairs the **edition**, not shared Core.

During a Weekly/Special production run, shared implementation roots are read-only except for consuming an already reviewed Core revision:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

Edition production may write only edition-scoped source/research/publication/execution/gate artifacts and normal branch/state metadata needed for that edition.

If a likely shared-Core defect appears:

```text
record symptom / reproduction / impact
-> classify SHARED_CORE_DEFECT
-> write/update sources/<issue>/execution/defects/<id>.md
-> if a semantically safe edition-local workaround exists, use it without changing the shared contract
-> otherwise stop the edition as BLOCKED_CORE_DEFECT
-> repair shared Core in a separate Core-maintenance session/branch
```

A production session must not edit a generic validator, renderer, schema, workflow, checklist or Core contract merely to keep the current edition moving. This preserves the distinction between real production validation and debugging Core into a passing state.

A later production stage may consume a newer reviewed Core only after that repair has passed the normal Core review/CI path and is integrated into the edition branch. Revalidate only affected accepted boundaries, record the integrated revision, and continue. The production session does not author that repair.

## Edition execution record

Repository state must be sufficient for another ChatGPT session to resume without prior chat history. Follow `docs/survey-production-core-v2-execution-record-policy.md`.

Normal edition production owns:

```text
sources/<issue>/execution/
  index.md
  sessions/
  reviews/
  defects/
```

Machine Human-review authority is stored under the Profile-bound source root at `gates/reviews/*-rN.json` plus `gates/review-index.json`. Human-readable `execution/reviews/*-rN.md` summarizes/pointers that exact authority; it is not a second State machine.

Create/update one concise session record for material actions and decisions. Do not log every tool call or chain-of-thought. Update `index.md` at Human Gate changes, candidate changes, shared-Core blocking changes, termination, and completion. Human Gate records must preserve the exact committed review-surface SHA separately from any later bridge request/event commit.

Machine lifecycle/checkpoint/candidate/gate artifacts remain authoritative for machine state; the execution tree is human-readable operational provenance.

## Grok / X Source Intake

X/Grok collection is a Source Intake subflow, not a third Human Gate. Read `docs/survey-production-core-v2-x-source-intake.md` for every edition.

- Weekly: X intake is required.
- Retrospective Period/Thematic: ChatGPT records an explicit `REQUIRED` or `NOT_REQUIRED` decision with rationale.
- Generative AI Foundations: when X is material, use the dedicated Drive category.

For a required run, ChatGPT prepares one self-contained Drive task file under:

```text
Grok_X_SourseIntake/<category>/<edition>/<run-id>/grok-task.md
```

The task file contains all instructions Grok needs and names the expected result file in the same run folder. ChatGPT gives the Human the exact Google Drive **task-file path/reference**. The Human gives that path/reference to Grok; the Human does not copy/paste the task body. Grok reads the task and writes the result into the same run folder.

**Do not search for, install, discover, or configure a Grok connector merely because X intake is required.** Absence of a Grok connector is not an error, missing dependency, Exception Gate, or reason to debug the production environment.

Once the expected result exists, ChatGPT imports the exact bytes into repository Raw storage, records `DISCOVERY_RECORDED` or `NO_MATERIAL_DISCOVERY`, and resumes automatically without a routine confirmation.

## Reader-facing publication boundary

Internal Architecture, Selection, Evidence, Draft Package/Result and Profile Synthesis artifacts are research/editorial authorities. They are not legal fallback prose for the publication.

After Architecture approval, ChatGPT explicitly authors the canonical reader-facing source (`<survey_root>/main.tex` plus supporting files as applicable). The Reader Manuscript Manifest binds exact Production Profile, exact approved Architecture, exact reader-facing source/supporting files, complete mapping of Architecture `must_cover_requirements` to reader-facing locations, and Profile-required reader requirements such as final synthesis and Weekly community movement.

Before a Publication Candidate may exist, one exact source/PDF revision must pass three distinct layers:

1. deterministic Quality Bundle for crisp machine-checkable invariants;
2. ChatGPT Semantic/Editorial Review for publication boundary, factual/editorial fidelity and Profile-specific semantics;
3. ChatGPT Visual Review of the exact rendered PDF.

The Publication Candidate atomically binds the Reader Manuscript, exact source, exact PDF, all three QA authorities and page count. `PUBLICATION_PREVIEW` reviews that exact candidate. A rebuilt or merely similar PDF is not the approved artifact. Commit the Candidate/PDF review surface before presenting the Gate so the Human decision can bind a reconstructable repository commit.

If Publication Preview returns `REQUEST_CHANGES`, invalidate affected validation/candidate authority according to the Human-supplied allowed regeneration boundary, perform the requested repair, rerun affected QA and return with a new candidate revision. After Human approval, Freeze/Release re-use the approved exact bytes; do not add a second routine post-approval visual-quality gate.

## Stage/checkpoint use

Before adopting a compact local Stage Checkpoint, validate the exact intended artifact set with `scripts/survey_stage_validation_v2.py` and include its exact `CORE_STAGE_CONTRACT` deterministic result. A canonical filename or ChatGPT PASS statement is not a substitute for exact stage authority validation.

Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery is compatibility/audit code, not the canonical production hot path.

For thematic or series requests, resolve scope from canonical planning/series authority rather than duplicating topic logic in Core configuration. `Generative AI Foundationsの次巻` is resolved from `docs/generative-ai-foundations-special-series.md` and repository evidence, not a parallel machine series engine.

Retrospective Period work uses the generic bounded Period Profile. Monthly, half-year, annual and custom bounded periods must not become separate authoring engines. Public Special release identity derives from the bound Profile's `survey_root` basename.

Frozen historical releases remain immutable.

## Core v2 change-management final audit

Core-maintenance work follows `docs/survey-production-core-v2-final-audit-rule.md`.

Mandatory sequence:

```text
finish every intended candidate change
-> finish required regression/CI repair and repository synchronization
-> freeze one candidate head SHA
-> run all seven acceptance points from zero on that exact head
-> do not mutate the candidate during the audit
-> present that exact passing SHA for Human full-candidate review
```

The seven points are Weekly viability, Special viability, generality, recurrence prevention, control proportionality, autonomous progression/stop discipline, and Human Gate round-trip viability.

If any audit finding requires a repository change, **invalidate the entire audit**, repair in Core maintenance, freeze a new candidate head, and rerun all seven points from point 1. Never carry forward earlier PASS verdicts after candidate mutation.

The final audit result binds the exact candidate SHA and is recorded in PR/Human-review metadata rather than a post-audit candidate-tree commit.
