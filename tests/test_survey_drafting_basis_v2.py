from __future__ import annotations

import copy
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_architecture_v2 as architecture
from scripts import survey_completeness_v2 as completeness
from scripts import survey_discovery_v2 as discovery
from scripts import survey_drafting_v2 as drafting
from scripts import survey_drafting_v2_base as drafting_base
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_screening_v2 as screening
from tests import test_survey_evidence_v2 as evidence_tests


IMPLEMENTATION_SHA = "4" * 40


class DraftingEffectiveDiscoveryBasisTests(unittest.TestCase):
    """Drafting must resolve the validated effective Screening Discovery basis.

    Screening supports DIRECT (root == effective) and validated
    DERIVED_EXPANSION bases. Drafting callers canonically supply the root
    Discovery path; Candidate Matrix re-derivation requires the effective path.
    These tests lock the generic (profile-neutral, issue-neutral) behavior:
    DIRECT unchanged, DERIVED_EXPANSION repaired, unrelated bases rejected,
    and package/provenance authority never weakened.
    """

    # -- fixture builders -------------------------------------------------

    def _record(
        self,
        issue_id: str,
        discovery_id: str,
        origin: str,
        source: dict,
        *,
        parent_refs: list[str] | None = None,
        obligation_ids: list[str] | None = None,
        research_pass: int = 0,
    ) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "discovery_id": discovery_id,
            "provenance": {
                "origin": origin,
                "research_pass": research_pass,
                "parent_refs": parent_refs or [],
                "obligation_ids": obligation_ids or [],
                "reason": f"fixture provenance for {discovery_id}",
            },
            "source": copy.deepcopy(source),
        }

    def _patch_root_acceptance(self, root: Path, root_path: Path, issue_id: str):
        """Bind the resolver to the sandbox root graph (repo-established pattern).

        Materializing a real Discovery acceptance requires X Intake authority,
        so DERIVED_EXPANSION fixtures bind the accepted root graph the same way
        as the Screening expansion-authority tests: a marker file plus a patched
        Discovery acceptance reader returning normalized root records.
        """
        marker = root / "sources" / issue_id / "discovery" / "discovery-accepted-v2.json"
        core.write_json(marker, {"fixture": "patched root Discovery authority"})
        root_records = screening.read_jsonl(root_path)
        normalized = [
            discovery._normalize_record(root, row, issue_id) for row in root_records
        ]

        def fake_root_acceptance(repo_root: Path, acceptance_path: Path) -> dict:
            return {
                "issue_id": issue_id,
                "discovery_path": str(root_path.relative_to(root)),
                "discovery_sha256": core.sha256_file(root_path),
                "records": normalized,
            }

        patcher = mock.patch.object(
            discovery, "validate_acceptance", side_effect=fake_root_acceptance
        )
        patcher.start()
        self.addCleanup(patcher.stop)

    def _screening_results(
        self, root: Path, package_path: Path, decisions: dict[str, str]
    ) -> Path:
        package = core.load_json(package_path)
        results_dir = package_path.parent / "results"
        results_dir.mkdir(parents=True)
        for batch in package["input"]["batches"]:
            rows = screening.read_jsonl(package_path.parent / batch["path"])
            core.write_json(
                results_dir / f"{batch['batch_id']}.json",
                {
                    "schema_version": "2.0-rc1",
                    "issue_id": package["issue_id"],
                    "batch_id": batch["batch_id"],
                    "basis": screening.expected_result_basis(
                        root, package_path, package, batch
                    ),
                    "decisions": [
                        {
                            "discovery_id": row["discovery_id"],
                            "decision": decisions[row["discovery_id"]],
                            "reason": "explicit test disposition",
                            "scope_tags": ["fixture"],
                            "duplicate_group": None,
                            "verification_targets": ["canonical source"],
                            "confidence": "high",
                        }
                        for row in rows
                    ],
                },
            )
        return results_dir

    def _derived_chain(self, research_profile: str) -> dict:
        """Build root -> DERIVED_EXPANSION -> Screening -> Evidence -> Matrix chain."""
        helper = evidence_tests.SurveyEvidenceV2Tests(
            methodName="test_evidence_package_is_exact_and_preserves_task_bytes"
        )
        helper.setUp()
        temp, root, cfg = helper.sandbox()
        self.addCleanup(temp.cleanup)
        profile_path, state_path = helper.init_profile(root, cfg, research_profile)
        issue_id = core.load_json(state_path)["issue_id"]

        raw = root / "raw/source.json"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text('{"fixture":"shared raw"}\n', encoding="utf-8")
        source_a = helper.source(f"https://example.invalid/root-a")
        source_b = helper.source(f"https://example.invalid/root-b")
        roots = [
            self._record(issue_id, "root-a", "BASE", source_a),
            self._record(issue_id, "root-b", "BASE", source_b),
        ]
        children = [
            self._record(
                issue_id, "child-1", "REFERENCE_EXPANSION", source_a,
                parent_refs=["root-a"], research_pass=1,
            ),
            self._record(
                issue_id, "child-2", "REFERENCE_EXPANSION", source_b,
                parent_refs=["root-b"], research_pass=1,
            ),
        ]
        root_path = root / "sources" / issue_id / "discovery" / "discovery.jsonl"
        derived_path = root / "sources" / issue_id / "screening" / "input" / "event-discovery.jsonl"
        screening.write_jsonl(root_path, roots)
        screening.write_jsonl(derived_path, children)
        self._patch_root_acceptance(root, root_path, issue_id)

        package_path = screening.prepare_package(
            root,
            state_path,
            derived_path,
            root / "sources" / issue_id / "screening" / "v2" / "package",
            IMPLEMENTATION_SHA,
        )
        results_dir = self._screening_results(
            root, package_path, {"child-1": "KEEP", "child-2": "KEEP"}
        )
        screening_acceptance = screening.accept_results(
            root,
            package_path,
            results_dir,
            root / "sources" / issue_id / "screening" / "v2" / "runs",
            IMPLEMENTATION_SHA,
        )
        resolved = screening.resolve_effective_discovery_basis(
            root, package_path, IMPLEMENTATION_SHA
        )
        self.assertEqual(resolved["mode"], "DERIVED_EXPANSION")

        _, evidence_acceptance = helper.make_evidence(
            root, state_path, derived_path, screening_acceptance
        )
        views_acceptance = helper.make_views(root, profile_path, evidence_acceptance)
        ledger = evidence.build_materiality_ledger(
            root,
            profile_path,
            derived_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            IMPLEMENTATION_SHA,
        )
        ledger_path = root / "sources" / issue_id / "materiality-ledger.json"
        evidence.write_materiality_ledger(ledger_path, ledger)
        profile = core.load_json(profile_path)
        evidence_rows = core.load_json(evidence_acceptance)["results"]
        obligations = [
            {
                "obligation_id": initial["obligation_id"],
                "dimension": initial["dimension"],
                "description": initial["description"],
                "status": "SATISFIED",
                "discovery_ids": ["child-1", "child-2"],
                "evidence_task_ids": [row["evidence_task_id"] for row in evidence_rows],
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
                    "final_pass_new_sources": 2,
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
                derived_path,
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
            derived_path,
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
            "state_path": state_path,
            "issue_id": issue_id,
            "root_path": root_path,
            "derived_path": derived_path,
            "screening": screening_acceptance,
            "evidence": evidence_acceptance,
            "views": views_acceptance,
            "ledger_path": ledger_path,
            "completeness_path": completeness_path,
            "matrix_path": matrix_path,
            "matrix": matrix,
            "research_profile": research_profile,
        }

    def _selection_for(self, chain: dict) -> dict:
        profile = core.load_json(chain["profile_path"])
        rows = sorted(chain["matrix"]["rows"], key=lambda row: row["candidate_id"])
        usages = ["PRIMARY", "SUPPORTING"]
        assignments = [
            {
                "candidate_id": row["candidate_id"],
                "disposition": "SELECTED",
                "rationale": "explicit editorial disposition for fixture",
                "architecture_usage": usages[index % len(usages)],
                "publication_role": f"{profile['publication_profile']}:FIXTURE_ROLE",
                "architecture_role": f"{profile['research_profile']}:FIXTURE_ROLE",
                "profile_extensions": {},
            }
            for index, row in enumerate(rows)
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
                "disposition_counts": {"SELECTED": len(assignments)},
                "selected_count": len(assignments),
            },
        }

    def _architecture_for(
        self,
        chain: dict,
        selection_path: Path,
        research_profile: str,
        *,
        extra_packages: tuple[dict, ...] = (),
    ) -> dict:
        selection = core.load_json(selection_path)
        usage = {row["candidate_id"]: row["architecture_usage"] for row in selection["assignments"]}
        primary = sorted(cid for cid, kind in usage.items() if kind == "PRIMARY")
        supporting = sorted(cid for cid, kind in usage.items() if kind == "SUPPORTING")
        profile = core.load_json(chain["profile_path"])
        boundaries = sorted(
            {
                boundary
                for row in chain["matrix"]["rows"]
                for boundary in row["remaining_boundaries"]
            }
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
                    "purpose": "Carry the selected candidates into drafting.",
                    "primary_candidate_ids": primary,
                    "supporting_candidate_ids": supporting,
                    "must_cover_requirements": ["subject identity"],
                    "boundaries": boundaries,
                    "drafting_order": 1,
                    "profile_extensions": (
                        {"lineage_package_role": "CORE"}
                        if research_profile == "THEMATIC"
                        else {"weekly_package_role": "LATE_BREAKING"}
                    ),
                    "publication_extensions": (
                        {"longform_chapter_kind": "lineage"}
                        if research_profile == "THEMATIC"
                        else {"magazine_package_kind": "late-breaking"}
                    ),
                },
                *extra_packages,
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

    def _authorized_drafting_chain(
        self, research_profile: str, *, extra_packages: tuple[dict, ...] = ()
    ) -> dict:
        chain = self._derived_chain(research_profile)
        root = chain["root"]
        selection = self._selection_for(chain)
        selection_path = root / "selection-v2.json"
        core.write_json(selection_path, selection)
        plan = self._architecture_for(
            chain, selection_path, research_profile, extra_packages=extra_packages
        )
        architecture_path = root / "architecture-v2.json"
        core.write_json(architecture_path, plan)
        summary = architecture.build_architecture_review_summary(
            root,
            chain["profile_path"],
            chain["derived_path"],
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
        summary_path = root / "architecture-review-summary-v2.json"
        core.write_json(summary_path, summary)
        attention_path = root / "architecture-review-attention-v2.json"
        review_attention.build_attention(
            root, chain["screening"], chain["ledger_path"], selection_path, attention_path
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
        approval_path = root / "architecture-approval-v2.json"
        core.write_json(approval_path, approval)
        chain.update(
            {
                "selection_path": selection_path,
                "architecture_path": architecture_path,
                "review_summary_path": summary_path,
                "review_attention_path": attention_path,
                "approval_path": approval_path,
                "package_id": "pkg-001",
            }
        )
        return chain

    def _derive(self, chain: dict, discovery_path: Path) -> dict:
        return drafting.derive_draft_package(
            chain["root"],
            chain["profile_path"],
            discovery_path,
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
            chain["package_id"],
            IMPLEMENTATION_SHA,
        )

    # -- requirement A: DIRECT compatibility --------------------------------

    def test_direct_basis_resolution_is_identity(self) -> None:
        from tests import test_survey_drafting_v2 as drafting_tests

        helper = drafting_tests.SurveyDraftingV2Tests(
            methodName="test_drafting_requires_exact_independent_architecture_approval"
        )
        chain = helper.build_authorized_chain("THEMATIC")
        self.addCleanup(helper.doCleanups)
        resolved = drafting_base._resolve_effective_screening_discovery(
            chain["root"], chain["screening"], chain["discovery_path"], IMPLEMENTATION_SHA
        )
        self.assertEqual(resolved.resolve(), chain["discovery_path"].resolve())
        package = helper.derive_package(chain)
        self.assertEqual(package["package_id"], core.load_json(chain["architecture_path"])["packages"][0]["package_id"])

    # -- requirements B/C: DERIVED_EXPANSION from root / effective caller -----

    def test_derived_expansion_from_root_caller_passes(self) -> None:
        for research_profile in ("THEMATIC", "WEEKLY"):
            with self.subTest(research_profile=research_profile):
                chain = self._authorized_drafting_chain(research_profile)
                package = self._derive(chain, chain["root_path"])
                self.assertEqual(package["package_id"], "pkg-001")
                self.assertEqual(len(package["evidence_inputs"]), 2)

    def test_derived_expansion_from_effective_caller_passes(self) -> None:
        chain = self._authorized_drafting_chain("THEMATIC")
        package = self._derive(chain, chain["derived_path"])
        self.assertEqual(package["package_id"], "pkg-001")
        self.assertEqual(len(package["evidence_inputs"]), 2)

    def test_cross_package_synthesis_shares_effective_basis(self) -> None:
        """The synthesis wrapper resolves the same effective basis from root."""
        synthesis_package = {
            "package_id": "pkg-002",
            "title": "Cross-package synthesis",
            "purpose": "Synthesize already-placed candidates without new destinations.",
            "primary_candidate_ids": [],
            "supporting_candidate_ids": [],
            "must_cover_requirements": [],
            "boundaries": [],
            "drafting_order": 2,
            "profile_extensions": {"lineage_package_role": "SYNTHESIS"},
            "publication_extensions": {"longform_chapter_kind": "synthesis"},
        }
        chain = self._authorized_drafting_chain(
            "THEMATIC", extra_packages=(synthesis_package,)
        )
        package = drafting.derive_draft_package(
            chain["root"],
            chain["profile_path"],
            chain["root_path"],
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
            "pkg-002",
            IMPLEMENTATION_SHA,
        )
        self.assertEqual(package["package_id"], "pkg-002")
        self.assertEqual(len(package["evidence_inputs"]), 2)
        self.assertTrue(
            all(item["architecture_usage"] == "SUPPORTING" for item in package["evidence_inputs"])
        )

    # -- requirement D: unrelated Discovery rejected --------------------------

    def test_unrelated_discovery_is_rejected_fail_closed(self) -> None:
        chain = self._authorized_drafting_chain("THEMATIC")
        helper = evidence_tests.SurveyEvidenceV2Tests(
            methodName="test_evidence_package_is_exact_and_preserves_task_bytes"
        )
        helper.setUp()
        unrelated_path = chain["root"] / "sources" / chain["issue_id"] / "discovery" / "unrelated.jsonl"
        screening.write_jsonl(
            unrelated_path, [helper.discovery(chain["issue_id"], "unrelated-source")]
        )
        with self.assertRaisesRegex(
            ValueError, "does not match validated Screening root/effective Discovery"
        ):
            self._derive(chain, unrelated_path)

    # -- requirement E: package binding tamper ---------------------------------

    def test_screening_package_binding_tamper_fails_closed(self) -> None:
        chain = self._authorized_drafting_chain("THEMATIC")
        acceptance_path = chain["screening"]
        package_path = acceptance_path.parent / "package.json"

        with self.subTest(case="sibling package missing"):
            missing = package_path.with_name("package.json.moved-aside")
            package_path.rename(missing)
            try:
                with self.assertRaises(ValueError):
                    self._derive(chain, chain["root_path"])
            finally:
                missing.rename(package_path)

        with self.subTest(case="acceptance package_sha256 mismatch"):
            acceptance = core.load_json(acceptance_path)
            tampered = copy.deepcopy(acceptance)
            tampered["package_sha256"] = "0" * 64
            core.write_json(acceptance_path, tampered)
            try:
                with self.assertRaises(ValueError):
                    self._derive(chain, chain["root_path"])
            finally:
                core.write_json(acceptance_path, acceptance)

        with self.subTest(case="actual package SHA mismatch"):
            package = core.load_json(package_path)
            tampered = copy.deepcopy(package)
            tampered["prompt"]["sha256"] = "0" * 64
            core.write_json(package_path, tampered)
            try:
                with self.assertRaises(ValueError):
                    self._derive(chain, chain["root_path"])
            finally:
                core.write_json(package_path, package)

    # -- requirement F: derived Discovery drift --------------------------------

    def test_derived_discovery_drift_fails_closed(self) -> None:
        chain = self._authorized_drafting_chain("THEMATIC")
        # Any byte change breaks the package-declared discovery SHA binding.
        # (Appended blank lines are skipped by the JSONL reader, so this
        # isolates the SHA-drift check from record-content checks.)
        with open(chain["derived_path"], "a", encoding="utf-8") as fh:
            fh.write("\n")
        with self.assertRaisesRegex(ValueError, "basis drift"):
            self._derive(chain, chain["root_path"])

    # -- requirement G: expansion provenance corruption -------------------------

    def _screening_prepare_for_corrupt_children(
        self, children: list[dict]
    ) -> dict:
        """Prepare (not accept) a Screening package over corrupt expansion children.

        Acceptance itself must fail: it runs the same
        ``resolve_effective_discovery_basis`` authority that the Drafting loader
        consumes, so corruption can never reach Drafting re-derivation.
        """
        helper = evidence_tests.SurveyEvidenceV2Tests(
            methodName="test_evidence_package_is_exact_and_preserves_task_bytes"
        )
        helper.setUp()
        temp, root, cfg = helper.sandbox()
        self.addCleanup(temp.cleanup)
        profile_path, state_path = helper.init_profile(root, cfg, "THEMATIC")
        issue_id = core.load_json(state_path)["issue_id"]
        raw = root / "raw/source.json"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text('{"fixture":"shared raw"}\n', encoding="utf-8")
        source_a = helper.source("https://example.invalid/root-a")
        source_b = helper.source("https://example.invalid/root-b")
        roots = [
            self._record(issue_id, "root-a", "BASE", source_a),
            self._record(issue_id, "root-b", "BASE", source_b),
        ]
        root_path = root / "sources" / issue_id / "discovery" / "discovery.jsonl"
        derived_path = root / "sources" / issue_id / "screening" / "input" / "event-discovery.jsonl"
        screening.write_jsonl(root_path, roots)
        screening.write_jsonl(derived_path, children)
        self._patch_root_acceptance(root, root_path, issue_id)
        package_path = screening.prepare_package(
            root,
            state_path,
            derived_path,
            root / "sources" / issue_id / "screening" / "v2" / "package",
            IMPLEMENTATION_SHA,
        )
        package = core.load_json(package_path)
        results_dir = package_path.parent / "results"
        results_dir.mkdir(parents=True)
        for batch in package["input"]["batches"]:
            rows = screening.read_jsonl(package_path.parent / batch["path"])
            core.write_json(
                results_dir / f"{batch['batch_id']}.json",
                {
                    "schema_version": "2.0-rc1",
                    "issue_id": issue_id,
                    "batch_id": batch["batch_id"],
                    "basis": screening.expected_result_basis(root, package_path, package, batch),
                    "decisions": [
                        {
                            "discovery_id": row["discovery_id"],
                            "decision": "KEEP",
                            "reason": "explicit test disposition",
                            "scope_tags": ["fixture"],
                            "duplicate_group": None,
                            "verification_targets": ["canonical source"],
                            "confidence": "high",
                        }
                        for row in rows
                    ],
                },
            )
        return {
            "root": root,
            "package_path": package_path,
            "results_dir": results_dir,
            "issue_id": issue_id,
        }

    def test_expansion_provenance_corruption_blocked_before_drafting(self) -> None:
        """Corrupt expansions must fail the shared resolver authority.

        Acceptance runs the same ``resolve_effective_discovery_basis`` that the
        Drafting loader consumes as its single source of truth (the resolver
        itself is covered thoroughly by the Screening expansion-authority
        tests); a corrupt expansion therefore can never become Drafting input.
        """
        helper = evidence_tests.SurveyEvidenceV2Tests(
            methodName="test_evidence_package_is_exact_and_preserves_task_bytes"
        )
        helper.setUp()
        source_a = helper.source("https://example.invalid/root-a")

        with self.subTest(case="parent outside accepted roots"):
            orphan = self._record(
                "SP001", "child-orphan", "REFERENCE_EXPANSION", source_a,
                parent_refs=["missing-root"], research_pass=1,
            )
            prepared = self._screening_prepare_for_corrupt_children([orphan])
            with self.assertRaisesRegex(ValueError, "outside accepted root"):
                screening.accept_results(
                    prepared["root"],
                    prepared["package_path"],
                    prepared["results_dir"],
                    prepared["root"] / "sources" / prepared["issue_id"]
                    / "screening" / "v2" / "runs",
                    IMPLEMENTATION_SHA,
                )

        with self.subTest(case="silent root omission"):
            partial = self._record(
                "SP001", "child-partial", "REFERENCE_EXPANSION", source_a,
                parent_refs=["root-a"], research_pass=1,
            )
            prepared = self._screening_prepare_for_corrupt_children([partial])
            with self.assertRaisesRegex(ValueError, "silently omitted"):
                screening.accept_results(
                    prepared["root"],
                    prepared["package_path"],
                    prepared["results_dir"],
                    prepared["root"] / "sources" / prepared["issue_id"]
                    / "screening" / "v2" / "runs",
                    IMPLEMENTATION_SHA,
                )


if __name__ == "__main__":
    unittest.main()
