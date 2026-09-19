# W38 execution instruction — initialize through Grok/X handoff blocking stop

Status: `EXECUTION_AUTHORITY / W38_INITIALIZATION / CORE_BASELINE_PINNED / AWAITING_GROK_BLOCKING_STOP`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `2026-W38`

Work branch: `weekly/2026-W38-v2-work`

## 1. Mission

Initialize the new W38 weekly edition from the current reviewed `main`, establish the canonical W38 calendar/profile/state, generate the fresh weekly Grok/X source-intake task from the current Core policy, apply the accepted W37 X-intake breadth hardening as an edition-local W38 collection requirement without modifying shared Core, and stop at the first legitimate blocking point awaiting the Human-mediated Grok result.

This execution does **not** authorize formal Discovery acceptance without the completed Grok/X result, and does not authorize Screening, Evidence, Selection, Architecture, Draft, Publication Preview, Freeze, Release, or any Human decision.

## 2. Reviewed starting authority

Reviewed `main`:

- HEAD: `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`
- tree: `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`

Pinned Production Line:

- branch: `production/survey-core-v2`
- HEAD: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

The Production Line remains intentionally pinned while separate shared-Core work is handled elsewhere. Do not advance or modify it in this execution.

W37 is read-only precedent:

- `2026-W37` is `RELEASED / COMPLETE`
- Human Architecture approved
- Human Publication Preview r4 approved
- public Release `weekly/2026-W37` exists
- exact released PDF SHA-256:
  `09dea4e7fe7eecc6c4dae39a308899849ac84e598f9251b3d415e24b7ee3e268`

No W37 byte may be modified.

## 3. W38 branch topology

The branch has been created from exact reviewed main solely for this W38 production line:

`weekly/2026-W38-v2-work`

Before this execution request was added, the branch base was exactly:

`2ab91516e89b8d706bfe143ebc0e435fa5735e7a`

with tree:

`279ecbd91ee41cb2967532cf831c43ba3a4cbea3`

No alternate W38 branch, fallback branch, repair branch, review branch, or temporary content branch is authorized.

## 4. W38 canonical calendar

Issue:

`2026-W38`

Profiles:

- research profile: `WEEKLY`
- publication profile: `WEEKLY_MAGAZINE`

Target Human gate for the later full production lifecycle:

`ARCHITECTURE_REVIEW`

Expected canonical weekly window under the current repository rule:

America/New_York:

`[2026-09-11T18:00:00-04:00, 2026-09-18T18:00:00-04:00)`

UTC:

`[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`

JST reference:

`[2026-09-12T07:00:00+09:00, 2026-09-19T07:00:00+09:00)`

The end is exclusive. An event exactly at `2026-09-19 07:00 JST` is outside ordinary W38 and must be handled as late-breaking/post-cutoff material if otherwise relevant.

At Sol preflight on 2026-09-19, the current JST time was already after 07:00, so the W38 ordinary observation window was complete.

The worker must independently recompute/verify this with the current repository calendar implementation before writing W38 state. If the current canonical planner yields a different issue/window, STOP before writes and report expected versus actual.

## 5. Starting guard

The Muse invocation will provide an Exact Starting SHA/tree equal to the commit containing this execution request.

Before any repository/GitHub write, verify read-only:

