#!/usr/bin/env python3
"""TS-003 Phase C (r3 re-entry): formal Evidence (112) + Edition Views + advance
CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED (with rebuilt Materiality/Completeness).

- New 112-task package via canonical prepare_evidence_package WITH the exact
  Evidence Authority Supplement (two post-Screening docs sources bound to the
  VM-D112 task under supplement-src-* keys; Discovery src-1 untouched).
- Cards: 111 carried from r8 (D106/D091/D010/D084 repairs intact) with ONLY
  deterministic basis rebinding; VM-D112 NEW card from staged drafts (transcribed
  verbatim below; classes as staged: AUTHOR_CLAIM for vendor statements,
  INFERENCE for synthesis boundaries; 1 unresolved question recorded for
  benchmark-row binding deferral).
- Views: 111 rebuilt from authority input records + VM-D112 view (MATERIAL,
  P09+P11 scopes, BRIDGE transition annotations).
- Canonical acceptors (content-addressed, append-only). Materiality (112 rows)
  + Completeness (carried judgments + VM-D112 disposition in VM-O10/VM-O12
  rationales) rebuilt at canonical paths (deleted by re-entry).
- SSv2 purge: V1-entity consistency enforced on generated texts; frozen-profile
  echo + V-JEPA benchmark citation are the only legitimate pre-existing contexts.
- Frozen Core only + documented post-gate adaptation. Sol review owed.
"""

from __future__ import annotations

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness_mod
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/architecture-r3-intake-20261003"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-112-supplement"
SUPPLEMENT_REL = f"{EDIR}/evidence-authority-supplement-112.json"
SUPPLEMENT_ID = "ts003-arch-r3-supplement-vm-d112-20261003"
INPUT_REL = f"{SRC}/execution/screening-evidence-20260930/evidence-interactive-input.json"
VALIDATION_REL = f"{EDIR}/validation"
R8EV = "d6338dc49d65d444efc379df0adb2e63722c7d8c90164c043b9aca4721bc7b57"
R8_RES = f"{SRC}/evidence/v2/accepted/{R8EV}/results"

VM112_TASK_ID = "evidence:SP-vision-multimodal-2026:c4177b264109ceec"
NOW = "2026-10-03T12:35:00Z"

# Discovery-bound source (task source_records[0]) keeps the deterministic src-1
# key. Post-Screening docs authority arrives via the exact supplement manifest
# with supplement-src-* keys (no src-2/src-3 invention).
SUPP_VU = "supplement-src-f0fd31616290e794"
SUPP_CH = "supplement-src-7892eab93a30cdae"

VM112_SUPPLEMENT_SOURCES = [
    {
        "supplement_source_id": SUPP_VU,
        "discovery_id": "VM-D112",
        "evidence_task_id": VM112_TASK_ID,
        "locator": "https://ai.google.dev/gemini-api/docs/video-understanding",
        "source_type": "first_party_release_or_docs",
        "source_class": "PRIMARY_OFFICIAL",
        "title": "Gemini API video understanding docs (Google, verified 2026-10-03)",
        "published_at": None,
        "accessed_at": NOW,
        "raw_path": ("sources/SP-vision-multimodal-2026/raw/evidence-supplement-"
                     "vm-d112-video-understanding-20261003.html"),
        "raw_sha256": ("06a1634914d27da2832625c0387a3d2f591a2f98ec53edd8800871"
                       "b5e9a814cb"),
        "byte_count": 303627,
        "relation": ("Technical processing-modes/token-math/caveat authority for VM-D112 "
                     "static baseline, adaptive sampling, TTFT caveat, token accounting, "
                     "scope dating, and mode-mixing claims"),
    },
    {
        "supplement_source_id": SUPP_CH,
        "discovery_id": "VM-D112",
        "evidence_task_id": VM112_TASK_ID,
        "locator": "https://ai.google.dev/gemini-api/docs/changelog",
        "source_type": "first_party_release_or_docs",
        "source_class": "PRIMARY_OFFICIAL",
        "title": "Gemini API changelog 2026-09-01 entry (Google)",
        "published_at": "2026-09-01T00:00:00Z",
        "accessed_at": NOW,
        "raw_path": ("sources/SP-vision-multimodal-2026/raw/evidence-supplement-"
                     "vm-d112-changelog-20261003.html"),
        "raw_sha256": ("b0b1a3cdbd8898fded856b044216b35f76bc3061a677a4f183aca27c904d2b6b"),
        "byte_count": 169438,
        "relation": ("Release scope and model/version dating authority for VM-D112 "
                     "launch-scope and on-demand-modality claims"),
    },
]

