# J-GAS 2026-W43 — Editorial Sol acceptance of independent r8 ZIP technical audit and Human core-free proof review offer

Date: 2026-10-28 JST.
Authority: EDITORIAL_SOL_ADJUDICATION_ONLY / NONCANONICAL_CORE_FREE_PROOF_ACCEPTED_FOR_HUMAN_CONTENT_AND_LAYOUT_REVIEW.
Repository: eariver/japanese-generative-ai-survey, existing branch weekly/2026-W43-v2-work.

## 0. Source, fixed identity, evidence

Independent audit report received from user: `20261028001028_SolReview.md`, auditor timestamp 2026-10-28 00:10:28 JST. Attached report raw SHA-256 `48870b821b571fda31fc6f0411f61a48b09eff59f02637e26631134c28164d0d` (verified by editorial Sol locally). This entry is a disposition of the independent report, NOT a claim that the report was stored/read back from Drive by this editorial session.

Independent terminal: `INDEPENDENT_W43_R8_P2_SIDECAR_AND_PDF_PASS`. P0=0, P1=0, P2=4; P2s are non-blocking, documented continuing limits.
Immutable r8 article/PDF HEAD `953a9d331972fdae237da4bd0f1019b17168a118`, Root Tree `dfafff50c946e3d0abc051eb419797de283b192a`.
Immutable r8 PDF path `sources/2026-W43/execution/core-free-preview-r8/main.pdf`, SHA-256 `abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`, 487351 bytes, 22 A4 pages.
Immutable r8 TeX SHA-256 `4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d`.
P2 sidecar fixed HEAD `de5e41c253de37015fdb828503040f818698c6bc`, Root Tree `5da261bfc4c1791f912033937ea1bf909f39ffc1`.
Frozen main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core v2 `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

Immutable GitHub PDF URL:
https://github.com/eariver/japanese-generative-ai-survey/blob/953a9d331972fdae237da4bd0f1019b17168a118/sources/2026-W43/execution/core-free-preview-r8/main.pdf

## 1. Independent executable evidence accepted

The SEPARATE independent Sol normal Chat audited the uploaded fixed ZIP, verified 60 entries (53 files), matched ZIP SHA256 `14132547eab1a3853ec9459832d76a7a8c5553804c7103a536874208106adfdc`, recomputed fixed PDF/TeX/log/checker and Git-style BLOB hashes, and verified fixed GitHub trees.
Real Python process results:
- r8 exact fidelity clean 27/27 PASS, exit 0.
- r8 existing negatives 12/12 PASS, exit 0. Original N-operator-insert taxonomy limitation not hidden.
- P2 strict sidecar 4 actual PASS + 1 baseline INFO, exit 0; strict operator insertion two required causes, N10 and N13 detected.
- Independent NEW N15 P1 ordinary prose OpenMDW-1.1 licence OSI UNVERIFIED -> falsely OSI APPROVED was non-noop (SHA changed) and rejected, exact original checker exit 3, 24/27 PASS and 3/27 FAIL for PROSE_FIDELITY_LOSS.
- Actual fixed PDF binary parsed: 22 A4 pages, 75 external URI actions / 28 unique HTTP target strings, 8 TOC named internal destination links landing pp3/6/9/11/12/14/15/17, 14 embedded Unicode font subsets, Japanese text layer, no harmful action or missing page observed.
- New 150dpi render ALL 22 pages compared to fixed committed PNGs: 99.8215% mean pixel identity, min 99.7124% (p11); difference consistent with Ghostscript version 10.05.1 vs 10.06.0 anti-aliasing. No material content loss. All 22 pages reviewed, old A/B/C meta corrections visible on p04/p11/p22. Two minor Overfull vbox 2.61676pt warnings on pp14/15 visibly nonblocking.
- 20 tables, 3 figures, 5 code, 5 recap, 36 bibliography keys, segmented two-column 32 begin/ends maintained. Original code and PDF print matched within contract limits.

## 2. Four P2 / scope limits accepted without artifact mutation

P2-A original r8 `build-manifest-r8.json` retains invalid 39-char historical Tree `2429f675db817cc38333182734ed6338e1abc68`; correct 40-char `2429f675db817cc38333182734ed6338f1eabc68` in additive P2 sidecar. Read both; do NOT edit fixed r8 manifest.
P2-B original r8 checker accepts an insertion negative under any expected cause; strict sidecar asserts all expected causes incl. READER_META_LEAK. Operator meta taxonomy is not exhaustive; exact diff protects bounded r7→r8 fidelity.
P2-C old r8 page QA has misplaced notes; additive sidecar corrects Table11=p13, Table16=p17, recap heading=p20, bibliography heading=p21. Do NOT rewrite fixed r8 page QA.
P2-D 2 mild Overfull vbox warnings remain logged but new independent render finds no substantive clipping. Do NOT alter approved PDF solely to suppress these warnings.

Scientific limits unchanged: 36 bibliography keys, 15 CURATED_REVIEW_REQUIRED (13 natural + 2 further-reading); not upgraded by audit. Edition-specific 31 Architecture obligations historical distinct r3.2 independent 20/11 vs r2 diagnostic 18/13 are NOT new r8 Human approval. No all-primary-source truth certification or independent full benchmark. LuaLaTeX was not independently rebuilt in auditor's session but authenticated build logs and real PDF rendering/structure were checked.

## 3. Editorial decision / Human pre-review offer, not a lifecycle gate

Adjudication: `SOL_W43_R8_INDEPENDENT_TECHNICAL_PASS_ACCEPTED / HUMAN_NONCANONICAL_PDF_CONTENT_LAYOUT_REVIEW_PENDING`.

Only the exact fixed r8 PDF may now be **shown to the user for Human review of article content, Japanese prose, coverage/depth, visual layout, tables and bibliography**. This is an *edition-local noncanonical, UNVALIDATED core-free PDF proof*, visibly marked `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` and `NOT A PUBLICATION PREVIEW`. Passing the technical audit DOES NOT turn it into an official canonical `Publication Preview` or a publication-ready artifact. Do not call its viewing/approval the approved `human_gates.publication_preview` event.

Do not auto-approve the Human's assessment; wait for explicit Human acceptance or requested changes to this specific PDF exact SHA. Do not create a Human Gate receipt yet. No automatic Freeze/Release. If the Human accepts this core-free proof, separately plan the lawful route from the frozen-Core native Draft blocker to any actual official Publication Preview / publishing; changing Core is NOT authorized. Only Human may authorize a specifically governed exception route with documented scope/limitations. No `DRAFT_COMPLETE`, `ADVANCE_STAGE`, `publication_preview: approved`, canonical PDF substitution, tag, PR/merge or release through this disposition.

Native Core blocker remains `BLOCKED_DRAFT_NATIVE_VALIDATION` (`Screening package basis drift: state_sha256`), and `sources/2026-W43/production-state.json` remains `ARCHITECTURE_ESTABLISHED` with `human_gates.architecture_review=approved`, `human_gates.publication_preview=pending`, draft/validation/publication_preview machine checkpoints pending. Shared Frozen Core v2, Architecture/Selection/Evidence/State and formal Human Gates are immutable in this action.

## 4. Human review points

For this 22-page technical proof, ask the Human to check: (1) whether P1–P8 provide sufficient technical depth and 5-paragraph recap, (2) Japanese naturalness/terminology and unsupported claims, (3) readability of two-column pages, 20 full-width tables, figures, code and sources, (4) the explicit uncertainty markings for source-original unknowns, post-cutoff links, release status, claims/benchmarks/licence, (5) completeness and whether correction is required before any public issue.

Next action is HUMAN review / decision of exactly pinned noncanonical proof. Muse work is NOT required merely because independent PASS occurred. If Human requests changes, issue a new bounded instruction with new immutable proof SHA and independent re-audit of affected scope. If Human accepts, record only the content/layout pre-review approval (distinct from Human Publication Preview Gate) and decide separately how publication authorization is to proceed.

This record changes only the editorial evidence lane. The branch itself gains one documentation commit; no previous r8 PDF, TeX, images, manifest, sidecar, source/prod State, Frozen Core, release or formal Gate is changed.
