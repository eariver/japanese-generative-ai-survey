# W43 r3.4→r3.5 source crosswalk delta (edition-local, UNVALIDATED)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED`. Base: `w43-r3-4-source-crosswalk-delta.md` + `w43-r3-3-source-crosswalk.md` (37 keys).
No citation key added, removed, or re-pointed in r3.5. No new primary read. Two physical-row bindings corrected; evidence authority unchanged.

## Changed (2 physical rows only, R32-FULL-003 P1)

- `p7-f1-01` (COBOL): reader physical now prints enterprise share explicitly —
  `…・企業現場40%超（オンラインバンキング言及、精度とは別）`.
  Claim `40%+ / enterprise share / COBOL (field) / percent of online banking` stays bound to `p7-f1-01`
  (own-block, stable identity, count 29 preserved). Qualifier separates prevalence from benchmark
  accuracy `10.9→72.1` (same row, distinct facet). Provenance stays accepted-derived
  `task-160489b77720f40bd1e1 claim-3` (`Enterprise feedback-driven (COBOL 40%+ online banking…)`),
  `ARCHIVE_UNAVAILABLE (page day-only)` — honestly qualified, not promoted to raw-primary.
  Ledger `p7-f1-01` note clarified: `+ enterprise 40%+ online banking (prevalence, accuracy separate per r3.5)`.
- `p8-f2-03` (registry clock): reader physical now prints full npm timestamp with role separation —
  `版固定 ｜registry／releaseの時刻（npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠） ｜…`.
  Claim `2026-10-22T15:21:49Z / registry clock / TanStack AI 1.0.0 npm` stays bound to `p8-f2-03`
  (own-block, stable identity, count 29 preserved). GH `15:18:14Z` vs npm `15:21:49.491Z` kept as separate
  origins; ledger clock retains millis `.491Z`, reader displays seconds (documented normalization);
  scoped URL `https://registry.npmjs.org/@tanstack%2Fai` + `RAW_NOT_ARCHIVED` preserved.
  Ledger `p8-f2-03` note clarified: `physical prints npm 2026-10-22T15:21:49Z (GH 15:18:14Z separate)`.

## Unchanged (explicitly re-affirmed)

MEMT-README (66x storage line 24 / parametric scope line 55 / license 208–219; 1.86x SOURCE_UNVERIFIED),
patch-rendered (stages 17–22, Daybreak/checker outside, CVE unidentified≠absent), tanstack-gh
(15:18:14Z archived) + tanstack-npm (15:21:49.491Z, RAW_NOT_ARCHIVED, scoped), all other 32 keys
byte-identical in meaning. 96 blocks / 20 tables / 80 rows (78 DATA + 2 NOTE) / 29 claims preserved.
r3.4 bytes intact.
