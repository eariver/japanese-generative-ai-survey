# Core v2 post-integration repair checkpoint — transport + Thematic initialization

Status: `IMPLEMENTATION IN PROGRESS / PRODUCTION VALIDATION FAILED EVIDENCE RETAINED`

Date: 2026-08-25 JST

## Context

PR #447 was merged after explicit Human approval as merge commit `eb493a8cbc7c3eeb3b9049dd818b37ec966a2f28`. The reviewed Core was then synchronized into the W33 and SP001 canonical work branches before post-integration production validation resumed.

The first live post-integration trials exposed two shared-Core/operator defects. Per the redesign authority, the affected production attempts are failed evidence; edition-local work is preserved, shared Core is repaired separately, and clean validation must be rerun after reviewed integration.

## Finding PI-001 — connector-created Issue #448 transport produced no observable execution

W33 was synchronized with reviewed main, then an immutable request-only commit was created:

- branch: `weekly/2026-W33-v2-work`
- request: `sources/2026-W33/execution/requests/postmerge-w33-init-r1.json`
- request commit: `52e5615cf745bdb2d239336241d7bb86a18cd7fd`
- queue comment: `/survey-core-execute 52e5615cf745bdb2d239336241d7bb86a18cd7fd`
- queue: Issue #448

The request remained exact branch head and no canonical Profile/State or `Execute Core operator request postmerge-w33-init-r1` writeback appeared. In the same connector session, connector-created pull requests did trigger the repository's ordinary PR CI, so the post-integration repair adds a connector-native default-branch `pull_request_target` transport to the *same* operator workflow rather than adding an eighth workflow.

The PR transport remains trust-rooted in default branch and is admitted only for same-repository PRs targeting `main`, authorized repository associations, a reserved operator title prefix, and a request-only current work-branch head. It then reuses the same reviewed-main/protected-path preflight and reviewed-main trusted runtime.

Issue #448 remains a valid/manual transport path; the PR transport is an additional connector-safe trigger, not a second executor or lifecycle engine.

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
- add a canonical-materialization regression.

## Acceptance boundary

This branch must not be merged merely because unit CI is green. Required before returning to production validation:

1. Core CI and Pipeline contract tests PASS on exact repair head;
2. workflow count remains seven;
3. default-branch trust/root and isolated-runtime protections remain intact for both transports;
4. canonical Thematic materialization regression PASS;
5. docs/authority synchronized with the actual dual-transport contract;
6. fresh review of the repair PR and explicit Human merge approval.

After reviewed merge, synchronize the new main into W33/SP001 and rerun clean post-integration initialization. The failed W33 request remains historical production evidence and is not treated as a successful Core transition.
