# P6a deep draft r14 — training methods and systems (NON_CANONICAL technical prep)

Status: `TECHNICAL_PREP_R14 / NON_CANONICAL / NOT_ARCHITECTURE / NOT_READER_PROSE`
Covers (ordinary 28 only): `candidate:2026-W40:92241424368e1305` (ContextLM, PRIMARY)
+ `candidate:2026-W40:a5143ea24719b616` (Olmo-core 3, PRIMARY).
Conditional subjects (AstaBrief COND-A, AutoSynthData COND-B) are EXCLUDED from this
file's 28-scope sections and appear ONLY in the labeled appendix at the end —
they are NOT drafted as official P6a subsections here.
Basis: W40 accepted Evidence/Views (claim-level + bounded excerpts + ar5iv full-text
for ContextLM §§1–6). Every number below carries numerator/denominator/hardware/
baseline/version; anything beyond consumed evidence is marked `UNVERIFIED` — no
fabricated specificity. Never cite as HUMAN APPROVED; never merge into
`architecture-v2.json` or `surveys/.../main.tex` (not written here).

## 1. ContextLM — file-as-context (arXiv:2609.37725, Shao et al. 13 authors, UW/Meta/MIT/Trillium)

Paper: submitted 2026-09-29T14:50:08Z (arXiv v1, in-window, exact).
Consumed: abstract + ar5iv HTML full text §§1–6 (sole version v1; PDF bytes NOT consumed
— binary fetch; figures garbled; Appendices B–F and code unread). Claims below are
AUTHOR_CLAIM (paper-reported, not independently reproduced) unless labeled PRIMARY_FACT.

### 仕組み (mechanism)

モデルは文脈を追記専用ログとして扱わず、自身が編集できるファイルとして管理する。
Bash 同期で永続化され、マルチエージェット文脈ファイルへ拡張できる (claim-1,
PRIMARY_FACT: 投稿事実 + 中心的定義のみ; 編集操作の具体 API は UNVERIFIED)。
形式化の骨格 (claim-2 の役割記述; 式の厳密な記号定義は ar5iv §§1–6 に基づくが、
本ドラフト消費範囲では役割レベルのみを主張し、完全な式展開は UNVERIFIED):
Eq.1 追記専用 (append-only) ベースライン遷移、Eq.2 モデル制御遷移
ct+1=fCLM(ct)、Eq.3 prefix-reuse に基づく FLOPs 指標、Eq.4–5 スキル進化の記述、
Eq.6 成功ゲート付き効率 GRPO (<2 successes → 0 報酬)。
Suffix Cache Reuse (Fig.4; 図自体は garbled のため構造的主張のみ)。
診断用 ContextBench 4 タスク: Needle / Sudoku / KV / Log。

### 条件・指標・ベースライン (with denominators)

| 主張 | 分子/分母・条件 | ベースライン・版 |
|---|---|---|
| BrowseComp-Plus +11.4% 精度 / −21.5% FLOPs | 精度差分 (CLM vs Codex 要約); FLOPs は Eq.3 prefix-reuse 指標 | Codex summarization 比較; 別集計で −28.9% の記載もあり (両値を保持、統合しない) |
| 12h EdgeBench +5% / −59% FLOPs | 同上指標 | 同上一連の paper 内比較 |
| BCP 59.4% | ベンチマーク正答率 (分母= BCP 設問集合; 集合規模は UNVERIFIED) | Codex 要約比較 (+11.4% の対応値) |
| TB2.1 matched at 70% FLOPs | 同等成績到達時の FLOPs 比率 70% | Terminal-Bench 系比較対象 (厳密版名は UNVERIFIED) |
| TBLite 73.7% vs 67.0% | 正答率差 +6.7pp | TBLite 上の比較対象 (名称 UNVERIFIED) |
| 数学 Table 1 sweeps OpenEvolve | Table 1 内スイープ (対象範囲 UNVERIFIED) | OpenEvolve |
| EdgeBench-10: 44.6/179 PFLOPs vs 42.3/437 (Qwen3.6-27B) | 精度 / 消費PFLOPs の対 | Qwen3.6-27B |
| 51.0/50.4 vs 42.3 (Claude 4.6) | 同上 | Claude 4.6 (版・設定 UNVERIFIED) |
| swarm +65% same spend | 同一計算支出下の改善率 | swarm 比較対象 (詳細 UNVERIFIED) |
| skill evolution +35.9 ContextBench | ContextBench 上の改善幅 (単位 pp/相対は原文要確認→ UNVERIFIED として保持) | 進化前スキル |
| RL Qwen3.5-9B 28.8→42.5 (Table 2), 1.34 vs 2.19 PFLOPs | 正答率 +13.7pp / 効率比 | Table 2 内ベースライン |
| SCR 65% of SGLang (−35% server compute) | サーバ計算量比 (matched perf 条件) | SGLang |
| skill-optimization steering +35.9pp held-out | ホールドアウト改善幅 | collector abstract 値 (本文対応 UNVERIFIED) |
| online RL Qwen3.5-9B +47.6% / −12% FLOPs BrowseComp-Plus | 同上 | collector abstract 値 (本文対応 UNVERIFIED) |

### 安全性・来歴・ライセンス

編集可能文脈は prompt-injection の持続チャネルになり得る (OpenAI 2026b の
compaction-summary 注入を引用; paper 内の指摘として帰属)。
コード: github.com/facebookresearch/context-language-models (存在の主張;
内容・版ピンは UNVERIFIED)。
資金: Singapore NRF/AIVP + Schmidt AI2050 (謝辞記載として帰属)。
論文ライセンス: CC-BY-4.0 (PDF メタデータ由来, claim-5)。
リポジトリ README ライセンス: UNVERIFIED (r14 消費範囲では未確認; 引用しない)。

