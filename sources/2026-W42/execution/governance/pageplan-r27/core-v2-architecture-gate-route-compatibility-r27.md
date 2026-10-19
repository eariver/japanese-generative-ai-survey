# W42 r27 — Core v2 Architecture/Gate route compatibility (NONCANONICAL preflight)

Status: `SOL_W42_R27_PREFLIGHT_EVIDENCE / READ_ONLY_CORE / NO_GATE_ACTION`. Frozen Core v2 (`774dd39a…`) and reviewed main (`c8d0ecc1…`) only read. No stage transition, no candidate, no Gate record written. Dry-runs executed via read-only import of frozen modules in an isolated worktree (`/tmp/w42_dryrun.py`, kept outside the repo); zero repo writes by the checks themselves.

## 1. Exact function authorities (verified in source, not quoted from memory)

- `scripts/survey_human_gate_v2.py:357-361` `_validate_gate_pending(state, gate)`:
  requires `state.lifecycle_state == GATE_STATES[gate]` **AND** `state.human_gates[key] == "pending"`,
  where `GATE_STATES = {"ARCHITECTURE_REVIEW": "ARCHITECTURE_ESTABLISHED", "PUBLICATION_PREVIEW": "RELEASE_CANDIDATE"}` (lines 40-43).
- `request_architecture_revision` (1352) → `request_changes(..., gate="ARCHITECTURE_REVIEW", ...)` (1365) → `_validate_gate_pending(state, "ARCHITECTURE_REVIEW")` (1296).
- `record_architecture_approval` (605) → `_validate_gate_pending(state, "ARCHITECTURE_REVIEW")` (617).
- `request_publication_preview_revision` (1380) → `request_changes(..., gate="PUBLICATION_PREVIEW", ...)` → `_validate_gate_pending(state, "PUBLICATION_PREVIEW")`.
- `_validate_review_index_semantics` (121): any row after an ACTIVE APPROVED decision for the same gate raises
  `"Human Gate review index has review after active APPROVED decision"` (133-134); contiguous revisions enforced (135-138);
  Publication Preview `REQUEST_CHANGES` with `_reopens_architecture(boundary)` (boundary strictly before
  `ARCHITECTURE_ESTABLISHED`, line 118) clears `approved_active["ARCHITECTURE_REVIEW"]` (168-175) — the ONLY lawful path to a second Architecture approval.
- `_current_pending_gate` (364): pending Gate derives from `orchestration.gate_at_state` lifecycle mapping
  (`config/survey-production-v2.json:214-217`: only `ARCHITECTURE_ESTABLISHED→ARCHITECTURE_REVIEW` and
  `RELEASE_CANDIDATE→PUBLICATION_PREVIEW`); current lifecycle `DRAFT_COMPLETE` maps to NO pending Gate.

## 2. Dry-run evidence (frozen functions, current committed bytes)

Current state: `lifecycle_state=DRAFT_COMPLETE`, `architecture_review=approved`, `publication_preview=pending`.

| # | check | result |
|---|---|---|
| D1 | `validate_agent_state(repo_root, cfg, state)` (`survey_agent_control_v2.py:321`) | **no errors** — State resumable, checkpoints/provenance/history consistent |
| D2 | `_validate_gate_pending(state, "ARCHITECTURE_REVIEW")` | **raises** `HumanGateError: ARCHITECTURE_REVIEW decision requires pending ARCHITECTURE_ESTABLISHED Human Gate` — direct `request-architecture-revision` from DRAFT_COMPLETE is Core-impossible |
| D3 | `_validate_gate_pending(state, "PUBLICATION_PREVIEW")` | **raises** `HumanGateError: PUBLICATION_PREVIEW decision requires pending RELEASE_CANDIDATE Human Gate` — cross-Gate reopen cannot be initiated from DRAFT_COMPLETE; a pending-publication flag in state is NOT proof the Gate is actionable |
| D4 | `_validate_review_index_semantics` on committed `review-index.json` | **passes** — r1 ACTIVE APPROVED, no review-after-approved |
| D5 | same validator on simulated index with appended `ARCHITECTURE_REVIEW r2 APPROVED` | **raises** `review after active APPROVED` — fabricating r2 approval is Core-rejected |
| D6 | `_reopens_architecture(boundary)` | `True` only for boundaries strictly before `ARCHITECTURE_ESTABLISHED` (e.g. `ISSUE_INITIALIZED`); `None`/`DRAFT_COMPLETE`/`ARCHITECTURE_ESTABLISHED`/later → `False` |
| D7 | r1 `page_plan` shape vs `survey_architecture_v2_base.py:524-544` rules | **passes**: `{target_pages, max_pages, notes}` exact keys, both positive numbers, `30 >= 28`, notes non-empty |

