from scripts import revise_special_half_year_review_repairs_v32 as repair


def test_zero_padded_month_date_excludes_current_navigation_chrome() -> None:
    summary = (
        "Products Models Rerank Semantic search ranking Research "
        "Hardware-aware dynamic speculative decoding "
        + ("navigation " * 500)
        + "Apr 04, 2024 Introducing Command R+: A Scalable LLM Built for Business. "
        "Command R+ is a RAG-optimized model designed for enterprise-grade workloads."
    )
    window = repair._safe_event_window(
        summary,
        [("2024-04-04", "DEPLOYMENT_AVAILABILITY")],
        "Command R / Command R+",
    )

    assert "Command R+" in window
    assert "RAG-optimized" in window
    assert "rerank" not in window.lower()
    assert "speculative decoding" not in window.lower()


def test_long_unanchored_html_fails_closed() -> None:
    summary = "Current navigation Rerank speculative decoding " + ("chrome " * 1200)

    assert repair._safe_event_window(
        summary,
        [("2024-04-04", "MODEL_LAUNCH")],
        "Command R / Command R+",
    ) == ""


def test_concise_feed_without_literal_date_keeps_legacy_fallback() -> None:
    summary = "Command R launched with retrieval-augmented generation for enterprise workloads."

    assert repair._safe_event_window(
        summary,
        [("2024-03-11", "MODEL_LAUNCH")],
        "Command R / Command R+",
    ) == summary


def test_date_variants_keep_padded_and_unpadded_month_days() -> None:
    variants = repair._date_variants("2024-04-04")

    assert "Apr 04, 2024" in variants
    assert "Apr 4, 2024" in variants
    assert "April 04, 2024" in variants
    assert "April 4, 2024" in variants
