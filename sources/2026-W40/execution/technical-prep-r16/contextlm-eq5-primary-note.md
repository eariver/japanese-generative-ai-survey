# ContextLM Eq.5 primary note r16 — focused noncanonical supplement (A04)

Status: `TECHNICAL_NOTE_R16 / NON_CANONICAL / NOT_ARCHITECTURE_SECTION`
Scope: Eq.5 ONLY (+ its §4.2 surroundings for the train/dev/test split and the
in-context vs in-weights distinction). NOT a redevelopment of r15 P6a/P6b
(preserved immutable). r15 Eq.6 interpretation and all other metrics are UNCHANGED
by this note (verified relationship below, no modification).
Primary source: arXiv:2609.37725v1, §4.2 "In-Context Learning and Reinforcement
Learning for CLMs", Eq.5 with anchor `S4.E5`.
Retrieved r16: `https://ar5iv.labs.arxiv.org/html/2609.37725` (ar5iv rendering of v1),
2026-10-10 JST, 417,994 bytes, SHA-256
`a568b7e1100aefec37b2f610ec1c9df0f21552a2448c2fd110ae4af5972a382c`
(transport-local, uncommitted). Symbols transcribed from equation alttexts +
surrounding prose (both verified, quoted below). Status: fully resolved
(not `A04_PARTIAL` — the equation IS accessible and quoted).

## Exact equation (transcribed, not inferred)

`s* = argmax_s E_{x∼D}[ R( τ(x; s) ) ]` …(5)

Variable definitions (paper's own, §4.2):
- `s` (blue in paper): an in-context instruction or skill document
  ("Let s denote an in-context instruction or skill document").
- `τ(x; s)`: the trajectory induced by Eq.4 on task instance x
  ("For task instance x, let τ(x; s) be the trajectory induced by Eq. 4").
- `R(τ)`: a trajectory-level reward.
- `D`: the task-instance distribution the expectation runs over
  (instantiated as data splits below — paper's own split names kept).
- Trailing clause: "while keeping everything else fixed" — i.e. model parameters
  are FROZEN during this optimization (in-context learning, not weight training).

## What is optimized (in natural Japanese)

最適化対象はスキル文書 s 自体であり、モデルの重みではない。タスク分布 D から
引いた入力 x に対し、スキル s 付きで Eq.4 (`c_{t+1} = f_θ^CLM(c_t; s)`) に従って
生成される軌跡 τ の軌跡レベル報酬 R の期待値を最大化する s* を選ぶ。
「他はすべて固定」の下での選択であり、重み更新を伴わない in-context 側の学習である。

## Training / development / held-out test の使い分け (paper's own names kept)

実装は prompt-evolution loop (Agrawal et al., 2026):
1. 各ラウンドでエージェントは **training split** 上で rollout を生成し、
   proposer model が trace から候補スキルを生成する。
2. 候補は **development split** 上で評価され、次ラウンドのスキルが選ばれる。
3. 進化終了後、最終スキルを **held-out test split** 上で一度だけ評価する。
Optimizer は stronger external model (assisted evolution) でも agent 自身
(self-evolution) でもよい — いずれも文脈内での進化であり重みは不変。
用語の注意: paper は training / development / held-out test の三名を用いる。
一般的な train/dev/test との対応付けは行わず、paper 名のまま記述する。
35.9 points の報告 (abstract) はこの進化ループによる held-out 精度改善
("improving held-out accuracy by up to 35.9 points on a context-management task
while reducing compute") であり、RL (Eq.6) の 28.8→42.5 とは別系列 — 混同しない。

## Skill evolution (in-context) vs RL parameter training (Eq.6) — explicit distinction

- Skill evolution (§4.2 前半, Eq.4–5): 最適化変数は自然言語スキル s、重み θ は固定。
  学習は文脈内に留まる (in-context learning)。評価は上記 3-split 運用。
- RL (§4.2 後半 "Reinforcement Learning for CLMs", Eq.6): stepwise GRPO で重みに
  内面化する (internalize them in model weights) パラメータ学習。
  効率項 `A_i^{eff}` は成功群内の推論コスト再順位付けのみ (r15 検証済み、
  本ノートで変更なし)。
- 両者は §4.2 の前後半で別の見出しの下に記述される独立の学習様式であり、
  Eq.5 を RL の式と読むこと、逆に Eq.6 をスキル進化と読むことは誤りである。

## Relationship to r15 Eq.4 (verified, unchanged)

Eq.4 `c_{t+1} = f_θ^CLM(c_t; s)` は Eq.5 の軌跡生成器 (τ の定義に Eq.4 を引用と明記)。
r15 の Eq.4 記述と一致し、変更は不要・実施しない。

## Source→Claim anchors (this note)

| Claim | Pin |
|---|---|
| Eq.5 symbols + "while keeping everything else fixed" | ar5iv S4.E5 alttext + §4.2 prose (retrieved r16, hash above) |
| s/τ/R/D definitions, Eq.4 reference | §4.2 "Steering…" + "Evolving…" paragraphs |
| train/dev/held-out loop, assisted/self | §4.2 "In our implementation…" paragraph (Agrawal et al., 2026) |
| in-context vs in-weights split | §4.2 subsection halves ("…in context or in weights", "Reinforcement Learning for CLMs") |
| 35.9 points held-out | abstract (r15-verified, unchanged) |

## Still UNVERIFIED (unchanged from r15)

arXiv PDF bytes, figures, Appendices B–F, code, CLM repo commit pin, Eq.5 以外の
未引用セル。本ノートは Eq.5 のみを解決し、他を開いたまま残す。
