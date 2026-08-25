from __future__ import annotations

import copy
import shutil
import unittest
from pathlib import Path

from scripts import survey_architecture_v2 as architecture
from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from tests import test_survey_architecture_v2 as architecture_tests


IMPLEMENTATION_SHA = "4" * 40


class SurveyDraftingV2Tests(unittest.TestCase):
    def build_authorized_chain(self, research_profile: str) -> dict:
        chain = architecture_tests.SurveyArchitectureV2Tests.chain(self, research_profile)

        # Drafting production consumes the content-addressed canonical accepted
        # Evidence tree, not only the earlier per-run acceptance. Preserve the
        # exact accepted bytes while making this Draft fixture match that
        # production authority shape.
        evidence_acceptance = core.load_json(chain["evidence"])
        accepted_dir = (
            chain["profile_path"].parent
            / "evidence"
            / "v2"
            / "accepted"
            / evidence_acceptance["result_set_sha256"]
        )
        accepted_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(chain["evidence"].parent, accepted_dir)

        selection = architecture_tests.SurveyArchitectureV2Tests.selection_for(chain)
        selection_path = chain["root"] / "selection-v2.json"
        core.write_json(selection_path, selection)
        plan = architecture_tests.SurveyArchitectureV2Tests.architecture_for(
            chain, selection_path, research_profile=research_profile
        )
        architecture_path = chain["root"] / "architecture-v2.json"
        core.write_json(architecture_path, plan)
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
            architecture_path,
            IMPLEMENTATION_SHA,
        )
        self.assertEqual(summary["readiness"]["status"], "READY_FOR_ARCHITECTURE_REVIEW")
        summary_path = chain["root"] / "architecture-review-summary-v2.json"
        core.write_json(summary_path, summary)
        attention_path = chain["root"] / "architecture-review-attention-v2.json"
        review_attention.build_attention(
            chain["root"], chain["screening"], chain["ledger_path"], selection_path, attention_path
        )
        approval = {
            "schema_version": "2.0-rc1",
            "approval_id": f"approval:{chain['matrix']['issue_id']}:architecture",
            "issue_id": chain["matrix"]["issue_id"],
            "gate": "ARCHITECTURE_REVIEW",
            "decision": "APPROVED",
            "architecture_sha256": core.sha256_file(architecture_path),
            "architecture_review_summary_sha256": core.sha256_file(summary_path),
            "architecture_review_attention_sha256": core.sha256_file(attention_path),
            "reviewed_by": "human-reviewer",
            "reviewed_at": "2026-08-22T03:00:00+09:00",
            "review_reference": "human-gate-fixture",
        }
        approval_path = chain["root"] / "architecture-approval-v2.json"
        core.write_json(approval_path, approval)
        chain.update(
            {
                "selection_path": selection_path,
                "architecture_path": architecture_path,
                "review_summary_path": summary_path,
                "review_attention_path": attention_path,
                "approval_path": approval_path,
            }
        )
        return chain

    def derive_package(self, chain: dict) -> dict:
        package_id = core.load_json(chain["architecture_path"])["packages"][0]["package_id"]
        return drafting.derive_draft_package(
            chain["root"],
            chain["profile_path"],
            chain["discovery_path"],
            chain["screening"],
            chain["evidence"],
            chain["views"],
            chain["ledger_path"],
            chain["completeness_path"],
            chain["matrix_path"],
            chain["selection_path"],
            chain["architecture_path"],
            chain["review_summary_path"],
            chain["approval_path"],
            package_id,
            IMPLEMENTATION_SHA,
        )

    @staticmethod
    def valid_result(package: dict, package_path: Path, prompt_path: Path) -> dict:
        card = package["evidence_inputs"][0]["evidence_card"]
        task_id = package["evidence_inputs"][0]["evidence_task_id"]
        claim = card["claims"][0]
        ref = {
            "evidence_task_id": task_id,
            "kind": "CLAIM",
            "evidence_id": claim["statement_id"],
            "subject_id": claim["subject_id"],
            "subject_role": claim["subject_role"],
        }
        block_id = "block-001"
        return {
            "schema_version": "2.0-rc1",
            "issue_id": package["issue_id"],
            "research_profile": package["research_profile"],
            "publication_profile": package["publication_profile"],
            "package_id": package["package_id"],
            "draft_version": "v0.1",
            "status": "ESTABLISHED",
            "basis": {
                "draft_package_sha256": core.sha256_file(package_path),
                "prompt_id": "article-drafting-v2",
                "prompt_sha256": core.sha256_file(prompt_path),
            },
            "runner": {
                "provider": "fixture",
                "model": "fixture-model",
                "invocation": "unit-test",
                "generated_at": "2026-08-22T03:10:00+09:00",
                "run_reference": None,
            },
            "headline": "Evidence-bound headline",
            "deck": "The source authors report the tested method.",
            "deck_attribution_mode": "ATTRIBUTED",
            "deck_evidence_refs": [copy.deepcopy(ref)],
            "blocks": [
                {
                    "block_id": block_id,
                    "block_type": "PARAGRAPH",
                    "text": "The source authors report that Target Model introduces the tested method.",
                    "attribution_mode": "ATTRIBUTED",
                    "evidence_refs": [copy.deepcopy(ref)],
                }
            ],
            "must_cover_coverage": [
                {"requirement": requirement, "block_ids": [block_id]}
                for requirement in package["package"]["must_cover_requirements"]
            ],
            "boundary_dispositions": [
                {
                    "boundary": boundary,
                    "handling": "RESPECTED_BY_OMISSION",
                    "block_ids": [],
                    "rationale": "The unsupported statement is intentionally omitted.",
                }
                for boundary in package["package"]["boundaries"]
            ],
            "profile_extensions": {},
            "publication_extensions": {},
        }

    def test_weekly_and_thematic_share_generic_draft_contract_without_dummy_fields(self) -> None:
        for research_profile in ("WEEKLY", "THEMATIC"):
            with self.subTest(research_profile=research_profile):
                chain = self.build_authorized_chain(research_profile)
                package = self.derive_package(chain)
                self.assertNotIn("late_breaking", package["package"])
                self.assertNotIn("this_week_summary_forbidden", package["drafting_constraints"])
                if research_profile == "WEEKLY":
                    self.assertIn("weekly_package_role", package["profile_extensions"])
                    self.assertNotIn("lineage_package_role", package["profile_extensions"])
                else:
                    self.assertIn("lineage_package_role", package["profile_extensions"])
                    self.assertNotIn("weekly_package_role", package["profile_extensions"])

                package_path = chain["root"] / f"draft-package-{research_profile}.json"
                core.write_json(package_path, package)
                result = self.valid_result(package, package_path, chain["root"] / drafting.DRAFT_PROMPT)
                self.assertEqual(
                    drafting.validate_draft_result(result, package_path, chain["root"] / drafting.DRAFT_PROMPT),
                    [],
                )
                self.assertNotIn("late_breaking_acknowledged", result)

    def test_drafting_requires_exact_independent_architecture_approval(self) -> None:
        chain = self.build_authorized_chain("THEMATIC")
        approval = core.load_json(chain["approval_path"])
        approval["architecture_sha256"] = "0" * 64
        core.write_json(chain["approval_path"], approval)
        with self.assertRaisesRegex(ValueError, "does not bind exact Architecture bytes"):
            self.derive_package(chain)

    def test_draft_result_rejects_subject_rebinding_and_silent_requirement_drop(self) -> None:
        chain = self.build_authorized_chain("THEMATIC")
        package = self.derive_package(chain)
        package_path = chain["root"] / "draft-package.json"
        core.write_json(package_path, package)
        prompt_path = chain["root"] / drafting.DRAFT_PROMPT
        result = self.valid_result(package, package_path, prompt_path)

        rebound = copy.deepcopy(result)
        rebound["blocks"][0]["evidence_refs"][0]["subject_id"] = "comparator"
        errors = drafting.validate_draft_result(rebound, package_path, prompt_path)
        self.assertTrue(any("subject binding does not match" in error for error in errors))

        dropped = copy.deepcopy(result)
        dropped["must_cover_coverage"] = []
        errors = drafting.validate_draft_result(dropped, package_path, prompt_path)
        self.assertTrue(any("must-cover requirement exactly once" in error for error in errors))

        weekly_pollution = copy.deepcopy(result)
        weekly_pollution["late_breaking_acknowledged"] = False
        self.assertIn(
            "fields must exactly match generic v2 contract",
            "; ".join(drafting.validate_draft_result(weekly_pollution, package_path, prompt_path)),
        )

    def test_profile_synthesis_payload_is_profile_owned_and_exact_input_bound(self) -> None:
        for research_profile in ("WEEKLY", "THEMATIC"):
            with self.subTest(research_profile=research_profile):
                chain = self.build_authorized_chain(research_profile)
                package = self.derive_package(chain)
                package_path = chain["root"] / f"package-{research_profile}.json"
                core.write_json(package_path, package)
                result = self.valid_result(package, package_path, chain["root"] / drafting.DRAFT_PROMPT)
                result_path = chain["root"] / f"result-{research_profile}.json"
                core.write_json(result_path, result)
                synthesis_input = drafting.build_synthesis_input(
                    chain["root"],
                    chain["profile_path"],
                    chain["architecture_path"],
                    chain["review_summary_path"],
                    chain["approval_path"],
                    [(package_path, result_path)],
                )
                input_path = chain["root"] / f"synthesis-input-{research_profile}.json"
                core.write_json(input_path, synthesis_input)
                payload = {
                    key: f"fixture {key}"
                    for key in synthesis_input["profile_payload_requirements"]
                }
                synthesis_result = {
                    "schema_version": "2.0-rc1",
                    "issue_id": synthesis_input["issue_id"],
                    "research_profile": synthesis_input["research_profile"],
                    "publication_profile": synthesis_input["publication_profile"],
                    "synthesis_version": "v0.1",
                    "status": "ESTABLISHED",
                    "basis": {
                        "synthesis_input_sha256": core.sha256_file(input_path),
                        "prompt_id": "profile-synthesis-v2",
                        "prompt_sha256": core.sha256_file(chain["root"] / drafting.SYNTHESIS_PROMPT),
                    },
                    "runner": {
                        "provider": "fixture",
                        "model": "fixture-model",
                        "invocation": "unit-test",
                        "generated_at": "2026-08-22T03:20:00+09:00",
                        "run_reference": None,
                    },
                    "profile_payload": payload,
                    "publication_payload": {},
                }
                self.assertEqual(
                    drafting.validate_synthesis_result(
                        synthesis_result, input_path, chain["root"] / drafting.SYNTHESIS_PROMPT
                    ),
                    [],
                )
                if research_profile == "THEMATIC":
                    self.assertNotIn("signals", payload)
                    polluted = copy.deepcopy(synthesis_result)
                    polluted["profile_payload"]["this_week_signals"] = "forbidden dummy"
                    self.assertTrue(
                        any(
                            "Profile-owned requirements" in error
                            for error in drafting.validate_synthesis_result(
                                polluted, input_path, chain["root"] / drafting.SYNTHESIS_PROMPT
                            )
                        )
                    )
                else:
                    self.assertIn("signals", payload)
                    self.assertNotIn("branch_transition_synthesis", payload)

    def test_wu009_schema_drift_invalidates_initialized_state(self) -> None:
        chain = self.build_authorized_chain("THEMATIC")
        state_path = chain["root"] / "sources" / chain["matrix"]["issue_id"] / "production-state.json"
        state = core.load_json(state_path)
        contract_path = chain["root"] / drafting.DRAFT_RESULT_SCHEMA
        contract_path.write_text(contract_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "semantic contract files differ"):
            core.transition_state(
                chain["root"],
                core.load_json(chain["root"] / core.DEFAULT_CONFIG),
                state,
                "DISCOVERY_COLLECTED",
                IMPLEMENTATION_SHA,
                core.parse_instant("2026-08-22T03:30:00+09:00"),
            )


if __name__ == "__main__":
    unittest.main()
