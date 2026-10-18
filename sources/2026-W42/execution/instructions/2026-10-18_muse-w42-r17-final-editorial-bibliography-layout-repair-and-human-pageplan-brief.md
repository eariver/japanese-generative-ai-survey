# J-GAS W42 Muse r17 — bounded final editorial/bibliography/layout repair + Human page-plan decision brief

Date: 2026-10-18 JST
Status: `SOL_EXECUTION_AUTHORITY / R16_INDEPENDENT_REQUEST_CHANGES_ADOPTED / SINGLE_BOUNDED_R17 / NONCANONICAL_ONLY`
Repo `eariver/japanese-generative-ai-survey`; branch `weekly/2026-W42-v2-work` (EXISTING ONLY).

## 0. Fail-closed identity guard

Sol dispatch gives **Exact Starting Remote HEAD** and **Expected Starting Tree** (the commit containing this instruction). BEFORE any writes, read actual remote branch ref + commit object + root tree (read-only) and compare both byte-for-byte with Sol dispatch. Also verify main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`, Frozen Core v2 `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Independently audited r16 baseline HEAD/Tree `a54d55b8ee6d8030d0f0a21d704dc20aec3918e9`/`a8c82b1bafb7b97c5064c5346164db665895e715`.

ANY mismatch, ambiguous precondition, missing root Tree => **STOP / ZERO WRITES**, report expected versus actual. No fallback/repair/review branch, no reset, rebase, force, history rewrite. Before final push, re-read remote lease; normal commit and non-force push ONLY. Full current ancestor and immutable-path diff protection mandatory.

Fully protected: main, Frozen Core, shared roots; W42 canonical discovery, evidence/views, materiality, completeness, selection, **approved Architecture r1**, production-state, human gates, review index, checkpoints, canonical Draft v10.0 and synthesis; all pre-r17 r11–r16 historical edition-local files **including original r16 proof**. No formal Stage transition/VALIDATED_DRAFT, Reader or Publication Preview, Human Gate, Freeze/Release.

All written artifacts must be NEW `sources/2026-W42/execution/editorial-revision-r17/` and `execution/diagnostic-r17/`, a session report under `execution/sessions/`, plus append-only truthful `execution/index.md`. No new selected topic or architecture rescope.

## 1. Required reading / exact distinction

1. Sol ruling: `sources/2026-W42/execution/reviews/sol-w42-r16-external-audit-disposition-20261018.md`. This cites the original external report `20261018165050_SolReview.md` delivered separately by Human, **not stored here**; do not claim direct review of raw report unless obtained.
2. r16 session, source repair ledger, 7 Draft proposals, reader, citation ledger, bibliography map, change and validation reports, `diagnostic-r16/main.tex`, `preview.sty`, full `main.log`, manifest, `review-pages-r16.md`, 21 PNGs/PDF. External independent r16 auditor independently byte-verified PDF and inspected 21 PNGs; the large 12.5MB contact sheet was not viewable.
3. Original Human r9 Architecture dossier and Human r1 approval evidence, original `architecture-v2.json`, 7 packages/28 selected (PRIMARY16+SUPPORTING12), 26.5-body plan / magazine target28 max30, r9 provenance errata.
4. Carefully distinguish `execution/diagnostic-r16/` as NONCANONICAL, not a formal publication; never use stale `preview-r15/main.pdf` as current manuscript.

## 2. Unit A — high-priority, SOURCE-CONSTRAINED text and bibliographic corrections

Write `editorial-revision-r17/finding-closure-matrix-r17.md` with each F16-01..F16-09 exact block IDs, primary URL/section, old wording, new wording, verification source, remaining unknown, pass/fail. No generic "all addressed" labels without results.

**F16-01 / Maia P2 t2-03 and t2-20 (HIGH).** Official https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ "Rack-scale architecture": 24 4-accelerator trays = 96 accelerators in **one pod**, 167kW rack. Eliminate `96ポッド` (NOT 96 pods). `750GB` is **750 GB/s** bandwidth only in original specified cross-rack/pair configuration; distinguish GB, GB/s, HBM GB, TB/s, accel vs pod vs tray. Scan all seven proposals, proposed tables/notes, generated reader and TeX, new sidecars. Do not make 7× vendor comparison universally achievable or independent reproduction.

**F16-02 / LFM P2 t2-21 and t2-08 (HIGH).** Check https://www.liquid.ai/lfm-license §§1/4/5/11 and hosting FAQ, exact qualification of §5(c). Say Legal Entity controlled-entity annual revenue threshold **US$10 million** (not profit, not model-only proceeds); model hosting/redistribution platform is a **distribution channel**, never `台座` or `模型`. Distinguish downstream users' obligation and actual eligibility of nonprofit/non-commercial/research conditions — no blanket exemption. Leave per-file weight license unopened if not actually read. Preserve vendor/weight license provenance.

