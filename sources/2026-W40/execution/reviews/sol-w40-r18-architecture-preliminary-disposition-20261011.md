# Sol W40 r18 — preliminary Architecture Review disposition (Human decision NOT recorded)

Status: `MACHINE_GATE_REACHED / SOL_PRELIMINARY_REVIEW_FINDINGS / INDEPENDENT_AUDIT_REQUIRED / NO_HUMAN_DECISION`  
Date: 2026-10-11 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Reviewed Muse r18 HEAD: `c81296e1598a68f2879ea32c90d731ef1f418047`  
Reviewed Tree: `faffcf97f6a13d845ed5b95169bf8a7162407ca4`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
W40 State: `ARCHITECTURE_ESTABLISHED / ARCHITECTURE_REVIEW / HUMAN_GATE_REACHED`.

## Verified, independent read-only inspection

- Git compare against r18 exact start `710e83017086e7ac7a0c40658c4ff05ca41c08f9`: 4 normal FF commits, 17 W40-local file changes, no Shared Core/schema/config/workflow or other Edition.
- Canonical `candidate-matrix-v2.json`, `candidate-selection-v2.json`, `architecture-v2.json`, `architecture-review-summary-v2.json`, `architecture-review-attention-v2.json` are committed. Selection and Architecture Stage validations declare PASS; State pins real stage checkpoint refs. Gates both pending, provenance null, no Draft.
- Sol independently joined canonical Selection/Architecture to r15 lossless Boundary source. **28/28 selected candidates placed**, 20 PRIMARY / 8 SUPPORTING, no HOLD/REJECT in packages, **113/113 literal Boundary memberships**, 105 unique package strings, 0 missing/extra, per-package P1 14/12; P2 8/8; P3 13/13; P4 10/8; P5 18/17; P6a 10/10; P6b 15/15; P7 19/16; P8 6/6. Distinct P6a/b share valid `WEEKLY:training-eval-infra` profile role. Core-derived Review Summary `readiness.status=READY_FOR_ARCHITECTURE_REVIEW`; human_review null.
- The above is **structural**, not Human/editorial approval. A separate independent technical and governance audit is necessary before deciding to APPROVE vs REQUEST_CHANGES.

## Review findings requiring adjudication

### R18-P01 (MODERATE / factual review-surface contradiction)

Canonical `architecture-review-summary-v2.json:416` contains:
`AstaBrief/AutoSynthData exact Oct 2 publication times unproven (day-only everywhere checked); held TIME_UNRESOLVED.`
This is false for the **original issuer-authored hosted article event**. Sol r11's verified original HF org JSON-LD `datePublished` is AstaBrief `2026-10-02T15:19:50.340Z` and AutoSynthData `2026-10-02T04:01:31.290Z`, both within W40. Canonical `candidate-selection-v2.json` and Architecture thesis correctly explain their HOLD arises **solely from Core #562 old upstream-authority supersession gap**, not a missing article clock. Inherited source: immutable `profile-completeness-v2.json:221`; unchanged frozen Core `survey_architecture_v2_base.py:914–916` mechanically copies residual limitations from accepted Completeness. Do NOT hand-edit generated Summary or old Completeness. Independently decide whether an explicit additive audit/Human review correction suffices for truthful approval of a 28-item scoped edition, or whether governed pre-Gate revision is necessary. Record exact difference between article event and weight/code upload clocks.

### R18-P02 (MODERATE / technical cross-topic contamination)

Canonical `architecture-v2.json:234` (P6b purpose) groups `TTFA protocol clause-verified` inside **AgentPerf**, but the r15 source `execution/technical-prep-r15/p6b-deep-draft.md:73,98,160` binds TTFA 50-prompt/batch1/3 warm-up/median to **OpenTTS**, a different publication/evaluation platform. Cross-referencing must not cause reader text to attribute OpenTTS's TTFA protocol to AgentPerf. Explicitly separate in P6b purpose / must-cover.

### R18-P03 (MODERATE / technical cross-topic contamination)

Canonical `architecture-v2.json:213` (P6a Olmo-core 3 must-cover) includes `scripts temporal split with commit history as dated negative`. The evidence is **OpenTTS** W40 Sep30 publication promise vs Oct7 added evaluation scripts, documented in `execution/technical-prep-r15/p6b-deep-draft.md:117–126,162`, and has no relation to the Olmo-core 3 controlled MoE MXFP8/negative result method. Remove from P6a Olmo-core 3 and place, if useful, in the OpenTTS P6b must-cover.

### R18-P04 (REVIEW REQUIRED / Stage basis and gate governance)

Muse's `execution/sessions/muse-w40-r18-20261011.md` notes that standalone Core `validate-state` reports pre-existing agent-first history/attestation divergences, whereas `validate_agent_state` and two `CORE_STAGE_CONTRACT` validations PASS. Inspect the two State versions at r18 base and final, two stage checkpoint records, exact Core semantic checks and any error message available. Determine whether an inherited known diagnostic difference vs an actual invalid canonical machine transition. Do not assert a clean `validate-state` PASS that was never obtained. If independent reproduction unavailable, mark `NOT_INDEPENDENTLY_REPRODUCED` and request exact logs. No invented Core fix; #562 remains separate.

### R18-P05 (CONTENT SUFFICIENCY / Reviewer judgment)

Canonical Architecture has 9 editorial packages and 9 goals, with approximately 2–5 must-cover lines per package, but the detailed r15 P6a/P6b technical drafts are **noncanonical**. Check whether Architecture's must-cover requirements and purpose actually bind sufficient depth, discriminated baselines, dates, source attribution and legal distinctions for Draft stage; distinguish clean validator compliance from expected longform manuscript sufficiency. No arbitrary page cap, no stealth 30-item inclusion. Reuse existing source-to-claim support as evidence, not as a claim that referenced documents automatically satisfy canonical content instructions.

## Current decision and action boundary

`INDEPENDENT_R18_ARCHITECTURE_AUDIT_REQUIRED`. Do not yet record `APPROVED` or `REQUEST_CHANGES` for Human Architecture Gate; no State or canonicals edited. Prepare evidence-backed independent findings, deciding whether P01–P03 need a formally governed revision versus additive clarification. Any change to generated canonical Architecture after checkpoint is **NOT permitted by direct file edit**; follow the already-present reviewed-Core pending-Gate revision/invalidation mechanism if authorized. No W40 Stage promotion, Draft, Freeze, Release, supplementary publication or shared Core update. Core Issue #562 remains separate and not a prerequisite for the 28-item W40 normal path.
