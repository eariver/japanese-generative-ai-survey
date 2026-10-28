# W43 source-to-print diff and allowlist r3 (source-anchored, every changed line)

Source: r3.5 reader `6f07cb49…` (529 lines). Print: `reader-print-projection-r3.md` `63ad2617…`.
`diff` changed markers: 71 (`<`+`>`), = 35 modified source lines + 1 title + 1 added TanStack line + symmetric diff sides.
Validator: `print-semantic-fidelity-check-r3.py` → `PRINT_SEMANTIC_PASS` (10 positive + 4 negatives, exit 0).

## Allowlist classes (every changed line belongs to exactly one)

- CLASS TITLE (1 line): L1 `# W43 …（非正規編集資産）` → `# 週刊…印刷用原稿 r3`. Reason: clean reader title (r1/r2 contract §2.1).
- CLASS TOKEN (33 lines): 19 operator-token substitutions, meaning-preserving natural Japanese, limits retained. Full list with counts: PRIMARY_METADATA→一次資料（付随情報）(3), PRIMARY_RAW→一次資料 (2, incl. dedup collapse), SOURCE_UNVERIFIED→未検証… (4), RENDERED_ONLY/TEXT (5), NOT_EXECUTED (4), NOT_RUN→未実行（API呼出しなし）(2), PSEUDOCODE/NONRUNNABLE/IMPORT_UNVERIFIED (5), NEVER_STORY→当週の対象外 (2), POST_CUTOFF→集計期間外… (1), UNRESOLVED_FAQ_ATTRIBUTION (2), UNRESOLVED_VENDOR_DOC_CONFLICT/UNRESOLVED (4), COMPARATOR/UNIT_UNVERIFIED (4), VENDOR_BENCH→発行元測定（独立再現なし）(4). No value/unit/comparator/claim altered.
- CLASS PATH (12 lines, subset of the 33): backticked repo-internal paths → `（保存済み一次資料・詳細は出典一覧）`. SAFE rule (F-R3-01): strip ONLY spans containing internal hints (`sources/`, `.md`, `.py`, `.html`, `task-`, `memt-`, `deepinfer-`, `flint-`, `recursive-`, `w43-`, `environ.py`); HTTP-method+path spans (`POST /v1/decisions`, the ONLY such span besides one `sources/…md`) are NEVER stripped. Verified: 2 slash-spans in source = 1 API route preserved + 1 internal path neutralized.
- CLASS R3-DUP (1 line): L480 `…集計期間外のため当週非選択 であり当週非選択、` → `…集計期間外のため当週非選択であり、` (redundant second 当週非選択 removed; token already encodes it; particle adjusted; meaning preserved).
- CLASS R3-TANSTACK (1 added line): p8-f2 table gains `典拠: 安定核=tanstack-gh（GH 15:18:14Zのみ）／npm=tanstack-npm（15:21:49Z・別典拠・原本未取得）`. Reason: F-R3-03 minimal repair — the only material table with zero exact key traceability; keys+clocks from accepted crosswalk, no value change, GH≠npm separation explicit. 80 ｜-row count unaffected (note line has no ｜).
- CLASS R3-POST (0 changed lines, verified identical): L473 `読み方：\`POST /v1/decisions\`…` is byte-identical to source (r1/r2 had destructive substitution; r3 restores/preserves). Allowlist records it as PROTECTED-IDENTICAL.

## Explicit non-changes (verified by validator)

- 20 headers identical order, 80 ｜ rows (row-level count + representative qualifiers; full cell map in fidelity doc), 3 figures identical, 5 recap paras identical, 29 claim literals all present, URL hygiene (34 http URLs, 0 malformed), qualifiers retained, TanStack keys present.
- Negatives prove load-bearing: API deletion / clock swap / JP-in-URL injection / qualifier strip are all detected.

No new research, no new article, no substantive rewrite. r1/r2 differential note: vs r2 projection, r3 differs in exactly 4 hunks (title r3, POST restore, dup cleanup, TanStack line); all other lines identical.
