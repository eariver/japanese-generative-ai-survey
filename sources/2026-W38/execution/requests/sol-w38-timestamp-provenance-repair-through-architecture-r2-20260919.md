# W38 execution instruction — timestamp provenance repair and fresh Human Architecture Review r2

Status: `EXECUTION_AUTHORITY / METADATA_ONLY_REPAIR / ARCHITECTURE_BYTES_FROZEN / FRESH_HUMAN_ARCHITECTURE_REVIEW_R2`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W38-v2-work`

## 1. Mission

Repair the W38 pre-Human-Gate timestamp provenance defect identified by Independent Sol audit **without regenerating Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture**.

The existing Human Architecture Review r1 shell/dossier must remain preserved as historical bytes but must not be used for Human decision because its dossier timestamp is future-dated.

Create a fresh Human Architecture Review r2 surface bound to the same Architecture content plus the append-only correction ledger, using actual timezone-aware wall-clock provenance.

Normal endpoint:

`ARCHITECTURE_ESTABLISHED / fresh Human Architecture Review r2 pending`

No Human decision is authorized in this execution.

## 2. Invocation guard

The Muse invocation MUST provide the exact current remote HEAD/tree after this request commit is pushed.

Before any write, verify read-only:

- remote `weekly/2026-W38-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- remote tree == Exact Starting Tree supplied in the invocation;
- Exact Starting SHA parent == `d9cc09784371fabcfc8f9274d406b13ca3713aab`;
- parent tree == `85d9bc8e88f6266db80f4caa6912a691ed13097a`;
- remote `main` HEAD == `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- remote `main` tree == `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

If any guard differs, perform zero repository/GitHub writes and STOP with expected/actual values.

If the local clone is stale, use the already-authorized bounded fetch + fast-forward-only synchronization pattern from:

`sources/2026-W38/execution/requests/sol-w38-stale-local-sync-and-resume-20260919.md`

Do not treat stale local `main` as authority; remote `origin/main` is the reviewed main authority.

## 3. Mandatory read order

Read at minimum:

1. this request;
2. `sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md`;
3. `sources/2026-W37/execution/provenance/w37-execution-time-correction-20260919.md`;
4. `sources/2026-W38/execution/reviews/architecture-r1.md`;
5. `sources/2026-W38/execution/reviews/architecture-r1-dossier.md`;
6. `sources/2026-W38/architecture-v2.json`;
7. `sources/2026-W38/architecture-review-summary-v2.json`;
8. `sources/2026-W38/architecture-review-attention-v2.json`;
9. `sources/2026-W38/production-state.json`;
10. `sources/2026-W38/execution/index.md`;
11. current review/governance authority for Human Architecture Review.

## 4. Frozen semantic authority

The following bytes are frozen for this repair and MUST NOT change:

- `sources/2026-W38/architecture-v2.json`
  - SHA-256 `c123f9af386d0c85e0abc41f4fd91ada7807b6a42816718f1c4e02a01ae5bc48`
- `sources/2026-W38/architecture-review-summary-v2.json`
  - SHA-256 `e286edc9817584c23996f160c0d6f8dbd3b6336e698976ce928e937dacd7969b`
- `sources/2026-W38/architecture-review-attention-v2.json`
  - SHA-256 `044545e97c2e161144a5e78150a0d825573b6ccd229e13aac90aaa21b00e3e09`

Also do not modify:

- Discovery artifacts;
- Screening artifacts;
- Evidence artifacts;
- Materiality artifacts;
- Completeness artifacts;
- Selection artifacts;
- candidate matrix/selection;
- Grok Raw/Sol r2 correction;
- existing r1 Human Architecture Review files;
- existing production-state history values;
- existing architecture-stage-validation-r1 bytes.

This is metadata/provenance repair only.

## 5. Correction authority

The new append-only correction ledger is:

`sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md`

It records Independent Sol audit wall time:

- JST `2026-09-19T14:04:15+09:00`
- UTC `2026-09-19T05:04:15Z`

It establishes that the following existing metadata fields are invalid as actual wall-clock chronology:

- Production State transitions after `ISSUE_INITIALIZED`;
- Sol Evidence review Date `06:05Z`;
- Sol Materiality/Selection review Date `06:20Z`;
- Sol Architecture review Date `06:35Z`;
- Architecture validation `recorded_at 06:44Z`;
- Human Architecture Review r1 dossier Date `07:00Z`.

Their substantive stage/review/validation identities remain usable as described by the correction ledger.

Do not rewrite those historical files merely to make their timestamps look plausible.

## 6. Current wall-clock requirement

For every **new** r2 review/session/provenance record created by this execution:

- obtain actual current wall-clock time at the moment of record generation;
- use an explicit timezone-aware timestamp;
- do not synthesize rounded stage times;
- do not copy a future monotonic timestamp from Production State;
- do not use a time later than the commit that eventually contains the record.

A suitable local source is the system clock, for example:

```bash
date --iso-8601=seconds
date -u --iso-8601=seconds
```

Use the actual output, not a prewritten value from this request.

If the system clock itself appears inconsistent with the Git commit clock by a material amount, STOP and report rather than fabricate a timestamp.

## 7. Fresh Human Architecture Review r2

Create new files; do not overwrite r1:

