# J-GAS W43 — Editorial Sol r6: close independent r5 P1, bounded print P2, prepare new noncanonical PDF

Date: 2026-10-27 JST
Status: `INDEPENDENT_R5_REQUEST_CHANGES_ADJUDICATED / EDITORIAL_SOL_AUTHORIZED_BOUNDED_REPAIR / FROZEN_CORE_IMMUTABLE / HUMAN_PUBLICATION_PREVIEW_PENDING`
Repository: `eariver/japanese-generative-ai-survey`
Executor: Muse Worker, existing branch ONLY `weekly/2026-W43-v2-work`.

## 0. Mandatory six-way fail-closed remote guard

A new Sol contract commit advances W43 WORK; **the exact post-contract HEAD/root Tree given by Sol's separate dispatch is the mandatory Muse execution starting pair**. Verify all three remote branch HEAD/root Tree pairs read-only before any local/repo/GitHub writes; verify the new contract-only commit's parent is the WORK pre-contract pair:

| ref | remote HEAD | remote root Tree |
|---|---|---|
| W43 WORK **pre-contract parent only** | `598a9e80b3d00a61997f636cde72d81a9d8a5cbf` | `e6b7f1f52fb727d61ca54f5717955866c06eca08` |
| reviewed main | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| Frozen production/survey-core-v2 | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

Mismatch → **ZERO WRITES** report expected vs actual and STOP. NO new branch, fallback/review/repair branch, reset/rebase/force, PR/merge, main/Frozen Core updates, shared Core tool modification, GitHub mutations beyond normal FF commits on existing W43 and ONLY paths explicitly allowed below. Local clean outdated checkout may fetch+ff-only. Recheck remote before normal non-force push, then remote commit/Tree/file-diff readback.

## 1. Independent audit — accepted, do not overstate

Review the FULL independent read-only report `20261027011100_SolReview.md` supplied to editorial Sol. Its recorded terminal:
`INDEPENDENT_W43_R5_REQUEST_CHANGES`, P0=0, P1=1, P2=3.

Independent auditor **actually fetched and viewed all 22 PNG page bytes** and independently verified six raw SHA-256s (including PDF). Independently written JS joined 20 tables, 80 ordered rows, **307 nonempty TeX cells**, 29 claim row facets, with zero mismatches, `PASS_WITH_LIMITATIONS`. Actual r3 paper showed no major missing page, tofu, or broken primary table. These positive findings stand.

- **P1 `W43-R5-AUD-01` ACCEPTED**: r5 `V06-recap` only joins r3.5 reader and projection, not TeX recap; `V06-figures` checks headings not all figure content; ordinary P1–P8 prose outside 20 tables lacks lossless TeX check. Novel in-memory adversarial TeX mutation changed first recap paragraph from cautious view to 'all independently validated commercially' without triggering r5 table/citation/specific qualifier checks. r5 `H00` hashes fixed on-disk files, NOT arbitrary input strings passed to validator. This is **checker scope defect**, not observed real PDF false assertion.
- **P2 `W43-R5-AUD-02` ACCEPTED AS LIMIT**: portable repo-root absent in auditor context, so r5 Python 22 clean checks / 23 negatives were NOT independently executed. Two TeX row swap negatives duplicated; six-input hash negatives not fully covered. Muse r5 handoff says 24 clean although result JSON has 22 — correct accounting, no fake external rerun.
- **P2 `W43-R5-AUD-03` ACCEPTED AS ONGOING CURATED QUALIFIER**: 36 references classification 19 EXACT_VISIBLE, 1 MACHINE_ONLY, 13 NATURAL, 2 FURTHER, 1 UNAVAILABLE, 0 ORPHAN. The 13+2 require editorial tier/claim judgment, never upgrade a URL or natural phrase to archived source or independent verification. No unfounded full provenance PASS. Missing AA originals, FLUX PR/FAQ, Voxtral units, `RAW_NOT_ARCHIVED` scoped npm registry, 404, post-cutoff references remain caveated.
- **P2 `W43-R5-AUD-04` ACCEPTED READER-FACING PRINT REPAIR**: Actual PDF p20 visibly prints blue-grey internal production note `P8の後に置く独立した締めくくり（5段落）。新規のP9パッケージではない。` just after the `今週の総括` title. This instruction is not part of the actual five recap paragraphs, not a reader-worthy technical sentence and MUST disappear from **new printed PDF only**. Print dense tables p07/p14/p16/p19, small bibliography p21–22 as legibility checks; no missing/clipped cells independently reported.
- **Volume / Architecture**: Approved 8 packages P1–P8, 19 selected 12+7, 31 must-cover historically 20 SUBSTANTIVE_COMPLETE/11 PARTIAL, zero NOT_VISIBLE. Target ~38 pages / max 44 is editorial estimate, not guaranteed min. Actual r3 print = 22 pages (cover1 TOC1 body+recap18 bibliography2). r2 coverage diagnosis locates all 31. The 11 PARTIAL are predominantly missing independent reproduction/original tables/vendor-state, not automatic fillable prose. DO NOT pad, invent measurements, claim 31/31 authoritative PASS, revise Human-approved Architecture, or demand 38pp without evidence. Instead analyze 11 PARTIAL as evidence-limited vs genuinely fixable explanatory gap for Sol editorial decision.

