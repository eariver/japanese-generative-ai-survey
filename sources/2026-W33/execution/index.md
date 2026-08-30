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

## Why the run is back at ISSUE_INITIALIZED

Architecture Review r1 requested changes at `CANDIDATES_NORMALIZED`, but Sol subsequently verified that the five unresolved W32 carry-over records bind only prior-week authority in Discovery. Current Core Evidence validation does not permit introducing a new source outside the Discovery/Screening source set. Therefore fresh first-party verification requires Discovery authority repair.

The Owner explicitly approved Architecture Review r2 with:

- decision: `REQUEST_CHANGES`
- regeneration boundary: `ISSUE_INITIALIZED`

Formal record:

`sources/2026-W33/gates/reviews/architecture-r2.json`

Core bridge result commit:

`85b374b5ad4d4dad047c668d00b262aa66291ed5`

Core result:

- lifecycle: `ISSUE_INITIALIZED`
- next action: `stage:discovery`
- all machine checkpoints: pending
- r1 and r2 Human review records retained in `sources/2026-W33/gates/review-index.json`

Sol rollback verification:

`sources/2026-W33/execution/reviews/w33-architecture-revision-r2-sol-review-20260830-r1.md`

## Current bounded task

Current Luna handoff:

`sources/2026-W33/execution/handoffs/w33-discovery-carryover-repair-luna-r1.md`

Purpose: repair first-party Discovery source authority for exactly these five existing records:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

The final Discovery set must retain exactly the existing 41 `discovery_id` values. The other 36 records must remain semantically unchanged. `base-official-index-minimax-news` is not part of this repair.

Allowed first-party surfaces and claim boundaries are frozen in the handoff. Luna may create only:

- repaired `sources/2026-W33/discovery/discovery-v2.jsonl`;
- new Raw captures under `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/`;
- `sources/2026-W33/execution/sessions/w33-luna-discovery-carryover-repair-20260830-r1.md`.

Luna must not change Production State, X intake, acceptance/checkpoints, downstream artifacts, Human Gate records, or shared Core.

Expected Luna stop:

`DISCOVERY_CARRYOVER_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

## Human review requirements that must survive regeneration

The Owner accepted the existing Architecture except for the required changes below.

Preserve unless newly accepted evidence justifies a change:

- the six substantive W33 packages;
- the 28-candidate placement strategy;
- target 18 pages / hard maximum 24 pages;
- `w33-agent-evaluation-reliability` as comparative synthesis rather than candidate-by-candidate mini-articles.

Mandatory Architecture change on regeneration:

- every Weekly issue must contain an explicit independent `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
- it must summarize what changed across the week, why it matters, and what to watch next;
- it must be a formal Architecture element, not merely page-plan prose.

Owner finding authority:

`sources/2026-W33/execution/reviews/w33-owner-architecture-review-findings-20260830-r1.md`

Owner r2 decision authority:

`sources/2026-W33/execution/reviews/w33-owner-architecture-review-decision-20260830-r2.md`

## Historical accepted authority

The pre-revision accepted artifacts remain historical evidence/provenance and must not be silently overwritten as if still checkpoint-authoritative:

- Discovery: 41 records, SHA-256 `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Screening result-set: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- Evidence result-set: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- repaired View-set: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- Materiality Ledger SHA-256: `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`
- old Profile Completeness SHA-256: `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`, overall `INCOMPLETE`
- old Selection: SELECTED 28 / HOLD 6 / REJECT 3
- old Architecture: six substantive packages, 18-page target / 24-page cap

These artifacts will be regenerated from the repaired Discovery basis after Sol accepts the Luna proposal.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/gates/review-index.json`
4. `sources/2026-W33/gates/reviews/architecture-r2.json`
5. `sources/2026-W33/execution/reviews/w33-architecture-revision-boundary-sol-correction-20260830-r1.md`
6. `sources/2026-W33/execution/reviews/w33-architecture-revision-r2-sol-review-20260830-r1.md`
7. `sources/2026-W33/execution/handoffs/w33-discovery-carryover-repair-luna-r1.md`
8. latest Luna carry-over Discovery-repair session, if any
9. latest Sol review of the repaired Discovery proposal, if any

Do not replay the old Architecture path again merely because chat history is missing. Current authority is the r2 rollback to `ISSUE_INITIALIZED` and the bounded five-carry-over Discovery repair task.
