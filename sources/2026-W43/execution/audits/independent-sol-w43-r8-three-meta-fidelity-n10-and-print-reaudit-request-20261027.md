# J-GAS W43 r8 — Independent Sol 3-meta, N10, build-trace and new-PDF re-audit contract

Date: 2026-10-27 JST.
Status: INDEPENDENT_SOL_R8_READ_ONLY_AUDIT_REQUEST / R8_NONCANONICAL_PRINT / HUMAN_PDF_GATE_PENDING.
Repository: eariver/japanese-generative-ai-survey.
Executor: a SEPARATE independent Sol session (not Muse worker or editorial Sol).
Write final Japanese audit to Google Drive folder GPT-Sol_Review as yyyyMMddHHmmss_SolReview.md. No repository/GitHub writes, no State/Gate/Architecture/Core modifications, no branch creation, no PR/issue, no Freeze/Release.

## 0. Exact fixed audit subjects: do not substitute post-request tip

Fixed r8 Muse implementation commit:
- Branch for ancestry: weekly/2026-W43-v2-work.
- **Fixed r8 HEAD: 953a9d331972fdae237da4bd0f1019b17168a118.**
- **Fixed r8 root Tree: dfafff50c946e3d0abc051eb419797de283b192a.**
- Fixed r8 sole parent (r8 instruction contract): 88a6ffbb1ceffd6cef0ecdf0e2af1d489993bbca, root Tree e50ff33f8215c50b4f76e4128b05992f18883d0f.
- Historical fixed r7 subject: HEAD 3b1178ff5140ff03f4291701c346a6329a228a1b, root Tree a196ebb56c19d12f805793330dfca9488b024f26.
- Protected main HEAD 041a08dfef3112643cbf85b4a86a7b6f9128aed6, root Tree a134dc36a407d08ab1de416324229b3955e0325a.
- Protected Frozen production/survey-core-v2 HEAD 774dd39a951c9ac3818e83dfffd4c7666efb0a20, root Tree cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481.

The separate audit request is committed AFTER r8; current branch tip may advance by one documentation-only commit. Verify remote branch ancestry and exact protected main/Frozen pairs, inspect fixed r8 commit object by full immutable SHA, compare to r8 instruction parent (one FF commit, W43 execution paths only). If any fixed object cannot be accessed, report AUDIT_PIN_NOT_VERIFIED; never silently audit current tip as r8.

## 1. Immutable r8 output objects to authenticate

- PDF: sources/2026-W43/execution/core-free-preview-r8/main.pdf
  reported SHA-256 abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72, 487351 bytes, 22 A4 pages. Actual Git blob ae195cdc283071cb8d220e0d9672183fe3a8befa.
- TeX: sources/2026-W43/execution/core-free-preview-r8/main.tex
  reported raw SHA-256 4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d, 97447 bytes.
- style: core-free-preview-r8/preview.sty SHA-256 0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44 (identical to fixed r7).
- preserved build trace:
  core-free-preview-r8/main-tex-log.txt size 78170 bytes, reported SHA-256 2242237a2533507e5cc28f27794c6eed23d9d58c2cc97b3a0ec79d21eafeb424; actual Git blob d1b8449af49b249928c7a2d5d29db25005180269.
  core-free-preview-r8/compiler-pass1.stdout.txt 17504 bytes, SHA-256 feebd453523886a73a437323017612e5af94d455a9d35e79555dd7cbb11d4228;
  core-free-preview-r8/compiler-pass2.stdout.txt 17412 bytes, SHA-256 e59feddcc99d81f7495655a6ea0737d0c09a96d64a43983e359e0fbc377826e4.

Independently fetch actual binary/source/log bytes and recompute SHA-256, Git objects, page boxes, object stream metadata, CJK fonts, links, text extraction. Distinguish actual audited evidence, worker manifest claims, missing tooling and unverified claims. Do not call PDF visual PASS from a SHA alone.

## 2. Previous r7 audit to close, without upgrading existing boundaries

