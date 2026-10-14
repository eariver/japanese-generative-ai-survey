# W41 r4 compat validation report (unmodified frozen Core)

Date: 2026-10-12 JST. Core files untouched (`git status` over config/schemas/scripts/.github/docs/AGENTS.md empty).

## 1. Failure reproduction (r1, unmodified Core)

`survey_evidence_v2.task_authority_sources` over `evidence/v2/packages/r1` tasks:
9 exact failures, all `unsupported source_type for Evidence authority: 'SECONDARY_OBSERVATION'`:
agr, nemotron-hf, nace-drex, nace-ndi, elevenlabs, tencent-hold, pixelcanary-hold, tbcvideo-hold, elyza-prewindow (task IDs in projection-ledger.json).

## 2. Projection proof (compat package, unmodified Core)

- Builder `execution/compat/evidence-source-class-projection-r4/build_projection_r4.py`: closed 9-set (unknown SECONDARY_OBSERVATION aborts); 36 tasks (9 projected + 27 passthrough byte-identical).
- DOUBLE_BUILD_IDENTICAL_PASS (tmp rebuild byte-equal incl. filenames).
- `task_authority_sources` 36/36 PASS with ZERO Core patching/override; 9 projected resolve to SECONDARY (sibling-consistent).
- Negative injection `BOGUS_UNREVIEWED_TYPE` → FAIL_CLOSED_PASS.

## 3. Supplement proof (unmodified Core)

- 7 raw excerpt files (5,xxx B total) under `external/evidence-supplement/r4/`; manifest `evidence-authority-supplement-r4.json` via `build_evidence_authority_supplement`: 8 entries, `validate_evidence_authority_supplement` PASS (raw SHA/bytes, discovery/screening binding, task identities, class==map).

## 4. Derived r2 package proof (unmodified Core)

- Builder `build_r2_package.py`: 36 tasks (9 projected + supplement bindings on 8 tasks), authority_supplement + contracts.supplement; DOUBLE_BUILD_IDENTICAL_PASS.
- `validate_evidence_package_basis` PASS (override context covers only historical state-basis wrapper, same as agent-tool; no source-map override).
- `task_authority_sources` 36/36 PASS, unmodified Core.

## 5. Card/View proof (unmodified Core)

- Input `results/r2/interactive-evidence-input-r2.json` (36 records, runner muse-spark) `validate_interactive_input` PASS (exact non-DROP coverage + completeness obligations).
- `_build_card` + `validate_evidence_card(..., repo_root=...)` 36/36 PASS: 3 VERIFIED / 21 PARTIAL / 12 NEEDS_MORE; 21 MATERIAL / 13 HOLD / 2 CONTEXT.
- Key fixes: nanobanana/synthid/drex/mistral/egemma/textgrain/decisions/ultrafast cite PRIMARY_OFFICIAL supplements alongside lineage src-1; clef weight-repo-status VERIFIED→UNRESOLVED; decisions VERIFIED scoped to changelog (pricing UNRESOLVED).
- `validate_edition_view` 36/36 PASS (provisional card-SHA binding; NOT acceptance).

## 6. Non-regression

- r1 package/results/views, canonical Discovery (37), Screening acceptance (37), production-state.json: bytes unchanged except state-independent additions (verified via git status allowlist + SHA spot checks).
- No `accept_evidence_results`, no views acceptance, no ledger, no EVIDENCE_REVIEWED, no Selection/Architecture/Human Gate.
