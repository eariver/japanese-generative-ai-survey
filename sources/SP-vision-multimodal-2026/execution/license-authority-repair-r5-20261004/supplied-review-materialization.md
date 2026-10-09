# Supplied independent review — materialization (FINAL LICENSE AUTHORITY REPAIR / FACT-FINDING)

Provenance: worker transcription of the supplied task instruction received 2026-10-05
against Exact Starting SHA `089af4726d21575a40130e37adf367c90d26e475`
(tree `344674e32b495da68c52459b568fbb2c23dd830e`; remote HEAD/tree read-only verified
exact-match before any write; zero-write stop on mismatch was armed but not triggered).
Lifecycle `ARCHITECTURE_ESTABLISHED`, r5 PENDING. Frozen Core read-only. No new branches.

This file is a worker transcription, NOT a Human review, NOT a Human r5 decision.

## Mission (§1)

Fresh independent review confirms structural blockers nearly resolved. Narrow blockers only:

- VM-D074 Qwen3-VL model-weight license authority under-binding
- VM-D075 Qwen3-Omni code / model-weight license authority under-binding
- resulting P09 canonical license state
- reflecting current Evidence residuals on the Human Architecture Review surface

No Discovery reopen, no 112-card re-survey, no Selection redesign, no 16-package redesign.

## Direction-selection policy (§2, acknowledged)

Worker may autonomously take the Recommended path (incl. bounded rewind/replay/
Owner-Exception equivalent) when ALL of the following hold: exact task scope, existing
branch only, immutable provenance, Core-controlled machinery, no shared Core change,
no force/reset/history rewrite, no Human Gate decision, no Draft/TeX/PDF, terminal
not exceeded. STOP only for: shared-Core change needed, destructive/history-rewriting
ops, real scope expansion beyond D074/D075, Human APPROVE/REQUEST_CHANGES judgment
needed, or no canonical path (manual mutation only remaining).

## Key verified facts (worker research 2026-10-05, first-party only)

- Qwen3-VL code: Apache-2.0 since repo LICENSE commit 2024-09-06 (single commit, unchanged).
- Qwen3-VL weights: `Qwen/Qwen3-VL-8B-Instruct` (+4B sibling verified) `license: apache-2.0`
  since 2025-10-11 creation commits; all pre-cutoff 2026-09-30. Bound artifacts:
  `model-00001..4-of-00004.safetensors` (+ index). No generalization beyond checked cards.
- Qwen3-Omni code: Apache-2.0 since repo inception commit 2025-09-22 (identical bytes).
- Qwen3-Omni weights: `Qwen/Qwen3-Omni-30B-A3B-Instruct` `license: apache-2.0` since
  2025-09-20 initial commits (current header normalizes `license: other /
  license_name: apache-2.0`). Bound artifact: `model-00001-of-00015.safetensors`.
- Discovery contradiction confirmed: VM-D075 summary claims "Apache 2.0 omni weights"
  while canonical Evidence left weights unresolved. Repaired by binding above authority
  (Discovery summary alone never becomes final authority).
