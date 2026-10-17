# W42 r14 visual review index (independent-auditor readable)

Status: `NONCANONICAL / NOT A PUBLICATION PREVIEW`. PDF built from r14 proposals (v14.0) only; canonical Draft/State/Gate untouched.

## How a separate read-only session can inspect these pages

1. **GitHub web (recommended):** open any PNG below — GitHub renders images inline. Directory: `sources/2026-W42/execution/preview-r14/pages/` on branch `weekly/2026-W42-v2-work` (exact commit SHA in the build manifest footer).
2. **Raw file URLs:** `https://raw.githubusercontent.com/eariver/japanese-generative-ai-survey/<commit>/sources/2026-W42/execution/preview-r14/pages/p-XX.png` and `.../main.pdf` (replace `<commit>` with the exact pushed HEAD in the manifest footer).
3. **This index + contact sheets** give the full-page overview without downloading the PDF.

## Files and hashes

- `preview-r14/main.pdf` — 17 pages (LuaLaTeX, TeX Live 2026). SHA256 + byte length in build manifest (computed at commit).
- `preview-r14/main.tex` (744 physical lines via `wc -l`) + `preview.sty` (verbatim W41 layout; only documented deviation is the package-name rename, no macro changes).
- `preview-r14/main.log` — committed complete build log via `git add -f` (repo `.gitignore` excludes `*.log`; remote blob read-back verified).
- Contact sheets: `pages/contact-01-09.png`, `pages/contact-10-17.png` (3-col thumbnails).
- Per-page PNGs @150dpi with SHA256 in the manifest table below.

## Page images (relative links render on GitHub web)

### p-01.png — cover (title/deck/NONCANONICAL marker/cutoff/repo/build)
![p-01](pages/p-01.png)
### p-02.png — P1 body
![p-02](pages/p-02.png)
### p-03.png — P1 body + P1 table
![p-03](pages/p-03.png)
### p-04.png — P1/P2 boundary + P2 table
![p-04](pages/p-04.png)
### p-05.png — P2 body
![p-05](pages/p-05.png)
### p-06.png — P3 body (MTP Table-8 paragraphs)
![p-06](pages/p-06.png)
### p-07.png — P3 body + note
![p-07](pages/p-07.png)
### p-08.png — P3 table + P4 start
![p-08](pages/p-08.png)
### p-09.png — P4 body + P4 table
![p-09](pages/p-09.png)
### p-10.png — P4 body
![p-10](pages/p-10.png)
### p-11.png — P4/P5 boundary + P5 table
![p-11](pages/p-11.png)
### p-12.png — P5 body + P5 sources area
![p-12](pages/p-12.png)
### p-13.png — P6 body + P6 table
![p-13](pages/p-13.png)
### p-14.png — P6 body + P7 start
![p-14](pages/p-14.png)
### p-15.png — P7 table + P7 closing (chapter-end partial, flagged)
![p-15](pages/p-15.png)
### p-16.png — bibliography head (B01–B45 area)
![p-16](pages/p-16.png)
### p-17.png — bibliography tail (B46–B59) + NONCANONICAL marker
![p-17](pages/p-17.png)

## Per-page visual QA checklist (150dpi renders inspected)

| page | content | overflow/clipped | tiny type | mojibake | table ok | verdict |
|---|---|---|---|---|---|---|
| 1 | cover | none | none | none | n/a | PASS |
| 2 | P1 body | none | none | none | n/a | PASS |
| 3 | P1 + table 1 | none | none | none | ok | PASS |
| 4 | P1/P2 + table 2 | none | none | none | ok | PASS |
| 5 | P2 body | none | none | none | n/a | PASS |
| 6 | P3 body (Table-8) | none | none | none | n/a | PASS |
| 7 | P3 body + note | none | none | none | n/a | PASS |
| 8 | P3 table + P4 start | none | none | none | ok | PASS |
| 9 | P4 body + table 4 | none | none | none | ok | PASS |
| 10 | P4 body | none | none | none | n/a | PASS |
| 11 | P4/P5 + table 5 | none | none | none | ok | PASS |
| 12 | P5 body | none | none | none | n/a | PASS |
| 13 | P6 body + table 6 | none | none | none | ok | PASS |
| 14 | P6 body + P7 start | none | none | none | ok (P6 table in-chapter) | PASS |
| 15 | P7 table + closing | none | none | none | ok (in-chapter; chapter-end partial ~35% flagged, not a defect) | PASS |
| 16 | bibliography B01–B45 | none | none | none | n/a | PASS |
| 17 | bibliography B46–B59 + marker | none | none | none | n/a | PASS (tail carries 14 entries; normal bib tail, not a 2-entry orphan) |

Log-level QA: zero `Overfull/Underfull \hbox`, zero `Missing character`, zero undefined citations/refs after final runs; zero `Overfull \vbox` (the r13 43.6pt float warning is GONE — early table placement fixed the root cause). Per-row table cites verified on p-08/p-13/p-15 renders.

## TeX/PDF QA limitations (honest)

- This is Muse's own visual QA, NOT an independent auditor PASS (per contract, independent review is separate).
- Remote fetch (GitHub web/API) was not testable from this session; paths above are the documented retrieval route. If the auditor's text-only API cannot fetch binary PNG/PDF, report `PDF_INDEPENDENT_VISUAL_QA_BLOCKED` with this index as the handoff.
- p15 (~35%) and p17 (bib tail) are partial pages by construction (chapter end + bibliography tail). No padding was added.
