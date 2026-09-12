# W34 Publication Boundary Validator sidecar report (read-only, non-authoritative)

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Date: 2026-09-12

## Tool authority

- Repository: `eariver/publication-boundary-redteam`
- Exact SHA: `7b9de2105c690daaafa6698c1791d51ca84a92c0` (verified: fresh clone HEAD equals pinned SHA)
- Checkout: `/tmp/opencode/pb-redteam` (outside the Survey repository; Survey repo untouched by the tool)
- Command (semantically equivalent to the prescribed form, extended to the section/bib files that `main.tex` inputs):
  `publication-boundary-scan surveys/weekly/2026-W34/main.tex surveys/weekly/2026-W34/sections/*.tex surveys/weekly/2026-W34/references.bib --profile weekly --format json`
- Exit status: `1`
- Aggregate status: `FAIL`
- Counts: targets 11 (passed 9 / needs-review 1 / failed 1); total findings 165 (hard_fails 164 / review_required 1 / info 0)

## Scanned source

- `surveys/weekly/2026-W34/main.tex` SHA-256: `2c41cc6fdec3142d9fa48d404b1bf0ad41d41fba164dcb020af02d6af4cd3f36`
- Section SHAs: recorded in the execution log (00 `746396b3…`, 10 `9f7ed1bd…`, 20 `5c7550d8…`, 30 `07fd2cc0…`, 40 `312ac975…`, 50 `27ddfece…`, 60 `f947c387…`, 70 `d5ce0e4d…`, 99 `05d9a2f2…`)
- `references.bib` SHA-256: `15f360f4843033321c4043fec9b9969689e7496eea41e3cb04e56edbe724d6a2`
- Validated PDF: `surveys/weekly/2026-W34/main.pdf` (12 pages, CI run `34669447838` success)
- Raw JSON: `publication-boundary-scan-w34.json` (this directory)

## Exact findings

1. `references.bib` → `FAIL` (164 hard fails = 41 entries × 4 rules: `RULE-BIB-INTERNAL-TAG-LEAK`, `RULE-TERM-CORE-EVIDENCE-NOTE`, `RULE-TERM-CORE-V2`, `RULE-TERM-MATERIALITY-FIELD` on every `note = {Core v2 Evidence: VERIFIED; materiality: MATERIAL}` line).
   - Assessment: TRUE POSITIVE against the reader-facing boundary. The note text came from the current Core weekly renderer's `_bib_text` template, not from Evidence prose. No HOLD/SELECTED-equivalent factual content is at stake; the disposition metadata belongs in repository manifests, not the printed bibliography.
2. `sections/20-agent-workflows.tex` → `NEEDS_REVIEW` (1 finding: `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` on the claim-boundary block, asking for explicit vendor-stated framing).
   - Assessment: LIKELY FALSE POSITIVE / language-coverage gap. The boundary block states `Mistral-reported`, `no independent reproduction`, and scope limits explicitly; the rule appears not to recognize this phrasing.
3. All other 9 targets → `PASS` with zero findings.

## Handling (per execution authority §9)

- Aggregate is `FAIL` → STOP before Publication Candidate. No Candidate built. No publication text auto-edited in response to the sidecar.
- Returned to Sol with this report plus `feedback-publication-boundary-redteam.md`. Shared-Core observation recorded there; no shared-Core edit made on this branch.

Markers: `PUBLICATION_BOUNDARY_SIDECAR_EXECUTED`, `PUBLICATION_PREVIEW_HUMAN_DECISION_NOT_GENERATED`.
