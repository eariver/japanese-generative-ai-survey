# Survey Production Core v2 — post-completion final audit rule

Status: `CANONICAL REDESIGN-CANDIDATE FINAL AUDIT RULE / IMPLEMENTATION NOT STARTED`  
Established: 2026-08-22 JST  
Redesign alignment: 2026-08-23 JST  
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

## 2. Six acceptance points

Every final audit evaluates all six points in this priority order:

1. **Weekly viability** — a normal future Weekly edition can be compiled through the requested Human Gate without edition-specific rescue work, including required Grok/X Source Intake, exact Google Drive task-file path handoff, returned-result import, mandatory Weekly community treatment, and no in-run shared-Core repair.
2. **Special viability** — the redesigned Core remains viable for `RETROSPECTIVE_PERIOD`, standalone `THEMATIC`, `LONGFORM_SPECIAL`, SP-001–003-style work, and Generative AI Foundations guided-series work. Representative acceptance evidence must cover bounded-period semantics, standalone Thematic/Longform publication, and the Foundations living-series boundary rather than inferring all Special viability from SP001 alone.
3. **Generality** — the Core/Profile design is not overfit to W33/W34/SP001–003, one cadence, one topic taxonomy, or one publication shape. Shared Core, Research Profile, Publication Profile and edition/series authority remain orthogonal. Later Weekly issues and previously unplanned Specials can be produced through generic Profile/planning authority without new authoring workflows.
4. **Historical and clarified requirement recurrence prevention** — known Human Review defect families and later clarified requirements have an appropriate owner: narrow deterministic protection for crisp invariants, ChatGPT research/editorial/visual review for semantic judgment, Human review at the two normal Gates, or explicit legacy-only disposition. Publication Boundary defects from #400/#433/#434 are included here.
5. **Control proportionality** — after 1–4 are satisfied, routine work is not burdened with unnecessary Human Gates, workflow ceremony, profile-specific authoring workflows, or validators that pretend to replace qualitative judgment. GitHub Actions satisfy the adopted Actions responsibility policy.
6. **Autonomous progression / stop discipline** — after the user supplies the target and requested stopping Gate, ChatGPT proceeds through ordinary edition-local research/editorial work and transient retries without repeatedly stopping for confirmation. A production session may stop only for an actual normal Human Gate, a genuine Owner-level Exception Gate, the permitted manual Grok task-file path handoff, or a recorded shared-Core defect that makes correct production impossible under the current reviewed Core. A production session does **not** author or debug shared Core merely to keep the edition moving.

Lower-numbered points win if priorities conflict, but point 6 is an explicit acceptance condition rather than an optional usability preference.

## 3. Generality evidence expected by points 2 and 3

Do not claim cross-profile generality from only W33 and SP001.

The final redesign acceptance package should include a small representative matrix, not an exhaustive synthetic future-edition matrix:

- one clean future Weekly cold-start run;
- one clean standalone `THEMATIC + LONGFORM_SPECIAL` cold-start run, with SP001 as a required regression case;
- one representative `RETROSPECTIVE_PERIOD` production/replay through the requested Human Gate;
- one Foundations-guided volume/scenario through at least Architecture Review;
- structural compatibility review against monthly, half-year and annual Retrospective guidance and against unplanned future Thematic work.

A real acceptance run that discovers a shared-Core defect is preserved as failed evidence. Repair Core in the separate Core-maintenance flow, then rerun the affected acceptance trial cleanly. Do not debug the acceptance candidate in place and count the salvaged run as proof of cold-start viability.

## 4. Candidate immutability during the final audit

Once the audit candidate SHA is frozen:

- do not change code, config, schemas, workflows, tests, guides, Findings, Repair Sets, closure documents, or other candidate-tree content during the audit;
- do not silently reinterpret a failure as an acceptable exception merely to preserve the frozen SHA;
- CI evidence used for the final audit must apply to that exact candidate SHA or to the pull-request merge candidate that contains exactly that head plus the unchanged target base, as appropriate to the workflow;
- the audit may read historical evidence and current repository state, but must reach its six verdicts afresh rather than carrying forward an earlier PASS.

## 5. Invalidation rule

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

## 6. Recording the final result without mutating the candidate

The repository stores this rule before the candidate is frozen. The final audit result itself is recorded outside the candidate tree — normally in the PR/Human-review handoff — and must name the exact audited head SHA plus the required CI and representative-production evidence identities.

This avoids the self-invalidating pattern:

```text
finish audit
-> commit an audit PASS document
-> candidate SHA changes
-> the committed PASS no longer describes the current candidate
```

Historical diagnostic audits may remain in Git history, but they must be labeled invalidated/superseded when later candidate changes occurred.

## 7. Relation to Human Gates and Grok transport

This rule does **not** add a third publication/editorial Human Gate.

The two normal production Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

A genuine Exception Gate remains reserved for an Owner decision that repository authority cannot safely resolve. It must not be used for routine uncertainty, ordinary research refinement, edition-local QA repair or transient execution retry.

When Grok execution requires Human mediation, ChatGPT prepares one self-contained task file in the configured Google Drive location and gives the Human the exact Drive **task-file path/reference**. The Human gives that path/reference to Grok. Grok reads the file and writes the instructed result. This is operational transport, not editorial approval and not another Human Gate. ChatGPT must not search for a Grok connector merely because the run is required.

Once the returned result exists, ChatGPT imports it and resumes automatically toward the requested Gate.

## 8. Production vs Core-maintenance rule

A production session owns edition-local work and transient execution recovery. It does not author shared-Core repairs.

If a likely shared-Core defect appears:

```text
record symptom / reproduction / impact
-> classify as shared Core
-> if a semantically safe edition-local workaround exists, use it only when doing so does not alter the shared contract
-> otherwise stop/pause the edition at a recorded Core dependency
-> repair shared Core separately
```

For a formal Core acceptance run, any shared-Core defect invalidates that run as acceptance evidence even if a local workaround could make the publication look acceptable. The repaired Core must be tested by a clean rerun.

For ordinary later production after Core is already accepted, a separately reviewed Core repair may be integrated according to the repository's maintenance policy, but affected semantic boundaries must be revalidated and the edition record must not imply that the pre-repair path validated the new Core.

## 9. Actions / deterministic-tool implication

The final audit must verify the adopted GitHub Actions responsibility policy.

Retain Actions where there is clear independent/reproducibility/security value, including:

- CI/regression execution;
- pinned reproducible build;
- deterministic validation;
- exact-byte Freeze/Release integrity;
- credential-isolated publication/reconciliation.

Do not count workflow automation itself as a virtue. Actions must not be the reasoning/editorial/publication-authoring loop, and the redesign must not replace the old workflow set with cadence/topic-specific authoring workflows.

## 10. Reader-facing publication implication

The final audit must explicitly check that:

- internal Architecture/Review/Selection/Evidence state is not a legal fallback source for reader-facing prose;
- a distinct reader-facing manuscript/publication surface exists before assembly;
- known-token lint is defense-in-depth only;
- ChatGPT semantic/editorial QA checks Publication Boundary and Architecture content fidelity;
- ChatGPT reviews the exact rendered PDF visually;
- exact source/PDF/candidate identity remains deterministic and atomic.

A machine PASS without reader-facing quality does not satisfy points 1, 2 or 4.

## 11. Scope of this rule

This post-completion six-point audit is a **Core-v2 change-management acceptance rule** for deciding whether an implementation candidate is ready to be presented for Human full-candidate review/merge. It does not run for every Weekly/Special lifecycle stage.
