# J-GAS W43 — Post-r8 Human proof approval: read-only feasibility of lawful canonical publication path

Date: 2026-10-28 JST.
Authority: EDITORIAL_SOL_READ_ONLY_RESEARCH_REQUEST / NO_GOVERNANCE_CHANGE / NO_EXECUTION_APPROVAL
Executor: Muse/OpenCode or another bounded engineering reviewer, reporting to editorial Sol. NO ChatGPT Work requirement.

## 0. Exact fail-closed start

Repository eariver/japanese-generative-ai-survey
Existing branch weekly/2026-W43-v2-work; do not create new branch.
Expected remote pre-contract HEAD:
589019fa183e73035a24699b54b5aa38fc03ddb4
Expected remote pre-contract Root Tree:
b42a1e1b4d6949f84c55588f16c15cc6dbccede1
The final contract-only commit HEAD/Tree will be supplied by editorial Sol alongside dispatch. Before reading candidate execution code, verify exact remote final contract HEAD/Tree and its parent equals the above pre-contract HEAD. Mismatch → STOP without writes.
Reviewed main HEAD/Tree:
041a08dfef3112643cbf85b4a86a7b6f9128aed6 / a134dc36a407d08ab1de416324229b3955e0325a
Frozen production/survey-core-v2 HEAD/Tree:
774dd39a951c9ac3818e83dfffd4c7666efb0a20 / cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481

Read-only only. Do not run write-capable tests against GitHub or canonical production State. Use read-only git show/cat-file, inspect committed source and policy. No push, commit, Issue, PR, local repo mutations, state/gates mutation, repair branch, temporary core patch, mock receipt, simulated PASS labelled real, tag, freeze or release. Output only an analysis/report IN CHAT to editorial Sol; if a local scratch test becomes necessary, first justify, isolate in /tmp, and DO NOT claim it is validated canonical authority.

## 1. What is ALREADY approved and what is NOT

Human Owner explicitly wrote in editorial Sol Chat on 2026-10-28:
「確認の結果OKです、承認します。」
It followed presentation of exactly pinned 22-page r8 NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF, post independent terminal INDEPENDENT_W43_R8_P2_SIDECAR_AND_PDF_PASS (P0=0, P1=0, P2=4 nonblocking).

Human content/layout PRE-REVIEW approval record:
sources/2026-W43/execution/governance/human-w43-r8-corefree-proof-content-layout-approved-20261028.md

Fixed r8 HEAD/Tree:
953a9d331972fdae237da4bd0f1019b17168a118 / dfafff50c946e3d0abc051eb419797de283b192a
Fixed PDF:
sources/2026-W43/execution/core-free-preview-r8/main.pdf
SHA256:
abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72
Fixed P2 sidecar HEAD:
de5e41c253de37015fdb828503040f818698c6bc

THIS is NOT an exact-byte canonical PUBLICATION_PREVIEW Human Gate. DO NOT assume or request that worker records production-state human_gates.publication_preview=approved. No Release authorization, no exception_gate consent, no permitted Core modification or publication waiver.

## 2. Current actual blocker

Current sources/2026-W43/production-state.json:
lifecycle_state ARCHITECTURE_ESTABLISHED;
human_gates.architecture_review approved;
human_gates.publication_preview pending;
exception_gate.status inactive;
next_action stage:drafting-synthesis;
machine_checkpoints.draft/validation/publication_preview/freeze/release pending.
Canonical native drafting attempt failed before artifacts with:
ValueError: Screening package basis drift: state_sha256
Document:
sources/2026-W43/execution/defects/w43-drafting-screening-basis-drift-20261025.md
Related bridge-state validator mismatch:
sources/2026-W43/execution/defects/w43-screening-prepare-state-basis-20261025.md
Do not misrepresent PDF QA as a replacement Draft/Validation checkpoint.

## 3. Mandated source reads and evidence

