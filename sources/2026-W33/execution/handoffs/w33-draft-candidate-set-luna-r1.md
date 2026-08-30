# 2026-W33 complete Draft candidate set — Luna handoff r1

## Purpose

Generate and internally repair the complete W33 Draft candidate set from the already-approved Architecture, then stop for Sol semantic/editorial review **before** any Draft checkpoint or Production State advancement.

This is intentionally a larger Luna work unit than prior single-transition tasks. The unit includes all seven Draft packages/results plus Weekly Profile Synthesis, deterministic validation, and a bounded internal semantic self-review/repair loop.

The rollback boundary remains cheap: Production State must stay at `ARCHITECTURE_ESTABLISHED` with Draft checkpoint `pending` throughout this task.

Normal completion status:

`DRAFT_CANDIDATE_SET_READY_FOR_SOL_REVIEW`

## Repository authority

Repository:

`eariver/japanese-generative-ai-survey`

Branch:

`weekly/2026-W33-v2-work`

The caller will provide an **Exact Starting SHA**. Before any GitHub write, verify that the remote branch HEAD exactly equals that caller-supplied SHA.

If it does not match, perform no GitHub write and stop with the actual remote HEAD.

Reviewed-main Core authority:

`6267de3f6876f491950139757bfdf1085fc07bdc`

Shared Core/config/schema/workflow authority is read-only. Do not modify it.

## Mandatory current state

Before drafting, verify current canonical Production State:

`sources/2026-W33/production-state.json`

Required:

- lifecycle: `ARCHITECTURE_ESTABLISHED`
- `human_gates.architecture_review = approved`
- Architecture approval provenance is non-null and resolves exactly to canonical approval bytes
- `next_action = stage:drafting-synthesis`
- `terminal_reason = null`
- Architecture checkpoint: `passed`
- Draft checkpoint: `pending`
- Publication Preview: `pending`
- Exception Gate: `inactive`

If any of these conditions fail, stop `NEEDS_SOL_REVIEW` without Draft writes.

## Mandatory read order

Read and treat as authority in this order:

1. reviewed-main `config/survey-production-v2.json`
2. reviewed-main `scripts/survey_drafting_v2.py`
3. reviewed-main `scripts/survey_drafting_v2_base.py`
4. reviewed-main `scripts/survey_draft_profile_v2.py`
5. reviewed-main `scripts/survey_stage_validation_v2.py`
6. reviewed-main `schemas/draft-v2-package.schema.json`
7. reviewed-main `schemas/draft-v2-result.schema.json`
8. reviewed-main `schemas/profile-synthesis-v2-input.schema.json`
9. reviewed-main `schemas/profile-synthesis-v2-result.schema.json`
10. reviewed-main `config/prompts/article-drafting-v2.md`
11. reviewed-main `config/prompts/profile-synthesis-v2.md`
12. `sources/2026-W33/production-profile.json`
13. `sources/2026-W33/production-state.json`
14. `sources/2026-W33/gates/architecture-approval.json`
15. `sources/2026-W33/gates/reviews/architecture-r3.json`
16. `sources/2026-W33/architecture-v2.json`
17. `sources/2026-W33/architecture-review-summary-v2.json`
18. `sources/2026-W33/architecture-review-attention-v2.json`
19. current accepted upstream artifacts through the existing Stage Checkpoint provenance chain: Discovery acceptance, Screening acceptance, Evidence acceptance, Edition Views acceptance, Materiality Ledger, Profile Completeness, Candidate Matrix, Candidate Selection
20. `sources/2026-W33/execution/reviews/w33-architecture-approval-materialization-sol-review-20260831-r1.md`

Do not use chat history as authority when repository authority is available.

## Frozen semantic basis

The Owner-approved Architecture has seven packages in this order:

1. `w33-frontier-models-access`
2. `w33-cyber-access-governance`
3. `w33-serving-runtime`
4. `w33-memory-decoding-systems`
5. `w33-agent-evaluation-reliability`
6. `w33-multimodal-media`
7. `w33-week-in-review`

The first six are substantive packages. The seventh is the mandatory independent Weekly synthesis chapter.

Do not change:

