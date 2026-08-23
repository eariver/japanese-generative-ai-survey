# Survey Production Core v2 — Redesign Plan after W33 / SP001 Production Validation

Status: `REDESIGN REQUIRED / IMPLEMENTATION NOT STARTED`  
Established: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Primary production evidence: Issues #400, #433, #434 and the W33/SP001 execution records

## 1. Decision

The first real Core v2 production trials did not validate the merged pipeline.

- `2026-W33` reached Publication Preview but was rejected in Issue #433.
- `SP001` reached Publication Preview, was rejected in Issue #400, and a 19-page Human-directed revision substantially improved the artifact but still retained reader-facing production/editorial leakage.
- Issue #434 demonstrates that the central failure is shared across `WEEKLY_MAGAZINE` and `LONGFORM_SPECIAL`: internal Architecture / Review / Selection / Evidence state can flow into reader-facing publication prose without an adequate semantic publication boundary.

Both trials are therefore evidence for redesign, not successful Core v2 acceptance runs. The current W33/SP001 attempts must not be used to claim cold-start production validity. After redesign, both profiles require clean re-validation; SP001 should be rerun so the rejected 11-page version, Human-directed 19-page salvage version, and redesigned cold-start version can be compared.

This plan consolidates and supersedes the earlier assumption that W33/SP001 should continue accumulating incremental Core repairs while still serving as validation runs.

## 2. What the trials established

### 2.1 Machine PASS did not imply publication quality

SP001's rejected 11-page candidate reached `READY_FOR_PUBLICATION_PREVIEW` after Core deterministic and semantic quality checks passed. It nevertheless had:

- severe LONGFORM_SPECIAL underdevelopment;
- mixed-layout regression;
- missing reader-facing synthesis / Technical Notes depth;
- internal Evidence / materiality / verification language in the PDF.

W33 likewise reached `RELEASE_CANDIDATE` with machine checkpoints through validation marked passed, while the 6-page Preview still exposed internal Architecture / Screening / Evidence language and underfulfilled Architecture must-cover content.

The quality model therefore over-credited properties that were machine-checkable and underrepresented properties that require editorial judgment.

### 2.2 The Publication Boundary is structurally missing

W33 provides a direct example:

- internal `profile_payload.current_interpretation` contains review-reactive language;
- `carry_over_summary` contains `HOLD_OUT`, `Screening`, and `DROP` production state;
- `publication_payload` is empty;
- publication assembly still produced reader-facing prose by falling back to internal fields.

SP001 showed the same defect with different vocabulary (`Verify ...`, Evidence pass notes, Evidence IDs, `本 package`, selection/coverage language).

The redesign must make internal editorial/provenance artifacts non-renderable by default. Reader-facing publication content must exist as a distinct artifact/surface and must not silently fall back to internal fields.

### 2.3 Human-directed salvage is not cold-start validation

The 19-page SP001 revision proves that the selected Evidence and Architecture contained enough material to produce a substantially better Special after detailed Human criticism. It does **not** prove that Core v2 could produce that quality autonomously.

The salvage required, among other things:

- generic renderer hardening merged to `main` and reintegrated into the edition branch;
- shared style changes for longform full-width/multicolumn behavior;
- workflow rerouting around GitHub bot-trigger limitations;
- a second authority repair because revised PDF bytes initially did not update the Quality Regression Bundle and Publication Candidate;
- detailed Human identification of remaining semantic leakage after deterministic reader-surface checks reported no findings.

A future acceptance run must therefore be evaluated from a clean start without in-run shared-Core repair.

### 2.4 Production sessions became Core-maintenance/debug sessions

SP001's Architecture-stage worklog records generic Core control workflow creation/repair while the edition was being compiled. Its Publication-stage log records additional generic renderer/style changes to `main`, then reintegration into the work branch.

W33 similarly created repeated execution-only PRs/rebuild loops and used pending generic Core repair logic during the production run.

This destroys the distinction between:

- `the pipeline worked`, and
- `the production session repaired the pipeline until it worked`.

The rule remains:

> **Production sessions repair editions; Core-maintenance sessions repair shared Core.**

If a shared Core defect blocks correct production, record it and stop or use only a semantically safe edition-local workaround. Do not author a generic Core repair from the edition session.

### 2.5 GitHub Actions became a production orchestrator rather than an independent verifier

The trials used Actions for stage adoption, Drafting/Synthesis generation, semantic publication assembly, publication mutation, quality-bundle creation, candidate/state mutation, bot commits, export/rebuild transport, and release-candidate authority handling.

This created concrete operational failures:

- write-capable workflow chaining stopped when a previous commit was authored by `github-actions[bot]`;
- temporary PRs were needed primarily as execution triggers;
- source/PDF revision and candidate authority refresh became separate operations;
- pipeline mechanics consumed significant production effort unrelated to researching/editing the issue.

The existing `docs/survey-production-core-v2-github-actions-policy.md` is adopted as a redesign constraint: Actions should be retained only where Actions execution itself has a clear benefit or the task is genuinely mechanical and non-editorial.

