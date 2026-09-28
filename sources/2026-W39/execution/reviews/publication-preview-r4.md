# Human Publication Preview — 2026-W39 r4 (PENDING, no decision recorded)

Generated: `2026-09-29T02:28:00+09:00` (`2026-09-28T17:28:00Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `eb3bb84fa72af02f30d8dfe888304c5988479013` (exact W39-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r4 bytes under review):
  - `sources/2026-W39/publication/v2/publication-candidate-v2.json` (candidate SHA `d399c25cfabbef368dc9e15156cae2fea56f43faf3ae1f32ab18633a0296048e`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W39/main.pdf` (12 pages, 331169 bytes, SHA `19767148dfcd6b449b32920d0250b097feab441c28fba32b31c316a951d2d5b8`, CI run `36456312074`, artifact `10986695131`)
  - `sources/2026-W39/publication/v2/reader-manuscript-v2.json` (manifest SHA `c28127ce9857f80b1388ca8165c6c332d7bc498c5a8117ee55ac8c2ae68aef34`)
  - `sources/2026-W39/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `de88903132bf722a2fe2e8ad55ce06f84a958e1b6993c7e5d6efa8eb3f699efb`, 3 deterministic PASS)
  - `sources/2026-W39/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W39/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W39/publication/v2/reader-surface-gate-v2.json` (gate SHA `4f6c8cc73319ba00ad2b94d81d6c9135a0a23b064a89e0ce2f0c3095b1089dc7`, PASSED with 0 findings and 0 suppressions)
- PDF four-surface byte identity (all independently computed from real bytes):
  - `SHA256(repository main.pdf)` = `19767148dfcd6b449b32920d0250b097feab441c28fba32b31c316a951d2d5b8`
  - `repository main.pdf.sha256` = `19767148dfcd6b449b32920d0250b097feab441c28fba32b31c316a951d2d5b8`
  - `SHA256(artifact main.pdf)` = `19767148dfcd6b449b32920d0250b097feab441c28fba32b31c316a951d2d5b8` (independently downloaded artifact `10986695131` from run `36456312074`)
  - `artifact main.pdf.sha256` = `19767148dfcd6b449b32920d0250b097feab441c28fba32b31c316a951d2d5b8`
  - byte counts `331169` on all surfaces; result: **IDENTITY PASS**
- Terminology corpora SHAs (4-file union): base `44c354e8ddcbdae6d81cd36c76e48ef676655d258da611665f354a41cadb6c3c` / supplement `adf4305554d315c930a568d3c63067123811568bd3c2df84e6cd8dab372c1829` / r2-residual `257df61b51b3dfc06f9ade2383848c021c8ddb3a3779d88d70fc8e0479b02a27` / r3-residual `3cc8300eec691191e6cbd111e5c40c052d3631e02c2fd9cf9dc32b317b0252e3`; search forms 406 combined; hits adjudicated per occurrence ledger below
- Architecture approval provenance: Human Architecture Review r1 `APPROVED` (reviewed `9767d68e0d83aa667eaeeee6394806c612708682`, reviewed_at `2026-09-28T00:24:35Z`, record `sources/2026-W39/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`); r1/r2/r3 Preview `REQUEST_CHANGES` (boundaries all `DRAFT_COMPLETE`; records `gates/reviews/publication-r1.json`, `publication-r2.json`, `publication-r3.json`); approved Architecture bytes unchanged since approval
- Full r4 dossier: `sources/2026-W39/execution/reviews/publication-preview-r4-dossier.md` (required reading)

## Human decision

`PENDING` — no r4 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r4 review performed yet).

## Regeneration boundary

None selected (no r4 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
