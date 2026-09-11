# Core v2 repair — Drafting resolves effective Screening Discovery basis (DERIVED_EXPANSION)

Status: `PLANNED / IMPLEMENTATION_PENDING / TESTS_PENDING`

Execution identity: `Execution agent: Muse Spark 1.3`
Execution mode: `SHARED_CORE_MAINTENANCE_IMPLEMENTATION`

Maintenance branch: `fix/core-v2-drafting-derived-discovery-basis-20260911`
Exact Starting main SHA: `6d748a962d57beff89da7c1b20cb5a9a86c8e261`
Exact Starting main tree: `672ea7ba23662a8015c120ab3ab17bb058be200e`
W34 reproduction SHA (read-only): `ff95a093efe788457c15bf75ac52516bb2649523`
W34 reproduction tree (read-only): `adf32a76d319211cdb2cdc1ea43621d7ad5d5d82`
W34 defect authority (read-only):
`sources/2026-W34/execution/defects/w34-drafting-expansion-discovery-basis-20260911.md`
at `weekly/2026-W34-v2-work@ff95a093efe788457c15bf75ac52516bb2649523`

Pre-write guards (verified read-only before branch creation, re-verified on resume):
- remote `main` HEAD == `6d748a962d57beff89da7c1b20cb5a9a86c8e261` — MATCH
- remote `main` tree == `672ea7ba23662a8015c120ab3ab17bb058be200e` — MATCH
- maintenance branch absent on remote before creation — MATCH (local-only branch created from exact SHA)
- remote W34 HEAD == `ff95a093efe788457c15bf75ac52516bb2649523` — MATCH
- W34 tree == `adf32a76d319211cdb2cdc1ea43621d7ad5d5d82` — MATCH (informational)

## 1. Defect symptom

Canonical Drafting fails at WU-009 upstream basis load for every package with:

```text
WU-009 upstream Architecture basis invalid:
Screening acceptance points at a different Discovery set
```

No Draft artifact is written. Stages through Architecture (root Discovery →
validated DERIVED_EXPANSION → effective Screening Discovery → Screening →
Evidence → Selection → Architecture) pass; only Drafting Candidate Matrix
re-derivation fails.

W34 concrete values (read-only reference):
- Root Discovery `sources/2026-W34/discovery/discovery-v2.jsonl` — 369 records
- Effective Screening Discovery `sources/2026-W34/screening/input/event-discovery-v2.jsonl` — 439 records
- Screening acceptance `.../screening/v2/accepted/41503363.../screening-accepted.json`
- `resolve_effective_discovery_basis()` mode = `DERIVED_EXPANSION` (clean)

## 2. Root cause hypothesis

`scripts/survey_drafting_v2_base.py::_load_drafting_basis()` passes the caller-supplied
`discovery_path` verbatim into `architecture.validate_candidate_matrix(...)`, which
re-derives via `_load_upstream` → `evidence.validate_screening_acceptance(...)`.
That validator requires the caller path to equal the Screening package's **effective**
Discovery path (`effective["path"]`).

