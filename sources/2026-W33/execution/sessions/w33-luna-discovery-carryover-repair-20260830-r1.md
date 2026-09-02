# W33 Luna Discovery carry-over repair r1

Status: `DISCOVERY_CARRYOVER_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

Issue: `2026-W33`
Branch: `weekly/2026-W33-v2-work`
Worker: Luna bounded Discovery repair

## Starting authority

- Supplied Exact Starting SHA: `457c75a923a459f31733e8cb4a1b8c5d159f39a7`
- GitHub remote branch HEAD verified before any repository write: `457c75a923a459f31733e8cb4a1b8c5d159f39a7`
- Owner instruction followed: start from a new clone of the specified branch HEAD, then verify clone-immediate local HEAD, origin tracking HEAD, and `git ls-remote` branch HEAD before work.
- Reviewed-main SHA: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Handoff: `sources/2026-W33/execution/handoffs/w33-discovery-carryover-repair-luna-r1.md`
- Canonical repair commit pushed with `force=false`: `b7df5119bf1e6622fca30f6fbfc85113ecb17583`, parent `457c75a923a459f31733e8cb4a1b8c5d159f39a7`.
- Final bookkeeping commit SHA is reported by the final remote-ref readback. It is intentionally not self-embedded in this record because a Git commit cannot contain its own object ID.

## Frozen scope

Exactly these five existing Discovery records were repaired:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

The Discovery set remains 41 records with the exact same 41 `discovery_id` values. The other 36 parsed JSON objects are unchanged. `base-official-index-minimax-news` was not touched. No Discovery topic or ID was added.

The current records' parsed provenance identity was preserved exactly. In the starting JSONL, all five records use `provenance.origin = GAP_FILL` with `research_pass = 1`, empty `parent_refs`, and `weekly:carry-over` in `obligation_ids`; this existing schema-valid identity was retained rather than reclassifying the records to `CARRY_OVER` or changing their obligation graph.

## Required authority and bounded research

Read before writing, in handoff order: reviewed-main `AGENTS.md`; session bootstrap; execution-record policy; `survey_discovery_v2.py`; Discovery and acceptance schemas; W33 production profile; Production State; W33 Discovery JSONL; X Source Intake manifest; Architecture Review r1/r2; Owner findings; Sol boundary correction; and the specified W32 matrix/selection history.

Only the handoff-named first-party surfaces were contacted. No X, Reddit, news, aggregator, mirror, search-result snippet, or unrelated W33 topic was used as technical evidence. The optional GitHub Copilot weekly-release corroboration page was read but was not bound because the Kimi primary changelog was sufficient.

## Source-local findings and bindings

### `carry-w32-claude-retirement`

- First-party URL: https://platform.claude.com/docs/en/about-claude/model-deprecations
- Finding: Anthropic's deprecation history establishes the `claude-opus-4-1-20250805` retirement on 2026-08-05, the 2026-06-05 developer notification/deprecation date, and `claude-opus-4-8` as the recommended replacement.
- Boundary: the dates apply to Anthropic-operated platforms; partner-operated platforms may use different schedules. No third-party availability inference was made.
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/anthropic-claude-opus-4-1-deprecation.md`

### `carry-w32-copilot-cloud-agent`

- First-party URLs: https://github.blog/changelog/2026-08-03-customize-the-reasoning-level-for-copilot-cloud-agent/ and https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/
- Finding: GitHub establishes a narrower 2026-08-03 cloud-agent update: selectable reasoning levels for supported models, plus issue/PR-comment-triggered Copilot automations.
- Boundary: plan and administrator-policy limits remain attached; the older June/July cloud-agent features were not aggregated into an August launch claim.
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/github-copilot-cloud-agent-reasoning.md`
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/github-copilot-automations-comments.md`

### `carry-w32-kimi-k3-copilot`

- First-party URL: https://github.blog/changelog/2026-08-06-kimi-k3-is-now-available-in-github-copilot/
- Finding: GitHub establishes Kimi K3 availability in Copilot on 2026-08-06, with gradual rollout, a documented pause/resumption note, named Copilot plans/surfaces, and Business/Enterprise administrator-policy requirements.
- Boundary: the capture retains GitHub's hosting, provider-list-pricing, rollout, and governance claims only; no external model benchmark or Moonshot claim was imported.
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/github-kimi-k3-copilot.md`

### `carry-w32-openai-gpt56-update`

- First-party URLs: https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/ and https://deploymentsafety.openai.com/gpt-5-6-august-update
- Finding: OpenAI establishes a distinct 2026-08-06 GPT-5.6 Sol/Luna ChatGPT update: focused/reliability changes and effort control for Sol, expanded Luna access, and an August-specific safety/model-scope distinction.
- Boundary: this is not the original GPT-5.6 launch. OpenAI states that the Work/Codex versions are not changed by the ChatGPT release; product/safety evaluation figures remain OpenAI-attributed.
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/openai-gpt-5-6-chatgpt-august-update.md`
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/openai-gpt-5-6-august-safety-update.md`

### `carry-w32-repowise`

- First-party URLs: https://github.com/repowise-dev/repowise, https://github.com/repowise-dev/repowise-bench, https://github.com/repowise-dev/repowise-bench/blob/master/BENCHMARK_REPORT_FLASK_V3.md, and https://github.com/repowise-dev/repowise-bench/blob/master/repro/README.md
- Finding: the project repositories establish Repowise's codebase-intelligence identity and MCP/CLI tool surface, and establish a benchmark/reproduction method with pinned tasks, byte-identical prompts, same-setup arm comparisons, deterministic retrieval grading, and explicit audit controls.
- Boundary: all performance numbers remain project-reported. Retrieval/work reduction is not general task success; small n, judge noise, prompt caching, benchmark/repository scope, and credential requirements remain attached. No independent reproduction was performed.
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/repowise-project.md`
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/repowise-benchmark.md`
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/repowise-flask-v3.md`
- Raw: `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/repowise-reproduction.md`

