from __future__ import annotations

import json
from pathlib import Path

root = Path('.').resolve()

# 1. Publication review contract: every LONGFORM_SPECIAL visual review must
# explicitly assess the mixed-layout house style.
config_path = root / 'config/publication-review-v2.json'
config = json.loads(config_path.read_text(encoding='utf-8'))
visual = config['publication_profiles']['LONGFORM_SPECIAL']['visual']
assert visual == [], visual
visual.append('LONGFORM_MIXED_LAYOUT')
config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# 2. Require explicit evidence that the visual reviewer actually checked the
# three stable mixed-layout surfaces. This remains an agent visual judgment;
# deterministic Core only requires that the judgment was explicitly made.
fidelity_path = root / 'scripts/survey_reader_fidelity_v2.py'
fidelity = fidelity_path.read_text(encoding='utf-8')
fidelity = fidelity.replace(
    'raise ValueError(f"semantic review requires exactly one {check_id} check")',
    'raise ValueError(f"publication review requires exactly one {check_id} check")',
)
old = '''def validate_review_depth(\n    profile: dict[str, Any],\n    architecture: dict[str, Any],\n    manuscript: dict[str, Any],\n    page_count: int,\n    checks: list[dict[str, Any]],\n    review_kind: str,\n) -> None:\n    """Require explicit package/block-level semantic review for LONGFORM_SPECIAL."""\n    if (\n        review_kind != "SEMANTIC_EDITORIAL"\n        or profile.get("publication_profile") != "LONGFORM_SPECIAL"\n    ):\n        return\n\n    package_ids = [\n'''
new = '''def validate_review_depth(\n    profile: dict[str, Any],\n    architecture: dict[str, Any],\n    manuscript: dict[str, Any],\n    page_count: int,\n    checks: list[dict[str, Any]],\n    review_kind: str,\n) -> None:\n    """Require explicit LONGFORM semantic depth and visual-layout review."""\n    if profile.get("publication_profile") != "LONGFORM_SPECIAL":\n        return\n\n    if review_kind == "VISUAL":\n        mixed_layout = _check_row(checks, "LONGFORM_MIXED_LAYOUT")\n        _require_evidence(\n            mixed_layout,\n            {\n                "reader-layout:balanced-two-column-narrative",\n                "reader-layout:wide-surfaces-full-width",\n                "reader-layout:references-one-column",\n            },\n            "LONGFORM_MIXED_LAYOUT",\n        )\n        return\n\n    if review_kind != "SEMANTIC_EDITORIAL":\n        return\n\n    package_ids = [\n'''
assert old in fidelity
fidelity = fidelity.replace(old, new, 1)
fidelity_path.write_text(fidelity, encoding='utf-8')

# 3. Direct regression: an exact-PDF visual review cannot pass LONGFORM_SPECIAL
# without explicitly recording all three mixed-layout surfaces.
test_path = root / 'tests/test_survey_reader_fidelity_v2.py'
test = test_path.read_text(encoding='utf-8')
needle = '''    def test_weekly_profile_is_not_subject_to_longform_traceability(self) -> None:\n'''
insert = '''    def test_longform_visual_review_requires_explicit_mixed_layout_evidence(self) -> None:\n        profile = {"publication_profile": "LONGFORM_SPECIAL"}\n        checks = [\n            {\n                "check_id": "LONGFORM_MIXED_LAYOUT",\n                "status": "PASS",\n                "detail": "The exact PDF was reviewed against the Special mixed-layout policy.",\n                "evidence_locations": [\n                    "reader-layout:balanced-two-column-narrative",\n                    "reader-layout:wide-surfaces-full-width",\n                    "reader-layout:references-one-column",\n                ],\n            }\n        ]\n        fidelity.validate_review_depth(\n            profile,\n            self._architecture(target_pages=18),\n            self._manuscript(),\n            13,\n            checks,\n            "VISUAL",\n        )\n\n        checks[0]["evidence_locations"].remove("reader-layout:balanced-two-column-narrative")\n        with self.assertRaisesRegex(ValueError, "balanced-two-column-narrative"):\n            fidelity.validate_review_depth(\n                profile,\n                self._architecture(target_pages=18),\n                self._manuscript(),\n                13,\n                checks,\n                "VISUAL",\n            )\n\n'''
assert needle in test
test = test.replace(needle, insert + needle, 1)
test_path.write_text(test, encoding='utf-8')

