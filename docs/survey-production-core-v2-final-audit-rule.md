# Survey Production Core v2 — post-completion final audit rule

Status: `CANONICAL REDESIGN-CANDIDATE FINAL AUDIT RULE / OPERATOR-BRIDGE MAINTENANCE SYNCHRONIZED / READY FOR FIXED-HEAD EXECUTION`  
Established: 2026-08-22 JST  
Redesign alignment: 2026-08-23 JST  
Operator-bridge maintenance synchronization: 2026-08-23 JST  
Related audit: `docs/survey-production-core-v2-redesign-preimplementation-audit.md`

## 1. Principle

A full-candidate audit is meaningful only after implementation, repair, regression, documentation and review-package synchronization are complete.

Therefore the mandatory order is:

```text
finish every intended candidate change
-> finish regression/CI repair
-> synchronize repository-owned authority/docs/findings/Repair Set
-> freeze one candidate branch head SHA
-> run the complete six-point acceptance audit from zero on that exact SHA
-> if and only if all six pass without changing the candidate, present that exact SHA for Human full-candidate review
```

A partial audit performed while the candidate is still changing is diagnostic evidence only. It is never final approval evidence.

This fixed-head audit is the **Core change-management boundary before Human review**. It establishes that the redesign candidate is coherent, regression-covered, cross-profile-capable by contract/structural evidence, and safe to present as one immutable candidate.

It does **not** retroactively convert W33/SP001 into successful production trials, and it does not replace the clean real-production re-validation required after the redesigned Core is reviewed/integrated into `main`.

## 2. Six acceptance points

Every final audit evaluates all six points in this priority order:

1. **Weekly viability** — a normal future Weekly edition is supported through the requested Human Gate without edition-specific rescue architecture: required Grok/X Source Intake, exact Google Drive task-file path handoff, returned-result import, mandatory Weekly community treatment, Reader Manuscript/QA/Candidate boundaries, and no permission for in-run shared-Core repair are all present and mutually consistent.
2. **Special viability** — the redesigned Core remains structurally and executably viable for configured `RETROSPECTIVE_PERIOD`, standalone `THEMATIC`, `LONGFORM_SPECIAL`, SP-001–003-style work, and Generative AI Foundations guided-series work. Evidence must cover bounded-period cold-start Profile materialization from existing configured-period authority, standalone Thematic/Longform publication, and the Foundations living-series boundary rather than inferring all Special viability from SP001 alone. One Retrospective adapter must cover monthly/half-year/annual configured periods without becoming three editorial engines.
3. **Generality** — the Core/Profile design is not overfit to W33/W34/SP001–003, one cadence, one topic taxonomy, or one publication shape. Shared Core, Research Profile, Publication Profile and edition/series authority remain orthogonal. Later Weekly issues and previously unplanned Specials can use generic Profile/planning authority without new authoring workflows.
4. **Historical and clarified requirement recurrence prevention** — known Human Review defect families and later clarified requirements have an appropriate owner: narrow deterministic protection for crisp invariants, ChatGPT research/editorial/visual review for semantic judgment, Human review at the two normal Gates, or explicit legacy-only disposition. Publication Boundary defects from #400/#433/#434 are included here.
5. **Control proportionality** — after 1–4 are satisfied, routine work is not burdened with unnecessary Human Gates, workflow ceremony, profile-specific authoring workflows, or validators that pretend to replace qualitative judgment. GitHub Actions satisfy the adopted Actions responsibility policy.
6. **Autonomous progression / stop discipline** — after the user supplies the target and requested stopping Gate, ChatGPT proceeds through ordinary edition-local research/editorial work and transient retries without repeatedly stopping for confirmation. A production session may stop only for an actual normal Human Gate, a genuine Owner-level Exception Gate, the permitted manual Grok task-file path handoff, or a recorded shared-Core defect that makes correct production impossible under the current reviewed Core. A production session does **not** author or debug shared Core merely to keep the edition moving.

Lower-numbered points win if priorities conflict, but point 6 is an explicit acceptance condition rather than an optional usability preference.

## 3. Evidence model for the fixed-head audit

The fixed-head audit must be performed afresh on one immutable candidate SHA and uses the strongest evidence available before Human merge review:

- exact-head CI/regression results;
- schema/config/script/workflow inspection;
- representative cross-profile unit/contract fixtures;
- historical W33/SP001 failure evidence as regression targets, never as PASS runs;
- Retrospective monthly/half-year/annual configured-period Profile fixtures plus guidance compatibility inspection;
- standalone Thematic and Foundations-series authority compatibility inspection;
- PR-scope inspection proving that the redesign did not silently mutate edition outputs or frozen historical releases;
- explicit review of the Actions surface, Human Gate model, Reader Publication Boundary and Production/Core responsibility boundary.

