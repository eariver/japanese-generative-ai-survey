# W42 r22 reader-and-source-hash invariance (diagnostic-only; NONCANONICAL)

Date: 2026-10-18 JST. Selected C2 + Candidate B both print-only transforms of exact r21 TeX (which itself is print-only transform of exact r18 Reader). No Reader/prose/quote/order/scope bytes changed. No font/margin/line-spacing tricks, no filler.

## 1. Original master identities (read-only)

- r18 `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json`: git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` (verified `git hash-object`), 96,844B, 7 chapters/28 selected, 136 paragraphs/25,015 paragraph chars/7 tables/7 notes/7 headings/157 blocks. 7 per-chapter Draft proposals v18.0 + source authority (90 B keys, 19 aliases, 177 citation ledger rows) unchanged.
- r21 TeX `execution/diagnostic-r21/main.tex`: 95,112B/968 lines, SHA256 `278a609aa53de12097ce3b1cb78ddbbe6e09b12d6fe4d81cf361ca689feec10a`; `preview.sty` byte-identical to r20/r19/r18 (`f0492fb6…` via `git hash-object`, verified same across r21/B/C2 copies). r21 PDF 21pp 509,133B SHA `b8ac6172…`; fresh A rebuild same TeX SHA, PDF `c3f7f509…` trailer-ID-only diff (same 509,133B/pages/per-page chars; runs 2–4 identical). r21 150/150 non-TABLE blocks + 7 table texts/citations verified in r21 report (inherited here by diff transitivity).

## 2. New TeX diffs (exact, prose-preserving)

Selected C2 vs r21 (9 diff lines):
```diff
-% W42 r21 NONCANONICAL …
+% W42 r22-C2 NONCANONICAL …
 % [r19] Table 7 relocated Alt B; content byte-identical.
-
-
+\needspace{8\baselineskip} % [r22-C2] keep ASPIRE paragraph together below Table7 (print-only, no Reader change)
 NVIDIAのASPIREは、日付の切り分けがすべてだ。…
```
No paragraph/quote/cite text added/removed/reordered. All 7 `table*` blocks byte-identical (verified `grep` + `diff` shows only moves for B, no content edits for C2). All `\cite{…}` keys unchanged (169 `\cite{B` in each of r21/B/C2). All 7 captions unchanged (`WonderとArgon`/`効率主張`/`重み・実装・ライセンス`/`生産性とゲート`/`安全の四つの局面`/`科学エージェントの証拠`/`専門・身体の三件`).

Candidate B vs r21: header `r21`→`r22-B`; removed `placeins` (1 line) + 3 `FloatBarrier` lines; cut Table4/5/6 blocks (658/472/517B, byte-identical) from after Decider/METR/Deep-Review to after Scion-API/subject-separation/tool-contribution with 3 provenance comments + blanks (971 lines, matches r21 Alt-B report). No prose edits. TeX SHA `fb644c00…`, 95,106B/971 lines.

## 3. Verbatim-body/table equality (same-method, all three)

- Tables: 7/7 `begin{table*}` in r21/B/C2; captions/cites/rows byte-identical (diff shows only relocation, no cell edits).
- Non-TABLE blocks: r21 150/150 verified; C2/B inherit via zero-prose-diff (above). PDF-text spot checks (normalized whitespace): ASPIRE `v1.0告知では80課題で99%` + `卓上片づけの実機` + `凍結基盤モデル依存は弱モデル未検証` present in all three PDFs; Glimpse `WGO 42.70…HSS 46.36…` present; all chapter headings present in order P1..P7 + bibliography.
- Zero internal block IDs/editor notes in print: TeX grep 0 `alias-of`/`normalization`/`CLAIM_BOUNDARY` in all three; block-ID regex `t\d+-\d+` 1 hit each (`t7-02` in provenance comment, legitimate external code, same as r21); PDF-text block-ID pattern 0 hits; PDF-text `NONCANONICAL` count 1 (cover only) in all three.
- Body sequence via PDF extraction + visual page breaks (extraction alone NOT layout PASS): `pdftotext` full-text order P1→P7→bib identical across r21/B/C2 (modulo pagination); actual visual breaks checked on PNGs (see audit + review indexes), not source only.

## 4. Font/spacing invariants, 90/19/177

- Fonts (log): HaranoAjiMincho-Regular/Bold, HaranoAjiGothic-Bold, lmroman8/9/10/12, lmmono10, lmsans10-bold in all three; no font/margin/line-spacing changes (`preview.sty` byte-identical; `diff` sty empty).
- Bibliography: 90 `\bibitem[B` in each TeX; 19 `（同一資料）` aliases in each; 7× `[二次・参考]` display labels (B63/B64/B66/B67/B68/B70/B71) + existing B08/B10/B15 = 17 `[二次・参考]` strings in TeX, 0 `[SECONDARY]` (preserved from r21, no regression in B/C2); publishers/URLs/ledger untouched. 177-row ledger + 90-key bib-map + dup-matrix blobs unchanged (read-only, `git status` clean except new r22 paths).
- URL parsing Bxx list and aliases unchanged: PDF-text `[B` count 278 identical same-method across r21/B/C2; unique `B\d+` 92 identical; B28 complete, B57 kept-together readable, B74 `https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B` clean, B90 terminal `https://huggingface.co/LiquidAI/LFM2.5-24B-A2B` in all three.
- Prior independent regressions preserved in print (all viewed): Argon random world (no fixed seed), Maia 24 trays/96 accelerators one-pod/750GB/s, Earth model-dependent negatives, NVIDIA native MTP mean acceptance length (not rate), wetlab 131/311 vs eight clones separated, LFM license legal entity ($10M/revenue/hosting=channel), ASPIRE publisher real-robot results (LIBERO-Pro 99%, etc., with dialog-figure unresolved note).

## 5. New hashes (read-back)

- Selected C2 TeX `7e95ae849bda603ad8cbd9355befbe8c9fa8a74c1dbc7aef51b819a0e7ecaa5b` (95,226B/968 lines); PDF 21pp 509,061B `38d3796f38e91ca9d6ace2d711b72a3f219db3b17aaf82f22a44c8216f679796`; log 77,332B/1475 lines `916b6176…` 0 errors. Per-page chars [480/2495/2668/2353/2552/2431/2731/2674/1787/2526/2011/2227/2187/2231/2665/2129/2346/702/2850/3108/2698]; p01–p15 + p18–p21 PNG-identical to r21 (sha256 verified).
- Candidate B TeX `fb644c008b54c7c81024f43804597906f39d660147a51ce0f11f0a9c686a9651` (95,106B/971 lines); PDF 20pp 508,225B `26fee7bc8720dd6c36fd613a80ee61cae4c3ef6f23e7ef389476ac94ed1310ae`; per-page [480/…/2351/2434/2049/…/2115/2850/3108/2698].
- A rebuild TeX `278a609a…` identical to r21; PDF `c3f7f509…` (trailer-ID-only diff from r21 `b8ac6172…`, same bytes/pages/chars).

No shared-Core/main/canonical/State/Gate bytes touched. Only new `typeset-repair-r22/`, `diagnostic-r22/`, one session, index append.

(End.)
