# ERRATUM (non-mutating) — checkpoint free-text MATERIAL count vs canonical authority

Status: `IMMUTABLE_EXCEPTION / INFORMATIONAL`
Date: 2026-10-10Z (Muse r10; Sol adjudication F-W40-C01)
Scope: W40 edition only; NO rewrite of any immutable artifact performed.

## Statement

`sources/2026-W40/orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json` carries free-text fields
(`summary`, `reviews[0].evidence`) written during the r9 transition that say MATERIAL30 (or equivalent
thirty-count phrasing). The CANONICAL authority is MATERIAL29:

- `evidence/v2/views/accepted/1effd7444d88497d44741e7a359c60e42c25f8efb56361e1d739199d326e6b28/`
  (35 views: 29 MATERIAL / 4 HOLD / 2 CONTEXT);
- `materiality-ledger-v2.json` (37 rows: 29 MATERIAL / 4 HOLD / 2 CONTEXT / 2 EXCLUDED);
- this r10 count report (28 SELECTED = 20 PRIMARY / 8 SUPPORTING + 1 INSPECT + 4 HOLD + 2 REJECT).

## Ruling

- The checkpoint `summary`/`reviews[].evidence` strings are FREE-TEXT non-authority per the reviewed-main
  checkpoint schema (`build_stage_checkpoint()` validates structure, not recounts); SHA/State integrity is
  NOT broken (Sol r9 audit + Sol adjudication confirm). No rollback/rewrite is authorized or needed.
- All downstream consumers MUST use the canonical counts above (29/4/2+2; 28=20/8), never the checkpoint prose.
- This file is the correction record; future dossiers must cite it instead of the checkpoint prose.
- CV2-DM-016 remains OPEN_CORE (related deferred-maintenance context, unchanged).
