# 2026-W33 Sol→Luna handoff — Selection proposal r1

Status: `READY_FOR_LUNA / SELECTION_PROPOSAL_ONLY / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at handoff creation: `EVIDENCE_REVIEWED`  
Current machine action: `stage:selection`  
Target Human Gate: `ARCHITECTURE_REVIEW`  
Sol/Luna operating authority: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`  
E/M/C advancement verification: `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-advance-sol-review-20260830-r1.md`

The caller must give Luna the exact current branch SHA containing this handoff, the Sol advancement verification, and the recovery-index update that points here. Luna must begin from that exact SHA. If remote branch HEAD differs before execution, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`; do not silently rebase, merge, switch basis, or force-push.

## 1. Objective

Perform only the W33 Selection proposal/materialization phase:

1. derive the canonical 37-row Candidate Matrix deterministically from the frozen E/M/C authority;
2. evaluate every Matrix candidate under the Selection rubric below;
3. create exactly one complete Candidate Selection assignment for every Matrix candidate;
4. validate Matrix and Selection against current Core;
5. record the proposal and any unresolved editorial questions in one Luna session record;
6. commit/push the Candidate Matrix, Candidate Selection, and Luna session record;
7. stop for Sol semantic review.

Do **not** create a Selection Stage Checkpoint and do **not** run `ADVANCE_STAGE`.

Successful endpoint:

`SELECTION CANDIDATE COMMITTED -> STOP FOR SOL REVIEW`

## 2. Frozen upstream authority

### Production State

At start verify:

- path: `sources/2026-W33/production-state.json`
- SHA-256: `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`
- lifecycle: `EVIDENCE_REVIEWED`
- next action: `stage:selection`
- Evidence / Materiality / Completeness: `passed`
- Selection: `pending`
- Architecture: `pending`
- Architecture Review: `pending`
- terminal reason: null

Production State must remain byte-identical during this task.

### Production Profile

Path:

`sources/2026-W33/production-profile.json`

SHA-256:

`19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`

Exact W33 scope dimensions:

- `current relevance`
- `technical significance`
- `carry-over obligations`

Temporal window:

- start: `2026-08-07T18:00:00-04:00`
- end/cutoff: `2026-08-14T18:00:00-04:00`

### Evidence acceptance

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/evidence-accepted.json`

- result-set identity: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- results: 37
- VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

### repaired Edition View acceptance

`sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/edition-views-accepted.json`

- View-set identity: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- acceptance SHA-256: `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`
- MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0

### Materiality Ledger

`sources/2026-W33/materiality-ledger-v2.json`

SHA-256:

`cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`

### Profile Completeness

`sources/2026-W33/profile-completeness-v2.json`

SHA-256:

`9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`

Accepted status:

`INCOMPLETE`

This is a bounded explicit limitation, not a request to reopen research.

## 3. Required read order

Before any write, read in this order:

1. `AGENTS.md` from reviewed main.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed main.
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed main.
4. `config/survey-production-v2.json` from reviewed main, especially `EVIDENCE_REVIEWED -> stage:selection -> SELECTION_COMPLETE`.
5. `schemas/candidate-matrix-v2.schema.json` from reviewed main.
6. `schemas/candidate-selection-v2.schema.json` from reviewed main.
7. `scripts/survey_architecture_v2.py` and `scripts/survey_architecture_v2_base.py` from reviewed main.
8. `scripts/survey_stage_validation_v2.py` from reviewed main.
9. `sources/2026-W33/production-profile.json`.
10. `sources/2026-W33/production-state.json`.
11. `sources/2026-W33/execution/index.md`.
12. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`.
13. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`.
14. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-advance-luna-r1.md`.
15. `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-advance-20260830-r1.md`.
16. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-advance-sol-review-20260830-r1.md`.
17. the exact frozen Evidence acceptance/cards, repaired Edition Views, Ledger, and Completeness.
18. this handoff.

