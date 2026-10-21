# W42 r21 float-boundary repair and layout comparison (diagnostic-only; NONCANONICAL)

Date: 2026-10-18 JST. Authority: `SOL_EXECUTION_AUTHORITY / R20_INDEPENDENT_REQUEST_CHANGES_ADOPTED / R21_NONCANONICAL_TYPESSETTING_ONLY` + `SOL_R21_SUPPLEMENT / USER_OPTION_B_EDITORIAL_PREFERENCE_NOT_GATE`. Branch `weekly/2026-W42-v2-work` (existing only). No Architecture revision, no Stage validation/Reader/Publication/Freeze/Release, no Human Gate call.

## 0. Identity guard (read-only, before any write)

- Exact Starting Remote HEAD `78e6275e477d93756d972cf004ee206716c400a4` == `git ls-remote` + `FETCH_HEAD`; Expected Starting Tree `711d8b97fa170a93082cfa148ce7c31b408b4e20` == `FETCH_HEAD^{tree}`.
- Reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19` (ls-remote + rev-parse).
- Frozen Core v2 `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` (rev-parse; commit exists, tree matches; ancestor path verified via `774dd39a^{tree}`).
- Independently audited r20 `f44d3301cde2ef0b9ead52f9613e4a08a6ea42e4`/`cc58032feb618cabb7e142a4fd5d36f91e59492a` (local ancestor before FF).
- All matched → proceeded. FF-only local `f44d3301c` → `78e6275e4` (2 Sol dispatch commits: r21 instruction + Option B supplement). No fallback/new branch, no reset/rebase/force.

## 1. Reads (no source rewrite)

- r21 F-08 contract + Option B addendum (both as execution contract) → Sol r20 disposition (F-08 remaining, p21 stamp fixed, `HUMAN_PAGEPLAN_CONSULTATION_READY`) → Human Option B preference record (7ch/28sel, 17.0 provisional, 21/23 Sol-proposed not Human-approved) → r20 Muse session/validation/brief + r20 TeX/style/log/manifest/PDF/20 PNGs + r19 display-map/policy + r18 Reader `reader-preview-r18.PROPOSED.json` (7ch/136P/25015ch/7T/7N/7H/157 blocks; blob `fc4fd9f2…`) + 7 proposals (P1 `b6e1c7cc…` P2 `badbbbd0…` P3 `d81023c1…` P4 `e8b7aa46…` P5 `bde64f2c…` P6 `aedfb8f4…` P7 `9e8924ea…`) + bib-map `44494d98…`/ledger `d7503523…`/dup-matrix `e7025ca6…` (90/19/177) → architecture-v2 (26.5/28/30) + r1 basis/gates + production-state `63edc922…` (`DRAFT_COMPLETE`/approved/pending). MD wrapper excluded from print by construction. No r18 master edit. No new depth research.

## 2. Problem (r19 + r20, independently inspected)

- P4 Table4 at PDF p12 top AFTER P5 heading on p11 right (r20). TeX Table4 lines 436–453 BEFORE P5 `\section` line 468, but `table*[htbp]` in `\twocolumn` defers to next page top.
- P5 Table5 at p14 top AFTER P6 heading on p13 right. TeX Table5 526–539 before P6 section 569.
- P6 Table6 at p16 top AFTER P7 heading on p15 right. TeX Table6 635–648 before P7 section 675.
- Table1/2/3/7 already acceptable in r20; must protect. Table7/Glimpse unbroken, B28/B57 keep-together, B74 clean, B90 terminus, 0 machine-provenance must hold.

## 3. Alternatives rendered (both genuinely compiled, source-bytes-preserving, print-only)

### Alt A — FloatBarrier before next chapter (ADOPTED as r21 final)

- Change: `main.tex` + `\usepackage{placeins}` (1 line) + 3× `\FloatBarrier` immediately before P5/P6/P7 `\section` (3 lines). Table4/5/6 source positions unchanged (after own-chapter prose). `preview.sty` byte-identical (`f0492fb6…`).
- Build: deterministic epoch ×3, all three byte-identical (SHA `2a188e40…` without bib fix; final with bib fix `b8ac6172…`, see §4). 21pp in both.
- Result (visual, all pages opened):
  - p12: Table4 top, then P5 heading below on same p12 → Table4 BEFORE P5 heading. SOLVED.
  - p14: Table5 top, then P6 heading below on same p14 → SOLVED.
  - p16: Table6 top, then P7 heading below on same p16 → SOLVED.
  - p01–p10 PNG byte-identical to r20 (cover/Table1-3/P1-P4 early preserved).
  - Cost: p11 right-column bottom honest blank (P5 heading pushed), body 16→17pp, bib still 3pp, total 20→21pp. No table-only pages. p18 is honest short P7 tail (702 chars, left-column only) to inherited `\clearpage` before bib, not padding.
- Logical reading preserved: tables remain after full chapter details (summary position), then next heading on same page below table. Preferred for `Retain printed reading order`.

### Alt B — Early relocation within same chapter, no barrier (EVALUATED, REJECTED for final)

- Change: cut Table4 (18 lines) from after Decider to after Scion-API paragraph (early P4); Table5 (14 lines) from after METR to after 主体分け (early-mid P5); Table6 (14 lines) from after Deep Review to after 道具寄与 (early-mid P6). No new packages, `preview.sty` identical. +3 provenance comments +3 blanks (971 lines wc -l).
- Build: deterministic ×3, byte-identical SHA `af413d85…`, 20pp (same as r20).
- Result (visual):
  - p11: Table4 top, P5 heading on p12 → Table4 BEFORE P5 heading. SOLVED.
  - p13: Table5 top, P6 heading at bottom of same p13 → SOLVED.
  - p15: Table6 top, P7 heading on p16 → SOLVED.
  - All 20 pages well-filled (no sparse tail; p11 2351/p12 2434/p13 2049 chars), no extra page.
- Tradeoff: tables appear before some summarized prose (e.g., Table4 before HydraFusion/AutoFix/Decider details it summarizes; Table5 before distillation/ECDSA; Table6 before later Earth AI/Deep Review). Prose order unchanged, but table-vs-prose summary order changed from original authorial `details-then-summary` to `preview-then-details`. Still `after an associated portion` and `BEFORE next heading`, but less faithful to original reading order than Alt A. Therefore documented but NOT adopted.
- No barrier blank, no page growth, but early-summary compromise. If future Human prefers 20pp retention, Alt B proves 20pp fix exists; current r21 adopts Alt A for reading fidelity and honest 21pp measurement.

Both alternatives prove inherited `jlreq`+`twocolumn`+`table*` class CAN be fixed inside this unit; no `R21_FLOAT_BOUNDARY_BLOCKED` needed. No font shrink, margin change, filler, or numeric-target styling in either.

## 4. Adopted r21 render (Alt A + display-label fix)

Source: exact `diagnostic-r20/main.tex` → `/tmp/opencode/w42r21build/final/main.tex`:

- Header `% W42 r20 …` → `% W42 r21 …` (same 121B; provenance only; reported).
- +1 `placeins` line, +3 `FloatBarrier` lines (see diff below; total 964→968 lines wc -l).
- Bibliography display only: 7× `[SECONDARY]` → `[二次・参考]` (B63/B64/B66/B67/B68/B70/B71). Publisher/kind/URL/alias/category/ledger untouched. Before→after recorded in `bibliography-display-map-r21.json`. B28/B57 text, all URLs, B74, B90, 90 keys/19 aliases/177 rows unchanged.
- Sizes: r20 94,781B → r21 95,112B (+331B = 4 layout lines + 7 label deltas with UTF-8 growth; header same length). SHA r20 `909e3b87…` → r21 `278a609a…`. Lines 964→968. `preview.sty` byte-identical (`f0492fb6…`).

```diff
-% W42 r20 NONCANONICAL DIAGNOSTIC TeX/PDF — NOT a validated release, NOT a Publication Preview, NOT FOR HUMAN APPROVAL.
+% W42 r21 NONCANONICAL DIAGNOSTIC TeX/PDF — NOT a validated release, NOT a Publication Preview, NOT FOR HUMAN APPROVAL.
 \usepackage{preview}
