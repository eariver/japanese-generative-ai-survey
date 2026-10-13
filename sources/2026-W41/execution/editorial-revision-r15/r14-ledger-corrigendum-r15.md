# W41 r14 ledger corrigendum (supersession by new record; r14 file preserved)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER_CORRIGENDUM`
Date: 2026-10-14 JST
Authority: `SOL_W41_R14_AUDIT_ACCEPTED / EDITORIAL_REPAIR_AND_READER_PROOF`
Supersedes: `sources/2026-W41/execution/editorial-revision-r14/change-ledger-r14.md` entry `R13-a04 / P5/p3` only
Superseded file action: PRESERVED UNCHANGED (no edit, no deletion)

## False record in r14 ledger

r14 ledger `R13-a04 / P5/p3 / BEFORE→AFTER / reason: vendor-tail dedup` states:

- Before tail `（いずれも発行元の申告値）。` (duplicates p2 intro marking)
- After: tail removed

This Before text does not exist in r13 proposal bytes.

## Mechanical truth (r13 → r14 actual)

Method: exact block-text comparison of
`editorial-revision-r13/proposals/P5/draft-result.json` vs
`editorial-revision-r14/proposals/P5/draft-result.json`
(block `p3`, all other P5 blocks except p13/t3/t1 unchanged in this comparison).

- r13 P5/p3 tail (actual):
  `…と同じ測定母集団であるとは断定しない。条件の異なる数値を一つの頑健性指標に束ねないことが正確さの条件だ。`
- r14 P5/p3 tail (actual):
  `…と同じ測定母集団であるとは断定しない。`
- Actual r13→r14 delta: deletion of final sentence
  `条件の異なる数値を一つの頑健性指標に束ねないことが正確さの条件だ。`
- r13 P5/p3 contains no tail `（いずれも発行元の申告値）。` anywhere.
  Full r13 p3 text ends with the robustness sentence above (verified by bytes).

Source: r13 P5 `ef9316b7…`, r14 P5 `b5ebe134…` (full SHA in validation reports).
Audit ID: R14-A02 scope (r13→r14 erroneous deletion).
Verdict: r14 ledger entry `R13-a04 / P5/p3` is INCORRECT and is SUPERSEDED by this record.
No other r14 ledger entries are altered by this corrigendum.

## r15 repair (this revision)

r15 P5/p3 restores the erroneously deleted sentence, yielding byte-equality
with r13 P5/p3 body text for block `p3`:

- r14 → r15 After tail:
  `…と同じ測定母集団であるとは断定しない。条件の異なる数値を一つの頑健性指標に束ねないことが正確さの条件だ。`
- Population non-identity distinction (`FPR試験と類義語置換試験の母集団・条件が同一とは断定しない`) is retained.
- Source: `evidence:2026-W41:6601f7ffad5b2624` claim-1 (tgrain).
- Verdict: RESOLVED.

Audit history is not silently corrected: r14 file remains, this file supersedes
only the identified entry.

(End of file)
