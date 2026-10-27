# Session — Muse W43 integrated contract: guard verification + native Draft (2026-10-28)

Contract: `execution/instructions/sol-w43-r8-baseline-to-publication-ready-integrated-muse-general-contract-20261028.md`
(plus Owner fast-recovery `sol-w43-runtime-only-draft-basis-compat-fast-recovery-20261028.md`).

## 1. Guard verification (all PASS, read-only first)

Local HEAD was `88e791258` (2 behind remote). `git fetch origin` revealed
remote `weekly/2026-W43-v2-work` = `284aed8b7e08346257b9f66952cdb7b8b6b51ef8`
(the contract's exact starting HEAD; initial "object not found" was a stale
local clone, resolved by fetch — no fabrication).

| Guard | Expected | Actual | Verdict |
|---|---|---|---|
| Work HEAD / Tree | `284aed8b…` / `101ca977…` | identical | PASS |
| Pre-contract parent | `fd1833c79…` / `85d82582…`, single-file contract addition | identical (`--stat`: 1 file, +185) | PASS |
| `origin/main` HEAD / Tree | `041a08df…` / `a134dc36…` | identical (local `main` ref was stale; `origin/main` authoritative) | PASS |
| Frozen `production/survey-core-v2` | `774dd39a…` / `cd46a6f7a…` | identical | PASS |
| Fixed r8 HEAD / Tree | `953a9d33…` / `dfafff50…` | identical | PASS |
| Fixed r8 PDF SHA256 | `abd5b99b…` (487351B, 22p) | `git show 284aed8b:…r8/main.pdf \| sha256sum` identical | PASS |
| State at post-contract HEAD | ARCHITECTURE_ESTABLISHED, arch approved, preview pending, exception inactive | identical | PASS |

Clean tree confirmed; `git merge --ff-only origin/weekly/2026-W43-v2-work`
→ `284aed8b…`/`101ca977…`. No reset/rebase/force/new-branch.

## 2. Research (no restart)

Read approved `architecture-v2.json` (8 packages P1–P8), attention basis
(screening acceptance `75dd95db…`, package `b7e9a6d4…`), defect records
(drafting basis drift; screening prepare basis), frozen runner/validator code,
and W42 precedent (native trusted RELEASE_CANDIDATE via operator bridge;
r34 compat Freeze is NOT reused — different defect family).

Key find: frozen reviewed `scripts/run_drafting_synthesis_v2_agent.py` +
`survey_agent_tool_v2.current_stage_basis_override()` is the canonical
agent-first admission for exactly this Screening→Draft historic-State mismatch
(W42 r10 precedent). The W43 launcher therefore delegates to frozen authority
instead of inventing a new monkeypatch — narrower than the contract's maximum
allowance, fully within the Owner's "bypass, no comprehensive suite" grant.

## 3. Draft execution

Provisional input verified (8 pkgs, exact field sets, `issue_id 2026-W43`);
screening basis pins verified (historic `885927bd…` vs current `b0450d25…`,
profile/discovery MATCH). Ran W43 launcher → frozen agent wrapper → exit 0:
8 `draft-package.json` + 8 `draft-result.json` (all ESTABLISHED v1.0) +
synthesis input/result (ESTABLISHED v1.0, empty `publication_payload` per
native pattern). Evidence: `execution/compat-w43-draft-run-evidence-20261028.md`.
`scripts/__pycache__/` removed.

Provenance boundary kept: r8 proof untouched; native results are genuine stage
authority, NOT an r8-equivalence claim (reader mapping follows separately).

## 4. Next

Commit launcher + draft + evidence + this session + index (normal commit,
non-force push, remote read-back). Then ADVANCE_STAGE #1
(ARCHITECTURE_ESTABLISHED → DRAFT_COMPLETE, 18 artifacts) via trusted
Issue #448 operator transport with immutable request-only commit.

Terminal so far: `MUSE_W43_DRAFT_ARTIFACTS_READY_FOR_STAGE` (Stage still
ARCHITECTURE_ESTABLISHED — transition only via trusted bridge PASS).
