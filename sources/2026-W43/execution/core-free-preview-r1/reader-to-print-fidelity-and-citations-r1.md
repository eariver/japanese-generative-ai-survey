# W43 reader-to-print fidelity and citations r1

Source (exact bytes): `sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md` (`6f07cb49…`).
Print: `sources/2026-W43/execution/core-free-preview-r1/reader-print-projection-r1.md` (`e1a49da9…`) → `main.tex` (`0d8a8a09…`) → `main.pdf` 22 pages (`fd88cb7c…`).
Ledger `6fd9d6fe…`, manifest `85d94d74…`. Checker `EDITION_LOCAL_ROW_JOIN_PASS` exit 0.

## 1. Headings/paragraphs/text mapping

- `# W43 … r3.5（非正規編集資産）` → `\section*{週刊生成AI技術調査 2026-W43 — 印刷用原稿 r1}` (title clean only).
- `## P1 — …` … `## P8 — …` (8 packages) → `\section{P1 …}` … `\section{P8 …}` same order, same prose. 62 paragraphs preserved verbatim except operator-token → natural Japanese (see diff doc) and internal-path backticks → `保存済み一次資料`.
- `### …` subsections → `\subsection*` same order/text.
- `> 【読み方の注意】…` (8 notes) → blue-gray `tcolorbox` same text (tokens naturalized, limits retained).
- `# 今週の総括` five paragraphs → `\section*{今週の総括}` standalone after P8, before references. Not P9. Text identical to source recap (5 paras, no new claim).
- Inline `code`, `**bold**`, `POST /v1/decisions`, env vars preserved as `\texttt`/`\textbf`; bare URLs → `\url` for breaking only.

## 2. Tables: 20 headers → 20 printed tables, 80 rows → 80 cells, no loss/dup

Headers (order pinned, TeX `\caption` identical except token naturalization):
1. `【表：公開状態×時点（Kimi）】` (p1-t1, 4 rows)
2. `【表：total／effective／active と文脈（計数規約を見出しに明記）】` (p1-t2, 4 rows)
3. `【表：bench×harness×分母（帰属明示）】` (p1-t3, 3 rows)
4. `【表：可用性×時刻×約款（発表／プレビュー／GA／重み配布／再現を別列）】` (p1-t4, 3 rows)
5. `【表：核×役割（DeepInfer）】` (p2-t1, 5 rows)
6. `【表：bench×分母×条件（MemT）】` (p2-t2, 4 rows incl. 66x storage / 1.86x SOURCE_UNVERIFIED / 11bench parametric scope)
7. `【表：MemT権利対応（p2-f2、§2.5実物）】` (p2-f2, 4 rows: paper CC BY-NC-SA / software PolyForm / third-party MIT / weights excluded)
8. `【表：権限×条件（Duet）】` (p3-t1, 4 rows)
9. `【表：旧／新／未来の三段（auto-mode）】` (p3-t2, 4 rows: 8/7 OUT / 10/22 IN / next-week FUTURE)
10. `【表：倍率×削減率×出典／版／時刻】` (p4-t1, 5 rows incl. 25.37x/22.31x/95.52% VERIFIED, 26.5x incongruent, 22x lower-bound)
11. `【表：機能×モデル×対応言語×出典／版／時刻】` (p5-t1, 4 rows: STT 50+, Realtime 35+/40+, TTS unresolved, 11-lang sample ≠ coverage)
12. `【表：AA×原表有無（Ming）】` (p5-t2, 4 rows: Controlled/Robustness/Provider Voice vendor-cited, MIT confirmed)
13. `【表：様式×評価・料金の実数行列（p5-f1 …）】` (p5-f1, 4 rows: WER 4.1/4.0 COMPARATOR_UNVERIFIED, cpWER 18.4/18.6 vs Pyannote 19.0, recall 94.6/81.4, latency sub-500ms, prices Mini $0.0035 confirmed / Small $0.004 UNIT_UNVERIFIED / Realtime $0.008 UNIT_UNVERIFIED / TTS $13 confirmed / agent $0.04/$0.08 UNIT_UNVERIFIED)
14. `【表：手順×来歴×限界（Bio）】` (p7-t1, 4 rows)
15. `【表：言語別デルタと労力・費用の注記（p7-f1 …）】` (p7-f1, 6 rows: COBOL 10.9→72.1 + 19/20≥83% exception + hidden byte-parity + 企業現場40%超 prevalence separate from accuracy; OCaml/Fortran/VB; effort 86.6% low / 97.9% high; cost Luna $0.77 vs Sol $3.48)
16. `【表：bench×分母×条件（Low-resource）】` (p7-t2, 3 rows)
17. `【表：料金×条件×版（Decisions）】` (p8-t1, 4 rows: $0.10/$0.01, 400 per-request, v1 GA/beta, US/EU/ZDR)
18. `【表：安定核 vs 実験harness（p8-f2 …）】` (p8-f2, 3 rows: stable 76 pkgs + GH 15:18:14Z / npm 15:21:49Z separate; harness 0.x experimental; 版固定 npm 2026-10-22T15:21:49Z GH separate, Metrics OUT, Grok 当週の対象外)
19. `【表：API×移行×約款（発表／配布／無料期限を別status）】` (p8-t2, 4 rows: MIT vendor-declared SHA unseen, $0.75/1k till 10/31 16:00 UTC, DeepSWE 77 vs 74.2 vendor harness)
20. `【表：重み vs API vs 追加物（p8-f3 …）】` (p8-f3, 3 rows)

