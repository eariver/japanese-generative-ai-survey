"""Regression tests for generic reviewed-Draft supersession authority.

Covers instruction T1-T20 plus negative cases on synthetic generic fixtures
(WEEKLY and THEMATIC/LONGFORM shapes prove profile/path genericity).
No edition-specific conditionals exist in the implementation; the T19 test
proves it functionally. Uses real generic Draft validators throughout.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pypdf

from scripts import survey_agent_control_v2 as agent
from scripts import survey_draft_revision_v2 as draft_revision
from scripts import survey_drafting_v2_base as drafting_base
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_quality_v2 as quality
from scripts import survey_reader_publication_v2 as reader
from scripts import survey_stage_validation_v2 as stage_validation

T0 = datetime(2026, 10, 3, 12, 0, 0, tzinfo=timezone.utc)
EXECUTOR = "draft-revision-regression-fixture"

PRODUCERS = [
    ("discovery", "ISSUE_INITIALIZED", "DISCOVERY_COLLECTED"),
    ("screening", "DISCOVERY_COLLECTED", "CANDIDATES_NORMALIZED"),
    ("evidence", "CANDIDATES_NORMALIZED", "EVIDENCE_REVIEWED"),
    ("materiality", "CANDIDATES_NORMALIZED", "EVIDENCE_REVIEWED"),
    ("completeness", "CANDIDATES_NORMALIZED", "EVIDENCE_REVIEWED"),
    ("selection", "EVIDENCE_REVIEWED", "SELECTION_COMPLETE"),
    ("architecture", "SELECTION_COMPLETE", "ARCHITECTURE_ESTABLISHED"),
    ("draft", "ARCHITECTURE_ESTABLISHED", "DRAFT_COMPLETE"),
]

RESEARCH_PROFILES = {
    "WEEKLY": ("WEEKLY", "WEEKLY_MAGAZINE", "2026-W35",
               {"mode": "ROLLING_WINDOW",
                "window_start": "2026-09-24T00:00:00Z",
                "window_end": "2026-10-01T00:00:00Z",
                "cutoff": "2026-10-01T00:00:00Z",
                "timezone": "UTC"}),
    "THEMATIC": ("THEMATIC", "LONGFORM_SPECIAL", "2026-TM-FIX",
                 {"mode": "OPEN_HISTORY_AS_OF", "as_of": "2026-10-01T00:00:00Z"}),
}


def _hex(n: int) -> str:
    return f"{n:040x}"


class Fixture:
    """Minimal synthetic DRAFT_COMPLETE edition with real Draft validators passing."""

    def __init__(self, root: Path, base: Path, profile_key: str = "WEEKLY",
                 survey_dirname: str = "survey") -> None:
        research, publication, issue, temporal = RESEARCH_PROFILES[profile_key]
        self.repo = root
        self.cfg = core.load_json(root / core.DEFAULT_CONFIG)
        self.base = base
        self.research = research
        self.publication = publication
        self.issue = issue
        self.src = self.base / "src"
        self.survey = self.base / survey_dirname
        self.src.mkdir(parents=True)
        self.survey.mkdir(parents=True)
        (self.src / "draft" / "v2" / "packages" / "pkg-a").mkdir(parents=True)
        (self.src / "draft" / "v2" / "packages" / "pkg-b").mkdir(parents=True)
        (self.src / "gates").mkdir(parents=True)
        (self.src / "orchestration" / "v2" / "checkpoints").mkdir(parents=True)
        (self.src / "execution" / "reviews").mkdir(parents=True)
        (self.src / "publication" / "v2" / "deterministic").mkdir(parents=True)
        self.profile = self._profile(temporal)
        core.write_json(self.src / "production-profile.json", self.profile)
        self._upstream_files()
        self._evidence_authority()
        self._architecture_files()
        self._approval_files()
        self._draft_packages()
        self._draft_results_v1()
        self._synthesis_v1()
        self._review_file()
        self._write_state(provisional=True)
        self._checkpoint_records()
        self._write_state(provisional=False)

    # -- profile / upstream -------------------------------------------------
    def _profile(self, temporal: dict) -> dict:
        return {
            "schema_version": self.cfg["schema_version"],
            "issue_id": self.issue,
            "research_profile": self.research,
            "publication_profile": self.publication,
            "research_scope": {
                "question": "Can reviewed Draft bytes be rebound without rewriting history?",
                "inclusion": ["draft revision"],
                "exclusion": ["upstream research"],
                "scope_dimensions": ["revision"],
                "initial_obligations": [
                    {"obligation_id": "ob-1", "dimension": "revision",
                     "description": "rebind safely"}
                ],
                "temporal_policy": temporal,
            },
            "paths": {
                "source_root": str(self.src.relative_to(self.repo)),
                "survey_root": str(self.survey.relative_to(self.repo)),
                "work_branch": "test/draft-revision",
            },
            "contract": {
                "pipeline_contract_version": "2.0-rc1",
                "quality_contract_version": "2.0-rc1",
                "research_profile_version": "2.0-rc1",
                "publication_profile_version": "2.0-rc1",
                "pipeline_contract_sha256": "0" * 64,
                "quality_contract_sha256": "0" * 64,
                "research_profile_sha256": "0" * 64,
                "publication_profile_sha256": "0" * 64,
            },
        }

    def _upstream_files(self) -> None:
        import json as _json
        (self.src / "discovery.json").write_text('{"accepted": true}', encoding="utf-8")
        (self.src / "screening.json").write_text('{"accepted": true}', encoding="utf-8")
        for name in ("evidence.json", "views.json", "ledger.json", "completeness.json",
                     "selection.json", "matrix.json"):
            (self.src / name).write_text(_json.dumps({"fixture": name}), encoding="utf-8")

    def _matrix_file(self) -> None:
        import json as _json
        (self.src / "matrix.json").write_text(_json.dumps({
            "fixture": "matrix.json",
            "basis": {
                "evidence_acceptance_sha256": core.sha256_file(self.src / "evidence.json"),
                "edition_views_acceptance_sha256": core.sha256_file(self.src / "views.json"),
            },
        }), encoding="utf-8")

    # -- architecture / approval --------------------------------------------
    def _architecture_files(self) -> None:
        self._matrix_file()
        arch = {
            "schema_version": "2.0-rc1",
            "issue_id": self.issue,
            "research_profile": self.research,
            "publication_profile": self.publication,
            "status": "PROPOSED",
            "basis": {
                "production_profile_sha256": core.sha256_file(self.src / "production-profile.json"),
                "profile_completeness_sha256": core.sha256_file(self.src / "completeness.json"),
                "materiality_ledger_sha256": core.sha256_file(self.src / "ledger.json"),
                "candidate_matrix_sha256": drafting_base._object_sha(self.shared_matrix),
                "candidate_selection_sha256": core.sha256_file(self.src / "selection.json"),
            },
            "editorial_thesis": "Fixture thesis.",
            "architecture_goals": ["rebind safely"],
            "page_plan": {"target_pages": 1, "max_pages": 4, "notes": "fixture"},
            "packages": [
                {"package_id": "pkg-a", "title": "Package A", "purpose": "Carry A.",
                 "primary_candidate_ids": ["candidate:a"], "supporting_candidate_ids": [],
                 "must_cover_requirements": ["req-a"], "boundaries": ["keep scope a"],
                 "drafting_order": 1, "profile_extensions": {}, "publication_extensions": {}},
                {"package_id": "pkg-b", "title": "Package B", "purpose": "Carry B.",
                 "primary_candidate_ids": ["candidate:b"], "supporting_candidate_ids": [],
                 "must_cover_requirements": ["req-b"], "boundaries": ["keep scope b"],
                 "drafting_order": 2, "profile_extensions": {}, "publication_extensions": {}},
            ],
            "selected_exceptions": [],
            "profile_extensions": {},
            "publication_extensions": {},
            "human_review": {"reviewed_by": None, "reviewed_at": None, "review_reference": None},
        }
        core.write_json(self.src / "architecture-v2.json", arch)
        (self.src / "architecture-review-summary-v2.json").write_text("{}", encoding="utf-8")
        (self.src / "architecture-review-attention-v2.json").write_text("{}", encoding="utf-8")

    def _approval_files(self) -> None:
        arch = self.src / "architecture-v2.json"
        summ = self.src / "architecture-review-summary-v2.json"
        attn = self.src / "architecture-review-attention-v2.json"
        core.write_json(self.src / "gates" / "architecture-approval.json", {
            "schema_version": "2.0-rc1",
            "approval_id": "fixture-approval-r1",
            "issue_id": self.issue,
            "gate": "ARCHITECTURE_REVIEW",
            "decision": "APPROVED",
            "architecture_sha256": core.sha256_file(arch),
            "architecture_review_summary_sha256": core.sha256_file(summ),
            "architecture_review_attention_sha256": core.sha256_file(attn),
            "reviewed_by": "fixture-human",
            "reviewed_at": "2026-10-03T11:00:00Z",
            "review_reference": "fixture",
        })
        approval = core.load_json(self.src / "gates" / "architecture-approval.json")
        assert not drafting_base.validate_architecture_approval(approval, arch, summ, self.issue)

    # -- draft packages / results / synthesis --------------------------------
    def _card(self, task_id: str, subject: str) -> dict:
        return {
            "evidence_task_id": task_id,
            "issue_id": self.issue,
            "temporal": {"events": []},
            "claims": [{"statement_id": "claim-1", "subject_id": subject,
                        "subject_role": "PRIMARY_SUBJECT", "text": "fixture claim"}],
            "metrics": [],
            "limitations": [{"statement_id": "limit-1", "subject_id": subject,
                             "subject_role": "PRIMARY_SUBJECT", "text": "fixture limit"}],
        }

    def _evidence_authority(self) -> None:
        cards = {task: self._card(task, subject)
                 for task, subject in (("task-a", "subj-a"), ("task-b", "subj-b"))}
        candidates = (("candidate:a", "task-a"), ("candidate:b", "task-b"))
        acceptance = {
            "issue_id": self.issue, "research_profile": self.research,
            "results": [{"evidence_task_id": task,
                         "sha256": drafting_base._object_sha(cards[task])}
                        for _, task in candidates]}
        matrix = {
            "issue_id": self.issue, "research_profile": self.research,
            "basis": {"evidence_acceptance_sha256": drafting_base._object_sha(acceptance)},
            "rows": [{"candidate_id": cid, "evidence_task_id": task,
                      "evidence_sha256": drafting_base._object_sha(cards[task])}
                     for cid, task in candidates]}
        self.shared_cards = cards
        self.shared_acceptance = acceptance
        self.shared_matrix = matrix

    def _draft_packages(self) -> None:
        import json as _json
        profile_path = self.src / "production-profile.json"
        arch_path = self.src / "architecture-v2.json"
        summ_path = self.src / "architecture-review-summary-v2.json"
        approval_path = self.src / "gates" / "architecture-approval.json"
        arch = core.load_json(arch_path)
        for pid, cid, task, subject in (("pkg-a", "candidate:a", "task-a", "subj-a"),
                                        ("pkg-b", "candidate:b", "task-b", "subj-b")):
            matrix, acceptance, card = (
                self.shared_matrix, self.shared_acceptance, self.shared_cards[task])
            plan = [p for p in arch["packages"] if p["package_id"] == pid][0]
            package = {
                "schema_version": "2.0-rc1",
                "issue_id": self.issue,
                "research_profile": self.research,
                "publication_profile": self.publication,
                "package_id": pid,
                "basis": {
                    "production_profile_sha256": core.sha256_file(profile_path),
                    "architecture_sha256": core.sha256_file(arch_path),
                    "architecture_review_summary_sha256": core.sha256_file(summ_path),
                    "architecture_approval_sha256": core.sha256_file(approval_path),
                    "candidate_matrix_sha256": drafting_base._object_sha(matrix),
                    "candidate_selection_sha256": arch["basis"]["candidate_selection_sha256"],
                    "evidence_acceptance_sha256": drafting_base._object_sha(acceptance),
                },
                "package": {
                    "title": plan["title"], "purpose": plan["purpose"],
                    "drafting_order": plan["drafting_order"],
                    "primary_candidate_ids": list(plan["primary_candidate_ids"]),
                    "supporting_candidate_ids": list(plan["supporting_candidate_ids"]),
                    "must_cover_requirements": list(plan["must_cover_requirements"]),
                    "boundaries": list(plan["boundaries"]),
                },
                "candidate_matrix": matrix,
                "evidence_acceptance": acceptance,
                "evidence_inputs": [{
                    "candidate_id": cid, "architecture_usage": "PRIMARY",
                    "evidence_task_id": task,
                    "evidence_sha256": drafting_base._object_sha(card),
                    "evidence_card": card,
                }],
                "drafting_constraints": {
                    "language": "ja", "raw_sources_forbidden": True,
                    "unknowns_remain_unknown": True,
                    "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
                },
                "profile_extensions": {},
                "publication_extensions": {},
            }
            package_path = self.src / "draft" / "v2" / "packages" / pid / "draft-package.json"
            core.write_json(package_path, package)
            errors = drafting_base.validate_self_contained_draft_package(
                package, profile_path, arch_path, summ_path, approval_path)
            assert not errors, (pid, errors)

    def _result_object(self, pid: str, text: str) -> dict:
        package_path = self.src / "draft" / "v2" / "packages" / pid / "draft-package.json"
        package = core.load_json(package_path)
        task = package["evidence_inputs"][0]["evidence_task_id"]
        subject = package["evidence_inputs"][0]["evidence_card"]["claims"][0]["subject_id"]
        claim_ref = {"evidence_task_id": task, "kind": "CLAIM", "evidence_id": "claim-1",
                     "subject_id": subject, "subject_role": "PRIMARY_SUBJECT"}
        limit_ref = {"evidence_task_id": task, "kind": "LIMITATION", "evidence_id": "limit-1",
                     "subject_id": subject, "subject_role": "PRIMARY_SUBJECT"}
        req = package["package"]["must_cover_requirements"][0]
        boundary = package["package"]["boundaries"][0]
        return {
            "schema_version": "2.0-rc1",
            "issue_id": self.issue,
            "research_profile": self.research,
            "publication_profile": self.publication,
            "package_id": pid,
            "draft_version": "r1",
            "status": "ESTABLISHED",
            "basis": {"draft_package_sha256": core.sha256_file(package_path),
                      "prompt_id": "article-drafting-v2",
                      "prompt_sha256": core.sha256_file(
                          self.repo / drafting_base.DRAFT_PROMPT)},
            "runner": {"provider": "fixture", "model": "fixture",
                       "invocation": "fixture r1",
                       "generated_at": core.iso_utc(T0),
                       "run_reference": "fixture-r1"},
            "headline": f"Headline {pid}",
            "deck": f"Deck {pid} carries the package thesis.",
            "deck_attribution_mode": "FACTUAL",
            "deck_evidence_refs": [claim_ref],
            "blocks": [
                {"block_id": f"{pid}-b1", "block_type": "PARAGRAPH", "text": text,
                 "attribution_mode": "FACTUAL", "evidence_refs": [claim_ref]},
                {"block_id": f"{pid}-boundaries", "block_type": "CLAIM_BOUNDARY",
                 "text": f"Boundary for {pid}.",
                 "attribution_mode": "FACTUAL", "evidence_refs": [limit_ref]},
            ],
            "must_cover_coverage": [{"requirement": req, "block_ids": [f"{pid}-b1", f"{pid}-boundaries"]}],
            "boundary_dispositions": [{"boundary": boundary, "handling": "EXPLICITLY_STATED",
                                       "block_ids": [f"{pid}-boundaries"],
                                       "rationale": "Fixture boundary preserved explicitly."}],
            "profile_extensions": {},
            "publication_extensions": {},
        }

    def _draft_results_v1(self) -> None:
        from scripts import survey_drafting_v2 as drafting
        _ = drafting
        for pid in ("pkg-a", "pkg-b"):
            package_path = self.src / "draft" / "v2" / "packages" / pid / "draft-package.json"
            result = self._result_object(pid, f"Body {pid} version one carries mechanism and limit.")
            errors = drafting_base.validate_draft_result(
                result, package_path, self.repo / drafting_base.DRAFT_PROMPT)
            assert not errors, (pid, errors)
            core.write_json(
                self.src / "draft" / "v2" / "packages" / pid / "draft-result.json", result)

    def _synthesis_payload(self) -> dict:
        if self.research == "WEEKLY":
            return {"profile_payload": {"signals": "s", "current_interpretation": "c",
                                        "carry_over_summary": "o"},
                    "publication_payload": {}}
        return {"profile_payload": {
            "branch_transition_synthesis": "b", "parallel_competing_relations": "p",
            "unresolved_lineage_questions": "u", "historical_attribution_boundaries": "h"},
            "publication_payload": {}}

    def _synthesis_v1(self) -> None:
        from scripts import survey_drafting_v2 as drafting
        pairs = [(self.src / "draft" / "v2" / "packages" / pid / "draft-package.json",
                  self.src / "draft" / "v2" / "packages" / pid / "draft-result.json")
                 for pid in ("pkg-a", "pkg-b")]
        expected = drafting.build_synthesis_input(
            self.repo, self.src / "production-profile.json",
            self.src / "architecture-v2.json",
            self.src / "architecture-review-summary-v2.json",
            self.src / "gates" / "architecture-approval.json", pairs)
        core.write_json(self.src / "draft" / "v2" / "profile-synthesis-input.json", expected)
        payload = self._synthesis_payload()
        result = {
            "schema_version": "2.0-rc1", "issue_id": self.issue,
            "research_profile": self.research, "publication_profile": self.publication,
            "synthesis_version": "v1.0", "status": "ESTABLISHED",
            "basis": {"synthesis_input_sha256": core.sha256_file(
                self.src / "draft" / "v2" / "profile-synthesis-input.json"),
                "prompt_id": "profile-synthesis-v2",
                "prompt_sha256": core.sha256_file(self.repo / drafting.SYNTHESIS_PROMPT)},
            "runner": {"provider": "fixture", "model": "fixture", "invocation": "fixture",
                       "generated_at": core.iso_utc(T0), "run_reference": "fixture-r1"},
            "profile_payload": payload["profile_payload"],
            "publication_payload": payload["publication_payload"],
        }
        errors = drafting.validate_synthesis_result(
            result, self.src / "draft" / "v2" / "profile-synthesis-input.json",
            self.repo / drafting.SYNTHESIS_PROMPT)
        assert not errors, errors
        core.write_json(self.src / "draft" / "v2" / "profile-synthesis-result.json", result)

    def _review_file(self) -> None:
        core.write_json(self.src / "execution" / "reviews" / "sol-review-r1.json", {
            "decision": "PASS", "reviewed_by": "fixture-sol",
            "review_reference": "fixture Sol review r1", "scope": "draft revision",
        })

    # -- checkpoints / state --------------------------------------------------
    def _contract_report(self, record_path: Path, from_state: str, to_state: str, artifacts: list) -> Path:
        report_path = record_path.parent / (record_path.stem + "-core-contract.json")
        state_path = self.src / "production-state.json"
        core.write_json(report_path, {
            "schema_version": "2.0-rc1",
            "check_id": "CORE_STAGE_CONTRACT",
            "status": "PASS",
            "issue_id": self.issue,
            "from_state": from_state,
            "to_state": to_state,
            "production_state": {"path": str((self.src / "production-state.json").relative_to(self.repo)),
                                   "sha256": core.sha256_file(state_path) if state_path.is_file() else "0" * 64},
            "production_profile": {
                "path": str((self.src / "production-profile.json").relative_to(self.repo)),
                "sha256": core.sha256_file(self.src / "production-profile.json")},
            "implementation_commit_sha": core.repository_commit_sha(self.repo),
            "contract": core.contract_identity(self.repo, self.cfg, self.research, self.publication),
            "artifacts": artifacts,
            "recorded_at": core.iso_utc(T0),
        })
        return report_path

    def _checkpoint_records(self) -> None:
        F = lambda *parts: self.src.joinpath(*parts)
        stage_rows = {
            "discovery": [("discovery-acceptance", F("discovery.json"))],
            "screening": [("screening-acceptance", F("screening.json"))],
            "evidence": [("evidence-acceptance", F("evidence.json")),
                         ("edition-views-acceptance", F("views.json")),
                         ("materiality-ledger", F("ledger.json")),
                         ("profile-completeness", F("completeness.json"))],
            "materiality": [("evidence-acceptance", F("evidence.json")),
                            ("edition-views-acceptance", F("views.json")),
                            ("materiality-ledger", F("ledger.json")),
                            ("profile-completeness", F("completeness.json"))],
            "completeness": [("evidence-acceptance", F("evidence.json")),
                             ("edition-views-acceptance", F("views.json")),
                             ("materiality-ledger", F("ledger.json")),
                             ("profile-completeness", F("completeness.json"))],
            "selection": [("candidate-matrix", F("matrix.json")),
                          ("candidate-selection", F("selection.json"))],
            "architecture": [("issue-architecture", F("architecture-v2.json")),
                             ("architecture-review-summary", F("architecture-review-summary-v2.json")),
                             ("architecture-review-attention", F("architecture-review-attention-v2.json"))],
            "draft": ([(f"draft-package:{pid}", F("draft", "v2", "packages", pid, "draft-package.json"))
                       for pid in ("pkg-a", "pkg-b")]
                      + [(f"draft-result:{pid}", F("draft", "v2", "packages", pid, "draft-result.json"))
                         for pid in ("pkg-a", "pkg-b")]
                      + [("synthesis-input", F("draft", "v2", "profile-synthesis-input.json")),
                         ("synthesis-result", F("draft", "v2", "profile-synthesis-result.json"))]),
        }
        stamp = T0
        for name, from_state, to_state in PRODUCERS:
            stamp = stamp + timedelta(minutes=1)
            record_path = self.src / "orchestration" / "v2" / "checkpoints" / f"{from_state}.json"
            artifacts = [
                {"name": n, "path": str(p.relative_to(self.repo)), "sha256": core.sha256_file(p)}
                for n, p in stage_rows.get(name, [])
            ]
            report_path = self._contract_report(record_path, from_state, to_state, artifacts)
            core.write_json(record_path, {
                "schema_version": "2.0-rc1",
                "issue_id": self.issue,
                "from_state": from_state,
                "to_state": to_state,
                "checkpoints": sorted({n for (n, f, _t) in PRODUCERS if f == from_state}),
                "recorded_at": core.iso_utc(stamp),
                "implementation": {
                    "repository_commit_sha": core.repository_commit_sha(self.repo),
                    "orchestrator_version": self.cfg["orchestrator_version"],
                },
                "contract": core.contract_identity(self.repo, self.cfg, self.research, self.publication),
                "artifacts": artifacts,
                "reviews": [{
                    "check_id": "CORE_STAGE_CONTRACT",
                    "kind": "DETERMINISTIC",
                    "status": "PASS",
                    "executor": "fixture",
                    "evidence": "fixture stage contract",
                    "result": {"path": str(report_path.relative_to(self.repo)),
                               "sha256": core.sha256_file(report_path)},
                }],
                "summary": f"fixture {name}",
            })

    def _write_state(self, provisional: bool = False) -> None:
        states = ["ISSUE_INITIALIZED", "DISCOVERY_COLLECTED", "CANDIDATES_NORMALIZED",
                  "EVIDENCE_REVIEWED", "SELECTION_COMPLETE", "ARCHITECTURE_ESTABLISHED",
                  "DRAFT_COMPLETE"]
        history = [{
            "from": None if i == 0 else states[i - 1],
            "to": name,
            "recorded_at": core.iso_utc(T0 + timedelta(minutes=i)),
            "repository_commit_sha": core.repository_commit_sha(self.repo),
        } for i, name in enumerate(states)]
        provenance = {}
        for name, from_state, _ in PRODUCERS:
            p = self.src / "orchestration" / "v2" / "checkpoints" / f"{from_state}.json"
            if provisional or not p.is_file():
                provenance[name] = {"path": str(p.relative_to(self.repo)), "sha256": "0" * 64}
            else:
                provenance[name] = {"path": str(p.relative_to(self.repo)), "sha256": core.sha256_file(p)}
        approval = self.src / "gates" / "architecture-approval.json"
        state = {
            "schema_version": "2.0-rc1",
            "issue_id": self.issue,
            "research_profile": self.research,
            "publication_profile": self.publication,
            "lifecycle_state": "DRAFT_COMPLETE",
            "profile": {"path": str((self.src / "production-profile.json").relative_to(self.repo)),
                        "sha256": core.sha256_file(self.src / "production-profile.json")},
            "contract": {
                "pipeline_contract_version": "2.0-rc1",
                "quality_contract_version": "2.0-rc1",
                "research_profile_version": "2.0-rc1",
                "publication_profile_version": "2.0-rc1",
                "pipeline_contract_sha256": "0" * 64,
                "quality_contract_sha256": "0" * 64,
                "research_profile_sha256": "0" * 64,
                "publication_profile_sha256": "0" * 64,
            },
            "implementation": {"repository_commit_sha": core.repository_commit_sha(self.repo),
                               "orchestrator_version": self.cfg["orchestrator_version"]},
            "human_gates": {"architecture_review": "approved", "publication_preview": "pending"},
            "human_gate_provenance": {
                "architecture_review": {"path": str(approval.relative_to(self.repo)),
                                        "sha256": core.sha256_file(approval)},
                "publication_preview": None,
            },
            "target_gate": "ARCHITECTURE_REVIEW",
            "next_action": None,
            "terminal_reason": None,
            "exception_gate": {"status": "inactive", "reason": None},
            "machine_checkpoints": {n: ("passed" if n in [p[0] for p in PRODUCERS] else "pending")
                                    for n in core.CHECKPOINTS},
            "checkpoint_provenance": {n: provenance.get(n) for n in core.CHECKPOINTS},
            "legacy_compatibility": {"mode": "NON_AUTHORITATIVE_READ_ONLY",
                                     "legacy_state_path": str((self.src / "legacy.json").relative_to(self.repo)),
                                     "legacy_state_present": False, "legacy_state_sha256": None},
            "history": history,
        }
        state = core.refresh_state_control(state, self.cfg)
        core.write_json(self.src / "production-state.json", state)

    # -- revision helpers ------------------------------------------------------
    def revise_results(self, version_text: str) -> None:
        """Rewrite both result bodies (reviewed successor bytes)."""
        for pid in ("pkg-a", "pkg-b"):
            path = self.src / "draft" / "v2" / "packages" / pid / "draft-result.json"
            result = core.load_json(path)
            for block in result["blocks"]:
                if block["block_type"] == "PARAGRAPH":
                    block["text"] = version_text
            core.write_json(path, result)
        pairs = [(self.src / "draft" / "v2" / "packages" / pid / "draft-package.json",
                  self.src / "draft" / "v2" / "packages" / pid / "draft-result.json")
                 for pid in ("pkg-a", "pkg-b")]
        expected = drafting_base.build_synthesis_input(
            self.repo, self.src / "production-profile.json",
            self.src / "architecture-v2.json",
            self.src / "architecture-review-summary-v2.json",
            self.src / "gates" / "architecture-approval.json", pairs)
        core.write_json(self.src / "draft" / "v2" / "profile-synthesis-input.json", expected)
        current = core.load_json(self.src / "draft" / "v2" / "profile-synthesis-result.json")
        current["basis"] = {
            "synthesis_input_sha256": core.sha256_file(
                self.src / "draft" / "v2" / "profile-synthesis-input.json"),
            "prompt_id": "profile-synthesis-v2",
            "prompt_sha256": core.sha256_file(self.repo / drafting_base.SYNTHESIS_PROMPT),
        }
        errors = drafting_base.validate_synthesis_result(
            current, self.src / "draft" / "v2" / "profile-synthesis-input.json",
            self.repo / drafting_base.SYNTHESIS_PROMPT)
        assert not errors, errors
        core.write_json(self.src / "draft" / "v2" / "profile-synthesis-result.json", current)


def _tex_escape(value: str) -> str:
    return value.replace("\\", "\\textbackslash{}").replace("{", "\\{").replace("}", "\\}")


class DraftRevisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(".").resolve()
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)

    def make_fixture(self, profile_key: str = "WEEKLY"):
        temp = tempfile.TemporaryDirectory(dir=str(self.root))
        fix = Fixture(self.root, Path(temp.name), profile_key)
        return temp, fix

    def state_path(self, fix: Fixture) -> Path:
        return fix.src / "production-state.json"

    def review_path(self, fix: Fixture) -> Path:
        return fix.src / "execution" / "reviews" / "sol-review-r1.json"

    def establish(self, fix: Fixture, reason: str = "reviewed terminology repair") -> Path:
        return draft_revision.establish_draft_revision(
            fix.repo, fix.cfg, self.state_path(fix), reason, EXECUTOR,
            self.review_path(fix).relative_to(fix.repo), T0, None)

    def assert_state_valid(self, fix: Fixture) -> None:
        state = core.load_json(self.state_path(fix))
        self.assertEqual(
            agent.validate_agent_state(fix.repo, fix.cfg, state), [])

    # -- T1: drift reproduction ------------------------------------------------
    def test_t1_drift_reproduced_on_revision_surface(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            state = core.load_json(self.state_path(fix))
            errors = agent.validate_agent_state(fix.repo, fix.cfg, state)
            drifted = sorted(
                e[len("Stage Checkpoint artifact drift: "):]
                for e in errors if e.startswith("Stage Checkpoint artifact drift: "))
            self.assertEqual(
                drifted,
                ["draft-result:pkg-a", "draft-result:pkg-b",
                 "synthesis-input", "synthesis-result"])
            self.assertEqual(
                [e for e in errors if not e.startswith("Stage Checkpoint artifact drift: ")], [])
        finally:
            temp.cleanup()

    # -- T2: establishment ------------------------------------------------------
    def test_t2_establishment_rebinds_and_preserves_history(self) -> None:
        temp, fix = self.make_fixture()
        try:
            checkpoint = fix.src / "orchestration" / "v2" / "checkpoints" / "ARCHITECTURE_ESTABLISHED.json"
            before = core.sha256_file(checkpoint)
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            record_path = self.establish(fix)
            self.assertEqual(record_path.name, "draft-surface-revision-r1.json")
            self.assertEqual(core.sha256_file(checkpoint), before)
            state = core.load_json(self.state_path(fix))
            self.assertEqual(
                state.get("draft_revision_provenance"),
                {"path": str(record_path.relative_to(fix.repo)),
                 "sha256": core.sha256_file(record_path)})
            self.assert_state_valid(fix)
        finally:
            temp.cleanup()

    # -- T3: package mutation rejected ------------------------------------------
    def test_t3_draft_package_mutation_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            package = fix.src / "draft" / "v2" / "packages" / "pkg-a" / "draft-package.json"
            payload = core.load_json(package)
            payload["package"]["purpose"] = "Mutated purpose."
            core.write_json(package, payload)
            with self.assertRaises(draft_revision.DraftRevisionError) as ctx:
                self.establish(fix)
            self.assertIn("not eligible", str(ctx.exception))
        finally:
            temp.cleanup()

    # -- T4: architecture / approval mutation rejected ---------------------------
    def test_t4_architecture_mutation_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            arch = fix.src / "architecture-v2.json"
            payload = core.load_json(arch)
            payload["editorial_thesis"] = "Mutated thesis."
            core.write_json(arch, payload)
            with self.assertRaises(draft_revision.DraftRevisionError):
                self.establish(fix)
        finally:
            temp.cleanup()

    def test_t4b_approval_mutation_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            approval = fix.src / "gates" / "architecture-approval.json"
            payload = core.load_json(approval)
            payload["review_reference"] = "Mutated reference."
            core.write_json(approval, payload)
            with self.assertRaises(draft_revision.DraftRevisionError):
                self.establish(fix)
        finally:
            temp.cleanup()

    # -- T5: selection/evidence upstream mutation rejected -----------------------
    def test_t5_selection_mutation_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            selection = fix.src / "selection.json"
            selection.write_text('{"fixture": "mutated"}', encoding="utf-8")
            with self.assertRaises(draft_revision.DraftRevisionError):
                self.establish(fix)
        finally:
            temp.cleanup()

    def test_t5b_evidence_mutation_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            evidence = fix.src / "evidence.json"
            evidence.write_text('{"fixture": "mutated"}', encoding="utf-8")
            with self.assertRaises(draft_revision.DraftRevisionError):
                self.establish(fix)
        finally:
            temp.cleanup()

    # -- T6: invalid revised result rejected --------------------------------------
    def test_t6_invalid_revised_result_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            path = fix.src / "draft" / "v2" / "packages" / "pkg-a" / "draft-result.json"
            result = core.load_json(path)
            result["blocks"][0]["evidence_refs"] = [{
                "evidence_task_id": "task-a", "kind": "CLAIM", "evidence_id": "no-such-claim",
                "subject_id": "subj-a", "subject_role": "PRIMARY_SUBJECT"}]
            core.write_json(path, result)
            with self.assertRaises(draft_revision.DraftRevisionError) as ctx:
                self.establish(fix)
            self.assertIn("pkg-a", str(ctx.exception))
        finally:
            temp.cleanup()

    # -- T7: bad synthesis derivation rejected --------------------------------------
    def test_t7_bad_synthesis_derivation_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            path = fix.src / "draft" / "v2" / "profile-synthesis-input.json"
            payload = core.load_json(path)
            payload["drafts"][0]["draft_result"]["blocks"][0]["text"] = "Tampered text."
            core.write_json(path, payload)
            with self.assertRaises(draft_revision.DraftRevisionError) as ctx:
                self.establish(fix)
            self.assertIn("Synthesis Input", str(ctx.exception))
        finally:
            temp.cleanup()

    # -- T8: synthesis result mismatch rejected --------------------------------------
    def test_t8_synthesis_result_mismatch_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            path = fix.src / "draft" / "v2" / "profile-synthesis-result.json"
            payload = core.load_json(path)
            payload["basis"]["synthesis_input_sha256"] = "0" * 64
            core.write_json(path, payload)
            with self.assertRaises(draft_revision.DraftRevisionError) as ctx:
                self.establish(fix)
            self.assertIn("Synthesis Result", str(ctx.exception))
        finally:
            temp.cleanup()

    # -- T9: wrong prior checkpoint rejected -----------------------------------------
    def test_t9_wrong_prior_checkpoint_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            record_path = self.establish(fix)
            record = core.load_json(record_path)
            record["prior_checkpoint"] = {"path": "sources/elsewhere.json", "sha256": "0" * 64}
            core.write_json(record_path, record)
            state = core.load_json(self.state_path(fix))
            record2, errors = draft_revision.resolve_active_draft_revision(
                fix.repo, fix.cfg, state)
            self.assertIsNone(record2)
            self.assertTrue(errors)
        finally:
            temp.cleanup()

    # -- T10: unreferenced forgery inert ------------------------------------------------
    def test_t10_unreferenced_forged_record_inert(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            record_path = self.establish(fix)
            forged = fix.src / "draft" / "v2" / "draft-surface-revision-r99.json"
            shutil.copyfile(record_path, forged)
            state = core.load_json(self.state_path(fix))
            record, errors = draft_revision.resolve_active_draft_revision(
                fix.repo, fix.cfg, state)
            self.assertIsNotNone(record)
            self.assertEqual(errors, [])
            self.assertEqual(
                state.get("draft_revision_provenance", {}).get("path"),
                str(record_path.relative_to(fix.repo)))
            self.assert_state_valid(fix)
        finally:
            temp.cleanup()

    # -- T11: corrupt pointer fail-closed ------------------------------------------------
    def test_t11_corrupt_pointer_fail_closed(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            self.establish(fix)
            state_path = self.state_path(fix)
            state = core.load_json(state_path)
            state["draft_revision_provenance"] = {
                "path": str((fix.src / "draft" / "v2" / "draft-surface-revision-r1.json").relative_to(fix.repo)),
                "sha256": "0" * 64,
            }
            core.write_json(state_path, state)
            record, errors = draft_revision.resolve_active_draft_revision(
                fix.repo, fix.cfg, state)
            self.assertIsNone(record)
            self.assertTrue(errors)
            self.assertTrue(agent.validate_agent_state(fix.repo, fix.cfg, state))
        finally:
            temp.cleanup()

    def test_t11b_missing_pointer_target_fail_closed(self) -> None:
        temp, fix = self.make_fixture()
        try:
            state_path = self.state_path(fix)
            state = core.load_json(state_path)
            state["draft_revision_provenance"] = {
                "path": str((fix.src / "draft" / "v2" / "draft-surface-revision-r1.json").relative_to(fix.repo)),
                "sha256": "0" * 64,
            }
            core.write_json(state_path, state)
            record, errors = draft_revision.resolve_active_draft_revision(
                fix.repo, fix.cfg, state)
            self.assertIsNone(record)
            self.assertTrue(errors)
        finally:
            temp.cleanup()

    # -- T12: review authority rejected ---------------------------------------------------
    def test_t12_missing_review_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            (fix.src / "execution" / "reviews" / "sol-review-r1.json").unlink()
            with self.assertRaises(draft_revision.DraftRevisionError):
                self.establish(fix)
        finally:
            temp.cleanup()

    def test_t12b_non_pass_review_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            core.write_json(fix.src / "execution" / "reviews" / "sol-review-r1.json", {
                "decision": "REQUEST_CHANGES", "reviewed_by": "fixture-sol"})
            with self.assertRaises(draft_revision.DraftRevisionError) as ctx:
                self.establish(fix)
            self.assertIn("PASS", str(ctx.exception))
        finally:
            temp.cleanup()

    def test_t12c_anonymous_review_rejected(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            core.write_json(fix.src / "execution" / "reviews" / "sol-review-r1.json", {
                "decision": "PASS", "reviewed_by": "  "})
            with self.assertRaises(draft_revision.DraftRevisionError):
                self.establish(fix)
        finally:
            temp.cleanup()

    # -- T13: second revision chains ---------------------------------------------------------
    def test_t13_second_revision_chains(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            r1 = self.establish(fix)
            r1_sha = core.sha256_file(r1)
            fix.revise_results("Body revised a third time with tighter wording.")
            r2 = self.establish(fix, reason="second reviewed pass")
            self.assertEqual(r2.name, "draft-surface-revision-r2.json")
            self.assertEqual(core.sha256_file(r1), r1_sha)
            record2 = core.load_json(r2)
            self.assertEqual(
                record2["supersedes"],
                {"path": str(r1.relative_to(fix.repo)), "sha256": r1_sha})
            state = core.load_json(self.state_path(fix))
            self.assertEqual(
                state.get("draft_revision_provenance", {}).get("path"),
                str(r2.relative_to(fix.repo)))
            self.assert_state_valid(fix)
        finally:
            temp.cleanup()

    def write_pub_pdf(self, pdf: Path, producer: str) -> None:
        writer = pypdf.PdfWriter()
        writer.add_blank_page(612, 792)
        writer.add_metadata({"/Producer": f"draft-revision-fixture/{producer}"})
        with open(pdf, "wb") as handle:
            writer.write(handle)

    def _pub_review_rows(self, fix: Fixture, profile: dict) -> tuple[list, list]:
        repo = fix.repo
        cov_a = "Section 1 \u2014 Headline pkg-a"
        cov_b = "Section 2 \u2014 Headline pkg-b"
        fin = "Section 3 \u2014 Finale"

        def row(check_id: str, detail: str,
                locations: list[str] | None = None) -> dict[str, object]:
            return {"check_id": check_id, "status": "PASS", "detail": detail,
                    "evidence_locations": locations or ["review:fixture-evidence"]}

        sem_expected = reader._expected_review_checks(repo, profile, "SEMANTIC_EDITORIAL")
        sem_rows: list[dict[str, object]] = []
        for check_id in sorted(sem_expected):
            if check_id == "ARCHITECTURE_CONTENT_FIDELITY":
                sem_rows.append(row(
                    check_id,
                    "All packages represented with pages:1. package:pkg-a package:pkg-b.",
                    [cov_a, cov_b, "package:pkg-a", "package:pkg-b",
                     f"coverage:{cov_a}", f"coverage:{cov_b}",
                     f"package:pkg-a@{cov_a}", f"package:pkg-b@{cov_b}"]))
            elif check_id == "LONGFORM_TECHNICAL_DEPTH":
                sem_rows.append(row(
                    check_id,
                    "Technical depth across packages with pages:1. package:pkg-a package:pkg-b.",
                    [cov_a, cov_b, "package:pkg-a", "package:pkg-b",
                     f"coverage:{cov_a}", f"coverage:{cov_b}",
                     f"package:pkg-a@{cov_a}", f"package:pkg-b@{cov_b}"]))
            elif check_id == "FINAL_SYNTHESIS_QUALITY":
                sem_rows.append(row(
                    check_id,
                    "Finale synthesis for the analyst reader. package:pkg-b with pages:1.",
                    [fin, "reader-role:final-synthesis", "package:pkg-b",
                     f"final:{fin}", f"package:pkg-b@{cov_b}"]))
            else:
                sem_rows.append(row(check_id, f"Fixture pass for {check_id}."))
        vis_expected = reader._expected_review_checks(repo, profile, "VISUAL")
        vis_rows = [
            row(check_id,
                "Fixture visual pass with reader-layout:balanced-two-column-narrative "
                "reader-layout:wide-surfaces-full-width "
                "reader-layout:references-one-column.",
                ["reader-layout:balanced-two-column-narrative",
                 "reader-layout:wide-surfaces-full-width",
                 "reader-layout:references-one-column"])
            if check_id == "LONGFORM_MIXED_LAYOUT"
            else row(check_id, f"Fixture pass for {check_id}.")
            for check_id in sorted(vis_expected)]
        return sem_rows, vis_rows

    def _build_pub_qa(self, fix: Fixture, manuscript_path: Path) -> dict[str, Path]:
        """Build (or rebuild after PDF regeneration) PDF-bound QA docs."""
        repo, src = fix.repo, fix.src
        tex = fix.survey / "main.tex"
        pdf = fix.survey / "main.pdf"
        profile_path = src / "production-profile.json"
        profile = core.load_json(profile_path)
        det_ids = sorted(
            check_id for check_id, kind in quality.expected_checks(
                fix.cfg, profile["research_profile"],
                profile["publication_profile"]).items()
            if kind == "DETERMINISTIC")
        self.assertTrue(det_ids)
        bundle_rows = []
        for check_id in det_ids:
            result_file = src / "publication" / "v2" / f"quality-{check_id}.txt"
            if not result_file.exists():
                result_file.write_text(
                    f"fixture deterministic evidence for {check_id}\n", encoding="utf-8")
            bundle_rows.append({
                "check_id": check_id, "kind": "DETERMINISTIC", "status": "PASS",
                "executor": EXECUTOR, "evidence": f"fixture evidence {check_id}",
                "recorded_at": core.iso_utc(T0),
                "result": {"path": str(result_file.relative_to(repo)),
                           "sha256": core.sha256_file(result_file)}})
        bundle_path = src / "publication" / "v2" / "quality-regression-bundle-v2.json"
        if bundle_path.exists():
            bundle_path.unlink()
        quality.build_bundle(
            repo, fix.issue, tex, pdf, bundle_rows, bundle_path,
            production_profile_path=profile_path)
        sem_rows, vis_rows = self._pub_review_rows(fix, profile)
        sem_path = src / "publication" / "v2" / "semantic-editorial-review-v2.json"
        if sem_path.exists():
            sem_path.unlink()
        reader.build_review_record(
            repo, manuscript_path, pdf, 1, "SEMANTIC_EDITORIAL",
            sem_rows, EXECUTOR, T0, sem_path)
        vis_path = src / "publication" / "v2" / "visual-review-v2.json"
        if vis_path.exists():
            vis_path.unlink()
        reader.build_review_record(
            repo, manuscript_path, pdf, 1, "VISUAL",
            vis_rows, EXECUTOR, T0, vis_path)
        return {"bundle": bundle_path, "semantic": sem_path, "visual": vis_path}

    def rebuild_pub_qa(self, fix: Fixture, manuscript_path: Path) -> dict[str, Path]:
        """Rebuild PDF-bound QA docs (bundle + reviews) after PDF regeneration."""
        return self._build_pub_qa(fix, manuscript_path)
    def build_publication_family(self, fix: Fixture) -> dict[str, Path]:
        repo, src = fix.repo, fix.src
        tex = fix.survey / "main.tex"
        tex.write_text(
            "\\documentclass{article}\n\\begin{document}\n"
            "\\section{Headline pkg-a}\n"
            "Mechanism narrative with stated limit, revised second pass.\n\n"
            "\\section{Headline pkg-b}\n"
            "Second storyline with evidence, revised second pass.\n\n"
            "\\section{Finale}\n"
            "Synthesis finale for the analyst reader.\n"
            "\\end{document}\n",
            encoding="utf-8")
        pdf = fix.survey / "main.pdf"
        self.write_pub_pdf(pdf, "fixture-build-1")
        bib = src / "references.bib"
        bib.write_text(
            "@misc{fixture2026,\n title={Fixture source},\n year={2026}\n}\n",
            encoding="utf-8")
        profile_path = src / "production-profile.json"
        manuscript_path = src / "publication" / "v2" / "reader-manuscript-v2.json"
        reader.build_manuscript_manifest(
            repo, fix.issue, profile_path,
            src / "architecture-v2.json",
            src / "gates" / "architecture-approval.json",
            tex,
            [{"role": "BIBLIOGRAPHY", "path": str(bib.relative_to(repo))}],
            [{"package_id": "pkg-a", "requirement": "req-a", "status": "FULFILLED",
              "reader_locations": ["Section 1 \u2014 Headline pkg-a"],
              "detail": "Section 1 carries the pkg-a mechanism within limits."},
             {"package_id": "pkg-b", "requirement": "req-b", "status": "FULFILLED",
              "reader_locations": ["Section 2 \u2014 Headline pkg-b"],
              "detail": "Section 2 carries the pkg-b storyline with evidence."}],
            [{"requirement_id": "FINAL_SYNTHESIS", "status": "FULFILLED",
              "reader_locations": ["Section 3 \u2014 Finale"],
              "detail": "Finale synthesizes both storylines for the analyst reader."}],
            EXECUTOR, T0, manuscript_path)
        qa = self._build_pub_qa(fix, manuscript_path)
        bundle_path, sem_path, vis_path = qa["bundle"], qa["semantic"], qa["visual"]
        profile = core.load_json(profile_path)
        tex = fix.survey / "main.tex"
        sem_surface_path = src / "publication" / "v2" / "semantic-surface-review-v2.json"
        sem_surface_base = {
            "schema_version": "2.0-rc1",
            "issue_id": fix.issue,
            "publication_profile": profile["publication_profile"],
            "review_kind": "SEMANTIC_EDITORIAL",
            "reviewed_surface": {
                "path": str(tex.relative_to(repo)),
                "sha256": core.sha256_file(tex)},
            "checks": [{
                "check_id": "READER_PIPELINE_INDEPENDENCE",
                "status": "PASS",
                "detail": "No internal pipeline leakage in reader source.",
                "evidence_locations": [f"reader-source:{tex.relative_to(repo)}"]}],
            "decision": "PASS",
            "reviewed_by": EXECUTOR,
            "reviewed_at": core.iso_utc(T0),
            "status": "PASSED",
            "findings": [],
            "summary": "Fixture surface review.",
        }
        sem_surface_payload = dict(sem_surface_base)
        sem_surface_payload["review_sha256"] = core.sha256_object(sem_surface_base)
        core.write_json(sem_surface_path, sem_surface_payload)
        gate_path = reader.build_reader_surface_gate(
            repo, manuscript_path, sem_surface_path, recorded_at=T0)
        return {"manuscript": manuscript_path, "source": tex, "pdf": pdf,
                "bundle": bundle_path, "semantic": sem_path, "visual": vis_path,
                "gate": gate_path}

    def checkpoint_reviews(self, fix: Fixture, report: Path) -> Path:
        reviews_path = fix.src / "execution" / "reviews" / "checkpoint-reviews.json"
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT",
            "kind": "DETERMINISTIC",
            "executor": EXECUTOR,
            "evidence": "fixture stage validation PASS",
            "result_path": str(report.relative_to(fix.repo))}]})
        return reviews_path

    def validate_reader_stage(self, fix: Fixture) -> tuple[dict[str, Path], Path]:
        family = self.build_publication_family(fix)
        supplied = {
            "reader-manuscript": family["manuscript"],
            "validated-source": family["source"],
            "publication-pdf": family["pdf"],
            "quality-regression-bundle": family["bundle"],
            "semantic-review": family["semantic"],
            "visual-review": family["visual"],
            "reader-surface-gate": family["gate"],
        }
        report = fix.src / "publication" / "v2" / "stage-validation-report.json"
        stage_validation.validate_stage(
            fix.repo, fix.cfg, self.state_path(fix), supplied, report, T0)
        return supplied, report

    # -- T14: hook parity + CLI ------------------------------------------------------
    def test_t14_hook_parity_and_cli(self) -> None:
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            self.establish(fix)
            state = core.load_json(self.state_path(fix))
            self.assertEqual(agent.validate_agent_state(fix.repo, fix.cfg, state), [])
            latched = stage_validation._prior_artifacts(fix.repo, fix.cfg, state)
            record = core.load_json(
                fix.repo / state["draft_revision_provenance"]["path"])
            revised = draft_revision.record_revised_rows(record)
            self.assertTrue(revised)
            for name, row in revised.items():
                self.assertIn(name, latched)
                self.assertEqual(core.sha256_file(latched[name]), row["sha256"])
            fix.revise_results("Body revised a third time with tighter wording.")
            proc = subprocess.run(
                [sys.executable, "-m", "scripts.survey_agent_control_v2",
                 "--repo-root", str(fix.repo),
                 "establish-draft-revision",
                 "--state", str(self.state_path(fix).relative_to(fix.repo)),
                 "--reason", "cli second pass",
                 "--executor", EXECUTOR,
                 "--review", str(self.review_path(fix).relative_to(fix.repo)),
                 "--recorded-at", core.iso_utc(T0)],
                capture_output=True, text=True, cwd=str(self.root))
            self.assertEqual(proc.returncode, 0, proc.stderr)
            state = core.load_json(self.state_path(fix))
            self.assertTrue(
                state.get("draft_revision_provenance", {}).get("path", "").endswith(
                    "draft-surface-revision-r2.json"))
            self.assert_state_valid(fix)
        finally:
            temp.cleanup()

    # -- T15: stage validation with revision-bound artifacts ------------------------------
    def test_t15_stage_validation_passes_with_revision(self) -> None:
        temp, fix = self.make_fixture("THEMATIC")
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            self.establish(fix)
            family = self.build_publication_family(fix)
            supplied = {
                "reader-manuscript": family["manuscript"],
                "validated-source": family["source"],
                "publication-pdf": family["pdf"],
                "quality-regression-bundle": family["bundle"],
                "semantic-review": family["semantic"],
                "visual-review": family["visual"],
                "reader-surface-gate": family["gate"],
            }
            report = fix.src / "publication" / "v2" / "stage-validation-report.json"
            stage_validation.validate_stage(
                fix.repo, fix.cfg, self.state_path(fix), supplied, report, T0)
            payload = core.load_json(report)
            self.assertEqual(payload.get("status"), "PASS")
            self.assertEqual(
                agent.validate_agent_state(
                    fix.repo, fix.cfg, core.load_json(self.state_path(fix))), [])
        finally:
            temp.cleanup()

    # -- T16: checkpoint advance binds revision ----------------------------------------------------------------
    def test_t16_checkpoint_advance_binds_revision(self) -> None:
        temp, fix = self.make_fixture("THEMATIC")
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            record_path = self.establish(fix)
            supplied, report = self.validate_reader_stage(fix)
            reviews_path = self.checkpoint_reviews(fix, report)
            checkpoint = agent.build_stage_checkpoint(
                fix.repo, fix.cfg, self.state_path(fix), supplied, reviews_path,
                "Advance DRAFT_COMPLETE on revised surface.", T0 + timedelta(hours=1), None)
            checkpoint_payload = core.load_json(checkpoint)
            names = sorted(row["name"] for row in checkpoint_payload["artifacts"])
            self.assertEqual(
                names,
                ["publication-pdf", "quality-regression-bundle", "reader-manuscript",
                 "reader-surface-gate", "semantic-review", "validated-source",
                 "visual-review"])
            agent.advance_with_checkpoint(
                fix.repo, fix.cfg, self.state_path(fix), checkpoint)
            state = core.load_json(self.state_path(fix))
            self.assertEqual(state.get("lifecycle_state"), "VALIDATED_DRAFT")
            self.assertEqual(
                state.get("draft_revision_provenance"),
                {"path": str(record_path.relative_to(fix.repo)),
                 "sha256": core.sha256_file(record_path)})
            self.assert_state_valid(fix)
        finally:
            temp.cleanup()

    # -- T17a: rollback clears stale pointer ---------------------------------------------------------------------------
    def test_t17_rollback_clears_stale_pointer(self) -> None:
        from scripts import survey_human_gate_v2 as human_gate
        temp, fix = self.make_fixture()
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            record_path = self.establish(fix)
            record_sha = core.sha256_file(record_path)
            state = core.load_json(self.state_path(fix))
            updated = human_gate._revised_state(
                fix.repo, fix.cfg, state, "ARCHITECTURE_REVIEW", "SELECTION_COMPLETE")
            self.assertIsNone(updated.get("draft_revision_provenance"))
            self.assertEqual(updated.get("lifecycle_state"), "SELECTION_COMPLETE")
            # The historical record file itself is never touched by rollback:
            # unreferenced it is inert historical evidence.
            self.assertEqual(core.sha256_file(record_path), record_sha)
            self.assertEqual(
                agent.validate_agent_state(fix.repo, fix.cfg, updated), [])
        finally:
            temp.cleanup()

    # -- T17b: post-validation boundary rejects new supersession -------------------------------------------------------------
    def test_t17b_boundary_rejects_after_validated_draft(self) -> None:
        temp, fix = self.make_fixture("THEMATIC")
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            self.establish(fix)
            supplied, report = self.validate_reader_stage(fix)
            reviews_path = self.checkpoint_reviews(fix, report)
            checkpoint = agent.build_stage_checkpoint(
                fix.repo, fix.cfg, self.state_path(fix), supplied, reviews_path,
                "Advance DRAFT_COMPLETE on revised surface.", T0 + timedelta(hours=1), None)
            agent.advance_with_checkpoint(
                fix.repo, fix.cfg, self.state_path(fix), checkpoint)
            state = core.load_json(self.state_path(fix))
            self.assertEqual(state.get("lifecycle_state"), "VALIDATED_DRAFT")
            fix.revise_results("Body revised a third time with tighter wording.")
            with self.assertRaises(draft_revision.DraftRevisionError) as ctx:
                self.establish(fix, reason="late revision after validation")
            self.assertIn("DRAFT_COMPLETE", str(ctx.exception))
            # Active pointer remains the validated r1 authority, untouched;
            # the unreviewed third bytes correctly report as drift (fail-closed).
            state = core.load_json(self.state_path(fix))
            self.assertIsNotNone(state.get("draft_revision_provenance"))
            drifted = sorted(
                e for e in agent.validate_agent_state(fix.repo, fix.cfg, state)
                if e.startswith("Stage Checkpoint artifact drift: "))
            self.assertEqual(
                drifted,
                ["Stage Checkpoint artifact drift: draft-result:pkg-a",
                 "Stage Checkpoint artifact drift: draft-result:pkg-b",
                 "Stage Checkpoint artifact drift: synthesis-input",
                 "Stage Checkpoint artifact drift: synthesis-result"])
        finally:
            temp.cleanup()

    # -- T18: coexistence with publication revalidation ------------------------------------------------------------------
    def test_t18_coexists_with_publication_revalidation(self) -> None:
        temp, fix = self.make_fixture("THEMATIC")
        try:
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            record_path = self.establish(fix)
            record_sha = core.sha256_file(record_path)
            supplied, report = self.validate_reader_stage(fix)
            reviews_path = self.checkpoint_reviews(fix, report)
            checkpoint = agent.build_stage_checkpoint(
                fix.repo, fix.cfg, self.state_path(fix), supplied, reviews_path,
                "Advance DRAFT_COMPLETE on revised surface.", T0 + timedelta(hours=1), None)
            agent.advance_with_checkpoint(
                fix.repo, fix.cfg, self.state_path(fix), checkpoint)
            state = core.load_json(self.state_path(fix))
            self.assertEqual(state.get("lifecycle_state"), "VALIDATED_DRAFT")
            # Regenerate a publication-surface byte (PDF layout rebuild) and
            # refresh the PDF-bound QA docs, then revalidate. Draft pointer
            # must survive untouched alongside the new publication authority.
            self.write_pub_pdf(fix.survey / "main.pdf", "fixture-build-2")
            self.rebuild_pub_qa(fix, supplied["reader-manuscript"])
            pub_path = agent.revalidate_publication_surface(
                fix.repo, fix.cfg, self.state_path(fix),
                "REVIEWED_CORE_CHANGE", "revalidate after layout rebuild",
                EXECUTOR, T0 + timedelta(hours=2), None)
            state = core.load_json(self.state_path(fix))
            self.assertIn("publication_revalidation_provenance", state)
            self.assertEqual(
                state.get("draft_revision_provenance"),
                {"path": str(record_path.relative_to(fix.repo)), "sha256": record_sha})
            self.assertEqual(core.sha256_file(record_path), record_sha)
            self.assert_state_valid(fix)
            record = core.load_json(record_path)
            pub_record = core.load_json(fix.repo / state["publication_revalidation_provenance"]["path"])
            self.assertNotEqual(
                str(record_path.relative_to(fix.repo)),
                state["publication_revalidation_provenance"]["path"])
            self.assertEqual(record["reason_class"], "REVIEWED_DRAFT_REVISION")
            self.assertNotEqual(record["reason_class"], pub_record.get("reason_class"))
        finally:
            temp.cleanup()

    # -- T19: generic across WEEKLY and THEMATIC ------------------------------------------------------------------------------
    def test_t19_generic_across_profiles(self) -> None:
        contracts: dict[str, object] = {}
        for profile_key in ("WEEKLY", "THEMATIC"):
            temp, fix = self.make_fixture(profile_key)
            try:
                fix.revise_results("Body revised carries mechanism and limit, second pass.")
                record_path = self.establish(fix)
                state = core.load_json(self.state_path(fix))
                self.assertEqual(
                    agent.validate_agent_state(fix.repo, fix.cfg, state), [])
                record = core.load_json(record_path)
                self.assertEqual(record["issue_id"], fix.issue)
                self.assertEqual(
                    record["validation"]["architecture"]["sha256"],
                    core.sha256_file(fix.src / "architecture-v2.json"))
                contracts[profile_key] = record["core"]["contract"]
            finally:
                temp.cleanup()
        self.assertNotEqual(contracts["WEEKLY"], contracts["THEMATIC"])

    # -- T20: historical checkpoint bytes untouched --------------------------------------------------------------------------------
    def test_t20_historical_checkpoint_bytes_untouched(self) -> None:
        temp, fix = self.make_fixture("THEMATIC")
        try:
            checkpoint = fix.src / "orchestration" / "v2" / "checkpoints" / "ARCHITECTURE_ESTABLISHED.json"
            before = core.sha256_file(checkpoint)
            fix.revise_results("Body revised carries mechanism and limit, second pass.")
            self.establish(fix)
            self.build_publication_family(fix)
            self.assertEqual(core.sha256_file(checkpoint), before)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
