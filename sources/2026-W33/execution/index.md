# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `DISCOVERY_COLLECTED`
- Current machine action: `stage:screening`
- Discovery checkpoint: `passed`
- Screening checkpoint: `pending`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Human Architecture Review history: r1 `REQUEST_CHANGES`, r2 `REQUEST_CHANGES`
- Active regeneration boundary: `ISSUE_INITIALIZED`
- Drafting/publication remains unauthorized.

Architecture Review r2 rolled the run back to `ISSUE_INITIALIZED` so five unresolved W32 carry-over obligations could receive fresh first-party Discovery authority. Discovery repair and deterministic Discovery advancement are complete. Revised Screening is now Sol-accepted and awaits deterministic advancement only.

## Human revision requirements

Formal r2 review:

`sources/2026-W33/gates/reviews/architecture-r2.json`

Decision:

- `REQUEST_CHANGES`
- regeneration boundary: `ISSUE_INITIALIZED`

Required outcomes that must survive downstream regeneration:

1. close or explicitly dispose the five W32 carry-over obligations from fresh first-party authority;
2. rerun affected downstream stages;
3. regenerate Architecture with an explicit mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
4. preserve the previously accepted six substantive packages, 28-candidate placement strategy, target 18 pages / hard maximum 24 pages, and Agent Reliability comparative-synthesis constraint unless newly accepted evidence justifies a change.

## Current repaired Discovery authority

Discovery:

- path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- record count: 41
- exact Discovery ID set unchanged
- non-target parsed records unchanged: 36/36

Five records rebound to fresh first-party authority:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

Discovery acceptance:

- path: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- SHA-256: `777414eefad7280d45fc847dd44a0bdeeef225b6dd0c3e1f4b90bc8b1acb7995`
- X Source Intake SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`

Discovery transition authority:

- request/event commit: `46dc068b1d74a9c18d43b4712b2b6e73ee035186`
- checkpoint: `sources/2026-W33/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`
- bridge status: PASS
- resulting State: `DISCOVERY_COLLECTED / stage:screening`

## Current revised Screening authority — Sol accepted

Historical Screening remains immutable history:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`

It is not current authority because its package basis predates the repaired Discovery.

Current accepted revised Screening run:

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/`

Frozen identities:

- result-set identity: `0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a`
- acceptance SHA-256: `e6f0392004191b4668e4231c57839044e4b08ff1e32763403f2d92630b0b0a0f`
- package SHA-256: `047f595c0b8216a780c4b5c11d9e0cfa9a263e5ec35aa4287f15aae82bdfbd46`
- package State basis SHA-256: `6ef1fb8724989ed69251bef0a77421339933133feccb21781fa688f0b17f997d`
- package repaired Discovery basis SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- records: 41
- decisions: `KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4`

Revision semantics:

- 36 non-target decision objects are field-for-field historical carry-forward;
- exactly the five repaired carry-over decisions changed;
- all five are now `KEEP / high` because first-party source identity/content is sufficient for Evidence verification;
- `KEEP` is Screening triage only and does not pre-decide Materiality or publication treatment.

Luna session:

`sources/2026-W33/execution/sessions/w33-luna-screening-revision-20260830-r1.md`

Sol review:

`sources/2026-W33/execution/reviews/w33-screening-revision-sol-review-20260830-r1.md`

Decision:

`ACCEPT / SCREENING_REVISION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

## Current bounded task

Handoff:

`sources/2026-W33/execution/handoffs/w33-screening-revision-advance-luna-r1.md`

Objective:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`

only.

Required current artifact:

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json`

Expected request id:

`w33-screening-revision-advance-20260830-r1`

Expected successful endpoint:

`CANDIDATES_NORMALIZED_READY_FOR_SOL_EVIDENCE_REVISION_POLICY`

No Evidence / Materiality / Completeness research is authorized in this advancement task.

## Next semantic stage after advancement

After Sol verifies the deterministic Screening transition, the next task is a regenerated Evidence / Materiality / Completeness policy and Luna execution scoped to the current revised Screening basis.

The five repaired carry-over obligations must be explicitly disposed there. Do not replay the historical Evidence/View/Completeness outputs as current authority. Historical `INCOMPLETE` Completeness was the reason for the Architecture revision and must be replaced by regenerated authority.

## Historical downstream identities

Historical only until regenerated/re-checkpointed:

- old Screening result-set: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- old Evidence result-set: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- old repaired View-set: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- old Completeness: `INCOMPLETE`
- old Selection: SELECTED 28 / HOLD 6 / REJECT 3
- old Architecture: six substantive packages, target 18 pages / cap 24 pages

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
4. `sources/2026-W33/discovery/discovery-accepted-v2.json`
5. `sources/2026-W33/execution/sessions/w33-luna-discovery-repair-advance-20260830-r1.md`
6. `sources/2026-W33/execution/sessions/w33-luna-screening-revision-20260830-r1.md`
7. `sources/2026-W33/execution/reviews/w33-screening-revision-sol-review-20260830-r1.md`
8. `sources/2026-W33/execution/handoffs/w33-screening-revision-advance-luna-r1.md`
9. latest revised-Screening advancement session/result, if any
10. latest Sol advancement verification, if any

Do not repeat Discovery repair or revised Screening merely because chat history is missing. Current authority is the Sol-accepted revised Screening result-set above; the next operation is deterministic Screening advancement only.
