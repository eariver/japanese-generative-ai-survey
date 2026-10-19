# J-GAS W42 — Muse r29 canonical Reader manuscript and TeX/PDF build up to independent-review boundary

Date: 2026-10-20 JST
Status: `SOL_EXECUTION_AUTHORITY / HUMAN_R29_BUILD_ONLY / NO_STAGE_NO_GATE / STOP_AT_INDEPENDENT_REVIEW`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W42-v2-work`

## 0. Git preflight and protected scope (strict fail-closed)

Sol's dispatch must supply the EXACT full Starting Remote HEAD and Root Tree of the W42 branch commit that contains this instruction. Before any workspace changes, read-only check:
- remote W42 HEAD and root Tree equal dispatch values, including exact commit ancestry;
- reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`;
- Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- State-pinned implementation SHA `a4f25630270f029656f35771592f9ebda02fa5cc` / Tree `e68560d1542806b61b4c55f03063839fd2ec30c0` as read from actual `sources/2026-W42/production-state.json`;
- independent-audited r26 HEAD `2981b30b783e858737fc69cf439afbbfe19d5105` / Tree `617a52200d82575b91a3cd345037daad2e8fbbbd`;
- unchanged W42 state blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`, architecture r1 blob `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`, gate review-index blob `6682579c135fc72599bfdbb883621da726e09f83`, r18 Reader master blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`.
On any mismatch, conflicting output file, missing authority, or unsafe dirty local checkout, **ZERO WRITES / STOP** and report expected/actual. Existing branch only. No new/fallback/repair/review branch, `reset --hard` (including local), rebase, forced history rewrite, force push, or overriding user work. Prefer a freshly constructed isolated checkout/worktree without a new branch. Recheck remote SHA just before push, normal FF commit/non-force push only; final remote read-back HEAD/Tree and changes.

**Historical/protected BYTE-EXACT:** all shared Core/config/scripts/schemas/main and Frozen Core; W42 canonical Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/approved Architecture r1/Draft v10.0/Synthesis, Production Profile, State, all Human Gates and review-index, orchestration checkpoints and existing canonical outputs; r18 Reader and all its proposals; every r11–r28 execution file, independent audit report and decision (except append-only `execution/index.md`). No stage transition or mutation of any other issue.

**New write allowlist, and NO overwrites:** only `sources/2026-W42/publication/v2/reader-manuscript-v2.json`; `surveys/weekly/2026-W42/main.tex`, `main.pdf` and `preview.sty` (if required as local byte-verified style) plus strictly necessary reproduction assets *beneath this issue survey directory*; `sources/2026-W42/execution/publication-build-r29/` for logs, reproducibility proofs, manifests, full page images and independent audit handoff; `sources/2026-W42/execution/sessions/muse-w42-r29-20261020.md`; truthful append-only `sources/2026-W42/execution/index.md`. The exact canonical targets were absent at Sol dispatch; recheck before any new write.

Do NOT create `sources/2026-W42/publication/v2/semantic-editorial-review-v2.json`, `visual-review-v2.json`, `reader-surface-gate*`, a claimed reviewer-PASS `quality-regression-bundle-v2.json`, a Publication Candidate, Gate receipt, bridge request, checkpoint, or modification of `production-state.json`. For required deterministic quality checks, store reports under new **execution** r29 rather than making unapproved canonical status claims.

## 1. Mandatory authority/read order

1. New `execution/governance/human-w42-r29-canonical-reader-pdf-build-authorization-20261020.md`; `execution/reviews/sol-w42-r28-bridge-stage-routing-disposition-20261020.md`; r28 routing reports/packet; conditional Route A Human decision; r26 independent PASS_WITH_LIMITATIONS original and Sol disposition; approved r1 Gate/Architecture and actual W42 State/Profile.
2. Reader source authority `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` exact Git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, seven r18 Chapter v18.0 proposals, quotation/coverage/selection mapping, 90-key bibliography map, 19 aliases and 177-line citation ledger.
3. Independently audited **r26** diagnostic print `execution/diagnostic-r26/main.tex` Git blob `ffdd45742c16fc2f19fd21805479ca9d8373f30b`, `main.pdf` SHA256 `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0`, `preview.sty` SHA256 `f0492fb6b2b9085f282a12120885b20271ec11b0fab56d8848d6f0ee474d534d`, 21pp images/log/manifest, r26 all-7-table cell parity, nonTABLE fidelity, page boundary ledger. Retain good `MULTICOL-V2` inter-segment wide tables, 7mm gutter, font and page geometry unless a justified print-only production-cover change demands safe reflow.
4. Frozen State-pinned Core `scripts/survey_reader_publication_v2.py`, `scripts/survey_reader_fidelity_v2.py`, `scripts/survey_reader_surface_gate_v2.py`, `schemas/reader-manuscript-v2.schema.json`, `scripts/survey_stage_validation_v2.py`, `config/survey-production-v2.json`, relevant bibliography/quality validators. Read Core semantics BEFORE constructing formal Reader manifest; don't invent schema fields.

