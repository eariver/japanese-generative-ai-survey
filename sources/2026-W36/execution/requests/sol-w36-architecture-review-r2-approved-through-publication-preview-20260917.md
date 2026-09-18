# W36 execution instruction — Architecture Review r2 APPROVED through Publication Preview

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_REVIEW_R2_APPROVED / CONTINUE_TO_PUBLICATION_PREVIEW`

Date: `2026-09-17 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W36-v2-work`

## 1. Human decision authority

The Human has explicitly reviewed the W36 Architecture Review r2 and decided:

`APPROVED`

Exact reviewed production authority:

`3e1e0fc3b802bf388e56486c638acba35b7bc2ae`

Reviewed production tree:

`f0aa9bbd5ad1b4ff3cf987688087f4d5ac1aa1eb`

Architecture Review r2 presentation-shell parent authority:

`21f97abc5e495a63ff398961747e1c1bda010bcf`

The r2 decision is approval of the existing Architecture bytes. Do not reinterpret this approval as permission to modify Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture before drafting.

The prior r1 decision remains historically valid as `REQUEST_CHANGES`, revision 1, boundary `SELECTION_COMPLETE`. This instruction records the new r2 decision as the next Architecture Review revision and does not overwrite r1 provenance.

The Human approval follows independent review of r2. Blocking findings are zero. RC-1 acquisition-status wording and RC-2 worker-review provenance are accepted as repaired.

## 2. Mission

Record the Human Architecture Review r2 decision through the canonical Human Gate protocol, verify the resulting immutable approval authority, then continue W36 production autonomously through drafting, canonical validation, publication rendering/candidate construction, and all required pre-publication reader-surface checks until the next Human Gate:

`PUBLICATION_PREVIEW`

Normal terminal state for this run is a fresh Publication Preview Human Gate pending, with a durable reviewable PDF/candidate and no Publication Preview Human decision recorded.

Do **not** Freeze or Release in this run.

## 3. Starting guard

The Muse invocation will supply the Exact Starting SHA equal to the commit containing this execution request.

Before any repository/GitHub write, read-only verify all of the following:

- remote `weekly/2026-W36-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- Exact Starting SHA parent == `21f97abc5e495a63ff398961747e1c1bda010bcf`;
- remote `main` HEAD == `5acbff8528890ed9fc324c0227e6c4e43067c438`;
- remote `main` tree == `451fd7c6c6a9fcda59daa81fe484c62291e7d018`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote `production/survey-core-v2` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- current W36 Production State reports `ARCHITECTURE_ESTABLISHED`, `next_action = ARCHITECTURE_REVIEW`, `terminal_reason = HUMAN_GATE_REACHED`, and Architecture Review pending;
- `sources/2026-W36/execution/reviews/architecture-r2.md` identifies reviewed production authority `3e1e0fc3b802bf388e56486c638acba35b7bc2ae`, tree `f0aa9bbd5ad1b4ff3cf987688087f4d5ac1aa1eb`, and r2 decision still `PENDING` before this approval is recorded;
- `sources/2026-W36/architecture-v2.json` is the reviewed r2 Architecture with the corrected NVIDIA/Hugging Face transaction-status thesis;
- candidate Selection remains `18 SELECTED / 1 HOLD`, Evidence remains `13 VERIFIED / 6 PARTIAL`, and accepted upstream authorities are unchanged from r2 review.

If any guard differs, perform no repository/GitHub write, report expected versus actual, and STOP.

No force push, reset, rewrite, fallback branch, alternate W36 branch, or unsolicited Core repair branch is authorized.

## 4. Mandatory read order

After the guard passes, read at minimum:

1. `sources/2026-W36/execution/reviews/architecture-r2.md`
2. `sources/2026-W36/execution/reviews/architecture-r2-dossier.md`
3. `sources/2026-W36/gates/reviews/architecture-r1.json`
4. `sources/2026-W36/execution/decisions/w36-worker-pregate-review-provenance-20260917-r2.md`
5. this execution request
6. `sources/2026-W36/production-state.json`
7. `sources/2026-W36/architecture-v2.json`
8. `sources/2026-W36/architecture-review-summary-v2.json`
9. `sources/2026-W36/candidate-selection-v2.json`
10. current canonical Human Gate implementation/contracts, especially `scripts/survey_human_gate_v2.py`
11. current canonical drafting / validation / publication / reader-surface pipeline contracts and commands from the reviewed Core implementation.

Repository-local current Core behavior is authoritative. Do not use Google Drive.

## 5. Record Architecture Review r2 APPROVED

Use the canonical Human Gate protocol to record the explicit Human decision against the exact reviewed r2 bytes.

Required semantics:

- gate: `ARCHITECTURE_REVIEW`
- next Architecture review revision: `2`
- decision: `APPROVED`
- reviewed repository production commit SHA: `3e1e0fc3b802bf388e56486c638acba35b7bc2ae`
- reviewed_by: `Human Owner`
- review reference: this execution request plus the r2 Human-facing review surface
- requested changes: none
- regeneration boundary: none

