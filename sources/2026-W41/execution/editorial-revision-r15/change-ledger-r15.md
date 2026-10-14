# W41 r15 change ledger (actual JSON diffs; mechanical verification)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-14 JST
Authority: `SOL_W41_R14_AUDIT_ACCEPTED / EDITORIAL_REPAIR_AND_READER_PROOF`
Convention: Before = r14 proposal text; After = r15 proposal text (verified by
programmatic block-text diff). Version/runner metadata bumps (v14.0→v15.0) excluded
from "changed" judgments below. r14 file
`execution/editorial-revision-r14/change-ledger-r14.md` is preserved unchanged;
its P5/p3 entry is separately superseded by `r14-ledger-corrigendum-r15.md`.

Proposal SHAs (v15.0):

- P1 `202c90b77b1a…` (16 blocks), P2 `03c1487c2b6e…` (17), P3 `587283f4370e…` (22),
  P4 `2d5b5b87658a…` (7), P5 `c29f7febdd8d…` (19), P6 `ed95fd791775…` (13).
- Synthesis input `6df8a3bb57bf…`, result `516f51d4f61f…`.
- Preview `15d0ebe66970…` (67 paras, 16121 body chars, 5 tables).

## Carried without body change (verified zero body diff r14→r15)

- P1: headline/deck/blocks identical. Actual change status: NO_BODY_CHANGE in r15
  (version bump only). Validation: draft-check PASS.
- P2: identical. NO_BODY_CHANGE. Validation: PASS.
- P6: identical. NO_BODY_CHANGE. Validation: PASS.

P1/P2/P6 body-change prohibition observed.

## Changed in r15

### A-01 / P5/p2 / BEFORE→AFTER / reason: trailing duplicate removal

- Before tail: `…母集団の異なる数値と混ぜてはならない。いずれもブログ掲載の発行元測定で、独立再現はない。`
- After tail: `…母集団の異なる数値と混ぜてはならない。`
- Deleted exact sentence: `いずれもブログ掲載の発行元測定で、独立再現はない。`
- Kept: opening `以下はいずれも発行元の実験結果であり、第三者の独立再現ではない。`
  plus FPR 1% / 200 token約80% / 400 token約95% / psych-ELI5 + math caveat.
  No other p2 text changed.
- Source: `evidence:2026-W41:6601f7ffad5b2624` claim-1 (tgrain).
- Audit ID: R14 A-01. Verdict: RESOLVED.

### A-02 / P5/p3 / BEFORE→AFTER / reason: restore r13 sentence erroneously deleted r13→r14

- Before tail: `…と同じ測定母集団であるとは断定しない。`
- After tail: `…と同じ測定母集団であるとは断定しない。条件の異なる数値を一つの頑健性指標に束ねないことが正確さの条件だ。`
- Restored exact sentence: `条件の異なる数値を一つの頑健性指標に束ねないことが正確さの条件だ。`
- Population distinction retained: FPR試験と類義語置換試験の母集団・条件同一性を断定しない.
  Resulting r15 p3 body equals r13 p3 body.
- Source: `evidence:2026-W41:6601f7ffad5b2624` claim-1 (tgrain).
- Audit ID: R14 A-02 (see `r14-ledger-corrigendum-r15.md` for r14 ledger correction).
- Verdict: RESOLVED.

### A-04-P3p9 / P3/p9 / BEFORE→AFTER / reason: editorial-work viewpoint strip

- Before tail: `…モデルの公開日時を直接示すものではない。記事の時計は発行元ブログの記録、SNS投稿は参考記録という扱いを徹底する。`
- After tail: `…モデルの公開日時を直接示すものではない。`
- Deleted exact sentence: `記事の時計は発行元ブログの記録、SNS投稿は参考記録という扱いを徹底する。`
- Kept: Clef-omni blog metadata `2026年10月9日18時27分34秒（UTC）`, SNS post-time
  distinguished as not directly showing model pub datetime. No other p9 text changed.
- Source: clef claim-1 (JSON-LD timestamp).
- Audit ID: R14 A-04 (P3/p9). Verdict: RESOLVED.
- Invariant: P3 MoE values (78.1B/3.46B, 501B/23B, 1.05T/52B) untouched (p13 unchanged).

