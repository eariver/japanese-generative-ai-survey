# P6a deep draft r15 — ContextLM + Olmo-core 3 (NON_CANONICAL successor)

Status: `TECHNICAL_PREP_R15 / NON_CANONICAL / NOT_ARCHITECTURE / NOT_READER_PROSE`
Successor of (r14 preserved immutable): `../technical-prep-r14/p6a-deep-draft.md`
Covers (ordinary 28 only): `candidate:2026-W40:92241424368e1305` (ContextLM, PRIMARY)
+ `candidate:2026-W40:a5143ea24719b616` (Olmo-core 3, PRIMARY).
COND-A/B appear ONLY in the labeled appendix, sectionless (canonical HOLD).
New r15 source retrievals (2026-10-10 JST evening, transport-local /tmp, uncommitted):
ar5iv HTML 2609.37725 (417,994 B — equations/tables/abstract verified);
Ai2 blog olmocore3 (1,166,521 B — MXFP8/negatives/mechanisms verified);
Tech Report landing allenai.org/papers/olmocore3 (HTTP 200, 16.5 MB shell — body NOT
text-accessible, no PDF link, see §4 NOT-retrievable); CLM repo LICENSE via raw
(C BY-NC 4.0 text, main-as-of-retrieval, commit unpinned).
Every quantitative claim cites primary URL + revision/section/table. `VERIFIED` below
means article/paper text confirmed — NOT independent replication. Never cite as
HUMAN APPROVED; never merge into `architecture-v2.json` / `main.tex` (not written).

## 1. ContextLM (arXiv:2609.37725v1, Shao et al. 13 authors, UW/Meta/MIT/Trillium)

Paper clock: submitted 2026-09-29T14:50:08Z, sole version v1 (PRIMARY_FACT).
Consumed: abstract + ar5iv full-text §§1–6 + §5 tables (PDF bytes unconsumed;
figures garbled; Appendices B–F and code unread — limits kept).

### なぜファイルなのか (why/how)

従来のハーネスは文脈管理を外部制御 (external harness control) に置き、要約・圧縮・
切り捨てをモデル外の決め打ち手順で行う。CLM はこの制御をモデル自身の振る舞い
(intrinsic model behavior) に移す。文脈をファイルとして扱い、モデルが無制限の更新
(unrestricted updates) を加えられるようにすることで、何を残すかの判断自体を学習
可能にする。複数エージェントの文脈がファイルとして共存する系へ自然に拡張できる。
Bash 同期で永続化される (W40 Evidence claim-1 の範囲; 同期プロトコルの詳細は
UNVERIFIED)。要約型 (append-only/summary) との対比は式で定義される (§1.1)。

### 形式化 (Eq.1–6; exact symbols verified from ar5iv alttexts)

- Eq.1 追記専用ベースライン: `c_{t+1} = c_t ⊕ f^{LM}_θ(c_t)` — 既存文脈に生成分を
  連結するのみで、過去の書き換え・削除はできない。
- Eq.2 モデル制御遷移: `c_{t+1} = f^{CLM}_θ(c_t)` — 次ターン文脈全体がモデルの出力。
  ターン間の同期 (sync back to next turn) はこの遷移の実行として理解される
  (実装詳細 UNVERIFIED)。
- Eq.3 prefix-reuse FLOPs 指標:
  `FLOPs_{prefix-reuse} = FLOPs_{prefill}(unmatched context suffix) + FLOPs_{decode}(generated tokens)`、
  すなわち「最初の prefix 不一致以降のトークンの再プリフィル計算量 + 新規出力トークンの
  デコード計算量」。したがって wall time でも full-cache hit-rate でもない。
  文脈再利用の良し悪しを計算量で測るための定義であり、一致 prefix 部分は課金されない。
  r14 までの「FLOPs 削減」記述はすべてこの定義下の値である。
- Eq.4 スキル条件付き遷移: `c_{t+1} = f^{CLM}_θ(c_t; s)` — 進化した自然言語スキル
  指示 s によるステアリング (in-context 側の学習)。
- Eq.5 (スキル進化ループの記述; 厳密な更新式の全文引用は ar5iv §§4–5 の範囲外のため
  UNVERIFIED とし、役割のみ主張)。
