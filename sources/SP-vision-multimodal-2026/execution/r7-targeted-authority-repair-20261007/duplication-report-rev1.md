# Edition-local duplication report — known cross-package pairs (r7-rev1)

Method: human-readable semantic comparison of PRIMARY vs secondary prose (not a
lexical-similarity threshold). Before = fresh-121-r7 bytes (commit `c7aaf74f7`);
after = rev1 working-tree bytes. All comparisons at block level with refs intact
(no authority removed; only prose trimmed/refocused).

## 1. SigLIP 2 — P06-B08 (PRIMARY) vs P07A-B05 (secondary)

- Before: P07A-B05 was a near-complete restatement of the P06 staged recipe
  (sigmoid loss, LocCa, SILC, TIPS/DINO-line masked prediction, online curation,
  WebLI 109 langs, NaFlex aspect/multi-res, RefCOCO/OWL-ViT/dense/PaliGemma gains,
  NaFlex limits) — same mechanism paragraph twice.
- After: P07A-B05 keeps only the image-level-alignment significance (CLIP-lineage
  position, staged-teacher components named once, NaFlex/WebLI named as training
  context, RefCOCO/OWL-ViT/dense/PaliGemma gains read as image-level extension,
  limits stay paper-scoped, P07B boundary explicit). P06-B08 untouched (full recipe).
- Verdict: duplication removed; P07A answers only `why it matters to image-level
  alignment`. Refs unchanged (D039 c1/c2 + D114 c1/c2/c3).

## 2. VSI-Bench — P10-B6 (PRIMARY, three-role chain) vs P11-b8 (secondary)

- Before: P11-b8 restated the full VSI design (288 videos/5131 Qs, 3 types/8 tasks,
  MCA/MRA, no-see baseline, CoT-down/cognitive-map-up, abstract-level restraint).
- After: P11-b8 is a 3-sentence synthesis (VSI shows the scaffold effect; the effect
  belongs to a different column than this section's contract; abstract-level
  restraint kept, debiased-subset analysis not attempted). MCA/MRA detail lives only
  in P10-B6.
- Verdict: duplication removed; PARTIAL-depth treatment preserved per Architecture.

## 3. SAM 3 — P03-B8 (PRIMARY, promptable perception) vs P11-b10 (secondary)

- Before: P11-b10 restated the full mechanism (noun phrase + pos/neg boxes + SAM-2
  clicks, shared encoder, existence-token split, inherited memory, fine-grained
  zero-shot weakness, linear cost) already in P03-B8.
- After: P11-b10 keeps the contract framing (concept instruction as auxiliary basis
  for the stored-timeline contract, novelty/limits attributed to P03's scope).
  Mechanism detail lives only in P03-B8.
- Verdict: duplication removed; secondary answers `why it matters to the stored
  timeline`.

## 4. Agentic Video — P09-B11 (PRIMARY, token/context economics) vs P10-B7 / P11-b9

- Before: P10-B7 and P11-b9 each restated the full static-vs-agentic pipeline
  (1fps + 1kbps audio, per-query retrieval, interest-window resampling, 88%/66%
  ceilings, saved-posts/YouTube scope, online-state disclaimer).
- After: P10-B7 keeps only the chain position (third step: tool-assisted perception;
  ceilings are provider-measured upper bounds; token scope; neither general
  reasoning nor online-state evidence). P11-b9 keeps only the contract position
  (third contract vs online streaming; static defaults vs per-query retrieval;
  provider-measured ceilings; offline-timeline scope). Full pipeline, token math,
  and ceiling tables live only in P09-B11.
- Verdict: duplication removed on both secondaries; chain/contract roles intact.

## Residual

No other cross-package pair repeats full mechanisms at paragraph scale. P15
synthesis intentionally re-states per-contract verdicts with fresh comparative
framing (methodology-first, no catalogue); per-thread 40/40 consumption preserved
and separately audited.
