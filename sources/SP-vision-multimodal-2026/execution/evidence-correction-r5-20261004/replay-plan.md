# Downstream deterministic replay plan — evidence-correction-r5 (POST-AUTHORIZATION only)

Scope: executes ONLY after the rewind to CANDIDATES_NORMALIZED is authorized through
an explicit Human decision (see `reentry-analysis.md`). Uses current frozen Core pipeline
only (phase pattern of `execution/architecture-r3-intake-20261003/phase_*.py`).
No Discovery/Screening redo (112 records + Screening authority carried byte-identical).

## Step 0 — authorized rewind (Human decision first)

State returns to CANDIDATES_NORMALIZED through the authorized mechanism; r4 APPROVED
history preserved (`gates/reviews/architecture-r4.json` + approvals snapshot NEVER deleted;
active `gates/architecture-approval.json` superseded per cross-gate semantics only by the
authorized operation). Downstream authority from the boundary invalidated by Core
(draft checkpoints/results stay on disk but unbound until fresh Draft post-r5 — Draft is
NOT regenerated this run; P15 overlay NOT implemented this run).

## Step 1 — Evidence acceptance (new content-addressed set)

- 104 cards carried byte-identical (hash-proven); 8 staged corrected cards
  (`staged-cards/`, canonical `validate_evidence_card` PASS already) admitted via the
  canonical acceptor (`accept_evidence_results` equivalent path with exact task/package basis).
- New `evidence-accepted.json` + `results/` set under `evidence/v2/accepted/<new-sha>/`;
  old sets retained (append-only). PARTIAL×5 preserved (VM-D077 stays PARTIAL).
- Expected: result_count 112; result-set old hash `33ec63cb…106f` → new hash (computed).

## Step 2 — Edition Views acceptance

- 104 views carried (deterministically unchanged); 8 views rebuilt from corrected cards
  (canonical `validate_edition_view` + `validate_edition_views_acceptance`).

## Step 3 — Materiality + Completeness

- Materiality ledger: 112 rows; dispositions carried; VM-D062/061/034/033/024/028/108/077
  rationales updated ONLY where corrected claims change the materiality basis (LLaVA
  topology correction may shift VM-O10/bridging rationale wording — ledger explicitly).
- Profile completeness: obligations VM-O01..VM-O16 carried; no new obligations.

## Step 4 — Candidate Matrix

- 112 rows; row identities preserved; `evidence_sha256` rebased ONLY for the 8 corrected
  tasks; `evidence_acceptance_sha256` basis rebased to the new set. Four-node P04 cap,
  SSV2-free texts, V1 lineage untouched.

## Step 5 — Selection

- No arbitrary change: 112 SELECTED expected (陈述; verify each disposition; diff explicitly
  if the LLaVA topology correction forces any semantic change — none anticipated).

## Step 6 — Architecture (fresh authority)

- 16-package skeleton preserved; P04 cap; P07A/B split; P11 three contracts; P14 four-pole;
  VM-D112 P09/P11 SUPPORTING; SS V1 lineage; P15 39-authority map (11 axes) preserved
  byte-identical as allowlist (NEVER add D112; NEVER weaken to 14).
- Fresh `architecture-v2.json` bytes (re-derived; expected semantic diff: NONE — basis-hash
  rebinding only; any genuine semantic diff explicitly recorded).
- Fresh `architecture-review-summary-v2.json` + `architecture-review-attention-v2.json`.

## Step 7 — checkpoints/state → ARCHITECTURE_ESTABLISHED, r5 PENDING

- Required checkpoints rebuilt via canonical stage validation
  (`survey_stage_validation_v2` stage-contract validations per stage, recorded as reviews).
- State advanced CANDIDATES_NORMALIZED → … → ARCHITECTURE_ESTABLISHED EXCLUSIVELY via
  `advance_with_checkpoint` (canonical path/value checks; history appended).
- r4 approval NEVER applied to the fresh Architecture. New surface prepared as
  Human Architecture Review r5 PENDING (review-index shows next revision 5, no r5 record,
  no decision). STOP. No Draft/TeX/PDF/validation.

## Handoff for post-r5 Draft revision (§12 deferred list)

MiniGPT-4/LLaVA/DINO/MAE prose sync (LLaVA S03 phrasing swap on corrected claim-4),
MMMU/MMBench decontamination, I-JEPA wording (canonical readback in ledger),
P15 39-authority materialization + repetition removal, POPE terminology, terminology
normalization, DreamerV3 depth (card sufficient as-is), Molmo 2 wording/currentness,
synthesis regeneration, ledgered deletions (scale catalogs, inventories, causal glosses,
triplications).
