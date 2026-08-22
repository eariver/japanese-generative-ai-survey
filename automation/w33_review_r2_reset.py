#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core

ROOT = Path('.').resolve()
SRC = ROOT / 'sources/2026-W33'
STATE = SRC / 'production-state.json'
WORKLOG = ROOT / 'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'
REV = SRC / 'orchestration/v2/review-revisions/architecture-review-r1-rejected.json'

DOWNSTREAM = [
    SRC / 'orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json',
    SRC / 'orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json',
    SRC / 'orchestration/v2/checkpoints/SELECTION_COMPLETE.json',
    SRC / 'materiality-ledger-v2.json',
    SRC / 'profile-completeness-v2.json',
    SRC / 'candidate-matrix-v2.json',
    SRC / 'candidate-selection-v2.json',
    SRC / 'architecture-v2.json',
    SRC / 'architecture-review-summary-v2.json',
    SRC / 'architecture-review-attention-v2.json',
]

state = core.load_json(STATE)
if state['issue_id'] != '2026-W33' or state['lifecycle_state'] != 'ARCHITECTURE_ESTABLISHED':
    raise SystemExit('expected pending W33 ARCHITECTURE_ESTABLISHED state')
if state['human_gates']['architecture_review'] != 'pending':
    raise SystemExit('Architecture Review must still be pending')

REV.parent.mkdir(parents=True, exist_ok=True)
core.write_json(REV, {
    'schema_version': '1.0',
    'issue_id': '2026-W33',
    'review_round': 'r1',
    'decision': 'REVISION_REQUESTED',
    'requested_changes': [
        'Preserve and publish a recurring weekly Grok/X community-movement section even though X is not technical fact authority.',
        'Do not equate three feature packages with the complete set of weekly topics; route CONTEXT items into recurring roundup/watch sections.',
        'Add a final weekly synthesis/summary requirement after the body sections.',
    ],
    'audit_branch': 'backup/2026-W33-v2-architecture-r1-rejected',
    'revision_restart_stage': 'CANDIDATES_NORMALIZED',
    'notes': 'Fresh Source Intake, Discovery and Screening remain authoritative. Evidence and all downstream editorial artifacts are regenerated for r2.',
})

# Logical review revision: preserve accepted fresh Discovery/Screening, invalidate only
# Evidence and downstream checkpoints. r1 is preserved on the audit branch above.
state['lifecycle_state'] = 'CANDIDATES_NORMALIZED'
state['human_gates']['architecture_review'] = 'pending'
state['human_gate_provenance']['architecture_review'] = None
for name in ('evidence','materiality','completeness','selection','architecture','draft','validation','publication_preview','freeze','release'):
    state['machine_checkpoints'][name] = 'pending'
    state['checkpoint_provenance'][name] = None
state['history'] = [row for row in state['history'] if row['to'] in {'ISSUE_INITIALIZED','DISCOVERY_COLLECTED','CANDIDATES_NORMALIZED'}]
state = core.refresh_state_control(state, core.load_json(ROOT / core.DEFAULT_CONFIG))
core.write_json(STATE, state)

for path in DOWNSTREAM:
    if path.exists():
        path.unlink()

cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
errors = agent.validate_agent_state(ROOT, cfg, core.load_json(STATE))
if errors:
    raise SystemExit('review-revision reset state invalid: ' + '; '.join(errors))

with WORKLOG.open('a', encoding='utf-8') as fh:
    fh.write('''\n\n## Architecture Review r1 — revision requested\n\nHuman Review did not approve the first Architecture. The review identified a Weekly editorial-coverage defect rather than a Source Intake shortage.\n\n- Fresh Grok/X Raw explicitly reported abundant community signal; r1 compressed it into one generic CONTEXT claim and then HOLD, losing the required weekly community-movement section.\n- r1 selected seven MATERIAL candidates but left thirteen CONTEXT candidates out of the issue, making the three feature packages appear to be the whole week.\n- The revised issue must retain the three feature themes while adding recurring X Community Pulse, Research Watch, OSS/GitHub Watch / roundup coverage, and a final weekly synthesis/summary.\n- X remains SOCIAL_OBSERVATION only; no technical/model/benchmark claim is promoted without primary Evidence.\n- The complete r1 state and artifacts are preserved at `backup/2026-W33-v2-architecture-r1-rejected`.\n- Canonical lifecycle was logically returned to `CANDIDATES_NORMALIZED` for review revision. Fresh Source Intake, Discovery, and Screening remain authoritative; Evidence and downstream artifacts are regenerated as r2.\n''')

print('W33 review revision reset validated: CANDIDATES_NORMALIZED')
