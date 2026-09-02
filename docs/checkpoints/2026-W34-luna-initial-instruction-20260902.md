# 2026-W34 — Luna Initial Production Instruction

Status: **INITIAL EXECUTION AUTHORITY FROM SOL**  
Date: 2026-09-02 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Canonical work branch: `weekly/2026-W34-v2-work`  
Reviewed main baseline: `c7a898889463b049dea4ee7337ee16ad5fbf3191`  
Requested task boundary: **W34 initialization + non-X Source Intake readiness; stop before formal Discovery acceptance unless the required Grok/X result is already canonically imported and dispositioned.**

The exact starting SHA for this Luna run is supplied by Sol alongside this document after the instruction commit is created. Treat that SHA as mandatory execution input; do not infer or substitute it.

---

## 1. Mission

Start production of `2026-W34` under the current reviewed Survey Production Core v2 and complete as much ordinary Source Intake work as possible **without waiting for Grok/X collection**.

This first assignment is deliberately bounded. It is not an Architecture task, Selection task, drafting task, or publication task.

Primary deliverables are:

1. canonical W34 initialization;
2. canonical W34 Weekly window/profile/state verification;
3. broad **non-X** Source Intake and raw/provenance capture;
4. W33 carry-over recheck initialization;
5. a structured non-X candidate/source inventory with coverage and gap notes;
6. durable execution records that let Sol resume without chat history;
7. a precise stop report identifying what remains before `DISCOVERY_COLLECTED` can be accepted.

Grok/X is required by the Weekly Profile, but **waiting for Grok is not part of this assignment**. If Grok output is absent, continue all independent work and stop only at the bounded pre-Discovery handoff described below.

---

## 2. Sol / Luna responsibility boundary

### Sol owns authority and judgment

Sol remains responsible for:

- orchestration and lifecycle boundary decisions;
- research strategy and final completeness/materiality judgment;
- acceptance/rejection of technical Evidence;
- final Candidate Selection and Architecture synthesis;
- preparation and presentation of Human `ARCHITECTURE_REVIEW` and exact-byte `PUBLICATION_PREVIEW`;
- interpretation and recording of explicit Human decisions;
- reader-facing editorial direction and semantic/visual quality bar;
- Grok/X task definition, Drive handoff, returned Raw disposition, and X-to-primary-source gap-fill decisions;
- any force/reset/history rewrite decision;
- shared-Core defect disposition;
- Freeze/Release choreography.

### Luna is the bounded execution/research worker

For this assignment Luna may:

- perform exact-start guards and repository/state inspection;
- execute canonical initialization and deterministic stage mechanics;
- run configured non-X collectors;
- perform broad primary-source discovery/search expansion outside X;
- preserve/import Raw bytes and provenance;
- normalize source/candidate inventories where current Core permits;
- initialize/recheck Weekly carry-over obligations;
- write edition-local execution/session records;
- run deterministic validators and report exact results;
- commit only to the canonical W34 work branch within the task boundary.

Luna must not:

- infer Human approval or rejection;
- make final Architecture or Publication Preview decisions;
- choose final materiality/Selection on Sol's behalf;
- author final reader-facing publication prose in this first assignment;
- modify shared Core;
- create alternative/fallback/repair/review branches;
- force-push, reset, rewrite or rebase canonical history;
- treat absent Grok output as a terminal state or Exception Gate;
- advance a lifecycle edge whose required X precondition is not satisfied.

---

## 3. Start guard — mandatory before any write

Before writing anything:

1. Read remote `refs/heads/weekly/2026-W34-v2-work`.
2. Compare its HEAD to the **Exact Starting SHA supplied by Sol with this instruction**.
3. Confirm current `main` is still compatible with the reviewed baseline named above. If `main` moved after this instruction was issued, inspect the movement before using any new shared authority; do not silently change the reviewed-main baseline for an already-materialized operator request.

If the work-branch HEAD does not exactly equal the supplied Exact Starting SHA:

- perform no repository/content writes;
- do not create another branch;
- report the actual HEAD and stop.

Do not use a high-level empty diff/null file list as proof that a commit is empty. When commit shape matters, verify parent/tree and exact changed paths using raw/compare authority.

---

## 4. Mandatory read order