**Known immutable subjects:**
- r5 QA fixed HEAD `fa1caaedb6f2b09a6d8e1f77a505d363ca6d0c31`, root Tree `4576f190346da02c1937778e459eb0391fbf6430`.
- r3 old-print fixed HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`, root Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`.
- Old r3 PDF SHA256 `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`, 483305 bytes, 22 pages. Old r3 TeX SHA256 `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`.
- Original r3.5 accepted reader SHA256 `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`, ledger `6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4`, physical manifest `85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111`, original independent reader r3.5 `PASS_WITH_LIMITATIONS`, old `R32-FULL-003=FIXED`. Do not claim r5 independent P1 reopens the source editorial audit.

## 2. Sequential phase A — full visible prose/figure/code/recap source→TeX proof (BLOCKING)

Phase A first. Run no new PDF print until the new checker genuinely proves its bounded coverage.

Create an **edition-local r6** validator, self-contained invocations/results + exact semantic evidence:

1. Accept `--repo-root PATH` and/or explicit input file paths rather than hard-coded `/home/eariver/git/japanese-generative-ai-survey`. Fail with named missing dependencies, never invent a source. Support an offline staged inputs directory for independent auditor replay, with manifest of exactly required paths/hashes and reproduce commands; no implicit remote fetching, no Core dependencies beyond immutable edition-local originals.
2. Real SHA-256 for six actual immutable bytes; for *ephemeral mutants* bind the tested text argument to its computed hash and expected pinned bytes, so a changed TeX in memory cannot pass a stale on-disk H00 oracle. Distinguish intentional `MUTATED_INPUT` failures from absent path failures.
3. Beyond previously checked **20 ordered tables, 80 physical rows, 307 nonempty cells, 29 anchored claims** and 36 bibliography items: deterministically map **EVERY** source reader-visible normal paragraph, section/subsection, verbatim code block, complete figure body/labels/content, and **all five recap paragraphs** from r3.5 reader → r3 projection → old r3 TeX visible content. Parse TeX real section/paragraph/figure boundaries and escapes; source-to-projection changes must be fixed allowlisted per line/segment, including operator metadata translations, internal repository paths and the ONE printable-production-note insertion. No 'header exists' or 'same paragraph count' proxy. Prove exact normalized content under bounded formatting transformations, line-by-line ordered 1:1 mapping, not global bag-of-words. If exact match impossible, give exact segment ID, expected/actual and reason, and **STOP as PARTIAL/BLOCKED**; no false lossless PASS.
4. Protect P8 `POST /v1/decisions`, URL body link boundaries, data provenance qualifiers, potentially fragile multiline code, all 3 figures' labels and full content, and complete P8→5-paragraph recap, not only 4 global qualifier strings. Preserve numeric values, negative claims, quotation scopes and evidence tiers; don't accept a reworded proposition on string overlap.
5. Negatives through the **same** checker on actual changed in-memory inputs, with asserted explicit failure cause: independent audit's `N-AUD-RECAP-SEMANTIC-REVERSAL` exactly, deleting a mid-section non-table paragraph, changing an internal figure's edge/step, changing a code environment variable/default in a code block, swapping two full prose paragraphs while keeping counts and word bag, destroying only a TeX recap paragraph, and altering only TeX body (on-disk immutable originals untouched). Carry 80-cell/29-claim tests, eliminate duplicated TeX row swap test, test hash corruption separately for each of six pinned source/print inputs. NO tautology, unconditional True, sample-only or global regex without structural anchors.
6. Record actual commands and exit status in a **portable runner**, correct check counts (r5 had 22 clean; avoid handoff '24'), SHA of validation scripts and output. Auditor must be able to rerun from a read-only checkout or a documented staged directory with source bytes; avoid a local machine path assumption. If Python tooling constrained, report exact limitation rather than success.
7. Provide an exact reviewed natural-reference report for 13 NATURAL + 2 FURTHER: key → original source claim → reader paragraph/figure/table → printed citation or natural mention → official URL ↔ archived bytes/derived/RAW_NOT_ARCHIVED/404 → confidence. **Editorial judgment stays open** on evidence-limited cases; do not fabricate newly archived originals or unilaterally change status. The other 21 keys retain exact category transparency.
8. List all 11 approved Architecture PARTIAL IDs (`§1.4, §2.6, §3.3, §4.1, §4.3, §5.1, §5.2, §5.3, §5.4, §6.2, §7.1, §7.3, §8.3` should be taken from the actual accepted 31-entry diagnosis and counted, not this illustrative list) and classify evidence-bound vs editing-depth issue with specific printed page and citation. **Use actual file as authority; do not trust this sentence's illustrative count**. No automatic promotions or extra technical writing in this phase.

