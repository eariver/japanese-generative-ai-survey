# Sol W40 — Independent r15 audit disposition

Status: `SOL_W40_R15_AUDIT_ACCEPTED / BOUNDED_REVISION_REQUIRED / R16_EDITION_LOCAL_ONLY_AUTHORIZED / SELECTION_ACCEPTANCE_HOLD`  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Independent review target HEAD: `305aafa8a2d243565a197bb4abc275d987c970e1`  
Independent review target Tree: `a5ba0bd20947a236e54eb1ea2fb4178e076eb9dd`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`

This file is **Sol's editorial adoption of a Human-supplied, separately conducted, read-only independent r15 audit**. It is not the auditor's original manuscript, a Human architecture decision, a Core acceptance, or publication authority. Preserve the fact that the independent reviewer could not directly reproduce every Muse execution claim.

## 1. Independent overall verdict

`BOUNDED_REVISION_REQUIRED`. No detected Git/Core/State/Gate invariant breach.

**Accepted for staging, not formally accepted:**
- Git identity and pre-r15 one-commit, ten-file W40-local changes.
- r13 Selection (28 SELECTED; 20 PRIMARY / 8 SUPPORTING) and r14 Coverage map; exact r15 candidate-to-boundary preservation.
- **113 candidate-boundary relationships**, with exact original strings and 28/28 candidates; **105 unique strings after dedup within package**, zero missing, zero unsupported.
- Static equivalent of unchanged Core `validate_architecture` literal Boundary membership. Muse reported one ephemeral in-memory PROPOSED validator execution with 0 errors using placeholder fields; independent reviewer did not rerun that Python execution. Neither represents actual Architecture approval.
- P6a main technical corrections for ContextLM Eq.6, metrics and MXFP8/Olmo-core boundaries, and P6b roofline/OpenTTS correct measurements; RL Hub remains NOT_REPRODUCIBLY_PINNED for taskset revisions.
- Provenance caveat: local mtime is `MUSE_LOCAL_MTIME_REPORTED / NOT_INDEPENDENTLY_REPRODUCED`; no invented millisecond GET clock.
- r14 supplement feasibility: `NO NORMAL SUPPLEMENT_PATH_ESTABLISHED`. AstaBrief/AutoSynthData remain MATERIAL editorial direction but canonical HOLD due to separately maintained #562/CV2-DM-022.
- Shared Core not modified; `production-state.json` stays `EVIDENCE_REVIEWED`, next `stage:selection`; Gates pending/null.

## 2. Adopted remaining r15 findings A01–A05

| ID | Severity | Sol disposition and bounded r16 scope |
|---|---|---|
| R15-A01 | MODERATE | ACCEPT. r15 outline per-package raw relationship counts disagree with correct r15 JSON. Correct P1 raw 14 (unique12), P4 raw10 (unique8), P5 raw18 (unique17), P7 raw19 (unique16). Other packages unchanged. Build r16 successor outline from **existing exact r15 Boundary JSON**, not manual fresh totals. |
| R15-A02 | MODERATE | ACCEPT. r15 Handoff candidate-level Boundary count distribution is wrong. Exact distribution verified from Candidate Matrix: one candidate has 7, nine have 5, seven have 4, eleven have 3; `1×7 + 9×5 + 7×4 + 11×3 = 113`, `1+9+7+11=28`. Add r16 Handoff correction; preserve historical r15 handoff. |
| R15-A03 | MINOR | ACCEPT. Existing validation shows correct literal membership but does not record independently recalculated `unexpected_strings_count` and deterministic/idempotent roundtrip. Publish r16 machine-readable **new** validation addendum from the r15 source+Selection+Matrix+Coverage bytes. Do not edit historical validation nor regenerate authoritative r15 Boundary JSON. |
| R15-A04 | MINOR | ACCEPT. ContextLM Eq.5 is accessible in arXiv:2609.37725 v1, §4.2 / skill evolution. Re-read the exact primary HTML/paper, transcribe verified mathematical equation and explain its optimization objective and training/development/test split. Do NOT infer an equation from the r15 prose or auditor's unquoted assertion. If not accessible, document honest blocking evidence; no fabricated symbols. |
| R15-A05 | MINOR | ACCEPT. r15 Handoff erroneously assigns dedup to P4 −3/P5 −2. Correct dedup by identical strings in package: **P1 −2, P4 −2, P5 −1, P7 −3**; `113−8=105`. Reconcile independently from Matrix and r15 package arrays in r16 handoff/addendum. |

Exact per-package result for r16 documentation:

| Pkg | Raw candidate→Boundary relations | Unique exact strings | Exact dedup |
|---|---:|---:|---:|
| P1 | 14 | 12 | 2 |
| P2 | 8 | 8 | 0 |
| P3 | 13 | 13 | 0 |
| P4 | 10 | 8 | 2 |
| P5 | 18 | 17 | 1 |
| P6a | 10 | 10 | 0 |
| P6b | 15 | 15 | 0 |
| P7 | 19 | 16 | 3 |
| P8 | 6 | 6 | 0 |
| TOTAL | **113** | **105** | **8** |

## 3. Core boundary

Core Issue #562 / CV2-DM-022 remains a **separate** Core maintenance task. Do not add new Shared Core defect IDs for these Edition-local review-documentation errors. Do not patch Core in Weekly/Special. No prior human Gate decision exists to admit two canonical HOLD subjects. This r16 instruction does not permit Selection Acceptance, Architecture stage/canonical JSON, checkpoint, Human Gate, Freeze, Release, or supplementary public PDF authorization.

All r15 accepted artifacts should remain immutable: `execution/architecture-boundaries-r15.json`, r15 validation, r15 drafts, Handoff, and source inputs. Create r16 addenda/successors only. Preserve corrected soundness/completeness and prior r14 publication-contract conclusions.

Authorized contract: `sources/2026-W40/execution/instructions/2026-10-10_muse-w40-r16-bounded-documentation-and-eq5-repair.md`.

Terminal after Muse: `SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_REQUIRED`.
