# J-GAS W42 Muse r18 — bounded Reader-surface decontamination and Human page-plan arithmetic correction

Date: 2026-10-18 JST
Authority `SOL_EXECUTION_AUTHORITY / R17_EDITORIAL_PREFLIGHT_S17_01_S17_04 / R18_MICRO_REPAIR / NONCANONICAL_ONLY`
Repository `eariver/japanese-generative-ai-survey`
Existing branch ONLY `weekly/2026-W42-v2-work`.

## 0. Fail-closed git identity and immutable controls

Sol dispatch supplies **Exact Starting Remote HEAD** and **Expected Starting Tree** for commit containing this contract. Fetch/ref + Git commit/root Tree read-only and require exact match before any write. Also verify main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`, Frozen Core v2 `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. r17 baseline HEAD/Tree `8509ee3354cc2b4e83abe5b230b8733485676320`/`87ba200f48d791cc24a465b752c7a55222b28c92`. If mismatch/undetermined → **ZERO WRITES, STOP and report**. No new/fallback/review/repair branch, no reset/rewrite/rebase/force; normal commit and non-force push to existing branch with remote lease check just before push.

Fully protect **main, Frozen Core, shared roots, W42 accepted Evidence/Selection/Architecture, Human Architecture r1, canonical Draft v10.0, Production State, Human Gates/review index/checkpoints, r11–r17 historical artifacts**. Changes ONLY NEW `sources/2026-W42/execution/editorial-revision-r18/`, `execution/diagnostic-r18/`, `execution/sessions/`, append-only `execution/index.md`. All artifacts PROPOSED/NONCANONICAL. No new candidate, chapter, page-target, change in approved Architecture, formal Reader/Publication/Freeze/Release/Stage/Human Gate.

## 1. Mandatory read order

Read `execution/reviews/sol-w42-r17-editorial-closure-preflight-20261018.md` (operative ruling), Sol r17 instruction, r17 session, r17 proposal/reader JSON+MD, citation/bibliography normalization, full diagnostic TeX/style/log/manifest/page index, split contact sheets + individual p16/p17/p19/p20 PNG, and `editorial-revision-r17/human-architecture-pageplan-decision-brief-r17.PROPOSED.md`. Confirm exact verified r17 baseline and 90/90 URL parser/19 aliases/177 ledger rows. r17 21pp diagnostic is historical, not permission to do formal publication.

## 2. Unit A: reader-facing internal-ID leak removal (P0 mandatory)

The r17 reader prose/TeX contains **editorial block-id references**. Make a minimal, meaning-preserving repair on r18 new proposed source:
1. P1 `t1-23` currently: `失敗の内訳はt1-16に集約し、ここでは…`. Remove the reader-invisible block pointer, explain in natural prose that the separate discussion of failure modes complements token counts/cost figures, **or omit the process cross-reference entirely**. Keep single-run evidence, cost denominators, fixed-seed correction, no death-count duplication.
2. P6 `t6-08` currently: `（開放問の数値はt6-06に集約しここでは繰り返さない）`. Remove the parenthetical editorial planning notation; link GeoKTools and Table-5 observed differences through actual benchmark names/comparison conditions, without repeating GeoExpertQueries cells. Preserve Pro negative, Flash positive, domain negatives and all unanswered paper/repo count conflicts.
3. P7 `t7-19` currently: `（t7-07の数値行はここでは繰り返さない）`. Remove this process note; genuinely interpret Glimpse benchmark comparability and vendor-vs-independent methodology without redundant 12-row data. Keep HSS negative, API/non-open-weights and priced token comparison.
4. **Global reader-surface gate**: examine all r18 HEADING/PARAGRAPH/TABLE/NOTE texts, headline/deck, Synthesis-bound reader output, TeX and extracted PDF text for internal block IDs matching `t[1-7]-[0-9]{2,}`, edition-local file paths, `CLAIM_BOUNDARY`, `accepted_context_notes`, `draft-result`, reviewer/machine instructions and editorial placeholders. Distinguish legitimate external technical code/formula; report every hit and why accepted or repaired. **Success requires 0 unintentionally leaked internal identifiers in reader output.** Don't replace leaks with verbose artificial prose.

## 3. Unit B: arithmetic and Human-brief integrity (P0 mandatory)

