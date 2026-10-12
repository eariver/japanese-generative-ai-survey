# W41 r9 editorial inheritance supplement (r8 PASS assets preserved)

Status: `EDITION_LOCAL / SUPPLEMENT / NON_CANONICAL`
Date: 2026-10-13 JST
Operator basis: invalidation seq 1 (`architecture-invalidation-0001.json`, `69bf505d…`)
to CANDIDATES_NORMALIZED; regeneration r9 completed to ARCHITECTURE_ESTABLISHED.

## Preserved r8 assets (unmodified, still valid)

- `execution/architecture-resource-plan-r8.md` — 6 packages, 57–80 paragraphs,
  shares 20/18/25/7/18/12, 3 comparison tables + 5–7 spec boxes, uncapped.
- `execution/claim-evidence-trace-r8.md` — 20 SELECTED rows with claim/source IDs.

Both files reference r6/r7 SHAs in prose; those SHA references are historical
evidence of the reviewed preview lineage, not live basis pointers. They are NOT
silently rewritten. The live canonical basis after r9 is recorded below.

## Old basis → new basis crosswalk

| Artifact | r7 (pre-invalidation) | r9 (current canonical) | Meaning change |
|---|---|---|---|
| Materiality ledger | `51890f067daf…` (37: 20/13/3/1) | `51890f067daf…` (identical bytes) | none |
| Completeness | `f3d5a122534b…` (residual[9] with legacy spans) | `5340aa87464e…` (residual[9] JP bounded, spans absent) | residual[9] only |
| Matrix | `0d56de2b8b1b…` (36) | `edab1ea81912…` (36, rows identical, basis rebound) | basis only |
| Selection | `3bedcb4a…` (20/13/2/1) | `47910f2a3487…` (assignments identical, basis rebound) | basis only |
| Architecture | `3554041e3d54…` (6 pkgs) | `9a79e8d37ca9…` (texts + boundaries identical, basis rebound) | basis only |
| Summary | `f3058466c828…` (READY, legacy spans in residual[9]) | `b7274c38755b…` (READY, spans absent) | residual[9] via Completeness |
| Attention | `4b274a87ac47…` (39 items) | `d2fe8ffa96a8…` (items identical, basis rebound) | basis only |

Assignments, placements, must-cover counts (27), and package structure are
unchanged. The r8 dossier, trace, and resource plan therefore remain applicable:
re-read every SHA citation in those files through this table.

## Editorial quality carried forward

- 6-package technical composition, 27 must-cover, 57–80 paragraph budget, 3 tables +
  5–7 boxes, no PDF page cap, no degeneration into spec lists: all preserved.
- Mistral Large 4 Draft guard: official blog/docs pin 52B active; the 49B figure is a
  secondary X-derived record whose original X post was NOT directly fetched — keep the
  disagreement unresolved in Draft and never reconcile 49B as an official pin. Source:
  Matrix boundary + Card claim-2 (SOCIAL_OBSERVATION) + Architecture P3 must-cover.
- textGrain guards preserved: tech-report PDF binary-unparsed (no method beyond blog
  facts); all figures vendor-run, never independently reproduced.
- Weight-declaration vs download-verification distinction preserved: publisher
  open-weights statements are distinct from downloaded bytes (Clef/SPDX, Liquid,
  Beam intent, Mistral end-of-month, Perplexity paths). No downloaded-bytes claim
  beyond stated locations in Draft.
- Vendor-metric guards preserved: 44% is time-to-start (not wall-time); Decisions 10x
  has no methodology on page; all benches publisher-measured.

(End of file)
