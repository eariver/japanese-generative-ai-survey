# Repository agent instructions

## Survey Production Core v2 bootstrap

For Weekly/Special start/resume requests, use current reviewed `main` as source of truth and read `docs/survey-production-core-v2-session-bootstrap.md` plus the applicable Profile/period/thematic/series guide.

The user only needs to identify the target and desired Human Gate. Do not ask them to restate repository-owned mechanics.

ChatGPT is the primary research/editorial/publication operator. Deterministic scripts and GitHub Actions protect exact identities/provenance/invariants/build/release integrity; they do not replace research/editorial judgment or make Human Gate decisions.

## Continuous progression

Do not stop for ordinary internal work. Source Intake, search expansion, Screening, Evidence, completeness/materiality, Selection, Architecture preparation, reader-facing authorship, synthesis, deterministic QA, semantic/editorial QA, PDF build, visual QA, transient retry, and edition-local repair are autonomous work toward the requested Gate.

The two normal Human Gates are:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

A genuine Owner Exception Gate remains separate. Grok Drive path handoff is transport, not a third Gate.

## Durable Human review surface

Before presenting either normal Human Gate:

1. commit exact current Production State and every configured Gate input;
2. **push/retain that commit on the Profile-bound canonical work branch**;
3. use that exact SHA as `reviewed_repository_commit_sha`;
4. present only those committed bytes.

Canonical Human Gate Core requires the commit to exist, remain reachable from the canonical work branch, and exact-bind reviewed State/Gate bytes. Publication Preview also binds exact Candidate-bound PDF.

In connector-safe bridge mode, that reviewed commit must additionally be the immutable request-only commit parent. The later request/event commit is not the Human-reviewed commit.

## Human decision semantics

At either normal Gate the Human may explicitly choose:

- `APPROVED`
- `REQUEST_CHANGES`

ChatGPT/Core must never infer a decision from silence.

Every APPROVED review gets an immutable approval snapshot under `gates/reviews/approvals/` in addition to the current active canonical approval.

### Architecture `REQUEST_CHANGES`

The Human supplies requested changes and one allowed pre-Architecture regeneration boundary. Core records rN, invalidates only affected downstream authority, and returns to that boundary. ChatGPT repairs and resumes to Architecture Review rN+1.

### Publication Preview `REQUEST_CHANGES`

If the chosen boundary is publication-local (`ARCHITECTURE_ESTABLISHED` or later), preserve valid active Architecture approval and regenerate publication authority.

If Publication feedback reveals an upstream defect and the Human chooses a boundary before `ARCHITECTURE_ESTABLISHED`, Core must:

- preserve prior Architecture rN review record + immutable approval snapshot;
- verify and supersede the active canonical Architecture approval;
- clear active Architecture provenance;
- mark Architecture Review pending again;
- invalidate downstream authority from the chosen boundary;
- resume to Architecture Review rN+1 before new publication continuation.

This is normal dependency-aware revision, not an Exception Gate.

## Production versus Core-maintenance responsibility

Production repairs the edition, not shared Core. During edition production, shared roots are read-only:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

If a shared-Core defect appears, record it under the edition execution tree and repair Core separately. A formal production-validation run that discovers shared-Core failure is failed evidence and must be rerun cleanly after reviewed repair.

## Edition execution records

Repository state must allow another session to resume without chat history. Follow `docs/survey-production-core-v2-execution-record-policy.md`.

Maintain:

```text
{source_root}/execution/index.md
{source_root}/execution/sessions/
{source_root}/execution/reviews/
{source_root}/execution/defects/
```

Machine Human-review authority lives under:

```text
{source_root}/gates/reviews/*-rN.json
{source_root}/gates/reviews/approvals/*-rN.json
{source_root}/gates/review-index.json
```

Keep Human-reviewed commit, request commit, trusted executor run, and bot output commit distinct.

## Grok / X Source Intake

Read `docs/survey-production-core-v2-x-source-intake.md` for each edition.

- Weekly: required.
- Retrospective/Thematic: explicit REQUIRED/NOT_REQUIRED rationale.
- Foundations: dedicated Drive category when material.

Prepare one self-contained Drive task file and give the Human its exact path/reference. Import returned bytes exactly and resume automatically. Do not search for/install a Grok connector merely because X intake is required.

## Reader-facing publication boundary

Internal Evidence/Selection/Architecture/Draft artifacts are not legal fallback publication prose.

After Architecture approval, ChatGPT authors canonical reader-facing source. Before Candidate assembly, exact source/PDF must pass:

1. deterministic QA;
2. ChatGPT semantic/editorial QA;
3. ChatGPT exact-PDF visual QA.

Candidate atomically binds exact reader source/PDF/reviews. Rebuilt/different PDF is not the reviewed Candidate.

## Operator bridge trust model

Use direct exact local CLI when available.

Connector-safe operator execution uses:

```text
request-only work-branch commit
-> .github/workflows/survey-production-v2-operator-bridge.yml
   read-only signal only, no trusted execution
-> workflow_run
-> .github/workflows/pipeline-contract-tests.yml loaded from default branch
   read-only trusted preflight
   -> write-capable executor only after PASS
```

The work branch may not prove its own trust. Trusted preflight derives protected-path authority from the named reviewed-main commit, not the work-branch config under review.

The bridge request surface is exactly:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`
- `RECORD_ARCHITECTURE_APPROVAL`
- `REQUEST_ARCHITECTURE_REVISION`
- `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- `REQUEST_PUBLICATION_PREVIEW_REVISION`

No arbitrary command or generic Human-decision surface is allowed.

## Profile generality

- Weekly uses generic `WEEKLY + WEEKLY_MAGAZINE`.
- Monthly/half-year/annual/custom bounded Retrospective uses one generic `survey_period_v2` path.
- Thematic scope comes from planning authority, not topic-specific Core logic.
- Generative AI Foundations remains a living series authority layered over Thematic/LONGFORM, not a parallel machine series engine.

Frozen historical releases remain immutable.

## Core v2 change-management final audit

Follow `docs/survey-production-core-v2-final-audit-rule.md`:

```text
finish all candidate changes
-> exact-head diagnostic CI
-> synchronize authority
-> pre-freeze cross-check
-> freeze one SHA
-> fresh Points 1–7 from zero
-> no candidate mutation during audit
-> only 7/7 PASS -> Human full-candidate review
```

Point 7 must include:

- durable work-branch reviewed-commit reachability;
- exact review bytes;
- immutable approval history;
- Publication→Architecture cross-gate reopen;
- default-branch trusted operator bootstrap.

Any candidate-tree change invalidates the entire audit; never carry forward prior PASS verdicts.
