# J-GAS W42 — Muse r23 SYSTEMIC full-width-table float/sentence repair

Date: 2026-10-18 JST
Status: `SOL_EXECUTION_AUTHORITY / R22_DIRECT_VISUAL_REQUEST_CHANGES / R23_GLOBAL_LAYOUT_STRATEGY / NONCANONICAL_ONLY`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W42-v2-work`

## 0. Exact Git guard / protected scope

Sol dispatch provides NEW Exact Starting Remote HEAD/Tree from the commit containing this contract. Before any write, read remote W42 ref, commit, root Tree, reviewed main HEAD/Tree (`c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / `801de813319f08777ab1581a5e8875fc1ac5df19`), frozen Core HEAD/Tree (`774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`), and r22 baseline HEAD/Tree (`d0cf7cb82d744260f630a5f9043fecc80d4b139f` / `f21e36ec710dc1a717060804961a2ede25043a7f`). Missing or mismatched evidence => ZERO WRITES/STOP with actual vs expected. Recheck remote lease immediately before push; normal commit and non-force FF push only. No new/fallback/repair/review branches, no reset, force, rebase or history rewrite.

Frozen: shared Core v2/main; W42 canonical Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/Architecture, approved Human Architecture r1, canonical Draft v10.0/Synthesis, production-state.json, all Human Gates, checkpoints/review-index, ALL historical execution bytes r11–r22. New r23 outputs ONLY `sources/2026-W42/execution/typeset-repair-r23/`, `execution/diagnostic-r23/`, one new `execution/sessions/muse-w42-r23-20261018.md` and strictly truthful append-only `execution/index.md`. NO formal reader, stage transition, Publication/Freeze/Release/Human Gate.

## 1. Mandatory read-first, source of truth, accepted positives

Read the new Sol r22 direct-visual `execution/reviews/sol-w42-r22-direct-visual-preflight-REQUEST_CHANGES-20261018.md` BEFORE trusting r22 Worker PASS. Read original r22 instruction, source invariance, C2 TeX/PDF/21 page PNGs/manifest, candidate-B TeX/PDF/20 page PNGs, r21 and prior float failures. The exact r18 Reader `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json`, git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, governs all 7 chapters/28 selections/157 blocks/136 paragraphs/25,015 paragraph characters/7 tables/7 notes; 90 B keys,19 aliases,177 citation ledger lines. 150 non-TABLE Reader blocks, every TABLE cell/caption/citation, order/claims/quotes/scope, and 7 chapter memberships must be preserved byte-exact. No new research, prose editing, filler or content deletion.

r22 C2 genuinely repairs Table7/ASPIRE p16→17, and Tables4/5 currently precede next chapter headings without breaking previous paragraphs. Do not regress them. Reader page-count goal is not a quality gate: Human selected Option B as *editorial* preference, 17.0 planned body pages, Sol suggested provisional issue target 21/max23; NO formal Human Architecture r2/Gate approval, no page padding.

## 2. r22 is NOT a print PASS: exhaustive actionable known failures

Current C2 21pp has four FULL-WIDTH top-of-page `table*` inserts between adjacent pieces of uncompleted narrative sentence, and a predominantly empty final P7 page:

- F22-01 Table1: p03 right end `失敗の記録と立直` → p04 top Table1 → p04 below `しの手順が残ることが…`.
- F22-02 Table2: p05 right tail `16種ベンチを温度条件つきで示す流儀は分母の開` → p06 top Table2 → printed continuation below table begins in mid-paragraph `も、温度・ベンチ名とセットで読む…`; reconstruct entire source-contiguous phrase from main.tex, map both-column physical order. Do NOT treat this fragment as a complete sentence.
- F22-03 Table3: p08 right end `一つのエンドポ` → p09 top Table3 → p09 below `イントではほぼ基盤と同等の…`.
- F22-04 Table6: p15 right end `VERID較正の意味を確認する。染料と水によ` → p16 top Table6 → p16 below `る検証、フィードバックで5倍超…`.
- F22-05 p18 P7 final technical-body page: only 702 raw chars, upper-left partial column; right column totally empty, most of the page blank. Also audit p11 barrier and p16 needspace whitespace. This is visibly poor print fill, not automatically PASS merely because contents are genuine.

Fixing one can move another. Therefore **NO single-spot needspace-only patch and no trusting a 0-warning log or per-page character totals as proof**. A final candidate with ANY sentence/paragraph bisected by ANY table, ANY table beyond its own chapter boundary, a table-only page, or an enormous avoidable terminal article page MUST FAIL.

## 3. r23 task: replace ad-hoc local float repairs with global layout strategy

