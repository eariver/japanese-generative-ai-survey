# J-GAS W43 — Sol r4 bounded print-checker integrity and exact citation accounting

Status: `EDITORIAL_SOL_R3_CHECKER_REQUEST_CHANGES / NONCANONICAL_CORE_FREE / NOT_HUMAN_PDF_APPROVED`
Date: 2026-10-27 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W43-v2-work`
Worker: Muse.

## 0. Six-way remote immutable guard

First, read-only check all three remote HEAD/root Tree pairs before any write; the W43 pair below is **PRE-CONTRACT parent**. Sol's dispatch gives an exact NEW post-contract W43 HEAD/Tree; that post-contract pair controls execution, and it must be the one-normal-FF-commit child of the W43 parent below with this new instruction as the sole changed file.

| Ref | HEAD | root Tree |
| --- | --- | --- |
| W43 parent | `3cdf2a01b810a972ecddfaa41c7dccded55c75f9` | `17b0525fec79d5624a227f82bf7c5493dd1e5b73` |
| main | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| production/survey-core-v2 | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

ANY mismatch -> ZERO WRITES; report exact expected/actual. No new/fallback/review/repair branches, no reset/rebase/force, no main/Core writes, no PR/merge. Clean behind local checkout may fetch then ff-only; recheck remote at push; normal commit, non-force push, remote readback. Do not silently overwrite another worker.

## 1. Fixed subject, source of truth, and Sol editorial observations

Muse r3 fixed HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`, root Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`.
- r3 print `sources/2026-W43/execution/core-free-preview-r3/main.pdf`: declared SHA256 `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`, 483305 bytes, 22 pages; 22 PNGs/3 contact sheets exist in GitHub. r3 TeX SHA256 `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`.
- Git diff from r3 dispatch one FF commit, 43 paths confined to W43 edition-local execution. Main/Frozen Core unchanged.
- Editorial Sol independently inspected r3 TeX: `\\texttt{POST /v1/decisions}` is present, guide `\\url{https://developers.openai.com/api/docs/guides/decisions}` has a correct delimiter, TanStack keys now visibly printed in a table source note, 20 tables/3 figures/36 bibliography labels, compiler log 22 pages and no overfull/illegal errors. These **positive r3 print repairs remain accepted**. All 8 chapters P1–P8, 19 selected, 80 table rows (78 DATA/2 NOTE), 29 claims, five-paragraph recap still protected. Do not undo r3 print fixes.
- Earlier independent r3.5 **source/content audit** `20261026231458_SolReview.md`: `PASS_WITH_LIMITATIONS`, original `R32-FULL-003=FIXED`, remaining P0/P1=0; do not reopen except discovered substantive regression. Current edition-local r3 print is NOT independently visual-audited or Human-approved. No official Core Draft because frozen native Draft is blocked.

**Sol-verified r3 QA defects**:
A. In r3 `print-semantic-fidelity-check-r3.py`:
`(len(rs)==80 and len(rp)==80 and sorted(rs)!=sorted(rp) or True) and len(rp)==80`
passes any 80-row projection; an explicit tautology `or True` bypasses row equality. Replace with a real **80-row bidirectional ordered source-row-to-projection-to-TeX** semantic join. Source/projection may differ in explicitly approved natural-language operator-token substitutions; treat those with deterministic row-id/cell-position allowlist and assertions of exact meaning, unit, comparator, source tier, not a count-only or permissive token match. Require each of 20 exact ordered table headers, 80 physical rows, their DATA/NOTE types, uniqueness, fixed row-to-physical-cell mapping, 29 anchored claims (same row, model/metric/printed value/unit/comparator), three figure blocks, P8 route and 5 recap paragraphs. A swapped, duplicate, omitted, altered row or reassigned claim must fail, even if aggregate counts stay 80.

B. `N-wrong-clock` merely constructs a changed string and checks that it differs; it does **not** invoke the common positive validator against that mutated input. `N-qualifier-stripped` similarly only checks that text deletion occurred. And `neg()` detects missing API route only if it vanishes in BOTH projection and TeX; removing in either alone can slip through. Replace all negative cases with execution of the **same** validation entrypoint used for clean input against isolated ephemeral files/strings. Require assertions of **specific expected failure cause**, not merely a crash or any failure. Minimum true negatives: API deletion projection-only, TeX-only, both; swapped GH/npm times while row count unchanged; wrong provider-scoped npm URL; Japanese punctuation swallowed by `\\url`; source qualifier stripped in projection and in TeX separately; delete/duplicate/swap physical table row (including in same table with count held constant); alter table header, row NOTE/DATA, change model/variant/metric/printed number, drop one claim, alter actual printed bibliography URL. Ensure actual test result identifies bad source and negative's intended reason. No `or True`, no count-only fake semantic check, no regex of product name as substitute for claim-specific semantics. Distinguish statutory environment/unsupported tests explicitly.

C. r3 `source-key-audit-r3.md` claims an exhaustive exclusive classification `18/15/2/1/0` (EXACT_IN_BODY / NATURAL / FURTHER / UNAVAILABLE / ORPHAN), but the **actual r3 TeX body** before `\\begin{thebibliography}` has **20 exact string occurrences among 36 distinct `\\bibitem` keys**, because `tanstack-gh` and `tanstack-npm` were newly inserted. r3 audit still categorizes those in NATURAL rather than EXACT; do not double-classify as mutually exclusive groups. More important: `recap` literal appears in internal `\\label{sec:recap}` and may not be **reader-visible citation**. Classify separately `EXACT_VISIBLE_CITATION`, `EXACT_MACHINE_ONLY` (labels, comments, source metadata), `EXPLICIT_NATURAL_REFERENCE`, `FURTHER_READING`, `UNAVAILABLE_NO_CLAIM_PROOF`, `ORPHAN/AMBIGUOUS`; use positive explicitly computed TeX *reader-visible* spans, not mere substring anywhere in the pre-bib TeX. Give a row for each of 36 bibitems, each assigned exactly one exclusive primary category, evidence tier, genuine body location and exact claim if any. Additional qualifications can be auxiliary flags, not double counting. Clearly report no claim-provenance support from a 404/RAW_NOT_ARCHIVED raw body and provider-clock separation. Recalculate the true distribution from data rather than presupposing a particular sum. Reader-visible bibliography references are not necessarily a `\\cite`; plain keyed source notes work if the key is genuinely printed. Correct both human-facing audit and any machine validations of those counts.

D. `PRINT_SEMANTIC_PASS` previously covered mostly 35 global literals. It did NOT prove that each claim stayed in its correct 80-row physical location nor that all keys mapped to their source tiers. Make names/descriptions of passed checks match actual coverage; if full verification cannot be implemented under exact scope, emit `PRINT_SEMANTIC_PARTIAL/REQUEST_CHANGES` and stop without invented PASS.

## 2. Bounded action and output surfaces

**Prefer fixing validator, reference report and sidecar evidence ONLY**; do not rebuild an unchanged TeX/PDF just to change a validation report. If a truly reader-visible content error is found by strengthened checks, STOP with exact immutable source→projection→TeX/PDF discrepancy and propose a separate narrow text/print repair; no silent scientific rewriting.

Create files exclusively under new `sources/2026-W43/execution/core-free-preview-r4/`:
- versioned **new** `print-semantic-fidelity-check-r4.py` + `print-semantic-fidelity-check-r4.result.json` (or equivalent) with real positive and negative runs, reproducible invocations, error labels and actual exit codes;
- `claim-and-table-print-binding-r4.md` with per-table header/row/claim actual semantic join and exact failure cases, r3.5 Reader raw input SHA and r3 print files hashes;
- `source-key-audit-r4.md`, 36-key one-class-per-key inventory and programmatically checked classification.
- `r3-pdf-artifact-readback-and-qa-boundaries-r4.md` with fixed PDF/TeX/PNG GitHub blob IDs/sizes/SHA claims and explicit limitation that reading log and binary existence is NOT independent all-page visual inspection. If PDF bytes are locally available to Muse, independently check raw sha256 and compare extracted text to protected values; do not claim Sol did so.
- `independent-semantic-visual-audit-request-r4.PROPOSED.md` only after validator is honest PASS, fixed previous r3 PDF HEAD/Tree; state Human Gate/Native Draft boundaries.
- `SOL_W43_CORE_FREE_PREVIEW_R4_QA_HANDOFF.md` under `execution/`, new session file and append-only `execution/index.md`.

All r1/r2/r3 preview assets, r3.5 reader/ledger/manifest/checker, original Architecture/Selection/Evidence/State/Human approvals, shared Core/main/Frozen branches byte-identical. No native `DRAFT_COMPLETE`, no official publication/v2 manuscript, no canonical `surveys/weekly/2026-W43/main.pdf`, no Gate decision, no Freeze/Release.

## 3. Terminal, deliverable

Success **only if** actual source/projection/TeX row+claim fidelity is established with real negatives and all 36 source keys honestly categorized: `MUSE_W43_R4_PRINT_QA_INTEGRITY_READY_FOR_SOL_RECHECK`. Keep fixed r3 PDF; don't claim new r4 PDF if none authored.

Otherwise `MUSE_W43_R4_PRINT_QA_INTEGRITY_BLOCKED`, with specific rows/claims/negative tests and diagnostics. In either case report starting/final remote HEAD + Root Tree, exactly allowed paths, unchanged main/Frozen Core/State/Gate, actual tool executions, raw hashes, scope of unresolved source confidence and PDF visual access limitation.

Only upon editorial Sol recheck of a genuine r4 PASS will a **separate independent Sol** read-only semantic+all-page visual audit be commissioned. If that auditor cannot retrieve PDF/PNG bytes, it must state `PDF_VISUAL_AUDIT_BLOCKED` rather than pretend to have inspected pages. Human PDF review and eventual publication/bypass require separate decision and are NOT authorized by this instruction.
