# W43 r7 reader-facing meta scan (Phase A inventory)

Date: 2026-10-27 JST. Subject: fixed r6 TeX/PDF (HEAD `d8e21b8fe`, TeX SHA256
`7c052f05…`, PDF SHA256 `113b179a…`, 22p) → new r7 (this namespace).
Method: actual TeX parsing (comment-stripped visible surface) + independent
PDF text readback (`pdftotext -layout` on real r7 bytes). NOT keyword count
alone. All pages scanned (r7: 22p), not only known p03/p21.

Drive audit report was inaccessible (HTTP 401 on fetch); applied the binding
transcription in the Sol execution contract §1. Never claimed to read
inaccessible content.

## A. Known reader-visible meta (all removed/normalized in r7)

| # | r6 span | r7 span | r6 location | class |
|---|---|---|---|---|
| 1 | `\section*{週刊生成AI技術調査 2026-W43 --- 印刷用原稿 r3}` | `\section*{週刊生成AI技術調査 2026-W43}` | l.19 interior heading | EDITORIAL_META_REPLACEMENT |
| 2 | `\surveyeditiondescriptor{週刊Technical Survey（編集プレビュー・未承認）}` | `\surveyeditiondescriptor{週刊Technical Survey}` | l.7 cover setup | EDITORIAL_META_REPLACEMENT |
| 3 | cover anchors `{2026-W43 Weekly --- 読者確認用プレビュー}` | `{}` (W42 baseline: empty) | l.9 | EDITORIAL_META_REPLACEMENT |
| 4–11 | `\section{P1 --- …}` … `\section{P8 --- …}` (8×) | `\section{…}` (prefix stripped) | ll.23–681 | OPERATOR_ID_NORMALIZATION |
| 12–14 | box titles `文脈長の三層（p1-f1、§1.3実物）`, `資格・承認フロー（p3-f1、§3.2実物）`, `協調開示の五段階（p6-f1、§6.1実物）` | bare descriptive titles | ll.131,356,566 | OPERATOR_ID_NORMALIZATION |
| 15–19 | captions `MemT権利対応（p2-f2、§2.5実物）`, `様式×…（p5-f1、§5.1–5.2実物。…）`, `言語別…（p7-f1、§7.2実物。…）`, `安定核…（p8-f2、§8.2実物）`, `重み…（p8-f3、§8.3実物）` | operator IDs stripped; scientific tails KEPT (see §C) | ll.224–803 | OPERATOR_ID_NORMALIZATION |
| 20 | verbatim header `【例：Decisions要求・応答（p8-f1、§8.1実物。公式ガイド転載・未実行（API呼出しなし））】` | `【例：Decisions要求・応答（公式ガイド転載・未実行（API呼出しなし））】` | l.710 | OPERATOR_ID_NORMALIZATION |
| 21 | bib preface `本プレビューは非正準の編集 proof であり、受理済み Core 証拠の代替ではない。…分離記録した文脈注記の詳細は引用対応表を参照。` | `本稿で参照した資料を以下に示す。各資料の確認範囲や未検証事項は本文・注記に明記した。` | l.854 | EDITORIAL_META_REPLACEMENT |

Machine traceability preserved: `\label{sec:P1}`…`\label{sec:P8}`,
`\label{sec:cover-title}`, `\label{sec:recap}`, 36 `\bibitem` keys, URLs —
all byte-identical. TOC regenerated (no P prefixes, verified p02 image +
text extraction).

## B. Lower-priority sweep (explicit verdicts)

Scanned comment-stripped visible surface + PDF text layer for: QA/review/
approval statuses, `UNVALIDATED`/`NONCANONICAL` embedded in article, internal
SHA, staging filename/artifact path, session/approval refs, standalone
`reader`/`projection`/`proof`, print revision.

- `NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF` occurs 2× in visible layer:
  cover safety mark (p01, separate muted line under cover block) + end
  footer (p22, centered muted line after bibliography). Both are
  PROOF_STATUS_RELOCATED safety marks, NOT magazine content. PDF
  Subject/Keywords metadata identical. No other occurrence. (TeX preamble
  `%` comments + `\hypersetup` values are invisible; kept as provenance.)
- No internal SHA, staging path, session ID, approval ref, or print-revision
  string in visible surface (grep over stripped body: 0 hits for
  `sources/`, `.md`, `task-`, `SHA256`, `UNVALIDATED-20`, `r3.5`, `r6`).
- Standalone `proof`: only inside the two safety marks + bib preface
  replacement removed the one article occurrence. `projection`/`reader`:
  0 visible hits.
- Natural prose `実物` (e.g. l.27「動かせる実物」) is ordinary Japanese, not
  an operator tag; kept. Only parenthesized `(pX-fY、§…実物)` tags removed.

## C. Scientific qualifiers (MUST stay — all verified present in r7)

`pdftotext` counts on real r7 bytes: 未検証 21, 未実行 8, 原本未取得 2,
発行元測定 10, 独立再現なし 8, 未取得 31, 発行元公表 2, plus 未確認/未開封/
未照合 families. Spot checks: p5 caption keeps「数値は全て発行元公表・
独立再現なし。比較対象・単位は行内でqualified」; p7 caption keeps「数値は
全て発行元測定」; code header keeps「公式ガイド転載・未実行」; bib tiers
(`原表未取得`, `404`, `締切後`, `独立再現なし`) byte-identical to r6.
Validator `M-qualifiers` PASS; negative `N-qualifier-delete` detected with
`SCIENTIFIC_QUALIFIER_LOSS`.

## D. Non-editable

No `NOT_AUTOMATICALLY_EDITABLE` spans: every candidate operator tag had a
clean descriptive remainder. No technical argument rewritten (ledger holds
23 exact old→new pairs; all other prose/values byte-identical per validator
18/18).
