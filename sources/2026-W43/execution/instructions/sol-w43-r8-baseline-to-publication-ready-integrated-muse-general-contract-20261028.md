# J-GAS 2026-W43 — r8-approved proof to exact-PDF Publication Ready
## Integrated Muse execution + independent General CoWorker regression review

Date: 2026-10-28 JST
Contract status: PREPARED_BY_EDITORIAL_SOL / AWAITING_EXPLICIT_DISPATCH_TO_MUSE
Execution authorization upon later dispatch: W43_WRITE_ENABLED / HUMAN_FINAL_PUBLICATION_PREVIEW_GATE_IS_THE_STOP
Repository: eariver/japanese-generative-ai-survey
EXISTING branch only: weekly/2026-W43-v2-work
Executor: Muse worker; independent QA CoWorker: a SEPARATE Muse instance named "General".
No ChatGPT Work or further independent GPT audit required.

### 0. Overall result and non-negotiable stop

Deliver as much of the **lawful** W43 weekly pipeline as possible in ONE continuous worker job:
  approved Architecture -> W43-only temporary historical-basis compatibility
  -> actual Core-native P1–P8 Draft Packages/Results and Profile Synthesis
  -> DRAFT_COMPLETE trusted stage transition
  -> exact Reader Manuscript, canonical TeX/PDF and deterministic/semantic/visual quality records
  -> VALIDATED_DRAFT trusted transition
  -> exact publication candidate READY_FOR_PUBLICATION_PREVIEW
  -> RELEASE_CANDIDATE trusted transition
  -> General independent regression/visual review, corrections/rebuild/recheck as needed
  -> FINAL HANDOFF: READY_FOR_HUMAN_PUBLICATION_PREVIEW with immutable commit PDF URL, SHA256, bytes, pages, exact Candidate, release procedure.

**At this stop, DO NOT record Publication Preview approval, Freeze, merge, tag, or publish.** The next Human Owner decision is the FINAL GO/REQUEST_CHANGES on the displayed exact release PDF. Prior Human approval of the noncanonical r8 proof does NOT count as the canonical exact-byte Publication Preview approval. After Human GO, create a SEPARATE permission-bound release execution using the canonical preview-approval, Freeze, merge, GitHub release workflow. Do not require an extra routine Human Freeze/Release approval after the exact-PDF GO when normal policy supports deterministic continuation.

This is NOT a mere Draft handoff. Do not stop at Draft/Validation/QA boundaries unless a REAL non-recoverable validation, authority, data or tool failure occurs. Do not interrupt the Human for routine layout/editorial/CI decisions or for a new independent GPT audit. General's findings should be addressed within the same work unit.

The user's present direction: 「先ほどReviewしたPDFから問題が回帰しなければそれをPublishして構わない… Review済みPDFと同等の品質が再現できたPDFを生成して、あとは私が確認してGOを出せばPublishできる状態… MuseはCoWorkerとして独立したMuseを使うことができます。（Generalという名前で扱うことができます）」.
This means optimize for a genuinely completed, byte-pinned release-ready PDF and one final Human GO, never fabricate an already-issued GO.

### 1. Exact repository guard and write authorization

Pre-contract W43 branch expected HEAD:
fd1833c79d82dfc078bff330e782d1ba2c1af14f
Pre-contract Root Tree:
85d82582273815293ff6b1fa59d6773c5cfae2a7
The editorial Sol will supply the exact post-contract branch HEAD/Root Tree at dispatch. Before any writes:
- Verify remote existing W43 branch HEAD and Root Tree match supplied exact post-contract pins.
- Verify post-contract HEAD has exactly the one-file contract addition from above pre-contract parent.
- Verify main HEAD/Tree = 041a08dfef3112643cbf85b4a86a7b6f9128aed6 / a134dc36a407d08ab1de416324229b3955e0325a.
- Verify protected production/survey-core-v2 HEAD/Tree = 774dd39a951c9ac3818e83dfffd4c7666efb0a20 / cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481.
- Verify approved Architecture, Human Architecture approval, current W43 State, Screening, Evidence, Selection and reference PDF fixed hash. On mismatch, STOP with actual/expected; no push or “best effort” substitution.

