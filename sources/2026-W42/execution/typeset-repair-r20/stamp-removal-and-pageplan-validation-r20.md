# W42 r20 stamp-removal and page-plan validation (diagnostic-only; NONCANONICAL)

Date: 2026-10-18 JST. Authority: `SOL_EXECUTION_AUTHORITY / R19_SOL_PRINT_PREFLIGHT / R20_ONE_DEFECT_ONLY / NONCANONICAL`. Branch `weekly/2026-W42-v2-work`. No Architecture revision, no Stage validation/Reader/Publication/Freeze/Release, no Human Gate call.

## 0. Identity guard (read-only, before any write)

- Exact Starting Remote HEAD `b10ae74ccd815c9f2c8c2c6b9d92f1372116c2ca` == `git ls-remote` + `FETCH_HEAD`; Expected Starting Tree `9327b1fb02c894b4122aff9d28bcfc904eeb64b7` == `FETCH_HEAD^{tree}`.
- Reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19` (ls-remote + rev-parse).
- Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` (rev-parse; ancestor of reviewed main).
- r19 inspected baseline `fc5a3cdb52dd1d6f62de91d007dcd4973c5f5093`/`e4f7fa41030df236767381157105ec145d385e17` (local ancestor; Sol dispatch parent).
- All matched → proceeded. FF-only local `fc5a3cdb5` → `b10ae74cc` (1 Sol dispatch commit). No fallback/new branch, no reset/rebase/force.

## 1. Reads (no source rewrite)

- Sol r19 disposition `sol-w42-r19-print-preflight-disposition-20261018.md` (F-01/F-02/F-04 corrected, F-03 stamp split fixed but new p21 stamp-only defect; r20 one-defect authorized).
- r19 contract `2026-10-18_muse-w42-r19-typesetting-bibliography-and-pageplan-reconciliation.md` + Muse r19 session/validation/brief; r18 Reader `reader-preview-r18.PROPOSED.json` (7ch; blob `fc4fd9f2…` reconfirmed) + 7 proposals + bib-map/matrix/ledger (90/19/177); r19 display-map/policy + source hashes + exact `diagnostic-r19/main.tex` (95,034B, SHA `b845ad57…`, 965 lines wc -l) / `preview.sty` (SHA `f0492fb6…`) / manifest/log (21pp/509,010B/SHA `7aced283…`) / p1,p16–p21 PNGs.
- Preserve byte-exact reader-facing texts: 7 chapters, 136 paras/25,015 chars, 7 tables, 7 notes, 7 headings/157 reader blocks, Table7 placement; all source/category aliases byte-identical; r19 bibliography printed text unchanged (verified via extracted-text identity below).

## 2. Bounded physical fix (ONE justified deletion)

Source: exact `diagnostic-r19/main.tex` → temp `/tmp/opencode/w42r20build/main.tex`.

- Header comment line 1: `% W42 r19 …` → `% W42 r20 …` (same byte length 121B; provenance only; reported).
- Deleted exactly ONE line (index 964, 252B + 1 newline = 253B): `\begin{center}\color{SurveyMuted}--- \mbox{NONCANONICAL DIAGNOSTIC} / \mbox{NOT A PUBLICATION PREVIEW} / \mbox{NOT FOR HUMAN APPROVAL} ---\\{\footnotesize 非正準の診断文書であり、正式公開文書でも人承認用でもない}\end{center}` after `\end{thebibliography}`, before `\end{document}`.
- Result tail: `\end{thebibliography}` + blank + `\end{document}` (no trailing newline, matching r19 style). Cover macro line 9 with all three warnings byte-identical.
- Sizes: r19 95,034B → r20 94,781B (diff -253B = deleted line only; header same length). SHA r19 `b845ad577d362a67a022b530c76e0ebb38cabf74fe27c0a244c67cdb759e27ea` → r20 `909e3b87f981e5b4e5fe7cf724f23ddc683f709538efb9dba916e409f0d2b8f6`. Lines wc -l 965 → 964. `preview.sty` byte-identical (`f0492fb6…`).
- Diff (unified, n=2) shows ONLY header r19→r20 + one deleted stamp line; all other bytes identical outside span (verified via `new[1:] == old[1:964]+old[965:]`).
- TeX `NONCANONICAL` counts: r19 3 (header/cover/terminal) → r20 2 (header/cover). Cover intact. Manifest/filenames/session/page review mark `NONCANONICAL / NOT FOR HUMAN APPROVAL`; no canonical Reader/PDF paths.
- No margin/font/title/chapter/bib-print/figure/float/needspace/citation-order/reference change; no new wording/data/paraphrase/filler.

```diff
-% W42 r19 NONCANONICAL DIAGNOSTIC TeX/PDF — NOT a validated release, NOT a Publication Preview, NOT FOR HUMAN APPROVAL.
+% W42 r20 NONCANONICAL DIAGNOSTIC TeX/PDF — NOT a validated release, NOT a Publication Preview, NOT FOR HUMAN APPROVAL.
@@ -963,4 +963,3 @@
 \end{thebibliography}

-\begin{center}\color{SurveyMuted}--- \mbox{NONCANONICAL DIAGNOSTIC} / \mbox{NOT A PUBLICATION PREVIEW} / \mbox{NOT FOR HUMAN APPROVAL} ---\\{\footnotesize 非正準の診断文書であり、正式公開文書でも人承認用でもない}\end{center}
 \end{document}
```

## 3. Fresh physical diagnostic proof and QA

