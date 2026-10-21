# W42 r11 change ledger (Sol B01–B05 / M01–M05 closure)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-18 JST
Old (canonical, UNTOUCHED): `sources/2026-W42/draft/v2/packages/*/draft-result.json` (v10.0, ESTABLISHED)
New (proposed): `execution/editorial-revision-r11/proposals/*/draft-result-r11.PROPOSED.json` (v11.0, REVISED)
Volume: 117→82 paragraphs, 24,030→20,082 body chars, tables 6→7 (P7 new), notes 7→7. No filler; every deletion is a duplication/meta-voice removal paired with retained or new source-backed content.

## BLOCKERS

### D10-B01 OSI correctness — RESOLVED
- Before: P3 `p3-n1` blanket false `OSI承認は本号のいずれのライセンスにも成立していない`; `p3-p10` `Beamのように何でもできるもの`.
- After: `q3-n1` states Apache License 2.0 itself IS OSI-approved (license-text status), then separates per-model coverage: Beam full-file Apache confirmed (third-party terms still reserved); Granite/MiniCPM tag-only; Muse/Kommunity/LFM/OpenMDW custom or partially verified, no OSI claim. `q3-10` + `q3-t1` replace blanket permission with bounded terms (redistribution/attribution/LICENSE-copy/change-notice/patent/third-party).
- Official reference: https://opensource.org/license/apache-2.0 (OSI listing). No opposite blanket ('all open weights OSI-approved') introduced.

### D10-B02 reader-surface machine trace — RESOLVED
- Before: `execution/draft-reader-preview-r10.json` carried all seven CLAIM_BOUNDARY blocks with raw English (`r7 card authority`, `No r7 finding recorded`, checksums, control names).
- After: `reader-preview-r11.PROPOSED.json/.md` contain ZERO boundary blocks and zero `AUTHORITY_CONSUMED`/`No r7`/`CLAIM_BOUNDARY`/checksum fragments (programmatic scan clean). Canonical boundary records are retained verbatim inside each proposed Draft Result (validator-kept, same block IDs `P*-boundaries`, EXPLICITLY_STATED).
- Substantive cautionary content preserved as Japanese NOTE/prose blocks in every chapter (license tiers, vendor-only numbers, pending reports, X-as-post-existence).

### D10-B03 meta-voice/duplication → real reporting — RESOLVED
- Removed all 44+ flagged formulae: `実務への含意を書く` closings (rewritten as plain synthesis), `もう一段読む/もう一度書く/もう一度読む` openers (rewritten as direct statements), `良い記事だ/良い書き方`, `本号の仕事`, trailing duplicate closings (p1-p9/p15/p16/p17/p18, p2-p8/p15/p16, p3-p10/p20/p21, p4-p9/p17/p18, p5-p7/p14, p6-p6/p15, p7-p7/p15 and merged duplicates p1-p13→p1-q1-09, p4-p15/p4-p16→p4-q4-06/07, p7-p8..p7-p14 consolidated into q7-01..q7-06 + focused additions).
- New source-backed content (no invention): memory-vs-focus distinction (P1), numeric-denominator practice (P2), Scion WAL/lock-free/cache + detection-vs-delivery separation (P4), Anthropic claim/independent-limits + METR startup record (P5), Earth autorater honesty + trial reporting (P6), Vals-vs-vendor-chart actor specification (P7), plus per-chapter mechanism paragraphs (wave2: task examples, N2P/IO split, 5-stage post-train, cost-table practice, API-query scaling, marker-token format, July scan/Oct correction, titrations, STOC/ICML trials, Rosalind work areas, AutoClaw staging, VLA pricing, Harvey width).