1. remote `weekly/2026-W38-v2-work` HEAD/tree exactly equal the invocation values;
2. the Exact Starting SHA parent is the original W38 base `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
3. that parent tree is `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
4. remote `main` remains `2ab91516e89b8d706bfe143ebc0e435fa5735e7a` / tree `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
5. remote `production/survey-core-v2` remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
6. shared-Core bytes under `.github/**`, `config/**`, `schemas/**`, `scripts/**`, `templates/**`, `tests/**` are unchanged from the reviewed baseline relevant to this execution;
7. `sources/2026-W38/**` and `surveys/weekly/2026-W38/**` do not already contain a competing initialized production state;
8. current planner maps the latest completed cutoff to `2026-W38` and the exact window in §4.

If any guard differs, perform zero writes and STOP with expected/actual values.

No force push, reset, rebase, squash, history rewrite, or destructive cleanup is authorized.

## 6. Mandatory read order

After the guard passes, read at minimum:

1. this execution request;
2. `AGENTS.md`;
3. `docs/survey-production-core-v2-session-bootstrap.md`;
4. `docs/survey-production-core-v2-sol-luna-review-governance.md`;
5. current `config/weekly-pipeline.json`;
6. current W38-relevant Production Core v2 profile/config contracts;
7. current weekly initialization helper/controller;
8. current X source-intake policy/helper and prompt templates;
9. `docs/weekly-pipeline-operations.md`;
10. `docs/weekly-carryover-policy.md`;
11. W37 initialization/session records as procedural precedent only;
12. W37 final Grok r3 task/result provenance as X-collection-quality precedent only.

Do not copy W37 generated artifacts, hashes, candidate IDs, X result bytes, Evidence, Selection, Architecture, Draft, or Human decisions.

## 7. Phase A — canonical W38 initialization

Initialize W38 through the current canonical Core v2 path.

Required semantics after initialization:

- issue: `2026-W38`
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

Initialize edition-local execution records according to current repository policy:

```text
sources/2026-W38/execution/index.md
sources/2026-W38/execution/sessions/
sources/2026-W38/execution/reviews/
sources/2026-W38/execution/defects/
```

Record actual timezone-aware wall-clock timestamps. Do not synthesize future timestamps. Preserve the existing #507 timestamp-provenance discipline.

## 8. Phase B — fresh W38 Grok/X source-intake task

Build the weekly-required X source-intake run using the current canonical X intake helper and current common + WEEKLY overlay policy.

Expected run identity:

`weekly-x-2026-W38`

Required result state after task generation:

`AWAITING_GROK`

Expected repository task path:

`sources/2026-W38/external/x/weekly-x-2026-W38/grok-task.md`

Expected Human-mediated Drive handoff path:

`Grok_X_SourseIntake/Weekly/2026-W38/weekly-x-2026-W38/grok-task.md`

Expected initial result filename:

`grok-x-result.md`

If the current helper emits a canonical path/name that differs, use the helper output and report it rather than hard-coding a stale convention.

Do not attempt Google Drive access from Muse. Do not install/search for a Drive connector. The Human will transfer the task to Grok and later provide/stage the resulting bytes.

The task must be freshly rendered for W38. Verify that stale W37 identity strings such as:

- `2026-W37`
- `weekly-x-2026-W37`

do not remain in the W38 task payload except inside an explicitly labeled procedural-precedent note that is not part of the collection instructions.

## 9. W38 edition-local X breadth hardening

The first W38 Grok run should incorporate the successful W37 r3 collection lessons immediately rather than repeating the low-yield W37 r1/r2 cycle.

This is **edition-local task hardening only**. Do not change shared Core/templates.

The W38 task must require all of the following:

### 9.1 Full A-L lane scan

Independently inspect all Weekly A-L lanes before final ranking.

For every lane ending the first pass as `NONE_FOUND`, `NONE_FOUND_CONFIRMED`, or `UNCERTAIN`, retain the searches attempted.

For C/D/E/F, perform the normal required targeted second pass when initially weak.

### 9.2 Open-world discovery

After the lane scan, run at least one vendor/model/project-name-agnostic open-world pass intended to discover topics not anticipated by the task.

Include:

- independent developers;
- researchers;
- OSS maintainers;
- evaluators;
- operators;
- keyword snowballing;
- one-hop graph expansion through quote-posts, replies, related accounts, repositories, papers, and newly surfaced terminology where useful;
- runtime/inference work;
- quantization;
- failed reproduction;
- benchmark regressions;
- agent/MCP/harness tooling;
- security incidents;
- multimodal/audio/video workflows;
- operational constraints;
- fast-moving research adoption.

Every candidate should preserve discovery origin using one or more of:

- `KNOWN_EVENT_FOLLOWUP`
- `LANE_SEARCH`
- `OPEN_WORLD_X`
- `ACCOUNT_GRAPH_EXPANSION`
- `KEYWORD_SNOWBALL`
- `LATE_BREAKING`

### 9.3 Candidate-level direct-X provenance

Maintain a full deduplicated candidate pool, not only selected highlights.

For every plausible material candidate record at least:

- candidate ID/title;
- lane(s);
- discovery origin(s);
- event;
- event date/time when known;
- X momentum timing when observable;
- why now;
- representative direct X post URLs;
- account names;
- post date/time when available;
- account/source role: `OFFICIAL`, `INDEPENDENT`, or `COMMUNITY`;
- candidate URL count;
- independent-account count;
- source-breadth class;
- counter-signal/reaction;
- primary-source candidates;
- verification-needed claims;
- confidence;
- Raw-intake disposition.

Use source-breadth classifications:

- `MULTI_ACCOUNT_X`
- `SINGLE_SOURCE_X`
- `OFFICIAL_ONLY_X`
- `UNVERIFIED_X_REFERENCE`

Do not claim broad community momentum from a single official or single independent source.

### 9.4 Low-yield diagnostic

After the initial A-L scan plus first open-world pass, calculate:

- ordinary-window unique direct X post URLs;
- unique independent accounts;
- deduplicated candidate-pool size;
- weak-lane count;
- proportion of strong candidates that are single-source or official-only.

Trigger one mandatory expansion pass if **any** of these conditions holds:

- fewer than 12 unique ordinary-window X post URLs;
- fewer than 6 unique independent accounts;
- fewer than 8 deduplicated candidates;
- 4 or more lanes remain weak/unresolved;
- more than half of strong candidates are `SINGLE_SOURCE_X` or `OFFICIAL_ONLY_X`.

These are under-search diagnostics, not publication quotas.

If the full expansion pass still yields low counts, report the low yield honestly. Do not invent candidates or URLs.

### 9.5 Run-health audit

The final Grok result must include:

- total unique X post URLs;
- ordinary-window unique X post URLs;
- late-breaking unique X post URLs;
- total unique accounts;
- independent-account count;
- official-account count;
- full candidate-pool count;
- strong-candidate count;
- non-selected candidate count;
- source-breadth classification counts;
- open-world/graph/snowball discovery counts;
- lane-by-lane final coverage;
- whether low-yield expansion fired;
- expansion actions if fired;
- remaining access/search limitations.

All X output remains Raw Observation/community signal and is not final technical Evidence.

## 10. Phase C — bounded pre-Discovery preparation

While waiting for Grok, you may perform only non-authoritative preparation that does not advance the production lifecycle, such as:

- breadth-oriented first-party/public source scouting across required weekly lanes;
- identifying likely primary-source authorities for later semantic consumption;
- recording possible W37 carry-over candidates as derivation inputs only;
- noting obvious W38-window events that may require later verification.

Any such preparation must be clearly marked non-authoritative and must not create accepted Discovery decisions.

Do not use snippets as evidence.
Do not equate retrieval success with semantic consumption.
Do not create Evidence claims.
Do not assign KEEP/DROP/HOLD/SELECTED decisions.
Do not create Architecture packages.

## 11. Carry-over rule

W37 conclusions do not carry into W38.

W37 may be used only as a source of possible carry-over inputs under the current carry-over policy.

Every carry-over item must later be revalidated against W38:

- time-window membership/status;
- current primary authority;
- materiality;
- evidence sufficiency;
- publication relevance.

No W37 Selection, Evidence classification, Architecture placement, wording, or Human approval is inherited.

## 12. X authority boundary

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

Late-breaking X rows must remain separately bounded from the ordinary W38 window.

## 13. Core freeze and known defects

This W38 initialization does not authorize repair of any shared-Core defect.

In particular do not repair during this execution:

- profiled Freeze visual-authority compatibility defect;
- Freeze stage validator Human-Gate/checkpoint classification defect;
- release workflow nonexistent `validate-state` CLI defect;
- Issue #508 generic Weekly trailing-box pagination hardening;
- #434/#500/#501/#502 carry-forward quality hardening;
- any other shared-Core issue discovered during initialization.

If a shared-Core defect blocks initialization or X task generation, record the exact defect under the W38 edition execution tree and STOP at the last valid state.

No changes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

are authorized.

Production Line must not move.

## 14. Required normal stop

The expected successful stop is:

`ISSUE_INITIALIZED / AWAITING_GROK`

with:

- W38 canonical state initialized;
- exact W38 window recorded;
- fresh `weekly-x-2026-W38` Grok task generated;
- W38 edition-local X breadth hardening included;
- task committed and non-force pushed;
- remote branch HEAD/tree read back;
- no formal Discovery accepted;
- no Screening/Evidence/Selection/Architecture created;
- no Human decision generated.

Do not advance `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` until the completed Grok result has been imported, recorded, and dispositioned through the canonical X intake path.

## 15. Final report

Report at minimum:

- execution request starting SHA/tree;
- original W38 base SHA/tree;
- main HEAD/tree at start and stop;
- Production Line HEAD/tree at start and stop;
- initialized W38 lifecycle and target gate;
- exact ET/UTC/JST window;
- X run ID/status;
- repository Grok task path;
- Human Drive handoff path;
- expected result filename;
- whether W38 X breadth hardening was included;
- any pre-Discovery preparation path;
- remote final W38 HEAD/tree;
- changed paths;
- shared-Core changed paths = 0;
- formal Discovery count = 0;
- Human decisions = 0;
- confirmation of no force/reset/rebase/squash/history rewrite.

Do not start W39 in this execution.
