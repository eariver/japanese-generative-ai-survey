# Architecture r6 delta-review supplement (edition-local)

Run: `r6-final-authority-correction-20261006` (Owner-Exception, Core-controlled rewind
ARCHITECTURE_ESTABLISHED → CANDIDATES_NORMALIZED, then deterministic replay).
Prior canonical bytes: HEAD `4e2d8837514f1529fdd1e695ed7d3952e44eda3d`
(tree `f179f3e0343225a1d70e92ee2709b8c0f9e44664`).
Regenerated canonical bytes (uncommitted working tree at supplement creation):

- Evidence acceptance (new): `81e3b75be5ac2b489512898dfe236a20b41a73617a8cb5b4b7783f868580764b`
  (`evidence-accepted.json` SHA `4258dc755a89083cf972669e4a8dca21320504a319549a956802ed8285b7947a`,
  121 results: VERIFIED 116 / PARTIAL 5; prior `68be75fd…` preserved as history).
- Selection (new SHA `20142cf9002e9992c883ae884edf40a363f7b863c58ee537ad7c1a715d758858`, 121 assignments).
- Completeness (new SHA `f1898ed63b2eca6e9fb2c4c2a7c85e9ba0326f21b0ab3cc068dbf0660917610f`, 14 SATISFIED / 2 LIMITATION).
- Architecture (prior HEAD SHA `3cadf5e820199a4cb1642c2efec0ddfa827b47b91656e9977693485fa701f14f`
  → regenerated SHA `bbf3eaa62f182a7ecac33533be7450638581d5ff5aca3218894cf96c95623070`).
- Review summary (prior `7d5cfdc9…` → regenerated `618cde08…`).
- Review attention (prior `9a68d243…` → regenerated `c774f9b4…`).

Core-generated summary/attention are rebuilt deterministically but do not print a
side-by-side semantic delta; this supplement is the explicit Human-facing delta record.
It creates no Human decision.

## VQA (VM-D038 / P07A / VM-O07)

- Old source set: `https://arxiv.org/abs/1505.00468` only (Antol et al., VQA v1).
- New source binding: `https://arxiv.org/abs/1505.00468` (preserved v1 predecessor)
  + `https://arxiv.org/abs/1612.00837` (Goyal et al., VQA v2; supplement
  `supplement-src-2931815e4c48399b`, raw HTML v3 216781 bytes, SHA
  `658b6449a5d429537a2059b96625c328e957437fa7fa491265b709a0b4d6c1f7`).
  Enrichment of the EXISTING VM-D038 candidate; NOT new Discovery/candidate/node; NO VQA-CP.
- Old limitation wording: `VQA-v2 training contamination and prior-exploitability
  qualify naive accuracy readings; bind split + extraction rule.`
- New limitation wording (verbatim in Evidence + P07A boundary): `VQA-family
  accuracy can exploit question/answer priors; VQA v2 reduces this bias using
  complementary image pairs, so dataset version/split and answer extraction must
  remain bound to evaluation claims.`
- New claim-3 (AUTHOR_CLAIM, src VQA-v2): complementary construction
  (same question + similar/complementary images + different answers, ~2x pairs);
  SOTA worse on balanced set (prior exploitation); mitigation reduces but does not
  eliminate language priors.
- Old Architecture wording removed from P07A boundaries; replaced with the new
  limitation verbatim. VQA predecessor role, CLIP addressability transition,
  original-CLIP limits, D07A metric identity, D07A/D07B separation, ALIGN/SigLIP
  lineage preserved. No package redesign. VM-O07 completeness rationale unchanged
  (already source-accurate from the prior run).

## Measurement provenance (VM-D065/066/070/071, P09, P15, G05)

- Old binary/overbroad wording: blanket `All benchmark claims vendor-measured`,
  `No-degradation and leaderboard claims vendor-measured`, `Vendor-measured evals
  at this read level`, `vendor-claim quarantine`, vendor-only G05
  (`independent reproduction of current vendor/model-report scores (all vendor
  scores quarantined with attribution)`).
- New three-way taxonomy (applied consistently):
  `author/developer self-reported` (Qwen3-VL / Qwen3-Omni / InternVL3 / Molmo 2
  paper measurements) vs `provider/vendor-reported` (Gemini model cards, Agentic
  Video official-service ceilings) vs `independent third-party` (separate category
  when applicable). Author/developer and provider/vendor are both first-party with
  distinct provenance roles; neither is independent.
- Affected Evidence IDs: VM-D038 (above) + VM-D065 + VM-D066 + VM-D070 + VM-D071
  (5 corrected; 116 carried byte-identical). Unchanged: VM-D072 / VM-D073 /
  VM-D112 (provider/vendor preserved), VM-D074–D077 (project roles), Whisper/BEATs/CLAP.
- P09 delta: 2 must_cover refinements (first-party latency/token figures;
  provider/vendor ceilings for VM-D112) + 3 author-boundary carries verbatim
  (065 with `measurements`, 066, 070); Molmo 2 `Author-measured comparisons`
  preserved; provider/vendor verbatim carries preserved (072/073/112); no technical
  content or package-structure change.
- P15 delta: purpose `vendor-vs-independent separation` → three-way separation;
  must_cover `P09 Gemini-3.x vendor-vs-independent poles` → three-way poles;
  Gemini boundaries use `provider/vendor-reported` labels where the Architecture
  speaks (verbatim evidence carries preserved where the validator requires exact
  text); map key `p09_vendor_vs_independent` → `p09_measurement_provenance`
  (40 distinct IDs unchanged); methodology-first, X01–X04, contracts, no ranking,
  convergence synthesis preserved.
- G05 delta: completeness residual/closure `G05 … vendor/model-report scores (all
  vendor scores quarantined …)` → `G05 independent reproduction of current
  first-party model/report/card measurements remains limited (author/developer
  paper measurements and provider/vendor reporting surfaces are both first-party
  with distinct provenance roles; all first-party scores quarantined with
  attribution)`. G05 remains MEASUREMENT/REPRODUCTION GAP, NOT coverage gap.

## Invariants held at supplement creation

Discovery 122 / Evidence 121 (116/5) / Selection 121 / Completeness 14/2 /
Architecture 16 packages / page plan unchanged / P15 40 IDs unchanged /
DISCOVERY_COVERAGE_FROZEN_FINAL preserved. No new Discovery, no removed
candidate, no disposition change, no new PARTIAL, no VERIFIED change, no new
Architecture limitation, no shared Core change. Draft NONE for the r6 authority
chain (fresh-121-r5-rev2 is historical/regression material only).
