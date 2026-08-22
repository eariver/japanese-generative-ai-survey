#!/usr/bin/env python3
from pathlib import Path

p = Path('.github/workflows/survey-production-v2-ci.yml')
text = p.read_text(encoding='utf-8')

def rep(old, new, count=1):
    global text
    actual = text.count(old)
    if actual != count:
        raise SystemExit(f'replacement count {actual} != {count}: {old!r}')
    text = text.replace(old, new)

rep('      - "schemas/stage-validation-attestation-v2.schema.json"\n', '      - "schemas/stage-validation-attestation-v2.schema.json"\n      - "schemas/stage-handoff-v2.schema.json"\n', 2)
rep('          scripts/survey_orchestrator_v2.py\n          scripts/survey_findings_v2.py\n', '          scripts/survey_orchestrator_v2.py\n          scripts/survey_handlers_v2.py\n          scripts/survey_handoff_v2.py\n          scripts/survey_findings_v2.py\n')
rep('          tests.test_survey_orchestrator_provenance_v2\n          tests.test_survey_findings_v2\n', '          tests.test_survey_orchestrator_provenance_v2\n          tests.test_survey_handoff_v2\n          tests.test_survey_findings_v2\n')
rep("              Path('schemas/stage-validation-attestation-v2.schema.json'),\n", "              Path('schemas/stage-validation-attestation-v2.schema.json'),\n              Path('schemas/stage-handoff-v2.schema.json'),\n")
p.write_text(text, encoding='utf-8')
