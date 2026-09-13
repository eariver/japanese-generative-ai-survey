# W34 Luna — post-#483 Core sync and Screening recovery

## Authority and start guard

- Repository: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W34-v2-work`
- User-supplied Exact Starting SHA: `00991bbf080482436a8109b6a42a700cd291b3bd`
- Reviewed main SHA: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- Both remote start guards: **PASS** before writes.
- The instruction file contains an older embedded start SHA (`aa41ccd55ed630fa96c05efa3658bb403a779fba`); the current user request supplied the authoritative start guard for this continuation.

## Main synchronization

The reviewed `main` was merged into the existing W34 branch with a normal non-force merge. Merge commit:

`b8a0ae502fd03d17bcb4f5d9e1f67a26c77ab30e`

The W34 start is the first parent and reviewed `main` is the second parent. The merge was conflict-free, retained W34 edition-local artifacts, and adopted the reviewed shared-Core tree. No reset, rebase, rewrite, force update, or new branch was used.

## Affected-boundary revalidation

- Agent-first `validate_agent_state()` before package preparation: **PASS**.
- Accepted root Discovery: 40 records / 40 unique IDs; acceptance and Discovery checkpoint unchanged.
- Existing event-level input: 105 records / 105 unique IDs before repair.
- Historical Screening acceptance `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662`: retained unchanged and validated on its original 105-record basis.
- Historical 105 Sol decision authority: reused without mutation.

## Corrected current Screening basis

The temporary candidate was strictly UTF-8 decoded, JSONL-parsed, validated by the current `survey_screening_v2.validate_discovery_set()` and `validate_discovery_expansion()`, and then copied to the canonical current input only after those checks passed.

- Path: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- SHA-256: `9bfc0fc9b63f97cc9568dc53bb06595dd2540b92e843b55b2650abcbcc97aca2`
- Byte count: `297363`
- Records / unique IDs: `110 / 110`
- Existing 105-record prefix: byte-identical
- Accepted roots / accounted roots / unaccounted roots: `40 / 40 / 0`
- Event crosswalk: `W34-C001`–`W34-C105`, `105/105`, missing `0`, duplicate `0`
- Current crosswalk: `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.2.json`
- New children: five Sol-authorized `COVERAGE_PASSTHROUGH` records, each with one exact accepted parent, copied parent source, parent Raw paths only, and exact parent obligations.

The five coverage children are not new Weekly events and all receive the Sol-authorized `DROP` decision. DailyX/Grok/X material remains Discovery/community signal and is not promoted to technical Evidence.

## Screening package and acceptance

The canonical agent-first wrapper prepared and accepted a new package using current checkout implementation SHA `b8a0ae502fd03d17bcb4f5d9e1f67a26c77ab30e`.

- Package: `sources/2026-W34/screening/v2/prepared/w34-event-screening-r2/package.json`
- Package SHA-256: `4e53370d1f7f4b822698331c2a1a81bdf1cfc7e59d9600f87469932e495e6e79`
- Package schema / issue / profile: `2.0-rc1` / `2026-W34` / `WEEKLY`
- Input: 110 records, 3 batches (`43 / 44 / 23`)
- Corrected acceptance: `sources/2026-W34/screening/v2/accepted/5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98/screening-accepted.json`
- Corrected result-set SHA: `5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98`
- Corrected acceptance validation: **PASS**
- Decision totals: `KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 30 / TOTAL 110`
- Expected non-DROP Evidence tasks: `80`

The historical 105-run remains present, content-addressed, and byte-unchanged. The corrected run is a second immutable run.

## Formal Stage Checkpoint and bounded stop

Actual current-Core stage validation passed against the corrected acceptance. The canonical agent-first `advance-stage` machinery then created:

`sources/2026-W34/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`

and advanced the State to `CANDIDATES_NORMALIZED`. The passed Screening checkpoint binds the corrected acceptance by exact artifact path and SHA. `resolve_active_screening_acceptance()` returned only the corrected run; it did not use accepted-directory count, mtime, digest ordering, or latest-run heuristics.

The actual Core-derived next action is `stage:evidence-materiality-completeness`, the configured Evidence-stage handoff. No Evidence acceptance or downstream Evidence work was performed.

## Traceability and exclusions

- DailyX: 7/7 files, 76/76 topics.
- Grok r2: 47/47 URLs; `10 ORDINARY_WINDOW / 20 BACKGROUND_ONLY / 17 LATE_BREAKING`.
- Carry-over: one `RECHECKED_UNRESOLVED`, not promoted.
- External sidecars `eariver/publication-boundary-redteam` and `eariver/survey-core-v2-authority-auditor`: **not executed**.
- No Discovery rollback/reacceptance, accepted Discovery mutation, 105-decision reinterpretation, Evidence acceptance, Materiality, Completeness, Selection, Architecture, Human Gate, drafting, Freeze, or Release.
- No W33/SP001/SP002/SP003 or `main` production write.

## Durable validation

See `validation-v0.1.json` for hashes, exact paths, machine counts, immutable-boundary comparisons, and the complete changed-path inventory captured before the validation record itself was written.

## Diagnostic regression

- Targeted Core regression: 25 tests, 0 failures, **PASS**.
- Full Python discovery: `PYTHONPATH=. /tmp/w34-post483-recovery-MFXxnu/venv/bin/python -m unittest discover -s tests -p 'test*.py' -v`.
- Full result: 737 tests, 0 failures, 6 skipped, **PASS** (`Ran 737 tests in 307.938s; OK (skipped=6)`).

Final status: `READY_FOR_SOL_EVIDENCE`.
