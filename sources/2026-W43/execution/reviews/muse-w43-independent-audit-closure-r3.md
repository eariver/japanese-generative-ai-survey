# Muse W43 independent-audit closure r3 (W43-IA-001..015)

Status: `SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_READY_R3_INTEGRATED` (pending independent Sol re-audit; NO ADVANCE_STAGE).
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Contract `sol-w43-evidence-r3-integrated-independent-audit-20261025.md` (sole active; narrow r3 superseded, retained as history).

## Reviewed authority

- Independent report transcription `execution/audits/independent-sol-w43-evidence-comprehensive-report-transcription-20261025.md` (original `20261025125414_SolReview.md` 44914B SHA256 `8e3218ec…`), 32/32 Cards+Views, P1×8/P2×7, REQUEST_CHANGES, EVIDENCE_REVIEWED blocked.
- Sol adjudication `execution/reviews/sol-w43-independent-audit-consolidated-adjudication-20261025.md` (binding disposition, 8 must-fix + 7 handle).
- Starting preflight PASS (read-only): work HEAD `f421dceb0e504966e20f21f6e87b08657a6962f7` / Tree `b79d51b08e86eba5a30b8e35af25adc564fc5698`; main `041a08df…` / `a134dc36…`; Frozen `774dd39a…` / `cd46a6f7a…` (origin refs verified).
- Frozen Core unchanged; native `survey_agent_tool_v2` agent-first adapter + derived-only 7-projection (W42 precedent). Issues #568/#569 remain OPEN.

## Human decision

- NONE. No Human Gate requested or impersonated. Architecture/Publication remain pending. No `ADVANCE_STAGE`, Selection, Architecture, Draft, PDF.

## Requested changes

All 15 audit findings handled in one bounded r3 (P1 FIXED must-pass; P2 RESOLVED / RESOLVED_WITH_LIMITATION / UNRESOLVED_DEFERRED_WITH_RATIONALE, no silent omission).