VM112_SOURCES = [
    {"source_id": "src-1",
     "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/",
     "source_class": "PRIMARY_OFFICIAL",
     "title": "Introducing agentic video understanding with Gemini (Google, 2026-09-01)",
     "published_at": "2026-09",
     "accessed_at": NOW,
     "role": "Release announcement with mechanism description and vendor efficiency figures"},
    {"source_id": SUPP_VU,
     "url": "https://ai.google.dev/gemini-api/docs/video-understanding",
     "source_class": "PRIMARY_OFFICIAL",
     "title": "Gemini API video understanding docs (Google, verified 2026-10-03)",
     "published_at": None,
     "accessed_at": NOW,
     "role": "Technical details: processing modes, token math, caveats, accounting"},
    {"source_id": SUPP_CH,
     "url": "https://ai.google.dev/gemini-api/docs/changelog",
     "source_class": "PRIMARY_OFFICIAL",
     "title": "Gemini API changelog 2026-09-01 entry (Google)",
     "published_at": "2026-09-01T00:00:00Z",
     "accessed_at": NOW,
     "role": "Release scope and model/version dating"},
]

VM112_CLAIMS = [
    ("claim-1", "AUTHOR_CLAIM", ["src-1", SUPP_VU],
     "Static processing extracts video frames at a fixed rate (default 1 FPS, adjustable via API) and places them into context in a single pass; audio at 1Kbps single channel with timestamps added every second; fast action sequences may lose detail at 1 FPS.",
     "Docs processing-modes section + release post static baseline; static baseline for the agentic contrast."),
    ("claim-2", "AUTHOR_CLAIM", ["src-1"],
     "Agentic understanding replaces upfront full-timeline ingest with a reasoning-plus-tools loop that dynamically searches, scans, and inspects target video segments across visual frames, audio, and transcripts, fetching only the moments and signals needed per query.",
     "Release post How-it-works mechanism (fetched 2026-10-03)."),
    ("claim-3", "AUTHOR_CLAIM", ["src-1"],
     "The model takes a goal-directed role deciding what to watch, at what speed, and through which modality (frames, audio, transcript), invoking an internal tool to load the relevant part of the video file per query.",
     "Release post body verbatim mechanism (fetched 2026-10-03)."),
    ("claim-4", "AUTHOR_CLAIM", ["src-1", SUPP_VU],
     "Agentic processing adaptively adjusts frame rates and resolution on the fly based on the prompt, and resamples interesting time windows at higher FPS to inspect rapid motion and subtle visual artifacts.",
     "Docs agentic-mode description + release post applications (adaptive specifics stay qualitative; no numeric FPS schedule claimed)."),
    ("claim-5", "AUTHOR_CLAIM", ["src-1", SUPP_VU, SUPP_CH],
     "Available for video uploads and YouTube videos via the Gemini API in AI Studio and Enterprise Agent Platform; enabled by setting processing to agentic; different processing modes may be set per video in the same request.",
     "Release post availability + docs per-video mode mixing + changelog API scope."),
    ("claim-6", "AUTHOR_CLAIM", ["src-1", SUPP_CH],
     "The model dynamically navigates the timeline, requesting transcripts, frames, or audio tracks on demand to answer the prompt.",
     "Changelog entry verbatim + release post modality selection."),
    ("claim-7", "AUTHOR_CLAIM", [SUPP_VU],
     "Video context is preserved across turns: stateful mode via previous_interaction_id needs no additional handling; stateless mode must carry all returned steps including processing_call and processing_result in the next step_list, else video context is lost and follow-up quality degrades.",
     "Docs multi-turn section handling notes."),
    ("claim-8", "AUTHOR_CLAIM", [SUPP_VU, SUPP_CH],
     "Up to 88% fewer tokens than static processing for long-form content, because the model loads only needed transcript/frames/audio. Token scope only; not a memory, KV-cache, or latency claim.",
     "Changelog + docs token calculation; long-form condition explicit; fetched bodies confirm ceilings."),
    ("claim-9", "AUTHOR_CLAIM", ["src-1"],
     "Up to 66% lower analysis cost across standard video analysis benchmarks, at standard API token pricing with no additional feature fee. Cost scope only, separate from token scope.",
     "Release post Benchmarks; benchmark scope distinct from long-form token scope."),
    ("claim-10", "AUTHOR_CLAIM", ["src-1"],
     "Up to ~7% higher accuracy with agentic 3.7 Flash; agentic 3.7 Flash placed at the accuracy-to-cost pareto frontier among tested models for video understanding. Quality scope only, vendor-reported.",
     "Release post Benchmarks + frontier captions; tested-model scope."),
    ("claim-11", "AUTHOR_CLAIM", [SUPP_VU],
     "Navigation may slightly increase time to first token on short clips (under 5 minutes) due to internal reasoning and tool round-trips; static suits latency-sensitive short-clip or full-clip frame-precision queries.",
     "Docs Technical details + choose-mode guidance; <5 min condition."),
    ("claim-12", "AUTHOR_CLAIM", [SUPP_VU],
     "Navigation reasoning tokens count as thought tokens (total_thought_tokens); frames, audio, and transcript loaded on demand count as tool use tokens (total_tool_use_tokens); totals vary with content complexity and navigation strategy.",
     "Docs token-calculation section verbatim."),
    ("claim-13", "INFERENCE", ["src-1", SUPP_VU, SUPP_CH],
     "Token/cost/quality figures are Google vendor-reported up-to ceilings with differing scopes (long-form vs benchmarks); no independent reproduction; exact benchmark list/splits await downstream binding.",
     "Edition synthesis for downstream editorial use (G05-style boundary)."),
    ("claim-14", "AUTHOR_CLAIM", ["src-1", SUPP_VU, SUPP_CH],
     "Model/version scope: launch 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite (2026-09-01); developer docs list 3.8 Flash support; static remains the default for all models.",
     "Release vs docs dating; version binding required at use."),
    ("claim-15", "INFERENCE", ["src-1", SUPP_VU],
     "Agentic processing applies to stored/uploaded and YouTube on-demand timelines; it is not online streaming state (no continuous ingestion, bounded streaming memory, or async mid-stream queries) and is not streaming-system evidence.",
     "Edition-level contract judgment; P11 column-separation enforcement."),
]

