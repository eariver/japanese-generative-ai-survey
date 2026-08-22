#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from scripts import survey_architecture_v2 as arch
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as attention

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources/2026-W33"
PROFILE = SRC / "production-profile.json"
STATE = SRC / "production-state.json"
LEDGER = SRC / "materiality-ledger-v2.json"
COMPLETE = SRC / "profile-completeness-v2.json"
MATRIX = SRC / "candidate-matrix-v2.json"
SELECTION = SRC / "candidate-selection-v2.json"
ARCH = SRC / "architecture-v2.json"
SUMMARY = SRC / "architecture-review-summary-v2.json"
ATTENTION = SRC / "architecture-review-attention-v2.json"
WORKLOG = ROOT / "docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md"

CYBER_PRIMARY = "candidate:2026-W33:6118ffacbd5f2ab4"
CYBER_SUPPORT_1 = "candidate:2026-W33:b585d075aee90b44"
CYBER_SUPPORT_2 = "candidate:2026-W33:ed6c8786bd01008d"
SERVING_PRIMARY = "candidate:2026-W33:4dbf548aae8b62fd"
SERVING_SUPPORT_1 = "candidate:2026-W33:5c01e3060037bcb5"
SERVING_SUPPORT_2 = "candidate:2026-W33:cff4fbabb60c45ab"
ULTRAFAST_PRIMARY = "candidate:2026-W33:8f686c0ca43adb04"

VENDOR_BOUNDARY = "Capability/performance statements are first-party vendor claims unless separately supported by independent evidence."
PROJECT_BOUNDARY = "Performance and resource numbers in release notes are project-reported and are not a cross-framework controlled benchmark."


def checkpoint_artifacts() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for checkpoint in sorted((SRC / "orchestration/v2/checkpoints").glob("*.json")):
        payload = core.load_json(checkpoint)
        for row in payload.get("artifacts", []):
            name = row["name"]
            path = ROOT / row["path"]
            existing = result.get(name)
            if existing is not None and existing.resolve() != path.resolve():
                raise ValueError(f"checkpoint artifact name divergence: {name}")
            result[name] = path
    return result


