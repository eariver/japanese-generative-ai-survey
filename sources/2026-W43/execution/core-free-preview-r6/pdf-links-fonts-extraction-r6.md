# r6 PDF link / font / extraction record (real bytes, not TeX inference)

Method: PyMuPDF link-annotation read + text extraction on the actual
`main.pdf` (482659 bytes, SHA256
`113b179a4fab82df28a5d9f1ac1ac6c588ce2a0a253b988ba590944057f76320`),
cross-checked with whitespace-collapsed matching. No TeX-string inference.

## Link annotations (`/Annots`)

- Total link annotations: 44 (all pages scanned 1..22).
- `http(s)` targets: 36. Non-http (internal TOC/section links): 8.
- Malformed (CJK punctuation inside URL): **0**.
- Every bibliography URL from the 36 `\bibitem`s resolves to a clickable
  annotation on the expected page: p18 = Decisions guide (1); p21 = 20
  source links (KIMI-X … securing-page-rss); p22 = 15 (bio-page …
  decisions-ref-create). Scoped npm URL keeps its `%2F` encoding in the
  target; the Japanese-parenthesis body URL from r1/r2 is gone (clean
  `\url{...}` only).
- 404 (`decisions-ref-create`) target present as printed text + annotation;
  it is recorded, never a proof (see claim-tier curation).

## Fonts (all embedded subsets, no tofu observed on any inspected page)

15 embedded subsets: LMRoman{7,8,9,10,12} (+Bold/Italic cuts),
LMMono{8,10}, LMSans10-Bold, HaranoAjiGothic-{Regular,Bold},
HaranoAjiMincho-{Regular,Bold} (all `cid` CJK). No missing-glyph boxes on
p-01/07/14/16/18/19/20/21/22 spot inspection or contact sheets.

## Extracted-text verification (actual PDF bytes)

All required strings present in extracted Unicode (whitespace-collapsed):
`POST /v1/decisions`, guide URL, scoped npm URL, GH-vs-npm separation
sentences, TanStack keys + both clocks, all load-bearing qualifiers
(`持続性能の66倍ではない`, `精度とは別`, `未実行`, `独立再現なし`),
all five recap semantic cores, `今週の総括` title.
Production note `P8の後に置く独立した締めくくり` is **absent** from the
extracted text (the authorized deletion is effective in print bytes).
36 http URLs: 0 malformed. 29 claim values verified at the TeX-visible
layer by S10; PDF extraction confirms the same values survive typesetting
(spot-checked KIMI clock, TanStack clocks, COBOL accuracy band, npm clock).

## Page boxes

A4 (595.276 x 841.89 pt), 22 pages. No `/MediaBox` anomalies reported by
pdfinfo. No large empty body page (full-page matrix in the QA doc).

## Limitation

Text extraction confirms presence, not typographic perfection; glyph-level
visual QA is recorded separately in `physical-page-and-table-qa-r6.md`
(actual inspected PNGs, not extraction alone).
