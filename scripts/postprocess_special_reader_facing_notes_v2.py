#!/usr/bin/env python3
"""Reader-facing Special Technical Notes entry point with current artifact taxonomy.

Keep compatibility fixes that must be applied before importing the legacy reader-facing
wrapper here so both translation and leak detection see the same reader vocabulary.
"""
from __future__ import annotations

from scripts import postprocess_special_reader_facing_notes_core as core

# BENCHMARK is a valid Evidence artifact type used by retrospective issues.  It must
# never surface as a raw machine taxonomy label in reader-facing Technical Notes.
core.TYPE_LABELS.setdefault("BENCHMARK", "評価ベンチマーク")

from scripts import postprocess_special_reader_facing_notes as compat  # noqa: E402

translate_machine_labels = compat.translate_machine_labels
reader_taxonomy_findings = compat.reader_taxonomy_findings


def main() -> int:
    return compat.main()


if __name__ == "__main__":
    raise SystemExit(main())
