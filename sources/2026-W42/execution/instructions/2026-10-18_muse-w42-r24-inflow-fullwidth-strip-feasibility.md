# J-GAS W42 Muse r24 — in-flow full-width block feasibility, NOT another table* patch

Date: 2026-10-18 JST
Status: SOL_EXECUTION_AUTHORITY / R23_SYSTEMIC_LAYOUT_BLOCKED / R24_INFLOW_FULLWIDTH_FEASIBILITY / NONCANONICAL_ONLY
Repository: eariver/japanese-generative-ai-survey
Existing branch ONLY: weekly/2026-W42-v2-work

## 0. Fail-closed Git identities and immutable authority

Sol dispatch shall supply **Exact Starting Remote HEAD** and **Expected Starting Tree** matching the commit containing this contract. BEFORE WRITES verify both full SHAs from remote ref + commit/root tree, and:
- reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / Tree `801de813319f08777ab1581a5e8875fc1ac5df19`
- Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- r23 baseline HEAD `7f9ccdbe573850021b787c694b30ebd756c37576` / Tree `6c019ee0333888e032b00b8d514c193ac8661c27`.
Any mismatch or missing proof => ZERO WRITES, STOP actual vs expected. Before push recheck exact remote lease. Existing branch only, normal FF commits/non-force push. Never create replacement/fallback/review/repair branch; no force, rebase, reset or rewritten history.

