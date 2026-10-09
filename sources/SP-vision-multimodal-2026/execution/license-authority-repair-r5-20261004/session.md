# Session — TS-003 Final License Authority Repair (VM-D074/VM-D075)

## Starting authority (read-only verified before any write)

- Branch `special/vision-multimodal-2026-work`, HEAD `089af4726d21575a40130e37adf367c90d26e475`,
  tree `344674e32b495da68c52459b568fbb2c23dd830e`; remote HEAD/tree exact-match.
- Lifecycle `ARCHITECTURE_ESTABLISHED`, r5 PENDING (no r5 record). Frozen Core read-only.

## Supplied mission (§1)

Structural blockers nearly resolved. Narrow blockers only: VM-D074/VM-D075 license
under-binding + P09 state + residuals on the review surface. No Discovery reopen,
no 112 re-survey, no Selection redesign, no 16-package redesign.

## Direction selection (§2)

Worker autonomously took the Recommended path (no Human question): all §2 conditions
verified (exact scope, existing branch, immutable provenance, Core machinery, Core
unchanged, no force/reset/rewrite, no gate decision, no Draft/TeX/PDF, terminal kept).
Formal revision-path probe fail-closed first (zero writes). Record: `direction-selection.md`.

## Research (first-party only, read-only web + curl snapshots)

- Qwen3-VL code Apache-2.0 since 2024-09-06 (single LICENSE commit, byte-identical now).
- Qwen3-VL weights: 8B-Instruct (+4B sibling) `license: apache-2.0` since 2025-10-11 creation.
- Qwen3-Omni code Apache-2.0 since 2025-09-22 inception (byte-identical now).
- Qwen3-Omni weights: 30B-A3B-Instruct `license: apache-2.0` since 2025-09-20 initial
  (current header normalizes `license: other / license_name: apache-2.0`).
- All pre-cutoff 2026-09-30. Bound artifacts enumerated; no over-generalization.

## Staging (untracked exec records only)

- `evidence-authority-supplement-vm-d074.json` (4 sources, Core-built + validated).
- `evidence-authority-supplement-vm-d075.json` (4 sources, Core-built + validated).
- `staged-vm-d074-license.json` (4 claims; code-only claim-3 + new weights claim-4;
  canonical-validated, VERIFIED kept).
- `staged-vm-d075-license.json` (2 claims; resolved buckets; limitation-2 removed as
  resolved; living-surface kept; canonical-validated, VERIFIED kept).

## Authorized execution (§2 pre-authorized; Core-controlled only)

- Rewind ARCHITECTURE_ESTABLISHED → CANDIDATES_NORMALIZED (10 Core-computed paths; CLEAN).
- Replay: Evidence d62028f5 (110 carried + D074/D075 corrected) → Views → Materiality →
  Completeness → EVIDENCE_REVIEWED → Matrix (2 SHAs) + Selection carried (0 diffs) →
  SELECTION_COMPLETE → Architecture P09 sync → Summaries fresh → ARCHITECTURE_ESTABLISHED.
- Union supplement (20 entries) reused read-only at package build; dedicated files untouched.

## Close-out

- Consistency: G06 0, unscoped 0, outside-canonical 0 across arch/summary/attention;
  P09 buckets canonical; P15 39-map; 16 skeleton; G01/G02 preserved.
- No other Evidence/Core/Draft/TeX/PDF changes. STOP at r5 PENDING. See execution-report.md.
