# W41 Sol Materiality/Completeness Review handoff r5 (pre-transition)

Status: `SOL_MATERIALITY_COMPLETENESS_REVIEW_READY` (REVIEW_PENDING — no EVIDENCE_REVIEWED, no Materiality/Completeness PASS, no Sol approval forged)
Date: 2026-10-12 JST
Branch: `weekly/2026-W41-v2-work` (existing only; no new branch, no force, no rewrite)
Starting HEAD `7741e7d20e8e7948c0a619e4f048c5601da4085c` / Tree `55c49f41acc077e42d80cab821cfdfe6a55d0b81` (verified read-only; instruction parent cbcfbd4c; r4 241a1cd5 in ancestry)
Reviewed main `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`; Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` (shared roots untouched)
Sol authority: `execution/reviews/sol-w41-evidence-authority-binding-r2-20261012.md` (TECHNICAL_PASS, ACCEPTANCE_CONDITIONAL on SC-E41-05/06)
Ending HEAD/Tree: recorded in session r5 + commit (this file written pre-commit).

## 1. SC-E41-05 attestation (exact-nine, fail-closed)

- New guarded builder `execution/compat/evidence-source-class-projection-r4/build_r2_package_r5.py` enforces the ledger allowlist (did+task-id+original type, cardinality 9); aborts on tenth/missing/unknown/extra diffs (only projection + 8 supplement bindings permitted).
- Regeneration byte-identical to reviewed r4 r2 package (36 tasks + package.json): IDENTICAL_PASS. Double-build IDENTICAL_PASS. Negatives (tenth/missing/unknown): 3/3 FAIL_CLOSED_PASS.
- SHA crosswalk: r2 package/tasks SHAs unchanged from r4 (see ledger rows + byte-equality proof in session log). No Discovery/Screening mutation.

## 2. SC-E41-06 attestation (editorial/provenance)

- NanoBanana categorical absence → scoped negative-search observation (card claim-2 + verification finding revised; SOCIAL_OBSERVATION retained).
- Supplement `accessed_at` provenance ledger `execution/source-intake/w41-supplement-access-provenance-r5.md`: all 8 entries labeled BUNDLE_WINDOW_ESTIMATE / PER_PAGE_UNKNOWN; card limitations carry the caveat.
- Raw files labeled BOUNDED_EXCERPT (verbatim + reviewer headers/NOTEs); card limitations state it for all 8 supplemented tasks.
- textGrain method assertions restricted to blog-documented facts (limitation added; PDF unread retained).
- HOLD/cutoff discipline preserved (StepFun, MS day-only, Tencent month-only, 4 W40 HOLDs, Drex Sep origins, Clef blog-vs-X clocks).

## 3. Formal acceptances (frozen Core)

- Evidence Acceptance `evidence/v2/accepted/717ea04a51bda4ab8b1d652d9ca92122e6f67431815c5bd910de15e2bad522db/evidence-accepted.json`: 36 cards (3 VERIFIED / 21 PARTIAL / 12 NEEDS_MORE), validated.
- Views Acceptance `evidence/v2/views/accepted/e0a6c921efec0037ffcc3c6708866b22845eb22fe30cf6ae403539c971aac2dc/edition-views-accepted.json`: 36 views rebuilt on accepted SHAs, validated.
- Cards live in `evidence/v2/results/r5/` (28 non-revised differ from r2 ONLY in runner timestamps; 8 substantively revised per §2). r1/r2 assets preserved.

## 4. Materiality/Completeness proposals (NONACCEPTED review inputs)

- `execution/materiality-ledger-r5.PROPOSED.json` (Core-built+validated, 37 rows): 21 MATERIAL / 13 HOLD / 2 CONTEXT / 1 EXCLUDED (sweep). HOLD 13 = 12 NEEDS_MORE cards + Drex PARTIAL/HOLD; CONTEXT 2 = usage-policy + ELYZA. MATERIAL led by frontier releases + first-party-corroborated APIs + downloadable open weights. No empty-short-issue risk: 21 MATERIAL cover frontier/open-weight/audio/safety/retrieval/agent lanes.
- `execution/profile-completeness-r5.PROPOSED.json` (overall LIMITED): obligations current-relevance SATISFIED / technical-significance LIMITATION / carry-over SATISFIED; residuals (09:00 absence, X-authorship, unread bodies, JS/timeout gaps, day/month clocks, snippet-only pricing, delegated reads). Full validator PASS under agent-tool override (bare run notes only the known historical screening state-basis drift).
- Counterfactual omissions: Nano Banana now MATERIAL-bound (card found); d1/Nova/textGrain/Mistral/Haiku/embedding/decision/local-edge all MATERIAL with vendor-metric caveats; no justified-hold gap blocks issue formation, but 12 NEEDS_MORE need Sol's gap-fill-vs-HOLD call.

## 5. State / stop

- State `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; evidence/materiality/completeness checkpoints PENDING (no transition run); gates pending.
- Unresolved: projection approval (Sol), NEEDS_MORE disposition, unread bodies, delegated re-verification, vendor-only benchmarks, Core map repair + clean rerun before any future canonical reliance beyond this reviewed acceptance.
- Changed paths: compat (r5 builder), results/r5 (37), results input file, accepted evidence+views, execution ledger/proposals/log/handoff/session/index, provenance ledger. Nothing outside sources/2026-W41.
