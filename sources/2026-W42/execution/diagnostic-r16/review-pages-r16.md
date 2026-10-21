# W42 r16 diagnostic visual QA — per-page review index (all 21 pages opened @150dpi)

Build: LuaHBTeX 1.24.0 (TeX Live 2026), `lualatex -interaction=nonstopmode -halt-on-error` ×stable runs (final two byte-identical). Log: 0 warnings (excl. one infwarerr package-info line), 0 overfull, 0 underfull, 0 errors, 0 missing glyphs. Fonts: HaranoAji Mincho/Gothic + Latin Modern. PDF 506,978 bytes / SHA256 `e2919ec9341f1e8fb4e650a6e77111a8e3b8576cc3b8b54e20549d088854c8ac`.

- p01 cover: title/date/edition descriptor (診断用・非正準・未承認） + NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL stamp + cutoff/repo/build lines. Sparse by design (cover). PASS.
- p02 P1 head + headline/deck + t1-02..t1-05 + OOD t1-22 start. Cites [B01..B06] render blue/linked. Full. PASS.
- p03 P1 Argon pricing (t1-19), anecdotes (t1-09), Focus checkpoint (t1-20), Copilot distribution (t1-21, repaired), science vignettes (t1-10), Minecraft conditions (t1-11, repaired: ランダム生成/Faldor/CC BY 4.0/4+1 agents), ledger start. Full. PASS.
- p04 P1 Table 1 (Wonder/Argon rows; Minecraft cell fixed ランダム生成・固定種なし） + P1 closing + P2 § head + Maia SDLA/NUMA (repaired 24トレイ・96加速器 in t2-03). Dense. PASS.
- p05 P2 LFM bench (per-temp, AutomationBench outlier, simulator confound), license operative (法主体の年商 + §5(a)(b) + B90), sealed-eval, serving-cost, 24トレイ・96加速器 (t2-14). Note box (t2-12). Full. PASS.
- p06 P2 Table 2 (Maia 24トレイ・96加速器167kW; LFM 33T事前学習・総36T訓練予算・能動24.5億 — repaired) + applicability t2-20 + P3 § head + Spark arch. Dense. PASS.
- p07 P3 Beam safety + n=20 uplift method (t3-24), Nemotron MTP (acceptance length, draft 7, temp split) + B60 cites, MOPD, LiLiCorr. Clean. PASS.
- p08 P3 QAD/context-reuse/Dynamo + Spark arch/VRAM crosswalk (t3-25) + Bolt dating + Granite DI + MiniCPM + FLUX + rights note (未確認 fixed) + synthesis. Full. PASS.
- p09 P3 Table 3 (Nemotron row 未確認ファイル — fixed) + P4 § head + Codex practice (t4-03 rewritten, cost numbers moved out) + cost ledger t4-21 (定数条件フラグ依存 — fixed). Dense. PASS.
- p10 P4 CI triad, Scion scale/WAL (t4-07 data-plane vs t4-23 control-plane distinct), HydraFusion, Max. Clean. PASS.
- p11 P4 autofix/AI-Scan gates + Decider DI/calibration (t4-24) + note box + P5 § head + unintended categories. Full. PASS.
- p12 P4 Table 4 + P5 correction chain (t5-20: Oct 9→12, fetch-limit≠injection, halt ALL evals) + actor split + distillation efficacy (t5-06 trimmed). Dense. PASS.
- p13 P5 adversary TPP (t5-08 rewritten), durability ledger (t5-19: Sep-24 charging, cat-and-mouse), ECDSA method + residual (B-163 + 4 base OPEN, 未解決, 再現コードCC0 — fixed), METR zero-results + note box + P6 § head + VERID/aptamer. Full. PASS.
- p14 P5 Table 5 + P6 Earth design + 4×2+SD (Flash +10.5 / Pro −3.2) + procedure. Dense. PASS.
- p15 P6 tools decomposition (EE 38→54%, Flash <1/3 Pro), saturation, repo discrepancy (220/210 + K=2 110/100 + 44-vs-45), B61 cite, screening-vs-8-clone + methods-blocked note, Deep Review SPOT. P7 § head at bottom. Full. PASS (ex-p15 whitespace resolved by content growth).
- p16 P6 Table 6 + P7 GLM-Legal anchor (Vals + chart-omission) + design readings + regression (41.83/45.19) + ASPIRE dating + v1.0 real-robot (B89) + repo-ownership boundary. Dense. PASS.
- p17 P7 Glimpse mechanism + HSS negative + pricing + note box (t7-10) + reflections (PLawBench, Harvey LAB, frozen-frontier, direct-action future) + closing synthesis. Full, no orphan. PASS.
- p18 Table 7 ONLY (GLM/ASPIRE/Glimpse rows; ASPIRE real-robot evidence + B89 cite). Sparse (~1/4 occupied) — documented consequence of pre-bibliography float flush (see reconciliation §2). Table itself clean, no clipping. PASS with noted sparsity.
- p19 bibliography head (出典一覧と確認水準 + 参考文献 B01–B33) + B89/B90 present at tail (p21). Clean wrapping (xurl), no stranded single-URL page. PASS.
- p20 bib B34–B69 (B69 normalized, no "(via X)"). PASS.
- p21 bib B70–B90 (B73 normalized, B86 normalized bare URL, B88 normalized, B89 GEAR, B90 HF card) + diagnostic footer stamp. PASS.

No clipped URL/glyph, no isolated tail entry, no cross-chapter table floats (all 7 tables render inside own chapter except Table 7 flushed to p18 — same-chapter, pre-bib; recorded). Old r14 p15-partial and p16→17 B48-split classes: absent in this layout (bib starts p19; B48 mid-bib with wrapped entries, verified unstranded).
