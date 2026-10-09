# Session — TS-003 r7 Targeted Authority Repair (ARCHITECTURE_ESTABLISHED, r7 PENDING)

Run: `execution/r7-targeted-authority-repair-20261007`
Authorization: run-specific Human Owner conditional approval + bounded Owner-Exception
re-entry (this task message §0; transcribed in `owner-exception-authorization.md`).
No prior exception reused. No shared Core modification. No force push.

## Starting authority (read-only verified before any write)

- Branch `special/vision-multimodal-2026-work` (existing only), HEAD
  `1bada73fc8cf84689489e9d397e5db300cbb444f`, tree
  `7cdcf4b4973a47b89da7b9e0046c95a23ce646b9` (local==remote; clean tree).
- Lifecycle `DRAFT_COMPLETE`, Human Architecture Review r6 APPROVED, Draft fresh-121-r6.

## Re-entry

1. Fail-closed probes (`probe_reentry_r7.py` → `reentry-probes-r7.md`): both
   `request_changes` paths FAIL-CLOSED (no pending gate at DRAFT_COMPLETE; Human
   decision must not be fabricated); operator invalidation FAIL-CLOSED (r1–r6
   history); forward advance cannot rewind; shared-Core CLOSED. Zero writes.
2. Core-controlled rewind (`execute_exception_rewind.py` →
   `owner-exception-execution.json`): DRAFT_COMPLETE → CANDIDATES_NORMALIZED via
   ONLY Core machinery (gate context PUBLICATION_PREVIEW, cross-gate reopen).
   12 Core-computed paths removed (downstream authority + canonical approval +
   selection-architecture-input); r1–r6 reviews/approvals snapshots + Discovery/
   Screening/Evidence-store/Draft/Publication intact; `validate_agent_state` CLEAN.

## Evidence repair

3. Staged 2 corrected cards (`stage_cards_r7.py` → `staged-cards/`,
   `staging-report.json`); both canonical-validated against the 81e3b75b basis:
   VM-D108 (grades removed; bounded INFERENCE with paper-measures-nothing
   preserved; limitation refined), VM-D010 (claim-3 empirical ablation; design
   contract preserved). Grade/overstatement tokens kept out of canonical card
   text entirely (old/new wordings live in this session + supplement + report).

## Replay

4. Evidence (`replay_evidence_r7.py`): 121-task package re-prepared over unchanged
   Discovery/Screening + carried r6final supplement (121/121 task SHAs identical);
   119 carried byte-identical; 2 corrected consumed; new acceptance `66c9932e…`
   (116/5 held).
5. Views/Materiality/Completeness (`replay_views_materiality_r7.py`): 121 views
   rebuilt (new acceptance `681faf19…`); ledger 122 rows; completeness obligations/
   residual/closure semantically identical (14/2 held); grade/overstatement purge
   verified; advanced to EVIDENCE_REVIEWED.
6. Selection (`replay_selection_r7.py`): matrix re-derived (121 rows; exactly
   VM-D108 + VM-D010 evidence SHAs changed; corrected limitation flows into
   remaining_boundaries); 121 assignments carried byte-identical + basis rebase
   (0 rationale/disposition changes); advanced to SELECTION_COMPLETE.
7. Architecture (`replay_architecture_r7.py` →
   `architecture-r6approved-to-r7regen.diff`, 28 lines): HEAD r6-approved base +
   refreshed basis + PROPOSED + P05/P15 DocVQA verbatim limitation carries only
   (P02 asserted clean, unchanged). Delta guard enforced. Summary + attention
   rebuilt and validated. 16 packages, 40-map (keys+set identical), page plan,
   freeze preserved. Advanced to ARCHITECTURE_ESTABLISHED with gates pending.
8. Review surfaces: Core summary/attention + edition-local
   `architecture-r7-delta-review-supplement.md`.

## Conditional approval (§§8–9)

9. Audit (`conditional_approval_audit_r7.py` →
   `conditional-approval-audit-r7.json`): 27/27 PASS on ACTUAL bytes. r7 APPROVED
   materialized via the established Human Gate mechanism (record + snapshot +
   canonical approval + index append; Core index-validator defect handling per
   `core-defect-review-index-r6.md` precedent, Core untouched). r1–r6 preserved
   as immutable history; r7 active.

## Fresh Draft (§§10–18)

10. After r7 APPROVED: completely fresh Draft `fresh-121-r7` authored from the
    corrected chain (r6 as negative regression only) with the §11–§18 guards
    (P07A VM-D114 overlay binding; DocVQA/DETR guards; P01 candidate-specific
    transfer boundary; P08 Molmo/PixMo source-bounded wording; P14/P15
    predictive-representation vs world-model distinction; §17 Japanese
    normalization; fresh profile synthesis); deterministic + semantic +
    Japanese + regression audits PASS. STOP — no reader-publication-validation,
    TeX, PDF, Preview, Freeze, Release.

## Deviations

- Architecture validator requires verbatim evidence-limitation carries (P05/P15
  use the exact corrected limitation; framing lives in must_cover/review/synthesis).
- Tracked `__pycache__` hygiene; `PYTHONDONTWRITEBYTECODE=1` for audit runs.
- V-JEPA Policy / 2.1, VQA-CP, successor papers, UI-TARS/OS-Atlas/Aguvis/ShowUI,
  π₀.5/π₀.7, WAM/WorldVLA/DreamZero/UWM: no intake (counts 122/121/121 unchanged).

## End state

Lifecycle ARCHITECTURE_ESTABLISHED → (r7 APPROVED) → DRAFT_COMPLETE; Architecture
AI Review PENDING; Draft AI Review PENDING; reader-publication-validation NOT
STARTED; no TeX/PDF. STOP for independent Human/Sol AI review.
