# W42 Muse r14 — source-grounded technical deepening, citation traceability and auditable PDF layout repair

Status: `EXECUTION_AUTHORITY / SOL_R13_REQUEST_CHANGES / FROZEN_CORE_IMMUTABLE / R14_NONCANONICAL_ONLY`
Date: 2026-10-18 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W42-v2-work`

## 0. Start guard — fail closed

The Sol dispatch message supplies the exact **current** remote W42 HEAD and Tree (they are newer than r13 because this Sol disposition and instruction are added as a separate normal commit). Before any writes, verify with remote Git refs and commit objects, read-only:

- W42 HEAD == `DISPATCH_EXPECTED_W42_HEAD` and Tree == `DISPATCH_EXPECTED_W42_TREE` (values given in execution message, not literal placeholders)
- reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`
- Frozen Core `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

If **any** identity mismatches or cannot be verified, STOP / ZERO WRITES, report expected vs actual. Never reset/rebase/rewrite/force or make new/fallback/review/repair branches. Use normal commit(s) and **non-force push only** to the existing branch. Recheck remote HEAD before push; do not overwrite concurrent work.

Protected root/file set: `main`, `production/survey-core-v2`, shared `scripts/`, `schemas/`, `config/`, `.github/`, frozen Core assets, canonical W42 discovery/evidence/selection/architecture, canonical Draft v10.0, synthesis, production-state, machine checkpoints, gate records and approvals. All r14 outputs are **edition-local under `sources/2026-W42/execution/`**, and remain PROPOSED/NONCANONICAL, apart from append-only edition execution index. No VALIDATED_DRAFT, Human Publication Preview, Freeze, Release, or formal Stage advancement.

## 1. Mandatory read and baseline

Read, in order:
1. `sources/2026-W42/execution/reviews/sol-w42-r13-external-review-disposition-20261018.md` (Sol-adopted external findings; original external report `20261018040632_SolReview.md` was delivered by Human and is not claimed to exist in this repo).
2. `sources/2026-W42/execution/reviews/sol-w42-r12-external-review-disposition-20261018.md`.
3. r13 original instruction, session, validation report, source readings, deepening matrix, ledger and all seven proposed Draft JSONs / reader JSON/Markdown.
4. r13 `preview-r13/main.tex`, style, bibliography map, citation ledger, PDF images, build manifest and page review index.
5. Accepted W42 Architecture, Human r1 approval, selection 28 (16 PRIMARY/12 SUPPORTING), canonical Evidence cards/Views and protected State. W41 style/reference in read-only mode.

Explicit base: fixed r13 proof HEAD `5520e8f5b1f3c07686873cdf75a7086761bdea14`, 19 pages, 103 paragraphs / 19,193 paragraph-only chars, 59 end bibliography keys, 117 citation ledger rows, r12 comparison 92 paragraphs / 18,165 chars. Historic r13 `main.log` is **absent**, not committed; do not claim otherwise.

This is a response to an independent `REQUEST_CHANGES`, **not** permission to alter Frozen Core or rerun Human Architecture Gate.

## 2. Work units in sequence

### Unit A — original-source research and technical completeness (before prose expansion)

Create `execution/editorial-revision-r14/source-verification-matrix-r14.md`: for each of 16 PRIMARY topics, state the concrete source URL/document section/table, mechanism/inputs/outputs, evaluation method and denominator, comparison conditions, negative cases / limits, claim status (publisher/academic/independent), proposed block, and what is unverified. For 12 SUPPORTING topics, give their bounded comparison role. Do not invent undocumented details.

Prioritize:
- P1: Wonder/Gemini 4 Argon, Active Memory/Focus lifecycle and agent long-run evaluation; distinguish single trial (e.g. Minecraft 27h14m) from replicable benchmark/claims.
- P2: Maia/HBM4/NUMA and prefill-decode data movement / queuing / resource bottlenecks, LFM batch/hardware/temperature comparability and *document-specific* rights.
- P3: Nemotron LiLiCorr/QAD, MTP native drafter. Independently read https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/ and https://docs.nvidia.com/nemotron/latest/nemotron/super35/rl/index.html (Table 8). Verify SPEED-Bench split, draft length 7, temperature-0 greedy 4.287→4.718 **average acceptance length**, and temperature-1 3.787→4.612 separately. If an item cannot be accessed, mark not verified and leave it out.
- P4: Codex experimental comparator/CI, Scion WAL/cache competition/recovery, HydraFusion routing costs/failure and AutoFix/AI Scan permissions/stop conditions.
- P5: unintended behavior test protocol, distillation offense/defense comparability, NIST ECDSA generator/seed provenance, METR participant access vs published findings.
- P6: read original Earth AI GRA paper and reconstruct **4 configurations × 2 models** (Flash + Gemini 3.1 Pro), numeric scores and uncertainty/3 repetitions, evaluator, model-dependent planner contribution, failures/saturation/resource caps. Differentiate tool access vs plan. Also aptamer 0/167→54/208→131/311 screening, criteria/population, and later eight-clone titration, which **do not share a denominator**; Deep Review comparator and Rosalind terms.
- P7: Vals independent score dataset/evaluation transparency vs issuer metrics, GLM-Legal, ASPIRE sim/real generalization, Glimpse negative cases and API listing vs substantiated functionality.

If original primary papers/tables cannot be read, do not fill gaps with plausible invented denominators. Record `SOURCE_INACCESSIBLE` plus precise link/section and consequence. Use reputable original documents over secondary summaries when accessible. The 28 selected items / approved 7-chapter narrative are immutable; do not add topics or reselect.

### Unit B — evidence-grounded reader manuscript and per-claim citations

Create `execution/editorial-revision-r14/` with seven P1–P7 `draft-result-r14.PROPOSED.json`, reader-preview Markdown/JSON, research/claims ledger, r13→r14 block diff, change ledger, synthesis proposal, and reproducible counter scripts/results. Derive from r13 without rewriting r13 historical files.

Every substantive addition must answer a real technical question with verified mechanism, measurement, failure mode, reproducibility or license right; no boilerplate inflation. Prefer meaningful contrast and interpretation to news/brand lists. Balance P1/P2/P4/P5/P7 depth, not exclusively P3/P6.

For hard numbers, benchmark comparisons, licensing, vendor/independent evaluation and key conditional results: use a **claim/block → source URL + original section/table + conditions → TeX cite** crosswalk. Fix P1 s1-02 eight-source lumping, P3 mixed metrics, P6 GRA/aptamer/SPOT, and P7 Vals issuer-vs-independent metrics. Cite close to claims or in explicit table-source columns, not a broad paragraph-level cluster. Preserve existing B01–B59 identities where still valid; add stable identifiers for verified new references; do not mislabel vendor evidence as independent replication. Recheck F01/F02, MTP length-not-rate and aptamer separate screening/confirmation.

Replace duplicated chapter-end URL blocks with concise chapter navigation or rely on inline cites plus one complete end bibliography. **Do not discard bibliographic entries** to reduce page count. Remove `accepted_context_notes` from reader surface but keep detailed internal trace in sidecar. Replace unnatural `専門身体` and repeated P7 OpenRouter/API caveat. Avoid unexplained jargon, false translation, excessive Sino-Japanese phrasing, ungrounded conclusions and machine-editorial notes.

Counters MUST define exact source and inclusion criteria separately: paragraph-only, table, note, heading, combined `block.text`, TeX-bib and PDF extraction. Record r11→r13 (+21 paras/+2,189 chars) separately from **r12→r13 (+11/+1,028)**; r14 deltas against the same definitions. Reconcile r13 22,446 all-block vs 22,315 “body chars” without declaring either wrong until definitions are tested. Record actual TeX line count with command/procedure (r13 820 logical lines, prior validation report 808 stale).

Run frozen Draft checks on seven r14 **proposals** and synthesis-check genuinely; preserve machine-readable receipts. These PASS results must not imply canonical acceptance or Stage migration.

### Unit C — render revised NONCANONICAL proof with genuine log trace

Build `execution/preview-r14/main.tex`, style, PDF, build manifest, **full actual `main.log`**, all new page PNGs, contact sheets, index and visual-QA table. Use approved W41-aligned style within edition-local transport; do not edit shared style. Do not fabricate r13 log: explicitly document `r13 main.log missing at source HEAD` and new r14 build provenance. If gitignore blocks log, stage **only exact intended file** (`git add -f`) and verify commit inclusion and remote SHA/blob read-back. If full log would disclose secrets or unsafe private data, STOP and report rather than claim committed.

Solve floating table instability structurally (`table*`, float barriers/clearpage, two-column switches, chapter boundaries, bibliography configuration). p16 float-only near-empty layout and p19 two-entry orphan bibliography page **must not recur**. Respect full original bibliography, no evidence deletion. Avoid wrong-chapter tables at chapter transitions. Fix any overfull/underfull hbox/vbox requiring reader attention, missing glyphs, undefined refs/citations, clipped URLs, awkward bibliography entry splits. Never label overfull 43.6pt `harmless` without actual page visual evidence.

Build actual PDF, calculate and record PDF SHA-256, byte length, page count, toolchain/TeX/engine/fonts/build commands, warning counts and full `main.log`. Generate and commit **every page PNG** plus overview/contact sheet(s), and a clickable complete page index; inspect every rendered page as an image, not a text-only check. Preserve cover/footer `NONCANONICAL EDITORIAL PROOF / NOT A PUBLICATION PREVIEW`.

Architecture target: **28 pages total, max 30, article-body plan 26.5**. These are planning targets, not a claim that PDF total equals body pages. **No page padding**, font/white-space inflation or repeated source boxes to hit 28. Validate real density and technical substance after fixing floats/bibliography. If the target still cannot be supported by primary-source-backed actual depth, document section-level shortfall and raise `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED` to Sol at the r14 terminal point. Do not silently downscope to 19 pages or amend Architecture.

### Unit D — verification, read-back, finish

Produce:
1. `execution/editorial-revision-r14/validation-report-r14.md` with real frozen CLI receipts, source/sample citation checks, counters with baseline definitions, all protected SHAs, and complete negative findings.
2. `execution/preview-r14/build-manifest-r14.md` (actual PDF bytes/hash, all artefact hashes/counts, fonts/commands, log read-back, TeX line counts).
3. `execution/preview-r14/review-pages-r14.md` with fixed-commit-safe links and page-by-page density/flow observations.
4. `execution/sessions/muse-w42-r14-20261018.md` with complete changes/failures and separate noncanonical vs Stage status.
5. Append/update `execution/index.md` with r14 status only, never falsify Production State or Gate.

Check `main.log` exists as a committed repository file, not merely in local workspace; verify the actual remote GitHub path and new PDF/PNG hashes against committed objects. Verify all expected PDF pages exist, format readable, references non-orphaned, and r14 changes are only within authorized execution paths.

Normal commit(s), non-force push, exact final HEAD/Tree and remote read-back. If critical unmet conditions, stop with `R14_REVIEW_READY_WITH_BLOCKERS` and disclose, rather than claiming publication-ready. Never create an approval, fake checkpoints, move `DRAFT_COMPLETE`, or merge to main.

## 3. Terminal gate

Stop at **`SOL_W42_R14_REVIEW_READY / NONCANONICAL`**, or a truthful named blocker. No formal Reader/Publication Stage and no Human Publication Preview submission. Sol will decide whether material factual and all-page visual changes warrant another separate independent audit; Muse self-QA cannot count as independent PASS.

Report exact starting and final HEAD/Tree, commits, source access limitations, validators, all seven chapter actual sizes, new PDF pages/bytes/SHA256, log path/blob, page PNG set, known warnings and the unresolved 28-page plan gap.
