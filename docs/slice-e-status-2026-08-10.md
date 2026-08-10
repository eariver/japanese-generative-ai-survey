# Slice E Status Snapshot — 2026-08-10

This note records the implementation state reached after the W32 end-to-end reference issue and the subsequent weekly-pipeline orchestration work. It supplements `weekly-pipeline-implementation-status.md` until that document is next consolidated.

## Scope and safety boundary

Slice E is the auditable GitHub work-branch / Draft-PR control layer around the deterministic and LLM-assisted stages.

The following remain explicit human/reviewer gates and are not inferred by automation:

- Candidate Selection `APPROVED`;
- Issue Architecture `APPROVED`;
- Visual Review;
- Freeze;
- merge of the weekly work PR;
- public GitHub Release publication.

Canonical weekly work branch:

```text
weekly/<issue>-work
```

Automation may prepare or refresh a Draft PR while it remains Draft. It may not overwrite a PR after a human marks it ready for review.

## Current lifecycle handoff

The implemented coarse lifecycle path now has deterministic persistence boundaries through Evidence review:

```text
reviewed Source Intake accepted
  -> DISCOVERY_COLLECTED
  -> complete validated Screening accepted
  -> CANDIDATES_NORMALIZED
  -> complete validated Evidence accepted
  -> EVIDENCE_REVIEWED
  -> Human Selection Gate remains next
```

The gate transitions are deliberately narrow:

- Source Intake acceptance: `raw_sources_preserved = passed`;
- Screening acceptance: `candidate_inventory = passed`;
- Evidence acceptance: `evidence_normalized = passed`;
- `candidate_selection` remains `pending` after Evidence acceptance.

## Weekly work branch / Draft PR control

Implemented:

- canonical weekly work branch creation;
- Draft PR creation/update only while the PR remains Draft;
- no merge, freeze, tag, or Release from PR control;
- safe fast-forward of a work branch that has **no unique weekly commits** and is behind `main`;
- refusal to auto-rebase/rewrite a work branch once it contains unique weekly commits;
- deterministic PR metadata and gate checklist;
- assistant-controlled allowlisted workflow dispatch.

Real W33 empty-branch smoke on 2026-08-10:

- run `31378759882`;
- empty `weekly/2026-W33-work` safely fast-forwarded;
- resulting branch relation `ahead=0 / behind=0` at that point;
- PR creation correctly deferred as `WAITING_FOR_WORK_COMMIT`.

The branch must be realigned again after later control-code merges if it still has no unique weekly commits.

## Reviewed Source Intake acceptance

Implemented:

- exact successful `workflow_dispatch` run verification for `.github/workflows/weekly-pipeline.yml` on `main`;
- repository / workflow / event / ref / run identity checks;
- exact Artifact name, run linkage, expiry state, and SHA-256 digest checks;
- reviewed Artifact import only into the canonical weekly work branch;
- append-only collector Raw / summary / collector-run persistence;
- deterministic screening data from the intake Artifact is **not** committed and is regenerated later;
- Raw index update/check before work-branch commit;
- source plan SHA and review reference recorded in acceptance provenance;
- first accepted new-issue Source Intake creates/advances `pipeline-state.json` to `DISCOVERY_COLLECTED`;
- later Source Intake is rejected once lifecycle advances beyond `DISCOVERY_COLLECTED`.

Real W32 resolver smoke:

- source run `31359910803`;
- import smoke run `31378110064`;
- real W32 run / Artifact metadata validation passed;
- workflow then stopped at the missing W32 work-branch gate;
- Frozen W32 content was not modified.

W32 predates reviewed collector import. Its committed main tree therefore has the Frozen Raw baseline but not the replay collector tree. A later W32 screening-package smoke correctly reached Raw-integrity success and then stopped because `sources/2026-W32/collectors` is absent. W32 must not be backfilled merely to make the new pipeline fit the historical reference issue.

## Screening execution package

Implemented read-only package preparation:

```text
accepted collector tree + pipeline state + Raw index
  -> deterministic screening index/batches
  -> commit-pinned Screening Run Package
```

The package pins:

- source ref and commit SHA;
- `pipeline-state.json` SHA-256;
- `raw-index.json` SHA-256;
- exact `source-screening-v0.1` prompt bytes / SHA;
- exact result-schema bytes / SHA;
- screening manifest / index SHA;
- every batch path, record count, byte size, and SHA-256.

`prepare-weekly-screening.yml` is read-only and defaults to the canonical weekly work branch. `main` is permitted only for a `FROZEN` historical replay/smoke.

A real W32 smoke exposed and fixed an Actions `PYTHONPATH` issue before the historical no-collector-tree boundary was reached.

## Screening result acceptance

Implemented complete-only acceptance:

