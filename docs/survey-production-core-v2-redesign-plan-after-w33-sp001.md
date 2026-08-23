# Survey Production Core v2 — Redesign Plan after W33 / SP001 Production Validation

Status: `REDESIGN IMPLEMENTED / FIXED-HEAD AUDIT PENDING`  
Established: 2026-08-23 JST  
Implementation synchronized: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Primary production evidence: Issues #400, #433, #434 and the W33/SP001 execution records  
Pre-implementation audit: `docs/survey-production-core-v2-redesign-preimplementation-audit.md`  
Implementation worklog: `docs/checkpoints/survey-production-core-v2-redesign-worklog.md`

## 1. Decision

The first real Core v2 production trials did not validate the merged pipeline.

- `2026-W33` reached Publication Preview but was rejected in Issue #433.
- `SP001` reached Publication Preview, was rejected in Issue #400, and a Human-directed 19-page salvage revision materially improved the artifact but still retained reader-facing production/editorial leakage.
- Issue #434 established the shared defect across `WEEKLY_MAGAZINE` and `LONGFORM_SPECIAL`: internal Architecture / Review / Selection / Evidence state could flow into reader-facing publication prose without an adequate semantic Publication Boundary.

Those trials remain failed/non-validating production evidence. They must not be rewritten as successful runs merely because the redesign has now been implemented.

The redesign objective is a smaller and more general Core in which stable Core/Profile/edition authority constrains ChatGPT reasoning while deterministic tooling protects only crisp invariants. The implementation must not become a W33/SP001-specific repair.

## 2. What the trials established

### 2.1 Machine PASS did not imply publication quality

SP001's rejected candidate and W33's rejected Preview demonstrated that deterministic and workflow-level PASS states could coexist with:

- inadequate longform or issue-level development;
- missing or weak reader-facing synthesis;
- internal Evidence/materiality/selection language in the publication;
- Architecture requirements being referenced rather than actually fulfilled;
- layout/profile regressions not adequately represented by machine checks.

The redesign therefore separates deterministic QA from ChatGPT semantic/editorial review and exact-PDF visual review.

### 2.2 The Publication Boundary had to become structural

Internal research/editorial artifacts are not reader manuscript authority. Screening, Selection, Evidence, Architecture rationale, Human-review rationale, internal IDs, obligations, package/coverage/promotion vocabulary and raw internal paths must not become publication prose merely because a reader-facing field is absent.

The implemented design introduces an explicit Reader Manuscript / reader-facing source boundary and fails closed when required reader content is missing.

### 2.3 Human-directed salvage is not cold-start validation

The improved SP001 salvage proved that the underlying research material was capable of supporting a better publication. It did not prove that the pre-redesign Core could produce that quality autonomously. The salvage depended on detailed Human criticism, shared renderer/style repair and later authority rebinding.

Future production acceptance must therefore be measured from a clean start with no in-run shared-Core repair.

### 2.4 Production sessions had become Core-maintenance sessions

The W33/SP001 trials blurred the difference between:

- `the production system worked`; and
- `the edition session repaired the production system until it worked`.

The implemented invariant is:

> **Production sessions repair editions; Core-maintenance sessions repair shared Core.**

A likely shared-Core defect is recorded under the edition execution record. A semantically safe edition-local workaround may be used without altering the shared contract; otherwise the production run blocks and Core repair proceeds separately.

### 2.5 GitHub Actions had become a production orchestrator

Actions were used for editorial stage control, Drafting/Synthesis, publication mutation, layout repair, candidate/state mutation, bot commits and execution-trigger PRs. This created operational coupling without adding independent editorial value.

The redesign adopts `docs/survey-production-core-v2-github-actions-policy.md` as a hard constraint:

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.**

### 2.6 Publication revision authority was not atomic

SP001 produced a concrete failure in which revised PDF bytes and old Quality/Candidate authority coexisted. The redesign therefore requires one exact Publication Candidate to bind the current Reader Manuscript, source, PDF and all QA/review authorities. Source/PDF drift invalidates downstream Candidate/Preview/Freeze identity.

### 2.7 Execution records were useful but inconsistent

W33 and SP001 both demonstrated the value of session provenance, but their logs were fragmented or became stale. The redesign standardizes edition-local execution records under `{source_root}/execution/`.

## 3. Implemented responsibility model

### 3.1 ChatGPT owns reasoning and publication authorship

ChatGPT owns:

