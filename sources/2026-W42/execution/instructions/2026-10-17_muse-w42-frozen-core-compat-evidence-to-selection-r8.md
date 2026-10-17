# W42 Muse r8 — Frozen Core unchanged: native agent-first Evidence admission + edition-local source projection → Selection review

Status: **`EXECUTION_AUTHORITY / HUMAN_APPROVED_NO_CORE_CHANGES / EDITION_LOCAL_COMPATIBILITY / STOP_AT_SOL_SELECTION_REVIEW`**  
Date: 2026-10-17 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Existing production branch only: `weekly/2026-W42-v2-work`

## 1. Exact authority / guarded start

Invocation message supplies the **exact remote W42 Starting HEAD and Tree**. In read-only preflight check both, plus reviewed `main` HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` (Tree `801de813319f08777ab1581a5e8875fc1ac5df19`) and frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` (Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`). Mismatch → **ZERO WRITES / report actual SHA and Tree**. No new, fallback, review or maintenance branch; no reset/rebase/force. Normal commits and non-force push to existing W42 branch only.

The Human Owner explicitly instructs **NO CHANGES to frozen Core v2**. Do not modify any shared `scripts/`, `schemas/`, `config/`, orchestration definitions, `.github/`, Core branches or main. Edition-local implementation under `sources/2026-W42/execution/` only. Preserve exact accepted W42 Discovery (50), Screening (50), all canonical checkpoints/State, the original 7 Daily X raw items and the Grok raw X file.

Mandatory read (in order):
- `sources/2026-W42/execution/reviews/sol-w42-r7-core-blocker-and-editorial-authority-audit-20261017.md`
- `sources/2026-W42/execution/defects/cv2-w42-001-evidence-prepare-state-basis.md` and `cv2-w42-002-evidence-source-type-vocabulary.md`
- [Issues #568 and #569](https://github.com/eariver/japanese-generative-ai-survey/issues/568); `docs/core-v2-deferred-maintenance-summary.md` sections CV2-DM-016/CV2-DM-023.
- `sources/2026-W42/execution/evidence-r7/` (49 proposed cards, substantive views and correction ledger), r6 first-party report/license/method bundles and unconsumed/partial source status; `materiality-r7.PROPOSED.json`, `completeness-r7.PROPOSED.md`, `selection-sketch-r7.PROPOSED.md`.
- Frozen first-party code: `scripts/survey_agent_tool_v2.py` (`current_stage_basis_override`, `verify_current_stage_basis`); `scripts/run_evidence_v2_interactive.py` (`run`); `scripts/survey_agent_control_v2.py` (`validate_agent_state`); `scripts/survey_evidence_v2.py` (`prepare_evidence_package`, `_source_class`, `validate_evidence_card`, `validate_evidence_package_basis`, `accept_evidence_results`, `accept_edition_views`, `build_materiality_ledger`); `scripts/survey_stage_validation_v2.py`; all applicable frozen schemas; previous accepted TS-001 DM-016 edition-local projection precedent and W41 accepted Evidence/Views methodology.

## 2. Crucial implementation discovery: first-party frozen Core ALREADY has the State adapter

Direct legacy `core.verify_state_basis` fails for agent-advanced State. **DO NOT invent a new generic monkeypatch, fake a legacy PASS, or bypass State integrity.** The unmodified frozen `survey_agent_tool_v2.current_stage_basis_override()` already binds `core.verify_state_basis` to **`verify_current_stage_basis`**, requiring true current work-tree implementation SHA and `agent.validate_agent_state`, and restores originals on exit. The frozen interactive Evidence runner uses this around Evidence prepare and acceptance. This is the preferred existing *native* compatibility admission. Record that default legacy helper remains broken (#568/DM-023), while approved edition-local process can invoke the official existing agent-first adapter.

Prove `agent.validate_agent_state` is clean **before/after**, confirm source/checkpoint actual sha256, and negative-test tampered copy of State/checkpoint in an isolated temp environment. No editable live machine State until valid Core stage acceptance and bridge transition.

## 3. Bounded source_type projection — existing CV2-DM-016 precedent

The canonical 50-source Discovery contains **17 unsupported records across 10 labels**. Only modify **derived Evidence Task copies**, *never* accepted Discovery/Screening/source root raw facts. Produce explicit edition-local strict allowlist of the **17 exact discovery_id→original source_type→projected Core source class** entries; all types already in `SOURCE_CLASS_MAP` must remain untouched. Rationale must cite source origin and exact locator.

Conservative candidate projection: X_VENDOR_STATEMENT, X_OBSERVATION (3), DEV_POST, PAPER_LEAD (4), COMMUNITY_LEAD (3), COMMUNITY_ROUNDUP, COMMUNITY_BLOG_LINKED, COMMUNITY_PRICE_PAGE → **SOCIAL** *when the authority is the X/community lead*, not the independently read linked article; SECONDARY_CLAIM, SECONDARY_VENDOR_ROUNDUP → **SECONDARY**. Review each exception by source origin, not blanket name matching. When a true first-party blog, model card, paper, license, repo or external evaluation was subsequently consumed, represent it as **separate, real, task-bound Evidence Authority Supplement** with exact URL, raw captured bytes/hash/access proof and declared class. No source promotion from an X quotation alone. Unknown type → FAIL CLOSED.

Use frozen Core `prepare_evidence_package` in the native agent-first context, project exact Task-copy `source_records[].source_type` in derived package, recompute per-task `sha256`, package metadata and dependency hashes accurately; create original/projected task hash ledger with per-field diff to assert the **only** authorized source-record change is the classification string. Revalidate using **unmodified frozen Core** schema, task/card/acceptance routines under the standard frozen adapter. Preserve canonical discovery/screening input SHA and state identifiers. Test that projection cannot alter other fields, accepted authority or checkpoint provenance.

This is compatibility transport, not a new source discovery, source integrity downgrade, or a Core repair. The source projection requires validation from *actual Core APIs*, not a local validator with relaxed rules.

## 4. 50/50/50 machine and 49-substantive editorial invariants

W42 has 50 non-DROP Screening decisions: 49 actual research/editorial candidates + **one required Grok/X provenance binder** `w42-grok-x-ledger-20261017`. Frozen Core mechanically requires exactly **50 Evidence tasks, 50 Evidence Cards, 50 Edition Views**. The binder is not a 50th release/article. It must have a truthful `OTHER` provenance entity, bounded primary-subject observation of receipt/reconciliation linked to actual Grok raw, appropriate `PARTIAL/NEEDS_MORE` or other defensible status, `NON_MATERIAL` neutral view (unless the actual schema requires another honest classification), and explicit `NEVER_STORY` editorial rule. No fabricated technical result or `VERIFIED` new event; no silent drop or forged special exemption. Any schema difficulty → bounded FAIL CLOSED with exact error.

The other 49 must inherit r6/r7 substantive source-consumption work (151 raw factual/editorial claims, properly separated); **do not fall back to shallow 68 claims**. Convert into actual Core v2 Cards, entity/subject-role anchored claims and method/metric baselines, source_ids bound exactly to Discovery or real supplements. Not all 151 draft strings are validated primary facts; omit unsupported or label EDITORIAL properly via allowed Core class. Eight r7 editorial claims point to unrelated bundle-09: rebind to actually relevant source or remove; never treat `analyst-note` as Vendor primary. First-party paper/pdf/weights/licence analysis remains scoped to exactly what was read. Every Core `VERIFIED` is actual bounded verification; deficient source claim→`PARTIAL`/`NEEDS_MORE`/HOLD with explicit limits.

## 5. Core acceptance, quality and cautious State advance

First run all frozen Core validators for:
- 50 Evidence Task packages; complete 50 result Cards; 50 Edition Views;
- input SHA/prompt/schema identity and supplementary original source authority;
- accepted Evidence, views, materiality ledger and completeness, all with exact hash binding;
- 50 downstream dispositions, 49 editorial/non-editorial binder distinction;
- **agent-first** State checks before and after; stage-contract `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` with actual bridge receipts.

Use the frozen first-party agent-stage tool/bridge for lawful stage advancement. Fail closed if stage validation rejects an artifact even after native compatibility. Do not hand-author fake accepted receipts. Do not claim Core `PASS` unless a specific actual validation and read-back passed. Capture original-default-path failure distinctly from bounded compatibility-path PASS, including command-line invocation, test artifacts, SHA digests, precise adapter scope, and negative-case checks.

## 6. Editorial materiality and Selection after lawfully accepted Evidence

Only upon actual accepted Evidence/Views/Materiality/Completeness:
- Do not rubber-stamp r7 28 MATERIAL/14 CONTEXT/7 HOLD/1 ledger, whose r7 per-candidate reasons are boilerplate. Produce meaningful **positive and negative rationale for each MATERIAL candidate** and each non-selected high-signal candidate, including why this W42 window, what technical principle/method is actually supported, vendor vs independent limits, comparative utility, topical diversity and residual holes.
- For 6 proposed editorial packages (frontier, open-weight licensing, agents/coding, safety, science, specialist/community), decide overlap/dedup with source depth in mind. Reassess dense P2 vs P6 overlap and GLM-Legal, Fish audio, ASPIRE engineering and Sakana/Amazon research sidebars. Compare r7 15.5-page suggestion to a technically justified ~20–24-page sensitivity plan; don't truncate reader-level technical explanation to hit an arbitrary magazine length.
- Build materiality/Selection **proposals** with explicit per-item roles and omit/HOLD reasoning; user-facing Japanese should preserve established technical vocabulary and actual metric/benchmark names; no synthetic Human approval.
- **Stop at `SOL_MATERIALITY_SELECTION_REVIEW_READY`**, i.e. independent Sol review of positive/negative Selection prior to Architecture. Under no circumstance auto-accept Selection/Architecture merely because executor-generated proposals are schema-valid.

## 7. Deliverables and fallback

Single substantive execution unit rather than repeated micro-tasks. Deliver:
1. edition-local compatibility runner if needed (under W42 execution only), original/projection SHA ledger, source-class map, frozen-Core API call logs and negative tests;
2. true 50/50/50 Core accepted Evidence/Views if achievable; actual Materiality+Completeness, real stage checkpoint if lawful;
3. 49-story-candidate editorial rationale and genuine non-story ledger handling;
4. independent-source gap/negative-space accounting (no pretending published vendor press = reproduced benchmark);
5. substantive Selection proposals, package page-depth alternatives and omitted candidates matrix;
6. status dossier with actual final HEAD/Tree, unchanged Core/main/shared roots, bridge receipt, validation evidence, unresolved/blocked anomalies.

If acceptance remains blocked, **stop at concrete earlier blocker**, commit diagnostics/partial edition-local drafts only, preserve the last valid `CANDIDATES_NORMALIZED` and do not create/alter Human Gate records. If successful, resume from real `EVIDENCE_REVIEWED`; no Architecture/Draft/PDF or Human Gate yet. Always normal commit and non-force push on existing branch.

Core Issues #568/#569 and DM-016/DM-023 **remain OPEN_CORE** whether edition-local workaround succeeds or not.