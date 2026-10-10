# W40 shared Core v2 defect — pre-Architecture upstream supersession gap

Status: `OPEN_CORE / EDITION_LOCAL_CONTINUITY_PLANNED`  
Inventory: `CV2-DM-022` in `docs/core-v2-deferred-maintenance-summary.md`  
GitHub tracking: https://github.com/eariver/japanese-generative-ai-survey/issues/562  
First detected: 2026-10-10 JST, `2026-W40`, stage `EVIDENCE_REVIEWED`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`

## Reproduction

Canonical W40 authority is accepted Discovery37, Screening37, Evidence35, Views35, Materiality37 and LIMITED Completeness, with production lifecycle `EVIDENCE_REVIEWED`, next action `stage:selection` and both Human Gates pending.

Two previously `HOLD / TIME_UNRESOLVED` items are now proven as *issuer-hosted articles* within the W40 half-open period, but not proven as new weight/code-file releases:

- AstaBrief, official `allenai` Hugging Face article: `2026-10-02T15:19:50.340Z`.
- AutoSynthData, official `ServiceNow-AI` Hugging Face article: `2026-10-02T04:01:31.290Z`.

Sol r11 provisionally approved treating both as MATERIAL (Plan B). Accepted Views and Materiality still say HOLD. The Core Selection validator rejects selecting HOLD rows. `transition_state` is forward-only; `invalidate_pending_gate` cannot apply until a valid reached pending Human Gate and passed Architecture checkpoint, which W40 does not have. No safe same-State upstream reattestation path currently exists. Manually editing accepted SHA-bound authority or State is prohibited.

## Evidence

- `sources/2026-W40/execution/host-timestamp-ledger-r11.md`
- `sources/2026-W40/execution/core-reentry-feasibility-r11.md`
- `sources/2026-W40/execution/selection/selection-counterfactual-r11.md`
- `sources/2026-W40/execution/reviews/sol-w40-selection-r11-scope-decision-20261010.md`
- [Core Issue #562](https://github.com/eariver/japanese-generative-ai-survey/issues/562)

## Edition production vs Core maintenance

No shared Core code, schema, config or workflow changes inside this edition. W40 r12 may continue using the existing 28 Core-valid SELECTED candidates and separately staged, explicitly non-canonical AstaBrief / AutoSynthData technical supplements **for Sol review only**.

This does not authorize formal Selection/Architecture promotion of the two HOLD candidates, bypass of unmodified validators, fabricated Human Gate records, or release of these supplements as accepted chapters. It is **not a completed workaround** until independently validated. The generic Core contract gap remains OPEN for a separately managed Core maintenance task.

Related but distinct: CV2-DM-016 source-type taxonomy mismatch; CV2-DM-021 post-validation revalidation reason.

## Deferred Core fix boundaries

A separately reviewed pre-Architecture same-State supersession operation must preserve historical accepted bytes and SHA lineage, verify exact branch/main/state identities, safely version new acceptance and checkpoint references, address State history and implementation-SHA bindings, and pass cross-profile/negative regression. No implementation in W40.
