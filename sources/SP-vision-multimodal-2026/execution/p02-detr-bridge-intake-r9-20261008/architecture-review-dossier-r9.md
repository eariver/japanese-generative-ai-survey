# TS-003 Human Architecture Review Dossier — r9 candidate (P02 bounded completeness repair)

Status: `ARCHITECTURE_REVIEW_R9_PENDING / DOSSIER_COMPLETE / NO_APPROVAL_RECORDED`

- Edition: `SP-vision-multimodal-2026` (THEMATIC / LONGFORM_SPECIAL)
- Revision: Architecture r9 candidate (`architecture-v2.json`, status PROPOSED)
- Lifecycle: `ARCHITECTURE_ESTABLISHED`; gates: architecture_review `pending`,
  publication_preview `pending`; no active approval (r8 approval superseded by
  Core cross-gate reopen; r1–r8 review/approval records preserved as history).
- Reviewed bytes: the exact pushed head of branch
  `special/vision-multimodal-2026-work` for run
  `execution/p02-detr-bridge-intake-r9-20261008` (HEAD/Tree reported in the run's
  final report; verifiable via the branch head).
- Prior approved authority: r8 (`56658960dff0269a89bf38d5b3027147dea7159f5c15337ff8a74d6ea7e4d773`),
  preserved as immutable history (`gates/reviews/architecture-r8.json` +
  `approvals/architecture-r8.json`).

## 1. Research coverage (Sol Discovery completeness review r9: PASS)

- Source-intake surfaces exercised: arXiv abs + full-body HTML for the three
  bounded primaries; DINO related-work re-read; negative-space sweep bounded to
  DINO's explicit "based on DN-DETR, DAB-DETR, and Deformable DETR" statement.
- Discovery: 125 records (122 carried byte-identical + VM-D123 Deformable DETR,
  VM-D124 DAB-DETR, VM-D125 DN-DETR). VM-D122 NOT reused; canonical counter order
  kept (no hand-edited IDs).
- Residual gaps: Conditional/Anchor DETR deliberately outside (related work, not
  design bases); DINO deformable-attention use is efficiency-scoped (paper-stated).
- X/Grok intake: NOT_REQUIRED with rationale (bounded primary-paper intake).

## 2. Evidence quality (Sol authority-consumption review r9: PASS)

- Evidence acceptance `2b1f2463…` (124 results: 121 carried + 3 new).
- Status: VERIFIED 119 / PARTIAL 5 (116 + 3 new VERIFIED; PARTIAL unchanged).
- All four material authorities CONSUMED (Deformable/DAB/DN bodies read;
  DINO §§abstract/1-3 re-read, card NOT recollected, intact at claim level).
- Screening 125 (`cdf7a075…`): KEEP 116 + INSPECT 5 + MAYBE 3 + DROP 1
  (D122 DROP carried; 3 new KEEP).
- Views 124 (`8eb6c9e5…`); ledger 125 rows; completeness 14/2 with VM-O02
  SATISFIED (11 bound records: 8 carried + 3 new).

## 3. Candidate map

- 124 SELECTED (121 carried + Deformable PRIMARY / DAB SUPPORTING / DN PRIMARY,
  all `THEMATIC:transition-anchor`).
- DINO remains detector-family capstone toward Grounding DINO; DINO-name
  disambiguation preserved.

## 4. Negative-space / omission review

- Conditional DETR, Anchor DETR: omitted with documented reason (see Sol reviews).
- Diffusion-model denoising literature: excluded by mechanism distinction.
- No random expansion: exactly the 3-paper bounded family was intaken
  (Discovery/Screening/Evidence counts prove it).

## 5. Editorial thesis

Unchanged from r8: detection lineage now complete at the mechanism level —
R-CNN/Faster progression, one-stage operating points, DETR set prediction,
DETR-successor bridges (sparse attention, dynamic anchors, denoising), DINO
convergence, YOLO-World open-vocabulary bridge, with DINO-name disambiguation.

## 6. Architecture packages

- 16 packages; 15 byte-identical to r8-approved (delta guard enforced).
- P02 delta only (`architecture-r8approved-to-r9regen.diff`, 66 lines):
  +2 primary transition nodes, +1 supporting brief node, +4 must-cover
  requirements (3 bridges + DINO convergence), +4 boundaries (3 verbatim Evidence
  limitations + parallel/convergent genealogy statement), depth classes extended,
  page budget held at 6.

## 7. Page/section allocation

Unchanged (P02 budget 6 held; no inflation for the 3 records, per task §9).

## 8. Counterfactual alternatives considered

- (a) Draft-wording fix without intake: REJECTED — the gap is a genuine
  completeness defect (must-cover lineage claim vs missing authorities), not prose.
- (b) Full DETR-successor taxonomy (Conditional/Anchor DETR chapters): REJECTED —
  disproportionate; DINO does not claim them as design bases.
- (c) DINO card recollection: REJECTED as unnecessary — re-read confirmed the
  existing card already carries the predecessor margins and lineage role.

## 9. Known limitations / risks

- New cards bind arXiv versions as retrieved (Deformable v4, DAB v4, DN v3/CVPR);
  version-bind noted in Discovery scope limits.
- DINO deformable-attention use is efficiency-scoped; Architecture does not
  overclaim it.
- rev5 Draft (fresh-121-r8-rev5) remains on disk as historical artifact only;
  draft checkpoint provenance cleared — it is NOT regenerated authority and no
  rev6 was produced. Queued rev5 review corrections stay deferred.
- Coverage Freeze stays active except this explicitly recorded bounded exception
  (`coverage-freeze-exception.md`).

## 10. Sol findings and recommendation

- Sol blocking findings: none. Non-blocking: none material.
- Sol reviews r9 (discovery / evidence-consumption / materiality-selection /
  architecture): all PASS, in-run.
- Recommendation: Human APPROVED (continue to fresh Draft addressing queued rev5
  corrections) or REQUEST_CHANGES with a pre-Architecture boundary. Sol does not
  approve; the worker recorded no approval, generated no Draft, started no
  publication work.

## 11. Human decision options (only now that the above is presented)

- `APPROVED` — record against the durable reviewed commit via the Human Gate
  mechanism; then continue to drafting.
- `REQUEST_CHANGES` — supply requested changes + one allowed pre-Architecture
  regeneration boundary; Core invalidates only affected downstream authority and
  returns to that boundary.
