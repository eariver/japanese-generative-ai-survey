# J-GAS W42 Muse r25 — pagination-safe two-column wide-table system, bounded feasibility

Date: 2026-10-18 JST
Status: `SOL_EXECUTION_AUTHORITY / R24_LAYOUT_QUALITY_BLOCKED / R25_TWO_TRACK_TABLE_PAGE_SAFETY / NONCANONICAL_ONLY`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W42-v2-work`

## 0. Exact Git guard, protected authority, no formal gate

Sol shall supply an Exact Starting Remote HEAD and Expected Starting Tree that match the commit containing this contract. Before any writes read remote branch, commit and root tree; also verify reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/tree `801de813319f08777ab1581a5e8875fc1ac5df19`; frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`; r24 baseline HEAD `7e0b0b8eebb778225ef43eabab974260841d1257`/tree `34b32ea4aa2ef3472be39d65ceebf362873d9d2c`. Any mismatch/missing evidence => ZERO WRITES STOP with actual/expected. Before push recheck exact remote lease. Existing branch, normal commit(s), non-force push only; no new/fallback/repair/review branch, no reset/rebase/force/history rewrite.

Immutable: all Core/shared main roots and W42 canonical Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/Architecture, Human Architecture r1 approval and all Gates, Draft v10.0/Synthesis, Production State, checkpoints, r18 Reader master exact blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, and ALL prior execution history r11–r24. Writing allowed ONLY new `sources/2026-W42/execution/typeset-repair-r25/`, `execution/diagnostic-r25/`, one session `execution/sessions/muse-w42-r25-20261018.md`, truthful append-only `execution/index.md`. NO formal Reader, canonical Architecture revision, State/Gate, Publication/Freeze/Release.

Reader authority is 7 chapters,28 selections,136 paragraphs/25,015 paragraph chars,7 tables/7 notes/7 headings/157 reader blocks,90 B keys/19 aliases/177 ledger lines. EVERY reader text/claim/source mapping, all table captions' visible words, table cells/row order/cites, notes, chapter ordering remain byte-exact. Permitted print-only wrapper restructuring needed for a two-column layout; no shortening, padding, changing column width, fonts, margins or line spacing for target-page quotas. Human Option B editorial preference is not Gate approval; Sol tentative issue21/max23 is a planning suggestion, NOT a hard success criterion.

## 1. Read first: why r24 did not pass

Read Sol `execution/reviews/sol-w42-r24-direct-visual-disposition-REQUEST_CHANGES-20261018.md` FIRST, then r24 session, full `diagnostic-r24/` 21-page PNG/PDF/TeX/log, sample, invariance, r23/r22 controls, and r18 Reader/master. Understand explicitly:
- r24 `cuted` strip fixed the four old narrative-splitting double floats (Tables1/2/3/6).
- New F24-01 Table4 on PDF p11 is truncated into FOOTER; Decider v1.2 row missing, 93pt overfull.
- NEW F24-02 TABLE3 caption at *bottom* of p08, ALL rows begin p09. Previous Worker QA failed to report caption/body separation; treat as hard FAIL.
- F24-03 huge sparse terminal body p18: 508 raw characters upper-left, right empty.
- F24-04 `cuted` output warnings correlate with real visual faults. Package compilation exit 0 != print PASS.

Before building propose a page/column/element geometry acceptance model: each Table1..7 must have caption AND its entire row grid visible on SAME page, between safe top/bottom print bounds, no text/footer collision, no orphaned caption/row, no unbounded box, no physical sentence/word bisection by an intervening wide element, no chapter crossing, and manageable remaining body-page occupancy. Enforce against true rendered images AND text bounding boxes where available, not pdftotext counts alone.

## 2. Phase A: two genuinely distinct layout-system prototypes, fast stop if not feasible

Build in isolated local workspaces with current jlreq/LuaLaTeX/LuaTeX-ja, same source prose/table bytes and original font/page geometry. For each method, first make a representative sample containing genuine W42 Table3 (long 6-row comparison) and Table4 (including the Decider row), their surrounding real paragraphs, and a P4/P5 boundary. The sample should be stressed at near-bottom insertion, where r24 failed. Validate footers, page numbers, captions and links, not merely TeX exit status.

Track A — measured, page-aware in-flow `cuted strip`: check documentation/output-routine semantics, determine whether a complete `strip` with caption+tabularx can be kept atomic, compute/estimate actual element height with safety reserve BEFORE placement, shift placement to a paragraph boundary with adequate space if possible. `needspace` alone without proof of complete table geometry is NOT an acceptable answer; if the output routine still splits caption from grid, reject Track A. No scaling, shrinking row text, deleting Decider row or squeezing margins.

