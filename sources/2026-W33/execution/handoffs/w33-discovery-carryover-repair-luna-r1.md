# 2026-W33 Sol→Luna handoff — five-carry-over Discovery authority repair r1

Status: `READY_FOR_LUNA / DISCOVERY_REPAIR_PROPOSAL_ONLY / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at specification time: `ISSUE_INITIALIZED`  
Current machine next action: `stage:discovery`  
Architecture Review r2 decision: `REQUEST_CHANGES`  
Regeneration boundary: `ISSUE_INITIALIZED`

The caller supplies the exact branch SHA containing this handoff. Luna must verify that the remote branch HEAD equals that exact SHA before any write. If it does not, write nothing and stop with the actual remote HEAD.

## 1. Objective

Repair **Discovery source authority for exactly five existing W32 carry-over records** so that their later W33 Evidence work may use fresh first-party authority instead of only the prior-week Selection document.

This is a bounded Discovery repair proposal. It is **not** a new general Discovery pass.

The worker endpoint is:

`DISCOVERY_CARRYOVER_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

Do not advance lifecycle state. Do not create a Discovery acceptance/checkpoint. Do not regenerate Screening/Evidence/Selection/Architecture in this task.

## 2. Human revision authority

The Owner's Architecture Review r2 is recorded at:

- `sources/2026-W33/gates/reviews/architecture-r2.json`
- decision: `REQUEST_CHANGES`
- regeneration boundary: `ISSUE_INITIALIZED`

Required downstream outcomes from that Human review are:

1. repair Discovery source authority for the five active W32 carry-over obligations;
2. re-run the affected downstream pipeline from Discovery using the repaired basis;
3. later regenerate Architecture with an explicit mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
4. preserve the previously Owner-accepted six substantive packages, 28-candidate placement strategy, 18-page target / 24-page hard cap, and Agent Reliability comparative-synthesis constraint unless newly accepted evidence justifies a downstream change.

This Luna task performs only item 1.

## 3. Required authority reads

Read before writing:

1. reviewed-main `AGENTS.md`;
2. reviewed-main `docs/survey-production-core-v2-session-bootstrap.md`;
3. reviewed-main `docs/survey-production-core-v2-execution-record-policy.md`;
4. reviewed-main `scripts/survey_discovery_v2.py`;
5. reviewed-main Discovery schema(s) used by the current 2.0-rc1 runtime;
6. `sources/2026-W33/production-profile.json`;
7. `sources/2026-W33/production-state.json`;
8. `sources/2026-W33/discovery/discovery-v2.jsonl`;
9. `sources/2026-W33/external/x/x-source-intake-v2.json`;
10. `sources/2026-W33/gates/reviews/architecture-r1.json`;
11. `sources/2026-W33/gates/reviews/architecture-r2.json`;
12. `sources/2026-W33/execution/reviews/w33-owner-architecture-review-findings-20260830-r1.md`;
13. `sources/2026-W33/execution/reviews/w33-architecture-revision-boundary-sol-correction-20260830-r1.md`;
14. reviewed-main `sources/2026-W32/candidate-matrix-v0.2.md` and `sources/2026-W32/candidate-selection-v0.1.md` only as historical carry-over context, not as the new first-party authority.

## 4. Frozen repair scope

The final Discovery set must remain exactly **41 records with the same 41 `discovery_id` values**.

Only these five records may be semantically edited:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

All other 36 Discovery records must remain byte-for-byte semantically unchanged. Preserve their order and serialized JSON objects exactly when practical; at minimum, their parsed JSON objects must compare exactly equal before/after.

`base-official-index-minimax-news` is **not** part of this repair and must remain unchanged.

For each of the five target records, preserve exactly unless current schema validation proves impossible:

- `schema_version`;
- `issue_id`;
- `discovery_id`;
- `provenance.origin = CARRY_OVER`;
- `provenance.research_pass`;
- `provenance.parent_refs`;
- `provenance.obligation_ids`, including `weekly:carry-over`.

The intended repair is the **source authority and source-local description/timing**, not the identity or obligation graph.

## 5. First-party source allowlist

External research is allowed **only** for the five targets below, using the named first-party surfaces. Do not browse for additional W33 topics. Do not use X, Reddit, news articles, aggregators, mirrors, vendor comparison blogs, search-result snippets, or secondary commentary as technical evidence.

### 5.1 `carry-w32-claude-retirement`

Primary source:

- `https://platform.claude.com/docs/en/about-claude/model-deprecations`

Bounded fact to recover:

