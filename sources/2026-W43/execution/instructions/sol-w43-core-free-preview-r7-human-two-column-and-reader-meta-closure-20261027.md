# J-GAS W43 — Editorial Sol r7 execution contract: restore Weekly two-column layout, remove reader-visible production metadata

Date: 2026-10-27 JST.
Authority: editorial Sol's adjudication of independent r6 audit, with Human Comments as binding reader-facing requirements.
Status: `INDEPENDENT_R6_REQUEST_CHANGES_ACCEPTED / P1_LAYOUT_AND_META_BOUNDED_REPAIR / R7_NONCANONICAL_PDF_ONLY / HUMAN_GATE_PENDING`.
Repo: `eariver/japanese-generative-ai-survey`.
Branch: existing ONLY `weekly/2026-W43-v2-work`.
Execution: Muse Worker. No independent audit or Human Gate decision may be forged.

## 0. Six-way exact, fail-closed start guard

A Sol-created commit containing **only this contract** advances W43 after the pair below. The **post-contract HEAD/Tree in the accompanying Sol dispatch** is the exact Muse execution start. The old W43 pair below is the contract parent, **NOT** a fallback execution start. Check remote HEAD and root Tree read-only for all three refs before ANY write; verify dispatch HEAD parent/Tree and that the Sol commit added precisely this one contract.

| Ref | Expected HEAD | Expected Root Tree |
|---|---|---|
| W43 **pre-contract parent** | `08507893367762455a1ced8ceee2c35b42a6d8d6` | `081d84110a10a2f8d8c26c790c13e9ef1c22c94b` |
| main | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| production/survey-core-v2 (Frozen) | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

Any mismatch: ZERO WRITES, report actual+expected exact HEAD/Tree, halt. Local clean checkout may fetch+FF-only, never reset/rebase/force. No new/fallback/review/repair branch, no PR, no merge, no Core/shared files, no normal main changes. Final normal non-force FF push only after re-verifying exact remote starting HEAD and guards; remote readback HEAD, root Tree, parent and all changed paths.

## 1. Authority and accepted independent audit

Authoritative new r6 independent Sol report saved by auditor on Drive:
`https://drive.google.com/file/d/1TJwC41xoEteT3ZiS9AZ2iYJHWLFOkJo-/view?usp=drivesdk`.
The report terminal `INDEPENDENT_W43_R6_REQUEST_CHANGES`, P0=0, P1=2, P2=4. Read full report if connected; if inaccessible, apply its key findings explicitly transcribed here. Never claim to have read inaccessible content.

**Accepted blocking Human Comments:**
- `W43-R6-AUD-01` P1: r6 normal pages are essentially **single-column**, unlike established Weekly **segmented two-column** layout.
- `W43-R6-AUD-02` P1: reader-visible **production/completion/review/meta** strings leak into title, bibliography introduction, figure/caption labels, etc. Separate internal editorial status from scientific evidence and publisher safety warning. Human wanted no process-meta in magazine prose.

