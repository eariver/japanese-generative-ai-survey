# J-GAS W42 r21 — Sol direct-visual editorial preflight / r22 routing

Date: 2026-10-18 JST
Authority: `SOL_DIRECT_VISUAL_PREFLIGHT / R21_COMPLETED / R21_PRINT_NOT_APPROVED / R22_LAYOUT_ONLY`
This is an editor's direct GitHub-read/PNG examination, NOT an external independent audit or a Human Gate approval.

## 1. Exact examined identity and preserved authority

Repo `eariver/japanese-generative-ai-survey`, branch `weekly/2026-W42-v2-work`.
r21 HEAD `84d9093da8b5bc985e6a834d356697a369211d2a`, root Git Data Tree `4789c036afd20321298f8155be2f16dce16c3ae4`; parent Sol Option B dispatch `78e6275e477d93756d972cf004ee206716c400a4`. One normal commit, 35 changed files, edition-local `sources/2026-W42/execution/` only.
main remains `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, frozen Core `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20`; canonical `production-state.json` blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb` = `DRAFT_COMPLETE`, Human Architecture r1 `approved`, Publication `pending`. The accepted Architecture's 26.5 body/28 target/30 max is unchanged, as are r18 Reader bytes, canonical Draft, Evidence/Selection and Gate records.

Muse r21 result: new NONCANONICAL diagnostic PDF **21 pages**, **509,133 bytes**, reported SHA256 `b8ac6172b6c122b862987030d05c365621744a714496f74d79a48d62a84da7b3`. Full LuaLaTeX log reports the same page count/bytes and 0 overfull/underfull/missing-glyph/LaTeX error/warning. Sol has not independently computed full PDF SHA256. Muse source map r18 Reader blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`: 7 chapters,28 selected,136 paragraphs/25015 paragraph chars,7 tables/7 notes/7 headings,157 blocks, 90 B keys,19 aliases,177 citation ledger rows. Sol directly fetched r21 master and confirmed Reader SHA, TeX 7 tables and bibliography display 71 full/19 alias.

## 2. r21 progress — visually verified

Sol fetched and **opened actual fixed-commit PNGs p11–p18**:
- p12 Table 4 (P4) is ABOVE the P5 heading — F-08 #1 corrected.
- p14 Table 5 (P5) is ABOVE the P6 heading — F-08 #2 corrected.
- p16 Table 6 (P6) is ABOVE the P7 heading — F-08 #3 corrected.
- B63/B64/B66/B67/B68/B70/B71 secondary classifications now use `[二次・参考]`, not `[SECONDARY]` (TeX text/bibliography-display map confirms).
- r21 actual physical 21=cover1+body17 (p2–p18)+bib3; effective occupied body area `UNMEASURED <= 17`. The Human **editorial** preference Option B (7 chapters/28 selected/17.0 body allocation) and Sol **tentative**, not Human-approved, full issue target21/max23 are recorded in PROPOSED brief. Coincidental r21 21 physical pages does not constitute Architecture revision or publication approval.

## 3. NEW PRINT BLOCKER — Table 7 bisects ASPIRE sentence

**S21-01 / HIGH / PDF p16→p17 visual**: The r21 correction for Tables 4–6 caused an inherited/new reflow hazard at Table 7. At bottom of r21 p16 **right column**, P7 ASPIRE text ends mid-sentence:
`… v1.0 告知では 80 課題で`.
r21 p17 begins a FULL-WIDTH `表 7 比較表：専門・身体の三件` and only **below** that table the ASPIRE paragraph continues:
`99%、卓上片づけの実機（Opus 4.6 模擬・GPT-5.5 実機）…`.
The table therefore cuts into one sentence, even though **Glimpse's** later paragraph itself is no longer bisected. r21 Muse's claim `Table7/Glimpse unbroken; all-page PASS` misses the *ASPIRE* paragraph. This is a concrete physical reader-flow FAIL; no reasonable interpretation of zero TeX warnings can fix it.

**S21-02 / MAJOR LAYOUT QUALITY / p18 sparse tail**: p18 contains just **702 pdftotext raw characters**, all at upper left in a single partially filled column (P7 closing only); the right column and much of the page remain completely empty before a `\\clearpage` for the bibliography. This sparse tail is not a stamp-only page and reflects an honest FloatBarrier layout cost, but **still requires real editorial quality adjudication**; describing it `not massive` without inspecting occupied area is unconvincing. Together with blank lower-right p11, r21 adopted Alt A (barriers) is not yet a print-quality PASS merely because 21 equals a tentative target.

## 4. Genuine alternative, according to Muse's documented trials

r21 `typeset-repair-r21/float-boundary-repair-and-layout-comparison-r21.md` reports **Alt B**: move each Table4/5/6 earlier within its own chapter; it rendered 20pp, corrected all F-08 cross-chapter placements and had denser usable pages, but the tables precede some narrative details. This is a legitimate editorial tradeoff rather than an automatic rejection. **Alt B proof is not archived in GitHub** at fixed r21 HEAD; cannot be independently visually assessed from report alone. An alternative that preserves all source bytes, passes ALL sentence-continuity/float-order tests, and avoids huge blank partial-page is preferred over attaining any exact numerical target.

## 5. Sol ruling

r21 bounded Muse execution COMPLETE and protected state PRESERVED; **r21 PDF editorial approval WITHHELD**. Do not call formal Reader/Publication/Freeze/Release or Human Gate. Do not request Human reapproval solely from this unqualified print proof. Human's Option B editorial preference REMAINS VALID without modification, but actual Gate governance remains a separate future authorization and workflow.

Delegate one more **systematic** r22 print-only unit, NOT piecemeal single-float patch:
- compare the two layout strategies and consider an improved third, including Table7 location/ASPIRE paragraph continuity, all chapter headings and all 7 tables;
- commit genuinely rendered candidate proofs (or at least all actual PNGs/manifest for the relevant alternatives) so an external auditor can compare;
- require all 7 tables not crossing chapter boundaries AND not inserted between two halves of a **single** paragraph/sentence at a page break, all individual page openings and no giant sparse terminal body page, plus no bibliography/orphan regressions;
- hold r18 Reader and all evidence/canonical files byte-identical; no font/margin padding;
- reissue NONCANONICAL PDF plus Option B plan brief based on measured outcome, never assume 20 or 21 pages.

Next bounded contract: `sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r22-global-float-sentence-continuity-and-layout-selection.md`. An independent focused print comparison audit should follow the r22 build before any formal publication or canonical revision.