Track B — another **independent layout architecture**, not a different `strip` argument: evaluate `multicol`/`multicols*` to keep body as TWO columns in segments, put full-width NONFLOATING table between segments with a safe paragraph boundary. Its output routine and balancing are different, so establish compatibility with jlreq, luatexja, bibliography, tcolorbox and hyperref before using. Preserve same font/column widths/gutter/page geometry. Never use a one-column body fallback disguised as a two-column magazine; `multicols*` can be tested for reduced forced balancing but MUST be visually verified for sparse/blank leaves. CTAN https://ctan.org/pkg/multicol (documented switch without forced `\\clearpage`), https://www.ctan.org/pkg/cuted (strip is distinct). Other genuinely independent method only with rationale and real sample proof.

For each Phase A approach, record engine/packages/version, minimal source (real table bytes, no invented sample cells), log, PDF SHA/pages and full PNGs. Failure of one does NOT automatically abort the other; if both fail, terminal `R25_PAGINATION_SYSTEM_FEASIBILITY_BLOCKED`, archive evidence and DO NOT proceed to full W42.

## 3. Phase B: full W42 only after one Phase A candidate visibly PASSes

Implement all 7 W42 wide tables using the sample-proven method. No hybrid async `table*` that reintroduces paragraph bisection. Preserve exact source content; wrapper-only changes must map old-to-new visible captions/citations and table rows 1:1. Build multiple deterministic passes. Compare C2 r22, r23 SA/SB, and r24 STRIP; do not target an arbitrary page count. If both A/B sampled viable, render both full issue if manageable and select by objective QA, not self preference.

Mandatory all-7 physical table ledger: for each Table N write source chapter, actual p/position/columns, last physical sentence/words BEFORE the table and first AFTER, whether intact paragraph, caption page and row grid page count, all rows/cell/cites visible, no footer overlap, strict placement before next chapter heading, no blank table-only pages. Verify Table1 `立直し`, Table2 `分母の開示`, Table3 `エンドポイント`, Table6 `による検証`, Table7 ASPIRE; preserve Table4/5 boundaries and Decider row. All captions MUST remain attached to their rows; row count/cell text equality must be checked against source AND PDF, not just source hashes.

Inspect EACH individual PDF page/PNG, not merely contact sheets; list precise page regions for all seven tables and every odd whitespace location. Verify p18 problem objectively: any short end-of-article page comparable to r24 p18 508 characters left-only and entire right blank is a quality FAIL unless a print-design alternative can justify it to Sol with objective visual comparisons. Do not stuff text or manipulate font/margins to match 21/23. Validate whole magazine: cover three NONCANONICAL warning lines, 7 chapters/28 topics/7 notes, 90 B bibliography items (71 full+19 aliases), 177 ledger source mapping, 7 printed secondary labels, B28/B57/B74/B90 URLs and B90 terminus, no printed internal IDs, no missing glyphs/hyperlinks, no clipping of citations. Preserve known technical regressions (Argon random world, Maia 24/96/750GB/s, Earth negative Pro vs positive Flash, native MTP accepted-token LENGTH not rate, wetlab 131/311 vs 8 clone cohort, LFM legal entity/license, ASPIRE robot results + limits).

If new layout provides complete readable 20/21/22/23pp, any is acceptable subject to real page plan and editorial quality; do not force any count. Effective occupied area report measured method or `UNMEASURED`, no invented decimal pages.

## 4. Proof artifacts, governance and terminal

All edition-local new files:
- `typeset-repair-r25/phaseA-two-system-geometry-and-interoperability-r25.md`, versioned code evidence, explicit warning/clip/caption tests.
- `typeset-repair-r25/global-seven-table-source-to-physical-ledger-r25.md` with ALL seven before/after quotes + bounding observations and candidate comparison.
- `typeset-repair-r25/reader-content-and-bib-invariance-r25.md`, exact Reader master/caption/cell/source/quote/hash diff.
- `typeset-repair-r25/human-option-b-pageplan-r25.PROPOSED.md`, only physical measured counts, NO architecture r2/Gate.
- `diagnostic-r25/` genuine sample candidate PDF/log/TeX and ALL page PNGs for both approaches, full candidate PDF/TeX/log/manifest/all page PNGs if viable, contact sheets and reviewer-friendly per-page index.
- `sessions/muse-w42-r25-20261018.md`, truthful index append; clean normal commit, non-force push and final read-back.

Allowed terminal:
- `SOL_W42_R25_INDEPENDENT_PRINT_AUDIT_READY / NONCANONICAL` ONLY if ALL seven tables complete and same-page, all narrative/chapters/pages/URLs/content readable, and no giant avoidable terminal void; self-reported ready is still subject to Sol and separate independent auditor.
- `R25_PAGINATION_SYSTEM_FEASIBILITY_BLOCKED` if both Phase A alternatives fail real table stress tests.
- `R25_LAYOUT_QUALITY_BLOCKED` if a sample works but full W42 proof still fails.

Never claim official Publication, Human Gate, Architecture revision, Freeze/Release on r25. Stop with honest blocker/proof if no suitable result.