# 4. Existing publication-chain fixture must provide the newly required visual
# evidence so the full candidate/Human-Gate regression remains meaningful.
pub_test_path = root / 'tests/test_survey_publication_v2.py'
pub_test = pub_test_path.read_text(encoding='utf-8')
needle = '''            if profile["publication_profile"] == "LONGFORM_SPECIAL" and kind == "SEMANTIC_EDITORIAL":\n                if check_id in {"ARCHITECTURE_CONTENT_FIDELITY", "LONGFORM_TECHNICAL_DEPTH"}:\n                    evidence_locations.extend(sorted({"package:PKG-1"} | exact_blocks))\n                if check_id == "FINAL_SYNTHESIS_QUALITY":\n                    evidence_locations.extend(\n                        ["package:PKG-1", "reader-role:final-synthesis", "Section 1 — Final synthesis"]\n                    )\n'''
replacement = needle + '''            if (\n                profile["publication_profile"] == "LONGFORM_SPECIAL"\n                and kind == "VISUAL"\n                and check_id == "LONGFORM_MIXED_LAYOUT"\n            ):\n                evidence_locations.extend(\n                    [\n                        "reader-layout:balanced-two-column-narrative",\n                        "reader-layout:wide-surfaces-full-width",\n                        "reader-layout:references-one-column",\n                    ]\n                )\n'''
assert needle in pub_test
pub_test = pub_test.replace(needle, replacement, 1)
pub_test_path.write_text(pub_test, encoding='utf-8')

# 5. Worklog is candidate-tree authority, so it is written before final audit.
worklog = root / 'docs/checkpoints/core-v2-longform-mixed-layout-review-400-worklog.md'
worklog.write_text('''# Core v2 LONGFORM mixed-layout review hardening — Issue #400\n\n## Trigger\n\nHuman Publication Preview re-review of SP001 regenerated r2 exact PDF (13 pages, SHA-256 `590a53e11934ae25176050e5105b59a2bb09eda4b045e9b211b486e5be90ba2b`) found that ordinary narrative had regressed to full-width one-column even though `docs/special-layout-policy.md` requires mixed layout for normal Specials. The exact-PDF visual review had passed because the LONGFORM_SPECIAL review contract contained no profile-specific visual check.\n\n## Scope\n\n- add `LONGFORM_MIXED_LAYOUT` to the LONGFORM_SPECIAL visual review family;\n- require explicit visual evidence for balanced two-column normal narrative, full-width wide/synthesis/Technical-Notes surfaces, and one-column References;\n- keep layout assessment ChatGPT-owned rather than inferring visual quality from TeX tokens or page count;\n- add direct negative regression and update existing publication-chain fixtures;\n- no workflow, schema, lifecycle, Human Gate, edition-local, or renderer change in this maintenance candidate.\n\n## Intended invariant\n\nAn exact-PDF visual review for `LONGFORM_SPECIAL` cannot be recorded as valid unless it explicitly states that the reviewer checked all three stable mixed-layout surfaces. Weekly and other publication profiles remain unaffected. Architecture-specific exceptions remain Human/editorial concerns; this change does not impose a deterministic TeX implementation such as global `twocolumn` or `multicols`.\n\n## Human Gate\n\nThis shared-Core maintenance must complete exact-head CI and the canonical seven-point final audit before Human maintenance review. It must not be merged without explicit Human approval. SP001 remains paused after canonical Publication Preview r2 `REQUEST_CHANGES` rollback until this Core maintenance is approved and merged.\n''', encoding='utf-8')
