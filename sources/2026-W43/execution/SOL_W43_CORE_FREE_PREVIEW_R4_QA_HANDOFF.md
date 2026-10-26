# SOL_W43_CORE_FREE_PREVIEW_R4_QA_HANDOFF

Status: `MUSE_W43_R4_PRINT_QA_INTEGRITY_READY_FOR_SOL_RECHECK`
Date: 2026-10-27. Branch: `weekly/2026-W43-v2-work` (existing only).
Sole contract: `sol-w43-core-free-preview-r4-print-checker-integrity-20261027.md`

## 0. Guards (read-only PASS, ff-only)

- Dispatch `e707379f7440d336b94908e7d56bffc6869d2f1e` / `08d6cfd0b4f45a475a490d193caaf87245f1bbf5` == origin; parent `3cdf2a01b810a972ecddfaa41c7dccded55c75f9` / `17b0525fec79d5624a227f82bf7c5493dd1e5b73` (r3 per §0); diff = contract file only.
- main `041a08df…`/`a134dc36…`, frozen `774dd39a…`/`cd46a6f7a…` verified via API+ls-remote.
- Local `3cdf2a01…` clean → fetch + ff-only → `e707379f…`. No reset/rebase/force/branch/PR/main/Core writes.

## 1. Integrity repairs (validator + accounting; print bytes fixed)

A. New `print-semantic-fidelity-check-r4.py`: single `validate()` (proj+tex, manifest ground truth, TOKEN_SUBS allowlist, TeX caption/row identity, per-claim own-row value+variant+quals in proj AND correct TeX span visible + per-claim bib URL). `or True` eliminated; count-only replaced by ordered join + anchoring. Clean `PRINT_SEMANTIC_PASS` (22 checks, exit 0).
B. 17 true negatives via SAME entrypoint on ephemeral mutants, each asserting its SPECIFIC cause: API deletion proj-only/tex-only/both; clock swap (count held); wrong scoped npm URL; JP-in-URL; qualifier stripped proj/tex separately; row delete/dup80/swap (count-held variants); header alter; NOTE-row alter; model/variant, metric number, claim-value drop (all CLAIM_ANCHOR); bib URL alter. `NEGATIVES_PASS` 17/17 exit 0. Old single-side slip-through and diff-only negatives closed.
C. `source-key-audit-r4.md` + classifier script: programmatic 19/1/13/2/1/0 (visible/machine/natural/further/unavailable/orphan), ORPHAN 0. Corrects r3 18/15/2/1/0 (tanstack-gh/npm now exact-visible via r3 repair; recap is machine-only label). GH≠npm and 404/RAW guards explicit.
D. Names match coverage; literals labeled global-supplement, anchoring proved per-row/per-table.

## 2. Outputs (NEW r4 namespace only; print fixed)

`core-free-preview-r4/` (validator + clean/negative results, classifier + audit, claim-table binding, readback/boundaries, visual-request, manifest, build notes) + this handoff + session + index append. r1/r2/r3, r3.5, Architecture/Selection/Evidence/State/Gates/main/Frozen unchanged. No TeX/PDF rebuild, no canonical PDF, no Stage/Freeze/Release. `.aux`-type byproducts: none (validator-only run).

## 3. r3 artifact standing (read back, not re-audited visually)

r3 PDF `d0fa8b56…` 483305B 22p (blob `4e016ab1…`), TeX `bb0e7e1d…` (blob `79a90d40…`), p-18 PNG blob `22bfb2df…`; local SHA256 + `pdftotext` protected-string checks pass (POST, TanStack keys, qualifiers, clocks, recap). Log/blob/texture ≠ all-page visual QA (stated in boundaries doc). Separate independent semantic + all-page visual audit still required; on media failure report `PDF_VISUAL_AUDIT_BLOCKED`.

Final HEAD/Tree via push/readback (handoff cannot self-contain hash). Commit-pinned r4 file URLs in session/final report post-push.

`MUSE_W43_R4_PRINT_QA_INTEGRITY_READY_FOR_SOL_RECHECK`
