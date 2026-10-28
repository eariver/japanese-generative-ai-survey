# Muse W43 Selection + proposed Architecture depth review r1

Status: `PROPOSED_FOR_SOL_AUDIT / NO_STAGE_ADVANCE / NO_HUMAN_APPROVAL`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. State `EVIDENCE_REVIEWED` (selection pending, architecture pending, Gates pending). Frozen Core unchanged.

## Reviewed authority

- Trusted bridge `bridge-runs/sol-w43-evidence-r4-advance-20261025/receipt.json` (ADVANCE `CANDIDATES_NORMALIZED→EVIDENCE_REVIEWED` PASS 2026-10-25T07:07:42Z on r4 authority; checkpoint `CANDIDATES_NORMALIZED.json`).
- Sol r4 acceptance `reviews/sol-w43-evidence-r4-postcutoff-independent-acceptance-20261025.md` (PASS_WITH_LIMITATIONS, NOT Human Gate; Metrics OUT, 20/10/2, 19/13 erratum, 4 rehashed raws).
- r4 authority: Evidence `fb6e5900…` (32 PARTIAL), Views `482a084e…` (20/10/2), ledger (20/19/10/2, Metrics MAYBE→NON_MATERIAL), completeness LIMITED, supplement-r4 25 (11 NULL, 0 `T00:00Z`), compat-r4 `8c5bebb5…`.
- r4 proof/crosswalk/diff from prior session; r1/r2/r3, Discovery/Screening, State/Checkpoints, Core/main/Gates immutable.

## Human decision

- NONE. No Human Architecture/Publication approval requested, recorded, or inferred. Review summary is `READY_FOR_ARCHITECTURE_REVIEW` (validator state), NOT a Human decision. No `ADVANCE_STAGE`, invalidation, revision, Draft, PDF.

## Requested changes

- None executed. This is a proposal for independent Sol audit. If Sol REQUEST_CHANGES, a new bounded contract will follow; no silent rework here.

## Regeneration boundary

- No regeneration executed beyond this proposal. All 6 outputs are new content-addressed edition-local files (matrix/selection/architecture/summary/attention + archived input/audit). No overwrite of prior authority (canonical paths did not previously exist — verified before run).

## Shared-Core implication

