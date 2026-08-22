# Survey Production Core v2 — post-completion final audit rule

Status: `CANONICAL PRE-MERGE REVIEW RULE`  
Established: 2026-08-22 JST

## 1. Principle

A full-candidate audit is meaningful only after implementation, repair, regression, documentation and review-package synchronization are complete.

Therefore the mandatory order is:

```text
finish every intended candidate change
-> finish regression/CI repair
-> synchronize repository-owned authority/docs/findings/Repair Set
-> freeze one candidate branch head SHA
-> run the complete five-point acceptance audit from zero on that exact SHA
-> if and only if all five pass without changing the candidate, present that exact SHA for Human full-candidate review
```

A partial audit performed while the candidate is still changing is diagnostic evidence only. It is never final approval evidence.

## 2. Five acceptance points

Every final audit evaluates all five points in this priority order:

1. **Weekly viability** — a normal future Weekly edition can be compiled through the requested Human Gate without edition-specific rescue work.
2. **Special viability** — Retrospective Period, standalone Thematic, SP-001–003 style work and Generative AI Foundations guided-series work can be compiled through the requested Human Gate.
3. **Generality** — the Core/Profile design is not overfit to W33/W34/SP001–003 and can support later Weekly issues and previously unplanned Specials through generic Profile/planning authority.
4. **Historical Issue recurrence prevention** — known Human Review defect families have an appropriate deterministic, ChatGPT research/editorial/visual, Human-review, or legacy-only prevention owner.
5. **Control proportionality** — after 1–4 are satisfied, routine work is not burdened with unnecessary Human Gates, workflow ceremony, or validators that pretend to replace qualitative judgment.

Lower-numbered points win if priorities conflict.

## 3. Candidate immutability during the final audit

Once the audit candidate SHA is frozen:

- do not change code, config, schemas, workflows, tests, guides, Findings, Repair Sets, closure documents, or other candidate-tree content during the audit;
- do not silently reinterpret a failure as an acceptable exception merely to preserve the frozen SHA;
- CI evidence used for the final audit must apply to that exact candidate SHA or to the pull-request merge candidate that contains exactly that head plus the unchanged target base, as appropriate to the workflow;
- the audit may read historical evidence and current repository state, but must reach its five verdicts afresh rather than carrying forward an earlier PASS.

## 4. Invalidation rule

If any of the five points reveals a defect that requires a repository change:

```text
record/classify the finding
-> mark the current final audit INVALIDATED
-> leave the Human full-candidate review boundary
-> complete all required repairs
-> complete regression and documentation synchronization
-> freeze a new candidate SHA
-> rerun all five acceptance points from point 1
```

There is no “resume from point 4” or “recheck only the failed point” path after candidate mutation.

Even a documentation-only change made to the candidate after the audit invalidates that audit, because the reviewed candidate SHA changed.

## 5. Recording the final result without mutating the candidate

The repository stores this rule before the candidate is frozen. The final audit result itself is recorded outside the candidate tree — normally in the PR/Human-review handoff — and must name the exact audited head SHA plus the required CI run identities.

This avoids the self-invalidating pattern:

```text
finish audit
-> commit an audit PASS document
-> candidate SHA changes
-> the committed PASS no longer describes the current candidate
```

Historical diagnostic audits may remain in Git history, but they must be labeled invalidated/superseded when later candidate changes occurred.

## 6. Relation to Human Gates

This rule does **not** add a third publication/editorial Human Gate.

The two normal production Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

The post-completion five-point audit is a **Core-v2 change-management acceptance rule** for deciding whether an implementation candidate is ready to be presented for Human full-candidate review/merge. It does not run for every Weekly/Special lifecycle stage.

## 7. Toolchain-upgrade implication

When a reusable defect is found during a real edition:

```text
repair the generic tool on main through normal review/CI
-> integrate the reviewed main repair commit into the edition work branch
-> use the integrated branch head as the actual execution toolchain
-> revalidate/migrate only affected accepted boundaries
-> record that actual implementation commit in the next Stage Checkpoint
-> continue
```

Do not treat the initialization implementation SHA as an edition-wide lock. Do not run an unintegrated second checkout of `main` against edition artifacts and then claim the work branch itself contained that toolchain. If the changed contract cannot be reconciled safely, use an Exception Gate.
