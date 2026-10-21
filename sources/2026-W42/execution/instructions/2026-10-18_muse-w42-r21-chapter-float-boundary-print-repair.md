# J-GAS W42 Muse r21 — chapter-boundary float ordering repair (F-08 only)

Date 2026-10-18 JST
Authority: `SOL_EXECUTION_AUTHORITY / R20_INDEPENDENT_REQUEST_CHANGES_ADOPTED / R21_NONCANONICAL_TYPESSETTING_ONLY`
Repository `eariver/japanese-generative-ai-survey`.
Existing branch ONLY `weekly/2026-W42-v2-work`.

## 0. Preflight, fail closed

Sol dispatch supplies Exact Starting Remote HEAD + Expected Starting Tree for the commit containing this instruction. Verify both from remote ref/commit/tree in read-only operations before ANY writes. Verify main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`, Frozen Core v2 `production/survey-core-v2` HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`, independently audited r20 HEAD/Tree `f44d3301cde2ef0b9ead52f9613e4a08a6ea42e4`/`cc58032feb618cabb7e142a4fd5d36f91e59492a`. If mismatch or unverifiable: **ZERO WRITES / STOP / expected vs actual**. Before push recheck remote lease. Existing branch normal commit + non-force push ONLY; no branch creation, fallback, force, reset, rebase or rewrite.

Absolutely unchanged: main; frozen Core/shared roots; W42 canonical Discovery/Evidence/Selection/Architecture and approved Human r1; canonical Draft v10.0/Synthesis, `production-state.json` (`DRAFT_COMPLETE/architecture approved/publication pending`), gates/checkpoints/review indexes; all past r11–r20 `execution/` bytes. New work only under `sources/2026-W42/execution/typeset-repair-r21/`, `execution/diagnostic-r21/`, `execution/sessions/` plus a truthful append to `execution/index.md`. NO formal Reader/Publication Preview, Freeze/Release, Stage or Human Gate.

## 1. Read order and hard freeze

1. `execution/reviews/sol-w42-r20-independent-audit-disposition-20261018.md` and this contract. The raw independent report `20261018191937_SolReview.md` is user-delivered externally, not committed; do not claim you read raw auditor bytes unless independently retrieved.
2. r20 Muse session, validation, TeX/PDF/log/manifest and ALL 20 page PNGs; r20 page-plan PROPOSED brief, r19 display-map/policy. Chapter-boundary reference problem exists in **r19 and r20**.
3. Exact r18 master `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` and P1…P7 proposals; authoritative bibliography map/dup matrix/citation ledger (90 B keys/19 aliases/177 rows), r19 display map. Reader technical bytes, roles, source locators/rights, 7 TABLE and 7 NOTE content **MUST be identical**.
4. Approved `sources/2026-W42/architecture-v2.json`, Human r1 basis/gates and production state as read-only context. No new depth research needed.

## 2. Core F-08: prevent Tables 4/5/6 crossing the following chapter heading

Actual independently inspected r20:
- P4 Table 4 at PDF p12 top **after** P5 heading on p11 right.
- P5 Table 5 at p14 top **after** P6 heading on p13 right.
- P6 Table 6 at p16 top **after** P7 heading on p15 right.
- Table1/2/3/7 already acceptable; protect those and avoid P7 Glimpse/table-7 regression.

The current r20 TeX declares Table4 environment around lines 436–453 BEFORE P5 `\\section` around line 468; Table5 ~526–539 before P6 section ~569; Table6 ~635–648 before P7 section ~675. TeX source membership alone cannot PASS: **the printed physical order must have each table BEFORE its next chapter heading.**

Build at least two genuinely rendered, source-bytes-preserving print-only layout alternatives where feasible. Candidate methods: `placeins` / `\\FloatBarrier` immediately before relevant next `\\section`, carefully scoped `\\clearpage`, `dblfloatfix`/two-column barriers or moving table environment code to a *completed paragraph boundary within the same chapter* while preserving all table cells/caption/citations. Correct interpretation: a barrier after an already printed next-chapter heading is too late. Nonfloating full-width implementation may be considered if safe with real two-column semantics. Retain printed reading order and all source-body paragraphs/notes as exact bytes. **DO NOT** blindly add `\\clearpage` causing table-only pages or massive whitespace; do not shrink font, change margins, insert filler or meet numeric target by styling. If the inherited TeX class makes a clean solution impossible inside this unit, stop with `R21_FLOAT_BOUNDARY_BLOCKED`, demonstrate actual render and limitation, and request Sol layout authority rather than falsely PASS.

Inspect all 7 tables physical positions:
- each table after an associated portion of its own chapter AND **BEFORE any following chapter heading**;
- no isolated comparison-table page, no sentence interrupted by floating Table7, no cross-chapter image/table; table captions and evidence untouched.
For P4↔P5, P5↔P6, P6↔P7 measure exact page,column, last own-chapter prose vs table vs next section. Verify resulting logical reading with all-page visual images, not only source/LaTeX log.