## Raw capture integrity

All captures use `collector_id = sol-approved-carryover-repair` and `collector_run_id = w33-five-carryover-r1`. Retrieval timestamp in each capture: `2026-08-30T10:16:12Z`.

| Target | Raw path | SHA-256 | Bytes |
|---|---|---|---:|
| Claude | `.../anthropic-claude-opus-4-1-deprecation.md` | `ec7ea2bd5345615351dc195b58204fcd08889a4ece9b7ef765bffea36b0db160` | 1292 |
| Copilot cloud agent | `.../github-copilot-cloud-agent-reasoning.md` | `4862ba2341c338f1b0305fd6d221fb84600fcce81d2d821a308f68bac7be375f` | 1238 |
| Copilot cloud agent | `.../github-copilot-automations-comments.md` | `99dc408f4fcaa19ad5fcb88ecbf74d1e715aa9f94a9046028ccf7a98d9ae9ad8` | 1204 |
| Kimi | `.../github-kimi-k3-copilot.md` | `2f1b0eb5362735dbc417072cb40746bd778393e0e2b9a53a1d459c1089e87385` | 1597 |
| GPT-5.6 | `.../openai-gpt-5-6-chatgpt-august-update.md` | `9a7bc8583a7af49752c586e7ce7fc500472512a2e3caf61b0510806b9b766606` | 1526 |
| GPT-5.6 | `.../openai-gpt-5-6-august-safety-update.md` | `7c329c176d66039cde14a42e8a05d1e1359ad262f0fd04d15e5bbabebb2d1705` | 1599 |
| RepoWise | `.../repowise-project.md` | `c2eca79a9f3428dbe803de88347f551bd73ed475e78d5eb6f5c60ca3a2198f71` | 1821 |
| RepoWise | `.../repowise-benchmark.md` | `2b9ee5d764155d9da0e9f4a835061819aa67884addc24480b3e95816a483d473` | 1758 |
| RepoWise | `.../repowise-flask-v3.md` | `691cb0931c664569fb10f3a63f6be1fd79ef173d76bf972d155f068b6017189f` | 2205 |
| RepoWise | `.../repowise-reproduction.md` | `11deb9957593f3d540ce6de6dfd3f9323cd00fe7da73c72a8dec929e5630402d` | 1928 |

`.../` denotes `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/`.

## Discovery and invariant validation

- Starting Discovery JSONL SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Repaired Discovery JSONL SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- Discovery parse: PASS
- Record count: `41`
- Exact 41-ID set equality: PASS
- Non-target parsed-object equality: PASS for all 36 records
- Target frozen schema/issue/discovery/provenance identity: PASS for all five
- Every bound `source.raw_paths` exists as a regular file: PASS
- Temporary `scripts.survey_discovery_v2.build_acceptance(...)` plus validation, outside the repository: PASS
- No Discovery acceptance/checkpoint was written or committed

## Protected authority validation

- Production State initial SHA-256: `0f5b14d6f8afc85605fc621b88e9c4005f70e13e7dbc727f68dae2cc5ca4d56c`
- Production State final SHA-256: `0f5b14d6f8afc85605fc621b88e9c4005f70e13e7dbc727f68dae2cc5ca4d56c`
- Production State byte identity: PASS
- Production State lifecycle/next action: `ISSUE_INITIALIZED / stage:discovery`
- X Source Intake initial SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- X Source Intake final SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- X Source Intake byte identity and `COMPLETE` validation: PASS
- Screening, Evidence, Edition Views, Materiality, Completeness, Matrix, Selection, Architecture, Human Gate records/index, shared Core, and `execution/index.md`: unchanged
- `ADVANCE_STAGE`: not executed
- Human Gate decision: not made or recorded
- Regeneration boundary: not selected or recorded by Luna
- Downstream regeneration: not performed

## Changed paths and commit boundary

Only these allowlisted paths changed before the session record:

1. `sources/2026-W33/discovery/discovery-v2.jsonl`
2. the 10 files under `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/`

The final bookkeeping commit adds only this session record. `git diff --check` passed for the repair commit and all changed paths are within the handoff allowlist.

## Expected versus observed

- All five expected source-local outcomes were observed: Claude retirement established; Copilot August cloud-agent update established with a narrower scope; Kimi Copilot availability established; GPT-5.6 distinct August update established rather than original launch; RepoWise project/method evidence established with project-reported limitations.
- The handoff's conceptual wording refers to these as carry-over records, while the current JSONL's actual schema-valid `provenance.origin` is `GAP_FILL`; this was preserved exactly and is surfaced for Sol review rather than silently normalized.

## End state and Sol handoff

- Stop condition: `DISCOVERY_CARRYOVER_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`
- State remains `ISSUE_INITIALIZED / stage:discovery`; no checkpoint was created.
- Sol review is required for the repaired Discovery basis and for the subsequent r2-directed downstream rerun. Luna made no Materiality, Selection, Architecture, Human Gate, or publication decision.
- Sol must retain the r2 requirements for downstream work, including explicit disposal of the five carry-over obligations and the mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` Architecture chapter.
