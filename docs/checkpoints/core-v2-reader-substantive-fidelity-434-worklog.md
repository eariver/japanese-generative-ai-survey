# Core v2 reader substantive fidelity maintenance — Issue #434

Date: 2026-08-27
Branch: `fix/core-v2-reader-substantive-fidelity-434`
Base reviewed `main`: `079dac9605e4cf55a239de6f03e37a93f756a918`
Maintenance PR: `#473` — `Core v2: enforce reader substantive Architecture fidelity`

## Trigger

SP001 Publication Preview candidate `aa5b0665cf96546c88601883eac82819f1e428f1` was Human-reviewed under Issue #400 and remains revision-required. The cold-start candidate improved Publication Boundary leakage and restored mixed layout, but compressed the approved six-package `LONGFORM_SPECIAL` Architecture into a seven-page candidate while `LONGFORM_TECHNICAL_DEPTH` still passed. Issue #434 records this as a shared Architecture -> Publication substantive-fidelity defect.

## Maintenance scope

This branch changes shared Core only. It does not edit SP001 generated publication bytes.

## Responsibility split

The implementation follows the existing Reader Manifest authority: deterministic helpers protect exact identity and traceability; substantive/editorial adequacy remains ChatGPT-owned semantic review.

Accordingly, this repair does **not** make page targets into quotas and does not infer quality from fixed character counts, citation counts, source diversity, package-to-section ratios, or one-block-per-requirement rules.

### Deterministic Reader Manuscript traceability

`scripts/survey_reader_fidelity_v2.py` now requires LONGFORM coverage claims to resolve to real, non-empty numbered TeX content blocks using exact locations such as:

- `Section N — title`
- `Subsection N.M — title`

The same applies to `FINAL_SYNTHESIS`. Abstract locations such as `main.tex :: Sections 1–6` are not sufficient authority for a new LONGFORM Reader Manifest.

The deterministic layer only proves that the author-accountability map points at exact reader-facing bytes already bound by the Reader Manifest. It does not declare those bytes editorially sufficient.

### Semantic/editorial substantive fidelity

For LONGFORM `SEMANTIC_EDITORIAL` review:

- `ARCHITECTURE_CONTENT_FIDELITY` must explicitly bind every approved `package:<id>` and every exact Reader Manifest coverage block;
- `LONGFORM_TECHNICAL_DEPTH` must explicitly bind every approved package and every exact coverage block, preventing generic topic-presence review from standing in for package/content review;
- `FINAL_SYNTHESIS_QUALITY` must bind the final Architecture package, the exact `FINAL_SYNTHESIS` reader location, and `reader-role:final-synthesis`;
- when actual pages are below the soft Architecture `target_pages`, `LONGFORM_TECHNICAL_DEPTH` must additionally record the exact `page-plan:<actual>/<target>` observation and the explicit semantic disposition `density-review:below-target-substantive`.

This makes a below-target result reviewable rather than automatically invalid: ChatGPT may still judge a compact result substantive, but must do so consciously and against exact package/block evidence.

### Integration and regression coverage

- `scripts/survey_reader_publication_v2.py` validates exact LONGFORM traceability when Reader Manuscript authority is built/revalidated, then validates the package/block-bound semantic review when publication review records are built/revalidated.
- `tests/test_survey_reader_fidelity_v2.py` covers exact traceability, abstract/nonexistent/empty location rejection, non-overfit layout freedom, package/block semantic evidence, final-synthesis evidence, below-target density disposition, and WEEKLY non-applicability.
- `tests/test_survey_publication_v2.py` and `tests/test_survey_human_gate_v2.py` migrate LONGFORM fixtures from abstract `main.tex:*` locations to exact reader blocks and package-bound semantic review evidence.

## SP001 expected effect

The current SP001 Reader Manifest at `aa5b0665...` already uses exact Section-level coverage locations, so deterministic traceability alone does not reject it. That is intentional: exact Section bytes exist.

Its current semantic review does **not** satisfy the repaired contract: the Architecture/depth checks use generic `reader-manuscript-v2.json :: architecture_coverage` / `main.tex :: Sections ...` evidence rather than explicit package-plus-exact-block review, and the 7-page result is below the approved soft 18-page target without an exact `page-plan:7/18` density disposition. Therefore the old candidate cannot be revalidated as a new acceptable LONGFORM candidate under the repaired Core merely because required topics appear.

A regenerated SP001 candidate must supply an exact accountability map and a fresh semantic review that actually assesses each package/block, final synthesis role, and any below-target density before Publication Candidate authority can pass.

## Diagnostic history

- Initial diagnostic Core CI on old head `1ac49d00...` exposed nine failures sharing one cause: the Human Gate fixture still generated LONGFORM reader source with no numbered sections / abstract locations. The production gate implementation itself compiled, and the new direct fidelity tests passed on that head.
- The Human Gate and Publication fixtures have since been migrated to exact reader locations and semantic package/block evidence.
- Several intermediate heads were intentionally superseded while correcting the responsibility split; none is final-audit authority.
- No Core merge has been performed.

## Remaining steps

1. Obtain green exact-head diagnostic `Survey Production Core v2 CI` and `Pipeline contract tests` for PR #473.
2. Repair any remaining regressions before freezing a candidate.
3. Synchronize repository authority and perform the pre-freeze full-PR cross-check required by `docs/survey-production-core-v2-final-audit-rule.md`.
4. Freeze one maintenance SHA and execute all seven final-audit points from zero on that exact SHA. Any mutation invalidates the audit.
5. Present the 7/7 candidate for Human Core-maintenance review; do not merge without explicit Human approval.
6. After approved Core repair is merged to `main`, resume SP001 through the canonical revision path, regenerate Publication Candidate, perform fresh exact-byte semantic/visual review, and return to Publication Preview Human Gate.
7. Do not Freeze/Release SP001 before explicit Human Publication Preview approval.
