# W40 Muse r6 — exact Evidence supplement provenance + 35 full factual Card candidates

Status: `SOL_BOUNDED_EXECUTION_AUTHORITY / PROJECTION_SEMANTICS_APPROVED / CARD_AUTHORITY_REPAIR_ONLY / STOP_BEFORE_EVIDENCE_ACCEPTANCE`
Review: `sources/2026-W40/execution/reviews/sol-w40-evidence-authority-consumption-r2-20261010.md`
Repository: `eariver/japanese-generative-ai-survey`
**Existing and only branch**: `weekly/2026-W40-v2-work`
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Reviewed Muse r5 HEAD/Tree: `8afb94c5ae93f016e4dd0228f66c142a842cafbe` / `b3e75757e7528cab3fb9b30f58a7f283b8dcb81a`
r6 exact Starting HEAD/Tree: supplied by Sol's outer invocation **after this contract commit**.

## 0. Fail-closed admission (read-only first)

Verify remote W40 branch HEAD equals outer Starting SHA, its commit Tree equals outer Starting Tree, remote main HEAD equals reviewed `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, r5 reviewed `8afb94c5ae93f016e4dd0228f66c142a842cafbe` is strict ancestor, state `CANDIDATES_NORMALIZED` / `stage:evidence-materiality-completeness`, evidence/materiality/completeness pending, both Human Gates pending. Any mismatch => STOP, zero writes and expected/actual report. No new/fallback/repair branch, no local reset or force/rebase/history rewrite, no Core/scripts/schemas/config/CI/main/other edition modifications. Edition-local files on existing W40 branch, normal commit and non-force push only.

## 1. Authorized narrow compatibility semantics (SC-E01)

Sol approved only the **mapping semantics** and proof lineage in `execution/compat/evidence-source-class-projection-r5/projection-ledger.json`:
- `PRIMARY_RESEARCH_ABSTRACT`→`PRIMARY_PAPER` for exactly contextlms + prewindow LIFT;
- `EVALUATOR_PUBLISHER`→`PRIMARY_OFFICIAL` for AA-AgentPerf-Local, strictly evaluator-own-report provenance (NOT evaluated model vendor and NOT external reproduction).
- 3 derived Task copies and 32 unchanged semantic classes, old/new task hashes and unknown-type fail-closed guard.

Use exact approved mapping in a new **derived** r6 task package, with full ledger. Do NOT change canonical Discovery, Screening, existing original tasks, r5 ledger or frozen Core. Since a source supplement changes task/package SHA, recompute a new deterministic r6 package/ledger, prove only expected source_type and explicitly authorized supplement bindings changed. Hash identity of 35 Evidence tasks and package must be reproducible in double-build. Unknown-source negative injection remains fail-closed.

## 2. Canonical Evidence Authority Supplement (SC-E07)

Use frozen `schemas/evidence-authority-supplement-v2.schema.json` and `survey_evidence_v2.build_evidence_authority_supplement` / `validate_evidence_authority_supplement`. Prepare a **new W40 edition-local immutable supplement manifest** with entries tied to the correct non-DROP Discovery/Evidence task IDs. Before creating, read actual schema/validators and the existing immutable 37 Discovery / accepted Screening.

Required newly task-bound authorities, from r5 pre-existing bounded original-source excerpts (raw path bytes/SHA recalculated), additional captured bytes when necessary:
1. **ELYZA 33B Dense** pinned `README.md` at `6ca556b2ddc4642580752b3a1ae2d7e7681106fc`, `source_type=PRIMARY_REPOSITORY`, `source_class=PRIMARY_REPOSITORY`, to task for `w40-weak-elyza-20261002`.
2. **ELYZA 32B-A3B MoE** pinned `README.md` at `5260ecc249f32ef5005ef940c78f41f130d9c468` with same provenance class/task.
3. **ProvenanceGuard** original `arxiv.org/abs/2606.18037v2` / version-qualified ar5iv text plus existing r5 paper excerpt, `PRIMARY_PAPER`. Verify revision and avoid an invented manuscript version if ar5iv revision differs. Blog remains separately bound as Sept 29 W40 event.
4. **Context Language Models** original v1 `arxiv.org/abs/2609.37725v1` and ar5iv full-paper excerpt read r5, `PRIMARY_PAPER`, with exact source versus PDF-not-read distinction.

Use mapping-valid supplement `source_type` values from frozen `SOURCE_CLASS_MAP` (do **not** invent `PRIMARY_MODEL_CARD` in a supplement, which the map rejects). Source original URLs, retrieval instants, day-only release date as metadata/nullable published_at, rights, actual raw file hash/byte length, concrete relation/claim role must be grounded. If exact original fetch timestamp isn't proven, use recorded actual access log (not arbitrary 06:00Z for each page). No false full-HTML-byte equivalence. Validate manifest raw/screening/task binding exactness, missing file/hash negative cases and uniqueness.

Package + tasks must carry `authority_supplement` and each task's `authority_supplement_source_ids` via reviewed frozen Core mechanics, then apply the approved r5 source-type projection **only in new derived Task copies**. Rerun all package basis, 35/35 task_authority_sources, negative unknown-type and reproducibility checks. If frozen Core cannot compose supplement with task projection, report precise `CORE_ACCEPTANCE_BLOCKED`; NEVER modify Core to circumvent.

## 3. Repair r5 draft Card authority references and chronology

- ELYZA 33B/MoE benchmark/training/Apache-2.0 claims must cite their exact **new primary model-card source IDs**, not `SECONDARY` legacy `src-1` alone. Legacy Discovery source `SECONDARY / UNVERIFIED` stays present for historical lineage but does not serve as sole support for a new primary VERIFIED claim. Both official primary model cards are required as separate source entries.
- ProvenanceGuard claim about paper equations, experimental values/units, sample labels and method must cite supplement `PRIMARY_PAPER` (plus blog if relevant). W40 news timing (team blog Sep29) should cite the original blog. Correct arXiv history: **first submission 2026-06-16 15:10:29 UTC, v2 2026-07-26 10:47:53 UTC**, not Aug27. Verify manuscript text version and ensure no claims accidentally borrow later update.
- Context Language Models paper equation/tables should cite original/fulltext primary supplement authority; retain `PDF bytes not consumed` and untouched code/appendix limits.
- Gemini Argon publisher-announced 1M **output** tokens retained; other validated r5 scientific corrections and ELYZA Japanese significance retained.
- Carefully audit the remaining 30 reviewer records for **promoted PRIMARY_FACT/AUTHOR_CLAIM supported only by an old secondary/rumor/social locator** or unconsumed paper, not just the five r5 examples. Resolve with appropriate supplement where material and realistically sourced, or reduce claim/status with explicit factual reason. Do not manufacture new materials to certify unsupported evidence. Prior fixed 37 Discovery / 37 Screening and r4/r5 review-input history immutable.
- `Card.status=VERIFIED` is claim set with actual bound authority, not just a syntactically legal `source_ids` or existence of a cited URL.

## 4. Build complete 35-card PRE-ACCEPTANCE package

Construct a new separate W40 r6 **35/35 complete factual Evidence Card candidate result set**, one per non-DROP task, with filenames and exact candidate package task SHA contract; verify 35 unique task IDs and full distinct non-DROP Discovery coverage. Use the *actual Core Card schema* rather than treating r5 `interactive-evidence-r5.json` as accepted Card results.

Validate every candidate with **unmodified** `survey_evidence_v2.validate_evidence_card(..., repo_root=...)` and exact source/supplement binding; run core preflight including semantic source crosswalk and class/rights/temporal audit; record real exit codes, package/card digests, mismatches and run logs. Ensure unsupported-type repro fails on original and no skipped `task_source_ids=None` illusion of approval.

All outputs should remain in clearly labeled `PROPOSED_NOT_ACCEPTED` directories; do NOT invoke `accept_evidence_results`, do NOT create `evidence-accepted.json`, `edition-views-accepted.json`, `EVIDENCE_REVIEWED` checkpoint, Materiality/Completeness accepted, Selection, Architecture or Human Gate. Do not mutate existing 35 draft views to give them premature accepted Card SHA authority; staged replacements may be separate.

## 5. Terminal dossier and stop

Write `execution/SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF-r6.md` and session/validation logs, covering:
- Starting/Final HEAD/Tree, parent/fast-forward, reviewed main, changed-file allowlist, Core/State/Human unchanged;
- exact r5→r6 projection SHA diff + one-to-one source-type change classification and negative tests;
- supplement manifest SHA, all 4 core original source entries and attached raw SHA/bytes, canonical Discovery/Screening identities, exactly bound task/source IDs;
- 35 Card candidates and full validator exit status, any impossible or incomplete source bindings, semantic claim-to-source count and explicit unresolved issues;
- ProvenanceGuard arXiv v1/v2 dates + correct Sep29 team-blog distinction, source version used;
- ELYZA MATERIAL-vs-HOLD justification and benchmark table footnotes, with some benchmark regressions preserved;
- true residual limitations (Olmo report fetch >5MB, paper appendices/figure loss, AstaBrief/AutoSynthData release times unknown, carried W39 rumors HOLD).
- Terminal `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` only if all above complete, else `SOL_EVIDENCE_AUTHORITY_REVIEW_BLOCKED` with exact blocking test/ID.

Stop for Sol independent final Evidence/Card source-binding review. **Sol r2 approves the narrow projection interpretation only; no canonical Evidence Acceptance or stage advancement occurs in r6.**
