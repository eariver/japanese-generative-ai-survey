# r14 source-supported deepening matrix (per PRIMARY: question → source → denominator → mechanism → negatives → new block)

Scope: approved 28 selected / 7 packages unchanged. New blocks are marked [NEW]; reused card facts are not repeated here unless their denominator is newly clarified. Lengths are estimates (Japanese chars).

## P1 (Wonder / Argon)
- PRIMARY Wonder — Q: Active MemoryとActive Focusは動作上どう違うか。 Source: Meta announcement (memory=会話またぎ保持 / focus=遂行注意; accepted card C2). Denominator: n/a (definitions). Negatives:保持範囲・削除手段の詳細は未公開. Block: r13 s1-03/s1-04 (kept). ~200字.
- PRIMARY Argon — Q: なぜ事例の厚みが利用の出発点になるのか。 Source: Google announcement (Chrome/ADK/xTB/Gemma E2B vendor figures; accepted card C2). Negatives: 測定条件の開示は限定的. Block: r13 s1-08/s1-09 (kept). ~200字.
- PRIMARY Argon/Minecraft — Q: 27h14mの失敗様式は何を示すか。 Source: arXiv 2610.22319 (27h14m, 2,783 programs, 605 deaths, single trial, structured-only; accepted card C7). Denominator: deaths/programs per single run. Negatives: 単一試行・非視覚. Block: r13 s1-15 kept (failure history).
- SUPPORTING: なし (P1 has 2 PRIMARY only).

## P2 (Maia 300 / LFM2.5)
- PRIMARY Maia — Q: UMA→NUMAとダイ分離は何を変えるか。 Source: Azure deep-dive (accepted card C1/C2). Negatives: 効率基準無名. Blocks: r13 s2-02/s2-09 (kept).
- PRIMARY Maia — Q: prefill/decode分離と96トレイ167kWは運用上何を意味するか。 Source: same deep-dive (accepted card C3/C4). Block: r13 s2-14/s2-15 (kept).
- SUPPORTING LFM — Q: なぜ温度つき16種表が分母の手本になるか。 Source: Liquid AI blog (accepted card C3). Denominator: per-bench temps; 27.69 vs 8.72 next. Negatives: 発行者計測. Block: r13 s2-16 kept (temperature-table practice).
- SUPPORTING LFM — Q: 288GB級HBMと文脈長の関係は。 Source: same + HBM4 288GB@18TB/s (accepted card). Block: r13 s2-17 kept (HBM-context premise).

## P3 (Spark / Beam / Nemotron + Granite/MiniCPM/FLUX)
- PRIMARY Spark — Q: 2×M5 Ultra実装像は何を示すか。 Source: Meta announcement (accepted card C2). Block: r13 s3-02 area (kept).
- PRIMARY Beam — Q: LICENSE全文は何を保証し何を残すか。 Source: repo LICENSE file full text (accepted card C3, F01-corrected). Negatives: 第三者条項残存. Block: r13 s3-04 kept (F01).
- PRIMARY Nemotron — Q: MTP受理長の正体とLiLiCorr/QAD/再利用/配置の機構。 Source: NVIDIA research page S3a (MTP mechanism) + Training Recipe S3b Table 8 (SPEED-Bench qualitative split, draft length 7; greedy temp-0 4.287→4.718; sampled temp-1 3.787→4.612; +10.1%/+21.8%; cross-model rows) + developer blog S1 (LiLiCorr 2.3x; QAD; context reuse; Dynamo; MOPD teachers). Negatives: full 79pp PDF bytes not retained; greedy crown belongs to others (Gemma 4.837/Qwen3.5 4.799); agentic-teacher edge unconfirmed. Blocks: r13 s3-06 rewritten with Table-8 numbers + NEW Table-8/MOPD blocks.
- SUPPORTING Granite/MiniCPM/FLUX — comparative roles only (kept; tag-only vs full-file tiers).

