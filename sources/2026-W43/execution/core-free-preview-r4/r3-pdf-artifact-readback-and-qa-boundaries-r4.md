# W43 r3 PDF artifact readback and QA boundaries r4

Fixed r3 subject: HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`, Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`.

## Remote blob readback (GitHub API, exact)

- `core-free-preview-r3/main.pdf`: blob `4e016ab1e2beec8b4063778226e0404184ffcbc3`, 483305 bytes; local SHA256 `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca` (matches committed bytes).
- `core-free-preview-r3/main.tex`: blob `79a90d4098a4b87605588d6cc57c7e785062d6d9`, 91053 bytes.
- `core-free-preview-r3/pages/p-18.png` (POST/URL page): blob `22bfb2df64a574b8fcacf40fc992b2298af7b470`, 344880 bytes. All 22 PNGs + 3 contact sheets present under same tree.

## Independent local byte/text verification (Muse, NOT Sol)

- Raw SHA256 recomputed locally: `d0fa8b56…` == declared. `pdfinfo`: 22 pages, A4, LuaLaTeX.
- `pdftotext` extraction (44513 chars, whitespace-normalized): `POST /v1/decisions` x1, `tanstack-gh` x2, `tanstack-npm` x2, `持続性能の66倍ではない` x1, `精度とは別` x1, `15:21:49` x4, `15:18:14` x4, `今週の総括` x1, `NONCANONICAL` x1. Protected values present in PDF text layer with GH≠npm separation intact.

## Explicit boundaries (what this is NOT)

- Reading `main.log` (0 warnings), remote blob existence/size, local SHA256, and `pdftotext` string presence **do NOT constitute independent all-page visual QA**. Layout defects (clipping, floats, fonts, caption detachment, near-empty pages) cannot be established from logs or text extraction.
- Muse inspected r3 PNG renderings locally in-session (contact sheets + p-18/p-21 300dpi spot checks: POST restored, URL boundary clean, bib complete). Sol has independent obligation to commission a **separate Sol semantic + all-page visual audit with real binary/page access**; if that auditor cannot retrieve PDF/PNG bytes it must state `PDF_VISUAL_AUDIT_BLOCKED`, not PASS.
- No Human PDF decision, no Stage/validation, no Freeze/Release follows from this readback.
