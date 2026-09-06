# Survey Production Core v2 Current Pending Human Gate Repair Validation r3

Date: 2026-09-06

Status: `READY_FOR_FRESH_SOL_REVIEW`

## Fixed-head scope

- Starting maintenance SHA: `41f499535fe7c7d482930d246c9af12462e058f6`
- Reviewed main SHA: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
- PR: `#484`
- W34 exact fixture SHA: `df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`

This is a bounded repair of the Sol finding that `target_gate` is the
eventual run destination, not the identity of the currently pending Human
Gate. No W34 artifact or branch was modified. No sidecar was run and PR #484
was not merged.

## Semantic repair

`scripts/survey_human_gate_v2.py` now derives the current pending Gate from:

1. `state.lifecycle_state`;
2. `config/survey-production-v2.json` `orchestration.gate_at_state`;
3. the configured Gate's `pending` status;
4. null Human Gate provenance; and
5. `terminal_reason == HUMAN_GATE_REACHED`.

Both live `invalidate_pending_gate()` and immutable
`validate_operator_invalidation_record()` use the same derivation. Neither
uses `state.target_gate == gate` as a current-Gate precondition.

`target_gate` is not mutated by invalidation and remains the eventual target
in the resulting State. The configured safe boundary policy is unchanged;
`operator_pending_gate_invalidation_boundaries.PUBLICATION_PREVIEW` remains
empty, so an operator cannot cross an approved Architecture from Publication
Preview.

## Mandatory positive regression

The fixture initializes with `target_gate = PUBLICATION_PREVIEW`, progresses
normally to `ARCHITECTURE_ESTABLISHED`, and retains:

- Architecture Review pending;
- Architecture Review provenance null;
- zero Human review records; and
- `terminal_reason = HUMAN_GATE_REACHED`.

The operator then successfully invalidates:

`ARCHITECTURE_REVIEW -> CANDIDATES_NORMALIZED`

The test verifies that lifecycle and checkpoint consequences are correct,
Human records remain zero, no Human decision is created, `target_gate` remains
`PUBLICATION_PREVIEW`, the operator record gate is `ARCHITECTURE_REVIEW`, and
immutable prior-State validation passes.

## Negative and rollback preservation

The operator invalidation suite covers 22 tests, including the prior
negative/rollback set and the new eventual-target/current-Gate mismatch. It
continues to cover non-pending Gates, lifecycle and terminal-reason mismatch,
stale commit/branch heads, State and Gate-input byte drift, missing or unsafe
Gate inputs, active provenance, existing Human records, invalid boundaries,
partial-cleanup rollback, immutable authority drift, and sequence
gap/duplicate rejection.

Existing Human Gate round-trip and Architecture `REQUEST_CHANGES`/
`APPROVED` semantics remain covered by the affected regression group.

## Validation

- Focused operator invalidation: `22 tests — PASS`
- Broad affected Core regression: `152 tests`, with all changed Core paths
  passing
- Syntax/compile validation: `PASS`
- `git diff --check`: `PASS`
- W34 exact regression: intentionally not executed by this task; the W34
  remote ref was verified read-only at `df3d0dfe...` and no W34 files were
  changed
- Sidecar tools executed: `0`
- Human review records created: `0`
- Force/reset/rewrite/rebase: unused

The one broad-suite failure is the pre-existing isolated CLI smoke
environment's missing `jsonschema` dependency; the production workflow
installs its trusted runtime requirements. It is not caused by the Gate
identity repair.

## Handoff boundary

This repair does not perform W34 Evidence regeneration, Architecture Review,
Publication Preview, sidecar QA, PR merge, main update, or seven-point audit.
The exact ending branch SHA and its parent are reported in the completion
handoff after the non-force branch update.
