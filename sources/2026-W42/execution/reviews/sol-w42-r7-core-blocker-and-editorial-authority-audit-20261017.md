# W42 Sol independent review r7 — REAL CORE BLOCKER / EDITORIAL PROPOSAL NOT APPROVED

Date: 2026-10-17 JST. Reviewed exact remote HEAD `1057abe18023ce17466b64ae403a64bd2f920fca`.
Branch `weekly/2026-W42-v2-work`. Main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`. Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`.
Disposition: **`STOP_CORE_EVIDENCE_ACCEPTANCE_BLOCKED / SOL_SELECTION_REQUEST_CHANGES / NO_ARCHITECTURE_AUTHORITY`**.

## 1. Verified production invariants

- Muse r7 is present as one normal commit. Accepted Discovery (50, including one non-editorial Grok/X binder) and Screening (KEEP 29 incl. binder, INSPECT 16, MAYBE 5) are intact; machine State remains `CANDIDATES_NORMALIZED` and Evidence/Materiality/Completeness/Selection/Architecture pending.
- Main and frozen Core are unchanged. No Human Gate passed, no PDF. Muse appropriately failed closed rather than waiving validators.
- r7 49 substantive candidate-local proposal cards contain 151 claims. Kinds (independently parsed): VENDOR 124 / X_OBSERVATION 10 / INDEPENDENT 4 / SECONDARY 4 / EDITORIAL 9; every claim has `authority`. 9 EDITORIAL internal repo-path references are not external URLs; those are not primary authority.

## 2. Core compatibility defects — independently substantiated by exact source-code reading

**CV2-W42-001 CONFIRMED (legacy-vs-agent State validation mismatch).** Frozen `scripts/survey_evidence_v2.py:prepare_evidence_package` calls `core.verify_state_basis`, which invokes strict `core.validate_state_semantics`. The agent-first bridge canonically records `orchestration/v2/checkpoints/` and per-transition implementation SHAs, whereas strict legacy semantics expects old attestation paths / pinned init SHA. Frozen `scripts/survey_agent_control_v2.py:verify_agent_state_basis` explicitly validates agent-resumable states without global commit pinning. Independently inspected W41 `main` RELEASED state: it carries the same checkpoint paths and multiple per-transition SHAs, corroborating the cross-edition mismatch. Muse's local execution reproduction of exact error counts is retained in `execution/defects/cv2-w42-001...`; independently running code was not possible through the connector, so the execution-error claim is attributed to Muse, whereas structural conflict is source-confirmed.

**CV2-W42-002 CONFIRMED (cross-stage vocabulary-contract mismatch).** Exact frozen `SOURCE_CLASS_MAP` in `scripts/survey_evidence_v2.py` has no entries for 17 canonical W42 Discovery records. Independently compared all 50 accepted `discovery-v2.jsonl` rows to the map: 17 missing over 10 distinct labels: X_VENDOR_STATEMENT 1, COMMUNITY_BLOG_LINKED 1, DEV_POST 1, COMMUNITY_PRICE_PAGE 1, X_OBSERVATION 3, PAPER_LEAD 4, COMMUNITY_LEAD 3, SECONDARY_CLAIM 1, COMMUNITY_ROUNDUP 1, SECONDARY_VENDOR_ROUNDUP 1. The helper `_source_class` raises on missing values; both `task_authority_sources` and non-supplement `validate_evidence_card` call it. The source records passed Discovery/Screening but cannot be consumed by strict Core Evidence. Diagnose as a shared **cross-stage contract incompatibility with edition-local noncanonical labels**, not automatic proof every missing type should be permanently added to Core. An isolated repair proposal must map individual types by REAL authority source rather than naive blanket `COMMUNITY_*`⇒SOCIAL.

**CV2-W42-003 NEW: required 50th Evidence task.** Core's `prepare_evidence_package` emits one task for EVERY non-DROP Discovery row. W42 Screening has 50 non-DROP, including the Grok/X binder marked KEEP. Therefore Core Evidence requires **50 task results and 50 compatible Edition Views**, not merely the 49 substantive editorial cards/views in the r7 local draft. The binder must receive lawful machine Evidence/neutral view disposition without being selected as a story; if the current schema cannot represent that cleanly, stop and seek contract repair, not silent drop, a fake verified model announcement, or upstream DELETE.

