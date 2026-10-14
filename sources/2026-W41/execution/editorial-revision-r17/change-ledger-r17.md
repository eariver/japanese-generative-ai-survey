# W41 r17 change ledger (actual JSON diffs; mechanical verification)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-14 JST
Authority: `SOL_W41_R16_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_READER_ACCURACY_REPAIR`
Convention: Before = r16 proposal text; After = r17 proposal text (verified by
programmatic block-text diff). Version/runner bumps (v16.0→v17.0) excluded.
r16 files preserved unchanged (no overwrite).

Proposal SHAs (v17.0):

- P1 `f30b4c1afa2d…` (16 blocks, prompt-length clarification), P2 `296d6eeecdf9…` (17, NO_BODY_CHANGE),
  P3 `3b18bf4f3253…` (22, NO_BODY_CHANGE), P4 `03875d88d188…` (7, NO_BODY_CHANGE),
  P5 `714134390b1b…` (19, NO_BODY_CHANGE), P6 `c6e448e51676…` (13, NO_BODY_CHANGE).
- Synthesis input `b9baa39dcec5…`, result `df0f020d0670…`.
- Preview `ddb0145ad48b…` (67 paras, 16398 body chars, 5 tables).

## Carried without body change (verified zero body diff r16→r17)

- P2, P3, P4, P5, P6: headline/deck/blocks identical. NO_BODY_CHANGE (version bump
  only). Validation: draft-check PASS. Bib title fixes are NOT grounds for body
  regeneration (titles live in `references.bib`, not in article prose).

## Changed in r17 (M-01 only; P1 blocks p5/t1/p9/p12)

### M-01 / P1/p5 / BEFORE→AFTER / reason: price-boundary condition clarification

- Before: `料金設計の要点は10万tokenを境とする二段階制で…10万以下では…10万超では…`
- After: `料金設計の要点は1リクエストの入力prompt長による二段階制で…
  1リクエストの入力prompt長が10万token以下の場合（Prompt ≤100k tokens）、…。
  1リクエストの入力prompt長が10万tokenを超える場合（Prompt >100k tokens）、…。
  境界を決めるのは各リクエストのprompt長であり、月間累積使用量や出力token長、
  タスク全体の累積消費量ではない。また10万tokenを境として累進的に一部分だけ
  高額化する読み方もしない。`
- Numbers unchanged (Input $0.10/$0.50, Output $0.50/$2.50, Cache read
  $0.01/$0.05, 5m Cache write $0.125/$0.625; Sonnet $0.20→$0.10).
- Source: announcement pricing table (S1/r17 supplement: overview spec page
  re-verified 2026-10-14, `for prompts up to/over 100,000 tokens`).
- Audit ID: M-01. Verdict: RESOLVED.

### M-01 / P1/t1 / BEFORE→AFTER / reason: same (column headings unified)

- Before Haiku price fragment: `10万以下は…、10万超は…` (no column labels).
- After: `Prompt ≤100k tokens（10万token以下）は…、Prompt >100k tokens
  （10万token超）は…。境界は各リクエストのprompt長で決まる。`
- Numbers unchanged. Source: same. Audit ID: M-01. Verdict: RESOLVED.

### M-01 / P1/p9 / BEFORE→AFTER / reason: status-line consistency

- Before: `Haiku側は二段階料金表（100万token当たりの4区分）と…`
- After: `Haiku側は入力prompt長による二段階料金表（100万token当たりの4区分）と…`
- Source: same. Audit ID: M-01. Verdict: RESOLVED.

### M-01 / P1/p12 / BEFORE→AFTER / reason: guidance consistency

- Before: `自タスクのtoken量がHaikuの10万token境界のどちら側に該当するかを確認し、…`
- After: `1リクエストの入力prompt長が10万token以下か超えるかを確認し、…`
- Table-estimate vs individual-bill distinction kept. Source: same.
- Audit ID: M-01. Verdict: RESOLVED.

## Coverage note

- must_cover 27/27 and boundaries 42/42 preserved (P1 pricing substance still maps
  P1 must-cover[2]; no requirement dropped/invented).

(End of file)
