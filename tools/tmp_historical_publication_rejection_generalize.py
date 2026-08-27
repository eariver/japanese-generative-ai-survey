from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: exact replacement count {count} != 1 for {old[:120]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


replace_once(
    "scripts/survey_human_gate_v2.py",
    '''        else:\n            candidate = schema_gate.load_and_validate_json(\n                candidate_path,\n                repo_root / publication.CANDIDATE_SCHEMA,\n                label="Publication Candidate historical review surface",\n            )\n            if candidate.get("issue_id") != state["issue_id"]:\n                raise HumanGateError("Publication Candidate historical review issue identity mismatch")\n            if candidate.get("publication_profile") != profile.get("publication_profile"):\n                raise HumanGateError("Publication Candidate historical review profile identity mismatch")\n''',
    '''        else:\n            # REQUEST_CHANGES records the exact historical review surface. A\n            # newer Candidate schema or substantive validator may be the reason\n            # the Human is rejecting these bytes, so rejection must not require\n            # the historical artifact to satisfy current acceptance contracts.\n            candidate = core.load_json(candidate_path)\n            if candidate.get("issue_id") != state["issue_id"]:\n                raise HumanGateError("Publication Candidate historical review issue identity mismatch")\n            if candidate.get("publication_profile") != profile.get("publication_profile"):\n                raise HumanGateError("Publication Candidate historical review profile identity mismatch")\n''',
)

replace_once(
    "tests/test_survey_human_gate_v2.py",
    '''        original_validate_candidate = publication.validate_candidate\n\n        def reject_under_current_validator(*args, **kwargs):\n            raise ValueError("current validator rejects reviewed historical candidate")\n\n        publication.validate_candidate = reject_under_current_validator\n        try:\n''',
    '''        original_validate_candidate = publication.validate_candidate\n        original_schema_loader = human_gate.schema_gate.load_and_validate_json\n\n        def reject_under_current_validator(*args, **kwargs):\n            raise ValueError("current validator rejects reviewed historical candidate")\n\n        def reject_under_current_candidate_schema(path, schema_path, *args, **kwargs):\n            if Path(path).resolve() == candidate["candidate"].resolve():\n                raise ValueError("current schema rejects reviewed historical candidate")\n            return original_schema_loader(path, schema_path, *args, **kwargs)\n\n        publication.validate_candidate = reject_under_current_validator\n        human_gate.schema_gate.load_and_validate_json = reject_under_current_candidate_schema\n        try:\n''',
)

replace_once(
    "tests/test_survey_human_gate_v2.py",
    '''        finally:\n            publication.validate_candidate = original_validate_candidate\n\n        self.assertEqual(state["lifecycle_state"], "DRAFT_COMPLETE")\n''',
    '''        finally:\n            publication.validate_candidate = original_validate_candidate\n            human_gate.schema_gate.load_and_validate_json = original_schema_loader\n\n        self.assertEqual(state["lifecycle_state"], "DRAFT_COMPLETE")\n''',
)

replace_once(
    "docs/checkpoints/core-v2-historical-publication-rejection-worklog.md",
    '''- `REQUEST_CHANGES` uses `False` so an exact historical candidate can be rejected after validator evolution.\n- The rejection path still validates the Publication Candidate against the current envelope schema, requires exact issue/profile identity, requires a durable PDF authority, verifies exact PDF SHA-256, and then relies on the existing reviewed-commit durability check to prove exact reviewed State/Candidate/PDF bytes are committed and reachable from the canonical work branch.\n''',
    '''- `REQUEST_CHANGES` uses `False` so an exact historical candidate can be rejected after validator or Candidate-schema evolution.\n- The rejection path requires a parseable JSON object, exact issue/profile identity, a durable PDF authority, and exact PDF SHA-256, then relies on the existing reviewed-commit durability check to prove exact reviewed State/Candidate/PDF bytes are committed and reachable from the canonical work branch. It deliberately does not require current Candidate schema or substantive-validation success because either may be the reason the historical bytes are being rejected.\n''',
)

replace_once(
    "docs/checkpoints/core-v2-historical-publication-rejection-worklog.md",
    '''A Human Gate round-trip regression test now simulates a historical Publication Candidate that the current `publication.validate_candidate()` rejects.\n''',
    '''A Human Gate round-trip regression test now simulates a historical Publication Candidate that both the current `publication.validate_candidate()` path and the current Candidate schema would reject.\n''',
)