- research strategy and gap closure;
- Screening/Evidence interpretation;
- materiality and Candidate Selection;
- Architecture;
- Drafting and Synthesis;
- reader-facing claim/limitation wording;
- Weekly Grok/X community synthesis;
- final `総括` or equivalent synthesis;
- prose quality, technical depth, repetition and coherence;
- publication-source authoring and layout/composition decisions;
- semantic/editorial review;
- exact rendered-PDF visual review and edition-local repair.

Helper scripts may support these tasks but do not substitute deterministic proxies for editorial judgment.

### 3.2 Repository scripts own narrow deterministic operations

Examples include:

- schema/path validation;
- hashing/provenance and exact authority binding;
- deterministic bibliography/identifier checks;
- known-token leakage lint;
- exact source/PDF/candidate accounting;
- reproducible transformation after editorial decisions are explicit;
- execution-record structure validation.

Scripts must not silently decide what material survives, how much technical detail a section receives or whether reader-facing explanation is adequate.

### 3.3 GitHub Actions owns independent/reproducible execution

The canonical redesign surface contains six workflows only:

1. `pipeline-contract-tests.yml`
2. `survey-production-v2-ci.yml`
3. `build-weekly-survey.yml`
4. `build-special-pdf.yml`
5. `survey-production-v2-export-publication-preview.yml`
6. `survey-production-v2-release.yml`

These cover CI/regression, reproducible build verification, exact-byte Preview transport and controlled release. Ordinary research/editorial/publication lifecycle stages are not workflow-dispatched; release is the only lifecycle stage dispatched to Actions.

## 4. Generality model — Core, Profile and edition authority remain orthogonal

The implemented model is:

```text
shared invariant Core
+ Research Profile constraints
+ Publication Profile constraints
+ edition/series planning authority
+ ChatGPT reasoning/editorial judgment
+ narrow deterministic helpers
+ independent CI/build/release verification
```

### 4.1 Shared Core

Shared Core owns only cross-profile invariants such as:

- lifecycle and the two normal Human Gates;
- source/Evidence/provenance integrity;
- internal-vs-reader-facing Publication Boundary;
- deterministic / semantic / visual QA separation;
- candidate revision invalidation and exact-byte authority;
- execution-record requirements;
- Production-vs-Core-maintenance responsibility boundary;
- Grok/X evidence role and transport discipline.

Shared Core must not encode W33/SP001 topic structure, edition-specific family names, fixed chapter counts or one issue's Architecture vocabulary.

### 4.2 Research Profiles

- `WEEKLY` owns rolling-window/current-week semantics, carry-over, Weekly community signal and issue-level synthesis.
- `RETROSPECTIVE_PERIOD` owns bounded-period reconstruction, coverage audit, chronology/lifecycle identity, normalization and period-scale synthesis.
- `THEMATIC` owns research-question closure, lineage/branch relationships, historical attribution and open-history/current-state boundaries.

### 4.3 Publication Profiles

- `WEEKLY_MAGAZINE` owns compact magazine publication semantics.
- `LONGFORM_SPECIAL` owns longform Special publication identity and profile-appropriate mixed-layout semantics.

Publication Profile does not replace Research Profile. Retrospective and Thematic Specials may both use `LONGFORM_SPECIAL` while retaining different research closure and synthesis requirements.

### 4.4 Edition and series authority

Monthly, half-year and annual guidance may add scale-specific chronology/compression rules without creating cadence-specific Core workflows. Generative AI Foundations remains a living series authority layered over `THEMATIC + LONGFORM_SPECIAL`, not a rigid generic machine series engine.

## 5. Implemented reader-facing Publication Boundary

The Core explicitly separates internal research/editorial/provenance material from reader-facing publication authority.

The Reader Manuscript binds:

- exact Production Profile;
- exact approved Architecture;
- exact reader-facing source/supporting files;
- mapping of Architecture `must_cover_requirements` to reader-facing locations;
- Profile-required reader obligations, including concluding synthesis and Weekly community movement where applicable.

Internal Draft/Profile/Evidence/Selection/Architecture fields are not legal fallback prose. Missing required reader-facing content fails closed to ChatGPT authoring.

## 6. Architecture fidelity means content fidelity

A must-cover requirement is not fulfilled because the publication mentions that Architecture requested it.

The required traceability is:

```text
must-cover requirement
-> accepted supporting Evidence / Observation
-> actual reader-facing section/block
-> ChatGPT fulfillment judgment
```

