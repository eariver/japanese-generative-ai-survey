from __future__ import annotations

import copy
import unittest
from pathlib import Path

from scripts import survey_architecture_v2 as architecture
from scripts import survey_completeness_v2 as completeness
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from tests import test_survey_evidence_v2 as evidence_tests


IMPLEMENTATION_SHA = "4" * 40


class SurveyArchitectureV2Tests(unittest.TestCase):
    def chain(self, research_profile: str):
        helper = evidence_tests.SurveyEvidenceV2Tests(
            methodName="test_evidence_package_is_exact_and_preserves_task_bytes"
        )
        helper.setUp()
        temp, root, cfg = helper.sandbox()
        self.addCleanup(temp.cleanup)
        profile_path, state_path = helper.init_profile(root, cfg, research_profile)
        issue_id = core.load_json(state_path)["issue_id"]
        discovery_path, screening_acceptance = helper.make_screening(
            root,
            state_path,
            [helper.discovery(issue_id, "target-source")],
            {"target-source": "KEEP"},
        )
        _, evidence_acceptance = helper.make_evidence(
            root, state_path, discovery_path, screening_acceptance
        )
        views_acceptance = helper.make_views(root, profile_path, evidence_acceptance)
        ledger = evidence.build_materiality_ledger(
            root,
            profile_path,
            discovery_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            IMPLEMENTATION_SHA,
        )
        ledger_path = root / "sources" / issue_id / "materiality-ledger.json"
        evidence.write_materiality_ledger(ledger_path, ledger)
        profile = core.load_json(profile_path)
        evidence_row = core.load_json(evidence_acceptance)["results"][0]
        obligations = [
            {
                "obligation_id": initial["obligation_id"],
                "dimension": initial["dimension"],
                "description": initial["description"],
                "status": "SATISFIED",
                "discovery_ids": ["target-source"],
                "evidence_task_ids": [evidence_row["evidence_task_id"]],
                "rationale": "fixture evidence satisfies the Profile initial obligation",
            }
            for initial in profile["research_scope"]["initial_obligations"]
        ]
        completeness_result = {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "research_profile": research_profile,
            "basis": {
                "production_profile_sha256": core.sha256_file(profile_path),
                "materiality_ledger_sha256": core.sha256_file(ledger_path),
            },
            "overall_status": "READY",
            "obligations": obligations,
            "residual_limitations": [],
            "closure": (
                {
                    "expansion_passes": 1,
                    "final_pass_new_sources": 0,
                    "final_pass_new_material_obligations": 0,
                    "final_pass_new_material_obligations_open": 0,
                    "targeted_gap_fill_completed": True,
                    "open_material_obligations": 0,
                    "limitations": [],
                    "status": "COMPLETE",
                }
                if research_profile == "THEMATIC"
                else None
            ),
        }
        self.assertEqual(
            completeness.validate_profile_completeness(
                completeness_result,
                root,
                profile_path,
                discovery_path,
                screening_acceptance,
                evidence_acceptance,
                views_acceptance,
                ledger_path,
                IMPLEMENTATION_SHA,
            ),
            [],
        )
        completeness_path = root / "sources" / issue_id / "profile-completeness.json"
        core.write_json(completeness_path, completeness_result)
        matrix = architecture.derive_candidate_matrix(
            root,
            profile_path,
            discovery_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            ledger_path,
            completeness_path,
            IMPLEMENTATION_SHA,
        )
        matrix_path = root / "sources" / issue_id / "candidate-matrix-v2.json"
        architecture.write_candidate_matrix(matrix_path, matrix)
        return {
            "root": root,
            "profile_path": profile_path,
            "discovery_path": discovery_path,
            "screening": screening_acceptance,
            "evidence": evidence_acceptance,
            "views": views_acceptance,
            "ledger_path": ledger_path,
            "completeness_path": completeness_path,
            "matrix_path": matrix_path,
            "matrix": matrix,
        }

    @staticmethod
    def selection_for(chain: dict, *, disposition: str = "SELECTED") -> dict:
        row = chain["matrix"]["rows"][0]
        profile = core.load_json(chain["profile_path"])
        selected = disposition == "SELECTED"
        assignments = [
            {
                "candidate_id": row["candidate_id"],
                "disposition": disposition,
                "rationale": "explicit editorial disposition for fixture",
                "architecture_usage": "PRIMARY" if selected else "NONE",
                "publication_role": (
                    f"{profile['publication_profile']}:FIXTURE_ROLE" if selected else None
                ),
                "architecture_role": (
                    f"{profile['research_profile']}:FIXTURE_ROLE" if selected else None
                ),
                "profile_extensions": {},
            }
        ]
        return {
            "schema_version": "2.0-rc1",
            "issue_id": chain["matrix"]["issue_id"],
            "research_profile": chain["matrix"]["research_profile"],
            "publication_profile": profile["publication_profile"],
            "selection_version": "v0.1",
            "status": "ESTABLISHED",
            "basis": {
                "production_profile_sha256": core.sha256_file(chain["profile_path"]),
                "candidate_matrix_sha256": core.sha256_file(chain["matrix_path"]),
                "profile_completeness_sha256": core.sha256_file(chain["completeness_path"]),
                "materiality_ledger_sha256": core.sha256_file(chain["ledger_path"]),
            },
            "assignments": assignments,
            "summary": {
                "candidate_count": len(assignments),
                "disposition_counts": {disposition: len(assignments)},
                "selected_count": 1 if selected else 0,
            },
        }

    @staticmethod
    def architecture_for(chain: dict, selection_path: Path, *, research_profile: str) -> dict:
        cid = chain["matrix"]["rows"][0]["candidate_id"]
        profile = core.load_json(chain["profile_path"])
        package_profile_extensions = (
            {"lineage_package_role": "CORE"}
            if research_profile == "THEMATIC"
            else {"weekly_package_role": "LATE_BREAKING"}
        )
        publication_extensions = (
            {"longform_chapter_kind": "lineage"}
            if research_profile == "THEMATIC"
            else {"magazine_package_kind": "late-breaking"}
        )
        return {
            "schema_version": "2.0-rc1",
            "issue_id": chain["matrix"]["issue_id"],
            "research_profile": research_profile,
            "publication_profile": profile["publication_profile"],
            "status": "PROPOSED",
            "basis": {
                "production_profile_sha256": core.sha256_file(chain["profile_path"]),
                "profile_completeness_sha256": core.sha256_file(chain["completeness_path"]),
                "materiality_ledger_sha256": core.sha256_file(chain["ledger_path"]),
                "candidate_matrix_sha256": core.sha256_file(chain["matrix_path"]),
                "candidate_selection_sha256": core.sha256_file(selection_path),
            },
            "editorial_thesis": "A bounded editorial thesis derived from selected evidence.",
            "architecture_goals": ["preserve evidence boundaries", "make compression auditable"],
            "page_plan": {"target_pages": 12, "max_pages": 24, "notes": "fixture-only planning"},
            "packages": [
                {
                    "package_id": "pkg-001",
                    "title": "Primary package",
                    "purpose": "Carry the selected primary candidate into drafting.",
                    "primary_candidate_ids": [cid],
                    "supporting_candidate_ids": [],
                    "must_cover_requirements": ["subject identity"],
                    "boundaries": list(chain["matrix"]["rows"][0]["remaining_boundaries"]),
                    "drafting_order": 1,
                    "profile_extensions": package_profile_extensions,
                    "publication_extensions": publication_extensions,
                }
            ],
            "selected_exceptions": [],
            "profile_extensions": {},
            "publication_extensions": {},
            "human_review": {
                "reviewed_by": None,
                "reviewed_at": None,
                "review_reference": None,
            },
        }

    def validate_selection(self, chain: dict, selection: dict) -> list[str]:
        return architecture.validate_selection(
            chain["root"],
            selection,
            chain["profile_path"],
            chain["matrix_path"],
            chain["completeness_path"],
            chain["ledger_path"],
        )

    def validate_architecture(self, chain: dict, plan: dict, selection_path: Path) -> list[str]:
        return architecture.validate_architecture(
            chain["root"],
            plan,
            chain["profile_path"],
            chain["completeness_path"],
            chain["ledger_path"],
            chain["matrix_path"],
            selection_path,
        )

    def test_weekly_and_thematic_share_core_without_dummy_profile_fields(self) -> None:
        for research_profile in ("WEEKLY", "THEMATIC"):
            with self.subTest(research_profile=research_profile):
                chain = self.chain(research_profile)
                row = chain["matrix"]["rows"][0]
                if research_profile == "WEEKLY":
                    self.assertEqual(
                        set(row["profile_extensions"]),
                        {"why_this_issue", "window_relation", "carry_over"},
                    )
                    self.assertNotIn("lineage_role", row["profile_extensions"])
                else:
                    self.assertIn("lineage_role", row["profile_extensions"])
                    self.assertNotIn("why_this_issue", row["profile_extensions"])
                self.assertNotIn("timing_relation", row)
                self.assertNotIn("why_now_confirmed", row)

                selection = self.selection_for(chain)
                self.assertEqual(self.validate_selection(chain, selection), [])
                selection_path = chain["root"] / f"selection-{research_profile}.json"
                core.write_json(selection_path, selection)
                plan = self.architecture_for(
                    chain, selection_path, research_profile=research_profile
                )
                self.assertEqual(self.validate_architecture(chain, plan, selection_path), [])
                plan_path = chain["root"] / f"architecture-{research_profile}.json"
                core.write_json(plan_path, plan)
                summary = architecture.build_architecture_review_summary(
                    chain["root"],
                    chain["profile_path"],
                    chain["discovery_path"],
                    chain["screening"],
                    chain["evidence"],
                    chain["views"],
                    chain["ledger_path"],
                    chain["completeness_path"],
                    chain["matrix_path"],
                    selection_path,
                    plan_path,
                    IMPLEMENTATION_SHA,
                )
                self.assertEqual(
                    summary["readiness"]["status"], "READY_FOR_ARCHITECTURE_REVIEW"
                )
                self.assertEqual(
                    summary["major_material_destinations"][0]["destination_kind"],
                    "PRIMARY",
                )

    def test_matrix_is_exact_derivation_and_cannot_silently_drop_material_candidate(self) -> None:
        chain = self.chain("THEMATIC")
        self.assertEqual(
            architecture.validate_candidate_matrix(
                chain["matrix"],
                chain["root"],
                chain["profile_path"],
                chain["discovery_path"],
                chain["screening"],
                chain["evidence"],
                chain["views"],
                chain["ledger_path"],
                chain["completeness_path"],
                IMPLEMENTATION_SHA,
            ),
            [],
        )
        truncated = copy.deepcopy(chain["matrix"])
        truncated["rows"] = []
        truncated["summary"] = {
            "candidate_count": 0,
            "materiality_counts": {},
            "evidence_status_counts": {},
        }
        errors = architecture.validate_candidate_matrix(
            truncated,
            chain["root"],
            chain["profile_path"],
            chain["discovery_path"],
            chain["screening"],
            chain["evidence"],
            chain["views"],
            chain["ledger_path"],
            chain["completeness_path"],
            IMPLEMENTATION_SHA,
        )
        self.assertTrue(errors)
        self.assertIn("does not exactly match", errors[0])

    def test_selection_is_internal_complete_and_has_no_human_approval_semantics(self) -> None:
        chain = self.chain("WEEKLY")
        selection = self.selection_for(chain)
        selection["approval"] = {"approved_by": "human"}
        self.assertIn("Human approval fields are forbidden", "; ".join(self.validate_selection(chain, selection)))

        selection = self.selection_for(chain)
        selection["assignments"] = []
        selection["summary"] = {
            "candidate_count": 0,
            "disposition_counts": {},
            "selected_count": 0,
        }
        self.assertIn(
            "assign every Matrix candidate exactly once",
            "; ".join(self.validate_selection(chain, selection)),
        )

    def test_profile_owned_roles_use_owned_namespace_without_global_enum(self) -> None:
        chain = self.chain("THEMATIC")
        selection = self.selection_for(chain)
        selection["assignments"][0]["publication_role"] = "LONGFORM_SPECIAL:CUSTOM_FUTURE_ROLE"
        selection["assignments"][0]["architecture_role"] = "THEMATIC:LINEAGE_BRANCH_ALPHA"
        self.assertEqual(self.validate_selection(chain, selection), [])

        wrong_namespace = copy.deepcopy(selection)
        wrong_namespace["assignments"][0]["publication_role"] = "WEEKLY_MAGAZINE:LATE_BREAKING"
        self.assertIn(
            "outside Publication Profile namespace LONGFORM_SPECIAL:",
            "; ".join(self.validate_selection(chain, wrong_namespace)),
        )
        wrong_namespace = copy.deepcopy(selection)
        wrong_namespace["assignments"][0]["architecture_role"] = "WEEKLY:LATE_BREAKING"
        self.assertIn(
            "outside Research Profile namespace THEMATIC:",
            "; ".join(self.validate_selection(chain, wrong_namespace)),
        )

        changed_matrix = copy.deepcopy(chain["matrix"])
        changed_matrix["rows"][0]["materiality"] = "NON_MATERIAL"
        changed_matrix["summary"]["materiality_counts"] = {"NON_MATERIAL": 1}
        changed_path = chain["root"] / "changed-matrix.json"
        core.write_json(changed_path, changed_matrix)
        selection["basis"]["candidate_matrix_sha256"] = core.sha256_file(changed_path)
        errors = architecture.validate_selection(
            chain["root"],
            selection,
            chain["profile_path"],
            changed_path,
            chain["completeness_path"],
            chain["ledger_path"],
        )
        self.assertIn("NON_MATERIAL candidate cannot be SELECTED", "; ".join(errors))

    def test_selected_primary_requires_exactly_one_destination_or_exception(self) -> None:
        chain = self.chain("THEMATIC")
        selection = self.selection_for(chain)
        selection_path = chain["root"] / "selection.json"
        core.write_json(selection_path, selection)
        plan = self.architecture_for(chain, selection_path, research_profile="THEMATIC")
        plan["packages"][0]["primary_candidate_ids"] = []
        errors = self.validate_architecture(chain, plan, selection_path)
        self.assertIn("requires exactly one Architecture destination", "; ".join(errors))

        cid = selection["assignments"][0]["candidate_id"]
        plan["selected_exceptions"] = [
            {
                "candidate_id": cid,
                "reason": "explicit structural deferral",
                "exception_kind": "DEFERRED",
            }
        ]
        errors = self.validate_architecture(chain, plan, selection_path)
        self.assertNotIn("requires exactly one Architecture destination", "; ".join(errors))
        self.assertIn("requires prior factual candidate placements", "; ".join(errors))

    def test_review_summary_blocks_valid_but_incomplete_profile_completeness(self) -> None:
        chain = self.chain("THEMATIC")
        incomplete = core.load_json(chain["completeness_path"])
        incomplete["obligations"][0]["status"] = "NEEDS_RESEARCH"
        incomplete["overall_status"] = "INCOMPLETE"
        incomplete["closure"]["open_material_obligations"] = 1
        incomplete["closure"]["status"] = "NEEDS_RESEARCH"
        incomplete_path = chain["root"] / "incomplete.json"
        core.write_json(incomplete_path, incomplete)
        self.assertEqual(
            completeness.validate_profile_completeness(
                incomplete,
                chain["root"],
                chain["profile_path"],
                chain["discovery_path"],
                chain["screening"],
                chain["evidence"],
                chain["views"],
                chain["ledger_path"],
                IMPLEMENTATION_SHA,
            ),
            [],
        )
        matrix = architecture.derive_candidate_matrix(
            chain["root"],
            chain["profile_path"],
            chain["discovery_path"],
            chain["screening"],
            chain["evidence"],
            chain["views"],
            chain["ledger_path"],
            incomplete_path,
            IMPLEMENTATION_SHA,
        )
        matrix_path = chain["root"] / "matrix-incomplete.json"
        core.write_json(matrix_path, matrix)
        altered_chain = dict(chain)
        altered_chain["matrix"] = matrix
        altered_chain["matrix_path"] = matrix_path
        altered_chain["completeness_path"] = incomplete_path
        selection = self.selection_for(altered_chain)
        selection_path = chain["root"] / "selection-incomplete.json"
        core.write_json(selection_path, selection)
        plan = self.architecture_for(
            altered_chain, selection_path, research_profile="THEMATIC"
        )
        plan_path = chain["root"] / "architecture-incomplete.json"
        core.write_json(plan_path, plan)
        summary = architecture.build_architecture_review_summary(
            chain["root"],
            chain["profile_path"],
            chain["discovery_path"],
            chain["screening"],
            chain["evidence"],
            chain["views"],
            chain["ledger_path"],
            incomplete_path,
            matrix_path,
            selection_path,
            plan_path,
            IMPLEMENTATION_SHA,
        )
        self.assertEqual(summary["readiness"]["status"], "BLOCKED")
        self.assertIn(
            "Completeness is INCOMPLETE",
            "; ".join(summary["readiness"]["errors"]),
        )


if __name__ == "__main__":
    unittest.main()