# Survey Production Core v2 — agent session bootstrap

Status: `PRE-MERGE CANONICAL CANDIDATE / AUDIT-STABLE PRE-AUDIT`  
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

An external Grok/X collection may create an **operational wait** inside Source Intake when no result is yet available. This is not Human approval and does not add a normal Human Gate. If a result already exists in the configured Google Drive run folder, read/import it and continue without stopping.

## 2. Authority order at session start

Before changing an edition, read current `main` and at minimum:

1. `AGENTS.md`;
2. `docs/survey-production-core-v2-authority.md`;
3. this file;
4. `docs/survey-production-core-v2-issue-prevention-checklist.md`;
5. `docs/survey-production-core-v2-x-source-intake.md`;
6. the applicable Profile/period/thematic/series guide;
7. existing canonical Production Profile/State and stage artifacts for the target, if any.

For Core-v2 implementation/review work, also read `docs/survey-production-core-v2-final-audit-rule.md` before claiming Human full-candidate readiness.

Repository state outranks chat history. A new session must be able to resume from repository state alone.

While PR #310 is unmerged, Core v2 production remains disabled: current `main` is still the production source of truth and W33/SP001 must not be initialized from the improvement branch.

## 3. Resolve the target without user ceremony

### Weekly

For an explicit issue such as `2026-W35`, use the configured Weekly cutoff calendar. The issue must have completed its editorial cutoff. Initialize with the generic Weekly Profile; do not add issue-specific Core logic.

```text
python scripts/survey_production_v2.py init-weekly --issue-id 2026-W35 --target-gate ARCHITECTURE_REVIEW
```

If canonical Profile/State already exists, resume it rather than reinitializing.

Weekly Grok/X intake is required by Profile. It cannot be skipped because conventional collectors produced many records.

### Retrospective Period

Monthly, half-year and annual configured Specials use the same `RETROSPECTIVE_PERIOD` Profile through `scripts/survey_period_v2.py`:

```text
python scripts/survey_period_v2.py plan --special-slug 2025-H2
python scripts/survey_period_v2.py initialize --special-slug 2025-H2 --target-gate ARCHITECTURE_REVIEW
```

Custom bounded periods may be supplied through a repository-owned spec. Calendar boundaries retain their declared timezone authority while stored instants may be normalized. A bounded Period cannot initialize until its period end has passed; planning before that point fails closed rather than compiling an incomplete retrospective as if complete.

For X, ChatGPT makes an explicit `REQUIRED` / `NOT_REQUIRED` decision based on the retrospective research question and records the rationale.

### Standalone Thematic

Resolve the research question/scope from the canonical thematic planning authority. For the first Pilot, `SP001` points to `TS-001` in `docs/thematic-special-backlog.md`; the detailed scope is **not** duplicated in Pilot configuration.

If a machine-readable scope file does not yet exist, ChatGPT reads the named planning-authority entry and materializes the question, inclusion/exclusion, dimensions and initial obligations. That is an internal agent action, not a Human Gate.

For W33/SP001 Pilot validation, use the side-effect-free planner first:

```text
python scripts/survey_pilot_bootstrap_v2.py plan --pilot W33
python scripts/survey_pilot_bootstrap_v2.py plan --pilot SP001
```

`SP001` may return `MATERIALIZE_SCOPE`; ChatGPT performs that action and replans. `INITIALIZE`, `RESUME`, and genuinely inconsistent partial initialization have their ordinary meanings.

For X, ChatGPT explicitly decides whether X community/adoption/implementation signal is material to the thematic question.

### Guided series / Generative AI Foundations

For a request such as `Generative AI Foundationsの次巻`, read `docs/generative-ai-foundations-special-series.md`, inspect repository evidence for completed/in-progress volumes, resolve the next volume according to the living series architecture, and materialize that volume's Thematic scope from the series authority.

Do not ask the user to identify a volume number that the repository can determine. Do not create a parallel machine Series engine or duplicate the living series plan solely for bootstrap convenience.

