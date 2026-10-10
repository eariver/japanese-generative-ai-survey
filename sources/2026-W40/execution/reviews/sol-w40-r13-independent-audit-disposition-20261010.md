# Sol W40 — Independent r13 audit disposition

Status: `SOL_W40_R13_AUDIT_ACCEPTED / REVISION_REQUIRED / BOUNDED_R14_AUTHORIZED / SELECTION_ACCEPTANCE_HOLD`  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Independent review target HEAD: `eb0d8f1685278d02b0d889c2b0ae16f77d722907`  
Independent review target Tree: `601b6527eb6e1b72d3e2b1d9a554999fb217102a`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Current canonical State (before this disposition): `EVIDENCE_REVIEWED` / next `stage:selection`

## 1. Scope and authority

The independent read-only r13 audit was handed to Sol by the Human. This file records **Sol's editorial disposition** of that audit, NOT a fabricated original independent auditor file, Selection Acceptance, Human decision, Core patch or publication authorization.

Independent verdict: `REVISION_REQUIRED`.

Individual auditor results:
- `EDITORIAL_REPAIR_ACCEPTABLE: NO` (remaining verifier semantic and provenance error)
- `SUPPLEMENT_PUBLICATION_PATH_ESTABLISHED: NO`
- `SELECTION_ACCEPTANCE_READY: NO`
- `ARCHITECTURE_PREPARATION_READY: NO` (Role/coverage mismatch)

Accepted PASS boundaries: Git identity, r13 one-commit 12-file W40-local change, unchanged accepted upstream/Production State/Human Gates, 35 distinct Candidate IDs, 28 SELECTED (20 PRIMARY / 8 SUPPORTING), 4 HOLD, 3 REJECT, zero INSPECT, and r12→r13 DGX-only assignment disposition+rationale delta with basis unchanged. Muse reports unmodified Python Core Selection Validator PASS; independent auditor reviewed its code and independently recomputed important constraints but **could not execute original Python validator**. Preserve that epistemic distinction.

## 2. Sol dispositions for independent F01–F08

| ID | Severity from audit | Sol decision and required r14 action |
|---|---|---|
| W40-R13-F01 | MAJOR | ACCEPTED. `survey-production-v2-release.yml` checks count of **assets with expected filename**, not total Release assets == 1. A second differently named asset may be technically present, but no Core approval semantics exist for its publication. Repair contract analysis and do not upload/authorize any asset. |
| W40-R13-F02 | MAJOR | ACCEPTED. P5: SynthID Bio is PRIMARY, not SUPPORTING. Role map is 3 PRIMARY / 2 SUPPORTING. Reconcile candidate IDs from exact Selection JSON. |
| W40-R13-F03 | MAJOR | ACCEPTED. P7: VSS 3.3 and Nemotron ASR are PRIMARY, AMD Ross SUPPORTING; map is 3 PRIMARY / 2 SUPPORTING. Resolve apparent 27-item annotated outline versus 28 SELECTED with machine-generated one-to-one coverage. |
| W40-R13-F04 | MAJOR | ACCEPTED. Evidence ledger `2026-10-10 ~19:57Z` is AFTER r13 commit at `2026-10-10T11:02:43Z`; likely JST/UTC confusion but **do not assert causal explanation without raw logs**. Different SHA256 on same byte count proves byte difference ONLY, not specifically dynamic framing. Historical r13 ledger remains as evidence; add accurate correction/uncertainty ledger. |
| W40-R13-F05 | MODERATE | ACCEPTED. Reader `supporting_files` may hold SHA-bound `BIBLIOGRAPHY/STYLE/SUPPORTING_SOURCE` but has no SUPPLEMENT approval role. Mandatory coverage validation rejects inaccurate coverage records; extra plain prose may not be caught mechanically and requires semantic/Human review. Distinguish machine gate, editorial contract and Owner authority. |
| W40-R13-F06 | MODERATE | ACCEPTED. AutoSynthData negative gate rejects invalid mutations and principally exercises **soundness**; positive gate accepts a witness/reference trajectory and exercises consistency/feasibility for that trajectory; neither alone proves universal **completeness**, which requires valid-alternative acceptance. Repair r14 note; preserve three distinct verifier properties. |
| W40-R13-F07 | MODERATE | ACCEPTED. Create a machine-checkable 28-item matrix with exact Candidate ID and Role, one canonical staging package per PRIMARY and at least one per SUPPORTING. Build P6a/P6b substantive technical preparation with model/paper-specific mechanisms, experiment conditions and limitations; no assumed/fabricated metrics. Keep both HOLD subjects CONDITIONAL. |
| W40-R13-F08 | MINOR | ACCEPTED. r13 handoff's 'closed' language is overstated for F03/F06/F08. Create truthful r14 supersession/addendum and per-finding evidence. Never rewrite r13 history silently. |

## 3. Publication and continuity adjudication

**Core change separation remains binding.** Issue #562 / CV2-DM-022 is maintained by the separate Core task. No Shared Core code/config/schema/workflow repair is permitted in Weekly or Special production.

The two issuer-hosted Oct 2 article subjects AstaBrief and AutoSynthData remain editorially material but formally canonical HOLD. Frozen-Core compliant 28 selected items are a **preview, not a completed editorially sufficient W40 release**. Publishing detached supplemental research may require explicit Human authorization and its own reviewed authority; simply adding extra GitHub Release assets is not a Core-sanctioned supplement. There is currently **no approved normal path** to include the HOLD subjects under W40's Core architecture and publication authority.

Stop formal `EVIDENCE_REVIEWED → SELECTION_COMPLETE` until a valid new reviewed Core authority/re-entry or an independently authorized, semantically and legally sufficient publication decision, with Sol review and Human authority as needed. Don't invent a release exception. Technical staging and deep draft development may proceed.

## 4. Next bounded instruction

`sources/2026-W40/execution/instructions/2026-10-10_muse-w40-r14-bounded-editorial-contract-repair.md`

Terminal: `SOL_W40_R14_BOUNDED_REPAIR_REVIEW_REQUIRED`, no Selection Acceptance, canonical Architecture, Stage transition, Human Gate, Freeze or Release.
