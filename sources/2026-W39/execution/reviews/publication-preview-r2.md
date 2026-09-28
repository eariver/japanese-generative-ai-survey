# Human Publication Preview — 2026-W39 r2 (PENDING, no decision recorded)

Generated: `2026-09-28T23:23:00+09:00` (`2026-09-28T14:23:00Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `d95a811abd014ad4476d8f305b792920aa6e87fe` (exact W39-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r2 bytes under review):
  - `sources/2026-W39/publication/v2/publication-candidate-v2.json` (candidate SHA `5a9b9633bd95320ae5f7743396a202d162564427f406f1315d98df7724879f9e`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W39/main.pdf` (12 pages, 328743 bytes, SHA `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db`, CI run `36434164543`, artifact `10975205959`)
  - `sources/2026-W39/publication/v2/reader-manuscript-v2.json` (manuscript SHA `4e7d29ee54dc82fda4ee7f622c44a69e3be3029fad45290eb38355cc5882748a`)
  - `sources/2026-W39/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `344b424aa46485435f0164debf717e1ea4dbbd5d61f560297ed71d61f5cb02e2`, 3 deterministic PASS)
  - `sources/2026-W39/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W39/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W39/publication/v2/reader-surface-gate-v2.json` (gate SHA `538a0f25d1ee3d14f8d1186e049bab5a48f63c083536d66e8fbf542054e2faec`, PASSED with 0 findings and 0 suppressions)
- PDF four-surface byte identity (all independently computed from real bytes):
  - `SHA256(repository main.pdf)` = `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db`
  - `repository main.pdf.sha256` = `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db`
  - `SHA256(artifact main.pdf)` = `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db` (independently downloaded artifact `10975205959` from run `36434164543`)
  - `artifact main.pdf.sha256` = `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db`
  - byte counts `328743` on all surfaces; result: **IDENTITY PASS**
- Terminology corpus SHAs: base `44c354e8ddcbdae6d81cd36c76e48ef676655d258da611665f354a41cadb6c3c` / supplement `adf4305554d315c930a568d3c63067123811568bd3c2df84e6cd8dab372c1829`; search forms base 178 + supplement 177 = 352 combined; hits adjudicated per occurrence ledger below
- Architecture approval provenance: Human Architecture Review r1 `APPROVED` (reviewed `9767d68e0d83aa667eaeeee6394806c612708682`, reviewed_at `2026-09-28T00:24:35Z`, record `sources/2026-W39/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`); r1 Preview `REQUEST_CHANGES` (boundary `DRAFT_COMPLETE`, record `sources/2026-W39/gates/reviews/publication-r1.json`); approved Architecture bytes unchanged since approval
- Full r2 dossier: `sources/2026-W39/execution/reviews/publication-preview-r2-dossier.md` (required reading)

## Human decision

`PENDING` — no r2 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r2 review performed yet).

## Regeneration boundary

None selected (no r2 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