### 限界 (causal boundaries)

arXiv アブストラクト + ar5iv 本文 §§1–6 のみ。Appendices B–F・コード・図の数値読み取りは
未消費。再現実験なし。ベースラインの厳密版・設定の多くは原文確認待ち (表に明記)。
「SOTA 証明」として読まない (W40 時期の paper-claim として扱う)。

## 2. Olmo-core 3 — open MoE training stack (Ai2, Oct 1 day-only)

Source: https://allenai.org/blog/olmocore3 (FIRST_PARTY_ANNOUNCEMENT; 日付 day-only
"October 1, 2026", 時刻 UNVERIFIED) + Tech Report + Code (github.com/allenai/olmo-core)
+ interactive demo (narrative.allen.ai/scaling-up-training) — いずれもリンク存在として
消費、内容の深読みは bounded quotes の範囲。
性質の境界 (Sol 確定): 次世代 Olmo MoE のための学習インフラであり、新しい事前学習済み
基盤モデルの重みリリースではない。混同しない。

### 仕組み (pipeline)

FSDP (fully sharded data parallelism) ベースの旧実装から DDP (distributed data
parallelism) ベースへ転換し、expert を GPU 常駐させ、データをルーティングする
("keeps experts resident on GPUs and routes the relevant data to them")。
構成要素: expert parallelism / pipeline parallelism / distributed optimizer /
rowwise expert parallelism / GPU-resident routing / grouped GEMM / MXFP8。
MXFP8 は BF16 比 +21% (条件: 103→95 GiB の記載と対応; 厳密な測定条件は UNVERIFIED)。

### 条件・指標 (vendor-measured, B300, stated configs — 一般化しない)

| 主張 | 分子/分母・条件 | ベースライン・版 |
|---|---|---|
| 47B MoE 52,000 vs 19,400 tokens/s/GPU (~2.7x) | 8x B300 上の予備テスト | 旧 FSDP 実装 (同一 47B) |
| expert 8→128 (4/token, ~3.2B active)、容量 4.6B→47B で throughput −5% 未満 | 同一トークンあたり active 固定の拡張試験 | 拡張前構成 |
| 1.2T total / 58.36B active / 512 GPU で 858 TFLOP/s/GPU (最高観測; random routing) | B300 範囲の複数構成ベンチ | 構成内比較 (外部比較なし) |
| 2.38T short-capacity test | 短時間容量試験 (full training run ではないと明記) | — (能力上限の探索) |
| MXFP8 +21% vs BF16 | スループット比 (103→95 GiB 対応) | BF16 同一構成 |

### ネガティブ結果 (report 内容として保持)

token gerrymandering、expert-LR、input-value timing、overlap slowdowns — いずれも
Ai2 報告の問題記載として扱い、解決済みと読まない (解決状態 UNVERIFIED)。

### 限界

全 throughput 値は Ai2 測定・B300・ stated configs。一般化しない。
HF blog index の Oct 1 記載は傍証であり primary authority ではない。
Tech Report / Code の中身は r14 消費範囲外 (リンク存在のみ)。

## 3. Source→Claim table (P6a)

| 段落主張 | Source | Class | ID anchor |
|---|---|---|---|
| CLM 投稿事実・定義 | arXiv abs + ar5iv v1 | PRIMARY_FACT | evidence:2026-W40:8d261dee1d3bdf14 / claim-1 |
| CLM Eq.1–6 役割・SCR・ContextBench | ar5iv §§1–6 | AUTHOR_CLAIM | 同 task / claim-2 (厳密式展開は UNVERIFIED) |
| CLM 各ベンチ数値 | ar5iv 本文表 | AUTHOR_CLAIM | 同 task / claim-3 (分母・版の欠落は表に明記) |
| CLM 安全性・来歴・CC-BY-4.0 | 本文 + PDF メタ | AUTHOR_CLAIM / PRIMARY_FACT(lic) | 同 task / claim-4, claim-5 |
| Olmo-core 3 リリース事実 (day-only) | Ai2 blog | FIRST_PARTY (day) | evidence:2026-W40:3d0bd53e29394b6b / claim-note §1–2 |
| Olmo-core 3 機構・数値・否定結果 | Ai2 blog bounded quotes | VENDOR_CLAIM | 同 task / excerpt quotes + claim-note §3–4 |

## 4. 日本語品質セルフレビュー (paragraph-level)

- 訳語: data parallelism「データ並列」、pipeline parallelism「パイプライン並列」、
  throughput「スループット」、inference なし。本文の「文脈ファイル」は paper の
  "context as editable file" の直訳として初出で英語併記済み。
- 過剰漢字の回避: 「持続チャネル」は persistence channel の逐語訳として初出限定で使用、
  以降は「持続的な注入経路」と言い換える (本ドラフト内では単発のため維持)。
- 断定の弱め: vendor-measured 値には「〜と報告」「〜の記載」と帰属を付け、
  断定的現在形 (「〜である」) を避けた。UNVERIFIED 箇所は条件文にせず明示した。
- 残課題: Eq.1–6 の厳密な数式日本語化は原文確認待ち (無理な敷衍をしない)。

## Appendix COND (separately labeled; NOT part of 28; NOT drafted as subsections)

- COND-A AstaBrief: r13 note の訂正済み技術内容 (SFT/DPO lineage、密度フィルタ、
  51.1s/178.5s、2025-vintage、license split) を将来 P6a 第三 PRIMARY 候補として参照
  可能だが、本ファイルでは節を起こさない (canonical HOLD のため)。
- COND-B AutoSynthData: r14 note の verifier/gate 内容を将来 P6a 第四 PRIMARY 候補として
  参照可能だが、本ファイルでは節を起こさない (同上)。
