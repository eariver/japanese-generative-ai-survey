# Muse pre-Human upstream authority feasibility (W43 Metrics cutoff)

Status: `READ_ONLY_FEASIBILITY / NO_CORE_CHANGE / NO_STAGE_ADVANCE`
Date: 2026-10-25. State `CANDIDATES_NORMALIZED` (Discovery/Screening passed; Evidence pending; Gates pending). This document decides nothing; Sol decides the canonical contract.

## Reviewed authority

- Frozen `scripts/survey_production_v2.py::transition_state` (verbatim): `target_index != current_index + 1` → `non-monotonic transition refused: exactly one forward step is required`. No backward move; `LIFECYCLE` has no rewind. State provenance + `LIFECYCLE` + checkpoint attestation enforced via `verify_state_basis`.
- Frozen `scripts/survey_core_execution_bridge_v2.py::execute_request`: allowlist `INITIALIZE_WEEKLY/RETROSPECTIVE/THEMATIC` + `ADVANCE_STAGE` + 4 Human Gate kinds (`RECORD_ARCHITECTURE_APPROVAL`, `REQUEST_ARCHITECTURE_REVISION`, `RECORD_PUBLICATION_PREVIEW_APPROVAL`, `REQUEST_PUBLICATION_PREVIEW_REVISION`). **No `INVALIDATE_STAGE` kind** (`unsupported operator bridge operation` otherwise). W43 receipts `sol-w43-discovery-advance-20261025` + `sol-w43-screening-advance-20261025` are `ADVANCE_STAGE` PASS only.
- Frozen `scripts/survey_human_gate_v2.py::invalidate_pending_gate`: requires `_current_pending_gate == gate`, Architecture checkpoint passed for `ARCHITECTURE_REVIEW`, no prior Human reviews, exact HEAD/branch-head, gate-input surface. Config `operator_pending_gate_invalidation_boundaries: ARCHITECTURE_REVIEW [ISSUE_INITIALIZED..EVIDENCE_REVIEWED..SELECTION_COMPLETE]`, `PUBLICATION_PREVIEW []`. W43 is **not at either pending gate** → mismatch → fail-closed. `REQUEST_*_REVISION` require real Human decisions at their gates (none made; creating one is prohibited).
- Frozen `survey_agent_tool_v2` / `survey_agent_control_v2` / `survey_stage_validation_v2` / `survey_discovery_v2` / `survey_screening_v2` + frozen profile/State schemas read; W34 `docs/checkpoints/2026-09-05-core-v2-pre-human-evidence-regeneration-repair-validation-r1.md` is a **pre-Human Architecture Gate** Core-maintenance candidate (pending-gate invalidation + supplements + checkpoint-bound active resolution), **not available** at pre-gate W43. Issues #568/#569 remain OPEN (no edition workaround).
- W43 checkpoints `DISCOVERY_COLLECTED` + `DISCOVERY_COLLECTED` (Screening) PASS; accepted Discovery/Screening/Evidence r3 authority graph is trusted history; canonical files immutable.

## Human decision

- NONE. No Human Gate operation requested, recorded, or inferred. No `ADVANCE_STAGE`, invalidation, revision, Selection, Architecture, Draft, PDF.

## Requested changes

- None executed. The only lawful next step is Sol's single bounded canonical remediation contract after this feasibility (possibly separate Core maintenance + Human/operator consent). No Evidence r4, no Screening rerun, no derived-only bypass executed.

## Regeneration boundary

- No regeneration executed. If Sol later authorizes: boundary must be explicit upstream authority restoration (not silent Evidence rewrite), with superseded-history preservation + machine provenance re-attestation + parent/child hash-graph rebuild + fail-closed tamper checks + genuine operator/Human consent as applicable. Until then `CANDIDATES_NORMALIZED` with pending Evidence is the only truthful State.

## Shared-Core implication