### 2.6 Revision authority is not atomic

After the successful SP001 19-page rebuild, the repository contained:

- new PDF/preflight bytes for the 19-page revision;
- old Quality Regression Bundle / Publication Candidate authority still bound to the superseded 11-page PDF.

A separate repair PR was required to rebind the Human Gate input.

A Publication revision must invalidate and recreate the complete candidate authority atomically. A state in which the visible PDF and candidate manifest refer to different bytes must be structurally impossible or fail closed immediately.

### 2.7 Existing execution records are useful but inconsistent

W33 produced a long issue-specific worklog plus distributed state/orchestration artifacts. The worklog header became stale relative to later lifecycle progress.

SP001 produced multiple date/session-specific checkpoint files with valuable detail, but the records are fragmented and use ad-hoc naming.

The next flow must standardize where the production narrative is stored, how sessions append to it, and how much detail is required. See `docs/survey-production-core-v2-execution-record-policy.md`.

## 3. Target responsibility model

### 3.1 ChatGPT owns reasoning and publication authorship

ChatGPT is responsible for:

- research strategy and gap closure;
- Screening / Evidence interpretation;
- materiality and Candidate Selection;
- Architecture;
- Drafting and Synthesis;
- reader-facing claim/limitation wording;
- Weekly community-movement synthesis from Grok/X;
- final `総括`;
- prose quality, depth, repetition and coherence;
- publication-source authoring;
- layout/composition decisions;
- semantic review of the reader-facing candidate;
- rendered-PDF visual review and editorial/layout repair.

Helper scripts may support these tasks, but may not substitute a generic rule for editorial judgment.

### 3.2 Repository scripts own narrow deterministic operations

Examples:

- schema/path validation;
- hashing and provenance;
- exact source-to-artifact accounting;
- deterministic bibliography/identifier checks;
- known-token leakage lint;
- exact-byte candidate manifest generation;
- reproducible transformation only after editorial decisions are explicit.

Scripts must not silently choose what content survives, how much technical detail a chapter receives, or whether a reader-facing explanation is editorially adequate.

### 3.3 GitHub Actions owns independent/reproducible execution

Examples:

- CI/regression tests;
- schema/contract verification;
- reproducible TeX/PDF build under a pinned environment;
- deterministic compiler/preflight checks;
- independent exact-byte verification;
- freeze/release integrity and controlled publication of already-approved bytes.

Actions should normally report PASS/FAIL and artifacts. They should not be the authoring/mutation loop for prose, synthesis, layout repair, or semantic quality.

## 4. Redesigned publication boundary

The Core must explicitly separate at least these layers.

### Internal research/editorial/provenance layer

Repository-only material such as:

- Candidate/Screening/Evidence disposition;
- Architecture rationale;
- Human Review rationale and rejected alternatives;
- internal Evidence IDs;
- materiality/status enums;
- obligation/TODO language;
- raw Core contract terms;
- internal source paths and processing state.

These fields are **not legal reader-facing inputs**.

### Reader-facing manuscript layer

A distinct, explicitly authored artifact must contain publication-ready content such as:

- article/section thesis;
- actual technical narrative;
- reader-facing claim boundaries;
- source-specific limitations;
- chronology/comparison/synthesis;
- Weekly community observations;
- concluding synthesis;
- reader-facing bibliography metadata.

Publication assembly may consume this layer plus publication metadata. It must not fall back to internal Architecture/Profile/Evidence text when a reader-facing field is missing.

If required reader-facing content is absent, publication assembly fails closed and returns control to ChatGPT authoring.

## 5. Architecture fidelity must mean content fidelity

A must-cover requirement is not fulfilled because the manuscript says that Architecture requires it.

For each Architecture package, the production session must perform a lightweight coverage review:

```text
must-cover requirement
-> supporting accepted Evidence / Observation
-> reader-facing section/block that actually explains it
-> ChatGPT fulfillment judgment
```

This mapping is traceability, not a machine substitute for editorial review.

Examples of unacceptable fulfillment:

- `承認済みArchitectureはXを観察軸としている`
- `このpackageではYをcoverする`

Examples of actual fulfillment:

- reader-facing prose explains the observed X/community movement;
- the Serving feature explains concrete release-level changes in each selected project;
- a longform family chapter explains version-to-version transitions and their technical significance.

## 6. Quality model: separate deterministic, semantic, and visual review

The future candidate should require three different classes of evidence.

### Deterministic QA

Machine-verifiable only:

- schema/invariants;
- exact bytes/hashes;
- citations/references;
- required identifiers;
- build/preflight;
- known forbidden exact tokens/patterns;
- candidate/source/PDF identity.

### ChatGPT semantic/editorial QA

Required before Publication Preview:

- internal-vs-reader boundary review;
- Architecture must-cover content fulfillment;
- technical depth appropriate to `WEEKLY_MAGAZINE` / `LONGFORM_SPECIAL`;
- source-class-appropriate Claim Boundary wording;
- `総括` quality;
- Weekly Grok/X community disposition and published synthesis;
- repetition / generic fallback / production-language review;
- reader-facing bibliography review.