**Nonblocking/P2 governance and technical qualification:**
- `AUD-03`: r6 source→projection→TeX checker saved 36/36 and 38/38, but the independent Sol could not execute the Python checker in its environment; status `CHECKER_REPLAY_NOT_RERUN`. r7 must maintain a portable test entrypoint; worker PASS does not become independent PASS.
- `AUD-04`: two wrong historical r3 HEAD/Tree strings in r6 build-manifest + Muse's *proposed* audit request. Never mutate immutable r6; create a **corrective r7 provenance supersession** with correct immutable r3 refs and explain r6's erroneous records.
- `AUD-05`: r2 diagnosis has 31 row entries 18 SUBSTANTIVE/13 PARTIAL but prose totals 20/11, while the actual earlier independent r3.2 report evaluates **20/11** for **the then-current r3.2** and gives different PARTIAL IDs. Differences in 14 ID categories, 8 one direction/6 reverse; DO NOT identify merely two promotions or transplant old grade to newer edition. r3.2 was before fixes of MemT storage-only, Patch stage 4/5, and others. Use **versioned grading**. Do not change approved Architecture or official Human Gate.
- `AUD-06`: bibliography 36 refs, category 19 exact-visible / 1 machine-only / 13 natural / 2 further / 1 unavailable / 0 orphan. The 13+2 are `CURATED_REVIEW_REQUIRED`; missing original raw, 404, post-cutoff, vendor benchmarks and GH/npm clocks not independently proven. No automatic source confidence upgrades or unjustified deletion.
- Independently verified r6 PDF 482659 bytes SHA256 `113b179a4fab82df28a5d9f1ac1ac6c588ce2a0a253b988ba590944057f76320`, 22 pages and **22/22 r6 images visually inspected**. Source r3→r6 TeX equals exactly one deletion of old p20 note. P20 recap note now gone, five paragraphs intact. No omitted chapters or major broken tables reported. Previous r3→r6 and r5 content fidelity gains preserved.
- Human approval remains PENDING; Core native Draft BLOCKED. The PDF stays `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`. It is NOT an official publication candidate.

**Exact r6 source pin**: HEAD `d8e21b8fe6513ff0592604292bdec034d2c3eeea`; Tree `9ec7dd73d4acc50be48672fd3970af0e2b30925d`. Fixed r6 TeX SHA256 `7c052f05227228332fecec469b3b90e1b8952d4c3ab44ea65f180cecd4dd662b`; fixed r6 PDF as above. Correct historical r3 HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`, correct r3 root Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`; old r3 PDF SHA256 `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`. Never use wrong r6 manifest historical r3 refs `3cdf2a01b810a972ecddfaa41c3dccded55c75f9` / `17b0525fec79d5624a227f82bf7dccded55c75f9`.

## 2. Preflight: compare a **real released Weekly** reference, no improvised style

Mandatory read-only reference at reviewed main SHA above:
- `surveys/weekly/2026-W42/main.tex` and `surveys/weekly/2026-W42/preview.sty`.
- W42 normal story uses `\\begin{multicols}{2}` / `\\end{multicols}` **segmented around wide tables**, full-width tables outside multicols, then resumes columns; 7mm gutter. W42's bibliography ALSO uses segmented two-column `multicols` in its finished issue.
- W43 r6 `core-free-preview-r6/preview.sty` already loads multicol and sets `\\columnsep=7mm` yet **W43 r6 main.tex contains no `\\begin{multicols}{2}`**, explaining the single-column regression. W43's r6 style alone is not sufficient; install actual environments in **new r7 TeX**.
- Inspect how W42 handles full-width `tabularx`, `\\captionof`, long code, full-width special material, page flow, headings and bibliography. Adapt to W43's 20 tables + 3 figures + 5 verbatim blocks + 36 bibliography items without cutting content or treating a two-column environment as universal. Prefer W42's actual proven mixed-width geometry, not a full-text `multicols` blanket. Keep A4/10pt/18mm page margins unless a reasoned, explicitly bounded need arises.
- Human demanded **visibly two-column normal explanatory prose**, NOT merely a loaded package or fake line draw. Keep normal prose/section subsections in two columns, full-width wide tables/code/diagrams separated safely without disrupting reading order or note proximity. Allow a single column for cover, TOC, exceptional full-width material; quantify share of narrative pages/blocks in 2-col vs exceptions. Visual audit at 100% print scale and/or >=150dpi for legibility.
- No minimum page count: prior 22/38 gap was estimate, not mandated number. Repagination is expected when correct layout returns. Avoid underfilled body pages or awkward forced breaks; no padding, no text expansion invented from missing source.

## 3. Phase A: reader-facing meta inventory and exact authorized replacements

