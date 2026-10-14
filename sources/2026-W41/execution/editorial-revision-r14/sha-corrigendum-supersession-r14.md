# SHA corrigendum supersession (R13-A02)

Status: `SUPERSEDES_R13_CORRIGENDUM / R12_ARTIFACTS_UNCHANGED`
Date: 2026-10-13 JST
Supersedes (preserved, not overwritten):
`sources/2026-W41/execution/editorial-revision-r13/r12-validation-report-corrigendum-r13.md`.
All values below were recomputed by Muse from actual file bytes on 2026-10-13
(read-only `sha256sum`); the independent-audit table (§5.1) matches on all four lines.
File-byte SHA-256 and Git blob SHA are distinct and are not confused here.

## 1. r12 Validation Report actual record

File: `sources/2026-W41/execution/editorial-revision-r12/validation-report-r12.md` (tail):

- Input：`5273d76d…`
- Result：`3e0efa8a…`

## 2. r12 artifacts actual file SHAs

- `editorial-revision-r12/proposed-profile-synthesis-input.json`:
  `afdc2b63fdbf17600a07a1f1f557cb016b80551dc22916efc5f08463108477f3`
- `editorial-revision-r12/proposed-profile-synthesis-result.json`:
  `42bf700e5f9a4fbf74da9bdf7627101899a5f168cba705e54f56a91c74d10f3b`

## 3. r12 Result-internal Input reference

- `basis.synthesis_input_sha256` inside the r12 Result:
  `afdc2b63fdbf17600a07a1f1f557cb016b80551dc22916efc5f08463108477f3`
- Matches the actual r12 Input file SHA: input/result binding intact.

## 4. r13 Corrigendum errors (superseded record's misstatements)

- (a) Claimed the old report recorded `df0d16b6…`. The actual report (§1) records
  `5273d76d…` — the `df0d16b6…` claim does not match the report on GitHub.
- (b) Asserted `5273d76d…` as the authoritative r12 Input SHA. The actual file SHA
  (§2) is `afdc2b63…` — the report's value was the stale one, not the correction.
- (c) The "superseded pre-fix build" explanation for `df0d16b6…` is withdrawn:
  no evidence for it could be produced; it is not restated as fact here.

## 5. r13 artifacts actual SHAs + internal refs (unchanged, for contrast)

- r13 Input: `77eee03d3e5997bcc0ee9343ecddf29b4c5004c48b29ae581557dbbd47ee7e66`
- r13 Result: `7435346d13232cd9d07517f758b8ea8259e1ea049f63706109b850d3fe154667`
- r13 Result-internal Input ref: `77eee03d…` (matches actual Input — binding intact).

## 6. r14 artifacts actual SHAs + internal refs (this revision)

- r14 Input: recorded in `validation-report-r14.md` (recomputed at build time).
- r14 Result: recorded in `validation-report-r14.md` (recomputed at build time).
- Result-internal Input ref verified to match the actual r14 Input file SHA.

## Standing

The erroneous subject is the audit-trail paperwork (r12 report line + r13 corrigendum),
not the r12/r13 Synthesis artifacts themselves: both generations bind Input↔Result
correctly, and that PASS is retained. No Synthesis file was modified by this correction.

(End of file)
