# W40 Muse r7 — ProvenanceGuard primary-paper version pin only

Status: `SOL_BOUNDED_AUTHORITY / SC-E09_SOURCE_VERSION_REPAIR / STOP_AT_SOL_EVIDENCE_REVIEW`
Authoritative Sol r3 review: `sources/2026-W40/execution/reviews/sol-w40-evidence-authority-consumption-r3-20261010.md`
Repository: `eariver/japanese-generative-ai-survey`
Only existing branch: `weekly/2026-W40-v2-work`
Reviewed main SHA: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Reviewed Muse r6 HEAD/Tree: `b33f6aae45605ebf17792f4bd588252d76bfb860` / `6498ea6560778c4d1cd261eb93529f58e26ce7c8`
**Starting SHA/Tree for r7** must come from outer invocation after this file is committed.

## 0. Guard and immutable limits

Before ANY write, verify read-only remote branch HEAD=outer Starting SHA, commit Tree=outer Starting Tree, remote main HEAD=`afdb3df3faa20af3bb5798be429bba8dbd2100b1`, Muse r6 `b33f6aae45605ebf17792f4bd588252d76bfb860` strict ancestor and Production State `CANDIDATES_NORMALIZED`, next action `stage:evidence-materiality-completeness`; Human Gates pending/pending. Mismatch => STOP with actual/expected, ZERO WRITES. No new/review/fallback/repair branch, reset, force, history rewrite, shared Core/schema/CI/main/other edition modifications, Human Gate writes or Screen/Discovery acceptance changes. Normal commits + nonforce push to existing W40 only.

## 1. Mission — one source version + propagation, not a new wide research pass

Review the official **`https://arxiv.org/html/2606.18037v2`** (July 26, 2026, four author version) against **Muse r5 actually consumed ar5iv excerpt** and its method/evaluation claims, authors and tables. The prior r6 manifest claims consumption of v3 published Aug 27, but the archived paper excerpt lists exactly the four-author v2; newer third-party catalogs show additional later-author metadata. The reviewer requires **source-version identity**, not merely probable v3 existence.

**Preferred bounded route**: Establish the read source's core equations, tables, metrics and author list against primary v2, and use v2 in a new r7 Evidence Authority Supplement: version-pinned locator to original v2, `published_at=2026-07-26T10:47:53Z` and relation explicitly `ar5iv excerpt assessed against primary v2`. Record the different original paper v1 date (Jun 16) and Sep 29 W40 team-blog event; do not say v2 is W40 original publication.

If Muse finds genuine contrary evidence that the excerpts were from v3, the alternative is permitted only with exact primary v3 link, versioned original text, matching author body/table evidence and substantiated original timestamp; do not guess URL/time from a secondary catalog or conflate later abstract metadata with already consumed content. If v2/v3 changes materially affect the stated evaluation figures, correct only these affected claim lines with explicit version/difference ledger, otherwise keep scientific findings intact.

## 2. Deterministic authority rebuild

- Preserve r6 manifest/package/Cards as immutable superseded PROPOSALS; create versioned `r7` copies under W40.
- Rebuild Evidence Authority Supplement with four task-bound sources: unchanged exact ELYZA 33B/32B and CLM entries, corrected ProvenanceGuard paper entry (source ID may change if locator changes; obey schema). Recalculate raw hashes/bytes and manifest SHA; zero fabricated source bytes or publication instants. Use frozen Core supplement builder/validator to certify SHA + id + source type/class.
- Rebuild exact r7 derived task package from original r1 canonical + reviewed r5 source projection, with appropriate new supplement references, deterministic 35 task SHA package, double-build and unknown-type fail-closed. **No mutation** of original Discovery 37, Screening 37, canonical r1 tasks, r5/r6 historical proposals.
- Update only relevant Proposed ProvenanceGuard reviewer input/temporal event to v2 or explicitly proved matching revision. Keep W40 Sep 29 blog event, author-reported metrics and pre-window paper status distinguished.
- Regenerate a complete **35-card Proposed result set** under r7 basis and ensure all `validate_evidence_card(card,task,sha,package,repo_root)` Core checks PASS without skipping source binding, and complete 35/35 card source-role audit. Record paths, authoritative input hashes, actual executed commands/exits. Update only new r7 views if essential; do not claim views accepted/rebound to nonexistent accepted Card results.
- Hold r6 DGX as an item-level Selection check (source day/time may be revisited at Selection), while preserving ELYZA new primary bindings and MATERIAL reviewer conclusion.

## 3. Stop / report

Produce `sources/2026-W40/execution/SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF-r7.md`, validation log, task/Card lineage, source version comparison record, file SHA checks and exact git readback proof.

Terminal `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` only if the version issue is closed and **35 Card source bindings pass**; else `SOL_EVIDENCE_AUTHORITY_REVIEW_BLOCKED`. Keep Production State `CANDIDATES_NORMALIZED`, evidence/materiality/completeness checkpoints pending, both Human Gates pending. No formal Evidence Acceptance, Stage advance, Selection/Architecture or Human Gate. Stop for Sol independent review.
