# Sol W40 — adoption of independent r18 Architecture audit

Status: `SOL_R18_AUDIT_ADOPTED / BOUNDED_REVISION_REQUIRED / HUMAN_ARCHITECTURE_APPROVAL_HOLD / R19_ARCHITECTURE_ONLY_REGENERATION_PREPARED`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`
Independent auditor's reviewed HEAD: `88e98b3858739de72f8a7b56394dc0616901fac6`, Tree `038c27b4e7e152b45492b627125618baa21e098a`
Canonical Architecture authority HEAD: `c81296e1598a68f2879ea32c90d731ef1f418047`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`

The Human supplied a separately conducted read-only independent r18 audit dated 2026-10-11 JST. This is **Sol's disposition and follow-up instruction**, NOT a Human Gate decision, formal `REQUEST_CHANGES`, an independent rerun of all Core commands, or evidence that legacy `validate-state` passed.

## Accepted positive findings

- Remote HEAD/Tree/main, 4-commit r18 FF from `710e83017086e7ac7a0c40658c4ff05ca41c08f9`, canonical commit and audit-only follow-on: PASS.
- Canonical Matrix has 35 distinct; Selection 28 SELECTED (20 PRIMARY/8 SUPPORTING), 4 HOLD, 3 REJECT. Nine packages place 28/28, 113/113 original Matrix literal boundary memberships and 105 package-unique strings; zero missing, extra, HOLD/REJECT intrusion. PASS.
- Selection and Architecture Stage attestation/hash integrity and agent-first checkpoint path: structural PASS. The *legacy* `scripts/survey_production_v2.py::validate-state` mismatch was **NOT independently reproduced** as CLI stderr. The independent audit found preexisting agent-first vs legacy history/attestation semantics; do not claim legacy PASS or a new r18 invariant breach.
- Production State `ARCHITECTURE_ESTABLISHED / ARCHITECTURE_REVIEW / HUMAN_GATE_REACHED`, Selection/Architecture passed, Human Gates pending and provenance null. Draft/Freeze/Release unstarted.

## Adopted findings and disposition

| Finding | Severity | Disposition |
|---|---|---|
| R18-F01 | MODERATE | CONFIRMED. `architecture-review-summary-v2.json:416` echoes outdated source `profile-completeness-v2.json:221`: original issuer-hosted 2026-10-02 article publication instants for AstaBrief (`15:19:50.340Z`) and AutoSynthData (`04:01:31.290Z`) were resolved in r11, not TIME_UNRESOLVED. Article timestamps do not establish new weights/code/dataset release. **Correct via explicit review-packet erratum**, not by directly editing accepted Completeness or generated Summary. State this residual verbatim false inherited sentence alongside its correction; new Summary may still mechanically include it. |
| R18-F02 | MAJOR | CONFIRMED. `architecture-v2.json:234` associates `TTFA protocol clause-verified` with AgentPerf. Source `execution/technical-prep-r15/p6b-deep-draft.md:73–105,160` assigns 50 English prompts, batch1, first3 warmups excluded, median, H200 to **OpenTTS**. Architecture-only correction required. |
| R18-F03 | MAJOR | CONFIRMED. `architecture-v2.json:213` attributes 2026-10-07 eval-script commit sequence to Olmo-core 3. It is **OpenTTS**, as `technical-prep-r15/p6b-deep-draft.md:117–126` establishes. Move relevant chronology to OpenTTS must-cover; restore pure MoE negative-results scope to Olmo. |
| R18-F04 | MINOR | CONFIRMED attribution ambiguity: ContextLM must-cover `dispatch` at `architecture-v2.json:211` lacks ContextLM source; it belongs under Olmo expert dispatch/routing per `technical-prep-r15/p6a-deep-draft.md:110–119`. |
| R18-F05 | MODERATE | `architecture-v2.json:244` `Spaces app + scripts` risks backdating OpenTTS eval scripts to W40. Separate 2026-09-30 article's future promise from 2026-10-07 first code commit, with W40 cutoff `2026-10-02T22:00:00Z`. |
| R18-F06 | MODERATE | Insufficient canonical binding of r15/r16 NON_CANONICAL technical depth. Add explicit bounded must-cover checks for ContextLM relative/denominator/base and Eq5 vs Eq6; Olmo 47B vs1.2T vs2.38T; AgentPerf roofline vs non-spec + single-user vs production; OpenTTS TTFA/metric preference limits/scripts chronology; RL Hub framework version != taskset revision. Reference exact source notes, no blind transclusion. |
| R18-F07 | MINOR | `execution/index.md:15–18` falsely labels historical `EVIDENCE_REVIEWED / stage:selection / none` as Current after r18. Update navigation **only after** new Stage stop; preserve historical SHA and states in a labeled history, never modify old authority. |
| Legacy note | WATCH | Core legacy `validate-state` remains `NOT_INDEPENDENTLY_REPRODUCED` for exact command stderr. Request execution diagnostics (command, exit, stdout, stderr) alongside agent-first result without assuming this is #562 or silently changing Shared Core. |

## Scope and procedure

Approve the editorial r19 repair *direction* (not yet a Human review decision): keep 35 canonical Matrix, same Selection 28P/S split (28 = 20P+8S), 4 HOLD, 3 REJECT, accepted upstream, 113 literal Boundaries unchanged. Core #562 stays independently OPEN; continue existing 28-item W40 normal route.

To change checkpoint-pinned Architecture, use the currently configured **operator unpresented pending-Gate invalidation** (not `request_architecture_revision`/Human `REQUEST_CHANGES`), `gate=ARCHITECTURE_REVIEW`, `regeneration_boundary=SELECTION_COMPLETE`, only if no Human review record exists and the current exact Gate surface is valid. The current GitHub snapshot has `sources/2026-W40/gates/review-index.json` absent, pending/null Gate, `HUMAN_GATE_REACHED`; execution must recheck at runtime before mutation. Operator invalidation requires exact branch HEAD and will delete superseded canonical Architecture/Checkpoint files **through the reviewed Core operation** with recorded provenance, not direct hand-edit. Preserve old bytes via Git commits and operator invalidation record. Selection checkpoint and canonical Selection MUST remain pinned and unchanged.

**Critical implementation compatibility:** `scripts/run_selection_architecture_v2_interactive.py::run` requires `EVIDENCE_REVIEWED` at line 167 and refuses overwriting canonical Matrix/Selection/input archive; it **cannot** regenerate Architecture only from `SELECTION_COMPLETE` and must not be used as an override. On official `SELECTION_COMPLETE` regenerate Architecture JSON with existing schema/validators, derive `architecture-review-summary-v2.json` and `architecture-review-attention-v2.json` via standard unchanged Core functions. Stage validation and checkpoint generation must independently PASS. Output a fresh Human Architecture Review, **no automatic Human acceptance**.

Read details: `execution/instructions/2026-10-11_muse-w40-r19-bounded-architecture-gate-invalidation-and-regeneration.md`.

**Final target:** `FRESH_HUMAN_ARCHITECTURE_REVIEW_PENDING / R19_INDEPENDENT_REVIEW_REQUIRED` (only if actually ready).
