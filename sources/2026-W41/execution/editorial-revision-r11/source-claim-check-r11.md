# W41 r11 source–claim check (programmatic + editorial)

Status: `EDITION_LOCAL / AUDIT_EVIDENCE`
Date: 2026-10-13 JST
Method: official `draft-check` CLI 6/6 PASS + programmatic ID audit below + editorial spot-check.

## Programmatic audit results (executed, all PASS)

- Every `evidence_refs` tuple (task/kind/id/subject/role) in 6 proposals resolves to a real
  Card ID in accepted Evidence `717ea04a…` with matching subject binding: PASS (via Core validator).
- Every must-cover requirement maps to existing block IDs (exact-once, no blanket): PASS.
- Every Architecture boundary disposed exactly once: PASS.
  P4 legacy boundary → RESPECTED_BY_OMISSION with exclusion rationale; supplement
  timestamp/excerpt boundaries (P2×3, P3×3, P4×2, P5×3) → RESPECTED_BY_OMISSION as
  provenance metadata; all substantive boundaries → EXPLICITLY_STATED with block maps.
- Attribution modes cover all referenced classes (VENDOR→ATTRIBUTED/MIXED,
  INFERENCE→INFERENCE/MIXED, SOCIAL_OBSERVATION→SOCIAL/MIXED, PRIMARY_FACT→FACTUAL/MIXED): PASS.
- basis binds exact canonical package SHA + prompt SHA (`b6873133…`): PASS 6/6.
- New specifics and their anchors:
  - Synonym triple + FPR/conditions → textgrain claim-1 (covers "edit-weakening numbers").
  - Elo 1050±14 → nano claim-1 (covers "vendor SxS Elo"; figure from bound excerpt NOTE).
  - SynthID scale pair → synth claim-1 (covers "scale counts vendor-stated").
  - Decisions typed-answers function → decisions claim-1 (same changelog entry, bound excerpt).
  - MRL truncation dims → egemma claim-1 (768-d MRL anchor; publisher-described).
  - Mistral per-1M display → ml4 claim-1 (sale-pricing pair anchor).
  - Absolute/relative splits (13.4pp/~32%) → arithmetic on cited claim-1 figures (no new facts).
- No invented source IDs, no fabricated experiments, no SELECTED-outside promotion
  (20/13/2/1 dispositions untouched; Grok+HOLDs+INSPECTs absent from prose).

## Editorial spot-check (values against Card/excerpt texts)

- 44% (web-search, start-latency, non-wall-time), Haiku split/prices/bench table,
  Decisions beta/10x-caveat, Kolibri scale/compute, d1 Index/8ms, EGemma split/MRL/8K/MTEB,
  Beam scale/intent, Mistral 52B/1.05T/prices/49B-note, Clef timestamp/prices, Nova GA/regions/256K,
  Nano specs/Elo/blog-note, textGrain rollout/FPR/gating, SynthID scope/partners/scale,
  Cyber terms/>90%, math listing/non-release, Ironclad 11-tasks/deltas: all match consumed texts.

## Guard checks

- Legacy spans (`no blog post exists` / `rollout post nonexistent` / `blog post does not exist`):
  0 hits in all 6 proposal reader fields + preview + synthesis result. 1 lawful hit each in
  P4 proposal `boundary_dispositions[]` machine trace (required verbatim, OMISSION-handled).
- Old over-assertions (`テキスト除外`, `ベンチマークも存在しない`, `精度ベンチなし`,
  `今日落とせる`, `落として使える`): 0 hits in P3/P5 proposals.
- Priority C self-reference patterns (9 listed): 0 hits in proposals.

(End of file)
