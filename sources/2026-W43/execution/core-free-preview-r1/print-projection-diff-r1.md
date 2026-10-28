# W43 print-projection diff r1 (r3.5 reader -> print projection)

Source (exact bytes): `sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md`
Print: `sources/2026-W43/execution/core-free-preview-r1/reader-print-projection-r1.md`

Presentation-only; no substantive claim change. Every print-only wording change maps source-id span -> print span.

## Title
- BEFORE: `# W43 日本語本文プレビュー r3.5（非正規編集資産）`
- AFTER: `# 週刊生成AI技術調査 2026-W43 — 印刷用原稿 r1`
- Reason: clean reader-facing title; internal asset label removed per contract §2.1.

## Operator-token replacements (counts are occurrences in source)
- `# W43 日本語本文プレビュー r3.5（非正規編集資産）` x1 -> `# 週刊生成AI技術調査 2026-W43 — 印刷用原稿 r1` — title: remove internal asset label, neutral reader-facing title
- `SOURCE_UNVERIFIED` x4 -> `未検証（保存済み資料に記載なし・比較条件未確認）` — operator token -> natural Japanese; limit retained
- `RENDERED_ONLY` x3 -> `描画抽出のみ（原本HTMLの閲覧ではない）` — operator token -> natural Japanese
- `RENDERED_TEXT` x2 -> `描画抽出テキストのみ（原本HTMLの閲覧ではない）` — operator token -> natural Japanese
- `NOT_EXECUTED` x4 -> `未実行` — operator token -> natural Japanese
- `NOT_RUN` x2 -> `未実行（API呼出しなし）` — operator token -> natural Japanese
- `PSEUDOCODE` x2 -> `疑似コード（実行できない抜粋）` — operator token -> natural Japanese
- `NONRUNNABLE` x2 -> `実行不可の抜粋` — operator token -> natural Japanese
- `IMPORT_UNVERIFIED` x1 -> `導入経路は未確認` — operator token -> natural Japanese
- `NEVER_STORY` x2 -> `当週の対象外` — internal story flag -> natural Japanese; selection unchanged
- `POST_CUTOFF／OUT` x1 -> `集計期間外のため当週非選択` — operator token -> natural Japanese
- `UNRESOLVED_FAQ_ATTRIBUTION` x2 -> `未照合の記述の食い違い（出典・版・観測時刻は未特定のため確定した矛盾としない）` — operator token -> natural Japanese; limitation retained
- `UNRESOLVED_VENDOR_DOC_CONFLICT` x1 -> `資料間で不一致があり単一値に統一しない` — operator token -> natural Japanese
- `UNRESOLVED` x2 -> `未解決（単一値に統一しない）` — operator token -> natural Japanese
- `COMPARATOR_UNVERIFIED` x1 -> `比較対象・内訳は未確認` — operator token -> natural Japanese
- `UNIT_UNVERIFIED` x3 -> `単位の記載は未確認` — operator token -> natural Japanese
- `VENDOR_BENCH` x4 -> `発行元測定（独立再現なし）` — operator token -> natural Japanese
- `PRIMARY_RAW` x2 -> `一次資料` — operator token -> natural Japanese
- `PRIMARY_METADATA` x2 -> `一次資料（付随情報）` — operator token -> natural Japanese

## Internal-path backticks neutralized
- Backticked repo-internal paths (containing `/`, `.md`/`.py`/`.html`, `sources/`, `task-`, `memt-`/`deepinfer-`/`flint-` prefixes) replaced with `（保存済み一次資料・詳細は出典一覧）`. API paths (`POST /v1/decisions`), env-var names, model/param identifiers without slashes preserved as code.
- Approximate replacements in this class: (see TeX/projection diff via `diff -u` for exact lines).

## Structure preserved (verified by checker inputs)
- P1–P8 eight chapters, 19 selected placements (12 primary + 7 supporting) unchanged.
- 20 tables / 80 physical rows (78 DATA + 2 NOTE), 3 figures, 2 code examples + 2 JSON illustrative blocks, 29 claims unchanged in meaning/units/comparators.
- Standalone `今週の総括` five paragraphs immediately after P8, before references. Not P9, no new package, no new claim.
- Source/claim authority levels and negative findings retained in natural Japanese; no invented articles, values, grants, comparisons, or primary evidence.
- Full line-level verification: run `diff -u` between source and projection; only title, operator tokens above, and internal-path backticks differ.
