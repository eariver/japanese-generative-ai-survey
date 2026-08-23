# Survey Production Core v2 — Post-Merge Production Feedback Backlog

Status: `W33 + SP001 REVIEW COMPLETE / REDESIGN REQUIRED`  
Established: 2026-08-23 JST  
Review closed: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`

## Current authority

The initial feedback-collection phase is complete.

The consolidated redesign direction is now:

- `docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md`
- `docs/survey-production-core-v2-github-actions-policy.md`
- `docs/survey-production-core-v2-execution-record-policy.md`

The W33 and SP001 Core v2 attempts are retained as failed / non-validating production trials. Their outcomes must not be interpreted as proof that the merged Core v2 can produce acceptable Weekly or LONGFORM_SPECIAL publications from a clean start.

Primary review evidence:

- Issue #400 — SP001 first Publication Preview plus Human re-review of the 19-page salvage revision;
- Issue #433 — W33 Publication Preview rejection;
- Issue #434 — shared Core v2 Publication Boundary defect across both profiles;
- W33 work branch: `weekly/2026-W33-v2-work`;
- SP001 work branch: `special/SP001-v2-work`.

## Feedback item PFB-001 — Use one self-contained Grok task file in Google Drive

Status: `ACCEPTED / CARRY INTO REDESIGN`

Prefer one run-specific Markdown file in Google Drive containing the complete Grok/X task: role, scope, research questions, evidence boundary, output format, and result destination. A separate `grok-prompt.md` is not required unless future evidence shows a concrete benefit.

Preferred operational shape:

```text
Grok_X_SourseIntake/
  <category>/<edition>/<run-id>/
    <grok-task-file>.md
    <result>.md
