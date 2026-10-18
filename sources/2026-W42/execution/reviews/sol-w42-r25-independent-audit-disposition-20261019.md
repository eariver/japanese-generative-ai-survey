# J-GAS W42 r25 — Sol disposition on independent print audit

Date: 2026-10-19 JST
Status: `SOL_EDITORIAL_DISPOSITION / INDEPENDENT_W42_R25_PRINT_AUDIT_REQUEST_CHANGES_ACCEPTED / R26_BOUNDED_READER_FIDELITY_REPAIR / NONCANONICAL_ONLY`

## Reviewed authority

Independent one-shot read-only report is preserved **verbatim including final newline** in the adjacent `independent-w42-r25-print-audit-REQUEST_CHANGES-20261019.md` (uploaded by user as `20261019013100_SolReview.md`; exact original SHA256 `181f6620350108f1fb8de9ca1eb01d1e15a2ea719bab91fb10176f45c1db78c7`; Git blob `ce7f45cf07f3747eb8c3d8a75adbc250d7e64fbc`). Independent auditor checked PDF/TeX/log hashes and all 21 page PNGs. Scope: fixed r25 HEAD `b992685a66ccfd9eef3073a448771d2f224bea9c`, Tree `d552721744c4e8b6e71adf0bdb90753f36036066`.

This Sol independently refetched r18 Reader (Git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`) and r25 TeX (`54aca5f2d9bb3ae427dbd04939278a1bf3e78e94`). BOTH independent MAJOR findings are reproduced:
- **BLOCKER-01**: r18 P2 Table2 LFM2.5 `t2-11`: `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）`; r25 table: `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万ドル`. The latter drops the legal-entity turnover qualifier.
- **BLOCKER-02**: r18 P3 Table3 Nemotron3.5 `t3-18`: `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`; r25 table: `OpenMDW：Super VL未開封、OSI主張不可、EXO不採用`. A provenance status is materially rewritten.

Both altered strings ALSO occur in `execution/diagnostic-r22/main.tex` (Git blob `6099efb03886f8c3262163f98e60cb21d6fd6d6a`), so they PREDATE r25 multicol. Never falsely attribute those content differences to r25's layout redesign.

## Editorial decision

**REQUEST_CHANGES accepted.** The independent auditor confirmed r25's physical 7-table/21-page output has no major geometry flaws, and the old r22/r24 table splitting, caption orphaning, clipped Decider and sparse terminal page are corrected. p03/p11/p13 whitespace is an aesthetic limitation, not a present blocker. Main and Frozen Core remain unchanged; `production-state.json` remains `DRAFT_COMPLETE`, Architecture Human Review r1 `approved`, Publication Preview `pending`. Formal Architecture page plan 26.5 body / 28 target / 30 maximum has NOT been revised; Option B 17.0 planned body and Sol issue21/max23 are non-Gate editorial proposals.

Root cause is unreliable **r18 Reader→diagnostic TeX cell fidelity**, not physical page placement: r22 onward inherited a shortened baseline and incorrectly claimed table-cell identity by diff transitivity. Next r26 must restore exact two strings and independently check ALL cells from r18 source (no inherited transitivity), while retaining working r25 multicol architecture and re-rendering/visually checking all pages. No canonical Reader/Architecture/State/Gate/Publication/Freeze/Release authority. Next contract: `sources/2026-W42/execution/instructions/2026-10-19_muse-w42-r26-two-cell-reader-fidelity-and-print-regression.md`.