**Phase A exit if all verifiable checks PASS**: `R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED`. If any genuine loss or coverage limitation cannot be resolved without changing source/projection/TeX, exit `MUSE_W43_R6_FULL_VISIBLE_FIDELITY_BLOCKED` with precise counterexample, and DO NOT enter Phase B or generate PDF. Do not self-exempt the narrative with "sampled only."

## 3. Sequential Phase B — one deliberate print-only r6 PDF revision (only after A)

Source r3.5 reader, ledger, manifest and r3 projection/TeX/PDF originals remain immutable. Copy **r3** projection/TeX/sty into NEW edition-local `sources/2026-W43/execution/core-free-preview-r6/` (r6 is a new proof, NOT overwrite r3). Remove exactly the P20 production note printing action following `\\section*{今週の総括}` / `\\label{sec:recap}`:

`{\\small\\color{SurveyMuted}P8の後に置く独立した締めくくり（5段落）。新規のP9パッケージではない。\\par}`

**Do not remove the five actual recap paragraphs, and do not rewrite them.** This is the only permitted change to reader-visible words. Other safe changes limited to TeX layout fixes necessary for a real defect found on print inspection (must enumerate and STOP for Sol if substantive). Preserve truthful noncanonical/UNVALIDATED labels as required, but eliminate internal editorial process instructions as magazine prose.

