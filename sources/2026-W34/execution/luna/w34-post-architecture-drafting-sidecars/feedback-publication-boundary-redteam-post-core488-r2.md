# Feedback — Publication Boundary Validator sidecar A rerun (post-Core-#488)

Tool: `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0`
Scanned artifact: regenerated W34 `surveys/weekly/2026-W34/main.tex` + sections + `references.bib` at `0d544ff4...` (Weekly profile, JSON output)
Run: 2026-09-12, exit 1, aggregate `NEEDS_REVIEW` (0 hard fails, 1 needs-review on section 20, 10/11 targets PASS)

## Usability (unchanged from original run)

- Pinned-SHA clone plus `PYTHONPATH=src` invocation works without installation. JSON output remains machine-readable with per-target status, rule IDs, severities, and line-precise locations.

## Useful findings

- The original 164 bibliography HARD_FAILs are fully resolved: `references.bib` now PASS with 0 findings across all four internal-metadata rules. This confirms the integrated Core #488 repair end-to-end on real W34 authority (41/41 cite keys/order preserved, leak 0).
- The single remaining finding is the already-known section-20 `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` REVIEW_REQUIRED on Mistral-reported prose that explicitly states `Mistral-reported`, `no independent reproduction`, and scope limits. Still assessed as likely false positive / language-coverage gap, consistent with the original Sol disposition. No prose change made.

## New / different findings vs original run

- None. No new REVIEW_REQUIRED, no new HARD_FAIL, no rule-ID changes. The only delta is the elimination of the 164 bibliography findings.

## Operational usefulness

- Confirmed as an effective pre-candidate gate for the bibliography defect class. Recommend keeping it NON-AUTHORITATIVE (one residual likely-false-positive persists by design).

Disposition: tool REMAINS NON-AUTHORITATIVE read-only second opinion.

Markers: `SIDECAR_A_RERUN_FEEDBACK_RECORDED`.
