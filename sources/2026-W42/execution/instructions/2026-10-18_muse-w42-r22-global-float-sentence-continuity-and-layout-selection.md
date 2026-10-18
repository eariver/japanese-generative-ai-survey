# J-GAS W42 Muse r22 — holistic float-flow repair and independently comparable print alternatives

Date: 2026-10-18 JST
Status: `SOL_EXECUTION_AUTHORITY / R21_DIRECT_VISUAL_PRINT_BLOCKER / R22_GLOBAL_TABLE_SENTENCE_ORDER / NONCANONICAL_ONLY`
Repository: `eariver/japanese-generative-ai-survey`
Branch: existing ONLY `weekly/2026-W42-v2-work`

## 0. Fail-closed exact Git guard

Sol dispatch supplies Exact Starting Remote HEAD + Expected Starting Tree for the commit containing this contract. Before any write, read remote ref/commit/root Tree read-only and compare full SHAs exactly; check reviewed main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`, Frozen Core HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`, and r21 baseline HEAD/Tree `84d9093da8b5bc985e6a834d356697a369211d2a`/`4789c036afd20321298f8155be2f16dce16c3ae4`. Any mismatch/missing proof => **ZERO WRITES, STOP and actual/expected**. Before push recheck remote lease. No new/fallback/repair/review branches, force, rebase, reset or history rewrite. Normal commit + non-force push existing branch only.

Protected read-only: ALL shared Core/main roots; W42 canonical Discovery/Evidence/Selection/Architecture, Human r1 gate/approval, canonical Draft v10.0/Synthesis, `production-state.json`, checkpoints/review index; ALL r11–r21 historical execution bytes. New content may be placed ONLY in NEW `sources/2026-W42/execution/typeset-repair-r22/`, `execution/diagnostic-r22/`, one session in `execution/sessions/`, truthful append-only `execution/index.md`. No formal Stage/Reader/Publication/Freeze/Release/Human Gate.

## 1. Authority, exact source, previous result

Read first `execution/reviews/sol-w42-r21-direct-visual-preflight-disposition-20261018.md` and this r22 contract; original r20 independent report was user-delivered outside GitHub, raw audit file not committed.

