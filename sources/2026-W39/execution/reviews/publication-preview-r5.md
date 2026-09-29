# Human Publication Preview — 2026-W39 r5 (PENDING, no decision recorded)

Generated: `2026-09-29T03:37:00+09:00` (`2026-09-28T18:37:00Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `342adad3400bd6dee07fb920441f8e259f18eb15` (exact W39-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r5 bytes under review):
  - `sources/2026-W39/publication/v2/publication-candidate-v2.json` (candidate SHA `18b9ab48868136eb6e5c47320a03a6cbc46769928d2fc3810f773b3ffe8926e1`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W39/main.pdf` (12 pages, 335104 bytes, SHA `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f`, CI run `36465420944`, artifact `10989018607`)
  - `sources/2026-W39/publication/v2/reader-manuscript-v2.json` (manifest SHA `a51809e98e2c4ac3b8b143837ab5722253fe57714c90ea7efc6db1408cb70fb0`)
  - `sources/2026-W39/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `ef8c9ce24c7a623d70e6d05faa5eec59d560159f201d8b9ce8b79804daccf2a9`, 3 deterministic PASS)
  - `sources/2026-W39/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W39/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W39/publication/v2/reader-surface-gate-v2.json` (gate SHA `3c05f3bf767fbbee6cdc8035ad3c35c64315f07f7bc59847fe002d977e0034d5`, PASSED with 0 findings and 0 suppressions)
- PDF four-surface byte identity (all independently computed from real bytes):
  - `SHA256(repository main.pdf)` = `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f`
  - `repository main.pdf.sha256` = `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f`
  - `SHA256(artifact main.pdf)` = `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f` (independently downloaded artifact `10989018607` from run `36465420944`)
  - `artifact main.pdf.sha256` = `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f`
  - byte counts `335104` on all surfaces; result: **IDENTITY PASS**
- Architecture approval provenance: Human Architecture Review r1 `APPROVED` (reviewed `9767d68e0d83aa667eaeeee6394806c612708682`, reviewed_at `2026-09-28T00:24:35Z`, record `sources/2026-W39/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`); r1/r2/r3/r4 Preview `REQUEST_CHANGES` (boundaries all `DRAFT_COMPLETE`; records `gates/reviews/publication-r1.json` through `publication-r4.json`); approved Architecture bytes unchanged since approval
- Full r5 dossier: `sources/2026-W39/execution/reviews/publication-preview-r5-dossier.md` (required reading)

## Human decision

`PENDING` — no r5 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r5 review performed yet).

## Regeneration boundary

None selected (no r5 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
