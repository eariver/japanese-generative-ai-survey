# r13 source-supported deepening matrix (per PRIMARY: question → source → denominator → mechanism → negatives → new block)

Scope: approved 28 selected / 7 packages unchanged. New blocks are marked [NEW]; reused card facts are not repeated here unless their denominator is newly clarified. Lengths are estimates (Japanese chars).

## P1 (Wonder / Argon)
- PRIMARY Wonder — Q: Active MemoryとActive Focusは動作上どう違うか。 Source: Meta announcement (memory=会話またぎ保持 / focus=遂行注意; accepted card C2). Denominator: n/a (definitions). Negatives:保持範囲・削除手段の詳細は未公開. Block: r12 q1-03 (kept). ~200字.
- PRIMARY Argon — Q: なぜ事例の厚みが利用の出発点になるのか。 Source: Google announcement (Chrome/ADK/xTB/Gemma E2B vendor figures; accepted card C2). Negatives: 測定条件の開示は限定的. Block: r12 q1-08 (kept). ~200字.
- PRIMARY Argon/Minecraft — Q: 27h14mの失敗様式は何を示すか。 Source: arXiv 2610.22319 (27h14m, 2,783 programs, 605 deaths, single trial, structured-only; accepted card C7). Denominator: deaths/programs per single run. Negatives: 単一試行・非視覚. Block: [NEW P1-F1] 失敗履歴の読み (~180字).
- SUPPORTING: なし (P1 has 2 PRIMARY only).

## P2 (Maia 300 / LFM2.5)
- PRIMARY Maia — Q: UMA→NUMAとダイ分離は何を変えるか。 Source: Azure deep-dive (accepted card C1/C2). Negatives: 効率基準無名. Blocks: r12 q2-02/q2-09 (kept).
- PRIMARY Maia — Q: prefill/decode分離と96トレイ167kWは運用上何を意味するか。 Source: same deep-dive (accepted card C3/C4). Block: r12 q2-15 (kept, m04-relevant but substantive).
- SUPPORTING LFM — Q: なぜ温度つき16種表が分母の手本になるか。 Source: Liquid AI blog (accepted card C3). Denominator: per-bench temps; 27.69 vs 8.72 next. Negatives: 発行者計測. Block: [NEW P2-F1] 温度・バッチ・ハード開示の作法 (~180字).
- SUPPORTING LFM — Q: 288GB級HBMと文脈長の関係は。 Source: same + HBM4 288GB@18TB/s (accepted card). Block: [NEW P2-F2] 物理量と文脈長の関係 (~150字).

## P3 (Spark / Beam / Nemotron + Granite/MiniCPM/FLUX)
- PRIMARY Spark — Q: 2×M5 Ultra実装像は何を示すか。 Source: Meta announcement (accepted card C2). Block: r12 q3-02 area (kept).
- PRIMARY Beam — Q: LICENSE全文は何を保証し何を残すか。 Source: repo LICENSE file full text (accepted card C3, F01-corrected). Negatives: 第三者条項残存. Block: r12 q3-04 rewritten (F01).
- PRIMARY Nemotron — Q: MTP受理長の正体とLiLiCorr/QAD/再利用/配置の機構。 Source: NVIDIA developer blog live read S1 (MTP multi-token verify; LiLiCorr 2.3x DGX Spark; QAD match-BF16 + NVFP4 KV; prefix caching + Mamba states; Dynamo 16×B200 8x users −85%; MOPD teacher scoring). Negatives: 復号条件・ドラフト長は未確認 (M01). Blocks: [NEW P3-F1..F5] (~200字 each).
- SUPPORTING Granite/MiniCPM/FLUX — comparative roles only (kept; tag-only vs full-file tiers).

## P4 (Codex / Scion / HydraFusion + gates/Decider)
- PRIMARY Codex — Q: 保守流儀の移転可能性の留保は何か。 Source: OpenAI engineering post (accepted card C1/C2: single-team internal). Negatives: 他条件での再測定なし. Block: [NEW P4-F1] 生存・移転の注意 (~170字).
- PRIMARY Scion — Q: WAL/ロックフリー/キャッシュはなぜ速いか。 Source: Anthropic post (accepted card C3/C4). Blocks: r12 q4-05 + wave additions (kept; m04 dups r4-16/r4-17 DROPPED).
- PRIMARY HydraFusion — Q: Maxの段差は何を選ばせるか。 Source: GitHub announcement (accepted card: effort tiers, Pro+). Block: [NEW P4-F2] Max段差 (~150字).
- SUPPORTING autofix/AI Scan/Decider — guardrail roles (kept; F02-cleaned refs).