`sources/2026-W38/execution/reviews/architecture-r2.md`

`sources/2026-W38/execution/reviews/architecture-r2-dossier.md`

r2 must present the same Architecture triple from §4.

The reviewed repository authority for r2 should be the exact pre-r2 commit containing:

- unchanged Architecture triple;
- unchanged production artifacts;
- the W38 timestamp correction ledger.

The r2 surface must explicitly disclose:

1. r1 was not used for decision because its review-surface timestamp provenance was invalid;
2. r1 remains preserved;
3. no Architecture/Selection/Evidence bytes changed;
4. Production State/architecture-validation historical timestamp fields are invalid as actual wall-clock times under the correction ledger;
5. lifecycle/state identities remain authoritative;
6. Architecture content finding remains:
   - 7 packages;
   - 11 SELECTED / 1 HOLD;
   - 9 VERIFIED + 3 PARTIAL;
   - completeness LIMITED with 3/3 obligations SATISFIED;
   - no Architecture-content blocking finding identified by the prior Sol semantic review;
7. Human decision remains `PENDING`.

Do not create or infer `APPROVED` or `REQUEST_CHANGES`.

## 8. Review content fidelity

The r2 dossier may reuse the substantive r1 Architecture review content because Architecture bytes are unchanged, but it must:

- remove invalid future times as asserted chronology;
- point to the correction ledger;
- preserve all research/evidence limitations;
- preserve all seven Architecture packages;
- preserve the DeepSeek HOLD / GLM DROP treatment;
- preserve X-as-Raw-Observation boundary;
- preserve benchmark/reproduction caveats;
- preserve primary-source gaps;
- preserve counterfactual alternatives.

Do not silently strengthen any claim.

## 9. Human-readable execution index repair

Update:

`sources/2026-W38/execution/index.md`

The top-level current authority section is stale and currently says `ISSUE_INITIALIZED`.

Correct the navigation metadata to reflect actual machine authority:

- lifecycle: `ARCHITECTURE_ESTABLISHED`;
- terminal reason: `HUMAN_GATE_REACHED`;
- next action: `ARCHITECTURE_REVIEW`;
- Architecture Review: pending;
- r1 review surface: superseded for Human decision by timestamp-provenance repair, historical bytes retained;
- r2 review surface: current pending Human target;
- link the W38 correction ledger.

Do not hand-edit `production-state.json` in order to make the index match; the machine state is already semantically correct.

## 10. Session provenance

Create a short edition-local session/provenance note recording:

- Starting SHA/tree;
- reason for repair (#507 recurrence);
- exact correction-ledger path;
- Architecture triple SHA identity before/after = unchanged;
- changed paths;
- actual new record timestamps;
- r2 reviewed repository commit;
- r2 Human decision pending;
- shared-Core changed paths = 0;
- remote main unchanged;
- Production Line unchanged.

## 11. Validation

Before final commit/push:

1. verify the three frozen Architecture SHAs exactly equal §4;
2. verify Evidence/Selection/Architecture semantic files were not changed;
3. verify r1 files still exist and are unchanged;
4. verify new r2 files contain no Human decision;
5. verify new timestamps are not future-dated relative to actual current wall time;
6. verify new record timestamps do not post-date their containing commit after commit/read-back;
7. verify production-state lifecycle remains `ARCHITECTURE_ESTABLISHED`;
8. verify target gate remains `ARCHITECTURE_REVIEW`;
9. verify shared-Core changed paths = 0.

If a new r2 timestamp accidentally post-dates its containing commit, do not present r2 to the Human. Create a bounded correction before reporting completion.

Do not rerun the canonical Architecture stage transition merely to regenerate a validation timestamp; the existing stage validation result remains substantively valid with timestamp caveat.

## 12. Allowed changed-path envelope

Expected changed/added paths are limited to edition-local review/navigation/provenance surfaces such as:

- `sources/2026-W38/execution/reviews/architecture-r2.md`
- `sources/2026-W38/execution/reviews/architecture-r2-dossier.md`
- `sources/2026-W38/execution/index.md`
- one new W38 timestamp-repair session/provenance note

The correction ledger itself is already committed before this request.

No other path is needed for the normal repair.

If additional semantic-stage paths appear, STOP before push and report them.

## 13. Shared-Core freeze

Do not modify:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`
- `production/survey-core-v2`

Issue #507 remains generic Core work outside this edition-local repair.

## 14. Commit discipline

Stay on existing:

`weekly/2026-W38-v2-work`

Use normal commits and non-force push only.

Forbidden:

- new branch;
- force push;
- reset;
- rebase;
- squash;
- history rewrite;
- destructive cleanup.

## 15. Normal stop

Stop at:

`ARCHITECTURE_ESTABLISHED / fresh Human Architecture Review r2 pending`

Do not start Draft.

Do not record a Human decision.

Final report must include:

- Starting SHA/tree;
- correction ledger identity;
- unchanged Architecture triple SHAs;
- r2 review/dossier paths and SHAs;
- actual r2 generation timestamps;
- reviewed repository commit;
- ending SHA/tree;
- changed paths;
- production-state lifecycle/gate;
- main/Production Line unchanged;
- shared-Core changed paths = 0;
- exact stop reason.