**Read-only applies to guards and to protected data, NOT this worker's outputs.** \`git fetch origin\` and verified \`git merge --ff-only origin/weekly/2026-W43-v2-work\` (or \`git pull --ff-only\`) are explicitly authorized when local checkout is clean and ancestor of the exact remote HEAD. Worker may write under the W43 edition output paths specified in §8, stage request-only and execution-record commits, and must \`git add\`, normal commit, non-force push on the existing branch, remote read-back and exact SHA/Tree reporting. Never create a fallback/review/repair branch, reset/rebase/force push/merge commits on W43. Do not commit secrets, caches, untrusted temp credentials, virtual environments or huge diagnostic scratch.

Existing fixed r8 subject:
HEAD 953a9d331972fdae237da4bd0f1019b17168a118; Root Tree dfafff50c946e3d0abc051eb419797de283b192a.
Reference PDF \`sources/2026-W43/execution/core-free-preview-r8/main.pdf\`
SHA256 abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72, 487351B, 22 A4 pages.
Reference r8 TeX SHA256 4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d.
Reference P2 sidecar HEAD de5e41c253de37015fdb828503040f818698c6bc / Tree 5da261bfc4c1791f912033937ea1bf909f39ffc1.
Independent GPT PASS report 20261028001028_SolReview.md; terminal INDEPENDENT_W43_R8_P2_SIDECAR_AND_PDF_PASS, P0=0 P1=0 and accepted bounded P2=4.
Human r8 content/layout pre-review APPROVED record:
\`sources/2026-W43/execution/governance/human-w43-r8-corefree-proof-content-layout-approved-20261028.md\`
Previous runtime-only quick-recovery contract (superseded as its narrow stopping point ONLY):
\`sources/2026-W43/execution/instructions/sol-w43-runtime-only-draft-basis-compat-fast-recovery-20261028.md\`.
Existing completion target is broader, so the earlier "stop after Draft" instruction is superseded; its Core-protection and minimal verification rules remain.

### 2. Execution plan — protect baseline, don't restart research

Read the approved W43 r6 Architecture, accepted Selection/Evidence/Screening, prior r8 QA/fidelity/P2 supersessions and W42 native release-run patterns. Do NOT restart Discovery, Screening, Evidence, Selection, Architecture, source intake/Grok or invent later-week facts merely because the normal pipeline has been blocked. Treat the accepted r8 PDF as the editorial baseline.

Current actual W43 State: ARCHITECTURE_ESTABLISHED; architecture_review=approved, publication_preview=pending, exception_gate inactive; Draft/Validation/Preview/Freeze/Release pending.
Blocking known shared frozen-Core mismatch:
\`Screening package basis drift: state_sha256\`.
Original Screening state_sha256 885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596 vs current trusted State SHA b0450d25b9dd4db8424d1c92d713d28c1b268b4e6a3b960a053f9684bb3eebb6. The past delta reflects trusted agent-first Stage advancement. Also old direct-local \`verify_state_basis\`/history/checkpoint naming convention differs from agent-first bridge. This is a known compatibility defect, not permission to rewrite accepted records.

### 3. W43 transient compatibility: small, transparent, not a Core rewrite

Owner expressly allows workaround without comprehensive extra test suite:
「仕様修正ではなく迂回で構いません。そのための慎重なテストも不要です。」

Implement bounded **W43-only, process-local** adapter in \`sources/2026-W43/execution/runtime-compat/\` for the documented historic Screening State equality / old direct-local State history+path admission collision in Draft. Do NOT edit any tracked shared \`scripts/\`, \`schemas/\`, \`config/\`, \`.github/\`, \`tests/\`, AGENTS.md, reviewed main, frozen production Core, existing State/Gates or approved upstream bytes.

Admission (minimum, not another comprehensive campaign):
- Verify W43 issue/Profile, active accepted Screening package/hash and Discovery/profile/prompt/result-contract SHA, current trusted State via actual \`survey_agent_control_v2.validate_agent_state\`, active approved Architecture, and expected diagnosed **historic State SHA vs current State SHA**.
- Bypass ONLY historical State byte sameness and incompatible old direct-local validator convention. Preserve other accepted Screening archived files and accepted effective Discovery chain, accepted Matrix/Selection/Architecture and source SHA checks, Draft and synthesis result/schema checks. No global sha256 monkey-patch, replacement State, catch-all suppressed exceptions or false official PASS.
- Invoke original native interactive Draft package/result/synthesis generation via temporary adapter; use prior 8-package diagnostic input as PROVISIONAL only:
\`sources/2026-W43/execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json\`.
The prior input is shorter/older than r8; don't silently drop approved r8 paragraphs or claim semantic equivalence. It can seed native data if content is reconciled to the approved reference. Source-scope mismatch => fix edition-local input, not silently weaken a reviewer check.
- If a subsequent stage faces SAME historic-vs-agent-first validator mismatch, use a **separately named, hash-bound edition-local transient adapter only for that exact mismatch**, recorded at that transition; do not broaden to bypass a different source/claim/error. Existing first-party operator bridge and actual Stage authority are preferred.
- Do not reopen already approved Human Architecture. Do not use a fake Stage PASS. Where a deterministic canonical Stage validator cannot run truthfully even with narrow compat, stop \`BLOCKED_STAGE_AUTHORITY\` with all genuine completed work committed and an actionable remainder.

Minimal factual verification is mandatory despite waived comprehensive suite: actual SHA/ID and gate pin consistency, genuine native output files, real exit codes/native validation, source/claim sanity, correct Stage and Human provenance, and no P0/P1 content regression.

### 4. Preserve r8 substance, not merely page count

Use r8 as the agreed baseline. Its observed independent audit invariants:
- 8 narrative packages P1–P8 plus substantive final 「今週の総括」 five-paragraph recap AFTER P8, BEFORE reference list;
- 22 A4 pages, two-column main reading flow, 20 numbered tables (80 ordered table rows, 307 parsed cells as appropriate to r8 checker), 3 figures, 5 code items, 36 bibliography keys, 29 anchored claims, main-TeX paragraph anchors 77 where parser supports them, 32 two-column begin/end in proof TeX;
- fixed A/B/C critical caveats: p04 Flint total vs active denominators; p11 FLUX FAQ cannot be asserted as independently reconciled primary original; p22 recap is derived synthesis with no new first-hand claim;
- 75 external URI actions/28 targets, 8 named TOC internal links, embedded Japanese fonts and usable text, URL punctuation/%2F correct;
- strict P2 page correction: Table11 p13, Table16 p17, recap p20, reference head p21 in original PDF. New PDF physical pages MAY shift only when necessary from declared layout changes, with no broken references or missing content. Original P2 corrected positions must NOT be mislabeled as defects if layout legitimately shifts.
- Source honesty: 36 keys with 15 CURATED_REVIEW_REQUIRED, 13 natural+2 further; 404 is not proof, incomplete primary attribution not upgraded, vendor data/benchmarks not independently reproduced, licence and availability caveats unchanged, timestamps/source cutoff preserved. No unexplained unsupported future claims.
- Historical Architecture 31 obligations have qualified coverage 20/11 (not 31/31); the 11 partials may not be secretly dropped or falsely represented as substantive proof.

Treat semantic fidelity, claim qualifiers, tables/cells, links, recap, and legibility as **blocking**. A canonical candidate need NOT share identical PDF bytes with r8 because print metadata/build timestamps change. A plausible 21/22/23-page PDF is NOT a pass by itself; content and page layout are decisive. Never equate page-count equality to quality.

Preferred shortest route: **reuse the already Human-reviewed r8 narrative/TeX arrangement as the source for a faithful canonical publication-layer rendering**, while making an honest provenance/binding to real native Draft/Reader Manuscript and canonical quality records. Preserve renderable copy and use existing edition-local print assets/templates; remove only noncanonical PROOF metadata in the newly generated canonical PDF. If an exact faithful canonical conversion is feasible, prefer it over reauthoring 8 articles from the older, shorter provisional input. Do not relabel the old r8 PDF or copy it into canonical location while leaving untrue provenance; generate and verify new candidate's own bytes.

Before building new Candidate, produce a **reader-to-r8 content mapping** by P1–P8 and recap:
- paragraphs/headings meaningful diff and ordering, structural counts, all 20 table rows/cells and all 29 anchors bound to matching claims, all 3 figures/5 code and 36 bib keys;
- present author caveats, source tier, release/weight licensing and timing;
- normalized TeX delta categories: required canonical metadata/preamble/source/provenance change vs permitted typesetting-only change vs substantive editorial change (substantive changes require explicit qualified rationale and General audit; don't silently change r8's meanings);
- validate new PDF extracted text and real visual pages, not just candidate manifest.

### 5. Native Stages — continue without Human review stops

A. Actual Draft/Synthesis: generate exactly P1–P8 validated native packages/results + profile synthesis, correct 5-paragraph weekly recap as **true final reader payload**, not an orphan sidecar. Native schema binding honest and SHA-pinned. Keep W43 State ARCHITECTURE_ESTABLISHED until genuine Draft output is committed. Build Stage Checkpoint artifacts via trusted operator \`ADVANCE_STAGE\` using the immutable request-only transport pattern already demonstrated by W42; admit ONLY genuine files/reviews and trusted bridge PASS. Verify State actually advances to \`DRAFT_COMPLETE\`, canonical checkpoint/provenance and Human Architecture approved bytes unchanged. A failing Stage must never be represented as advanced.

B. Publication authoring/Validation: from actual Draft basis produce canonical:
\`sources/2026-W43/publication/v2/reader-manuscript-v2.json\`,
\`surveys/weekly/2026-W43/main.tex\`,
\`surveys/weekly/2026-W43/main.pdf\`,
\`sources/2026-W43/publication/v2/quality-regression-bundle-v2.json\`,
\`sources/2026-W43/publication/v2/semantic-editorial-review-v2.json\`,
\`sources/2026-W43/publication/v2/visual-review-v2.json\`,
\`sources/2026-W43/publication/v2/reader-surface-gate-v2.json\`
where correct according to CURRENT schemas/validated W42 precedent. Use current filenames required by Core, not fabricated substitutes. Produce PDF with LuaLaTeX (repeat until references stabilize, no build errors), 22-page baseline-informed layout, all-page PNG plus contact sheets/physical page ledger, font/link extraction, exact SHA. Keep r8 reference untouched.

C. General independent CoWorker: before committing candidate approvals, spawn **separate fresh independent Muse CoWorker "General"** and request an adversarial r8→candidate semantic + visual **regression audit**. General MUST read the actual immutable r8 PDF and current actual candidate TeX/PDF/Reader/QA, independently parse PDF and render all candidate pages (not assume executor's review), and compare to baseline against §4. Record General's own unedited report in edition-local \`execution/audits/general-w43-r8-to-candidate-*.md\`. General is prohibited from authoring/rebuilding Candidate, editing upstream inputs or rubber-stamping worker reports. Ask explicitly for regression verdict \`GENERAL_W43_EQUIVALENCE_PASS\` / \`GENERAL_W43_REQUEST_CHANGES\` / \`GENERAL_W43_INCONCLUSIVE\`, with P0/P1/P2, actual commands/evidence, coverage, independent semantic and reader-facing conclusions. It is a Muse CoWorker independent of executing Muse **within that workflow**, NOT a new independent external GPT audit; describe independence honestly.
  Minimum risk-specific checks: high-signal number+unit+denominator and future/published timing; 20 tables with ordered rows and qualifiers; 3 diagrams, 5 code; Decisions JSON/400 PER REQUEST and HTTP path; Flint, Nemotron licensing, FLUX attribution; 36 references and 15 caveats; exact order P8/recap/bib; all PDF pages legible/URLs/TOC; any inappropriate process meta leakage; source-range/cutoff and false upgrade of partial 11. Reuse existing r8 fidelity/P2 test evidence without demanding another 27+12 exhaustive campaign.
  If General finds P0/P1, worker makes focused EDITION-LOCAL source/TeX/PDF/QA corrections, regenerates dependent exact-byte artifacts, then invokes a NEW General read of changed regions + essential global invariants. Iterate, preserving prior versions. Never use General's PASS for bytes changed afterward: independent PASS must bind final PDF SHA and commit. P2 can be explicitly bounded as nonblocking, but old known 4 P2 are not counted as newly resolved or silently altered. No ungrounded "equivalent" claim.

D. Advance Native Stage via trusted bridge only when true input-based validators can pass:
 \`DRAFT_COMPLETE\` -> \`VALIDATED_DRAFT\` (seven genuine input roles like W42);
 \`VALIDATED_DRAFT\` -> \`RELEASE_CANDIDATE\` (publication-candidate bound to exact PDF).
Use stage APIs/official requests on exact current W43 branch, immutable request-only commits, expected from-state, real artifact paths, actual executor+review provenance, CI evidence. No local manual edit of production-state.json, checkpoint/approval records to fake bridge progression. If candidate changes after a Stage binds old bytes, use only sanctioned published versioned/rewind/revalidation mechanism, or regenerate **before** stage to prevent stale checksum; don't overwrite already bound immutable Stage and pretend State valid. Schedule General audit before final affected Stage crossing where possible, ensuring General PASS binds final Candidate/PDF; after Stage crossing, reconfirm candidate/PDF bytes and General report identity.

E. Final publication candidate:
\`sources/2026-W43/publication/v2/publication-candidate-v2.json\` has status \`READY_FOR_PUBLICATION_PREVIEW\`, real immutable references to Reader Manuscript, TeX, repository-resident PDF, quality bundle, semantic/visual reviews. Profile/manifest/State/Stage gating and exact PDF link validated by the first-party preview-export mechanism if available; use committed SHA-pinned GitHub PDF link if not. Make a preview zip/PNG contact sheets optional if useful to Human, but GitHub exact PDF must be primary. Log that source is not UNVALIDATED proof; never invent formal acceptance if stage not reached.

### 6. No publication before Human GO; prepare the actual future release

**STOP at Human Publication Preview pending** when actual State = \`RELEASE_CANDIDATE\`, canonical PDF/Candidate SHA pins + independent General PASS and no open P0/P1. Terminal:
\`MUSE_W43_EXACT_PDF_READY_FOR_HUMAN_PUBLICATION_PREVIEW_GO\`.
Final report in Japanese must give:
- exact immutable current W43 work HEAD + Root Tree, comparison main/Frozen refs;
- original baseline r8 PDF URL/SHA and new candidate immutable URL/path/SHA/bytes/pages;
- W43 transient adapter name and limited effect + honesty limitations;
- actual Stage records \`DRAFT_COMPLETE\`, \`VALIDATED_DRAFT\`, \`RELEASE_CANDIDATE\` with checkpoint paths/SHAs and real bridge run URLs;
- exact Reader/TeX/PDF/Candidate/bundle/reviews source SHAs;
- full important semantic claim/figure/code/table/bib fidelity and General independent verdict with fixed PDF SHA, P0/P1/P2, unverified source caveats;
- a FINAL GO decision sheet specifying **what exact SHA Human approval will bind**, and the existing reviewed-commit hash containing exact State/Gate input bytes.

Prepare AFTER-GO steps but DO NOT execute:
1. On explicit Human GO for that exact Candidate/PDF, record \`RECORD_PUBLICATION_PREVIEW_APPROVAL\` through first-party operator transport, with durable reviewed-commit pin and actual Human text/date (do not invent timestamps).
2. Under the canonical approved release identity \`weekly/2026-W43\`, run \`RELEASE_CANDIDATE→FROZEN\` with exact PDF freeze record / release manifest. Only narrowly scoped separately approved compatibility for a genuinely repeated frozen validator admission flaw; no new Owner approval invented.
3. Create normal history-preserving main PR/merge; verify the exact FROZEN State, PDF, Source Manifest/Release Manifest on main; then dispatch \`.github/workflows/survey-production-v2-release.yml\` with exact permitted \`issue_id\`, \`production_state_sha256\`, \`release_manifest_sha256\`, \`release:2026-W43\` confirmation (check actual workflow inputs; these are illustrative until inspected). Do NOT start workflow pre-GO.
4. Verify published GitHub Release \`weekly/2026-W43\` download PDF SHA == Human-approved PDF SHA; close release provenance via first-party flow/PR. The final GO on exact Candidate/PDF is the one normal Human publication gate; **no routine second Human Freeze/Release gate**.
5. If a real blocker after GO requires changed PDF/source SHA, return to Human for newly changed exact PDF; no silent substitution/rebuild. If a new exceptional publication route is required, stop and seek explicit new Human scope authorization, not presume it from this contract.

### 7. Minimal QA and time economy

The Human waived **additional broad new regression campaign** for known runtime compat, but wants no regression relative to r8. Honor this by focusing on identity checks, existing canonical validators and **General's independent PDF content/visual comparison**. No redundant independent GPT audit, no another 27/12 stress suite merely for ceremony. No Core redesign, no multiple unproductive preliminary plans, no user-facing micro-approvals. Seek one coherent release-ready result.

Accept technical differences in PDF metadata/fonts/pixel rasterization if no reader-visible harm; require report of any substantial page/section/table count changes. If no canonical path after bounded runtime compat, stop precisely \`MUSE_W43_CANONICAL_PUBLICATION_GATE_BLOCKED\`, push all safe real work and provide the smallest necessary missing bridge/gate primitive instead of pretending Candidate/Release-ready.

### 8. Allowlisted outputs and repository boundary

WRITE ENABLED:
- New \`sources/2026-W43/execution/runtime-compat/\` launcher, per-step adapter logs (only if needed);
- New W43 \`sources/2026-W43/draft/v2/\`, \`sources/2026-W43/publication/v2/\`, \`surveys/weekly/2026-W43/\` genuine canonical files and PDF;
- New W43 \`sources/2026-W43/execution/...\` bounded execution requests, validation, audits/general, rendered pages, hash/semantic crosswalks, implementation handoffs, sessions, bridge receipts, and append-only execution/index.md;
- Trusted operator-generated changes to W43 \`production-state.json\`, \`orchestration/v2/checkpoints/\` and Gate provenance **ONLY from actual authorized first-party stage operations**; worker may not manually edit State/Gates. No canonical Human Publication Preview approval before Human GO.
- W43 release-specific request PREPARATION only under execution/; do not create freeze/release manifests before GO.

PROTECTED:
- All shared \`scripts/\`, \`schemas/\`, \`config/\`, \`.github/\`, \`tests/\`, common Core, main and production/survey-core-v2 refs; W43 approved Architecture/Selection/Screening/Evidence/Discovery/canonical upstream; existing all \`execution/core-free-preview-r1…r8\`, P2 sidecar, prior Human approval; other Weekly/Special editions. Do not move or modify reference r8 PDF, merely read it.
- No fallback branch, forced push, unreviewed migration, secret exfiltration, unrelated issue/PR, or action outside W43.

Commit in logical bounded units on the SAME W43 branch with normal commits and non-force pushes, read back remote HEAD/Tree after each stage; mandatory final verified remote readback. General's report is committed by execution Muse verbatim and names immutable PDF SHA; do not alter report findings to present PASS.

### 9. Actual terminal and handoff

Preferred successful terminal:
\`MUSE_W43_EXACT_PDF_READY_FOR_HUMAN_PUBLICATION_PREVIEW_GO\`
  State RELEASE_CANDIDATE, genuine Candidate READY_FOR_PUBLICATION_PREVIEW, General regression PASS on exact final PDF SHA, no open P0/P1, fixed PDF GitHub SHA-pinned URL, and fully prepared AFTER-GO publication runbook.

If General needs fix: worker repairs before terminal, calls General again. If blocked, no fabricated success:
\`MUSE_W43_CANONICAL_PUBLICATION_GATE_BLOCKED\`
with last genuine State, detailed error, exact missing API/condition, committed real artifacts and next owner decision if genuinely needed.

Do not send a report that merely says "Draft generated" when downstream still possible. Do not request Human GO on an UNVALIDATED, unbound or mismatched PDF. The requested outcome is **one finished, regression-checked, immutable Candidate** followed by one Human exact-PDF GO.
