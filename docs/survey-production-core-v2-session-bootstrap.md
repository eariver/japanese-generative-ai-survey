# Survey Production Core v2 — agent session bootstrap

Status: `PRE-MERGE CANONICAL CANDIDATE`  
Applies to: Weekly, Retrospective Period, standalone Thematic, and guided Special series work  
Primary operator: **ChatGPT**

## 1. Minimal user contract

A user may start or resume production with only a target and desired stopping Human Gate, for example:

```text
2026-W35をArchitecture Reviewまで編纂してください
Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください
2025-H2をPublication Previewまで進めてください
```

That is sufficient instruction. ChatGPT must reconstruct everything else from current repository authority instead of asking the user to restate pipeline mechanics.

After receiving such a request, continue without stopping for ordinary internal work until one of these conditions is reached:

1. `ARCHITECTURE_REVIEW` Human Gate;
2. exact-byte `PUBLICATION_PREVIEW` Human Gate;
3. a genuine `EXCEPTION_GATE_REQUIRED` condition that cannot be resolved safely without Owner judgment;
4. the explicitly requested earlier stopping point, if the user named one that is itself repository-supported.

Initialization, Source Intake, Screening, Evidence work, Completeness/materiality reasoning, Selection, Architecture preparation, drafting, synthesis, deterministic QA, ChatGPT semantic/visual review, Freeze preparation, and retryable internal repairs are not Human Gates.

## 2. Authority order at session start

Before changing an edition, read current `main` and at minimum:

1. `AGENTS.md`;
2. `docs/survey-production-core-v2-authority.md`;
3. this file;
4. `docs/survey-production-core-v2-issue-prevention-checklist.md`;
5. the applicable Profile/period/thematic/series guide;
6. existing canonical Production Profile/State and stage artifacts for the target, if any.

Repository state outranks chat history. A new session must be able to resume from repository state alone.

While PR #310 is unmerged, Core v2 production remains disabled: current `main` is still the production source of truth and W33/SP001 must not be initialized from the improvement branch.

## 3. Resolve the target without user ceremony

### Weekly

For an explicit issue such as `2026-W35`, use the configured Weekly cutoff calendar. The issue must have completed its editorial cutoff. Initialize with the generic Weekly Profile; do not add issue-specific Core logic.

```text
python scripts/survey_production_v2.py init-weekly --issue-id 2026-W35 --target-gate ARCHITECTURE_REVIEW
```

If canonical Profile/State already exists, resume it rather than reinitializing.

### Retrospective Period

Monthly, half-year and annual configured Specials use the same `RETROSPECTIVE_PERIOD` Profile through `scripts/survey_period_v2.py`:

```text
python scripts/survey_period_v2.py plan --special-slug 2025-H2
python scripts/survey_period_v2.py initialize --special-slug 2025-H2 --target-gate ARCHITECTURE_REVIEW
```

Custom bounded periods may be supplied through a repository-owned spec. Calendar boundaries retain their declared timezone authority while stored instants may be normalized.

### Standalone Thematic

Resolve the research question/scope from the canonical thematic planning authority. For the first Pilot, `SP001` points to `TS-001` in `docs/thematic-special-backlog.md`; the detailed scope is **not** duplicated in Pilot configuration.

If a machine-readable scope file does not yet exist, ChatGPT reads the named planning-authority entry and materializes the question, inclusion/exclusion, dimensions and initial obligations. That is an internal agent action, not a Human Gate.

For W33/SP001 Pilot validation, use the side-effect-free planner first:

```text
python scripts/survey_pilot_bootstrap_v2.py plan --pilot W33
python scripts/survey_pilot_bootstrap_v2.py plan --pilot SP001
```

`SP001` may return `MATERIALIZE_SCOPE`; ChatGPT performs that action and replans. `INITIALIZE`, `RESUME`, and genuinely inconsistent partial initialization have their ordinary meanings.

### Guided series / Generative AI Foundations

For a request such as `Generative AI Foundationsの次巻`, read `docs/generative-ai-foundations-special-series.md`, inspect repository evidence for completed/in-progress volumes, resolve the next volume according to the living series architecture, and materialize that volume's Thematic scope from the series authority.

Do not ask the user to identify a volume number that the repository can determine. Do not create a parallel machine Series engine or duplicate the living series plan solely for bootstrap convenience.

If the series document permits multiple equally valid next volumes and repository state cannot resolve the choice, that is an Owner decision and may become an Exception Gate.

## 4. Initialization and resume semantics

The start request authorizes deterministic initialization and canonical work-branch creation. Initialization is not a Human Gate.

Initialization writes immutable launch provenance:

- Production Profile;
- Production State;
- issue/Profile/path identity;
- initialization implementation/contract identity.

The initialization implementation commit is **historical provenance, not a permanent runtime pin**. Later stages may use newer reviewed `main` tooling. Each completed Stage Checkpoint records the implementation and current contract used for that stage.

When resuming, validate with the agent-first validator:

```text
python scripts/survey_agent_control_v2.py validate-state --state <source_root>/production-state.json
```

Do not use the legacy `survey_production_v2.py validate-state` command as the canonical resume decision, because that command intentionally retains the historical edition-wide pin semantics for compatibility testing.

