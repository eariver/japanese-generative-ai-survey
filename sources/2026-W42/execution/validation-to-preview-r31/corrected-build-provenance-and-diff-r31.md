# W42 r31 corrected build provenance and diff (r30 → r31)

Status: `SOL_W42_R31_CORRECTED_PREVIEW_READY` (pending trusted re-advance) / State `DRAFT_COMPLETE` after native Gate rollback
Date: 2026-10-20 JST. Worker: Muse (r31 integrated governed recovery execution).

## 1. Gate rollback (trusted, first-party)

- Human Publication Preview REQUEST_CHANGES r1 recorded by trusted GitHub Actions operator run (request-only commit + preflight + receipt; see session for run URL/IDs).
- State returned to `DRAFT_COMPLETE`; checkpoints `DRAFT_COMPLETE.json` / `VALIDATED_DRAFT.json` invalidated by design (receipt `removed_paths`); Architecture r1 approval preserved; r29/r30 bytes and audits retained in history.
- Stale r30 current singletons (TeX/PDF/Reader/QA/reviews/gate/candidate binding old SHAs) replaced below; old byte proof retained in prior commits.

## 2. Old → new manifest

| Artifact | r30 (stale, history) | r31 (current) |
|---|---|---|
| TeX | `2ed5848a…` 96790 B | `008b6a27…` 97154 B (+364: 6 §7 lines + header provenance line) |
| PDF | `8c7a06e7…` 505102 B, 21 pp | `02638611…` 505327 B, 21 pp (+225) |
| Reader file | `47634ae3…` | (rebuilt below; primary binds new TeX) |
| preview.sty | `f0492fb6…` (unchanged; byte-identical file retained, not rebuilt) | same bytes |

## 3. Exact TeX delta (7 changed lines, Section 7 only)

1. Header: added `% r31:` provenance line (comment, not typeset).
2. §7 deck: `ASPIREのOSS公開` → `ASPIRE v1.0公開`.
3. T7 ASPIRE row: `10月公開が今週の出来事` → `8月公開済みのリポジトリの10月16日v1.0公開が今週の出来事`.
4. §7 lead (line 720): `19.17％・79件中7位` → + `（2026年10月12日時点のVals公表値）`.
5. §7 design (line 742): `79件中7位・19.17％` → + `（2026年10月12日時点のVals公表値）`.
6. §7 body (line 759): repo-publication sentence → August-public/Oct-16-v1.0 distinction (licensing + numbers intact).
7. §7 X-post (line 763): `10月16日のX投稿` → date-neutral `告知投稿` (no new uncited fact).

Unchanged-block metrics: P1–P6 byte-identical; bibliography identical (90 keys); cites 169/729/90 same order; T1–T6 identical; T7 single ASPIRE cell corrected (109/110 cells unchanged, 1 corrected); 28/28 Selection coverage intact.

## 4. Primary evidence

- ASPIRE commits re-queried via `gh api`: `7ba73d3…` 2026-08-21T19:53:37Z `Public release`; `fa00f0ef…` 2026-10-16T03:57:48Z `ASPIRE v1.0 release`.
- Vals: 79 = Oct-12 snapshot, 72min = official hlab-v1 `1h12m` (per archived r30 audit §4; r30 F02 drift concern resolved, re-adjudicated in new reviews).
- Build: LuaHBTeX 1.24.0, `SOURCE_DATE_EPOCH=1792311600`, 3 runs (2–3 identical), 21 pages, log 0 errors/overfull/underfull/missing/warnings.
- Page map identical to r30 (tables p04/p06/p09/p12/p14/p16/p17); p16/p17/p18 char deltas confined to lengthened ASPIRE prose; no reflow, no padding.

## 5. Regenerated authorities (all validators PASS)

- Reader manuscript (same 27+2 coverage, new primary binding), quality bundle (3 deterministic + fresh result files), semantic (11) + visual (2) worker reviews with repair-aware details, separate delta surface semantic (4 checks, raw verbatim) + surface gate PASSED.
- 21 new PNGs + main.log under `validation-to-preview-r31/`; contact sheets below.
- Focused delta content/visual/surface review authority: `delta-review-raw-r31.md` (PASS, no blocking findings).