- package count or order;
- candidate placement semantics;
- must-cover requirements;
- Architecture boundaries;
- Profile extensions;
- Publication extensions;
- target 18 / hard max 24 page Architecture plan;
- Agent Reliability comparative-synthesis requirement;
- mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` role.

## Important cross-package synthesis contract

`w33-week-in-review` intentionally has no direct PRIMARY/SUPPORTING Architecture candidate placement.

Use the reviewed-main compatibility behavior in `scripts/survey_drafting_v2.py`.

It permits exactly one final empty-placement cross-package synthesis package and derives its Draft-time Evidence inputs as `SUPPORTING` references to candidates already placed in the other Architecture packages.

These are Draft-time references only. They MUST NOT mutate Candidate Selection or Architecture placement/destination semantics.

Do not bypass this behavior by manually inventing a synthetic candidate or by assigning direct Architecture placements to `w33-week-in-review`.

## No new research

This task is Drafting, not Source Intake or Evidence repair.

Forbidden as factual authority:

- web search;
- Google Drive source expansion;
- fresh vendor documentation;
- fresh papers;
- Raw source payloads;
- new X/Grok research;
- unstated external knowledge;
- new factual claims inferred from general model knowledge.

Use only factual Evidence embedded in the canonically derived Draft Packages.

If a desired sentence cannot be supported by the structured Evidence supplied to that Draft Package, omit it or preserve the uncertainty/boundary. Do not repair Evidence during this task.

## Output root

Create the candidate set only under:

`sources/2026-W33/drafting/v2/luna-r1/`

Required layout:

```text
sources/2026-W33/drafting/v2/luna-r1/
  packages/
    w33-frontier-models-access.json
    w33-cyber-access-governance.json
    w33-serving-runtime.json
    w33-memory-decoding-systems.json
    w33-agent-evaluation-reliability.json
    w33-multimodal-media.json
    w33-week-in-review.json
  results/
    w33-frontier-models-access.json
    w33-cyber-access-governance.json
    w33-serving-runtime.json
    w33-memory-decoding-systems.json
    w33-agent-evaluation-reliability.json
    w33-multimodal-media.json
    w33-week-in-review.json
  synthesis-input.json
  synthesis-result.json
