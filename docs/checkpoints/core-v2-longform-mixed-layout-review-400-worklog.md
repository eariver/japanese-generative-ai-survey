# Core v2 LONGFORM mixed-layout review hardening — Issue #400

## Trigger

Human Publication Preview re-review of SP001 regenerated r2 exact PDF (13 pages, SHA-256 `590a53e11934ae25176050e5105b59a2bb09eda4b045e9b211b486e5be90ba2b`) found that ordinary narrative had regressed to full-width one-column even though `docs/special-layout-policy.md` requires mixed layout for normal Specials. The exact-PDF visual review had passed because the LONGFORM_SPECIAL review contract contained no profile-specific visual check.

## Scope

- add `LONGFORM_MIXED_LAYOUT` to the LONGFORM_SPECIAL visual review family;
- require explicit visual evidence for normal narrative column treatment, full-width wide/synthesis/Technical-Notes surfaces, and one-column References;
- keep layout assessment ChatGPT-owned rather than inferring visual quality from TeX tokens or page count;
- preserve the existing policy exception for a specific Human-approved Issue Architecture without permitting a Visual-review marker to self-authorize that exception;
- add direct negative regressions and update existing publication/Human-Gate chain fixtures;
- no permanent workflow, schema, lifecycle, Human Gate, edition-local, or renderer change in this maintenance candidate.

## Intended invariant

For a normal `LONGFORM_SPECIAL`, exact-PDF Visual review must explicitly record:

- `reader-layout:balanced-two-column-narrative`;
- `reader-layout:wide-surfaces-full-width`;
- `reader-layout:references-one-column`.

The default two-column narrative requirement may be replaced only when the Human-reviewed Architecture carries the machine-readable publication extension:

```json
{
  "publication_extensions": {
    "longform_layout": {
      "allow_nonstandard_narrative_columns": true
    }
  }
}
```

In that case Visual review must also record `reader-layout:architecture-approved-narrative-exception`. The evidence marker alone is insufficient. The exception is deliberately narrow: it does not bypass full-width wide-surface or one-column References review. This preserves `docs/special-layout-policy.md`, which makes mixed layout the normal Special identity while allowing a specific approved Issue Architecture to require otherwise.

SP001's current approved Architecture carries no such publication extension, so the Issue #400 full-width one-column narrative regression cannot pass this contract.

Weekly and other publication profiles remain unaffected. The change does not impose a deterministic TeX implementation such as global `twocolumn` or `multicols`; it requires the exact-PDF reviewer to state what was actually checked.

## Human Gate

This shared-Core maintenance must complete exact-head CI and the canonical seven-point fixed-head final audit before Human maintenance review. It must not be merged without explicit Human approval. SP001 remains paused after canonical Publication Preview r2 `REQUEST_CHANGES` rollback until this Core maintenance is approved and merged.

## Diagnostic regression history

- The first temporary targeted run failed before publication tests because the temporary transport had not installed `config/survey-production-v2-requirements.txt`; `pypdf` was missing. The transport was corrected rather than weakening the production parser.
- The corrected targeted run passed `test_survey_reader_fidelity_v2` and `test_survey_publication_v2`, proving the initial direct mixed-layout negative regression and publication-chain fixture.
- Diagnostic full Pipeline run #3510 (`33171970760`) then ran 722 tests and found 12 errors, all from the shared Human-Gate LONGFORM fixture omitting the newly required mixed-layout evidence. No production implementation failure was observed. The shared fixture was updated so Architecture/Publication round-trip tests exercise the new visual contract instead of bypassing it.
- The fixture-repair affected regression then ran the fidelity, publication, Human Gate, bridge Human Gate, and Human Gate audit-matrix suites: 49 tests in 341.109s, all PASS. Its temporary workflow/payload removed themselves before the repaired candidate commit.
- Head `782acabe91a30ab299b6a99abf69419b0c01b8b7` then received PR-triggered Core #1227 (`33172912918`) and Pipeline #3515 (`33172912960`) as `action_required` with zero jobs because that head was bot-authored. These runs are diagnostic/platform-state only and are not final CI evidence.

## Pre-freeze generality correction

Static review against `docs/special-layout-policy.md` found that an unconditional balanced-two-column requirement would overconstrain the existing policy clause allowing a specific approved Issue Architecture to require another layout. That finding invalidated the unconditional form before freeze.

The maintenance was therefore generalized to use Architecture-owned, machine-readable authority rather than natural-language exception parsing:

- default: `reader-layout:balanced-two-column-narrative` is required;
- Visual marker alone cannot self-authorize a narrative-column exception;
- only `publication_extensions.longform_layout.allow_nonstandard_narrative_columns=true` in the Human-reviewed Architecture enables the exception path;
- the exception path additionally requires `reader-layout:architecture-approved-narrative-exception` Visual evidence;
- `reader-layout:wide-surfaces-full-width` and `reader-layout:references-one-column` remain mandatory under the exception.

Direct regressions exercise all four cases: normal mixed-layout PASS, missing normal narrative marker FAIL, exception marker without Architecture authority FAIL, Architecture authority plus exception marker PASS, and attempted bypass of the wide-surface requirement FAIL.

Temporary generalization run `33173884092` / job `98857431279` applied this repair and reran the same affected five suites: **49 tests in 479.338s, all PASS**. The temporary workflow and patch script then removed themselves, producing diagnostic head `489cb1ecabcd6801c501662fa36479a10832edef` with no permanent Actions-surface addition.

## Final-candidate procedure

All heads and runs named above are diagnostic and non-final because later intended candidate-tree mutations occurred. This worklog synchronization is the final intended tree mutation before fixed-head qualification.

The resulting exact head must now:

1. pass exact-head `Survey Production Core v2 CI` and `Pipeline contract tests`;
2. pass a full PR-scope pre-freeze cross-check against unchanged `main` authority;
3. be frozen by exact commit/tree/base identity;
4. undergo Points 1–7 of `docs/survey-production-core-v2-final-audit-rule.md` from zero without candidate mutation;
5. receive a 7/7 result only outside the candidate tree.

Any finding requiring repository mutation invalidates the audit and restarts this sequence. PR #475 remains Draft/open/unmerged until explicit Human Core-maintenance approval. SP001 remains paused at its canonical Publication Preview r2 revision boundary.