Protected byte-exact: all shared Core/main roots; all canonical W42 Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/Architecture/Draft v10.0/Synthesis, architecture r1 gate/approval, production-state.json, Human Gates, checkpoint/review-index, r18 Reader proposal (Git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`), r11–r23 historical execution outputs. Allowed new edition-local files only under `sources/2026-W42/execution/typeset-repair-r24/`, `execution/diagnostic-r24/`, one session in `execution/sessions/`, truthful append-only `execution/index.md`. NO formal Reader, Architecture revision, Gate, stage transition, Publication Preview, Freeze, Release.

## 1. Read first and state the narrowed hypothesis

Mandatory read first:
- `execution/reviews/sol-w42-r23-blocking-stop-feasibility-disposition-20261018.md`.
- r23 global float root-cause and comparison, reader invariance and r23 SA/SB proof PDFs/all PNGs.
- r22 C2 full proof, r22 Sol visual REQUEST_CHANGES, r18 Reader and all 7 chapter Draft v18.0 proposals, source authority (90 keys, 19 aliases, 177 ledger rows), canonical Architecture/State/Gates.

Known defects: top-of-page full-width `table*` split narrative across p03→04 T1 `立直/し`, p05→06 T2 `開/示だ`, p08→09 T3 `エンドポ/イント`, p15→16 T6 `によ/る`; r22 C2 fixed T7 ASPIRE but retained p18 low-fill 702-character tail. r23 SA/SB/SC did not simultaneously fix these. No 0-warning/self-PASS without explicit visual boundary proof.

**New hypothesis, not previously tested**: swap *asynchronous* `table*` floats for *in-flow* wide blocks at paragraph boundaries using `cuted` `strip` or a demonstrably safe alternative while preserving the two-column body. Do NOT try merely `needspace` or float placement variants again.

## 2. Phase A: minimally scoped compatibility/geometry feasibility (mandatory first)

In isolated local workspace (not canonical), identify actual `lualatex`, kernel and `cuted.sty` versions via log/kpsewhich. Read the installed package docs/source and check caveats (footnotes, floats, right-column transition, output routine, multiple strips/page). **Do not blindly import** new package into shared style. Using current `jlreq`/`luatexja`/`tabularx`/`hyperref`/`tcolorbox` toolchain, build a small realistic sample that includes at least two consecutive actual W42 comparison tables and surrounding verbatim paragraphs.

Experiment with:
A) `cuted` `strip` non-floating table body + explicitly validated in-flow caption/number/label. Check `\captionof{table}` if compatible, otherwise documented local `\refstepcounter{table}` wrapper that reproduces visible caption and hyperlink target semantics.
B) An independent safe alternative **if necessary**: a documented in-flow two-column/full-width output-routine method or an explicitly bounded column-switch alternative; record why it meets or fails the existing typography. Never silently fall back to permanently one-column magazine. Do not change font, margin, baseline, page size, column gap/ratio, prose.

Treat any missing/duplicated characters, table cells, captions, citations, links, failing TeX compilation, unacceptable overfull/underfull boxes, mixed page order or footnote displacement as FAIL, not a nuisance to ignore. Page breaks and blank area must be assessed visually.

If no compatible method even for the representative sample, archive exact source, build log, errors, minimal sample proof where possible and terminate `R24_INFLOW_FEASIBILITY_BLOCKED`; do not claim W42 full print PASS.

## 3. Phase B: full W42 diagnostic candidates ONLY if Phase A is viable

Replace all seven *print-only* table wrappers with source-order in-flow full-width blocks, anchored after the existing legitimate introductory paragraphs and before next chapter headings. Do not alter actual table **cells, captions' visible text, citations, row order, number/semantic reference and chapter membership**. The `table*` container and `\caption` command may be changed to necessary in-flow wrappers; record exact semantic equivalence. All 150 non-table Reader blocks, every Reader sentence, 7 notes, 7 headings, 7 table bodies, 28 topics, citation mapping must stay byte-identical in prose and table data.

Ensure all 7 full-width tables are physically after their relevant context, strictly before next chapter heading; no floated table inserted in a continuing sentence/paragraph/word. Explicitly verify Table1/2/3/6 known bisections, Table4/5 chapter crossings, Table7/ASPIRE. Check that in-flow insertion doesn't create new split/overlap, duplicate or omit content or disturb non-table notes/citations.

Compare at least the best new non-floating build against r22 C2 (21pp/4 splits/p18 tail) and r23 SA/SB (22pp/splits and voids). If useful, test a second in-flow anchor choice or caption method; document genuine rendered proof. Page plan Human Option B is 7 chapters/28 topics, provisional body 17.0; Sol tentative issue target21/max23 is NOT a hard output quota and NOT Human-approved. A clean 20, 21, 22 or 23 page render can all be considered; do not pad or shrink to hit a number.

**Print-readability gate**: no table splitting a single paragraph or sentence, no table beyond hosting chapter, no orphan/table-only pages, no large avoidable near-empty terminal P7 body page (r22 p18 was 702 raw chars), no mysterious blank leaves or extreme column imbalance; ensure cover & 3 bibliography pages only if actually rendered as such. Honest objective PDF page counts, page-by-page char/area occupancy; if area not measured report UNMEASURED instead of inventing an estimate.

## 4. Mandatory evidence and visual QA

For every actual serious candidate archive full TeX, local styling (if any), PDF, complete compile logs, SHA256/bytes/pages/engine/kernel/package versions, page PNGs for ALL pages, contact sheets and a physical table/paragraph-boundary ledger. Open **every single page PNG**; verify both columns (top/bottom of prior and next page) with **verbatim trailing and leading phrase** for every T1..T7. Use source-to-print mapping, not pdftotext-only or zero-TeX-warning claims. Any newly introduced gap/overlap, non-canonical wrapper/leaked IDs or missing table cell is a hard fail.

Verbatim-body and bibliography regression checks: source r18 Reader blob, 136 paragraphs/25,015 chars, 7 tables/7 notes/7 headings/157 blocks, 90 bibliography keys (71 full + 19 aliases), 177 citation rows, 7 secondary display labels, B28/B57/B74/B90 printable URL/body, terminal bibliography, cover 3 diagnostic warning lines, no internal machine IDs. Preserve Argon random world, Maia24/96/750GB/s, Earth negative result, native MTP acceptance length (not rate), wet-lab131/311 vs eight clones, LFM licensing legal entity, ASPIRE real robot caveats. Explicitly compare table-number labels, captions and PDF-text counts to r22.

Never use r24 experiment output to claim canonical approval.

## 5. Files, stop and report

Write in NEW r24 execution paths:
- `typeset-repair-r24/inflow-feasibility-and-interoperability-r24.md`: exact installed package and sample tests; package/output-routine risks.
- `typeset-repair-r24/nonfloating-table-boundary-audit-r24.md`: 7-table physical ledger; before/after comparison; root cause/change; all-page QA.
- `typeset-repair-r24/reader-table-and-bibliography-invariance-r24.md`: source and print semantic and byte preservation; wrapper-only diffs.
- `typeset-repair-r24/option-b-physical-pageplan-r24.PROPOSED.md`: actual physical cover/body/bibliography; no formal Gate; 21/23 tentative.
- `diagnostic-r24/` sample-and-candidate full proof PDF/PNG/log/manifests; final candidate PDF/TeX/PNG ONLY when valid.
- `execution/sessions/muse-w42-r24-20261018.md` and truthful index append.

Terminal:
- `SOL_W42_R24_INDEPENDENT_PRINT_AUDIT_READY / NONCANONICAL` only if actual full W42 two-column PDF demonstrably meets all 7-table/boundary/occupancy/content requirements.
- `R24_INFLOW_FEASIBILITY_BLOCKED` if package/engine/semantic interaction cannot pass small sample.
- `R24_LAYOUT_QUALITY_BLOCKED` if sample works but full 7-table W42 PDF still fails.

Normal FF commit, non-force push, remote HEAD/Tree and proof read-back before reporting. Worker self-PASS != Sol/independent auditor PASS. Do not update Architecture/Gates/Publication/Freeze/Release.
