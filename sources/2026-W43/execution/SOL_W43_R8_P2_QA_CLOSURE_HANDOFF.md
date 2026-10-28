# SOL W43 r8 P2 QA closure handoff — sidecar-only (NO new PDF)

Date: 2026-10-27 JST. Branch `weekly/2026-W43-v2-work` ONLY.
Terminal: `MUSE_W43_R8_P2_QA_SIDECAR_READY_FOR_INDEPENDENT_EXECUTION`

## Start guard (all PASS)

- Exact start HEAD `c2ea53b0ca518a8c4230161242e13a7536712879` / Tree `9d0756b758baef29651bc91603fc73c6ded9c293` — remote `ls-remote` + fetch `rev-parse` match; local was 1-behind (`953a9d33…`) → `merge --ff-only`, no reset/rebase/force/new-branch.
- Reviewed main `041a08df…`/`a134dc36…`, Frozen `774dd39a…`/`cd46a6f7a…` — match.
- Pre-contract `5bfc1483cc5e56a4d4b6fb15c34a240aab3445f`/`c8ef1a4add5eebb7e21634d4f73095a3aff4ec2d` — parent match, diff = this contract only.
- Immutable r8 subject `953a9d33…`/`dfafff50…` (PDF `abd5b99b…`, TeX `4ed553e5…`, log `2242237a…`) verified.

## P2 closures (all additive under `execution/r8-p2-qa-closure/`)

- P2-01: manifest `pre_contract_tree` 39-char typo identified; GitHub commit API confirms correct `2429f675db817cc38333182734ed6338f1eabc68`; `r8-p2-historical-tree-supersession.md` records BAD/correct/evidence/scope. Fixed manifest untouched.
- P2-02: original `N-operator-insert` baseline measured `['PROSE_FIDELITY_LOSS']` (not guessed); strict sidecar `r8-p2-negative-taxonomy-sidecar.py` (stdlib, SHA-pinned inputs) requires ALL causes — same mutant now yields BOTH `READER_META_LEAK` (controlled `編集承認ゲート通過済み` taxonomy) + `PROSE_FIDELITY_LOSS`. `SIDECAR_STRICT_PASS` 5/5 exit 0 (clean/N10/N13 incl.; N13 anchor count == 1, mutant hashes recorded). Staged-dir replay PASS. Evidence: `r8-p2-sidecar-strict-all.json` + `r8-p2-sidecar-test-evidence.md`.
- P2-03: PDF bytes + PNGs re-inspected; supersession corrects Table11 p13 (not p12 header), Table16 p17 (not p14), recap `今週の総括` p20 bottom (not p19), bib heads p21 mid-page (not p20). Matrix + image SHA in `r8-p2-physical-page-anchors.json`; notes in `r8-p2-physical-page-qa-supersession.md`. Originals untouched.

## Runbook + boundary

- `r8-independent-verification-runbook.md`: exact pins/commands for checkout + staged-dir, original 27/27+12/12, sidecar strict, PDF parse/render, font/link checks, novel-mutant requirement, NOT_RERUN labeling; connector-only audit insufficient.
- Executed (Muse) vs awaiting independent execution strictly separated (see test-evidence). No independent PASS claimed; external terminal legitimately stays INCONCLUSIVE until independent run. Human PDF Gate PENDING; ARCHITECTURE_ESTABLISHED; Draft BLOCKED. No new PDF/TeX/checker/manifest/QA edits; no r1–r7/Core/Architecture/Selection/Evidence/State/Gate writes; no Freeze/Release.
