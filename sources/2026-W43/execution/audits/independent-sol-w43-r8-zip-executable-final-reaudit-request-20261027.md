# J-GAS W43 r8 — Independent Sol executable final re-audit using fixed ZIP

Date: 2026-10-27 JST
Authority: editorial Sol, new bounded independent verification commission.
Status: INDEPENDENT_SOL_ZIP_BASED_READ_ONLY_EXECUTION_REQUEST / NO_WORK / HUMAN_PDF_GATE_PENDING

## 0. Role, separation, inputs

You are the independent Sol auditor in a SEPARATE normal Chat session, independent of editorial Sol and Muse Worker. ChatGPT Work is unavailable and MUST NOT be used. The user will attach:
- JGAS_W43_r8_independent_audit.zip (4,118,744 bytes; SHA256 14132547eab1a3853ec9459832d76a7a8c5553804c7103a536874208106adfdc; 60 ZIP entries).
- JGAS_W43_r8_ZIP_technical_verification.md, the editorial Sol **non-independent** reference execution record, NOT an audit PASS.
Read this formal contract entirely and the previous independent INCONCLUSIVE report where available. Do not infer that ZIP content alone proves GitHub provenance. Do not assume the independent run has succeeded until personally executed.

All GitHub and repository operations in this audit are STRICTLY READ-ONLY. Do not create commits, branches, issues, PRs, workflows, State transitions, Human Gate approvals, Freeze or Release. Temporary local extracted files and outputs are allowed under isolated /tmp or /mnt/data only. Final Markdown audit goes to Google Drive folder GPT-Sol_Review as yyyyMMddHHmmss_SolReview.md; verify Drive readback. If Drive write is not available, report that explicitly and deliver local audit Markdown with honest limits, not fictitious upload.

## 1. Fixed subjects / remote guards

Repository: eariver/japanese-generative-ai-survey

(A) Immutable r8 PDF/TeX subject:
- HEAD 953a9d331972fdae237da4bd0f1019b17168a118
- Root Tree dfafff50c946e3d0abc051eb419797de283b192a
- r8 PDF: sources/2026-W43/execution/core-free-preview-r8/main.pdf, 487351 bytes, SHA256 abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72
- r8 TeX SHA256 4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d
- r7 TeX SHA256 9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0
- r8 original checker SHA256 58abfc0dd3fcb38bc1461a540b62ecbce92ab84eddcd5ed60439489e057e5e98
- r8 preserved build log SHA256 2242237a2533507e5cc28f27794c6eed23d9d58c2cc97b3a0ec79d21eafeb424

(B) Immutable P2 sidecar subject:
- HEAD de5e41c253de37015fdb828503040f818698c6bc
- Root Tree 5da261bfc4c1791f912033937ea1bf909f39ffc1
- Sidecar solely adds 11 paths under sources/2026-W43/execution compared with its parent c2ea53b0ca518a8c4230161242e13a7536712879; the fixed r8 PDF/TeX/checker remain UNCHANGED.

(C) Prior historical evidence:
- Fixed r7 HEAD 3b1178ff5140ff03f4291701c346a6329a228a1b, Tree a196ebb56c19d12f805793330dfca9488b024f26.
- reviewed main HEAD 041a08dfef3112643cbf85b4a86a7b6f9128aed6, Tree a134dc36a407d08ab1de416324229b3955e0325a.
- Frozen production/survey-core-v2 HEAD 774dd39a951c9ac3818e83dfffd4c7666efb0a20, Tree cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481.
- This contract belongs to a descendant commit, so NEVER audit current branch tip in place of fixed (A) and (B).

Verify fixed commits and root Trees using GitHub Git commit API, protected branch current refs, and ancestry. When missing or mismatched, report expected/actual and terminal AUDIT_PIN_NOT_VERIFIED; never quietly substitute files.

## 2. ZIP trust, safe extraction, separate independent run