- Rebuild actual `main.pdf` from versioned `main.tex` using recorded lualatex commands and exit codes, save `main.log`, size/pages, raw SHA256, Git blob SHA, compile diagnostics; verify 20 tables/80 rows/307 cells, 29 claims, 3 figures, 36 bibliography entries, P1–P8, 19 placements, 5 recap paragraphs, `POST /v1/decisions`, guide URL, TanStack GH vs npm clocks and provenance qualifiers. Print SHA changes; do NOT assert old r3 PDF hash for r6.
- Real PDF binary `/Annots` link targets and selectable/extracted Unicode text must be tested using actual PDF bytes if available, especially p18 guide, scoped npm link and 36 sources; record count of good/bad links, unsupported annotation parsing, relevant limitations. PDF fonts/embedding and page boxes where tool supports. Do not infer from TeX URL string alone.
- Render every actual new PDF page to `pages/p-01.png…p-NN.png`; all 22 expected only if actual PDF has 22 (no invented page count). Save per-page PNG SHA256/blob metadata and contact sheets; perform all-page visual inspection with special print-size table legibility on p07/p14/p16/p19 and reference p21–p22 (page positions may shift); check no internal production note at recap, no glyph tofu, line overlap, bibliography link wrapping, or large empty body page. Document per-page QA with actual inspected images; do not claim editorial Sol/independent auditor already did it.
- Run Phase A verifier against new r6 TeX/PDF with **a single authorized print-only deletion** of production note as part of segment allowlist; no other prose changes. Original r3.5 reader and immutable r3 PDF still tracked separately. Negative test inserting process note into new TeX should fail `INTERNAL_PRINT_NOTE_LEAK`.
- Regenerate an independent-review REQUEST only (not an audit result) that pins **new r6 print PDF** with exact content hashes, and old r3/r5 historical subject SHA. Separate audit must review r6 print delta, not reuse prior r3 22-page visual result as if r6 binary were identical.

If Phase B build or visual QA BLOCKS, commit truthful partial work and report, do not declare PDF ready. Under NO circumstances create canonical `surveys/weekly/2026-W43/main.pdf`, promote native Stage, mark Human Publication Preview approved, or start Freeze/Release.

## 4. Allowed output and immutable guards

Allowed new files ONLY under `sources/2026-W43/execution/core-free-preview-r6/` and
`sources/2026-W43/execution/SOL_W43_CORE_FREE_PREVIEW_R6_HANDOFF.md`,
one new versioned `sources/2026-W43/execution/sessions/muse-w43-core-free-preview-r6-20261027.md`,
and append-only `sources/2026-W43/execution/index.md`.

Expected r6 namespace artifacts include:
- `full-reader-visible-segment-join-r6.py`, `full-segment-join-clean-r6.json`, `full-segment-join-negatives-r6.json`, `source-to-projection-to-tex-segment-map-r6.md`, `six-input-identity-and-mutant-binding-r6.json`, `portable-runbook-r6.md`.
- `reference-claim-tier-curation-r6.md`, `architecture-11-partial-disposition-r6.md`.
- Conditional Phase B: `main.tex`, `preview.sty`, `main.pdf`, `main.log`, `reader-print-projection-r6.md`, `print-only-diff-r6.md`, `build-manifest-r6.json`, `pdf-links-fonts-extraction-r6.md`, `physical-page-and-table-qa-r6.md`, `pages/*.png`, `pages/contact-sheet-*.png`, `independent-sol-r6-print-semantic-visual-audit-request.PROPOSED.md`.

**Immutable** r1/r2/r3 print and source assets, r4/r5 QA/checker/results, r3.5 reader/ledger/manifest, human-approved Architecture r6, Evidence, Selection, State, Gates, audit reports/contracts, main and Frozen Core v2. Preserve past independent auditor findings and exact provenance.

## 5. Exit statuses and accountability

- Phase A actual full-visible equality succeeds AND Phase B clean rebuild actual PDF/all-page media/integrity succeeds:
`MUSE_W43_R6_CORE_FREE_PDF_READY_FOR_INDEPENDENT_REAUDIT`.
- Phase A incomplete or finds substantive discrepancy:
`MUSE_W43_R6_FULL_VISIBLE_FIDELITY_BLOCKED` (NO Phase B).
- Phase B failed after Phase A PASS:
`MUSE_W43_R6_PDF_BUILD_OR_VISUAL_QA_BLOCKED`.

Regardless of success: no independent acceptance claimed, no Human PDF approval, no formal Draft/Validation/Publication Preview/Freeze/Release. Core-native Draft remains BLOCKED. Muse must report exact six-way start guard, normal FF only, final remote HEAD and root Tree, changed paths, actual script outputs/exit codes, actual r6 TeX/PDF hashes/size/page count, all page image references, explicit unanswered original-material questions, and a concise handoff for **separate independent Sol one-shot re-audit**. If PDF/PNG not actually readable in an independent session, that reviewer must separately report `PDF_VISUAL_AUDIT_BLOCKED`.
