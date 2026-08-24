# Core v2 post-integration repair checkpoint — transport + Thematic initialization

Status: `PREFREEZE CANDIDATE COMPLETE / EXACT-HEAD CI + FRESH SEVEN-POINT AUDIT PENDING / PRODUCTION FAILED EVIDENCE RETAINED`

Date: 2026-08-25 JST

## Context

PR #447 was merged after explicit Human approval as merge commit `eb493a8cbc7c3eeb3b9049dd818b37ec966a2f28`. The reviewed Core was then synchronized into the W33 and SP001 canonical work branches before post-integration production validation resumed.

The first live post-integration trials exposed two shared-Core/operator defects. Per the redesign authority, the affected production attempts are failed evidence; edition-local work is preserved, shared Core is repaired separately, and clean validation must be rerun after reviewed integration.

Repair is isolated on `maintenance/core-v2-postintegration-transport-thematic` / PR #452. Candidate-tree implementation, regression, operational bootstrap, and narrow authority synchronization are complete. The tree must not change again unless exact-head CI or fresh audit exposes a defect; any such mutation restarts the prefreeze/audit sequence.

## Finding PI-001 — connector-created Issue #448 transport produced no observable execution

W33 was synchronized with reviewed main, then an immutable request-only commit was created:

- branch: `weekly/2026-W33-v2-work`
- request: `sources/2026-W33/execution/requests/postmerge-w33-init-r1.json`
- request commit: `52e5615cf745bdb2d239336241d7bb86a18cd7fd`
- queue comment: `/survey-core-execute 52e5615cf745bdb2d239336241d7bb86a18cd7fd`
- queue: Issue #448

The request remained exact branch head and no canonical Profile/State or `Execute Core operator request postmerge-w33-init-r1` writeback appeared. In the same connector session, connector-created pull requests did trigger the repository's ordinary PR CI, so the post-integration repair adds a connector-native default-branch `pull_request_target` transport to the *same* operator workflow rather than adding an eighth workflow.

The PR transport remains trust-rooted in default branch and is admitted only for same-repository PRs targeting `main`, authorized repository associations, a reserved operator title prefix, and a request-only current work-branch head whose branch equals immutable request `work_branch`. It then reuses the same reviewed-main/protected-path preflight and reviewed-main trusted runtime.

Issue #448 remains a valid/manual transport path; the PR transport is an additional connector-safe activation path, not a second executor or lifecycle engine. An operator transport PR is execution transport only and must not be merged as production/integration authority.

## Finding PI-002 — canonical Thematic scope materialization was not accepted by Bridge initialization

SP001's canonical scope authority is `sources/SP001/research-scope-v2.json`, validated by `schemas/thematic-scope-spec-v2.schema.json`. It intentionally contains editorial scope/planning authority but does not contain execution-time `temporal_mode` or `as_of`.

`survey_pilot_bootstrap_v2` correctly combines that materialization with temporal policy and initialization time before calling `core.thematic_profile`. The operator bridge instead passed `spec_path` JSON directly to `core.thematic_profile`, while its E2E regression used a raw Core spec that did contain `temporal_mode`/`as_of`. Therefore the regression did not represent the canonical SP001 path.

Repair:

- retain generic raw Core thematic spec compatibility;
- recognize canonical `thematic-scope-spec-v2` materialization;
- revalidate planning-authority entry and exact SHA;
- require explicit request `temporal_mode` for the canonical materialization path;
- derive `as_of` from immutable request `recorded_at`, matching `SET_AT_INITIALIZATION` semantics;
- bind source/work branch to request identity, with optional explicit `survey_root`;
- use the same generic `core.thematic_profile()` path;
- add canonical-materialization positive and fail-closed regressions.

A prefreeze review of the first repair candidate then found one narrower PI-002 identity ambiguity: for a legacy raw Thematic spec, an operation-level `survey_root` could be schema-valid but silently ignored. The first freeze candidate `f76161aeae2ebffd473a2b1414a516162faa4253` was therefore invalidated before final audit. Profile identity validation now requires any request-owned `survey_root` to match the generated Profile exactly, and a negative raw-spec regression proves disagreement fails closed.

## Candidate scope at prefreeze

Intended PR #452 candidate scope is limited to:

1. existing operator workflow dual default-branch activation (`issue_comment` + constrained same-repository `pull_request_target`) with one common preflight/executor;
2. canonical Thematic materialization translation in the generic bridge while preserving raw-spec compatibility;
3. the two optional Thematic request fields needed by that generic translation (`temporal_mode`, `survey_root`) with explicit Profile identity validation;
4. regressions for canonical materialization, raw-spec path disagreement, and dual transport;
5. current final-audit, agent bootstrap, session bootstrap, and narrow post-integration authority documentation.

No eighth workflow, no new lifecycle state, no new Human Gate, no arbitrary executable request surface, no SP001/W33 topic hardcoding, and no parallel Retrospective/Thematic engine is intended.

`main` remained unchanged at `eb493a8cbc7c3eeb3b9049dd818b37ec966a2f28` throughout repair prefreeze cross-check.

## Diagnostic CI history

The first repair head `f2b8599b47c45c2f2164cf9c8c4d3902e14f1f6e` exercised the new canonical-Thematic regressions successfully but failed the full suite on one stale static assertion that required the workflow step-name substring `Parse exact operator command`. That compatibility assertion was restored without weakening transport semantics.

The later `f76161ae...` candidate reached prefreeze but was invalidated by the raw-spec `survey_root` identity finding above before any final seven-point verdict could be issued. No CI or audit verdict from either diagnostic candidate may be reused for the final candidate.

The authoritative CI evidence must be the exact later prefreeze head after this final identity hardening and all authority/bootstrap synchronization. Exact run IDs and final seven-point verdicts are recorded outside the candidate tree so recording them cannot mutate the audited SHA.

## Acceptance boundary

This branch must not be merged merely because unit CI is green. Required before returning to production validation:

1. Core CI and Pipeline contract tests PASS on the exact immutable repair head;
2. workflow count remains seven;
3. default-branch trust/root and isolated-runtime protections remain intact for both transports;
4. canonical Thematic materialization and request-owned path identity regressions PASS;
5. docs/authority and operational bootstrap remain synchronized with the actual dual-transport contract;
6. full PR-scope/stale-text cross-check finds no unintended candidate change;
7. freeze one exact SHA and rerun all seven final-audit points from Point 1 without candidate mutation;
8. only unchanged 7/7 PASS may leave draft status and be presented for fresh Human full-candidate review;
9. explicit Human merge approval is required. PR #447 approval does not transfer to PR #452.

After reviewed merge, synchronize the new main into W33/SP001 and rerun clean post-integration initialization. The failed W33 request remains historical production evidence and is not treated as a successful Core transition. The live matrix must exercise connector-native PR transport writeback/receipt and canonical SP001 Thematic initialization before the remaining Retrospective/Foundations/generalization scenarios continue.