Read current code and config at reviewed main and frozen production/survey-core-v2, relevant schemas and W43 State, along with:
- docs/survey-production-core-v2-authority.md
- docs/survey-production-core-v2-final-audit-rule.md
- docs/survey-production-core-v2-operator-execution-bridge.md
- docs/survey-production-core-v2-session-bootstrap.md
- docs/survey-production-core-v2-sol-luna-review-governance.md
- docs/freeze-release-policy.md
- docs/weekly-release-policy.md
- docs/core-v2-deferred-maintenance-summary.md
- docs/weekly-release-process.md
- sources/2026-W43/execution/defects/w43-drafting-screening-basis-drift-20261025.md
- sources/2026-W43/execution/defects/w43-screening-prepare-state-basis-20261025.md
- historic W41/W42 edition-local compatibility records, only as EXACT evidence, not automatically portable authority.

For each proposed step distinguish:
1. current frozen Core supported canonical API/CLI (names, exact inputs, output authority);
2. agent-first bridge behavior; 
3. release preview/validation/checkpoint prerequisites and Human Gate provenance;
4. previously authorized edition-local runtime-only compatibility; its precise defect, Human consent scope, and whether this W43 drafting failure is SAME or DIFFERENT;
5. any shared-Core repair that necessarily changes frozen bits;
6. independent audit and Human-specific consent required if any.
Look for current code reality, not optimistic interpretation of older docs or the PDF.

## 4. Evaluate three paths separately

A. **Normal canonical native recovery**: Is there a strictly legal existing frozen-Core mechanism for resolving W43 historical screening State basis without altering accepted research authority / State or shared Core? If NOT, say impossible with concrete function/API call and failure cause. A future generic shared Core maintenance may need a separate reviewed candidate, formal audit and new baseline decision; W43's currently protected Frozen Core v2 MUST remain unchanged.

B. **Edition-local runtime-only compatibility, conditional**: Can a narrowly bounded proven W41-style compatibility be applied to THIS actual W43 native drafting cause, preserving original active Screening and trustworthy stage/human provenance? Does repository authority expressly permit it? Show a semantic gap analysis: W41 later Freeze gate schema vs W43 early Draft state_sha256 are different; prior success is NOT authorization for this new failure. DO NOT implement. If feasible, draft a narrowly scoped HUMAN OWNER Exception Gate proposal with its affected functions and input hashes, allowed transient behavior, positive and negative tests, audit duties, fail-closed conditions, and what machine artifacts would remain canonical. Distinguish technical feasibility from lawful authorization.

C. **Noncanonical proof-only alternative**: Can a distinct explicitly-labelled edition publication policy lawfully publish without canonical Publication Preview / Freeze? Review exact docs and current release workflow. Do NOT invent a backdoor. If no explicit sanctioned path, label NOT AUTHORIZED. A Human proof acceptance alone is not a release exception. Only a separate explicit Human owner publication-scope exception could start such a discussion, and it cannot silently masquerade as canonical Release.

In all paths preserve accepted W43 Architecture, Evidence, Selection and r8 byte identity; preserve 36 bibkeys and 15 CURATED_REVIEW_REQUIRED; nothing in this task approves a public release or new research.

## 5. Required report and stop

Respond IN CHAT ONLY with:
- exact triple Git guards + protected refs,
- repository-file-based feasibility matrix for paths A/B/C;
- line/code-level description of root cause and genuine chain of authority;
- if B/C are theoretically viable, precise human decision text for a future proposal (not consent inferred now);
- first irreducible missing approval/primitive for any proposed path;
- ranked recommendation: preserve frozen Core and prefer canonical path; only propose exception if policy+technical evidence justify it;
- exact next bounded execution task after that separate decision, or STOP if no lawful path.

Report terminal one of:
READ_ONLY_NATIVE_PUBLICATION_PATH_EXISTS
READ_ONLY_BOUNDED_COMPAT_CANDIDATE_NEEDS_OWNER_AUTHORITY
READ_ONLY_SHARED_CORE_REVIEWED_REPAIR_REQUIRED
READ_ONLY_NO_LAWFUL_PATH_PROVEN.

Never write an edited State/Gate/approval or claim canonical preview. Never declare release ready solely because of the independent r8 PASS and Human proof acceptance.
