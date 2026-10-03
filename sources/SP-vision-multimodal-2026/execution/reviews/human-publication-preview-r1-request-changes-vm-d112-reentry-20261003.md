# Human Decision Record — Publication Preview r1 REQUEST_CHANGES (upstream re-entry to DISCOVERY_COLLECTED)

- Issue / edition: `SP-vision-multimodal-2026` (TS-003)
- Gate: `PUBLICATION_PREVIEW`, revision: `1` (first Publication Preview review; no prior publication-rN exists)
- Decision: `REQUEST_CHANGES` with upstream regeneration (NOT an approval of any kind)
- Reviewed by: `Human Owner`
- Human decision date: `2026-10-03 JST` (recorded here as `2026-10-03T12:00:00+09:00`; day-precision as given)
- Work branch: `special/vision-multimodal-2026-work`
- Reviewed repository commit: `3f3ff84331cf370743d690b3e5c78693291a8a63` (branch HEAD at decision materialization)
- Regeneration boundary: `DISCOVERY_COLLECTED`
- Core v2 Freeze: remains in force (no Core change authorized)

## Actual Human decision (verbatim)

> TS-003について、VM-D112 Agentic Video Understandingを正式なDiscovery / Screening / Evidence pipelineへ投入するためのedition-local governed re-entryを承認する。

ただし、以下は絶対条件である。

> **Survey Production Core v2のFreezeは解除しない。**

## Scope clarification (faithful record, no new decision inferred)

This Human approval authorizes **TS-003 edition-local re-entry only**. It does
not authorize any of the following, and none of them is claimed here:

- Publication Preview APPROVED
- Architecture APPROVED (old r2 approval is to be reopened per Core semantics, not reused)
- Freeze APPROVED
- Release APPROVED
- Core v2 Freeze release, Shared Core changes, Core script/schema/config/validator/contract changes, Core repair on main, or frozen Core artifact rewrites

## Requested changes carried to the operator request

- Bounded admission/disposition of VM-D112 Agentic Video Understanding through the formal pipeline (Discovery supplement → Screening → Evidence → Materiality/Completeness → Selection → Architecture)
- Preserve all accepted existing technical scope unless regeneration requires deterministic rebinding
- Preserve Core v2 Freeze (frozen Core code untouched; no validator change or bypass)
- Stop at fresh Human Architecture Review (no reader r15 / TeX / PDF / Publication Preview approval / Freeze / Release in this pass)

## Provenance

- This record is the `review_reference` for operator request `ts003-vm-d112-cross-gate-reentry-20261003`.
- Record created edition-locally by the Work execution role as a faithful transcription of the already-given Human decision quoted above. No decision was inferred, and no additional approval was requested.