## 3. Page-target semantics (Route A legality core)

- `survey_reader_fidelity_v2.py` module docstring: **"A soft Architecture page target is never a quota."**
  `validate_review_depth` returns immediately unless `publication_profile == "LONGFORM_SPECIAL"` (line ~418).
  W42 profile is `WEEKLY / WEEKLY_MAGAZINE` → the below-target density-evidence rule does not apply at all.
  Even where it applies, below-target requires extra review evidence, not failure.
- Architecture validator (`survey_architecture_v2_base.py:524-544`): positivity + `max >= target` sanity only.
  r1 notes themselves: `"target ~27-30 pages, not a hard cap."` → target 28 is advisory; max 30 is the cap.
- Publication validators (`survey_publication_v2.py`, `survey_reader_publication_v2.py`): `page_count` **byte-consistency**
  (asserted == exact PDF bytes; candidate == approval == freeze bindings) and architecture **coverage**
  (packages × `must_cover_requirements` 1:1, profile identity, canonical source authority). No comparison of
  candidate pages against `target_pages=28` exists anywhere in Core.
- Repo-wide grep for `target_pages` consumers: only `survey_reader_fidelity_v2.py:481`,
  `survey_architecture_v2_base.py:524-544`, and the interactive selection CLI shape check. No hidden quota.

**Therefore Route A is Core-validator-clean**: nothing in frozen Core fails a content-complete 21pp formal Reader/Publication
Candidate for falling short of the advisory 28. What Core DOES require is the normal stage flow
(`DRAFT_COMPLETE → validation artifacts → VALIDATED_DRAFT → candidate → RELEASE_CANDIDATE → Publication Preview pending`)
with byte-exact bindings — canonical Publication engineering that is explicitly OUT of scope for r27 (no candidate built here).

## 4. Route B mechanics (for the record; NOT invoked)

A lawful r2 would require: (i) first completing validation + candidate stages under r1 to reach `RELEASE_CANDIDATE` with
Publication Preview pending; (ii) Human `REQUEST_CHANGES` on Publication Preview with a pre-`ARCHITECTURE_ESTABLISHED`
regeneration boundary; (iii) Core then deletes superseded checkpoint provenances (`_superseded_checkpoint_paths`),
canonical regeneration artifacts (`_superseded_canonical_artifacts` per `canonical_regeneration_artifacts` config),
and Gate authority paths including the active r1 approval provenance (`_superseded_gate_authority_paths`, only when the
cross-gate reopen fired); (iv) state regresses to the boundary with review-index active flag cleared; (v) a fresh
Architecture Review r2 + new Human APPROVED. Invalidation surface: every checkpoint/artifact at/after the boundary,
the r1 approval snapshot authority, and dependent Draft/Reader derivations. No shortcut exists: D2+D3+D5 prove it
cannot start from `DRAFT_COMPLETE`.

## 5. No invalid writes

This unit wrote ONLY `execution/governance/pageplan-r27/*` (this file, budget/coverage, decision packet, PROPOSED r2 + diff),
one session file, and an append-only index entry. No Core file, no canonical JSON, no Gate record, no State field,
no candidate, no approval, no `request-*`/`record-*` invocation. The `*.PROPOSED.json` is edition-local proposal text,
not canonical authority and not a Gate event.