- one exact result file per package batch;
- no missing or extra files;
- every result revalidated against the exact batch and prompt bytes;
- current work-tree `pipeline-state.json` and Raw-index bytes must still match the package basis for a new acceptance;
- accepted result set addressed by deterministic result-set SHA-256;
- raw result JSON, per-batch validation reports, reviewed records, verification queue, progress manifest, package manifest, and acceptance manifest persisted append-only;
- exact already-accepted result set remains an idempotent audit object after later lifecycle progress.

On successful new acceptance:

```text
DISCOVERY_COLLECTED
  -> CANDIDATES_NORMALIZED
candidate_inventory: pending -> passed
```

This transition intentionally closes Source Intake so later Raw collection cannot invalidate the accepted screening basis.

Partial screening may be resumed outside the repository, but persistence to the weekly work branch is complete-only.

## Evidence execution package

Implemented read-only Evidence package preparation from one explicitly selected accepted Screening result-set SHA:

```text
accepted screening verification queue
  -> deterministic Evidence Tasks
  -> commit-pinned Evidence Execution Package
```

The package requires:

- lifecycle `CANDIDATES_NORMALIZED`;
- `candidate_inventory = passed`;
- `evidence_normalized = pending`;
- one exact accepted Screening result-set SHA.

It pins:

- source ref / commit / pipeline-state SHA;
- accepted Screening manifest SHA;
- verification queue SHA;
- exact `primary-source-verification-v0.1` prompt bytes / SHA;
- exact Evidence Run and Evidence Card schemas / SHA;
- deterministic Evidence Task manifest / index SHA;
- every Evidence Task ID, path, byte size, and SHA-256.

`prepare-weekly-evidence.yml` is read-only and reads only `weekly/<issue>-work`.

Known deliberate boundary: an empty verification queue is currently rejected. A zero-Evidence issue needs an explicit no-task/no-Evidence path rather than silently passing `evidence_normalized`.

## Evidence result acceptance

Implemented complete-only acceptance:

- one exact Evidence Run per package task;
- no missing / extra result files;
- every Evidence Run revalidated against the exact Evidence Task and Evidence prompt bytes;
- current candidate-normalized state and accepted Screening basis must still match package hashes for a new acceptance;
- accepted set addressed by deterministic result-set SHA-256;
- raw Evidence Run JSON, validation reports, deterministic merged Evidence output, candidate-ready queue, hold/rejected queues, progress manifest, package manifest, and acceptance manifest persisted append-only;
- exact already-accepted Evidence set remains an idempotent audit object after later lifecycle progress;
- narrow recovery exists for an interrupted transaction where accepted files exist but the coarse lifecycle transition was not written.

On successful new acceptance:

```text
CANDIDATES_NORMALIZED
  -> EVIDENCE_REVIEWED
evidence_normalized: pending -> passed
```

The contract explicitly stops before Selection:

```text
candidate_selection = pending
```

`CANDIDATE / HOLD / INSPECT_MORE / REJECT` in Evidence remains an Evidence recommendation, not a Human Selection decision.

## Not yet connected

The deterministic contracts are ahead of the production execution transport. Remaining Slice E work includes:

1. production / interactive runner integration that actually produces Screening result JSON from a Screening package;
2. a reviewed Artifact transport/import workflow for those Screening results, using `accept_screening_results.py`;
3. production / interactive primary-source Evidence runner integration that produces Evidence Run JSON;
4. a reviewed Artifact transport/import workflow for Evidence results, using `accept_evidence_results.py`;
5. deterministic accepted-Evidence -> Candidate Record / comparison-matrix orchestration on the weekly work branch;
6. Human Selection template generation and explicit `APPROVED` gate handling without automatic approval;
7. persistence/orchestration for approved Architecture, article Draft Results, post-draft synthesis, generated TeX/Bib, source preflight, PDF build, and visual-review evidence;
8. explicit Freeze recording / final weekly work PR handoff;
9. zero-Evidence issue path;
10. first complete new-issue E2E run.

## W33 timing

On 2026-08-10, W33 is still a future issue under the project calendar.

The next editorial cutoff is:

```text
2026-08-14 18:00 America/New_York
```

Only after that cutoff does the rolling planner resolve W33. A premature W33 Source Intake attempt (`31377560587`) was correctly rejected because the latest completed cutoff still mapped to W32.

`weekly_pipeline.py init --issue-id` now treats the supplied issue as an assertion; it cannot relabel the current cutoff into a future issue.

Therefore the first real W33 operational sequence must wait for the W33 cutoff and then proceed as:

```text
Source Intake
  -> review Artifact
  -> reviewed import to weekly/2026-W33-work
  -> Screening package
  -> Screening execution/result review
  -> complete Screening acceptance
  -> Evidence package
  -> Evidence execution/result review
  -> complete Evidence acceptance
  -> Candidate comparison
  -> explicit Human Selection Gate
```

No step in this sequence authorizes unattended public publication.
