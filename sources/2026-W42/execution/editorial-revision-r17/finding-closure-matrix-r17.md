# W42 r17 finding-closure matrix (F16-01..F16-09)

Date: 2026-10-18 JST. Branch `weekly/2026-W42-v2-work`. Baseline r16 HEAD `a54d55b8...`, dispatch HEAD `6f434325...`.
Status: `SOL_W42_R17_FINAL_DIAGNOSTIC_AND_PAGEPLAN_REVIEW_READY / NONCANONICAL` candidate (pending Sol r17 closure audit).

Scope: bounded editorial/bibliography/layout repair only. Approved 7 chapters / 28 selected / Human Architecture r1 / Core v2 / canonical Draft / State / Gates / checkpoints unchanged. No padding, no margin/font/whitespace manipulation for page targets. New artifacts only under `editorial-revision-r17/`, `diagnostic-r17/`, `sessions/`, plus append-only `execution/index.md`.

Verification method: r16 primary-source-repair-ledger (live 2026-10-18 re-reads A1–A6) + official URLs below + curl HTTP 200 receipts 2026-10-18 for 7 key sources (not 90/90 HTTP). URL syntax validated 90/90 via parser. TeX built from exact r17 bytes, 21pp diagnostic PDF verified.

## F16-01 [HIGH] Maia pod/bandwidth — PASS (bounded)

- Primary URL: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ (“Rack-scale architecture”: “96 accelerators across 24 four-accelerator trays within a 167-kW rack … all 96 accelerators in the rack to form a pod”; 750GB/s peer subset cross-rack). HTTP 200, 333,115 bytes 2026-10-18.
- Blocks:
  - P2 t2-03 old: “ラック内ハーフスイッチの96ポッド構成 … ピア間750GB/s … （1トレイに加速器4基とホスト・記憶・蓄積・冷却 …）”
  - P2 t2-03 new: “ラック内ハーフスイッチで96加速器を束ねる1ポッド構成（24トレイ×加速器4基＝96加速器、1ラック＝1ポッド） … 加速器間750GB/s（帯域、一部ラック横断時の条件つき上限） … （1トレイに加速器4基とホスト・メモリ・ストレージ・冷却 …）”
  - P2 t2-20 old: “ラック規模7倍は96加速器の満配置 … 加速器間750GBは一部横断時の上限 …”
  - P2 t2-20 new: “ラック規模7倍は96加速器の満配置（24トレイ×4基、1ラック＝1ポッド、167kW） … 加速器間750GB/sは一部ラック横断時の帯域上限（容量のGBではなく帯域のGB/s、HBM 288GB・帯域18TB/sとは別の物理量） …”
  - P2 t2-11 table: “24トレイ・96加速器167kW” kept; “商用上限1000万ドル” → “商用上限1000万米ドル（法主体の年商）”; residual “96ポッド” eliminated (0 remain P1–P7/TeX).
- Scan: full-text P1–P7 + TeX for `96ポッド` = 0 remain; `750GB` without `/s` = 0 remain; GB (HBM 288GB) vs GB/s (750GB/s, 18TB/s) vs accel/pod/tray distinguished in t2-02/t2-03/t2-20.
- No 7× vendor comparison made universally achievable; no independent reproduction claimed (vendor-only, unnamed Maia-200 baseline held).
- Remaining unknown: Maia paper baseline details, Nemotron PDF bytes (held from r16, not re-asserted).
- Verdict: PASS.

## F16-02 [HIGH] LFM license — PASS (bounded)

- Primary URLs: https://www.liquid.ai/lfm-license (§§1/4/5/11 + FAQ + redline, HTTP 200 179,469 bytes); https://huggingface.co/LiquidAI/LFM2.5-24B-A2B (lfm1.0 tag, HTTP 200). Re-reads per r16 A6 (Legal Entity = acting + all controlled entities; Threshold = annual revenue US$10M+; §5(a)(b) entity-wide; §5(c) qualified non-profit; §4 hosting = distribution channel; §11 auto-termination).
- Blocks:
  - P2 t2-21 old: “… 利益でも模型売上でもなく年商 … §4で台座の無償配布は流通として許容 … 非営利・研究は適用除外。 …”
  - P2 t2-21 new: “… 利益でもモデル由来収益でもなく法主体全体の年商 … §4でホスティング基盤による配布は流通チャネルとして許容 … 非営利・研究の適用は§5(c)の適格条件を満たす場合に限られ、無条件の適用除外ではない。 …”
  - P2 t2-08 old: “… 利益ではなく年商）を設け、研究利用に影響しない。 …”
  - P2 t2-08 new: “… 利益ではなく年商）を設ける。適格な非営利・研究利用は§5(c)の条件範囲で許容されるが、無条件の適用除外ではない。 …”
