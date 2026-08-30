# W33 Luna revised Screening r1

Status: `SCREENING_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Branch: `weekly/2026-W33-v2-work`  
Worker: Luna bounded Screening revision  
Recorded: `2026-08-30T11:43:53Z`

## Starting authority

- Supplied Exact Starting SHA: `c58f5a7e9300ce02ba14eba1ec73a8e00c0137f6`
- GitHub remote branch HEAD verified before any repository write: `c58f5a7e9300ce02ba14eba1ec73a8e00c0137f6`
- Owner instruction followed: clone the specified branch HEAD before starting work; clone-immediate local HEAD and origin tracking HEAD both matched the supplied SHA.
- Reviewed `main` SHA: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Handoff: `sources/2026-W33/execution/handoffs/w33-screening-revision-luna-r1.md`
- Lifecycle at start: `DISCOVERY_COLLECTED`
- Machine next action at start: `stage:screening`
- Current Production State SHA-256 and size: `6ef1fb8724989ed69251bef0a77421339933133feccb21781fa688f0b17f997d` / 3042 bytes

The candidate materialization commit was pushed through the authenticated GitHub connection with `force=false`:

- Candidate commit: `5a8d0e93b1d1c8875b2e1aed33a365897890c807`
- Candidate commit parent: `c58f5a7e9300ce02ba14eba1ec73a8e00c0137f6`

The final bookkeeping commit SHA is reported by remote-ref readback and is intentionally not self-embedded in this record because a Git commit cannot contain its own object ID.

## Frozen scope and inputs

This was a Screening revision proposal only. No new source investigation, Discovery materialization, semantic change outside the five handoff targets, lifecycle advancement, or Human Gate operation was performed.

- Repaired Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Repaired Discovery SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- Repaired Discovery record count: `41`
- Repaired Discovery acceptance SHA-256: `777414eefad7280d45fc847dd44a0bdeeef225b6dd0c3e1f4b90bc8b1acb7995`
- Historical accepted Screening result-set: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- Historical acceptance SHA-256: `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`

The 36 non-target decision objects were copied field-for-field from the historical accepted `screening-accepted.json`. Only the following five decision objects were replaced, using the Sol-frozen semantics from the handoff:

### `carry-w32-claude-retirement`

- decision: `KEEP`
- reason: Anthropic first-party documentation establishes the exact Claude Opus 4.1 retirement chronology and affected Anthropic-platform scope, so the carry-over is sufficiently grounded for Evidence verification.
- scope_tags: `carry-over`, `model-lifecycle`
- duplicate_group: `null`
- verification_targets:
  - verify the August 5 retirement versus June 5 deprecation chronology;
  - preserve Anthropic-operated versus partner-operated platform scope;
  - determine later whether this is W33 materiality, carry-over closure, or contextual disposition.
- confidence: `high`

### `carry-w32-copilot-cloud-agent`

- decision: `KEEP`
- reason: GitHub first-party August 3 changelogs establish concrete cloud-agent updates for reasoning-level control and comment-triggered automations, resolving the prior source-identity uncertainty.
- scope_tags: `carry-over`, `coding-agents`, `developer-tools`
- duplicate_group: `null`
- verification_targets:
  - verify exact feature/plan/admin-policy boundaries;
  - keep the August update separate from older June/July cloud-agent features;
  - determine later whether it is current W33 materiality or carry-over closure/context.
- confidence: `high`

### `carry-w32-kimi-k3-copilot`

- decision: `KEEP`
- reason: GitHub first-party changelog establishes Kimi K3 Copilot availability, rollout/resumption, named surfaces, and administrator-policy boundaries, making the carry-over suitable for Evidence verification.
- scope_tags: `carry-over`, `frontier-models`, `developer-tools`
- duplicate_group: `null`
- verification_targets:
  - verify rollout date, pause/resumption, surfaces/plans, hosting/billing, and admin-policy scope;
  - do not import independent Kimi benchmark claims;
  - determine later whether the pre-window event is material, contextual, or simply closes the carry-over obligation.
- confidence: `high`

### `carry-w32-openai-gpt56-update`

- decision: `KEEP`
- reason: OpenAI first-party product and Deployment Safety pages establish a distinct August 6 GPT-5.6 Sol/Luna ChatGPT update, resolving the prior chronology uncertainty and justifying Evidence verification.
- scope_tags: `carry-over`, `frontier-models`
- duplicate_group: `null`
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
- duplicate_group: `null`
- verification_targets:
  - verify benchmark/run chronology and exact methodological scope;
  - retain small-n, judge-noise, caching, credential, and repository/task-scope limitations;
  - distinguish retrieval/work reduction from general task success;
  - treat all performance claims as project-reported and determine later whether the item is W33 material or carry-over context only.
- confidence: `high`

## Canonical Screening materialization

The repository's canonical `run_screening_v2_interactive.py` runner was used with the agent-first `current_stage_basis_override()`. It prepared a fresh package from the current State and repaired Discovery, created one batch for all 41 records, materialized one result per Discovery ID, called `survey_screening_v2.accept_results(...)`, and performed no State transition.

New accepted run:

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/`

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| `package.json` | `047f595c0b8216a780c4b5c11d9e0cfa9a263e5ec35aa4287f15aae82bdfbd46` | 1749 |
| `input/batches/batch-001.jsonl` | `85577066e4120b402847b6715cab87a556a1b53d3baa3ce9ccf4be0952ba2ffd` | 44326 |
| `results/batch-001.json` | `148a6e072cde004d652a3fedb6523529f7668b9081e5b593d0b3861717034200` | 23300 |
| `screening-accepted.json` | `e6f0392004191b4668e4231c57839044e4b08ff1e32763403f2d92630b0b0a0f` | 23237 |
| `interactive-decisions.json` | `8bb149eb3a206d9043b3507423eeffddf2b5cc4889bc052508da9159836d96ad` | 22888 |
| `interactive-audit.json` | `2a7004be40c7cc62a2d1f1fd663001cbbea6fe214722c2e118735e1caa8e7857` | 835 |