- Eq.6 成功ゲート付き効率 GRPO (F02 correction — exact symbols):
  成功群 `G_g^+` 内の軌跡 i について
  `A_i^{eff} = clip((c̄_g − c_i)/c̄_g, −1, 1)`、群外は 0。
  群内の成功軌跡が 2 本未満の場合、全軌跡に `A_i^{eff} = 0`。
  続く本文: "the efficiency signal only re-ranks among successful trajectories by
  inference cost"、統合式 `A_i = A_i^{out} + w_eff A_i^{eff}`,
  "to encourage trajectories that are both correct and efficient"。
  RL 信号への意味: 効率項は成功者間の推論コスト順位付けにしか働かず、成功が 1 本
  以下の群では完全に黙る。その場合も `A_i^{out}` は残るため、 total `A_i` がゼロに
  なるとは限らない — r14 以前の「<2 successes → 0 (全体)」という読みは誤りであり、
  ゼロになるのは効率アドバンテージ `A_i^{eff}` の側だけである。効率シグナルは
  「正解の中で安い順に並べ替える」再ランキングであり、正誤判定そのものは
  `A_i^{out}` が担う。

### Suffix Cache Reuse (SCR) — mechanism and limits

"reuses cached states beyond the matching prefix to reduce re-prefilling while
empirically preserving task performance" (abstract + §1)。通常サービングの
prefilling / re-prefilling に対し、一致 prefix を超えたキャッシュ状態を使い回して
再プリフィルを減らす。効果は task 性能の経験的保持 (empirically preserving) を条件
とする主張であり、無条件の等価性ではない。サーバ計算量 −35% (SGLang 比、matched
perf 条件) はこの機構の報告値。実装・適用条件の詳細は UNVERIFIED。

### 測定値 (paper-defined; denominators/baselines/sections kept separate)

| 主張 | 定義・分母・条件 | ベースライン・出典箇所 |
|---|---|---|
| BCP 59.4% (32K context), +11.4% relative | 正答率の相対改善 (relative と paper が明記) | 最強 baseline Codex-style summarization (§5) |
| −21.5% prefix-reuse FLOPs | 上記対比の計算量差 | Codex-style summarization (§5; 次点の内の1) |
| −28.9% prefix-reuse FLOPs | 同上 | MEM1 (次点の内の2; 両者を統合しない) |
| TB2.1: 最強と同等精度 at 70% FLOPs | 同等到達時の計算量比 | Codex-style summarization (§5; 導入部の 29.5% fewer とは記載箇所が別 — 統合せず両記) |
| TBLite 73.7% vs 67.0% at 91% FLOPs | 正答率差 +6.7pp + 計算量比 | 同上 (§5) |
| 数学: OpenEvolve 比 up to 16.8% (Heilbronn), 3.0% (circle packing) | タスク別改善率 | specialized evolution harness (§5/Table 1系) |
| 12h EdgeBench (10-task subset): +5% / −59% FLOPs | 正答率・計算量 | Codex-style summarization (abstract + §5) |
| 24h 6-repo swarm: +65% end-to-end speedup at same compute | 同一計算支出下の速度向上 | 同上 |
| skill steering: up to 35.9 POINTS (held-out, context-management task) | 単位は points (%, pp への読み替え禁止) | 進化前スキル (abstract) |
| online RL Qwen3.5-9B: 28.8→42.5 BrowseComp-Plus (+13.7pp) | 正答率 | Table 2 内 baseline |
| 上記 RL: 同 recipe の Codex-summary harness 比 +0.4 points, −38.8% FLOPs | 同一学習手順下の対比 | Codex-style summary harness (§4SS/§5) |
| 抽象の +47.6% / −12% FLOPs | 相対表記 (paper のまま; pp 化しない) | §4 導入部の RL 記述 |
|統制条件: shared Mini-SWE-Agent backbone, out-of-box (no training), Qwen3.6-27B, 32K context, 100-turn cap; 比較対象 MEM1 / Self-Compact / ACM / RLM (§2/§5)。ContextBench の評価対象: Mini-SWE-Agent (base, CM なし), Codex-style Summary (OpenAI 2026a), Context Folding, RLM, Self-Compact, ACM + CLM (§3; 詳細・定性例は Appendix D のため UNVERIFIED)。

