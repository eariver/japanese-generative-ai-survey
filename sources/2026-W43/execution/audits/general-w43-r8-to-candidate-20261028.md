# GENERAL independent adversarial regression audit: W43 r8 proof baseline vs canonical candidate

VERDICT: GENERAL_W43_EQUIVALENCE_PASS

Date (UTC): 2026-10-28. Auditor role: independent regression auditor ("General"), read-only; no TeX/PDF/JSON edits, no rebuilds, no commits. All evidence below was derived by the auditor directly from file bytes (sha256sum, diff, PyMuPDF 1.28.2 text/link/font/TOC extraction, independent r150 PNG renders of all 22 pages). Worker evidence files were used only as secondary cross-checks, never as primary authority. Scratch: /tmp (diff at /tmp/r8_to_cand.diff, extracts at /tmp/r8.txt and /tmp/cand.txt, renders at /tmp/general-renders/cand-p01..22.png).

Scope note: this audits BYTE/RENDER equivalence of the canonical candidate against the Human-approved r8 proof baseline. It does not re-litigate r8's own editorial correctness and is not a publication gate.

## 1. SHAs measured by the auditor (all match expected/worker-claimed values)

| File | SHA256 measured | Bytes | Expected / worker claim | Match |
|---|---|---|---|---|
| sources/2026-W43/execution/core-free-preview-r8/main.pdf | abd5b99bd051703dbdc9420c19965ed039585c0436090ae6e65c6d17dc72 | 487351 | abd5b99b... (task baseline) | YES |
| sources/2026-W43/execution/core-free-preview-r8/main.tex | 4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d | 97447 | task string gives prefix 4ed553e5d779dc6696322fe6eba (appears truncated; first 48 hex chars identical to measured) | YES (prefix) |
| surveys/weekly/2026-W43/main.tex (candidate) | 3fa6ca3b4c610cd12fecd3e6ce449e0d9cffd9e7edc67efb1b85f5bd0e758784 | 97156 | worker-claimed (bound in 5 formal records, verified in section 7) | YES |
| surveys/weekly/2026-W43/main.pdf (candidate) | b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165 | 486967 | worker claim b09fd181... | YES, exact |
| surveys/weekly/2026-W43/preview.sty | 0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44 | 6109 | identical to r8 preview.sty (diff -q: identical) | YES |
| sources/2026-W43/execution/core-free-preview-r8/preview.sty | 0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44 | 6109 | — | — |

Commands: `sha256sum` on all five paths; `stat -c '%n %s bytes'`; `diff -u r8/main.tex cand/main.tex > /tmp/r8_to_cand.diff` (29 lines incl. headers); `pdfinfo` on both PDFs (both: 22 pages, A4 595.276x841.89, LuaLaTeX/LuaTeX-1.24.0, PDF 1.7).

Byte deltas candidate-vs-r8: PDF -384 bytes, TeX -291 bytes — direction and magnitude consistent with banner/metadata-line removal only (see section 2).

## 2. TeX diff, classified hunk by hunk (complete diff, nothing else differs)

`diff -u` output is 4 hunks only (full text verified by auditor):

1. L1 comment: r8 `% W43 r7 NONCANONICAL Core-free PDF proof ... UNVALIDATED, NOT a publication candidate.` replaced by candidate `% W43 canonical Reader TeX -- faithful canonical rendering of the Human-approved r8 reader arrangement (r8 TeX 4ed553e5...); proof-only marks removed, no reader prose/cell/citation change.` — REQUIRED canonical-metadata/comment change, non-rendered. No P-class.
2. `\hypersetup`: `pdfsubject/pdfkeywords = NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` replaced by `pdfsubject={Japanese Generative AI Technical Survey -- 2026-W43}`, `pdfkeywords={2026-W43, weekly survey}` — REQUIRED canonical-metadata change, non-rendered body. Verified in candidate PDF metadata via pdfinfo/PyMuPDF. No P-class.
3. Cover safety-mark line removed: `\surveycover` followed by `{\centering\footnotesize\color{SurveyMuted}--- NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF \quad NOT A PUBLICATION PREVIEW ---\par}` — rendered banner removal, intended. This line also explains the single `\footnotesize` census delta (30 in r8 vs 29 in candidate; zero real `\footnote{` in either file). No P-class.
4. End-of-document banner removed: `\begin{center}\color{SurveyMuted}--- NONCANONICAL ... NOT A PUBLICATION PREVIEW ---\end{center}` before `\end{document}` — rendered banner removal, intended. No P-class.

Classification: 2 required canonical-metadata/comment changes + 2 intended rendered proof-banner removals = the worker-claimed "4 proof-mark line removals". Zero hunks touch prose, numbers, qualifiers, tables, figures, code, citations, or bibliography. Any substantive meaning/source/number/qualifier change would be P0/P1 — none exists.

