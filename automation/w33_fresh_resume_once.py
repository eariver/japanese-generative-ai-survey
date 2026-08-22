#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_agent_control_v2 as agent
from scripts import survey_x_intake_v2 as xintake

ROOT = Path('.').resolve()
ISSUE = '2026-W33'
SOURCE = ROOT / 'sources' / ISSUE
RAW = SOURCE / 'external/x/weekly-x-2026-W33-fresh-r1/raw/grok-x-result.md'
MANIFEST = SOURCE / 'external/x/x-source-intake-v2.json'
STATE = SOURCE / 'production-state.json'
SEED = SOURCE / 'source-intake-v2/fresh-non-x-screening-seed/screening-index.jsonl'
AUDIT = SOURCE / 'source-intake-v2/fresh-candidate-audit.json'
WORKLOG = ROOT / 'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'
EXPECTED_RAW_SHA = '11cc3fbb64aa6f7f467834e81022a0338fbb45d46e50d20b8d4a36ff5c81f930'

LANES = {
    'A': ['language model','foundation model','reasoning','llm','transformer','mixture of experts','moe'],
    'B': ['agent','coding','code generation','computer use','tool use','tool-call','swe','terminal'],
    'C': ['multimodal','vision-language','vlm','vision language','image understanding','video understanding'],
    'D': ['image generation','text-to-image','image editing','diffusion','flow matching','image synthesis'],
    'E': ['video generation','text-to-video','image-to-video','video editing','video synthesis','t2v','i2v'],
    'F': ['speech','audio','music generation','text-to-speech','tts','voice','audio generation'],
    'G': ['open weight','open-weight','quantization','quantized','gguf','local inference','mlx','llama.cpp','consumer gpu'],
    'H': ['inference','serving','throughput','latency','vllm','sglang','flashinfer','cuda','kernel','speculative decoding'],
    'I': ['memory','retrieval','rag','multi-agent','multi agent','context engineering','long context'],
    'J': ['benchmark','evaluation','eval','leaderboard','judge model'],
    'K': ['safety','security','jailbreak','cyber','alignment','red team','vulnerability'],
    'L': ['world model','robotics','3d generation','simulation','emerging'],
}