## 3. Optional print-only bibliography display language

At p20 r20 B63/B64/B66/B67/B68/B70/B71 display **`[SECONDARY]`** while other source labels in the reader bibliography use `二次・参考`. If no extra source/data rewrite is needed, change only these printed classification labels to a consistent `[二次・参考]`, retaining all 90 B keys,19 aliases,71 full links,177 ledger records and source classifications/URL strings. All internal evidence provenance remains in immutable sidecars. Record exact before→after and verify no fact/source boundary change. This is secondary to F-08. Don't touch B28/B57 text, all URL no-orphans, B74 clean URL, B90 last entry and 0 machine-provenance output.

## 4. Diagnostic render, strict all-page QA

Generate fresh print-only TeX from r20 model and freeze r18 Reader bytes. Archive new `execution/diagnostic-r21/`: `main.tex`, identical/unmodified `preview.sty` unless separately justified, **complete** `main.log`, actual compiled `main.pdf`, machine-readable SHA256/bytes/page count and build receipt, ALL individual page PNGs, 2–3 compact contact sheets and per-page **actually opened** visual QA report. Ensure **NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL** remains unbroken on cover; there must be no post-bibliography stamp-only page.

Verify: Table4/5/6 strictly precede next chapter heading in PHYSICAL reading order, Tables1/2/3/7 remain within own chapter, Table7 and Glimpse paragraph unbroken, no chapter float drift, all 7 notes, all citations and 90 keys, no reader block-ID/editor metadata, no orphan URL/B28/B57, clean bibliography B90 terminus and clear CJK. Check p1, **all** interior pages and final page; detect big empties, warnings, over/underfull and missing glyphs. No 20-page count precondition: actual TeX layout may differ and must be measured, not invented. Fail-closed on visual regression. If PDF source/bytes cannot be preserved for independent review, mark `VISUAL_AUDIT_BLOCKED`.

Publish `typeset-repair-r21/float-boundary-repair-and-layout-comparison-r21.md`, real original and alternatives including page/column evidence and solved/not solved statuses; display-only change diff, body/bibliography invariants receipt, and accurate validation.

## 5. Revised PROPOSED Human page-plan brief

After ACTUAL r21 render, create `typeset-repair-r21/human-architecture-pageplan-decision-brief-r21.PROPOSED.md` based on current measured cover, physical body, bibliography pages and chapter starts **page+column**; chapter sharing page must not be summed. Effective occupied area: `UNMEASURED; <= actual body physical pages` unless independently reliable measured definition exists; no invented 15.5–17. Existing r20 measured historical 20=1+16+3 stays history only.

Approved Architecture **unchanged** 7 chapters/28 items, body26.5, magazine target28/max30, Human r1 APPROVED. Option A maintain 26.5 with genuinely new source evidence (no forced text), Option B provisional P1 2.5/P2 2.5/P3 3/P4 2.5/P5 2/P6 2.5/P7 2 = 17.0 PLANNED not observed; Option C structural only with new evidence. Recalculate conditional `26.5 + r21 actual cover + r21 actual bib` as a **hypothetical not a real PDF**, note max30 and uncertainty, and if layout creates more than planned 17 body pages, explain rather than secretly changing proposal. Keep Human **editorial consultation** distinct from later explicitly authorized Core-compliant reopening/re-gating: current `DRAFT_COMPLETE/architecture approved` not a directly pending approval; do NOT invoke any gate or write to canonical.

## 6. Completion and QA

Deliver: `typeset-repair-r21/float-boundary-repair-and-layout-comparison-r21.md`; QA/validation report; optional `bibliography-display-map-r21.json` if classification render updated; updated PROPOSED page-plan brief; full independent-reviewable `diagnostic-r21` PDF/TeX/log/all PNG; session `execution/sessions/muse-w42-r21-20261018.md` and execution index append.

Verify r18 reader master / 7 proposals **unchanged blob IDs**, 90 authority keys/19 alias/177 ledger unchanged, all older execution r11–r20 identical, Core/main/state/Architecture/Human r1 unchanged. Normal commit nonforce + remote HEAD/Tree readback, list all files and full SHA. All r21 changes edition-local only.

Terminal `SOL_W42_R21_FLOAT_BOUNDARY_INDEPENDENT_AUDIT_READY / NONCANONICAL` iff visually both old and all three F-08 defects resolved without regressions, otherwise `R21_FLOAT_BOUNDARY_BLOCKED` with concrete screenshots/source conditions. **NO Reader/Publication/Freeze/Release/Human Gate**. Human A/B editorial preference can be asked in Sol chat separately and is not contingent on this bounded print correction.