First create a complete visible-surface **meta scan inventory** of r6 TeX/cover/bib/captions/figure titles/notes using actual TeX parsing and independent PDF text readback, not keyword count alone. Audit all pages, not only known p03/p21:
- `\\section*{週刊生成AI技術調査 2026-W43 --- 印刷用原稿 r3}`: remove internal `印刷用原稿 r3`; use normal reader issue heading or suppress redundant interior title if cover already says it, while preserving section/text and TOC semantics.
- `\\surveyeditiondescriptor{週刊Technical Survey（編集プレビュー・未承認）}` and cover `2026-W43 Weekly --- 読者確認用プレビュー`: author a **neutral reader edition description** (e.g. `週刊Technical Survey`), while preserving **visually distinct proof status marker** until explicit Human publication approval.
- Bibliography preface: `本プレビューは非正準の編集 proof であり、受理済み Core 証拠の代替ではない。…分離記録した文脈注記の詳細は引用対応表を参照。` → neutral source guide such as `本稿で参照した資料を以下に示す。各資料の確認範囲や未検証事項は本文・注記に明記した。`. Preserve specific bibliography tier information, never pretend every source archived.
- Remove, neutralize or relocate reader-visible operator IDs `p1-f1`, `p2-f2`, `p3-f1`, `p5-f1`, `p6-f1`, `p7-f1`, `p8-f1/f2/f3`, `§5.1–5.2実物` etc from figure box titles, captions and code-example headings. Preserve actual feature/model/units, figure and table semantics and `\\label` machine traceability in TeX / separate map. Use reader labels such as `表：様式別の評価値と料金（発行元公表。比較条件・単位に未確認事項あり）`, not unqualified raw numeric comparison.
- Reader-visible `P1 ---`, `P2 ---`, … `P8 ---` are operator package IDs in chapter titles, whereas W42 published reader chapter titles have no P1 prefix. Remove visible package prefix while preserving editorial package identity in TeX machine labels (`\\label{sec:P1}`) and external mapping, regenerate TOC; do not delete 8 technical stories.
- Inspect lower-priority metadata outside these known examples: QA/review/approval statuses, `UNVALIDATED` or `NONCANONICAL` **embedded in article**, internal SHA, staging filename, artifact path, session/approval references, standalone `reader` / `projection` / `proof`, print revision. Explicitly differentiate from genuine story terms `APIプレビュー`, `未実行`, `発行元測定`, `原資料未取得`, `確度未検証`, `404証拠不可`, `POST_CUTOFF`, etc; **NEVER** strip legitimate epistemic/cutoff disclosures, license restrictions, benchmarks denominators or vendor/reproduction limits. Keep actual bibliographic source keys where necessary, URL annotations intact.
- Protect against false marketing: `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` cannot be removed from PDF's safety/provenance layer while this is Core-free. Keep an explicit, visually separate **proof-only footer/watermark or cover safety mark + PDF metadata**, not magazine content. Report where it appears. No pretending Human approved.
- This is a bounded reader-surface rewrite, not permission to rewrite technical arguments. Log EVERY changed reader-visible span as `meta-change-ledger-r7.json`: old exact TeX span, new span, line/section/page at r6, class (EDITORIAL_META_REPLACEMENT / OPERATOR_ID_NORMALIZATION / UNCHANGED_SCIENTIFIC_QUALIFIER / PROOF_STATUS_RELOCATED), justification and protected scientific facets. Explicit whitelist of metadata replacements; all other prose, 29 claims and values unchanged. If a candidate expression also bears source provenance or measurement condition and cannot be safely changed, mark it `NOT_AUTOMATICALLY_EDITABLE` and solicit Sol's judgment instead of guessing.
- Only phase-A staged edits/candidate work in r7 namespace; no immutable r6 edit.

## 4. Phase B: rebuild genuine segmented 2-column r7 PDF (only after A inventory checked)

