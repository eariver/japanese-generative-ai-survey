# Owner Exception authorization (run: sync-repair-r5) — materialization (immutable provenance)

Provenance: worker transcription of the explicit Human authorization received via the
operator question channel on 2026-10-04 for run `sync-repair-r5-20261004`
(inspection confirmed formal operator path unavailable — fail-closed probe, zero writes;
prior exceptions NOT reused). Transcription only; NOT a Human GATE decision record
(no `gates/reviews/*-rN.json`, no approval, no REQUEST_CHANGES/APPROVED).
Worker generated no part of the decision.

## Human authorization (selected option + description, verbatim)

Selected: "Authorize (Recommended)"

"Core machinery only, immutable exception provenance, rationale-only Selection sync +
P06/P09 Architecture sync + summaries/checkpoints replay, STOP at ARCHITECTURE_ESTABLISHED
r5 PENDING. No Evidence/Draft/TeX/PDF changes."

## Bounds acknowledged by worker

- Single run only (`sync-repair-r5-20261004`); single minimal boundary (SELECTION_COMPLETE).
- Core-controlled machinery only (`_revised_state`, `_superseded_*`, Core state IO,
  `validate_agent_state`, canonical stage pipeline + `advance_with_checkpoint`).
- No Human-gate decision function invoked; no `reviewed_by/reviewed_at` fabricated.
- Consume: staged targeted texts ONLY (1 Selection rationale + P06 must_cover line +
  P09 scoped companion line) + strictly necessary deterministic downstream regeneration
  (Selection file, Architecture file, review summary/attention, checkpoints, state).
- No Discovery/Screening/Evidence/Materiality/Completeness semantic change; Evidence
  result-set hash unchanged; VM-D077 supplement unchanged.
- Selection disposition/count/placement unchanged; 16-package skeleton, P15 39-map preserved.
- r4 APPROVED history preserved, never reused. No Draft/TeX/PDF/validation.
- Fallback contracted: any condition unsatisfiable → stop blocked (no manual mutation).

## Amendment (same channel, 2026-10-04)

Human authorized boundary amendment: SELECTION_COMPLETE → EVIDENCE_REVIEWED
(selected "Amend to EVIDENCE_REVIEWED (Recommended)": same Core machinery and
protections; rebuild EVIDENCE_REVIEWED checkpoint on the rationale-edited Selection,
then advance; all other bounds unchanged). Reason: surviving EVIDENCE_REVIEWED
checkpoint pins the pre-edit selection SHA; Core cannot advance past the resulting
drift without rebuilding that checkpoint from EVIDENCE_REVIEWED. Recorded as a second
rewind execution record; the first (SELECTION_COMPLETE) record is preserved.
