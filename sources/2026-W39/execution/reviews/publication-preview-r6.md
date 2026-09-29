# Human Publication Preview — 2026-W39 r6 (PENDING, no decision recorded)

Generated: `2026-09-29T09:56:00+09:00` (`2026-09-29T00:56:00Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `98cffa3bbaf36801de1d7bcb8b2449cc0bb0b9d6` (exact W39-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r6 bytes under review):
  - `sources/2026-W39/publication/v2/publication-candidate-v2.json` (candidate SHA `b042be85f0cf8b7f028ac8f7a96f7d2db6fc4f06acd256960a30f992d4975563`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W39/main.pdf` (12 pages, 335817 bytes, SHA `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`, CI run `36504726702`, artifact `11006941649`)
  - `sources/2026-W39/publication/v2/reader-manuscript-v2.json` (manifest SHA `af7176f213883905f268f3249962f369f7bb1ab2442e256d79e9c3503a5895e6`)
  - `sources/2026-W39/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `5f54da01efca964791b82e76c45a5809d22a88cdd75cc748efbc9089f8bb344f`, 3 deterministic PASS)
  - `sources/2026-W39/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W39/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W39/publication/v2/reader-surface-gate-v2.json` (gate SHA `ab83ffa97d24a7550a932ea0d73716c3d70aac46f156052a920416f90ccc437b`, PASSED with 0 findings and 0 suppressions)
- PDF four-surface byte identity (all independently computed from real bytes):
  - `SHA256(repository main.pdf)` = `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`
  - `repository main.pdf.sha256` = `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`
  - `SHA256(artifact main.pdf)` = `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121` (independently downloaded artifact `11006941649` from run `36504726702`)
  - `artifact main.pdf.sha256` = `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`
  - byte counts `335817` on all surfaces; result: **IDENTITY PASS**
- Architecture approval provenance: Human Architecture Review r1 `APPROVED` (reviewed `9767d68e0d83aa667eaeeee6394806c612708682`, reviewed_at `2026-09-28T00:24:35Z`, record `sources/2026-W39/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`); r1–r5 Preview `REQUEST_CHANGES` (boundaries all `DRAFT_COMPLETE`; records `gates/reviews/publication-r1.json` through `publication-r5.json`); approved Architecture bytes unchanged since approval
- Full r6 dossier: `sources/2026-W39/execution/reviews/publication-preview-r6-dossier.md` (required reading)

## Human decision

`PENDING` — no r6 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r6 review performed yet).

## Regeneration boundary

None selected (no r6 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