## 3. Unit-A provenance precision findings

- 151 bounded claims show substantial improvement over r4 68. Vendor/independent/X/editorial claim kinds now separate. Original Grok/X raw and expiry of X-derived corroboration remain accurately qualified.
- **E42-R7-P1 — 9 editorial references require correct source binding.** Nine `EDITORIAL` claims are assigned a repo path; 8 of these point to `ev-bundle-09-ocp-changelog-minecraft-r6.md`, whose actual contents cover NVIDIA OCP/SMLIB, Claude changelog, Minecraft and Qwen—not AI Scan, wet-lab, Rosalind, METR, AWS or MS Decision-1. Simply replacing `analyst-note` with an unrelated file path is not source traceability. Rebind each editorial synthesis to the genuinely supporting repo bundle or explicitly mark unsupported and omit. Do not count syntactic path validity as semantic authority.
- Metadata-only X observations can remain as leads if no original X post was fetched; source paths must distinguish original first-party authority from secondary Grok ledger.

## 4. Materiality and Selection verdict — only exploratory, no editorial approval

- r7 `materiality-r7.PROPOSED.json` has 28 MATERIAL, 14 CONTEXT, 7 HOLD, 1 NON_EDITORIAL, but nearly every `reason` is mechanical (`screening KEEP, N linked claims, M unresolved targets, Sol decides`). This is NOT independent positive/negative materiality analysis. Strong individual substantive Views can be reused to craft reasoned decisions.
- The six-package `selection-sketch-r7.PROPOSED.md` names plausible topical groupings (frontier, open-weight licensing, coding/agents, safety, science, special/community) and a safety-led alternative. It is a useful working outline, **not selection acceptance or final Architecture**. P2/P6 repeat MiniCPM/FLUX/LFM themes, suggesting overlap; P6 commingles weak community leads with GLM/Fish/ASPIRE science/engineering; actual prominence, comparative framing and Japanese/technical research balance need Sol-controlled review. The provisional 15.5pp plus up to 1pp of sidebars may compress 28 purported MATERIAL candidates excessively; propose an explicit 20–24pp sensitivity option if technical evidence warrants rather than page-cap-first truncation.
- Critical HOLD stands for uncorroborated X-only security allegations, unidentified harness-17 paper and out-of-window misdated items. Distinguish technical paper background from fresh W42 release claims. 49 candidates != 49 articles.

## 5. Authorized next steps / freeze invariant

1. **No Evidence Acceptance or Architecture advancement** under current Core state. Treat r7 research and six-package sketch as nonbinding.
2. Human's **Frozen Core v2 unchanged** policy remains operative. Do not edit frozen Core scripts, mutate accepted upstream files, sneak a compatibility shim around mandatory validation, or manufacture machine checkpoint approval.
3. Recommend isolated Core compatibility repair **only by explicit Human authorization as a separate maintenance track**, with focused tests including W41 RELEASED read-only, W42 CANDIDATES_NORMALIZED, all Evidence source_types, no weakening of unrelated State guards, and 50th provenance binder acceptance semantics. A lawful reviewed Core change/reintegration is a versioned exception to the freeze and cannot be done silently.
4. If the Human rules out Core modification, a distinct formally reviewed edition-local rewind/normalization plus faithful approved evidence preparation path is required. CV2-W42-001 remains even after type normalization; no demonstrated end-to-end Core-compliant solution exists under unmodified frozen Core. No unproven workaround authorized.
5. After a valid path resolves blockers, rebuild **50** Core Evidence and Edition Views, per-source citation reconciliation, Materiality/Completeness with candidate-specific positive and negative rationales, and request fresh Sol Selection semantic review. Architecture only after that independent approval.

No new Human Architecture Review or Publication Preview decision is requested in this record. This is an operational Core-maintenance decision boundary, distinct from both publication gates.
