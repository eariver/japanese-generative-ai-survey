# r13 timestamp provenance correction (immutable notice; no history rewrite)

Status: `PROVENANCE_CORRECTION / NONAUTHORITATIVE / NO_REWRITE`
Date recorded: 2026-10-18 JST (verified executor clock `date -u`: 2026-10-17T18:2xZ = 03:2x JST; git author dates use +0900 consistently).

## Observed discrepancy (M06)
- r12 `*_draft-result-r12.PROPOSED.json` carry `runner.generated_at = 2026-10-18T03:00:00Z`; r12 proposed synthesis `generated_at = 2026-10-18T04:00:00Z`.
- r12 work commit `456f662e4` authored `2026-10-18 02:47:18 +0900` (= 2026-10-17T17:47:18Z); proposal file mtimes `2026-10-18 02:42 JST` (= 2026-10-17T17:42Z).
- Therefore the r12 stamps labeled `Z` (UTC) are ~9–10h AHEAD of the true generation/commit instants.

## Evidence
1. `git log --format=%ad/%cd` (all commits in this lane use `+0900` author/committer dates; no TZ anomaly in git itself).
2. Filesystem mtimes of r12 outputs: `2026-10-18 02:42 JST` — minutes BEFORE the 02:47 JST commit, consistent with generate-then-commit in JST wall-clock.
3. The r12 stamps `03:00Z/04:00Z Oct 18` coincide numerically with the JST wall-clock generation window (02:xx–04:xx JST), not with UTC.
4. Executor clock verified live during r13 (`date -u` ↔ `date` agree on +0900 offset).

## Assessment
- Most probable mechanism: JST wall-clock values written with a `Z` (UTC) suffix — a timezone-labeling error by the r12 executor, NOT evidence of intentional future-dating (content is identical either way; no gate depends on these stamps).
- Intent cannot be proven from repository bytes; no allegation of fabrication is made. Unknown remainder explicitly marked as unknown.
- r12 files and commits are historical and MUST NOT be rewritten (rewriting would destroy the evidence this notice relies on).

## r13 rule (fail-closed)
- Every r13 `generated_at` MUST be taken from verified executor UTC (`date -u`) at build time and cross-checked against file mtimes before commit.
- If a required timestamp cannot be verified, mark source `unknown` in NONAUTHORITATIVE metadata and fail closed (do not invent).
- r13 build stamps recorded in `validation-report-r13.md` with the verification commands.
