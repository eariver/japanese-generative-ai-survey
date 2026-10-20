# W42 r30 L03 — independent re-render of immutable r29 PDF and page equivalence

Scope: Sol disposition `W42-R29-L03` (MEDIUM / VERIFICATION-LIMIT). Source PDF and canonical PNGs unchanged.
Date: 2026-10-20 JST. Worker: Muse (W42 r30 execution). Worker evidence, not an independent verdict.

## Inputs (immutable, byte-verified before render)

- PDF: `surveys/weekly/2026-W42/main.pdf`, SHA256 `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9`, 505102 bytes, `%PDF-1.7`
- Reference PNGs: `sources/2026-W42/execution/publication-build-r29/pages/p-01.png` .. `p-21.png` (committed at r29)

## Renderer (recorded)

- PyMuPDF 1.28.2 (MuPDF 1.28.2), Python bindings, `page.get_pixmap(dpi=150)`
- Page size: 595.3 × 841.9 pt (A4) on all pages
- Command pattern: `pymupdf.open(pdf)` → per-page `get_pixmap(dpi=150)` → PNG save (no PDF modification)

## Results

- Page count: **21** (matches `Output written on main.pdf (21 pages, 505102 bytes)` and build manifest)
- Page dimensions: uniform A4 on all 21 pages
- Pixel comparison vs committed PNGs (SHA256 per page):
  - **Byte-identical: 21/21 pages** (p-01 through p-21, differing: none)
- Outcome: full page mapping and visible equivalence established at identical pipeline + resolution. No antialias-tolerance argument needed; no renderer-difference mislabeling (same-renderer comparison, both sides hashed).

## Limitations

- Equivalence is proven for this renderer/resolution pair. A different renderer (e.g., Poppler) was not run; cross-renderer pixel identity is not claimed.
- Log-cleanliness ≠ visual proof; here both hold (log 0 errors/warnings per r29 manifest; pixels identical per this check).

## Conclusion for formal visual evidence

`EXACT_PDF_VISUAL_REVIEW` can cite: immutable PDF SHA256 + 21/21 byte-identical re-render + all-21 committed PNGs + r26→r29 p02–p21 blob identity (independent r29 report §2.2). Source PDF and PNGs were not altered to force equality.