Built in temp clean workspace from r20 TeX + identical r19 style. Deterministic `SOURCE_DATE_EPOCH=1792311600 FORCE_SOURCE_DATE=1 lualatex -interaction=nonstopmode -halt-on-error main.tex` ×3; run1 SHA `41a0dc44…` (aux unstable), run2/run3 SHA `e0e0f56f…` identical → stable. Final `main.pdf` **20 pages, 508,316 bytes**, SHA256 `e0e0f56fc0b201144b286373e6c42c2da6277120e1e9bff30dce46fe0894e20a`; `main.log` 77,220B/1471 lines, SHA `511b6e3a…`, 0 overfull/underfull/errors/missing-glyphs/undefined (final run; first-run undefined refs resolved via reruns, as in r19). Fonts HaranoAjiMincho-Regular/Bold, HaranoAjiGothic-Bold, lmroman8/9/10/12, lmmono10, lmsans10-bold. CreationDate/ModDate 2026-10-18 17:20 JST (epoch-pinned).

Archived fresh `execution/diagnostic-r20/`: `main.tex`, `preview.sty`, complete `main.log`, `main.pdf`, `build-manifest-r20.json` (above SHAs/bytes/pages/build metadata; per-page raw `pdftotext` chars), 20 individual PNGs @150dpi (`p-01..p-20.png`) + 3 contact sheets (`contact-sheet-r20-01-p01-07.png` 1,683,966B, `-02-p08-14.png` 1,727,589B, `-03-p15-20.png` 1,312,547B), `review-pages-r20.md`.

Visual QA (ALL 20 PNGs individually opened; see `review-pages-r20.md`):
- cover 3 uninterrupted warnings, unmistakably diagnostic;
- p16→p17 no Table7/Glimpse bisection (`高密度`/`の再走査` unbroken), no isolated Table7; p16 ends at completed paragraph, p17 Table7 in-flow with complete t7-07 below;
- B28 labeled + URL complete same page, B57 readable (same ASPI/RE intra-entry wrap as r19, kept together), all 90 Bxx (71 full + 19 concise `→ [Bxx]（同一資料）`) preserved, links not clipped, 7 tables/7 notes in-chapter;
- no bib URL orphans, no machine provenance leak (TeX 0 `alias-of`/`normalization`/`CLAIM_BOUNDARY`; PDF-text block-ID pattern 0 hits), no last blank/stamp-only page, no orphan trailing stamp, no new empty pages/large blank columns;
- PDF extracted text 0 unintended internal block IDs; 286 Bxx cite occurrences (expected citations).
- Per-page raw lengths r20 identical to recomputed r19 p1–p20; full-text 47,874 vs r19 48,041 (diff 167 = r19 p21 raw). Body/bib pagination unchanged; deletion caused no other visual issue. NOT `R20_VISUAL_QA_BLOCKED`.

## 4. Page counts (remeasured, not assumed)

- r19 measured: 21 = cover1 (p1) + body16 (p2–p17) + bib3 (p18–p20) + stamp-terminal1 (p21).
- r20 measured: **20 = cover1 (p1) + body16 (p2–p17) + bib3 (p18–p20)**. Diagnostic-only terminal page eliminated; NOT counted as publication need.
- Chapters (rechecked on r20 PNGs, overlapping, NOT additive): P1 p2–p4 / P2 p4–p6 / P3 p6–p9 / P4 p9R–p11L / P5 p11R–p13 / P6 p13R–p15 / P7 p15–p17.
- Effective usable-page occupied area: `UNMEASURED; <= 16 PHYSICAL BODY PAGES`.
- Conditional (labeled, NOT rendered): approved-body 26.5 + cover1 + bib3 = **30.5** vs target28/max30 (exceeds max 0.5). r19 26.5+5=31.5 included artificial stamp; superseded. Option B indicative 17.0 (2.5+2.5+3+2.5+2+2.5+2) remains proposal-only, NOT observed 16. Architecture 26.5/target28/max30 unchanged. No filler, no r2 assumption (DRAFT_COMPLETE/approved/pending; consultation vs authorization split).

## 5. Frozen authority re-verification (read-only)

- r18 Reader blob `fc4fd9f2…`, P1–P7 proposal SHAs, bib-map `44494d98…`, ledger `d7503523…` unchanged; `editorial-revision-r18/` diff empty (working tree clean except new r20 paths before commit).
- production-state blob `63edc922…` (DRAFT_COMPLETE/approved/pending); checkpoints/approvals/review-index; canonical Draft/Synthesis v10.0; Evidence/Views/Materiality/Selection/Architecture; r11–r19 execution bytes; main + Frozen Core. All untouched.
- Only new edition-local: `typeset-repair-r20/`, `diagnostic-r20/`, one session, index append. No formal Reader/Publication, no architecture amendment.

## 6. Residuals

- B57 intra-entry ASPI/RE wrap (kept together, readable; same as r19).
- Effective area UNMEASURED (no fake metric).
- 83/90 HTTP UNVERIFIED carried from r17 (no new reachability claims).
- Contact-sheet scale 0.4 thumbs (compact; full PNGs authoritative).
- Manifest per-page chars are `pdftotext` raw (incl. newlines); r19 manifest used different counting (e.g., p1 467 vs raw 480) — correspondence proven via identical-method recomputation (r19 p1–p20 raw == r20 p1–p20), not via cross-method equality.

Stop: `SOL_W42_R20_FOCUSED_INDEPENDENT_AUDIT_READY / NONCANONICAL` (cover intact, no terminal-stamp page, all pages QA, brief reflects true pagination).