The r17 Human-pageplan proposed brief says **r17 cover1 + bib4** but uses **26.5+4=30.5** as though all nonbody matter were 4 pages. Fix the conditional arithmetic to **26.5+1+4=31.5 total** (approved body plan plus *r17 observed* cover+bibliography allocation), not a real already rendered 31.5pp PDF. Keep the distinct r16 comparison `26.5+1+3=30.5` as historically true for its observed nonbody split. Never silently mix effective vs physical body pages or subtract double-counted chapter spans. Acknowledge target28/max30 remains approved and this hypothetical layout would exceed max30 by 1.5 pages; bibliography style changes could affect future counts. Distinguish this hypothetical from measured r17 21 total pages and effective body 15.5–17. Review all new decision text and table sums for consistency.

Reissue fresh `editorial-revision-r18/human-architecture-pageplan-decision-brief-r18.PROPOSED.md` that cites verified actual **r18** diagnostic page split/estimated article area after render, preserving actual factual scope and Option A/B/C without selecting Human preference. Do not propose adding decorative editorials or sponsored matter as a means to fulfill technical-body target. If option B chapter allocations are given, add them and verify sum algorithmically. **Do not claim frozen Core supports a post-approved Architecture amendment unless documentation, schema and CLI route are verified read-only**; list uncertainty and feasible governance options, NO invocation/writes.

## 4. Unit C: focused visual layout hygiene without content inflation

Using a local ephemeral build, regenerate TeX and new diagnostic PDF from **exact r18 proposed JSON+reader+citation bytes**, not r17 TeX copy masquerading as new. Preserve r17 successful Table 7 in-body, no isolated table page, 7 tables/7 notes and natural chapter order. Specifically inspect p16→p17 paragraph/table relationship; page top Table 7 over interrupted running sentence from previous page may need better reader flow or anchored positioning. Minimize modifications; do not cause float drift, table-only pages, clipping, large whitespace, or body/bib mixing.

r17 bibliography B57 ASPIRE link had 2-character `ASPI/RE` continuation over p19→p20. If reasonable, prevent an entry stranded with a 2-character trailing URL piece via entry-level pagination/barrier/needspace while preserving readable publisher-title-alias crossrefs and unchanged PDF page-quality criteria. **Do not change text width/font/margins or pad** to force 28 pages. If no safe solution without producing worse page artifacts, record as minor known limitation and stop for independent review.

Archive genuine build into new `execution/diagnostic-r18/`: full PDF/TeX/style/**complete main.log**, manifest (sha256/bytes/pages/build/fonts/warning counts), all individual page PNGs, 2–3 split lightweight contact sheets, page-by-page review and actual *opened* verification. Record PDF total/cover/body/bib actual, effective article-body range/measurement limits and contrast to approved 26.5/28/max30. Claim NO formal Publication Preview/approved manuscript. Keep old r16/r17 original bytes untouched.

## 5. Unit D: frozen validation, exact source and decisive stop

Produce fresh r18 edition-local proposal JSONs for all P1–P7, reader JSON/MD, proposed Synthesis, bibliography/citation maps (can reuse unchanged evidence information but copy new audited versions to r18), block-diff and 3-point leak-removal receipts, technical/language regression scan, notes on Human page-plan arithmetic, visual test report and validation report.

Run real frozen Draft checks 7/7 and Synthesis check PASS from r18 files; checks do **not** replace reader-surface test. Count paragraph chars, tables, notes, 90 bibliography keys/19 aliases/177 citation rows; if changed, explain precisely. Confirm no regressions in Maia ONE pod + 750 GB/s, LFM Legal Entity §5(c), Argon random Easy+non-playing Observer, ASPIRE publisher real-robot results and figure UNKNOWN, Earth tool-vs-plan Pro negative/Flash positive/GeoKTools Table-5, aptamer 131/311 vs separate 8 clone, Nemotron accepted **token length** vs rate, chronology, source rights and independent source tiers.

Write `editorial-revision-r18/reader-surface-and-pageplan-closure-r18.md`: explicit S17-01/02/03/04 old→new, exact regex/static receipt, no unreported leaks, what is intentionally left, complete human brief math verification. Record whether all reader-surface hazards closed. If any new PDF only generated to reprint uncorrected IDs or any discrepancy persists, stop `R18_READER_SURFACE_BLOCKED` honestly.

Commit via exact remote lease and normal nonforce push only to W42 existing branch. Remote readback final HEAD/Tree + all new blobs + historical-state invariants. Terminal `SOL_W42_R18_FOCUSED_CLOSURE_AUDIT_READY / NONCANONICAL` (or `R18_READER_SURFACE_BLOCKED`). Sol then requests an **independent focused audit** of r17→r18 and only afterward considers asking Human to revisit the page-plan. Do not call Human Gate, no formal publication.