SOURCE_WEIGHT = {
    'official-feed-item': 8,
    'github-release': 7,
    'official-index-snapshot': 3,
    'paper': 1,
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def lane_hits(text: str) -> dict[str, int]:
    low = text.lower()
    out: dict[str, int] = {}
    for lane, terms in LANES.items():
        score = 0
        for term in terms:
            count = low.count(term)
            if count:
                score += min(count, 3) * (3 if ' ' in term else 2)
        if score:
            out[lane] = score
    return out


def load_seed() -> list[dict]:
    rows = []
    with SEED.open(encoding='utf-8') as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def build_audit(rows: list[dict]) -> dict:
    by_lane: dict[str, list[dict]] = {lane: [] for lane in LANES}
    source_counts: dict[str, int] = {}
    all_scored: list[dict] = []
    for row in rows:
        st = row.get('source_type','')
        source_counts[st] = source_counts.get(st, 0) + 1
        text = ' '.join(str(row.get(k) or '') for k in ('title','summary_text'))
        hits = lane_hits(text)
        base = SOURCE_WEIGHT.get(st, 0)
        item = {
            'screening_id': row.get('screening_id'),
            'source_type': st,
            'collector_id': row.get('collector_id'),
            'collector_run_id': row.get('collector_run_id'),
            'observed_at': row.get('observed_at'),
            'published_at': row.get('published_at'),
            'title': row.get('title'),
            'locator': row.get('locator'),
            'raw_paths': row.get('raw_paths'),
            'summary_excerpt': (row.get('summary_text') or '')[:1800],
            'metadata': row.get('metadata') or {},
            'lane_scores': hits,
            'source_weight': base,
            'overall_score': base + sum(hits.values()),
        }
        all_scored.append(item)
        for lane, lane_score in hits.items():
            lane_item = dict(item)
            lane_item['lane_score'] = lane_score + base
            by_lane[lane].append(lane_item)
    for lane in by_lane:
        by_lane[lane].sort(key=lambda x: (-x['lane_score'], -(x['overall_score']), str(x.get('published_at') or ''), str(x.get('screening_id'))))
        by_lane[lane] = by_lane[lane][:25]
    all_scored.sort(key=lambda x: (-x['overall_score'], str(x.get('screening_id'))))
    official_github = [x for x in all_scored if x['source_type'] in {'official-feed-item','github-release'}]
    return {
        'schema_version': '1.0',
        'issue_id': ISSUE,
        'basis': {
            'seed_path': str(SEED.relative_to(ROOT)),
            'seed_sha256': sha256(SEED),
            'record_count': len(rows),
            'legacy_w33_source_intake_used': False,
            'fresh_x_raw_path': str(RAW.relative_to(ROOT)),
            'fresh_x_raw_sha256': sha256(RAW),
        },
        'source_counts': source_counts,
        'lane_policy': LANES,
        'top_by_lane': by_lane,
        'official_and_github_candidates': official_github,
        'top_overall': all_scored[:120],
        'notes': [
            'This is a deterministic review aid, not editorial Screening authority.',
            'Scores are keyword/source-type prioritization only; ChatGPT must semantically inspect candidates and verify primary sources before Evidence.',
            'All records derive from the fresh Core v2 W33 non-X Source Intake run; legacy W33 intake is excluded.',
        ],
    }


def main() -> None:
    if sha256(RAW) != EXPECTED_RAW_SHA or RAW.stat().st_size != 15036:
        raise SystemExit(f'fresh Grok Raw byte mismatch: sha={sha256(RAW)} bytes={RAW.stat().st_size}')
    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    manifest = core.load_json(MANIFEST)
    if manifest.get('status') == 'AWAITING_GROK':
        xintake.record_result(
            ROOT, cfg, MANIFEST, 'weekly-x-2026-W33-fresh-r1', RAW,
            'grok-x-result.md', '2026-08-22T15:59:41+00:00',
            datetime.now(timezone.utc).isoformat(), 'SUCCESS', 'DISCOVERY_RECORDED',
            ['x-weekly-signal-wave'],
            'Fresh Grok/X pass completed the required Weekly coverage scan and returned material community signal. The Raw remains discovery/community-signal only; all technical claims require downstream primary-source verification.',
        )
    xintake.validate_manifest(ROOT, cfg, MANIFEST, require_complete=True)

    state = core.load_json(STATE)
    if state['exception_gate']['status'] == 'required':
        state['exception_gate'] = {'status': 'inactive', 'reason': None}
        state = core.refresh_state_control(state, cfg)
        core.write_json(STATE, state)
    errors = agent.validate_agent_state(ROOT, cfg, core.load_json(STATE))
    if errors:
        raise SystemExit('state validation after Exception Gate clear failed: ' + '; '.join(errors))

    rows = load_seed()
    audit = build_audit(rows)
    core.write_json(AUDIT, audit)

    with WORKLOG.open('a', encoding='utf-8') as fh:
        fh.write('\n## Fresh Grok result import and Exception Gate resolution\n\n')
        fh.write(f'- Imported Drive result as exact repository Raw: `{RAW.relative_to(ROOT)}`.\n')
        fh.write(f'- Raw authority: `{EXPECTED_RAW_SHA}`, 15036 bytes.\n')
        fh.write('- X manifest changed from `AWAITING_GROK` to `COMPLETE`; result status `SUCCESS`.\n')
        fh.write('- X discovery disposition: `DISCOVERY_RECORDED` as `x-weekly-signal-wave`; technical claims remain non-authoritative until primary-source verification.\n')
        fh.write('- Exception Gate cleared after fresh X result import; lifecycle remains `ISSUE_INITIALIZED`, next action `stage:discovery`.\n')
        fh.write(f'- Generated deterministic fresh candidate audit from all {len(rows)} non-X screening-seed records; legacy W33 intake excluded.\n')

    print(json.dumps({
        'raw_sha256': sha256(RAW),
        'raw_bytes': RAW.stat().st_size,
        'manifest_status': core.load_json(MANIFEST)['status'],
        'state': core.load_json(STATE),
        'audit_path': str(AUDIT.relative_to(ROOT)),
        'audit_record_count': len(rows),
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
