# W41 Repair R7-02 finding — legacy-negative reader-surface exclusion (lawful investigation)

Status: `INVESTIGATED / LAWFUL_CORRECTION_NOT_AVAILABLE / LAWFUL_STATE_PRESERVED`
Date: 2026-10-12 JST
Scope: `architecture-review-summary-v2.json` `residual_limitations[9]`:
`r6: Nano Banana legacy categorical absence (no blog post exists / rollout post nonexistent)
excluded from reader surfaces; see nanobanana-legacy-negative-exclusion-r6.md.`
Authoritative guards: r6 exclusion overlay + r7 contract §4 + Sol S41-B.

## 1. Distinction (as ordered)

1. Machine boundary (byte-exact, Core-required): `architecture-v2.json` P4
   `boundaries[]` literal `Pricing/license absent; docs page unfetched; rollout post
   nonexistent.` — preserved, labeled `LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE` in
   `execution/architecture-trace-exception-r7.md`, never in reader prose. Lawful.
2. Human-reader surface: summary `residual_limitations[9]` names both legacy spans
   inside a meta-sentence documenting their exclusion. Sol flags this as a prohibited
   reader-surface occurrence. The concern is understood: a Human reading the summary
   sees the forbidden strings even though the sentence endorses nothing.

## 2. Lawful-correction investigation (Frozen Core unchanged, no forgery)

Finding 1 — summary is exactly the Core derivation (empirical, r8):
re-running frozen `build_architecture_review_summary` reproduces the canonical file
byte-identically (SHA `f3058466…` both ways). `residual_limitations` is a verbatim
`list(upstream completeness residuals)` (`survey_architecture_v2_base.py` builder).

Finding 2 — hand-editing the summary is unlawful and fails closed:
`survey_stage_validation_v2.py` SELECTION_COMPLETE branch rebuilds the expected summary
and raises `Architecture Review Summary differs from validated derivation` on any
byte difference; the summary SHA is also bound in the SELECTION_COMPLETE checkpoint
and Architecture basis. Editing bytes = hash forgery + validation failure.

Finding 3 — the upstream (Completeness residual[9]) cannot be amended lawfully in r8:
the residual text lives in canonical `profile-completeness-v2.json`, bound by the
CANDIDATES_NORMALIZED checkpoint (SHA `a0c30419…` in Production State provenance) and
by matrix/selection/architecture/summary bases. Amending it requires rebuilding that
checkpoint, but `build_stage_checkpoint` refuses divergent overwrite of an existing
canonical checkpoint path, and State advancement is monotonic-forward only
(`advance_with_checkpoint`; no amend-past operation). Rewriting checkpoint or State
bytes by hand is forgery, explicitly forbidden by this repair order §5.

Finding 4 — no edition-local canonical procedure exists for this correction:
no Core operation amends a historical checkpoint or re-points State provenance outside
a forward transition or a Human `REQUEST_CHANGES` regeneration boundary (neither
available: the Human Gate is pending, no decision has been made).

## 3. Conclusion

R7-02 is **not correctable by any lawful edition-local step in r8**. The current
lawful State (ARCHITECTURE_ESTABLISHED, all validations PASS, verified read-only
in §4) is preserved untouched. No canonical bytes were altered, no validator
bypassed, no hash forged.

## 4. Required follow-on (reported, not executed)

Removal of the legacy spans from the Human-reader surface requires, in order:
1. A versioned Evidence reacceptance that narrows the root categorical spans at their
   source (accepted Card limitation-1 `rollout post nonexistent`, supplement role and
   r4 manifest relation `no blog post exists`) the way r5 narrowed claim-2 — new
   versioned run, historical bytes preserved, no in-place rewrite; and
2. downstream regeneration through the affected checkpoints (Completeness residuals
   reworded without quoting the spans → Materiality/Selection/Architecture/summary
   rebuilt → new checkpoints) via a Sol-authorized bounded unit crossing a Human
   `REQUEST_CHANGES` regeneration boundary if State must rewind, or via fresh forward
   authority if Sol so directs.
Both steps are outside r8 scope and are Sol/Human decisions. **No such reacceptance
was started.**

## 5. Mitigation within lawful bounds (done in r8)

- Reader-surface grep audit re-run: exactly two hits repository-wide in Architecture
  surfaces — (a) P4 machine boundaries trace (lawful, labeled), (b) summary[9]
  meta-reference (this finding). Zero hits in title/purpose/must_cover (6 packages),
  technical prep, resource plan, selection rationales, dossier, and preview narrative.
- This finding plus the trace exception give Sol the exact bytes, locations, and
  Core citations needed to brief the Human: the summary sentence endorses nothing and
  points at the exclusion overlay; the Human Gate decision (APPROVED vs REQUEST_CHANGES
  with a regeneration boundary) is the lawful instrument that can resolve it.

## 6. Verification appendix

- `validate_agent_state` on current Production State: PASS (bindings intact, no drift).
- Re-derived summary == canonical summary: True (`f3058466…`).
- Code cites: builder verbatim copy (`survey_architecture_v2_base.py`, summary builder);
  equality enforcement (`survey_stage_validation_v2.py`, `review != expected` branch);
  divergent-overwrite refusal (`survey_agent_control_v2.py`, checkpoint builder).

(End of file)