The Drafting runner (`scripts/run_drafting_synthesis_v2_interactive.py::_upstream()`)
always supplies the **root** Discovery path (via `discovery-accepted-v2.json`).
For `DIRECT` bases (root == effective) this passes; for any validated
`DERIVED_EXPANSION` (effective != root) it deterministically mismatches.
This is a shared-Core basis-resolution defect in the Drafting common layer, not an
edition data error. Same defect family as the 2026-09-04 Screening-expansion
authority gap (Evidence repaired via PR #484); the Drafting re-derivation path was
not covered.

## 3. Intended repair design (profile-neutral, generic)

In `_load_drafting_basis()`, before Candidate Matrix validation, resolve the
canonical effective Discovery basis from the validated Screening package:

```text
caller discovery_path + screening acceptance (screening-accepted.json)
  -> verify sibling package.json binding (exists, regular safe file,
     acceptance package_sha256 == actual package SHA)
  -> screening.validate_package_basis(...) (reuse existing)
  -> screening.resolve_effective_discovery_basis(...) as single source of truth
     (root path / effective path / mode; expansion provenance stays intact)
  -> caller discovery_path must equal trusted root OR trusted effective
     (resolved absolute paths); unrelated third path -> FAIL CLOSED
  -> pass trusted effective path to architecture.validate_candidate_matrix(...)
```

- `DIRECT` (root == effective): behavior identical to before.
- `DERIVED_EXPANSION`: canonical root caller is resolved through the validated
  expansion to the effective derived Discovery used for Matrix re-validation.
- No root→derived validation is re-implemented in Drafting; the existing resolver
  remains the authority. No W34/issue/count/SHA/profile literals or branches.

Caller entry points covered (all pass through `_load_drafting_basis`):
ordinary Draft package path, cross-package synthesis path
(`scripts/survey_drafting_v2.py` wrapper delegates / calls base loader), direct
Drafting API callers.

## 4. Scope

- `scripts/survey_drafting_v2_base.py` — the repair (import screening module,
  resolve + identity-check + pass effective path).
- Minimal test fixture/helper adjustments only if an existing helper interface
  forces it; existing `resolve_effective_discovery_basis()` API reuse first.
- New focused regression test file (e.g.
  `tests/test_survey_drafting_effective_discovery_basis.py`) if no natural
  existing file fits; prefer extending existing Drafting tests where natural.

## 5. Non-goals

- No W34 production writes (W34 branch is strictly read-only for this work).
- No change to approved W34 Architecture / Evidence / Selection / State.
- No weakening of expansion provenance validation.
- No schema / config / lifecycle / Human Gate semantics changes. If such a change
  appears necessary, stop and request Sol review instead of widening scope.
- No W34-specific branching, path literals, count dependence (369/439),
  result-set SHA dependence, or WEEKLY-only special cases.

## 6. Authority / security invariants to preserve

- Sibling `package.json` is never trusted "because it is there": require exists +
  regular safe repository-local file (reject symlink/missing) + acceptance
  `package_sha256` == actual SHA, plus existing `validate_package_basis` checks.
- Existing `resolve_effective_discovery_basis()` provenance checks stay intact:
  root path/SHA, derived path/SHA, record counts, preservation of all root
  identities, conflicting root records, new identity count, root coverage
  completeness, parent reconstruction. Drafting only *consumes* that authority.
- Caller Discovery allowlist: trusted root or trusted effective only; unrelated
  path fails closed (no silent substitution).
- Human Gate semantics, lifecycle semantics, Selection/Architecture/Evidence/
  Screening data models unchanged.

## 7. Planned changed paths

- `scripts/survey_drafting_v2_base.py` (production repair)
- `tests/test_survey_drafting_effective_discovery_basis.py` (new; name subject to
  repo convention final check) — requirements A–G + Drafting integration
  regression (DIRECT + DERIVED_EXPANSION, incl. synthesis wrapper path)
- This document (updated in place through implementation/testing)

Expected no-change areas: `schemas/`, `config/`, lifecycle, Human Gate semantics,
Screening/Evidence/Selection/Architecture data models, W34 production bytes.

## 8. Planned tests

- A. DIRECT compatibility: root == effective still PASSes Drafting basis validation.
- B. Valid DERIVED_EXPANSION from root caller: loader resolves effective derived
  Discovery; Candidate Matrix validation PASSes (core regression).
- C. Valid DERIVED_EXPANSION from effective caller: PASSes (or documented reason +
  fixed expectation if the API contract should forbid it).
- D. Unrelated Discovery rejected: FAIL CLOSED.
- E. Package binding tamper (sibling missing / acceptance package_sha256 mismatch /
  actual SHA mismatch): FAILs.
- F. Derived Discovery drift from package-declared SHA: FAILs.
- G. Expansion provenance corruption representative cases (root identity loss,
  conflicting root record, incomplete root coverage, invalid parent
  reconstruction): Drafting path does not PASS; map to existing resolver coverage
  where already covered instead of mass-duplicating tests.
- Integration: synthetic fixture root → DERIVED_EXPANSION → Screening acceptance →
  Evidence/Matrix authority → Draft Package derivation reaches derivation without
  WU-009 mismatch; DIRECT fixture still passes; synthesis wrapper
  (`survey_drafting_v2.py`) same effective-basis semantics where feasible.
- Existing suites: Screening/expansion authority, Evidence, Candidate
  Matrix/Architecture, Drafting, cross-package synthesis Drafting, Agent/Core
  state, Human Gate regression; then broader Core suite + pipeline contract suite.
- W34 exact read-only reproduction with candidate code: upstream basis load /
  Draft Package derivation over real W34 bytes (all 7 Architecture packages if
  feasible) no longer emits `Screening acceptance points at a different Discovery
  set`; outputs confined to /tmp/disposable worktree/ignored temp area.
- Negative W34 validation on temp-fixture copies (derived SHA / package SHA /
  root-derived relationship corruption still fail closed). Real W34 bytes never
  mutated.

## 9. CI plan

- Local: focused new regression → related existing suites → broader Core suite →
  pipeline contract suite → W34 read-only reproduction → exact candidate CI.
- Push logical checkpoints: (1) this policy doc, (2) implementation + focused
  regression, (3) final test-result/document closeout. Fresh remote HEAD check
  before each push; remote HEAD read-back after each push. No force push / reset /
  rebase / amend of published commits / squash.
- After PR: fix candidate HEAD, run existing Core CI + pipeline contract CI on the
  exact SHA; no Human review on failure — fix, rerun, update this document.

## 10. W34 resume plan (downstream, not this branch)

After shared-Core repair lands via normal change management: rerun W34 Drafting
cleanly from the parked approval state through the canonical wrapper, continue
`DRAFT_COMPLETE` → validation/PDF → `VALIDATED_DRAFT` → Boundary Validator →
Candidate → `RELEASE_CANDIDATE` → Auditor → `SOL_PUBLICATION_PREVIEW_REVIEW_READY`.
No hand-authored Draft/approval/state/index bypass records.

## 11. Tests / results

`PENDING — no test result claimed yet.` No test has been executed for this repair;
no PASS is claimed. Iteration log follows in execution order (failures preserved,
not hidden):

### Test iteration log

(none yet)

### Focused new regression

(none yet)

### Related existing suites

(none yet)

### Broader Core suite

(none yet)

### Pipeline contract suite

(none yet)

### W34 read-only reproduction

(none yet)

### Negative validation

(none yet)

### GitHub Actions (exact-head CI)

(none yet)

## 12. Repair content (final)

PENDING — implementation not started.

- Changed files: (pending)
- Function-level changes: (pending)
- Why root/effective mismatch resolves: (pending)
- DIRECT impact: (pending)
- DERIVED_EXPANSION impact: (pending)
- Fail-closed preservation: (pending)
- Design deviations from §3 with reasons: (pending)

## 13. Final candidate record (final)

PENDING.

- Candidate HEAD: (pending)
- Candidate tree: (pending)
- Changed paths: (pending)
- Residual limitations: (pending)
- W34 read-only reproduction result: (pending)
- Downstream resume implication: (pending)

---
Markers (target at handoff): `SHARED_CORE_DEFECT_REPRODUCED`
`REPAIR_POLICY_DOCUMENTED_BEFORE_CODE_CHANGE`
`DIRECT_DISCOVERY_BASIS_REGRESSION_PASS`
`DERIVED_EXPANSION_DRAFTING_REGRESSION_PASS`
`UNRELATED_DISCOVERY_FAIL_CLOSED_PASS`
`EXPANSION_PROVENANCE_NOT_WEAKENED`
`W34_READ_ONLY_REPRODUCTION_PASS`
`EXACT_HEAD_CI_PASS`
`W34_PRODUCTION_UNCHANGED`
`HUMAN_APPROVAL_NOT_GENERATED`
`SOL_CORE_REPAIR_REVIEW_READY`