80 physical `｜` rows → printed `tabularx` rows 1:1, order preserved, 78 DATA + 2 NOTE (`p1-t2-04`, `p4-t1-05 NOTE`) excluded from claims per manifest. 13 sanctioned aliases pinned. No duplicated/lost rows (TeX has 20 `table` envs; `grep -c begin{table}` = 20).

## 3. Figures: 3 blocks preserved

- p1-f1 `【図：文脈長の三層】` Kimi 1M / Flint 512k対応/256k推奨/262144設定 / Nemotron 64K + effective/total/active unequivalence.
- p3-f1 `【図：資格・承認フロー】` path A live / path B coming-soon NOT_LIVE_VERIFIED (rendered as 提供予定), Managed-Agents never sees secrets (design claim, no independent test).
- p6-f1 `【図：協調開示の五段階】` validate+fix / advance-notice / coordination / prepare / publish, Daybreak/checker outside, CVE unidentified.

Rendered as numbered `figure` + `tcolorbox`, text identical (tokens naturalized).

## 4. Code/illustrative blocks

- p2 bash (MTP_VARLEN) + python (deterministic sampling PSEUDOCODE/NONRUNNABLE/NOT_EXECUTED/IMPORT_UNVERIFIED) → `verbatim`, labels preserved as 未実行/疑似コード/実行不可/導入未確認.
- p8 JSON choice request/response (official guide illustrative, NOT_RUN) → `verbatim`, reading note `NOT_RUN → 未実行`, TTL 30m not W43 fact.

## 5. Claims: 29 meanings/units/comparators preserved

Baseline from strict checker (own-block DATA, physical-value proof):
- p2-f2 licenses (4): CC BY-NC-SA 4.0 / PolyForm 1.0.0 / MIT flash-linear-attention / weights excluded (units n/a, URLs github.com/MemTensor, 5 RAW_PRIMARY content-checked).
- p5-f1 Voxtral (9): WER 4.1/4.0, cpWER 18.4/18.6 vs Pyannote 19.0, recall 94.6/81.4, latency sub-500ms (500ms+未満), prices Mini $0.0035 confirmed / Small $0.004 UNIT_UNVERIFIED / Realtime $0.008 UNIT_UNVERIFIED / TTS $13 confirmed / agent $0.04/$0.08 UNIT_UNVERIFIED. Comparators/units qualified, AA originals unfetched.
- p7-f1 low-resource (8): COBOL 10.9→72.1 + 40%+ enterprise prevalence (企業現場/オンラインバンキング + 精度とは別, never accuracy), OCaml 25.6→85.8, Fortran 21.4→83.5, VB 27.5→89.4, low 86.6% / high 97.9%, cost $0.77 vs $3.48 (cost ≠ quality).
- p8 clocks/scale (4): GH 15:18:14Z vs npm 15:21:49Z separate origins (GH ≠ npm proof, scoped URL + RAW_NOT_ARCHIVED), scale 76/23/8/143, Metrics 23:42:03Z OUT.
- p8 DeepSeek (4): MIT vendor-declared (LICENSE bytes/SHA unseen), $0.75/1k till 10/31 16:00 UTC, DeepSWE 77 vs 74.2 vendor harness, free-period UTC deadline.

All units/comparators/denominators/URLs/tiers unchanged; NOTE rows excluded; no URL-only proof.

## 6. Citations: 36 keys → bibliography URLs resolved

From `w43-r3-3-source-crosswalk.md` (37 keys, 1 empty → 35 valid + decisions-guide = 36 `bibitem`s):
KIMI-X `https://x.com/Kimi_Moonshot/status/2113680701770068067`, KIMI-BLOG, FLINT-CARD, FLINT-ART, NEMO-CARD, NEMO-COMMITS, DI-README/ENV/LICENSE, MEMT-README, duet-blog-1021, 1pw-blog-1022, automode-art-1022, flux-page-1019/elo/keyframes-conflict/speed-recalc, voxtral-card-units/announce, deepinfer-import-scope, ming-readme-license/aa-cited, eleven-blog, patch-rendered, securing-page-rss, bio-page, lowres-page, decisions-page/guide/ts-ref/ref-create, tanstack-gh/npm/blog, deepseek-1017, recap LIMITED. Archive paths with bytes marked FIRST_PARTY; others DERIVED_ONLY/UNRESOLVED/QUALIFIED as in crosswalk. No padded URL dumps; reader-visible 典拠 lines point to bibliography.

Source tier unaltered: 5 RAW_PRIMARY / 24 QUALIFIED_UNAVAILABLE / 0 OTHER.