If a newer tool/schema changes an already accepted artifact contract, revalidate or migrate the affected boundary before continuing. Do not replay unrelated completed stages. Use an Exception Gate only when compatibility cannot be established without changing approved editorial authority.

## 5. Autonomous research/editorial loop

For each internal stage:

```text
read Profile + State + applicable guide/checklist
-> make the research/editorial plan appropriate to the actual edition
-> produce/update canonical stage artifacts
-> run deterministic checks that genuinely apply
-> perform required ChatGPT research/editorial/visual reviews
-> repair ordinary findings and re-check
-> write one compact Stage Checkpoint
-> advance Production State exactly one lifecycle step
-> continue immediately unless a Human/Exception Gate is reached
```

The canonical local-stage record is `schemas/stage-checkpoint-v2.schema.json` under:

```text
<source_root>/orchestration/v2/checkpoints/<FROM_STATE>.json
```

It binds:

- lifecycle transition;
- canonical artifact hashes;
- deterministic or reasoned ChatGPT review evidence;
- implementation commit used at that boundary;
- current contract identity;
- a concise readiness summary.

Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery remains repository compatibility/audit code. It is **not required by the agent-first production hot path**.

## 6. Issue Prevention Checklist

At relevant stages, apply `docs/survey-production-core-v2-issue-prevention-checklist.md`.

Its ownership modes distinguish:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

A semantic/visual finding is not a reason to stop. ChatGPT normally repairs it, reruns affected checks, records concise evidence, and continues. A deterministic failure likewise triggers local repair/retry when safe.

Do not manufacture a validator for an open-ended editorial question, and do not rely on agent memory for a crisp invariant that has a reliable deterministic check.

## 7. Architecture Review — Human Gate 1

The first normal stop is reached when State is:

```text
lifecycle_state = ARCHITECTURE_ESTABLISHED
terminal_reason = HUMAN_GATE_REACHED
next_action = ARCHITECTURE_REVIEW
human_gates.architecture_review = pending
```

Present the repository-backed Architecture, Review Summary, bounded Attention surface, research limitations and material unresolved questions. Never infer approval from silence or from the original compilation request.

After explicit approval, record the exact Architecture approval through the agent-first control path. The approval binds the reviewed Architecture/Review/Attention bytes. Then continue autonomously toward Publication Preview unless the user explicitly asked to stop after Architecture approval.

## 8. Drafting, quality and Publication Preview — Human Gate 2

After Architecture approval, continue through drafting/synthesis, applicable deterministic validation, ChatGPT semantic review, rendering and ChatGPT visual review preparation.

Quality review has three kinds:

- `DETERMINISTIC` — executable result authority required;
- `AGENT_SEMANTIC` — reasoned ChatGPT review tied to the exact source revision;
- `AGENT_VISUAL` — reasoned ChatGPT review tied to the exact rendered PDF revision.

Checks are Profile/Publication-aware. Weekly does not inherit every Long-form/Period-specific check merely because the Core supports those profiles.

At `RELEASE_CANDIDATE`, stop for exact-byte Publication Preview approval. The human approves one specific Publication Candidate and PDF SHA/page count. A rebuilt or merely similar PDF is not approved.

## 9. Freeze and Release

After Publication Preview approval, continue without adding another routine Human Gate:

1. perform/record the exact approved-PDF visual review;
2. build Freeze Record and Release Manifest against the same source/PDF bytes;
3. transition to `FROZEN` with a compact Stage Checkpoint;
4. merge the frozen production changes through the normal reviewed repository path;
5. run the dedicated Release workflow against current `main`;
6. create or reconcile the issue-only GitHub Release;
7. download/recheck released asset SHA-256 and byte count;
8. record Merge Verification, immutable Release Record and one compact `FROZEN -> RELEASED` Release Stage Checkpoint.

External Release reconciliation remains fail-closed and idempotent. Existing tag/title/target/asset divergence is an error, not permission to overwrite history.

## 10. When an Exception Gate is justified

Use an Exception Gate only when safe autonomous continuation genuinely needs Owner judgment, including cases such as:

- target/series scope is materially ambiguous and repository authority does not decide it;
- canonical Profile/State is partially initialized in a way that cannot be safely reconstructed;
- accepted Raw/external artifact identity cannot be established;
- a tool/schema upgrade would require changing accepted editorial meaning rather than merely revalidating it;
- current bytes differ from already Human-approved Architecture or Publication Preview authority;
- frozen/release identity diverges and automatic reconciliation would alter published history.

Do **not** stop for an ordinary search refinement, weak-source replacement, local QA failure, CI retry, wording/layout repair, or generic defect that can be repaired without changing approved authority.

## 11. Session handoff rule

If the conversation ends before the requested Gate, commit enough repository state that a new ChatGPT session can continue. At minimum preserve/report:

```text
issue_id / resolved target
work_branch
Production State path + SHA-256
lifecycle_state
next_action / terminal_reason
latest compact Stage Checkpoint
open Human/Exception Gate, if any
known unresolved research limitations
```

A later session starts from repository reality, validates the agent-first State, reads the current Issue Prevention Checklist and applicable guide, and continues. Conversation history is supplementary only.