For editorial precedent only, Luna may read `sources/2026-W32/candidate-selection-v0.1.md`. It is not W33 factual authority and must not override current Core or W33 Evidence.

If repository/Core authority materially contradicts this handoff, stop with `CORE_OR_AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 4. Core Selection contract

Current Core requires exactly two current-stage artifacts at `EVIDENCE_REVIEWED`:

- `candidate-matrix`
- `candidate-selection`

Candidate Matrix is a deterministic derivation. It is not a Luna semantic opinion.

Candidate Selection must:

- assign every Matrix candidate exactly once;
- use disposition only `SELECTED`, `HOLD`, `REJECT`, or `INSPECT`;
- give every assignment a non-empty rationale;
- use architecture usage only `PRIMARY`, `SUPPORTING`, or `NONE`;
- for `SELECTED`, use `PRIMARY` or `SUPPORTING` and at least one Profile-owned role;
- for every non-selected candidate, use `architecture_usage=NONE`, `publication_role=null`, `architecture_role=null`;
- never SELECT a Matrix candidate whose materiality is `NON_MATERIAL` or `HOLD`;
- never SELECT a candidate whose Evidence status is `REJECTED` or `NEEDS_MORE`;
- bind exact Profile/Matrix/Completeness/Materiality bytes.

The W33 research role namespace is `WEEKLY:`.  
The publication role namespace is `WEEKLY_MAGAZINE:`.

Human approval fields are forbidden in Candidate Selection.

## 5. Deterministic Candidate Matrix

Write the canonical Matrix at:

`sources/2026-W33/candidate-matrix-v2.json`

Use current Core derivation, equivalent to:

```bash
python scripts/survey_architecture_v2.py \
  --repo-root . \
  --implementation-sha 6267de3f6876f491950139757bfdf1085fc07bdc \
  matrix \
  --profile sources/2026-W33/production-profile.json \
  --discovery sources/2026-W33/discovery/discovery-v2.jsonl \
  --screening sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json \
  --evidence sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/evidence-accepted.json \
  --views sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/edition-views-accepted.json \
  --ledger sources/2026-W33/materiality-ledger-v2.json \
  --completeness sources/2026-W33/profile-completeness-v2.json \
  --output sources/2026-W33/candidate-matrix-v2.json
