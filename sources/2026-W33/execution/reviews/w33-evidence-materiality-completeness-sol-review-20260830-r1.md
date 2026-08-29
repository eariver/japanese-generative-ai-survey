# W33 Evidence / Materiality / Completeness Sol review — 2026-08-30 r1

Issue: `2026-W33`  
Reviewer: `ChatGPT GPT-5.6 Sol`  
Reviewed branch: `weekly/2026-W33-v2-work`  
Luna exact starting SHA: `75d4cd6d14a73eee548fc52d3a460a7887e9c855`  
Canonical GitHub candidate commit: `8734705209cc14f79cb09c2f016f421d44a1df17`  
Canonical GitHub reviewed head: `164e1f2bfbd33cbda8b5dd6f0a0d9a3c12129538`  
Luna record: `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-20260830-r1.md`  
Sol policy: `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md` plus corrective overlay `w33-evidence-materiality-completeness-luna-r2.md`

## Review decision

`REPAIR_REQUIRED / EVIDENCE_LAYER_ACCEPTED_AS_REPAIR_BASIS / EDITION_VIEW_SEMANTIC_REPAIR_REQUIRED / NO_UPSTREAM_SOURCE_EXPANSION`

The Luna candidate is structurally strong and preserves the frozen source boundary correctly. The factual Evidence accepted run is suitable to freeze as the input basis for a bounded repair. The current Edition Evidence View set is **not yet accepted as semantic authority**, because its `materiality.rationale` and Weekly `profile_annotations.why_this_issue` are systematically too generic across heterogeneous candidates.

This is a bounded downstream semantic-repair case, not a reason to restart Discovery, Screening, or Evidence research.

Production State must remain `CANDIDATES_NORMALIZED`. No `ADVANCE_STAGE` is authorized by this review.

## Canonical Git / transport boundary

GitHub is the recovery authority.

Canonical remote chain:

1. exact Luna start: `75d4cd6d14a73eee548fc52d3a460a7887e9c855`
2. candidate artifacts: `8734705209cc14f79cb09c2f016f421d44a1df17`
3. Luna bookkeeping/session: `164e1f2bfbd33cbda8b5dd6f0a0d9a3c12129538`

The user/Luna reported local chain is:

- `75d4cd6d... -> 3bb7eb09... -> ee332534...`

Those local commit identities are transport provenance only. Repository navigation and all later handoffs must use the canonical GitHub chain above. The remote history is two commits ahead / zero behind from the supplied starting SHA and is a fast-forward descendant.

Remote candidate commit tree: `03db1583cd8532bdc2a7fee09e11fdb6fa14e6d2`.  
Remote final reviewed tree: `d80c198323801102cb2bc72ec5d334fb9c052e2c`.

The second remote commit adds only the Luna session record; candidate artifact bytes are therefore those established by `8734705209cc14f79cb09c2f016f421d44a1df17`.

## Candidate artifact identity

### Evidence