If the series document permits multiple equally valid next volumes and repository state cannot resolve the choice, that is an Owner decision and may become an Exception Gate.

Each Foundations volume still uses a normal `THEMATIC` Production Profile. If X is material, set the X Source Intake series context to `GENERATIVE_AI_FOUNDATIONS` so the Google Drive handoff uses the dedicated series category rather than the standalone Thematic folder.

## 4. Initialization, resume and reviewed tool upgrades

The start request authorizes deterministic initialization and canonical work-branch creation. Initialization is not a Human Gate.

Initialization writes immutable launch provenance:

- Production Profile;
- Production State;
- issue/Profile/path identity;
- initialization implementation/contract identity.

The initialization implementation commit is **historical provenance, not a permanent runtime pin**. Later stages may use newer reviewed generic tooling, but the edition branch must first actually contain that reviewed repair.

Canonical upgrade procedure:

```text
generic repair reviewed/merged on main
-> integrate that reviewed main repair commit into the edition work branch
-> validate the edition State with the integrated branch toolchain
-> revalidate/migrate only accepted boundaries affected by the change
-> execute the next stage from that integrated branch head
-> Stage Checkpoint records that actual head + current contract
```

Do not execute an unrelated second checkout of `main` against edition files and then claim the work branch contained those tools. If an accepted contract cannot be migrated or revalidated safely, use an Exception Gate.

When resuming, validate with the agent-first validator:

```text
python scripts/survey_agent_control_v2.py validate-state --state <source_root>/production-state.json
```

Do not use the legacy `survey_production_v2.py validate-state` command as the canonical resume decision, because that command intentionally retains the historical edition-wide pin semantics for compatibility testing.

For legacy Screening/Evidence helper entrypoints that still invoke the old pin check internally, run them through the narrow current-tool bridge:

```text
python scripts/survey_agent_tool_v2.py <allowlisted screening/evidence helper arguments>
```

The bridge does not make an arbitrary external tool authoritative; it verifies current agent-first State and the actual current work-branch implementation before delegating.

## 5. Source Intake and Grok/X Google Drive handoff

Read `docs/survey-production-core-v2-x-source-intake.md` before accepting Discovery.

### 5.1 Decide X applicability

- `WEEKLY`: decision is always `REQUIRED`.
- `RETROSPECTIVE_PERIOD`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- `THEMATIC`: ChatGPT chooses `REQUIRED` or `NOT_REQUIRED` with rationale.
- Foundations volumes use `THEMATIC` plus `series_context = GENERATIVE_AI_FOUNDATIONS` when X is required.

A `NOT_REQUIRED` decision is a research judgment, not a shortcut. Record why X would not materially improve the current question.

### 5.2 Prepare one or more Grok runs

For every required run, ChatGPT defines:

- purpose;
- research questions;
- coverage focus;
- time scope;
- stable run ID;
- expected result filename.

Create a small spec and render the run package with:

```text
python scripts/survey_x_intake_v2.py build \
  --profile <source_root>/production-profile.json \
  --spec <run-spec.json>
```

This writes:

```text
<source_root>/external/x/x-source-intake-v2.json
<source_root>/external/x/<run-id>/grok-instruction.md
<source_root>/external/x/<run-id>/grok-prompt.md
```

The generated prompt is self-contained and binds the intended Google Drive path.

### 5.3 Provision the Google Drive target

Use the connected Google Drive capability to resolve the exact root folder named:

`Grok_X_SourseIntake`

Persistent categories are:

```text
Weekly
Retrospective_Special
Thematic_Special
Generative_AI_Foundations
```

Create the missing edition/run folders so the exact target exists before Grok runs:

```text
Grok_X_SourseIntake/<category>/<edition-folder>/<run-id>/
```

Do not commit the account-specific Drive folder ID/URL to the repository. Repository artifacts record the stable folder-name path; the connector resolves the actual account-specific ID at runtime.

### 5.4 Execute / wait for external X collection

Give Grok the generated instruction/prompt. Grok searches X and saves its final Markdown **only** in the exact Drive run folder. Grok must not push to GitHub.

