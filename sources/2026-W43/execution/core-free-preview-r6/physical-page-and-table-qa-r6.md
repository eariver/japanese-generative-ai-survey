# r6 physical page and table QA (all 22 pages inspected as images)

Subject: `main.pdf` r6 (SHA256 `113b179a…`, 482659 bytes, 22 pages A4) +
`pages/p-01.png … p-22.png` (150 dpi, pdftoppm) +
`pages/contact-sheet-01..03.png`.
Inspector: Muse Worker (this session). All statements below describe the
actual inspected image bytes. No editorial-Sol / independent-auditor
inspection is claimed.

## Full-page matrix (p01–p22)

| Page | Content | Result |
|---|---|---|
| p01 | Cover (title/date/anchors/cutoff/repo/build) | PASS, no tofu, rule + headline intact |
| p02 | TOC (P1–P8, recap, bibliography) | PASS, entries + leaders legible |
| p03–p05 | P1 body + tables 1–4 + context figure box | PASS, rows complete, 典拠 notes wrap |
| p06–p08 | P2 body + tables 5–7 + code verbatims | PASS, bash/python/JSON blocks uncut |
| p09–p10 | P3 body + tables 8–9 + approval-flow figure | PASS |
| p11 | P4 prose + table 10 (recalc) + qualifiers | PASS, arithmetic + UNRESOLVED note intact |
| p12–p13 | P5 prose + tables 11–13 + figure/table notes | PASS, dense real-number matrix legible at print size |
| p14 | P5–P6 boundary (表13 ctd. + P6 prose + reading note) | PASS, no clipped cells, no overlap |
| p15 | P6 figure (5-stage) + securing prose | PASS, all 5 stages + Daybreak/CVE caveats legible |
| p16 | P7 tables 14–16 (Bio + low-resource deltas) | PASS, COBOL 40%+ prevalence separated from accuracy; cost≠quality note intact |
| p17 | P7 prose + tables + P8 head | PASS |
| p18 | P8 JSON verbatims + reading guide + guide URL + TanStack prose; `POST /v1/decisions` | PASS, URL is clean hyperlink (blue), no JP-parenthesis inside link |
| p19 | Tables 18–20 (TanStack clocks + DeepSeek) + prose | PASS, GH 15:18:14Z vs npm 15:21:49Z separated; 典拠 lines wrap, none clipped |
| p20 | P8 tail prose + reading note + **`今週の総括` + 5 paras** | PASS — production note ABSENT (authorized deletion confirmed on-page); 5 paras complete; no empty-body gap beyond normal paragraph spacing |
| p21 | Bibliography head + entries 1–~24 | PASS, long URLs wrap (mid-token breaks are TeX xurl behavior, links verified functional); qualifiers intact |
| p22 | Bibliography ctd. + NONCANONICAL banner + page number | PASS, 404 entry transparent; banner present; no truncation |

## Print-size legibility (contract focus pages)

- p07 (MemT bench matrix + rights table): PASS — 1.86x SOURCE_UNVERIFIED
  and 66x storage-only qualifiers readable; no cell clipping.
- p14 (表13 boundary): PASS — cpWER/recall/units qualifiers intact.
- p16 (Bio + low-resource): PASS — see matrix.
- p19 (TanStack + DeepSeek): PASS — see matrix.
- p21–p22 (bibliography): PASS — 36 entries complete; wraps are
  line-breaks, not missing text (all URLs present as annotations).

## Defect check (all negative)

- Tofu / missing glyphs: none on any page.
- Overlapping text / overfull runoff: none (log: 0 overfull/underfull).
- Missing/clipped table cells: none (20/20 tables, 80/80 rows visible).
- Barcode/figure loss: 3/3 figure boxes present with full bodies.
- Large empty body page: none (p22 tail whitespace is the normal
  bibliography end + banner, identical in kind to r3).
- Internal production note at recap: ABSENT (the one intended change).
- Stale r3 bytes: none — PDF hash differs from r3 (`d0fa8b56…` -> 
  `113b179a…`), TeX hash differs (`bb0e7e1d…` -> `7c052f05…`); old
  subjects tracked separately in the build manifest.

## 300 dpi spots

p-18 (POST + guide URL) and p-21 (bibliography) re-rendered at 300 dpi
for hyperlink/URL-wrap confirmation: links clean, wraps legible.
(Spot files kept in /tmp only; 150 dpi set is the committed record.)

Verdict: `R6_VISUAL_QA_PASS_WORKER` — worker-level only. Independent
all-page re-audit with real binary access is still required and is
requested separately; that reviewer must report `PDF_VISUAL_AUDIT_BLOCKED`
rather than PASS if their binary access fails.
