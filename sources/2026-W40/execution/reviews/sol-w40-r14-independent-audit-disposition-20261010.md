# Sol W40 — Independent r14 audit disposition

Status: `SOL_W40_R14_AUDIT_ACCEPTED / REVISION_REQUIRED / R15_BOUNDED_REPAIR_AUTHORIZED / SELECTION_ACCEPTANCE_HOLD`  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Independent review HEAD: `d954797213c78c4cb9914399b3a1f80c5d3c6e5e`  
Independent review Tree: `bd48195905aa1617d33634e50ac998af255ffa8d`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`

This is Sol's disposition of a **separately conducted, Human-delivered, read-only independent r14 audit**, NOT a representation that Sol performed the audit or that the Human approved a Gate. The uploaded original audit remains externally supplied; preserve the distinction between its claims and Sol's decision.

## Audit outcome

Independent verdict: `REVISION_REQUIRED`, not `BLOCKED_INVARIANT_BREACH`.

| Independent readiness | Result | Sol decision |
|---|---|---|
| COVERAGE_28_READY | YES | ACCEPT for staging; 28 exact Candidate IDs, 20 PRIMARY/8 SUPPORTING, correct destination/Role. |
| BOUNDARY_PRESERVATION_READY | NO | MUST correct before Architecture-preparation approval. |
| TECHNICAL_PREP_ACCEPTABLE | NO | MUST repair technical misreadings and materially deepen source-grounded prose. |
| PROVENANCE_CORRECTION_ACCEPTABLE | NO | MUST delimit auditable evidence from Muse's local-file mtime assertion. |
| SUPPLEMENT_PUBLICATION_PATH_ESTABLISHED | NO | ACCEPT no normal path under current reviewed Core; no permission to publish companion or extra asset. |
| SELECTION_ACCEPTANCE_READY | NO | HOLD; AstaBrief/AutoSynthData are technically MATERIAL yet canonical HOLD because of separate Core #562. |
| ARCHITECTURE_PREPARATION_READY | NO | HOLD until Boundary and technical depth repairs independently reviewed. |

## Findings adopted for r15

| ID | Auditor severity | Sol decision / required outcome |
|---|---|---|
| W40-R14-F01 | MAJOR | ACCEPT. 28 selected Candidate Matrix rows contain 113 `remaining_boundaries` entries. Current map uses prose `package_boundary` but lacks exact array-level preservation. Create lossless candidate-to-boundary and package-to-aggregated-boundary staging with independent Core-rule-equivalent membership check (exact strings, no semantic substitution). Retain exact 28-ID map and its validated Roles. |
| W40-R14-F02 | MAJOR | ACCEPT. ContextLM Eq.6: when there are fewer than two successful rollouts, **efficiency advantage** `A_i^{eff}` becomes zero; this does not imply total `A_i = A_i^{out} + w_eff A_i^{eff}` or outcome advantage becomes zero. Correct the RL meaning and explicitly label full equations by primary source. |
| W40-R14-F03 | MODERATE | ACCEPT. ContextLM: actual editable-file context mechanism, prefix reuse FLOPs vs wall clock, +11.4% relative vs -21.5% Codex-summary and -28.9% MEM1, 35.9 points, Suffix Cache Reuse conditions, paper CC BY 4.0 vs repo CC BY-NC 4.0 (verify each artifact and its revision). |
| W40-R14-F04 | MODERATE | ACCEPT. Olmo-core 3: B300 4-GPU/load-balanced MXFP8 BF16 comparison for +21% and 103→95 GiB; explain negative token gerrymandering / expert learning rate outcomes rather than enumerate buzzwords. Keep random-routing system measurements vs full training separate. |
| W40-R14-F05 | MAJOR | ACCEPT. AgentPerf: reported speculative +30–120% **above bandwidth-constraint roofline**, not controlled speculative-vs-non-speculative increase. Initial 14 configs all use speculative methods per independent primary review; independently reverify and preserve hardware/model/version/metric scope. |
| W40-R14-F06 | MODERATE | ACCEPT. OpenTTS: Seed-TTS/CV3 aggregation, multilingual macro and CJK CER, H200 throughput, TTFA batch=1/50 English prompts/3 warmups excluded/median; scripts described as future at W40 article time vs repo currently visible must be time-sliced, not backdated. |
| W40-R14-F07 | MINOR | ACCEPT. RL Environments Hub: framework pin does not fully pin dataset/taskset; annotate exact dataset revision, config, environment and missing reproducibility inputs instead of assuming code versions suffice. |
| W40-R14-F08 | MODERATE | ACCEPT. Correct r14 provenance `CONFIRMED` overstatement: 19:57 +0900 file mtimes were reported by Muse from locally held files, **not independently remeasured by auditor from reproducible repository evidence**. Keep correct JST→UTC arithmetic and git-commit time distinct; timestamp precision/HTTP completion semantics remain bounded. |

## Preserved PASS / boundaries

- Git identity and bounded 12 W40-local r14 changes PASS; no shared-Core/accepted-upstream/State/Gate mutations.
- Full 28/28 Selection↔Matrix↔Coverage Role mapping PASS: 20 PRIMARY, 8 SUPPORTING, no selected missing or HOLD/REJECT intrusion; P5 and P7 corrected; Ross SUPPORTING placed.
- AutoSynthData verifier triad, positive/negative gate relationships and finite-test limitation PASS. Do not reopen fixed finding without concrete evidence.
- Publication topology revised r14 analysis PASS. Release asset name duplicate check != total count; no normal Core supplement approval or reader-complete release while both MATERIAL items are canonical HOLD.
- Main Work State is `EVIDENCE_REVIEWED`, next `stage:selection`; accepted upstream and Human Gates remain immutable.
- Issue #562 / CV2-DM-022 is a **separate Core maintenance task**; do NOT fix in Weekly/Special. Do not misclassify the 8 findings as new Core maintenance items.

## Decision and scope

Authorize bounded r15 edition-local **research, exact-boundary staging, technical corrections, and provenance wording** only. Preserve r14 files as historical review evidence; create r15 successors instead of silently rewriting history. No forced small-page-count limit: technical completeness prevails.

Core rule must be satisfied in eventual formal Architecture: each selected candidate's every original `remaining_boundaries` string must occur in the containing package's `boundaries` array (after exact-string de-duplication within a package, if required). An outline paraphrase is NOT enough. r15 must validate this using actual Matrix/Selection bytes and original Core rule.

The two other editorially MATERIAL candidates (AstaBrief, AutoSynthData) remain `NON_CANONICAL / HOLD`. No formal Selection Acceptance, canonical Architecture artifact, stage/checkpoint transition, Human Gate, Freeze, public companion or release. Do not infer alternate authority from GitHub's ability to upload assets. `SELECTION_ACCEPTANCE_READY = NO` until lawful Core supersession or a separately explicitly authorized valid exception and renewed Sol review.

Follow: `sources/2026-W40/execution/instructions/2026-10-10_muse-w40-r15-boundary-preservation-and-technical-depth-repair.md`.

Terminal status: `SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_REQUIRED`.
