from __future__ import annotations

from pathlib import Path

root = Path('.').resolve()

# Generic error wording is used by semantic and visual review evidence.
fidelity_path = root / 'scripts/survey_reader_fidelity_v2.py'
fidelity = fidelity_path.read_text(encoding='utf-8')
old_error = 'raise ValueError(f"{label} must bind exact semantic-review evidence; missing={missing}")'
new_error = 'raise ValueError(f"{label} must bind exact review evidence; missing={missing}")'
assert old_error in fidelity
fidelity = fidelity.replace(old_error, new_error, 1)
fidelity_path.write_text(fidelity, encoding='utf-8')

# Human-Gate round-trip fixture creates LONGFORM publication candidates too; it
# must satisfy the same mixed-layout visual review contract as production.
test_path = root / 'tests/test_survey_human_gate_v2.py'
test = test_path.read_text(encoding='utf-8')
needle = '''            if kind == "SEMANTIC_EDITORIAL" and check_id == "FINAL_SYNTHESIS_QUALITY":\n                locations.extend(["package:PKG-1", "reader-role:final-synthesis", final_block])\n            rows.append(\n'''
replacement = '''            if kind == "SEMANTIC_EDITORIAL" and check_id == "FINAL_SYNTHESIS_QUALITY":\n                locations.extend(["package:PKG-1", "reader-role:final-synthesis", final_block])\n            if kind == "VISUAL" and check_id == "LONGFORM_MIXED_LAYOUT":\n                locations.extend(\n                    [\n                        "reader-layout:balanced-two-column-narrative",\n                        "reader-layout:wide-surfaces-full-width",\n                        "reader-layout:references-one-column",\n                    ]\n                )\n            rows.append(\n'''
assert needle in test
test = test.replace(needle, replacement, 1)
test_path.write_text(test, encoding='utf-8')

worklog_path = root / 'docs/checkpoints/core-v2-longform-mixed-layout-review-400-worklog.md'
worklog = worklog_path.read_text(encoding='utf-8')
append = '''\n## Diagnostic regression history\n\n- The first temporary targeted run failed before publication tests because the temporary transport had not installed `config/survey-production-v2-requirements.txt`; `pypdf` was missing. The transport was corrected rather than weakening the production parser.\n- The corrected targeted run passed `test_survey_reader_fidelity_v2` and `test_survey_publication_v2`, proving the new direct mixed-layout negative regression and publication-chain fixture.\n- Diagnostic full Pipeline run #3510 (`33171970760`) then ran 722 tests and found 12 errors, all from the shared Human-Gate LONGFORM fixture omitting the newly required mixed-layout evidence. No production implementation failure was observed. The shared fixture is updated in this candidate so Architecture/Publication round-trip tests exercise the new visual contract instead of bypassing it.\n\nThe diagnostic heads/runs above are not final audit evidence because this fixture repair mutates the candidate tree.\n'''
assert '## Diagnostic regression history' not in worklog
worklog_path.write_text(worklog.rstrip() + '\n' + append, encoding='utf-8')
