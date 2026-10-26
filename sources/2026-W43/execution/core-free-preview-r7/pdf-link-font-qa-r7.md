# W43 r7 PDF link / font / text-layer QA (real bytes)

Tooling: `pdfinfo` / `pdffonts` / `pdftotext -layout` + pymupdf annotation walk
on real `main.pdf` (SHA256 `5d01f496…`, 487514 B, 22p A4). Never inferred from
TeX literals. Raw machine dump: `pdf-links-fonts-raw-r7.json`.

## Links

- 83 total annotations: 75 URI + 8 GoTo (TOC §1–§8 internal links).
- 75 http annot rects → **28 unique http URIs**, 0 malformed (no spaces/CJK/
  unescaped; npm scoped registry correctly percent-encoded
  `https://registry.npmjs.org/@tanstack%2Fai` ×2 rects).
- Rect count (75) > URI count (28) because narrow two-column bib lines split
  long URLs across lines (one annot per line fragment). r6 reported 44 annots
  under its counter; the difference is fragmentation from two-column reflow,
  NOT added/removed destinations (unique-URI set compared below).
- Required destinations all present + clickable: Decisions guide
  (10 rects, p18), `POST /v1/decisions` in text layer (p18), GH
  `…/releases/tags/%40tanstack%2Fai%401.0.0` + `15:18:14` in text (p19),
  npm `15:21:49.491Z` in text (p19), KIMI-X `17:15:24Z`, all 36 bib keys'
  URLs or explicit URL-less records (tanstack-blog URL未取得, flux-keyframes
  URL未取得, recap派生 URL未取得 — matches r6 bib, no silent drops).
- No Japanese-parenthesized official Decisions URL (clean URL used).

## Fonts

14 embedded subsets, all `emb=yes sub=yes uni=yes` (pdffonts):
LMRoman{7,8,9,10,10-Bold,12,12-Bold}, LMSans10-Bold, LMMono{8,10},
HaranoAjiMincho-{Regular,Bold}, HaranoAjiGothic-{Regular,Bold}.
CJK body + Latin/code coverage confirmed; no tofu observed p01–p22 at
inspected scales. Creator LuaLaTeX, Producer LuaTeX-1.24.0.

## Page boxes / metadata

A4 (595.276×841.89pt) all pages, no rotation/encryption. Title
`Japanese Generative AI Technical Survey – 2026-W43`; Subject+Keywords
`NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` (safety layer intact).

## Limits

Annotation semantics (which rect belongs to which bib key) mapped by
page+proximity, not per-key click-tested in a viewer. Independent re-audit
should click-sample bib URLs.