- Frozen Core unchanged (`scripts/`, `schemas/`, `config/`, `.github/`, `AGENTS.md` untouched; issues #568/#569 remain OPEN). All validations are genuine native calls (matrix/selection/architecture/summary/attention + stage scratch precheck). Core PASS = schema/integrity + disposition/placement/basis rules only; content correctness (clocks, licenses, benchmarks, fused-URL avoidance) is editorial proof below, not Core proof.
- Naive MAIN_EVENT Metrics or SELECTED Metrics/Grok would PASS some narrow schema checks in isolation but FAIL the exact validators used here (NON_MATERIAL SELECTED rejected; non-selected placement rejected) and — decisively — the editorial supersession requirement. A Core PASS without the explicit OUT/provenance chain must never be read as story approval.

## 32-row disposition (SELECTED 19 / HOLD 1 / REJECT 12)

Basis: Discovery decision/reason + r4 Card claims/View rationale + ledger disposition. Roles: SELECTED → PRIMARY/SUPPORTING + `WEEKLY:` architecture_role (publication_role None, W42 precedent); REJECT/HOLD → NONE/None/None.

| Discovery | Scr | View | Disp | Use | Role | Rationale (positive + negative, gate where HOLD) |
|---|---|---|---|---|---|---|
| w43-primary-duet-20261021 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:agent-systems | Proactive agent + credential architecture + safety stack; vendor-described, per-connector live unverified — bounded |
| w43-r2-1password-20261022 | KEEP | MATERIAL | SELECTED | SUPPORTING | WEEKLY:agent-systems | Approval-gated injection, no-secrets; live/rolling/coming-soon + plan scope stated, no functional test |
| w43-primary-automode-20261021 | KEEP | MATERIAL | SELECTED | SUPPORTING | WEEKLY:agent-systems | Oct22 IN (Aug7 OUT), next-week FUTURE, classifier untested; binds Duet approval |
| w43-primary-kimi-20261023 | KEEP high | MATERIAL | SELECTED | PRIMARY | WEEKLY:open-weights | X 17:15:24Z IN + 1M ctx + vendor benches + cyber removal; weights Nov4 FUTURE, no local run, 2.8T X-only |
| w43-r4-flint-20261021 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:open-weights | 39.8B/2.5B, 512K/256K/262144, Eureka + quant, benches + speed apparatus vendor-only, Apache-2.0 |
| w43-primary-nemotron-e4b-20261023 | KEEP high | MATERIAL | SELECTED | SUPPORTING | WEEKLY:open-weights | Compact + 07:00Z/commits IN + OpenMDW (OSI unverified) + Gemma Apache-2.0; efficiency/license comparator |
| w43-primary-deepinfer-20261020 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:inference-infrastructure | OSS cut + exact env vars at 9bd9cf24 + kernels + hardware + benches + non-inclusions; no independent run |
| w43-r2-memt-20261019 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:inference-infrastructure | MoS + 34B + 1.86x/66x + SGLang + license split (paper≠software); equations not line-read, no repro |
| w43-primary-flux-max-20261019 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:video-generation | Speed contradiction preserved (25.37 vs 22.31 vs 26.5x), Elo vendor-cited AA unfetched, pricing; no fastest headline |
| w43-primary-voxtral-20261020 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:speech-systems | Family + WER/diarization/recall + sub-500ms + TTS judge + pricing/endpoints/SDK; vendor evals, AA unfetched |
| w43-r2-ming-20261019 | KEEP | MATERIAL | SELECTED | SUPPORTING | WEEKLY:speech-systems | Open MIT + tasks + AA cited ranks (unfetched) + roadmap pending + month-only dating |
| w43-primary-eleven-20261020 | KEEP | MATERIAL | SELECTED | SUPPORTING | WEEKLY:speech-systems | Realtime + protocol compat + vendor AA + TTFA vendor-measured; SDK rework, guide unopened |
| w43-primary-patch-planet-20261021 | INSPECT→MATERIAL | MATERIAL | SELECTED | PRIMARY | WEEKLY:security-safety | GPT-5.6 Sol + 5-stage + Wiz/Cloudflare + $1B + checker + zero CVE (report≠proof); rendered-only, no vuln repro |
| w43-r2-openai-securing-20261023 | KEEP high | MATERIAL | SELECTED | PRIMARY | WEEKLY:security-safety | Containment + red-team + safety gating; page day-only + RSS 10:00Z secondary; vendor-described |
| w43-r2-openai-bio-20261021 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:scientific-evaluation | Team protocol + blinded 75% + wet-lab pending (ZERO repro); dataset/code team provenance |
| w43-r2-openai-lowresource-20261019 | KEEP | MATERIAL | SELECTED | PRIMARY | WEEKLY:scientific-evaluation | we/our protocol + MultiLangBench + COBOL parity + open suite (release≠repro); vendor tables, hidden tests held |
| w43-primary-decisions-api-20261022 | INSPECT→MATERIAL | MATERIAL | SELECTED | PRIMARY | WEEKLY:developer-tooling | GA Oct22 + 400Q + caching + GPT-Live + pricing/ZDR + 10x vendor + anecdotes bias; main page not archived |
| w43-primary-tanstack-20261023 | KEEP | MATERIAL | SELECTED | SUPPORTING | WEEKLY:developer-tooling | Stable core vs 0.x harness + codemod; product Oct22 IN vs blog UNRESOLVED (separate events) |
| w43-primary-deepseek-1017-20261017 | KEEP | MATERIAL | SELECTED | SUPPORTING | WEEKLY:developer-tooling | 1017 snapshot + demos + MIT weights/converts + Harness + Search/Fetch pricing + DeepSWE/HLE; SHA/billing untested |
| w43-r2-moss-trainer-20261018 | KEEP | MATERIAL | HOLD | NONE | None | HOLD: third-party single-run (HostAccumulator, 117.7s vs 8.8s, custom license, no independent GPU/VRAM). Gate: independent measurement + release scope. Narrative withheld. |
| w43-primary-github-metrics-20261023 | MAYBE low | NON_MATERIAL POST_CUTOFF | REJECT | NONE | None | REJECT: 23:42:03Z OUT +1h42m03s; facts preserved + supersession; W44 pointer only; MAYBE retained as history |
| w43-r4-grok-x-ledger-20261024 | MAYBE | NON_MATERIAL OTHER | REJECT | NONE | None | REJECT: audit binder NEVER story; COMPLETE/PARTIAL, 2 pinned IDs, no inflation |
| w43-carry-7151fcdc6c3ee392 | MAYBE | CONTEXT | REJECT | NONE | None | X-only support signal, no depth |
| w43-lead-muse-10m-20261021 | MAYBE | CONTEXT | REJECT | NONE | None | Secondary-only adoption, no primary books |
| w43-lead-oracle-revision-20261021 | MAYBE | CONTEXT | REJECT | NONE | None | v2 revision only, delta UNRESOLVED — bibliography |
| w43-primary-github-deprecation-20261019 | MAYBE | CONTEXT | REJECT | NONE | None | Changelog-level deprecation, ops hygiene |
| w43-primary-github-teams-20261023 | MAYBE low | CONTEXT | REJECT | NONE | None | IN 21:29:58Z but changelog-level only; lane covered by Decisions/TanStack/DeepSeek — withheld anti-padding |
| w43-primary-openai-cloud-20261021 | INSPECT | CONTEXT | REJECT | NONE | None | Distribution preview, not a model; thin for capability article |
| w43-r2-ambench-v2-20261020 | MAYBE | CONTEXT | REJECT | NONE | None | v2 revision only, delta UNRESOLVED — bibliography |
| w43-r2-moss-api-20261020 | MAYBE | CONTEXT | REJECT | NONE | None | README mention only, no deployment proof |
| w43-r2-moss-report-announce-20261019 | MAYBE | CONTEXT | REJECT | NONE | None | Announcement of OUT body — bibliography |
| w43-support-vercel-ollama-20261017 | MAYBE low | CONTEXT | REJECT | NONE | None | Composite Oct17+Oct23, no unified timestamp; distribution trace only |

19 DROP excluded from Matrix/Selection (19 EXCLUDED ledger rows verified individually); 12 W42 carries 11 EXCLUDED + 1 CONTEXT (`7151fcdc…` REJECT above, disposition preserved).

## Per-package depth map (8 packages, target 30 / max 34, est 29.0)

- **P1 open-weights (Kimi P + Flint P + Nemotron S, order 1, 5.0pp)**: question —開放の規模と手元の実行可能性をどう両立させるか. Must-cover: MoE configs/ctx/training/benches/availability/pricing above; comparison table Kimi-vs-Flint-vs-Nemotron (params/active/ctx/weights/license). Boundaries: Nov4 FUTURE, vendor harnesses, 2.8T X-only, OSI unverified, speed vendor-measured. Backing: 3 first-party bodies (Kimi blog 390KB + X raw, Flint article 366KB + card, Nemotron page/commits) + HF/API metadata; absences: weight blobs, independent runs, full bench repros.
- **P2 infra (DeepInfer P + MemT P, order 2, 4.0pp)**: question —推論切出しと持続記憶の機構条件とは. Must-cover per depth review above + mechanism figure/table; boundaries vendor-only + equations unread + license limits. Backing: environ.py/README/LICENSE bytes + paper PDF + README license section; absences: independent serve/measure, patent scope.
- **P3 agent (Duet P + 1Password S + Automode S, order 3, 4.0pp)**: question —資格に触れず働く条件. Must-cover per above + permission diagram; boundaries live/repro/FUTURE. Backing: announcements + 1Password blog + auto-mode article/X; absences: per-connector live, behavioural repro, classifier test.
- **P4 video (FLUX P sole, order 4, 2.5pp)**: question —速さの見出しをどう疑うか. Must-cover arithmetic + Elo/pricing + platform; boundaries AA/PR-origin/no-fastest. Backing: model page + blog + PR note; absences: AA original, independent timing.
- **P5 speech (Voxtral P + Ming S + Eleven S, order 5, 3.0pp)**: question —様式別の合成・認識を何で比べるか. Must-cover per above with eval/AA tables attributed; boundaries vendor-judge/AA-unfetched/no-e2e. Backing: vendor announcements + README + blog; absences: AA originals, migration guide, independent run.
- **P6 security (Patch P + Securing P, order 6, 3.5pp)**: question —見つけて直す協調と囲う訓練. Must-cover 5-stage + $1B + checker + containment/red-team/gating with RSS caveat; process figure; boundaries rendered-only/vuln-unverified/RSS-secondary. Backing: rendered article + RSS + research page; absences: original HTML, independent vuln/patch confirmation.
- **P7 science (Bio P + Lowresource P, order 7, 3.0pp)**: question —手順・盲検・hiddenをどう読むか. Must-cover protocols/denominators/artifacts/limits tables; boundaries team/internal/sample/hidden/cost. Backing: research pages + bioRxiv/HF/GitHub + open suite; absences: wet-lab, external replication, billing audit.
- **P8 devtooling (Decisions P + TanStack S + DeepSeek S, order 8, 2.5pp)**: question —判断のAPI化と道具・配布の条件. Must-cover per above + API/migration tables; boundaries latency-bias/unarchived/harness/SHA-billing/blog-gap. Backing: changelog + release/npm + docs; absences: main page bytes, migration test, hash/billing proof, blog clock.
- No empty placeholder package (all 8 have ≥1 PRIMARY; at most one empty PRIMARY/SUPPORTING allowed and unused). Draftable cross-package synthesis permitted only if validator allows (none inserted — no padding).
- Descriptions are reader-facing Japanese (proposed titles/purposes in input are Japanese); technical identifiers stay in English/standard loanwords; Sino-Japanese neologisms avoided.

## Claim → true primary source (no fused URLs; rendered vs bytes; vendor vs independent)

- Metrics: `src-1` (Discovery day-precision, history) + `supplement-src-1a8d33ae41ab22ad` (changelog 107700B, 23:42:03Z) — reader cites supplement + JSON-LD excerpt; technical facts VENDOR, OUT verdict primary.
- Teams: `src-1` + `supplement-src-52dba048e55beefa` (Teams HTML 105311B, 21:29:58Z vs modified 23:46:48Z) — REJECT from narrative but clock IN preserved in Evidence (anti-padding rationale documented).
- Kimi: X-leg facts → `src-1` X part (208731B raw, 17:15:24Z); blog facts → `supplement-src-041ec6c5600beb4d` (390347B, DATE_ONLY null) — `2.8T/104B` X-only, `1M` blog; weights FUTURE.
- Nemotron: page/card facts → `src-1` + `supplement-src-9e10348cb212038f` (card 59009B, DATE_ONLY null); commits 15:12–19:03Z → `supplement-src-deae3d33c374f4eb` (1307B) — IN rests on latter + page 07:00Z.
- Flint: article facts (512K/256K, speed apparatus) → `supplement-src-d2d2f48e181fb4dd` (366583B); card facts (39.8B/2.5B, 262144, Apache-2.0) → `supplement-src-e1fe975d225aaa88` (6250B); `src-1` retained internally as `DISCOVERY_ONLY_NOT_CITABLE`.
- TanStack: product facts → `supplement-src-22fcccb239a19447` (GH release 27590B, 15:18:14Z Oct22); blog day-only → `src-1` + DATE_ONLY null (no clock claim).
- Securing: containment facts → `src-1` (page day-only); hour 10:00Z → `supplement-src-7648a293320fac45` (RSS 803075B, secondary provenance labeled).
- Patch: RENDERED_TEXT facts → `supplement-src-fe148ca1b75a67dd` (3210B rendered; curl 9946B spinner only, NOT original HTML) + `src-1`; GPT-5.6 Sol verbatim; zero CVE.
- DeepInfer: literals → `supplement-src-e20f1cffc1444d3a` (environ.py 8738B @9bd9cf24) + `supplement-src-d0805b13331ce793` (README) + `supplement-src-d818147e4521ac7a` (LICENSE); repo OUT/IN split noted.
- MemT: paper facts → `supplement-src-927931f4a303eaa6` (paper 7096280B, no license terms); license facts → `supplement-src-baee90a6382ccdbd` (README 10170B @e75c13d: paper CC BY-NC-SA vs software PolyForm vs MIT vs excluded).
- Ming: README facts + `supplement-src-1d329e6cfb492783` (74543B @028c1ea) + LICENSE `supplement-src-5bb55c72ae60d4a2` (1067B MIT); AA ranks vendor-cited, pages unfetched.
- Duet/1Password/Automode/Decisions/Bio/Lowresource/DeepSeek/Voxtral/Eleven: `src-1` (+ existing r2/r3 supplements where bound: automode `6f18…`, decisions `2a49…`) with vendor/author vs independent-repro caution in prose; no new fused URL created (supplement-r4 has zero fused URLs; fused `src-1` locators for Kimi/Flint flagged `DISCOVERY_ONLY_NOT_CITABLE`).
- Grok: `src-1` only (X raw 13425B); NEVER cited as story.

## Residuals / thin-section warnings

- 5 LIMITED carried (GCP date conflict, Kimi/Flint fused refs, Oracle/AMBench deltas, Duet/1Password live integration, licenses/weights-OSI) — no P1 escalation without new conflicting primaries; prose carries explicit limits.
- Missing: AA originals (FLUX/Ming/Eleven), Oracle/AMBench full v1→v2 diffs, deployment restrictions (Teams plans, Duet plans, 1Password plans), subjective evals (testimonials, blinded 75% team estimate), Grok provenance, Kimi/Flint fused-locator hygiene, TanStack blog clock, Securing page clock, Vercel composite dating.
- Thinnest packages without full bodies: P4 (single-source methodology critique — acceptable as critical reading, not a roundup), P5 Eleven leg (vendor AA via blog, guide unopened), P8 DeepSeek leg (SHA/billing untested). If Sol finds any package content-starved, the honest repair is HOLD/REJECT demotion (e.g., DeepSeek→HOLD, Teams stays REJECT), not padding.
