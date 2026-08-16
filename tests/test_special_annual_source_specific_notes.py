from __future__ import annotations

import re

from scripts import revise_special_annual_source_specific_notes as annual
from scripts import revise_special_annual_source_specific_notes_v2 as annual_v2
from scripts import revise_special_half_year_review_repairs_v32 as event_hardening


def _labels(text: str) -> set[str]:
    return {
        label
        for label, pattern in annual._ANNUAL_SIGNAL_PATTERNS
        if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    }


def test_2023_method_vocabulary_covers_issue_139_regressions() -> None:
    qlora = (
        "QLoRA backpropagates through a frozen 4-bit quantized model into LoRA adapters. "
        "QLoRA introduces 4-bit NormalFloat (NF4), double quantization, and paged optimizers."
    )
    assert {"4-bit NormalFloat (NF4)", "double quantization", "paged optimizers"} <= _labels(qlora)

    flash = (
        "FlashAttention-2 improves work partitioning by parallelizing attention across thread blocks "
        "and distributing work between warps to reduce shared-memory communication."
    )
    assert {
        "attention work partitioning",
        "thread-block attention parallelism",
        "warp-level work distribution",
    } <= _labels(flash)

    vllm = (
        "vLLM introduces PagedAttention. PagedAttention applies ideas from virtual memory and paging "
        "to the KV cache so logical blocks can map to non-contiguous physical blocks."
    )
    assert {"PagedAttention / paged KV-cache", "virtual-memory-style KV-cache paging"} <= _labels(vllm)


def test_reasoning_and_sequence_model_details_are_concrete() -> None:
    tot = (
        "Tree of Thoughts enables exploration over thoughts, lets the model look ahead, and uses "
        "backtracking when necessary."
    )
    assert {"Tree-of-Thought search", "multi-path reasoning with lookahead/backtracking"} <= _labels(tot)

    mamba = (
        "Mamba uses selective state spaces: SSM parameters are functions of the input and the model "
        "uses a hardware-aware parallel algorithm in recurrent mode."
    )
    assert {
        "selective state-space model",
        "input-dependent SSM parameters",
        "hardware-aware recurrent parallel algorithm",
    } <= _labels(mamba)


def test_long_unanchored_living_html_fails_closed() -> None:
    summary = "Current navigation and unrelated product chrome. " * 500
    window = event_hardening._safe_event_window(summary, [("2023-06-20", "release")], "vLLM")
    assert window == ""


def test_generic_fallback_detector_rejects_v04_regression_phrasing() -> None:
    assert annual._GENERIC_RE.search(
        "一次資料で「vLLM / PagedAttention」の2023年における公開・リリースの経緯を確認できる。"
    )
    assert annual._GENERIC_RE.search(
        "能力や性能に関する評価は、提供元・プロジェクト側の主張として扱う。"
    )
    assert annual._GENERIC_RE.search(
        "一次資料で確認できる範囲の事実を記録しており、独立再現ではない。"
    )


def test_legacy_annual_manifest_gets_reader_flags_only_in_copy() -> None:
    original = {
        "articles": [
            {"package_id": "runtime", "evidence_record_count": 4, "technical_notes_path": "technical-notes/40.tex"},
            {"package_id": "chronology", "evidence_record_count": 0, "technical_notes_path": "technical-notes/80.tex"},
        ]
    }
    compatible, visible = annual_v2._reader_flagged_manifest(original)
    assert visible == 1
    assert compatible["articles"][0]["technical_notes_reader_facing"] is True
    assert compatible["articles"][1]["technical_notes_reader_facing"] is False
    assert "technical_notes_reader_facing" not in original["articles"][0]
    assert annual_v2._COMPAT_CONTRACT == "EVIDENCE_BACKED_READER_FACING_FLAGS_IN_MEMORY_V2"
