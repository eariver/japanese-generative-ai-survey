# Repository agent instructions

## Survey Production Core v2 bootstrap

When a user asks to start, resume, or continue a Weekly or Special edition, treat the current `main` branch as the production source of truth and read `docs/survey-production-core-v2-session-bootstrap.md` plus the applicable Profile/series guide before doing editorial work.

The user only needs to identify the target and, when relevant, the Human Gate at which to stop. Do **not** require the user to restate manifest paths, pipeline stages, search tactics, Human Gate rules, taxonomy policy, quality checks, external-source mechanics, or release mechanics that the repository already owns.

Examples of sufficient requests are:

> `2026-W35をArchitecture Reviewまで編纂してください。`

> `Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください。`

From that instruction, ChatGPT is the primary research/editorial operator. It must resolve the target from repository authority, initialize or resume canonical Production Profile/State, read historical Issue-prevention guidance, construct an appropriate research plan, use deterministic tools only where they add real safety or efficiency, and continue autonomously.

**Do not stop for ordinary internal work.** Source Intake, search expansion, Screening, Evidence work, Completeness/materiality review, Candidate Selection, Architecture preparation, drafting, synthesis, deterministic QA, semantic/editorial review, PDF build, agent visual review, Freeze preparation, retryable CI/tool failures, and generic repairs that do not change approved scope/bytes are not user decision points.

The operating default is continuous progression toward the requested Gate. Do not ask the user to confirm routine next steps, approve internal transitions, choose among repository-resolvable mechanics, or authorize ordinary retries. A production session may pause only at a normal Human Gate, a genuine Owner-level Exception Gate, or an unavoidable manual Grok instruction/result transport when the external Grok execution itself cannot be performed directly. Once that Grok result is available, resume automatically without asking for another routine confirmation.

X/Grok collection is a Source Intake subflow, not a third Human Gate. Read `docs/survey-production-core-v2-x-source-intake.md` whenever producing an edition. Weekly requires a Grok/X intake run. Retrospective Period and Thematic work require an explicit ChatGPT `REQUIRED` or `NOT_REQUIRED` decision with rationale; Generative AI Foundations uses the dedicated series Drive category when X is material. ChatGPT creates the run-specific Grok instruction/prompt and provisions the exact Google Drive target below `Grok_X_SourseIntake/<category>/<edition>/<run-id>/`. Grok writes the result only to that Drive run folder. ChatGPT then reads the Drive file, imports its exact bytes into repository Raw storage, and records either Discovery linkage or an explicit no-material-discovery disposition before Discovery Acceptance may pass. Waiting for an external Grok result is an operational dependency while State remains in Source Intake; it is not Human approval or an Exception Gate by itself.

The only normal Human Gates are:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`.

Raise an Exception Gate only when safe continuation genuinely requires Owner judgment, such as unresolved scope ambiguity, incompatible accepted-artifact migration, or a conflict that would require changing already approved authority. Never convert a routine tool/network failure or an internally repairable defect into a Human Gate.

The start request itself authorizes deterministic initialization and creation of the canonical work branch/state. Initialization is not a Human Gate. Never infer Human Gate approval from a request to start or continue compilation.

Repository state must remain sufficient for another ChatGPT session to resume without prior conversation history. Each completed stage records compact checkpoint provenance, including the implementation/contract used at that boundary. The initialization implementation commit is historical provenance, not a permanent toolchain lock.

A later stage may use newer reviewed `main` tooling only after the reviewed repair is actually integrated into the edition work branch. Revalidate or migrate only accepted boundaries affected by the change, then record the actual integrated work-branch head in the next Stage Checkpoint. Do not run an unintegrated second checkout of `main` against edition artifacts and claim that the edition branch used those bytes.

Before a compact local Stage Checkpoint is adopted, run the exact intended stage artifact set through `scripts/survey_stage_validation_v2.py` and include its exact `CORE_STAGE_CONTRACT` deterministic result. A canonical filename or a ChatGPT PASS statement is not a substitute for semantic stage validation. Legacy Screening/Evidence helpers that retain the historical pin internally may be invoked through the narrow allowlisted `scripts/survey_agent_tool_v2.py` bridge after current agent-first State/tool identity has been validated.

For thematic or series requests, resolve editorial scope from the canonical backlog/series document rather than duplicating it in bootstrap configuration. In particular, `Generative AI Foundationsの次巻` is resolved from `docs/generative-ai-foundations-special-series.md` and repository evidence of completed/in-progress volumes; do not invent a parallel machine series plan unless real production later requires one.

Retrospective Period work uses the bounded Period Profile and must not initialize before the period end. Quality applicability must come from the exact bound Production Profile. Public Special release identity comes from that Profile's `survey_root` basename, allowing an internal source ID such as `SP-2025-H2` to retain the established public identity `special/2025-H2`.

Cross-edition pipeline, validator, schema, workflow, or checklist improvements belong on `main` through the repository's normal review/CI process. Edition-specific Evidence, Architecture, drafts, provenance, external-intake manifests/prompts/Raw, and release artifacts remain scoped to that edition's canonical work branch and paths. Frozen historical releases remain immutable.

## Core v2 change-management final audit

Before presenting a Survey Production Core v2 implementation candidate for Human full-candidate review, read and follow `docs/survey-production-core-v2-final-audit-rule.md`.

The mandatory sequence is:

```text
finish every intended candidate change
-> finish all required regressions and repository synchronization
-> freeze one candidate head SHA
-> audit all six acceptance priorities from zero on that exact head
-> do not mutate the candidate during the audit
```

The sixth point independently verifies **autonomous progression / stop discipline**: normal production must not repeatedly stop for internally resolvable work. Only an actual Human Gate, genuine Owner-level Exception Gate, or unavoidable manual Grok transport may interrupt progress toward the requested Gate.

If any audit finding requires a repository change, **invalidate the entire audit**, complete all repairs, freeze a new candidate head, and rerun all six points from point 1. Never carry forward earlier PASS verdicts after changing the candidate.

The final audit result must bind the exact candidate SHA. Record it in PR/Human-review metadata rather than committing a post-audit PASS document that would itself change the audited SHA.

## Pre-merge Core v2 development boundary

While PR #310 remains unmerged, current `main` is still the production authority. Do not initialize W33/SP001 or another Core v2 production edition from the improvement branch. Core v2 development may change only the improvement branch until explicit Human full-candidate approval and merge.
