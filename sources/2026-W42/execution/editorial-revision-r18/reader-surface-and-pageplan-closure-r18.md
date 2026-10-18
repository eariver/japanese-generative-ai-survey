# W42 r18 reader-surface and pageplan closure (S17-01..S17-04)

Date: 2026-10-18 JST. Baseline r17 HEAD `8509ee33…`, dispatch HEAD `9c95ede0…`.
Status: `SOL_W42_R18_FOCUSED_CLOSURE_AUDIT_READY / NONCANONICAL` candidate (pending independent focused audit).

## S17-01 — reader-surface block-ID leaks: CLOSED (3/3 repaired, 0 residual)

Old → new (meaning-preserving, minimal; no analytical content deleted):

1. P1 `t1-23`
   - Old: `…提供原価ではない。失敗の内訳はt1-16に集約し、ここでは初回起動の単一試行という限界とセットで読む。固定シードや…`
   - New: `…提供原価ではない。初回起動の単一試行という限界とセットで読む。固定シードや…`
   - Method: process cross-reference omitted entirely (contract option 2). Cost denominators, single-run limit, fixed-seed correction kept; death-count duplication still avoided (counts live once in t1-16).
2. P6 `t6-08`
   - Old: `…計画の上乗せは効かない（開放問の数値はt6-06に集約しここでは繰り返さない）。CBGBも…`
   - New: `…計画の上乗せは効かない。CBGBも…`
   - Method: parenthetical planning note deleted; GeoKTools/Table-5 link stands on benchmark names (GeoKTools, CBGB, Table-5 domains) and comparison conditions (tool-only vs full-GRA, same-model control). Pro negative, Flash positive, domain negatives, paper/repo count conflicts preserved.
3. P7 `t7-19`
   - Old: `…発行者構築ベンチでの測定という前提で読む（t7-07の数値行はここでは繰り返さない）。HSS46.36が…`
   - New: `…発行者構築ベンチでの測定という前提で読む。HSS46.36が…`
   - Method: process note deleted; comparability genuinely interpreted (vendor-built bench, Sol46.6/Opus44.6 condition-identity unconfirmed, API/weights/pricing scope). HSS negative, 12-row mechanism in t7-07, pricing kept.

Receipts:
- Block-diff r17→r18: exactly 3 changed blocks (`t1-23`, `t6-08`, `t7-19`; P2/P3/P4/P5 0). File: `block-diff-r17-r18.json`.
- Regex gate on all r18 HEADING/PARAGRAPH/TABLE/NOTE + headline/deck: pattern `t[1-7]-[0-9]{2,}` → 0 hits. File-path/`CLAIM_BOUNDARY`/`accepted_context_notes`/placeholder patterns → 0 hits. Frozen-operation strings (`SOL_EXECUTION_AUTHORITY`, `NONCANONICAL`, gate ops) → 0 hits.
- Accepted legitimate external codes (7, each with rationale, NOT leaks):
  - `Muse条項`, `Muse・Kommunity` (P3 t3-18/t3-19): Meta Muse model-license naming, external license terms.
  - `Sol Ultra`, `Sol Medium` (P4 t4-21): cost-ledger model variant names, external price rows.
  - `Astra・Sol・Luna` pool (P4 t4-08/t4-22): HydraFusion model-pool names, external system description.
  - `Sol46.6` (P7 t7-19): comparator benchmark score label, external evaluation figure.
- TeX body scan (cites/labels stripped): 0 internal-ID hits. Extracted PDF text scan: the 3 old strings absent. Visual: p3/p14/p17 PNGs opened, no IDs printed.
- Intentionally left: nothing leaked; negative evidence (GeoKTools/Table-5, HSS shortfall, failure denominators) preserved in place.

## S17-02 — pageplan arithmetic: CORRECTED

