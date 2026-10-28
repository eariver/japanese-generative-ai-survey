# W43 Core-free Preview r3 — independent semantic/visual review request (PROPOSED)

To: Independent Sol. From: Muse Worker. Worker claim: `MUSE_W43_CORE_FREE_PREVIEW_R3_READY_FOR_SOL_RECHECK` (pending Sol adjudication; BLOCKED only if new defects found).

## Fixed pointers (verify after push/readback)

- r3.5 source `6f07cb49…`, ledger `6fd9d6fe…`, manifest `85d94d74…` (checker PASS).
- r3 projection `63ad2617…`, TeX `bb0e7e1d…` (20 tables/3 figs/36 bib), PDF `d0fa8b56…` 483305B 22p, log 0 warnings, 22 PNGs + 3 contact sheets (SHA map in manifest).
- F-R3-01: PDF p-18 `POST /v1/decisions` restored (300dpi verified). F-R3-02: body URL clean, 0 JP-in-URL (validator PASS). F-R3-03: 18/15/2/1/0 key audit; TanStack exact keys now in print. F-R3-04: allowlist + `PRINT_SEMANTIC_PASS` (10 pos + 4 neg, exit 0).

## Scope

- Verify every r3 page image vs TeX: POST presence, URL boundaries, TanStack note, 20 tables, code/URLs, bib completeness, P8→recap→refs, no new layout defects.
- Verify 36 bibitem provenance displays + GH≠npm separation + post-cutoff guards.
- Adjudicate volume (22 vs 38) and whether r3 print is fit for Human PDF viewing.

No independent PASS, Human decision, Stage, Freeze/Release claimed. If media access blocked, report `PDF_VISUAL_AUDIT_BLOCKED`, not PASS.
