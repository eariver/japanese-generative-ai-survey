# W43 Sol — Core-free/noncanonical PDF Preview r1 execution contract

Date: 2026-10-26 JST. Status: `EDITORIAL_SOL_AUTHORITY / INDEPENDENT_R35_PASS_WITH_LIMITATIONS_ACCEPTED / PDF_PROOF_ONLY / NOT_DRAFT_COMPLETE`.
Repository: `eariver/japanese-generative-ai-survey`. Branch: only existing `weekly/2026-W43-v2-work`. Executor: Muse Worker. Independent Sol review and Human Owner approval are separate.

## 0. Remote six-way fail-closed guard

BEFORE any edits, read each remote ref HEAD and Git root tree, compare all six values. The following W43 pair is the **pre-contract parent**; the **dispatch message** gives Muse's real post-contract starting W43 HEAD/tree. The main/Core pairs stay unchanged.

| Ref | HEAD | Root Tree |
| --- | --- | --- |
| Work (pre-contract parent) | `8c61ecd56aaa662209ef8cb83fdcfb0bc2c9bcd4` | `845f6cbde32d99bade83c591d586c1f206d697fd` |
| main | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| production/survey-core-v2 | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

The dispatch W43 HEAD/tree, rather than stale parent values above, authorize execution. Its parent must be `8c61ecd...`, only new file diff must be this contract. Any mismatch -> ZERO WRITES, exact expected/actual, STOP. Clean local behind -> fetch/ff-only. No new/fallback/review/repair branch, reset/rebase/force, overwriting somebody's work, PR, merge or main/Core edits. Normal non-force commits/push and remote readback; recheck remote head before push.

## 1. Audit adjudication and protected authority

Independent Sol report `20261026231458_SolReview.md` on fixed **Muse r3.5** HEAD `bc6b1cdf8af266e0072df75449719bf535c65b18` / root Tree `dfe0eefeb9921327ce17986914fb3c9c02f68bd1` has ruled `R32-FULL-003=FIXED`, P0=0, remaining P1=0, overall **PASS_WITH_LIMITATIONS**. Editorial Sol accepts this as permission **only to build noncanonical, Core-free, UNVALIDATED TeX/PDF preview**. It is not a Human decision or Core Stage PASS. Previous 9 original findings keep independently adjudicated FIXED/QUALIFIED status; 31 Architecture obligations keep independent 20 SUBSTANTIVE_COMPLETE/11 PARTIAL baseline. Do not claim all 31 complete.

The independent review checked 20 headers, 80 physical rows (78 DATA, 2 NOTE), 3 figure blocks, 96 ledger blocks, 29 numerical claims, 13 sanctioned aliases, repaired COBOL 40%+ and npm time. Python's saved result lists 24/24 negatives, but independent Sol **did not run the Python negative tests itself**. Residual limitations: `claim_id/source_class` expected-map testing not exhaustive, some original raw snapshots unavailable, no independently reproduced benchmarks. Do not promote qualified evidence to verified raw.

Read before work:
- `sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md` (audit-fixed source), ledger, manifest, strict checker, result, r3.5 source crosswalk and QA.
- `sources/2026-W43/execution/SOL_W43_CORE_FREE_EDITORIAL_R3_5_P1_REPAIR_HANDOFF.md`.
- `sources/2026-W43/execution/governance/human-w43-r6-architecture-approved-with-closing-weekly-summary-20261025.md` and `execution/governance/sol-w43-core-free-editorial-bypass-authorization-20261025.md`, approved `architecture-v2.json`, Selection, `production-profile.json`, `production-state.json`.
- W42 layout reference **read-only**: `sources/2026-W42/execution/preview-r15/main.tex`, `preview.sty`, later r26/r29 table/print diagnostics if helpful. Reuse style patterns, not W42 stories. Frozen Core tools are read-only references, not executables to workaround Stage.

