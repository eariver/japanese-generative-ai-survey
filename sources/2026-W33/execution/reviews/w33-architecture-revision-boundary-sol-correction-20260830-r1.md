# 2026-W33 Sol correction — Architecture revision boundary r1

Decision: `BOUNDARY_CORRECTION_REQUIRED / CANDIDATES_NORMALIZED_INSUFFICIENT / RECOMMEND_ISSUE_INITIALIZED`

Issue: `2026-W33`  
Branch: `weekly/2026-W33-v2-work`

## Correction

The previously recommended Human regeneration boundary `CANDIDATES_NORMALIZED` is too shallow to satisfy the Human-requested carry-over repair under the current Core v2 source-binding contract.

This is a Sol recommendation defect, not a Human execution defect. The Owner explicitly approved the boundary that Sol recommended, and the canonical bridge correctly materialized that decision. The error was in Sol's earlier assumption about where fresh first-party source authority can enter the pipeline.

## Why `CANDIDATES_NORMALIZED` cannot satisfy the requested repair

Current `scripts/survey_evidence_v2.py` creates each Evidence Task with `source_records` copied exactly from the accepted Discovery record and validates every Evidence Card source URL against those task source locators.

The validator explicitly rejects a source not represented in the task Discovery source and instructs that it must be added through Discovery/Screening first.

The five active carry-over Discovery records are all currently bound only to the prior-week repository authority:

- source type: `prior-week-authority`
- collector: `repository-current-main`
- locator: current-main `sources/2026-W32/candidate-selection-v0.1.md`

They do not contain the fresh first-party vendor/project sources required by the Human revision.

Therefore fresh first-party Evidence for:

1. `carry-w32-claude-retirement`
2. `carry-w32-copilot-cloud-agent`
3. `carry-w32-kimi-k3-copilot`
4. `carry-w32-openai-gpt56-update`
5. `carry-w32-repowise`

cannot legally be added at the current Evidence stage without changing accepted Discovery/Screening authority.

## Why `ISSUE_INITIALIZED` is the minimum correct boundary

Core Human-Gate revision semantics preserve checkpoints completed before the selected boundary.

- `DISCOVERY_COLLECTED` preserves the Discovery checkpoint, so Discovery bytes remain frozen and fresh first-party Discovery records cannot be added.
- `CANDIDATES_NORMALIZED` preserves both Discovery and Screening, so Evidence remains bound to the old carry-over source records.
- `ISSUE_INITIALIZED` invalidates the Discovery checkpoint and permits a new bounded Discovery pass, followed by Screening and normal downstream regeneration.

Thus the minimum correct boundary for the Human-requested fresh-source repair is:

`ISSUE_INITIALIZED`

## Intended repaired Discovery pattern

The repair should preserve historical carry-over provenance rather than silently rewrite it away.

Preferred pattern, following the already successful Qwen carry-over resolution model:

- retain the existing five carry-over records as prior-week obligations/provenance;
- collect bounded fresh first-party W33 source records for the five obligations;
- add new GAP_FILL Discovery records with explicit linkage/provenance to the carry-over obligations;
- re-run Screening so resolved old carry-over records can be explicitly disposed/superseded where justified;
- create Evidence only from accepted first-party Discovery source records;
- regenerate Edition Views, Materiality, Completeness, Matrix, Selection, and Architecture;
- include the Human-required mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` Architecture chapter.

Do not assume all five have a positive W33 event. Fresh first-party research may establish a distinct W33 delta, stale continuity/no W33 delta, or a remaining bounded limitation. The obligation is explicit disposition, not forced inclusion.

## Current state complication

Architecture Review r1 has already been correctly recorded as:

- decision: `REQUEST_CHANGES`
- boundary: `CANDIDATES_NORMALIZED`

and Production State is now `CANDIDATES_NORMALIZED`.

Current canonical Human-Gate API requires an Architecture revision decision to be made while State is at the pending `ARCHITECTURE_ESTABLISHED / ARCHITECTURE_REVIEW` gate. It provides no direct operation to revise an already-applied regeneration boundary from an intermediate state.

Therefore the existing r1 record must remain immutable. It must not be edited or replaced.

## Canonical correction route

Absent a shared-Core maintenance change, the safe existing-contract route is:

1. deterministically replay the unchanged current accepted E/M/C, Selection, and Architecture authorities back to `ARCHITECTURE_ESTABLISHED` without new research or semantic changes;
2. return to Architecture Review r2;
3. obtain/record a new explicit Human `REQUEST_CHANGES` decision selecting `ISSUE_INITIALIZED`;
4. let Core invalidate Discovery and all downstream checkpoint authority;
5. then execute the bounded first-party carry-over repair from Discovery forward.

This replay is procedural only. It does not re-approve the blocked Architecture, does not start Drafting, and does not erase Architecture Review r1 history.

## Human authority required

Because the regeneration boundary is a Human-controlled field, Sol cannot reinterpret the Owner's prior approval of `CANDIDATES_NORMALIZED` as approval of `ISSUE_INITIALIZED`.

A new explicit Owner authorization for the corrected boundary is required before Architecture Review r2 can be materialized.

Sol recommendation:

`REQUEST_CHANGES / regeneration_boundary = ISSUE_INITIALIZED`

The requested substantive changes remain exactly the same:

- close or explicitly dispose the five active W32 carry-over obligations through fresh first-party W33 source authority;
- regenerate downstream authority;
- add an explicit mandatory Weekly synthesis chapter.

## Stop

Do not launch Luna carry-over Evidence research from the current `CANDIDATES_NORMALIZED` state. Doing so could only reproduce the old source gap or violate Evidence source-binding rules.
