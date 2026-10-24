# W43 Screening Kimi chronology erratum r3 (2026-10-25)

Historical r2 batch/results/acceptance (`screening/v2/packages/r1`, `accepted/18525774…`) preserved unchanged. This erratum bridges r2 → r3.

## Before (r2 accepted, immutable)
- Record `w43-primary-kimi-20261023`, `batch-003`, reason: `KEEP: announce and API live Oct 23 17:15:24Z (45min inside cutoff, X HTML archived); …`
- Error: `17:15:24Z` to exclusive cutoff `22:00:00Z` is 4h44m36s, not 45 minutes. Reintroduced the old r1 error that Discovery r3 had explicitly fixed.

## After (r3 active)
- Same ID/decision/confidence/targets; reason corrected to: `KEEP: announce and API live Oct 23 17:15:24Z (4h44m36s before Oct 23 22:00Z cutoff, X HTML archived); …`
- Basis: Discovery `published_at=2026-10-23T17:15:24Z`; Profile cutoff `2026-10-23T18:00:00-04:00` = `2026-10-23T22:00:00Z`; difference 4h44m36s.

## 51-to-51 identity proof
- r3 `packages/r2` built by frozen native adapter from identical Discovery/state (package SHA `b7e9a6d4…` identical to r1 package — same inputs).
- 51 decisions reproduced by ID from r2 results; programmatic diff: exactly 1 decision object differs (`w43-primary-kimi-20261023`), exactly 1 field (`reason`); other 50 byte-identical; Kimi non-reason fields identical.
- New content-addressed acceptance `accepted/75dd95db…/screening-accepted.json` (SHA `566cde3b…`) differs from old digest `18525774…` — correction effective, no accidental equality.
- Histogram unchanged: KEEP 17 / MAYBE 11 / INSPECT 4 / DROP 19.
