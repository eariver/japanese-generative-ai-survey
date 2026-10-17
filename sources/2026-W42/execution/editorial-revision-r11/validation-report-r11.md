# W42 r11 validation report (frozen validators + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite.

## Frozen CLI validations (all PASS, real receipts)

- `survey_drafting_v2_base.py draft-check` (canonical package × r11 proposal): P1–P7 all `{"passed": true, "errors": []}` (schema, identity, stable refs, attribution, must-cover, boundaries).
- Proposal SHAs (v11.0, REVISED): P1 `d7887f24…` (13p), P2 `aca76495…` (12p), P3 `39d259c6…` (13p), P4 `f9407cd3…` (13p), P5 `f169eee7…` (11p), P6 `d6f81af2…` (10p), P7 `c65c2737…` (10p). Tables 7, notes 7.
- `synthesis-input` built via frozen CLI from the 7 proposal pairs (embeds current proposal SHAs); proposed synthesis result written; `synthesis-check` `passed: true`.
- `validate_agent_state`: PASS (checked during bridge pre-work; State DRAFT_COMPLETE preserved).

## Reader preview fidelity

- `reader-preview-r11.PROPOSED.json`: 82 paragraphs / 20,082 body chars / 7 tables / 7 notes; zero CLAIM_BOUNDARY blocks; zero machine-trace fragments (scan: `AUTHORITY_CONSUMED`, `No r7 finding`, `CLAIM_BOUNDARY`, checksums, Hangul/simplified ghosts — all clean; one documented exception: `SRFT` as named method).
- Body equality vs proposals: programmatic — preview texts are exact copies of proposal visible blocks (same build script, same source objects); `block-diff-r11.json` records old→new mapping.

## Canonical invariants (all preserved)

- `production-state.json`: DRAFT_COMPLETE, architecture approved, publication pending (SHA unchanged by this unit; verified at commit).
- Draft checkpoint `ARCHITECTURE_ESTABLISHED.json`: unchanged.
- Architecture approval + review index + r1 record/snapshot: unchanged.
- Canonical Draft Results/Packages/Synthesis (v10.0): SHAs unchanged (read-only inputs to draft-check).
- Accepted Evidence/Views/Materiality/Selection/Architecture: untouched. No TeX/PDF. Publication Preview not started.

## Proposal chain of custody

- Basis of every proposal = live canonical `draft-package.json` SHA (byte-identical, verified by draft-check `basis` binding).
- Runner metadata: `muse-w42-r11-editorial-repair-proposal`, 2026-10-18T02:30:00Z.
- Archive note: builder scripts live outside the repo (`/tmp`, not committed); reproducible inputs are the committed `interactive-drafting-synthesis-r10.json` (canonical) plus this ledger's before/after record.

(End of file)