```

Also create exactly one Luna session record:

`sources/2026-W33/execution/sessions/w33-luna-draft-candidate-set-20260831-r1.md`

Do not create a canonical Stage Checkpoint or bridge request in this task.

## Step 1 — derive all seven Draft Packages canonically

Resolve all upstream artifact paths from canonical State/checkpoint provenance and current accepted authorities rather than guessing stale historical paths.

For each Architecture package, derive the Draft Package with the reviewed-main `scripts/survey_drafting_v2.py` behavior and exact current:

- Production Profile
- Discovery acceptance basis
- Screening acceptance
- Evidence acceptance
- Edition Views acceptance
- Materiality Ledger
- Profile Completeness
- Candidate Matrix
- Candidate Selection
- approved Architecture
- Architecture Review Summary
- Architecture Approval
- reviewed-main implementation authority

Do not hand-author or edit a derived Draft Package.

After derivation, validate every package against its schema and self-contained provenance contract.

## Step 2 — generate all seven Draft Results

Generate one reader-facing Japanese Draft Result per derived package using only:

- the exact Draft Package;
- reviewed-main `config/prompts/article-drafting-v2.md`;
- reviewed-main Draft Result schema/validator.

Final candidate version for this handoff:

- `draft_version = v1.0`
- `status = DRAFT`

Runner metadata must truthfully identify the actual Luna execution model/runtime and generation time.

### Generic Draft requirements

For every Draft Result:

- preserve `issue_id`, profiles, package ID, package/prompt SHA bindings;
- preserve exact Profile/Publication extensions;
- produce coherent reader-facing Japanese, not an internal research memo;
- every evidence-dependent factual/metric/event/limitation/inference assertion must carry correct structured Evidence refs;
- preserve subject identity and role (`PRIMARY_SUBJECT`, `COMPARATOR`, `RELATED`);
- use correct attribution mode for vendor/project/author claims, social observations, and inference;
- unknowns remain unknown;
- cover every Architecture `must_cover_requirement` exactly through `must_cover_coverage`;
- dispose every Architecture boundary exactly once;
- use `EXPLICITLY_STATED` when the limitation materially affects reader interpretation;
- use `RESPECTED_BY_OMISSION` only when the unsupported claim is correctly absent;
- never hide a material caveat merely to make the prose cleaner;
- do not expose repository paths, candidate IDs, evidence task IDs, internal status vocabulary, or pipeline mechanics in reader-facing text unless genuinely reader-relevant;
- avoid one-source/one-candidate mini-article structure when the Architecture calls for synthesis/comparison;
- respect the package's target page intent by writing densely and selectively rather than exhaustively reproducing Evidence.

### Package-level editorial requirements

#### `w33-frontier-models-access`

Treat access mode and deployment surface as the comparison axis. Preserve preview/GA/open-weight/partner distinctions and source-attributed limitations. Do not turn index/chronology/context evidence into unsupported launch claims.

#### `w33-cyber-access-governance`

Separate authorized vulnerability/security-testing access from general model availability. Keep model scope, access scope, safeguards, and partner distribution boundaries explicit.

#### `w33-serving-runtime`

Explain framework/runtime/front-end-cache/kernel as different implementation layers. Do not write four disconnected release-note summaries.

#### `w33-memory-decoding-systems`

Compare mechanisms by which memory placement/prefetch/decoding policy change inference-system bottlenecks. Paper-reported numbers remain author-reported, not independently reproduced facts.

#### `w33-agent-evaluation-reliability`

This MUST remain a comparative synthesis. Do not produce a sequence of six paper summaries. Organize around scaffolding, evaluation design, task horizon, failure structure, and the distinction between success-rate reporting and reliability understanding.

#### `w33-multimodal-media`

Synthesize the selected multimodal/media developments according to their common product/technical implications while preserving each Evidence boundary and attribution.

#### `w33-week-in-review`

This is a reader-facing independent final chapter, not the machine-readable Profile Synthesis payload.

It MUST:

- synthesize across the six prior substantive packages;
- answer **what changed this week**;
- answer **why those changes matter together**;
- answer **what readers should watch next**;
- use only the cross-package Evidence references canonically supplied by its Draft Package;
- add no new facts or synthetic candidate;
- avoid repeating six miniature section summaries;
- identify the week's higher-order pattern: model/access, operational runtime, and evaluation/reliability moving together;
- preserve material uncertainty and attribution;
- avoid presenting rejected carry-over items or the sole HOLD item as W33 developments.

## Step 3 — deterministic Draft validation

For every Draft Result:

1. validate JSON schema;
2. run the canonical Draft Result validator against its exact package and `article-drafting-v2` prompt;
3. run Draft extension propagation validation;
4. verify every must-cover requirement is represented exactly once in coverage authority and maps to valid reader-facing blocks;
5. verify every Architecture boundary has exactly one valid disposition;
6. verify all structured Evidence refs resolve within the package and preserve subject role/attribution semantics.

Any deterministic failure must be repaired before continuing.

Do not weaken validators or edit shared Core to make a result pass.

## Step 4 — Luna internal semantic/editorial review and repair loop

After all seven deterministic validations pass, perform a cross-package semantic/editorial review of the complete set.

Review at minimum:

### Evidence fidelity

- no unsupported factual expansion;
- no vendor/project/paper claim silently promoted to neutral fact;
- no comparator property attached to the wrong subject;
- no unresolved limitation erased;
- no date/window/context boundary rewritten as launch chronology.

### Architecture fidelity

- every package fulfills its purpose and must-cover requirements;
- boundaries are reader-visible when materially necessary;
- first six packages preserve their distinct editorial roles;
- `w33-agent-evaluation-reliability` is genuinely comparative;
- `w33-week-in-review` is genuinely cross-package synthesis.

### Reader quality

- Japanese is clear, technically precise, and magazine-readable;
- headlines/decks accurately describe the article rather than overclaim;
- paragraphs have a coherent argument and do not read as Evidence dumps;
- repeated background/explanations across packages are reduced;
- transitions make the issue read as one edition rather than seven unrelated notes;
- technical terminology is introduced with enough context for a technically literate general AI reader;
- prose density is consistent with each package's `publication_extensions.target_pages` and the 18-page issue target, without forcing unsupported detail merely to fill space.

### Cross-package duplication

Flag and repair:

- the same factual event unnecessarily explained in multiple substantive packages;
- generic model-access framing repeated verbatim across packages;
- `w33-week-in-review` copying paragraphs rather than synthesizing;
- duplicated caveat language when a shorter package-specific boundary is sufficient.

If defects are found, revise the affected Draft Result(s) inside this same Luna work unit and rerun all affected deterministic and semantic checks.

Do not broaden Evidence to repair prose.

## Step 5 — build Weekly Profile Synthesis input

Only after all seven Draft Results pass the internal review, build `synthesis-input.json` canonically from the complete seven Draft Package/Result pairs.

The synthesis input must exactly match `build_synthesis_input(...)` under reviewed-main Core.

It must contain exactly one validated Draft Result for every Architecture package.

## Step 6 — generate Weekly Profile Synthesis Result

Generate `synthesis-result.json` using only:

- canonical `synthesis-input.json`;
- reviewed-main `config/prompts/profile-synthesis-v2.md`;
- reviewed-main Profile Synthesis Result schema/validator.

Final candidate version:

- `synthesis_version = v1.0`
- `status = DRAFT`

For W33, Research Profile payload keys must exactly be:

- `signals`
- `current_interpretation`
- `carry_over_summary`

Publication Profile payload requirements for `WEEKLY_MAGAZINE` are currently empty; preserve the exact current contract rather than inventing publication payload fields.

The Profile Synthesis is machine-readable issue-level synthesis metadata. It is NOT a replacement for the reader-facing `w33-week-in-review` Draft Result.

Do not introduce new factual claims in Profile Synthesis; synthesize only from validated Draft Results and retain material caveats.

## Step 7 — validate complete candidate set

Before writing the final session status, require:

- exactly 7 Draft Packages;
- exactly 7 Draft Results;
- exact package/result package-ID equality;
- all package schemas PASS;
- all Draft Result schemas PASS;
- all canonical Draft validators PASS;
- all extension propagation checks PASS;
- canonical `synthesis-input.json` derivation equality PASS;
- Profile Synthesis schema PASS;
- canonical Profile Synthesis validator PASS;
- internal semantic/editorial review PASS after any repairs;
- Production State remains byte-identical to the task's starting State;
- Architecture approval, Architecture, Review Summary, Review Attention, Matrix, Selection, Evidence acceptance and earlier accepted authority remain unchanged;
- no Stage Checkpoint created;
- no operator bridge request created;
- no lifecycle transition performed.

## Luna session record

Write:

`sources/2026-W33/execution/sessions/w33-luna-draft-candidate-set-20260831-r1.md`

It must record at minimum:

- caller-supplied Exact Starting SHA and remote verification result;
- reviewed-main SHA;
- starting/final branch HEAD;
- starting/final Production State SHA-256 and proof they are equal;
- Architecture approval SHA-256;
- all seven package paths and SHA-256 values;
- all seven result paths and SHA-256 values;
- synthesis input/result paths and SHA-256 values;
- actual runner/model identities;
- deterministic validation results;
- internal semantic/editorial review checklist and any repairs made;
- explicit confirmation that no new research/raw-source/web authority was used;
- explicit confirmation that no State/checkpoint/bridge operation occurred;
- exact changed-path inventory;
- final status.

## Write allowlist

Only these paths may be created/modified:

1. `sources/2026-W33/drafting/v2/luna-r1/**`
2. `sources/2026-W33/execution/sessions/w33-luna-draft-candidate-set-20260831-r1.md`

No other repository path may change.

## Protected / forbidden writes

Do not modify:

- `sources/2026-W33/production-state.json`
- `sources/2026-W33/production-profile.json`
- `sources/2026-W33/gates/**`
- `sources/2026-W33/orchestration/**`
- `sources/2026-W33/architecture-v2.json`
- `sources/2026-W33/architecture-review-summary-v2.json`
- `sources/2026-W33/architecture-review-attention-v2.json`
- `sources/2026-W33/candidate-matrix-v2.json`
- `sources/2026-W33/candidate-selection-v2.json`
- accepted Discovery/Screening/Evidence/View/Materiality/Completeness authority
- `config/**`
- `schemas/**`
- `scripts/**`
- `.github/**`
- shared docs/Core authority
- execution recovery index
- operator requests/bridge runs

## Stop conditions

Stop `NEEDS_SOL_REVIEW` without unauthorized repair if:

- remote HEAD != caller Exact Starting SHA before first write;
- current State does not satisfy the mandatory Draft-stage preconditions;
- Architecture Approval does not validate against the exact current Architecture/Review Summary/Attention bytes;
- a derived Draft Package cannot be produced canonically;
- the seven-package set cannot be derived without changing approved Architecture semantics;
- deterministic Draft validators expose a shared Core defect rather than a Draft content defect;
- a desired editorial statement requires new factual research/Evidence;
- cross-package synthesis cannot be completed from the canonically supplied Evidence;
- any sixth/eighth package or synthetic candidate appears necessary;
- any write outside the allowlist would be required;
- Production State or accepted upstream authority would need modification.

Do not solve these conditions by changing shared Core or upstream accepted bytes.

## Normal endpoint

On success, commit the candidate artifacts and Luna session on the existing branch using normal non-force updates.

Stop at:

`DRAFT_CANDIDATE_SET_READY_FOR_SOL_REVIEW`

Do not perform `ADVANCE_STAGE`.
Do not create the Draft Stage Checkpoint.
Do not begin reader-manuscript/publication validation.
Do not create a Publication Candidate.
Do not approach the Publication Preview Human Gate in this task.
