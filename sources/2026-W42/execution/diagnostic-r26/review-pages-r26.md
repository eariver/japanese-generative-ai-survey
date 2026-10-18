# W42 r26 visual QA — MULTICOL-V2 + two restored cells (ALL 21 pages opened @150dpi; READY)

Build: LuaHBTeX 1.24.0, epoch 1792311600 (runs 2-3 byte-identical `c76f4a6e975039…`). TeX `5bbdca1b…` (= r25 `837f5535…` + exactly 2 cell restores + header/provenance lines only); preview.sty byte-identical to r22/r25; multicol + capt-of unchanged; 7 measured atomicity needspaces kept (T1 18 / T2 18 / T3 30 / T4 30 / T5 22 / T6 22 / T7 20, no wrapper change). Log 0 errors, 0 overfull, 0 underfull, 0 missing glyphs, 0 warnings (excl pkg-info). 21 pages; page→table mapping identical to r25 (T1 p04 / T2 p06 / T3 p09 / T4 p12 / T5 p14 / T6 p16 / T7 p17).

- p01: cover. Title, 2026-W42, 2026-10-18, 7-area descriptor, 3 diagnostic lines (NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL) intact. Cutoff/repository/build block, edition descriptor. No machine IDs. — PASS.
- p02: P1 head (Wonder/Argon), deck, first HEADING, opening paragraphs + cites. Two-column flow normal. — PASS.
- p03: P1 continues (Argon pricing → Minecraft conditions →台帳→ safety numbers). Ends complete with `[B01,B62,B63,B05,B65,B08,B04,B07,B06]` mid-sentence boundary clean. Lower whitespace present (T1 atomicity cost, same as r25). No sentence bisection. — PASS.
- p04: T1 atomic (caption 表1 + Wonder + Argon rows, cites B01/B62/B63/B02 + B05/B65/B08/B04). Below-table NOTE box intact, `Wonderの例示タスク…` fresh, `失敗の記録と立直しの手順…` complete (r22 `立直/し` split absent). P2 section head same page. — PASS.
- p05: P2 continues (Maia/LFM paragraphs, AutomationBench 27.69, temps, HBM4, sealed-eval, §5 license scope). Ends complete. Light lower whitespace (same as r25). — PASS.
- p06: T2 atomic (caption 表2 + Maia 300 + LFM2.5 rows). LFM2.5 cell prints RESTORED `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商） [B11, B69, B12]` — visually verified, row unclipped, table un-split. NOTE box below, P2 resumes; P3 head NOT on this page (same as r25). `分母の開示だ…AutomationBench` intact. — PASS (BLOCKER-01 closed).
- p07: P3 head (Spark Open/Beam/Nemotron…), deck, HEADING, Spark paragraphs (Muse terms, 2000万ドルMaaS門), Beam paragraphs (LICENSE全文確認). MTP `受理長` wording (rate-vs-length correct). — PASS.
- p08: P3 continues (MOPD/MTP/QAD, QAD, context reuse, deployment, MOPD配分, LiLiCorr … through Granite/MiniCPM/FLUX paragraphs). Ends complete before T3. `エンドポイント` intact (`一つのエンドポイントに`). Body license sentence uses `Super VLのライセンスファイル自体は未確認` (consistent with restored table). — PASS.
- p09: T3 atomic (caption 表3 + ALL 6 rows: Spark/Beam/Nemotron/Granite/MiniCPM/FLUX). Nemotron cell prints RESTORED `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用 [B21, B72, B22, B20]` — visually verified. Caption orphan absent (r24 F24-02 stays fixed). NOTE box + P3 closing + cites below. — PASS (BLOCKER-02 closed).
- p10: P4 head (Codex/Scion/HydraFusion), deck, HEADING, Codex paragraphs (1400 PRs, container numbers). — PASS.
- p11: P4 continues (HydraFusion routing, Max, autofix/AI Scan gates, Decider v1.1→v1.2 paragraphs). Ends complete `…版管理の手本たるゆえんだ。[B37, B36, B38]`. Lower whitespace (T4 atomicity, same as r25). — PASS.
- p12: T4 atomic (caption 表4 + ALL 6 rows incl Decider v1.2 `2セント/M入力・出力無料 [B37, B36, B38]`). No footer collision (r24 F24-01 stays fixed). NOTE box, P4 closing, P5 head same page below table. — PASS.
- p13: P5 safety body both columns (Anthropic蒸留防御 numbers, ECDSA解明, METR). Ends complete. Lower whitespace (T5 atomicity, same as r25). — PASS.
- p14: T5 atomic (caption 表5 + 4 rows: 開示/防御/解明/接近). NOTE box, P5 closing, P6 head same page. — PASS.
- p15: P6 deep dive (wet-lab 131/311 + 8 clones, aptamer stages, Earth GEO design, GeoKTools numbers). No gaps. — PASS.
- p16: T6 atomic (caption 表6 + 4 rows: ウェットラボ/地球AI/Deep Review/Rosalind). `染料と水による検証` complete (r22 `によ/る` split absent). NOTE box, P7 head same page right column. — PASS.
- p17: T7 atomic (caption 表7 + 3 rows: GLM-Legal/ASPIRE/Glimpse). Above ends complete, below fresh `独立評価の設計を読む…`. ASPIRE `80課題で99%…卓上片づけ…` complete in body (no T7 bisection). Reading order normal. — PASS.
- p18: P7 Glimpse + NOTE box + law/robotics closing. Both columns filled to mid-lower page; whitespace below is normal body→bib transition (same class as r25). No left-only orphan tail. — PASS.
- p19: bib B01–B14(+). Blue URLs, publisher labels, `[二次・参考]` where due. No clipped entries. — PASS.
- p20: bib B28–B54. B28 long model-API URL wraps readably; B57 NVlabs/ASPIRE kept-together; B74 OpenBMB clean. No missing glyphs. — PASS.
- p21: bib B55–B90 + 19 `→ [Bxx]（同一資料）` alias cross-refs. B90 `https://huggingface.co/LiquidAI/LFM2.5-24B-A2B` terminal intact at page end; no stamp, no footer collision. — PASS.

Compared vs r25 (21pp, same page map): only visible deltas are the two restored cells (p06/p09) + reflow-neutral bytes. No new orphans/clips/collisions/splits; whitespace regions same pages (p03/p11/p13/p18, unchanged class). Zero machine IDs; 7 captions numbered 表1–7 in order; no table-only leaf; no chapter crossing.

(End — 21/21 opened, READY.)
