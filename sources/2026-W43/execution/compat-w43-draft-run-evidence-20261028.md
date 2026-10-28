# W43 Draft run evidence — Owner-authorized runtime compat (2026-10-28)

Authority:
`sol-w43-r8-baseline-to-publication-ready-integrated-muse-general-contract-20261028.md` §3
plus `sol-w43-runtime-only-draft-basis-compat-fast-recovery-20261028.md` (Owner: bypass allowed,
no comprehensive extra test suite; minimal factual verification mandatory).

## 0. Mechanism actually used (narrower than a new monkeypatch)

No new validator patch was written. The W43-only launcher
`sources/2026-W43/execution/runtime-compat/w43-draft-agent-launcher.py`
performs edition-local admission checks and then `exec`s the **frozen reviewed**
`scripts/run_drafting_synthesis_v2_agent.py` (present in frozen Core
`774dd39a` and reviewed main `041a08df`), which runs the unmodified
`run_drafting_synthesis_v2_interactive.py` under frozen
`survey_agent_tool_v2.current_stage_basis_override()`.

That frozen override tolerates **exactly**
`Screening package basis drift: state_sha256` when the sibling
`screening-accepted.json` binds the exact package SHA, substitutes the current
State SHA, re-runs the original validator, and replaces `verify_state_basis`
with the agent-first `validate_agent_state`. All package-content hash checks
(prompt, result contract, archived batches/results, profile/discovery root)
remain the original frozen logic. No module was "temporarily adapted": zero
`scripts/` edits, zero in-process patch invented by this run.

Note: launcher `W43_ADMISSION_PASS` banner lines were lost to stdout buffering
across `os.execvp` (unflushed pipe buffer discarded on exec). Admission success
is proven by the exec path being reached (any failure exits 1 before exec) and
by the independent re-verification of all pins below.

## 1. Command and exit

```text
PYTHONPATH=<repo> python3 sources/2026-W43/execution/runtime-compat/w43-draft-agent-launcher.py \
  --repo-root . --state sources/2026-W43/production-state.json \
  --input sources/2026-W43/execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json
```

Exit: `0`. Runner printed the 8-package JSON summary (P1–P8 package/result
pairs + synthesis input/result + archive). Zero writes outside
`sources/2026-W43/draft/v2/`; no State/Gate/metrics mutation
(runner never advances Production State by design).

## 2. Admission pins verified (pre-exec, re-verified read-only)

| Item | Value |
|---|---|
| State `issue_id` / `lifecycle_state` | `2026-W43` / `ARCHITECTURE_ESTABLISHED` |
| `human_gates` | architecture_review=approved, publication_preview=pending |
| Agent-first `validate_agent_state` | VALID (zero errors) |
| Screening acceptance (attention-pinned SHA match) | `75dd95db…/screening-accepted.json`, package `b7e9a6d4…` |
| Historic basis `state_sha256` | `885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596` |
| Current State SHA | `b0450d25b9dd4db8424d1c92d713d28c1b268b4e6a3b960a053f9684bb3eebb6` |
| Basis `profile_sha256` vs live profile | MATCH `4447d25e…` |
| Basis `discovery_sha256` vs live discovery JSONL | MATCH `f62d8459…` |

## 3. Input provenance

Provisional input (diagnostic evidence, NOT production authority):
`execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json`
SHA256 `d1cb5277e9243d0feb04f585be8d316e0f6137b2ebd5c9d4763d68760690c409`
(8 packages P1–P8, 113 blocks, `draft_version v1.0`, `issue_id 2026-W43`).

Runner-archived copy `draft/v2/interactive-drafting-synthesis-input.json`
SHA256 `3238daf825ce9c14b9a269ba21989e4cb89958c681b44caab24cea8e50175735`
— byte-different (re-serialization only), JSON-semantically identical
(`a == b` verified in Python).

## 4. Genuine native outputs (all ESTABLISHED)