## P4 (Codex / Scion / HydraFusion + gates/Decider)
- PRIMARY Codex — Q: 保守流儀の移転可能性の留保は何か。 Source: OpenAI engineering post (accepted card C1/C2: single-team internal). Negatives: 他条件での再測定なし. Block: r14 NEW Codex survivorship/transfer (r13 lacked it).
- PRIMARY Scion — Q: WAL/ロックフリー/キャッシュはなぜ速いか。 Source: Anthropic post (accepted card C3/C4). Blocks: r13 s4-05/s4-06/s4-14 (kept).
- PRIMARY HydraFusion — Q: Maxの段差は何を選ばせるか。 Source: GitHub announcement (accepted card: effort tiers, Pro+). Block: r13 s4-08 kept (Max tiering).
- SUPPORTING autofix/AI Scan/Decider — guardrail roles (kept; F02-cleaned refs).

## P5 (unintended / distillation + ECDSA / METR)
- PRIMARY unintended — Q: 誰が何をどう調べたか。 Source: Anthropic report + Oct 12 correction + July scan (accepted card C1/C2/C4) + da.gd operator (partial). Negatives: 自己評価範囲. Block: r14 NEW investigation-actor layering (r13 s5-04 partial).
- PRIMARY distillation — Q: 10–100xと<0.1%の分母は何か。 Source: Anthropic report (accepted cards C1–C4). Negatives: 迂回可能・耐久性未確認. Blocks: r13 s5-06/s5-07 kept.
- SUPPORTING ECDSA/METR — method closure + access-only (kept; m03/m05 wording fixed).

## P6 (wetlab / Earth / Deep Review + Rosalind)
- PRIMARY wetlab — Q: 131/311と8クローンは別工程か。 Source: aptamer sandbox excerpt (accepted card C2: trajectory + 8-clone titrations, no linkage). Negatives: 連関は未確立. Block: r13 s6-02 (trajectory) + s6-15 (separation) kept.
- PRIMARY wetlab — Q: FAP単一標的の意味。 Source: r8 wetlab blog excerpt (FAP single-digit nM/8.6x; non-infectious testbeds). Block: r13 s6-04 kept (FAP scope).
- PRIMARY Earth — Q: 4条件比較は何を分離したか。 Source: arXiv 2610.15750 live read S2 (§3 configs; $0.199 vs $0.167 +10.5pp; 3→52→63; searches 7.0→3.2; EE 54/38). Blocks: r14 NEW 4-config/cost + tool-vs-plan (r13 lacked verified numbers).
- PRIMARY Earth — Q: golden workflowと飽和の扱い。 Source: same (§4: 3 experts blind; 4 unreconciled kept; UnivEARTH 87–94 saturated; 25/76 + 85/220 splits released). Blocks: r13 s6-08/s6-09/s6-10 kept (golden/saturation/splits) + r14 NEW model-comparison caution + best-effort/failure accounting.
- PRIMARY Deep Review — Q: PATの三段階因果は何か。 Source: SPOT paper (accepted card). Block: r13 s6-11 kept (SPOT trials).
- SUPPORTING Rosalind — access/pricing only (kept; m04 r6-12 dropped as dup).

## P7 (GLM-Legal / ASPIRE + Glimpse)
- PRIMARY GLM — Q: ValsとZ.ai図の行為主体は誰か。 Source: Vals page (independent) vs Z.ai announcement (vendor chart omitting 6 higher). Negatives: 方法・再現の限界. Blocks: kept (q7-01/02 + wave).
- PRIMARY ASPIRE — Q: 凍結基盤依存は何を狭めるか。 Source: repo + Jun-30 paper background (accepted card C1/C3). Negatives: 弱モデル未検証. Block: r13 s7-13 kept (dependence).
- SUPPORTING Glimpse — Q: API存在と仕様根拠は別か。 Source: Elorian blog (specs) + OpenRouter listing (existence only). Block: r13 s7-07/s7-08 area kept (existence vs spec).
- (m04: r7-11 VLA paragraph DROPPED as duplicate of r7-06 pricing.)

## Deletions with reason (m04/M03 space discipline)
- P1 s1-15 (Argon hike detail) merged into pricing block; freed ~150字.
- P2: no deletions (evidence thin; kept all).
- P4: no deletions.
- P6 s6-12 (Rosalind dup) → DROPPED in r14 (coverage via table row).
- P7 s7-08 (OpenRouter dup) → DROPPED in r14 (merged into s7-07).
Net r13→r14: −3 dup blocks + 15 new source-backed blocks → 103→112 paras, 19,193→20,479 paragraph-only chars (+9/+1,286 exact). No quota claimed.
