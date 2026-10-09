# TS-003 r9 — Sol Evidence Authority-Consumption Review r9b (fresh)

Status: `SOL_EVIDENCE_CONSUMPTION_REVIEW_R9B / PASS / AUTHORIZE_MATERIALITY_SELECTION`

Date: `2026-10-08`

Run: `execution/r9-evidence-attribution-closure-20261008`

Reviewed authority: Evidence acceptance 124 results
(`evidence/v2/accepted/6b55033d…`; 120 carried + 4 corrected).

Disposition: **PASS**. This review SUPERSEDES
`p02-detr-bridge-intake-r9-20261008/sol-evidence-consumption-review-r9.md`, whose
finding that VM-D123/124/125 claims 1–3 are all source-local was incorrect. The
old file remains untouched as immutable history; it is NOT active authority
(all lifecycle checkpoints now bind the corrected acceptance).

## 1. Reading ≠ binding (the defect class)

The prior run correctly read all four primary bodies but bound three
DINO-authored inheritance statements to predecessor-only sources. This review
verifies the complete tuple per claim: text / class / source_ids / registered
source / context / subject / source support.

## 2. Per-claim verification (corrected acceptance)

- VM-D011 detector-DINO (src-1 = DINO paper 2203.03605):
  - claim-1 AUTHOR_CLAIM/src-1/ev-vmd011 — capstone numbers (+6.0/+2.7 over
    DN-DETR; 63.2/63.3 SwinL). Source-local (DINO abstract/results). PRESERVED.
  - claim-2 INFERENCE/src-1/ev-vmd011 — Grounding-DINO-base role + name rule.
    PRESERVED.
  - claim-3 AUTHOR_CLAIM/src-1/ev-vmd011 — NEW. DINO-authored predecessor lineage
    (based on DN/DAB/Deformable; dynamic anchors DAB-line; denoising DN-line;
    deformable attention + query selection Deformable-line; contrastive denoising /
    mixed query selection / look-forward-twice as DINO's own). Every element was
    verified in the DINO body (§§abstract/1/3 related-work + design statements
    quoted in the run record). Source-local. ADDED.
- VM-D123 Deformable DETR (src-1 = 2010.04159):
  - claim-1/claim-2 AUTHOR_CLAIM/src-1 — motivation/mechanism/convergence.
    Source-local. PRESERVED.
  - claim-3 AUTHOR_CLAIM/src-1 — REWRITTEN to Deformable-native machinery only
    (2D reference points, two-stage variant, iterative refinement); the
    "feeds DN/DAB/DINO" tail and DINO context removed. No DINO-dependent
    AUTHOR_CLAIM remains. Source-local.
- VM-D124 DAB-DETR (src-1 = 2201.12329):
  - claim-1/claim-2 AUTHOR_CLAIM/src-1 — 4D queries/updates/priors; cascade
    reading + 45.7 AP. Source-local. PRESERVED.
  - claim-3 REMOVED. No `directly feeds DINO` on DAB source. That statement now
    lives on VM-D011/claim-3 (DINO paper as source).
- VM-D125 DN-DETR (src-1 = 2203.01305):
  - claim-1/claim-2 AUTHOR_CLAIM/src-1 — instability diagnosis/denoising
    mechanism; DAB-based +1.9 AP/generality. Source-local. PRESERVED.
  - claim-3 REMOVED. No DINO margins/inheritance on DN source. Those facts now
    live on VM-D011/claim-3. Query-denoising ≠ diffusion distinction preserved
    in the limitation.

## 3. Tuple audit result

- Every AUTHOR_CLAIM's source_ids resolves to a registered source whose body
  supports the claim text; no context pointer references a source absent from
  source_ids (full-surface scan in the run audit).
- Statuses: revalidated through the normal contract, not forced — 119 VERIFIED /
  5 PARTIAL held (no status change was needed; attribution was the defect, and
  corrected cards pass as VERIFIED).
- No AUTHORITY_NOT_FOUND / RETRIEVAL_FAILED / CAPTURED_BUT_UNCONSUMED among the
  four material authorities.

## 4. Authorization

Materiality, Completeness (VM-O02), Selection authorized on this corrected basis.
Architecture preparation authorized with r9 semantics preserved. No Human Gate
decision fabricated.