- Anthropic's deprecation history states that Claude Opus 4.1 (`claude-opus-4-1-20250805`) was retired on **2026-08-05**;
- the deprecation was announced to affected API developers on 2026-06-05;
- the recommended replacement shown by Anthropic is Claude Opus 4.8.

Do not infer anything about Copilot or other third-party availability from this source.

### 5.2 `carry-w32-copilot-cloud-agent`

Primary sources:

- `https://github.blog/changelog/2026-08-03-customize-the-reasoning-level-for-copilot-cloud-agent/`
- `https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/`

Bounded facts to recover:

- GitHub published concrete Copilot cloud-agent updates on **2026-08-03**;
- reasoning level can be selected for supporting models when delegating a cloud-agent task;
- Copilot automations can be triggered from issue/PR comments, subject to the plan/policy constraints stated by GitHub.

The old W32 shorthand was under-specified. Repair it to the narrower first-party-confirmed W32 cloud-agent update. Do not aggregate older June/July features into a supposed single August launch.

### 5.3 `carry-w32-kimi-k3-copilot`

Primary source:

- `https://github.blog/changelog/2026-08-06-kimi-k3-is-now-available-in-github-copilot/`

Optional first-party corroboration only if useful:

- `https://github.blog/changelog/2026-08-13-github-copilot-weekly-releases-august-10/`

Bounded facts to recover:

- GitHub states that Kimi K3 became available in GitHub Copilot on **2026-08-06**;
- the page records the temporary rollout pause and resumed rollout in editor notes;
- GitHub lists the Copilot surfaces/plans where rollout occurs and notes administrator policy requirements for Business/Enterprise.

Do not import Moonshot/model benchmark claims unless the GitHub page itself attributes them and they are needed only for source-local context.

### 5.4 `carry-w32-openai-gpt56-update`

Primary sources:

- `https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/`
- `https://deploymentsafety.openai.com/gpt-5-6-august-update`

Bounded facts to recover:

- OpenAI published an **2026-08-06** ChatGPT update for GPT-5.6 Sol and expanded GPT-5.6 Luna access;
- the product page describes focused/reliability changes and the thought-effort control for Plus/Pro users;
- the Deployment Safety Hub identifies the August update and its scope/boundaries.

Do not rewrite this as the original GPT-5.6 model launch. The carry-over concerns a distinct August product/model-behavior update.

### 5.5 `carry-w32-repowise`

First-party project sources:

- `https://github.com/repowise-dev/repowise`
- `https://github.com/repowise-dev/repowise-bench`
- `https://github.com/repowise-dev/repowise-bench/blob/master/BENCHMARK_REPORT_FLASK_V3.md`
- `https://github.com/repowise-dev/repowise-bench/blob/master/repro/README.md`

Bounded facts to recover:

- the project/repository identity and actual tool surface;
- the project's own benchmark methodology for agent-efficiency claims;
- the paired same-model/same-harness nature of the reported comparisons where directly documented;
- project-reported reductions in tool calls/files read/tokens only with exact methodology and caveats attached;
- explicit limitations such as judge noise, benchmark/repository scope, and the distinction between retrieval/work reduction and general task success.

Treat all benchmark numbers as **project-reported**, not independently reproduced. Do not promote project marketing wording into independent performance fact.

## 6. Raw capture contract

Create concise source-local captures under exactly:

`sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/`

Use stable filenames such as:

- `anthropic-claude-opus-4-1-deprecation.md`
- `github-copilot-cloud-agent-reasoning.md`
- `github-copilot-automations-comments.md`
- `github-kimi-k3-copilot.md`
- `openai-gpt-5-6-chatgpt-august-update.md`
- `openai-gpt-5-6-august-safety-update.md`
- `repowise-project.md`
- `repowise-benchmark.md`
- `repowise-flask-v3.md`
- `repowise-reproduction.md`

A capture may be omitted if genuinely redundant, but each of the five target Discovery records must bind at least one new first-party Raw capture.

Each Raw capture must contain only:

- exact source URL;
- source/page title;
- retrieval timestamp in UTC;
- explicit event/publication/update date if the source states one;
- concise source-local observations required for the Discovery record;
- direct attribution of vendor/project claims;
- important limitations/boundaries.

Do not create long mirrors of entire pages.

Use:

- `collector_id = sol-approved-carryover-repair`
- `collector_run_id = w33-five-carryover-r1`

## 7. Target Discovery record repair rules

For each target record:

