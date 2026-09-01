# 2026-W33 Sol→Luna handoff — revised Screening from repaired Discovery r1

Status: `READY_FOR_LUNA / SCREENING_REVISION_PROPOSAL_ONLY / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at specification time: `DISCOVERY_COLLECTED`  
Current machine next action: `stage:screening`

The caller supplies the exact branch SHA containing this handoff. Luna must verify remote branch HEAD equals that SHA before any write. If not, write nothing and stop with the actual remote HEAD.

## Objective

Create a fresh, complete Screening v2 accepted result-set whose package basis pins the current repaired Discovery and current `DISCOVERY_COLLECTED` State.

This task is Screening proposal/materialization only. Do not advance lifecycle state.

Success endpoint:

`SCREENING_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

## Frozen authority

Required reads before writing:

1. reviewed-main `AGENTS.md`
2. reviewed-main `docs/survey-production-core-v2-session-bootstrap.md`
3. reviewed-main `docs/survey-production-core-v2-execution-record-policy.md`
4. reviewed-main `scripts/survey_screening_v2.py`
5. reviewed-main `config/prompts/source-screening-v2.md`
6. reviewed-main `schemas/screening-v2-batch-result.schema.json`
7. `sources/2026-W33/production-profile.json`
8. `sources/2026-W33/production-state.json`
9. `sources/2026-W33/discovery/discovery-v2.jsonl`
10. `sources/2026-W33/discovery/discovery-accepted-v2.json`
11. `sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`
12. `sources/2026-W33/execution/reviews/w33-discovery-repair-advance-sol-review-20260830-r1.md`
13. historical accepted Screening:
   `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`
14. Architecture Review r2 authority and Owner findings, only to preserve future constraints; do not perform Architecture work.

Current repaired Discovery SHA-256:

`6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`

Current repaired Discovery acceptance SHA-256:

`777414eefad7280d45fc847dd44a0bdeeef225b6dd0c3e1f4b90bc8b1acb7995`

Current State must begin as:

- lifecycle `DISCOVERY_COLLECTED`
- next action `stage:screening`
- Discovery checkpoint passed
- Screening and later checkpoints pending

## Core constraint

Do not reuse the old accepted Screening package/result bytes as current authority. The current Screening package must be newly prepared from current State and repaired Discovery bytes because Core basis validation pins both hashes.

Core requires exactly one Screening decision for every Discovery record in the package. Therefore produce a complete 41-decision result set.

## Semantic delta policy

The historical 41-record Screening result-set is semantic precedent for the 36 Discovery records that were not changed by the repair.

For exactly those 36 non-target records:

- carry forward the historical decision object exactly, field-for-field, unless a purely mechanical package/basis constraint requires serialization changes outside the decision object;
- do not semantically reconsider or rewrite their decision/reason/scope tags/duplicate group/verification targets/confidence.

Only these five records may receive new Screening semantics:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

All five are frozen by Sol to `KEEP` with `high` confidence.

Expected final counts:

- KEEP 31
- INSPECT 3
- MAYBE 3
- DROP 4

If these counts do not result while all 36 non-target decisions are exact carry-forwards and all five target decisions use the frozen semantics below, stop for Sol review rather than changing additional records.

## Frozen revised decisions

Use the exact decision intent below. Wording may be normalized only if the Screening schema requires it, but do not change semantic content.

### `carry-w32-claude-retirement`

- decision: `KEEP`
- reason: Anthropic first-party documentation establishes the exact Claude Opus 4.1 retirement chronology and affected Anthropic-platform scope, so the carry-over is sufficiently grounded for Evidence verification.
- scope_tags: `carry-over`, `model-lifecycle`
- duplicate_group: null
- verification_targets:
  - verify the August 5 retirement versus June 5 deprecation chronology;
  - preserve Anthropic-operated versus partner-operated platform scope;
  - determine later whether this is W33 materiality, carry-over closure, or contextual disposition.
- confidence: `high`

### `carry-w32-copilot-cloud-agent`

- decision: `KEEP`
- reason: GitHub first-party August 3 changelogs establish concrete cloud-agent updates for reasoning-level control and comment-triggered automations, resolving the prior source-identity uncertainty.
- scope_tags: `carry-over`, `coding-agents`, `developer-tools`
- duplicate_group: null
- verification_targets:
  - verify exact feature/plan/admin-policy boundaries;
  - keep the August update separate from older June/July cloud-agent features;
  - determine later whether it is current W33 materiality or carry-over closure/context.
- confidence: `high`

### `carry-w32-kimi-k3-copilot`

- decision: `KEEP`
- reason: GitHub first-party changelog establishes Kimi K3 Copilot availability, rollout/resumption, named surfaces, and administrator-policy boundaries, making the carry-over suitable for Evidence verification.
- scope_tags: `carry-over`, `frontier-models`, `developer-tools`
- duplicate_group: null
- verification_targets:
  - verify rollout date, pause/resumption, surfaces/plans, hosting/billing, and admin-policy scope;
  - do not import independent Kimi benchmark claims;
  - determine later whether the pre-window event is material, contextual, or simply closes the carry-over obligation.
- confidence: `high`

### `carry-w32-openai-gpt56-update`

