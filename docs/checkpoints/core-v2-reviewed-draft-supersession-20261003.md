# Core v2 reviewed-Draft supersession repair — canonical worklog

Maintenance branch: `fix/core-v2-reviewed-draft-supersession-20261003`
Authority: `docs/checkpoints/2026-10-03-core-v2-reviewed-draft-supersession-repair-instruction.md`
(`EXECUTION_AUTHORITY / SHARED_CORE_MAINTENANCE / INVESTIGATE_FIRST / FIX_GENERIC_REVIEWED_DRAFT_SUPERSESSION_GAP / STOP_AT_SOL_CORE_REVIEW`)
Role: maintenance execution; Sol Core review separate, never claimed here. No merge to
`production/survey-core-v2` or `main`. No Human decision inferred or generated.

## 1. Startup guards (origin = source of truth)

Verified read-only before proof/commit (local staleness noted, not used):

- `origin/production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree
  `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` — PASS (local ref identical).
- `origin/main` HEAD `d6381568cc897a47d6de992189e20339350342b7` / tree
  `83ce3a216d852a1c32d0138f9c56fadefa800666` — PASS. (Local `refs/heads/main` is stale at
  `f823befe`; never used as authority, never written.)
- `origin/special/vision-multimodal-2026-work` HEAD `4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633` /
  tree `70b9c28158860ef19d0e0c87612abf9413255c17` — PASS. (Local `refs/heads/special/...`
  is stale at parent `78b770fb`; never used, never written. Disposable proof used a detached
  worktree pinned to exact `4d541ee`, removed afterwards.)
- Maintenance branch `fix/core-v2-reviewed-draft-supersession-20261003` starts from frozen Core
  `774dd39a` plus the instruction commit `789417ba952a1789368d35d2db68492c9409fc45`
  (pre-existing, not created by this work). No new branch, no reset/rebase/squash/force-push.
- Accepted Draft authority `79d2b3e291e10896ed616bd698abefc1e479ddbe` and candidate r3 PDF
  SHA-256 `637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795` confirmed in
  fixture (PDF bytes verified equal).

## 2. Defect reproduction (disposable detached worktree at exact `4d541ee`)

New Core overlaid read-only into the worktree (never committed there). Before establishment:

```text
validate_agent_state → 18 errors, all on the eligible revision surface:
Stage Checkpoint artifact drift: draft-result:P01, P02, P03, P04, P05, P06,
  P07A, P07B, P08, P09, P10, P11, P12, P13, P14, P15 (16),
  synthesis-input, synthesis-result (2)
