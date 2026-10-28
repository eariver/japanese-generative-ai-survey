# r8 P2-01 — historical pre-contract Tree SHA supersession (additive provenance, no fixed-manifest edit)

Date: 2026-10-27 JST. Sidecar-only. Fixed r8 artifacts are NOT modified.

## Bad field (immutable original preserved)

- File: `sources/2026-W43/execution/core-free-preview-r8/build-manifest-r8.json`
- Git blob: `227dbabb2e97f1309e70cf311ad9b5d0da97ce61`
- Raw SHA256: `c01c4da4d5bac99f291486530e79f762c19d0d6504ada6ea2d9dbb1d980d622c`
- Introduced in commit: `953a9d331972fdae237da4bd0f1019b17168a118` (r8 implementation, parent `88a6ffbb1…`)
- Field: `pre_contract_tree = "2429f675db817cc38333182734ed6338e1abc68"`
- Defect: 39 hex characters — NOT a valid Git tree identifier (Git SHA1 hex requires 40 chars). Missing one `f` after `6338`.

## Correct HEAD → Tree (verified, not from text alone)

- Actual pre-contract W43 HEAD (contract §0 + Git history): `be17e9944818442181975fa66b51912d2e7db8d8`
- Local verification (read-only):
  - `git cat-file -p be17e9944818442181975fa66b51912d2e7db8d8` → `tree 2429f675db817cc38333182734ed6338f1eabc68`
  - `git rev-parse be17e9944818442181975fa66b51912d2e7db8d8^{tree}` → `2429f675db817cc38333182734ed6338f1eabc68` (40 chars)
- GitHub Git commit API (independent of local text):
  - `gh api repos/eariver/japanese-generative-ai-survey/git/commits/be17e9944818442181975fa66b51912d2e7db8d8 --jq '{sha, tree.sha, parents}'`
  - Actual response (2026-10-27): `{"sha":"be17e9944818442181975fa66b51912d2e7db8d8","tree":"2429f675db817cc38333182734ed6338f1eabc68","parents":["3b1178ff5140ff03f4291701c346a6329a228a1b"]}`
  - Correct Tree: `2429f675db817cc38333182734ed6338f1eabc68` (40 hex chars; diff vs bad = insert `f`: `6338e1…` → `6338f1…`)

## Scope (precise)

- ONLY the `pre_contract_tree` metadata string in `build-manifest-r8.json` is malformed. No other manifest field is corrected here.
- Fixed r8 subject remains valid and unchanged:
  - HEAD `953a9d331972fdae237da4bd0f1019b17168a118` / Root Tree `dfafff50c946e3d0abc051eb419797de283b192a`
  - PDF `abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72` (487351B, 22 A4)
  - TeX `4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d`
  - Log `2242237a2533507e5cc28f27794c6eed23d9d58c2cc97b3a0ec79d21eafeb424`
- Do NOT silently edit the fixed manifest, TeX, PDF, checker, or page QA. Consumers must read this sidecar alongside the original manifest. A future edition (not r8) may carry a corrected manifest copy; r8 stays byte-identical for audit-pin stability.
