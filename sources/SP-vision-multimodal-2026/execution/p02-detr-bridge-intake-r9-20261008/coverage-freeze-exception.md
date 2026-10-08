# Coverage Freeze — bounded exception record (P02 DETR-successor bridge, r9)

Status: `COVERAGE_FREEZE_ACTIVE_WITH_SINGLE_RECORDED_EXCEPTION`

- Freeze baseline: unchanged (no frozen historical releases touched; `specials/`,
  `surveys/` trees untouched — verified in the r9 audit).
- Exception (this run only, `execution/p02-detr-bridge-intake-r9-20261008`):
  three pre-cutoff primary papers admitted as bounded P02 transition nodes under
  Human-bounded revision direction (`bounded-revision-authorization.md`):
  - VM-D123 Deformable DETR (arXiv:2010.04159)
  - VM-D124 DAB-DETR (arXiv:2201.12329)
  - VM-D125 DN-DETR (arXiv:2203.01305)
- Counts: Discovery 122 → 125; Screening 122 → 125; Evidence 121 → 124;
  Selection 121 → 124; Materiality ledger 122 → 125 rows. No other lane touched.
- VM-D122 NOT reused. No freshness intake. No random additions.
- Freeze resumes in full after this exception: any further intake needs a new
  Human-bounded direction.
