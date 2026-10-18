# W42 Muse r20 — diagnostic-only terminal-stamp elimination and page-plan recalibration

Date: 2026-10-18 JST
Authority `SOL_EXECUTION_AUTHORITY / R19_SOL_PRINT_PREFLIGHT / R20_ONE_DEFECT_ONLY / NONCANONICAL`
Repo: `eariver/japanese-generative-ai-survey`, existing branch ONLY `weekly/2026-W42-v2-work`.

## 0. Exact remote identity / read-only protection

Sol dispatch includes Exact Starting Remote HEAD and Expected Starting Tree for THIS instruction commit. Before writes fetch remote ref + commit + root Tree and compare byte-for-byte. Check reviewed main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`; Frozen Core `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`; r19 inspected baseline HEAD/Tree `fc5a3cdb52dd1d6f62de91d007dcd4973c5f5093`/`e4f7fa41030df236767381157105ec145d385e17`. If anything mismatches/cannot be proven, ZERO WRITES / STOP / report expected vs actual. Recheck remote HEAD lease before push; fast-forward normal commit + non-force push existing branch only. Never create fallback/new/repair/review branch, reset/rebase/force/rewrite.

Protect unconditionally main, shared Core, W42 canonical Discovery/Evidence/Selection/Architecture/Human approval/canonical Draft v10.0/Production State/Review Index/Gates/Checkpoints, every r11–r19 historical execution blob. Write ONLY NEW `sources/2026-W42/execution/typeset-repair-r20/`, `execution/diagnostic-r20/`, one session under `execution/sessions/` and truthful append to `execution/index.md`. No Architecture revision, no Stage validation/Reader/Publication/Freeze/Release or Human Gate call.

## 1. Read exactly, no source rewrite

Read `execution/reviews/sol-w42-r19-print-preflight-disposition-20261018.md`; r19 Sol instruction and Muse result; fixed r18 Reader source `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` with all r18 proposal blocks; r18 bib/source/ledger (90 keys/19 aliases/177 rows); r19 `typeset-repair-r19/bibliography-display-map-r19.json` and policy, source hashes and exact `diagnostic-r19/main.tex`/`preview.sty`, manifest/log, p1,p16–21 images. Preserve byte-exact reader-facing texts: 7 chapters,136 paragraphs/25,015 chars,7 tables,7 notes,7 headings/157 reader blocks and Table7 placement. All source/category aliases remain byte-identical; r19 bibliography printed text unchanged.

The current `diagnostic-r19/main.tex` contains **duplicate** noncanonical stamp: r19 cover macro already shows all three contiguous warnings; after `\end{thebibliography}` there is a centered redundant warning block which flows to an entirely extra p21. Repair ONLY that diagnostic-print-only final block, with no changes to cover stamp. Do not delete a warning from the cover or from the machine-readable manifest; avoid adding other appendix text to fill space.

## 2. Bounded physical fix

Generate new r20 TeX from exact r19 TeX in temp with **ONE justified deletion**: remove the complete stand-alone post-bibliography `\begin{center}...NONCANONICAL...\end{center}` block and leave `\end{document}` correctly closed; all other TeX source bytes must compare unchanged outside this exact span (possibly update only diagnostic header comment to `r20` if unavoidable and report). New TeX remains clearly diagnostic by:
- cover shows `NONCANONICAL DIAGNOSTIC`, `NOT A PUBLICATION PREVIEW`, `NOT FOR HUMAN APPROVAL` in 3 intact lines;
- manifest, filenames, session and page review mark `NONCANONICAL / NOT FOR HUMAN APPROVAL`;
- no canonical Reader or PDF paths, no official Gate/Preview.

Do NOT remove all warnings in the name of fewer pages, do NOT hide classification in a watermark that renders illegibly. Do NOT manipulate margins, font size, title or chapter text, bibliography prints, figures, floats, `needspace`, citation order, or reference style. No new wording, data, paraphrases or filler. Prove TeX text equivalence (diff shows only expected final block, optional header-comment) and PDF body textual correspondence with r19.

## 3. Fresh physical diagnostic proof and QA

Build in a temporary clean workspace from new r20 TeX / identical r19 style. Produce fresh `execution/diagnostic-r20/`: `main.tex`, `preview.sty`, **complete** `main.log`, freshly compiled `main.pdf`, manifest with SHA256/bytes/pages/build metadata, all individual page PNGs and compact split contact sheets, `review-pages-r20.md`. Stable deterministic build if supported, record actual. **Do not assume physical page count=20 before building.**

Open ALL r20 pages individually (do not rely on text-identical old page assertions because page-break behavior could change):
- cover shows all three uninterrupted warnings and document unmistakably diagnostic;
- p16→p17 no Table7/Glimpse sentence bisection, no isolated Table7;
- B28 stays labeled and URL complete on same page, B57 stays readable, all 90 Bxx entries preserve 71 full+19 concise aliases in print, links not clipped, 7 tables/7 notes visible;
- no bibliography URLs orphaned across pages, no machine provenance leak, no last blank/stamp-only page and no orphan trailing stamp; no other new empty pages/large blank columns due to change;
- no overfull/underfull/missing CJK/LaTeX errors, inspect real render not just log; new PDF extracted text 0 unintended internal block IDs.
If deleting final duplicate alone causes a different visual issue, STOP with named `R20_VISUAL_QA_BLOCKED`; do not improvise a broader rewrite under this contract.

## 4. Re-issue correctly calibrated Human page-plan PROPOSED brief

Create `typeset-repair-r20/human-architecture-pageplan-decision-brief-r20.PROPOSED.md`, anchored to r20 REAL observed cover, body-physical (count p2–pN), bibliography. Distinguish r19 **21 pages (cover1+body16+bib3+diagnostic-only stamp1)** from the new intrinsic r20 physical page count. Do not count any diagnostic-only terminal page as magazine content. If r20 indeed becomes cover1 + body16 + bibliography3 = **20 pages**, state it as MEASURED and compute the **conditional** approved-body 26.5 + cover1 + bibliography3 = **30.5** (vs target28/max30) — if actual changes, recalculate from real measured counts; neither 30.5 nor 31.5 is a real printed document. Never use unsupported `15.5–17` effective-body estimate; state `effective usable-page occupied area UNMEASURED; <= [observed body physical]`. Chapter start/stop pages and columns must be rechecked visually from new proof; never add overlapping chapter ranges. Option B remains *indicative only* P1 2.5/P2 2.5/P3 3/P4 2.5/P5 2/P6 2.5/P7 2 =17.0 planned; never equate this to observed physical 16. Human Architecture r1 body-plan26.5/issue target28/max30 remain unchanged. Human preference consultation permitted later; Human Gate revision from present DRAFT_COMPLETE/approved/pending **NOT assumed executable** without separate read-only governance preflight/explicit Human authorization. No advertising/editorial filler proposal.

Also write `typeset-repair-r20/stamp-removal-and-pageplan-validation-r20.md` with exact TeX before/after diff and source hashes, PDF build receipts, all-page QA, prior versus new count, conditional arithmetic and residuals. Session `execution/sessions/muse-w42-r20-20261018.md` and append-only `execution/index.md`.

## 5. Stop and QA authority

Verify frozen authority unchanged (Reader and 7 Draft proposals, evidence, map, source ledger, Core, canonical, State, Human Gate, historical r19). Only new edition-local artifacts and index append; verify final remote SHA + Tree + hashes. Do not run formal Reader/Publication or architecture amendment.

Stop `SOL_W42_R20_FOCUSED_INDEPENDENT_AUDIT_READY / NONCANONICAL` only if cover warning intact, no trailing terminal-stamp page, all pages QA, and updated brief reflects TRUE rendered pagination. Otherwise `R20_VISUAL_QA_BLOCKED` with exact evidence. Then Sol independently checks and commissions a single focused reader/visual/pageplan audit before asking Human to decide whether to keep body 26.5 or approve a new planning direction.