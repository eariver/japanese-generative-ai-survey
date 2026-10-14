# W41 r16 change ledger (actual JSON diffs; mechanical verification)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-14 JST
Authority: `SOL_W41_R15_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_PUBLICATION_REPAIR`
Convention: Before = r15 proposal text; After = r16 proposal text (verified by
programmatic block-text diff). Version/runner bumps (v15.0→v16.0) excluded.
r15 files preserved unchanged (no overwrite).

Proposal SHAs (v16.0):

- P1 `7494b44c3dd3…` (16 blocks, pricing completion), P2 `a7337ae2110d…` (17, NO_BODY_CHANGE),
  P3 `557350f3a0fe…` (22, NO_BODY_CHANGE), P4 `957fca91fc34…` (7, NO_BODY_CHANGE),
  P5 `eebd1b5825b4…` (19, M06 cleanup), P6 `c841dcfbdf4d…` (13, NO_BODY_CHANGE).
- Synthesis input `689fe5776283…`, result `16e53b887ec2…`.
- Preview `c1935ede5dd8…` (67 paras, 16117 body chars, 5 tables).

## Carried without body change (verified zero body diff r15→r16)

- P2, P3, P4, P6: headline/deck/blocks identical. NO_BODY_CHANGE (version bump only).
  Validation: draft-check PASS. r15 editorial closure (PASS) not disturbed.

## Changed in r16

### R15-M04 / P1/p5 / BEFORE→AFTER / reason: full price-table confirmation (supplement)

- Before: two-tier outline with cache-read only (`10万以下が$0.01、10万超が$0.05`);
  input/output unit unknown; formal table check required.
- After: two-tier with per-1M-token unit and 4 rows —
  ≤100k: Input $0.10 / Output $0.50 / Cache read $0.01 / Cache write (5分) $0.125;
  >100k: Input $0.50 / Output $2.50 / Cache read $0.05 / Cache write (5分) $0.625;
  Sonnet halving kept. Table is confirmed; bill still needs usage
  (table estimate vs individual bill distinguished).
- Source: official page `https://www.anthropic.com/claude-haiku-5-5` (Oct 7),
  re-fetched 2026-10-14; recorded in `editorial-source-supplement-r16.md`
  as SOURCE_VERIFIED / NOT_CANONICAL_ACCEPTANCE (Card claim-1 covers cache-read
  + Sonnet halving only; input/output/cache-write/unit are supplement additions,
  not pre-existing Card claims).
- Audit ID: R15-M04. Verdict: RESOLVED (pending independent semantic adoption check).

### R15-M04 / P1/t1 / BEFORE→AFTER / reason: same price-table completion

- Before Haiku row: cache-read only + `入力・出力本体の単価や課金単位の別は取得本文に示されていない
  （この数値だけでの利用費試算は不可、正式料金表の確認が必要）`.
- After Haiku row: two-tier 4-row table per 1M tokens (values as in p5) +
  `実際の請求額には使用量が必要（料金表の推定額と個別の実請求額は別）`.
- No contradiction with old text introduced: the table-exists fact and the
  usage-needed-for-bill fact are kept distinct (no claim that unit/rows were
  previously confirmed).
- Source: same supplement. Audit ID: R15-M04. Verdict: RESOLVED.

### R15-M04 / P1/p9 / BEFORE→AFTER / reason: pricing-status consistency

- Before: `Haiku側は二段階料金とcache-read区分・ベンチ表の値が確定し、
  課金単位の別とsystem-card全文・測定条件が未確認である`.
- After: `Haiku側は二段階料金表（100万token当たりの4区分）とベンチ表の値が確定し、
  system-card全文・測定条件が未確認である`.
- Source: same supplement. Audit ID: R15-M04. Verdict: RESOLVED.

### R15-M04 / P1/p10 / BEFORE→AFTER / reason: same

- Before: `Haikuのcache-read区分は数値付きで確定する一方`.
- After: `Haikuの料金表は数値付きで確定する一方` (GPT-6料金未確認 kept).
- Source: same supplement. Audit ID: R15-M04. Verdict: RESOLVED.

### R15-M04 / P1/p12 / BEFORE→AFTER / reason: estimation guidance consistency

- Before: third point requires formal-table + unit check before estimating
  (`費用の金額計算には正式な料金表の確認が要る`).
- After: `確認した料金表（100万token当たり）と使用量と合わせて試算すること。
  料金表からの推定額と使用者個別の実請求額は別のものとして扱いたい。`
- Table-estimate vs individual-bill confusion avoided (no conflation).
- Source: same supplement. Audit ID: R15-M04. Verdict: RESOLVED.

### R15-M04 / P1/n1 / BEFORE→AFTER / reason: same

- Before: `入力・出力本体の単価や課金単位の別は取得本文に示されていない。`
- After: `100万token当たりの単価を示す。実際の請求額には使用量が必要である。`
- Source: same supplement. Audit ID: R15-M04. Verdict: RESOLVED.

### R15-M06 / P5/p6 / BEFORE→AFTER / reason: retrieval-language naturalization

- Before: `取得した公式ブログで検証対象として明示されているのは画像・映像・音声であり、
  テキストの対応状況はこの資料からは確認できない。`
- After: `公式ブログで検証対象として示されているのは画像・映像・音声であり、
  テキストへの対応は公表資料で確認できない。`
- Scope unchanged (Google-or-partners image/video/audio; text support not established
  by this announcement). Uncertainty kept.
- Source: `evidence:2026-W41:ef2ef9a25ec009ba` claim-1/limitation-1 (no new claim).
- Audit ID: R15-M06. Verdict: RESOLVED.

### R15-M06 / P5/p7 / BEFORE→AFTER / reason: same

- Before: `synthid.comはJSシェルのみで、対応形式や料金、ライセンス条項は取得できない。
  取得した資料の範囲内では、…確認できなかった。…「効き目」の測定は手元にない…
  取得による裏付けはない。`
- After: `synthid.comは表示の確認ができておらず、対応形式や料金、ライセンス条項は確認できない。
  公表資料では、…確認できなかった。…「効き目」の測定は確認できない…裏付けはない。`
- Boundaries kept (portal unverifiable, accuracy absent). Audit ID: R15-M06. Verdict: RESOLVED.

### R15-M06 / P5/n1 / BEFORE→AFTER / reason: same

- Before: `textGrainの数値はベンダー実施の一次読み、…`
- After: `textGrainの数値はブログ記載の発行元測定の読み取り、…`
- Source: tgrain claim-1 (no new claim). Audit ID: R15-M06. Verdict: RESOLVED.

## Coverage note

- must_cover 27/27 and boundaries 42/42 preserved (P1 pricing substance still maps
  P1 must-cover[2]; P5[0] still maps p2/p3/t2/p13/t3; no requirement dropped/invented).

(End of file)