| ID | Sev | Item | Exact sources inspected | Depth | Before → After | Verdict |
|---|---|---|---|---|---|---|
| W43-IA-001 | P1 | GCP date/preview | Cloud blog 224991B (`d77a62…`): JSON-LD `datePublished 2026-10-21`, rendered `October 22, 2026`, `first_published 2026-10-22T04:10` | PARTIAL_PRIMARY_READ (raw + meta) | `blog dated Oct 22 (RSS Oct21)` + missing preview → `JSON-LD Oct21 / displayed Oct22 / first_published 04:10; rolling private preview to select enterprise (NOT GA); ZDR + Confidential Compute coming soon; published_at NULL date precision` | FIXED |
| W43-IA-002 | P1 | Flint 512K/256K | Article 366583B (`ce42b7…`) + card 6250B (`432443…`) | PARTIAL_PRIMARY_READ | `262144 ctx` as max → `up to 512K / recommend 256K / config 262144 distinct; 125+ M4 Pro MacBook Pro / 150+ 64GB RTX Spark short-context 128K-avg prefill-excluded (*Muse124K, 2x)`; split fused URL to 2 supplements | FIXED |
| W43-IA-003 | P1 | DeepInfer env | environ.py 8738B (`fe2c53…`) + README 4660B + LICENSE 11357B at `9bd9cf24…` Oct21; repo OUT Oct16 vs IN Oct20 | PARTIAL_PRIMARY_READ (code) | `ENABLE_MTP_VARLEN / NEXTN_DECODE d5` → `DEEPINFER_ENABLE_MTP_VARLEN=1, DEEPINFER_USE_NEXTN_DECODE default5 0-disables` pinned | FIXED |
| W43-IA-004 | P1 | GitHub enum | Changelog 107700B (`be7fab…`) datePublished `2026-10-23T23:42:03Z` | PARTIAL_PRIMARY_READ | `user/auto/product/other/unknown` → `user_selected/auto/product_selected/other/unknown; enterprise/org/enterprise-user/org-user 1-day/28-day; request_count=model requests NOT prompts; best-effort integration ID not verified identity` | FIXED |
| W43-IA-005 | P1 | FLUX math | Model 326207B (`9e8ddf…`) + blog 225919B (`50ac7d…`) | PARTIAL_PRIMARY_READ | `10.95 vs277.80=22x /12.45s` → `10.95/277.80=25.37x PR vs 12.45/277.80=22.31x page~22x correct; blog 26.5x/96.2% inconsistent on same inputs (true95.52%); Elo1139 vendor-cited AA unfetched; no fastest headline` | FIXED |
| W43-IA-006 | P1 | Patch model | Rendered 3210B (`f70ef5…`) RENDERED_TEXT (curl 9946B spinner); Oct21 | PARTIAL_PRIMARY_READ (rendered) | `GPT-6 Sol` + pseudo-locator → `GPT-5.6 Sol` + authentic `.../coordinated-disclosure-of-critical-vulnerabilities/` bound; 5-stage + Wiz/Cloudflare + $1B + checker skill; zero CVE; vendor disclosure≠CVE proof; RENDERED_TEXT labeled | FIXED |
| W43-IA-007 | P1 | MemT license | README 10170B (`5d576f…`) at `e75c13d0…` Oct20 + paper 7096280B | PARTIAL_PRIMARY_READ | `license via paper source_ids / PDF license sections` → `paper CC BY-NC-SA4.0 vs software PolyForm1.0.0 vs MIT third-party vs excluded weights/data per README; paper has NO terms; 1.86x/66x baselines bounded` | FIXED |
| W43-IA-008 | P1 | Independent-eval wording | Bio + lowresource + Ming pages/README (Discovery src-1; no new supplement needed for wording) | PARTIAL_PRIMARY_READ | `Independent technical evaluation / Independent eval methodology / independent #1 robustness` → `research-team evaluation protocol / coauthored blinded expert preference (75% distributed) / publisher reporting third-party leaderboard; wet-lab unvalidated; AA unfetched; independent repro ZERO` (Views + Card limitations) | FIXED |
| W43-IA-009 | P2 | Kimi/Flint fused URL | Kimi blog 390347B (`86cc8b…`) + X raw 208731B; Flint article+card above | PARTIAL_PRIMARY_READ | Fused single `sources[0].url` → split supplements (Kimi blog separate from X 17:15:24Z 4h44m36s; Flint article separate from card); `2.8T/104B X-only not blog; weights Nov4 FUTURE` | RESOLVED |
| W43-IA-010 | P2 | Oracle/AMBench delta | v2 PDFs bound (261750B + 2379235B); v1→v2 full diff NOT line-read | METADATA_ONLY | `v2 revision event` retained with explicit `UNRESOLVED substantive delta; CONTEXT bibliography; no W43 new-research promotion` | UNRESOLVED_DEFERRED_WITH_RATIONALE |
| W43-IA-011 | P2 | Duet/1Password live | Announcement + 1Password blog (Discovery src-1; wording fix, no new raw) | PARTIAL_PRIMARY_READ | `6000+ connectors / coming soon / rolling-out` → `catalogue vs live inventory split; 1Password coming soon not live; approval + no-password/OTP + plan scope bounded; behaviour unreproduced` | RESOLVED_WITH_LIMITATION |
| W43-IA-012 | P2 | Nemotron/Ming/DeepInfer/MOSS licenses | Nemotron card 59009B OpenMDW-1.1; Ming README 74543B + LICENSE 1067B MIT at `028c1ea…`; DeepInfer LICENSE above; Kohaku LICENSE 12141B custom at `da5dd97e…` | PARTIAL_PRIMARY_READ | `OpenMDW-1.1 / MIT / Apache-2.0 / Kohaku License` → `README terms vs LICENSE bytes vs OSI vs weight/data split; OpenMDW OSI UNVERIFIED; commercial/OSI withheld; baselines vendor-labelled` | RESOLVED_WITH_LIMITATION |
| W43-IA-013 | P2 | Auto/MOSS chronology | Auto-mode 599884B (Aug7 OUT vs Oct22 IN); MOSS dates | PARTIAL_PRIMARY_READ | `original 08-07 / 10-22 update; report OUT vs announce IN; README line vs deployment` → `Aug7 OUT / Oct22 IN / next-week FUTURE; Oct16 base OUT vs Oct18 trainer / Oct19 announce / Oct20 API-mention IN; event_types split; platform page metadata-only` | RESOLVED |
| W43-IA-014 | P2 | Grok + 7 projections | X raw 13425B SHA `4571e0de…`; ledger 7 mapped/25 passthrough | SECONDARY_OR_X_ONLY | `COMPLETE → PARTIAL sensor; 2 pinned IDs; 7 projections SOCIAL/SECONDARY not primary; paper only via PDF; binder NON_MATERIAL NEVER_STORY` | RESOLVED |
| W43-IA-015 | P2 | r2 metadata errata | Supplement JSON (6 not 8); Tree `b8e1a207edb3cc82927284241e486ce468360642` | REPORT_ONLY | Preserve history; erratum in history/r2/README + closure; r1/r2/handoff immutable | RESOLVED |

