from __future__ import annotations

import re

from scripts import revise_special_annual_source_specific_notes_v3 as annual_v3


def test_toolformer_signals_match_abstract_method_language() -> None:
    text = (
        "Toolformer learns in a self-supervised way how to use external tools via simple APIs, "
        "including which API calls to make and how to incorporate their results."
    )
    labels = {
        name
        for name, pattern in annual_v3._TOOLFORMER_PATTERNS
        if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    }
    assert labels == {
        "self-supervised tool-use learning",
        "model-selected external API calls",
    }
    assert annual_v3._TOOLFORMER_SIGNALS == labels
