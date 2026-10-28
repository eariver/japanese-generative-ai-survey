# J-GAS W43 — Sol bounded r3 print-projection semantic preservation + reader bibliography linking repair

Date: 2026-10-26 JST.
Status: `EDITORIAL_SOL_R2_PRINT_FIDELITY_REQUEST_CHANGES / INDEPENDENT_R35_TEXT_P1_CLOSED / NONCANONICAL_PDF_ONLY / HUMAN_GATE_PENDING`
Repository: `eariver/japanese-generative-ai-survey`. Worker: Muse on existing `weekly/2026-W43-v2-work` ONLY.

## 0. Exact six-way remote guard and write permissions

**All six values must be checked read-only from remote refs + actual git/commit root trees before ANY write**. This contract's own parent is r2 HEAD `f29e77ebf4637721ae880aea7ae9c5c3062396e8`, Tree `22371300ee060eace667c09731fb3b069d2b5dfa`, NOT the later actual Muse start. Sol's separate dispatch supplies exact post-contract starting W43 HEAD/Tree: use those, and confirm the post-contract commit is one normal FF child of this r2 pair changing only this contract file.

Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
Mismatch → ZERO WRITES, actual/expected report, STOP. No new branch/fallback/review/repair, no reset/rebase/force, no main/Core changes or PR/merge. Normal FF commits + non-force push on existing W43 ONLY; check remote before push, read back exact final SHA/Tree and path diff.

## 1. Sol r2 recheck — accepted vs new print blockers

Fixed r2 review subject:
- HEAD `f29e77ebf4637721ae880aea7ae9c5c3062396e8`, Root Tree `22371300ee060eace667c09731fb3b069d2b5dfa`.
- r2 `sources/2026-W43/execution/core-free-preview-r2/main.pdf` exists in GitHub, declared raw SHA256 `922fa1d582515841d8393014ed693b4af833ee8ebb5835ff92328bd01ebb9060` / 483473B / 22 pages; 22 PNGs + 3 contact sheets present. TeX compiler log has 0 Overfull, 0 Illegal, 0 Errors. **These are connector/readback + Muse build proofs; Sol has not read actual PDF bitmap or performed independent all-page visual QA**, because this connector cannot transmit binary. No fake independent visual PASS.
- Sol independently read r2 **main.tex** and confirmed r1's 60-char-cut source descriptions FIXED, all 36 `\bibitem` entries complete. In particular MemT 66x storage not speed; GH 15:18:14Z is not raw proof of npm 15:21:49.491Z, which remains `RAW_NOT_ARCHIVED`.
- r2 coverage diagnosis indexes all 31 approved Architecture `must_cover_requirements`: 20 SUBSTANTIVE / 11 PARTIAL / 0 NOT_VISIBLE **as a worker observation**, consistent with earlier independent baseline 20/11, not an independent substantive 31/31 PASS. PDF length 22 vs estimate 38/max44. Architecture's actual `page_plan.notes` explicitly says estimates, not page-count promises, and forbids padding. **Sol permits only a 22-page diagnostic proof to proceed to focused independent semantic/visual review once print defects close; no Human PDF approval and no claim that technical depth has been independently revalidated**. Do not force 38 via padding or unsupported writing.

**NEW confirmed r2 print-fidelity failures (NOT issues in approved source r3.5):**

**F-R3-01 P8 endpoint silently deleted during projection**:
- Original immutable r3.5 Reader line 473: `読み方：\`POST /v1/decisions\` に \ `model`・`input`... `.
- r1 AND r2 projection line 473 instead says `読み方：（保存済み一次資料・詳細は出典一覧） に `model`...`.
- TeX line ~753 duplicates missing endpoint. An internal-file-path stripper treated an **API route** as a repo file path, contrary to r1 contract's 'preserve POST /v1/decisions' rule and the r2 20/80/29 PASS (this is a paragraph, not one of 29 table claims). This is an unacceptable loss of technical meaning, not a styling substitution.
- **Restore exact reader-facing method/path `POST /v1/decisions`**, typeset semantically as a safe escaped monospaced token, preserve rest of request/response illustration and NOT_RUN, and include a negative regression test mutating this token out of the projection/TeX (must FAIL). Verify actual source/PDF text extraction as accessible.

