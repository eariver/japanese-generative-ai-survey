# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `ISSUE_INITIALIZED`
- Current machine action: `stage:discovery`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Human Architecture Review history: r1 `REQUEST_CHANGES`, r2 `REQUEST_CHANGES`
- Active regeneration boundary: `ISSUE_INITIALIZED`
- Drafting/publication remains unauthorized.

Architecture Review r2 rolled the run back to `ISSUE_INITIALIZED` because fresh first-party repair of five W32 carry-over obligations had to enter through Discovery authority. The Core rollback completed successfully and all machine checkpoints are currently pending.

## Human revision authority

Formal r2 review:

`sources/2026-W33/gates/reviews/architecture-r2.json`

Decision:

- `REQUEST_CHANGES`
- regeneration boundary: `ISSUE_INITIALIZED`

Owner-required downstream outcomes:

1. repair Discovery source authority for the five active W32 carry-over obligations;
2. rerun downstream Core stages from repaired Discovery;
3. regenerate Architecture with an explicit mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
4. preserve the previously accepted six substantive packages, 28-candidate placement strategy, target 18 pages / hard maximum 24 pages, and Agent Reliability comparative-synthesis constraint unless newly accepted evidence justifies a change.

## Repaired Discovery authority — Sol accepted

Luna repair range:

`457c75a923a459f31733e8cb4a1b8c5d159f39a7 -> b7df5119bf1e6622fca30f6fbfc85113ecb17583 -> 41bbee74dc14b99369afbeeffaa4f2e84397ba7a`

Repaired Discovery:

- path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- records: 41
- exact Discovery ID set unchanged
- non-target parsed records unchanged: 36/36

Exactly five records were rebound to fresh first-party authority:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

Accepted source-local outcomes:

- Claude Opus 4.1 retirement established for 2026-08-05 on Anthropic-operated platforms;
- concrete 2026-08-03 GitHub Copilot cloud-agent reasoning/comment-automation updates established, narrower than the old shorthand;
- Kimi K3 GitHub Copilot availability established for 2026-08-06 with rollout/policy boundaries;
- distinct 2026-08-06 GPT-5.6 Sol/Luna ChatGPT update established, not the original GPT-5.6 launch, with Work/Codex non-change preserved;
- Repowise project/tool and benchmark methodology established, with all performance claims retained as project-reported and no independent reproduction claim.

Luna session:

`sources/2026-W33/execution/sessions/w33-luna-discovery-carryover-repair-20260830-r1.md`

Sol review:

`sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`

Decision:

`ACCEPT / FIVE_CARRYOVER_SOURCE_AUTHORITY_REPAIRED / HANDOFF_ORIGIN_TYPO_CORRECTED / APPROVED_FOR_DISCOVERY_ADVANCEMENT`

### Provenance correction

The repair handoff accidentally wrote that the five records should preserve `provenance.origin = CARRY_OVER`. The actual Starting Discovery authority has all five records as `GAP_FILL` with `weekly:carry-over` obligations. Luna correctly preserved the actual Starting provenance. This is a Sol handoff typo, not a worker defect. No provenance migration is required.

## X authority

X Source Intake remains byte-identical and COMPLETE:

- path: `sources/2026-W33/external/x/x-source-intake-v2.json`
- SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`

No X recollection is authorized for this revision.

## Stale Discovery acceptance

Current canonical path:

`sources/2026-W33/discovery/discovery-accepted-v2.json`

still binds the pre-repair Discovery SHA-256:

`632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`

It is therefore stale and must not be reused for the new checkpoint.

The next task must regenerate/replace it from the repaired Discovery SHA `6e6590b5...` plus unchanged X SHA `4e90919e...`, validate it under current reviewed-main Core, and then perform exactly one deterministic transition.

## Current Luna task

Handoff:

`sources/2026-W33/execution/handoffs/w33-discovery-repair-advance-luna-r1.md`

Objective:

`ISSUE_INITIALIZED -> DISCOVERY_COLLECTED`

only.

Required sequence:

1. regenerate and replace `discovery-accepted-v2.json` in an acceptance-materialization commit;
2. create request-only `w33-discovery-repair-advance-20260830-r1.json`;
3. dispatch through the canonical Core operator bridge;
4. verify new `ISSUE_INITIALIZED.json` checkpoint and `DISCOVERY_COLLECTED / stage:screening` State;
5. create the Luna session record;
6. stop before Screening.

Expected Luna success status:

`DISCOVERY_COLLECTED_READY_FOR_SOL_SCREENING_POLICY`

## Historical downstream artifacts

Pre-r2 Screening/Evidence/View/Materiality/Completeness/Selection/Architecture artifacts remain in the repository for history/provenance but are no longer checkpoint authority after the r2 rollback. They must not be mechanically treated as current results.

Notable historical identities include:

- old Screening result-set: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- old Evidence result-set: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- old repaired View-set: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- old Completeness: `INCOMPLETE`
- old Selection: SELECTED 28 / HOLD 6 / REJECT 3
- old Architecture: six substantive packages, target 18 pages / cap 24 pages

The revision must rerun affected stages from the new Discovery checkpoint and explicitly dispose the five carry-over obligations from the repaired first-party basis.

## Architecture requirements that must survive regeneration

Preserve unless newly accepted evidence justifies a change:

- the six substantive W33 packages;
- 28-candidate placement strategy;
- target 18 pages / hard maximum 24 pages;
- `w33-agent-evaluation-reliability` as comparative synthesis rather than candidate-by-candidate mini-articles.

Mandatory addition:

- an explicit independent `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter in every Weekly issue;
- it must summarize what changed across the week, why it matters, and what to watch next;
- it must be a formal Architecture element, not page-plan prose only.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/gates/review-index.json`
4. `sources/2026-W33/gates/reviews/architecture-r2.json`
5. `sources/2026-W33/execution/reviews/w33-architecture-revision-boundary-sol-correction-20260830-r1.md`
6. `sources/2026-W33/execution/reviews/w33-architecture-revision-r2-sol-review-20260830-r1.md`
7. `sources/2026-W33/execution/sessions/w33-luna-discovery-carryover-repair-20260830-r1.md`
8. `sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`
9. `sources/2026-W33/execution/handoffs/w33-discovery-repair-advance-luna-r1.md`
10. latest Luna repaired-Discovery advancement session, if any
11. latest Sol advancement verification, if any

Do not repeat the five-source research after it has been accepted merely because chat history is missing. Current semantic authority is the repaired 41-record Discovery basis above; the next operation is deterministic Discovery advancement only.
