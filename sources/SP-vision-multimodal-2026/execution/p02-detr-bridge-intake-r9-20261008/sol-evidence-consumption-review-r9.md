# TS-003 P02 Bounded Bridge — Sol Evidence Authority-Consumption Review r9

Status: `SOL_EVIDENCE_CONSUMPTION_REVIEW_R9 / PASS / AUTHORIZE_MATERIALITY_SELECTION`

Date: `2026-10-08`

Run: `execution/p02-detr-bridge-intake-r9-20261008`

Reviewed authority: Evidence acceptance 124 results
(`evidence/v2/accepted/2b1f2463…`; 121 carried + 3 new).

Decision: **PASS**.

## 1. Consumption states (governance §4.2)

- VM-D123 Deformable DETR: AUTHORITY_CONSUMED. arXiv abs verified
  (2010.04159, ICLR 2021 Oral) + HTML body consumed: slow-convergence/limited-
  resolution motivation, small sampling set around a reference point, multi-scale
  without FPN, 10x fewer epochs, small-object gains, code release. Card claims
  1-3 + limitation are source-local; ICLR Oral stated.
- VM-D124 DAB-DETR: AUTHORITY_CONSUMED. arXiv abs verified (2201.12329,
  ICLR 2022) + abstract/body consumed: 4D box-coordinate queries, layer-by-layer
  dynamic updates, explicit positional priors, soft-ROI-pooling cascade reading,
  45.7 AP R50-DC5/50ep. Card claims 1-3 + limitation source-local. NOTE: a wrong
  candidate locator (2206.03627, an astrophysics paper) was caught and corrected
  to 2203.01305-class verification discipline before intake; no wrong bytes entered.
- VM-D125 DN-DETR: AUTHORITY_CONSUMED. Identity verified (2203.01305, CVPR 2022
  Oral; TPAMI 2024 extended) + CVPR open-access body consumed: matching-instability
  diagnosis, noised GT box/label reconstruction with attention-mask leakage control,
  DAB-DETR-based evaluation (+1.9 AP, parity at ~50% epochs), generality to
  Deformable DETR/Anchor/Faster R-CNN/Mask2Former. Card claims 1-3 + limitation
  source-local; denoising is query-denoising training, not diffusion denoising.
- VM-D011 detector-DINO: AUTHORITY_CONSUMED (prior) + RE-READ completed, NOT
  recollected. DINO body (§§abstract/1-3) verified to state: design based on
  DN-DETR + DAB-DETR + Deformable DETR; dynamic anchor boxes refined step-by-step
  (DAB-following); deformable attention for efficiency; contrastive denoising,
  mixed query selection, look-forward-twice as DINO's own improvements (+6.0/+2.7
  over DN-DETR at 12/24 epochs). Existing card intact (claim-level verified).
- No AUTHORITY_NOT_FOUND / RETRIEVAL_FAILED / CAPTURED_BUT_UNCONSUMED among the
  four material authorities. No generic placeholder text in new cards.

## 2. Statuses

All three new cards VERIFIED via the normal contract (canonical
`validate_evidence_card` + acceptance validation): 119 VERIFIED / 5 PARTIAL held
(116 + 3 new VERIFIED; PARTIAL 5 unchanged). No forced status.

## 3. Authorization

Materiality, Completeness (VM-O02), Selection authorized on this consumed basis.
Architecture remains unauthorized by this review. No Human Gate decision fabricated.
