# W41 r17 source–claim check (programmatic + editorial)

Status: `EDITION_LOCAL / AUDIT_EVIDENCE`
Date: 2026-10-14 JST
Method: official `draft-check` CLI 6/6 PASS + `synthesis-check` PASS + programmatic
audits + excerpt spot-check (changed scope only; r16-verified carry-overs retained).

## Programmatic audits (executed, all PASS)

- `evidence_refs`/modes unchanged r16→r17 for all 6 packages (P1 24 refs incl.
  Haiku claim-1; supplement S17 facts NOT encoded as Card refs).
- must_cover 27 exact-once; boundaries 42 exact-once (P1 pricing still maps
  must-cover[2]; no blanket).
- basis binds canonical package SHA + prompt SHA; synthesis input rebuilt via CLI,
  result binds new input SHA (`b9baa39dcec5…`); payload keys intact.
- No invented IDs/experiments; no disposition changes; Grok+HOLDs absent.

## Excerpt spot-check (delta scope only)

- P1 prompt-length (p5/t1/p9/p12) vs S17-1 spec page: `prompts up to/over 100,000
  tokens` confirmed as per-request prompt length; unified headings
  `Prompt ≤100k / >100k tokens`; Japanese per-request phrasing used; monthly/
  output/task-total readings excluded; progressive-partial reading excluded ✓.
- Numbers unchanged from S1 (Input $0.10/$0.50, Output $0.50/$2.50, Cache read
  $0.01/$0.05, 5m write $0.125/$0.625; Sonnet $0.20→$0.10); 1h values ($0.20/$1)
  NOT in prose ✓. Bill guidance (table + usage → estimate; ≠ billed amount;
  no guessed examples) ✓.
- P2/P3/P4/P5/P6: zero body diff; bib-title work caused no body changes ✓.

## Guard checks

- Legacy spans: 0 in reader fields; 1 lawful P4 machine trace.
- Over-assertions: 0. Internal metadata in changed blocks: 0.
- Relative dates: 0.

(End of file)