```

Expected structural result:

- candidate count: 37
- materiality: MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0
- Evidence: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

After generation, independently derive a fresh temporary Matrix and require exact byte-equivalent JSON content before commit.

Do not hand-edit Matrix rows.

## 6. Selection artifact

Write the proposal at:

`sources/2026-W33/candidate-selection-v2.json`

Use:

- `schema_version`: `2.0-rc1`
- `issue_id`: `2026-W33`
- `research_profile`: `WEEKLY`
- `publication_profile`: `WEEKLY_MAGAZINE`
- `selection_version`: `w33-selection-luna-r1`
- `status`: `ESTABLISHED`
- exact hash basis required by Core
- exactly 37 assignments

The Selection artifact is a **Luna proposal** until Sol reviews it. Core schema status `ESTABLISHED` does not mean Sol or Human approval.

## 7. Selection rubric

Evaluate each candidate independently. Do not optimize a target count.

### A. Eligibility is necessary, not sufficient

A candidate is technically eligible for `SELECTED` only when:

- materiality is `MATERIAL` or `CONTEXT`; and
- Evidence status is `VERIFIED` or `PARTIAL`.

`PARTIAL` may be selected when the verified portion is materially useful and its limitation can travel intact into Architecture. Do not promote unresolved claims merely because the candidate is otherwise important.

All `HOLD` / `NEEDS_MORE` candidates are non-selectable under current authority.

### B. MATERIAL does not mean automatically SELECTED

The 25 MATERIAL candidates are the main selection pool, not an instruction to create 25 independent stories.

Select only when the candidate adds meaningful marginal reader/editorial value after considering:

- current W33 relevance;
- concrete technical significance;
- evidence strength and remaining boundaries;
- distinctness from already stronger candidates;
- usefulness as a primary development or as technical depth for another development;
- ability to preserve attribution/limitation accurately.

A valid MATERIAL candidate can still be `REJECT` at Selection when its marginal contribution is redundant or too narrow for the issue architecture.

### C. Single-home / duplicate consolidation

One underlying event, product update, or factual development must not become multiple independent PRIMARY items solely because it appears in:

- a dedicated first-party page plus an index;
- a release note plus a corroborating index;
- several distribution/access-channel records;
- an event plus a community/X signal;
- overlapping Evidence records for the same editorial fact.

Choose a single strongest PRIMARY home when appropriate. Other eligible records may be:

- `SELECTED + SUPPORTING` if they add distinct corroboration, access/distribution context, chronology, or community reaction useful to Architecture; or
- `REJECT` if they add no material marginal value.

Do not call the supporting record a second independent launch/story.

### D. CONTEXT candidates

A `CONTEXT` candidate should normally be either:

- `SELECTED + SUPPORTING` when the context is materially useful to a selected PRIMARY candidate or issue-level synthesis; or
- `REJECT` when it is redundant/unnecessary.

Do not assign a CONTEXT candidate `PRIMARY` in this W33 proposal. If Luna believes a CONTEXT item must become PRIMARY, use `INSPECT` and explain why the existing Materiality authority appears insufficient.

X/community signal is context only. It can support editorial interpretation but cannot serve as technical validation.

### E. HOLD / NEEDS_MORE candidates

Freeze the six current Matrix HOLD candidates to Selection `HOLD`, absent a direct internal authority contradiction:

- unresolved MiniMax official-index lead;
- Claude retirement W32 carry-over;
- Copilot cloud-agent W32 carry-over;
- Kimi K3 Copilot W32 carry-over;
- OpenAI GPT-5.6 update W32 carry-over;
- RepoWise W32 carry-over.

Use `architecture_usage=NONE` and null roles.

Do not turn these into `REJECT` merely to make the issue look cleaner; preserving the unresolved obligation is useful provenance.

### F. REJECT semantics

Use `REJECT` when the candidate is sufficiently understood but should not consume Architecture space because, for example:

- it is redundant with a stronger single-home candidate;
- its marginal W33 contribution is too small;
- it is post-cutoff/index chronology that adds no needed support;
- a technically valid paper/release is less useful than stronger candidates in the same editorial function;
- it does not improve the eventual issue after consolidation.

A REJECT rationale must state the concrete reason, not just “lower priority.”

### G. INSPECT semantics

Use `INSPECT` sparingly and only when the frozen authority supports more than one materially plausible Selection disposition and the choice requires Sol editorial judgment.

An INSPECT rationale must state the exact decision question and alternatives.

Do not use INSPECT merely to avoid making a proposal.

Sol will resolve any INSPECT assignments before lifecycle advancement.

### H. Breadth without quotas

The issue should avoid collapsing into one narrow theme, but there is no quota by topic or vendor.

When deciding marginal value, consider whether the selected pool collectively preserves the strongest non-redundant developments across relevant W33 technical planes, including as applicable:

- model/API capability and availability;
- agents, coding, evaluation, tool use, and security;
- inference/serving/runtime/framework engineering;
- multimodal/media/voice generation;
- research methods with distinct technical contributions.

This is a coverage sanity check, not count balancing. Do not select a weak candidate solely to fill a category.

### I. Papers and infrastructure

Papers are not automatically relegated to Paper Watch and releases are not automatically standalone stories.

A paper may be PRIMARY when its contribution is one of the issue's strongest distinct technical developments. Otherwise it may be SUPPORTING technical depth or REJECT.

Serving/runtime/framework releases may be consolidated where they represent the implementation follow-through of the same model/deployment trend. Preserve distinct changes when they genuinely add different engineering substance.

### J. Chronology and attribution

Preserve exact `window_relation`, source attribution, and remaining Evidence boundaries from Matrix/View authority.

A vendor-, project-, author-, RSS-, index-, or paper-reported result remains attributed downstream. Selection does not upgrade it to independent verification.

Post-cutoff context must not be silently rewritten as an in-window launch.

## 8. Architecture usage

For each `SELECTED` candidate choose:

### `PRIMARY`

Use when the candidate can anchor a distinct Architecture package or a major factual strand within one.

### `SUPPORTING`

Use when the candidate should be available to Architecture to deepen, corroborate, contextualize, or provide community/chronology support for a PRIMARY development, but should not independently drive package creation.

Every non-selected candidate must use `NONE`.

Do not construct Architecture packages in this task. Usage is only a proposal signal for the next phase.

## 9. Role vocabulary

Use the following bounded W33 role vocabulary unless an exact candidate requires a better prefixed role. Any deviation must be listed in the Luna session.

### Publication roles

- `WEEKLY_MAGAZINE:FEATURE`
- `WEEKLY_MAGAZINE:SECTION_CORE`
- `WEEKLY_MAGAZINE:PAPER_WATCH`
- `WEEKLY_MAGAZINE:BRIEF`
- `WEEKLY_MAGAZINE:CHRONOLOGY`
- `WEEKLY_MAGAZINE:SUPPORTING_CONTEXT`
- `WEEKLY_MAGAZINE:COMMUNITY_SIGNAL`

### Architecture roles

- `WEEKLY:PRIMARY_DEVELOPMENT`
- `WEEKLY:PRIMARY_RESEARCH`
- `WEEKLY:TECHNICAL_DEPTH`
- `WEEKLY:INFRASTRUCTURE`
- `WEEKLY:SUPPORTING_CONTEXT`
- `WEEKLY:CHRONOLOGY`
- `WEEKLY:COMMUNITY_SIGNAL`

For clarity, every SELECTED candidate should normally receive both a publication role and an architecture role, even though Core only requires at least one.

Role labels are proposals for Architecture, not final package placement.

## 10. Assignment rationale quality

Every assignment rationale must be candidate-specific and decision-useful.

For SELECTED, state:

- the concrete development/contribution;
- why it survives consolidation into the W33 issue;
- why PRIMARY or SUPPORTING is appropriate;
- the material limitation/attribution that must remain downstream.

For HOLD, state the exact unresolved boundary.

For REJECT, state the exact redundancy/marginal-value/scope reason and, where relevant, identify the stronger single-home candidate by candidate ID or discovery ID.

For INSPECT, state the exact unresolved editorial choice.

Do not reuse generic templates across heterogeneous candidates.

## 11. `profile_extensions`

Default assignment `profile_extensions` to `{}`.

Do not use extensions as a hidden second Selection policy or as a place to alter upstream factual semantics. If a candidate genuinely needs a W33-specific note that cannot be represented by rationale/roles, document the key/value in the Luna session and keep it non-authoritative relative to upstream Evidence/View bytes.

## 12. Required validation

Before commit verify all of the following:

1. Candidate Matrix exactly equals fresh current-Core derivation from frozen upstream artifacts.
2. Matrix has exactly 37 candidates.
3. Matrix counts remain MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0.
4. Matrix Evidence counts remain VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0.
5. Candidate Selection validates against `schemas/candidate-selection-v2.schema.json`.
6. `survey_architecture_v2.py selection-check` returns PASS.
7. exactly 37 assignments exist and every Matrix candidate appears exactly once.
8. no HOLD/NON_MATERIAL or NEEDS_MORE/REJECTED candidate is SELECTED.
9. every SELECTED candidate has PRIMARY or SUPPORTING usage and W33-prefixed role(s).
10. every non-selected candidate has NONE usage and null roles.
11. all six frozen HOLD candidates remain Selection HOLD.
12. every CONTEXT SELECTED candidate is SUPPORTING; any proposed CONTEXT PRIMARY is instead INSPECT for Sol.
13. duplicate/single-home groups are explicitly reasoned rather than double-counted.
14. no generic assignment rationale boilerplate remains.
15. Production State SHA-256 remains `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`.
16. no Selection checkpoint or state advancement occurred.
17. no Architecture artifact was created.

Validate the proposed current stage without committing the validation report, equivalent to:

```bash
python scripts/survey_stage_validation_v2.py \
  --repo-root . \
  --state sources/2026-W33/production-state.json \
  --artifact candidate-matrix=sources/2026-W33/candidate-matrix-v2.json \
  --artifact candidate-selection=sources/2026-W33/candidate-selection-v2.json \
  --output <scratch-outside-repository-or-uncommitted-temp>/selection-stage-contract.json