- decision: `KEEP`
- reason: OpenAI first-party product and Deployment Safety pages establish a distinct August 6 GPT-5.6 Sol/Luna ChatGPT update, resolving the prior chronology uncertainty and justifying Evidence verification.
- scope_tags: `carry-over`, `frontier-models`
- duplicate_group: null
- verification_targets:
  - distinguish the August 6 ChatGPT update from the original GPT-5.6 launch;
  - preserve the explicit Work/Codex unchanged boundary;
  - keep product/reliability/safety figures OpenAI-attributed;
  - determine later the correct W33 materiality/context disposition.
- confidence: `high`

### `carry-w32-repowise`

- decision: `KEEP`
- reason: Repowise first-party project and benchmark repositories establish project identity, tool surface, benchmark/reproduction methodology, and bounded project-reported work-reduction claims, providing sufficient basis for Evidence verification even though publication timing/materiality remains a later question.
- scope_tags: `carry-over`, `coding-agents`, `developer-tools`
- duplicate_group: null
- verification_targets:
  - verify benchmark/run chronology and exact methodological scope;
  - retain small-n, judge-noise, caching, credential, and repository/task-scope limitations;
  - distinguish retrieval/work reduction from general task success;
  - treat all performance claims as project-reported and determine later whether the item is W33 material or carry-over context only.
- confidence: `high`

## Required procedure

1. Verify the exact starting remote HEAD before any write.
2. Prepare a new Screening package from current `production-state.json` and repaired `discovery-v2.jsonl` using the canonical Core helper/runtime and current work-branch implementation identity under the same agent-first basis handling already used in W33.
3. Confirm package basis pins:
   - current profile SHA;
   - current State SHA;
   - repaired Discovery SHA `6e6590b5...`;
   - current prompt/result-contract hashes.
4. Construct exactly one result decision per all 41 Discovery IDs.
5. Copy the 36 historical non-target decision objects exactly from historical accepted Screening.
6. Replace only the five target decision objects using the frozen decisions above.
7. Validate result batch(es) against the new package.
8. Accept the result set with canonical `survey_screening_v2.accept_results(...)` into `sources/2026-W33/screening/v2/accepted/<new-result-set-sha>/`.
9. Re-run canonical acceptance validation against the accepted result.
10. Verify final counts exactly KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4.
11. Write a Luna session record and stop for Sol review.

## Historical immutability

Do not modify or delete the historical accepted Screening directory:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`

The new accepted Screening run must have a different content-addressed result-set SHA because its package basis and five decisions differ.

## Write allowlist

Allowed writes only:

1. a new Screening work/run directory if required by canonical prepare/accept helpers;
2. a new content-addressed accepted Screening directory under:
   `sources/2026-W33/screening/v2/accepted/<new-result-set-sha>/`
3. `sources/2026-W33/execution/sessions/w33-luna-screening-revision-20260830-r1.md`

If the canonical W33 runtime convention uses a transient unaccepted run path, include it only if necessary and document it; do not overwrite historical accepted runs.

Do not modify:

- `sources/2026-W33/production-state.json`
- repaired Discovery JSONL or acceptance
- X Source Intake
- any checkpoint
- any Evidence/View/Materiality/Completeness/Selection/Architecture artifact
- Human Gate records
- shared Core/config/schema/prompt files
- `sources/2026-W33/execution/index.md`

Do not call `ADVANCE_STAGE`.

## Validation requirements

Before final commit/session record, verify:

- Starting remote SHA exact match: PASS
- State remains byte-identical and `DISCOVERY_COLLECTED / stage:screening`
- repaired Discovery SHA remains `6e6590b5...`
- repaired Discovery acceptance remains valid and unchanged
- new Screening package basis matches current State/Discovery
- 41 unique Discovery IDs represented exactly once
- 36 non-target decisions exact equality to historical acceptance
- 5 target decisions exactly match frozen Sol semantics
- counts KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4
- new accepted run validates canonically
- historical accepted Screening run unchanged
- changed paths remain within allowlist
- no lifecycle advancement

## Session record

Record:

- supplied and verified Starting SHA
- Ending SHA
- reviewed-main SHA
- initial/final State SHA-256 and byte identity
- new package SHA-256
- new result-set SHA-256
- new acceptance path and SHA-256
- batch/input/result hashes
- exact 41-decision counts
- proof of 36 non-target exact carry-forward
- the five revised decisions
- historical accepted run unchanged proof
- canonical validation result
- changed-path allowlist result
- explicit confirmation that `ADVANCE_STAGE` was not run

## Stop conditions

Stop with `NEEDS_SOL_REVIEW` instead of broadening scope if:

- current remote HEAD differs from supplied Starting SHA;
- current State is not `DISCOVERY_COLLECTED / stage:screening`;
- repaired Discovery or acceptance hashes drift;
- Core cannot prepare a fresh package without modifying protected authority;
- 36 historical non-target decisions cannot be carried forward exactly;
- a sixth record appears to require semantic Screening change;
- the five frozen decisions do not validate;
- expected counts do not result;
- canonical acceptance validation fails.

## Success condition

Success is exactly:

`SCREENING_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

At success, State remains `DISCOVERY_COLLECTED / stage:screening`, Screening checkpoint remains pending, and no downstream stage has begun.