The fixed-head audit must not fabricate a synthetic claim that a clean real production run has occurred when it has not.

## 4. Post-integration real-production re-validation

After the candidate passes this fixed-head audit, receives Human full-candidate review, and the reviewed Core is integrated into `main`, run a small representative real-production matrix:

- one clean future Weekly cold-start run;
- one clean standalone `THEMATIC + LONGFORM_SPECIAL` cold-start run, with SP001 as a required regression case;
- one representative configured `RETROSPECTIVE_PERIOD` cold-start production/replay through the requested Human Gate using the same canonical Profile adapter available to connector-only and direct-local execution;
- one Foundations-guided volume/scenario through at least Architecture Review;
- structural confirmation against monthly, half-year and annual Retrospective guidance and unplanned future Thematic work.

A real production validation run that discovers a shared-Core defect is preserved as failed evidence. Repair Core in a separate Core-maintenance flow, then rerun the affected validation cleanly. Do not debug the production-validation edition in place and count the salvaged run as proof of cold-start viability.

The post-integration matrix is required to claim **real-production validation** of the redesigned Core. The pre-review fixed-head audit is required to decide whether one exact implementation candidate is coherent enough to present for Human full-candidate review.

## 5. Candidate immutability during the final audit

Once the audit candidate SHA is frozen:

- do not change code, config, schemas, workflows, tests, guides, Findings, Repair Sets, closure documents, worklogs or other candidate-tree content during the audit;
- do not silently reinterpret a failure as an acceptable exception merely to preserve the frozen SHA;
- CI evidence used for the final audit must apply to that exact candidate SHA or to the pull-request merge candidate that contains exactly that head plus the unchanged target base, as appropriate to the workflow;
- the audit may read historical evidence and current repository state, but must reach its six verdicts afresh rather than carrying forward an earlier PASS.

## 6. Invalidation rule

If any of the six points reveals a defect that requires a repository change:

```text
record/classify the finding
-> mark the current final audit INVALIDATED
-> leave the Human full-candidate review boundary
-> complete all required repairs in Core maintenance
-> complete regression and documentation synchronization
-> freeze a new SHA
-> rerun all six acceptance points from point 1
```

There is no “resume from point 4” or “recheck only the failed point” path after candidate mutation.

Even a documentation-only change made to the candidate after the audit invalidates that audit, because the reviewed candidate SHA changed.

## 7. Recording the final result without mutating the candidate

The repository stores this rule before the candidate is frozen. The final audit result itself is **recorded outside the candidate tree** — normally in the PR/Human-review handoff — and must name:

- the exact audited candidate head SHA;
- the unchanged base SHA/PR identity where relevant;
- exact-head CI/regression evidence;
- the six fresh verdicts and concise supporting evidence;
- any post-integration real-production validation still pending.

This avoids the self-invalidating pattern:

```text
finish audit
-> commit an audit PASS document
-> candidate SHA changes
-> the committed PASS no longer describes the current candidate
```

Historical diagnostic audits may remain in Git history, but they must be labeled invalidated/superseded when later candidate changes occurred.

## 8. Relation to Human Gates and Grok transport

This rule does **not** add a third publication/editorial Human Gate.

The two normal production Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

A genuine Exception Gate remains reserved for an Owner decision that repository authority cannot safely resolve. It must not be used for routine uncertainty, ordinary research refinement, edition-local QA repair or transient execution retry.

When Grok execution requires Human mediation, ChatGPT prepares one self-contained task file in the configured Google Drive location and gives the Human the exact Drive **task-file path/reference**. The Human gives that path/reference to Grok. Grok reads the file and writes the instructed result. This manual Grok handoff is operational transport, not editorial approval and not another Human Gate. ChatGPT **must not search for a Grok connector** merely because the run is required.

Once the returned result exists, ChatGPT imports it and **resumes automatically toward the requested Gate**.

## 9. Production vs Core-maintenance rule

A production session owns edition-local work and transient execution recovery. It does not author shared-Core repairs.

If a likely shared-Core defect appears:

```text
record symptom / reproduction / impact
-> classify as shared Core
-> if a semantically safe edition-local workaround exists, use it only when doing so does not alter the shared contract
-> otherwise stop/pause the edition at a recorded Core dependency
-> repair shared Core separately
```

For a formal post-integration Core production-validation run, any shared-Core defect invalidates that run as acceptance evidence even if a local workaround could make the publication look acceptable. The repaired Core must be tested by a clean rerun.