1. retain the same `discovery_id` and carry-over provenance graph;
2. replace the prior-week-only `source.locator` with the strongest first-party locator above;
3. replace/add `source.raw_paths` so the target binds the new first-party Raw capture(s);
4. set `source.collector_id` / `source.collector_run_id` to the repair collector identifiers above;
5. minimally revise title/summary/timing/window relation only as needed to accurately reflect the fresh first-party record;
6. preserve the distinction between an event established by the source and any still-unresolved claim;
7. do not decide Materiality, Selection, Architecture role, or publication prominence here.

A first-party source that proves the alleged event **did not occur as originally framed** is a valid repair outcome. In that case preserve the carry-over record but rewrite its Discovery summary to the exact negative/chronology finding rather than inventing a positive event.

## 8. Expected findings if sources remain as Sol prechecked

These are verification expectations, not authority substitutes. Luna must independently contact/read the named first-party sources.

Expected source-local outcome:

- Claude Opus 4.1 retirement: **first-party event established** for 2026-08-05;
- GitHub Copilot cloud-agent August update: **first-party W32 update established**, but narrower than the old shorthand;
- Kimi K3 in GitHub Copilot: **first-party event established** for 2026-08-06;
- GPT-5.6 August update: **first-party distinct August update established** for 2026-08-06, not original launch;
- RepoWise: **first-party project/method evidence established**; performance claims remain project-reported and must retain methodology limitations.

If any source is unavailable or contradicts these expectations, do not force the expected result. Record the actual source-local outcome and flag it for Sol review.

## 9. Validation before commit

Before committing, require all of the following:

1. `production-state.json` remains byte-identical to task start and lifecycle remains `ISSUE_INITIALIZED`;
2. Discovery JSONL parses;
3. exactly 41 unique `discovery_id` values remain;
4. the exact set of 41 IDs is unchanged;
5. parsed JSON objects for all 36 non-target records are exactly equal before/after;
6. the five target records retain their frozen provenance identity fields from section 4;
7. every `source.raw_paths` path exists;
8. the existing X Source Intake remains valid and unchanged;
9. run `scripts.survey_discovery_v2.build_acceptance(...)` only to a temporary non-repository output (or equivalent no-write validation) and require PASS;
10. no Discovery acceptance/checkpoint is committed;
11. no shared Core file is modified;
12. no non-allowlisted file is modified.

## 10. Write allowlist

Only these writes are allowed:

1. `sources/2026-W33/discovery/discovery-v2.jsonl`
2. files under `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/`
3. `sources/2026-W33/execution/sessions/w33-luna-discovery-carryover-repair-20260830-r1.md`

No other path may change.

In particular, do not modify:

- `sources/2026-W33/production-state.json`;
- `sources/2026-W33/external/x/x-source-intake-v2.json` or any X Raw;
- any `discovery-accepted-v2.json`;
- any Screening/Evidence/View/Materiality/Completeness/Selection/Architecture artifact;
- any checkpoint;
- any Human Gate record/index;
- any Core/config/schema file;
- `sources/2026-W33/execution/index.md`.

## 11. Commit shape

Preferred:

1. one commit containing the repaired Discovery JSONL plus new Raw captures;
2. one final bookkeeping commit containing only the Luna session record.

Both commits must use normal fast-forward branch updates (`force=false`).

## 12. Luna session record

The session record must state:

- supplied Starting SHA and verified remote Starting SHA;
- Ending SHA;
- reviewed-main SHA;
- initial/final Production State SHA-256 and byte-identity result;
- exact five target IDs;
- proof that the other 36 parsed Discovery records were unchanged;
- Discovery record count and exact ID-set equality result;
- first-party URL(s) contacted for each target;
- Raw capture path(s) and SHA-256 for each target;
- concise source-local finding for each target;
- any expected-vs-observed discrepancy;
- temporary Discovery acceptance validation result;
- X manifest unchanged/valid result;
- changed-path allowlist result;
- confirmation that no lifecycle advancement or downstream regeneration occurred.

## 13. Stop conditions

Stop without repository writes if the starting remote HEAD does not equal the supplied Exact Starting SHA.

After work begins, stop with `NEEDS_SOL_REVIEW` rather than broadening scope if:

- a named first-party source is inaccessible and no other explicitly allowed first-party source establishes the target;
- a target would require a new Discovery ID;
- a non-target Discovery object would need semantic editing;
- current reviewed-main schema conflicts with this handoff;
- the exact 41-ID set cannot be preserved;
- temporary Discovery acceptance validation fails for a reason that requires changing non-target authority or shared Core.

## 14. Success condition

Success is exactly:

`DISCOVERY_CARRYOVER_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

At success, State must still be `ISSUE_INITIALIZED / stage:discovery` and no checkpoint may have been created.