**F-R3-02 print URL swallowed a Japanese parenthetical**:
- r3.5 reader line ~474 has clean `https://developers.openai.com/api/docs/guides/decisions` then `（観測2026-10-25、snapshot ...）`.
- r2 TeX line ~755 contains incorrect `\url{https://developers.openai.com/api/docs/guides/decisions（観測2026-10-25、snapshot}`. `\url` regex greedily swallowed Japanese punctuation and words, creating a wrong clickable body reference. The later correctly linked bibliography URL is NOT sufficient to excuse a malformed body URL.
- Correct URL parsing/delimiters; require **every** TeX `\url{...}` beginning http(s) to be valid URL text with no Japanese text punctuation like `（`, `）`, `、`, `。` etc. Verify all actual links in new PDF annotations when possible, not merely TeX syntax.
- Keep Oct25 observed docs post-cutoff qualified; the snapshot is genuinely edition-local archived but the editorial display should be e.g. '10月25日取得の補足資料' NOT a fake W43-time snapshot. Retain official source URL and original SHA where editorially necessary.

**F-R3-03 bibliography reference-key traceability claim false**:
- r2 bibliography-source-key-audit says `36/36 present, 0 duplicates, 0 unused (all keys appear in reader 典拠 notes or body)`.
- Sol independently searched the actual TeX **body before `\begin{thebibliography}`**: 36 bibitems exist, but 18 exact `\bibitem` keys have **zero** exact occurrences/citations in the printed body. Examples: `tanstack-gh`, `tanstack-npm`, `DI-ENV`, `DI-LICENSE`, `voxtral-card-units`, `patch-rendered`, `deepinfer-import-scope`, `decisions-ref-create`; `\cite{...}` count is 0. Some are legitimate further-reading or provenance-only keys, so **do not invent citations or forcibly cite unavailable originals**. But the `0 unused` claim is objectively untrue, and principal TanStack provider clocks cannot be followed via exact reader key.
- Prepare a reproducible exhaustive `source-key-audit-r3` distinguishing (a) EXACT_IN_BODY, (b) CLAIM_SUPPORTED_BY_EXPLICIT_NATURAL_LANGUAGE_REFERENCE, (c) SECONDARY_OR_FURTHER_READING, (d) SOURCE_UNAVAILABLE_DO_NOT_CITE, and (e) ORPHAN/AMBIGUOUS. Explicitly list all 36 printed bibitem labels, where/if referenced in body, exact claim/value, evidence tier and whether actual URL exists.
- Repair **necessary** per-claim source-key display for material technical assertions, especially TanStack GH vs npm clocks, MemT rights, Voxtral comparator/units, Patch rendered five stages, DeepInfer code. Links can be literal label in compact `典拠キー` note or appropriate `\cite` — do not scatter fake references or introduce a citation unsupported by the previously accepted 37-key crosswalk. A key with no body reference can be retained as honestly labeled further reading; if `UNAVAILABLE`, retain only if genuinely useful as a transparent unavailable-record, never a source validating claims.
- The bib-label `[KIMI-X]` etc must map exactly to line evidence; verify semantic line→source/clock/provenance, not just a numeric count. Absolute: no claim that GH JSON proves npm clock or derived snapshot is raw.

**F-R3-04 print-projection semantic diff proof**:
- r2 projection differs from r3.5 Reader in ~35 lines, with global operator-token substitutions. One was destructive (F-R3-01), and some printed repetitions are awkward, e.g. `未検証（...）` nested inside existing qualifier; optional natural Japanese cleanup only when auditable and meaning-preserving.
- Produce a **line-by-line, source-anchored allowlist for every changed source line** and a static print semantic-preservation validator that detects missing protected API paths, product IDs, all 29 claim literal equivalents, all table headers/80 rows, 3 figures, 5-paragraph recap, URL correctness and reader-source qualifiers. Include real negative tests for deleting API path, wrong provider clock/URL, malformed Japanese URL, and removing qualifiers from printed text. Do not substitute global regexp strip of things containing '/'.
- No new research, no new article, no fabricated raw. Preserve accepted r3.5 text/audit FIXED P1 and 31 Architecture obligations. Any substantive question → STOP for Sol adjudication.