- Design A — native operator rewind/invalidation at `CANDIDATES_NORMALIZED`: **NOT_SUPPORTED_UNDER_FROZEN_CORE**. Proof: `transition_state` refuses non-`+1`; bridge has no `INVALIDATE_STAGE`; `invalidate_pending_gate` gate-mismatches (not at Architecture/Publication). No explicit backward operator path exists.
- Design B — forward-only append-only editorial correction/exclusion (e.g., View → NON_MATERIAL/CONTEXT, ledger note) **without** changing accepted Discovery/Screening: **NOT Sufficient as authority repair**. Proof: `build_materiality_ledger` derives non-DROP rationale as tautology but Screening `reason` (`Fresh in-window lead`) + Discovery `published_at 2026-10-23` + `MAIN_EVENT` View premise remain trusted upstream; `validate_stage` (`_evidence_basis`) revalidates Screening→Evidence→Views→ledger→completeness chain against those authorities — a downstream label change does not invalidate or supersede the false IN premise. Claiming it cures provenance would be a manufactured PASS.
- Design C — separately reviewed Core maintenance and/or new explicit operator authority with Human control: **ONLY lawful path if pursued; NOT executed here**. Requires: exact frozen diff isolated to Core (not edition files), trust provenance (reviewed main + tests + work-branch reachability + dual-transport bootstrap per final-audit rule), checkpoint/State re-attestation design, 51-Screening + 32-Evidence regeneration order, hash-graph parent/child updates, tamper tests, and genuine user/Human approval where lifecycle requires. Until such maintenance is reviewed/integrated, report **`AUTHORITY_RESTORATION_UNSUPPORTED_UNDER_FROZEN_CORE`** and remain BLOCKED; do not run unsafe alternatives (State/JSON rewrite, checkpoint deletion, acceptance overwrite, branch reset/force, Human Gate fabrication, derived-only PASS).
- Ancillary: supplement `published_at` nullable → `DATE_ONLY_PLACEHOLDER_NOT_OBSERVED_CLOCK` labeling is schema-supported for future authority; but relabeling alone (even via valid Core accept) does not retroactively cure accepted Discovery/Screening IN premise without B/C authority decision. No Core edits made; W34 candidate not reused as edition patch.

## IA-017 / IA-018 / residual P2 (no churn)

- IA-017 (P2 LIMITED): Kimi claims 1–4 → `src-1` (fused Discovery provenance `X post + blog`, immutable) + `supplement-src-041ec6c5600beb4d` (blog exact `https://www.kimi.ai/blog/kimi-k3-1-pro`, 390347B; excerpt: `Full model weights will be released by Nov 4`, `1M-token context`, `Highspeed 2-3x`); X-only facts (17:15:24Z, 4h44m36s, `2.8T/104B`, post ID) belong to `src-1` X leg. Flint claims 1–3 → `src-1` (fused `article + HF card`, immutable) + `supplement-src-d2d2f48e181fb4dd` (article `https://recursive.com/updates/introducing-recursive-flint`, 366583B; excerpt `up to 512k / within 256k`, `125+ M4 Pro / 150+ RTX Spark short-context 128K-avg prefill-excluded`) + `supplement-src-e1fe975d225aaa88` (card `https://huggingface.co/RecursiveSI/flint`, 6250B; `39.8B/2.5B`, `262144`, `Apache-2.0`). Card schema still carries `src-1` internally as Discovery provenance; reader citations must use exact supplement IDs + URLs above, never the fused locator. Unproven benches/unreleased weights excluded.
- IA-018 erratum: `interactive-evidence-r2.json → r3.json` = **19 substantive / 13 rationale-only / 0 identical** (verified by JSON compare). All 32 accepted Card SHAs differ because package/basis/acceptance regenerated — not 32 claim edits. Prior closure `20 changed / 12 same` (accepted-Card text compare) is superseded for semantic inputs; old files unchanged (append-only erratum).
- Residual 5 LIMITED (GCP date conflict, fused refs, v1-v2 deltas, Duet/1Password live integration, licenses/weights-OSI) stay LIMITED absent new conflicting primaries; no P1 escalation, no AM-Bench/Oracle full-diff, no repro, no Selection; Grok NON_MATERIAL.
