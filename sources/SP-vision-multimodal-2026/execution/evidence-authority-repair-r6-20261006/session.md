# Session — TS-003 Targeted Evidence Authority Repair r6 (ARCHITECTURE_ESTABLISHED)

## Starting authority (read-only verified before any write)

- Branch `special/vision-multimodal-2026-work`, HEAD `f1108c0020098007d458df311b5733db4898dba7`,
  tree `c699a485fab7adc96b3cf250682b3d65b92e9083` (remote match; local==remote).
- Lifecycle `DRAFT_COMPLETE`, Architecture r5 APPROVED, Draft fresh-121-r5-rev2.
- Run-specific Human Owner authorization in the task message (§0); materialized in
  `owner-exception-authorization.md`. No prior exception reused.

## Defects (independent review, confirmed in canonical Evidence)

- VM-D023 LayoutLM: claim-1/claim-2 internal contradiction (image embeddings in
  v1 MVLM pre-training vs future work).
- VM-D039 CLIP: claim-3 + limitation-1 bag-of-words/compositionality
  misattributed to the 2021 original paper.
- VM-D116 pi-zero: claim-1 merged H=50 horizon with up-to-50 Hz control
  (`continuous 50Hz 50-step action chunks`).

## Work performed

1. Fail-closed probes (`probe_reentry.py` → `reentry-probes-r6.md`): no pending
   Human Gate at DRAFT_COMPLETE can authorize formal revision (both gate guards
   raise HumanGateError); Owner Exception consumed. Zero writes in probes.
2. Primary-source re-verification (read-only arXiv HTML of already-bound
   locators; no new sources): LayoutLM v5 (MVLM=text+2D layout; image=downstream;
   image-pretraining=future §5), CLIP v1 (§6 + §3.1.5 scope; BoW only for Joulin
   baseline/ablation), pi-zero v4 (H=50 §IV; up-to-50 Hz capability; 20 Hz UR5e/
   Franka + 16-action/0.8 s vs 50 Hz + 25-action/0.5 s replan, App.A-D).
3. Staged 3 corrected cards (`stage_cards_r6.py` → `staged-cards/`,
   `staging-report.json`): canonical `validate_evidence_card` PASS; statuses
   stay VERIFIED. All other cards untouched.
4. Core-controlled rewind (`execute_exception_rewind.py` →
   `owner-exception-execution.json`): DRAFT_COMPLETE → CANDIDATES_NORMALIZED.
   12 Core-computed paths removed (downstream authority only); r5 reviews +
   approvals + Discovery/Screening/Evidence-store/Draft/Publication intact;
   `validate_agent_state` CLEAN. No Human-gate decision function called.
5. Evidence replay (`replay_evidence.py` → `evidence-replay-report.json`):
   121-task package re-prepared deterministically (121/121 task SHAs identical
   to f6ef98cb); 118 cards carried byte-identical; 3 corrected consumed; new
   acceptance 68be75fd (116 VERIFIED / 5 PARTIAL held).
6. Views/Materiality/Completeness replay (`replay_views_materiality.py`):
   121 views rebuilt (new acceptance 4312a9c2); ledger 122 rows; completeness
   carried with ONE targeted correction (VM-O07 rationale BoW clause replaced;
   SATISFIED held); 14/2 held; BoW purge verified; advanced to EVIDENCE_REVIEWED.
7. Selection replay (`replay_selection.py`): matrix re-derived (121 rows; exactly
   the 3 corrected evidence SHAs changed); 121 assignments carried with ONE
   targeted correction (VM-D039 rationale); 0 disposition changes; advanced to
   SELECTION_COMPLETE.
8. Architecture replay (`replay_architecture.py` → `architecture-r5-to-r6.diff`,
   42 lines): r5-approved base + refreshed basis + PROPOSED + three targeted
   corrections only (P07A must_cover/boundary BoW→source-supported incl. verbatim
   limitation carry per validator; P05 +LayoutLM contract boundary; P13 +π₀
   H/rate/cadence boundary). Delta guard enforced. Summary + attention rebuilt
   and validated. 16 packages, 40-map, freeze preserved. Advanced to
   ARCHITECTURE_ESTABLISHED with gates pending.
9. Handoff records (no body rewrite): `draft-regeneration-guard-provenance-taxonomy.md`
   (author/vendor/independent three-way rule), `draft-regeneration-guard-japanese.md`.
10. V-JEPA Policy / V-JEPA 2.1 / π₀.5-π₀.7 / UI-TARS / OS-Atlas / Aguvis / ShowUI /
    WAM / WorldVLA / DreamZero / UWM: no intake, no screening (verified: counts
    122/121/121 unchanged).

## Deviations / failures

- Partial-file leftovers from two failed-then-fixed runs (ledger, architecture
  trio) were removed and regenerated deterministically; final bytes validated.
- Screening-acceptance glob ambiguity resolved via package-basis pinning.
- P07A boundary uses the verbatim corrected limitation (validator-required exact
  carry); framing lives in must_cover + verification record.
- `般化`-style audit flags adjudicated: BoW string survives ONLY in the D039
  correction verification finding (removal provenance, not a limitation — §16
  compliant); D023 forward-program substance preserved with §5 citation.

## End state

- Lifecycle ARCHITECTURE_ESTABLISHED; fresh Architecture PROPOSED.
- Human Architecture Review r6 PENDING (delta review). No r6 decision created.
- r5 review/approval records immutable history. Draft rev2 files preserved as
  history (NOT regenerated). No TeX/PDF. reader-publication-validation NOT STARTED.
- STOP.