If the result is absent, keep the Production State at Source Intake and preserve the `AWAITING_GROK` manifest. Report the exact run folder and prompt/instruction to the Human if manual transport is needed. This is not a Human Gate.

If the result is already present, continue immediately.

### 5.5 Import and disposition the Drive result

Use the connected Google Drive capability to read the returned Markdown. Copy the exact returned content into repository Raw storage, preferably:

```text
<source_root>/external/x/<run-id>/raw/<actual-drive-filename>.md
```

Do not paraphrase the Drive file before hashing/importing it.

Evaluate the result as research input. Then record one of:

```text
DISCOVERY_RECORDED
NO_MATERIAL_DISCOVERY
```

If material, the named Discovery record(s) must bind the exact imported Grok Raw path. If not material, record a non-empty rationale instead of fabricating a Discovery.

Record the result into the manifest:

```text
python scripts/survey_x_intake_v2.py record-result ...
```

Grok output remains Discovery/community-signal material. Technical facts still require normal authoritative Evidence verification.

### 5.6 Accept Discovery

Discovery Acceptance binds the exact completed X Source Intake manifest SHA. Therefore `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` cannot pass when:

- Weekly skipped X;
- a required Grok run is still awaiting output;
- imported Grok Raw bytes drifted;
- the X result was collected but never given a Discovery/no-material disposition;
- a `DISCOVERY_RECORDED` run names a Discovery that does not bind its imported Raw bytes.

Conventional collectors, direct ChatGPT web research and X/Grok all remain Source Intake surfaces. Collector success/count alone is never research completeness.

## 6. Autonomous research/editorial loop

For each internal stage:

