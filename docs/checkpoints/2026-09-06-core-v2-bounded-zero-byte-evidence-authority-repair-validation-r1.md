# Survey Production Core v2 — bounded zero-byte Evidence Authority repair

Status: `REPAIR_COMPLETE_READY_FOR_FRESH_SOL_PREFREEZE_CROSSCHECK`

This is the durable validation record for Luna/Work execution contract comment
`5559148031` on PR `#484`. It records the bounded zero-byte Evidence Authority
repair only. It is not a Seven-point audit, a freeze record, a Human approval,
or merge authorization.

## Fixed-head and write boundaries

- Repository: `eariver/japanese-generative-ai-survey`
- Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
- Exact starting maintenance SHA: `c1a76bce52c7b9c4c3c79bb3a8169e1533d3d57d`
- Starting candidate tree SHA: `e28aedd8b47ca1c206dead813057f65166c99040`
- Main guard: `d8fa79ef2affacec49a47e6fc88018fb99f36899`
- Main tree guard: `b6c1b2cbc13165e64ac1d88d4d36b7515f7494da`
- W34 exact fixture: `df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`
- Target PR: `#484`, draft/open/unmerged

Only the maintenance branch is permitted to receive the repair commit. The
main and W34 refs were treated as read-only, and no sidecar was executed.

## Bounded repair

The Evidence Authority Supplement schema now requires `byte_count >= 1`.
Runtime supplement construction independently checks the exact Raw file size
before binding the source, then retains the existing exact byte-count and
SHA-256 checks, repository-local path checks, and symlink checks. Rejection is
transactional: a zero-byte authority cannot leave an output manifest behind.

The implementation remains content-agnostic. It accepts ordinary text or
binary Raw bodies based on exact bytes and does not add MIME/content heuristics.

Changed paths for this repair are:

- `schemas/evidence-authority-supplement-v2.schema.json`
- `scripts/survey_evidence_v2.py`
- `tests/test_survey_evidence_v2.py`
- this validation record

No lifecycle, Human Gate, Evidence source-binding, or active checkpoint
resolution semantics were changed by this bounded repair.

## Source-type probe disposition

A lexical probe was run against the existing `source_type` classifier. Known
descriptive values used by the existing W34 supplement remain accepted, a
declared class mismatch is rejected, and a fully arbitrary value such as
`totally-arbitrary-source` is rejected. A descriptive value such as
`not-an-official-source` can still classify lexically when its declared class
matches. No separate fail-open negative test established that this classifier
is an independent authority bypass: task binding, explicit source class, Raw
path, byte count, and SHA validation still remain mandatory. Therefore no
source-type repair was added in this bounded task; the classifier question is
carried to the next full Seven-point audit as a separate review item.

## Validation results

Focused and affected tests, run with the repository requirements available,
all passed:

- Evidence, Supplement, interactive/agent-first, and active Evidence/View: `43 passed`.
- Selection, Architecture, Stage, Completeness, Screening and active Screening: `55 passed`.
- Human Gate, operator invalidation, rollback, historical-config binding, and
  Human Gate bridge: `61 passed`.
- Publication, orchestrator, bootstrap, operator workflow, downstream and
  screening archive: `47 passed`.
- Full Python suite: `774 passed, 6 skipped, 0 failed`.

The isolated operator CLI smoke test initially exposed only the disposable
diagnostic environment's missing `jsonschema`/`pypdf` dependencies. It passed
after the declared repository requirements were installed in the disposable
test runtime. The repository's existing SyntaxWarning output remains a
diagnostic warning and is unrelated to this repair.

The new zero-byte regression proves all of the following:

1. schema validation rejects a supplement entry declaring `byte_count: 0`;
2. runtime rejection still occurs when the schema layer is deliberately
   bypassed;
3. the rejected build leaves no output manifest;
4. a non-empty authority still binds successfully; and
5. existing SHA, byte-count, path, symlink, task-binding, and card-binding
   negative tests remain green.

Workflow count remains exactly `7`, and the Core still defines exactly the two
Human Gates `ARCHITECTURE_REVIEW` and `PUBLICATION_PREVIEW`.

## Fresh W34 exact read-only regression

The regression used a new disposable detached checkout at
`weekly/2026-W34-v2-work@df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f` and overlaid
the candidate Core. It did not commit or push the W34 fixture.

- Initial surface: `ARCHITECTURE_ESTABLISHED`, Architecture Review pending,
  null Human provenance, Human Review Index rows `0`.
- Operator invalidation: `ARCHITECTURE_REVIEW -> CANDIDATES_NORMALIZED` passed
  through the Core invalidation and Stage Checkpoint machinery; no Human
  record or Human decision was created.
- Supplement: `62` task-bound bindings over `61` unique Raw paths; every
  admitted Raw body was non-empty (minimum observed size `2162` bytes).
- Evidence: new accepted run retained beside historical run; counts were
  `VERIFIED 32 / PARTIAL 27 / NEEDS_MORE 14 / REJECTED 7`.
- Edition View: new accepted run retained beside historical run; counts were
  `MATERIAL 1 / CONTEXT 31 / HOLD 41 / NON_MATERIAL 7 / DUPLICATE 4`.
- Active resolution: checkpoint-bound resolver selected the new Evidence
  acceptance
  `88eda3550bd3df94e80fd9c11cc80f89a819667db9daeaa882472e2609052ca7` and new
  View acceptance
  `9f65aa5a8a032824566f4eabff6dab8ffb74beef6394d84a796bbeccbfedce97`, while
  historical accepted directories remained present.
- Selection mechanism: `SELECTED 1 / HOLD 64 / INSPECT 15`; this is recorded
  only as a mechanism regression result, not as a semantic success criterion.
- Architecture mechanism: one proposed package, `Verified developer-tooling
  change`; the review summary was `READY_FOR_ARCHITECTURE_REVIEW`.
- Final state: `ARCHITECTURE_ESTABLISHED`, `next_action=ARCHITECTURE_REVIEW`,
  `terminal_reason=HUMAN_GATE_REACHED`, Architecture Review pending, and
  Human Review Index rows `0`.

The W34 remote HEAD was read before and after the regression and remained
`df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`. Main remained
`d8fa79ef2affacec49a47e6fc88018fb99f36899`.

## Explicit non-actions and remaining boundary

- No Human review record, `REQUEST_CHANGES`, or `APPROVED` record was created.
- No main or W34 canonical artifact was written remotely.
- No Publication Boundary Validator or Authority Auditor run occurred.
- No new branch, force push, reset, rewrite, or rebase was used.
- Seven-point fixed-head audit remains deferred.
- Fresh Sol pre-freeze crosscheck, CI evidence for the final pushed SHA, and
  any W34 semantic/operator judgement remain downstream work.