- r17 error: cover1 + bib4 observed, but computed `26.5+4=30.5` (dropped the cover page).
- r18 correction: conditional hypothetical `26.5+1+4=31.5` total physical pages (approved body plan + r17-observed cover+bib allocation). NOT a real rendered 31.5pp PDF; distinct from measured r18 21 total. r16 comparison `26.5+1+3=30.5` kept as historically true for its observed nonbody split (cover1+bib3).
- Physical vs effective never mixed: body physical (p2–p17, 16pp) vs effective article area (~15.5–17, tables/notes discounted). Chapter spans not double-counted (ranges listed with flow caveat; tables counted once in hosting chapter).
- target28/max30 remain approved and unchanged; hypothetical 31.5 exceeds max30 by 1.5pp — stated explicitly. Bibliography style effects on future counts acknowledged (r18 bib 4pp with publisher labels + alias cross-refs vs r16 3pp raw URLs).
- New brief `human-architecture-pageplan-decision-brief-r18.PROPOSED.md` cites verified r18 split + effective range after render; Option sums verified algorithmically (B: 2.5+2.5+3+2.5+2+2.5+2=17.0). Magazine-signature filler suggestion from r17 removed (not an approved method). No Human preference selected; no Core amendment capability claimed (see S17-04).

## S17-03 — visual flow (Table 7, B57): IMPROVED, residual noted

- Table 7 in-body preserved from r17 (after t7-04, before ASPIRE). r18 p17 PNG opened: table at page top with P7 body text below/after; no orphan, no cross-chapter drift, no clipping/whitespace change. p16→p17 transition is the P6/Table-6 → P7-GLM-anchor chapter boundary (full paragraphs each side); the table float does not split a sentence (t7-04 paragraph complete before table; ASPIRE paragraph complete after). Reader flow accepted as natural.
- B57: `\needspace{4\baselineskip}` entry-level barrier added (preview.sty already provides needspace; no width/font/margin change). Result: B57 entry kept together on p20 (URL wraps ASPI/RE across two lines *within* the entry — normal xurl behavior, readable). The r17 defect (page-top lone `RE` continuation from p19) is gone. Side effect: B28 URL wraps across p18→p19 with 4-char `lein` carry at page top — minor, readable, same class as normal bibliography wrapping; recorded as known limitation, not a blocker (no safe fix without cascading pagination shifts or worse whitespace).
- No float drift, no table-only pages, no body/bib mixing. Log clean.

## S17-04 — decision boundary: RESPECTED

- Option B sum re-verified: 2.5+2.5+3+2.5+2+2.5+2 = 17.0 ✓ (algorithmic). 7 chapters + 28 selection + 26.5 approved plan + target28/max30 kept until independent closure + Human decision. No new candidate/chapter/page-target enacted.
- Magazine-signature filler proposal removed.
- Frozen Core legal path (read-only research, NO invocation): `scripts/survey_human_gate_v2.py` supports contiguous Human review revisions (Architecture r2…) and Publication Preview `REQUEST_CHANGES` with upstream `regeneration_boundary` reopening Architecture (`_reopens_architecture`, cross-gate rule). No verified shortcut for post-approval amendment without a new Human decision; silence ≠ approval. Feasible governance options for Human (not executed): (a) new Architecture Review r2 with revised allocations (Human APPROVED/REQUEST_CHANGES, r1 record preserved); (b) Publication Preview revision with upstream boundary (reopens Architecture per cross-gate rule). Brief lists uncertainty; no CLI invoked, no gate written.

## Regression guards (all held)

Maia ONE pod (24×4=96) + 750 GB/s band scope; LFM Legal-Entity annual-revenue $10M + §5(c) qualified + hosting=channel; Argon random Easy world + non-playing Observer + fixed-seed wording; ASPIRE publisher real-robot results with figure UNKNOWN; Earth tool-vs-plan (Pro negative / Flash positive / GeoKTools Table-5 domain negatives) + 220/210 + 44/45 splits; aptamer 131/311 screening vs separate 8-clone assays + DIRECT_FETCH_TOOL_LIMIT; Nemotron average acceptance **length** (not rate) + draft-7 + temp split; W42 chronology; license/independent-source tiers. No new facts; net −70 chars from leak removal (25,085→25,015); no padding.

## Stop assessment

All reader-surface hazards closed (0 unintentional leaks, receipts above). Pageplan math corrected and re-anchored to r18 measurements. Visual: Table-7 in-body kept, B57 orphan fixed, residual B28 wrap documented as minor. Frozen 7/7 + synthesis PASS (receipts in validation report) *plus* independent reader-surface gate PASS. No new PDF reprinting uncorrected IDs (extracted-text scan clean). → `SOL_W42_R18_FOCUSED_CLOSURE_AUDIT_READY / NONCANONICAL` (not BLOCKED).
