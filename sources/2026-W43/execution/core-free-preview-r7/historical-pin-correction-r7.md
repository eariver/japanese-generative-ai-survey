# Historical pin correction (r7 provenance supersession)

Immutable r6 files are NOT revised. This record supersedes two erroneous
historical pointer strings for readers of r7 and later.

## The error

`core-free-preview-r6/build-manifest-r6.json → historical_subjects`:

- `r3_print_head: "3cdf2a01b810a972ecddfaa41c3dccded55c75f9"` — WRONG
  (segment `…41c3dcc…`).
- `r3_print_tree: "17b0525fec79d5624a227f82bf7dccded55c75f9"` — WRONG
  (segment `…bf7dcc…`).

The same two corrupted strings were repeated in Muse's
`independent-sol-r6-print-semantic-visual-audit-request.PROPOSED.md`.
Live GitHub readback contradicts both (independent Sol r6 audit取值arms;
contract §1 confirms).

## Correct immutable refs (verified `git cat-file -t` + `rev-parse ^{tree}`
at execution start; chain: r3 commit → r3.5 → r4 → r5 → r6 `d8e21b8fe`)

- correct r3 HEAD: `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`
  (`…41c7dcc…`, `7` not `3`).
- correct r3 root Tree: `17b0525fec79d5624a227f82bf7c5493dd1e5b73`
  (`…bf7c54…`, `c54` not `dcc`).
- correct r3 PDF SHA256: `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`.
- correct r3 TeX SHA256: `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`.

## Scope containment

- The typos affect ONLY historical pointer strings. The r6 audit subject
  itself (HEAD `d8e21b8fe`, Tree `9ec7dd73…`, TeX `7c052f05…`, PDF
  `113b179a…`) is independently verified and NOT implicated.
- r7 manifest (`build-manifest-r7.json`) cites the CORRECT strings above and
  was hash-audited before commit (all SHA fields recomputed, see manifest).
- No `git filter-branch`/history rewrite; r6 stays byte-identical.
