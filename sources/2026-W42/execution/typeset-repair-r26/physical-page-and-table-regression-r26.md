# W42 r26 — physical page and table regression (NONCANONICAL, real-PDF based)

Basis: r26 `main.pdf` (sha256 `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0`, 21 pp, 508624 bytes), all 21 individual PNGs opened @150dpi (`review-pages-r26.md`), r25 baseline for comparison. Geometry: r25 MULTICOL-V2 kept byte-identical (needspace 18/18/30/30/22/22/20, `columnsep 7mm`, same fonts/margins); only two cell strings lengthened.

## 1. Physical 7-table ledger (image-verified)

| table | chapter/phys page | rows seen on page | directly before → directly after | verdict |
|---|---|---|---|---|
| T1 Wonder/Argon | P1, p04 | Wonder / Argon = 2 rows, cites B01/B62/B63/B02 + B05/B65/B08/B04 | p03 ends complete (safety numbers) → note box + `Wonderの例示タスク…`; P2 head same p04 | PASS (unchanged from r25) |
| T2 効率主張 | P2, p06 | Maia 300 / LFM2.5 = 2 rows | p05 ends complete → note box + `LFMの五段階の事後学習…`; P3 head p07 | PASS + CONTENT RESTORED (`…1000万米ドル（法主体の年商） [B11,B69,B12]` fully printed, atomic, unclipped) |
| T3 重み・実装・ライセンス | P3, p09 | Spark/Beam/Nemotron/Granite/MiniCPM/FLUX = 6 rows | p08 ends complete → license NOTE box + Nemotron本文; P4 head p10 | PASS + CONTENT RESTORED (`OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用 [B21,B72,B22,B20]` fully printed; caption+6 rows same page, no orphan) |
| T4 生産性とゲート | P4, p12 | Codex/Scion/HydraFusion/AutoFix/AI Scan/Decider v1.2 = 6 rows | p11 ends `…手本たるゆえんだ。[B37…]` → note box + P4 closing + P5 head same p12 | PASS (Decider final row + `[B37,B36,B38]` visible; no footer collision; r24 F24-01 stays fixed) |
| T5 安全の四局面 | P5, p14 | 開示/防御/解明/接近 = 4 rows | p13 safety body ends complete → note box + P5 closing; P6 head same p14 | PASS |
| T6 科学エージェントの証拠 | P6, p16 | ウェットラボ/地球AI/Deep Review/Rosalind = 4 rows | p15 wet-lab/Earth body → VERID `染料と水による検証` continues below table; P7 head same p16 right col | PASS |
| T7 専門・身体の三件 | P7, p17 | GLM-Legal/ASPIRE/Glimpse = 3 rows | p16 right-col P7 intro lines → table at top → `独立評価の設計を読む…`; ASPIRE `80課題で99%…卓上片づけ…` in body uncut | PASS (no bisection; ASPIRE boundary preserved) |

All 7 captions printed `表 1`–`表 7` in order; every caption + ALL rows + row cites on the SAME page; no split, no orphan, no footer collision/clipping, no table-only leaf. Expanded T2/T3 cells fit existing geometry: page map identical to r25, no pagination shift, no wrapper change required.

## 2. All-page notes (condensed; full text in `review-pages-r26.md`)

p01 cover 3 diagnostic lines, no machine IDs. p02 P1 head flow. p03 P1 end complete + whitespace (T1 atomicity cost, unchanged class). p04 T1 (立直し intact). p05 P2 cont (light whitespace, unchanged). p06 T2 restored. p07 P3 head (MTP受理長 correct). p08 T3 lead-in complete (エンドポイント intact; body `ファイル未確認` consistent). p09 T3 restored. p10 P4 head. p11 P4 end + whitespace (T4 atomicity, unchanged). p12 T4. p13 P5 end + whitespace (T5 atomicity, unchanged). p14 T5. p15 P6 (wet-lab 131/311, 8 clones, Earth deltas). p16 T6. p17 T7. p18 tail both columns filled, note box, no orphan tail. p19–p21 bib: 90 entries (71 full + 19 `→ [Bxx]（同一資料）`), 17 `[二次・参考]`, B28/B57/B74/B90 intact incl terminal B90 URL, no stamp.

Old-fault recheck (all image-verified, none recurred): r22 `立直し` (p04 ✓), `分母の開示` (p05–p06 ✓), `エンドポイント` (p08 ✓), `染料と水による検証` (p16 ✓); r24 T3 caption orphan (p09 caption+rows co-located ✓); r24 T4 Decider clip/footer collision (p12 full row, clear of footer ✓); r25 T7 ASPIRE boundary (p17 ✓).

## 3. Whole-magazine regressions

- Body flow: two-column throughout (8 `multicols` segments + bib segment); paragraph/sentence/word bisection at table boundaries: none (checked all 7 junctions).
- Reading order: P1→P7 chapters in order; tables physically inside their chapters (T1 before P2 head … T7 inside P7 before bib).
- Whiteness: p03/p11/p13 lower whitespace (pre-table atomicity), p05 light, p18 body→bib transition — same pages and same class as r25; area UNMEASURED (no numeric claim, per audit boundary).
- Citations/links: blue `\cite` links render on all checked pages; URL blue strings in bib; no HTTP liveness testing (out of scope, same as independent audit).
- Caveats preserved in print: Argon random one-run Minecraft; Maia24/96/750GB/s; Earth dependent negatives; MTP length-not-rate; wet-lab 131/311 vs 8 clones; LFM legal entity; ASPIRE publisher limits + real/sim conditions.
- Cover diagnostic wording, 7 headings, 7 notes, zero machine IDs — all preserved.

## 4. Build integrity

LuaHBTeX 1.24.0 (TeX Live 2026), `SOURCE_DATE_EPOCH=1792311600`, 3 runs (runs 2–3 byte-identical). Log: 0 errors / 0 overfull / 0 underfull / 0 missing glyphs / 0 warnings (excl pkg-info). PDF text extraction spot-check: p06 contains `法主体の年商` (not `未開封`/short form); p09 contains `ファイル未確認` (not `未開封`).
