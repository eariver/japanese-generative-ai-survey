# Architecture r7 delta-review supplement (edition-local)

Run: `r7-targeted-authority-repair-20261007` (Owner-Exception, Core-controlled rewind
DRAFT_COMPLETE → CANDIDATES_NORMALIZED, then deterministic replay).
Prior canonical bytes: HEAD `1bada73fc8cf84689489e9d397e5db300cbb444f`
(tree `7cdcf4b4973a47b89da7b9e0046c95a23ce646b9`), r6 APPROVED.
Regenerated canonical bytes (uncommitted working tree at supplement creation):

- Evidence acceptance (new): `66c9932ebc23a3c04df6c1dd2ba65fb300c7e090343e5062487160f00682c77f`
  (121 results: VERIFIED 116 / PARTIAL 5; prior `81e3b75b…` preserved as history;
  119 carried byte-identical, 2 corrected: VM-D108, VM-D010).
- Selection (new SHA `06d1eece30e28bd89de0f64a76063a9569a4f6c50a11734daf85e0f1bbccceed`,
  121 assignments carried byte-identical, 0 rationale/disposition changes).
- Completeness (new SHA `8fc5bb2d41828f2eef59bffe38a6d509d39f4ecd14e5f6940134bc4429cbc7e6`,
  obligations/residual/closure byte-identical, 14 SATISFIED / 2 LIMITATION).
- Architecture (prior r6-approved SHA `bbf3eaa62f182a7ecac33533be7450638581d5ff5aca3218894cf96c95623070`
  → regenerated SHA `ec1b9616226219c71d4b3f291d0dfc96e56cc8c8b947db4cdc12db2a074f3170`).
- Review summary (prior `618cde08…` → regenerated `3828d174373e6c294b768f575d9aecf3ee325f21d3dcb831f2659045c97aa876`).
- Review attention (prior `c774f9b4…` → regenerated `87aa3f5ce179d4c0a1485b99ff6887366029c07b72b4ed1141ce9c5fb03950db`).

Core-generated summary/attention are rebuilt deterministically but do not print a
side-by-side semantic delta; this supplement is the explicit Human-facing delta record.
It creates no Human decision.

## VM-D108 DocVQA (P05 / P15)

- Old claim-2: `Reporting discipline: ANLS, never bare accuracy alone
  (OCR-substring upper bounds inflate); contamination MEDIUM, language-prior HIGH
  (extractive shortcuts).` (INFERENCE carrying unmeasured severity grades.)
- New claim-2: `Reporting discipline: ANLS, never bare accuracy alone
  (OCR-substring upper bounds inflate). Because DocVQA uses public-source documents
  and extractive answers, evaluation of later pretrained foundation models should
  separately audit possible pretraining overlap and shortcut behavior; the DocVQA paper
  itself does not measure contamination prevalence or assign a risk level.` (INFERENCE.)
- Old limitation: `Extractive-shortcut vulnerability; web-document contamination.`
- New limitation (verbatim in Evidence + P05/P15 boundaries): `Extractive-shortcut
  vulnerability is a source-supported design concern; possible web-document pretraining
  overlap is an edition-level audit concern, not a paper-measured contamination rate.`
- Preserved: 12K+ images / ~50K questions / provenance / extractive setup / 9 reasoning
  categories / ANLS (+accuracy context) / baselines vs human 94.36% / open
  dataset+code+leaderboard. No replacement grading scale introduced.
- Downstream: P05/P15 must not present contamination as a measured level; edition-level
  audit concern stays visibly inference-bounded. Generic evaluation-contract wordings
  (`contamination opacity (closed models)`, `contamination binding` disciplines) are not
  DocVQA-graded claims and are preserved.

## VM-D010 DETR (P02 verified clean — no Architecture change)

- Old claim-3 tail: `NMS provably unnecessary only from later decoder layers
  (self-attention duplicate inhibition).`
- New claim-3 tail: `DETR is designed to omit NMS in the final set-prediction pipeline;
  layer-wise ablation shows that NMS can improve the first decoder layer, but its benefit
  decreases with depth and becomes harmful at the final output; the paper interprets this
  as duplicate suppression emerging through decoder interactions/self-attention.`
- Preserved: direct set prediction, Hungarian assignment, matching-cost vs training-loss
  distinction, object queries, parallel decoding, no anchors, NMS-free final pipeline,
  auxiliary losses as training recipe.
- Architecture/review surfaces contained no overstrong NMS wording, so P02 is unchanged
  (verified by assertion in the replay script). DETR correction is Evidence-local with
  downstream effect through the fresh Draft (§13 guard).

## Invariants held at supplement creation

Discovery 122 / Evidence 121 (116/5) / Selection 121 / Completeness 14/2 /
Architecture 16 packages / page plan 112/120 unchanged / P15 40 IDs unchanged
(map keys and set identical) / DISCOVERY_COVERAGE_FROZEN_FINAL preserved.
Exactly two Evidence semantic changes (VM-D108, VM-D010); 119 cards byte-identical.
No new Discovery/source/candidate, no disposition/status change, no new LIMITATION,
no package restructure, no shared Core change. Draft NONE for the r7 chain
(fresh-121-r6 is historical/regression material only).