```

Repository provenance must still hash-bind the exact task bytes and imported result bytes.

## Feedback item PFB-002 — Human passes the exact Drive task-file path to Grok; do not search for a Grok connector

Status: `ACCEPTED / CARRY INTO REDESIGN`

Normal boundary:

```text
ChatGPT prepares one self-contained task file in Drive
-> ChatGPT gives Human the exact Drive file path/reference
-> Human gives that file path/reference to Grok
-> Grok reads it and writes the instructed result
-> ChatGPT imports/dispositions the result and resumes automatically
```

Do not search for/install/configure a Grok connector merely because an X run is required. Absence of a Grok connector is not an Exception Gate or dependency failure.

## Feedback item PFB-003 — Require a concluding synthesis in every Weekly and Special

Status: `ACCEPTED / CARRY INTO REDESIGN`

Every reader-facing Weekly and Special requires a final substantive `総括` or explicitly equivalent section before non-editorial back matter. ChatGPT must judge synthesis quality; deterministic checks may only verify reliable structural presence/order.

## Feedback item PFB-004 — Weekly must always publish an explicit community-movement view informed by Grok/X

Status: `ACCEPTED / CARRY INTO REDESIGN`

Every Weekly requires a reader-facing `コミュニティの動き` component. The completed Grok/X result must receive editorial disposition, not merely technical import/disposition. Material observations are reflected in the issue or carry an internal exclusion reason; a quiet week is an explicit reader-facing finding rather than silent omission.

Grok/X remains Discovery/community-signal authority, not final technical Evidence authority.

## Feedback item PFB-005 — Production sessions repair editions, not shared Core v2

Status: `CONFIRMED BY W33 + SP001 / REQUIRED REDESIGN INVARIANT`

The trials confirmed this concern rather than merely suggesting it.

SP001 production created/repaired generic Core work-branch control workflows, semantic publication behavior, and shared longform style on `main`, then reintegrated those repairs into the edition branch. W33 likewise consumed pending/generic repair logic during the trial.

Required invariant:

> **A Production session repairs the edition. It does not repair shared Core v2.**

A shared Core defect is recorded and returned to Core maintenance. If there is no semantically safe edition-local workaround, the production attempt is blocked/terminated and later restarted from the appropriate clean boundary after reviewed Core repair.

## Feedback item PFB-006 — Reduce GitHub Actions from production worker to CI/build verifier

Status: `CONFIRMED BY W33 + SP001 / REQUIRED REDESIGN INVARIANT`

The trials confirmed excessive Actions orchestration. Actions were used for stage adoption, Drafting/Synthesis, publication generation/mutation, quality/candidate state, bot commits, rebuild/export transport and other production work. SP001 additionally hit write-capable workflow chaining limits after `github-actions[bot]` commits.

Use `docs/survey-production-core-v2-github-actions-policy.md` as the governing rule:

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.**

Existing workflows must be classified as `KEEP_AS_CI`, `SHRINK_TO_CI_ONLY`, `RETURN_TO_CHATGPT`, or `LEGACY_REMOVE_CANDIDATE`.

## Feedback item PFB-007 — Terminate the current W33/SP001 v2 trials as non-validating production attempts

Status: `RESOLVED / BOTH TRIALS TERMINATED FOR REDESIGN`

W33 should not receive further #433 salvage work under the current Core v2 path.

SP001's #400 19-page revision materially improved layout, depth, Technical Notes and synthesis, but Human re-review still found Publication Boundary leakage (`D017` / `D021`, `本 package`, source-promotion/coverage language). The revision also required shared-Core renderer/style repairs and an authority-rebind repair after the new PDF and old Publication Candidate diverged.

Therefore the 19-page revision is useful salvage evidence, not cold-start validation. SP001 remains unapproved and should be rerun after redesign.

## Feedback item PFB-008 — Make the reader-facing Publication Boundary structural, not stylistic

Status: `NEW / REQUIRED REDESIGN INVARIANT`

Issue #434 establishes a cross-profile defect: internal Architecture / Review / Selection / Evidence material can become reader-facing prose.

Required direction:

- explicit internal editorial/provenance layer;
- explicit reader-facing manuscript/publication layer;
- internal fields are not legal render inputs;
- no fallback from missing reader-facing fields to Architecture/Profile/Evidence text;
- missing required publication content fails closed back to ChatGPT authoring.

Known-token lint remains defense-in-depth only. SP001's 19-page revision passed deterministic leakage checks yet Human review still found semantically internal wording.

## Feedback item PFB-009 — Architecture fidelity means reader-facing content fulfillment

Status: `NEW / REQUIRED REDESIGN INVARIANT`

W33 demonstrated that a must-cover item could effectively be represented by prose saying that Architecture intended to cover it. That is not content fulfillment.

For each must-cover requirement, retain lightweight traceability:

```text
requirement
-> accepted Evidence/Observation
-> actual reader-facing section/block
-> ChatGPT fulfillment judgment
```

Do not substitute page quotas or string-presence checks for this editorial judgment.

## Feedback item PFB-010 — Separate deterministic QA from semantic/editorial and visual QA

Status: `NEW / REQUIRED REDESIGN INVARIANT`

Machine PASS must no longer imply publication-quality PASS.

Candidate readiness requires separate evidence for:

1. deterministic QA — schemas, hashes, citations, identifiers, compiler/preflight, known exact leakage patterns;
2. ChatGPT semantic/editorial QA — must-cover fulfillment, technical depth, reader-facing boundary, source-class wording, `総括`, Weekly community use, repetition/generic fallback, bibliography surface;
3. ChatGPT visual QA — exact rendered PDF review for layout, hierarchy, whitespace, tables/boxes/URLs and visually obvious content-thin pages.

The Quality Regression Bundle must not claim to have proven semantic quality that was never actually reviewed by ChatGPT.

## Feedback item PFB-011 — Publication revision/candidate authority must be atomic

Status: `NEW / REQUIRED REDESIGN INVARIANT`

SP001's revised 19-page PDF initially coexisted with Quality Regression Bundle / Publication Candidate authority still bound to the old 11-page PDF.

Any revision of publication source/PDF must invalidate downstream candidate authority and recreate the complete Human Preview candidate as one fail-closed finalization operation. A visible/reviewable PDF must never remain paired with an active candidate manifest for different bytes.

## Feedback item PFB-012 — Standardize edition-local execution records

Status: `NEW / REQUIRED REDESIGN INVARIANT`

The W33 and SP001 logs were valuable but inconsistent: W33 used a long worklog whose header became stale, while SP001 used multiple ad-hoc date/session checkpoint files.

Adopt `docs/survey-production-core-v2-execution-record-policy.md`.

Target location:

```text
sources/<issue-id>/execution/
  index.md
  sessions/
  reviews/
  defects/
```

The record is concise operational provenance, not a transcript or duplicate state machine.

## Feedback item PFB-013 — Real cold-start profile trials are required after Core repair

Status: `NEW / REQUIRED ACCEPTANCE RULE`

After redesign implementation and Core CI, validate with clean real production runs rather than only synthetic fixtures.

At minimum:

- one Weekly trial from clean current `main` with no in-run shared-Core repair;
- one LONGFORM_SPECIAL trial, using SP001 as the required regression case, with no in-run shared-Core repair.

If a shared-Core defect is discovered, retain the run as failed evidence, repair Core separately, and restart the affected acceptance run cleanly. Do not debug the pipeline inside the acceptance edition and then count that same run as PASS.

## Next step

Do not resume W33 or SP001 publication work under the current production path.

The next maintenance phase should implement the workstreams in `docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md`, beginning with responsibility/orchestration simplification and the reader-facing Publication Boundary, then reclassifying/removing inappropriate Actions workflows before clean profile re-validation.