- Global: `模型` → `モデル` P1–P7 (incl. P5 t5-06/t5-08 model/org transfer, conversation/model/account movement); `台座` → `ホスティング基盤`/`流通チャネル` (0 remain); per-artifact weight-license scope held (24B-file gap, DSpark soon, 33T pre-train vs 36T budget, 2.45B active vs 2B表記差 preserved).
- No blanket nonprofit/research exemption; no invented per-file applicability.
- Remaining unknown: per-file LICENSE text for each checkpoint (unopened, explicitly held).
- Verdict: PASS.

## F16-03 [MEDIUM] Minecraft translation — PASS (bounded)

- Primary URL: https://arxiv.org/html/2610.22319 (v1, 15 Oct 2026, Faldor et al., CC BY 4.0; HTTP 200 108,772 bytes). §§2/5: 4 player agents + 1 Observer (never plays); “randomly generated world”, “newly generated”, “fresh world”, “random seed”; no fixed/preselected seed. Denominators/limits per r16 A1 (2,783/2,839, 229, 605, 27h14m, single run).
- Blocks:
  - P1 t1-11 old: “4機のArgonエージェントと対戦しない見守り役1機が … 岩裏や龍相も見える … 視覚・キー操作の方式 …”
  - P1 t1-11 new: “4体のプレイヤーエージェントとプレイしないObserver1体が … 岩の裏側やエンダードラゴンの局面も構造化情報として把握できる … 視覚入力・キー操作による方式 …”
  - P1 t1-23: “見守り役” → “Observer”; “固定の種” → “固定シード”; cost/ledger kept, failure counts deduped to t1-16 (see F16-04).
  - P1 t1-13 table: “固定種なし” → “固定シードなし”.
  - P1 t1-16: “龍戦” → “エンダードラゴン戦”.
- Full scan P1–P7/TeX: `模型,台座,程序,固定種,龍相,96ポッド` = 0 remain (`程序` was already 0 in r16; `固定シード種` double-guard applied). Natural technical Japanese preserved; cited facts unchanged (2,783/2,839, 229, 605, 27h14m, single-run).
- Verdict: PASS.

## F16-04 [MEDIUM] Semantic dedup, preserve true findings — PASS (bounded)

- P6 t6-06 kept: experimental design (4 configs × Pro/Flash, 3 repeats mean±SD) + GeoExpertQueries Pro 50.8±1.7→47.6±2.7 (−3.2) / Flash 52.2±5.4→62.7±2.5 (+10.5) once.
- P6 t6-08 old repeated GeoExpert cells; new retains GeoKTools (Pro 84.5±1.4→81.6±1.4 plan-down; Flash 86.0±1.6→85.9±1.5 flat) + Table-5 domain negatives (Flash Natural Hazards +20.4, Public Health +13.1; Site Selection 71.4 vs 65.6 within variation; Pro no gain, Site Selection 48.1 vs 57.2 down) + CBGB Flash 87.9→86.4, with explicit “（開放問の数値はt6-06に集約しここでは繰り返さない）”. No deletion of GeoKTools/Table-5 negatives or explanation.
- P7 t7-07 kept: Glimpse 12-row mechanism + exact baselines (WGO 42.70, ERQA 83.75 tie, BabyVision 95.36, HSS 46.36 < Astra 53.6 honest shortfall, CharXiv-R 92.90, UGC-VideoCap 82.66, DREAM 76.04, TOMATO 93.60, Video-MME2 56.68, E.T. 63.55) + pricing (0.60 vs 10.00 −94%, VLA 0.035 vs 0.249).
- P7 t7-19 old repeated numeric row; new explains comparability (vendor-built bench, Sol46.6/Opus44.6 comparability unconfirmed), API/non-open weights, pricing scope, without repeating 12-row numbers (HSS 46.36 retained only as negative example).
- P1 t1-16 kept failure counts once (605 mostly monsters, End 69/14h, 22% error, void-reset); P1 t1-23 trimmed duplicate death counts, now cost + single-run + random world, with “失敗の内訳はt1-16に集約”.
- Other chapters: no new boilerplate deletions; P5 模型→モデル only; no novel counterexamples/licenses/reader conclusions deleted; net chars +253 (precision qualifications, not padding; P6 −64 via dedup).
- Verdict: PASS.

