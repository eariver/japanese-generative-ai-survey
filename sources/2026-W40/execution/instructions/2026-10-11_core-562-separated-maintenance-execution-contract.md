# Core #562 — Bounded separate maintenance execution contract (NOT YET WRITE-AUTHORIZED)

Status: `PREPARED / ZERO_CORE_WRITES_UNTIL_EXPLICIT_BRANCH_AUTHORITY`  
Date: 2026-10-11 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Issue: `#562 / CV2-DM-022`  
Reviewed main HEAD/Tree: `afdb3df3faa20af3bb5798be429bba8dbd2100b1` / `fe3f07c653f255f67087b4b46d006f8943df7115`  
Source briefing: `sources/2026-W40/execution/core-562-readonly-resumption-assessment-20261011.md`.

## 0. Absolute Core branch/write guard

**This file is a prepared implementation contract, NOT permission to create a branch, edit shared Core, change Issue #562, or start W40 Selection.** Require Owner-approved separate dedicated existing Core branch with exact remote HEAD/Tree, OR express authority to create a named dedicated Core branch from reviewed main. Without authorization, STOP at READ_ONLY. Never repurpose unrelated existing branches. Before work verify remote Core branch SHA/tree, remote main SHA/tree and the W40 branch's independently supplied exact HEAD/Tree; stale any => ZERO WRITES. No fallback/repair/review branch, no force/reset/rebase.

## 1. Scope: safe EVIDENCE_REVIEWED same-state supersession

Implement the smallest reviewed generic Core operation satisfying Issue #562, not a W40-specific hack:
- restrict to `EVIDENCE_REVIEWED`, Selection/Architecture pending, Human Gates pending with null provenance, exception inactive, explicit separately recorded Sol scope decision, exact changed-ID allowlist and old accepted/checkpoint SHAs;
- validate W40 remote HEAD and tree, reviewed Core/main identities, old acceptance basis and source-profile identity; preserve every old SHA/byte/history; append an auditable old→new supersession record with exact reviewer and reasons;
- version new immutable acceptance artifacts; transactional all-or-nothing validation/publication, stale/ref failures reject before activation, idempotent replay clear; no backward lifecycle transition, no fabricated Human Gate, no hand-edit of Production State;
- candidate evidence for hosted issuer articles bound to original Discovery task by exact Evidence Authority Supplement and lawful primary Raw body/archive policy; reject false model/dataset publication claims, invalid or out-of-window timestamps, missing hash or source locator;
- **first test** retaining the 37 Discovery and 37 Screening decisions `INSPECT` (non-DROP), while explicitly preserving and superseding historically stale publication-time rationale. If semantics requires changing accepted Screening rationale, choose minimum separately validated versioned Screening successor with diff allowlist; explain why.
- new Evidence Cards 35, Edition Views 35, Materiality Ledger 37, Completeness, Matrix/Selection preview must all validate against new exact basis; proposed AstaBrief/AutoSynthData `MATERIAL` remains editorial/provisional until independently reviewed. Old 28 selected remains unchanged as historical SHA-bound staging.

## 2. Required negative and cross-profile tests

Reject stale HEAD/tree/main or acceptance SHA; unauthorized IDs; wrong lifecycle; reviewed/present Human Gate; active exception; missing or changed Raw source/hash; unbound sources; malformed time; Evidence/View disagreement; incomplete 35/37 mapping; failed validators without partial activation; attempted backward state transition; duplicate replay. Test both WEEKLY and one non-WEEKLY profile. Repeat deterministic builds and compare content/SHA. Verify old accepted bytes remain reachable.

## 3. Review, handoff, hard stop

Submit Core-only implementation/tests/schema/docs on the **separately approved Core branch**; provide full starting/final SHA/tree, changed paths, per-requirement test evidence, old/new provenance semantics, explicit limitations. Independently review Core and use normal PR review/merge authority only after Owner approval; no unapproved auto-merge. Do not modify W40 in the Core unit. After merge into main, create a new separate SHA-guarded W40 supersession execution contract and **stop at Sol Evidence/Materiality re-review**, not Selection/Human Gate/publication.

Until Core branch authority supplied, TERMINAL: `AWAIT_EXPLICIT_CORE_MAINTENANCE_BRANCH_AUTHORITY`.