Accepted Evidence root:

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/`

- result-set identity: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- package SHA-256: `2655553661ebb6c2b0d2710403d2f8d0492f2d3e248ad3f71ffd06a561b7f39d`
- acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- task/result count: 37
- Evidence status distribution: `VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0`

The 37 tasks exactly cover all non-DROP Screening records. The four Screening DROP records receive no Evidence task.

### Edition Evidence Views

Current candidate View root:

`sources/2026-W33/evidence/v2/views/accepted/b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6/`

- candidate view-set identity: `b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6`
- acceptance SHA-256: `2a0e440473bab5d56cc0ae8ac58ef6d494ed1a80733f8869092c524da42bdbc5`
- current proposal distribution: `MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0`

This View set remains immutable historical candidate provenance. It is **not** the accepted semantic View authority for lifecycle advancement.

### Derived artifacts

- Materiality Ledger: `sources/2026-W33/materiality-ledger-v2.json`
  - candidate SHA-256: `1e092842633c90f3f2d1d1a9fd0fc3e497f2aea300b41bd63ec419ee0cad0a0b`
  - 41 rows, exactly one per Discovery record
- Profile Completeness: `sources/2026-W33/profile-completeness-v2.json`
  - candidate SHA-256: `4f670dbc75997084826f6a1cd6851a9afcb53bb2a4d2aa86e394c9d289c95463`
  - overall status: `INCOMPLETE`

Both are valid current-Core derivations from the candidate View set but must be regenerated after the View repair because their basis hashes will change.

## What passes Sol review

### 1. Source authority boundary

Luna correctly kept every Evidence Card source inside the generated task's accepted Discovery source authority. It did not silently add a better URL, mutate Discovery/Screening, or promote X/community material into technical authority.

`x-weekly-signal-wave` remains contextual/social evidence: its technical claims are not treated as independently verified technical authority.

### 2. Coverage and Core invariants

The candidate has:

- exactly 37 Evidence tasks/results for the 37 non-DROP records;
- one accepted View per accepted Evidence result;
- exactly 41 Materiality Ledger rows;
- all three exact W33 Profile dimensions only:
  - `current relevance`
  - `technical significance`
  - `carry-over obligations`;
- all three initial obligations preserved:
  - `weekly:current-relevance`
  - `weekly:technical-significance`
  - `weekly:carry-over`.

The Luna-reported current-stage validator, direct schemas, Evidence acceptance, View acceptance, deterministic Ledger validation, and Profile Completeness validation all passed.

### 3. Unresolved evidence is preserved rather than guessed

Six Evidence tasks are `NEEDS_MORE`: MiniMax plus five active W32 carry-over rechecks. That is appropriate under the frozen source contract.

The five active carry-over tasks are bound only to prior-week W32 selection authority. They cannot establish a fresh W33 first-party delta from those bytes. Luna correctly kept them `NEEDS_MORE / HOLD` rather than inventing chronology or adding unapproved first-party sources.

MiniMax likewise remains unresolved because the bound official index capture does not establish a dated qualifying W33 event body.

### 4. `INCOMPLETE` Completeness is a valid explicit limitation

Current Profile Completeness records:

- `weekly:current-relevance` -> `LIMITATION`
- `weekly:technical-significance` -> `LIMITATION`
- `weekly:carry-over` -> `NEEDS_RESEARCH`

Sol does **not** authorize a Discovery/Screening rewind or source expansion merely to force this status to `READY`.

Current Core stage validation requires Profile Completeness to be internally valid; it does not require `overall_status=READY`. Later Selection additionally forbids `HOLD` or `NEEDS_MORE` candidates from becoming `SELECTED`. Therefore the unresolved carry-over/MiniMax items can remain visible limitations and safely flow downstream as non-selectable candidates.

No Human Exception Gate is required for this condition.

## Sol-reviewed INSPECT / MAYBE dispositions

The current first-pass status/materiality proposals for the 11 Screening `INSPECT` / `MAYBE` records are semantically acceptable and should be treated as frozen defaults for the repair unless the exact existing Evidence bytes reveal an internal contradiction.

| Discovery | Screening | Evidence | Sol-reviewed materiality default | Boundary |
|---|---|---|---|---|
| `base-official-index-minimax-news` | INSPECT | NEEDS_MORE | HOLD | No dated qualifying W33 event body in bound index |
| `base-official-index-zai-release-notes` | INSPECT | PARTIAL | CONTEXT | Aug-18 index entry cannot resolve relation to Aug-14 gap-fill |
| `gapfill-model-glm-5_3` | INSPECT | PARTIAL | MATERIAL | First-party metadata establishes Aug-14 GLM-5.3 event/coding-cyber framing; detailed body claims remain unavailable |
| `base-arxiv-2608_09666v1` | MAYBE | PARTIAL | CONTEXT | Open-EA/EA-CoT-10K/EA-3B established; novelty delta from earlier ACL work unresolved |
| `base-arxiv-2608_13900v1` | MAYBE | VERIFIED | MATERIAL | Semantic ACID definitions/data-agent framework established; evaluation remains author-reported |
| `base-arxiv-2608_13613v1` | MAYBE | PARTIAL | MATERIAL | Unified generation/editing + diffusion-transformer contribution established; detailed baselines absent |
| `carry-w32-claude-retirement` | INSPECT | NEEDS_MORE | HOLD | Prior-week HOLD_OUT only; no fresh W33 first-party delta |
| `carry-w32-copilot-cloud-agent` | INSPECT | NEEDS_MORE | HOLD | Prior-week HOLD_OUT only; no fresh W33 first-party delta |
| `carry-w32-kimi-k3-copilot` | INSPECT | NEEDS_MORE | HOLD | Prior-week HOLD_OUT only; no fresh W33 first-party delta |
| `carry-w32-openai-gpt56-update` | INSPECT | NEEDS_MORE | HOLD | Prior-week HOLD_OUT only; no fresh W33 first-party delta |
| `carry-w32-repowise` | INSPECT | NEEDS_MORE | HOLD | Prior-week HOLD_OUT only; no fresh W33 first-party delta |

For GLM-5.3 and the two PARTIAL/MATERIAL research cases, later editorial language must stay inside the exact factual boundary; materiality does not convert unresolved benchmark/detail claims into verified facts.

## Blocking semantic defect: generic Edition View rationales

The candidate View set repeatedly uses generic boilerplate where r1 required each View to contain a concise but **decision-useful** rationale and accurate Weekly `why_this_issue`.

For example, materially different candidates such as SGLang, GLM-5.3, Agentic Transaction, VoiceDesigner, multiple other papers, runtimes, and model releases use the exact same MATERIAL text:

> `First-pass MATERIAL proposal: the bound source establishes a distinct W33 development with issue relevance and technical substance; source-attributed claims remain labeled.`

Likewise, distinct contexts such as official release indexes, the Open-EA novelty-overlap case, X/community signal, and the post-cutoff Z.ai index reuse the same CONTEXT text:

> `First-pass CONTEXT proposal: this bound source supplies chronology, corroboration, overlap, or community context rather than an independent main development.`

The `profile_annotations.why_this_issue` field repeats those same boilerplate strings.

This is not a JSON/schema defect; it is a **semantic/editorial authority defect**. The text does not identify the concrete W33 change, technical significance, contextual role, overlap, or limitation for the individual candidate.

This matters downstream because Candidate Matrix carries the Edition View `profile_annotations` into Selection. Accepting generic `why_this_issue` now would erase the item-specific reasoning needed for Selection and Architecture.

## Required bounded repair

The repair must **not** redo factual research. Freeze the accepted Evidence run `c86f49...` byte-for-byte.

Create a new content-addressed Edition View set from the same exact Evidence acceptance, with every one of the 37 Views receiving item-specific semantic treatment.

For every View:

1. re-read the exact accepted Evidence Card;
2. evaluate the materiality status under the existing Sol rubric;
3. write an item-specific `materiality.rationale`;
4. write an item-specific Weekly `profile_annotations.why_this_issue`;
5. preserve factual `window_relation` and `carry_over` semantics;
6. use only the three exact W33 Profile dimensions.

A MATERIAL rationale must state at least:

- the concrete W33 development; and
- the concrete technical/editorial reason it matters now;
- plus any material attribution/limitation that constrains downstream wording.

A CONTEXT rationale must state exactly what context it contributes, such as:

- chronology;
- corroboration;
- duplicate/index overlap;
- post-cutoff relation;
- community signal;
- or another specific bounded role.

A HOLD rationale must state the exact unresolved question and why the frozen source authority cannot close it.

Do not mechanically replace one generic template with another.

### Status changes during repair

The 11 INSPECT/MAYBE defaults above should remain unless exact existing Evidence bytes contradict them.

For the remaining 26 active candidates, Luna must re-evaluate the current status while producing item-specific reasoning. A status change is allowed **without new sources** if the existing Evidence clearly supports a different application of the Sol rubric. Every changed status must be listed explicitly in the repair session record with old status, new status, and reason.

No status may be changed merely to balance counts or simplify Selection.

## Derived artifact repair

After accepting the new View set through current Core:

1. regenerate `sources/2026-W33/materiality-ledger-v2.json` deterministically from the new View acceptance;
2. regenerate/revalidate `sources/2026-W33/profile-completeness-v2.json` against the new Ledger;
3. preserve legitimate `INCOMPLETE`, `LIMITED`, or `READY` outcome exactly as Core derives it;
4. do not force carry-over closure.

The old View accepted run remains immutable historical candidate provenance. Do not delete or rewrite it.

## Explicitly not authorized

This review does not authorize:

- new web/source acquisition for Evidence;
- Discovery or Screening mutation;
- Evidence Card edits;
- accepted Evidence run edits;
- Production State edits;
- checkpoint creation;
- `ADVANCE_STAGE`;
- Selection or Architecture work;
- Drafting/publication work;
- Human Gate action.

## Acceptance condition after repair

Sol will re-review the repaired candidate for:

- exact same Evidence result-set identity `c86f49...`;
- 37 item-specific View rationales/`why_this_issue` values;
- materiality status fidelity to the existing rubric;
- explicit accounting of any status changes;
- exact Profile dimensions;
- deterministic 41-row Ledger regeneration;
- valid Profile Completeness;
- unchanged Production State;
- no upstream or downstream scope drift.

Only after that re-review passes will Sol authorize a separate deterministic transition:

`CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED`.
