# Human Architecture Review — 2026-W35 r1 (REQUEST_CHANGES recorded)

## Reviewed authority

- Edition: `2026-W35` (WEEKLY + WEEKLY_MAGAZINE), target gate `ARCHITECTURE_REVIEW`
- Reviewed repository commit SHA: `676160e325db35840af1f36b8cac8c3dad54beb4` (production HEAD under review; presentation shell `a5ab5113ce3d3ab41cdbd1a8121d534c4c5fd455`)
- Lifecycle at review: `ARCHITECTURE_ESTABLISHED`; terminal `HUMAN_GATE_REACHED`
- Gate inputs reviewed (r1 bytes):
  - `sources/2026-W35/architecture-v2.json` (r1 thesis with unsupported cluster aggregation)
  - `sources/2026-W35/architecture-review-summary-v2.json`
  - `sources/2026-W35/architecture-review-attention-v2.json`
- Full r1 dossier: `execution/reviews/architecture-r1-dossier.md`
- Machine review record: `sources/2026-W35/gates/reviews/architecture-r1.json` (canonical); index `sources/2026-W35/gates/review-index.json`

## Human decision

`REQUEST_CHANGES` (revision 1).

Recorded via canonical `survey_human_gate_v2.py request-architecture-revision` against the exact reviewed bytes above; reviewed-by `Human Owner`; no-later-than anchor `2026-09-15T08:56:25+09:00` (Sol handoff commit time; the decision demonstrably existed by then; exact Human action time not separately timestamped).

## Requested changes

Remove/repair thesis-level aggregation of unsupported `sub-5%`, common-license, and common-offload claims while preserving the accepted Selection and five-package structure. Detail: restate P1 at the common-cluster level actually supported by accepted Evidence (per-model ratios 18B/320B, ~6B/125B, ~49B/770B; per-model bounded license states; preview statuses explicit; benchmark/vendor-claim boundaries preserved; X as community signal only). No other Human changes were requested; none invented.

## Regeneration boundary

`SELECTION_COMPLETE` (bounded Architecture-only correction; no Discovery/Screening/Evidence/Materiality/Completeness/Selection rerun; dispositions unchanged).

## Shared-Core implication

None. Edition-local Architecture correction; no Core defect discovered; no repair branch or PR; `main` and Production Line untouched and unmerged by design.

## Supersession note

r1 Architecture artifacts were invalidated by the canonical machinery (removed paths recorded in the run log); r2 was regenerated from the unchanged Selection and is presented separately in `architecture-r2.md`. This r1 record is preserved as immutable review history.