1. Verify actual uploaded ZIP exists locally, exact 4118744 bytes, SHA256 14132547eab1a3853ec9459832d76a7a8c5553804c7103a536874208106adfdc, CRC of all members, exact 60 entries. Check path traversal (absolute paths, ..), symlinks and overlarge archive bombs before extracting to a fresh isolated directory. If any fail, stop audit and report.
2. Explicitly authenticate the extracted PDF/TeX/validator/build logs against SHA256 above; verify expected fixed directory layout. Use GitHub read-only refs to cross-check Git file blob IDs/sizes, not simply user-supplied ZIP claim. If locally extracted bytes differ from fixed Github bytes, STOP and report contamination.
3. Inspect original and sidecar Python source before executing; treat as untrusted repository artifacts, execute in isolated temporary folder without secrets/network and without GitHub credential write access.
4. Do not present results in editorial Sol's previous JGAS_W43_r8_ZIP_technical_verification.md as your own. The previous report is a reference for comparing outcomes and highlighting discrepancies, not a shortcut.

## 3. Required independently executed Python tests

Use Python 3 on unpacked ZIP, placing outputs in NEW temporary files only:
- Original r8 checker: sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py
- P2 sidecar: sources/2026-W43/execution/r8-p2-qa-closure/r8-p2-negative-taxonomy-sidecar.py

A. python3 .../r8-exact-fidelity-check.py --repo-root <ZIP_extract_root> --mode clean
Expected 27/27, R8_EXACT_FIDELITY_PASS, process exit 0.
B. Same checker --mode negatives. Expected 12/12, R8_NEGATIVES_PASS, exit 0. Inspect every negative case, especially N-operator-insert's limited original cause classification.
C. python3 .../r8-p2-negative-taxonomy-sidecar.py --repo-root <ZIP_extract_root> --mode all
Expected SIDECAR_STRICT_PASS and exit 0. The output comprises FOUR actual PASS cases and ONE baseline INFO. Do not call this 'five independent negative tests'. Check that the strict operator insertion triggers BOTH PROSE_FIDELITY_LOSS and READER_META_LEAK (all causes required), N10 future weight→finished triggers PROSE_FIDELITY_LOSS, N13 original vendor quote→independent measurement triggers PROSE_FIDELITY_LOSS. Verify mutation SHA differs from clean SHA, old baseline still shows only PROSE_FIDELITY_LOSS.
D. Independently ADD one NEW scientifically material mutation NOT identical to the saved original 12 cases, N13 or prior editorial Sol's N14. Prior editorial N14 mutated P8 "400問 per request（毎回の上限であり総呼出上限ではない）" to a lifetime cap and produced process exit 3, so DO NOT reuse that as an independent novel mutant. Choose a different P1–P8 outside-table scientific caveat/release/license/clock or numeric claim inversion with source occurrence count exactly 1 and tables/figures/code/bibliography unchanged. Run the exact original checker on a TEMP mutated r8 TeX via --mode clean --tex <temp-file>, record actual nonzero exit, cause(s), output SHA, and scientific meaning. Avoid only changing a word's spelling.
E. Capture real command lines, stdout/stderr, exit codes, duration if available, Python version, all checks; NEVER elevate static inspection or Muse-produced JSON to independently executed PASS. Since clean checker compares to an expected fixed baseline and sidecar wraps it, clearly state that strict r7→r8 fidelity does NOT prove all claims in the r7 baseline are scientifically true.

## 4. Required PDF binary parser + actual 22-page re-render

Read ONLY the authenticated fixed r8 main.pdf. Use local PyMuPDF/Pillow/Poppler and optionally Ghostscript:
- Inspect 22 actual PDF page objects, all A4 Media/Crop boxes, Unicode Japanese text layer, print-safe noncanonical proof metadata, 20 tables, 3 diagrams, 5 code, 5 recap paragraphs, 36 bibliography keys, 32 segmented 2-column TeX begin/end.
- Enumerate LINK KINDS, not just external URI. Reference editorial ZIP report says 75 URI, 28 distinct targets, GoTo(kind=1) 0. Note the separate observed PDF direct read: **eight TOC internal named-destination links (PyMuPDF kind=4) on PDF page 2**, in addition to 75 URI links (kind=2). Verify these eight links and their actual destination pages independently. Distinguish named-destination links from LINK_GOTO kind=1; do not mistakenly declare all internal links absent. Verify Decisions Guide and percent encoded scoped npm %2F, no broken URI, CJK punctuation in URI, no malicious/action anomalies.
- Verify embedded CJK+Latin font subsets (worker/previous editorial: 14), ToUnicode status, 22 pageboxes, and link targets. Previous editorial execution used PyMuPDF 1.26.7, Ghostscript 10.05.1, produced 75 URI / 28 external and 14 embedded fonts.
- Independently render **all 22 pages from actual PDF** >=150dpi. Compare each against Git-committed corresponding p-01.png through p-22.png, record pixel agreement and page-specific material; do not demand byte-identical PNG from different Ghostscript versions. Previous editorial execution reported average pixel identity 99.822%, minimum 99.712%; this is prior baseline only, not independent observed number. Use visual close inspection and text anchor confirmation for differences.
- Inspect all pages, especially old A/B/C: p04 Flint table 'total vs active per token', p11 FLUX FAQ attribution limits, p22 [recap] derived-source note; long Decisions JSON p18; p14-15 near saved two Overfull vbox 2.61676pt warnings. Look for unreadable footnotes, clipping, link wrapping, column reading errors, white gaps, source entries. Build 22-row page matrix with observed landmarks and any meaningful discrepancies.
- Verify physical-page correction P2-03: Table 11 starts p13 (not p12), Table 16 p17 (not p14), recap heading p20 bottom (not p19), bibliography heads p21 mid-page (not p20). Read actual PDF text + newly rendered page images, compare saved supersession.
- Inspect saved main-tex-log.txt and compiler-pass1/2.stdout.txt: 2 LuaLaTeX passes, final PDF 487351 bytes/22 pages, Overfull warnings ×2; if independent lualatex not available, mark independent rebuild NOT_DONE, don't force identical SHA across non-deterministic TeX builds.

