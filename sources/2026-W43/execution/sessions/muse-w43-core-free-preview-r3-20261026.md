# Muse W43 Core-free Preview r3 worklog — 2026-10-26/27

Branch `weekly/2026-W43-v2-work`. Contract `sol-w43-core-free-preview-r3-print-projection-citation-boundary-20261026.md`.
Worker claim: `MUSE_W43_CORE_FREE_PREVIEW_R3_READY_FOR_SOL_RECHECK`.

## Guards

Remote 6-way PASS read-only (dispatch `36bb0eb2…`/`398db9a3…` parent `f29e77eb…`, diff contract only; main/frozen match). Local `f29e77eb…` clean → ff-only → `36bb0eb2…`.

## Repairs (print-only)

- F-R3-01: SAFE path rule (internal-hint gate + API-route never-strip) restores L473 POST in projection/TeX/PDF (p-18 300dpi). r1/r2 loss eliminated.
- F-R3-02: URL_RE excludes JP punct; 34 http URLs 0 malformed; SHA via nolinkurl; PDF link boundary verified.
- F-R3-03: 18/15/2/1/0 audit (false 0-unused corrected); TanStack exact-key 典拠 line added to p8-f2 (only body addition); others natural-language traceable, no invented cites; decisions-ref-create kept as transparent 404.
- F-R3-04: allowlist (35 modified + title + 1 added) + validator PRINT_SEMANTIC_PASS (10+4, exit 0).

## Build/proof

TeX `bb0e7e1d…` (20/3/36, bib transplanted from r2 complete block); PDF `d0fa8b56…` 483305B 22p 0 warnings; 22 PNGs + 3 sheets, all inspected (POST/URL/TanStack/bib focus); manifest/fidelity/QA/carryover/visual-request built. r3.5 checker exit 0 (inputs unchanged).

## Push/readback

Non-force commit + push + readback; scope = r3 namespace + handoff + session + index only.
Final HEAD: PENDING_AT_COMMIT; Tree: PENDING_AT_COMMIT.
PDF URL: PENDING_AT_COMMIT (`.../blob/<FINAL_HEAD>/sources/2026-W43/execution/core-free-preview-r3/main.pdf`).

No State/Core/Architecture/Selection/Evidence/Gates change. Stop at Sol recheck.