## P5 (unintended / distillation + ECDSA / METR)
- PRIMARY unintended — Q: 誰が何をどう調べたか。 Source: Anthropic report + Oct 12 correction + July scan (accepted card C1/C2/C4) + da.gd operator (partial). Negatives: 自己評価範囲. Block: [NEW P5-F1] 調査主体の層別 (~180字).
- PRIMARY distillation — Q: 10–100xと<0.1%の分母は何か。 Source: Anthropic report (accepted cards C1–C4). Negatives: 迂回可能・耐久性未確認. Blocks: kept (q5-05/06 + wave).
- SUPPORTING ECDSA/METR — method closure + access-only (kept; m03/m05 wording fixed).

## P6 (wetlab / Earth / Deep Review + Rosalind)
- PRIMARY wetlab — Q: 131/311と8クローンは別工程か。 Source: aptamer sandbox excerpt (accepted card C2: trajectory + 8-clone titrations, no linkage). Negatives: 連関は未確立. Block: r12 q6-02 + q6-10 REWRITTEN (M02: stages separated).
- PRIMARY wetlab — Q: FAP単一標的の意味。 Source: r8 wetlab blog excerpt (FAP single-digit nM/8.6x; non-infectious testbeds). Block: [NEW P6-F1] 標的と安全の条件 (~160字).
- PRIMARY Earth — Q: 4条件比較は何を分離したか。 Source: arXiv 2610.15750 live read S2 (§3 configs; $0.199 vs $0.167 +10.5pp; 3→52→63; searches 7.0→3.2; EE 54/38). Blocks: [NEW P6-F2/F3] (~200字 each).
- PRIMARY Earth — Q: golden workflowと飽和の扱い。 Source: same (§4: 3 experts blind; 4 unreconciled kept; UnivEARTH 87–94 saturated; 25/76 + 85/220 splits released). Blocks: [NEW P6-F4/F5] (~180字 each).
- PRIMARY Deep Review — Q: PATの三段階因果は何か。 Source: SPOT paper (accepted card). Block: kept.
- SUPPORTING Rosalind — access/pricing only (kept; m04 r6-12 dropped as dup).

## P7 (GLM-Legal / ASPIRE + Glimpse)
- PRIMARY GLM — Q: ValsとZ.ai図の行為主体は誰か。 Source: Vals page (independent) vs Z.ai announcement (vendor chart omitting 6 higher). Negatives: 方法・再現の限界. Blocks: kept (q7-01/02 + wave).
- PRIMARY ASPIRE — Q: 凍結基盤依存は何を狭めるか。 Source: repo + Jun-30 paper background (accepted card C1/C3). Negatives: 弱モデル未検証. Block: kept (q7-13).
- SUPPORTING Glimpse — Q: API存在と仕様根拠は別か。 Source: Elorian blog (specs) + OpenRouter listing (existence only). Block: [NEW P7-F1] 存在と内容の分離 (~150字).
- (m04: r7-11 VLA paragraph DROPPED as duplicate of r7-06 pricing.)

## Deletions with reason (m04/M03 space discipline)
- P1 r1-15 (Argon hike) → merged into r1-07 pricing block; freed ~150字.
- P2 r2-13 (N2P split) → essence kept in r2-02; freed ~150字.
- P4 r4-16/r4-17 (WAL/API dups) → kept r4-05/r4-14; freed ~300字.
- P6 r6-12 (Rosalind areas) → kept r6-07; freed ~150字.
- P7 r7-11 (VLA) → kept r7-06 line; freed ~130字.
Net: −6 blocks (~880字) + 15 new blocks (~2,700字) → paragraph chars ≈ 18,165 + ~1,800 ≈ ~20,000 (exact count reported after build; no quota claimed).
