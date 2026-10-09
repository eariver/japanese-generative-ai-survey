# Session — TS-003 r6 Final Authority Correction (ARCHITECTURE_ESTABLISHED, r6 PENDING)

Run: `execution/r6-final-authority-correction-20261006`
Authorization: run-specific Human Owner conditional approval + bounded Owner-Exception
re-entry (this task message §§0–2; transcribed in `owner-exception-authorization.md`).
No prior exception reused. No shared Core modification. No force push.

## Starting authority (read-only verified before any write)

- Branch `special/vision-multimodal-2026-work` (existing only), HEAD
  `4e2d8837514f1529fdd1e695ed7d3952e44eda3d`, tree
  `f179f3e0343225a1d70e92ee2709b8c0f9e44664` (remote match; local==remote).
- Lifecycle `ARCHITECTURE_ESTABLISHED`, Human Architecture Review r6 PENDING.
- Canonical Evidence 121 (VERIFIED 116 / PARTIAL 5), Selection 121, Architecture 16
  packages PROPOSED, Draft NONE for the r6 chain (fresh-121-r5-rev2 historical only).

## Re-entry

1. Fail-closed probes (`probe_reentry_final.py` → `reentry-probes-r6-final.md`):
   ARCHITECTURE_REVIEW pending predicate PASS-PENDING (formal `request_changes`
   would still need a Human decision — CLOSED to the worker); operator
   `invalidate_pending_gate` FAIL-CLOSED (review-index history r1–r5 blocks the
   no-records precondition; Core raises before any write); boundary allowlist
   INFO (CANDIDATES_NORMALIZED allowed but invocation closed); shared-Core CLOSED.
   Zero writes in probes.
2. VQA-v2 primary-source re-verification (read-only arXiv HTML v3, 216781 bytes):
   language priors, complementary image pairs (same question + similar images +
   two different answers), balanced ~2x dataset, SOTA worse on balanced set
   (prior exploitation). No contamination claim in source.
3. New authority supplement (`evidence-authority-supplement-r6final.json`, 23
   entries: 22 carried + VQA-v2 `supplement-src-2931815e4c48399b` with exact raw
   snapshot `snapshots/arxiv-1612.00837-v3.html`).
4. Staged 5 corrected cards (`stage_cards_r6final.py` → `staged-cards/`,
   `staging-report.json`); 4 validated now, VM-D038 validated in replay against
   the fresh package basis.
5. Core-controlled rewind (`execute_exception_rewind.py` →
   `owner-exception-execution.json`): ARCHITECTURE_ESTABLISHED →
   CANDIDATES_NORMALIZED via ONLY `_revised_state` +
   `_superseded_paths_for_regeneration` + `_superseded_gate_authority_paths` +
   `write_json` + `validate_agent_state`. 10 Core-computed paths removed
   (downstream authority only); r1–r5 reviews/approvals + Discovery/Screening/
   Evidence-store/Draft/Publication intact; `validate_agent_state` CLEAN. No
   Human-gate decision function called.

## Replay

6. Evidence (`replay_evidence.py` → `evidence-replay-report.json`): 121-task
   package re-prepared (120/121 task SHAs identical; VM-D038 differs by new
   supplement binding); 116 carried byte-identical; 5 corrected consumed; new
   acceptance `81e3b75b…` (116/5 held).
7. Views/Materiality/Completeness (`replay_views_materiality.py`): 121 views
   rebuilt (new acceptance `304d6dcf…`); ledger 122 rows; completeness obligations
   carried (16) with G05 residual/closure refined to the first-party gap (14/2
   held); contamination + blanket-vendor purge verified; advanced to EVIDENCE_REVIEWED.
8. Selection (`replay_selection.py`): matrix re-derived (121 rows; exactly the 5
   corrected evidence SHAs changed); 121 assignments carried with ONE targeted
   correction (VM-D065 rationale vendor → author/developer; VM-D112 provider
   ceilings preserved); 0 disposition changes; advanced to SELECTION_COMPLETE.
9. Architecture (`replay_architecture.py` →
   `architecture-r6prior-to-r6regen.diff`, 78 lines): HEAD r6-pending base +
   refreshed basis + PROPOSED + targeted corrections only (P07A contamination →
   verbatim corrected limitation; P09 2 must_cover + 3 author boundaries verbatim;
   P15 purpose/must_cover/map-key three-way; provider verbatim carries preserved).
   Delta guard (only P07A/P09/P15) enforced. Summary + attention rebuilt and
   validated. 16 packages, 40-map (key renamed, set unchanged), page plan, freeze
   preserved. Advanced to ARCHITECTURE_ESTABLISHED with gates pending.
10. Review surfaces: Core summary/attention + edition-local
    `architecture-r6-delta-review-supplement.md` (VQA old/new source+wording,
    provenance old/new taxonomy, affected IDs, P09/P15/G05 deltas, invariant list).

## Conditional approval (§§12–14)

11. Audit (`conditional_approval_audit.py` →
    `conditional-approval-audit-r6.json`): §12 A/B/C all PASS on ACTUAL bytes
    (25/25 incl. C7 after pycache hygiene). r6 APPROVED materialized via
    canonical `record_architecture_approval` (`--expected-revision 6`,
    reviewer Human Owner, conditional pre-authorization noted, actual SHAs bound).
    r5 (+ r1–r4) preserved as immutable history; r6 active.

## Fresh Draft (§§15–20)

12. After r6 APPROVED: completely fresh Draft `fresh-121-r6` authored from the
    corrected chain (r5-rev2 as negative regression only); 16 packages
    regenerated; deterministic + semantic + Japanese + regression audits PASS.
    See `fresh-draft-r6-*` records. STOP — no reader-publication-validation, TeX,
    PDF, Preview, Freeze, Release.

## Deviations

- Architecture validator requires verbatim evidence-limitation carries: P07A/P09
  author boundaries use exact corrected limitation text (framing lives in
  must_cover/purpose/verification records); provider boundaries (072/073/112)
  keep verbatim evidence text (vendor = provider/vendor; taxonomy lives in
  must_cover/purpose/surfaces). No shared Core change to rename the map key was
  needed (map key is edition-local; renamed safely).
- Tracked `__pycache__` `.pyc` files restored after hygiene; `PYTHONDONTWRITEBYTECODE=1`
  used for audit runs.
- V-JEPA Policy: deferred / no intake (counts 122/121/121 unchanged).

## End state

Lifecycle ARCHITECTURE_ESTABLISHED → (r6 APPROVED) → DRAFT_COMPLETE; Architecture
AI Review PENDING; Draft AI Review PENDING; reader-publication-validation NOT
STARTED; no TeX/PDF. STOP for independent Human/Sol AI review.
