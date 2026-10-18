# W42 r15 validation report (r15.1 rebuild; frozen validators + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition. No TeX/PDF rebuild (STOP per readiness).

## Frozen CLI validations (all PASS, real receipts)
- `survey_drafting_v2_base.py draft-check` (canonical package × v15.1 proposal): P1–P7 all `{"passed": true, "errors": []}` after expand, ref-fix (t1-21 claim-6 MIXED; t6-25 Rosalind refs), and flow reorder. Re-ran after every mutation.
- Proposal SHAs v15.1 REVISED: 136 paragraphs / 24,162 paragraph-only chars / 27,415 body-PTN chars / 7 tables / 7 notes. Per-chapter paragraph chars P1 3,568 / P2 3,321 / P3 4,570 / P4 3,793 / P5 2,827 / P6 3,410 / P7 2,673.
- Counter reconciliation (same definitions): r11 82/17,004 → r12 92/18,165 (+10/+1,161) → r13 103/19,193 (+11/+1,028) → r14 112/20,479 (+9/+1,286) → v15.0 122/21,575 (+10/+1,096) → v15.1 136/24,162 (+14/+2,587; +24/+3,683 vs r14). Body-PTN: 20,082 / 21,281 / 22,315 / 23,601 / 24,697 / 27,415.
- `synthesis-input` rebuilt via frozen CLI from 7 updated pairs (output to /tmp + copy over edition-local file; CLI refuses overwrite); `proposed-profile-synthesis-result.json` v1.1 (input-SHA re-bound, runner re-stamped); `synthesis-check` `passed: true`.
- Production State read-only check: `production-state.json` lifecycle `DRAFT_COMPLETE`, architecture `approved`, publication `pending` (verified unchanged at commit; no formal stage validation run — no transition requested).

## F01/F02 gates + duplicates (regression + repair)
- F01 RESOLVED (held): Earth Pro negative 50.8±1.7→47.6±2.7 (verified ±2.7, NOT ±2.5) + model-dependent planner reading; programmatic scan clean.
- F02 RESOLVED (held): 0 non-http URLs; repo discrepancy side-by-side + 44-vs-45 gap added; withheld tests never called open.
- Duplicates ELIMINATED (extends F-06): t1-17/t1-21, t4-04/t4-21, t7-03/t7-16 verbatim + t2-18/t2-21, t5-06/08-vs-t5-19 near-dups all rewritten distinct; t6-25 wrong-ref fixed (wet-lab → Rosalind claims). F-06 P6 merges (t6-09/t6-16) held.
- M01 (acceptance length + Table-8 conditions + greedy-vs-sampled honesty) held; M02 (denominator separation) held; M06 (timestamp notice) held. No EXO scores, no AA ranks, no X-only allegations. Translationese swept.

## Reader preview fidelity
- `reader-preview-r15.PROPOSED.json/.md` regenerated from v15.1 proposals: 136 paras / 7 tables / 7 notes; zero CLAIM_BOUNDARY; zero machine-trace/Hangul/Simplified ghosts; single documented `SRFT` exception retained from r12.
- Citation ledger: 163 → 177 rows (14 new blocks inherit template keys; t1-21 narrowed to claim-6 family; t6-25 Rosalind B51/B52/B86/B87). Bibliography keys unchanged (88 keys; S7-S10 sidecar URLs live in readings, not bib). TeX body NOT regenerated (no render); prior main.tex cites remain v15.0.

## TeX/PDF proof status (explicit)
- `preview-r15/main.pdf` (18pp, v15.0 content) retained byte-identical as layout reference ONLY. It does NOT contain v15.1 blocks and is NOT a v15.1 proof. No new PDF per contract STOP branch + user sufficiency rule (26.5pp plan not met; ~19-20pp projected).
- No `main.log`/`PNG`/`manifest` regeneration for v15.1 (nothing to verify visually). If Sol authorizes a v15.1 proof render, TeX must be regenerated from v15.1 reader + 177-row ledger with full LuaLaTeX + PNG + manifest procedure.

## Canonical invariants (all preserved; verify at commit)
- `production-state.json`: DRAFT_COMPLETE, architecture approved, publication pending (SHA unchanged).
- Draft checkpoint `ARCHITECTURE_ESTABLISHED.json`, approval, review index, r1 record/snapshot: unchanged.
- Canonical Draft Results/Packages/Synthesis (v10.0): unchanged (read-only validator inputs).
- Accepted Evidence/Views/Materiality/Selection/Architecture: untouched. r11-r14 proposals preserved. No TeX in canonical paths; Publication Preview not started.

## Remaining explicit unknowns (not hidden)
- Nemotron 79pp PDF bytes (S3a/S3b substitute); Maia paper annex/baseline; Vals full methodology + Z.ai rate card; HF file listings (24B/LFM, Granite/MiniCPM siblings); METR downstream; independent reruns throughout; Earth repo commit SHA (UNKNOWN recorded).
- 28pp target gap: ~6-7 body pages at measured density. Terminal `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED` stands (deepen with named primary reads vs amend plan). No silent downscope, no padding.
