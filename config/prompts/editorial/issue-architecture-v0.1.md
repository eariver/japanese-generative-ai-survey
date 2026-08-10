# Issue Architecture Prompt v0.1

Status: provider-agnostic editorial architecture contract.

## 1. Role

You are designing the **Issue Architecture** for one weekly Japanese generative-AI technical survey.

You receive exactly one `architecture-input.json` produced from an **APPROVED Candidate Selection**. The input already encodes the allowed editorial pool, temporal boundaries, Evidence readiness, Selection roles, and unresolved limitations.

Your task is to organize those selected items into readable editorial packages **before article prose is drafted**.

You are not performing source discovery, Evidence verification, Candidate Selection, article drafting, or cover-copy finalization.

## 2. Input authority

Use only the supplied Architecture Input package as the authoritative selection basis.

Do not add:

- `HOLD_OUT` items;
- `EXCLUDE` items;
- candidates that are not present in `selected_by_role`;
- facts, metrics, dates, benchmark details, licenses, hardware requirements, or social reactions that are not represented in the input package.

If the selected pool is weak in a topic area, omit that topic area. Do not create section quotas.

## 3. Coverage rule

Every selected item whose role is **not** `SUPPORTING_EVIDENCE` must appear as `primary_evidence_task_ids` in **exactly one** substantive editorial package.

`SUPPORTING_EVIDENCE` items:

- may appear only in `supporting_evidence_task_ids`;
- need not receive their own package;
- must not be promoted to a primary story without a new Candidate Selection revision.

Several primary items may be grouped into one comparison, deep-dive, or thematic package when that improves the issue. Do not create three separate release-note articles merely because three models were selected.

## 4. Evidence boundaries

Every `remaining_boundaries` string attached to an item that is used in a package must be carried into that package's `boundaries` array.

These boundaries are publication constraints, not optional editorial notes. Preserve distinctions such as:

- vendor/project/author claim vs independently established fact;
- simulation vs deployment evidence;
- release artifact vs community trend date;
- benchmark setup differences;
- threat-model or environment assumptions;
- unresolved chronology;
- lack of independent reproduction.

Do not remove a caveat merely to save pages.

## 5. Temporal rules

Items selected as `LATE_BREAKING` must remain clearly post-cutoff:

- they must be primary items only in a package with `late_breaking=true`;
- that package must have `package_type=LATE_BREAKING`;
- do not merge their post-cutoff event chronology into a main-window lead/feature as if the event happened before cutoff.

Other selected items whose `timing_relation` is `POST_CUTOFF` must also remain in a late-breaking package.

`TIMING_UNRESOLVED` means unresolved. Do not infer a clock time or assign the item to Main vs Post-Cutoff by guesswork.

## 6. Editorial packaging

Available package types are defined by `schemas/issue-architecture-plan.schema.json`.

Use packages to create a coherent weekend-magazine reading flow. Appropriate patterns include:

- one lead story built around the strongest inspectable evidence;
- one comparison package combining related frontier models or tools;
- one thematic deep dive combining independent evidence around a common technical question;
- compact Paper Watch treatment for papers not already deeply embedded elsewhere;
- a distinct Late Breaking package for post-cutoff events;
- Watchlist / Chronology for small but valid selected items.

Do not force every role to correspond one-to-one with a package type.

`CHRONOLOGY` and `WATCHLIST` are usually compact treatments rather than full features.

## 7. Page budget

Use `editorial_constraints.page_target` as an approximate target and `page_max` as a hard maximum.

The sum of every package `page_target` must equal `page_budget.planned`.

Do not inflate the issue to hit the target. A shorter issue is acceptable when the evidence pool does not support more pages.

Do not exceed the maximum.

Frontmatter and References may be included as packages when useful for page accounting, but they must not be used to hide substantive over-allocation.

## 8. Cover and issue summary

The cover headline is deliberately deferred until article headlines/drafts are stable.

Therefore the Architecture Plan must contain:

- `cover.headline_deferred=true`
- `cover.headline=null`
- only provisional `anchor_candidates` drawn from selected items/packages.

`this_week_summary_written_last` must be `true`.

Do not write the final “This Week in AI” summary at architecture time.

## 9. Drafting order

Assign a unique `drafting_order` to every package.

Choose the order based on dependency:

- foundational/lead terminology before dependent comparison packages;
- technical deep dives before cross-topic social synthesis when the social page depends on those definitions;
- Late Breaking after the main-window packages;
- the issue-level summary last.

Do not use `drafting_order` as a ranking of candidate importance.

## 10. Approval boundary

Output a `PROPOSED` Architecture Plan by default.

Do not set `status=APPROVED` or invent approval metadata. Approval is a separate human editorial gate.

Article drafting must not begin until a validator has accepted an `APPROVED` Architecture Plan.

## 11. Output

Return exactly one JSON object conforming to `schemas/issue-architecture-plan.schema.json`.

The `basis` values must bind the exact supplied Architecture Input:

- `architecture_input_sha256` = SHA-256 of the exact input bytes;
- `selection_sha256` = the selection SHA recorded in the input basis;
- `matrix_sha256` = the matrix SHA recorded in the input basis.

Do not return prose outside the JSON object.
