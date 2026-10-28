# Handoff — `MUSE_W43_PUBLIC_RELEASE_EXACT_BYTES_VERIFIED_COMPLETE` (2026-10-28)

## 1. Public release (verified, not merely listed)

- Release: https://github.com/eariver/japanese-generative-ai-survey/releases/tag/weekly/2026-W43
  tag `weekly/2026-W43`, title `Japanese Generative AI Technical Survey — 2026-W43`,
  published 2026-10-28T00:43:03Z by github-actions[bot].
- Asset `Japanese_Generative_AI_Technical_Survey_2026-W43.pdf`, downloaded and hashed:
  SHA256 `b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165`,
  486967 bytes — byte-identical to the Human-approved PDF.
- Release workflow run: https://github.com/eariver/japanese-generative-ai-survey/actions/runs/40610449934
  (conclusion FAILURE on a post-publish tooling bug; Release itself created +
  exact-byte verified by the workflow before the failure — see defect record
  `execution/defects/w43-release-workflow-validate-state-defect-20261028.md`).

## 2. Provenance closure (frozen builders, normal PR)

- Merge PR #573 (work → main, history-preserving): merge commit `90b39359e`,
  main unmoved before merge (`041a08df…`), zero protected-path changes,
  all checks PASS, FROZEN State + PDF `b09fd181…` verified on merged main.
- Provenance branch `release-record/2026-W43-40610449934` (from `90b39359e`):
  frozen `merge-verification-v2.json`, `release-record-v2.json` (RELEASED,
  release URL bound), `orchestration/v2/checkpoints/FROZEN.json`,
  `production-state.json` RELEASED / COMPLETE (all 12 checkpoints passed),
  `validate_agent_state` VALID, PDF unchanged.
- Provenance PR: (this PR). Merge it after checks; final main HEAD/Tree are the
  resulting merge commit, read back post-merge.

## 3. Authority chain (all pins re-verified at terminal)

- Human GO → approval `publication-preview:2026-W43:f9abcae4b07d24c79a6`
  (file `af676842…`, run 4060848059, bot `bfc777116`).
- Trusted Freeze attempt run #40608878000 failed CV2-DM-002 (evidence preserved);
  W43-only wrappers → FROZEN (commit `2f6966a87`); shared Core untouched.
- Candidate `b006f6df…` → PDF `b09fd181…` (486967B, 22p); General
  `GENERAL_W43_EQUIVALENCE_PASS` (P0 0/P1 0) bound to these bytes.
- Baseline r8 proof `abd5b99b…` untouched and NOT the release asset.
- Reviewed main `041a08df…`/`a134dc36…`; frozen Core `774dd39a…`/`cd46a6f7a…`.

## 4. Terminal

`MUSE_W43_PUBLIC_RELEASE_EXACT_BYTES_VERIFIED_COMPLETE` once this provenance
PR is merged and main reads RELEASED / COMPLETE with the PDF above.
No meaning/byte change was ever needed; no new Human scope was consumed.
