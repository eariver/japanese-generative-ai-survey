# Survey Production execution index — 2026-W42

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W42/production-state.json`.

## Current authority

- Issue / edition: `2026-W42`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W42-v2-work`
- Start-of-run reviewed `main`: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`
- Run started: `2026-10-17T06:33:00Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W42/production-profile.json`
- Production State: `sources/2026-W42/production-state.json`
- Current State SHA-256: see authoritative `sources/2026-W42/production-state.json` (updated r5; earlier snapshot in index was stale)
- Current lifecycle: `DRAFT_COMPLETE` (r10 Human Architecture r1 APPROVED recorded via frozen Gate; Japanese Draft JSON v10.0 validated; Sol Draft audit pending)
- Current terminal reason: `none`
- Current next action: `SOL_W42_JAPANESE_DRAFT_REVISION_R11_AUDIT` (independent Sol re-audit of r11 PROPOSED editorial repairs before any TeX/PDF)

## Human Gates

- Architecture Review: `approved` (r1, Human Owner, 2026-10-18 JST basis; provenance `sources/2026-W42/gates/architecture-approval.json`)
- Publication Preview: `pending`
- Detailed review records: `sources/2026-W42/gates/reviews/architecture-r1.json` (+ immutable snapshot `gates/reviews/approvals/architecture-r1.json`, index `gates/review-index.json`)

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Latest Drive task-file path/reference: https://docs.google.com/document/d/1Skp9SMKhpDpxJCTXcJA1cepZZBTL8WKJbIU4HcLy_nc/edit (Sol Drive materialized 2026-10-17; Grok task document; result now returned separately; `execution/operator-handoffs/2026-10-17_w42-grok-x-drive-task-dispatch.md`)
- Latest result disposition: `RAW_RECEIVED_VERIFIED / CORE_DISCOVERY_ACCEPTED` — Google Drive result https://drive.google.com/file/d/1G505Nie7-EJDtysTQKzGLxiFNk2SFUPY/view, archived under `external/x/weekly-x-2026-W42/raw/weekly-x-2026-W42.md` (18 status URLs; 12,373 bytes; SHA-256 c48a7426e5c616e72045390938da4f4755b800b51ba08d09c0329d8034df5358). See `execution/reviews/sol-w42-grok-x-intake-r1-20261017.md`. X manifest and canonical Discovery/Screening accepted r5; Evidence and Views formally accepted r8.

## Deviations

- Muse r1: 2 transient websearch 429s (recovered; no material loss). X/Grok Drive lane PARTIAL (leads only). All paper/license/benchmark bodies pending as explicit gaps (see completeness r1).

## Shared Core defects

- None recorded at initialization.

## Sessions

- `sessions/muse-w42-initial-20261017.md` (init + Source Intake + Discovery proposal r1; SOL_DISCOVERY_COMPLETENESS_REVIEW_READY candidate r1)
- `sessions/muse-w42-gapfill-20261017-r2.md` (Sol r1 REQUEST_CHANGES bounded gap-fill; proposal r2; REVIEW_READY candidate r2)
- `sessions/muse-w42-temporal-repair-20261017-r3.md` (Sol r2 temporal/provenance narrow repair; proposal r3; REVIEW_READY candidate r3)
- `sessions/muse-w42-evidence-prep-20261017-r4.md` (Discovery→Screening→Evidence-prep; acceptance BLOCKED on missing X manifest, proven; EVIDENCE_AUTHORITY_REVIEW_READY candidate r4)
- `sessions/muse-w42-grok-evidence-20261017-r5.md` (Grok intake COMPLETE → canonical Discovery+Screening acceptance → evidence executed; CANDIDATES_NORMALIZED; REVIEW_READY r5)
- `sessions/muse-w42-evidence-deepening-20261017-r6.md` (E42 authority gap-fill: 7 licenses, 8 paper/report bodies, 12 retries; 49 cards rebuilt 68→151 claims; REVIEW_READY r6)
- `sessions/muse-w42-selection-architecture-20261017-r9.md` (Sol r8 28/50 Selection + seven-package Architecture via frozen Core; two lawful bridge advances to ARCHITECTURE_ESTABLISHED; SOL_ARCHITECTURE_AUDIT_READY)

## Discovery review

- Sol Discovery Completeness Review r1: `REQUEST_CHANGES` (`execution/reviews/sol-w42-discovery-completeness-r1-REQUEST_CHANGES-20261017.md`); proposal r1 `discovery/discovery-v2-proposal-r1.jsonl` (39, PROPOSED_NOT_ACCEPTED, historical)
- Sol Discovery Completeness Review r2: `REQUEST_CHANGES` temporal/provenance (`execution/reviews/sol-w42-discovery-completeness-r2-REQUEST_CHANGES-20261017.md`); proposal r2 `discovery/discovery-v2-proposal-r2.jsonl` (49, PROPOSED_NOT_ACCEPTED, historical)
- Sol Discovery Completeness Review r3: `PASS_WITH_LIMITATIONS` (`execution/reviews/sol-w42-discovery-completeness-r3-PASS_WITH_LIMITATIONS-20261017.md`, with Grok X outstanding); proposal r3 `discovery/discovery-v2-proposal-r3.jsonl` (49: 46 unchanged, 3 temporal repairs, PROPOSED_NOT_ACCEPTED)

## Evidence prep (r4, provisional — acceptance blocked)

- Screening PROPOSED 49 (KEEP 28/INSPECT 16/MAYBE 5); evidence cards PROPOSED 49 (STRONG 23/PARTIAL 13/THIN 13, local shape); views PROPOSED 49; bundles r4 run `20261017T080000Z-muse-r4`
- Blocker: canonical Discovery acceptance fail-closed without X manifest (proven, 0 bytes); State stays ISSUE_INITIALIZED
- Sol Evidence Authority Review r4: pending (`execution/SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF-r4.md`)

## Canonical run (r5 — Grok received, acceptance chain green)

- X manifest `external/x/x-source-intake-v2.json` COMPLETE (PARTIAL/DISCOVERY_RECORDED → grok ledger; raw bytes match Sol audit)
- Canonical Discovery 50 (`discovery-v2.jsonl` + `discovery-accepted-v2.json`, graph 5818d9d2); canonical Screening 50 (`screening/v2/accepted/08738e09…`, KEEP 29/INSPECT 16/MAYBE 5)
- Lifecycle: CANDIDATES_NORMALIZED (discovery + screening passed); evidence executed 50 tasks, NOT accepted
- Sol Evidence Authority Review r5: `REQUEST_CHANGES` (`execution/reviews/sol-w42-evidence-authority-review-r5-REQUEST_CHANGES-20261017.md`): accepted Discovery+Screening preserved; current Evidence claims too compressed and primary license/PDF consumption missing; Muse r6 instructed via `execution/instructions/2026-10-17_muse-w42-evidence-authority-deepening-r6.md`.

## Evidence deepening (r6 — authority remediation, acceptances unchanged)

- 7 license investigations (2 full texts + 3 operative-terms + 2 tag-only); 8 paper/report bodies (PAT/Earth full-text, 3 wet-lab PDFs extracted, Nemotron report, Beam safety, Sakana/Amazon/Minecraft traced)
- 49 cards rebuilt (`execution/evidence-r6/evidence-cards-r6.PROPOSED.json`, 151 URL+kind-linked claims vs r4 68); views r6; gap matrix; depth audit; bundles r6 run `20261017T100000Z-muse-r6`
- Sol Evidence Authority Review r6: `RESEARCH_DEPTH_PASS_WITH_REPAIRS` (`execution/reviews/sol-w42-evidence-authority-review-r6-CONDITIONAL-PASS-20261017.md`); r7 executed below.

## Precision repair + conditional acceptance attempt (r7 — blocked without waiver)

- Unit A repairs complete (`execution/evidence-r7/`: cards/views/correction ledger; 22/22 sources fixed verified; EDITORIAL/X_OBSERVATION kinds; per-claim authority; reconciled limits/targets; 48/1 states; OSI scoping; 49 substantive views)
- Unit B BLOCKED by two proven Core guards: CV2-W42-001 (prepare-vs-advanced-state; reproduces on W41 RELEASED) + CV2-W42-002 (17 source_type vocabulary); defects under `execution/defects/`; accepted chain + State + Gates preserved; no waiver/bypass/mutation
- Unit C provisional (from unaccepted evidence): materiality PROPOSED (28/14/7/1), completeness note (LIMITED), selection sketch (6-package + alternative + unselected-reasons + pages)
- Sol Materiality/Selection Review r7: pending (`execution/SOL_MATERIALITY_SELECTION_REVIEW_HANDOFF-r7.md`)
- `sessions/muse-w42-evidence-materiality-20261017-r7.md`
- `sessions/muse-w42-frozen-compat-selection-20261017-r8.md` (Human no-Core-change compat: supplement + projection + 50/50/50 acceptance + selection proposal; REVIEW_READY r8)

## r7 Core blocker and Sol recovery decision

- Muse r7 submitted 49 updated local Evidence cards (151 claims), 49 substantive Edition Views, provisional 28 MATERIAL/14 CONTEXT/7 HOLD/1 non-editorial and six-package sketch. **No Evidence Acceptance**; formal state remains `CANDIDATES_NORMALIZED`.
- Sol r7 independent audit: `execution/reviews/sol-w42-r7-core-blocker-and-editorial-authority-audit-20261017.md` (`STOP_CORE_EVIDENCE_ACCEPTANCE_BLOCKED / SOL_SELECTION_REQUEST_CHANGES`). Core source confirmed old vs agent-first State validation and 17 unsupported `source_type` entries; Core also requires **50** Evidence tasks/views (49 editorial + 1 Grok binder). Materiality reasons are template-derived, non-authoritative; editorial bundle links require correction.
- Proposed recovery: `execution/decisions/sol-w42-core-evidence-compatibility-recovery-proposal-20261017.md` — explicit Human decision pending for narrow separate Core-maintenance exception; **NOT an execution authorization**. Frozen Core unchanged, Human publication Gates untouched. Absolute freeze would leave W42 paused pending a demonstrated lawful adapter.

## r8 Human Core-freeze decision and Edition-local continuation

- Human directive documentation: `execution/decisions/2026-10-17_human-no-core-change-edition-local-continuation.md` (supersedes prior Sol maintenance proposal; NOT a Human publication Gate).
- Human Owner instruction (2026-10-17 JST): **Core v2 changes prohibited**; register new defects in GitHub Issues and the post-Freeze deferred inventory; use bounded edition-local compatibility and continue W42.
- Issue [#568](https://github.com/eariver/japanese-generative-ai-survey/issues/568) / new `CV2-DM-023`: direct legacy Evidence prepare helper rejects valid agent-first State; official frozen `survey_agent_tool_v2.current_stage_basis_override` exists for native validated compatibility (not yet W42 accepted).
- Issue [#569](https://github.com/eariver/japanese-generative-ai-survey/issues/569) / existing `CV2-DM-016` recurrence: 17/50 canonical Discovery source types need a strictly logged **derived Evidence Task only** classification projection. Accepted Discovery/Screening untouched.
- `docs/core-v2-deferred-maintenance-summary.md` updated to `r1.2` on W42 work branch, with both issues, OPEN_CORE statuses, guarded-stop notes and pending edition-local validation; no Core source edit.
- Muse r8 execution request: `execution/instructions/2026-10-17_muse-w42-frozen-core-compat-evidence-to-selection-r8.md` (native current-stage adapter, 50 Evidence Cards including 1 truthful non-editorial X binder, genuine Core validation/acceptance if possible, then candidate-specific Materiality and Selection proposals). Stop at independent Sol review or a real Core blocker.
- Muse r8 completed: supplement r8 (91 raws, validated) + compat package (50 tasks, 17 projections + ledger) + interactive input (50 records) → 50 Core cards + 50 views ACCEPTED (`f2429e27…`, `4296ffd0…`), materiality ledger, LIMITED completeness → bridge ADVANCE → `EVIDENCE_REVIEWED`. Selection proposal r8 (`selection-proposal-r8.PROPOSED.md`, per-candidate rationale, 20–24pp plan). Dossier: `SOL_MATERIALITY_SELECTION_REVIEW_HANDOFF-r8.md`. Human Gates pending. Core `774dd39a…` and main unchanged.

## Sol r8 independent Materiality/Selection review and r9 dispatch

- Official State after r8 is `EVIDENCE_REVIEWED`; Evidence/Views/Materiality/Completeness checkpoints PASS (50 Core Cards: 43 PARTIAL, 7 NEEDS_MORE; 50 Views; 28 MATERIAL, 14 CONTEXT, 7 HOLD, 1 non-editorial; Completeness LIMITED).
- Sol r8 independent audit `execution/reviews/sol-w42-r8-evidence-materiality-selection-semantic-review-20261017.md`: Core machine acceptance real; 91 source supplement files are bounded **derived excerpts, NOT 91 exact original-body archives**; many accepted card claims overbind all task source IDs and leave generic UNRESOLVED targets. Do not rewrite accepted Evidence; use edition-local audited claim→specific-URL crosswalk.
- r8 executor six-package proposal **NOT adopted**: Maia 300 silently omitted despite MATERIAL; Scion/Glimpse roles not consistently placed; page plan risks compression. Sol has reviewed all 28 MATERIAL + 14 CONTEXT + 7 HOLD + 1 Grok binder and directed a **seven-package** technically substantial ~27–30pp design (28 SELECTED: 16 PRIMARY + 12 SUPPORTING; 5 INSPECT; 7 HOLD; 10 REJECT).
- Next Muse execution contract `execution/instructions/2026-10-17_muse-w42-selection-through-sol-architecture-audit-r9.md`. Lawful frozen-Core Candidate Selection → seven-package Architecture candidate with exact stage validation; stop for `SOL_ARCHITECTURE_AUDIT_READY`. Human Architecture Review and Publication Preview remain pending; no Draft/TeX/PDF.

## r9 Selection + Architecture execution (Sol design materialized, audit pending)

- Interactive input `execution/interactive-selection-architecture-r9.json` (50 semantically specific rationales; Sol §3 roles exact; 28/5/7/10 asserted) → frozen `run_selection_architecture_v2_interactive` (agent-first override): `candidate-matrix-v2.json` (50) + `candidate-selection-v2.json` (ESTABLISHED, 28) + `architecture-v2.json` (PROPOSED, 7 packages P1–P7, target 28 / max 30) + `architecture-review-summary-v2.json` (READY_FOR_ARCHITECTURE_REVIEW, zero errors) + `architecture-review-attention-v2.json`.
- Direct frozen validators: `selection-check` PASS; `architecture-check` PASS. Accepted Evidence/Views/Materiality bytes untouched.
- Bridge `muse-w42-selection-advance-20261017` (event-sha = r9 start HEAD): CORE_STAGE_CONTRACT PASS → `SELECTION_COMPLETE` (checkpoint `EVIDENCE_REVIEWED.json`).
- Edition-local `claim-to-source-crosswalk-r9.md`: 117 selected claims with best exact URLs, categories, draft caveats; 18 high-risk focus rows; 0 NON_PROMOTABLE; 91 supplements recorded as derived excerpts.
- Bridge `muse-w42-architecture-advance-20261017`: CORE_STAGE_CONTRACT PASS → `ARCHITECTURE_ESTABLISHED` (checkpoint `SELECTION_COMPLETE.json`); Architecture PROPOSED with null human_review; gates pending/pending; machine terminal `HUMAN_GATE_REACHED` (wait state only).
- Session: `sessions/muse-w42-selection-architecture-20261017-r9.md`. Sol audit handoff: `SOL_ARCHITECTURE_AUDIT_HANDOFF-r9.md` (terminal `SOL_ARCHITECTURE_AUDIT_READY`). No Human approval recorded/requested; no Draft/TeX/PDF. Generic Issues #568/#569 remain OPEN_CORE.
- Generic frozen-Core issues #568/#569 remain OPEN_CORE even after r8 edition-local compatible pass.

## Sol r9 Architecture independent audit and full Human dossier

- Independent Sol auditor reviewed immutable Muse r9 commit `4a1cb6b9df5a7b64bacdcd881af201e7bf0d28a1`, machine `ARCHITECTURE_ESTABLISHED` and original accepted Core checkpoint bytes: `execution/reviews/sol-w42-r9-independent-architecture-audit-PASS_WITH_LIMITATIONS-20261017.md`.
- Verdict `PASS_WITH_LIMITATIONS / READY_FOR_HUMAN_ARCHITECTURE_REVIEW`: 50 Matrix + Selection (28 SELECTED/5 INSPECT/7 HOLD/10 REJECT), 28 uniquely placed as 16 PRIMARY/12 SUPPORTING in 7 packages, target 28pp (max 30); zero substantive candidate omission after Maia/Scion/Glimpse restoration. 117 selected claim entries mapped to 62 best URLs, but source excerpts are NOT original full archives; Evidence 43 PARTIAL/7 NEEDS_MORE/0 VERIFIED; Completeness LIMITED.
- r9 editorial provenance defect: 6 vendor-source claims misclassified as independently publishable; EXO source unfetched; 3 product facts misclassified as legal text plus mixed-source claim. Sol non-Core errata: `execution/reviews/sol-w42-r9-claim-provenance-editorial-errata-20261017.md`. Errata binding on Draft, one EXO external-evaluation claim nonpromotable as independent. Historical Muse r9 crosswalk preserved, accepted Evidence unchanged.
- Architecture Attention shows 50 of 51 notices due frozen display cap. Omitted notice is Qwen-Image Turbo REJECT, present in canonical Selection and Review Summary; fully surfaced in Human dossier.
- Human-facing full 12-part Architecture Review: `execution/reviews/sol-w42-r9-human-architecture-review-dossier-20261017.md`. **Human Architecture Gate still pending**. No Draft/TeX/PDF. Frozen Core/main unchanged.

## Human Architecture r1 explicit approval — Gate RECORDED + Draft ESTABLISHED (2026-10-18 JST)

- Human Owner verbatim: **“W42 Human Architecture ReviewをAPPROVEDとします。Solの出典訂正と品質条件を含めて正式Gateの承認処理を進め、Museの次工程を指示してください。”**
- Actual, scoped Human decision preserved: `execution/human-architecture-approval-basis-r1.md`, reviewed Human-presented commit `6dc71ec99b0a1ab2b623512f2e5820968c2b496d`; 7 packages / 28 selected / target 28 pp (max 30) **plus binding Sol r9 claim errata and technical quality guards**.
- Human decision was **APPROVED**, and canonical `gates/architecture-approval.json`, r1 review record/index and Production State `human_gates.architecture_review=approved` were GENERATED by frozen `survey_human_gate_v2.py record-architecture-approval`, validated (agent-state + schemas + snapshot-agreement PASS), committed (`be3a49eaa`) and non-force pushed. Substantive Japanese Draft JSON v10.0 followed (117 paragraphs, 6 tables, 7 notes) with 7/7 Draft Results ESTABLISHED + Synthesis validated; bridge `muse-w42-draft-advance-20261017` moved state to `DRAFT_COMPLETE`. Session: `sessions/muse-w42-r10-20261017.md`.
- Authorized Muse r10 `execution/instructions/2026-10-18_muse-w42-human-architecture-approval-and-japanese-draft-r10.md`: phase A authentic Human Gate r1 recording and intermediate commit/push; **only after PASS** seven-package substantial Japanese Draft JSON and Core Draft/Synthesis validation, possibly lawful `DRAFT_COMPLETE`; stop `SOL_W42_JAPANESE_DRAFT_JSON_AUDIT_READY`. **No TeX/PDF** or later Human Preview/Release.
- Frozen Core remains unmodified; #568/#569 remain deferred OPEN_CORE; no accepted source/evidence/selection/Architecture artifact rewritten.

## Sol independent Japanese Draft audit r10 — editorial REQUEST_CHANGES (2026-10-18 JST)

- Official machine `DRAFT_COMPLETE` and Human Architecture Gate r1 `approved` independently reconfirmed. All seven Core Draft Results `ESTABLISHED`; 117 PARAGRAPH, 6 TABLE, 7 NOTE; 21,418 paragraph-only Japanese/technical characters. Publication Preview pending, frozen Core/main unmodified; no TeX/PDF.
- Sol editorial verdict: `REQUEST_CHANGES / NO_TEX_PDF_AUTHORITY`. Main B01 **false blanket OSI claim** in P3 note (Apache 2.0 is OSI-approved); B02 seven machine `CLAIM_BOUNDARY` blocks leaked into reader preview with internal English trace; B03 systematic repetitive editor-instruction prose; B04 Hangul/Simplified contamination (`무制限`, `误検出`) and malformed terms; B05 editorial source-extraction status narrated as published research.
- Major M01–M05: P5 3-vs-4 safety taxonomy, overbound block references vs precise source URLs, thin/redundant manuscript relative to 28-page plan, appended-out-of-order paragraph IDs, GLM-Legal Vals evaluator and vendor chart attribution ambiguity. Source-r9 errata remains binding.
- Full independent review: `execution/reviews/sol-w42-r10-independent-japanese-draft-audit-REQUEST_CHANGES-20261018.md`. This is a **Draft editorial finding only**; does not revoke approved Human Architecture r1 or passed machine Draft checkpoint.
- Next Muse bounded r11: `execution/instructions/2026-10-18_muse-w42-japanese-editorial-repair-and-adoption-proof-r11.md`. Seven corrected substantive Japanese Draft Results as **PROPOSED** edition-local sidecars, clean reader preview, claim→primary-source corrections, exact frozen validator tests and lawful **DRAFT_COMPLETE adoption-feasibility** proof. Canonical Draft/State/checkpoints **unchanged** until separate legitimate integration, if one exists. Stop for Sol independent r11 re-review; no PDF or Core changes.
- Generic Core defects #568/#569 and frozen Core status unchanged.

## Sol independent r11 Japanese Draft re-audit — conditional editorial PASS and r12 preview plan

- Muse r11 current reviewed commit `7de15dc5f4288842fbda00d040e8e413ff0f8a63` created seven **edition-local PROPOSED** Draft Results (no canonical overwrite), seven tables, seven reader NOTES. 82 paragraphs / **17,004 paragraph-only characters**; all visible reader blocks plus tables/notes/headings ~20k chars. Frozen 7/7 Draft and Synthesis validators reported PASS, canonical State still `DRAFT_COMPLETE` with Human Architecture r1 APPROVED, Publication Preview pending.
- Sol independent review `execution/reviews/sol-w42-r11-independent-japanese-draft-audit-CONDITIONAL-PASS-20261018.md`: substantive readability improvement, no machine trace in reader preview, correct general Apache OSI status, P5 four局面, multilingual artifacts removed. **F01 residual licensing source-tier contradiction**: LFM treated as full license text when only operative terms read; Beam paragraph claims no attribution despite Apache redistribution requirements. **F02 seven invalid citation mappings** P4/P5/P6 to unrelated r6 OCP/Claude/Minecraft research bundle. **F03 technical density** 17k paragraph chars vs 26.5pp approved body; do not pad to 28pp.
- Frozen Core source inspection confirms direct amended r11 Draft checkpoint replacement BLOCKED (r10 SHA immutable) and canonical Weekly auto renderer tied to r10 archive, but generic `reader-manuscript` binds Architecture/approval/actual TeX rather than Draft paragraph bytes. Thus revised reader text can be authored into a future distinct TeX publication source WITHOUT claiming a new accepted Draft hash, **subject to all later exact Core Reader/QA gates**.
- Next Muse r12 contract: `execution/instructions/2026-10-18_muse-w42-r12-editorial-source-repair-and-noncanonical-tex-preview.md`; **fix F01/F02 first**, revalidate full seven reader-friendly proposals/citations, then only if clean build edition-local explicit **NONCANONICAL TeX/PDF preview** and visual/page-density proof for Sol. No official Stage advance or TeX/PDF Publication Preview approval; immutable canonical Draft, State, Gate, main and Core remain untouched.

## Grok X reconciliation continuation

- Sol archived exact returned Grok result, recorded 18-post to 7-candidate map, and issued `execution/instructions/2026-10-17_muse-w42-grok-through-evidence-r5.md`; r5 Muse completed and accepted Discovery+Screening.

## Final disposition

`SOL_R11_EDITORIAL_CONDITIONAL_PASS / MUSE_R12_SOURCE_REPAIR_AND_NONCANONICAL_TEX_PROOF_PENDING` (r11 substantial improvement but F01 licensing/F02 7 wrong refs/F03 page density remain; DRAFT_COMPLETE and Architecture Human APPROVED, publication pending; no validated PDF or stage advance)
