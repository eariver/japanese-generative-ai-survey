from scripts.revise_special_reader_enum_cleanup import normalize, remaining_machine_enums


def test_reader_event_enum_cleanup_covers_project_and_evaluation_releases() -> None:
    source = (
        r"2026-04-23 (EVALUATION\_RELEASE)\n"
        r"2026-04-27 (PROJECT\_RELEASE)\n"
        r"2026-04-03 (MEDIA\_MODEL\_RELEASE)\n"
    )
    revised, count = normalize(source)
    assert count == 3
    assert "評価公開" in revised
    assert "プロジェクト公開" in revised
    assert "メディアモデル公開" in revised
    assert remaining_machine_enums(revised) == []
