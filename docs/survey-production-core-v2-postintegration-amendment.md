# Survey Production Core v2 — Post-integration operator/Thematic amendment

Status: `CURRENT NARROW AUTHORITY AMENDMENT / PR #452 REVIEW PENDING`  
Established: 2026-08-25 JST  
Repair branch: `maintenance/core-v2-postintegration-transport-thematic`

## 1. Scope and precedence

This amendment exists because the first real-production run after integration of PR #447 exposed two behaviors that were not represented by the frozen maintenance candidate: connector transport activation and canonical Thematic scope materialization.

For **PI-001 operator transport** and **PI-002 Thematic initialization only**, this file supersedes contradictory Issue-#448-only or raw-Thematic-spec-only wording in:

- `docs/survey-production-core-v2-redesign-authority.md`;
- `docs/survey-production-core-v2-operator-execution-bridge.md`;
- `docs/survey-production-core-v2-github-actions-policy.md`;
- `docs/survey-production-core-v2-final-audit-rule.md` where the old wording describes the sole connector transport rather than the Issue transport specifically.

All other lifecycle, Human-Gate, trust-root, reviewed-main, execution-record, publication, and seven-point audit requirements remain unchanged. This amendment does not make PR #452 merge-ready by itself; exact-head CI, fresh fixed-head audit, and explicit Human merge approval remain mandatory.

## 2. PI-001 — connector-safe transport is dual-trigger, single executor

The canonical operator workflow remains exactly one file:

`survey-production-v2-operator-bridge.yml`

The repository still has exactly seven workflows. No new executor, lifecycle engine, or Human Gate is added.

The same default-branch workflow may be activated by either of two transport events:

1. **Issue queue transport** — `issue_comment` on persistent Issue #448 with exact command `/survey-core-execute <lowercase-40-hex-request-commit>` from an authorized repository association.
2. **Connector-native PR transport** — `pull_request_target` for a same-repository PR targeting `main`, opened/synchronized/reopened by an authorized repository association, whose title begins with `Survey Core operator transport:` and whose PR head branch is exactly the `work_branch` named by the immutable operator request.

The PR transport is an activation fallback for connector environments in which a connector-created Issue comment does not observably trigger the default-branch workflow. It is transport only. Such a PR is not an integration request, not editorial authority, and must not be merged as part of production execution.

Both transports converge before trust admission. The supplied request commit is untrusted data until the common read-only preflight proves all existing invariants:

- exact current canonical work-branch head;
- exactly one newly added immutable operator request and no other change in that request commit;
- reviewed-main existence/ancestry and request-parent descent;
- initialization execution-record reviewed-main equality;
- Human reviewed-commit == request parent for Human-Gate operations;
- protected paths/config resolved from reviewed `main`, not the admitted branch;
- protected Core/contract byte equality;
- isolated Python startup for all pre-admission parsing.

Only the dependent post-preflight job receives `contents: write`. It rechecks branch/main authority, materializes `scripts/` from the reviewed-main commit into a separate trusted runtime, runs the same canonical bridge package, enforces Profile-bound writes, preserves immutable request authority, and pushes with `force-with-lease` against the admitted head.

A `pull_request_target` implementation that checks out or executes work-branch code before this admission sequence, permits fork PRs, accepts a PR head different from request `work_branch`, or grants write authority before common preflight is a regression.

## 3. PI-002 — canonical Thematic materialization is a first-class initializer input

`INITIALIZE_THEMATIC` continues to support the generic raw Core thematic spec used by existing compatibility/E2E fixtures.

It additionally accepts the repository-owned `schemas/thematic-scope-spec-v2.schema.json` materialization used by SP001 and the pilot bootstrap. That materialization owns editorial scope and planning-authority provenance; it intentionally does not own execution-time temporal identity.

For a canonical materialization the bridge must:

1. schema-validate the scope materialization;
2. require `issue_id` equality with the immutable request;
3. re-read the named planning-authority file, require the named entry to exist, and require exact SHA-256 equality with the materialized authority record;
4. require explicit request `operation.temporal_mode` from the generic allowed Thematic temporal modes;
5. derive `as_of` from immutable request `recorded_at`;
6. bind `source_root` and `work_branch` from immutable request identity;
7. accept an explicit `operation.survey_root` when the canonical publication path is not derivable from the scope materialization itself;
8. call the same generic `core.thematic_profile()` and `core.initialize()` used outside the bridge.

This is not an SP001 adapter. No topic name, branch-family prefix, source-root depth, or Special-series identity may be hardcoded.

Raw Core thematic specs remain backward compatible. If a raw spec and request both name a temporal mode, disagreement fails closed rather than being silently overwritten.

## 4. Production-validation consequence

The W33 request `52e5615cf745bdb2d239336241d7bb86a18cd7fd` remains failed historical evidence. It must never be relabeled as a successful initialization.

After PR #452 has exact-head CI PASS, is frozen and freshly audited, receives explicit Human approval, and is integrated unchanged:

1. synchronize that reviewed `main` into W33 and SP001 work branches;
2. leave the failed W33 request/history intact;
3. create a new immutable request-only commit for the clean rerun;
4. exercise the connector-native PR transport in real branch execution and confirm bot writeback/receipt;
5. run SP001 `INITIALIZE_THEMATIC` from its existing canonical `research-scope-v2.json`, explicit `OPEN_HISTORY_AS_OF`, canonical survey root, and fresh request timestamp;
6. continue both editions through canonical lifecycle validation to `ARCHITECTURE_REVIEW` unless another shared-Core defect is exposed;
7. then continue the remaining Retrospective / Foundations / generalization matrix required by the final audit authority.

If the live PR transport or canonical Thematic initialization fails after reviewed integration, that run is new failed production evidence and Core returns to maintenance again; it is not repaired in-place inside an edition.
