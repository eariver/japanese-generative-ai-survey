# W40 Muse r9 — Correct Materiality/Completeness semantics, advance Core stage conditionally, prepare Selection proposal

Status: `SOL_BOUND_EXECUTION_AUTHORITY / SOL_MC_CONDITIONAL_PASS / FIX_MC01_MC02 / BOUNDED_AT_SOL_SELECTION_SEMANTIC_REVIEW`  
Authority: `sources/2026-W40/execution/reviews/sol-w40-materiality-completeness-r1-20261010.md`  
Repository: `eariver/japanese-generative-ai-survey`  
**Existing branch ONLY:** `weekly/2026-W40-v2-work`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Reviewed Muse r8 HEAD/Tree: `6fc888be1920c8509ee8397479dc98b186121f9d` / `5d52f0edad1baf29423c26caf247eaf310ccb5a1`  
Exact r9 Starting HEAD/Tree: supplied by Sol in its *outer Muse invocation after this contract commit*.

## 0. Hard zero-write admission

Before ANY write, read-only verify remote W40 branch HEAD equals exact outer Starting SHA; its commit Tree equals exact outer Starting Tree; remote `main` HEAD equals `afdb3df3faa20af3bb5798be429bba8dbd2100b1`; starting commit is direct descendant of reviewed r8 `6fc888be1920c8509ee8397479dc98b186121f9d`; State `CANDIDATES_NORMALIZED`, next `stage:evidence-materiality-completeness`, Evidence/Materiality/Completeness checkpoints pending and Human Gates pending. On mismatch: STOP with expected/actual values, ZERO WRITES.

Do not create new/fallback/review/repair branches, local reset, rebase, force push, rewrite, or modify reviewed main, Core scripts/schemas/config/workflows, W39, other editions, existing human records. All writes edition-local W40 in the existing branch, normal commits, non-force push and exact remote read-back.

## 1. Read authorities in mandatory order