```

Zero drift on `draft-package:*`, Architecture, Architecture approval, Selection, Candidate
Matrix, Evidence, Edition Views, Materiality, Completeness, Discovery/Screening, Production
Profile, contracts. Root cause matches the instruction: historical
`ARCHITECTURE_ESTABLISHED.json` rows are re-validated byte-exact against live paths, so
legitimately Sol-reviewed successor Draft bytes fail closed as drift with no sanctioned
rebind path. `DRAFT_COMPLETE → VALIDATED_DRAFT` stage validation and checkpoint advance are
consequently blocked before stage semantics.

## 3. Design (generic, no edition/profile special-casing)

- State-bound optional pointer `draft_revision_provenance: {path, sha256} | null` (schema +
  `initial_state`/`refresh` consistent). Absent/null = no authority; unreferenced record files
  are inert; referenced-but-invalid pointer fails closed; pointer persists across forward
  transitions; sanctioned Human-gate rollback that invalidates the `draft` checkpoint clears it
  deterministically (`survey_human_gate_v2._revised_state`); coexists with
  `publication_revalidation_provenance` (different checkpoints/surfaces, no global-latest).
- Versioned immutable records `{source_root}/draft/v2/draft-surface-revision-rN.json`
  (schema `schemas/draft-surface-revision.schema.json`): schema version, issue, reason class
  `REVIEWED_DRAFT_REVISION`, reason, `DRAFT_COMPLETE` lifecycle, exact prior Draft checkpoint
  authority, superseded rows (name/path/prior/new SHA/bytes), preserved rows, review binding
  (path/SHA/decision/reviewer), validation section (result/synthesis/architecture/approval SHAs),
  Core contract + implementation SHA, executor, recorded_at, exact `supersedes` link (null for r1),
  establishment snapshot. Old records never mutated; sequence discovery is State-driven, so a
  forged unreferenced higher-number file is inert.
- Eligible surface: only `draft-result:<id>`, `synthesis-input`, `synthesis-result`.
  `draft-package:*`, Architecture/approval, Selection/Matrix/Evidence/Views/Materiality/
  Completeness/Discovery/Screening/Profile/contracts remain ordinary drift (fail closed).
- Review authority: exact repository-local JSON `{decision: PASS, reviewed_by}` bound by
  path+SHA-256 in the record; `_check_review_authority` revalidates bytes/decision/identity on
  every resolve. No Human gate created or implied; unreviewed mutations cannot self-authorize.
- Establishment boundary: `DRAFT_COMPLETE` + Architecture approved + Publication Preview
  pending (and no preview provenance) + validation/freeze/release pending + exception inactive +
  intact Architecture-approval provenance + valid prior draft provenance. Post-validation
  establishment is rejected (lifecycle gate).
- Fresh validation reuses existing generic Draft validators: every current Draft Result vs its
  unchanged Package, exact package/result pairing, Architecture+approval binding,
  synthesis-input exact derivation from current Results, synthesis-result validation. No weaker
  parallel validator.
- One shared resolver: `survey_draft_revision_v2.resolve_active_draft_revision` (+
  `record_revised_rows` full-current-row map, `draft_superseded_map` compat) consulted by both
  `survey_agent_control_v2.validate_agent_state` and `survey_stage_validation_v2._prior_artifacts`.
  Bound prior Draft checkpoint rows validate against revised bytes; all other checkpoints keep
  current behavior. Recursive `_validate_record_tree` validates chains against parent revised rows
  with every link bound to the same historical prior checkpoint.
- Chaining: r2+ binds prior record by exact `{path, sha256}`, leaves it byte-identical, becomes
  sole active pointer. Partial-chain correctness uses full revised-row maps (not only the latest
  superseded delta) in agent-control, stage-validation, and publication-revalidation preserved-
  provenance checks (the latter was a real coexistence bug found by T18 and fixed here).
- Forward compatibility proven: `validate_agent_state` PASS → stage validation PASS → checkpoint
  creation + `advance_with_checkpoint` unmodified → pointer persists → historical checkpoint
  byte-identical.

## 4. Changed files

- `scripts/survey_draft_revision_v2.py` (new): authority module + `establish-draft-revision` backend.
- `scripts/survey_agent_control_v2.py`: draft-aware `_validate_checkpoint_record` (full revised rows),
  draft-aware `_verify_preserved_provenance` for publication revalidation, `establish-draft-revision`
  CLI (repo-relative review path handling).
- `scripts/survey_stage_validation_v2.py`: `_prior_artifacts` via shared resolver (full revised rows).
- `scripts/survey_human_gate_v2.py`: `_revised_state` clears orphaned `draft_revision_provenance`
  when the `draft` checkpoint is invalidated (record file itself untouched → inert evidence).
- `scripts/survey_production_v2.py`: `initial_state` carries `draft_revision_provenance: None`.
- `schemas/survey-production-state.schema.json`: optional nullable pointer field.
- `schemas/draft-surface-revision.schema.json` (new): record contract.
- `tests/test_survey_draft_revision_v2.py` (new): T1–T20 (+T17b) generic suite, real Draft validators,
  WEEKLY + THEMATIC/LONGFORM fixtures, no edition IDs in implementation.

No workflow, config, edition-artifact, or Human-approval changes.

## 5. New operation / API

- `scripts/survey_agent_control_v2.py establish-draft-revision --state --reason --executor
  --review <repo-relative JSON PASS> [--recorded-at] [--implementation-sha]`
- `survey_draft_revision_v2.establish_draft_revision(...)`,
  `resolve_active_draft_revision(...)`, `record_revised_rows(...)`, `draft_superseded_map(...)`.

## 6. Review-authority model

Structured PASS binding, never prose parsing. For TS-003 the Sol authority is the markdown
`execution/sol-draft-review-r9.md` (Decision `PASS`, worker `79d2b3e2`, exactly 4 authorized reader
edits P03/P07B/P15). Because the generic Core requires a JSON PASS object, the disposable proof
introduced a proof-only binding file
`execution/draft-r9-20261002/draft-r9-review-authority.json`
(`{decision: PASS, reviewed_by: Sol, review_reference: {path, sha256 of the Sol markdown},
reviewed_worker_commit}`) strictly inside the disposable worktree. The r1 record binds the binding
file by exact path+SHA, and the binding file pins the Sol markdown bytes. No file was created on,
or pushed to, the real TS-003 branch.

## 7. Focused test matrix (all green)

`tests/test_survey_draft_revision_v2.py`: 26 tests (T1–T20 + T17a/T17b + negatives) — OK.
T1 drift repro; T2 establish + history preserved; T3 package reject; T4 arch/approval reject (incl.
T4b); T5 selection/evidence reject (incl. T5b); T6 invalid result reject; T7 bad synthesis derivation
reject; T8 synthesis-result mismatch reject; T9 wrong prior reject; T10 forged unreferenced inert;
T11 corrupt/missing pointer fail-closed (incl. T11b); T12 missing/non-PASS/anonymous review reject
(incl. T12b/c); T13 chaining r2 + r1 immutable; T14 hook parity (`validate_agent_state` +
`_prior_artifacts`) + `establish-draft-revision` CLI via `python -m`; T15 stage validation PASS;
T16 advance binds revision + pointer persists + history immutable; T17a rollback clears stale pointer
(record file untouched); T17b post-`VALIDATED_DRAFT` establishment rejected with fail-closed drift;
T18 draft + later publication revalidation coexist (PDF rebuild + QA refresh, both pointers valid);
T19 WEEKLY vs THEMATIC genericity (distinct contracts, no special-casing); T20 historical bytes
untouched. Plus path-escape/symlink/duplicate/unknown-name/unchanged-byte negatives.

## 8. Regression results

- New suite + production: `test_survey_draft_revision_v2` + `test_survey_production_v2` → 38 tests OK.
- Agent-control + stage-validation: `test_survey_agent_control_v2` + `test_survey_stage_validation_v2` →
  8 tests OK.
- Publication revalidation + Human-gate revision + Human-gate + schema:
  `test_survey_publication_revalidation_v2` + `test_survey_human_gate_revalidation_revision_v2` +
  `test_survey_human_gate_v2` + `test_schema_syntax` → 38 tests OK.
- `py_compile` / `compileall` on touched scripts — OK. `__pycache__` removed; no stray files.

## 9. Disposable TS-003 proof (exact `4d541ee`, detached worktree, since removed)

1. Pinned detached worktree to `4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633`
   (tree `70b9c28158860ef19d0e0c87612abf9413255c17`); overlaid only the new Core files
   (uncommitted, worktree-local).
2. Pre-state: lifecycle `DRAFT_COMPLETE`, arch approved, preview pending,
   validation/publication_preview/freeze/release pending, no `draft_revision_provenance`.
3. Sol markdown SHA-256 `1ba2a1f514cc172769ebefe8749410fc56d56fda096ee71bb5352eb8f35503bb`;
   proof-only binding JSON SHA-256
   `f3bc4968a9f06ed8c118906dc4a884b54bc8399ba18a74b20d018af240792f2f`.
4. Established `sources/SP-vision-multimodal-2026/draft/v2/draft-surface-revision-r1.json`,
   SHA-256 `4e636b766dffd50ecc1d22b740de7b28d236cd00d58a756f7def9a0513c9f9ab`:
   18 superseded (16 `draft-result:P01–P15` incl. P07A/P07B + `synthesis-input`/`synthesis-result`),
   16 preserved (`draft-package:*`), review `{PASS, Sol}`, `supersedes: null`.
5. Historical `ARCHITECTURE_ESTABLISHED.json` SHA-256 before/after:
   `21f79321a5426cfeec850140b081edf5959f6f1835baed5df15170bd71a9b798` — identical.
6. `validate_agent_state` → `[]` (PASS).
7. Normal `DRAFT_COMPLETE` stage validation with accepted r3 family (manuscript, `main.tex`,
   38pp `main.pdf` `637877b8…49795`, quality bundle, semantic + visual reviews,
   reader-surface gate) → report `PASS`.
8. Built `CHECKPOINTS/DRAFT_COMPLETE.json` (disposable SHA
   `0f002c9aaf64693996c1696039e4edc8c12f490fdb771da4b00c59126658fa5b`) via
   `CORE_STAGE_CONTRACT` review and advanced to `VALIDATED_DRAFT` in the disposable worktree:
   pointer persisted, post-advance `validate_agent_state` PASS, historical checkpoint still
   `21f79321…`.
9. No Human Preview approval, no Freeze/Release, no lifecycle advancement outside the disposable
   worktree.

## 10. Real TS-003 / main / production untouched

- `origin/special/vision-multimodal-2026-work` before and after: `4d541ee…` / tree `70b9c28…` —
  unchanged (verified post-proof).
- Detached worktree removed via `git worktree remove --force`; no commit, push, or file write to
  the real TS-003 branch (local stale ref at `78b770fb` predates this work and was never moved).
- `origin/main` (`d6381568…`) and `origin/production/survey-core-v2` (`774dd39a…`) never written.
- All proof mutations (r1 record, binding JSON, disposable reports/checkpoints, advanced state)
  existed only inside the removed disposable worktree.

## 11. Candidate

This worklog is committed on the canonical work branch
`fix/core-v2-reviewed-draft-supersession-20261003` with the implementation and tests above.
Final HEAD/tree: see branch HEAD at push (`git rev-parse HEAD` / `git rev-parse HEAD^{tree}`);
the pushed commit is the exact Human Gate input. Push is normal (non-force) only.

## 12. Unresolved questions (for Sol Core review)

1. Record family name `draft-surface-revision-rN.json` vs the instruction's suggested
   `draft-surface-revalidation-rN.json` — semantics identical; naming is the only delta.
2. Review binding is strict JSON PASS; TS-003's Sol authority is markdown, bridged by a
   proof-only JSON binder pinning exact markdown bytes. If Core prefers direct markdown
   acceptance, that would be a deliberate heuristic-parsing relaxation — not recommended.
3. Instruction T17 is specified as post-validation boundary rejection; this suite covers it as
   T17b and additionally covers rollback pointer-clearing as T17a (required by §6.1).

## 13. Stop states

`CORE_V2_REVIEWED_DRAFT_SUPERSESSION_REPAIR_CANDIDATE_COMPLETE` /
`GENERIC_FAIL_CLOSED_REVISION_AUTHORITY_IMPLEMENTED` /
`HISTORICAL_DRAFT_CHECKPOINT_IMMUTABLE` /
`TS003_DISPOSABLE_DRAFT_R9_TO_VALIDATED_DRAFT_PROOF_PASS` /
`REAL_TS003_UNCHANGED` / `AWAITING_SOL_CORE_REVIEW`
