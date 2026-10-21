# W42 r17 diagnostic visual QA — per-page review index (all 21 pages opened @150dpi)

Build: LuaHBTeX 1.24.0 (TeX Live 2026), `SOURCE_DATE_EPOCH=1792305000 lualatex -interaction=nonstopmode -halt-on-error` ×4 (final two byte-identical SHA256 `6b673a9329ec02d41cf22f6a6a634a315d8d5ad480f6d7274c5f5c7b4ffb5b8e`, 512,182 bytes). Log: 0 warnings (excl. pkg info), 0 overfull, 0 underfull, 0 errors, 0 missing glyphs. Fonts: HaranoAji Mincho/Gothic + Latin Modern. TeX 97,014 bytes / SHA256 `ee28a6c121d3dac02378095d552e57352d3af807cc7a4e5ea5130840b16dc639`. 136/136 paragraphs in TeX verified; 90/90 bib keys cited. Contact sheets split 3× (2.25/2.32/1.99MB).

- p01 cover: title/date/edition descriptor + NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL stamp + cutoff/repo/build. Sparse by design. PASS (viewed).
- p02 P1 head + t1-02..t1-05 + OOD start. Cites blue/linked. Full. PASS (viewed).
- p03 P1 Argon pricing, anecdotes, Focus checkpoint, Copilot distribution, science vignettes, Minecraft conditions t1-11 repaired (4体のプレイヤーエージェントとプレイしないObserver1体、ランダム生成、岩の裏側やエンダードラゴンの局面、視覚入力・キー操作). Ledger t1-23 start (Observer待機、固定シード、失敗集約t1-16). Full. PASS (viewed).
- p04 P1 Table-1 (Wonder/Argon; Minecraft cell 固定シードなし) + P1 closing + P2 head + Maia SDLA/NUMA + t2-03 repaired (96加速器を束ねる1ポッド、24トレイ×4基、加速器間750GB/s帯域、ホスト・メモリ・ストレージ・冷却). Dense. PASS (viewed).
- p05 P2 LFM bench, t2-08 repaired (法主体の年商1000万米ドル、§5(a)(b)、§5(c) qualified, LICENSE原文/24B個別未了), t2-20 repaired (満配置24トレイ×4基1ポッド167kW、750GB/s帯域上限、HBM GB vs GB/s区別), note box. Full. PASS (viewed).
- p06 P2 Table-2 (Maia 24トレイ・96加速器167kW; LFM 33T/36T/24.5億) + t2-21 repaired (法主体年商1000万米ドル、モデル由来収益否定、ホスティング=流通チャネル、§5(c)適格のみ、per-artifact scope) + P3 head. Dense. PASS (viewed).
- p07 P3 Beam safety + Nemotron MTP (acceptance length, draft 7, temp split) + B60, MOPD, LiLiCorr. Clean. PASS (viewed).
- p08 P3 QAD/Dynamo + Spark arch/VRAM + Bolt dating + Granite DI + MiniCPM (B74 bare in table [B27,B74,B26]) + FLUX + rights note + synthesis. Full. PASS (viewed).
- p09 P3 Table-3 + P4 head + Codex practice + cost ledger. Dense. PASS (viewed).
- p10 P4 CI triad, Scion WAL, HydraFusion, Max. Clean. PASS (viewed).
- p11 P4 autofix/AI-Scan gates + Decider + note box + P5 head. Full. PASS (viewed).
- p12 P5 correction chain + actor split + distillation efficacy (モデル・組織をまたぐ移転なし — 模型 fixed) + adversary TPP (会話・モデル・アカウント間の移動 — 模型 fixed) + durability + ECDSA + METR + P6 head. Dense. PASS (viewed).
- p13 P5 TPP + durability + ECDSA + METR zero-results + note + P6 VERID/aptamer (原典PDF直接取得不可、r6抽出範囲、新閾値なし — F16-08 held). Full. PASS (viewed).
- p14 P6 Earth design 4×2 + t6-06 (Flash +10.5/Pro −3.2) + procedure + Table-6 + tools decomposition t6-08 repaired (開放問数値はt6-06に集約、GeoKTools/Table-5 negatives retained) + repo discrepancy (220/210, 44/45) + B61. Dense. PASS (viewed).
- p15 P6 screening-vs-8-clone + Deep Review SPOT + P7 head. Full. PASS (viewed).
- p16 P6 Table-6 + P7 GLM-Legal anchor + t7-04 limits. Dense. PASS (viewed).
- p17 Table-7 IN-BODY (比較表：専門・身体の三件, GLM/ASPIRE/Glimpse rows) at top with P7 body text below/after (Glimpse mechanism t7-07 12-row baselines kept, boundary, t7-19 comparability rewritten, note box, closing). NO orphan table-only page (ex-r16 p18 FAIL eliminated). Full. PASS (viewed).
- p18 bib head (出典一覧と確認水準 + B01–B14 with publisher/kind/link, e.g., Faldor et al. arXiv, Meta発行者ページ) + B15–B28. Clean xurl wrapping. PASS (viewed).
- p19 bib B29–B57 (B32–B42 www-normalized prints, B44–B46 gstatic PDFs, B54 Vals独立評価). PASS (viewed).
- p20 bib B58–B81 (B58 Elorian, B59 OpenRouter二次, B60–B61, B62→B01 alias, B63–B64 SECONDARY X, B65→B05 alias reconciled一次, B66–B68 SECONDARY, B69→B11 alias, B70–B71 SECONDARY, B72→B20 alias, B73→B24 alias, B74 bare `https://github.com/OpenBMB/MiniCPM-V` + via @OpenBMB X note, B75→B32 alias … B81→B42 alias). Minor: B57 ASPIRE URL wraps ASPI/RE across p19→p20 (2-char carry, readable, entry continues, not isolated). PASS with noted carry (viewed).
- p21 bib B82–B90 (B82→B39 … B88→B59 alias reconciled二次, B89 GEAR real-robot section, B90 HF card 33T/36T/DSpark) + diagnostic footer stamp. PASS (viewed).

No clipped glyphs, no isolated table page, no cross-chapter table floats (all 7 tables in-chapter; Table-7 moved P7-end → P7-intro, same-chapter). Old r16 p18-orphan class: absent. B48-split class: absent (bib starts p18; entries wrap cleanly except noted B57 2-char carry).
