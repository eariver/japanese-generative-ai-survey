# TS-002 Issue #543 — Sol authoritative terminology map r6 (r9-next2 candidate resolution)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / R9_CONTINUATION / APPLY_WITHOUT_REINTERPRETATION`

## 1. Scope and authority

This file resolves the single `CANDIDATE_FOR_SOL_REVIEW` entry returned by Muse after applying the Sol r5 map during the same Human Publication Preview r9 `REQUEST_CHANGES` execution.

Human r9 authority remains active because the edition is still at `DRAFT_COMPLETE`; no new Human revision is required or authorized.

This file supplements the r2, r3, r4, and r5 Sol terminology maps. All earlier decisions remain frozen unless this file explicitly addresses this residual grammatical variant.

Frozen Core v2 remains immutable. Muse MUST NOT alter Core implementation, scripts, schemas, contracts, stage plan, transition rules, compatibility logic, templates, or shared configuration.

## 2. Candidate decision

### SOL-R6-N2-001 — `joint化` (Movie Gen / reception summary)

The two residual occurrences are grammatical variants of the concept already adjudicated by Sol r3 S016: audio-video joint generation / integrated audio-video generation.

Decision:

1. Capstone sentence:

- `映像のjoint化では、抄録段階のMovie Genと2026年の現行群を、開示の厚みの差を明示して並べる。`

must become:

> `音声・映像の同時生成では、抄録段階のMovie Genと2026年の現行群を、開示の厚みの差を明示して並べる。`

2. Reception-ledger sentence:

- `映像4件はjoint化の提供条件`

must become:

> `映像4件は音声・映像同時生成の提供条件`

Do not retain `joint化` as reader-facing terminology. Do not create a broader architecture claim beyond the already accepted Movie Gen / current-product capability boundary.

No citation change is authorized by this decision.

## 3. Closure rule

After applying this r6 map, Muse MUST again run the full pre-validation broad suspicious-translation scan over the reader-facing manuscript.

If any new unmapped candidate is found:

- do not modify it;
- record it in `sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r9-next3.md`;
- remain at `DRAFT_COMPLETE` under the same Human r9 authority;
- do not create r10.

If unresolved candidate count is zero, Muse may proceed through the existing Frozen Core path:

`DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE`

and stop at `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`.

No Freeze, Release, merge, or new Human approval is authorized.
