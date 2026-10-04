# P15 mixed-placement cross-package synthesis compatibility — design (edition-local)

Status: edition-local compatibility for TS-003 this run only. NOT a shared-Core change.
Shared roots (`scripts/`, `config/`, `schemas/`, `.github/workflows/`,
`docs/survey-production-core-v2-*.md`) are read-only this run.

## Problem

Approved Architecture root `publication_extensions.p15_cross_package_synthesis_map`
authorizes P15 to consume already-selected Evidence from other packages as synthesis
authority. But frozen `survey_drafting_v2.py` cross-package compatibility only handles a
package with NO direct PRIMARY/SUPPORTING candidates and exactly one final synthesis
package. P15 HAS its own 14 candidates (1 PRIMARY VM-D110 + 13 SUPPORTING reuse), so the
frozen path returns `[]` for cross refs and the frozen `validate_draft_result` (via
`_card_ref_index` built ONLY from canonical `draft-package.json:evidence_inputs`) rejects
any P15 result ref outside those 14 inputs as
`references Evidence outside Draft Package or unknown stable ID`, while
`run_drafting_synthesis_v2_interactive._refs` raises
`Discovery ID must resolve exactly once inside package P15` for overlay Discovery IDs.

## Decision

- Keep canonical P15 `draft-package.json` byte-identical (14 inputs; SHA binding preserved).
- P15 `draft-result.json evidence_refs` may reference the UNION of:
  (a) canonical P15 inputs, (b) overlay-allowlisted Evidence (map-only, SELECTED, accepted
  bytes verified).
- Cross-package use role = `CROSS_PACKAGE_SYNTHESIS_REFERENCE` (Draft-time synthesis only;
  no Selection/Architecture destination change; P12 etc. NOT added to supporting_candidate_ids).
- Result schema unchanged; attribution rules unchanged; subject binding verified to card bytes.

## Overlay authority construction (deterministic)

For each map axis → each Discovery ID:
Candidate Matrix row (candidate_id, evidence_task_id, evidence_sha256) →
Selection disposition (must be SELECTED) →
Evidence Acceptance result (task, sha, filename) → exact accepted Card file bytes
(sha256 verified) → card subject IDs (claims/metrics/limitations/events subject_id set).
Canonical home package = Architecture package (non-P15 preferred; dual P15-reuse noted)
whose PRIMARY/SUPPORTING lists the candidate. Plus global SHAs: Architecture file,
approval file, Matrix file, Acceptance file.

Script: `build_overlay_authority.py` (read-only inputs, writes only this dir artifact).
Artifact: `p15-cross-package-synthesis-authority.json`.

## P15 result generation with overlay

`regenerate_content_revision.py`:
- Phase 1: canonical `derive_draft_package` for all 16 (packages byte-identical).
- Phase 2: for P01–P14 + synthesis: identical to canonical runner (`_draft_result` +
  `validate_draft_result`).
- For P15: custom `_p15_refs_with_overlay(package, overlay, discovery_ids, mode)`:
  canonical IDs resolve via package inputs; overlay IDs resolve via overlay cards
  (mode CLAIMS/LIMITATIONS same row expansion as canonical `_ref_rows`); dedup; empty→error;
  attribution via union index (same `_attribution` logic over union classes).
- Validation: 15 packages canonical `validate_draft_result` must PASS; P15 validated by
  `validate_p15_overlay.validate_p15_result` (union index + allowlist/SELECTED/unknown/
  subject/duplicate/attribution checks + schema/basis/package-binding checks identical to
  frozen validator). Also run frozen `validate_draft_result` on P15 to record the EXPECTED
  generic-validator rejection as known boundary evidence (not hidden).

## Deferred Core maintenance candidate (not fixed now)

`mixed-placement synthesis package cannot consume Architecture-authorized cross-package
Evidence under current frozen Draft validator` — recorded in `defects/` execution-local
note + final report. Shared Core implementation/summary/main unchanged this run.
