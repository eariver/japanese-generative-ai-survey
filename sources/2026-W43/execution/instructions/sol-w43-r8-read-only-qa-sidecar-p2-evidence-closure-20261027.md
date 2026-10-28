# J-GAS W43 r8 — Editorial Sol bounded P2 QA sidecar closure (NO new PDF)

Date: 2026-10-27 JST
Status: EDITORIAL_SOL_ACCEPTED_R8_INCONCLUSIVE / P0_0_P1_0_P2_3 / QA_SIDECAR_ONLY / HUMAN_GATE_PENDING
Repository: eariver/japanese-generative-ai-survey
Execution role: Muse Worker, existing branch weekly/2026-W43-v2-work ONLY.
Audit authority: separate independent Sol session remains read-only; Muse does not self-certify independent audit.

## 0. Fail-closed Git guard before ALL writes

The Sol dispatch carries the POST-CONTRACT current W43 HEAD/Root Tree; that is the ONLY authorized execution start. Below is the PRE-CONTRACT PARENT, not an alternative starting head.

PRE-CONTRACT W43: HEAD 5bfc1483ccf5e56a4d4b6fb15c34a240aab3445f / Root Tree c8ef1a4add5eebb7e21634d4f73095a3aff4ec2d.
Reviewed main: HEAD 041a08dfef3112643cbf85b4a86a7b6f9128aed6 / Root Tree a134dc36a407d08ab1de416324229b3955e0325a.
Frozen production/survey-core-v2: HEAD 774dd39a951c9ac3818e83dfffd4c7666efb0a20 / Root Tree cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481.

Read-only check three remote HEAD/Tree pairs; verify new post-contract W43 HEAD has single parent PRE-CONTRACT and the Sol addition is THIS CONTRACT ONLY. On any mismatch ZERO WRITES, report expected vs actual and STOP. Use existing branch only, FF-only local sync, normal non-force commit+push, no new/fallback branch, reset/rebase/force, no merge, no PR/Issue. Reverify remote before push and read back postpush HEAD/Tree/full changed paths.

## 1. Independent r8 outcome to adjudicate, and fixed subject

External report: 20261027095107_SolReview.md (user supplied, read in editorial Sol session).
Independent terminal INDEPENDENT_W43_R8_INCONCLUSIVE, P0=0/P1=0/P2=3.

Immutable r8 subject: HEAD 953a9d331972fdae237da4bd0f1019b17168a118; Root Tree dfafff50c946e3d0abc051eb419797de283b192a.
Fixed r8 PDF sources/2026-W43/execution/core-free-preview-r8/main.pdf, SHA256 abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72, 487351 bytes, 22 A4 pages.
Fixed r8 TeX SHA256 4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d.
Fixed r8 log SHA256 2242237a2533507e5cc28f27794c6eed23d9d58c2cc97b3a0ec79d21eafeb424.
All 3 A/B/C reader-visible approval-meta fixes independently supported; 22 committed PNGs individually viewed by auditor; actual PDF and files raw hashes checked. No newly discovered P1 in inspected material. Two Overfull vbox 2.61676pt warnings were examined at p14/p15 in PNGs and not elevated to a printing P1.

**Do not rebuild/revise r8 PDF, r8 TeX, style, old build-log, checker or any r1-r8 artifact. Do not generate r9 PDF.** Current issue is QA provenance and independent execution logistics, not new article wording.

## 2. Three P2 closures — all edition-local ADDITIVE sidecars

P2-01: malformed historical Tree in fixed r8 build-manifest-r8.json:
- INCORRECT pre_contract_tree = 2429f675db817cc38333182734ed6338e1abc68 (39 hex chars)
- ACTUAL pre-contract W43 HEAD = be17e9944818442181975fa66b51912d2e7db8d8
- CORRECT corresponding Tree = 2429f675db817cc38333182734ed6338f1eabc68 (40 hex chars).
Verify actual old HEAD->Tree through GitHub Git commit API, not from this text alone. Add a new append-only provenance supersession r8-p2-historical-tree-supersession.md identifying BAD field and corrected HEAD/Tree with evidence links, immutable original manifest path/SHA, and precise scope. Do not silently change fixed manifest or claim fixed r8 was modified. The r8 fixed HEAD/Root Tree/PDF remain valid.

P2-02: r8 validator negative taxonomy for unknown editorial operator sentence:
- Fixed r8 r8-exact-fidelity-check.py stored negative N-operator-insert expected [READER_META_LEAK, PROSE_FIDELITY_LOSS] but observed only [PROSE_FIDELITY_LOSS]. Old evaluator uses any(e in causes for e in expect), so PASS covers only ONE expected class, not both. The full exact source-diff layer already rejects the mutant; this is a CATEGORY/test-assertion defect, not a bypass of strict prose fidelity.
- Build a separate QA-sidecar wrapper or isolated copy of checker, with explicit all-required-causes assertion and an expanded controlled process-meta taxonomy including unknown insertion 編集承認ゲート通過済み, without altering original fixed r8 checker or actual scientific prose.
- Execute original N-operator-insert as baseline and report actual old causes [] or [PROSE_FIDELITY_LOSS], NOT guess. In new strict wrapper, ensure same single mutation elicits **both** READER_META_LEAK and PROSE_FIDELITY_LOSS and both are REQUIRED, not optional. Also run one clean input, N10 ordinary prose inversion and N13 newly introduced Ming vendor quote→independent measurement reversal as separate scientific negatives with distinct material delta and actual exit codes. N13: fixed r8 P5 ordinary prose phrase 発行元引用として扱う → 独立測定結果として扱う, only if exact phrase is present once; check occurrence count.
- Never pass a negative that is a no-op, a malformed tokenization, a missing test file, or merely a stale expected hash. Required causes must be actual. Record actual JSON and stdout/stderr/exit codes, independent input hashes, source/original pair and mutated temporary copy hashes. This remains MUSE execution evidence, NOT independent Sol PASS.
- Build an **independently replayable, read-only** packet for a separate runner: lock original immutable SHA, SHA256 for original r7/r8 TeX, r8 script / wrapper and Python version, dependencies (prefer Python standard library), exact command lines for checkout or staged-dir, and expected outputs. No write to old artifact namespaces. Where reviewer cannot run Python, label NOT_RERUN, not a fake successful replay.