Previous independent Sol report: 20261027035724_SolReview.md (https://drive.google.com/file/d/1G97p7LnH5R3qeHLFMnE5JMfYt7ZcUDBW/view?usp=drivesdk).
Terminal INDEPENDENT_W43_R7_REQUEST_CHANGES, P0=0/P1=1/P2=4.
The r6 two-column defect had been independently accepted as visually corrected at r7, and r7 PDF 22/22 individual page PNGs had been viewed, but r7 PDF itself had not been independently rerendered.
P1 W43-R7-AUD-01: three reader-visible operator/approval metadata residue:
 A p04 Flint table 2: 計数規約は承認済みArchitecture境界注記
 B p11 FLUX paragraph: 承認済みArchitectureの旧ラベルはraw検証待ちの legacy として保持, plus duplication
 C p22 bibliography [recap]: P1-P8横断の編集合成.
P2 W43-R7-AUD-02: missing committed build log; AUD-03: N10 normal prose meaning inversion missed by prior checker; AUD-04: independent PDF self-render/parser/rebuild not completed; AUD-05: versioned 31 Architecture grading and 15 curated evidence links.

New r8 worker claims:
- r7→r8 TeX entire file equals EXACTLY A/B/C permitted changes; style identical.
- A becomes technical difference between total and active per token, no alteration of 39.8B/2.5B and underlying licensing/context claims.
- B condenses FLUX PR/blog versus FAQ-attributed (unverified URL/version/timestamp) difference: NOT a confirmed official contradiction, no keyframes/live/schema/GA invented.
- C becomes 本号の各主題を整理した派生記述, retaining derived-only, URL未取得 and no new data.
- 27/27 new strict clean, 12/12 saved negatives; old N10 Python check_mutation returned [] when executed by worker, new strict checker catches mutation with PROSE_FIDELITY_LOSS.
- PDF rerendered from changed r8 TeX, 22 A4 pages; all 22 new page PNGs viewed at full resolution by worker; full logs committed.
- 20 tables, 80 rows, 307 nonempty table cells (one authorised replacement), 3 figures, 5 code, 5 recap paragraphs, 36 bibliography keys, 29 claim anchors.
- 32 matched segmented two-column environments; bibliography two columns, wide tables/code/figures outside segment.
- PDF link/font worker analysis: 75 URI annotations, 28 unique HTTP URIs, 0 CJK-malformed links, 14 embedded subsets; selectable Unicode. 28 unique URLs vs 36 bibliography keys is NOT by itself a defect.

Challenge these claims. Editorial Sol already independently retrieved r7/r8 TeX strings and whitelist JSON via GitHub and verified **exactly three substitutions, exactly once each, no other TeX text differences** and style byte-identical. This check is NOT a substitute for PDF visual or validator independent run.

## 3. Audit A — whole-reader metadata and scientific fidelity

Re-read fixed r7 and r8 TeX in full; compare against core-free-preview-r8/meta-closure-and-semantic-diff-r8.json and the actual physical PDF text. Confirm exact A/B/C substitutions and preserve all: published API vs promised weights, vendor vs independently reproduced benchmarks, FLUX FAQ raw not verified, licence and rights scope, GH timestamp 15:18:14Z vs npm 15:21:49Z, npm raw not archived, cost/unit/comparator caveats, 404 nonproof, post-cutoff epistemic limits. Do not treat evidence disclaimers as mere operator meta.

Read every PDF page of new r8; scan cover, title, P1–P8 narrative, every table cell/caption, figure body, code preface, bibliography, references, recap and proof footers for unknown residual production/review/gate/approval phrasing beyond the old A/B/C list. Machine-only TeX comments/labels and separate NOT A PUBLICATION PREVIEW protective marks are permitted; printing them as a substantive article claim is not.

Verify 3 closures with explicit page + source-line citations:
- A at r8 printed p04;
- B at r8 printed p11;
- C at r8 printed p22.
If any further residual found, new finding with exact page and suggested bounded correction. No editorial rewriting outside scope.

## 4. Audit B — strict independent validator replay and genuinely NEW mutation

Read full core-free-preview-r8/r8-exact-fidelity-check.py, runbook, source r7/r8 TeX and saved r8-fidelity-clean.json / r8-fidelity-negatives.json. In independent isolated worktree/staged-dir, rerun **the real exact same checker** clean (claimed 27/27, exit 0) and negatives (claimed 12/12, exit 0), recording command, actual terminal exit code, pass count and EACH observed fail cause of deliberate mutants. Do not report independent rerun when only static source review is done.

Must replicate N10 ordinary P1 paragraph future-weights→already-finished inversion against unmodified scientific row and qualifier counts, record actual rejection PROSE_FIDELITY_LOSS and contrast with r7 old blind spot if runtime supports it. Add at least ONE NEW scientifically meaningful mutation not among 12 saved cases (not just another spelling variant) and verify actual detection. Prefer an outside-table P2/P5/P8 change preserving key qualifier word count and all row/fig/bib totals.

**Audit-specific potential test weakness to investigate (not yet a proven blocker):**
- Saved N-operator-insert entry says expected [READER_META_LEAK, PROSE_FIDELITY_LOSS] but observed only [PROSE_FIDELITY_LOSS]. The r8 test function uses any(e in causes for e in expect), NOT all, so a PASS label does not prove the distinct READER_META_LEAK cause fired. Determine whether meta-leak detection taxonomy is genuinely insufficient for unfamiliar operator prose, and independently assess P2 severity. The full exact byte-fidelity check does reject the insertion, so do not mislabel it a successful semantic bypass.
- Additional audit-specific raw provenance error: r8 build-manifest-r8.json pre_contract_tree field reads **2429f675db817cc38333182734ed6338e1abc68 (39 characters, invalid Git tree identifier)**, while the actual verified pre-contract parent tree is **2429f675db817cc38333182734ed6338f1eabc68 (40 characters)**. Current fixed r8 HEAD/root Tree and PDF are distinct correctly pinned objects. Confirm incorrect metadata, report as bounded P2 correction if justified, do not mutate immutable r8 files.
- r8 exact expected source is fixed r7, not a new independent source-of-truth audit of r3.5 original. Do not overstate universal original→print integrity based solely on the r7→r8 exact diff.

## 5. Audit C — full NEW r8 print and build reproducibility

Independently retrieve and inspect ALL fixed r8 pages p-01.png through p-22.png at readable individual-image scale, record page image SHA/blob and actual observations in a 22-row visual matrix. If ability permits, independently render 22 images directly from immutable r8 PDF and compare text/layout with committed page PNGs; distinguish any unverified image→PDF provenance. Prior r7 image audit is NOT a substitute.

Check P1–P8 normal two-column reading order; 20 full-width tables / 80 rows / 307 cells, all source qualifiers, all 3 diagrams, 5 verbatims including lengthy Decisions JSON, Kimi future release, FLUX uncertainty, 5 recap paras, no p20 old production note, 36 bibliography keys and URLs, correct TOC pages. Catch clipping, overflow, unexpectedly empty pages, bad line breaks, mixed column/caption/footnote reading order. Printed paper may remain 22 pages; do not impose that page count.

**Actual build warning:** committed main-tex-log.txt records TWO Overfull \vbox (2.61676pt too high) while output routine is active; worker reports no visible clipping around p14–15. Independent auditor must inspect those page boundaries, determine whether real text/image clipping exists and distinguish minor non-blocking warning vs actual P1 print defect. Do not claim "0 overfull" by copying older r7 QA.

Read both compiler stdout transcripts and saved full log; if rebuilding using separate isolated environment, report exact TeXLive packages, two pass return codes, page count and log differences. Do not demand identical PDF bytes from a nondeterministic PDF producer unless deterministic settings are proven; visual and semantic reproducibility may suffice.

Independently inspect PDF annotations / font embeddings / page boxes via PDF parser where available: official Decisions guide and percent-encoded scoped npm %2F URL, no CJK-punctuation URI contamination, CJK font subsets embedded, no corrupted internal links. 75 annotations are worker claim until independently parsed.

## 6. Evidence governance and no premature publication

Retain prior 31 Architecture requirement grades as versioned and non-equivalent: r3.2 independent 20 SUBSTANTIVE/11 PARTIAL vs later r2 diagnostic row arithmetic 18/13, 14 different IDs. Neither is current r8 31-row Human authority; do not rewrite architecture-v2.json or invent grade promotions.

Bibliography 36 keys, worker tier map 19 exact-visible, 1 machine-only, 13 natural, 2 further, 1 unavailable/404, 0 orphan. 13+2 remain CURATED_REVIEW_REQUIRED. The tier map and URLs do not prove source-original raw or all benchmark/law/license assertions. No promotion without evidence.

PDF is NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF only. Keep ARCHITECTURE_ESTABLISHED, Core-native Draft BLOCKED, Human PDF Preview Gate PENDING. No release, Freeze, PR or merge and no independent auditor mutation of repository/GitHub.

## 7. Deliverable and independent terminal

External final report in Japanese Markdown, saved and read back to Google Drive GPT-Sol_Review/yyyyMMddHHmmss_SolReview.md. Include exact fixed audit pins, actual raw hashes/logs, 22-page full audit matrix, P1 closure A/B/C, independent clean/negative and novel mutant results or honest NOT_RERUN, metadata typo and test-class taxonomy observations, overfull vbox ruling, PDF link/font verification status, P0/P1/P2 findings, limitations and Human items.

Explicit ONE terminal with evidence:
INDEPENDENT_W43_R8_PDF_PASS (all new full visual + semantic verified, P0=P1=0, P2 limits explicit);
INDEPENDENT_W43_R8_SEMANTIC_PASS_VISUAL_BLOCKED;
INDEPENDENT_W43_R8_REQUEST_CHANGES;
INDEPENDENT_W43_R8_INCONCLUSIVE.

Never write audit PASS into repository. Return exact Drive report URL. Editorial Sol alone adjudicates outcome; Human approval remains separate.
