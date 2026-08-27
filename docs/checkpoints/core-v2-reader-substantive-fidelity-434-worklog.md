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

`scripts/survey_reader_fidelity_v2.py` requires LONGFORM coverage claims to resolve to real, non-empty numbered TeX content blocks using exact locations such as:

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
- `tests/test_survey_publication_v2.py` and `tests/test_survey_human_gate_v2.py` exercise the integrated Publication Candidate and Human Gate round-trip paths with exact reader blocks and package-bound semantic review evidence.

## Human review of the first frozen candidate

The first frozen maintenance candidate was:

`b42c1f38e16a812bdd0925270de484a139d6d7cf`

It had exact-head green CI and a fresh 7/7 audit recorded outside the tree. PR review `5036108178` then identified three accepted-input counterexamples. That review **invalidated the freeze and superseded the old 7/7 result**; it must not be reused as approval evidence.

The three findings and repairs are:

1. **JSON-number `target_pages`** — canonical Architecture permits numeric values such as `18.0`, while the first implementation only applied the below-target review rule to Python `int`. The repaired fidelity validator accepts finite positive `int`/`float` values (excluding booleans), normalizes integral floats such as `18.0` to the canonical review marker `18`, and regression-tests `target_pages: 18.0` with a seven-page result.
2. **Exact PDF page-count authority** — the first implementation trusted caller-supplied `page_count`, so mutually consistent metadata could claim an 18-page result for a seven-page exact PDF. The repaired publication review derives page count deterministically from the exact repository PDF bytes, cross-checks the PDF page tree, rejects any asserted/recorded mismatch at both build and revalidation time, and passes only the derived count into longform density review. Publication and Human Gate fixtures now use inspectable Page-tree PDF bytes rather than text-only pseudo-PDFs. A direct mismatch regression proves that `asserted=18` cannot pass against an exact 12-page PDF.
3. **Canonical final-package ordering** — the first implementation used `packages[-1]`, even though Architecture finality is defined by maximum `drafting_order`. The repaired validator derives the unique final package from maximum canonical `drafting_order`, independent of JSON array position, and regression-tests reversed array order.

These are narrow contract repairs. They do not introduce a page quota, a new Human Gate, or an editorial-quality heuristic.

## SP001 expected effect

The current SP001 Reader Manifest at `aa5b0665...` already uses exact Section-level coverage locations, so deterministic traceability alone does not reject it. That is intentional: exact Section bytes exist.

Its current semantic review does **not** satisfy the repaired contract: the Architecture/depth checks use generic `reader-manuscript-v2.json :: architecture_coverage` / `main.tex :: Sections ...` evidence rather than explicit package-plus-exact-block review, and the 7-page result is below the approved soft 18-page target without an exact `page-plan:7/18` density disposition. The exact PDF-derived page-count rule additionally prevents that below-target condition from being bypassed through review metadata. Therefore the old candidate cannot be revalidated as a new acceptable LONGFORM candidate without regeneration/re-review.

A regenerated SP001 candidate must supply an exact accountability map and a fresh semantic review that actually assesses each package/block, final synthesis role, and any below-target density before Publication Candidate authority can pass.

## Diagnostic history

- Initial diagnostic Core CI on old head `1ac49d00...` exposed nine failures sharing one cause: the Human Gate fixture still generated LONGFORM reader source with no numbered sections / abstract locations. The production gate implementation itself compiled, and the new direct fidelity tests passed on that head.
- The Human Gate and Publication fixtures were migrated to exact reader locations and semantic package/block evidence.
- Frozen head `b42c1f38...` reached exact-head green CI and 7/7 audit, but PR review `5036108178` found the three accepted-input gaps above. Its audit is superseded.
- Post-review repairs migrate Publication/Human Gate PDF fixtures to deterministic page-tree authority and add direct regressions for float page targets, exact-PDF page-count mismatch, and array-order-vs-drafting-order final synthesis.
- Several intermediate heads are diagnostic only; none is final-audit authority.
- No Core merge has been performed.

## Remaining steps

1. Obtain green exact-head diagnostic `Survey Production Core v2 CI` and `Pipeline contract tests` for the post-review repair head.
2. Repair any remaining regressions before freezing a candidate.
3. Perform the pre-freeze full-PR scope/stale-authority cross-check required by `docs/survey-production-core-v2-final-audit-rule.md`.
4. Freeze one new maintenance SHA and execute all seven final-audit points from Point 1 on that exact unchanged SHA. The old `b42c1f38...` audit is not reusable.
5. Record any fresh 7/7 result outside the audited tree and present the candidate for Human Core-maintenance review; do not merge without explicit Human approval.
6. After approved Core repair is merged to `main`, resume SP001 through the canonical revision path, regenerate Publication Candidate, perform fresh exact-byte semantic/visual review, and return to Publication Preview Human Gate.
7. Do not Freeze/Release SP001 before explicit Human Publication Preview approval.
