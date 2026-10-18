# W42 r22 global table-and-paragraph-flow audit (diagnostic-only; NONCANONICAL)

Date: 2026-10-18 JST. Authority: `SOL_EXECUTION_AUTHORITY / R21_DIRECT_VISUAL_PRINT_BLOCKER / R22_GLOBAL_TABLE_SENTENCE_ORDER / NONCANONICAL_ONLY`. Branch existing ONLY `weekly/2026-W42-v2-work`. No Architecture revision, no Stage/Reader/Publication/Freeze/Release/Human Gate.
Status: `SOL_W42_R22_HOLISTIC_PRINT_AUDIT_READY / NONCANONICAL` (selected C2; all 7 tables + sentence continuity + old regressions visibly PASS; p18 tail residual documented as honest reasonable, not enormous avoidable; B full proof + A baseline proof archived for independent audit).

## 0. Identity guard (read-only, before any write)

- Exact Starting Remote HEAD `4850a017dcec38269ffdd943141e15d2a7c5ca48` == `git ls-remote origin weekly/2026-W42-v2-work` + `FETCH_HEAD`; Expected Starting Tree `c14605f2d15bd461c1c01a81e7b592eb0939b436` == `FETCH_HEAD^{tree}`.
- Reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19` (ls-remote + rev-parse).
- Frozen Core v2 `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- r21 baseline `84d9093da8b5bc985e6a834d356697a369211d2a`/`4789c036afd20321298f8155be2f16dce16c3ae4` (local ancestor before FF).
- All matched → proceeded. FF-only local `84d9093da` → `4850a017d` (1 Sol dispatch: r22 instruction + r21 disposition). No fallback/new branch, no reset/rebase/force. Before push rechecked remote lease (see session).

## 1. Reads (no source rewrite)