Use the canonical tool's actual execution timestamp for the decision record. Do not invent an earlier exact Human action timestamp.

After recording approval, verify all generated review-index / review-record / immutable approval-snapshot authorities and confirm the lifecycle consequence is the one defined by the current Core contract.

If the canonical Human Gate implementation refuses approval because reviewed bytes, revision identity, state, or provenance do not match, STOP rather than bypassing the guard.

## 6. Approved Architecture authority

The approved Architecture contains six packages, in this order:

1. `w36-astra-critical-cyber`
2. `w36-fermat-proof`
3. `w36-open-efficient`
4. `w36-frontier-coding`
5. `w36-agent-harness`
6. `w36-ecosystem-spatial-media`

The approved editorial thesis uses transaction-status-safe wording for NVIDIA/Hugging Face:

`NVIDIA agreed to acquire Hugging Face while pledging to preserve its open, compute-agnostic character`

Preserve the fact that the deal is agreed/announced and not closed, and that openness statements are commitments/pledges rather than observed post-acquisition facts.

Do not regress to r1 wording such as `moved to own` or any equivalent completed-ownership implication.

## 7. Drafting authority and evidence boundaries

After Architecture r2 approval is validly recorded, draft the W36 edition from the approved Architecture and accepted Evidence only.

Preserve all load-bearing evidence boundaries established in r2.

### Astra

- Critical-cyber designation and monitoring are first-party claims.
- Decreased monitorability is a required caveat, not optional color.
- vendor benchmarks/safety figures remain publisher-reported and unreproduced;
- full system-card/deployment-safety subpages not consumed must not be silently represented as consumed;
- no claim about production incident rates is established.

### Fermat

- describe as formalization / machine-checked verification, not a new mathematical proof idea;
- Lean repo/build/comparator/nanoda were not independently rerun;
- scale/autonomy claims remain source-bounded.

### NVIDIA / Hugging Face

- transaction is agreed/announced, not closed;
- `$12.93B` is the announced agreement figure from NVIDIA;
- openness, compute-agnostic, multi-cloud and multi-accelerator statements are pledges/commitments;
- do not imply completed ownership, completed regulatory clearance, or observed post-acquisition behavior.

### K2 / GLM-5.3

- license statements remain model-specific;
- K2 Apache 2.0 must not be generalized over datasets;
- GLM license nuance must not borrow MIT terms from the Flash variant to full weights;
- GLM ordinary-window placement retains the unresolved UTC-hour / medium-confidence boundary;
- vendor benchmark/ranking claims remain unreproduced.

### Fable/Mythos / Gemini / Muse Spark

- proprietary coding benchmarks/efficiency figures stay vendor-reported;
- methodology silence remains visible where recorded;
- Muse scorecard image values excluded from Evidence must not reappear in prose;
- Gemini card remains HOLD/context companion and must not be promoted as a separate selected event.

### Agent harness

- GA versus preview labels must remain accurate;
- Copilot/Kilo behavior is vendor-described and not independently tested here;
- live model/catalog counts are point-in-time claims where applicable.

### Spatial / image / video

- Atlas claims are vendor-reported and early-access bounded;
- Google Pics rollout sequencing remains product-announcement scope;
- H3 Max leaderboard/Pareto claims remain date-bound, source-bounded, and PARTIAL where Evidence records them so.

### X / Grok

- X/Grok is community/social observation and momentum context only;
- X must not become technical authority for benchmark, capability, security, pricing, license, architecture, autonomy, deal terms, or availability facts;
- late-breaking X rows remain outside ordinary-window totals.

### General

- PARTIAL Evidence must not be silently promoted to VERIFIED prose;
- HOLD items remain outside the selected Architecture except where the canonical downstream process explicitly permits non-promotional context;
- no model-specific license, benchmark, date, parameter, autonomy, or safety property may be generalized cluster-wide without authority.

Do not perform fresh research merely to improve prose. If drafting exposes a genuine factual contradiction or missing authority that makes the approved Architecture unusable, STOP with the exact blocking condition rather than silently changing upstream authority.

## 8. Research-stage freeze

This run must not rerun or semantically alter:

- Grok/X intake;
- Discovery;
- Screening;
- Evidence or Evidence views;
- Materiality;
- Completeness;
- Selection;
- Architecture.

Expected frozen counts:

- Discovery: `19`
- Screening: `19 KEEP / 0 DROP`
- Evidence: `13 VERIFIED / 6 PARTIAL`
- Materiality: `18 MATERIAL / 1 CONTEXT`
- Selection: `18 SELECTED / 1 HOLD`

The sole HOLD remains the Gemini model-card companion record.

If downstream validation exposes a genuine upstream defect, use the smallest valid canonical regeneration/exception mechanism and STOP if new Human authority would be required. Do not silently rewrite approved upstream authority.

## 9. Volume / compression policy

Do not invent a separate compression Human Gate.

