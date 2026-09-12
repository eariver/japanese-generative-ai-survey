# W34 Publication Boundary Validator sidecar A rerun — post-Core-#488 report (read-only second opinion, non-authoritative)

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Date: 2026-09-12
Identifier: `post-core488-r2`
Scanned W34 commit: `0d544ff4141372c07ae13c0d8c0ae88bc5b59c15` (reviewed Core #488 integrated + references.bib regenerated + fresh 12-page PDF)

## Tool authority

- Repository: `eariver/publication-boundary-redteam`
- Exact SHA: `7b9de2105c690daaafa6698c1791d51ca84a92c0` (verified: fresh out-of-repo checkout HEAD equals pinned SHA; checkout `/tmp/opencode/pb-redteam-r2`, Survey repo untouched by the tool)
- Command (same coverage as the original run):
  `publication-boundary-scan surveys/weekly/2026-W34/main.tex surveys/weekly/2026-W34/sections/*.tex surveys/weekly/2026-W34/references.bib --profile weekly --format json`
- Exit status: `1`
- Aggregate status: `NEEDS_REVIEW`
- Counts: targets 11 (passed 10 / needs-review 1 / failed 0); total findings 1 (hard_fails 0 / review_required 1 / info 0)

## Scanned source

- `surveys/weekly/2026-W34/main.tex` SHA-256: `2c41cc6fdec3142d9fa48d404b1bf0ad41d41fba164dcb020af02d6af4cd3f36` (byte-identical to the original failing run — prose untouched)
- `surveys/weekly/2026-W34/references.bib` SHA-256: `1d3fecf3186a057c9c0ad2323aabc2ae45fd185f3b1ccbce956032269ec4f172` (regenerated via integrated fixed `_bib_text`; 41 entries, leak 0)
- Validated PDF: `surveys/weekly/2026-W34/main.pdf` SHA-256 `f7403b0a98fb4d0b5ec6f4f6f3e05ce2a0eef06c034e530b27da9da3a68fb4d0` (12 pages, CI run `34689715616` success, TeX warning gate PASS)
- Raw JSON: `publication-boundary-scan-w34-post-core488-r2.json` (this directory)

## Exact findings

1. `references.bib` → `PASS` (0 findings). All four former rules are 0:
   - `RULE-BIB-INTERNAL-TAG-LEAK` = 0
   - `RULE-TERM-CORE-EVIDENCE-NOTE` = 0
   - `RULE-TERM-CORE-V2` (bibliography) = 0
   - `RULE-TERM-MATERIALITY-FIELD` = 0
2. `sections/20-agent-workflows.tex` → `NEEDS_REVIEW` (1 finding: `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING`, REVIEW_REQUIRED — the known Mistral-reported residual; reader prose was NOT edited to clear it, per standing Sol disposition).
3. All other 9 targets → `PASS` with zero findings.

## Diff vs original run (`publication-boundary-scan-w34.json`, aggregate FAIL / 165 findings)

- Bibliography HARD_FAIL: 164 -> 0 (all 41 `note = {Core v2 Evidence: …; materiality: …}` lines eliminated by the integrated Core repair; byte delta otherwise limited to `urldate` comma normalization).
- REVIEW_REQUIRED: 1 -> 1 (same section-20 finding, unchanged).
- Aggregate: FAIL -> NEEDS_REVIEW.

## Handling

- No Publication Candidate created. No lifecycle/Human advancement. No prose auto-edit. Architecture approval bytes/provenance unchanged (`0fef8e29...`).
- Returned to Sol with this report plus `feedback-publication-boundary-redteam-post-core488-r2.md`.

Markers: `PUBLICATION_BOUNDARY_SIDECAR_A_RERUN_EXECUTED`, `PUBLICATION_PREVIEW_HUMAN_DECISION_NOT_GENERATED`, `W34_POST_CORE488_SIDECAR_A_KNOWN_RESIDUAL_STOP_FOR_SOL_REVIEW`.