## 2. One narrow r3 print-only work unit and artifact scope

Create NEW versioned files only in `sources/2026-W43/execution/core-free-preview-r3/`, plus `sources/2026-W43/execution/SOL_W43_CORE_FREE_PDF_PREVIEW_R3_HANDOFF.md`, session log, append-only index. Original r1/r2, r3.5 reader/ledger/manifest/checker, old audit contracts are immutable; so are main, Frozen Core, all shared scripts/schemas/configs, W43 State/Architecture/Selection/Evidence/Human Gates/checkpoints/receipts.
- `reader-print-projection-r3.md`, `source-to-print-diff-and-allowlist-r3.md`, and machine `print-semantic-fidelity-check-r3.py` (or equivalent) plus actual check result and true negative tests. Restore P8 endpoint and correctly scope URLs; keep source-tier words honest.
- `main.tex`, `preview.sty` if needed, `main.pdf`, `main.log`, `build-manifest-r3.json`, all pages in `pages/p-01.png..p-NN.png`, contact sheets and every-page `physical-page-and-table-qa-r3.md`. Build from exact source r3.5 reader `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`, ledger `6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4`, manifest `85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111`.
- `source-key-audit-r3.md`, `reader-to-print-fidelity-and-citations-r3.md`, `architecture-volume-carryover-r3.md` (no 38-page padding, preserve baseline 20/11; previous r2 all31 indexed but independent review still pending).
- `independent-semantic-visual-review-request-r3.PROPOSED.md` request ONLY, exact SHA pointers and report of technical risk, NOT independent or Human PASS.
- Production-specific filename/binary verify via remote tree/contents/blob metadata; actual final HEAD/Root Tree and exact commit-pinned PDF URL after normal push. Do not pretend this connector can render images. Compiler error, missing PDF/page PNG or source fidelity failure → terminal BLOCKED with actual artifacts and reasons.

Keep: 8 chapters P1–P8, 19 selected, 20 tables/80 physical rows (78 DATA, 2 NOTE), 3 figures, 29 claims, 5 paragraphs concluding `今週の総括` after P8, 36 bibliography keys with honest status. Edition-local strict r3.5 checker allowed; **NO frozen Core Stage/Reader/Bridge/Preview/Release execution**, no canonical `surveys/weekly/2026-W43/main.pdf`, no false draft success. Human Publication Preview remains pending. r3.5 independent textual closure stands `PASS_WITH_LIMITATIONS`. Print preview not formally approved.

## 3. Stop criteria

Success only if destructive P8 route replacement repaired, TeX/PDF link integrity proven, all 36 bibitems honestly categorized with accessible material claim citations, full source-to-print semantic preservation and regression tests PASS, PDF/full-page proof real and no new critical layout defect:
`MUSE_W43_CORE_FREE_PREVIEW_R3_READY_FOR_SOL_RECHECK`.

Otherwise `MUSE_W43_CORE_FREE_PREVIEW_R3_BLOCKED`. If genuinely new missing technical coverage discovered in approved 31 must-cover, `VOLUME_OR_LAYOUT_REVIEW_REQUIRED` with exact evidence; page estimate alone does not authorize filler.

Next stage belongs to editorial Sol: examine r3 full proof, ask **separate independent Sol semantic and all-page visual audit with real binary/page access**; where independent media access fails, report `PDF_VISUAL_AUDIT_BLOCKED`, not PASS. Only after this can Human view unvalidated preview for a separate explicit decision. Separate Human governance decision required for any publication pathway while native Frozen Core Draft is blocked; no Freeze or Release by this instruction.