### D10-B04 lexicon/encoding — RESOLVED
- `무제한`→`無制限`, `疎疎チェックアウト`→`スパースチェックアウトと仮想チェックアウト`, `误検出`→`誤検出` (programmatic scan: Hangul/simplified hits now zero).
- Replaced: `anchor`→`独立評価の根拠` (P7 headline, 8 blocks, synthesis payloads), `tiers`→`確認水準` (P2/P3/synthesis), `corroboration`→`突き合わせ/裏づけ`, `first-hand`→`一次情報として`, `golden workflow`→`基準となる作業手順`, `trade-off`→`トレードオフ`, `dogfooding`→`自社での実地利用`, `fabric`→removed/reworded, `draft/review` adjectives→`草案/査読`, `veto`→`拒否権`, `bucket`→`トークン割当量`, `strike`→`行き止まり許容`, `workflow`→`作業手順`, `autorater`→`自動評価器`, `preserved thinking`→`思考温存`, `efficacy`→`有効性`, `verdict`→`評価`, `transcript`→`トランスクリプト（推論記録）`, `faithfulness`→`忠実性`, `fast`→`高速版`, `tuning`→`調整`, `git`→`Git`, `agent` generic→`エージェント`, `headline` (P6 meta)→rewritten, `building blocks`→`構成要素`, `soon`→`近く`, `TTFT85％減`→`TTFT 85％減`.
- Accepted named-term exceptions (documented, not rewritten): SRFT (method name), pass@k, lrand48(), CC0, AlphaFold3, Qwen3.8-27B (with naming caveat), benchmark/model proper nouns.

### D10-B05 process-as-narrative — RESOLVED
- `16ページの全文が抽出されている`→`16ページの技術報告で著者らが報告している`; `39ページの報告は…全文`→`10月11日付の39ページの報告が示す`; `全文3報抽出`→`三つの技術報告の著者報告`; `39pp全文`→`39ページ報告`. Retrieval status moved to boundary records + this ledger; no reader-facing full-text claims remain.

## MAJOR

- **M01**: P5 headline `安全の四つの局面`, HEADING + new `q5-00` defining four distinct objects (開示/防御/解明/接近), table renamed `安全の四つの局面` with four rows and distinct objects, `q5-07` closing rewritten. No three-layer language remains.
- **M02**: `citation-repair-ledger-r11.json` (96 rows): every factual block narrowed to best specific URLs (≤4), use categories `VENDOR_REPORTED` (89) / `MIXED_VENDOR_PLUS_INDEPENDENT_ANCHOR` (7, only Vals-discussing blocks). Composites split (Wonder pricing vs rank; Z.ai chart vs Vals; vendor chart vs independent result). EXO omitted; AA rank not adopted. MIXED attribution computed by frozen rules matches prose attribution.
- **M03**: depth kept (license/model table P3, paper methods P6, Maia architecture P2, engineering ops P4, safety/law P5/P7); NEW P7 domain/robotics/perception comparison TABLE. Page-feasibility estimate: ~20.1k body chars + 7 tables + 7 notes ≈ 18–22pp equivalent at magazine density before opening/methodology/sources; final pagination is a Sol/layout judgment, not claimed here.
- **M04**: narrative order restored (new `qN-##` IDs in flow order; `block-diff-r11.json` maps every r10 ID → r11 ID/dropped/merged; boundary IDs unchanged). Accepted arrays/hashes untouched.
- **M05**: `独立再現` vs `独自測定` distinguished (`q5-08`); Z.ai chart omission attributed to the publisher, not Vals (`q7-01`); `公表Maia 200比（基準詳細は非公開）`; units/dates checked (`TTFT 85％減`, Oct 23 future, Jun 30 background, Oct 11 report, Nov 30 pricing).

## Coverage / dispositions (validator-enforced, 7/7 PASS)

- must_cover mapped to explaining blocks (P1:4, P2:4, P3:4, P4:4, P5:4, P6:4, P7:3); boundaries EXPLICITLY_STATED with preserved rationale; official `draft-check` 7/7 PASS; `synthesis-check` PASS.

(End of file)
