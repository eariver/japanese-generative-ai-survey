# Special session bootstrap contract

Status: canonical session-entry contract for Special editorial work

## Purpose

This document makes Special compilation resumable across chat sessions without requiring a long operational prompt. Repository state and current `main` define the workflow; conversation history is not part of the publication contract.

## Minimal invocation

When the repository is already clear from context, the user may start with only:

> `<target> SpecialをArchitecture Reviewまで編纂してください。`

When repository identity should be explicit:

> `eariver/japanese-generative-ai-survey で <target> SpecialをArchitecture Reviewまで編纂してください。`

`<target>` may be a configured slug such as `2025-H1`, `2025-H2`, `2026-M07`, or another period represented by the current Special configuration.

The target plus the requested stopping Human Gate is sufficient. The user does not need to restate pipeline stages, manifest initialization, work-branch naming, period dates, Human Gate rules, page-budget policy, validation policy, or release mechanics.

## Required startup behavior

On every new Special production session:

1. Read current `main` first. Current code, config, schemas, workflows, and canonical docs take precedence over prior chat history or older editions.
2. Read `config/special-pipeline.json`, `docs/special-human-gates.md`, and `docs/special-editions.md`.
3. Resolve the requested target from current configuration. Do not infer a different calendar window from an older issue.
4. Inspect the canonical edition manifest, pipeline state, survey source, and work branch if they exist.
5. If the edition does not yet exist, initialize it using the current schema/workflow rather than copying another edition by hand.
6. If the edition already exists, resume from the recorded lifecycle state instead of restarting completed stages.
7. Read the applicable period guide. `HALF_YEAR` editions additionally require `docs/half-year-retrospective-specials.md`.
8. Proceed autonomously through all non-Human-Gate stages needed to reach the requested gate. Retry deterministic collection/CI failures when recovery does not require editorial judgment.
9. Stop at the requested Human Gate and present the repository-backed review package. Never infer or manufacture approval.

## Architecture Review default contract

For the common request to proceed through Architecture Review, perform the current Special flow through:

```text
Source Intake
  -> Screening
  -> Evidence normalization/review
  -> Candidate Selection (internal checkpoint)
  -> Architecture Proposal
  -> HUMAN GATE 1: Architecture Review
```

Do not start reader-facing drafting before Architecture approval.

Candidate Selection is not copied from another edition. Architecture, cluster names, story units, taxonomy, chapter count, thesis, and page allocation are derived from the target period's Evidence under the current period-specific guidance.

For `HALF_YEAR` editions, the Architecture Review package must satisfy the current requirements in `docs/half-year-retrospective-specials.md`, including cross-period normalization and candidates for cross-month comparison, half-year reclassification, cross-layer synthesis, and final half-year synthesis.

## State and implementation boundaries

Repository state must be sufficient for a later session to continue the edition without needing previous chat messages.

Use these boundaries:

- edition-specific Raw, Evidence, Selection, Architecture, drafts, review artifacts, freeze records, and release provenance belong to the edition's canonical paths/work branch;
- reusable fixes to pipeline code, schemas, validators, shared rendering, or workflows should be generalized and merged to `main` through normal review/CI before future editions rely on them;
- a previous edition is useful as provenance and implementation evidence, not as an editorial template;
- Human Gate approvals remain explicit and edition/revision scoped.

## Prompt expansion rule

If the user's prompt only supplies a target and stopping gate, silently expand it according to this contract. Do not ask the user to repeat repository rules that are already encoded here unless current repository state presents a genuine ambiguity or Exception Gate condition.