Create new `sources/2026-W43/execution/core-free-preview-r7/` with:
- `main.tex`, `preview.sty`, projection/reader bridge if needed, and supporting edition-local layout macros.
- TeX normally two-column for P1–P8 and five-paragraph recap. Full-width 20 tables/large code/figure may break into explicitly segmented columns as W42; avoid floating tables disappearing or moving sources away. Source/captions relative order must be retained, no figure body or actual table cell dropped. Do not force 22 pages.
- Bibliography laid out to match W42's normal readable two-column baseline if actually legible; avoid broken URLs and clickable annotation loss. No clipping/hanging label misalignment. If W42 reference proves a particular method unstable for this content, document the exception and real page-level reasoning.
- Build with versioned `lualatex` commands, exit 0, preserve `main.log`, print preview style, new PDF **raw SHA256**, blob, size, actual A4 page count. Render **every** page to PNGs >=150dpi, contact sheets, do full-page visual QA. Save **per-page image hash** and page matrix. Check all text columns clearly visible and flow-order correct; no blank body pages from repeated multicols/float breaks; check p-IDs using new positions rather than old hard-coded p18/p21 page numbers.
- Independently parse actual PDF link annotations, text extraction, fonts and page boxes where supported: official Decisions URL exact (no Japanese parenthetical), `POST /v1/decisions`, GitHub 15:18:14Z vs npm 15:21:49.491Z separate, percent-encoded npm scoped registry link, 36 references/click URLs, subset CJK fonts embedded. Do not call success from TeX literal presence only.
- Demonstrate **both** two-column on most normal story pages and full-width safety on high-density panels (MemT rights, Voxtral measurement/price rows, COBOL/low-resource table, TanStack/DeepSeek, code JSON). Worker outputs should include illustrative actual new page ids at >=150dpi to make independent review straightforward. No auto-infer that visual quality passes because there are no TeX overfull warnings.

## 5. Phase C: exact semantic provenance + independent replay bridge

- Old r3.5 Reader / Ledger / Manifest, r3 projection, fixed r6 TeX/PDF all immutable. Run prior r6 full semantic checker 36/36 + negative 38/38 **on fixed r6** for historical baseline where possible, and add a **new r7 printed-reader validator** accepting `--repo-root` or staged input files. It must map r3.5 original→r6 fixed→r7 normalized visible prose/figures/5 code blocks/20 tables/80 rows/**307 physical nonempty cells**/29 claims/5 recap paragraphs/36 bibliography keys with only Phase-A meta whitelist. For r7 segmented multicols, parse real structural content, not a bag of words; minted TeX layout commands are ignored only when proven zero effect on visible content. Parenthetical legal/provenance caveats remain in correct rows and paragraphs.
- Negatives using the SAME validator against changed inputs: delete one scientific qualifier while retaining metadata normalizations, swap GH/npm clock, mutate a COBOL or MemT table number, remove a paragraph in a multicol segment, change a figure edge, mutate a code token, reorder two panels or table rows, drop one bibliography citation, re-insert a reviewer/process sentence inside article, change only a proof footer status label. Verify expected error cause; no tautology or stale-hash/pass-by-presence.
- Define `READER_META_LEAK`, `LAYOUT_NOT_TWO_COLUMN`, `ROW_CELL_CLAIM_LOSS`, `SCIENTIFIC_QUALIFIER_LOSS`, `DOC_PROOF_STATUS_MISSING` as distinct fail codes. Link the tests to their expected page(s) / print PDF text layer and the whitelist manifest. If confident full coverage cannot be achieved, report bounded PARTIAL and exact unproven spans rather than full PASS.
- For independent replay of Python 36/38, don't make it another Muse-only assurance: package the exact checkout-free, read-only staged-file replay layout `--staged-dir` and input hashes and a single shell command. The independent auditor will need to execute it; do not claim independent verification at this stage.
- Correct **new** r7 provenance records to cite r3 HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9` and r3 Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`. Add `historical-pin-correction-r7.md` explaining why immutable r6 manifest and worker proposed audit contained wrong r3 strings and that r6 subject was NOT revised. Audit the complete SHA fields of r7 manifest before commit.
- Architecture 31: preserve approved `architecture-v2.json`. In a new r7 sidecar document compare **r3.2 external independent report 20/11** (then-current version, 11 PARTIAL IDs `§1.4, §2.2, §2.4, §3.2, §4.1, §5.1, §5.2, §6.1, §7.2, §8.2, §8.3`) against **r2 later diagnostic row arithmetic 18/13** (13 PARTIAL `§1.4, §2.6, §3.3, §4.1, §4.3, §5.1, §5.2, §5.3, §5.4, §6.2, §7.1, §7.3, §8.3`), exactly **14 shifted ID classifications**. These refer to different manuscript stages! Label respective evaluation dates and evidence, and **do not claim either is authoritative for new r7**. Produce current r7 31-row *coverage and evidence-limitation mapping* with exact chapter/printed-page, without autonomous promotion to canonical approved scoring. Present Sol editorial ruling questions separately, no Human Gate progression.
- Reference-tier curation: 36 total, 13 natural + 2 further retained `CURATED_REVIEW_REQUIRED`; no claiming archived raw from visible wording. Distinguish completeness of bibliography from source truth.