P1 8/8 FIXED (Stage-blocking cleared factually; trusted advancement still requires independent Sol re-audit, not Core PASS alone). P2 7/7 disposed (3 RESOLVED, 2 LIMITATION, 2 DEFERRED with rationale). No fake closure.

## Regeneration boundary

Edition-local only: supplement-r3 (21), compat-package-r3 + ledger-r3 + interactive-r3, Evidence `dbc27cd8…` (32 PARTIAL), Views `7a812053…` (20/11/1), ledger `31929cf5…` (51), completeness `abd6dadf…` (LIMITED). r1/r2 accepted dirs, Discovery/Screening/X Raw, Frozen Core/main, State, Checkpoints, Human Gates immutable. History/r2 snapshots canonical r2 ledger/completeness + README/SHA256SUMS.

## Shared-Core implication

- Canonical ledger non-DROP rationale remains frozen tautology by Core design; editorial basis in `w43-evidence-r3-materiality-rationale.md` + View rationales. This is a Core expressiveness gap, not an edition defect; no Core edit made (#569 context).
- Negative/semantic checks are schema-only except arithmetic/env-enum/license/string exact-match audits (FLUX 25.37/22.31, DeepInfer literals, GitHub literals, GPT-5.6, datePublished vs displayed). Core PASS is integrity, not scientific corroboration.
- Execution-record validator flags pre-existing Sol review heading gaps (r2 provenance, adjudication); new Muse docs carry required headings; no new failures added.

## 32-row semantic diff (r2 → r3)

- Cards CHANGED 20 (all P1 + Kimi/Duet/1Password/Nemotron/MOSS-trainer/automode/MOSS-report/API/Grok wording/split), SAME 12 (oracle/ambench claims same, decisions/tanstack/eleven/voxtral/deprecation/teams/deepseek/securing/vercel + muse-lead/carry/grok? actually Grok Card changed; 12 sames are mechanical hash/basis only).
- Views CHANGED 32/32 (all rationales editorially rewritten from tautology-adjacent to proof/novelty/IN-OUT basis; statuses 20/11/1 unchanged).
- Statuses: Cards 32 PARTIAL (no VERIFIED — zero independent repros by design); Views MATERIAL 20 / CONTEXT 11 / NON_MATERIAL 1; Ledger 20/11/1/19; Completeness LIMITED (LIMITATION/LIMITATION/SATISFIED).

## Literal/number regression checks (exact-match)

- `277.80/10.95=25.37`, `277.80/12.45=22.31`, page `22x` correct, blog `26.5x/96.2%` inconsistent — preserved, not silently resolved.
- `DEEPINFER_ENABLE_MTP_VARLEN`, `DEEPINFER_USE_NEXTN_DECODE default 5`, `0 disables` — exact code match at `9bd9cf24`.
- `user_selected/auto/product_selected/other/unknown`, `request_count=model requests NOT prompts`, `best-effort integration ID` — exact changelog match.
- `GPT-5.6 Sol` — exact rendered match; `GPT-6 Sol` zero occurrences in r3 Cards/Views.
- `datePublished 2026-10-21` vs `October 22, 2026` vs `first_published 2026-10-22T04:10` — all three stated, `T00:00Z` zero occurrences in r3 supplement/Cards.
- `512K / 256K / 262144` distinguished; `private preview to select enterprise` + `coming soon` ×2 present; `CC BY-NC-SA 4.0 / PolyForm Noncommercial 1.0.0 / MIT / OpenMDW-1.1 (OSI UNVERIFIED)` exact.
- Fused single-source ` + primary:` remains only in immutable Discovery src-1 locators (Kimi, Flint); r3 Cards bind ≥2 sources (Flint 3, Kimi 2, DeepInfer 4, FLUX 3, Patch 2, MemT 3, Ming 3, etc.); supplements contain zero fused URLs.

## 51 reconciliation + 12 carries + errata + gaps

- 51 rows: 20 MATERIAL / 11 CONTEXT / 1 NON_MATERIAL (Grok) / 19 EXCLUDED; 1:1 task mapping for 32 non-DROP; DROP reasons preserved; 12 carries (11 DROP + 1 CONTEXT) explicit.
- Errata (IA-015): r2 supplement 6 not 8; r2 starting Tree `b8e1a207edb3cc82927284241e486ce468360642` (not truncated `...3612`); history preserved.
- Residual UNVERIFIED: AA originals (FLUX/Ming/Eleven), Oracle/AMBench v1-v2 deltas, Patch original HTML (RENDERED only), OpenAI bio/lowresource byte archives (Discovery src-1 only), weight blob hashes, per-connector live status, client attribution, wet-lab, independent benches/speeds (ZERO repros).
- Reader risks: vendor numbers/benchmarks/speeds unreproduced; contradictory FLUX multiples must not be headlined as fastest; preview/coming-soon must not be read as GA/live; licenses must not be read as OSI/commercial proof beyond text; X signals must not be read as verified facts; paper dates must not be read as new W43 research where revision-only.

## Validators (frozen, with agent-first override where State-basis required)

- Supplement-r3 21/21 bytes+SHA PASS; compat-package-r3 basis PASS (7 projected/25 passthrough); interactive-r3 32/32 PASS.
- Evidence accept `dbc27cd8…` 32/32 Card PASS; Views accept `7a812053…` 32/32 PASS; ledger `31929cf5…` PASS; completeness `abd6dadf…` PASS (schema + profile/state + exec-record structure).
- Adapter tests 5/5 (frozen); negatives fail-closed (tampered byte_count, wrong binding, invalid projection, forged acceptance, missed Screening row, missing PDF; fused-URL semantic split verified with Discovery-immutability noted).
- Stage precheck `CANDIDATES_NORMALIZED→EVIDENCE_REVIEWED` to `/tmp/w43-r3-stage-precheck.json` PASS (state untouched, still `CANDIDATES_NORMALIZED`/pending, Gates pending). No operator request, no Issue #448 comment.
- Core PASS is schema/integrity only; factual closure above is independent-audit repair, not Core proof.

## New acceptance

- Evidence `sources/2026-W43/evidence/v2/accepted/dbc27cd8d5323c802bfb77c6fb4d6c917ba745417191da945c5ae8dbbdbad900/evidence-accepted.json` SHA256 `061c2233…` (32 PARTIAL).
- Views `sources/2026-W43/evidence/v2/views/accepted/7a8120533d6f666fb744303d8f828b680b4d8b6bc386ddf6904b6dee9e88963e/edition-views-accepted.json` SHA256 `5c3740ec…` (20/11/1).
- Ledger `sources/2026-W43/materiality-ledger-v2.json` SHA256 `31929cf5…` (51 rows).
- Completeness `sources/2026-W43/profile-completeness-v2.json` SHA256 `abd6dadf…` (LIMITED).