## F16-05 [MEDIUM] Normalized bibliography — PASS (bounded)

- B74: old `https://github.com/OpenBMB/MiniCPM-V (via @OpenBMB X 2026-10-12)` (parser-invalid, whitespace/parens) → new bare `https://github.com/OpenBMB/MiniCPM-V` + `locator_note: via @OpenBMB X 2026-10-12` + `provenance_note`. HTTP 200 verified.
- 90/90 URL syntax via `urllib.parse` (scheme/host/path/whitespace/trailing notes): invalid = 0. Ledger `narrowed_source_urls` repaired 38 instances across 5 patterns (B74, B73 “+ card …”, B69/B73 “(via X)”, B86 “(Life sciences section)”, B88 “Source: …”) → 0 invalid. HTTP reachability tested only 7 key critical sources (Maia, LFM license, Minecraft, MiniCPM-V, LFM blog, Nemotron blog, LFM HF card: all 200); remaining 83 NOT HTTP-verified, marked `UNVERIFIED` for reachability (never claimed 90/90 HTTP).
- 19 pairs normalized (host www-strip, trailing-slash strip, case-preserving path): all 19 identical post-normalization. Genuine aliases `alias_of` set, all 90 Bxx keys + 177 ledger rows retained:
  B01/B62, B05/B65, B11/B69, B20/B72, B24/B73, B32/B75, B33/B76, B34/B77, B35/B78, B39/B82, B40/B79, B41/B80, B42/B81, B43/B83, B48/B84, B50/B85, B51/B86, B52/B87, B59/B88.
  Categories reconciled: B62/B65 SECONDARY → 一次・発行者 (same first-party, trailing-slash error fixed); B88 一次 → 二次・参考 (OpenRouter secondary, same as B59). B69/B73/B86/B87 alias notes preserved/extended.
- Reader display: publisher/author (year where verified, else site/publisher label; no invented titles) + source kind + clean link; alias entries print “→ Bxx を参照” cross-ref, no duplicate URL print, Bxx citations intact, no dropped claims. Printed entries = 90 logical keys (71 canonical prints + 19 alias cross-refs); bibliography pages measured post-style (p18–p21, 4pp; see diagnostic).
- Preserved: Earth 220/210 + 44/45 splits, NVIDIA MTP acceptance length, wet-lab 131/311 vs 8-clone, W42 cutoff, license tiers.
- Artifacts: `bibliography-map-r17.json`, `bibliography-duplicate-matrix-r17.json`, `citation-repair-ledger-r17.json`, `bibliography-normalization-r17.md` (this file companion), TeX print rules in TeX header + map.
- Verdict: PASS (bounded; HTTP 83 UNVERIFIED explicitly).

## F16-06 [HIGH/EDITORIAL] P7 Table-7 orphan — PASS

- r16: p18 Table-7-only sparse (~1/4 occupied) via pre-bib float flush — FAIL (independent auditor).
- r17 Unit C: Table-7 moved to P7 introductory comparison (after t7-04 limits, before ASPIRE detail), same content, same `table*[htbp]` float, no font/margin/whitespace change, natural reading order preserved (intro → comparison table → ASPIRE/Glimpse mechanism → note → closing).
- Approaches compared (ephemeral builds, not committed):
  - A (adopted): float moved near intro — renders p17 top with body text below/after, no orphan, no cross-chapter drift, no pre-bib flush isolation.
  - B (tested/rejected): inline non-floating tabularx after t7-06 — renders but breaks two-column flow (overfull on narrow columns, poor page balance); rejected for flow disruption.