### 安全性・来歴・ライセンス (per-artifact, revisions stated)

編集可能文脈は prompt-injection の持続チャネルになり得る (OpenAI 2026b の
compaction-summary 注入を引用する paper 内指摘として帰属; 対策の有無 UNVERIFIED)。
コード github.com/facebookresearch/context-language-models (存在のみ)。
資金 Singapore NRF/AIVP + Schmidt AI2050 (謝辞記載)。
ライセンス分離 (F03 対応): paper = CC BY 4.0 (arXiv PDF メタデータ由来, v1) /
repo = CC BY-NC 4.0 (LICENSE ファイル本文を r15 に raw 取得・確認; 対象 revision は
main-as-of-2026-10-10、commit SHA unpinned — 特定 commit の指定引用はしない)。
どちらがどちらに適用されるかを混同しない。

## 2. Olmo-core 3 (Ai2 blog Oct 1 day-only + bounded excerpts)

性質境界: 次世代 Olmo MoE の学習インフラ。重みリリースではない。
Source: https://allenai.org/blog/olmocore3 (1.17 MB page retrieved r15, full-read;
時刻 day-only)。Tech Report/Code/demo はリンク存在のみ (Report 本文は r15
未取得 — §4 参照)。

### なぜ DDP 常駐なのか (dispatch/communication)

旧実装 FSDP はモデル全体と学習状態を全 GPU でシャード保持する。Olmo-core 3 は DDP
ベースに転換し expert を GPU 常駐させ、関連データをルーティングする
("keeps experts resident on GPUs and routes the relevant data to them")。
効果の向き: 全 GPU が全モデルを持つ必要がなくなり (scale out)、
ルーティング先へのデータ配送コストと expert 計算の実行コストが主要項になる。
Rowwise expert parallelism はルーティング済みデータを expert 入力バッファへ直接配置
し、並べ替えの余分を最小化。GPU-resident routing はルーティングメタデータを GPU 上に
置き、CPU がコピー待ちなくキューできるようにする。Grouped GEMM は多数の小 expert
計算を束ねて GPU 実行効率を上げる。分散 optimizer・pipeline parallelism・overlap は
構成要素として言及 (内部実装コードは読まない — 捏造しない)。

### MXFP8 (F04 — controlled config, exact)

"We measured MXFP8's effect on end-to-end training throughput in a controlled
benchmark on four NVIDIA B300 GPUs, with work distributed uniformly across experts.
With MXFP8 enabled across the parts of the system where it helped most, training
throughput was about 21% higher than with BF16 ... while peak active memory fell from
103 GiB to 95 GiB." 構成: B300×4、均一 expert 負荷 (equal expert load)、
対照 BF16 (higher-precision baseline)、適用箇所は効果のあった部分のみ
(where it helped most — 全面適用ではない)。増分の主因は feed-forward 計算と
expert 間データ移動であり attention 単独ではない。判定: controlled benchmark
(統制試験) であり、観測的 anecdote ではない — ただし B300×4・均一負荷という条件付き
であり、他構成への一般化はしない。数値形式の注意: MXFP8 は一部値を少数ビットで表す
低精度形式で、変換コストを上回る場合に計算・GPU 間データ移動を減らす
(as long as those savings outweigh the cost of converting — 条件文を保持)。

### 測定の分離 (47B measured vs 1.2T routing vs 2.38T capacity)

- 47B measured: 8×B300 予備試験、52,000 vs 19,400 tokens/s/GPU (~2.7x vs 旧実装)。
- expert 拡張: 8→128 (4/token, ~3.2B active)、容量 4.6B→47B で throughput −5% 未満。
- 1.2T total / 58.36B active / 512 GPU、最高 858 TFLOP/s/GPU (random routing):
  システム測定であり、random routing 条件下の値。モデル品質の主張と読まない。