```text
read Profile + State + applicable guide/checklist
-> make the research/editorial plan appropriate to the actual edition
-> perform applicable Source Intake, including X/Grok handoff above
-> produce/update canonical stage artifacts
-> run deterministic checks that genuinely apply
-> perform required ChatGPT research/editorial/visual reviews
-> repair ordinary findings and re-check
-> validate the exact intended stage artifact set with scripts/survey_stage_validation_v2.py
-> include its exact CORE_STAGE_CONTRACT result in the compact checkpoint review set
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
- exact `CORE_STAGE_CONTRACT` deterministic validation of State/Profile/current tool/current contract/artifacts;
- reasoned ChatGPT review evidence where required;
- implementation commit used at that boundary;
- current contract identity;
- a concise readiness summary.

A file with the expected artifact name is not enough. The semantic stage validator must accept the exact bytes that the checkpoint adopts. For Discovery, the accepted Discovery artifact transitively binds the completed X Source Intake manifest and imported Raw bytes.

Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery remains repository compatibility/audit code. It is **not required by the agent-first production hot path**.

## 7. Issue Prevention Checklist

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

## 8. Architecture Review — Human Gate 1

The first normal stop is reached when State is:

```text
lifecycle_state = ARCHITECTURE_ESTABLISHED
terminal_reason = HUMAN_GATE_REACHED
next_action = ARCHITECTURE_REVIEW
human_gates.architecture_review = pending
```

Present the repository-backed Architecture, Review Summary, bounded Attention surface, research limitations and material unresolved questions. Never infer approval from silence or from the original compilation request.

After explicit approval, record the exact Architecture approval through the agent-first control path. The approval binds the reviewed Architecture/Review/Attention bytes. Then continue autonomously toward Publication Preview unless the user explicitly asked to stop after Architecture approval.

## 9. Drafting, quality and Publication Preview — Human Gate 2

After Architecture approval, continue through drafting/synthesis, applicable deterministic validation, ChatGPT semantic review, rendering and ChatGPT visual review preparation.

Quality review has three kinds:

- `DETERMINISTIC` — executable result authority required;
- `AGENT_SEMANTIC` — reasoned ChatGPT review tied to the exact source revision;
- `AGENT_VISUAL` — reasoned ChatGPT review tied to the exact rendered PDF revision.

The Quality Bundle binds the exact Production Profile, source bytes and PDF bytes. Research/publication check applicability is derived from that Profile; it is not guessed from the issue ID. In particular, Retrospective Period checks cannot silently fall back to Thematic checks.

At `RELEASE_CANDIDATE`, stop for exact-byte Publication Preview approval. The human approves one specific Publication Candidate and PDF SHA/page count. A rebuilt or merely similar PDF is not approved.

## 10. Freeze and Release

After Publication Preview approval, continue without adding another routine Human Gate:

1. perform/record the exact approved-PDF visual review;
2. build the Freeze Record and Release Manifest with `scripts/survey_profiled_freeze_v2.py`, which revalidates Candidate/Quality/Profile/Preview/Visual authority;
3. transition to `FROZEN` with a compact Stage Checkpoint after exact stage validation;
4. merge the frozen production changes through the normal reviewed repository path;
5. run the dedicated Release workflow against current `main`;
6. create or reconcile the issue-only GitHub Release;
7. download/recheck released asset SHA-256 and byte count;
8. record Merge Verification, immutable Release Record and one compact `FROZEN -> RELEASED` Release Stage Checkpoint.

Public release identity is derived from the exact Production Profile `paths.survey_root` basename. This preserves internal source IDs such as `SP-2025-H2` while publishing the existing reader-facing identity `special/2025-H2`. Weekly and ordinary Thematic slugs naturally remain `weekly/2026-W35` and `special/SP001`-style identities.

External Release reconciliation remains fail-closed and idempotent. Existing tag/title/target/asset divergence is an error, not permission to overwrite history.

## 11. When an Exception Gate is justified

Use an Exception Gate only when safe autonomous continuation genuinely needs Owner judgment, including cases such as:

- target/series scope is materially ambiguous and repository authority does not decide it;
- canonical Profile/State is partially initialized in a way that cannot be safely reconstructed;
- accepted Raw/external artifact identity cannot be established;
- a tool/schema upgrade would require changing accepted editorial meaning rather than merely revalidating it;
- current bytes differ from already Human-approved Architecture or Publication Preview authority;
- frozen/release identity diverges and automatic reconciliation would alter published history.

Do **not** stop for an ordinary search refinement, weak-source replacement, local QA failure, CI retry, wording/layout repair, ordinary Grok result transport, or generic defect that can be repaired without changing approved authority.

A missing Grok result is not an Exception Gate if the task and Drive target are valid; it is incomplete Source Intake. A genuine inability to establish the returned external artifact's identity after reasonable recovery may become an Exception Gate because accepted Raw authority cannot be established safely.

## 12. Session handoff rule

If the conversation ends before the requested Gate, commit enough repository state that a new ChatGPT session can continue. At minimum preserve/report:

```text
issue_id / resolved target
work_branch
Production State path + SHA-256
lifecycle_state
next_action / terminal_reason
latest compact Stage Checkpoint
X Source Intake manifest path/status, if Source Intake is active
pending Grok run-id + Google Drive folder-name path, if AWAITING_GROK
open Human/Exception Gate, if any
known unresolved research limitations
```

A later session starts from repository reality, validates the agent-first State, reads the current Issue Prevention Checklist, X Source Intake authority and applicable guide, and continues. Conversation history is supplementary only.

## 13. Core-v2 candidate review rule

For changes to Survey Production Core v2 itself, follow `docs/survey-production-core-v2-final-audit-rule.md` exactly:

```text
complete every code/config/schema/workflow/test/doc/Finding/Repair-Set change
-> obtain complete cross-regression evidence
-> freeze one candidate head SHA
-> audit all five acceptance priorities from zero on that exact head
-> make no candidate-tree changes during the audit
```

If any audit finding requires a repository change, the entire audit is invalidated. Complete all repairs, freeze a new head, and rerun all five points from point 1. Never recheck only the failed point after changing the candidate.

The final PASS is recorded against the exact audited SHA in the PR/Human-review handoff rather than by committing a post-audit PASS document that would change the candidate SHA.
