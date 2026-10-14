# W41 r16 source–claim check (programmatic + editorial)

Status: `EDITION_LOCAL / AUDIT_EVIDENCE`
Date: 2026-10-14 JST
Method: official `draft-check` CLI 6/6 PASS + `synthesis-check` PASS + programmatic
audits + excerpt spot-check (changed scope only; r15-verified carry-overs retained).

## Programmatic audits (executed, all PASS)

- All `evidence_refs`/modes unchanged r15→r16 for all 6 packages
  (refs P1 24, P2 26, P3 42, P4 7, P5 26, P6 19; attribution modes intact).
  No new Card refs invented; supplement facts (S1) deliberately NOT encoded as
  Card refs (Cards unchanged by design).
- must_cover 27 exact-once, no blanket; boundaries 42 exact-once
  (P1 pricing still maps must-cover[2]; P5[0] still maps p2/p3/t2/p13/t3).
- Attribution modes cover all referenced classes.
- basis binds exact canonical package SHA + prompt SHA (`b6873133…`).
- No invented source IDs/experiments; no disposition changes;
  Grok+HOLDs+INSPECTs absent from prose.
- Synthesis input rebuilt from r16 pairs via official CLI; result basis binds new
  input SHA (`689fe577…`); payload keys match requirements (signals line updated
  for 4-row table; no key added/removed).

## Excerpt spot-check (delta scope only)

- P1 pricing (p5/t1/p9/p10/p12/n1) vs S1 official table: ≤100k Input $0.10 /
  Output $0.50 / Cache read $0.01 / Cache write $0.125; >100k $0.50 / $2.50 /
  $0.05 / $0.625; per-1M-token unit; Sonnet $0.20→$0.10 ✓. Bill guidance keeps
  table-estimate vs individual-bill distinct ✓. Old unknowns (`課金単位未確認`,
  `入力・出力料金未確認`, `試算不可`, `価格記載なし`) consistently replaced where
  the table now confirms, retained only where still true (system-card/IDs) ✓.
- New numbers appear ONLY via supplement S1 (NOT as Card claims) ✓.
- P5 M06 (p6/p7/n1): no numbers/scopes changed; bounded SynthID reading kept
  (Google-or-partners image/video/audio; text support not established by this
  announcement); portal-unverifiable + accuracy-absent kept ✓.
- P2/P3/P4/P6: zero body diff; prior audits retained ✓.

## Guard checks

- Legacy spans: 0 in reader fields/preview/synthesis-result; 1 lawful P4 machine trace.
- Over-assertions (テキスト除外, 今日落とせる, GrokのX告知は, 試算に使える, 値札付き,
  パートナー由来に限定): 0 (bib `text excluded` separately corrected to bounded
  announcement language; Architecture wording untouched).
- Internal metadata (revision/audit/deadline/acquisition process, 取得済み,
  一次読み): 0 remaining in changed proposal blocks (verified by diff).
- Relative dates (non-W41-clear): 0.

(End of file)
