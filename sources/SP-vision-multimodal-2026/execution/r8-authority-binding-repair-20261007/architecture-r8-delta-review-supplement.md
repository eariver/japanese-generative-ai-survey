# Architecture r8 delta-review supplement (edition-local)

Run: `r8-authority-binding-repair-20261007` (Owner-Exception, Core-controlled rewind
DRAFT_COMPLETE → CANDIDATES_NORMALIZED, then deterministic replay).
Prior canonical bytes: HEAD `722bcb5db933268fdf8871a2054f142f9d37f790`
(tree `718e12363cf2ba5bdf2192980e7e111823d3f11c`), r7 APPROVED.
Regenerated canonical bytes (uncommitted working tree at supplement creation):

- Evidence acceptance (new): `1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d`
  (121 results: VERIFIED 116 / PARTIAL 5; prior `66c9932e…` preserved as history;
  120 carried byte-identical, 1 corrected: VM-D039).
- Selection (new SHA `facf3d5c24a40fbc3ac7766397569c85915b927aa049005436dc4a6de3522198`,
  121 assignments carried byte-identical, 0 rationale/disposition changes).
- Completeness (new SHA `a547545cd9bb0e2888d88cdac76d5480728e12b50e40d4618b25cad046dc1565`,
  obligations/residual/closure semantically identical, 14 SATISFIED / 2 LIMITATION).
- Architecture (prior r7-approved SHA `ec1b9616226219c71d4b3f291d0dfc96e56cc8c8b947db4cdc12db2a074f3170`
  → regenerated SHA `56658960dff0269a89bf38d5b3027147dea7159f5c15337ff8a74d6ea7e4d773`).
- Review summary (prior `3828d174…` → regenerated `69a17899ae022ee0198e8a48feaf1401689b275a020d5d4d202abf0aa3b1017c`).
- Review attention (prior `87aa3f5c…` → regenerated `825d0081900adc724f3b6bf8d21fd5d384258e35948ed1141ce9c5fb03950db`).

## VM-D039 CLIP (Evidence-only wording fix)

- Old claim-1: `…matches supervised ResNet-50 on ImageNet with zero of its 1.28M labels;…`
- New claim-1: `…matches the supervised ResNet-50 baseline on ImageNet without using any of its 1.28M training examples;…`
- Preserved: 400M pairs, addressability, zero-shot, §6/§3.1.5 limits, no BoW
  misattribution, VERIFIED status, all other claims/limitations/verification.
- No new source. Exactly one Evidence semantic change (120 cards byte-identical).

## P11 SAM 3 (only Architecture semantic change)

- Old must-cover: `SAM 3 memory video tracking as supporting stored-timeline evidence`
- New must-cover: `SAM 3 concept-prompted video grounding and memory-based tracking
  are supporting temporal-grounding evidence; stored-timeline on-demand navigation
  remains the distinct VM-D112 contract.`
- Preserved: offline vs online vs stored-timeline three-contract structure, no P11
  restructuring, all other must-cover/boundaries/page weights.
- P07B must-cover UNCHANGED (incl. `SigLIP 2 localization transfer and SAM 3 concept
  grounding extend open-vocabulary perception (supporting)`). P15 UNCHANGED except
  hash rebinding. All other 15 packages byte-identical modulo basis/status/review.

## Invariants held at supplement creation

Discovery 122 / Evidence 121 (116/5) / Selection 121 / Completeness 14/2 /
Architecture 16 packages / page plan 112/120 unchanged / P15 40 IDs (+keys)
unchanged / DISCOVERY_COVERAGE_FROZEN_FINAL preserved. No new Discovery/source/
candidate, no disposition/status change, no new LIMITATION, no package
restructure, no shared Core change. Draft NONE for the r8 chain
(fresh-121-r7-rev1 is historical/regression material only).