Pin exact r3.5 source SHA256 before printing:
Reader `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`;
Ledger `6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4`;
Manifest `85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111`.
If any original-byte mismatch, stop. Muse need not pretend to have independently fetched the uploaded Sol audit; the binding disposition is copied accurately above.

**Absolute protection**: Frozen Core v2 unchanged; no edits to `scripts/`, `schemas/`, `config/`, `.github/`, main, old r1–r3.5 assets, accepted Evidence/Views/Materiality/Selection/Architecture, Human Gates, Production State, checkpoint receipts, old review records. Native Draft remains blocked at Screening state SHA drift by design; user expressly forbade Core repair and authorized only this editorial bypass. No native `DRAFT_COMPLETE`, `VALIDATED_DRAFT`, publication candidate, canonical Preview, Freeze, Release or gate mutation.

## 2. Only new edition-local output namespace

Create new files ONLY under `sources/2026-W43/execution/core-free-preview-r1/`, one `sources/2026-W43/execution/SOL_W43_CORE_FREE_PDF_PREVIEW_R1_HANDOFF.md`, one `execution/sessions/muse-w43-core-free-preview-r1-20261026.md` and append-only `execution/index.md`. Do not write `surveys/weekly/2026-W43/main.tex` or `main.pdf` nor canonical `sources/2026-W43/publication/v2/`.

Required outputs:
1. `reader-print-projection-r1.md` plus `print-projection-diff-r1.md`: presentation-only print manuscript faithfully projected from *exact r3.5*; all P1–P8, 19 selected (12 primary+7 supporting), 20 tables/80 rows, 3 figures, 29 claims and **five paragraphs of standalone 「今週の総括」 immediately after P8, before references**. Not P9. Keep source/claim authority levels and negative findings; no invented articles, values, grants, comparisons or primary evidence. Make every print-only wording change/dropped operator token auditable via source-id-to-print span and explicit before/after. Clean reader-facing title: do not print `非正規編集資産` or internal `ROW_JOIN`/`P1_OPEN`/`NEVER_STORY`/internal archive paths/QA scores. Retain semantic limits in natural Japanese (unverified, no original, out of window); do NOT erase them to sanitize layout. No substantive edits without a new Sol decision.
2. `main.tex`, any needed scoped `preview.sty`, and successful `main.pdf`. The metadata (NOT an intrusive publication cover stamp) must say `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`. Neutral public-facing weekly issue title/date/cutoff. TeX may use existing jlreq/LuaLaTeX print method, accurate Japanese glyphs, hyperlinks, citations, tables, figures. If no renderer, fonts, or compatible build, report actual errors and stop; never fake a PDF or URL.
3. `build-manifest-r1.json` with SHA256 of actual input reader/ledger/manifest, print projection, TeX, style, PDF (raw bytes), file sizes, actual compiler/tool versions, commands/exit codes, honest PDF page count, exact status, external proof paths and build warnings. `main.log`, `build-commands-and-limitations-r1.md`.
4. `reader-to-print-fidelity-and-citations-r1.md`: source block/paragraph/heading/text→print mapping; all 20 table headers/80 source rows to printed table cells (PDF may reflow); 3 figure blocks; all 29 claim meanings/units/comparators/data/NOTE exclusions, reference keys and bibliography URLs actually resolved, no duplicated/lost rows; source tier unaltered. Reader-visible sources must not be padded URL dumps.
5. `physical-page-and-table-qa-r1.md` and ALL page PNGs `pages/p-01.png` through `pages/p-NN.png`, plus numbered batch `contact-sheet-*.png`. Inspect **EVERY actual PDF page** for table width, font size, broken Japanese glyphs, clipping, weird floats, captions/row cohesion, code and URLs, near-empty or overfull pages, missing source note, order, bibliography, P8→summary continuity, cross-page word/sentence break. Record per-page observations and fixed errors, even if all pass.
6. `independent-visual-review-request-r1.PROPOSED.md`: request only, listing fixed PDF/TeX/PNG hashes, risks and open limitations. NO forged independent PASS, Human Gate or publication receipt.