## 3. Rendered-text comparison (both PDFs extracted by auditor)

- r8 extracted chars: 43299; candidate: 43149; delta -150.
- Unified text diff: exactly 4 removed lines (2 per banner: `— NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF` / `NOT A PUBLICATION PREVIEW —`), one block after the cover descriptor line (p1) and one after the final Decisions entry (p22). Nothing added, nothing else altered.
- Per-page text identity: pages 2–21 byte-identical as extracted text; p1 and p22 differ ONLY by the removed banner block (verified char counts: p1 578→503, p22 3456→3381; all other pages identical lengths).
- Whitespace-normalized full-text comparison: after stripping the two banner strings, the only residual is 4 dash characters (the `—...—` wrappers), i.e. no prose delta.
- Candidate extracted text contains zero occurrences of: NONCANONICAL, UNVALIDATED, PROOF, pipeline, ledger, GATE, INTERNAL. No reader-visible production metadata.
- Source cutoff present in candidate TeX L10 and rendered cover (p1): `2026-10-16 22:00 UTC -- 2026-10-23 22:00 UTC (Oct 17 07:00 JST -- Oct 24 07:00 JST)`.

## 4. Visual inspection — auditor's own renders, all 22 pages (150 dpi via PyMuPDF, /tmp/general-renders/)

- p1 (cover): neutral; title, 2026-W43, 2026-10-24, cover story, Editorial cutoff / Repository / Build block, Evidence-chain line. No proof banner. Clean.
- p2 (TOC): header/footer intact; 8 entries with leaders and targets 3/6/9/11/12/14/15/17 — match get_toc destinations exactly. Clean.
- p3 (P1 head + 表1): two-column body, full-width table, 典拠キー row. Caveat-A material visible (Flint total-vs-active denominators, 対応/推奨/設定三層). Clean.
- p4 (表2/表3 + 注意): denominator-explicit headers, no clipping. Clean.
- p5 (表4 + 文脈長の三層 figure box + 読み方の注意): figure box renders boxed, no overflow. Clean.
- p6 (P2 head + 表5 + code-discussion prose): section divider geometry holds. Clean.
- p7 (表6 + MemT prose): full-width table intact. Clean.
- p8 (表7 + 設定例A/B code blocks): two verbatim-style blocks render in monospace, no wrapping corruption. Clean.
- p9 (P3 head + 表8 + 注意 box): clean. p10 (表9 + 資格・承認フロー figure + 注意): figure box intact. Clean.
- p11 (P4 head + 表10 + Elo prose): caveat-B block present verbatim (FAQ未照合, 確定した矛盾としない, UNKNOWN apparatus). Clean.
- p12 (注意 box + P5 head): clean. p13 (表11/表12): clean. p14 (表13 + P6 head): clean, no visible vbox artifact. p15 (figure 協調開示の五段階 + 注意 + P7 head): clean, no visible vbox artifact. (The 2 benign 2.61676pt output-routine overfull vboxes sit at the p14→p15 boundary in BOTH build logs at the identical locus — pre-existing r8 condition, visually clean.)
- p16 (表14 + SQL prose): clean. p17 (表15/表16 + P8 head): clean. p18 (表17 + Decisions JSON code block): long JSON block renders without clipping; URL wraps correctly. Clean.
- p19 (表18 + prose + SHA/clock lines 15:18:14Z / 15:21:49Z visible): clean. p20 (表19/表20 + 注意 + 今週の総括 head + recap paras 1–2): clean.
- p21 (recap paras 3–5 + 出典一覧と確認水準 + 参考文献 head + KIMI/FLINT/NEMO/DI entries): clean, two-column bib. p22 (bib continued through decisions-ref-create + [recap] derived entry): ends with page number 22, no trailing banner. Clean.
- Across all pages: running heads (left title / right 2026-W43), footers (page numbers), section dividers, full-width tables/code/figure boxes, two-column bib — all intact; zero clipping, corruption, missing content, or metadata leakage observed.
- Secondary check: worker page-PNG ledger char counts match the auditor's independent per-page extraction on all 22 pages (22/22).

## 5. Count table — expected (r8 baseline) vs measured by auditor from candidate bytes

Every census below was run independently on BOTH TeX files and BOTH PDFs; columns are equal except where noted with cause.