**F16-03 / P1 Minecraft translation cleanup (MEDIUM).** Source https://arxiv.org/html/2610.22319; say four **player agents** and one non-playing **Observer**, not physical machines or non-fighting agent. Randomly generated Easy Minecraft world; don't translate seed as `種`. Natural technical Japanese for observation beyond blocks and dragon phases; preserve 2,783/2,839, 229, 605, 27h14m and single-run limits accurately. Full-text scan P1–P7 for `模型,台座,程序,固定種,龍相,96ポッド,750GB` and source-specific natural equivalents. Deliver old/new table without introducing Chinese-like unnatural compounds.

**F16-04 / semantic dedup, preserve true findings (MEDIUM).** P6 t6-06 should state experimental design and Pro-vs-Flash 4×2/SD once; t6-08 should retain **GeoKTools and Table 5 area-specific negative interactions and explanation** without repeating the identical GeoExpert cells. P7 t7-07 retains Glimpse result table and exact baselines; t7-19 explain comparability, API/non-open weights and pricing scope instead of repeating numeric row. P1 t1-16 vs t1-23 quantify failure counts only once while keeping mechanism/limitations. Review other 7 chapter repeated evaluation/boilerplate phrases; don't delete novel counterexamples, licenses, or key reader conclusions. No padding/extra fictional details; shrink if justified.

**F16-05 / normalized bibliography and source trace (MEDIUM).**
- B74 url **MUST** become bare `https://github.com/OpenBMB/MiniCPM-V`; place `via @OpenBMB X 2026-10-12` in distinct `locator_note`/`provenance_note`. Verify every one of 90 logical entries via actual URL parser (scheme/host/path/whitespace, trailing notes), NOT merely `startsWith('http')`; report invalid=0. Test HTTP reachability on key critical original sources feasible with tool and flag any skipped/failed key `UNVERIFIED`, never claim all 90 HTTP-verified without running all 90.
- External auditor lists 19 normalized duplicate pairs: `B01/B62;B05/B65;B11/B69;B20/B72;B24/B73;B32/B75;B33/B76;B34/B77;B35/B78;B39/B82;B40/B79;B41/B80;B42/B81;B43/B83;B48/B84;B50/B85;B51/B86;B52/B87;B59/B88`. Actually normalize host (www), trailing slash, URI encoding, redirects *where verifiable* and compare semantic identity. Don't blindly merge different source snapshots merely based on URL resemblance. For genuine aliases create `alias_of` metadata while retaining ALL 90 readable Bxx keys/177 ledger rows for backward trace; reconcile category (B62/B65 marked SECONDARY while same first-party site, B88) and specific source version/section.
- Design reader bibliography to show human-verifiable **publisher/author (year), source title, then clean link** where reliably known. Do not invent metadata; mark unverified titles as such or use grounded site/publisher label. For duplicate keys choose one canonical printed reference with alias cross-reference or clear separate labeling; maintain clickable Bxx citations and mapping, never drop a claim. Publish `editorial-revision-r17/bibliography-normalization-r17.md`, `bibliography-map-r17.json`, `citation-repair-ledger-r17.json` and TeX print rules. Clarify printed entry count vs 90 logical keys; bibliography-page allocation must be measured after style changes.
- Preserve primary source table/section locators, Earth unresolved paper-vs-repo 220/210 and 44/45, NVIDIA MTP acceptance **length** and wetlab 131/311 vs 8 clone. Do not introduce unsupported interpretation through dedupe.

**F16-08 / Wetlab Methods qualification.** Update ONLY newly authored r17 editorial status to `DIRECT_FETCH_TOOL_LIMIT / METHODS_NOT_INDEPENDENTLY_REVERIFIED` for PDF >5MB prior failed one-shot transfer; this is NOT `NOT_PUBLIC` or permanently inaccessible. A **bounded** alternate accessible first-party HTML/PDF streaming/browser pathway may be attempted, logging exact result (method and failure reason); do not stall whole r17 on this. Do not change specific numeric thresholds without reading original methods. Keep screening-vs-confirmation separate.

## 3. Unit B — full edition-local PROPOSED replacement + frozen validation

Create seven new `editorial-revision-r17/proposals/P1..P7/draft-result-r17.PROPOSED.json` and new reader JSON+MD, source/claim crosswalk, bibliography map/ledger, proposed synthesis input/result, r16→r17 block diff, change/readability report. r16 and earlier artifacts remain byte-identical. Preserve Human-selected 7 packages/28 items, must_cover/source boundary maps, source dates, source certainty. All corrections tied to original block IDs and official source locators; no invented science.

Run genuine frozen `draft-check` P1–P7 and `synthesis-check` on new proposed files; record receipts, reproducible counts (paragraph-only, PTN with headings, tables/notes) and exact changes from r16. Add one `editorial-revision-r17/content-quality-preflight-r17.md` separating factual/editorial/visual from pagination. Avoid adding lengthy generic caveats as substitute for detail. Even if original 28-page target is unachievable, **proceed to diagnostic build to measure**; no quota-driven draft inflation.

## 4. Unit C — layout engineering and measured diagnostic (HIGHEST EDITORIAL GATE)

