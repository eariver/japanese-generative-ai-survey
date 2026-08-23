import pytest

from scripts import survey_weekly_bibliography_v2 as bib


def test_bibliography_metadata_never_degrades_to_unknown_placeholder():
    record = {
        "title": "Expanding Daybreak as the Cyber Defense Window Narrows",
        "organization": "OpenAI",
        "published_date": "2026-08-10",
        "url": "https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows",
        "status": "VERIFIED",
        "materiality": "MATERIAL",
    }

    rendered = bib._bib_text("w2026w33example", record, "2026-08-14")

    assert "Unknown" not in rendered
    assert "organization = {{OpenAI}}" in rendered
    assert "date = {2026-08-10}" in rendered
    assert "urldate = {2026-08-14}" in rendered
    assert "note = {[V/M]}" in rendered
    assert record["url"] in rendered


def test_unsupported_human_author_is_omitted_not_invented():
    record = {
        "title": "Example Paper",
        "organization": None,
        "published_date": "2026-08-09",
        "url": "http://arxiv.org/abs/2608.00000v1",
        "status": "PARTIAL",
        "materiality": "CONTEXT",
    }

    rendered = bib._bib_text("w2026w33paper", record, "2026-08-14")

    assert "Unknown" not in rendered
    assert "author =" not in rendered
    assert "organization =" not in rendered
    assert "date = {2026-08-09}" in rendered
    assert "note = {[P/C]}" in rendered


def test_evidence_tag_mapping_is_fail_closed_and_self_documented():
    assert bib._evidence_tag("VERIFIED", "MATERIAL") == "V/M"
    assert bib._evidence_tag("PARTIAL", "CONTEXT") == "P/C"
    assert "V=VERIFIED" in bib.EVIDENCE_TAG_LEGEND
    assert "C=CONTEXT" in bib.EVIDENCE_TAG_LEGEND
    with pytest.raises(ValueError, match="unsupported Weekly bibliography evidence tag"):
        bib._evidence_tag("UNKNOWN", "MATERIAL")


def test_source_owner_fallbacks_are_deterministic():
    assert bib._source_organization("https://openai.com/index/example") == "OpenAI"
    assert bib._source_organization("https://github.com/sgl-project/sglang/releases/tag/v1") == "sgl-project"
    assert bib._source_organization("http://arxiv.org/abs/2608.00000v1") == "arXiv"
    assert bib._source_organization("Grok_X_SourseIntake/Weekly/2026-W33/run/result.md") == "Grok/X Source Intake"


def test_publication_date_normalization_accepts_iso_and_rfc_dates():
    assert bib._normalize_date("2026-08-09T11:54:09Z") == "2026-08-09"
    assert bib._normalize_date("Mon, 10 Aug 2026 10:00:00 GMT") == "2026-08-10"
    assert bib._normalize_date(None) is None
