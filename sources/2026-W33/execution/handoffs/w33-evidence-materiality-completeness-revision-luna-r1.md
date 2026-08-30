# 2026-W33 Sol→Luna handoff — Evidence / Materiality / Completeness revision r1

Status: `READY_FOR_LUNA / REGENERATE_FROM_REPAIRED_DISCOVERY_AND_REVISED_SCREENING / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at handoff creation: `CANDIDATES_NORMALIZED`  
Current machine next action: `stage:evidence-materiality-completeness`  
Requested endpoint: E/M/C candidate committed, **no `ADVANCE_STAGE`**

The caller must supply the exact branch SHA containing this handoff, the Sol revised-Screening advancement review, and the recovery-index update. Luna must verify the remote branch HEAD equals that exact SHA before any write. On mismatch, do not write; stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 1. Objective

Regenerate the W33 Evidence / Edition Evidence View / Materiality Ledger / Profile Completeness candidate from the current repaired authority.

The revision exists to close the five active W32 carry-over source gaps that previously caused:

`weekly:carry-over = NEEDS_RESEARCH`

and therefore:

`overall_status = INCOMPLETE`.

The task must produce current candidate artifacts for Sol review only. Do not transition Production State to `EVIDENCE_REVIEWED`.

## 2. Current frozen upstream authority

### Production State

Path:

`sources/2026-W33/production-state.json`

Required before write:

- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- Discovery checkpoint: `passed`
- Screening checkpoint: `passed`
- Evidence / Materiality / Completeness checkpoints: `pending`
- Architecture Review: `pending`
- terminal reason: `null`

Expected current State SHA-256 before this task:

`3894a6fc484870bbe7eb1e42e8440d65ac2ee4fe911bcf6528c29212e156ffce`

### Repaired Discovery

Path:

`sources/2026-W33/discovery/discovery-v2.jsonl`

SHA-256:

`6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`

Record count: 41.

### Current Discovery acceptance

Path:

`sources/2026-W33/discovery/discovery-accepted-v2.json`

SHA-256:

`777414eefad7280d45fc847dd44a0bdeeef225b6dd0c3e1f4b90bc8b1acb7995`

### Current revised Screening acceptance

Use exactly:

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json`

Frozen identity:

- result-set: `0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a`
- acceptance SHA-256: `e6f0392004191b4668e4231c57839044e4b08ff1e32763403f2d92630b0b0a0f`
- records: 41
- KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4

Do **not** use historical Screening result-set `648a1e...` as current authority.

### Sol semantic authority

Read and obey:

`sources/2026-W33/execution/reviews/w33-screening-revision-advance-sol-review-20260830-r1.md`

Decision:

`ACCEPT / STATE_TRANSITION_VERIFIED / REVISED_SCREENING_AUTHORITY_ESTABLISHED / READY_FOR_EVIDENCE_MATERIALITY_COMPLETENESS_REVISION`

## 3. Required read order

Before any production-artifact write, read in order:

1. `AGENTS.md` from reviewed `main`.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed `main`.
3. `sources/2026-W33/production-state.json`.
4. `sources/2026-W33/production-profile.json`.
5. `sources/2026-W33/execution/index.md`.
6. `config/survey-production-v2.json` from reviewed `main`.
7. `config/prompts/evidence-verification-v2.md` from reviewed `main`.
8. `scripts/survey_evidence_v2.py` from reviewed `main`.
9. `scripts/survey_completeness_v2.py` from reviewed `main`.
10. `scripts/survey_stage_validation_v2.py` from reviewed `main`.
11. all current Evidence / Edition View schemas referenced by current Core.
12. `sources/2026-W33/discovery/discovery-accepted-v2.json`.
13. `sources/2026-W33/discovery/discovery-v2.jsonl`.
14. current revised Screening acceptance `0723540.../screening-accepted.json`.
15. `sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`.
16. `sources/2026-W33/execution/reviews/w33-screening-revision-sol-review-20260830-r1.md`.
17. `sources/2026-W33/execution/reviews/w33-screening-revision-advance-sol-review-20260830-r1.md`.
18. historical E/M/C handoffs:
    - `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
    - `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md`
19. historical Sol E/M/C semantic reviews, including the repaired Edition View review.
20. this handoff last.

Current repository/Core shape wins over historical handoff mechanics when they conflict. This handoff wins over historical W33 E/M/C semantics for the five repaired carry-over records and current artifact identities.

## 4. Historical E/M/C is reference only

The following remain immutable historical provenance and must not be edited in place:

Historical Evidence acceptance:

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/`

