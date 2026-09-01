# Special session bootstrap contract

Status: canonical session-entry contract for Special editorial work

## Purpose

This document makes Special compilation resumable across chat sessions without requiring a long operational prompt. Repository state and current `main` define the workflow; conversation history is not part of the publication contract.

## Minimal invocation

When the repository is already clear from context, the user may start with only:

> `<target> SpecialをArchitecture Reviewまで編纂してください。`

When repository identity should be explicit:

> `eariver/japanese-generative-ai-survey で <target> SpecialをArchitecture Reviewまで編纂してください。`

`<target>` may be a configured slug such as `2022-Y`, `2021-Y`, `2020-Y`, `2023-Y`, `2024-H1`, `2024-H2`, `2025-H1`, `2025-H2`, `2026-M07`, or another period represented by the current Special configuration.

The target plus the requested stopping Human Gate is sufficient. The user does not need to restate pipeline stages, manifest initialization, branch creation, work-branch naming, period dates, Human Gate rules, page-budget policy, validation policy, source-coverage policy, or release mechanics.

For example, this is a complete annual-backfill request:

> `eariver/japanese-generative-ai-survey で2022-Y SpecialをArchitecture Reviewまで編纂してください。Architecture Reviewに到達するか、それ以前にException Gateが必要となるまでは自律的に進めてください。`

The same form applies to `2021-Y` and `2020-Y` by changing only the year in the slug.

## Configured-target bootstrap plan

A configured historical target must be resolvable **before** its edition manifest exists. Use the current control code to resolve the target from `config/special-pipeline.json`:

```text
python scripts/special_pipeline.py bootstrap-plan --special-slug <target>
```

The bootstrap plan is machine-readable and fixes the configured tier, exact coverage window, canonical `SP-<slug>` identity, init/work branch names, required period guide, initialization authority, normal Architecture-Review execution stages, and stopping Human Gate. It deliberately leaves `retrospective_as_of` as `SET_AT_INITIALIZATION`; unstarted historical editions must not be pre-initialized merely to make a future session easier.

The same operation is available as the `bootstrap-plan` command in the `Special survey pipeline spine` workflow. It does not require `specials/<slug>/edition.json` to exist.

If `bootstrap-plan` cannot resolve the slug, treat the target as unconfigured/ambiguous and use an Exception Gate rather than inventing a period.

## Start-prompt initialization authority

A request to compile a configured Special is itself authorization for the deterministic bootstrap needed to begin that edition. **Initialization is not a Human Gate.** Do not ask for a separate confirmation before creating or merging bootstrap repository state.

If the requested edition does not yet exist, the agent should autonomously:

1. resolve the configured period and current manifest contract from `main` using the configured-target bootstrap plan;
2. create `special/<slug>-init` from the current `main`;
3. create the schema-valid `specials/<slug>/edition.json` and `sources/SP-<slug>/pipeline-state.json` with lifecycle `ISSUE_INITIALIZED`, setting `retrospective_as_of` to the actual initialization session time;
4. validate the bootstrap against current code/config/schema;
5. open the initialization PR to `main` and merge it after deterministic validation succeeds;
6. create the canonical `special/<slug>-work` branch from the merged initialization state;
7. continue immediately through all non-Human-Gate work toward the requested stopping gate.

The start prompt authorizes these bootstrap actions because they establish deterministic control/provenance state and do not approve Candidate Selection, Architecture, Publication Preview, Freeze, or publication content. Ask the user only if initialization itself requires a genuinely new editorial/publication decision, such as an unconfigured/ambiguous target period or a requested scope that conflicts with current policy.

If an init/work branch or bootstrap PR already exists, inspect and resume it rather than creating a duplicate. A deterministic branch/PR conflict that can be resolved without changing editorial scope is not a Human Gate.

## Required startup behavior

On every new Special production session:

