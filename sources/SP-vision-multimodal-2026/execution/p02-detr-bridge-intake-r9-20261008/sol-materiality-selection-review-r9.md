# TS-003 P02 Bounded Bridge — Sol Materiality / Selection Review r9

Status: `SOL_MATERIALITY_SELECTION_REVIEW_R9 / PASS / AUTHORIZE_ARCHITECTURE_PREPARATION`

Date: `2026-10-08`

Run: `execution/p02-detr-bridge-intake-r9-20261008`

Reviewed state: lifecycle `SELECTION_COMPLETE`, matrix 124 rows, selection 124
assignments (121 carried + 3 new).

Decision: **PASS**.

## 1. Positive decisions (why each new item is material)

- VM-D123 Deformable DETR (PRIMARY, transition-anchor): the convergence/small-object
  repair DETR needed; DINO's stated deformable-attention/query-selection source.
  Without it, "DETR → DINO" skips the mechanism that made multi-scale DETR practical.
- VM-D124 DAB-DETR (SUPPORTING, transition-anchor): the 4D dynamic-anchor query
  formulation DINO explicitly adopts and refines layer-by-layer. Brief supporting
  treatment is proportionate: its content is consumed through DINO, not retold.
- VM-D125 DN-DETR (PRIMARY, transition-anchor): the denoising-training branch;
  DINO's contrastive denoising is an improvement on it (+6.0/+2.7 margins are
  measured against DN-DETR). Omitting it would leave DINO's "improved denoising"
  without its reference point.

## 2. Negative decisions

- No other candidate changed disposition: 121 assignments carried byte-identical
  (verified by the phase script against HEAD-committed authority).
- Conditional DETR / Anchor DETR: considered and NOT admitted. DINO cites them as
  related query-formulation work but does not claim them as design bases; the
  bounded direction explicitly excludes the full-successor taxonomy. This is a
  documented omission with reason, not an oversight.
- Diffusion-model denoising literature: out of scope by mechanism distinction
  (query-denoising training ≠ diffusion denoising); DN limitation states this.
- VM-D122 (DROP, out-of-window): untouched; NOT reused for the new intake
  (fresh VM-D123/124/125 allocated via the normal pipeline).

## 3. Grouping / compression

- The three nodes are bounded P02 transition nodes, not chapters; DINO remains the
  detector-family capstone toward Grounding DINO. Page budget unchanged (6).
- No sparse-issue compression concern: SELECTED = 124 (rich, not compressed).

## 4. Authorization

Architecture preparation authorized on these Selection semantics, P02 delta only.
No Human Gate decision fabricated.