Historical Edition View acceptance:

`sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/`

Historical Materiality Ledger / Profile Completeness are present at the canonical non-content-addressed paths but are no longer checkpoint authority after Architecture Review r2 rollback. They may be read as semantic reference, but current versions must be regenerated from the repaired basis.

Do not modify any file under the two historical content-addressed accepted directories.

## 5. Evidence task cardinality and carry-forward method

The current Screening still has exactly four DROP records, therefore current Core must produce exactly **37 Evidence tasks**.

Generate a fresh Evidence package/tasks from current State + repaired Discovery + revised Screening using current canonical Core helpers.

Do not reuse historical task bytes as current task authority.

### 32 non-target active records

For every active non-DROP record except the five IDs listed in section 6:

- use the newly generated current task identity and current basis hashes;
- preserve the historical accepted Evidence Card's **semantic payload** exactly where the current source/task content is unchanged;
- identity/basis/task hashes must be regenerated as required by current Core;
- map historical semantics by Discovery ID, not by assuming task filename/task ID stability;
- do not perform fresh external research for these 32 records;
- `base-official-index-minimax-news` is included in this semantic carry-forward set and retains its old bounded uncertainty.

If a generated task differs semantically from its historical task for a reason other than current basis/source repair, stop for Sol review instead of guessing.

## 6. Five repaired carry-over Evidence Cards

These five must be regenerated from the repaired Discovery-bound first-party Raw/source authority, not copied from the historical `NEEDS_MORE` cards.

No external Web/vendor-site/GitHub browsing is authorized in this task. Use the first-party source material already bound into repaired Discovery and its Raw captures.

### 6.1 `carry-w32-claude-retirement`

Target Evidence status: `VERIFIED`.

Required factual boundary:

- primary subject is Claude Opus 4.1 retirement / model lifecycle event;
- retirement event date: `2026-08-05`;
- deprecation/notification chronology: `2026-06-05`;
- preserve Anthropic-operated-platform scope;
- preserve that partner-operated platform schedules are not inferred;
- Anthropic's documented replacement may be recorded as Anthropic first-party lifecycle guidance;
- verification target must be resolved rather than left `UNRESOLVED` merely because the event is pre-window.

This card is factual only. Do not call the event W33-material inside the Evidence Card.

### 6.2 `carry-w32-copilot-cloud-agent`

Target Evidence status: `VERIFIED`.

Required factual boundary:

- establish the concrete GitHub first-party 2026-08-03 cloud-agent updates;
- distinguish reasoning-level control and comment-triggered automations from older June/July cloud-agent functionality;
- preserve feature / plan / administrator-policy boundaries from the bound first-party sources;
- do not aggregate older features into an August launch claim;
- resolve the former first-party source-identity target.

### 6.3 `carry-w32-kimi-k3-copilot`

Target Evidence status: `VERIFIED`.

Required factual boundary:

- GitHub Copilot availability event dated `2026-08-06`;
- preserve documented rollout and pause/resumption chronology;
- preserve named surfaces/plans and Business/Enterprise policy boundaries;
- do not import independent Kimi benchmark/performance claims not present in the task-bound source;
- resolve the former availability/distribution source target.

### 6.4 `carry-w32-openai-gpt56-update`

Target Evidence status: `VERIFIED`.

Required factual boundary:

- establish the distinct `2026-08-06` GPT-5.6 Sol/Luna ChatGPT update;
- do not rewrite it as the original GPT-5.6 launch;
- preserve explicit Work/Codex model-version non-change;
- retain product/reliability/safety figures as OpenAI-attributed vendor facts/claims according to current Evidence classification rules;
- resolve the former chronology/source target.

### 6.5 `carry-w32-repowise`

Target Evidence status: `PARTIAL`.

Required factual boundary:

- establish first-party project/tool identity;
- establish the bound benchmark and reproduction methodology that the repaired source supports;
- preserve project-reported work-reduction measurements as `PROJECT_CLAIM`/equivalent current schema semantics, never independent reproduction;
- do not generalize retrieval/work reduction into end-to-end task success;
- preserve small-n, judge-noise, caching sensitivity, repository/task scope, credential, and reproduction limitations;
- exact qualifying W33 event/publication chronology may remain unresolved;
- the card must make clear that the unresolved chronology is a limitation, not proof of a current W33 event.

