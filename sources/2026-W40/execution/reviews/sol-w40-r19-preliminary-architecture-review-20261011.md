# Sol W40 r19 — preliminary Architecture review
Status: `STRUCTURE_PASS / R19_EQ5_STATUS_AUDIT_REQUIRED / HUMAN_GATE_APPROVAL_HOLD`
Date: 2026-10-11 JST
Muse exact HEAD `c26c983bff02245fffa5543fea8aa86291f80807`, Tree `10af9fbd5051572266e3030596e278ba03a6abba`; reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1`.

## Independent checks

Git from Sol r19 instruction `d7ae8ecda45613cb1d4af9ad7ca289ef0f99d5a4` advanced exactly two normal commits. First `98021de9c96d32a97c2857510e19fcfae20b5271`: official unpresented Architecture pending-Gate invalidation to `SELECTION_COMPLETE`; four superseded canonical/checkpoint files removed with recorded prior SHA/commit and `human_decision:false`, Selection checkpoint preserved. Second `c26c983bff02245fffa5543fea8aa86291f80807`: regenerated Architecture+Summary+Attention, new Stage validation and official Checkpoint, State `ARCHITECTURE_ESTABLISHED`, Human Gate pending/provenance null. Shared Core/main/upstream unchanged.

Sol independently fetched/compared canonical old vs new JSON: unchanged 35-candidate Matrix, Selection 28 SELECTED (20 PRIMARY, 8 SUPPORTING), 4 HOLD, 3 REJECT, all 28 exactly placed in 9 packages. All 113 original literal Boundary relationships retained in 105 unique package strings, zero missing/extra or nonselected intrusion. All r18→r19 Architecture changes restricted to `/packages/5/must_cover_requirements/0..2`, `/packages/6/purpose` and `/packages/6/must_cover_requirements/0..2`. Other Package data, thesis, roles, page plan and evidence basis unchanged. Core Review Summary JSON changed only `basis.architecture_sha256`; source-inherited stale `TIME_UNRESOLVED` persists, covered explicitly by separate mandatory r19 erratum.

Direct independent SHA-256 computation using a JavaScript implementation tested on the standard `abc` vector matched:
Architecture `305a42d6e66b03c6226f17c0e5bbf578c6672a2594425dbde50502f24174d0b9`;
Review Summary `37ce43b2facdcf8839303a8a4e25a71f7f28a075ad6e97157670885106764d51`;
Attention `70ac43bdd0da014009f99abaf3aff00db8bdfbd9e44940ba087abf4cb5949319`;
State `c5cd881153c60f1e6a50743995fc0a68f22ebda901723a3eae38dc293d1d6ce6`;
architecture Checkpoint `71388dbcbe0156e8908066a4d78309e9159dfcfe5dec8a14a46e101f47551d3b`;
Stage validation r2 `ec9ab3758d344c7a18967da6aa8ef300b1d4d7244b309cd5a6052e663ea78ad5`.
Independent Core code execution was NOT attempted; hashes and State/Checkpoint structure verified separately from Muse's `PASS` record. Legacy `validate-state` remains exit1 per Muse, agent-first validator reported PASS; no fresh Core regression independently established.

## Previously open r18 findings

F01: explicit review-surface erratum binds exact new Summary and accepted Completeness, separates article datePublished from weight/code dates, holds due Core #562; old Summary mechanically still contains legacy false statement. F02: OpenTTS TTFA protocol no longer attached to AgentPerf. F03: OpenTTS Oct7 script history removed from Olmo and rehomed in OpenTTS. F04: unexplained ContextLM dispatch removed; Olmo expert routing/dispatch clarified. F05: OpenTTS W40 app vs later script availability separated. F06: denser canonical methods/baselines/controlled configs in P6a/P6b; **one possible qualification-status regression below**. F07: `execution/index.md` Current Authority correctly updated.

## R19-P01 — new possible misleading ContextLM Eq.5 qualification

Current canonical `sources/2026-W40/architecture-v2.json` P6a `must_cover_requirements[1]` says `Eq.5 full update text UNVERIFIED beyond ar5iv sections 4-5 scope per technical-prep-r16/contextlm-eq5-primary-note.md`.

Actual source `execution/technical-prep-r16/contextlm-eq5-primary-note.md` calls Eq.5 `fully resolved`, transcribes exact `s* = argmax_s E_{x∼D}[R(τ(x;s))]`, defines s/D/τ/R, fixed weights, train/development/held-out split, and distinguishes Eq.5 in-context evolution from Eq.6 RL. The older r15 P6a draft's unverified Eq.5 reference was superseded by r16. What remains UNVERIFIED is *PDF binary, figures, appendices, code, repository pin and unquoted other cells*, not Eq.5 formula. The r19 language may falsely downgrade verification or cause the later Japanese Draft to omit the equation.

Provisional severity `MODERATE / CLAIM_STATUS_AMBIGUITY`; requires independent adjudication. Minimal clarification if confirmed: Eq.5 exact formula/symbols VERIFIED by r16 ar5iv v1 §4.2, surrounding unretrieved materials explicitly delimited. Any change to checkpoint-pinned canonical Architecture must use the lawful pending-Gate repair process; no direct hand edit, no Human approval/rejection here.

Next: `execution/instructions/2026-10-11_sol-high-w40-r19-independent-architecture-readonly-audit.md`; Human Architecture Approval remains HOLD pending independent content audit. Core #562 remains separate and NOT a W40 28-item blocker.