This is traceability, not a machine substitute for editorial review. Supporting/context Evidence may be expressed through narrative, chronology, Technical Notes, comparison, attribution or bibliography; one paragraph per Evidence record is not required.

## 7. Implemented quality model

Candidate readiness uses three distinct authorities.

### 7.1 Deterministic Quality Bundle

Machine-verifiable properties only, such as:

- schemas/invariants;
- exact bytes/hashes;
- citation/reference integrity;
- identifiers;
- reproducible build/preflight;
- known forbidden exact patterns;
- source/PDF/candidate identity.

Agent semantic/visual PASS rows cannot impersonate deterministic results.

### 7.2 ChatGPT semantic/editorial review

Required before Publication Preview and bound to exact reader source bytes. It covers:

- Publication Boundary;
- Architecture must-cover fulfillment;
- technical depth;
- source-class-appropriate claim boundaries;
- concluding synthesis quality;
- applicable Grok/X editorial disposition;
- repetition/generic fallback/production-language leakage;
- reader-facing bibliography surface;
- Profile-specific chronology/historical/period/thematic semantics.

Known-token lint remains defense-in-depth only.

### 7.3 ChatGPT visual review

Required against the exact rendered PDF intended for Human Preview. It covers layout identity, hierarchy, whitespace/page balance, tables/boxes/URLs, clipping/overlap/glyph problems and visually obvious content-thin pages.

## 8. Profile requirements preserved and strengthened

### 8.1 Every Weekly/Special

- final substantive `総括` or explicitly equivalent synthesis;
- no internal production-state leakage;
- Human-review rationale is applied to content/structure rather than serialized as rebuttal prose;
- page targets remain planning envelopes rather than padding quotas.

### 8.2 Weekly

- reader-facing `コミュニティの動き` is mandatory;
- Grok/X intake receives explicit editorial disposition;
- material signals are published or have an internal exclusion reason;
- a quiet week is an explicit finding rather than silent omission;
- carry-over / Watch / Late Breaking / why-this-issue semantics remain Profile-owned.

### 8.3 Retrospective Period

The redesign preserves bounded-period coverage audit, supplemental primary-source gap fill, chronology/lifecycle identity, period normalization and synthesis, including annual temporal-skew/trajectory rules where applicable. Later outcomes must not be back-projected into the historical period.

### 8.4 Thematic

The redesign preserves research-question closure, lineage/parallel-branch reasoning where relevant, historical attribution and hindsight boundaries, and topic-specific Architecture derived from Evidence rather than generic family templates.

### 8.5 Longform Special

Architecture-selected material must receive profile-appropriate longform treatment. Supporting Evidence need not map one-to-one to prose. Structured chronology/comparison/Technical Notes may be used where useful. Mixed-layout identity remains an editorial/profile concern, not an Actions repair loop.

### 8.6 Generative AI Foundations

Foundations remains:

```text
living series authority
+ THEMATIC research profile
+ LONGFORM_SPECIAL publication profile
+ per-volume Architecture
```

The living series memo may evolve as detailed research proceeds.

## 9. Atomic revision lifecycle

The implemented publication sequence is:

```text
ChatGPT authors/edits reader-facing source
-> exact reproducible PDF build
-> deterministic QA
-> ChatGPT semantic/editorial review
-> ChatGPT exact-PDF visual review
-> Publication Candidate finalization binds all exact authorities
-> PUBLICATION_PREVIEW reviews that exact candidate
-> Human approval authorizes deterministic Freeze
-> Release reuses the already reviewed exact bytes
```

Any source/PDF change invalidates downstream candidate/approval/freeze identity. There is no legal active Candidate for superseded PDF bytes.

## 10. Human Gate and repair discipline

Normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Manual Grok Drive task-file path/reference handoff is transport, not a Human approval Gate.

After Human rejection, edition-local editorial/prose/layout repair may continue autonomously. A shared-Core defect is recorded and returned to Core maintenance. Formal acceptance evidence is invalidated if a shared-Core defect is discovered and repaired inside the same production validation run.

## 11. GitHub Actions generality guardrail

Do not reintroduce cadence/topic-specific authoring workflows. Where a crisp Profile-specific CI check is justified:

- prefer parameterized/shared verification driven by Profile/config;
- keep editorial decisions in ChatGPT;
- retain Actions only when GitHub-side execution has concrete independent, reproducibility or security value;
- avoid bot-commit workflow chains and PR-as-execution-trigger patterns unless a genuine GitHub-side property requires them.

Actions reduction must not weaken reproducible build, exact candidate identity, Freeze/Release integrity, credential isolation or release reconciliation.

