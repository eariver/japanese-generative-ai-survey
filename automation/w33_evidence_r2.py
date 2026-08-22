#!/usr/bin/env python3
from __future__ import annotations

from automation import w33_evidence_once as base

_original_card = base.card_for
_original_prepare = base.ev.prepare_evidence_package

def prepare_evidence_package(*args, **kwargs):
    # The legacy W33 helper creates WORK/results before package preparation.
    # Core v2 correctly requires a completely empty output_dir at prepare time.
    # Remove only that known empty child, prepare the package, then recreate it.
    results = base.RESULTS
    if results.exists():
        if any(results.iterdir()):
            raise ValueError('unexpected non-empty pre-created Evidence results directory')
        results.rmdir()
    path = _original_prepare(*args, **kwargs)
    results.mkdir(parents=True, exist_ok=True)
    return path

def card_for(task, meta, package):
    card = _original_card(task, meta, package)
    src = task['source_records'][0]
    st = src['source_type'].lower()
    if not (st.startswith('x-') or 'grok' in st):
        return card
    eid = 'subject'; sid = 'src'
    observations = [
        "Fresh Grok/X intake observed a dense same-week multi-lab release wave as the center of W33 discussion, including Grok 4.6, Gemini 3.7 Flash, DeepSeek V4-Pro-0813, GLM-5.3, Nemotron 3.5 Lightning, and Muse Glimmer as recurring comparison objects.",
        "Across the observed X candidate pool, agent/coding capability and cost per successful run displaced pure chat benchmarks as the dominant practitioner comparison axis.",
        "Open-weight and local-inference discussion strengthened during W33, including an explicit 'local AI era' narrative and recurring interest in local or edge deployment reports.",
        "Speed of harness and IDE integration became a visible community differentiator, with Cursor, Grok Build, Copilot, Zcode, Responses API, and Codex-oriented integration discussion appearing alongside model releases.",
        "Hands-on practitioner testing appeared within hours of releases; discussion praised speed or coding stability in some cases while also recording mixed speed-versus-capability sentiment and disappointment on selected micro-tasks.",
        "Correction and counter-signal discussion was also present: GLM-5.3 open-weight messaging was distinguished from delayed weight availability, and X-circulated benchmark or vulnerability counts were repeatedly identified as needing primary verification.",
    ]
    card['claims'] = [
        {
            'statement_id': f'claim-{i+1}',
            'text': text,
            'subject_id': eid,
            'subject_role': 'PRIMARY_SUBJECT',
            'evidence_class': 'SOCIAL_OBSERVATION',
            'source_ids': [sid],
            'context': 'W33 X community movement',
        }
        for i, text in enumerate(observations)
    ]
    card['limitations'] = [
        {
            'statement_id': 'lim-1',
            'text': 'X/Grok is discovery/community signal only and is not technical Evidence authority under the Core v2 contract.',
            'subject_id': eid,
            'subject_role': 'PRIMARY_SUBJECT',
            'evidence_class': 'SOCIAL_OBSERVATION',
            'source_ids': [sid],
            'context': 'Evidence boundary',
        },
        {
            'statement_id': 'lim-2',
            'text': 'Named models, integrations, benchmark labels, prices, dates, and performance figures in the community observations identify what was discussed on X; their underlying technical truth requires separately accepted primary Evidence before factual publication.',
            'subject_id': eid,
            'subject_role': 'PRIMARY_SUBJECT',
            'evidence_class': 'SOCIAL_OBSERVATION',
            'source_ids': [sid],
            'context': 'Community-signal boundary',
        },
    ]
    card['verification']['unresolved_questions'] = [
        'Individual technical/release/benchmark/pricing claims require separately accepted primary Discovery sources; Community Pulse may report only that these topics were salient on X unless reconciled elsewhere.'
    ]
    return card

base.ev.prepare_evidence_package = prepare_evidence_package
base.card_for = card_for
base.main()
