# Muse candidates for Sol review — TS-002 Issue #543 r2

Status: `CANDIDATE_FOR_SOL_REVIEW / NO_MUSE_DECISION`
Date: 2026-09-26 JST
Rule: unmapped or semantically uncertain occurrences are left UNCHANGED in `main.tex`. No proposed final Japanese wording is given (Sol editorial decision). Canonical English is quoted only when directly visible in already-consumed sources.

## C-001 — 自然さ得点 (Lyria context, outside SOL-S-005 btd110 scope)

- Term: 自然さ得点
- Sentence: `A/B選好や可用率や自然さ得点のベンダー図表は、ベンダー主張として引用し、方言や一部言語の例外などの限定とともに読む。` (preceded by Lyria hub / Stable Audio continuation context)
- Section: 音楽：制作手順としてのworkflow記録 (L1108)
- Citation: btd110,btd111,btd114,btd115,btd116,btd112,btd113
- Suspected canonical English: none visible for this metric in this context (Lyria hub / Stable Audio, outside btd110 Seed Audio 1.0).

## C-002 — 群化後継 ×2 (method-vs-model unclear)

- Term: 群化後継
- Sentence (L499): `群化後継の数値的主張は表の欠落により本稿では扱わず、機構の継承関係のみを記録する。`
- Sentence (L535 table): `群化後継 | 群化符号＋反復回避サンプリング（機構のみ） | 数値は未確立...`
- Section: ゼロショット話者複製 / VALL-E 2 mechanism
- Citation: btd059
- Suspected canonical English: Grouped Code Modeling (method) vs successor model ambiguous.

## C-003 — 距離/乖離/整合 outside btd065-only number-bearing scope (bulk)

Sol map authorizes only btd065-only number-bearing identities (applied). All other occurrences left unchanged. Representative entries (full enumeration available via grep):

- L662-s2: `第二に、整合の軸である。$1.28$や$0.31$や$0.29$は各フレーム内で比較できない` (btd066,btd068) — FAD/KLD/CLAP family but source binding mixed.
- L589 non-trio: `距離$47.68$、指標$8.13$と$4.01$、乖離$1.59$と$2.52$、距離$1.96$と$7.75$、全体$45.0$` (btd067) — FD/OVL/REL family per SOL-M-004 but exact number-to-metric binding for `$45.0$` (REL candidate), `$47.68$`, `$8.13$/$4.01$`, `$1.59$/$2.52$`, `$1.96$/$7.75$` not unambiguously labeled.
- L593: `$25.79$` (btd067) — same.
- L607: `乖離$1.59$ほか` (btd067 table) — same.
- L613: `開放距離$103.66$や$101.11$、乖離$2.14$、整合$0.29$` (btd068) — FD_openl3 family but exact binding unclear.
- L660/L685 summaries (btd066/btd067/btd068 mixed) — same.
- All remaining numberless generic 距離/乖離/整合 — generic distribution/metric nouns, no identity at stake.

## C-004 — 集合 variants (10)

- 非構造集合 L192/L239 (btd015/btd016) — unstructured-set evaluation; English not visible.
- 厳選千万部分集合 L705/L753 (btd075) — LVD-10M-F family but genitive/continuative variants of the authorized L807 sentence.
- 厳選千万が網全体を上回る L768 table (btd075) — short variant.
- 厳選千万の序列 L819 (btd074/btd075/btd124) — ranking variant.
- 網全体 L753/L768 (btd075) — unfiltered LVD-10M in variant sentences.
- 生成集合 L965/L997, 大規模実集合 L965, 試行集合 L965, 実集合 L997 (btd083/btd084) — FID definition/Eval sets; dataset-vs-statistical-set unclear.
- Note: L807 `厳選千万部分集合が網全体を上回る報告は` was resolved by authorized SOL-V-003 LVD rewrite (not a candidate).

## C-005 — 標本ごとの条件付き場 (L233, btd027)

- Sentence: `Flow Matching（フローマッチング）はこの隘路に対し、周辺場の代わりに標本ごとの条件付き場へ回帰するsimulation-free学習（シミュレーション不要の学習）を置き、勾配の等しさを要点とする転換を示した。`
- Section: 生成パラダイムと目的関数 / 流れへの再定式化
- Suspected canonical English: not visible beyond 条件付き場.

## C-006 — 開放重みの混合専門家配置 (L705)

- Sentence context: `閉鎖頂点と開放重みの混合専門家配置が能力と workflow の分岐を示し` (now: 非公開モデルと開放重みの混合専門家配置が…)
- Section: video/overview (btd077/btd124/btd138)
- Suspected canonical English: Mixture-of-Experts (MoE); particle-variant of the mapped form, left for Sol.

## C-007 — 一括要点標本 (L722, btd073)

- Sentence: `短断片中心であり、一括要点標本は高費用で、運動不足や低速高記憶サンプリングの問題が残る。`
- Section: データ効率化代償
- Note: reordered variant of prohibited 要点一括標本; Sol decides identity.

## C-008 — 開放凍結 (L1101)

- Sentence context: `開放凍結・API専念・廃止の方向は製品の事実であり` (btd123/btd126/btd127/btd128 lifecycle)
- Suspected canonical English: none (open-freeze direction).

## C-009 — 公開系列の線引き (L158)

- Sentence: `公開系列の線引きは二・二までであり、それ以降は応用接続のみである。`
- Section: compression claims (no autocite on sentence)
- Note: Wan2.2 lineage-adjacent; Sol decides.

## C-010 — 平滑化 math-smoothing (6)

- L233/L239 `振る舞いの悪い場には平滑化を要する` (btd028); L376 `潜在最適化は過度の平滑化を招く` (btd046); L395 table `継ぎ目・色ずれ・平滑化` (btd046); L433 `継ぎ目と色ずれと平滑化を伴い` (btd046); L926 `写実と過平滑の交換があり` (btd081).
- Mathematical smoothing/oversmoothing, not motion evaluation. No source-visible English.

## C-011 — 開放線 non-Wan senses (RETAIN-noted, for completeness)

- L39 (btd125, Wan hub evidence-boundary note), L688 (btd068 music Stable Audio Open context) — different meanings from the Wan2.2 frozen claim; left unchanged.

## C-012 — Seed-TTS descriptor variant 高忠実 vs 高品質 (FYI, no edit)

- Pre-existing (untouched, outside Sol map scope): `Seed-TTS（多用途・高忠実音声生成）` subsection title + `Seed-TTS（多用途・高忠実音声生成）は難発音指示に弱く…` body (btd061/btd062 context).
- r2 applied per SOL-S-004: `Seed-TTS（多用途・高品質音声生成モデル）` (L441) + `多用途・高品質音声生成モデル` (L521/L523/L544).
- Both variants now coexist. No proposal; Sol decides whether to unify.