## 12. Production re-validation strategy after reviewed integration

Unit/contract regression is necessary but not sufficient. After the redesign candidate passes fixed-head audit, receives Human full-candidate review and is integrated into `main`, perform clean real production validation.

### 12.1 Real cold-start trials

At minimum:

1. one clean future Weekly profile trial with no in-run shared-Core changes;
2. one clean standalone `THEMATIC + LONGFORM_SPECIAL` trial using SP001 as the required regression case, with no in-run shared-Core changes;
3. one representative `RETROSPECTIVE_PERIOD` run/replay through the requested Human Gate;
4. one Foundations-guided volume/scenario through at least Architecture Review.

### 12.2 Structural/Profile compatibility

Also verify that:

- monthly, half-year and annual guidance remains expressible through the generic bounded Period Profile;
- chronology, coverage-audit, temporal-skew and synthesis semantics remain available without cadence-specific production workflows;
- standalone future Thematic work need not resemble SP001;
- no generic Core behavior keys off W33/SP001 or Foundations volume names/topics.

### 12.3 Acceptance evidence discipline

For every real trial:

- compare cold-start outputs against relevant historical failure modes;
- verify production did not create/merge shared Core repairs;
- verify Actions stayed within policy;
- verify execution records are complete;
- preserve any failed trial and rerun only after separate reviewed Core repair.

W33/SP001 historical trials remain failed evidence; redesign implementation does not retroactively convert them into PASS.

## 13. Implementation workstreams and disposition

The redesign was implemented as coherent workstreams rather than per-Issue patch workflows.

0. **Authority normalization — IMPLEMENTED**
   - Production/Core responsibility boundary normalized;
   - Grok task-path handoff normalized;
   - final-audit and bootstrap authority synchronized;
   - cross-profile generality retained.

1. **Responsibility / orchestration simplification — IMPLEMENTED**
   - ordinary lifecycle returned to ChatGPT + deterministic scripts;
   - Actions reduced to six mechanical/reproducible/security-relevant workflows;
   - release is the only workflow-dispatched lifecycle stage.

2. **Reader-facing publication boundary — IMPLEMENTED**
   - explicit Reader Manuscript authority;
   - no internal fallback;
   - exact Architecture/Profile/source traceability.

3. **Editorial fidelity / quality review — IMPLEMENTED**
   - must-cover fulfillment review;
   - Weekly community and concluding synthesis requirements;
   - separate semantic/editorial and exact-PDF visual review authorities.

4. **Publication / candidate atomicity — IMPLEMENTED**
   - exact source/PDF/QA/review binding;
   - candidate revision invalidation;
   - exact-byte Preview/Freeze/Release chain.

5. **Execution record standardization — IMPLEMENTED**
   - canonical `{source_root}/execution/` tree;
   - helper and regression coverage for index/session/review/defect structure.

6. **Regression / generality acceptance — PARTIALLY COMPLETE**
   - deterministic regressions for the redesigned boundaries and six-workflow topology are implemented;
   - cross-profile contracts remain covered by Core tests;
   - complete fixed-head six-point audit is pending;
   - real cold-start Weekly, standalone Thematic/Longform, representative Retrospective and Foundations-guided validation remain post-integration requirements.

## 14. Explicit non-goals

- Do not solve editorial quality by adding large numbers of Actions checks.
- Do not encode prose quality as arbitrary word/page quotas.
- Do not make all semantic judgment into JSON schemas.
- Do not replace one workflow-heavy design with cadence/topic-specific workflow proliferation.
- Do not require one publication paragraph per Evidence record.
- Do not force all reader-facing manuscripts into one universal content schema beyond the provenance/coverage manifest needed for the structural boundary.
- Do not preserve legacy workflow complexity solely for compatibility if it is not on the production hot path.
- Do not create a rigid Foundations machine series engine.
- Do not treat the salvaged SP001 revision as evidence that the redesigned pipeline is production-ready.

## 15. Immediate maintenance sequence

Before Human full-candidate review of PR #446:

```text
finish all intended candidate-tree changes
-> complete regression/CI repair
-> inspect the entire PR diff for accidental scope/compatibility regressions
-> synchronize the implementation worklog
-> freeze one exact candidate head SHA
-> run all six final-audit points from zero on that unchanged SHA
-> if any audit finding requires a tree change, invalidate the audit and restart from a new SHA
-> present only the unchanged passing SHA for Human full-candidate review
```
