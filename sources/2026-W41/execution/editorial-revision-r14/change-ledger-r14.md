# W41 r14 change ledger (actual JSON diffs; no false fix records)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-13 JST
Convention: Before = r13 proposal text; After = r14 proposal text (verified by
programmatic block-text diff). Version/runner metadata bumps (v13.0→v14.0) excluded
from "changed" judgments below.

## Carried without body change (verified zero body diff)

- P1 (M01/M02 scope): r13 already carries the recommended billing wording, split
  conditions, headline/deck distinction. Actual change status: NO_BODY_CHANGE in r14
  (version bump only). Validation: re-run PASS.
- P2 (m01 scope): r13 already absolute-dated. NO_BODY_CHANGE in r14. Validation: PASS.
- P6: no r14 items. NO_BODY_CHANGE. Validation: PASS.

## Changed in r14

### R13-A01 / P5/t1 / BEFORE→AFTER / reason: Google-inclusive scope
- Before: "…｜利用制限：英語グローバル、パートナー由来に限定｜…"
- After: "…｜利用制限：2026年10月7日から英語で世界向けに提供｜…" with scope row
  "Googleまたは対象パートナー由来の画像・映像・音声（取得済み公式ブログで明示された範囲。
  テキストの対応状況はこの資料からは確認できない）".
- Source: synth excerpt enumeration + Card claim-1. Verdict: RESOLVED (no non-support
  verdict, RECONCILED reading kept, Architecture untouched).

### R13-A03 / P3/p9 / BEFORE→AFTER / reason: deadline-procedure strip
- Before: "…締切22時より前でウィンドウ内確定…週次のGrok X投稿23時11分は締切後であり…"
- After: "Clef-omniの公開時刻は、発行元ブログに記録された公開日時のメタデータに基づく。
  …SNS上の後続投稿日時は、モデルの公開日時を直接示すものではない。"
- Source: clef claim-1 (JSON-LD). Verdict: RESOLVED.

### R13-A03 / P3/p12 / BEFORE→AFTER / reason: internal process term strip
- Before: "今回のEvidenceが裏付けるのは…"
- After: "今回確認した資料から裏付けられるのは…"
- Scope unchanged (公開表明＋提示まで). Verdict: RESOLVED.

### R13-a07 / P3/p14 / BEFORE→AFTER / reason: three→four stages
- Before: "確認の三段階――公開表明、配布場所、実ファイル――"
- After: "確認の四段階――発行元による公開表明、発行元による配布先の提示、その提示先の実在確認、
  重みファイルの取得成功――" + license-check sentence kept. Matches p12. Verdict: RESOLVED.

### R13-a08 / P4/p3 / BEFORE→AFTER / reason: acquisition-centered → tech-article
- Before: "2026年10月12日に確認した発行元ページの範囲では…" (activity-centered).
- After: "Nano Banana 2.1の仕様は、取得済みのDeepMindモデルカードを一次資料として確認している。
  公式ブログ記事については、取得済み資料の範囲では確認できていない。ただし…断定できない。
  発行元情報の確認範囲は、モデルカードの仕様が確定し、ブログ記事の有無が未確定という内訳になる。"
- Facts kept (card-confirmed / blog-unconfirmed / no-existence-verdict); guard kept
  (no legacy spans). Verdict: RESOLVED.

### R13-a04 / P5/p3 / BEFORE→AFTER / reason: vendor-tail dedup
- Before: tail "（いずれも発行元の申告値）。" (duplicates p2 intro marking).
- After: tail removed; p2 intro marking + NOTE carry attribution. Population
  non-identity sentence kept. Verdict: RESOLVED.

### R13-a05 / P5/p13+t3 / BEFORE→AFTER / reason: AA units
- Before: "AA Indexで49.57と49.76" / "AA Index｜49.57｜49.76".
- After: "49.57ポイントと49.76ポイント" / "AA Index（ポイント）｜49.57｜49.76".
- Columns and values unchanged. Verdict: RESOLVED.

### R13-a06 / P5/t3 / BEFORE→AFTER / reason: history note → reader note
- Before: "条件注記：列の対応は2026年10月13日に公式ブログ本文で再確認した見出し…による。"
- After: "注：AA Indexの単位はポイント、その他の7指標は%。透かしなし／ありの両列はAstra max条件での
  発行元測定値。独立した再現は確認されていない。"
- Header-confirmation fact kept in `quality-table-evidence-review-r13.md` + r14 audit trail.
  Verdict: RESOLVED.

### SHA corrigendum (R13-A02 companion)
- Recorded in `sha-corrigendum-supersession-r14.md` (supersedes r13 corrigendum, which is
  preserved). Actual-status: r12/r13 artifacts bind correctly (PASS retained); only the
  paperwork SHAs were wrong. Verdict: CORRECTED (new doc, old docs untouched).

## Coverage note

- must_cover 27/27 and boundaries 42/42 preserved (P5[0] still maps p2/p3/t2/p13/t3).
  No requirement dropped or invented.

(End of file)
