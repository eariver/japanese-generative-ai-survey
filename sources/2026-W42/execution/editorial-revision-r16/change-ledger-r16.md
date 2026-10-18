# W42 r16 change ledger (vs r15.1 v15.1): bounded source repair, NO padding

Date: 2026-10-18 JST. Method: in-place retext of existing blocks (136 paras maintained; 24,162 → 24,832 para-chars, +670; PTN 27,415 → 28,144, +729). No blocks added/removed (frozen must_cover/boundary maps stable). All F-01–F-10 dispositions below; regressions held.

## F-01 Minecraft (A1): t1-11/t1-16/t1-23 + t1-13 table
- Randomly generated Easy world (no fixed/preselected seed — 「固定種」 deleted); 4 players + Observer (never plays); 2,783/2,839 programs; 229 messages; 605 deaths; median 33.5s; 40% duty; 6 restarts ~20min; 81 days; cost $520/$1,040 list-price est ($810/$1,620 session, NOT serving cost); End 69/14h; 22% error; void-reset; single run; structured-only vs SIMA2. F-10 程序/229通/605死/固定種 → プログラム/229件の交信/605回の死亡/ランダム生成（固定種なし）.

## F-02 Maia rack (A2): t2-03/t2-11/t2-14/t2-20
- **24 trays × 4 accelerators = 96 accelerators per 167-kW rack** (each tray: 4 accel + host/mem/storage/cooling; 2× Maia 200 density). 「96トレイ」×4 instances eliminated. t2-20 repurposed: applicability (full-96-config 7×, >2.5× perf/W, 750GB/s conditional, spare-tray tradeoff, Ignite Nov 2026). Unnamed-baseline deltas kept vendor-only.

## F-03 ASPIRE real robot (A3): t7-05/t7-17 + t7-09 table
- Prior "sim-only" suggestion corrected: publisher real-robot results EXIST — table bussing (Opus 4.6 sim → GPT-5.5 real), Rubik's/unscrew/pill/stack (Astra); with/without sim-skill design; tokens-until-first-success + held-out success of first-success code; figure values FIGURE_VALUES_UNRESOLVED (not invented); third-party reproduction NOT claimed. v1.0: 99% on 80 tasks; 3 new recipes distilled-from-demos (not new validation); pill seated-vs-tight; sandbox warning; Apache 2.0 + third-party retained. Frozen-frontier + not-fully-autonomous limits held.

## F-04 Earth AI (A4): t6-08 rewrite; t6-06/t6-21/t6-23 verified
- Same-model/same-bench control: GeoKTools Pro 84.5±1.4→81.6±1.4 (−2.9pp), Flash 86.0±1.6→85.9±1.5 (flat); CBGB Flash 87.9→86.4 (≤3pts). Table-5 domains: Flash hazards +20.4/health +13.1, site 71.4v65.6 within variation; Pro no gain anywhere, site 48.1v57.2 (recovery asymmetry: tools-only custom-code/aux vs GRA stops). Paper 220 vs repo 210, 18/19 & 74/72, CBGB 44-vs-45 held unresolved; tests withheld.

## F-05 Wet-lab (A5): t6-12 note; M02 held
- Aptamer PDF direct fetch BLOCKED (>5MB); thresholds beyond r6 extraction not asserted; 131/311 vs 8-clone separation held; no new claims.

## F-06 semantic dedup (purposes recorded in repair ledger A7)
- P2 t2-14 mechanism vs t2-20 applicability; t2-10 inventory vs t2-17 capacity→context; t2-08 cap vs t2-21 operative scope. P4 t4-03 practice vs t4-21 cost ledger; t4-07 data-plane vs t4-23 control-plane. P5 t5-06 efficacy vs t5-08 adversary vs t5-19 durability vs t5-07 calibration. P7 anchor vs regression; table vs negatives. P6 four Earth blocks distinct.

## F-07 bib integrity: bibliography-map-r16.json (90 keys; r15 preserved)
- B69/B73/B88 URL-normalized with notes separated; B86/B87 alias_of B51/B52; +B89 GEAR +B90 HF card. Ledger 177 rows (t7-05/17 +B89; t2-21 +B90). No http-string citations; A1–A6 links resolved live (aptamer PDF only failure).

## F-08/F-09 counts
- r16: 136 paras / 24,832 para-chars / 7 TABLE / 7 NOTE. P+T+N = 28,013; + HEADING 131 (20/17/15/21/28/10/20) = PTN 28,144. The r15.1 "131 unexplained" = headings by definition (line-by-line above). No fraud either way.
- Shortfall language retracted: prior "9,400 chars / 6–7 pages" was an unmeasured estimate (see reconciliation doc for measured ranges, not point claims).

## F-10 Japanese
- 程序→プログラム, 229通→229件の交信, 605死→605回の死亡/死亡605回, 固定種→ランダム生成（+固定種なし in table), 地球引擎→Earth Engine, 台座再配布→プラットフォーム再配布, 定数旗依存→定数条件フラグ依存, 再現符号→再現コード, 未開→未解決（t5-21）, 未開封→未確認/未取得 where "not retrieved" (t3-14, t3-23, t2-08, table rows). 固定種なし (negation) retained once in t1-13 table as explicit guard.

## Regressions held
- MTP average acceptance length (not rate), draft 7, temp split 4.287→4.718 / 3.787→4.612; wet-lab separation; license tiers; vendor-vs-independent; chronology; Pro negative; r13/r14/r15 history; lifecycle DRAFT_COMPLETE.
