# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `CANDIDATES_NORMALIZED`
- Current machine action: `stage:evidence-materiality-completeness`
- Discovery checkpoint: `passed`
- Screening checkpoint: `passed`
- Evidence / Materiality / Completeness checkpoints: `pending`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Human Architecture Review history: r1 `REQUEST_CHANGES`, r2 `REQUEST_CHANGES`
- Active regeneration boundary: `ISSUE_INITIALIZED`
- Drafting/publication remains unauthorized.

Architecture Review r2 rolled the run back to `ISSUE_INITIALIZED` so five unresolved W32 carry-over obligations could receive fresh first-party Discovery authority. Discovery repair, revised Screening, and both deterministic advancements are now complete. The current task is the regenerated E/M/C revision candidate only.

## Human revision requirements

Formal r2 review:

`sources/2026-W33/gates/reviews/architecture-r2.json`

Decision:

- `REQUEST_CHANGES`
- regeneration boundary: `ISSUE_INITIALIZED`

Required outcomes that must survive regeneration:

1. close or explicitly dispose the five W32 carry-over obligations from fresh first-party authority;
2. rerun affected downstream stages;
3. regenerate Architecture with an explicit mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
4. preserve the previously accepted six substantive packages, 28-candidate placement strategy, target 18 pages / hard maximum 24 pages, and Agent Reliability comparative-synthesis constraint unless newly accepted evidence justifies a change.

## Current repaired Discovery authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- records: 41
- Discovery acceptance SHA-256: `777414eefad7280d45fc847dd44a0bdeeef225b6dd0c3e1f4b90bc8b1acb7995`
- X Source Intake remains `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`

Five repaired carry-over records:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

All five retain actual Discovery provenance `GAP_FILL` with `weekly:carry-over`; earlier text saying `CARRY_OVER` was a Sol handoff typo already reviewed and corrected semantically.

## Current revised Screening authority

Use exactly:

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json`

Frozen identity:

- result-set: `0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a`
- acceptance SHA-256: `e6f0392004191b4668e4231c57839044e4b08ff1e32763403f2d92630b0b0a0f`
- decisions: KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4

Historical Screening result-set `648a1e...` is history only.

## Revised Screening advancement — verified

Luna session:

`sources/2026-W33/execution/sessions/w33-luna-screening-revision-advance-20260830-r1.md`

Request/event commit:

`5f06a9867cc68cd00cdb9760fc6621023f03647d`

Bridge result:

- receipt: PASS
- transition: `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`
- Screening checkpoint: `sources/2026-W33/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`
- checkpoint SHA-256: `d58ed1e71aaaef4aee4b8b9c3f9ebf4f23bf771bfc8f0190c9becba9c53fac4c`
- resulting State SHA-256: `3894a6fc484870bbe7eb1e42e8440d65ac2ee4fe911bcf6528c29212e156ffce`

Sol verification:

`sources/2026-W33/execution/reviews/w33-screening-revision-advance-sol-review-20260830-r1.md`

Decision:

`ACCEPT / STATE_TRANSITION_VERIFIED / REVISED_SCREENING_AUTHORITY_ESTABLISHED / READY_FOR_EVIDENCE_MATERIALITY_COMPLETENESS_REVISION`

## Current bounded task — E/M/C revision

Handoff:

`sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-revision-luna-r1.md`

This task must regenerate, but not checkpoint/advance:

1. a fresh content-addressed Evidence acceptance from current repaired Discovery + revised Screening;
2. a fresh content-addressed Edition Evidence View acceptance;
3. deterministic `sources/2026-W33/materiality-ledger-v2.json`;
4. validated `sources/2026-W33/profile-completeness-v2.json`.

Production State must remain `CANDIDATES_NORMALIZED` throughout.

### Frozen five-carry-over outcomes

Four source-resolved pre-window records:

- `carry-w32-claude-retirement` → Evidence `VERIFIED`, View `CONTEXT`
- `carry-w32-copilot-cloud-agent` → Evidence `VERIFIED`, View `CONTEXT`
- `carry-w32-kimi-k3-copilot` → Evidence `VERIFIED`, View `CONTEXT`
- `carry-w32-openai-gpt56-update` → Evidence `VERIFIED`, View `CONTEXT`

RepoWise:

- `carry-w32-repowise` → Evidence `PARTIAL`, View `NON_MATERIAL`
- project/tool/method authority is established;
- a qualifying W33 event chronology is not established;
- project-reported claims remain bounded and not independently reproduced;
- lack of qualifying W33 delta is an explicit non-inclusion disposition, not an open carry-over research obligation.

MiniMax is unchanged:

- `base-official-index-minimax-news` → Evidence `NEEDS_MORE`, View `HOLD`

Expected aggregate guardrails:

- Evidence: VERIFIED 24 / PARTIAL 12 / NEEDS_MORE 1 / REJECTED 0
- Views: MATERIAL 25 / CONTEXT 10 / HOLD 1 / NON_MATERIAL 1
- Materiality Ledger: exactly 41 rows

Expected Completeness:

- `weekly:current-relevance` = `LIMITATION`
- `weekly:technical-significance` = `LIMITATION`
- `weekly:carry-over` = `SATISFIED`
- overall = `LIMITED`
- no obligation = `NEEDS_RESEARCH`

The old residual limitation saying five active carry-over rechecks remain `NEEDS_RESEARCH/HOLD` must disappear. Legitimate MiniMax/index/vendor/project/author limitations must remain rather than being erased to force `READY`.

Expected Luna stop:

`EVIDENCE_MATERIALITY_COMPLETENESS_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

No `ADVANCE_STAGE`, Selection, Architecture, Human Gate, Drafting, or external source expansion is allowed.

## Historical E/M/C authority

Historical content-addressed runs remain immutable provenance and are not current checkpoint authority:

- Evidence: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- repaired View: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- historical Completeness: `INCOMPLETE`

For the 32 unchanged active records, Luna may carry forward the historical semantic payload while regenerating current identities/basis hashes. Historical accepted directories must not be modified.

## Architecture requirements after downstream regeneration

Preserve unless newly accepted evidence justifies change:

- six substantive W33 packages;
- 28-candidate placement strategy;
- target 18 pages / hard maximum 24 pages;
- `w33-agent-evaluation-reliability` as comparative synthesis.

Mandatory addition before the next Human Architecture Review:

- explicit independent `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
- it must summarize what changed across the week, why it matters, and what to watch next;
- it must be a formal Architecture element, not page-plan prose only.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this index
3. `sources/2026-W33/gates/reviews/architecture-r2.json`
4. `sources/2026-W33/discovery/discovery-accepted-v2.json`
5. current revised Screening acceptance `0723540.../screening-accepted.json`
6. `sources/2026-W33/execution/sessions/w33-luna-screening-revision-advance-20260830-r1.md`
7. `sources/2026-W33/execution/reviews/w33-screening-revision-advance-sol-review-20260830-r1.md`
8. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-revision-luna-r1.md`
9. latest Luna E/M/C revision session/result, if any
10. latest Sol E/M/C revision review, if any

Do not repeat Discovery repair or Screening revision. Current next task is the bounded regenerated E/M/C candidate only.