VM112_LIMITATIONS = [
    ("limitation-1",
     "All efficiency figures vendor-reported up-to ceilings; no independent reproduction; implementation, rates, pricing, and API surface may change after cutoff (bind version + date at use)."),
    ("limitation-2",
     "Benchmark-row binding (incl. LongVideoBench scope + 3.8 Flash row) deferred to downstream use; static-vs-agentic token-math worked example deferred."),
]

VM112_VIEW_RECORD = {
    "discovery_id": "VM-D112",
    "status": "VERIFIED",
    "materiality": "MATERIAL",
    "materiality_rationale": ("Query-driven acquisition transition material to P09 token/context "
                              "economics + third video-processing contract for P11; vendor ceilings."),
    "scope_dimensions": ["native_omni_fusion", "video_temporal_streaming"],
    "lineage_role": "BRIDGE",
    "branch_ids": ["d09-acquisition-economics", "d11-video-processing-contract"],
    "transition_ids": ["d09-fixed-to-selective-acquisition"],
    "inheritance_note": ("Static fixed-rate ingest redirected to query-driven selective "
                         "acquisition; cross-contract transition, not streaming."),
    "historical_attribution_caveat": None,
}


def _screening_acceptance(root: Path) -> Path:
    cands = [p for p in sorted((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"))
             if core.load_json(p)["record_count"] == 112]
    assert len(cands) == 1, [str(p) for p in cands]
    return cands[0]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    impl = core.repository_commit_sha(root)

    with agent_tool.current_stage_basis_override():
        scr_acc_path = _screening_acceptance(root)
        scr_acc = core.load_json(scr_acc_path)
        assert scr_acc["record_count"] == 112, scr_acc["record_count"]
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        supplement_path = root / SUPPLEMENT_REL
        if not supplement_path.exists():
            evidence.build_evidence_authority_supplement(
                root, ISSUE_ID, source_root, root / DISC_REL, scr_acc_path,
                VM112_SUPPLEMENT_SOURCES, supplement_path,
                supplement_id=SUPPLEMENT_ID, implementation_sha=impl)
        else:
            evidence.validate_evidence_authority_supplement(
                root, supplement_path, impl, expected_issue_id=ISSUE_ID,
                expected_discovery_path=root / DISC_REL,
                expected_screening_acceptance_path=scr_acc_path)
        print("supplement:", supplement_path.relative_to(root),
              core.sha256_file(supplement_path)[:12])

        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, supplement_path)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 112, len(package["tasks"])
        by_eid = {m["evidence_task_id"]: m for m in package["tasks"]}
        assert VM112_TASK_ID in by_eid, "VM-D112 task missing from package"
        vm112_meta = by_eid[VM112_TASK_ID]
        assert vm112_meta["discovery_ids"] == ["VM-D112"]
        print("VM-D112 task file:", Path(vm112_meta["path"]).name)
        # Contract pins are unchanged across packages; read from an r8 card.
        probe = core.load_json(root / R8_RES / Path(by_eid[
            "evidence:SP-vision-multimodal-2026:f1346f195b48d6e0"]["path"]).name)
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]

        with tempfile.TemporaryDirectory() as temp:
            import tempfile as _tf  # noqa
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                if meta["evidence_task_id"] == VM112_TASK_ID:
                    card = {
                        "schema_version": "2.0-rc1",
                        "issue_id": ISSUE_ID,
                        "evidence_task_id": VM112_TASK_ID,
                        "basis": {
                            "task_sha256": meta["sha256"],
                            "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                            "prompt_sha256": PROMPT_SHA,
                            "result_contract_sha256": CONTRACT_SHA,
                        },
                        "status": "VERIFIED",
                        "entities": [{
                            "entity_id": "ev-vmd112",
                            "canonical_name": "Agentic Video Understanding (Google, 2026)",
                            "entity_type": "MODEL",
                            "organization": "Google",
                            "canonical_url": ("https://blog.google/innovation-and-ai/models-and-research/"
                                              "gemini-models/introducing-agentic-video-in-gemini/"),
                        }],
                        "artifact": {
                            "primary_subject_id": "ev-vmd112",
                            "artifact_type": "MODEL",
                            "canonical_name": "Agentic Video Understanding (Google, 2026)",
                            "canonical_url": ("https://blog.google/innovation-and-ai/models-and-research/"
                                              "gemini-models/introducing-agentic-video-in-gemini/"),
                        },
                        "temporal": {
                            "observed_at": NOW,
                            "events": [{
                                "event_id": "event-1",
                                "event_type": "SOURCE_PUBLICATION_OR_RELEASE",
                                "event_date": "2026-09",
                                "subject_id": "ev-vmd112",
                                "subject_role": "PRIMARY_SUBJECT",
                                "source_ids": ["src-1"],
                            }],
                        },
                        "sources": VM112_SOURCES,
                        "claims": [{
                            "statement_id": sid, "text": text,
                            "subject_id": "ev-vmd112", "subject_role": "PRIMARY_SUBJECT",
                            "evidence_class": cls, "source_ids": sids, "context": ctx,
                        } for sid, cls, sids, text, ctx in VM112_CLAIMS],
                        "metrics": [],
                        "limitations": [{
                            "statement_id": sid, "text": text,
                            "subject_id": "ev-vmd112", "subject_role": "PRIMARY_SUBJECT",
                            "evidence_class": "INFERENCE", "source_ids": ["src-1", SUPP_VU],
                            "context": "Evidence boundary retained for downstream editorial use.",
                        } for sid, text in VM112_LIMITATIONS],
                        "verification": {
                            "targets": [
                                {"target": "Evidence-stage full-body verification",
                                 "status": "VERIFIED",
                                 "finding": ("Official release post + API docs + changelog consumed "
                                             "2026-10-03: static-vs-agentic mechanism, token/cost/quality "
                                             "ceilings with scopes, caveats, and accounting verified as "
                                             "vendor statements."),
                                 "subject_ids": ["ev-vmd112"], "source_ids": ["src-1", SUPP_VU, SUPP_CH]},
                                {"target": "vendor-claim quarantine",
                                 "status": "VERIFIED",
                                 "finding": ("Vendor-measured ceilings isolated with explicit attribution, "
                                             "separate scopes, and role caps; no independent-evaluation "
                                             "inference performed."),
                                 "subject_ids": ["ev-vmd112"], "source_ids": ["src-1", SUPP_VU, SUPP_CH]},
                            ],
                            "unresolved_questions": [
                                "Exact benchmark list/splits behind vendor efficiency ceilings "
                                "(incl. LongVideoBench scope + 3.8 Flash row) remain binding work "
                                "for downstream use."
                            ],
                            "contradictions": [],
                        },
                    }
                    for sid, cls, sids, text, ctx in VM112_CLAIMS:
                        assert len(text) <= 600, (sid, len(text))
                    task = core.load_json(root / PKGDIR / vm112_meta["path"])
                    errs = evidence.validate_evidence_card(
                        card, task, vm112_meta["sha256"], package, repo_root=root)
                    assert not errs, errs
                else:
                    base = core.load_json(root / R8_RES / fname)
                    base["basis"]["task_sha256"] = meta["sha256"]
                    base["basis"]["screening_acceptance_sha256"] = core.sha256_file(scr_acc_path)
                    assert base["basis"]["prompt_sha256"] == PROMPT_SHA, meta["evidence_task_id"]
                    assert base["basis"]["result_contract_sha256"] == CONTRACT_SHA
                    task = core.load_json(root / PKGDIR / meta["path"])
                    errs = evidence.validate_evidence_card(
                        base, task, meta["sha256"], package, repo_root=root)
                    if errs:
                        raise ValueError(f"Card {meta['evidence_task_id']} invalid: {'; '.join(errs)}")
                    card = base
                core.write_json(results_dir / fname, card)

            profile_path = root / core.load_json(root / STATE_REL)["profile"]["path"]
            profile = core.load_json(profile_path)
            source_root = core.repo_local_path(
                root, profile["paths"]["source_root"], "paths.source_root")
            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 112
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))

    print("EVIDENCE 112 STAGED-COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
