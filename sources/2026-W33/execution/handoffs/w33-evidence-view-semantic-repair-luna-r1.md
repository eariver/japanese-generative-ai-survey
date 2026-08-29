# 2026-W33 Sol→Luna handoff — Edition Evidence View semantic repair r1

Status: `READY_FOR_LUNA / EDITION_VIEW_SEMANTIC_REPAIR_ONLY / STOP_FOR_SOL_REREVIEW`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Sol review authority: `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`  
Original E/M/C policy: `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`  
Corrective Profile authority: `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md`  
Current lifecycle: `CANDIDATES_NORMALIZED`  
Requested stop: Sol re-review before any lifecycle advancement

The caller must supply the exact current branch SHA containing this handoff and the recovery-index update that points to it. Luna must start from that exact SHA. If the remote branch has moved before execution starts, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 1. Objective

Repair only the semantic quality of the W33 Weekly Edition Evidence Views while preserving the accepted factual Evidence bytes and source boundary.

The current candidate passed structural/Core validation but failed Sol semantic review because many materially different candidates reuse generic boilerplate in:

- `materiality.rationale`; and
- `profile_annotations.why_this_issue`.

The repair endpoint is:

`NEW ITEM-SPECIFIC VIEW SET + REGENERATED LEDGER/COMPLETENESS COMMITTED -> STOP FOR SOL REREVIEW`

Do not run `ADVANCE_STAGE`.

## 2. Frozen repair basis

### Production State

At start verify:

- path: `sources/2026-W33/production-state.json`
- SHA-256: `bc7d2cad5a2a53634b3eeaab12336dfd4a3c56e1db8677534c8dc5b03f60ba6f`
- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- Screening: `passed`
- Evidence / Materiality / Completeness: `pending`
- terminal reason: null

Production State must remain byte-identical throughout this repair.

### Accepted Evidence — immutable