1. Read current `main` first. Current code, config, schemas, workflows, and canonical docs take precedence over prior chat history or older editions.
2. Read `config/special-pipeline.json`, `docs/special-human-gates.md`, and `docs/special-editions.md`.
3. Resolve the requested configured target with `scripts/special_pipeline.py bootstrap-plan --special-slug <target>` (or the equivalent workflow) before assuming that an edition manifest already exists. Do not infer a different calendar window from an older issue.
4. Inspect the canonical edition manifest, pipeline state, survey source, init/work branches, and relevant PRs if they exist.
5. If the edition does not yet exist, execute the autonomous initialization sequence above using the current schema/workflow rather than copying another edition by hand.
6. If the edition already exists, resume from the recorded lifecycle state instead of restarting completed stages.
7. Read the applicable period guide listed by the bootstrap plan. `HALF_YEAR` editions additionally require `docs/half-year-retrospective-specials.md`; `ANNUAL` editions additionally require `docs/annual-retrospective-specials.md`.
8. Proceed autonomously through all non-Human-Gate stages needed to reach the requested gate. Retry deterministic collection/CI failures when recovery does not require editorial judgment.
9. Stop at the requested Human Gate and present the repository-backed review package. Never infer or manufacture approval.

## Architecture Review default contract

For the common request to proceed through Architecture Review, perform the current Special flow through:

```text
Initialization / resume (no Human Gate)
  -> canonical Source Intake (all enabled base collectors)
  -> period-specific coverage audit and primary-source gap-fill where required
  -> Screening
  -> Evidence normalization/review
  -> Candidate Selection (internal checkpoint)
  -> Architecture Proposal
  -> HUMAN GATE 1: Architecture Review
```

The standard Source Intake watchlists are a broad discovery baseline rather than a proof of historical completeness. Never replace the canonical base intake with a hand-curated chronology or a small set of expected headline events. Curated primary-source reconstruction is permitted only as supplemental gap-fill after the base intake has been preserved and audited under the applicable period guide.

Do not start reader-facing drafting before Architecture approval.

Candidate Selection is not copied from another edition. Architecture, cluster names, story units, taxonomy, chapter count, thesis, and page allocation are derived from the target period's audited Evidence under the current period-specific guidance.

For `HALF_YEAR` editions, the Architecture Review package must satisfy the current requirements in `docs/half-year-retrospective-specials.md`, including the Source Intake coverage audit, cross-period normalization, and candidates for cross-month comparison, half-year reclassification, cross-layer synthesis, and final half-year synthesis.

For `ANNUAL` editions, the Architecture Review package must satisfy `docs/annual-retrospective-specials.md`, including the annual coverage audit and within-year temporal-skew check, year-wide normalization, story-unit to annual-trajectory construction, evidence-derived phase analysis where useful, annual reclassification, cross-layer synthesis, final annual synthesis, and an explicit single-volume coherence assessment.

## Annual backfill invariants

Configured Annual editions such as `2022-Y`, `2021-Y`, and `2020-Y` reuse the Annual method, not the factual content or counts from `2023-Y`.

- Do not copy 2023 story units, trajectory names, chapter taxonomy, Evidence assignments, chronology counts, unresolved-date counts, or page counts into another year.
- Do not pre-initialize future backfill targets; set `retrospective_as_of` when that edition is actually started.
- Preserve each target year's own audited Source Intake, within-year skew analysis, normalization decisions, and chronology as edition-scoped provenance.
- Reusable validators may assert structural invariants, but year-specific record counts belong only to edition provenance and must not become cross-year workflow constants.
- A configured Annual period remains one annual issue unless its own audited Evidence creates the single-volume coherence Exception Gate described in `docs/annual-retrospective-specials.md`.

## State and implementation boundaries

Repository state must be sufficient for a later session to continue the edition without needing previous chat messages.

Use these boundaries:

- edition-specific Raw, Evidence, Selection, Architecture, drafts, review artifacts, freeze records, and release provenance belong to the edition's canonical paths/work branch;
- reusable fixes to pipeline code, schemas, validators, shared rendering, or workflows should be generalized and merged to `main` through normal review/CI before future editions rely on them;
- a previous edition is useful as provenance and implementation evidence, not as an editorial template;
- Human Gate approvals remain explicit and edition/revision scoped.

## Prompt expansion rule

If the user's prompt only supplies a target and stopping gate, silently expand it according to this contract. Do not ask the user to repeat repository rules that are already encoded here unless current repository state presents a genuine ambiguity or Exception Gate condition.