Do not set RepoWise to `NEEDS_MORE` solely because a qualifying W33 event date is not established. The factual project/method target is now sufficiently bounded for an explicit later non-material editorial disposition.

## 7. Expected Evidence aggregate guardrail

If the 32 historical semantics are carried forward correctly and the five repaired cards follow section 6, expected Evidence counts are:

- `VERIFIED`: 24
- `PARTIAL`: 12
- `NEEDS_MORE`: 1
- `REJECTED`: 0

The sole expected `NEEDS_MORE` is `base-official-index-minimax-news`.

Treat this as a semantic guardrail. Do not forge output to satisfy the count if current Core validation or exact source content contradicts it; stop for Sol review instead.

Accept the complete 37-card Evidence set using the current content-addressed Core acceptance mechanism. The resulting Evidence result-set identity will be new and must be reported.

## 8. Edition Evidence View regeneration

Create one current Edition Evidence View for every current accepted Evidence Card, using current Core schema/acceptance.

### 32 non-target views

Carry forward the historical **semantic view payload** from the repaired accepted historical View set, mapped through Discovery ID/current Evidence task, except for machine identity/hash fields that must bind the current Evidence bytes.

Do not reintroduce the original generic boilerplate that was rejected during the prior W33 View review. Preserve the candidate-specific repaired rationales / `why_this_issue` semantics for the 32 unchanged records.

### Five repaired carry-over views

The five current views are frozen as follows.

#### Claude retirement

- materiality: `CONTEXT`
- scope dimensions: `carry-over obligations`, `current relevance`
- factual chronology is pre-window relative to the W33 rolling window;
- `carry_over` semantics must be true/current-schema equivalent;
- rationale: explicitly closes the inherited lifecycle obligation but does not create a new in-window W33 headline.

#### Copilot cloud agent

- materiality: `CONTEXT`
- scope dimensions: `carry-over obligations`, `current relevance`
- 2026-08-03 is pre-window;
- treat as explicit carry-over closure/context, not as a W33 launch;
- preserve the narrow feature-update scope.

#### Kimi K3 Copilot

- materiality: `CONTEXT`
- scope dimensions: `carry-over obligations`, `current relevance`
- 2026-08-06 is pre-window;
- explicit carry-over closure/context;
- rollout/policy boundaries remain attached.

#### GPT-5.6 update

- materiality: `CONTEXT`
- scope dimensions: `carry-over obligations`, `current relevance`
- 2026-08-06 is pre-window;
- explicit carry-over closure/context;
- distinct from the in-window GPT-5.6 Ultrafast / Daybreak events already represented elsewhere.

#### RepoWise

- materiality: `NON_MATERIAL`
- scope dimensions: `carry-over obligations`, `current relevance`
- carry-over relation remains explicit;
- no qualifying W33 event/delta is established by the repaired bounded first-party authority;
- project/tool/method facts remain usable as audit context, but the W33 edition should not include RepoWise as a material development on this basis;
- unresolved exact chronology is a limitation supporting non-inclusion, not a reason to keep the carry-over open indefinitely.

Use the exact current-schema legal `window_relation`/`carry_over` values that correspond to these semantics. Do not invent enum strings from this prose if the schema uses different spellings.

## 9. Expected Edition View aggregate guardrail

Expected materiality counts:

- `MATERIAL`: 25
- `CONTEXT`: 10
- `HOLD`: 1
- `NON_MATERIAL`: 1

The sole expected HOLD is `base-official-index-minimax-news`.

Accept the complete current View set using the Core content-addressed acceptance mechanism. Report the new View-set identity.

## 10. Materiality Ledger regeneration

Regenerate the deterministic Materiality Ledger from the exact current:

- Production Profile;
- repaired Discovery;
- revised Screening acceptance;
- new Evidence acceptance;
- new Edition View acceptance;
- current implementation identity.

The Ledger must contain exactly 41 Discovery rows.

Because the canonical path already contains historical pre-r2 bytes, use a safe regeneration method:

1. derive and validate the new Ledger at a temporary path using canonical Core logic;
2. verify exact 41-row identity and upstream hashes;
3. replace the canonical file only with the exact validated generated bytes:
   `sources/2026-W33/materiality-ledger-v2.json`;