- 2.38T: short-capacity test ("a short-capacity test rather than a full training
  run" と明記) — 完了した大規模学習ではない。混同しない。

### ネガティブ結果 (mechanism/attempt/failure/evidence-limits)

1. Token gerrymandering: バランス促進 intended の score が改善する一方で実 workload
   が不均衡化 — 指標と実態の乖離という失敗様式 (blog が命名・説明)。
   試した最適化: routing balance score。観測: 失敗。示す範囲: 測定方法論への警告。
2. Expert learning-rate reduction: token 処理量の少ない expert の更新幅
   (learning rates = 更新サイズ) を下げる試み — テストしたモデル群で改善なし。
   他群への一般化は示されない。
3. Input-value timing: 同一形状でも処理値で GPU 計算時間が変わる —
   性能比較は shape 一致に加え input value 一致が必要 (比較方法論への制約)。
4. Comm/comp overlap (separate streams): 常に高速化せず、一部試験で end-to-end
   減速 — "more overlap does not necessarily mean higher throughput"。
   Report が採用/不採用の検討と併記 (blog の範囲; Report 本文未読のため詳細
   UNVERIFIED)。

## 3. Source→Claim table (P6a r15)

| 段落主張 | Primary source + pin | Class |
|---|---|---|
| CLM 投稿事実・定義 | arXiv abs 2609.37725 + ar5iv §§1–2 (v1, 2026-09-29T14:50:08Z) | PRIMARY_FACT |
| Eq.1/2/3/4/6 記号・定義文 | ar5iv alttexts S4.E1–E6 + §4SS2 ("fewer than two…", "only re-ranks…", "both correct and efficient") | AUTHOR_CLAIM (text-confirmed) |
| Eq.5 全文 | ar5iv §§4–5 (今回未引用) | UNVERIFIED (役割のみ) |
| BCP/TB/TBLite/EdgeBench/swarm/RL 数値 | ar5iv abstract + §5 (Table 1/Figure 5系; BCP 59.4%/11.4% relative/21.5%/28.9%; TB2.1 70%; TBLite 73.7/67.0/91%; RL 28.8→42.5/+0.4/−38.8%; steering 35.9 points) | AUTHOR_CLAIM (text-confirmed) |
| SCR 機構・−35% | ar5iv abstract + §1 ("beyond the matching prefix…empirically preserving") | AUTHOR_CLAIM |
| paper CC BY 4.0 / repo CC BY-NC 4.0 | arXiv PDF メタ (v1) / GH raw LICENSE (main, 2026-10-10取得, commit unpinned) | PRIMARY_FACT (artifact-scoped) |
| Olmo-core 3 機構・MXFP8・拡張・negatives | allenai.org/blog/olmocore3 (Oct 1 day-only; bounded quotes) | VENDOR_CLAIM (controlled箇所は明示) |
| Tech Report/Code/demo 中身 | リンク存在のみ (Report 本文未取得) | UNVERIFIED |

## 4. NOT retrievable (exact access record)

- arXiv PDF バイナリ (r4 で FAILED 済み; ar5iv rendering で代替、同一 v1)。
- ar5iv 図表画像・Appendices B–F・コード (r4 範囲外、今回も未取得)。
- Tech Report 本文: landing HTTP 200/16.5MB を取得も viewer shell で本文テキストなし
  (PDF リンクなし・MXFP8 言及なし) — 内容未取得、内部捏造なし。
- CLM repo commit SHA pin (LICENSE は main 現状確認のみ)。
- 上記以外の Eq/表セル: UNVERIFIED のまま残す。

## 5. 日本語品質セルフレビュー

- 訳語: prefix-reuse「接頭辞再利用」(初出英語併記)、re-ranks「再順位付け」、
  routing「ルーティング」、workload「作業負荷」。「効率アドバンテージ」は
  efficiency advantage の直訳として式文脈に限定。
- 断定制御: vendor/paper 値は「〜と報告」「〜と明記」と帰属化。統制条件
  (B300×4・均一負荷・BF16対照) は数値と一体で記述し、切り離し引用を防ぐ。
- 単位の厳密化: 35.9 は points と明記し %/pp 化を禁止、11.4% は relative と明記。
  29.5% (導入部) と 70% ( §5) は統合せず両記。
- 残課題: Eq.5 全文・Appendix D/E の日本語化は原文確認待ち。

## Appendix COND (labeled only; NOT subsections; NOT in 28)

- COND-A AstaBrief / COND-B AutoSynthData: r13/r14 の訂正済み内容を将来参照可能だが
  本ファイルに節を起こさない (canonical HOLD)。
