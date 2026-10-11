# W40 — Read-only Core #562 resumption assessment

Status: `CORE_562_SEPARATE_MAINTENANCE_REQUIRED / AWAIT_EXPLICIT_CORE_BRANCH_AUTHORITY / W40_SELECTION_HOLD`  
Date: 2026-10-11 JST  
Reviewed W40 HEAD: `f4b1b4855ca42be6e55876b4dcad1ed1ad7dc4eb` / Tree: `b61872bb3c5f4b865c2e725b0a3ca8f30c9ad29c`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Issue: https://github.com/eariver/japanese-generative-ai-survey/issues/562 (OPEN, no identified dedicated PR).  
Previous Sol staging closure: `execution/reviews/sol-w40-r17-edition-local-staging-closure-20261010.md`.

## 1. Authority boundary

Edition-local staging repair r13–r17 is CLOSED; 28/28 SELECTED (20 PRIMARY/8 SUPPORTING), 113 literal Candidate↔Boundary relationships in 105 unique Package strings, but **no canonical Selection Acceptance**. Production State blob `8f2a007c11d588ecd94c44fad10117609ce830fb` stays `EVIDENCE_REVIEWED`, next `stage:selection`, Selection/Architecture checkpoints pending, Human Gates pending/provenance null, exception inactive. Never advance Stage, edit accepted upstream manually, counterfeit a Gate, or publish on this basis.

AstaBrief `candidate:2026-W40:00ac1151955c20ff` and AutoSynthData `candidate:2026-W40:ba7d989d5b799f66` remain `HOLD` in canonical Matrix and Selection. Primary hosted issuer article JSON-LD datePublished values recorded in #562: `2026-10-02T15:19:50.340Z` (AstaBrief) and `2026-10-02T04:01:31.290Z` (AutoSynthData). These are article-event clocks, NOT independently established model/dataset/code release instants. Retain materiality judgment as provisional, not Human acceptance.

## 2. Newly confirmed Core feasibility detail (read-only)

Actual 37-row accepted Screening contains `w40-hold-astabrief-20261002: INSPECT` and `w40-hold-autosynthdata-20261002: INSPECT` — neither is DROP. Historical Screening reasons explicitly say publication time is unresolved, and AutoSynthData's historical note says dataset released; both now require source-specific qualification/correction, not silent propagation.

Reviewed main `scripts/survey_evidence_v2.py:224–228,279–323`: `validate_evidence_authority_supplement()` supports an extra explicit issuer source for a **non-DROP** Discovery task, SHA-bound to original Raw source bytes. `task_authority_sources()` / `prepare_evidence_package(..., supplement_manifest_path)` provide exact task/source binding. `build_materiality_ledger()` (1360–1385) does not hard-code `INSPECT→HOLD`; it derives downstream Materiality from Edition View for every non-DROP Discovery. `survey_architecture_v2_base.py:162–268` derives Matrix from validated Evidence/View/Ledger; its Selection check at 416–417 rejects HOLD.

**Tentative narrow path:** keep Discovery37/Screening37 unchanged only if the new audited Core supersession contract explicitly preserves historical reasons, records new corrected rationale/authority, and tests semantics; rebuild versioned Evidence35/Views35/Materiality37/Completeness and new Matrix/Selection staging. If retaining stale Screening explanations is semantically invalid under governance, supersede Screening as a separately approved minimal change. Do not assume validation PASS alone implies editorial approval.

Existing Core cannot do same-state prior-accepted authority supersession: `survey_production_v2.py::transition_state` (935–982) only permits a single forward lifecycle step; `survey_human_gate_v2.py::invalidate_pending_gate` (1103–1134) is inapplicable at `EVIDENCE_REVIEWED`. Evidence Authority Supplement alone does NOT grant reentry power. A bounded full HTML source capture may conflict with source retention/privacy/licensing policy; its actual raw-byte/SHA requirement must be satisfied lawfully, not asserted from a URL+metadata manifest.

## 3. Resolution path

Issue #562's requirements mandate separate approved Core maintenance and review. No suitable #562-specific existing Core branch or PR was identified during read-only inventory. Historical unrelated branches are not permission to reuse. Owner must explicitly designate an existing dedicated Core branch with exact HEAD/Tree, OR explicitly authorize a **named new dedicated Core branch** from reviewed main. This W40 instruction itself creates no such authority.

After independent Core implementation tests/normal PR review/merge to main, re-check latest main and W40 HEAD/Tree, lawfully supersede old Evidence/View/Materiality/Completeness authority in same `EVIDENCE_REVIEWED` state, independently review the new accepted two-item scope, then regenerate Selection and Architecture with fresh SHA guards. Prior 28-item content depth is a floor, not a page cap. No automatic 30-item approval: two source events must pass factual/editorial review.

Stop: `AWAIT_EXPLICIT_CORE_BRANCH_AUTHORITY / NO_W40_STATE_TRANSITION`.
