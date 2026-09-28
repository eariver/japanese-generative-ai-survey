# Human Publication Preview — 2026-W39 r3 (PENDING, no decision recorded)

Generated: `2026-09-29T01:21:00+09:00` (`2026-09-28T16:21:00Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `4463e80e1e01476adf12586a705006e7bbcda8a6` (tree `60c4cfaccaf2a21f4293a10ad9d79f74421d74dc`; exact W39-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r3 bytes under review):
  - `sources/2026-W39/publication/v2/publication-candidate-v2.json` (candidate SHA `7def181d8811b52ee20b17b7b5bca04eb6875c373d4e3203b944b651e0fc26c3`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W39/main.pdf` (12 pages, 329744 bytes, SHA `7fac4b5c76695edb9821dc3c2463bc281014407cd01ec5a9c4c1784d711d8cdb`, CI run `36440543369`, artifact `10979260910`)
  - `sources/2026-W39/publication/v2/reader-manuscript-v2.json` (manifest SHA `ee6af1894f71ddba702cbb0ffd037783ee2456841762cdda8a61369f23019f62`)
  - `sources/2026-W39/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `f410de5886f952b722592ab619670ce5ebdcb16e3e5df7bac9c8925849653154`, 3 deterministic PASS)
  - `sources/2026-W39/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W39/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W39/publication/v2/reader-surface-gate-v2.json` (gate SHA `9b84e041a3da9f81944a65953273d0235980a708d755f759209b356dc96c7bf7`, PASSED with 0 findings and 0 suppressions)
- PDF four-surface byte identity (all independently computed from real bytes):
  - `SHA256(repository main.pdf)` = `7fac4b5c76695edb9821dc3c2463bc281014407cd01ec5a9c4c1784d711d8cdb`
  - `repository main.pdf.sha256` = `7fac4b5c76695edb9821dc3c2463bc281014407cd01ec5a9c4c1784d711d8cdb`
  - `SHA256(artifact main.pdf)` = `7fac4b5c76695edb9821dc3c2463bc281014407cd01ec5a9c4c1784d711d8cdb` (independently downloaded artifact `10979260910` from run `36440543369`)
  - `artifact main.pdf.sha256` = `7fac4b5c76695edb9821dc3c2463bc281014407cd01ec5a9c4c1784d711d8cdb`
  - byte counts `329744` on all surfaces; result: **IDENTITY PASS**
- Terminology corpora SHAs: base `44c354e8ddcbdae6d81cd36c76e48ef676655d258da611665f354a41cadb6c3c` / supplement `adf4305554d315c930a568d3c63067123811568bd3c2df84e6cd8dab372c1829` / residual `257df61b51b3dfc06f9ade2383848c021c8ddb3a3779d88d70fc8e0479b02a27`; search forms base 178 + supplement 177 + residual 37 + 計り方 = 392 combined; hits adjudicated per occurrence ledger below
- Architecture approval provenance: Human Architecture Review r1 `APPROVED` (reviewed `9767d68e0d83aa667eaeeee6394806c612708682`, reviewed_at `2026-09-28T00:24:35Z`, record `sources/2026-W39/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`); r1 Preview `REQUEST_CHANGES` (boundary `DRAFT_COMPLETE`, record `sources/2026-W39/gates/reviews/publication-r1.json`); r2 Preview `REQUEST_CHANGES` (boundary `DRAFT_COMPLETE`, record `sources/2026-W39/gates/reviews/publication-r2.json`); approved Architecture bytes unchanged since approval
- Full r3 dossier: `sources/2026-W39/execution/reviews/publication-preview-r3-dossier.md` (required reading)

## Human decision

`PENDING` — no r3 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r3 review performed yet).

## Regeneration boundary

None selected (no r3 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
