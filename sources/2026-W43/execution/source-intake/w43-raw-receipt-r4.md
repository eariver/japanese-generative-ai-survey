# W43 r4 raw/hash receipt — Grok X + Flint first-party (2026-10-24)

No re-fetch or regeneration of Grok Raw. All hashes measured locally before consuming.

## Grok X weekly raw (Sol-imported, immutable)
- Repo path: `sources/2026-W43/external/x/weekly-x-2026-W43/weekly-x-2026-W43.md`
- Bytes: **13425** (`wc -c` readback) — matches Sol review §14.
- SHA256: `4571e0de469a7143fb1c46710c2e419a91404ff2d9538ae4d9a31a8b8f0be54a` — matches.
- Git blob: `f05a0c275f0103d0e1bfa5696bfebcae0b559536` (`git hash-object` readback) — matches.
- Sol import commit: `2282e146f2d866f832ad9ed8ee52334710c622c1` (2026-10-24T12:59:53Z). Drive source `1mNb23uZ_QB3RLqXTMmMu18Y51ahao6dO`, file `weekly-x-2026-W43.md`, observed `2026-10-24T12:43:17Z`, Drive stored 12:45Z.
- Status: PARTIAL sensor observation (NOT Evidence/Selection). Manifest `record-result` registered via canonical CLI: observed_at `12:43:17Z` (Grok), imported_at `12:59:53Z` (Sol import), PARTIAL / DISCOVERY_RECORDED → [`w43-r4-flint-20261021`, `w43-r4-grok-x-ledger-20261024`]. Manifest status now COMPLETE (= result registered, not claims verified).

## Flint first-party raw (r4 worker-fetched, read-only methods)
- Announcement HTML: `collectors/primary/runs/20261024T133000Z-muse-r4/raw/recursive-flint-announce-20261024T132900Z.html`, curl HTTP 200, **366583** bytes. Site republish stamp `Oct 23 8:37PM UTC` is Framer metadata; event date Oct 21 stands on index + HF + WIRED.
- HF API full body: `raw/hf-flint-api-full.json`, **5478** bytes (complete response archived, not a projection): `createdAt 2026-10-21T14:20:58Z`, sha `2a247be2…`, license `apache-2.0`, 733 likes.
- Derived consumption note: `notes/r4-note-01-flint-primary.md` (rendered reads, honestly labeled — not original bytes).
- r2 raw dir untouched (Kimi X HTML + 5 API projections preserved).

## Beam exclusion proof (no new bytes claimed)
- OUT on converging dates: quoted original post 09:01 EDT = 13:01Z Oct 16 (Sol review + Oct 16 tracker deck) + official blog Oct 16 + VB 6am PT Oct 16 + Baseten Oct 16. No Oct 17–23 first-party version/card/API event verified (Plotly Oct 17 = third-party eval, not release).
