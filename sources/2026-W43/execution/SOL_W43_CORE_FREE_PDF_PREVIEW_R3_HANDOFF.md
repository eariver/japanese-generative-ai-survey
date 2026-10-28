# SOL_W43_CORE_FREE_PDF_PREVIEW_R3_HANDOFF

Status: `MUSE_W43_CORE_FREE_PREVIEW_R3_READY_FOR_SOL_RECHECK`
Date: 2026-10-26/27. Branch: `weekly/2026-W43-v2-work` (existing only).
Sole contract: `sol-w43-core-free-preview-r3-print-projection-citation-boundary-20261026.md`

## 0. Guards (read-only PASS, ff-only)

- Dispatch `36bb0eb22a4a4212865550be6ebc06a8ac946306` / `398db9a33b3260e94298f4198b9871f54efbba62` == origin; parent `f29e77ebf4637721ae880aea7ae9c5c3062396e8` / `22371300ee060eace667c09731fb3b069d2b5dfa` (r2 per §0); diff = contract file only.
- main `041a08df…`/`a134dc36…`, frozen `774dd39a…`/`cd46a6f7a…` verified via API+ls-remote.
- Local `f29e77eb…` clean → fetch + ff-only → `36bb0eb2…`. No reset/rebase/force/branch/PR/main/Core writes.

## 1. r2 blockers repaired (print-only, no source change)

- F-R3-01: L473 `` `POST /v1/decisions` `` was stripped by path rule in r1/r2; r3 SAFE rule (strip only internal-hint spans; never HTTP-method+path) preserves it → projection code span + TeX `\texttt` + PDF p-18 verified (300dpi). Validator P-API-route PASS; N-API-deleted detects mutant.
- F-R3-02: r2 `\url{…decisions（観測…}` greedy match fixed by excluding JP punct from URL_RE; r3 TeX 34 http URLs 0 malformed (validator PASS; N-malformed-url detects injection). SHA via `\nolinkurl` (breakable, no false link). PDF p-18 link boundary verified.
- F-R3-03: false `0 unused` corrected to exhaustive 18/15/2/1/0 audit (exact/natural/secondary/unavailable/orphan=0). Minimal repair: TanStack exact-key 典拠 line added to p8-f2 (GH≠npm, RAW_NOT_ARCHIVED); others traceable via explicit natural language + crosswalk without invented cites (DI-ENV/LICENSE as file-provenance further reading; decisions-ref-create retained solely as transparent 404 record).
- F-R3-04: allowlist for every changed line (TITLE/TOKEN×33/PATH×12/DUP×1/TANSTACK+1/POST-identical) + `print-semantic-fidelity-check-r3.py` → `PRINT_SEMANTIC_PASS` (10 pos: API/20/80/3fig/29 literals/recap/URLs/qualifiers/TanStack; 4 neg: API deletion, clock swap, JP-URL, qualifier strip — all detected), exit 0. No global regexp strip of `/`.

## 2. Outputs (NEW r3 namespace only)

`execution/core-free-preview-r3/` (projection `63ad2617…`, diff+allowlist, checker+result, tex `bb0e7e1d…` 20/3/36, sty, pdf `d0fa8b56…` 483305B 22p 0 warnings, log, 22 PNGs + 3 sheets, key-audit, fidelity, QA, carryover, visual-request, manifest, build-doc) + this handoff + session + index append. r1/r2/r3.5 immutable. State/Architecture/Selection/Evidence/Gates/main/Frozen untouched. No Stage/Freeze/Release. `.aux/.toc/.out` excluded; `main.log` force-added.

## 3. Volume/coverage

Carryover: 31 indexed (20/11 observed, no new authority), all visible, 19 placements, recap, tiers preserved. 22p honest (1/1/18/2) vs 38/44; W42 21p precedent; no padding; no material missing must-cover → no VOLUME stop on coverage grounds. Sol adjudicates Human Gate sufficiency; separate independent semantic + all-page visual audit still required (this connector cannot render-verify binary beyond PNG readback).

Final HEAD/Tree via push/readback (handoff cannot self-contain hash). Commit-pinned PDF URL in session/final report post-push.

`MUSE_W43_CORE_FREE_PREVIEW_R3_READY_FOR_SOL_RECHECK`