## 5. P2 corrections, scientific/governance limits

P2-01: Sidecar historical-tree supersession corrects the malformed 39-char pre_contract_tree in immutable r8 build-manifest-r8.json to the independently verified 40-char 2429f675db817cc38333182734ed6338f1eabc68. The original manifest is NOT modified; report sidecar dependency explicitly.

P2-02: Extra process-meta classification is a controlled taxonomy supplement; strict all(e in causes ...) must hold for operator insertion; distinguish this from simply detecting arbitrary unauthorized byte edits. Novel process wording unseen by taxonomy may still be caught by exact fidelity without a dedicated READER_META_LEAK cause.

P2-03: Verify old page index QA error supersession from real PDF.

Maintain bibliographic tier bounds: 36 keys, 15 CURATED_REVIEW_REQUIRED (13 natural+2 further), 404 not proof, vendor claims do not become independent reproducibility. Versioned Architecture 31 requirement scores 20/11 (r3.2 independent) and 18/13 (r2 diagnostic) MUST NOT be treated as same authority or a current r8 substantive certification. Human PDF Gate stays PENDING; ARCHITECTURE_ESTABLISHED, Core-native Draft BLOCKED; Frozen Core v2 immutable; no publication approval/Freeze/Release.

## 6. Reporting, PASS criteria, fail-closed cases

Save Japanese Markdown independent report to Google Drive GPT-Sol_Review/yyyyMMddHHmmss_SolReview.md, and verify actual file readback when connector permits.

Required report content: exact Git pin matrix; uploaded ZIP SHA/file manifest and authenticated raw hashes; tools/versions; original checker clean/12 negatives and sidecar commands/outputs/exit codes; genuinely NEW mutant with proof of scientific materiality; PDF page tree/box/font/URI/internal link classification; 22-page re-render vs saved PNG matrix; A/B/C and P2-01/02/03 closure table; residual limitations and source-governance; P0/P1/P2 counts; full list of NOT_DONE; and one independent terminal.

Choose exactly one:
- INDEPENDENT_W43_R8_P2_SIDECAR_AND_PDF_PASS: actual Python clean/negative/sidecar/new mutant all executed and pass, authenticated PDF directly parsed + ALL 22 pages independently rendered/reviewed, P0=0 and P1=0, P2 boundaries made explicit. No requirement for original scientific claims to be independently reproduced or TeX binary build to be identical; keep those limits.
- INDEPENDENT_W43_R8_SEMANTIC_PASS_VISUAL_BLOCKED: scientific/semantic checks independently pass, but actual PDF visual evidence blocked.
- INDEPENDENT_W43_R8_REQUEST_CHANGES: confirmed significant semantic/reader-facing/PDF/provenance defect needing bounded correction.
- INDEPENDENT_W43_R8_INCONCLUSIVE: missing tools, failed trusted ZIP/materialization or mandatory execution; do not claim PASS for saved Muse results.

This is ONLY an independent recommendation; the editorial Sol makes the next human-review submission decision separately. Do not self-authorize Human PDF Gate, Release or Freeze.
