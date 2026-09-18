# W37 execution instruction — initialize through Grok/X handoff blocking stop

Status: `EXECUTION_AUTHORITY / W37_INITIALIZATION / CORE_BASELINE_PINNED / AWAITING_GROK_BLOCKING_STOP`

Date: `2026-09-18 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `2026-W37`

Work branch: `weekly/2026-W37-v2-work`

## 1. Mission

Initialize the new W37 weekly edition from the current reviewed `main`, establish the canonical W37 calendar/profile/state, generate the fresh weekly Grok/X source-intake task from the current Core policy, and stop at the first legitimate blocking point awaiting the Human-mediated Grok result.

This execution does **not** authorize formal Discovery acceptance without the completed Grok/X result, and does not authorize Screening, Evidence, Selection, Architecture, Draft, Publication Preview, Freeze, Release, or any Human decision.

## 2. Reviewed starting authority

Reviewed `main`:

- HEAD: `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`
- tree: `62cf5dfb30cc692cd19c11289fa80c837fd17b66`

Pinned Production Line:

- branch: `production/survey-core-v2`
- HEAD: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

The Production Line remains intentionally pinned while separate shared-Core work is handled elsewhere. Do not advance or modify it in this execution.

W36 is read-only precedent:

- `2026-W36` is `RELEASED / COMPLETE`
- Human Architecture r2 approved
- Human Publication Preview r2 approved
- public Release `weekly/2026-W36` exists
- exact released PDF SHA-256:
  `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`

No W36 byte may be modified.

## 3. W37 branch topology

The branch already exists and was created from exact reviewed main:

`weekly/2026-W37-v2-work`

Before this request was added, the branch base was exactly:

`6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`

with tree:

`62cf5dfb30cc692cd19c11289fa80c837fd17b66`

No alternate W37 branch, fallback branch, repair branch, review branch, or temporary content branch is authorized.

## 4. W37 canonical calendar

Issue:

`2026-W37`

Profiles:

- research profile: `WEEKLY`
- publication profile: `WEEKLY_MAGAZINE`

Target Human gate for the later full production lifecycle:

`ARCHITECTURE_REVIEW`

Canonical weekly window is the current repository rule:

America/New_York:

`[2026-09-04T18:00:00-04:00, 2026-09-11T18:00:00-04:00)`

UTC:

`[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`

JST reference:

`[2026-09-05T07:00:00+09:00, 2026-09-12T07:00:00+09:00)`

The end is exclusive. An event exactly at `2026-09-12 07:00 JST` is outside W37.

The worker must independently recompute/verify this with the current repository calendar implementation before writing W37 state. If the current canonical planner yields a different issue/window, STOP before writes and report expected versus actual.

## 5. Starting guard

The Muse invocation will provide an Exact Starting SHA/tree equal to the commit containing this execution request.

Before any repository/GitHub write, verify read-only:

1. remote `weekly/2026-W37-v2-work` HEAD/tree exactly equal the invocation values;
2. the Exact Starting SHA parent is the original W37 base `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
3. that parent tree is `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
4. remote `main` remains `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b` / tree `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
5. remote `production/survey-core-v2` remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
6. shared-Core bytes under `.github/**`, `config/**`, `schemas/**`, `scripts/**`, `templates/**`, `tests/**` are unchanged from the reviewed baseline relevant to this execution;
7. `sources/2026-W37/**` and `surveys/weekly/2026-W37/**` do not already contain a competing initialized production state;
8. current planner maps the latest completed cutoff to `2026-W37` and the exact window in §4.

If any guard differs, perform zero writes and STOP with expected/actual values.

No force push, reset, rebase, squash, history rewrite, or destructive cleanup is authorized.

## 6. Mandatory read order

After the guard passes, read at minimum:

1. this execution request;
2. current `config/weekly-pipeline.json`;
3. current W37-relevant Production Core v2 profile/config contracts;
4. current weekly initialization helper/controller;
5. current X source-intake policy/helper and prompt templates;
6. `docs/weekly-pipeline-operations.md`;
7. `docs/weekly-carryover-policy.md`;
8. current reader/publication boundary policy only as future constraints;
9. W36 initialization execution/session records as procedural precedent only.

Do not copy W36 generated artifacts, hashes, candidate IDs, X result bytes, Evidence, Selection, Architecture, Draft, or Human decisions.

## 7. Phase A — canonical W37 initialization

Initialize W37 through the current canonical Core v2 path.

Required semantics after initialization:

- issue: `2026-W37`
- research profile: `WEEKLY`
- publication profile: `WEEKLY_MAGAZINE`
- lifecycle: `ISSUE_INITIALIZED`
- target gate: `ARCHITECTURE_REVIEW`
- Human Architecture Review: pending
- Human Publication Preview: pending
- no later machine stage marked passed
- canonical calendar equals §4
- implementation authority is the reviewed branch/main baseline required by the current initializer.

Do not manually forge state JSON if a canonical initializer exists.

Record the execution/session provenance in an edition-local W37 path following current repository conventions.

## 8. Phase B — fresh W37 Grok/X source-intake task

Build the weekly-required X source-intake run using the current canonical X intake helper and current common + WEEKLY overlay policy.

Expected run identity:

`weekly-x-2026-W37`

Required result state after task generation:

`AWAITING_GROK`

Required repository task path should follow the canonical W36/W37 convention, expected approximately as:

`sources/2026-W37/external/x/weekly-x-2026-W37/grok-task.md`

Expected Human-mediated Drive handoff path should follow the existing convention:

`Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-task.md`

Expected initial Grok result filename:

`grok-x-result.md`

If the current helper emits a canonical path/name that differs, use the helper output and report it rather than hard-coding a stale convention.

Do not attempt Google Drive access from Muse. Do not install/search for a Drive connector. The Human will transfer the task to Grok and later provide/stage the resulting bytes.

The task must be freshly rendered for W37. Verify that stale W36 identity strings such as:

- `2026-W36`
- `weekly-x-2026-W36`

do not remain in the generated W37 task except where explicitly present in read-only historical/provenance discussion that is not part of the Grok task payload.

## 9. Phase C — bounded pre-Discovery preparation

While waiting for Grok, you may perform only non-authoritative preparation that does not advance the production lifecycle, such as:

- breadth-oriented first-party/public source scouting across the currently required weekly lanes;
- identifying likely primary-source authorities for later semantic consumption;
- recording possible W36 carry-over candidates as derivation inputs only;
- noting obvious W37-window events that may require later verification.

Any such preparation must be clearly marked non-authoritative and must not create accepted Discovery decisions.

Do not use snippets as evidence.
Do not equate retrieval success with semantic consumption.
Do not create Evidence claims.
Do not assign KEEP/DROP/HOLD/SELECTED decisions.
Do not create Architecture packages.

## 10. Carry-over rule

W36 conclusions do not carry into W37.

W36 may be used only as a source of possible carry-over inputs under the current carry-over policy.

Every carry-over item must later be revalidated against W37:

- time-window membership/status;
- current primary authority;
- materiality;
- evidence sufficiency;
- publication relevance.

No W36 Selection, Evidence classification, Architecture placement, wording, or Human approval is inherited.

## 11. X authority boundary

X/Grok output remains:

`SOCIAL_OBSERVATION / Raw Observation / community signal`

It must not by itself establish:

- technical specifications;
- benchmark scores;
- pricing;
- licensing;
- release availability;
- security/capability facts;
- acquisition/transaction status;
- model architecture facts.

Those require primary-source verification later.

Late-breaking X rows must remain separately bounded from the ordinary W37 window according to the current X intake contract.

## 12. Core freeze and known defects

This W37 initialization does not authorize repair of any shared-Core defect.

In particular do not repair during this execution:

- Issue #497 Freeze compatibility defects;
- release workflow nonexistent `validate-state` CLI defect;
- #434/#500/#501/#502 carry-forward quality hardening;
- reader-surface suppression plumbing;
- any other shared-Core issue discovered during initialization.

If a shared-Core defect blocks initialization or X task generation, record the exact defect in an edition-local W37 execution/defect record and STOP at the last valid state.

No changes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

are authorized.

Production Line must not move.

## 13. Required normal stop

The expected successful stop is:

`ISSUE_INITIALIZED / AWAITING_GROK`

with:

- W37 canonical state initialized;
- exact W37 window recorded;
- fresh `weekly-x-2026-W37` Grok task generated;
- task committed and non-force pushed;
- remote branch HEAD/tree read back;
- no formal Discovery accepted;
- no Screening/Evidence/Selection/Architecture created;
- no Human decision generated.

Do not advance `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` until the completed Grok result has been imported, recorded, and dispositioned through the canonical X intake path.

## 14. Final report

Report at minimum:

- execution request starting SHA/tree;
- original W37 base SHA/tree;
- main HEAD/tree at start and stop;
- Production Line HEAD/tree at start and stop;
- initialized W37 lifecycle and target gate;
- exact ET/UTC/JST window;
- X run ID/status;
- repository Grok task path;
- Human Drive handoff path;
- expected result filename;
- any pre-Discovery preparation path;
- remote final W37 HEAD/tree;
- changed paths;
- shared-Core changed paths = 0;
- formal Discovery count = 0;
- Human decisions = 0;
- confirmation of no force/reset/rebase/squash/history rewrite.

Do not start W38 in this execution.