If GitHub binary transport or rendering is blocked, state what is missing and STOP; do not claim audit-ready. Include actual PDF Git object verification / stable commit-pinned link in the final report only once it truly exists remotely. Keep incidental .aux/.synctex/cache out of git.

## 3. Publication fidelity and factual guards

- Window `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)` (Oct 17 07:00 JST–Oct 24 07:00 JST), inclusive start/exclusive end. 8 packages P1–P8, 19 selected (12 primary + 7 supporting), 31 Architecture must-cover baseline as accepted; recap is additional closing section NOT extra package.
- Human Architecture approximate target **38 pages**, max **44 pages**, prior body/front/back estimate ~37. Honest density and body-vs-bibliography page split. Never pad to 38 with giant whitespace, fonts, empty charts, duplicate prose; don't silently shrink for max44. If honest text is far shorter, unreadably cramped, or exceeds 44, report exact page/depth conflict and STOP `VOLUME_OR_LAYOUT_REVIEW_REQUIRED` for Sol.
- Preserve MemT 66x **storage not speed**, 11bench parametric-memory scope, 1.86x `SOURCE_UNVERIFIED`; Patch stage4 preparation vs stage5 patch-available guidance, Daybreak outside, unknown CVE != no CVE; FLUX FAQ unarchived/unattributed and keyframes live unresolved; Duet existing vs 1Password `coming soon`; Voxtral comparator/units unverified; DeepInfer code `PSEUDOCODE`, unexecuted; COBOL 40%+ enterprise prevalence ≠ accuracy 72.1%; GH saved release clock distinct from npm registry `RAW_NOT_ARCHIVED` time; DeepSeek MIT vendor-declared, model artifact LICENSE/SHA not retrieved. Vendor results not upgraded to independent.
- Ensure meaningful source attribution from the r3.3 37-key crosswalk + r3.5 delta and archived sources, precise URL/claim mapping, no false provider clock or future event as W43 IN. Internal QA controls remain sidecar, without disappearing reader-facing caution.
- For wide tables use proven multi-column full-width pagination-safe scheme; captions should not detach, no table overrun into another story, no orphan concluding paragraphs or one-page URL leftovers.

## 4. QA gate and terminal output

Only permitted local executable checks are edition-local r3.5 checker and normal typesetting/print QA. Report fresh exact commands/exit codes and actual PDF metadata. No native Core Stage/Bridge/Approval or formal validation; no bypass to RELEASED. Verify no unauthorized path changes; recheck remote, normal non-force commit and remote readback HEAD/Tree, compare paths, PDF binary existence and hashes. No unsupported claim of independent PDF visual QA.

Success terminal: `MUSE_W43_CORE_FREE_PDF_PREVIEW_R1_READY_FOR_SOL_VISUAL_REVIEW`, **only** if PDF and all-page images/contact sheets, full source/29-claim/20-table parity, bibliography and provenance records are real, committed and remote-verifiable, with no critical readability/layout defects.
Failure terminal: `MUSE_W43_CORE_FREE_PDF_PREVIEW_R1_BLOCKED`; volume failure `VOLUME_OR_LAYOUT_REVIEW_REQUIRED`, with truthful evidence and actual blocker.

Final Muse report must list exact start/final HEAD+Tree, six-way checks, normal FF ancestry, complete diff, immutable upstream State/Core/Human Gates, r3.5 input digests, each TeX/PDF/image path+SHA, actual page count, per-page QA, 29-claim mapping and unresolved provenance, a **verified commit-pinned GitHub PDF URL** or explicit unavailable status, and proposed independent visual review packet.

Stop at editorial Sol visual review. A separate independent semantic/visual review and explicit Human PDF approval are **future decisions**, NOT part of this execution. Freeze/Release need a separate Human-governed authorization while native Core is blocked.