Do not force a target page count by deleting selected material or load-bearing limitations.

Prioritize:

- coherent synthesis;
- evidence-bound prose;
- readable hierarchy;
- faithful six-package Architecture;
- preservation of caveats.

Ordinary weekly length or moderate overlength is not by itself a reason to stop. Treat volume as blocking only when it creates a real canonical quality failure such as severe layout breakage, gross duplication, unreadable density, or a reader-surface validation failure.

## 10. Validation and reader-surface requirements

Run the current canonical downstream pipeline from the approved Architecture through every stage required before Publication Preview.

At minimum ensure all current Core-required checks execute successfully, including any applicable:

- draft/schema validation;
- evidence/citation/provenance binding checks;
- Architecture-to-draft coverage checks;
- publication candidate validation;
- TeX/PDF generation and durable PDF authority recording;
- lexical reader-surface validation;
- persisted semantic reader-surface review gate;
- other publication-profile validations required before `PUBLICATION_PREVIEW`.

The pre-publication reader-surface semantic review must be genuinely produced/consumed according to the current Core contract. Production code must not manufacture a semantic PASS.

The Worker may perform Worker/Operator pre-gate checks, but must not label them as independent Sol/Human review. RC-2 provenance discipline remains binding downstream.

If a generic reusable Core defect is discovered, do not patch shared Core in this branch. Record the exact defect and STOP under the existing Core-repair / pinned-Production-Line policy. If the issue is edition-local content/data, repair only within the W36 branch and within the smallest valid downstream regeneration boundary.

Known Freeze-stage defects such as Issue #497 are out of scope because this run stops before Freeze. Do not repair them here.

Do not merge W36 to `main`.

## 11. Publication Preview deliverables

Before stopping, make the next Human review practical and auditable. Produce the canonical Publication Preview surface required by Core, including at least:

- durable publication candidate authority;
- durable PDF authority with exact path, SHA-256, byte count, and page count if available from canonical tooling;
- current Production State showing the Publication Preview Human Gate pending;
- machine validation summaries required by the profile;
- persisted lexical and semantic reader-surface results;
- a Human-facing Publication Preview review dossier/checkpoint summarizing:
  - exact reviewed production commit/tree;
  - Architecture r2 approval provenance;
  - final section/package structure;
  - page count and high-level layout;
  - evidence-boundary carry-through;
  - treatment of PARTIAL and HOLD material;
  - reader-surface lexical/semantic results;
  - known non-blocking residual limitations;
  - any material deviation from the approved Architecture;
  - exact PDF authority.

Do not record a Publication Preview Human decision.

## 12. Shared-Core freeze

No W36 run changes are authorized under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Do not modify `main`.

Do not modify `production/survey-core-v2`.

Do not repair Issue #497 or the known release-workflow `validate-state` CLI defect.

If current canonical downstream behavior requires a generic Core change to proceed, stop and report the defect instead of applying an edition-local workaround that changes shared semantics.

## 13. Commit / push discipline

Use the existing W36 branch only.

For every repository write sequence:

- preserve normal parentage;
- use normal commits;
- push non-force only;
- read back remote HEAD after push;
- do not rewrite or squash away review/gate provenance;
- retain r1 `REQUEST_CHANGES` and r2 `APPROVED` as immutable Human Gate history.

If remote HEAD changes unexpectedly before a write, STOP and report expected versus actual.

No new branch, fallback branch, review branch, repair branch, reset, rebase, squash, force push, or history rewrite is authorized.

## 14. Normal STOP condition

Normal successful terminal condition:

- Architecture Review r2 = canonically `APPROVED`;
- Draft and required downstream publication artifacts generated;
- all required pre-Publication-Preview machine and reader-surface gates passed;
- lifecycle at the current Core-defined Publication Preview stop, normally `RELEASE_CANDIDATE`;
- `PUBLICATION_PREVIEW` Human Gate = `pending`;
- no Publication Preview Human decision generated;
- no Freeze;
- no Release;
- `main` untouched;
- Production Line untouched;
- fresh Human-facing Publication Preview dossier/checkpoint committed and remote-read-back verified.

Then STOP.

## 15. Final report

At the stop, report at minimum:

- Starting SHA/tree;
- Architecture r2 reviewed production SHA/tree;
- Architecture r2 canonical approval review record / immutable approval authority;
- ending remote HEAD/tree;
- Draft identity and validation status;
- publication candidate identity;
- PDF path, SHA-256, byte count, and page count;
- final section/package structure;
- reader-surface lexical result;
- reader-surface semantic result;
- evidence-boundary carry-through summary;
- any downstream edition-local repairs and their regeneration boundary;
- any material deviation from approved Architecture;
- current lifecycle / next action / terminal reason;
- Publication Preview review surface path;
- Publication Preview Human decision status;
- shared-Core changed paths count;
- confirmation that `main` and Production Line are unchanged;
- exact stop reason.

Success requires:

`PUBLICATION_PREVIEW = PENDING`

not APPROVED.
