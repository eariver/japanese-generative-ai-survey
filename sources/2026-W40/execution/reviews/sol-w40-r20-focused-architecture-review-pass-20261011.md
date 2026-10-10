# Sol W40 r20 — focused Architecture review PASS

Status: `PASS_FOR_HUMAN_ARCHITECTURE_REVIEW / HUMAN_GATE_DECISION_PENDING`
Date: 2026-10-11 JST
Repository: `eariver/japanese-generative-ai-survey`
Exact Muse r20 reviewed HEAD: `3711d777f8c447d25c6e0bfb3212450974afe8ab`
Exact Muse r20 reviewed Tree: `9d339509775a74128581aeddeb755adee51ff3f5`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`

**Verdict:** Bounded r20 repair is complete. This is Sol's own GitHub-based focused review independent of Muse's self-report, **not a new separate third-party audit, not a full Core CLI execution replay, and NOT a Human Gate APPROVED or REQUEST_CHANGES decision**. Independent r19 one-shot audit had determined the full 28-item Architecture substantively adequate subject to exactly two documented residual findings; both are now CLOSED.

## Verified Stage and Git provenance
- The r20 implementation advanced via exactly two normal FF commits from Sol r20 instruction `db87d64e385b82451179689e1dc75f46941dd495`: official operator pending-Gate invalidation `512937f54c32f0deaff6734b27bb11a997cee6f1` (record sequence 0002; `human_decision:false`), then terminal regeneration `3711d777f8c447d25c6e0bfb3212450974afe8ab`.
- The intermediate commit removed old Architecture, derived Summary, Attention and Architecture checkpoint singleton paths, and placed State at `SELECTION_COMPLETE` with Selection passed and Architecture pending. The terminal State is `ARCHITECTURE_ESTABLISHED / ARCHITECTURE_REVIEW / HUMAN_GATE_REACHED`; Selection and Architecture `passed`; both Human Gates pending with null provenance, exception inactive, Draft pending. All prior canonical versions remain reachable in Git.
- Core Stage validation r3 records `CORE_STAGE_CONTRACT PASS`, and Review Summary records `READY_FOR_ARCHITECTURE_REVIEW`; official checkpoint binds regenerated files. Legacy `validate-state` exit1 remains a distinct preexisting diagnostic, NOT claimed PASS. Independent full Core CLI not rerun by Sol.
- Sol independently recalculated SHA-256 from GitHub actual UTF-8 files with a standard-test-vector-validated hash implementation: Architecture `a9b5c1182671bb913fbf56972907e19731e5ba4a928deaca9903a0d3a1461a44`; Summary `32f39de0b7cb3e469acf74668c420c246fb67f273ecd0c37bda91557eaa98d30`; Attention `70ac43bdd0da014009f99abaf3aff00db8bdfbd9e44940ba087abf4cb5949319`; State `19bd1a9749108cf61ff29159dac216922b7316e5a91ee41c2f82f2f20e4bcb89`; architecture checkpoint `95b7755a663e1dcfe33f3983e166cd8e549430bfde1bbda343d6852057423a8c`; unchanged Selection checkpoint `817075850a9390f735f9a9a4a35ebc9d391793b3ecd7907ba7d2308ebadfa678`; Stage validation r3 `a5d7abcea00abc25e545faf422eec5b83151ad9748da63eaddfbedaff913ba73`.

## Findings resolution (confirmed)

- **R19-F01 CLOSED (MODERATE):** Actual r19→r20 `architecture-v2.json` recursive JSON diff shows **exactly one changed scalar**: `/packages/5/must_cover_requirements/1`. The stale `Eq.5 ... UNVERIFIED` statement was precisely replaced: Eq.5 objective, variables, frozen model weights and training/development/held-out skill evolution `VERIFIED` by `arXiv:2609.37725v1 §4.2` and `execution/technical-prep-r16/contextlm-eq5-primary-note.md`. Eq.6 remains parameter-learning RL. Separate PDF bytes, figures, appendices B–F, code, unpinned repo version and uncited details remain UNVERIFIED. All other Architecture scalar values, source roles, candidate memberships and baselines unchanged.
- **R19-F02 CLOSED (MINOR):** Current `execution/index.md` State SHA-256 is exactly 64 hex, `19bd1a9749108cf61ff29159dac216922b7316e5a91ee41c2f82f2f20e4bcb89`, matching actual current `production-state.json` bytes. No stale 66-hex current value.
- **Integrity:** 35 Matrix candidates, 28 selected, 4 HOLD, 3 REJECT. Nine Package groups preserve 28/28 selected IDs (20 PRIMARY +8 SUPPORTING), all 113/113 original literal Candidate-boundary relations in 105 unique Package strings, no missing/extra, no HOLD/REJECT entry. Canonical Selection/Matrix, r15 Boundary source, accepted Completeness and Selection checkpoint unchanged before/after r20.
- The prior r18 F01–F07 were already independently adjudicated, with r19 fixes and r20 status update; no new change outside verified Eq.5 pointer.

## Mandatory inherited review-surface limitation

A **first-read** supplement MUST accompany any Human Gate or Draft review: `execution/reviews/w40-r20-architecture-review-surface-erratum.md` SHA-256 `564799edf0679c2fade1094139580e7c5d116a4abd3be2453de297f0ebcf3833`. It accurately binds NEW Review Summary and frozen Completeness bytes. The machine-generated Review Summary still inherits a *historically false as written* `TIME_UNRESOLVED` sentence about AstaBrief/AutoSynthData original hosted article times. Original issuer article JSON-LD `datePublished` clocks are verified (2026-10-02T15:19:50.340Z and 2026-10-02T04:01:31.290Z respectively), **not** model weights/code/dataset release clocks. Both candidates remain canonical HOLD due separate Core Issue #562, not due the original hosted article clock. This is an accepted additive erratum, not permission to rewrite immutable accepted upstream or publish a companion edition.

## Stop

`PASS_FOR_HUMAN_ARCHITECTURE_REVIEW / AWAIT_EXPLICIT_OWNER_HUMAN_DECISION`.

No Owner Human Gate decision, Draft, Preview, Freeze or Release is authorized or executed by this report. Before recording any Owner `APPROVED` or `REQUEST_CHANGES`, read back latest branch HEAD/Tree and exact reviewed Gate artifacts. Core #562 is separate, with 28-item W40 normal path valid.
