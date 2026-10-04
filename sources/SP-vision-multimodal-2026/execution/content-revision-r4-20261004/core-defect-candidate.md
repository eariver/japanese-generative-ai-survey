# Deferred shared-Core maintenance candidate (execution-local record; NOT fixed this run)

Title: `mixed-placement synthesis package cannot consume Architecture-authorized
cross-package Evidence under current frozen Draft validator`

## Observation

Approved Architecture `sources/SP-vision-multimodal-2026/architecture-v2.json`
(`71cb47989f328ed002f5db561345c7031d3360e6e4d7e0b0ee8d5f53d5975f72`) authorizes P15,
via root `publication_extensions.p15_cross_package_synthesis_map` (11 axes, 39 Discovery IDs),
to consume already-selected Evidence from other packages as synthesis authority
(`CROSS_PACKAGE_SYNTHESIS_REFERENCE` semantics; no new candidates, no destination change).

Frozen `scripts/survey_drafting_v2.py` cross-package compatibility only supports a package
with NO direct PRIMARY/SUPPORTING candidates and exactly one final synthesis package
(`_cross_package_reference_ids` returns `[]` when `_direct_candidate_ids` is non-empty).
P15 HAS its own 14 candidates, so:

- `run_drafting_synthesis_v2_interactive._refs` raises
  `Discovery ID must resolve exactly once inside package P15` for any map Discovery ID
  whose candidate lives in another package;
- frozen `validate_draft_result` (via `_card_ref_index` built ONLY from canonical
  `draft-package.json:evidence_inputs`) rejects any such ref as
  `references Evidence outside Draft Package or unknown stable ID` (64 errors on the
  revised P15 result, recorded in `overlay-validation-result.json`);
- frozen `build_synthesis_input` re-validates with the same frozen result validator and
  therefore cannot assemble synthesis input for a mixed-placement synthesis package.

## Edition-local disposition (this run only; shared Core read-only)

- Overlay authority `p15-cross-package-synthesis-authority.json` (49 entries / 39 unique IDs,
  all mechanically derived from current Matrix/Selection/Acceptance/Cards).
- P15-only compatibility validator `validate_p15_overlay.py` (union authority, same
  schema/attribution/subject rules; 0 errors on revised P15).
- Overlay-aware synthesis-input builder inside `regenerate_content_revision.py`
  (identical output schema; frozen-canonical for 15 packages + package-level for P15).
- Truthful reporting: `15/16 canonical Draft validation PASS` +
  `P15 edition-local cross-package compatibility validation PASS`; the generic Core
  rejection is recorded as a known compatibility boundary, never as canonical PASS.

## Request for separate Core maintenance (out of scope for this edition run)

A future reviewed Core change could teach the frozen validator a `mixed-placement synthesis`
mode: when Architecture defines an explicit cross-package synthesis map for a package that
also owns direct candidates, result refs resolving through that allowlist (SELECTED +
accepted bytes verified, `CROSS_PACKAGE_SYNTHESIS_REFERENCE` role, no destination mutation)
should validate. Shared `scripts/` + Core docs/main are UNCHANGED by this run.
