# Survey Production Core v2 Pre-Human Evidence Regeneration Repair Validation r2

Date: 2026-09-06

Status: `CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

## Fixed-head scope

- Exact reviewed `main` SHA at start: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
- Exact maintenance-branch starting SHA: `4d052597fd1d6bad8c1d3818c4b5e1c50f0273df`
- Exact W34 regression fixture SHA: `df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`
- W34 fixture remote writes: `0`
- W34 canonical branch writes: `0`
- `main` writes: `0`
- Sidecar runs: `0`
- New branch creation: `0`

This r2 pass is a bounded continuation of the existing maintenance candidate.
It does not merge the branch, create a PR merge, perform the seven-point audit,
change W34 production artifacts, create a Human decision, or run either
external sidecar.

## Changed paths in this r2 pass

- `scripts/run_evidence_v2_interactive.py`
- `tests/test_survey_operator_invalidation_v2.py`
- `tests/test_run_evidence_v2_interactive.py`
- `docs/checkpoints/2026-09-06-core-v2-pre-human-evidence-regeneration-repair-validation-r2.md`

The r1 validation record and all prior Core repair paths remain historical
authority. No edition-local W34 artifact was copied into the maintenance
branch.

## Design summary

The existing Core repair mechanisms are retained and tested with the two
bounded Sol findings:

1. pending Human Gate invalidation is a fail-closed operator control with
   transactional rollback coverage; and
2. interactive Evidence records are profile-specific and cannot leak
   Thematic fields into Weekly or Retrospective input.

The Core still has exactly seven workflows, exactly two Human Gates, and no
new lifecycle state. The operator path remains distinct from Human
`REQUEST_CHANGES` and Human `APPROVED` semantics.

## Pending Human Gate invalidation coverage

`survey_human_gate_v2.invalidate_pending_gate()` is covered by 20 test
methods. These cover the requested 19 fail-close conditions; symlink and
symlink-traversal are exercised in one combined test:

- non-pending Gate, lifecycle mismatch, and terminal-reason mismatch;
- stale invalidated commit and expected work-branch HEAD mismatch;
- current State byte drift;
- Gate input byte drift, missing input, symlink, and symlink traversal;
- active Human Gate provenance and an existing Human Review Index row;
- refusal to cross an approved Architecture from a pending Publication
  Preview;
- invalid regeneration boundary;
- injected partial cleanup failure with complete State/artifact restoration
  and no residual invalidation record;
- prior State, prior Gate input, invalidated checkpoint authority, and
  superseded canonical authority drift;
- invalidation sequence gap and duplicate detection.

Existing Human Gate round-trip and Architecture `REQUEST_CHANGES`/
`APPROVED` tests also pass. The operator operation creates no Human Review
Record, no `REQUEST_CHANGES`, no `APPROVED`, no Human revision increment, no
reviewer identity/time, and no fabricated feedback.

The supported pre-Human boundary remains:

`ARCHITECTURE_ESTABLISHED` -> `CANDIDATES_NORMALIZED`

An operator cannot rewind through an active Human Architecture approval from
Publication Preview.

## Profile-specific interactive Evidence contract

`run_evidence_v2_interactive.py` now validates an explicit record contract:

- Common fields are limited to `discovery_id`, `status`, `entity`,
  `artifact_type`, `claims`, `limitations`, `verification`, `materiality`,
  `materiality_rationale`, and `scope_dimensions`.
- `WEEKLY` additionally requires only `window_relation` and `carry_over`.
- `THEMATIC` additionally requires only `lineage_role`, `branch_ids`,
  `transition_ids`, `inheritance_note`, and
  `historical_attribution_caveat`.
- `RETROSPECTIVE_PERIOD` has no Thematic or Weekly-only record fields; its
  period annotations are derived by the existing Edition View semantics from
  common materiality/chronology inputs.
- `source_bindings` is permitted only as the explicit task-authority
  selection field.

Profile-inapplicable semantic fields fail closed. The module docstring now
states that Evidence source authority is either a Discovery-bounded source or
an exact task-bound Evidence Authority Supplement source. Single-source
legacy input remains compatible; multiple task-bound sources require explicit
`source_bindings`.

## Evidence Authority Supplement and active authority boundary

The previously implemented generic Evidence Authority Supplement contract is
retained. It binds exact repository-local Raw bytes, SHA-256, byte count,
locator, source class, publication/access metadata, and task identity without
changing Screening semantics. Evidence Cards can cite only task-bound
Discovery sources or validated supplement sources; arbitrary interactive URLs
remain prohibited.

Active Evidence and Edition View selection remains checkpoint-bound:

`Production State -> passed Evidence Stage Checkpoint provenance -> exact
Stage Checkpoint -> exact named artifact -> exact path/SHA validation`

Historical accepted directories, mtime, lexical order, and digest ordering are
not active-authority selectors. Historical accepted runs remain immutable when
new runs coexist.

## Targeted validation

The broad affected Core regression group passed:

`Ran 144 tests in 270.641s — OK`

This included the operator invalidation, Human Gate, agent control, Stage
Checkpoint, active Screening, Evidence/Card/acceptance, active Evidence/View,
interactive Evidence, agent-first Evidence, Selection/Architecture,
Completeness/Materiality, bootstrap/operator, and downstream publication
groups.

After adding the final Retrospective-only-field rejection case, the focused
repair set passed:

`Ran 28 tests in 50.434s — OK`

This is 20 operator invalidation tests plus 8 interactive Evidence profile and
source-binding tests. Syntax compilation and `git diff --check` also passed
for the changed source/test files.

## Full Python suite diagnostic

The local full-suite diagnostic completed as:

`Ran 768 tests in 278.006s — FAILED (failures=2, errors=3, skipped=6)`

The failures were classified as diagnostic-environment limitations, not
failures in the changed Core paths:

- three errors and one related failure require historical W32/Special release
  manifest files that are not present in this reconstructed scratch fixture;
- the operator workflow CLI smoke test returned `1` instead of its expected
  `2` because its intentionally isolated child interpreter did not have the
  locally target-installed `jsonschema` dependency after the test removed
  `PYTHONPATH`. The production workflow installs the requirements into its
  trusted runtime before invoking the CLI.

The workflow/bootstrap/operator targeted tests otherwise pass. No unrelated
manifest or dependency repair was added to this bounded Core branch.

## W34 exact read-only regression

The candidate Core was applied in a temporary detached checkout at
`weekly/2026-W34-v2-work@df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`. The
canonical W34 remote branch was never updated.

### Invalidation

- Gate: `ARCHITECTURE_REVIEW`
- Boundary: `CANDIDATES_NORMALIZED`
- Operation: PASS
- Human records created: `0`
- Human Review Index rows added: `0`
- Human provenance: `null` for Architecture Review and Publication Preview
- Final lifecycle: `CANDIDATES_NORMALIZED`
- Final next action before regeneration: Evidence stage
- Discovery/Screening remained passed; downstream checkpoints were pending

The invalidation record was temporary-fixture-local at:

`sources/2026-W34/execution/operator-invalidations/architecture-invalidation-0001.json`

The historical mutable canonical surfaces were superseded through the
operator path; accepted historical Screening/Evidence/View runs were retained.

### Supplement and formal regeneration

The temporary W34 supplement bound 61 substantive exact authority bodies with
60 unique Raw body SHA-256 values. It preserved all 80 non-DROP verification
attempts, including KEEP 45/45, INSPECT 16/16, and MAYBE 19/19. The
research-only classification remained VERIFIED 32, PARTIALLY_VERIFIED 27,
UNRESOLVED 14, and OUT_OF_WINDOW 7.

The old and new accepted runs coexist: 2 Evidence acceptance directories and
2 Edition View acceptance directories. The new active pair is:

- Evidence: `evidence/v2/accepted/bcf91f31d81935e0a48c1fde55f9d6db2192776b0d15a8cc11acfcc1ff9ee561/evidence-accepted.json`
- Edition View: `evidence/v2/views/accepted/43724d2264da8dff4892f7114c06d57060919d9b43f5248a7a0866b7b99ea102/edition-views-accepted.json`

The checkpoint-bound resolver selected those exact paths, not a directory
ordering heuristic. Its Evidence checkpoint authority was:

`orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json`

with checkpoint SHA-256
`661b8544867c17d7efa0b3ee2b1fd4f4db7411b5083e796b7377c2fbf2aab661`.

New Evidence status counts were `VERIFIED 32 / PARTIAL 27 / NEEDS_MORE 14 /
REJECTED 7`, replacing the prior `PARTIAL 80`. New Edition View counts were
`CONTEXT 41 / HOLD 31 / NON_MATERIAL 7 / MATERIAL 1`. The Materiality ledger
counts were `MATERIAL 1 / CONTEXT 41 / HOLD 31 / NON_MATERIAL 7 / DUPLICATE
4 / EXCLUDED 26`. Completeness remained `LIMITED` with concrete residual
authority, chronology, accessibility, and out-of-window boundaries.

Formal downstream progression reached `EVIDENCE_REVIEWED`,
`SELECTION_COMPLETE`, and `ARCHITECTURE_ESTABLISHED`. Selection counts were
`SELECTED 1 / HOLD 64 / INSPECT 15`. Architecture contained one package titled
`Verified developer-tooling change`.

The one-item Architecture and Selection result is recorded only as a
mechanism-regression outcome. It is not a semantic success criterion for
production W34 and must be reconsidered by the operator/Sol semantic process
after this Core candidate is accepted.

The final temporary State was:

- lifecycle: `ARCHITECTURE_ESTABLISHED`
- next action: `ARCHITECTURE_REVIEW`
- terminal reason: `HUMAN_GATE_REACHED`
- Architecture Review: pending
- Publication Preview: pending
- Human decisions: `0`

## Backward compatibility and retained limitations

- Existing editions without supplements retain the legacy single-source
  behavior.
- Existing accepted Screening/Evidence/View runs, Human history, and Git
  history remain immutable.
- The operator invalidation path does not cross actual Human approval.
- Retrospective interactive records use only the current Core's common inputs;
  no Thematic field is required or accepted.
- The full-suite diagnostic limitations above remain environment-specific and
  were not hidden by changing unrelated fixtures.

## Final handoff fields

- Workflow count: exactly `7` existing workflows; no eighth workflow added.
- Human Gate count: exactly `2` existing gates.
- Human review records created: `0`.
- Main writes: `0`.
- W34 writes: `0`.
- Sidecar runs: `0`.
- The exact ending maintenance-branch commit and
  `reviewed_repository_commit_sha` are the final remote commit SHA reported
  with this record after the non-force update; no post-handoff Human decision
  is implied.