4. do not hand-edit the derived rows.

Historical Ledger bytes remain recoverable in Git history and prior review/checkpoint hashes. Do not alter the historical content-addressed Evidence/View directories to preserve them.

Expected changed downstream dispositions for the five repaired carry-over rows:

- four `CONTEXT`;
- RepoWise `NON_MATERIAL`.

The already-DROP Qwen3.8 carry-over record remains its deterministic DROP disposition and must remain represented in the 41-row ledger.

## 11. Profile Completeness regeneration

Regenerate Profile Completeness against the exact new Ledger and current Profile/Core.

Preserve all three initial Profile obligations exactly:

1. `weekly:current-relevance` → `current relevance`
2. `weekly:technical-significance` → `technical significance`
3. `weekly:carry-over` → `carry-over obligations`

Expected semantic disposition:

### `weekly:current-relevance`

Status: `LIMITATION`.

Carry forward the prior non-carry-over current-relevance coverage structure, updated to current Evidence task identities as needed. Preserve legitimate index/post-cutoff/source-boundary limitations, including the unchanged MiniMax HOLD.

### `weekly:technical-significance`

Status: `LIMITATION`.

Carry forward the prior technical-significance coverage structure, updated to current Evidence task identities as needed. Preserve legitimate vendor/project/author-reported and partial-access limitations.

### `weekly:carry-over`

Status: `SATISFIED`.

Its `discovery_ids` must still explicitly account for all six inherited carry-over records:

- `carry-w32-claude-retirement`
- `carry-w32-copilot-cloud-agent`
- `carry-w32-kimi-k3-copilot`
- `carry-w32-openai-gpt56-update`
- `carry-w32-qwen38-27b`
- `carry-w32-repowise`

Its Evidence task references must bind the five current non-DROP carry-over Evidence tasks. The Qwen carry-over remains disposed at Screening as DROP and therefore has no current Evidence task.

Required rationale semantics:

- Claude/Copilot/Kimi/GPT-5.6 were explicitly closed from fresh first-party authority and retained only as pre-window context;
- RepoWise was explicitly disposed `NON_MATERIAL` because no qualifying W33 delta is established under the repaired source authority;
- Qwen3.8 carry-over was already disposed at Screening in favor of the dedicated W33 first-party gap-fill record;
- no active carry-over obligation remains open for additional research.

### Overall status

Expected:

`LIMITED`

because the two legitimate limitation rows / residual limitations remain, but no obligation should be `NEEDS_RESEARCH`.

The old residual limitation saying five active W32 carry-over rechecks remain `NEEDS_RESEARCH/HOLD` must be removed.

Permissible residual limitations include, when accurately grounded:

- MiniMax/index-level source limitation;
- vendor/project/author-reported claims and lack of independent reproduction where applicable;
- RepoWise chronology/method limitations, explicitly marked non-blocking after its non-material disposition.

For WEEKLY, `closure` remains `null` under current Core.

As with the Ledger, because the canonical path already contains historical bytes:

1. build/validate the new Completeness object at a temporary path;
2. validate with both current `survey_evidence_v2.py` completeness rules and `survey_completeness_v2.py` authoritative guard;
3. replace only with exact validated bytes at:
   `sources/2026-W33/profile-completeness-v2.json`.

Do not force `LIMITED` if the exact generated/validated obligations contradict the frozen semantics; stop for Sol review and report the discrepancy.

## 12. Required validation

Before commit, prove at minimum:

1. remote starting HEAD exact match before write;
2. current lifecycle/state hash and revised Screening identity match section 2;
3. fresh Evidence package has exactly 37 tasks and no task for any DROP record;
4. each task's source authority is contained in its repaired/current Discovery record;
5. current Evidence acceptance validates canonically;
6. 32 non-target Evidence semantic payloads are unchanged except machine identity/basis fields required by the new run;
7. five target Evidence results match section 6;
8. Evidence counts are 24 VERIFIED / 12 PARTIAL / 1 NEEDS_MORE / 0 REJECTED, or stop with discrepancy;
9. current Edition View acceptance validates canonically;
10. 32 non-target View semantic payloads preserve the prior repaired candidate-specific semantics except current identity/hash fields;
11. five target View dispositions match section 8;
12. View counts are 25 MATERIAL / 10 CONTEXT / 1 HOLD / 1 NON_MATERIAL, or stop with discrepancy;
13. Materiality Ledger validates and has exactly 41 rows;
14. Completeness validates under both Core completeness layers;
15. all three initial obligations are retained with exact IDs/dimensions;
16. `weekly:carry-over = SATISFIED`;
17. no Completeness obligation is `NEEDS_RESEARCH`;
18. overall Completeness is `LIMITED`;
19. old five-carry-over residual blocker text is absent;
20. Production State remains byte-identical at `CANDIDATES_NORMALIZED` throughout the candidate task;
21. Evidence/Materiality/Completeness checkpoints remain pending;
22. no Selection/Architecture/Human Gate/Drafting work occurs.