| Path | SHA256 |
|---|---|
| `sources/2026-W43/draft/v2/packages/P1/draft-package.json` | `2dc11f288d248eef220b9caf30ba3153b9f9de43b92b5bab686c796be5d8893e` |
| `sources/2026-W43/draft/v2/packages/P1/draft-result.json` | `ea83738181f84fda639be656ec5979968259422afb1f33dd1fa1c6a9676592c6` |
| `sources/2026-W43/draft/v2/packages/P2/draft-package.json` | `b62731216ba6572beabcca2d7b58fdbd785eb852edac795886f56731ac107e8d` |
| `sources/2026-W43/draft/v2/packages/P2/draft-result.json` | `120170d66a8aba6cbcf23679fab6b7e0597cf6fb00f803f3257c0abb4a901852` |
| `sources/2026-W43/draft/v2/packages/P3/draft-package.json` | `85ce0714667663b7c40e175d50855fc570a9ab3af31fd7b5cbf13d04af0465c5` |
| `sources/2026-W43/draft/v2/packages/P3/draft-result.json` | `ece07deb33899061a9ab98e5ed838b477e597b523397c2653f82951a0ae76e11` |
| `sources/2026-W43/draft/v2/packages/P4/draft-package.json` | `dc845e52b7c85776f21a8cc01237ff9e943a9a130d8c5ac04b3ee2d80f21701f` |
| `sources/2026-W43/draft/v2/packages/P4/draft-result.json` | `ea8566583d76beb90e9b464c4c08047f8b08db2f6dabc23efe83674e17d57aba` |
| `sources/2026-W43/draft/v2/packages/P5/draft-package.json` | `07769617d5f03a90d9d46921e0cacb75bd0da07a1761d81285060d6d0a7a83f8` |
| `sources/2026-W43/draft/v2/packages/P5/draft-result.json` | `9e7a03b0cad03af0433b413872d1a2345e9dcdccd04ceefefd489cb42e2e4d3d` |
| `sources/2026-W43/draft/v2/packages/P6/draft-package.json` | `dd68b7a8e68d948e144dd4ba7ae1bdd3fd59b104d3cce5c09f4350688eaa11bf` |
| `sources/2026-W43/draft/v2/packages/P6/draft-result.json` | `5027d5d591334a370aa637244130d465d7e7c45e9b3f5069a2fd598fcefc28fb` |
| `sources/2026-W43/draft/v2/packages/P7/draft-package.json` | `0dda680c12c1531962cd61aa91d0dc826133b54606ae46e2073ecdccbf4146d2` |
| `sources/2026-W43/draft/v2/packages/P7/draft-result.json` | `b536e643fb454a35b768df48e57edb12372b80926e2c85a9519efe965d49b71d` |
| `sources/2026-W43/draft/v2/packages/P8/draft-package.json` | `5014416cf187adc9c21c8928eda43da405cbee5742425a3b751dae2f10aab73a` |
| `sources/2026-W43/draft/v2/packages/P8/draft-result.json` | `f08a356198d16b31d0d27da1cbffc085d6e6721e33e2dd5772c80b84775a4ea2` |
| `sources/2026-W43/draft/v2/profile-synthesis-input.json` | `e31fa783aa1825c690273e405968684f685e2c30385ccc1aabfa895c8f9bd816` |
| `sources/2026-W43/draft/v2/profile-synthesis-result.json` | `30ae6b9e55c919975a051e3935d7f1b2cbcc0d83c596356f2dcf744e59bf81dd` |

All 8 draft-results: `status ESTABLISHED`, `draft_version v1.0`.
Synthesis: `status ESTABLISHED`, `synthesis_version v1.0`
(`publication_payload` empty — same as W42 r10 native pattern).

## 5. Native validations that actually ran (exit 0 = all PASS)

- Agent-first `validate_agent_state` on current State: VALID.
- Frozen `_resolve_effective_screening_discovery` (via override-tolerated
  `validate_package_basis`): PASS — profile/discovery/prompt/result-contract/
  archive checks all original logic.
- Frozen `derive_draft_package` ×8 + `validate_draft_result` ×8 +
  synthesis input/result validation: PASS.

## 6. Provenance boundary (honest limitations)

- Compat scope: exactly the diagnosed historic-vs-current `state_sha256`
  equality plus old direct-local `verify_state_basis` convention, at Draft
  entry only. No broader bypass, no catch-all suppression, no fake PASS.
- Reader-content caveat: provisional input predates the approved r8 proof
  (~22,185 body chars vs r8's full 22-page narrative + 5-paragraph recap).
  Native Draft results are genuine stage authority, NOT a claim of
  r8-equivalence. The r8→candidate reader mapping (§4 of the integrated
  contract) is produced separately before Candidate assembly.
- Fixed r8 proof, accepted research, State, Gates, shared Core: untouched.
- `scripts/__pycache__/` bytecode from the run removed.
