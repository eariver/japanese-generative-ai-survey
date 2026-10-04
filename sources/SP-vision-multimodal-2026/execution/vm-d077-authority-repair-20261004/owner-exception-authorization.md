# Owner Exception authorization (run 2) — materialization (immutable provenance)

Provenance: worker transcription of the explicit Human authorization received via the
operator question channel on 2026-10-04 for run `vm-d077-authority-repair-20261004`.
Transcription only; NOT a Human GATE decision record (no `gates/reviews/*-rN.json`,
no approval, no REQUEST_CHANGES/APPROVED). Prior run's exception does NOT carry over
(this is a new, separately authorized exception). Worker generated no part of the decision.

## Human authorization (selected option + description, verbatim)

Selected: "Authorize rewind+replay (Recommended)"

"Core machinery only, immutable exception provenance, r4 history preserved, consume staged
VM-D077 correction + P09 normalization + deterministic replay only, then STOP at fresh r5
PENDING. No Draft/TeX/PDF."

## Bounds acknowledged by worker

- Single run only (`vm-d077-authority-repair-20261004`); single boundary (CANDIDATES_NORMALIZED).
- Core-controlled machinery only (`_revised_state`, `_superseded_*`, Core state IO,
  `validate_agent_state`, canonical stage pipeline + `advance_with_checkpoint`).
- No Human-gate decision function invoked; no `reviewed_by/reviewed_at` fabricated.
- Consume: staged VM-D077 supplement + rebound card (canonical-validated) + P09
  normalization spec + strictly necessary deterministic downstream regeneration.
- r4 APPROVED history preserved (never reused as approval for regenerated authority).
- Discovery/Screening authority, 112-record scope, 16-package skeleton, Frozen Core preserved.
- No Draft/TeX/PDF/Candidate/validation. STOP at fresh ARCHITECTURE_ESTABLISHED, r5 PENDING.
- Fallback contracted: any condition unsatisfiable → stop blocked (no manual mutation).