+\usepackage{placeins} % [r21] flush dbl floats before next chapter
@@ -465,6 +466,7 @@
+\FloatBarrier % [r21] ensure preceding table* printed before next chapter
 \section{安全性と透明性:開示・蒸留・検証アクセス}
@@ -566,6 +568,7 @@
+\FloatBarrier % [r21] ensure preceding table* printed before next chapter
 \section{科学エージェント:ウェットラボ・地球AI・査読}
@@ -672,6 +675,7 @@
+\FloatBarrier % [r21] ensure preceding table* printed before next chapter
 \section{専門・身体性:法務・ロボティクス・視覚}
@@ -904,23 +908,23 @@
-\bibitem[B63]{B63} [SECONDARY] …
+\bibitem[B63]{B63} [二次・参考] …  (×7: B63/B64/B66/B67/B68/B70/B71; publishers/URLs identical)
```

Built in temp clean workspace from r21 TeX + identical r20 style. Deterministic `SOURCE_DATE_EPOCH=1792311600 FORCE_SOURCE_DATE=1 lualatex -interaction=nonstopmode -halt-on-error main.tex` ×3; all three SHA `b8ac6172b6c122b862987030d05c365621744a714496f74d79a48d62a84da7b3` identical → stable. Final `main.pdf` **21 pages, 509,133 bytes**; `main.log` 77,332B/1475 lines, SHA `bcc93bb6…`, 0 overfull/underfull/errors/missing-glyphs/undefined (final run; `placeins.sty` load line only). Fonts HaranoAjiMincho-Regular/Bold, HaranoAjiGothic-Bold, lmroman8/9/10/12, lmmono10, lmsans10-bold. CreationDate/ModDate 2026-10-18 17:20 JST (epoch-pinned).

Archived fresh `execution/diagnostic-r21/`: `main.tex`, `preview.sty`, complete `main.log`, `main.pdf`, `build-manifest-r21.json` (above SHAs/bytes/pages/build metadata; per-page raw `pdftotext` chars), 21 individual PNGs @150dpi (`pages/p-01..p-21.png`) + 3 contact sheets (`contact-sheet-r21-01-p01-07.png` 1,963,040B, `-02-p08-14.png` 1,954,499B, `-03-p15-21.png` 1,648,540B), `review-pages-r21.md`.

Visual QA (ALL 21 PNGs individually opened; see `review-pages-r21.md`):
- cover 3 uninterrupted warnings, unmistakably diagnostic;
- Table4/5/6 each strictly precede next chapter heading in PHYSICAL reading order (p12/p14/p16 tops with headings below on same pages), Tables1/2/3/7 remain within own chapter (p01–p10 PNG-identical to r20; Table7 p17 in-flow with complete Glimpse, no bisection);
- p16→p17→p18 no Table7/Glimpse bisection, no isolated Table7, no cross-chapter float; p18 honest short P7 tail (702 chars) to inherited `\clearpage`, not stamp-only;
- B28 complete on p20, B57 kept together on p21 (same ASPIRE wrap as r20), all 90 Bxx (71 full + 19 `→ [Bxx]（同一資料）`) preserved, B63/64/66/67/68/70/71 now consistent `[二次・参考]`, links not clipped, 7 tables/6注意 boxes in-chapter;
- no bib URL orphans beyond inherited B40 split (same as r20), no machine provenance leak (TeX 0 `alias-of`/`normalization`/`CLAIM_BOUNDARY`; PDF-text block-ID pattern 0 hits; B-count 840 identical to r20 same-method), no last blank/stamp-only page (p21 ends B90, no trailing stamp), no new table-only pages; p11 barrier blank + p18 short tail documented as honest costs, not massive.
- Per-page raw lengths: 480/2495/2668/2353/2552/2431/2731/2674/1787/2526/2011/2227/2187/2231/2665/2413/2064/702/2850/3108/2698; p01–p10 identical to r20; body/bib pagination remeasured (see §5). NOT `VISUAL_AUDIT_BLOCKED`.

## 5. Page counts (remeasured, not assumed)

- r20 measured: 20 = cover1 (p1) + body16 (p2–p17) + bib3 (p18–p20).
- r21 measured: **21 = cover1 (p1) + body17 (p2–p18) + bib3 (p19–p21)**. Diagnostic-only terminal page absent in both; cover 3 warnings intact in both.
- Chapters (rechecked on r21 PNGs + `pdftotext` page+column, overlapping, NOT additive): P1 p2–p4 / P2 p4–p6 / P3 p6–p9 / P4 p9R–p11 (+ Table4 p12 top) / P5 p12–p13 (+ Table5 p14 top) / P6 p14–p15 (+ Table6 p16 top) / P7 p16–p18 (Table7 p17 in-flow, tail p18). Tables counted in hosting chapter. p11 (2011 chars) is P4 only; p12 (2227) Table4+P5; p14 (2231) Table5+P6; p16 (2413) Table6+P7; p18 (702) P7 tail only.
- Effective usable-page occupied area: `UNMEASURED; <= 17 PHYSICAL BODY PAGES` (table/note/heading-inclusive upper bound, no double counting). The withdrawn r16–r18 `15.5–17` estimate is NOT revived. No numeric gap to 26.5 is issued.
- Conditional (labeled, NOT rendered): approved-body 26.5 + cover1 + bib3 = **30.5** vs target28/max30 (exceeds max 0.5). r20 30.5 persists as conditional; r21 actual 21 is NOT 30.5. Option B 17.0 remains proposal-only, NOT observed 17 (coincidental numeric equality explained in brief; planned allocation ≠ physical pages). Architecture 26.5/target28/max30 unchanged. No filler, no r2 assumption.

## 6. Frozen authority re-verification (read-only)

- r18 Reader blob `fc4fd9f2…`, P1–P7 proposal SHAs (`b6e1c7cc…`/`badbbbd0…`/`d81023c1…`/`e8b7aa46…`/`bde64f2c…`/`aedfb8f4…`/`9e8924ea…`), bib-map `44494d98…`, ledger `d7503523…`, dup-matrix `e7025ca6…` unchanged; `editorial-revision-r18/` diff empty (working tree clean except new r21 paths before commit).
- production-state blob `63edc922…` (DRAFT_COMPLETE/approved/pending); checkpoints/approvals/review-index; canonical Draft/Synthesis v10.0; Evidence/Views/Materiality/Selection/Architecture; r11–r20 execution bytes; main + Frozen Core. All untouched.
- Only new edition-local: `typeset-repair-r21/`, `diagnostic-r21/`, one session, index append. No formal Reader/Publication, no architecture amendment.

## 7. Residuals

- p11 right-column bottom blank (FloatBarrier cost, honest, not massive).
- p18 short P7 tail (702 chars, left-column only, right empty) to inherited `\clearpage` before bib (honest expansion tail, not padding).
- B57 intra-entry ASPI/RE wrap (kept together, readable; same as r20/r19).
- Effective area UNMEASURED (no fake metric).
- 83/90 HTTP UNVERIFIED carried from r17 (no new reachability claims).
- Contact-sheet scale 0.4 thumbs (compact; full PNGs authoritative).
- Manifest per-page chars are `pdftotext` raw (incl. newlines); r20 correspondence proven via identical-method recomputation (r20 p01–p10 raw == r21 p01–p10), not via cross-method equality.
- Alt B early-summary tradeoff documented (tables before some details) as rejected reason; Alt A preserves `details-then-summary`.

Stop: `SOL_W42_R21_FLOAT_BOUNDARY_INDEPENDENT_AUDIT_READY / NONCANONICAL` (cover intact, all three F-08 visually solved without table-only/massive regression, all pages QA, brief reflects true pagination; no candidate, no Gate action).