r22 contract + Sol r21 direct-visual disposition (S21-01 ASPIRE bisection HIGH/FAIL; S21-02 p18 sparse + p11 blank MAJOR) → r21 Muse session/comparison (`float-boundary-repair-and-layout-comparison-r21.md`: Alt A barriers 21pp adopted, Alt B early 20pp evaluated SHA `af413d85…` without display fix, no archived B PDF/PNGs) → r21 TeX/style/log/manifest/PDF + all 21 PNGs (opened p11–p18, confirmed Sol findings) + r21 display-map/PROPOSED brief → r20 proof (20pp) + r20/r19 controls → r18 Reader `reader-preview-r18.PROPOSED.json` (7ch/28sel/136P/25015ch/7T/7N/7H/157 blocks; blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`) + 7 v18.0 proposals + bib-map/ledger/dup-matrix (90 keys/19 aliases/177 rows) → architecture-v2 (26.5/28/30) + r1 basis/gates + production-state `63edc922…` (`DRAFT_COMPLETE`/approved/pending). MD wrapper excluded from print. No r18 master edit. No new research, no padding, no font/margin tricks.

## 2. Candidate A baseline inspection (r21 FloatBarrier, 21pp — NOT PASS)

A = committed `diagnostic-r21/` proof (PDF SHA `b8ac6172b6c122b862987030d05c365621744a714496f74d79a48d62a84da7b3`, 509,133B, 21pp) + fresh isolated rebuild (TeX SHA `278a609a…` identical; PDF `c3f7f509…` trailer-ID-only diff, same 509,133B/pages/per-page chars; runs 2–4 byte-identical). Inspected p11/p12/p13/p14/p15/p16/p17/p18 (images in `diagnostic-r21/pages/`, independently viewable):

- Tables 4/5/6 chapter boundaries SOLVED (F-08): Table4 p12 top + P5 heading same p12 below; Table5 p14 top + P6 heading same p14 below; Table6 p16 top + P7 heading same p16 below. Each table strictly BEFORE next heading in physical reading order. No table-only pages. Previous-page bottoms end complete paras; below-table starts new headings — no bisection for 4/5/6. Tables 1/2/3 in-chapter (p04/p06/p09, PNG-identical p01–p10 to r20).
- S21-01 CONFIRMED HARD FAIL: p16 right-column bottom ends mid-sentence `…v1.0告知では80課題で` (ASPIRE para1 `NVIDIAのASPIREは…` split); p17 top full-width Table7 `比較表：専門・身体の三件`; below-table continuation `99%、卓上片づけの実機（Opus 4.6模擬・GPT-5.5実機）…`. Table7 interposes between two halves of one sentence. Glimpse block intact does not excuse ASPIRE split. Images: `diagnostic-r21/pages/p-16.png` vs `p-17.png`.
- S21-02 CONFIRMED: p18 702 chars (`pdftotext` raw), left-column top only (PLawBench/Harvey/frozen/Glimpse-future/common-points), right empty, blank to inherited `\clearpage` before bib; p11 right-bottom honest barrier blank. No filler, no shrink.
- Old regressions in A all PASS (B28 complete p20, B57 kept-together p21, B74 clean, 90/71+19, 7× `[二次・参考]`, B90 terminus, cover intact, log 0 errors). But S21-01 alone disqualifies A. Not selected.

## 3. Candidate B reproduction (early relocation, 20pp — REJECTED with full proof)

Reconstructed from r18 Reader via r21-documented moves (preserving table bytes/captions/cites + r21 display fix, which r21 Alt-B SHA lacked): Table4 after P4 Scion-API para, Table5 after P5 `調べた主体を分けて書く。` para, Table6 after P6 `道具と計画の寄与は別々に測られている。` para; removed `placeins` + 3 `FloatBarrier`; header `r21`→`r22-B`. Result 971 lines (matches r21 Alt-B report `971 lines`), TeX SHA `fb644c00…`, deterministic 20pp SHA `26fee7bc…` (runs 2–4 identical), 508,225B, log 0 errors. Per-page chars 480/2495/2668/2353/2552/2431/2731/2674/1787/2526/2351/2434/2049/2693/2486/2361/2115/2850/3108/2698 — p11 2351/p12 2434/p13 2049 exactly match r21 Alt-B report. Fresh full proof archived `execution/diagnostic-r22/candidates/B/` (TeX/sty/PDF/log/manifest-B/20 PNGs + `review-pages-B.md`).

- Chapter boundaries SOLVED (all three on earlier pages, no barrier blanks, well-filled, no sparse tail): Table4 p11 top → P5 heading p12; Table5 p13 top + P6 heading same p13 below; Table6 p15 top → P7 heading p16; Table7 p17 top (ASPIRE completes p16, Glimpse starts p17 below Table7 — Table7 clean, S21-01 absent). 20pp = cover1+body16(p2–p17)+bib3(p18–p20); p17 2115 chars full.
- Holistic continuity FAIL — three real bisections by full-width tables at page tops (all viewed):
  - Table4 p11: p10 bottom-right `…無制限の` / below-Table4 `自動化ではないことの宣言であり…` (completing `無制限の自動化ではない…`, P4 `納品と検出のゲートは…` para split mid-sentence).
  - Table5 p13: p12 bottom `…隠れビッ` / below-Table5 `ト総当たりと格子…` (completing `隠れビット総当たり…`, ECDSA para split mid-word).
  - Table6 p15: p14 bottom `…採点` / below-Table6 `コードまで公開…` (completing `採点コードまで…`, baseline-procedure para split mid-phrase).
  Images in `candidates/B/pages/p-10.png`→`p-11.png`, `p-12.png`→`p-13.png`, `p-14.png`→`p-15.png`.
- Preview-before-details tradeoff (tables before some summarized prose, e.g. Table4 before HydraFusion/AutoFix/Decider details) is legitimate article design per contract and NOT the rejection reason. Rejection is solely physical sentence/word bisection, which logs cannot excuse.
- Additional trials: C3 = B + 3× `needspace` before the three split paras stays 20pp but merely shifts splits to adjacent paras (verified p11/p13/p15 still split); C1 = A + Table7 after ASPIRE gives 22pp with Table7 p18-top sparse 825 chars + p22 208-char bib orphan (worse). Both documented and rejected; hashes in session. Neither achieves clean 20pp.

Therefore B proves 20pp tail fix exists but does NOT pass holistic flow. Rejected; archived for audit, not selected.

## 4. Candidate C2 selected (A-base + Table7 needspace paragraph-boundary, 21pp — ADOPTED)

Change from exact r21 TeX: header `r21`→`r22-C2` (same length class, provenance only) + ONE `needspace{8\baselineskip}` before ASPIRE para1 (`NVIDIAのASPIREは…`) with provenance comment; 2 blank lines removed for clean separation (total 964→968 lines? Actually 968 lines, TeX 95,112B→95,226B +114B needspace line; SHA `278a609a…`→`7e95ae84…`). `preview.sty` byte-identical. No prose/quote/order/scope bytes changed; all 7 table blocks byte-identical; display map unchanged. Diff 9 lines (see invariance doc).

Build isolated clean workspace, deterministic epoch ×4 (runs 2–4 byte-identical SHA `38d3796f…`, 509,061B, 21pp, log 77,332B/1475 lines 0 errors). Archived `execution/diagnostic-r22/` (TeX/sty/PDF/log/manifest/21 PNGs/3 contact sheets/review index).

Visual QA ALL 21 pages (see `review-pages-r22.md`):
- Tables 1/2/3/4/5/6 placements identical to A (p01–p15 PNG-identical to r21, verified sha256): Table1 p04 + P2 same-page; Table2 p06 + P3; Table3 p09 + P4; Table4 p12 + P5 same-page; Table5 p14 + P6 same-page; Table6 p16 + P7 same-page. Each strictly BEFORE next heading, previous-page bottoms complete, below-table new headings — zero bisections. F-08 remains solved, no recurrence.
- Table7 S21-01 FIXED: p16 ends complete (`…注意を落とさない。[B55,B53,B54]`, end of `ただし独立の根拠にも限界はある…` para) + honest needspace blank (right-bottom ~1/4 page, not massive); p17 Table7 top; below-table fresh `NVIDIAのASPIREは…` through `…まま残る。[B57,B56,B89]` complete, then `リポジトリ…`, `実機…`, Glimpse, note box. No sentence carried across Table7. Before/after side-by-side in review index. Table7 in P7 (p17, after P7 heading p16, before bib p19) — in-chapter, before next heading. No table-only page.
- S21-02 residual: p18 identical to r21 (702 chars, 5 closing paras, left-only, right empty, blank to inherited `\clearpage`). Honest short tail from +1-page barrier expansion, not padding, not table-only/stamp-only, legitimate closing content, within Sol tentative max23. p11 barrier blank + p16 needspace blank both honest, none massive, no large avoidable void beyond inherited pagination cost. No filler/font/margin tricks. Judged reasonable physical fill: all body pages except p18 tail are 2011–2731 chars (full); p18 tail is closing fragment, not enormous empty (28% of typical full page, 5 paras). Avoiding it requires B layout which introduces three hard bisections (proven); therefore tail is NOT avoidable while maintaining continuity with supported print-only changes. Documented, not hidden.
- Old regressions all PASS (same as r21, verified same-method): Argon random world (no fixed seed), Maia 24 trays/96 accelerators one-pod/750GB/s, Earth model-dependent negatives, NVIDIA native MTP mean acceptance length (not rate), wetlab 131/311 separate from eight clones, LFM license legal entity, ASPIRE real-robot results; B28 complete p20, B57 kept-together p21 readable, B74 clean URL, 90 labels (71 full + 19 `→ [Bxx]（同一資料）`), B90 terminal `…/LFM2.5-24B-A2B`, 3-line NONCANONICAL cover intact, `[二次・参考]` 7× preserved, no machine provenance (0 `alias-of`/`normalization`/`CLAIM_BOUNDARY`; block-ID only `t7-02` in provenance comment), B-count PDF-text 278 identical across r21/B/C2, no wrapper injection. Log 0 errors/warnings.

## 5. Comparison and selection reason (objective, publication-readable)

| Axis | A (r21, 21pp) | B (early, 20pp) | C2 selected (21pp) |
|---|---|---|---|
| Tables 4/5/6 before next heading | PASS (p12/p14/p16 + headings same-page) | PASS (p11/p13/p15, earlier) | PASS (same as A, PNG-identical p11–p15) |
| Table7 before bib + in P7 | PASS position, FAIL continuity (bisects ASPIRE sentence p16→p17) | PASS position + PASS continuity (ASPIRE completes p16) | PASS position + PASS continuity (ASPIRE starts fresh p17 below Table7) |
| Sentence/paragraph continuity (all 7 tables) | FAIL (1: ASPIRE) | FAIL (3: P4/ECDSA/baseline, incl mid-word) | PASS (0 bisections, all 7 at paragraph boundaries, verified) |
| Sparse tail / voids | p18 702-char tail + p11 blank (honest) | No tail (full p17), no blanks (dense) | p18 702-char tail (same as A) + p11 blank + p16 needspace blank (all honest, none massive) |
| Pages | 21 | 20 | 21 |
| Reading order fidelity | details-then-summary (authorial) | preview-then-details (tables before some details; legitimate but less faithful) | details-then-summary (as A) |
| Old regressions | PASS | PASS (display preserved) | PASS |

Do not reject B merely for preview-before-details (contract allows it); reject B solely for three physical bisections. Do not favor A/C2 merely for 21pp equaling Sol tentative target (target is NOT success criterion; no padding). Select C2 because it is the ONLY candidate with zero real bisections, zero chapter crossings, zero table-only pages, preserved authorial table-after-prose order, and honest pagination (21pp acceptable under Option B; 20 valid but B fails continuity; 22 (C1) worse). C2 fixes S21-01 hard FAIL, preserves F-08 fixes with no recurrence, and holds S21-02 to same honest tail as A (not worsened; proven unavoidable without breaking continuity). Effective occupied body area `UNMEASURED; <=17 PHYSICAL BODY PAGES` (no invented 15.5–17).

## 6. Frozen authority re-verification (read-only)

r18 Reader blob `fc4fd9f2…`, P1–P7 proposal SHAs, bib-map/ledger/dup-matrix (90/19/177), `editorial-revision-r18/` diff empty except new r22 paths; production-state `63edc922…` (`DRAFT_COMPLETE`/approved/pending); checkpoints/approvals/review-index; canonical Draft/Synthesis v10.0; Evidence/Views/Materiality/Selection/Architecture; r11–r21 execution bytes; main + Frozen Core. All untouched. Only new edition-local: `typeset-repair-r22/`, `diagnostic-r22/`, one session, index append. No formal Reader/Publication, no architecture amendment.

Stop: `SOL_W42_R22_HOLISTIC_PRINT_AUDIT_READY / NONCANONICAL` — ready for Sol + independent focused image QA (A p16/p17 vs C2 p16/p17 vs B p10/p11/p12/p13/p14/p15 + manifests), then Human editorial page-plan consultation via PROPOSED brief. No candidate, no Gate action.

(End — 7/7 tables, 7/7 chapter boundaries, all paras checked on real pages, not TeX source only.)
