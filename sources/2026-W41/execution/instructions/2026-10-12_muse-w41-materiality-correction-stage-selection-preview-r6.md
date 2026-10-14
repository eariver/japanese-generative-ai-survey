# J-GAS W41 — Muse r6: Materiality Semantic Correction → Core Stage → Selection Preview

Status: `EXECUTION_AUTHORITY / SOL_MATERIALITY_R5_CONDITIONAL_PASS / CORE_V2_IMMUTABLE / STOP_BEFORE_SELECTION_ACCEPTANCE`
Date: 2026-10-12 JST
Repository: `eariver/japanese-generative-ai-survey`
Only existing branch: `weekly/2026-W41-v2-work`

## 0. Exact startup, fail-closed

The invoker supplies exact Starting HEAD/Tree for this instruction commit. Before ANY write read-only verify:
- remote W41 branch exact HEAD and Tree equal invoker values; this contract commit's parent is `9f3484e885192bc0d72f73683cd15ec318b37749` (Sol Materiality Review);
- Sol-reviewed r5 HEAD `3adbcf32b8aac21a50911a49de1a6c2f42580af3`, Tree `c8b00fd3716479c14c1e9f5ea1a945706ddeda49` in exact ancestry;
- remote main HEAD `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`, Tree `31c0adc5b57761e5073d100554279a8adc5a18f4`;
- remote production/survey-core-v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- W41 State `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; only Discovery and Screening checkpoints PASSED; Evidence/Materiality/Completeness PENDING, both Human Gates PENDING;
- immutable Evidence Acceptance set `717ea04a51bda4ab8b1d652d9ca92122e6f67431815c5bd910de15e2bad522db` 36; historical Edition View Acceptance set `e0a6c921efec0037ffcc3c6708866b22845eb22fe30cf6ae403539c971aac2dc` 36; 37 Discovery and 37 Screening unchanged; unowned workspace work absent.

Mismatch -> ZERO WRITES, report expected and actual; no new/review/repair/fallback branch; no force/reset/rebase/rewrite; no shared Core/schema/scripts/config/workflows or main/W40 changes; no Human decisions.

## 1. Sol review is binding

Read complete review:
`sources/2026-W41/execution/reviews/sol-w41-materiality-completeness-r5-20261012.md`.

Scope restrictions SC-M41-01..04 are binding. All fixes edition-local and versioned. **Do not undo or alter the canonical Evidence 36 Cards, its accepted manifest, r5 files, or original daily/weekly intake raw.**

## 2. SC-M41-01 — one View correction ONLY, with manifest reacceptance

- Create **separate** r6 36-View input directory by copying the 36 *historically accepted* r5 Views exactly as baseline.
- Modify exactly the View for `evidence:2026-W41:d3b121be6163f0ef` / `w41-grok-x-ledger-20261011`:
  * materiality.status `MATERIAL` -> `CONTEXT`,
  * materiality.rationale and profile_annotations.why_this_issue -> reason: `source-intake provenance and coverage limitation; not an independent technological event; no separate reader-facing news article`,
  * profile_annotations.window_relation `MAIN_EVENT` -> `OTHER`;
  * preserve all other keys, task ID and evidence SHA.
- **All 35 other Views must be byte-identical to r5 accepted Views.** Produce per-file SHA diff, and negative gate that aborts on any other changed file or View field.
- Validate 36/36 with frozen `validate_edition_view`, use `accept_edition_views` and `validate_edition_views_acceptance` with SAME original Evidence Acceptance 36. New content-addressed accepted View run; no manual acceptance JSON and no overwriting historical accepted Views.
- Expected status: MATERIAL 20 / HOLD 13 / CONTEXT 3 (Views; PLUS 1 DROP in Materiality ledger).

## 3. SC-M41-02 — reader-facing unsupported-negative exclusion

- Record `LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE` for Nano Banana Evidence task `evidence:2026-W41:e9e13879f1c0fcf8`. Exact legacy phrases occur in Card claim-1.context, limitation-1 `rollout post nonexistent`, supplement role/source relation `no blog post exists`. These are unsupported categorical absence claims, though claim-2 properly says `not found among checked pages`.
- Make an edition-local **publication exclusion/claim-source overlay** (non-authoritative over Core) with the precise forbidden positive assertions, admissible narrower language, source IDs, reader-output grep patterns, and audit procedure. Do not rewrite accepted Card/Raw. This is not a grant to override source truth; positive DeepMind model-card content remains available.
- If any Core/Selection/Draft path automatically surfaces the unsupported claim and cannot exclude it without changing accepted Card, STOP with exact reason and propose a separate versioned Card reacceptance; no silent erasure or Core patch.
- Preserve 8 supplement-access provenance caveats (BUNDLE_WINDOW_ESTIMATE, per-page unknown, BOUNDED_EXCERPT not HTML).

## 4. SC-M41-03/04 — Materiality, Completeness, technical-depth assessment

- Rebuild fresh schema-valid `materiality-ledger-r6.PROPOSED.json` **from the new accepted Views** and original accepted Evidence/Discovery/Screening. Verify 37 IDs, 36 Evidence + View pairs, exact basis hashes, distributions `20 MATERIAL / 13 HOLD / 3 CONTEXT / 1 EXCLUDED`.
- Rebuild `profile-completeness-r6.PROPOSED.json` from the new Ledger and original Profile. Preserve `LIMITED`, never upgrade to READY by dropping source/quality limitations. Run actual frozen Core `validate_profile_completeness` with exact basis; any known historical state-basis override must be narrowly documented, and must not disable source, SHA, acceptance or completeness checks.
- Write a **distinct editorial Materiality/Completeness dossier** beyond Core's tautological `Screening=KEEP; View=MATERIAL`: for each of the 20 genuine technology MATERIAL candidates, source and claim links, verified vs vendor metrics, technical mechanism, quantitative methodology actually read, Japanese relevance, link to related candidates, proposed role (lead/deep-dive/brief/comparator) and specific minimum evidence to explain without inflated claims. Group substantive themes (frontier; open weights/local/edge; decision models & agents; media/provenance; safety/cyber; retrieval/science) rather than equating 20 subjects to 20 separate articles. Identify where a putative standalone article would be too thin and combine it with a technical comparator. Include named counterfactual omitted high-material items and 13 HOLD reasons.
- Source intake and provenance coverage must be carried over: seven Daily X originals and 92 topics, Grok 14 posts 12 in-window/2 post-cutoff, no evidence of 09:00 independent runs, unconsumed reports/JS-gated pages, model weight license uncertainty, cutoff sensitivity, vendor-only metrics, W40 four carryover HOLD. X ledger may be a research source but NOT a publication event.

## 5. Stage and bounded Selection proposal

**Only after** all corrections/validations above pass with no new substantive Evidence contradiction:
1. Use frozen Core's canonical Stage Validation, exact machine checkpoint and authorized State transition to advance `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` while simultaneously completing Evidence/Materiality/Completeness checkpoint integrity. Stop if Core rejects `LIMITED` or other basis drift; no synthetic/pass metadata or direct hand-written State.
2. Read back remote exact canonical State/HEAD/Tree and passed checkpoints; retain Human Gates PENDING.
3. Prepare a **noncanonical Selection proposal / preview only** using existing Core schema/selection machinery when valid. Do NOT invoke canonical Selection Acceptance, no `SELECTION_COMPLETE` advancement, no Architecture stage and no Human architecture decision.
4. The proposal must choose enough substantive depth for a full W41 Weekly issue; no article-count inflation from Grok source ledger. Explain reader-level issue narrative, lead news selection, grouped technical mechanics, expected evidence citation and competing alternatives, treatment of all 20 MATERIAL, why 13 HOLD/3 CONTEXT excluded or used as sidebars, and honest page/word-depth estimates. Do not proceed to TeX/PDF or pretend exact pagination is fixed at this stage.

## 6. Terminal stop/validation

Stop at `SOL_SELECTION_MATERIALITY_PREVIEW_REVIEW_READY` ONLY if new 36 Views acceptance and combined Stage PASS are legitimately complete. Otherwise report `STAGE_BLOCKED`, with exact missing contract and no forbidden advance.

Final report includes Starting/Ending HEAD/Tree and main/Core hash, all changed paths, previous vs new View SHA changes (exactly one), Evidence accepted SHA unchanged, 36-card/36-View graph SHA, new Materiality/Completeness exact SHA, Core validation exit statuses and checkpoint IDs, source-authority exclusion overlay, editorial depth/counterfactual dossier and Selection preview path. Normal commits, non-force push only. Sol will independently review Selection before canonical acceptance or Architecture.
