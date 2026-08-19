import importlib.util
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "prepare_annual_reader_notes_ja_overrides.py"
spec = importlib.util.spec_from_file_location("prepare_annual_reader_notes_ja_overrides", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


@pytest.mark.parametrize("separator", [" ", "-"])
def test_generic_record_accepts_known_primary_source_orthography(separator: str) -> None:
    source = (
        f"The reviewed primary{separator}source set documents Prefix-Tuning as part of the 2021 "
        "generative-AI technical record. Technical, performance, access, and safety assertions remain "
        "attributed to the originating authors/projects rather than treated as independent reproduction."
    )

    result = module.translate_claim(source, "Prefix-Tuning", "2021")

    assert "Prefix-Tuning" in result
    assert "2021年" in result


@pytest.mark.parametrize("separator", [" ", "-"])
def test_technical_and_lifecycle_accept_known_primary_source_orthography(separator: str) -> None:
    technical = (
        f"The reviewed primary{separator}source set documents Example Model within 2021; "
        "technical and evaluation results remain attributed to the originating authors."
    )
    lifecycle = (
        f"The reviewed primary{separator}source set documents the 2021 release/publication lifecycle of Example Model; "
        "capability and performance claims remain attributed to the originating vendor, project, or authors."
    )

    assert "Example Model" in module.translate_claim(technical, "Example Model", "2021")
    assert "Example Model" in module.translate_claim(lifecycle, "Example Model", "2021")


def test_unknown_wording_remains_fail_closed() -> None:
    source = (
        "The reviewed primary_sources set documents Prefix-Tuning as part of the 2021 generative-AI technical record. "
        "Technical, performance, access, and safety assertions remain attributed to the originating authors/projects "
        "rather than treated as independent reproduction."
    )

    with pytest.raises(ValueError, match="unsupported Annual Technical Notes claim template"):
        module.translate_claim(source, "Prefix-Tuning", "2021")