**F16-06 p18 orphan table is NOT PASSABLE.** Generate TeX from new r17 reader/citation bytes in ephemeral local build only. Compare at least two legitimate table-placement approaches (e.g. move Table 7 to near P7 introductory comparison, inline/tabularx or side-safe nonfloat, `float`/barriers) and preserve natural reading sequence. `\clearpage` alone is not a fix; after Table 7 has rendered inside P7 body, flush before bibliography, avoid cross-chapter/into-bib floats. Show PDF screenshots/PNG for relevant pages and record tested layouts. Keep table content, do not shrink fonts, alter margins or insert whitespace solely to get a target count.

Write all successful diagnostic artifacts under NEW `execution/diagnostic-r17/`:
- exact TeX/style, genuine compiled PDF, **full** `main.log`, parser-read PDF page count + SHA256/bytes, build command/versions/embedded fonts; scanned warnings, over/underfull/undefined/missing CJK characters;
- **all individual page PNGs** (not subset), contact sheets **split into 2–3 small readable files with individually fetchable sizes**, and review-pages index with actual *viewed* page-by-page results;
- every key chapter table beside corresponding P1..P7 explanatory section, no isolated last table, no URL entry across pages leaving meaningless dangling fragments, bib sources readable and valid;
- compare r16 21 total / cover1 + body17 physical (effective ~15.5–17) + bib3 to r17 actual **new** cover/body/nonbody and effective-area range; identify p18 improvement separately from any page count shrinkage. Treat previous 9,400-character shortage / 6–7 pages as invalid exact claims.
- retain explicit prominent `NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL` proof labels. Do NOT touch canonical publication paths or old `diagnostic-r16/`.

On any nontrivial visual or factual blocker, **report unresolved and stop at BLOCKED/REQUEST_CHANGES**, not PASS. No formal Reader/Preview render.

## 5. Unit D — Human page-plan decision brief, DRAFT ONLY; no Human vote

After measuring actual repaired r17 PDF, create `editorial-revision-r17/human-architecture-pageplan-decision-brief-r17.PROPOSED.md`, clearly:
- fixed approved architecture allocations P1 4.0/P2 2.5/P3 5.0/P4 4.0/P5 3.0/P6 4.5/P7 3.5; body 26.5; magazine target28/max30; official `architecture-v2.json` and r1 Human approval unchanged;
- r16 original vs newly measured r17 total and physical/effective article-body pages, cover and bibliography print pages, chapter ranges without double counting, table/footnote overhead and unresolved source constraints;
- does content substantively meet reader technical goals (per chapter), irrespective of whether 26.5-page target is reached?
- **Option A** retain current targets and identify **specific** new original evidence required to support added pages without padding, if viable; **Option B** recommend defensible *provisional* new per-chapter allocations and total (including true bibliography), **preserve all 28 selected and 7 technical chapters**; **Option C** structural scope revision only if compelling newly documented reason. State trade-offs and residual risk.
- list exactly which Human approval/re-gating mechanics need authority confirmation under frozen Core workflow, rather than forge/revoke r1 or hand-write new gate data. **Muse's brief has no approval authority**. No unilateral changes to Architecture, State, approvals or checkpoints.

This brief is for Sol vetting and later Human decision **after** narrowly scoped independent r17 closure audit, not a new Human Architecture decision created during execution.

## 6. Deliverables, regression, terminal stop

At minimum:
1. `editorial-revision-r17/finding-closure-matrix-r17.md` for F16-01...F16-09 with old/new and honest remaining caveats.
2. 7 fresh Draft proposals + reader JSON/MD, ledger/bib/crosswalk, synthesis and actual frozen validation receipts, paragraph and PTN counter definitions.
3. Bibliography 90/90 URL syntax and real alias/classification matrix, source-display plan (no fabricated publisher/title), `bibliography-normalization-r17.md`.
4. Genuine independently-auditable new r17 diagnostic TeX/PDF/log, all page PNGs, split contact sheets, actual page-level visual QA and measurements, evidence of p18 orphan fixed or named unresolved blocker.
5. `human-architecture-pageplan-decision-brief-r17.PROPOSED.md` anchored to *actual* r17 measurements, not arbitrary 28pp padding.
6. `editorial-revision-r17/validation-report-r17.md`, `execution/sessions/muse-w42-r17-20261018.md`, append-only `execution/index.md`.

Regression requirements: frozen Core untouched; main untouched; all canonical W42 Evidence/Selection/Architecture/Human Gate/State/canonical Draft unchanged; r13–r16 historical bytes identical. Keep Minecraft randomly generated world, Maia rack 24 trays/96 accelerators in ONE pod, Earth Pro negative/Flash positive SD, ASPIRE publisher real-robot evidence, LFM exact thresholds, Nemotron Table 8 average **acceptance length**, wetlab separate denominators, W42 cutoff, license/independent source tiers.

Check remote HEAD/Tree immediately before commit, commit only allowed edition-local changes and non-force push; remote read-back final HEAD/Tree, full path list and historical blob identity. Terminal `SOL_W42_R17_FINAL_DIAGNOSTIC_AND_PAGEPLAN_REVIEW_READY / NONCANONICAL` only if all bounded factual/bib/visual corrections are demonstrably resolved; otherwise `R17_BOUNDED_REPAIR_BLOCKED` with actual failed gates. Never run formal Reader, Publication, Freeze, Release or any Human Gate action.
