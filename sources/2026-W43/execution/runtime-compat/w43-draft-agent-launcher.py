#!/usr/bin/env python3
"""W43-only transient Draft launcher (Owner-authorized runtime compat, no Core change).

Scope: work around ONLY the diagnosed historic Screening State equality /
old direct-local validator convention collision in Draft entry, by delegating
to the FROZEN reviewed agent-first admission mechanism
(`scripts/run_drafting_synthesis_v2_agent.py` under
`survey_agent_tool_v2.current_stage_basis_override()`).

This file performs W43 admission checks, then execs the frozen wrapper with
passthrough CLI args. It does not patch, wrap, or reimplement any validator.
Shared scripts/schemas/config remain untouched.

Expected pins (verified 2026-10-28, contract sol-w43-r8-baseline-...-20261028):
  historic screening basis state_sha256:
    885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596
  profile_sha256:
    4447d25ea73ab76062028e63f91065f80c9b93886a542356c50ae54bfb10b5af
  discovery_sha256:
    f62d8459b18bba9e939db3547a24c56722b7d59c97e7dc609cd3be6a42907ae2
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


HISTORIC_STATE_SHA256 = (
    "885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596"
)
EXPECTED_PROFILE_SHA256 = (
    "4447d25ea73ab76062028e63f91065f80c9b93886a542356c50ae54bfb10b5af"
)
EXPECTED_DISCOVERY_SHA256 = (
    "f62d8459b18bba9e939db3547a24c56722b7d59c97e7dc609cd3be6a42907ae2"
)

REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT))

from scripts import survey_agent_tool_v2 as runtime_tool  # noqa: E402
from scripts import survey_production_v2 as core  # noqa: E402


def fail(msg: str) -> int:
    print(f"W43_ADMISSION_FAIL: {msg}", file=sys.stderr)
    return 1


def main(argv: list[str]) -> int:
    # Passthrough CLI mirrors the frozen interactive runner:
    #   --repo-root . --state sources/2026-W43/production-state.json --input <path>
    args = argv[1:]
    try:
        state_arg = args[args.index("--state") + 1]
    except (ValueError, IndexError):
        return fail("missing required --state <production-state.json>")
    state_path = (REPO_ROOT / state_arg).resolve()
    try:
        state_path.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return fail("state path escapes repository")

    state = json.loads(state_path.read_text())
    if state.get("issue_id") != "2026-W43":
        return fail("state issue_id is not 2026-W43")
    if state.get("lifecycle_state") != "ARCHITECTURE_ESTABLISHED":
        return fail("state is not ARCHITECTURE_ESTABLISHED")
    if state.get("human_gates", {}).get("architecture_review") != "approved":
        return fail("architecture_review gate is not approved")
    if state.get("human_gates", {}).get("publication_preview") != "pending":
        return fail("publication_preview gate is not pending")

    cfg = json.loads((REPO_ROOT / "config" / "survey-production-v2.json").read_text())
    agent_errors = runtime_tool_AGENT_validate(cfg, state)
    if agent_errors:
        return fail("agent-first validate_agent_state: " + "; ".join(agent_errors))

    profile_path = REPO_ROOT / state["profile"]["path"]
    if core.sha256_file(profile_path) != EXPECTED_PROFILE_SHA256:
        return fail("profile bytes differ from accepted pin")
    if core.sha256_file(profile_path) != state["profile"]["sha256"]:
        return fail("profile bytes differ from State pin")

    attention = json.loads(
        (REPO_ROOT / "sources/2026-W43/architecture-review-attention-v2.json").read_text()
    )
    acceptance_rel = attention["basis"]["screening_acceptance_path"]
    if core.sha256_file(REPO_ROOT / acceptance_rel) != attention["basis"][
        "screening_acceptance_sha256"
    ]:
        return fail("screening acceptance bytes differ from attention pin")
    acceptance = json.loads((REPO_ROOT / acceptance_rel).read_text())
    package_path = (REPO_ROOT / acceptance_rel).parent / "package.json"
    if core.sha256_file(package_path) != acceptance.get("package_sha256"):
        return fail("screening package copy differs from acceptance pin")
    package = json.loads(package_path.read_text())
    basis = package.get("basis", {})
    if basis.get("state_sha256") != HISTORIC_STATE_SHA256:
        return fail("screening basis state_sha256 is not the diagnosed historic value")
    if basis.get("profile_sha256") != EXPECTED_PROFILE_SHA256:
        return fail("screening basis profile_sha256 drifted")
    if basis.get("discovery_sha256") != EXPECTED_DISCOVERY_SHA256:
        return fail("screening basis discovery_sha256 drifted")
    if core.sha256_file(REPO_ROOT / basis["discovery_path"]) != EXPECTED_DISCOVERY_SHA256:
        return fail("live discovery bytes differ from accepted pin")

    current_state_sha = core.sha256_file(state_path)
    print(f"W43_ADMISSION_PASS historic_state={HISTORIC_STATE_SHA256[:12]}… "
          f"current_state={current_state_sha[:12]}… agent_state=VALID")
    print("W43_ADMISSION_PASS delegating to frozen "
          "scripts/run_drafting_synthesis_v2_agent.py (no local validator patch)")

    os.execvp(
        sys.executable,
        [sys.executable, str(REPO_ROOT / "scripts" / "run_drafting_synthesis_v2_agent.py")]
        + args,
    )
    return 1  # unreachable


def runtime_tool_AGENT_validate(cfg: dict, state: dict) -> list[str]:
    from scripts import survey_agent_control_v2 as agent

    return agent.validate_agent_state(REPO_ROOT, cfg, state)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