- Measured r17: 21pp total, Table-7 on p17 with body text (p17 1,948 chars), p18 2,870 chars body (no isolated table page), bib p18–p21 (B57 ASPIRE URL wraps ASPI/RE across p19→p20, minor 2-char carry noted, not isolated). Zero overfull/underfull/undefined/missing-glyphs (log clean). All 7 chapter tables render inside own chapter.
- `\\clearpage` retained only pre-bib float flush (hygiene, not fix); Table-7 isolation resolved by move, not by clearpage.
- Screenshots: p-17.png (Table-7 + body), p-18.png (bib head), full 21 PNGs reviewed.
- Verdict: PASS (orphan eliminated; minor B57 URL carry noted, not a blocker).

## F16-07 [MEDIUM] Bibliography readability — PASS (bounded)

- r16: dense raw long blue URLs, weak identification, single 12.5MB contact sheet unviewable.
- r17: publisher/author + kind + clean link per entry; alias cross-refs avoid duplicate prints; xurl wrapping; entries verified readable in PNGs p18–p21; no invented titles (unverified titles marked via site/publisher label, e.g., “Hugging Face API — モデルAPI参照”).
- Contact sheets split into 3 small fetchable files (see diagnostic), each < ~2MB, independently openable (vs r16 12.5MB single).
- Bibliography page allocation measured post-style (4pp p18–p21), not assumed.
- Verdict: PASS.

## F16-08 [MEDIUM] Wet-lab Methods qualification — PASS (bounded)

- Status for newly authored r17 editorial only: `DIRECT_FETCH_TOOL_LIMIT / METHODS_NOT_INDEPENDENTLY_REVERIFIED` for aptamer PDF >5MB prior failed one-shot transfer. NOT `NOT_PUBLIC`, NOT permanently inaccessible.
- Bounded alternate attempt 2026-10-18: `curl -r 0-1023` to `https://www.gstatic.com/science-ai/agentic_aptamer_sandbox.pdf` → server ignored Range, returned 200 with 8,077,293 bytes (full). Tool cannot ingest >5MB in one transfer; streaming/range unsupported by host. Logged exact method + failure reason; no stall of r17.
- No numeric threshold changes; screening (131/311) vs 8-clone assays kept separate; r6 extraction scope held (27pp retained in collectors, not re-asserted beyond).
- Verdict: PASS (with explicit residual unknown).

## F16-09 [MEDIUM] Page-plan gap — MEASURED, NOT A PASS/FAIL REPAIR

- r16: 21pp total = cover1 + body17 physical (effective ~15.5–17) + bib3. Approved plan 26.5 body + nonbody 4 = 30.5 vs magazine target28/max30 — quantitatively questionable, but does NOT invalidate Human Architecture r1.
- r17 measured (deterministic builds, SOURCE_DATE_EPOCH fixed, final two byte-identical SHA `6b673a93…`): 21pp total, 512,182 bytes; cover1 + body p2–p17 (16pp physical; Table-7 now in-body, ex-orphan p18 eliminated as body-isolated page) + bib p18–p21 (4pp). Effective body ~15.5–17 (unchanged methodology; +253 chars net editorial precision, −64 P6 dedup, no padding). Prior 9,400-char / 6–7pp point estimates remain retracted as invalid exact claims.
- No Architecture/State/approval/checkpoint change; no padding; no retroactive revocation. Decision brief PROPOSED separately (Unit D), no Human vote.
- Verdict: MEASURED (see `human-architecture-pageplan-decision-brief-r17.PROPOSED.md`).

## Residual unknowns (explicit)

- Aptamer Methods thresholds (DIRECT_FETCH_TOOL_LIMIT); ASPIRE figure values (FIGURE_VALUES_UNRESOLVED); Earth repo SHA; Vals methodology/rate card; Maia paper/baseline; Nemotron PDF bytes; HF per-artifact licenses; METR downstream; independent reruns. Pagination decision belongs to Sol/Human (options A/B/C in brief).
- HTTP reachability: 83/90 UNVERIFIED (parser-valid only).
- Visual minor: B57 ASPIRE URL “ASPI/RE” carry p19→p20 (2-char, readable, not isolated).

Overall: F16-01..08 PASS (bounded), F16-09 MEASURED. No new technical facts invented. Ready for Sol r17 closure audit.