### A-04-P4p3 / P4/p3 / BEFORE→AFTER / reason: internal-management → tech-article distinction

- Before:
  `Nano Banana 2.1の仕様は、取得済みのDeepMindモデルカードを一次資料として確認している。公式ブログ記事については、取得済み資料の範囲では確認できていない。ただし、公式ブログがウェブ上に存在しないとは断定できない。発行元情報の確認範囲は、モデルカードの仕様が確定し、ブログ記事の有無が未確定という内訳になる。`
- After:
  `Nano Banana 2.1の技術仕様は、DeepMindのモデルカードに記された範囲で確認できる。公式ブログ記事の有無は、公開資料からは確認できていない。ただし、公式ブログがウェブ上に存在しないとは断定できない。技術仕様はモデルカードを根拠に扱い、ブログ記事の内容は未確認として区別する。`
- Facts kept: card-confirmed / blog-unconfirmed / no-existence-verdict.
  Removed: `取得済み`, `一次資料として確認している`, `確認範囲は…内訳になる`
  (internal acquisition-management phrasing).
- Source: nano card claims (model-card spec) + narrowed blog-search boundary.
- Audit ID: R14 A-04 (P4/p3). Verdict: RESOLVED.
- Guard: P4 Legacy Negative Guard preserved (no web-wide non-existence sentence;
  single lawful machine trace only, p1/p2/n1 unchanged).

### A-04-P5p13 / P5/p13 / BEFORE→AFTER / reason: editorial-act explanation strip

- Before: `列の対応は公式ブログ本文の見出しで確認した。`
- After: `列の対応は公式ブログ本文の見出しによる。`
- All 8 bench values unchanged (AA Index 49.57ポイント/49.76ポイント,
  AutomationBench 34.09%/34.86%, DeepSWE 72.80%/71.68%, Terminal-Bench 4.0
  53.90%/56.06%, Science 0.1 56.90%/60.00%, BrowseComp 87.92%/87.35%,
  HealthBench 64.27%/64.60%, GPQA 94.44%/93.94%).
  Vendor-quality vs detection-rate axis separation kept.
- Source: `evidence:2026-W41:6601f7ffad5b2624` claim-1 (Astra table anchor).
- Audit ID: R14 A-04 (P5/p13). Verdict: RESOLVED.

### A-04-P5t1 / P5/t1 / BEFORE→AFTER / reason: source limitation kept, tech-article naturalization

- Before textGrain row fragment:
  `類義語置換表はブログ一次読み（ベンダー実施）`
- After:
  `類義語置換表はブログ記載の発行元測定`
- Before SynthID row fragment:
  `Googleまたは対象パートナー由来の画像・映像・音声（取得済み公式ブログで明示された範囲。テキストの対応状況はこの資料からは確認できない）`
- After:
  `Googleまたは対象パートナー由来の画像・映像・音声（公式ブログで示された範囲。テキストへの対応は公表資料で確認できない）`
- Before mechanism fragment:
  `検証ポータルの射程はブログ確定、申告規模は画像・映像1800億件以上・音声24万年分、精度の評価数値は取得資料内に確認できず、ポータル本体はJS未取得`
- After:
  `検証ポータルの射程はブログ記載の範囲で確定、申告規模は画像・映像1800億件以上・音声24万年分、精度を示す評価数値は公表資料に示されておらず、ポータル本体の表示確認はできていない`
- Scope preserved: textGrain text-only; SynthID image/video/audio with
  Google-or-partners enumeration; text scope gap; English-global Oct 7;
  scale pair as申告規模; accuracy-absent; portal-unverifiable.
  Removed internal retrieval phrasing (`取得済み`, `この資料`, `取得資料内`, `JS未取得`, `一次読み`).
- Source: tgrain claim-1 + synportal claim-1 / limitation-1.
- Audit ID: R14 A-04 (P5/t1). Verdict: RESOLVED.

## Coverage note

- must_cover 27/27 and boundaries 42/42 preserved structurally and substantively
  (P5[0] still maps p2/p3/t2/p13/t3 with quality substance; no requirement
  dropped or invented; P1/P2/P6 untouched).

(End of file)
