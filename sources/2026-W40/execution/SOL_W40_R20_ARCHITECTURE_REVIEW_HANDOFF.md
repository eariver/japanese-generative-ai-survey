# W40 r20 → fresh Human Architecture Review handoff

Status: `FRESH_HUMAN_ARCHITECTURE_REVIEW_PENDING / R20_INDEPENDENT_FOCUSED_REVIEW_REQUIRED` candidate
Date: 2026-10-11 JST
Branch: `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Sol authority: `execution/reviews/sol-w40-r19-independent-architecture-audit-adoption-and-r20-scope-20261011.md` (R19-F01 canonical fix; R19-F02 Sol-fixed in index)
Contract: `execution/instructions/2026-10-11_muse-w40-r20-eq5-single-field-architecture-regeneration.md`
Prior canonical (r19, superseded, Git-reachable): commit `c26c983b`, Arch `305a42d6…`, Summary `37ce43b2…`, State `c5cd8811…`

## Exact review identity

- Lifecycle: `ARCHITECTURE_ESTABLISHED`; next `ARCHITECTURE_REVIEW`; terminal `HUMAN_GATE_REACHED`
- Production State: `sources/2026-W40/production-state.json` (`19bd1a9749108cf61ff29159dac216922b7316e5a91ee41c2f82f2f20e4bcb89`)
- Machine checkpoints: discovery/screening/evidence/materiality/completeness/selection/architecture passed; draft/validation/publication_preview/freeze/release pending
- Human Gates: architecture_review pending, publication_preview pending; both provenances null (no decision recorded)
- Operator invalidation: `execution/operator-invalidations/architecture-invalidation-0002.json` (`de2e7df3…`, seq 2, `human_decision:false`, boundary `SELECTION_COMPLETE`, invalidated commit `db87d64e`, prior State `c5cd8811…`); seq `0001` preserved

## Regenerated review targets (exact bytes)

- Issue Architecture `sources/2026-W40/architecture-v2.json` (`a9b5c1182671bb913fbf56972907e19731e5ba4a928deaca9903a0d3a1461a44`; PROPOSED, human_review null)
- Review Summary `sources/2026-W40/architecture-review-summary-v2.json` (`32f39de0b7cb3e469acf74668c420c246fb67f273ecd0c37bda91557eaa98d30`; `READY_FOR_ARCHITECTURE_REVIEW`, Core-derived equivalence holds)
- Review Attention `sources/2026-W40/architecture-review-attention-v2.json` (`70ac43bd…`, VALID, unchanged)
- Unchanged Selection/Matrix: `b7d20be2…` / `f07b1166…` (28 = 20P/8S + 4 HOLD + 3 REJECT); Selection checkpoint `81707585…` pinned throughout
- Stage validation r3 (`a5d7abce…`, PASS; r1/r2 preserved) + `architecture-reviews-r3.json`; rebuilt checkpoint `SELECTION_COMPLETE.json` (`95b7755a…`)
- MANDATORY first-read erratum (successor): `execution/reviews/w40-r20-architecture-review-surface-erratum.md` (`564799ed…`, binds NEW Summary `32f39de0…` + unchanged Completeness `f83b2d94…`); r19 erratum immutable/historical

## Single-field diff (only canonical Architecture change)

- Pointer `/packages/5/must_cover_requirements/1` (P6a ContextLM Eq.5-vs-Eq.6): prefix (quantitative context, Eq.4, group semantics) unchanged; trailing clause replaced:
  - OLD: `Eq.5 full update text UNVERIFIED beyond ar5iv sections 4-5 scope per technical-prep-r16/contextlm-eq5-primary-note.md.`
  - NEW: `Eq.5 exact optimization objective, variable definitions and fixed-weight training/development/held-out skill-evolution procedure VERIFIED against arXiv:2609.37725v1 §4.2 and execution/technical-prep-r16/contextlm-eq5-primary-note.md (in-context skill optimization, not Eq.6 parameter-learning RL); PDF bytes, figures, appendices B–F, code, unpinned repo revision and unquoted details remain UNVERIFIED.`
- Equation verified (r16): `s* = argmax_s E_{x∼D}[R(τ(x;s))]` — in-context skill optimization with frozen weights; Eq.6 trains parameters. No new claims or numeric edits; all other Architecture fields (thesis/goals/page_plan/9 packages/roles/boundaries/extensions/exceptions/basis) byte-identical.

## Invariance evidence (28/113/105)

- 28/28 SELECTED placed (20 PRIMARY exactly once each, 8 SUPPORTING ≥1); package IDs/memberships/orders identical; 113/113 literal `remaining_boundaries` memberships with 0 missing; per-package raw→unique unchanged (14/12, 8/8, 13/13, 10/8, 18/17, 10/10, 15/15, 19/16, 6/6); zero HOLD/REJECT contamination.
- Diagnostics: governing agent-first `validate_agent_state` PASS; legacy `validate-state` exit 1 with pre-existing agent-first/legacy semantics (exact command/output recorded in r20 session; not a new blocker; no Core change).

## Coverage / omissions (unchanged)

- Accepted upstream intact (Discovery37, Screening37, Evidence35, Views35, Ledger, Completeness LIMITED); 4 HOLD (incl. AstaBrief/AutoSynthData pending #562) + 3 REJECT outside all packages; supplements non-canonical, no companion PDF/release.
- Risk: 28-item scope temporarily omits two material announcements; erratum-corrected Summary line notwithstanding, Human may still reject on sufficiency. No Core rule bypassed.

## Human decision options (after dossier review)

- `APPROVED` → record against the reviewed commit below; continue to drafting.
- `REQUEST_CHANGES` → supply requested changes + one allowed boundary; Core records rN and returns there.

Reviewed commit for decision (final HEAD after push): branch `weekly/2026-W40-v2-work`; production chain `<final> <- 512937f54 (invalidation seq 0002) <- db87d64e (exact start)`. Exact Final HEAD/Tree reported at handoff delivery.