## 2. Materialize genuine canonical publication source and PDF

Create `surveys/weekly/2026-W42/main.tex` and PDF from the exact r18 Reader text + fully corrected r26 audited layout:
- Preserve **7 chapters/P1–P7, 28 selected topics, 157 Reader blocks = 136 paragraphs+7 headings+7 notes+7 tables, 7 captions/27 table rows/110 cells, no substantive cell differences, 150 nonTABLE literal inclusions, 90 B-keys/19 aliases/177 ledger rows**. Preserve B citation resolution, 729 uses/90 distinct/zero missing per r26, 71 full URL entries, B28/B57/B74/B90 and 17 secondary badges, all caveats (Argon random world+one run; Maia24/96/750GB/s; Earth model-dependent negatives; native MTP mean accepted-token length not rate; wet lab131/311 vs 8 clones; LFM legal-entity sales denominator; ASPIRE real robot result and publisher limits).
- **Remove diagnostic-only publication-surface elements from r26**: `NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL` cover stamp, `週刊Technical Survey（診断用・非正準・未承認）` descriptor and r26-only explanatory output markers in the reader-visible output. Preserve actual cover headline/deck, issue/date/cutoff and editorial meaning. Use a neutral weekly edition descriptor, and no fake `APPROVED`, `RELEASED` or review claim in the PDF. Any distinction between “constructed canonical file” and “not yet approved for release” belongs in governance/manifest/audit records, not in fake cover declarations.
- All Reader/body prose, 7 tables and citations remain untouched except necessary **print-only/cover metadata** changes. Rebuild: diagnostic-stamp removal can alter cover layout or page count. Do not assume exact r26 PDF SHA or page count, or copy the diagnostic PDF unchanged into canonical output. Record actual TeX diff and content invariance. If removing stamp affects pagination, independently inspect all physical table boundaries/last pages again before stopping.
- Keep exact source PDF locally in repository for immutable Git SHA-based independent review, not an external ephemeral link. Save TeX compilation inputs and exact engine/version/environment controls. Use correct `jlreq`/LuaLaTeX/TeX Live 2026, `multicol` + `capt-of`, 7 indivisible full-width comparisons within their own chapters, no orphan caption, page-footer collision or word/sentence bisection. No padding/shortening to force 21. Human Route A accepts approximately 21 pp and residual whitespace; if material pagination/content/quality drift, STOP blocked pending Sol rather than silently revise.

## 3. Formal Reader-facing manuscript manifest; Core schema, not hand-waved

Construct `sources/2026-W42/publication/v2/reader-manuscript-v2.json` using the **frozen Core official builder** `survey_reader_publication_v2.build_manuscript_manifest` and validate with `validate_manuscript_manifest`/schema. In particular:
- `primary_source` MUST bind **new canonical `surveys/weekly/2026-W42/main.tex` exact bytes**, not the r18 editorial-preview JSON and not the r26 diagnostic source. Trace r18/approved bibliography/style through `supporting_files` with genuine roles/paths/sizes and immutable SHA256.
- Bind W42 Production Profile, approved r1 Architecture and approval record exactly. Build `architecture_coverage` for each actual r1 `must_cover` requirement with genuine reader-facing locations and truthful detailed mapping, without inventing evidence or treating counts as full semantic validation. Preserve all approved packages/requirements.
- Map Core publication `reader_requirements` to genuine locations, and use author-attribution metadata truthfully; `READER_FACING_AUTHORED` means **authored**, not Human/Publication approved. Use builder's actual `manifest_sha256` computation rather than manually fabricating digest. Any impossible schema/coverage/Reader-Surface validation: `R29_CANONICAL_BUILD_BLOCKED` with precise reason, do not weaken Core. No inherited blanket PASS from r26.