def main() -> None:
    state = core.load_json(STATE)
    if state.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError(f"expected SELECTION_COMPLETE, got {state.get('lifecycle_state')}")
    selected = core.load_json(SELECTION)
    if selected.get("summary", {}).get("selected_count") != 7:
        raise ValueError("fresh W33 Architecture requires exactly seven formally selected candidates")

    accepted = checkpoint_artifacts()
    required = {
        "discovery-acceptance",
        "screening-acceptance",
        "evidence-acceptance",
        "edition-views-acceptance",
        "materiality-ledger",
        "profile-completeness",
        "candidate-matrix",
        "candidate-selection",
    }
    missing = sorted(required - set(accepted))
    if missing:
        raise ValueError("missing accepted upstream authority: " + ", ".join(missing))

    discovery_acceptance = core.load_json(accepted["discovery-acceptance"])
    discovery = ROOT / discovery_acceptance["discovery_path"]
    screening = accepted["screening-acceptance"]
    evidence = accepted["evidence-acceptance"]
    views = accepted["edition-views-acceptance"]

    for path in (ARCH, SUMMARY, ATTENTION):
        if path.exists():
            raise ValueError(f"refusing to overwrite Architecture artifact: {path}")

    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "research_profile": "WEEKLY",
        "publication_profile": "WEEKLY_MAGAZINE",
        "status": "PROPOSED",
        "basis": {
            "production_profile_sha256": core.sha256_file(PROFILE),
            "profile_completeness_sha256": core.sha256_file(COMPLETE),
            "materiality_ledger_sha256": core.sha256_file(LEDGER),
            "candidate_matrix_sha256": core.sha256_file(MATRIX),
            "candidate_selection_sha256": core.sha256_file(SELECTION),
        },
        "editorial_thesis": "W33 is defined by operationalization rather than a single general-purpose model launch: controlled cyber capability is paired with governed access and cloud distribution, while serving-stack releases and a limited high-speed inference preview show deployment infrastructure moving in parallel.",
        "architecture_goals": [
            "Lead with the Daybreak/cyber development as a capability-plus-governance story, not as an unrestricted model launch.",
            "Explain serving-stack movement across SGLang, vLLM, and FlashInfer without constructing an unsupported cross-framework benchmark ranking.",
            "Treat Ultrafast as a limited vendor preview and preserve vendor-reported speed claims as attributed claims rather than independent performance facts.",
            "Keep abstract-only papers, official-index signals, and Grok/X community context outside the main architecture unless Human Review explicitly promotes them."
        ],
        "page_plan": {
            "target_pages": 12,
            "max_pages": 16,
            "notes": "Use three substantive packages plus front/back matter. Do not add Paper Watch or unresolved signals merely to fill the page target."
        },
        "packages": [
            {
                "package_id": "pkg-01-cyber",
                "title": "Controlled cyber capability becomes governed infrastructure",
                "purpose": "Explain Daybreak as a W33 shift where specialized cyber capability, access policy, trusted-user distribution, and AWS availability become one operational story.",
                "primary_candidate_ids": [CYBER_PRIMARY],
                "supporting_candidate_ids": [CYBER_SUPPORT_1, CYBER_SUPPORT_2],
                "must_cover_requirements": [
                    "Separate model capability from the controls governing who can use higher-risk cyber capability.",
                    "Use the trusted-hands item to explain access/distribution policy rather than treating it as a second independent model launch.",
                    "Use AWS availability as distribution evidence, not as an independent benchmark or validation of model quality."
                ],
                "boundaries": [VENDOR_BOUNDARY],
                "drafting_order": 1,
                "profile_extensions": {},
                "publication_extensions": {}
            },
            {
                "package_id": "pkg-02-serving-stack",
                "title": "Serving stack co-evolution: runtime, orchestration, and kernels move together",
                "purpose": "Synthesize SGLang, vLLM, and FlashInfer releases as coordinated W33 serving-stack movement while preserving project-specific benchmark boundaries.",
                "primary_candidate_ids": [SERVING_PRIMARY],
                "supporting_candidate_ids": [SERVING_SUPPORT_1, SERVING_SUPPORT_2],
                "must_cover_requirements": [
                    "Describe the concrete release-level engineering changes represented by each project.",
                    "Avoid cross-framework leaderboard language because workloads, hardware, and measurement conditions are not controlled across projects.",
                    "Use supporting releases to show stack-wide movement rather than duplicating three standalone release articles."
                ],
                "boundaries": [PROJECT_BOUNDARY],
                "drafting_order": 2,
                "profile_extensions": {},
                "publication_extensions": {}
            },
            {
                "package_id": "pkg-03-ultrafast",
                "title": "Ultrafast preview: inference speed becomes a product mode",
                "purpose": "Cover OpenAI's Ultrafast preview as a distinct W33 deployment/product signal while keeping its speed statement explicitly vendor-reported and preview-bounded.",
                "primary_candidate_ids": [ULTRAFAST_PRIMARY],
                "supporting_candidate_ids": [],
                "must_cover_requirements": [
                    "State that Ultrafast is a preview rather than a generalized production guarantee.",
                    "Attribute the advertised speedup to the first-party source and do not convert it into an independent benchmark conclusion.",
                    "Connect the preview to the week's infrastructure theme without conflating it with the open-source serving-stack releases."
                ],
                "boundaries": [VENDOR_BOUNDARY],
                "drafting_order": 3,
                "profile_extensions": {},
                "publication_extensions": {}
            }
        ],
        "selected_exceptions": [],
        "profile_extensions": {},
        "publication_extensions": {},
        "human_review": {
            "reviewed_by": None,
            "reviewed_at": None,
            "review_reference": None
        }
    }
    core.write_json(ARCH, payload)
    errors = arch.validate_architecture(ROOT, payload, PROFILE, COMPLETE, LEDGER, MATRIX, SELECTION)
    if errors:
        raise ValueError("Issue Architecture invalid: " + "; ".join(errors))

    implementation_sha = core.repository_commit_sha(ROOT)
    with runtime_tool.current_stage_basis_override():
        summary = arch.build_architecture_review_summary(
            ROOT,
            PROFILE,
            discovery,
            screening,
            evidence,
            views,
            LEDGER,
            COMPLETE,
            MATRIX,
            SELECTION,
            ARCH,
            implementation_sha,
        )
    if summary.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise ValueError("Architecture Review Summary is blocked: " + "; ".join(summary.get("readiness", {}).get("errors", [])))
    core.write_json(SUMMARY, summary)

    attention.build_attention(ROOT, screening, LEDGER, SELECTION, ATTENTION, limit=50)
    attention.validate_attention(ROOT, ATTENTION)

    marker = "## Fresh Architecture stage after X/Grok remediation"
    text = WORKLOG.read_text(encoding="utf-8") if WORKLOG.exists() else "# 2026-W33 Core v2 compilation session worklog\n"
    if marker not in text:
        text += (
            "\n" + marker + "\n\n"
            "- Formal Selection checkpoint reached `SELECTION_COMPLETE` after exact Matrix/Selection validation.\n"
            "- Fresh Selection contains 31 assignments: 7 `SELECTED`, 24 `HOLD`; abstract-only papers, official-index signals, and Grok/X context were not promoted as filler.\n"
            "- Proposed Architecture rebuilt from the fresh selected authority only: (1) Daybreak/cyber governance and distribution, (2) SGLang/vLLM/FlashInfer serving-stack co-evolution, (3) OpenAI Ultrafast preview.\n"
            "- Architecture retains first-party/vendor and project-reported benchmark boundaries verbatim from Candidate Matrix remaining boundaries.\n"
            "- Page plan remains 12 target / 16 maximum, but explicitly forbids Paper Watch or unresolved-signal padding.\n"
            "- `architecture-v2.json` remains `PROPOSED`; Human Review metadata is null and no Architecture Review approval is written in this stage.\n"
            "- Architecture Review Summary and bounded Review Attention are regenerated from the fresh Core v2 chain.\n"
            "- Local production workaround for historical accepted Evidence State SHA uses the repository's pending fail-closed `fix/core-v2-historical-evidence-basis` logic plus regression tests; no non-State drift is relaxed.\n"
        )
        WORKLOG.write_text(text, encoding="utf-8")

    print(ARCH)
    print(SUMMARY)
    print(ATTENTION)


if __name__ == "__main__":
    main()
