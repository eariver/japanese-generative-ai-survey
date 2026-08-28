# Core v2 LONGFORM mixed-layout review hardening — Issue #400

## Trigger

Human Publication Preview re-review of SP001 regenerated r2 exact PDF (13 pages, SHA-256 `590a53e11934ae25176050e5105b59a2bb09eda4b045e9b211b486e5be90ba2b`) found that ordinary narrative had regressed to full-width one-column even though `docs/special-layout-policy.md` requires mixed layout for normal Specials. The exact-PDF visual review had passed because the LONGFORM_SPECIAL review contract contained no profile-specific visual check.

## Scope

- add `LONGFORM_MIXED_LAYOUT` to the LONGFORM_SPECIAL visual review family;
- require explicit visual evidence for balanced two-column normal narrative, full-width wide/synthesis/Technical-Notes surfaces, and one-column References;
- keep layout assessment ChatGPT-owned rather than inferring visual quality from TeX tokens or page count;
- add direct negative regression and update existing publication-chain fixtures;
- no workflow, schema, lifecycle, Human Gate, edition-local, or renderer change in this maintenance candidate.

## Intended invariant

An exact-PDF visual review for `LONGFORM_SPECIAL` cannot be recorded as valid unless it explicitly states that the reviewer checked all three stable mixed-layout surfaces. Weekly and other publication profiles remain unaffected. Architecture-specific exceptions remain Human/editorial concerns; this change does not impose a deterministic TeX implementation such as global `twocolumn` or `multicols`.

## Human Gate

This shared-Core maintenance must complete exact-head CI and the canonical seven-point final audit before Human maintenance review. It must not be merged without explicit Human approval. SP001 remains paused after canonical Publication Preview r2 `REQUEST_CHANGES` rollback until this Core maintenance is approved and merged.

## Diagnostic regression history

- The first temporary targeted run failed before publication tests because the temporary transport had not installed `config/survey-production-v2-requirements.txt`; `pypdf` was missing. The transport was corrected rather than weakening the production parser.
- The corrected targeted run passed `test_survey_reader_fidelity_v2` and `test_survey_publication_v2`, proving the new direct mixed-layout negative regression and publication-chain fixture.
- Diagnostic full Pipeline run #3510 (`33171970760`) then ran 722 tests and found 12 errors, all from the shared Human-Gate LONGFORM fixture omitting the newly required mixed-layout evidence. No production implementation failure was observed. The shared fixture is updated in this candidate so Architecture/Publication round-trip tests exercise the new visual contract instead of bypassing it.

The diagnostic heads/runs above are not final audit evidence because this fixture repair mutates the candidate tree.