| Invariant | Expected (r8) | r8 measured | Candidate measured | Verdict |
|---|---|---|---|---|
| Sections P1–P8, canonical order/titles | 8 | 8 | 8, identical titles | PASS |
| Tables (tabularx envs) | 20 | 20 | 20 | PASS |
| Table body rows (auditor `\\`-split; +20 captions = 80 ordered rows) | 80 ordered rows | 60 + 20 | 60 + 20 | PASS (equal; baseline label reconciled) |
| Table cells (auditor &-split) | 307 | 232 | 232 | PASS (equal; method-dependent label, r8==cand exactly) |
| Figures (full-width tcolorbox: 文脈長の三層 / 資格・承認フロー / 協調開示の五段階) | 3 | 3 | 3 | PASS |
| Code blocks (verbatim) | 5 | 5 | 5 | PASS |
| Bibkeys, canonical order | 36 | 36 (list verified identical) | 36, identical list/order | PASS |
| 典拠キー lines | 15 | 15 | 15 | PASS |
| 典拠 occurrences | 34 | 34 | 34 | PASS |
| \label / \captionof / multicols begin/end | 10 / 20 / 32+32 | same | 10 / 20 / 32+32 | PASS |
| \footnotesize (explained: one lost with cover banner) | 30 (r8) | 30 | 29 | PASS (only delta, caused by hunk 3) |
| Real \footnote{ | 0 | 0 | 0 | PASS |
| URI actions / unique targets / malformed | 75 / 28 / 0 | 75 / 28 / 0 (83 annots incl. 8 named dests) | 75 / 28 / 0, identical URI set | PASS |
| Fonts embedded | 14 | 14 (subset-prefixed Type0/Identity-H) | 14, same families (one subset tag rename JWHAJN→UCMWBM on LMRoman10-Regular: rebuild artifact, P2) | PASS |
| TOC targets | 3/6/9/11/12/14/15/17 | same via get_toc | 3/6/9/11/12/14/15/17 | PASS |
| Pages / size | 22 A4 | 22 A4, all rects 595.3x841.9 | 22 A4, all rects 595.3x841.9 | PASS |
| Overfull vbox | 2 benign pp14–15 | 2x 2.61676pt, same locus in r8 log | 2x 2.61676pt, same locus in cand log | PASS (pre-existing) |
| Underfull / missing chars / LaTeX errors+warnings | 0 | 0 (per build logs) | 0 (per candidate build log + preflight record) | PASS |
| NONCANONICAL/UNVALIDATED/PROOF in reader bytes | 0 | present (proof) | 0 in TeX and extracted PDF text | PASS |
| Recap position/content | 5 paras after P8 before bib | 5 paras L926–945 | 5 paras, identical (diff-proven) | PASS |
| Bib [recap] derived entry | present, no new claims | present | present (`新規数値なし ... 新規の一次主張を含まない`) | PASS |

High-signal number sweep (TeX counts r8==cand; PDF normalized counts confirm all present): Kimi 2.8T/104B, X 17:15:24Z; Flint 39.8B/2.5B/512k/256k/262144/Apache-2.0/49層/256 experts/SWA-513/150144/2026年6月; Nemotron 8B/4B/OpenMDW-1.1; FLUX 25.37x/22.31x/95.52%/26.5x/277.80/10.95/12.45; Decisions 400/404/HTTP paths; GH/npm clocks 15:18:14Z/15:21:49Z; 10月22日/23日; 9946B; 10億ドル Daybreak; cutoff 2026-10-16/2026-10-23/22:00. Row qualifiers (`直接比較できず`, `独立未再現`, `原表未取得`, `未照合`, `候補分母にしない`, `正として引用しない`) intact. All 36 bibkeys and all qualifier tiers (一次資料/保存済み/発行元記述/未照合・未解決/派生・限定/入手不可) preserved in canonical order with the keyframes-conflict and recap entries verbatim.

## 6. A/B/C fixed-caveat status (verified in candidate TeX AND rendered PDF text)

- A (p4, Flint total-vs-active denominators): PRESENT verbatim — `Flintの total／active per token とは計数規約が一致しないため、8B・4B・39.8B・2.5Bを等価に比較して優劣表を作ってはならない`, 表2 header `計数規約を見出しに明記`, 対応≠推奨≠設定三層. (PDF extraction inserts line-break spaces, e.g. `512k対応・256k推奨`; whitespace-normalized match confirmed.)
- B (p11, FLUX FAQ not independently reconciled): PRESENT verbatim — `FAQに由来するとされる未照合の記述「Two at launch（二様式で開始）」との未照合の食い違い`, `出典・版・観測時刻は未特定`, `発行者間の確定した矛盾とはしない`, `確定した資料間矛盾ではない`, `W43のlive／schema／GAは未検証`, bib `flux-keyframes-conflict [未照合・未解決] ... 確定矛盾としない`.
- C (p22/recap derived synthesis): PRESENT verbatim — bib `[recap] [派生・限定] URL未取得 --- 新規数値なし. 本号の各主題を整理した派生記述。新規の一次主張を含まない。` plus recap body closing (no first-hand claims).

## 7. Formal-record byte-binding spot check (independently hashed by auditor)

- reader-manuscript-v2.json binds TeX 3fa6ca3b... (byte_count 97156 — matches actual) and preview.sty 0199d86d... (6109 — matches actual). No PDF SHA in this manifest (by schema); PDF binding lives in the review/bundle records.
- quality-regression-bundle-v2.json binds TeX 3fa6ca3b... + PDF b09fd181... (486967 — matches actual) + all three deterministic artifacts by SHA.
- semantic-editorial-review-v2.json and visual-review-v2.json each bind TeX 3fa6ca3b... (97156) + PDF b09fd181... (486967) + 22 pages + reader_manuscript c24e0fe6b....
- reader-surface-semantic-review-v2.json and reader-surface-gate-v2.json bind TeX 3fa6ca3b... (+ sty 0199d86d..., mapping 462c2f4c..., manuscript c24e0fe6b...).
- deterministic/pdf-preflight.json: pages 22, pdf_bytes 486967, pdf_sha256 b09fd181..., tex_sha256 3fa6ca3b..., 0 errors, 2 benign vbox (same locus/note as r8), 0 underfull/missing-chars/warnings. identifier-preservation.json and subject-entity-property-binding.json (75 actions/28 targets/0 malformed — matches auditor's own 75/28/0 census) bind TeX 3fa6ca3b....
- NO byte mismatch found in any of the 7 formal records + 3 deterministic artifacts: every bound TeX/PDF SHA and byte count equals the auditor-measured bytes. No P0.
- Architecture cross-check: gates/architecture-approval.json is a Human APPROVED record (r6, 2026-10-25, architecture SHA 7d8f0ea5..., reviewed commit 809cd45...); manuscript architecture_coverage lists 31/31 FULFILLED, each carrying the explicit `13+2 CURATED_REVIEW_REQUIRED維持` and `旧版段階評価（20/11）の移植は行わない` qualifiers — i.e. the records openly state the stale versioned grades were NOT transplanted, so there is no silent false upgrade of the 11 partial obligations in the bytes. (Whether FULFILLED-via-delegation satisfies the Human gate is a Human judgment, not an r8-equivalence defect.)

## 8. Findings

P0 (wrong number/claim/attribution, missing content, broken reference/link, metadata leak, byte mismatch in formal records): NONE — zero findings.
P1 (qualifier/caveat weakened or dropped, table/cell/anchor loss, layout harming legibility): NONE — zero findings. All A/B/C caveats verbatim; all 20 tables/3 figures/5 code blocks render cleanly; TOC/section/recap/bib order intact.
P2 (cosmetic/typographic only, explicitly bounded): 
- P2-1: L1 TeX comment reworded (non-rendered, documents the canonicalization honestly).
- P2-2: pdfsubject/pdfkeywords canonicalized (intended removal of NONCANONICAL marks; verified in PDF metadata).
- P2-3: CreationDate/ModDate 2026-10-28 09:00 JST rebuild timestamps (epoch-pinned per preflight record; deterministic).
- P2-4: One CJK/Latin subset-tag rename (JWHAJN→UCMWBM on LMRoman10-Regular); 14/14 families still embedded, text extraction unaffected.
- P2-5: The 2 benign 2.61676pt output-routine overfull vboxes at the p14–p15 boundary are carried over from the identical r8 locus (pre-existing, visually clean on inspection).
- P2-6 (note, not a defect): worker census labels (80 ordered rows / 307 cells / 77 anchors / 29 claims) use the worker's own counting convention; the auditor's independent recount (60 body rows + 20 captions = 80; 232 &-cells; 34典拠+15典拠キー+10labels+etc.) agrees r8==candidate exactly on every sub-count, so equivalence is unaffected regardless of convention.

## 9. Commands run (auditor's own)

sha256sum+stat on r8/candidate TeX+PDF and both preview.sty; `diff -u` r8→candidate TeX; pdfinfo on both PDFs; PyMuPDF scripts for: full-text extraction + unified text diff, per-page text identity (22 pages), whitespace-normalized comparison, section/caption/label/verbatim/bibitem/url/典拠 censuses on both TeX files, font/link/TOC/rect extraction on both PDFs, normalized high-signal-number sweep, metadata-string scan; independent r150 render of all 22 candidate pages + read-inspection of each; formal-record SHA/byte cross-checks (json.load + re-scan for 64-hex bindings); build-log Overfull comparison (candidate log vs r8 logs); preview.sty diff -q; worker ledger char-count cross-check (22/22 match).

VERDICT: GENERAL_W43_EQUIVALENCE_PASS (zero P0/P1; six bounded P2 notes above, all nonblocking; candidate preserves the Human-approved r8 proof baseline with only the four intended proof-mark line changes).
