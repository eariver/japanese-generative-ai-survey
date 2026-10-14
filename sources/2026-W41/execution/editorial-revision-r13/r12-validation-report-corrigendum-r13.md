# W41 r12 validation-report corrigendum (m02)

Status: `EDITION_LOCAL / CORRIGENDUM / NON_DESTRUCTIVE`
Date: 2026-10-13 JST
Target: `sources/2026-W41/execution/editorial-revision-r12/validation-report-r12.md`
(r12 files themselves are NOT modified.)

## Discrepancy

The r12 validation report recorded the proposed Synthesis Input SHA as `df0d16b6…`
with a "(see file)" qualifier. Recomputation from actual file bytes gives
`5273d76dca518eadec70ebe5398f290596ae638a8bbb87dde927f54d594e16ba`.

## Verification (recomputed 2026-10-13, read-only)

- `proposed-profile-synthesis-input.json` file-bytes SHA-256:
  `5273d76dca518eadec70ebe5398f290596ae638a8bbb87dde927f54d594e16ba`.
- `proposed-profile-synthesis-result.json` file-bytes SHA-256:
  `3e0efa8aae55…` (matches the r12 report's result SHA).
- Result-internal `basis.synthesis_input_sha256`:
  `5273d76dca518eadec70ebe5398f290596ae638a8bbb87dde927f54d594e16ba`
  (matches recomputed input SHA — input/result binding intact).

The `df0d16b6…` value corresponded to a superseded pre-fix build noted during r12
assembly and was never the committed file's hash. No Git blob SHA is involved here;
all values above are file-content SHA-256 (content-addressed artifact hashes), not
`git hash-object` blob hashes — the two must not be confused.

## Standing correction

For r12 artifacts, the authoritative Synthesis Input SHA is `5273d76d…`.
r13 reports record current r13 SHAs only (see `validation-report-r13.md`).

(End of file)
