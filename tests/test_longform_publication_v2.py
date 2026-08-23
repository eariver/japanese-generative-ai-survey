from scripts import survey_longform_publication_v2 as longform


def test_preflight_rejects_one_column_and_metadata_leak():
    tex = "\\section{A}\n\\begin{technicalnote}[x]x\\end{technicalnote}\nCore v2 Evidence: VERIFIED"
    result = longform.preflight_tex(tex, "", 1)
    assert result["status"] == "FAIL"
    assert any("two-column" in finding for finding in result["findings"])
    assert any("production metadata" in finding for finding in result["findings"])


def test_preflight_accepts_balanced_mixed_layout_surface():
    tex = (
        "Theme at a glance\nCROSS-FAMILY SYNTHESIS\n"
        "\\begin{multicols}{2}a\\end{multicols}\n"
        "\\begin{multicols}{2}summary\\end{multicols}\n"
        "\\begin{technicalnote}[x]x\\end{technicalnote}\n"
        "\\clearpage\n\\clearpage"
    )
    result = longform.preflight_tex(tex, "", 1)
    assert result["status"] == "PASS", result


def test_reader_text_rejects_internal_verify_obligation():
    try:
        longform._reader_text("Verify the baseline before publication", "test")
    except ValueError as exc:
        assert "verification obligation" in str(exc)
    else:
        raise AssertionError("internal Verify obligation must be rejected")
