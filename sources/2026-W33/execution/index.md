# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `DISCOVERY_COLLECTED`
- Current machine action: `stage:screening`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Human Architecture Review history: r1 `REQUEST_CHANGES`, r2 `REQUEST_CHANGES`
- Active regeneration boundary: `ISSUE_INITIALIZED`
- Drafting/publication remains unauthorized.

Architecture Review r2 rolled the run back to `ISSUE_INITIALIZED` so five unresolved W32 carry-over obligations could receive fresh first-party Discovery authority. That repair has now been accepted and deterministically advanced to `DISCOVERY_COLLECTED`.

## Human revision authority

Formal r2 review:

`sources/2026-W33/gates/reviews/architecture-r2.json`

Decision:

- `REQUEST_CHANGES`
- regeneration boundary: `ISSUE_INITIALIZED`

Owner-required downstream outcomes:

1. close or explicitly dispose the five W32 carry-over obligations from fresh first-party authority;
2. rerun affected downstream stages;
3. regenerate Architecture with an explicit mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
4. preserve the previously accepted six substantive packages, 28-candidate placement strategy, target 18 pages / hard maximum 24 pages, and Agent Reliability comparative-synthesis constraint unless newly accepted evidence justifies a change.

## Current repaired Discovery authority

Discovery:

- path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- records: 41
- exact Discovery ID set unchanged from the original W33 set
- non-target parsed records unchanged: 36/36

Exactly five records were rebound to fresh first-party authority:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

Sol semantic review:

`sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`

Decision:

`ACCEPT / FIVE_CARRYOVER_SOURCE_AUTHORITY_REPAIRED / HANDOFF_ORIGIN_TYPO_CORRECTED / APPROVED_FOR_DISCOVERY_ADVANCEMENT`

The five records remain `provenance.origin = GAP_FILL` because that is the actual Starting Discovery authority. The earlier handoff text saying `CARRY_OVER` was a Sol typo; Luna correctly preserved repository authority.

## Current Discovery acceptance and checkpoint

Canonical acceptance:

- path: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- SHA-256: `777414eefad7280d45fc847dd44a0bdeeef225b6dd0c3e1f4b90bc8b1acb7995`
- repaired Discovery SHA: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- X Source Intake SHA: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- record count: 41

Advancement request:

`sources/2026-W33/execution/requests/w33-discovery-repair-advance-20260830-r1.json`

Event/request commit:

`46dc068b1d74a9c18d43b4712b2b6e73ee035186`

Bridge receipt:

`sources/2026-W33/execution/bridge-runs/w33-discovery-repair-advance-20260830-r1/receipt.json`

- status: PASS
- lifecycle: `DISCOVERY_COLLECTED`

Checkpoint:

`sources/2026-W33/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`

- checkpoint SHA-256: `54a6297242ec380df00ee0a19d86b689e4fe8fcdde37f928449633531c2697d2`
- Discovery checkpoint: passed
- Screening and all later checkpoints: pending

Luna session:

`sources/2026-W33/execution/sessions/w33-luna-discovery-repair-advance-20260830-r1.md`

Sol advancement verification:

`sources/2026-W33/execution/reviews/w33-discovery-repair-advance-sol-review-20260830-r1.md`

Decision:

`ACCEPT / STATE_TRANSITION_VERIFIED / REPAIRED_DISCOVERY_AUTHORITY_ESTABLISHED / READY_FOR_SCREENING_REVISION`

## Current Screening revision policy

Historical accepted Screening remains immutable history:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`

It cannot serve as the current Screening checkpoint because its package basis pins the pre-repair Discovery/State bytes.

Current handoff:

`sources/2026-W33/execution/handoffs/w33-screening-revision-luna-r1.md`

Required approach:

1. prepare a fresh Screening package from current `DISCOVERY_COLLECTED` State and repaired Discovery;
2. produce exactly 41 decisions as required by Core;
3. carry forward the historical decision objects exactly for the 36 non-target Discovery records;
4. revise only the five repaired carry-over records;
5. all five revised records are frozen to `KEEP` / confidence `high` by Sol;
6. accept a new content-addressed Screening result-set;
7. validate it canonically;
8. stop for Sol review without `ADVANCE_STAGE`.

Expected revised counts:

- KEEP 31
- INSPECT 3
- MAYBE 3
- DROP 4

The five repaired records move from historical `INSPECT` to `KEEP` because the prior `INSPECT` reason was insufficient source identity/content and that defect is now repaired. Screening is research-scope triage, not final Materiality. Temporal/materiality limitations must remain for Evidence/Materiality disposition.

Expected Luna success status:

`SCREENING_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

## Historical downstream authority

Pre-r2 Screening/Evidence/View/Materiality/Completeness/Selection/Architecture artifacts remain in the repository for history/provenance only until regenerated and re-checkpointed.

Notable historical identities:

- old Screening result-set: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- old Evidence result-set: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- old repaired View-set: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- old Completeness: `INCOMPLETE`
- old Selection: SELECTED 28 / HOLD 6 / REJECT 3
- old Architecture: six substantive packages, target 18 pages / cap 24 pages

Do not silently reuse these as current checkpoint authority.

## Architecture requirements that must survive regeneration

Preserve unless newly accepted evidence justifies change:

- six substantive W33 packages;
- 28-candidate placement strategy;
- target 18 pages / hard maximum 24 pages;
- `w33-agent-evaluation-reliability` as comparative synthesis.

Mandatory addition before the next Human Architecture Review:

- explicit independent `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
- summarize what changed across the week, why it matters, and what to watch next;
- formal Architecture element, not page-plan prose only.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this index
3. `sources/2026-W33/gates/reviews/architecture-r2.json`
4. `sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`
5. `sources/2026-W33/execution/sessions/w33-luna-discovery-repair-advance-20260830-r1.md`
6. `sources/2026-W33/execution/reviews/w33-discovery-repair-advance-sol-review-20260830-r1.md`
7. `sources/2026-W33/execution/handoffs/w33-screening-revision-luna-r1.md`
8. latest Luna revised-Screening session/result, if any
9. latest Sol review of revised Screening, if any

Do not repeat the five-source Discovery research or Discovery advancement merely because chat history is missing. Current next task is the bounded revised Screening run only.