## 13. Allowed repository writes

Allow only:

- one new content-addressed accepted Evidence result-set under `sources/2026-W33/evidence/v2/accepted/<new-result-set>/...`;
- one new content-addressed accepted Edition View set under `sources/2026-W33/evidence/v2/views/accepted/<new-view-set>/...`;
- replacement of `sources/2026-W33/materiality-ledger-v2.json` with exact newly generated/validated deterministic bytes;
- replacement of `sources/2026-W33/profile-completeness-v2.json` with exact newly generated/validated bytes;
- one session record:
  `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-revision-20260830-r1.md`.

If current canonical runners create additional **audit files inside the new content-addressed Evidence/View run directories**, those are allowed only when generated by the canonical runner and must be listed in the session record.

Do not modify:

- Production State;
- any checkpoint;
- repaired Discovery / Raw capture / Discovery acceptance;
- revised Screening accepted run;
- historical accepted Evidence/View run directories;
- Candidate Matrix / Selection / Architecture;
- Human Gate records;
- shared Core/config/schema/prompt files.

## 14. Commit boundary

Preferred sequence:

1. candidate materialization commit containing the new Evidence/View accepted runs plus regenerated canonical Ledger/Completeness;
2. bookkeeping commit adding only the Luna session record.

Before the first branch update, re-read remote HEAD and require it still equals the caller-supplied starting SHA. Use normal fast-forward only; never force-push.

## 15. Session record

The session record must include:

- supplied and verified starting SHA;
- candidate commit SHA and final bookkeeping SHA from remote readback;
- reviewed-main SHA;
- current Screening acceptance path/result-set/SHA;
- new Evidence result-set identity, acceptance SHA, status counts;
- new Edition View set identity, acceptance SHA, materiality counts;
- new Materiality Ledger SHA and row count;
- new Profile Completeness SHA, all three obligation statuses, overall status, residual limitations;
- exact mapping/disposition of all six carry-over Discovery IDs;
- confirmation that the four pre-window events were not promoted into in-window headline events;
- RepoWise `PARTIAL / NON_MATERIAL` rationale and residual limitation boundary;
- MiniMax residual `NEEDS_MORE / HOLD` boundary;
- changed-path inventory;
- validation results;
- Production State before/after SHA proving byte identity;
- any deterministic environment/tooling deviations.

Successful stop status:

`EVIDENCE_MATERIALITY_COMPLETENESS_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

Failure/status alternatives:

- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `SOURCE_BOUNDARY_CONFLICT_NEEDS_SOL_REVIEW`
- `SEMANTIC_GUARDRAIL_MISMATCH_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`
- `TRANSPORT_FAILURE_NEEDS_SOL_REVIEW`

## 16. Explicit prohibitions

Do not:

- browse external sources or add new source authority;
- alter repaired Discovery or Screening decisions;
- turn pre-window carry-over events into current-window events;
- turn project/vendor/author claims into independent verification;
- keep any of the five repaired carry-over records at `NEEDS_MORE/HOLD` merely by mechanically replaying the historical result;
- mark RepoWise as MATERIAL/CONTEXT without a qualifying W33 delta;
- erase legitimate limitations to force `READY`;
- advance Production State;
- begin Selection or Architecture regeneration;
- create or modify Human Gate decisions;
- create Drafting/publication artifacts;
- modify shared Core.

## 17. Endpoint

Successful endpoint:

`CANDIDATES_NORMALIZED + CURRENT E/M/C CANDIDATE COMMITTED -> STOP FOR SOL REVIEW`

Sol will then independently review the exact accepted Evidence/View bytes, deterministic Ledger, and Completeness result before authorizing any `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` advancement.
