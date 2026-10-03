# TS-003 VM-D112 Cross-Gate Re-entry Attempt — Execution Record (2026-10-03)

- Authority: already-given Human decision (Publication Preview r1 REQUEST_CHANGES,
  boundary DISCOVERY_COLLECTED, VM-D112 pipeline intake, Core Freeze preserved).
  No new decision inferred or requested.
- Terminal: blocked — frozen Core rejected the operation (exact error below).
  No workaround attempted.

## Start guard (§3)

- Expected HEAD `3f3ff84331cf370743d690b3e5c78693291a8a63` — remote HEAD MATCH
- Expected tree `5f5a48c3c12f01c3ae26a0fca6e6bf13bd84baa7` — remote tree MATCH
- Local HEAD identical, clean tree, no new branch.

## Human re-entry authority (§5)

- Immutable record: `sources/SP-vision-multimodal-2026/execution/reviews/human-publication-preview-r1-request-changes-vm-d112-reentry-20261003.md`
  (quotes the actual Human decision verbatim; classified as REQUEST_CHANGES /
  upstream-regeneration, not any approval).

## Canonical operator request (§6)

- Immutable request: `sources/SP-vision-multimodal-2026/execution/requests/ts003-vm-d112-cross-gate-reentry-20261003.json`
- `kind: REQUEST_PUBLICATION_PREVIEW_REVISION`, `expected_revision: 1`
  (first Publication Preview review; review-index has no publication-rN),
  `reviewed_repository_commit_sha: 3f3ff84331cf370743d690b3e5c78693291a8a63`
  (request-commit parent), `regeneration_boundary: DISCOVERY_COLLECTED`,
  `reviewed_by: Human Owner`, `reviewed_at: 2026-10-03T12:00:00+09:00`
  (Human decision date 2026-10-03 JST, day-precision),
  `reviewed_main_sha: d6381568cc897a47d6de992189e20339350342b7`
  (start-of-run reviewed main; schema-conformant, local execution only),
  `recorded_at: 2026-10-03T11:40:00Z`.
- Schema validation against frozen `schemas/operator-execution-request-v2.schema.json`: PASS.
- Request commit `3275ec94223fabff3db1553b72b274d2e8fcfc64` (parent =
  reviewed commit, per Core trust rule), pushed to the canonical work branch.

## Bridge execution (§7) — REJECTED by frozen Core, exact error

- Command: `python3 scripts/survey_core_execution_bridge_v2.py --repo-root . --request <request> --event-sha 3275ec94223fabff3db1553b72b274d2e8fcfc64 --ref-name special/vision-multimodal-2026-work`
- Exit code: `2`. No receipt (rejected in pre-execution gate check).
- Exact stderr:

```text
Production State is not resumable: Stage Checkpoint artifact drift: publication-pdf; Stage Checkpoint artifact drift: quality-regression-bundle; Stage Checkpoint artifact drift: reader-manuscript; Stage Checkpoint artifact drift: reader-surface-gate; Stage Checkpoint artifact drift: semantic-review; Stage Checkpoint artifact drift: validated-source; Stage Checkpoint artifact drift: visual-review
```

- Cause analysis (read-only, no Core change): the seven drifted artifacts are
  pinned by historical checkpoint `DRAFT_COMPLETE.json` at pre-rebuild SHAs;
  the later governed #559 cycle rebuilt PDF/TeX and revalidated artifacts
  without rebasing that checkpoint. The drift is pre-existing edition-local
  data state (proven identical on the clean starting tree; unrelated to this
  turn's files) — not a Core defect. `_canonical_existing_state` therefore
  refuses every bridge operation until the state is resumable, and no
  allowlisted operation repairs checkpoint drift. No workaround was attempted:
  no manual state imitation, no Core patch, no checkpoint rewrite.
- Working-tree effect of the failed run: none (no tracked modifications;
  only an empty untracked `bridge-runs/<request_id>/` directory, which git
  does not track).

## Downstream stages (§§9–18) — NOT EXECUTED (blocked)

- Canonical Discovery 112 / Screening / Evidence / Views / Materiality /
  Completeness / Selection / Architecture regeneration: not started — the
  pipeline never legitimately re-entered DISCOVERY_COLLECTED.
- r8 repairs (VM-D084 V1, VM-D010, VM-D091, VM-D106): untouched, no regression.
- SSv2 purge state: unchanged (fresh r8/v4 chain clean; r14 wording stale as before).
- Reader r15 / TeX / PDF / Preview / Freeze / Release: none (forbidden in any case).

## Lifecycle safety (§23)

- `production-state.json` untouched: `RELEASE_CANDIDATE`, `publication_preview = pending`,
  `freeze = pending`, `release = pending`. No gate record created
  (no publication-r1 entry; review-index unchanged). No approval fabricated.

## Core v2 Freeze (§4, §20, §22)

- `Core v2 Freeze: PRESERVED`
- `Shared Core files changed: NO` (verified: no tracked modifications under
  `config/`, `schemas/`, `scripts/`, `docs/`; full `git status` clean apart
  from the edition-local records committed below).
- Frozen validators (including `validate_discovery_expansion`) untouched.

## Final HEAD/tree

- Records committed as a normal commit on the existing branch (non-force pushed);
  final HEAD/tree reported in the turn final report.