For ordinary later production after Core is already accepted, a separately reviewed Core repair may be integrated according to repository maintenance policy, but affected semantic boundaries must be revalidated and the edition record must not imply that the pre-repair path validated the new Core.

## 10. Actions / deterministic-tool implication

The final audit must verify the adopted GitHub Actions responsibility policy.

The current maintenance candidate may retain Actions only where there is clear independent/reproducibility/security value, including:

- CI/regression execution;
- pinned reproducible build;
- deterministic validation;
- exact-byte Publication Preview transport;
- exact-byte Freeze/Release integrity;
- credential-isolated publication/reconciliation;
- the narrowly constrained operator execution bridge when the normal ChatGPT runtime lacks an exact local checkout/CLI execution substrate.

The operator bridge is admissible only when it remains an execution substrate for canonical deterministic Core mechanics. It must not accept arbitrary commands, own research/editorial/publication decisions, approve Human Gates, repair layout, or mutate shared Core during production. Retrospective cold start may use the bridge only to bind existing configured-period identity/window/paths to a ChatGPT-authored scope and Core contract; it may not synthesize period editorial taxonomy. Direct exact-local CLI execution remains preferred when available.

Do not count workflow automation itself as a virtue. Actions must not be the reasoning/editorial/publication-authoring loop, and the redesign must not replace the old workflow set with cadence/topic-specific authoring workflows.

The current intended Actions surface is exactly **seven workflows**:

1. `pipeline-contract-tests.yml`
2. `survey-production-v2-ci.yml`
3. `build-weekly-survey.yml`
4. `build-special-pdf.yml`
5. `survey-production-v2-export-publication-preview.yml`
6. `survey-production-v2-release.yml`
7. `survey-production-v2-operator-bridge.yml`

The original redesign plan's six-workflow wording records the pre-PFB-014 integrated surface and is superseded for current maintenance by `docs/survey-production-core-v2-redesign-authority.md` and `docs/survey-production-core-v2-operator-execution-bridge.md`. A new eighth workflow is prima facie architectural regression unless a later separately reviewed Core change explicitly revises this invariant under the same Actions admission rule.

## 11. Reader-facing publication implication

The final audit must explicitly check that:

- internal Architecture/Review/Selection/Evidence state is not a legal fallback source for reader-facing prose;
- a distinct Reader Manuscript / reader-facing publication surface exists before candidate assembly;
- known-token lint is defense-in-depth only;
- ChatGPT semantic/editorial QA checks Publication Boundary and Architecture content fidelity;
- ChatGPT reviews the exact rendered PDF visually;
- deterministic Quality Bundle contains deterministic authority only;
- Publication Candidate atomically binds exact Reader Manuscript/source/PDF/deterministic QA/semantic review/visual review;
- source/PDF change invalidates downstream Candidate/Preview/Freeze identity.

A machine PASS without reader-facing quality does not satisfy points 1, 2 or 4.

## 12. Cross-profile generality checklist

The fixed-head audit must explicitly inspect representative support for:

### Weekly

- `WEEKLY + WEEKLY_MAGAZINE` Profile composition;
- rolling-window semantics;
- required Grok/X task-file flow;
- mandatory `コミュニティの動き` and final synthesis;
- no cadence-specific authoring workflow.

### Retrospective Period

- configured slug is resolved from existing Special planning authority rather than invented by the bridge;
- one generic `BOUNDED_PERIOD` Profile builder covers representative monthly/half-year/annual periods;
- exact tier/window/identity/paths are deterministic while research question/dimensions/obligations remain ChatGPT-authored under required guides;
- coverage audit and supplemental primary-source gap fill remain Profile/guide-owned;
- chronology/lifecycle/normalization/synthesis semantics remain expressible;
- annual temporal-skew/trajectory guidance is not flattened into generic Core.

### Standalone Thematic / Longform

- topic-specific research closure and Architecture remain possible without SP001 fixed taxonomy;
- `THEMATIC + LONGFORM_SPECIAL` preserves historical attribution and longform/mixed-layout semantic requirements;
- no shared Core keys off SP001 family/package names.

### Foundations-guided work

- the living series memo remains an outer authority;
- Core does not create a rigid generic series engine;
- per-volume Architecture remains research-derived.

## 13. Scope of this rule

This post-completion six-point audit is a **Core-v2 change-management acceptance rule** for deciding whether an implementation candidate is ready to be presented for Human full-candidate review/merge.

It does not run for every Weekly/Special lifecycle stage, and it is not itself proof of a successful cold-start production run. Real production validation is separately recorded after reviewed Core integration as described above.
