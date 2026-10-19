# W42 r28 — default + pinned registry map vs the two DRAFT_COMPLETE identities (NONCANONICAL)

Status: `SOL_W42_R28_REGISTRY_EVIDENCE / READ_ONLY / NO_ALIAS / NO_CORE_CHANGE`. Frozen Core blobs verified identical
at reviewed main (`c8d0ecc1…`) and State-pinned implementation (`a4f25630…`, tree `e68560d1…`).

## 1. Immutable refs

| file | pinned blob | main blob | match |
|---|---|---|---|
| `config/survey-production-v2.json` | `cffe16fec2186d5d7c1297aa49b830d639865e96` | `cffe16fec2186d5d7c1297aa49b830d639865e96` | identical |
| `scripts/survey_handlers_v2.py` | `510a2abada13a165d404fba57a78daa67af2ff77` | `510a2abada13a165d404fba57a78daa67af2ff77` | identical |
| `scripts/survey_orchestrator_v2.py` | `5019b4f3d618cae6af3bc37dd7258bc5f49e1f68` | `5019b4f3d618cae6af3bc37dd7258bc5f49e1f68` | identical |

Configured DRAFT_COMPLETE contract (`config/survey-production-v2.json:330-346`):
`handler: stage:reader-publication-validation` / `validator: validate:reader-publication` /
`action_kind: LOCAL_STAGE` / `next_state: VALIDATED_DRAFT` / checkpoints `["validation"]` /
6 listed artifacts (reader-manuscript, validated-source, publication-pdf, quality-regression-bundle, semantic-review, visual-review).
State `next_action: stage:reader-publication-validation` agrees.

## 2. Default registry contents (real `register_handlers` output, 20 names)

`stage:architecture, stage:discovery, stage:drafting-synthesis, stage:evidence-materiality-completeness, stage:freeze, stage:publication-candidate, stage:release, stage:screening, stage:selection, stage:semantic-publication-validation, validate:architecture, validate:discovery, validate:drafting-synthesis, validate:evidence-materiality-completeness, validate:freeze, validate:publication-candidate, validate:release, validate:screening, validate:selection, validate:semantic-publication`

- `stage:reader-publication-validation`: ABSENT. `validate:reader-publication`: ABSENT. (Isolated test T1, real code.)
- The semantic-publication pair IS present — but no `stage_plan` lifecycle references it (verified full 10-lifecycle map;
  DRAFT_COMPLETE is the only reader stage). Registered yet unreferenced by any lifecycle: dead names for W42 purposes.

## 3. Proven mismatch (orchestrator-CLI path only)

`plan_action` (`survey_orchestrator_v2.py:289-290`) takes handler/validator verbatim from `stage_plan`, so a DRAFT_COMPLETE
Action Spec would carry the exact two identities; `execute_action` (`:531-536`) then fails closed:
`ValueError: registered handler unavailable: stage:reader-publication-validation` and
`ValueError: registered semantic validator unavailable: validate:reader-publication` (isolated test T2, real lookup lines).
No `--handler-module` registrar exists anywhere in the repo besides `survey_handlers_v2` (repo-wide grep), so the CLI flag
cannot supply the missing names from authorized in-repo code. This confirms Sol's mismatch note and the Human approval §3 premise.

## 4. Scope of the mismatch (what it does NOT prove)

The registry gap binds ONLY the orchestrator-CLI dispatch path. Whether W42 can advance depends on the authorized
operator transport, which is a different code path (see `operator-module-bridge-search-r28.md` and
`read-only-stage-contract-feasibility-r28.md`). Absence from the default registry ≠ impossibility of lawful advancement.
No alias was added, no name rebound, no validator bypassed to reach this conclusion.