Freeze this exact accepted Evidence run byte-for-byte:

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/`

- result-set identity: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- package SHA-256: `2655553661ebb6c2b0d2710403d2f8d0492f2d3e248ad3f71ffd06a561b7f39d`
- acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- task/result count: 37
- status distribution: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

No Evidence Task, Evidence Card, package, or Evidence acceptance byte may change.

### Current rejected View candidate — read-only historical input

Current historical View candidate:

`sources/2026-W33/evidence/v2/views/accepted/b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6/`

- view-set identity: `b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6`
- candidate distribution: MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0

Do not rewrite or delete this content-addressed historical run. It may be read as the previous proposal only.

### Current derived artifacts — replace by deterministic regeneration

Current candidate derived files:

- `sources/2026-W33/materiality-ledger-v2.json`
- `sources/2026-W33/profile-completeness-v2.json`

These are allowed to be replaced only because a new accepted View set necessarily changes their exact basis hashes. They must be regenerated through current Core, not manually edited.

## 3. Required read order

Before any repair write, read in order:

1. `sources/2026-W33/production-state.json`
2. `sources/2026-W33/production-profile.json`
3. `sources/2026-W33/execution/index.md`
4. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
5. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
6. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md`
7. `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-20260830-r1.md`
8. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`
9. `config/prompts/evidence-verification-v2.md`
10. `scripts/survey_evidence_v2.py`
11. `scripts/survey_completeness_v2.py`
12. accepted Evidence package and all 37 exact accepted Evidence Cards under `c86f49...`
13. current historical View candidate under `b6c605...`
14. this handoff

If exact repository/Core authority contradicts this handoff, stop rather than inventing a repair.

## 4. Sol semantic decisions frozen for this repair

### No upstream source expansion

Do not acquire a new Evidence source, alter Discovery/Screening, or mutate the Evidence accepted run.

The six current `NEEDS_MORE` tasks are legitimate unresolved outputs under the frozen authority:

- MiniMax official index;
- Claude retirement carry-over;
- Copilot cloud-agent carry-over;
- Kimi K3 Copilot carry-over;
- OpenAI GPT-5.6 update carry-over;
- RepoWise carry-over.

They do not trigger an upstream rewind in this repair.

### `INCOMPLETE` is allowed to remain

Profile Completeness may remain `INCOMPLETE` if current Core derives that result after the View repair. Do not force `READY` or `LIMITED`.

Selection later cannot select `HOLD` / `NEEDS_MORE` candidates under current Core. The visible limitation is therefore safe to carry forward after Sol accepts the repaired E/M/C package.

### Frozen default dispositions for 11 INSPECT/MAYBE records

Unless the **already accepted Evidence bytes themselves** expose an internal contradiction, retain these Sol-reviewed defaults:

| Discovery | Evidence | Materiality default |
|---|---|---|
| `base-official-index-minimax-news` | NEEDS_MORE | HOLD |
| `base-official-index-zai-release-notes` | PARTIAL | CONTEXT |
| `gapfill-model-glm-5_3` | PARTIAL | MATERIAL |
| `base-arxiv-2608_09666v1` | PARTIAL | CONTEXT |
| `base-arxiv-2608_13900v1` | VERIFIED | MATERIAL |
| `base-arxiv-2608_13613v1` | PARTIAL | MATERIAL |
| `carry-w32-claude-retirement` | NEEDS_MORE | HOLD |
| `carry-w32-copilot-cloud-agent` | NEEDS_MORE | HOLD |
| `carry-w32-kimi-k3-copilot` | NEEDS_MORE | HOLD |
| `carry-w32-openai-gpt56-update` | NEEDS_MORE | HOLD |
| `carry-w32-repowise` | NEEDS_MORE | HOLD |

If a contradiction is found, do not silently change a frozen default. Record it and stop with `SEMANTIC_CONFLICT_NEEDS_SOL_REVIEW`.

## 5. Repair rule for all 37 Views

Create a new View for every accepted Evidence task by re-reading its exact Evidence Card.

For every item, independently answer:

1. What concrete development/fact is established by this Evidence Card?
2. What is its relationship to the W33 window or explicit carry-over obligation?
3. Why is it MATERIAL, CONTEXT, NON_MATERIAL, or HOLD under the existing Sol rubric?
4. What exact source/attribution/verification limitation constrains that conclusion?

Then materialize item-specific values.

### `materiality.rationale`

Must be candidate-specific. It must identify the concrete reason for the chosen materiality status.

### `profile_annotations.why_this_issue`

Must be candidate-specific and useful to later Selection/Architecture. It should explain why this particular item belongs in W33 consideration, rather than merely restating a generic status definition.

It may overlap semantically with `materiality.rationale`, but should be written as a Weekly issue relevance statement rather than a boilerplate label.

### `scope_dimensions`

Use only exact W33 Profile strings:

- `current relevance`
- `technical significance`
- `carry-over obligations`

Do not invent adjacent dimensions.

### `window_relation` and `carry_over`

These remain factual chronology annotations. Do not change them to support a preferred editorial result.

## 6. Status-specific requirements

### MATERIAL

The rationale/why-this-issue must identify:

- the concrete W33 development;
- the specific technical/editorial significance;
- and any material attribution or unresolved boundary.

Examples of acceptable reasoning dimensions are model capability/release availability, runtime/framework change, new method/system contribution, deployment/distribution change, or another concrete verified delta. Do not use a generic sentence such as “distinct W33 development with technical substance.”

### CONTEXT

State the exact contextual function, such as:

- duplicate/index chronology;
- corroboration of a dedicated event;
- post-cutoff relationship;
- unresolved novelty overlap;
- X/community reaction/signal;
- or another specific relation.

Do not use a generic list of possible context roles.

### HOLD

Name the exact unresolved fact and frozen-source reason. For carry-over tasks, say which W33 delta cannot be established. For MiniMax, say that the accepted official index lacks a dated qualifying W33 event body.

### NON_MATERIAL

If any item changes to NON_MATERIAL, state the concrete reason the evidence establishes it should not contribute materially to W33.

## 7. Status changes outside the frozen 11

For the other 26 active records, Luna may revise the previous status using **only the existing accepted Evidence bytes**.

Do not preserve a status mechanically just because it was in `b6c605...`.

Every status change must be listed in the repair session with:

- discovery ID;
- evidence task ID;
- old status;
- new status;
- exact Evidence-based reason.

No count-balancing or issue-shape optimization is allowed here. Selection/Architecture comes later.

## 8. Materialization sequence

1. Build a complete 37-file temporary View set from the frozen Evidence acceptance.
2. Validate every View against current schema/Core rules.
3. Accept the complete set through current Core into a **new content-addressed accepted View run**.
4. Verify the new view-set identity differs from `b6c605...` when bytes differ.
5. Rebuild `sources/2026-W33/materiality-ledger-v2.json` from the exact new View acceptance using current Core.
6. Replace the root Ledger with that deterministic derivation.
7. Rebuild/revalidate `sources/2026-W33/profile-completeness-v2.json` against the new Ledger.
8. Run current-stage validation with the frozen Evidence acceptance + new View acceptance + regenerated Ledger + regenerated Completeness.
9. Confirm Production State byte identity is unchanged.
10. Commit the bounded repair artifacts and one repair session record.
11. Stop for Sol re-review.

Do not create an Evidence/Materiality/Completeness checkpoint and do not run the operator bridge.

## 9. Allowed repository writes

Only these categories are allowed:

- a **new** content-addressed accepted Edition View run under `sources/2026-W33/evidence/v2/views/accepted/<new-view-set>/...`;
- replacement `sources/2026-W33/materiality-ledger-v2.json`, deterministically regenerated from the new accepted View run;
- replacement `sources/2026-W33/profile-completeness-v2.json`, regenerated/revalidated from the new Ledger;
- one repair session record under `sources/2026-W33/execution/sessions/`.

Suggested session path:

`sources/2026-W33/execution/sessions/w33-luna-evidence-view-semantic-repair-20260830-r1.md`

Scratch files outside the repository are allowed and must not be committed.

## 10. Explicitly forbidden writes/actions

Do not modify:

- `sources/2026-W33/production-state.json`;
- `sources/2026-W33/production-profile.json`;
- Discovery;
- Screening;
- the accepted Evidence run `c86f49...`;
- the old View accepted run `b6c605...`;
- previous handoffs/reviews/sessions/checkpoints;
- shared Core/config/schemas/workflows;
- Selection/Architecture/Draft/publication artifacts.

Do not:

- browse for or add new Evidence authority;
- create a checkpoint;
- run `ADVANCE_STAGE`;
- begin Selection;
- infer Human approval.

## 11. Validation requirements

Before commit verify:

- exact accepted Evidence result-set remains `c86f49...`;
- exactly 37 repaired Views exist;
- every View binds the exact current Evidence SHA;
- no `materiality.rationale` is empty or generic status boilerplate;
- no `why_this_issue` is empty or generic status boilerplate;
- each rationale/why-this-issue names or unmistakably identifies the candidate-specific development/context/gap;
- all six NEEDS_MORE Evidence results remain HOLD unless Core requires otherwise;
- the 11 frozen INSPECT/MAYBE defaults remain unchanged absent a reported contradiction;
- any other materiality status change is explicitly enumerated;
- only exact Profile dimensions are used;
- new View acceptance validates;
- Ledger is exactly equal to a fresh Core derivation and contains 41 rows;
- Completeness validates and retains all three initial obligations;
- Production State SHA-256 remains `bc7d2cad5a2a53634b3eeaab12336dfd4a3c56e1db8677534c8dc5b03f60ba6f`;
- no checkpoint or lifecycle transition occurred.

## 12. Repair session record

Record at minimum:

- exact caller-supplied starting SHA;
- local and canonical GitHub commit identities if transport reconstruction differs;
- old and new View-set identities;
- old and new materiality distributions;
- all status changes;
- confirmation the 11 frozen defaults were retained or exact conflict details;
- confirmation Evidence `c86f49...` bytes were unchanged;
- new Ledger SHA-256 and equality-to-Core proof;
- new Completeness SHA-256, overall status, obligation summary, residual limitations;
- Production State starting/ending SHA-256;
- exact changed paths;
- validators run;
- stop reason.

Allowed stop statuses:

- `READY_FOR_SOL_REREVIEW`
- `SEMANTIC_CONFLICT_NEEDS_SOL_REVIEW`
- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`

## 13. Stop condition

Stop immediately after the repair commit(s) are on the canonical work branch and all validation is complete.

Do not advance to `EVIDENCE_REVIEWED`.

Sol will review the exact repaired bytes and, only if they pass, create a separate deterministic advancement handoff.
