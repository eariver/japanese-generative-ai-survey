# Fusion publication timestamp verification (edition-local verification record)

- subject: `https://cognition.com/blog/local-fusion`
- fetched_at: `2026-09-19T00:00:00Z` (operator fetch; response `HTTP/2 200`, `content-type: text/html; charset=utf-8`, 361355 bytes)
- first-party authority (page metadata, two agreeing signals):
  - `<meta property="article:published_time" content="2026-09-11T10:00:00-07:00"`
  - JSON-LD `"datePublished":"2026-09-11T10:00:00-07:00"`
- UTC conversion: `2026-09-11T10:00:00-07:00` = `2026-09-11T17:00:00Z`
- canonical W37 ordinary window (end-exclusive): `[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`
- comparison: `2026-09-11T17:00:00Z < 2026-09-11T22:00:00Z` → inside window (5h margin)
- classification: `ORDINARY_WINDOW` (exact-metadata basis, not calendar-date assumption)
- prior r1 defect repaired: the prohibited `assumed ordinary daytime` statement is withdrawn; this record replaces it
- sitemap note: `https://cognition.com/sitemap.xml` lists `<lastmod>2026-09-18T00:18:41.524Z</lastmod>` for this URL; treated as page-update metadata only, not publication authority
- raw page bytes: fetched HTML retained at fetch time for audit (`/tmp` fetch, 361355 bytes); claim-relevant meta lines preserved verbatim above