1. Reviewed `main` `docs/survey-production-core-v2-sol-luna-review-governance.md`, `docs/survey-production-core-v2-session-bootstrap.md`, frozen Evidence/View/Materiality/Completeness and Stage Checkpoint functions in `scripts/survey_evidence_v2.py`, `scripts/survey_agent_control_v2.py`, accepted `config/survey-production-v2.json`.
2. Sol independent Materiality review `sources/2026-W40/execution/reviews/sol-w40-materiality-completeness-r1-20261010.md` (this instruction's editorial acceptance conditions, exact M01/M02).
3. W40 `production-profile.json`, `production-state.json`, canonical Discovery 37, accepted Screening 37.
4. Exact accepted Evidence r8 `evidence/v2/accepted/0a62346f0729e768d1b67305dd96e0e99224326c862831abe79e43ced4875e07/evidence-accepted.json`; accepted Views r8 `evidence/v2/views/accepted/60b622f659224cf1862ecdb4aa06563ee4f31ed69d2bb74f9e88c32f76e2925e/edition-views-accepted.json`.
5. r8 draft Ledger `evidence/v2/results/r8/materiality-ledger-DRAFT.json` and Completeness `evidence/v2/results/r8/completeness-assessment-DRAFT.json`, r8 `SOL_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r8.md`, and earlier Sol Evidence r1–r4 review documents and exact source exceptions.
6. Selection schemas, frozen Core Selection operations, and any current Core Stage contract; W39 accepted precedents are **format-only**.

## 2. SC-M01 — X provenance ledger is CONTEXT, never a technical event

For exactly `w40-grok-x-ledger-20261009` (task `evidence:2026-W40:29dac8f036319411`), clone the current accepted 35 View bytes into a **new staging directory** and edit only that View:

- `materiality.status="CONTEXT"`, with a reason explicitly `Grok/X and Daily X Source Intake observation ledger used for provenance/negative-space checks, NOT a separately new model/product/paper/publication event, NOT article candidacy`.
- `profile_annotations.window_relation="OTHER"`, `why_this_issue` exact source-process contextual role; `carry_over=false`.
- `scope_dimensions` may retain current profile-valid dimensions if an annotation clarifies these measure research coverage, not technical merit; alternatively narrow to `current relevance` only. Keep accepted Evidence Card bytes, Evidence status `PARTIAL`, Evidence result SHA, X 4 URL and Daily X 64 distinct cohorts unchanged.
- **All other 34 View files byte-identical to r8.** No new or changed Evidence Card; no change in other materiality/HOLD statuses.

Run frozen `validate_edition_view` for all 35, `accept_edition_views` and `validate_edition_views_acceptance`, creating a **new** immutable accepted View set and exact new SHA. r8 Evidence Acceptance and r8 View Acceptance remain immutable historical identities.

Expected new View distribution = **29 MATERIAL / 4 HOLD / 2 CONTEXT** (the second CONTEXT is PRE_WINDOW LIFT).

## 3. SC-M02 — real Materiality Ledger and truthful Completeness scope

Using the **new** accepted View SHA, rebuild the 37-row canonical Materiality Ledger:

- Every row's `rationale` must explain specific W40 technical fact/date/newness, source actually consumed, author/vendor claims vs independent reproduction, grouping and counterfactual impact; *never just* `Screening=KEEP; Edition View=MATERIAL`.
- 29 MATERIAL rows have individual defensible importance rationales and editorial relation/grouping without forcing every row into a standalone article.
- 4 HOLD: W39 Pixel Canary/TBC unproven primary identity/performance; Oct2 AstaBrief and AutoSynthData exact publication-time unresolved. Those remain HOLD even if content interesting. LIFT PRE_WINDOW CONTEXT; Grok/X observation CONTEXT; 2 negative-space method logs EXCLUDED. DGX Spark 64GB ordinary event 13:00:39Z if publisher metadata genuinely present, Oct23 sales future; ELYZA MATERIAL despite screening MAYBE (new primary benchmark consumption).
- Preserve exact accepted Screening decisions including historical `MAYBE` and `INSPECT`, and `duplicate_group=null` for non-DROP as required by Core. Group at *Selection proposal* layer, not by forging Screening duplicate group.
- Use the official frozen `validate_materiality_ledger`, immutable `write_materiality_ledger` on **new canonical stage path**; if a pre-existing canonical artifact exists, never overwrite it; record exact path/SHA and stop if genuinely conflicting.
- Regenerate Completeness using frozen builder on revised Ledger/Views, with actual source consumption records and meaningful subset bindings in 3 obligations:
  - `weekly:current-relevance`: actual W40 developments, temporal qualification, and documented borderline leads as needed (exclude X and sweeps as technical events).
  - `weekly:technical-significance`: substantive technical candidates with project-specific rationale; exclude methodology-only records, avoid numeric-count-only argument.
  - `weekly:carry-over`: **exactly the two W39 carryovers** `w40-carryover-pixelcanary-20261009`, `w40-carryover-tbc-video-20261009` and their exact task IDs, not all 37.
- Result `overall_status=LIMITED` is defensible with 11 source/benchmark/rights/timestamp limitations, if no material obligation needs active research. Do not mechanically keep `SATISFIED` for an unreviewed issue. If any meaningful gap means `NEEDS_RESEARCH`/INCOMPLETE, **stop** for Sol; never force a readiness flag to advance.
- Re-run frozen `validate_materiality_ledger` and `validate_completeness`, schema tests, SHA and negative mutation tests. Clearly report why each limitation does or does not prevent weekly selection, and where it must appear in manuscript.

## 4. Conditional official Core Stage transition — only after all Sol corrections proven

Sol's r1 review has approved the **29-event materiality candidate basis and limited completeness** conditional on exactly the above M01/M02 semantic repairs; **it has not preapproved any new MATERIAL promotion or new candidate omission**.

If and ONLY if:
- existing r8 Evidence Acceptance SHA unchanged, 35 Cards untouched and accepted correctly;
- new Edition View acceptance valid with exactly one modified view and expected statuses;
- Materiality 37 rows with defensible source-specific rationales, and Completeness three semantically scoped obligations (carry-over 2), `LIMITED` (or stop on insufficient evidence);
- all frozen Core Stage Contract and exact accepted source/implementation SHA checks pass;

then use normal `survey_agent_control_v2.build_stage_checkpoint`, core deterministic stage-report validation and `advance_with_checkpoint` to perform **`CANDIDATES_NORMALIZED → EVIDENCE_REVIEWED`** and mark Evidence, Materiality and Completeness checkpoints passed together. No fabricated Sol PASS or manually written `production-state.json`; cite actual Sol r1 review `sources/2026-W40/execution/reviews/sol-w40-materiality-completeness-r1-20261010.md` as editorial decision source. Stage transition is a **single indivisible Core action**, not three handwritten flags.

If tool/bridge cannot perform legal transition from current reviewed main/implementation hashes, STOP `CORE_STAGE_BLOCKED` and report actual failed command/schemas/paths, not overwrite SHA identity or bypass Core.

## 5. Prepare *Selection proposal only*, stop at Sol

On success of formal state transition and new active Evidence/View pair, stage a Core-schema-conforming **PROPOSED_NOT_ACCEPTED Selection** with exact authoritative inputs/SHAs and reviewer dossier. Do not finalize Selection or advance `SELECTION_COMPLETE`.

Must include:
- technical/event-only set of 29 MATERIAL inputs with 4 HOLD / 2 CONTEXT and 2 EXCLUDED; drop X ledger from publishable narrative (only provenance methodology references allowed);
- group coherent packages without generic catch-all: frontier Sonnet/GPT6.1/Argon, Holo4+ELYZA Japanese open reasoning, locally served decision models Ollama/Clef/Strands, OpenAI DevDay/dots/API by product, safety/provenance, training/eval, image/video/audio and infrastructure;
- strong candidate inclusion priority for ELYZA, Holo4, Olmo-core, ContextLM, TTS, RL Environments, ProvenanceGuard (earlier missed), and reasonable editorial treatment of DGX Spark;
- explicit exclusions/holds and whether full primary-authority consumption would change editorial choice; preserve vendor-sourced benchmark qualifiers and licenses and pre-window dates;
- a **depth/budget proposal** specifying for each thematic package core mechanisms, evaluated metrics/conditions, comparisons/limitations, sources and estimated relative space; avoid a superficial 29-headline skim. Don't force precise page counts before Architecture, but propose substantive coverage.

Document reviewer assumptions, grouping/overlap map, selections and counterfactual missed-story audit. Distinguish provisional Materiality from canonical acceptance and never claim final Sol Selection PASS.

**STOP at** `SOL_SELECTION_SEMANTIC_REVIEW_READY` or `SOL_SELECTION_SEMANTIC_REVIEW_BLOCKED`; no Selection Acceptance/Checkpoint, Architecture, Draft, Human Gate, Publication.

## 6. Terminal deliverables, provenance and source protection

Deliver `sources/2026-W40/execution/SOL_SELECTION_SEMANTIC_REVIEW_HANDOFF-r9.md` with:
1. exact Starting and Final HEAD/Tree, remote main SHA, ancestry/changed-file allowlist, non-force push/read-back;
2. r8→r9 one-View diff and new accepted View SHA, old accepted Evidence+View preserved, SHA-based reference crosswalk of 35;
3. 37 Materiality Ledger row-specific rationales, 29/4/2+2 breakdown; X source record explicitly CONTEXT; 3 scoped Completeness obligations with carry-over exactly 2, residuals and validation outputs;
4. official Stage Checkpoint and State SHA, Core deterministic report and actual exit codes; `EVIDENCE_REVIEWED` only if genuinely reached;
5. Selection proposal groupings, negative decisions, primary evidence gaps, short-issue compression guard and suggested technical depth with source/repro caveats;
6. terminal `SOL_SELECTION_SEMANTIC_REVIEW_READY` or `_BLOCKED`, all Human Gates pending, CV2-DM-016 OPEN_CORE.

No new branches, shared Core changes or missing-source fiction. If stage fails, persist truthful edition-local results via normal commit and return blocker rather than forging machine state.