Known-token lint is only defense-in-depth. It cannot replace this review: SP001's 19-page revision passed deterministic leakage checks while Human Review still found Evidence IDs and production-selection vocabulary.

### ChatGPT visual QA

Review the exact PDF intended for Human Preview:

- all pages rendered/inspected;
- layout identity appropriate to profile;
- whitespace/page balance;
- hierarchy/scanability;
- tables/boxes/URLs;
- clipping/overlap/glyphs;
- visually obvious content-thin pages.

Actions may build the exact PDF; ChatGPT performs the editorial/visual judgment.

## 7. Profile requirements strengthened from the trials

### All Weekly and Special editions

- final substantive reader-facing `総括` (or explicitly equivalent heading) is required;
- internal production metadata must not be published;
- Human-review rationale changes the structure/content requirements, not the prose by being serialized as a rebuttal to a rejected draft;
- page targets remain soft; depth is judged against must-cover content, not page padding.

### Weekly

- a reader-facing `コミュニティの動き` component is mandatory every issue;
- completed Grok/X intake must be explicitly editorially dispositioned;
- material community signals are published or have an internal exclusion reason;
- a quiet week is represented as an explicit finding rather than omission.

### Longform Special

- selected Evidence must be developed into longform technical narrative, not compressed into Architecture-summary prose;
- profile-appropriate structured synthesis/chronology/comparison/Technical Notes must be used when they materially improve reader understanding;
- Special mixed-layout identity must be preserved, but layout choices remain editorial decisions assisted by policy/templates rather than Actions-authored repair loops.

## 8. Revision lifecycle must be atomic

Any Publication Candidate revision invalidates all downstream authority bound to the superseded source/PDF.

Target operation:

```text
ChatGPT edits reader-facing manuscript / publication source
-> exact reproducible PDF build
-> deterministic QA
-> ChatGPT semantic QA
-> ChatGPT visual QA
-> one candidate-finalization operation creates/rebinds:
     validated source identity
     exact PDF identity
     deterministic QA references
     semantic review reference
     visual review reference
     Publication Candidate
-> only this complete candidate may be presented at PUBLICATION_PREVIEW
```

There must be no legal state where a new preview PDF coexists with a still-active candidate manifest for old bytes.

## 9. Human Gate and repair discipline

Normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. `PUBLICATION_PREVIEW`

Manual Grok Drive task-file handoff remains an operational transport boundary, not a Human approval gate.

After a Human Gate rejection:

- edition-local editorial/prose/layout repair may continue autonomously;
- shared Core defects are recorded and returned to Core maintenance rather than repaired inside the edition run;
- if a shared defect prevents a semantically valid candidate, terminate/pause the edition at a recorded Core dependency;
- after Core redesign/repair, restart from the earliest boundary whose semantics may have been affected; do not pretend the old failed path validates the new Core.

## 10. Core repair / production acceptance strategy

Do not validate the redesign only with unit/contract fixtures.

After implementation and Core CI:

1. run a clean Weekly profile trial from current `main` with no in-run Core changes;
2. run a clean LONGFORM_SPECIAL trial (SP001 is the required regression case) with no in-run Core changes;
3. compare cold-start outputs against #433 and #400 failure modes;
4. verify that production sessions did not create/merge shared Core workflow/script/schema/style repairs;
5. verify that Actions stayed within the adopted Actions policy;
6. verify execution records are complete under the new record policy;
7. only then consider the Core production repair validated.

If a trial uncovers a shared Core defect, preserve the trial as failed evidence, repair Core separately, and restart the affected acceptance run cleanly.

## 11. Implementation workstreams

The implementation pass should be organized as a small number of coherent workstreams rather than per-Issue patch workflows.

1. **Responsibility / orchestration simplification**
   - Production vs Core-maintenance boundary
   - remove PR-as-execution-trigger patterns where they add no value
   - Actions workflow classification and reduction

2. **Reader-facing publication boundary**
   - explicit reader manuscript/publication payload
   - no internal fallback
   - source-class-aware claim boundaries
   - reader-facing bibliography transform

3. **Editorial fidelity / quality review**
   - must-cover content review
   - Weekly community requirement
   - concluding synthesis requirement
   - longform depth expectations
   - semantic/editorial review artifact

4. **Publication / candidate atomicity**
   - reproducible build
   - deterministic QA
   - exact candidate finalization/revision invalidation

5. **Execution record standardization**
   - edition-local log folder
   - rolling index and session logs
   - defect/deviation records
   - concise logging limits

6. **Regression and cold-start acceptance**
   - #400 / #433 / #434 fixtures where deterministic
   - Weekly and Longform real production reruns

## 12. Explicit non-goals

- Do not solve editorial quality by adding large numbers of new Actions checks.
- Do not encode prose quality as arbitrary word/page quotas.
- Do not make all semantic judgment into JSON schemas.
- Do not preserve legacy workflow complexity solely for compatibility if it is not on the new production hot path.
- Do not treat the salvaged SP001 revision as evidence that the current pipeline is production-ready.
