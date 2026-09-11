# Core v2 repair — Drafting resolves effective Screening Discovery basis (DERIVED_EXPANSION)

Status: `IMPLEMENTED / FOCUSED_AND_RELATED_PASS / FULL_SUITE_AND_W34_RUNNING`

(Interim status. Final states per mission §20 will be set exactly:
`IMPLEMENTED / LOCAL_TESTS_PASS / W34_READ_ONLY_REPRODUCTION_PASS / CI_PENDING`
after local + W34 pass, then
`IMPLEMENTED / TESTED / EXACT_HEAD_CI_PASS / SOL_CORE_REPAIR_REVIEW_READY`
after exact-head CI passes.)

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
- New focused regression test file
  `tests/test_survey_drafting_basis_v2.py` (renamed from the task's example so
  the Core CI `test_survey_*_v2.py` pattern also matches) — requirements A–G +
  Drafting integration regression (DIRECT + DERIVED_EXPANSION, incl. synthesis
  wrapper path)

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

No PASS is claimed for suites that have not been executed. Iteration log in
execution order (failures preserved, not hidden):

### Test iteration log

- Iteration 0 (pre-fix reproduction, read-only, disposable worktree
  `/tmp/w34-repro` at `ff95a093...`, maintenance-branch code at base commit
  `980d18b2` with production code still at Starting-SHA state):
  command: `python3 /tmp/w34-defect-repro.py`
  result: REPRODUCED — `validate_candidate_matrix` with the canonical root
  Discovery path returned
  `['Screening acceptance points at a different Discovery set']`;
  resolver mode `DERIVED_EXPANSION`, root 369 records, effective 439 records,
  caller==trusted root True, caller==trusted effective False.
  Marker: `SHARED_CORE_DEFECT_REPRODUCED`.
- Iteration 1 (focused new regression, post-fix):
  command: `python3 -m unittest tests.test_survey_drafting_basis_v2 -v`
  (8 tests; file renamed from the task's example name so it matches the Core CI
  pattern `test_survey_*_v2.py` as well as `test_*.py`)
  result: PASS — 8 tests, 0 failures, 0 skipped (~4s).
- Iteration 2 (guard proof that the new tests detect the defect):
  `git stash push -- scripts/survey_drafting_v2_base.py` (pre-fix production
  code), reran `test_derived_expansion_from_root_caller_passes` → FAILED with
  `ValueError: WU-009 upstream Architecture basis invalid: Screening acceptance
  points at a different Discovery set` (2 errors: THEMATIC + WEEKLY subtests);
  `git stash pop` restored the fix. The regression test guards the defect.
- Iteration 3 (related existing suites, post-fix):
  - `tests.test_survey_drafting_v2 tests.test_survey_drafting_integrity_v2
    tests.test_survey_draft_profile_v2
    tests.test_survey_interactive_drafting_cross_package_refs_v2`:
    PASS — 13 tests, 0 failures.
  - `tests.test_screening_expansion_authority_v2 tests.test_survey_screening_v2
    tests.test_survey_active_screening_acceptance_v2`: PASS — 22 tests, 0 failures.
  - `tests.test_survey_evidence_v2`: PASS — 12 tests, 0 failures.
  - `tests.test_survey_architecture_v2 tests.test_build_draft_packages
    tests.test_survey_drafting_historical_json_binding_v2`: PASS — 15 tests, 0 failures.
  - `tests.test_survey_agent_control_v2 tests.test_survey_agent_tool_v2
    tests.test_survey_human_gate_v2 tests.test_survey_human_gate_audit_matrix_v2`:
    PASS — 25 tests, 0 failures (362.5s; pre-existing slow suite).
- Iteration 4 (broader full suite): `python3 -m unittest discover -s tests -p
  'test_*.py'` (== pipeline contract suite command) started in background,
  log `/tmp/full-suite.log` — RUNNING at document update time.
- W34 read-only post-fix verification: 7-package `derive_draft_package` over
  real W34 bytes (`python3 -u /tmp/w34-postfix-verify.py`, log
  `/tmp/w34-postfix-verify.log`) — RUNNING. Pre-existing per-card Evidence
  validation cost dominates (~325s for 409 cards; unchanged by this repair —
  the repair only adds one resolver pass of ~seconds). Staged timing probe
  (`/tmp/w34-stage-timing.py`, log `/tmp/w34-stage-timing.log`): screening
  acceptance 2.7s PASS, evidence acceptance 325.2s PASS (409 results), views /
  ledger / completeness / matrix re-derivation pending.
  Final per-package outcome pending; basis load is package-independent so the
  first passing package already proves the mismatch-gone claim for the shared
  path, with all-7 confirmation to follow if the run completes in time.

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