First reproduce r22 C2 and rejected B as controls. Investigate TeX column/page-build semantics and why every table1/2/3/6 jumped ahead of an incomplete paragraph despite Worker QA. Identify invariant *source* position vs *physical* page position and distinguish pN left→right column from pN→pN+1. Diagnose, document and prove actual source-contiguous text for all four failures (especially Table2, where snippet order is nontrivial).

Render and compare at least TWO genuinely distinct global print-layout strategies, not just copies of C2 with different `needspace` amounts. Candidate approaches to evaluate, subject to verified engine/package semantics and preserving typography: (a) paragraph-boundary-safe deterministic placement of full-width comparisons inside their own chapters rather than asynchronous `table*` drift; (b) page/column boundary-controlled nonfloating full-width blocks or chapter-local restructuring of float anchors if supported by the existing jlreq/TeX toolchain; (c) selective anchoring and float scheduling together with explicit paragraph-completion checks. You may reject a technique with an actual rendered failure explanation. Hard breaks are acceptable ONLY if justified by better overall pages, no gigantic blank spaces or extra orphan leaves. No changes to fonts, margins, line spacing, column ratio or Reader content purely to reach 20/21/22 pages. Do not adopt a package with unvalidated two-column behavior. If a clean 20-page layout is real, it is acceptable; equally a clean 21/22/23 within the editorial plan is acceptable without padding.

Re-examine whether the P7 702-char last page can be eliminated through legitimate float scheduling/paragraph-boundary choices without forcing bisections. Show **actual** before/after page images with full page occupancy narrative, not unsupported "unavoidable" assertions. A text-only or one-column fallback should NOT silently replace the publication design.

## 4. Physical all-tables acceptance proof: mandatory independent-auditable ledger

For EACH Table 1..7:
1. Identify the chapter, precise PDF page/top position, the last 1–2 complete source sentences/paragraphs logically preceding the table, and the first 1–2 logically following it; include exact endings/startings in TeX and the printed words on p-1 vs page of table (left and right column where applicable).
2. Prove no paragraph / sentence / **word** was split by inserting the table. Do not confuse TeX source order with actual physical ordering. Cross-check source passage against page image and, where possible, positional PDF text extraction/reading-order mapping.
3. Prove the table is in its hosting chapter AFTER legitimate introductory context and STRICTLY BEFORE the next chapter heading in physical print order.
4. Open ALL page PNGs individually; inspect page/column transitions that have no table too, all section headings, notes, URL wraps and bibliography. Confirm p01 diagnostic three-line stamp and B28/B57/B74/B90, 71 full+19 aliases/90 bibliography items, 7x secondary-display fixes, 177-ledger map, zero printed machine IDs. Preserve Argon random world, Maia24/96/750GB/s, Earth dependent negatives, MTP accepted-token length, wet-lab 131/311 vs 8 clones, LFM legal-entity licensing, ASPIRE real robot caveats.
5. An unfilled previous-page column and a next-page float are NOT proof of paragraph-boundary safety: explicitly quote the previous printed trailing glyphs and next printed leading glyphs and verify whether the original sentence finished.

An independent reviewer must be able to evaluate alternatives WITHOUT rerunning builds. Archive actual TeX/sty/PDF/full engine logs/build-manifests/SHA256, full set of individual 1-based PNGs and contact sheets for every serious candidate (at minimum the selected plus best rejected), plus comparative annotated images for p03→04, p05→06, p08→09, p15→16, p16→17, and the prior p18 sparse tail.

## 5. Deliverables, verification, end state

Write:
- `typeset-repair-r23/global-float-root-cause-and-candidate-comparison-r23.md` with why r22 false-PASS happened, comparison alternatives/actual bisection excerpts, table-by-table ledger.
- `typeset-repair-r23/reader-and-source-invariance-r23.md` with exact byte checks against r18 Reader plus 90/19/177, file/change diff, style invariants.
- `typeset-repair-r23/option-b-pageplan-and-physical-fill-r23.PROPOSED.md` with actual cover/body/bib pages; measured occupied area if honestly measurable, otherwise `UNMEASURED`; 21/23 stays Sol tentative and 26.5/28/30 canonical unchanged.
- `diagnostic-r23/` genuinely built and archived selected and comparison proofs/manifest, full PNGs and detailed QA.
- `execution/sessions/muse-w42-r23-20261018.md` + truthful index append.

All changes edition-local. Normal commit/non-force push, final remote SHA/Tree and proper read-back. **Terminal only if** zero sentence/word/paragraph bisections across ALL 7 tables, zero chapter crossings, no avoidable large terminal blank and old regression gates visibly PASS: `SOL_W42_R23_INDEPENDENT_PRINT_AUDIT_READY / NONCANONICAL`. Otherwise `R23_SYSTEMIC_LAYOUT_BLOCKED` with actual rendered evidence. Worker self-PASS is never Sol or independent reviewer certification. No Human Gate/Reader/Publication/Freeze/Release.