Read r21 Muse session, layout-comparison report, TeX/style/full log/manifest/PDF, all 21 individual PNGs, current bibliography display-map/PROPOSED page-plan; r20 proof and r20/r19 controls. Source master remains **exact** r18 `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` and 7 r18 per-chapter Draft proposals + r18 source authority (90 B keys, 19 aliases, 177 citation ledger rows). Reader `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, 7 chapters/28 selection, 136 paragraphs/25,015 chars/7 tables/7 notes/7 headings/157 reader blocks. All technical prose/quote/order/scope must be byte-exact; NO newly researched material, editor padding or narration. Only TeX float placement/print labels/diagnostic page surfaces may change.

Current r21 21pp Alt A barrier solution fixed F-08 Table4/5/6 AFTER next heading, **but** a new **S21-01 printed-sentence bisection** persists: at r21 p16 right ASPIRE sentence ends `…80課題で`, then p17 TOP full-width Table7, then below table continuation `99%、卓上片づけの実機…`. Repaired Glimpse block is not proof ASPIRE is continuous. **Hard FAIL**.

Also r21 **S21-02**: p18 702 raw characters in small left-column tail and huge whitespace, p11 right-column lower blank, creating poor space utilization. This is NOT a legitimate reason to add filler or shrink type. One alternative already reportedly rendered at r21: `Alt B` early relocation of Tables4/5/6 within their chapters, gives 20pp and reportedly fuller pages, but no archived candidate PDF/PNGs and table precedes some detail paragraphs. Do not assume it PASS until independently reproducible proof exists.

## 2. Holistic float/paragraph/heading constraints

This time test **every** Table 1..7, not only prior failing numbered subset, and EVERY chapter P1..P7 boundary. The actual print must simultaneously meet:
1. Each Table N is physically after relevant introductory context *within its own chapter* and strictly **BEFORE the next chapter heading** in page/column reading order.
2. A full-width `table*` at the top of a new page must **NOT** interpose between the first and second part of a single narrative **paragraph or sentence** carried across the previous page/column (not just Glimpse; include ASPIRE, P4/P5/P6 bridging prose, all tables). Check the text boundary immediately BEFORE each table top and immediately AFTER it; if a paragraph is carried from preceding page, moving the table ahead of that paragraph or ensuring the paragraph completes before the page turn are acceptable, but don't change Reader bytes.
3. No table-only page, no last mostly empty technical-body page consisting solely of a short closing fragment, no large avoidable voids caused by manual barriers; maintain readable natural chapter transitions and reasonable whitespace. Compare alternatives explicitly; do not achieve quota by font/margin/line-spacing tricks or filler.
4. No regression to Table7/Glimpse old failure, B28 page-top URL orphan, B57 URL readability, B74 clean URL, 90 bibliography labels/71 full+19 aliases, B90 terminal and intact 3-line NONCANONICAL cover warning. Keep `[二次・参考]` printed label where r21 fixed it, no machine provenance leaked. All 7 TABLE and 7 NOTE objects remain in the same chapters and all required citations remain mapped.

**Mandatory genuine candidate comparison:**
- **Candidate A (r21 FloatBarrier)** as baseline: inspect p11/p12/p13/p14/p15/p16/p17/p18, report ASPIRE bisection and p18 sparseness; not a PASS candidate.
- **Candidate B (r21 early table relocation)**: reproduce a complete local build from r18 Reader, preserve table bytes/captions/cites, reconstruct r21 documented moves: Table4 after P4 Scion-API, Table5 after P5 subject separation, Table6 after P6 tool contribution. Freshly run and **archive independently viewable Candidate-B proof** `execution/diagnostic-r22/candidates/B/` with full PDF/log/manifest and ALL page PNGs or make a reasoned smaller comparison archive with at least page-by-page, every table, p15–end and page transition PNGs and raw hashes. Prefer full proof if repo file size permits. Evaluate all 7 tables, all paragraph-over-page transitions including ASPIRE, and bibliography.
- **Candidate C** if A and B are imperfect: adjust Table7 placement or add appropriate float/paragraph boundary controls without altering Reader block content. May use `placeins`, logical `\needspace` before ASPIRE paragraph, a safe paragraph-boundary placement of Table7, or corrected table placements. Fully render. Do not insert hard page breaks unless they actually improve reader flow and avoid excessive whitespace. Control physical order from real pages, not TeX source only.
- Choose the best demonstrably **publication-readable** combination across all 7 tables and full paragraphs; do not reject B simply because it has a preview-before-details tradeoff (valid article design if the opening context is supplied), and do not favor A merely because 21pp equals Sol's **tentative** issue target.

A current exact 20-page proof and 21-page proof are both potentially acceptable under Human's non-Gate Option B; actual physical pagination should determine the plan's feasibility.

## 3. Independent-verifiable physical and text checks

Compile each candidate in isolated local workspace (not canonical), record TeX/preview style build command/version and full engine log, SHA256/PDF pages/bytes and exact Reader-master hash. Archive selected result in `execution/diagnostic-r22/`: `main.tex`, `preview.sty`, `main.pdf`, complete `main.log`, build manifest with PDF SHA and true page count, all 1-based `pages/p-XX.png`, reasonably legible split contact sheets and detailed per-page visual index. Also keep exact source/diff/manifest for rejected alternative(s), including the actual images to substantiate claimed improvement.

**Visual QA must open ALL pages**. For each table, list PDF page, position, text ending before table on previous page or column, first text after table, whether carried paragraph got split; include screenshots/side-by-side before/after for Table4/5/6 and Table7/ASPIRE. For all chapter headings list actual page+column and preceding table position. Explicitly count page-body occupied distribution, empty/low-fill pages and bibliography terminations. If effective occupied page area cannot be accurately measured, report `UNMEASURED; <= physical-body pages` (no invented 15.5–17). Distinguish cover, body physical pages, references and diagnostic-only markings.

Run exact print-text equivalence checks: all 150 non-TABLE r18 blocks in print unchanged, all 7 table texts/citations unchanged, zero internal block IDs/editor notes; verify body sequence via PDF extraction and actual visual page breaks (text extraction by itself is NOT a layout PASS). URL parsing Bxx list and aliases do not change. Preserve independent prior regressions: Argon random world, Maia 24 trays/96 accelerators one pod/750 GB/s, Earth model-dependent negative result, NVIDIA native MTP mean acceptance length not rate, wetlab 131/311 separate from later eight clones, LFM license legal entity, ASPIRE publisher real robot results.

Any candidate with a real sentence bisection by a table, a table beyond its own next chapter heading, or an enormous avoidable sparse terminal article page is **NOT eligible** for terminal PASS, even if logs have 0 errors. If you cannot solve all simultaneously with supported layout changes, explicitly `R22_HOLISTIC_LAYOUT_BLOCKED` with candidate images/proofs, not a self PASS.

## 4. Human Option B page-plan PROPOSED, no canonical revision

Human chose editorial **Option B**: retain 7 chapters/28 topics and technical findings, provisional P1 2.5/P2 2.5/P3 3/P4 2.5/P5 2/P6 2.5/P7 2 = **17.0 planned body pages**. Sol proposed (NOT yet specifically Human-approved) issue target21/max23. Formal Architecture remains body26.5, issue target28/max30 and Human Architecture r1 approved; State DRAFT_COMPLETE/Publication pending. Do not change them.

After selecting actual r22 proof, write `typeset-repair-r22/human-architecture-pageplan-decision-brief-r22.PROPOSED.md` with new measured total, cover, body physical and bibliography, chapter boundaries, effective area `UNMEASURED` unless measured, and conditional arithmetic `26.5 + actual nonbody pages` labeled not actual print. If Candidate B yields 20pp, **20 may be valid**, even if Sol's tentative target=21; no padding. If 21/22 with good paragraph flow and no sparse tail, equally valid. Keep issue target21/max23 only as Sol's provisional recommendation for future explicit Human consultation/confirmation, not an r21/r22 success criterion. Reassess the recommendation against actual results; show tradeoffs.

Any formal amendment of approved Architecture, Human Gate, canonical Draft, State or Core commands needs distinct read-only governance preflight + explicit Human authority; no such writes in r22.

## 5. Outputs, commit and terminal

Deliver:
- `typeset-repair-r22/global-table-and-paragraph-flow-audit-r22.md` with exhaustive ALL-7-table page+column+paragraph boundary results, A/B/C comparison, both residuals S21-01/S21-02, and objective reason for choice.
- `typeset-repair-r22/reader-and-source-hash-invariance-r22.md` with original SHA/blob, verbatim-body/table equality, new TeX diff, font/spacing invariants, 90/19/177.
- `typeset-repair-r22/human-architecture-pageplan-decision-brief-r22.PROPOSED.md` reflecting physical actual and Option B as non-Gate.
- One selected noncanonical `diagnostic-r22` PDF/TeX/log/manifest/all PNGs/contact sheets with true all-page QA; independent-viewable candidate B proof/diff as above.
- Session `execution/sessions/muse-w42-r22-20261018.md` and truthful append-only `execution/index.md`.

Protect all files outside the new edition-local paths and index append; preserve r11–r21 history, Core/main/canonical/State/Gates. Before write and push enforce exact Git identity/lease. Normal FF commits, no new branch. Final remote SHA/Tree+file list+all important hash read-back.

Terminal `SOL_W42_R22_HOLISTIC_PRINT_AUDIT_READY / NONCANONICAL` **ONLY** if all 7 table placements, sentence continuity, reasonable physical page fill and old regressions visibly PASS. Otherwise `R22_HOLISTIC_LAYOUT_BLOCKED` with proof and no fabricated acceptance. No formal Reader/Publication/Freeze/Release/Human Gate. Sol will request focused independent layout comparison audit before any human **Gate** conversation.
