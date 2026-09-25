# TS-002 Sol Architecture Review r1

Status: `REQUEST_CHANGES / ACTIVE_PROVENANCE_SANITATION_REQUIRED`

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`
Branch: `special/beyond-text-2026-work`
Reviewed work HEAD: `d1b81f8ee6a3d83622ba1f780ee070000bda1ab9`
Reviewed work tree: `33e0ebafe90d6550509942d1c23cdc9e8f2737c0`
Reviewed main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`
Reviewed main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`

## Decision

The proposed TS-002 architecture is substantively acceptable, but the Human Architecture Gate is **not yet approved** because active downstream artifacts still carry stale pre-rebind provenance wording.

This is a bounded provenance-state sanitation request, **not** a request to redo Discovery, Screening, semantic Evidence research, Materiality reasoning, Selection, or the architecture design.

Draft and later stages remain unauthorized.

## What passes

- 14-package mechanism-led architecture: PASS.
- Representation-first editorial axis: PASS.
- Architecture vs objective vs sampling/inference separation: PASS.
- Generation vs editing separation: PASS.
- Speech / music / video as independent technical histories: PASS.
- Runtime and evaluation as first-class chapters: PASS.
- Closed-product capability/workflow/lifecycle quarantine: PASS.
- TS-002 / TS-003 boundary: PASS.
- Page envelope target 80 / guidance max 96, with depth preferred over compression: PASS.
- Transition-ledger retention: all 43 transitions mapped across the architecture: PASS.
- Selection anti-thinness: 134 SELECTED / 5 HOLD, no REJECT compression: PASS.
- Human gate mechanics: fresh pending Architecture Review, no fabricated approval: PASS.

## Blocking finding A1 — stale future-tense provenance instructions in active Evidence / Architecture

The provenance rebind completed successfully before this Architecture run. Canonical source locators are already corrected.

However, active rebound Evidence still contains stale wording inherited from r2, for example BT-D004:

`Recorded locator 2012.09812 is a transcription defect ... Future Discovery repair should correct the locator.`

The same stale sentence is propagated into `architecture-v2.json`. The exact phrase `Future Discovery repair should correct` appears multiple times in the active architecture (11 matches observed in Sol readback).

This is now factually obsolete: the Discovery locator repair already happened and canonical BT-D004 points to `2012.09841`.

If drafting begins from the current architecture boundaries, publication prose could reintroduce an already-resolved provenance defect or imply that the canonical source remains incorrect.

Required disposition:

- Historical audit artifacts may retain the old locator and the fact that it was once wrong.
- Active semantic artifacts must describe the correction in past tense, e.g. `Prior recorded locator X was a transcription defect; canonical locator was rebound to Y during the provenance repair.`
- No active artifact may state that a completed Discovery repair is still pending.
- Genuine unresolved body-access barriers must remain unresolved.

## Blocking finding A2 — Human dossier PARTIAL accounting is stale

`execution/architecture-review-dossier-r1.md` says `8 PARTIAL`, but its parenthetical enumeration includes nine items and still lists the Seamless v1/v2 boundary.

BT-D062 was rebuilt from the Seamless v2 source body and is now `VERIFIED`; it must not remain in the PARTIAL list.

Canonical non-VERIFIED set after provenance rebind is:

PARTIAL (8):
- BT-D022
- BT-D059
- BT-D076
- BT-D083
- BT-D089
- BT-D098
- BT-D106
- BT-D134

NEEDS_MORE / HOLD (5):
- BT-D024
- BT-D072
- BT-D091
- BT-D120
- BT-D125

Required disposition: regenerate/correct the Human dossier so counts and IDs agree with the active Evidence acceptance.

## Repair boundary

Allowed:

- edition-local active Evidence provenance wording sanitation;
- new content-addressed Evidence result-set / Views if required by canonical immutability;
- transition-ledger provenance wording refresh;
- deterministic downstream replay of Materiality / Completeness / Selection / Architecture;
- Architecture Review summary / attention / dossier regeneration;
- validation receipts and session report.

Not allowed:

- new Discovery research;
- new X collection;
- broad Screening rerun/research;
- semantic Evidence campaign redo;
- changing substantive claims, metrics, materiality decisions, selection decisions, chapter design, page allocation, or transition interpretation except where required to remove stale provenance-state wording;
- Draft or later stages;
- Shared Core changes.

## Expected invariant semantics

Unless canonical regeneration mechanically changes hashes/IDs only:

- Discovery: 139
- Screening: KEEP 134 / MAYBE 3 / INSPECT 2 / DROP 0
- Evidence status: VERIFIED 126 / PARTIAL 8 / NEEDS_MORE 5
- Materiality: MATERIAL 109 / CONTEXT 25 / HOLD 5
- Selection: SELECTED 134 / HOLD 5
- Completeness: 4 SATISFIED / 8 LIMITATION, overall LIMITED
- Transition ledger: 43 entries
- Architecture: 14 packages
- Page plan: target 80, guidance max 96
- Human Architecture Review: pending

## Stop condition

After sanitation and canonical replay, stop again at:

`ARCHITECTURE_REVIEW / AWAITING_HUMAN_ARCHITECTURE_DECISION_R2`

Sol will perform a readback before any Human approval is recorded.