### Changed files

- `scripts/survey_drafting_v2_base.py` (production repair only; +53 lines):
  - new import `from scripts import survey_screening_v2 as screening`
    (cycle-safe: `survey_evidence_v2` already imports it at top level; the
    screening module only imports `survey_production_v2` at top level);
  - new helper `_resolve_effective_screening_discovery(repo_root,
    screening_path, discovery_path, implementation_sha) -> Path`;
  - `_load_drafting_basis()` now passes the helper's trusted effective path
    (instead of the verbatim caller path) into
    `architecture.validate_candidate_matrix(...)`.
- `tests/test_survey_drafting_basis_v2.py` (new, 8 tests; name chosen so both
  CI patterns match: Core CI `test_survey_*_v2.py` and pipeline contracts
  `test_*.py`).
- This document (updated in place).

No schema / config / lifecycle / Human Gate / data-model changes. No
`survey_screening_v2.py` helper changes were needed — the existing API was
reused as-is. No `run_drafting_synthesis_v2_interactive.py` change — it flows
through the repaired loader.

### Function-level changes

`_resolve_effective_screening_discovery` (all generic, no issue/profile/count
literals):
1. loads the Screening acceptance (`screening-accepted.json`); missing/invalid
   bytes → `ValueError` fail closed;
2. requires a non-empty `package_sha256` binding in the acceptance;
3. derives sibling `package.json`; rejects symlink/missing (`is_symlink() or
   not is_file()`); requires actual SHA == acceptance `package_sha256`
   (same message as the downstream Evidence check:
   `accepted Screening package copy is missing or changed`);
4. reuses `screening.validate_package_basis(...)` (profile/state/discovery
   SHAs, prompt/result contracts, State basis — identical to what downstream
   re-checks);
5. reuses `screening.resolve_effective_discovery_basis(...)` as the single
   source of truth for trusted root path / trusted effective path / mode
   (expansion provenance validation untouched);
6. admits caller Discovery only if its resolved absolute path equals the
   trusted root OR the trusted effective path; any third path → `ValueError`
   (`Drafting Discovery basis does not match validated Screening
   root/effective Discovery basis`); returns the trusted effective path.

### Why the root/effective mismatch resolves

Downstream `evidence.validate_screening_acceptance` demands caller path ==
effective path. Previously Drafting forwarded the canonical root path, which
differs from effective exactly when the Screening package is a validated
`DERIVED_EXPANSION`. Now Drafting resolves root→effective through the same
validated authority and forwards the effective path, so re-derivation compares
identical bytes. `DIRECT` (root == effective) resolves to the caller path
itself — behavior identical to before (locked by
`test_direct_basis_resolution_is_identity`).

### DIRECT impact

None (identity). Existing Drafting/Screening/Evidence/Architecture suites pass
unchanged.

### DERIVED_EXPANSION impact

Repaired: root callers and effective callers both pass; synthesis wrapper
shares the loader so both its paths are repaired (ordinary path locked by
wrapper-level test, synthesis path locked by `pkg-002` test).

### Fail-closed preservation

Unrelated Discovery rejected; sibling missing/SHA-mismatch rejected; derived
drift rejected (package-declared SHA); provenance corruption blocked at the
shared resolver (acceptance cannot be produced, so Drafting input can never
exist). No new trust in nearby files; no silent substitution.

### Design deviations from §3 with reasons

- Test file renamed to `tests/test_survey_drafting_basis_v2.py` (Core CI
  pattern inclusion). No production-design deviation.

## 13. Final candidate record (final — interim values, pending full suite + W34 + CI)

- Candidate HEAD: (pending — checkpoint 2 commit to be recorded after push)
- Candidate tree: (pending)
- Changed paths: `scripts/survey_drafting_v2_base.py`,
  `tests/test_survey_drafting_basis_v2.py`,
  `docs/checkpoints/core-v2-drafting-derived-discovery-basis-repair-20260911.md`
- Residual limitations: (pending final runs; known: full W34 basis re-derivation
  is slow on real data — ~325s Evidence re-validation per pass, pre-existing
  Core behavior unchanged by this repair)
- W34 read-only reproduction result: (running — see §11 iteration 4)
- Downstream resume implication: (pending — W34 resumes after this repair lands)

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