P2-03: r8 PDF page QA notes have false physical page locations.
- Fixed old pdf-page-qa-r8.md says recap begins p19 and bib p20, and mentions table11 header p12, Table13/16 p14. Independent auditor visually observed: p19 has TanStack/DeepSeek + table18 (no recap heading), p20 bottom starts 今週の総括, p21 mid-page first 出典一覧/参考文献; table11 starts p13; table16 exists p17; table13 p14.
- Re-inspect immutable **actual PDF bytes** using PyMuPDF page text/layout and (if feasible) independently render each page; crosscheck committed r8 pages images. Derive actual p01–p22 matrix and section/table/recap/bib anchors, using both machine-extracted text and page images. For each old wrong page claim record exact old wording, corrected page, evidence from actual PDF extraction+image hash and confidence. Store r8-p2-physical-page-qa-supersession.md plus machine-readable page anchors JSON. Do not edit original page-qa-r8.md, PNGs or fixed PDF. If PDF byte acquisition is not possible, distinguish image-only findings explicitly and do not assert full PDF-to-image identity.

## 3. Critical remaining blocker is independently executed verification, NOT another design revision

The r8 external auditor's INCONCLUSIVE was primarily due to tool-path inability to:
- execute the ACTUAL Python r8 checker clean 27/27 and negatives 12/12 or new N13 with exit codes;
- independently rerender fixed r8 PDF from its real bytes and compare page images;
- parse actual PDF URI annotations, A4 boxes, font embeddings/ToUnicode;
- independently rebuild LuaLaTeX. The auditor DID authenticate r8 PDF/source/log raw hashes and viewed 22 repository PNG files individually. Do not conflate those two evidence levels.
- Since the tool limits cannot be solved by another Muse PASS alone, prepare a clear capability-aware runbook designed for an independent environment with direct Git checkout/filesystem and Python3 + PyMuPDF/pdfinfo or other PDF parser, and optionally LuaLaTeX. Explicitly state GitHub connector-only audit is insufficient for the prescribed independent execution tasks.
- Include all explicit independent commands and expected pins in a new r8-independent-verification-runbook.md. Use temporary checkout and Python script code, no GitHub writes. External observer may use a separate environment/Work session, but do not represent mere instructions or Muse's local outputs as independent replay. If independent environment is inaccessible, external terminal legitimately remains INCONCLUSIVE, and Human PDF Gate remains PENDING.
- Independent build is useful, but do not require deterministic PDF SHA from a new build unless deterministic environment proven. The mandatory focus is actual fixed PDF parsing/rendering, exact r8 checker Python execution, taxonomy proof, page matrix corroboration. Preserve uncertainty on full source truth, 31 architecture grading and 15 curated bibliography sources.
- An independent auditor must stay READ-ONLY and produce final report to Google Drive GPT-Sol_Review as yyyyMMddHHmmss_SolReview.md; no audit report in GitHub and no self-approved terminal.

## 4. Allowed paths and stop conditions

Write ONLY newly ADDED files under:
sources/2026-W43/execution/r8-p2-qa-closure/
plus ONE new handoff:
sources/2026-W43/execution/SOL_W43_R8_P2_QA_CLOSURE_HANDOFF.md
plus ONE new session log:
sources/2026-W43/execution/sessions/muse-w43-r8-p2-qa-closure-20261027.md
and append-only sources/2026-W43/execution/index.md.
Do not edit pre-existing r1–r8 files, including r8 validator, PDF, TeX, manifest, page QA, code, historical corrections; no edits to approved Architecture/Selection/Evidence/State/Human Gate, Frozen Core v2 or main. Keep 36 bibliography keys, 15 CURATED_REVIEW_REQUIRED unupgraded, grading versioned r3.2 20/11 vs later r2 18/13 with 14 ID changes.

Normal terminal:
MUSE_W43_R8_P2_QA_SIDECAR_READY_FOR_INDEPENDENT_EXECUTION
only if historical pin corrected via additive provenance, exact negative taxonomy tested, physical page positions clarified with real evidence, and executable independent runbook + actual Muse outputs are committed.
If failure, choose MUSE_W43_R8_P2_QA_SIDECAR_BLOCKED and identify exact blocker. No Human approval, no new PDF, no release/freeze. Report starting exact checks, final remote HEAD/Tree/parent, changed file whitelist, actual r8 PDF SHA unchanged and sidecar test cause results. External separate Sol independent check still required.
