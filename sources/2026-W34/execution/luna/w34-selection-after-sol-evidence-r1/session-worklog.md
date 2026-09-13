# W34 Selection after Sol Evidence r1 — Luna/Work execution worklog

Execution agent: Muse Spark 1.3

Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION

Role boundary: mechanical materialization / validation / checkpoint only.
Sol owns all Selection semantics via
`sources/2026-W34/execution/reviews/sol-selection-directive-20260909-r1.md`.
No Discovery / Screening / Evidence / Views / Materiality / Completeness rerun.

## Exact guard (verified read-only before any write)

- Repository: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W34-v2-work`
- Exact Starting SHA: `030eb723c12282f0cfd09aaada05d14f0c0906c7`
- Expected Starting Tree: `aba25c36b1119a6f48b6bdf7af5106dd34298f7a`
- Reviewed main SHA: `6d748a962d57beff89da7c1b20cb5a9a86c8e261`
- Remote verification (GitHub API + `git ls-remote`, read-only):
  - remote W34 HEAD = `030eb723c12282f0cfd09aaada05d14f0c0906c7` (MATCH)
  - remote W34 tree = `aba25c36b1119a6f48b6bdf7af5106dd34298f7a` (MATCH)
  - remote main HEAD = `6d748a962d57beff89da7c1b20cb5a9a86c8e261` (MATCH)
- Local work branch fast-forwarded `46a9ef78..030eb723` (6 commits, ff-only,
  no reset/rebase/rewrite) to the exact starting SHA before execution.

## Upstream basis (immutable, reused — not regenerated)

Resolved from the State-bound `CANDIDATES_NORMALIZED` checkpoint
(implementation `f062a12386d20a96d91eebe4d2d9f083181cd644`, NOT rewritten):

- profile: `sources/2026-W34/production-profile.json`
- discovery (effective Screening basis, DERIVED_EXPANSION):
  `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- screening:
  `sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json`
- evidence:
  `sources/2026-W34/evidence/v2/accepted/647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/evidence-accepted.json`
- views:
  `sources/2026-W34/evidence/v2/views/accepted/e2e644bcc97ac664949b272fca919923385af6192c65b5a3566e30382b0ca7ba/edition-views-accepted.json`
- ledger: `sources/2026-W34/materiality-ledger-v2.json`
- completeness: `sources/2026-W34/profile-completeness-v2.json`

## Matrix derivation note (current-Core basis override)

The standalone `survey_architecture_v2 matrix` CLI applies the strict
`validate_package_basis` state-SHA check and therefore rejects the valid
historical accepted Screening package (its recorded `state_sha256` predates
the `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` State advance; the accepted
package copy itself is byte-unchanged, `package_sha256` verified MATCH).

Current Core's own stage validator (`survey_stage_validation_v2.py`,
`validate_stage` line 531) derives its expected Matrix under
`survey_agent_tool_v2.current_stage_basis_override()`, which tolerates
exactly this content-addressed historical State-SHA drift. The edition-local
driver (`/tmp/opencode/derive_w34_matrix.py`, kept out of the repository
tree) therefore calls the identical Core `derive_candidate_matrix` under the
identical Core override context — the repository-owned equivalent derivation.
Final authority remains the independent Core stage validation, which
re-derives and byte-compares.

The effective `--discovery` input is the Screening-package-resolved
DERIVED_EXPANSION basis
(`screening/input/event-discovery-v2.jsonl`, SHA matches package basis),
exactly as `survey_stage_validation_v2._evidence_basis` resolves it.

## Steps

1. Matrix derivation -> `sources/2026-W34/candidate-matrix-v2.json`
2. Directive reconciliation -> `directive-reconciliation-r1.json`
3. Selection materialization -> `sources/2026-W34/candidate-selection-v2.json`
   (`selection_version = w34-sol-selection-r1`)
4. `selection-check` (Core) PASS
5. Stage validation `EVIDENCE_REVIEWED -> SELECTION_COMPLETE` (Core) PASS
   -> `validation/selection-stage-validation-r1.json`
6. `advance-stage` (Core) -> checkpoint `EVIDENCE_REVIEWED.json`,
   State -> `SELECTION_COMPLETE`
7. Commits (normal, non-force) + push + remote read-back
8. STOP at `SOL_SELECTION_REVIEW_READY` (no Architecture or later stages)