## 6. Allowed files, exit and publication guard

Write ONLY **new files** under `sources/2026-W43/execution/core-free-preview-r7/`, plus
`sources/2026-W43/execution/SOL_W43_CORE_FREE_PREVIEW_R7_HANDOFF.md`, one new versioned `sources/2026-W43/execution/sessions/muse-w43-core-free-preview-r7-20261027.md`, and append-only `sources/2026-W43/execution/index.md`.

Expected namespace contents: `meta-scan-r7.md`, `meta-change-ledger-r7.json`, `layout-design-vs-W42-r7.md`, `main.tex`, `preview.sty`, `main.pdf`, `main.log`, `pages/` PNGs/contact sheets, `new-physical-page-qa-r7.md`, `pdf-link-font-qa-r7.md`, `r7-reader-surface-semantic-join.py`, `r7-semantic-clean.json`, `r7-semantic-negatives.json`, `portable-independent-replay-r7.md`, `historical-pin-correction-r7.md`, `architecture-31-versioned-reconciliation-r7.md`, `reference-tier-status-r7.md`, `build-manifest-r7.json`, `independent-sol-r7-layout-and-meta-reaudit-request.PROPOSED.md`.
If length/time/tooling prevents Phase B/C honest complete execution, save only truthful partial artifacts under allowed paths with blockers; never simulate success.

**Immutable**: r1–r6 actual files, r3.5 source reader/ledger/manifest, original r3/r5/r6 checker outputs, approved Architecture/Selection/Evidence/State/Human Gate, main, Frozen Core v2. No changes to `surveys/weekly/2026-W43/main.pdf` (canonical path) or Core code/config/Stage. No publication approval, Freeze/Release/merge.

Terminal:
- `MUSE_W43_R7_TWO_COLUMN_READER_META_PDF_READY_FOR_INDEPENDENT_REAUDIT` only if real new PDF + 2-col visual and meta scan + fidelity + runbook all proven in worker scope.
- `MUSE_W43_R7_LAYOUT_OR_META_BLOCKED` if layout/reader-facing meta still defective; state exact pages/paragraphs, no false PASS.
- `MUSE_W43_R7_SEMANTIC_PROVENANCE_BLOCKED` if any scientific qualifier/citation/row, section/reading order cannot be preserved/verified; no PDF approval.

Report post-start exact HEAD/Root Tree, six-way guard, final FF commit+Tree, full changed path whitelist, actual new TeX/PDF hashes/page count, 22/?? pages all checked, reader-visible diffs and retained scientific qualifiers, reference tier limits, Architecture versioned grade issue, immutable r6 hashes and a PROPOSED independent read-only review subject. Independent Sol will **not** copy r6's image result; it must newly inspect every r7 page and independent re-run semantically possible tests before Human PDF Gate.
