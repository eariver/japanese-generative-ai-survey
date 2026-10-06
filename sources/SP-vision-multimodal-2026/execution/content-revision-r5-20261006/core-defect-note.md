# Edition-local Core-maintenance candidate (NOT fixed in this run)

Title: `mixed-placement synthesis packages cannot consume Architecture-authorized
cross-package Evidence under the frozen Draft validator`.

- Frozen `survey_drafting_v2._refs` / `_card_ref_index` resolve Evidence refs only
  inside a package's own `draft-package.json:evidence_inputs`.
- Frozen `validate_self_contained_draft_package` requires exactly one Evidence input
  per Architecture candidate placement, so the package cannot be extended either.
- Approved Architecture authorizes cross-package synthesis consumption
  (`publication_extensions.p15_cross_package_synthesis_map` for P15;
  `must_cover_requirements`-named authorities for P06/P10/P11), but the frozen
  validator rejects all such refs as
  `references Evidence outside Draft Package or unknown stable ID`.
- This run's compatibility (same class as content-revision-r4, extended from P15-only
  to multi-consumer P06/P10/P11/P15): canonical packages byte-identical +
  `cross-package-synthesis-authority.json` (Matrix→SELECTED→Acceptance→exact Card
  bytes, SHA-verified, 30 entries / 29 unique) + `validate_overlay.py`
  (frozen-identical schema/attribution/subject/duplicate/must_cover/boundary checks
  over the union index + allowlist/SELECTED/bytes enforcement) + overlay-aware
  synthesis builder. Frozen generic rejection recorded (`regen-report.json`:
  81 errors), not hidden.
- Shared roots untouched (`AGENTS.md`, `config/`, `schemas/`, `scripts/`,
  `.github/workflows/`, `docs/survey-production-core-v2-*.md`).
- Production repaired the edition; Core repair (if ever approved) happens separately
  with its own review.
