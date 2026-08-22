# Repository agent instructions

## Survey Production Core v2 bootstrap

When a user asks to start, resume, or continue a Weekly or Special edition, treat the current `main` branch as the production source of truth and read `docs/survey-production-core-v2-session-bootstrap.md` plus the applicable Profile/series guide before doing editorial work.

The user only needs to identify the target and, when relevant, the Human Gate at which to stop. Do **not** require the user to restate manifest paths, pipeline stages, search tactics, Human Gate rules, taxonomy policy, quality checks, or release mechanics that the repository already owns.

Examples of sufficient requests are:

> `2026-W35をArchitecture Reviewまで編纂してください。`

> `Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください。`

From that instruction, ChatGPT is the primary research/editorial operator. It must resolve the target from repository authority, initialize or resume canonical Production Profile/State, read historical Issue-prevention guidance, construct an appropriate research plan, use deterministic tools only where they add real safety or efficiency, and continue autonomously.

**Do not stop for ordinary internal work.** Source Intake, search expansion, Screening, Evidence work, Completeness/materiality review, Candidate Selection, Architecture preparation, drafting, synthesis, deterministic QA, semantic/editorial review, PDF build, agent visual review, Freeze preparation, retryable CI/tool failures, and generic repairs that do not change approved scope/bytes are not user decision points.

The only normal Human Gates are:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`.

Raise an Exception Gate only when safe continuation genuinely requires Owner judgment, such as unresolved scope ambiguity, incompatible accepted-artifact migration, or a conflict that would require changing already approved authority. Never convert a routine tool/network failure or an internally repairable defect into a Human Gate.

The start request itself authorizes deterministic initialization and creation of the canonical work branch/state. Initialization is not a Human Gate. Never infer Human Gate approval from a request to start or continue compilation.

Repository state must remain sufficient for another ChatGPT session to resume without prior conversation history. Each completed stage records compact checkpoint provenance, including the implementation/contract used at that boundary. The initialization implementation commit is historical provenance, not a permanent toolchain lock: a later stage may use newer reviewed `main` tooling, with targeted revalidation when an accepted artifact is affected.

For thematic or series requests, resolve editorial scope from the canonical backlog/series document rather than duplicating it in bootstrap configuration. In particular, `Generative AI Foundationsの次巻` is resolved from `docs/generative-ai-foundations-special-series.md` and repository evidence of completed/in-progress volumes; do not invent a parallel machine series plan unless real production later requires one.

Cross-edition pipeline, validator, schema, workflow, or checklist improvements belong on `main` through the repository's normal review/CI process. Edition-specific Evidence, Architecture, drafts, provenance, and release artifacts remain scoped to that edition's canonical work branch and paths. Frozen historical releases remain immutable.

## Pre-merge Core v2 development boundary

While PR #310 remains unmerged, current `main` is still the production authority. Do not initialize W33/SP001 or another Core v2 production edition from the improvement branch. Core v2 development may change only the improvement branch until explicit Human full-candidate approval and merge.