## 4. Deterministic QA, evidence and independent audit handoff

Re-run fresh r18 Reader→**new canonical TeX** 7 TABLE/27 row/110-cell exact comparison, verify 150 non-TABLE blocks, all notes/chapter order/citation ledger/bibliography/URLs. Separate actual source fidelity checks from printed PDF text/visual checks. Check zero unresolved B keys and printed internal machine IDs, no diagnostic-only text. Verify cover, all 7 full-width tables caption and rows on SAME physical page, correct chapter sequencing, no story interrupted by full-width table, table3 caption/row cohesion, table4 Decider, table7 ASPIRE, terminal P7 not near-empty, bibliography B90, no missing glyph, footnote/url clipping, compiler warnings. Record every PDF page count, actual page text-density/whitespace; area `UNMEASURED` unless measured. Compare before/after physical page map with r26; all pages must be readable.

Use Core deterministic validators only for artifacts that **already exist and meet their prerequisites**, never fabricate semantic-editorial or visual review judgments. Store machine-check evidence separately as r29 build reports (or labelled `PROPOSED`, NOT PASSED Human/independent records) under `execution/publication-build-r29/`. No `Reader-Surface Gate PASSED`, no `ADVANCE_STAGE` request, no new checkpoint; canonical state stays `DRAFT_COMPLETE`.

Deliver new r29 evidence:
- `execution/publication-build-r29/canonical-build-provenance-and-diff-r29.md` (r18→r26→r29 exact content/print provenance and exceptions);
- `execution/publication-build-r29/reader-manifest-and-architecture-coverage-r29.md` (builder/validator output and r1 must-cover location mapping);
- `execution/publication-build-r29/reader-fidelity-and-bibliography-parity-r29.md` (all rows/cells/citations, fresh);
- `execution/publication-build-r29/physical-print-page-and-table-ledger-r29.md` (all 7 physically, 1–N page review, blank/clip/exact typography and any regression);
- `execution/publication-build-r29/build-manifest-r29.json` (actual TeX/PDF/style/manuscript SHA256, sizes, page count, immutable refs, toolchain, compilation logs, zero tolerance for fake PASS);
- `execution/publication-build-r29/main.log`, **all individual `pages/p-01.png` .. `p-NN.png`**, contact sheets and `review-pages-r29.md` pointing to fixed files;
- `execution/publication-build-r29/independent-semantic-visual-audit-request-r29.PROPOSED.md` describing exact source/PDF refs, formal semantic/edit/aesthetic questions and previously closed errors, **without any fabricated independent outcome**;
- `execution/sessions/muse-w42-r29-20261020.md` and truthful append to `execution/index.md`.

If full-page evidence cannot fit Git or fail to persist, do not claim audit-ready. You may split evidence into multiple normal non-force fast-forward commits on the SAME branch under the same guard/lease and allowlist; all output must be remote-read-back verified.

## 5. Exit criteria / handoff — absolute no Stage or Gate

Success ONLY when canonical manifest + canonical source/PDF physically exist, fresh deterministic checks pass, ALL pages persisted, no source fidelity or layout regression, AND exact immutable remote HEAD/Tree are confirmed:
`SOL_W42_R29_CANONICAL_BUILD_INDEPENDENT_AUDIT_READY / STAGE_DRAFT_COMPLETE / PUBLICATION_UNAPPROVED`.

Blocked on any required artifact, substantive mismatch, missing QA proof, missing capture, poor print geometry or compile/manifest failure:
`R29_CANONICAL_BUILD_BLOCKED / NO_STAGE_OR_GATE` with evidence, exact blocker and no false READY.

**STOP at independent-review boundary.** Do not create formal `semantic-review`/`visual-review` records marked PASS; do not create `reader-surface-gate` PASSED, `quality-regression-bundle` falsely claiming human/agent PASS; do NOT call Bridge `ADVANCE_STAGE`, `VALIDATED_DRAFT` transition, Publication Candidate, Publication Preview Human Gate, Freeze, Release or any Architecture change. Muse self-declared deterministic build PASS is not a separate independent Sol review. Independent Sol will read the exact new HEAD and canonical PDF/images before any further authorization.

Finish with full remote HEAD/Tree, normal commit ancestry, complete changed-path list, number of pages, exact manifest/TeX/PDF hashes, diagnostics/known limits, and external audit handoff paths.
