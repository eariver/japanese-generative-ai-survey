# Core v2 reader substantive fidelity maintenance — Issue #434

Date: 2026-08-27
Branch: `fix/core-v2-reader-substantive-fidelity-434`
Base reviewed `main`: `079dac9605e4cf55a239de6f03e37a93f756a918`

## Trigger

SP001 Publication Preview candidate `aa5b0665cf96546c88601883eac82819f1e428f1` was Human-reviewed under Issue #400 and remains revision-required. The cold-start candidate improved Publication Boundary leakage and restored mixed layout, but compressed the approved six-package `LONGFORM_SPECIAL` Architecture into a seven-page candidate while `LONGFORM_TECHNICAL_DEPTH` still passed. Issue #434 records this as a shared Architecture -> Publication substantive-fidelity defect.

## Maintenance scope

This branch changes shared Core only. It does not edit SP001 generated publication bytes.

Implemented so far:

- `scripts/survey_reader_fidelity_v2.py`
  - resolves Reader Manifest accountability locations to exact numbered TeX sections/subsections;
  - requires one numbered reader section per approved LONGFORM package;
  - requires must-cover requirements to map to substantive reader blocks inside their own package;
  - limits one block from standing in for more than two Architecture obligations;
  - requires package-level minimum substantive text and source diversity;
  - preserves a reader-visible synthesis/conclusion role for the final Architecture package;
  - hardens semantic review so package-by-package evidence is mandatory;
  - when actual pages are below two thirds of the soft Architecture target, requires an explicit exact `page-plan:actual/target` density/depth review and substantive justification.
- `scripts/survey_reader_publication_v2.py`
  - invokes the substantive-fidelity validator when building and revalidating Reader Manuscript authority;
  - invokes longform density/depth validation when building and revalidating publication review records.
- `tests/test_survey_reader_fidelity_v2.py`
  - direct regressions for substantive block mapping, collapsed topic-presence rejection, thin-block rejection, final synthesis role, severe below-target review, and WEEKLY non-applicability.
- `tests/test_survey_publication_v2.py`
  - updates publication-chain fixtures to use exact reader blocks and package-bound semantic-review evidence instead of abstract `main.tex:*` placeholders for LONGFORM.

## SP001 expected effect

The current SP001 Reader Manifest maps several package must-cover requirements to the same whole-section location. Under the new gate this cannot establish substantive fidelity. A regenerated candidate must provide distinct reader-facing subsection/section treatment, sufficient source-backed depth, and explicit final-synthesis role before Reader Manuscript / semantic review authority can pass.

## Remaining steps

1. Open maintenance PR against current `main` and run exact-head CI.
2. Repair any regressions until diagnostic CI is green.
3. Execute the repository Core v2 final-audit rule on one frozen maintenance SHA; any mutation invalidates prior audit results.
4. Human-review and merge the Core maintenance only after the required audit surface is complete.
5. Re-run SP001 from its canonical work branch through the trusted default-branch Core, regenerate Publication Candidate, perform exact PDF semantic/visual review, and return to Publication Preview Human Gate.
6. Do not Freeze/Release SP001 before explicit Human Publication Preview approval.
