# Deferred Core process-gap candidate (execution-local; NOT fixed this run)

Title: `no formally supported Evidence-correction rewind from post-Architecture states
without passing through Publication Preview`

## Gap

- `request_*_revision` requires the gate's lifecycle (`ARCHITECTURE_ESTABLISHED` /
  `RELEASE_CANDIDATE`); `invalidate_pending_gate` requires a pending gate + zero Human
  records; forward advance cannot go backward. Empirically probed this run (fail-closed,
  zero writes; see `reentry-analysis.md`).
- The designed cross-gate path assumes Evidence defects surface at Publication Preview.
  A factual Evidence defect confirmed at DRAFT_COMPLETE (pre-validation) can only re-enter
  by (a) advancing through validation/TeX/PDF to RELEASE_CANDIDATE first (wasteful), or
  (b) an Owner Exception, or (c) hand-editing state (forbidden by production discipline).
- Related deferred defect (unchanged, still open): `mixed-placement synthesis package
  cannot consume Architecture-authorized cross-package Evidence under current frozen
  Draft validator` (see prior run `content-revision-r4-20261004/core-defect-candidate.md`).

Shared Core (`scripts/`, `config/`, `schemas/`, workflows, docs) UNCHANGED by this run.
