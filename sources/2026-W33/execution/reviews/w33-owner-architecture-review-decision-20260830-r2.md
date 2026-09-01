# 2026-W33 Owner Architecture Review decision r2

Decision: `REQUEST_CHANGES`

Issue: `2026-W33`  
Gate: `ARCHITECTURE_REVIEW`  
Human-selected regeneration boundary: `ISSUE_INITIALIZED`  
Formal Human review surface commit: `59e2a31982723a0ee88cfb4d0221e326cdf3dabb`  
Reviewed by: `Owner`  
Reviewed at: `2026-08-30T18:54:27+09:00`

## Human decision

The Owner explicitly approves the corrected Architecture Review revision path and selects:

`ISSUE_INITIALIZED`

as the regeneration boundary.

This is Architecture Review revision **r2**. It supersedes only the active regeneration boundary selected in Architecture Review r1; it does not erase or rewrite the immutable r1 `REQUEST_CHANGES` history.

## Why r2 is required

Architecture Review r1 selected `CANDIDATES_NORMALIZED`. After that decision was correctly materialized, Sol re-audited the current Core source-binding contract and the five active W32 carry-over Discovery records.

The audit established that current Core Evidence Cards may use only locators already represented by the generated Evidence Task's Discovery `source_records`. A task-external source is rejected with the requirement to add it through Discovery/Screening first.

The five carry-over Discovery records are currently bound only to prior-week repository authority and do not contain the fresh first-party locators needed for the requested W33 re-verification. Therefore `CANDIDATES_NORMALIZED` cannot satisfy the Human-requested source repair. `DISCOVERY_COLLECTED` is also too late because the Discovery checkpoint would remain authoritative.

The minimum valid boundary is therefore `ISSUE_INITIALIZED`, where Discovery can be repaired and re-accepted before Screening/Evidence are regenerated.

Sol correction authority:

- `sources/2026-W33/execution/reviews/w33-architecture-revision-boundary-sol-correction-20260830-r1.md`

## Reviewed surface

The r2 decision is against the replayed Architecture Review surface retained at commit `59e2a31982723a0ee88cfb4d0221e326cdf3dabb`.

Exact reviewed State:

- `sources/2026-W33/production-state.json`
  - SHA-256: `de65d12d77e0b5033197a96aac5eb02504ddd91ca14ab9f149e2b25da6fb6918`
  - lifecycle: `ARCHITECTURE_ESTABLISHED`
  - next action: `ARCHITECTURE_REVIEW`
  - terminal reason: `HUMAN_GATE_REACHED`

Exact formal Gate inputs remain the same Architecture bytes reviewed in r1:

- `sources/2026-W33/architecture-v2.json`
  - SHA-256: `84663aef1d557bcebaf1b0b8897207c537e48bbb4e410f55985296076ea2302e`
- `sources/2026-W33/architecture-review-summary-v2.json`
  - SHA-256: `4a5e0e45f71f69dea93e818465909003997865819032f777ab8461121acc4439`
- `sources/2026-W33/architecture-review-attention-v2.json`
  - SHA-256: `0e65dfc83153621012090d6489bbeba7669f880700be390e08608e9e334689f7`

Architecture Review r1 remains immutable at:

- `sources/2026-W33/gates/reviews/architecture-r1.json`

## Requested changes

The substantive requested changes remain unchanged from r1; only the regeneration boundary is corrected.

### 1. Repair Discovery source authority for the five active W32 carry-over obligations

Reopen from `ISSUE_INITIALIZED` and obtain fresh W33 first-party source authority for exactly these five inherited obligations:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

For each item, the repaired Discovery record must bind the relevant fresh first-party locator/capture when such authority exists, or explicitly preserve the unresolved/negative result if authoritative current evidence cannot establish the event.

Do not silently substitute secondary/community material for first-party authority. X remains discovery/community context only.

`base-official-index-minimax-news` remains a separate HOLD/NEEDS_MORE candidate and is not one of these five carry-over obligations.

### 2. Regenerate downstream authority from repaired Discovery

After Discovery repair:

- re-run/review Screening only as required by the new Discovery basis;
- regenerate Evidence Tasks/Cards from the repaired accepted Discovery/Screening authority;
- regenerate Edition Evidence Views, Materiality Ledger, and Profile Completeness;
- explicitly dispose `weekly:carry-over`;
- regenerate Candidate Matrix and Candidate Selection;
- regenerate Architecture from the new accepted upstream authority.

No old downstream checkpoint may be reused merely to avoid regeneration after its basis changes.

### 3. Add the mandatory Weekly synthesis chapter

The regenerated W33 Architecture must contain an explicit independent weekly synthesis / summary chapter as a formal Architecture element.

Semantic role:

`WEEKLY_SYNTHESIS / WEEK_IN_REVIEW`

It must synthesize:

- what changed during the week;
- why those changes matter;
- what should be watched next;
- evidence boundaries, uncertainty, and unresolved items.

It must be distinct from cover, contents, source notes, and references.

## Preserved editorial decisions

Unless newly accepted carry-over evidence materially requires a downstream change, preserve the Owner-accepted:

- six substantive package structure;
- 28-candidate placement strategy;
- 18-page target;
- 24-page cap;
- comparative-synthesis constraint for `w33-agent-evaluation-reliability`.

## Shared Core follow-up

The standing product requirement remains: every Weekly issue must include an explicit weekly synthesis chapter.

Shared Core / `WEEKLY_MAGAZINE` contract hardening remains a separate maintenance follow-up. This r2 decision does not authorize shared Core mutation during W33 repair.

## Current authorization

Authorized now:

- materialize Architecture Review r2 as `REQUEST_CHANGES`;
- use regeneration boundary exactly `ISSUE_INITIALIZED`;
- retain r1 review history unchanged;
- invalidate/remove downstream checkpoint/gate authority exactly as canonical Core defines for this boundary;
- return Production State to `ISSUE_INITIALIZED`;
- after Sol verifies the materialization, prepare a bounded Discovery repair handoff for the five carry-over obligations.

Not authorized in the Human-decision materialization step:

- Discovery source collection itself;
- Screening/Evidence regeneration;
- Selection/Architecture regeneration;
- Drafting;
- shared Core modification.