The new content-addressed result-set identity is:

`0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a`

Package basis:

- profile SHA-256: `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`
- State SHA-256: `6ef1fb8724989ed69251bef0a77421339933133feccb21781fa688f0b17f997d`
- repaired Discovery SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- prompt SHA-256: `3e45900ead73688eab8734036e6e476c1ec4f1a7ce38da42d5ca52a68ef0a862`
- result-contract SHA-256: `a05b65b41efbcaf654df5c3c5944254a76d93d8a28cab961f2c06f6d580da5a2`

## Validation

- Starting remote SHA exact match before write: `PASS`
- Current State remained byte-identical: `PASS` — initial/final SHA-256 `6ef1fb8724989ed69251bef0a77421339933133feccb21781fa688f0b17f997d`, 3042 bytes
- Lifecycle and next action remained `DISCOVERY_COLLECTED / stage:screening`: `PASS`
- Repaired Discovery hash and 41-record coverage: `PASS`
- Repaired Discovery acceptance canonical validation and unchanged hash: `PASS`
- New Screening package basis matched current profile, State, repaired Discovery, prompt, and result contract: `PASS`
- Canonical accepted Screening validation through `survey_screening_v2.validate_acceptance(...)` under `current_stage_basis_override()`: `PASS`
- New result-set directory name matched `result_set_sha256`: `PASS`
- Exactly 41 unique Discovery IDs, each represented once: `PASS`
- 36 non-target decision objects exact-equal to historical acceptance: `PASS`
- Only the five named target decision objects differed: `PASS`
- Five target decisions all `KEEP` / `high`: `PASS`
- Final counts: `KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4`: `PASS`
- Historical accepted Screening directory remained unchanged; its acceptance SHA-256 remained `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`: `PASS`
- No Screening checkpoint was recorded: `PASS`
- `ADVANCE_STAGE` was not executed: `PASS`
- No Evidence, Edition View, Materiality, Completeness, Selection, Architecture, Human Gate, or shared-Core artifact was changed: `PASS`

## Deviations / failures

- The first equivalent direct-script invocation failed before helper execution because the repo root was not on Python's module path (`ModuleNotFoundError: No module named 'scripts'`). The same canonical runner was then invoked from the repo root as a module.
- The module invocation initially reported the environment-only absence of `jsonschema`. The exact repository requirements were installed under `/tmp/w33-screening-revision-pydeps`; no repository dependency, config, schema, or script was modified.
- No semantic or scope broadening was performed in response to either environment issue.

## Changed paths and commit boundary

Candidate materialization commit `5a8d0e93b1d1c8875b2e1aed33a365897890c807` contains exactly these six allowlisted accepted-run files:

1. `sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/package.json`
2. `sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/input/batches/batch-001.jsonl`
3. `sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/results/batch-001.json`
4. `sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json`
5. `sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/interactive-decisions.json`
6. `sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/interactive-audit.json`

The follow-on bookkeeping commit adds only this session record. No protected or non-allowlisted path is part of this task.

## End state

- Stop condition: `SCREENING_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`
- State remains `DISCOVERY_COLLECTED / stage:screening`.
- Screening checkpoint remains pending; the new accepted run is a Sol-review candidate, not a lifecycle advancement.
- Sol review is required before any Screening checkpoint advancement or downstream Evidence work.
- `ADVANCE_STAGE` was not run.