Read current authority from the reviewed main baseline before production work:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-authority.md`
4. `docs/survey-production-core-v2-postintegration-amendment.md`
5. `docs/survey-production-core-v2-issue-prevention-checklist.md`
6. `docs/survey-production-core-v2-x-source-intake.md`
7. `docs/survey-production-core-v2-execution-record-policy.md`
8. `docs/survey-production-core-v2-operator-execution-bridge.md`
9. `docs/weekly-pipeline-operations.md`
10. `docs/weekly-carryover-policy.md`
11. applicable current Weekly/Profile configuration under `config/` as read-only authority
12. W33 `candidate-selection-v2.json` and any carry-over authority needed to derive W34 obligations

Repository authority outranks chat history and this document where the current reviewed Core defines a stricter invariant.

---

## 5. Shared-Core denylist

During this edition-production assignment, these are read-only:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

Do not patch a shared-Core defect inside W34 production. If one is encountered:

1. preserve failed evidence;
2. record it under `sources/2026-W34/execution/defects/` once the edition is initialized;
3. report impact and the narrowest safe edition-local workaround if one exists;
4. stop only if it is genuinely blocking the bounded assignment.

---

## 6. Phase A — initialize 2026-W34 canonically

Initialize `2026-W34` through the current canonical Core v2 `INITIALIZE_WEEKLY` path.

Use:

- issue: `2026-W34`
- research profile: generic `WEEKLY`
- publication profile: generic `WEEKLY_MAGAZINE`
- canonical work branch: `weekly/2026-W34-v2-work`
- reviewed main baseline: `c7a898889463b049dea4ee7337ee16ad5fbf3191`

Use exact local Core CLI if genuinely available. Otherwise use the reviewed connector-safe operator bridge exactly as current authority specifies.

### If connector-safe bridge is used

The operator request commit must be a **true request-only commit**:

- exactly one new request JSON under the canonical W34 execution request path;
- no unrelated file additions/modifications/deletions;
- exact current W34 branch head before activation;
- reviewed-main/protected-Core checks must pass;
- activate only a supported default-branch transport;
- never merge an operator transport PR as production authority;
- distinguish request commit, transport event, trusted workflow run, bot output commit and resulting branch HEAD.

Immediately before transport activation, re-read the remote branch and prove the request commit is still its exact HEAD.

If request shape or preflight fails, do not repair by force/reset/rewrite. Record/report the failure and preserve the branch.

### Initialization verification

After initialization, verify at minimum:

- `sources/2026-W34/production-state.json` exists and validates;
- `sources/2026-W34/production-profile.json` exists and binds `WEEKLY + WEEKLY_MAGAZINE`;
- canonical work branch in Profile/State is correct;
- execution tree exists according to current execution-record policy;
- exact Weekly editorial/collection window and cutoff are derived by current Core rather than guessed;
- initial lifecycle and `next_action` match canonical Core output;
- no shared-Core file changed.

Record the exact derived W34 window in the session record and final report.

---

## 7. Phase B — non-X Source Intake

After initialization, perform broad Source Intake **excluding X/Grok**.

Do not equate collector success or source count with completeness.

### 7.1 Configured collector surfaces

Exercise the current configured Weekly non-X collectors as applicable, including at minimum the canonical equivalents of:

- arXiv;
- GitHub Releases / configured repository watchlist;
- official news/blog/index snapshots.

Preserve exact Raw response bytes and collector provenance in the canonical W34 layout. Do not mutate previously indexed Raw bytes.

### 7.2 Research expansion beyond collectors

Collectors are seeds, not an exhaustive search. Expand through primary/authoritative sources across the Weekly technical surface, without X:

- Foundation Models / Reasoning
- Agents / Coding / Harness / Computer Use
- Multimodal Foundation Models
- Image Generation / Editing
- Video Generation / Editing
- Speech / Audio / Music Generation
- Open Weight / Local AI / Quantization
- Inference / Serving / Systems
- Memory / Multi-Agent / Retrieval
- Evaluation / Benchmarks
- Safety / Security
- Other Emerging Generative AI Technology

For each lane, record what was actually searched/inspected, useful source leads, negative/quiet findings, and unresolved gaps. Do not manufacture candidates to satisfy a quota.

Prefer authoritative source classes for technical facts:

- official vendor/project announcements and documentation;
- official repositories/releases/changelogs;
- papers/model cards/technical reports from original authors;
- other first-party technical artifacts.

Secondary media may be used as discovery leads but must not silently become technical Evidence.

### 7.3 Chronology discipline

Use the Core-derived W34 window/cutoff.

Keep distinct:

- underlying event date;
- source publication/update date;
- current-week technical adoption/integration signal;
- post-cutoff Late Breaking material.

Do not redraft a pre-window event as a W34 release merely because it is newly discovered.

---

## 8. Phase C — W33 carry-over obligations

Use current carry-over policy and **derive** the expected W34 set from canonical W33 Selection authority. Do not handcraft or guess the IDs.

Before any future Screening acceptance, ensure every expected carry-over obligation is represented in the W34 carry-over ledger with an allowed current status.

For this first assignment:

- initialize all expected obligations;
- recheck them against current non-X authoritative sources where feasible;
- distinguish current W34 events from previous-issue backfill/correction;
- `PENDING_RECHECK` may remain only where the bounded Source Intake work genuinely cannot resolve the obligation yet;
- do not force promotion merely to close the ledger.

Report the complete derived carry-over set and current status.

---

## 9. Grok/X nonblocking rule — critical

Weekly Grok/X is mandatory for eventual Discovery acceptance, but it is **not a blocking wait state for this assignment**.

Luna must not wait idle for Grok and must not create a fake `AWAITING_GROK` lifecycle terminal.

For this first assignment:

- do not provision or run a separate Grok connector;
- do not independently change the Sol-owned Drive task/result contract;
- if no canonical W34 Grok result has been imported/dispositioned, complete all independent non-X work and stop at the bounded pre-Discovery handoff;
- if a valid Grok result has already been canonically imported and dispositioned before you reach the boundary, report that fact, but do not assume it is valid merely because a file exists—validate current manifest/provenance requirements.

**Formal `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` acceptance is forbidden while the Weekly required Grok/X run is incomplete or undispositioned.**

Grok Raw observations are Discovery/community-signal input only; benchmark values, specifications, release dates, license claims and similar technical facts still require authoritative verification.

---

## 10. Candidate/source readiness output

Before stopping, leave a structured W34 non-X readiness view that Sol can consume without replaying the collection work.

At minimum include:

- sources/candidates discovered by lane;
- source class and authoritative locator;
- event/chronology note;
- why the item may matter for W34;
- what is already directly supported;
- what still requires Evidence verification;
- duplicate/overlap relationships;
- likely carry-over relationship where applicable;
- negative/quiet lane findings;
- residual research gaps.

This is **not final Candidate Selection**. Do not assign final Architecture roles on Sol's behalf.

---

## 11. Execution records

Maintain current W34 execution records according to repository policy, including:

```text
sources/2026-W34/execution/index.md
sources/2026-W34/execution/sessions/<session-id>.md
```

The session record must contain:

- Starting authority
- Actions actually performed
- External handoff
- Deterministic execution transport
- Deviations / failures
- End state

If bridge execution is used, retain exact identities for:

- reviewed main baseline;
- request path/id;
- request-only commit SHA;
- operator transport trigger;
- trusted default-branch workflow run;
- bridge receipt/result;
- bot output commit;
- resulting work-branch HEAD.

Do not turn Markdown execution records into a second lifecycle state machine.

---

## 12. Required validation before stop

Before reporting completion of this first assignment:

1. re-read remote W34 branch HEAD;
2. verify all writes are edition-local except the already-existing Sol instruction under `docs/checkpoints/`;
3. verify shared-Core denylist paths are unchanged relative to reviewed main;
4. validate W34 Production State/Profile and execution-record structure;
5. validate Raw provenance/index requirements for imported non-X Raw material;
6. verify every derived W33 carry-over obligation is represented;
7. explicitly state Grok/X status;
8. if Grok is incomplete, prove that formal Discovery acceptance was **not** performed.

No force/reset/rewrite/rebase.

---

## 13. Stop condition and completion report

### Normal stop when Grok is still outstanding

Stop after non-X Source Intake readiness is complete, with W34 still before formal `DISCOVERY_COLLECTED` acceptance.

Report:

- reviewed main baseline;
- initial Exact Starting SHA supplied by Sol;
- ending branch SHA;
- initialization request/run/output identities if applicable;
- validated Production State/lifecycle/next action;
- Core-derived W34 time window/cutoff;
- non-X collectors executed and Raw/provenance locations;
- broad-search coverage summary by lane;
- non-X candidate/source inventory count and key unresolved gaps;
- complete carry-over obligation list/status;
- Grok/X status;
- explicit statement that Grok waiting did not block non-X work;
- exact next action: Sol imports/dispositions the required Grok result, performs/assigns any primary-source gap-fill, then formal Discovery acceptance may proceed.

### If Grok is already complete

Do **not** automatically expand this first assignment into Screening/Evidence/Selection/Architecture. Stop after reporting that all Source Intake preconditions appear satisfied and let Sol independently verify before authorizing the next bounded task.

---

## 14. Explicit prohibitions for this first assignment

Do not:

- proceed to Architecture Review;
- establish final Candidate Selection;
- create final Architecture;
- draft reader-facing W34 publication source;
- build or present Publication Preview;
- Freeze or Release;
- close unrelated issues;
- repair shared Core;
- create new branches;
- modify W33 frozen/released authority;
- wait idly for Grok.

When this bounded assignment is complete, stop and return the exact completion report to Sol.