```

The expected target is `SELECTION_COMPLETE`, but this task must not perform the transition.

## 13. Allowed repository writes

Only:

1. `sources/2026-W33/candidate-matrix-v2.json`
2. `sources/2026-W33/candidate-selection-v2.json`
3. one Luna session record under `sources/2026-W33/execution/sessions/`

Suggested session path:

`sources/2026-W33/execution/sessions/w33-luna-selection-20260830-r1.md`

Scratch/validation files must remain outside the committed repository tree.

## 14. Explicit prohibitions

Do not:

- browse the web or acquire new Evidence;
- edit Discovery or Screening;
- edit Evidence Cards or accepted Evidence;
- edit repaired Edition Views;
- edit Materiality Ledger or Profile Completeness;
- edit Production Profile or Production State;
- reinterpret accepted Materiality as a new Evidence decision;
- create a Selection checkpoint;
- run `ADVANCE_STAGE`;
- create Architecture, Architecture Review Summary, or Attention artifacts;
- begin drafting or publication work;
- infer Human approval;
- modify shared Core/config/schema/workflow files;
- force-push, rebase, or rewrite canonical history.

## 15. Git boundary

Before first write, verify remote branch HEAD still equals the exact caller-supplied start SHA.

Preferred commits:

1. candidate commit containing exactly Candidate Matrix + Candidate Selection;
2. bookkeeping commit containing exactly the Luna Selection session record.

Use normal fast-forward updates only.

If native transport cannot push and authenticated connector reconstruction is required, preserve exact trees/content, report local and canonical GitHub commit identities separately, and use GitHub canonical SHAs for recovery.

## 16. Luna Selection session record

Record at minimum:

- exact caller-supplied starting SHA;
- reviewed main SHA;
- local/canonical candidate and bookkeeping commit SHAs if different;
- Candidate Matrix path/SHA-256 and exact counts;
- Candidate Selection path/SHA-256 and `selection_version`;
- disposition counts and selected count;
- list of all SELECTED candidates with title, usage, publication role, architecture role;
- all INSPECT candidates and exact decision question;
- the six frozen HOLD candidates and confirmation they remained HOLD;
- all duplicate/single-home consolidations, identifying primary/supporting/rejected records;
- all CONTEXT candidates and whether SUPPORTING or REJECT;
- any role-vocabulary deviations;
- current-stage validation result;
- Production State start/end SHA-256;
- exact changed paths;
- explicit confirmation no checkpoint/ADVANCE_STAGE/Architecture work occurred;
- final stop reason.

Allowed final status:

`SELECTION_CANDIDATE_READY_FOR_SOL_REVIEW`

Failure statuses:

- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `CORE_OR_AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `SELECTION_AMBIGUITY_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`
- `TRANSPORT_FAILURE_NEEDS_SOL_REVIEW`

Use `SELECTION_AMBIGUITY_NEEDS_SOL_REVIEW` only if an ambiguity prevents producing a coherent full proposal. Ordinary uncertain candidates should be assigned `INSPECT` and included in the complete proposal.

## 17. Stop condition and next owner

Stop immediately after the Candidate Matrix, complete Candidate Selection proposal, and Luna session record are committed on the canonical branch and validation is complete.

Do not advance to `SELECTION_COMPLETE`.

Next owner: Sol.

Sol will review the exact proposal, resolve any INSPECT assignments, accept/revise/reject the Selection semantics, and only then create a separate deterministic advancement handoff.