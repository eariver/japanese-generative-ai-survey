#!/usr/bin/env python3
from __future__ import annotations

from automation import w33_evidence_once as base

_original = base.card_for

def card_for(task, meta, package):
    card = _original(task, meta, package)
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

base.card_for = card_for
base.main()
