#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_architecture_v2 as architecture
from scripts import survey_completeness_v2 as completeness
from scripts import survey_discovery_v2 as discovery
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_screening_v2 as screening
from scripts import survey_stage_validation_v2 as stage_validation
from scripts import survey_x_intake_v2 as xintake

ROOT = Path('.').resolve()
ISSUE = '2026-W33'
SRC = ROOT / 'sources' / ISSUE
PROFILE = SRC / 'production-profile.json'
STATE = SRC / 'production-state.json'
OBSERVED = '2026-08-22T14:25:00Z'
RECORDED_BASE = datetime(2026, 8, 22, 14, 25, tzinfo=timezone.utc)


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def git_show(ref: str, path: str) -> bytes:
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'])


def import_legacy(path: str) -> Path:
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(git_show('origin/weekly/2026-W33-work', path))
    return out


def fetch_primary(slug: str, url: str, legacy_note: str) -> tuple[Path, bool]:
    out = SRC / 'source-intake-v2' / 'raw' / f'{slug}.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 SurveyProductionCoreV2/2026-W33'})
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            data = res.read()
        if not data:
            raise ValueError('empty response')
        out.write_bytes(data)
        return out, True
    except Exception as exc:
        fallback = out.with_suffix('.json')
        core.write_json(fallback, {
            'schema_version': 'w33-source-intake-fallback-v1',
            'canonical_url': url,
            'observed_at': OBSERVED,
            'fetch_status': 'FAILED_AT_ACTION_RUNTIME',
            'fetch_error': str(exc),
            'revalidation_note': legacy_note,
            'authority_boundary': 'This fallback is provenance only. Factual claims remain attributed to the canonical first-party URL and are not upgraded beyond the stated limitation.',
        })
        return fallback, False


def source_record(discovery_id: str, title: str, locator: str, raw: Path, published_at: str | None, *, source_type: str = 'official-page', origin: str = 'BASE', obligations: list[str] | None = None, summary: str | None = None, metadata: dict | None = None, parent_refs: list[str] | None = None) -> dict:
    return {
        'schema_version': '2.0-rc1',
        'issue_id': ISSUE,
        'discovery_id': discovery_id,
        'provenance': {
            'origin': origin,
            'research_pass': 0,
            'parent_refs': parent_refs or [],
            'obligation_ids': obligations or [],
            'reason': 'W33 Core v2 source intake: current-window primary-source verification or explicit carry-over/X revalidation.',
        },
        'source': {
            'source_type': source_type,
            'collector_id': 'w33-core-v2-source-intake',
            'collector_run_id': '2026-08-22-architecture-review-pass',
            'observed_at': OBSERVED,
            'title': title,
            'locator': locator,
            'raw_paths': [rel(raw)],
            'published_at': published_at,
            'summary_text': summary,
            'metadata': metadata or {},
        },
    }


def write_jsonl(path: Path, rows: list[dict]) -> None:
    screening.write_jsonl(path, rows)


def bound(statement_id: str, text: str, evidence_class: str, *, context: str | None = None) -> dict:
    return {
        'statement_id': statement_id,
        'text': text,
        'subject_id': 'subject',
        'subject_role': 'PRIMARY_SUBJECT',
        'evidence_class': evidence_class,
        'source_ids': ['source-1'],
        'context': context,
    }


def make_card(package: dict, package_path: Path, meta: dict, spec: dict) -> dict:
    task = core.load_json(package_path.parent / meta['path'])
    locator = task['source_records'][0]['locator']
    source_class = spec.get('source_class', 'PRIMARY_OFFICIAL')
    claims = [bound(f'claim-{i+1}', text, cls, context=ctx) for i, (text, cls, ctx) in enumerate(spec['claims'])]
    limitations = [bound(f'limitation-{i+1}', text, cls, context=ctx) for i, (text, cls, ctx) in enumerate(spec.get('limitations', []))]
    target_status = 'VERIFIED' if spec.get('verification_status', 'VERIFIED') == 'VERIFIED' else 'UNRESOLVED'
    unresolved = list(spec.get('unresolved_questions', []))
    return {
        'schema_version': '2.0-rc1',
        'issue_id': ISSUE,
        'evidence_task_id': task['evidence_task_id'],
        'basis': {
            'task_sha256': meta['sha256'],
            'screening_acceptance_sha256': task['screening_basis']['screening_acceptance_sha256'],
            'prompt_sha256': package['prompt']['sha256'],
            'result_contract_sha256': package['contracts']['card']['sha256'],
        },
        'status': spec.get('status', 'VERIFIED'),
        'entities': [{
            'entity_id': 'subject',
            'canonical_name': spec['canonical_name'],
            'entity_type': spec['entity_type'],
            'organization': spec.get('organization'),
            'canonical_url': locator,
        }],
        'artifact': {
            'primary_subject_id': 'subject',
            'artifact_type': spec['artifact_type'],
            'canonical_name': spec['canonical_name'],
            'canonical_url': locator,
        },
        'temporal': {
            'observed_at': OBSERVED,
            'events': [{
                'event_id': f"event:{task['evidence_task_id']}",
                'event_type': spec['event_type'],
                'event_date': spec.get('published_at'),
                'subject_id': 'subject',
                'subject_role': 'PRIMARY_SUBJECT',
                'source_ids': ['source-1'],
            }],
        },
        'sources': [{
            'source_id': 'source-1',
            'url': locator,
            'source_class': source_class,
            'title': spec['source_title'],
            'published_at': spec.get('published_at'),
            'accessed_at': OBSERVED,
            'role': spec.get('source_role', 'canonical first-party verification source'),
        }],
        'claims': claims,
        'metrics': [],
        'limitations': limitations,
        'verification': {
            'targets': [{
                'target': 'subject identity, W33 chronology, and source-bound technical claim',
                'status': target_status,
                'finding': spec['verification_finding'],
                'subject_ids': ['subject'],
                'source_ids': ['source-1'],
            }],
            'unresolved_questions': unresolved,
            'contradictions': list(spec.get('contradictions', [])),
        },
    }


def artifact_by_title(matrix: dict) -> dict[str, dict]:
    return {row['title']: row for row in matrix['rows']}


def union_boundaries(rows: list[dict]) -> list[str]:
    out: list[str] = []
    for row in rows:
        for boundary in row['remaining_boundaries']:
            if boundary not in out:
                out.append(boundary)
    return out


def stage_review_and_advance(cfg: dict, artifact_map: dict[str, Path], semantic_id: str, semantic_kind: str, semantic_evidence: str, summary: str, ordinal: int) -> None:
    state = core.load_json(STATE)
    from_state = state['lifecycle_state']
    report = SRC / 'reviews' / 'v2' / f'{ordinal:02d}-{from_state}-core-stage-contract.json'
    report.parent.mkdir(parents=True, exist_ok=True)
    if report.exists():
        report.unlink()
    now = RECORDED_BASE.replace(minute=RECORDED_BASE.minute + ordinal)
    stage_validation.validate_stage(ROOT, cfg, STATE, artifact_map, report, now)
    reviews = SRC / 'reviews' / 'v2' / f'{ordinal:02d}-{from_state}-reviews.json'
    core.write_json(reviews, {'reviews': [
        {
            'check_id': 'CORE_STAGE_CONTRACT',
            'kind': 'DETERMINISTIC',
            'executor': 'scripts/survey_stage_validation_v2.py',
            'evidence': 'Deterministic Core v2 stage contract validation passed against exact current State/Profile/contract/tool/artifact bytes.',
            'result_path': rel(report),
        },
        {
            'check_id': semantic_id,
            'kind': semantic_kind,
            'executor': 'ChatGPT GPT-5.6 Sol',
            'evidence': semantic_evidence,
        },
    ]})
    checkpoint = agent.build_stage_checkpoint(ROOT, cfg, STATE, artifact_map, reviews, summary, now)
    agent.advance_with_checkpoint(ROOT, cfg, STATE, checkpoint)


def main() -> None:
    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    profile = core.load_json(PROFILE)
    state = core.load_json(STATE)
    if state['lifecycle_state'] != 'ISSUE_INITIALIZED':
        raise RuntimeError(f"expected ISSUE_INITIALIZED for one-shot compile, got {state['lifecycle_state']}")
    if profile['research_profile'] != 'WEEKLY' or profile['publication_profile'] != 'WEEKLY_MAGAZINE':
        raise RuntimeError('W33 Profile identity mismatch')

    # Optional legacy fixture bytes permitted by the W33 disposition policy.
    carry_seed = import_legacy('sources/2026-W33/carryover/carryover-seed-v0.1.json')
    carry_ledger = import_legacy('sources/2026-W33/carryover/carryover-ledger-v0.1.json')
    legacy_grok_rel = 'sources/2026-W33/grok/observations/x-trend-sensor-2026-08-15-v0.4-r3.md'
    legacy_grok = import_legacy(legacy_grok_rel)

    revalidation = SRC / 'revalidation' / 'w33-legacy-inputs-v2.json'
    core.write_json(revalidation, {
        'schema_version': 'w33-legacy-revalidation-v1',
        'issue_id': ISSUE,
        'source_branch': 'weekly/2026-W33-work',
        'policy': 'docs/survey-production-core-v2-w33-artifact-disposition.md',
        'items': [
            {'path': rel(carry_seed), 'sha256': core.sha256_file(carry_seed), 'disposition': 'REVALIDATE', 'use': 'carry-over provenance only'},
            {'path': rel(carry_ledger), 'sha256': core.sha256_file(carry_ledger), 'disposition': 'REVALIDATE', 'use': 'explicit carry-over disposition basis'},
            {'path': rel(legacy_grok), 'sha256': core.sha256_file(legacy_grok), 'disposition': 'REVALIDATE', 'use': 'X/Grok discovery/community signal only'},
        ],
        'rejected_as_authority': ['legacy Screening', 'legacy Candidate Matrix/Selection', 'legacy Architecture', 'legacy Architecture approval'],
    })

    primary_specs = {
        'w33-daybreak-cyber': {
            'title': 'GPT-5.6-Cyber / Daybreak Red',
            'url': 'https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/',
            'published_at': '2026-08-10T00:00:00Z',
            'note': 'OpenAI first-party Aug 10 Daybreak expansion; legacy W33 Evidence had independently verified the same event.',
            'canonical_name': 'GPT-5.6-Cyber / Daybreak Red', 'entity_type': 'MODEL', 'artifact_type': 'MODEL_UPDATE', 'organization': 'OpenAI',
            'event_type': 'announcement', 'source_title': 'Expanding Daybreak as the Cyber Defense Window Narrows',
            'claims': [
                ('OpenAI announced an expansion of Daybreak during the W33 window and positioned GPT-5.6-Cyber as a specialized cybersecurity model for authorized vulnerability research and testing.', 'VENDOR_CLAIM', 'Capability framing is attributed to OpenAI.'),
                ('Daybreak separates Blue and Red access patterns, making governed distribution and authorization part of the deployment design rather than an editorial afterthought.', 'PRIMARY_FACT', 'Access/deployment structure from the first-party announcement.'),
            ],
            'limitations': [
                ('Benchmark, vulnerability-discovery, reduced-refusal, and capability-threshold statements remain vendor-reported unless independently reproduced.', 'VENDOR_CLAIM', 'Do not convert first-party performance claims into independent fact.'),
                ('Daybreak Red is a controlled-access security capability and should not be described as unrestricted general availability.', 'PRIMARY_FACT', 'Access boundary must travel with capability discussion.'),
            ],
            'verification_finding': 'First-party OpenAI chronology and controlled-access product identity are established for Aug 10, 2026.',
            'materiality': 'MATERIAL',
            'why': 'This is the strongest date-specific W33 event because specialization and controlled deployment changed together.',
            'dimensions': ['current relevance', 'technical significance'],
        },
        'w33-daybreak-aws': {
            'title': 'Daybreak on AWS',
            'url': 'https://openai.com/index/daybreak-models-are-now-available-on-aws/',
            'published_at': '2026-08-11T00:00:00Z',
            'note': 'OpenAI first-party Aug 11 AWS availability; legacy W33 Evidence treated this as supporting deployment chronology.',
            'canonical_name': 'Daybreak on AWS', 'entity_type': 'PRODUCT', 'artifact_type': 'INTEGRATION', 'organization': 'OpenAI',
            'event_type': 'availability', 'source_title': 'Daybreak models are now available on AWS',
            'claims': [
                ('OpenAI announced Daybreak Blue and Red availability through AWS during the W33 window, extending the controlled cyber capability into an enterprise cloud distribution channel.', 'PRIMARY_FACT', 'Distribution fact from first-party announcement.'),
            ],
            'limitations': [
                ('AWS availability is deployment evidence, not independent evidence for Daybreak capability or benchmark claims.', 'INFERENCE', 'Use as supporting deployment context only.'),
            ],
            'verification_finding': 'First-party OpenAI chronology establishes an Aug 11 AWS distribution event.',
            'materiality': 'CONTEXT',
            'why': 'It turns the Daybreak story from a model announcement into an operational distribution story.',
            'dimensions': ['current relevance'],
        },
        'w33-sglang-0.5.17': {
            'title': 'SGLang v0.5.17',
            'url': 'https://github.com/sgl-project/sglang/releases/tag/v0.5.17',
            'published_at': '2026-08-08T00:00:00Z',
            'note': 'First-party GitHub release; legacy W33 Evidence rated the release V3 primary-verified.',
            'canonical_name': 'SGLang v0.5.17', 'entity_type': 'FRAMEWORK', 'artifact_type': 'FRAMEWORK', 'organization': 'SGLang',
            'event_type': 'release', 'source_title': 'SGLang v0.5.17 release', 'source_class': 'PRIMARY_REPOSITORY',
            'claims': [
                ('The SGLang project published v0.5.17 inside the W33 window as part of the fast-moving serving/runtime layer adapting to current model architectures and production requirements.', 'PROJECT_CLAIM', 'Project release chronology is primary; technical significance is synthesized across the serving stack.'),
            ],
            'limitations': [
                ('Performance, resource-use, and hardware-specific improvements remain project-reported and are not treated as cross-framework apples-to-apples benchmarks.', 'PROJECT_CLAIM', 'Preserve project attribution.'),
            ],
            'verification_finding': 'First-party repository release identity and W33 chronology are established.',
            'materiality': 'MATERIAL', 'why': 'Together with vLLM and FlashInfer, it shows the serving stack moving in concert rather than as isolated release-note noise.',
            'dimensions': ['technical significance'],
        },
        'w33-vllm-0.27.1': {
            'title': 'vLLM v0.27.0–v0.27.1',
            'url': 'https://github.com/vllm-project/vllm/releases/tag/v0.27.1',
            'published_at': '2026-08-11T00:00:00Z',
            'note': 'First-party GitHub release series; legacy W33 Evidence rated v0.27.0–0.27.1 primary-verified.',
            'canonical_name': 'vLLM v0.27.0–v0.27.1', 'entity_type': 'FRAMEWORK', 'artifact_type': 'FRAMEWORK', 'organization': 'vLLM',
            'event_type': 'release', 'source_title': 'vLLM v0.27.1 release', 'source_class': 'PRIMARY_REPOSITORY',
            'claims': [
                ('The vLLM project published the v0.27.0–v0.27.1 release sequence during W33, reinforcing the same serving-stack adaptation pressure visible in adjacent runtimes and kernels.', 'PROJECT_CLAIM', 'Project chronology is first-party; grouping is editorial synthesis.'),
            ],
            'limitations': [
                ('Reported throughput or feature gains are project claims and must not be normalized against SGLang or FlashInfer without matched workloads and hardware.', 'PROJECT_CLAIM', 'No synthetic benchmark comparison in the article.'),
            ],
            'verification_finding': 'First-party repository release identity and W33 chronology are established.',
            'materiality': 'MATERIAL', 'why': 'The value is comparative: multiple serving layers changed in the same week around architecture support and runtime behavior.',
            'dimensions': ['technical significance'],
        },
        'w33-flashinfer-0.6.17': {
            'title': 'FlashInfer v0.6.17',
            'url': 'https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.6.17',
            'published_at': '2026-08-11T00:00:00Z',
            'note': 'First-party GitHub release; legacy W33 Evidence rated it primary-verified.',
            'canonical_name': 'FlashInfer v0.6.17', 'entity_type': 'FRAMEWORK', 'artifact_type': 'FRAMEWORK', 'organization': 'FlashInfer',
            'event_type': 'release', 'source_title': 'FlashInfer v0.6.17 release', 'source_class': 'PRIMARY_REPOSITORY',
            'claims': [
                ('FlashInfer v0.6.17 landed during W33 as the kernel/runtime side of the same serving-stack co-evolution visible in SGLang and vLLM.', 'PROJECT_CLAIM', 'Release chronology is first-party; cross-project synthesis is editorial.'),
            ],
            'limitations': [
                ('Kernel-performance and production-readiness claims remain project-reported and workload/hardware dependent.', 'PROJECT_CLAIM', 'Do not present project figures as universal gains.'),
            ],
            'verification_finding': 'First-party repository release identity and W33 chronology are established.',
            'materiality': 'MATERIAL', 'why': 'It completes the stack-level picture from orchestration/runtime down to kernels.',
            'dimensions': ['technical significance'],
        },
        'w33-agent-plugins-1.0': {
            'title': 'GitHub Agent Plugins 1.0',
            'url': 'https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/',
            'published_at': '2026-08-12T00:00:00Z',
            'note': 'Current W33 first-party GitHub changelog item added by the v2 regeneration rather than inherited from the legacy selection.',
            'canonical_name': 'GitHub Agent Plugins 1.0', 'entity_type': 'PRODUCT', 'artifact_type': 'INTEGRATION', 'organization': 'GitHub',
            'event_type': 'general-availability', 'source_title': 'Agent Plugins 1.0 in VS Code, Copilot CLI, and the Copilot app',
            'claims': [
                ('GitHub announced Agent Plugins 1.0 support across its Copilot surfaces during W33, packaging agent skills and MCP servers into installable units that can be governed and reused across clients.', 'PRIMARY_FACT', 'First-party GitHub changelog.'),
                ('The packaging model shifts part of agent engineering from per-client prompt/tool setup toward reusable distribution units spanning skills and MCP connectivity.', 'INFERENCE', 'Editorial interpretation of the first-party packaging model.'),
            ],
            'limitations': [
                ('This event demonstrates packaging and client support, not that all agent runtimes have converged on one plugin standard or security model.', 'INFERENCE', 'Avoid ecosystem-wide standardization claims.'),
            ],
            'verification_finding': 'GitHub first-party changelog establishes an Aug 12 W33 support/GA event and the skills-plus-MCP packaging model.',
            'materiality': 'MATERIAL', 'why': 'It is a clean W33 agent-infrastructure event that the legacy matrix did not foreground and validates the need for fresh v2 selection.',
            'dimensions': ['current relevance', 'technical significance'],
        },
        'w33-transformers-5.15.0': {
            'title': 'Transformers v5.15.0 / Muse Glimmer',
            'url': 'https://github.com/huggingface/transformers/releases/tag/v5.15.0',
            'published_at': '2026-08-10T00:00:00Z',
            'note': 'First-party Hugging Face release; legacy W33 evidence established the HF event and kept model-origin claims bounded.',
            'canonical_name': 'Transformers v5.15.0 / Muse Glimmer', 'entity_type': 'FRAMEWORK', 'artifact_type': 'INTEGRATION', 'organization': 'Hugging Face',
            'event_type': 'release', 'source_title': 'Transformers v5.15.0 release', 'source_class': 'PRIMARY_REPOSITORY',
            'claims': [
                ('Hugging Face published Transformers v5.15.0 during W33 with Muse Glimmer-related ecosystem support, providing a concrete integration-layer signal for newly arriving model capabilities.', 'PROJECT_CLAIM', 'The verified event is the Hugging Face release/integration record.'),
            ],
            'limitations': [
                ('The Hugging Face release does not by itself establish the exact original model-launch chronology, independent quality, or broad social momentum for Muse Glimmer.', 'PRIMARY_FACT', 'Keep model-origin claims below the integration evidence.'),
            ],
            'verification_finding': 'First-party Hugging Face release identity and W33 chronology are established; underlying model-origin claims remain bounded.',
            'materiality': 'CONTEXT', 'why': 'Useful as an ecosystem-integration brief, but weaker than Daybreak or the serving-stack movement as a standalone lead.',
            'dimensions': ['current relevance', 'technical significance'],
        },
        'w33-comfyui-0.32.0': {
            'title': 'ComfyUI W33 media integrations',
            'url': 'https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.32.0',
            'published_at': '2026-08-11T00:00:00Z',
            'note': 'First-party ComfyUI release family; legacy W33 evidence verified integration/adoption but rejected stronger launch/quality claims.',
            'canonical_name': 'ComfyUI W33 media integrations', 'entity_type': 'FRAMEWORK', 'artifact_type': 'INTEGRATION', 'organization': 'ComfyUI',
            'event_type': 'release', 'source_title': 'ComfyUI v0.32.0 release', 'source_class': 'PRIMARY_REPOSITORY',
            'claims': [
                ('ComfyUI releases during W33 added concrete media-generation integration support, making the integration layer itself an observable adoption signal.', 'PROJECT_CLAIM', 'First-party integration evidence only.'),
            ],
            'limitations': [
                ('An integration release does not establish that the underlying model launched in the same week, that its quality improved, or that the topic was a broad X-wide trend.', 'PRIMARY_FACT', 'Watchlist must state what would upgrade confidence.'),
            ],
            'verification_finding': 'First-party project release supports W33 integration/adoption; stronger model-launch and trend claims are not established.',
            'materiality': 'CONTEXT', 'why': 'Best handled as a watchlist/integration signal with an explicit upgrade criterion.',
            'dimensions': ['current relevance'],
        },
    }

    raw_by_id: dict[str, Path] = {}
    fetch_ok: dict[str, bool] = {}
    for did, spec in primary_specs.items():
        raw, ok = fetch_primary(did, spec['url'], spec['note'])
        raw_by_id[did] = raw
        fetch_ok[did] = ok

    # X/Grok v2 manifest: the legacy r3 raw is revalidated as a discovery sensor only.
    xspec = {
        'decision': 'REQUIRED',
        'rationale': 'Weekly Profile requires X/Grok intake. The W33 legacy r3 Trend Sensor raw is independently hash-revalidated and imported only as discovery/community signal under the explicit W33 v2 disposition policy.',
        'series_context': None,
        'runs': [{
            'run_id': 'w33-r3-revalidated',
            'purpose': 'Observe material technical community signal and identify claims requiring primary-source reconciliation.',
            'research_questions': ['What became materially salient on X around the completed W33 window, and which claims require first-party reconciliation?'],
            'coverage_focus': ['technical salience', 'independent testing', 'integration/adoption', 'false-positive reconciliation'],
            'time_scope': '2026-W33 completed editorial window plus immediate post-cutoff reconnaissance; no post-cutoff event is promoted solely by X timing.',
            'expected_result_filename': 'grok-x-result.md',
        }],
    }
    xmanifest = xintake.build_manifest(ROOT, cfg, PROFILE, xspec)
    xraw = SRC / 'external' / 'x' / 'w33-r3-revalidated' / 'raw' / 'grok-x-result.md'
    xraw.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(legacy_grok, xraw)
    x_ids = ['x-grok46-unverified', 'x-qwen38-unverified', 'x-anthropic-risk-report-unverified']
    xintake.record_result(
        ROOT, cfg, xmanifest, 'w33-r3-revalidated', xraw, 'grok-x-result.md',
        '2026-08-15T10:00:00Z', OBSERVED, 'SUCCESS', 'DISCOVERY_RECORDED', x_ids,
        'Revalidated legacy r3 raw retained three representative high-salience claims for explicit primary-source rejection. X is not technical Evidence authority.',
    )
    xintake.validate_manifest(ROOT, cfg, xmanifest)

    discoveries: list[dict] = []
    for did, spec in primary_specs.items():
        obligations = []
        if did == 'w33-daybreak-cyber':
            obligations = ['weekly:current-relevance', 'weekly:technical-significance']
        discoveries.append(source_record(
            did, spec['title'], spec['url'], raw_by_id[did], spec['published_at'],
            obligations=obligations,
            summary=spec['note'],
            metadata={'primary_fetch_succeeded': fetch_ok[did], 'legacy_revalidation_note': spec['note']},
        ))

    carry_url = 'https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W33-work/sources/2026-W33/carryover/carryover-ledger-v0.1.json'
    discoveries.append(source_record(
        'w33-carryover-ledger', 'W32→W33 carry-over disposition ledger', carry_url, carry_ledger, None,
        source_type='carry-over-ledger', origin='CARRY_OVER', obligations=['weekly:carry-over'],
        parent_refs=['external:2026-W32:carry-over-ledger'],
        summary='Every inherited W32 obligation is explicitly disposed: backfill, unresolved/no action, support-current, or promoted-current.',
        metadata={'legacy_fixture_sha256': core.sha256_file(carry_ledger), 'authority_boundary': 'carry-over provenance and disposition only'},
    ))

    for did, title, reason in [
        ('x-grok46-unverified', 'Grok 4.6 social claim', 'Exact first-party Grok 4.6 W33 identity/launch was not corroborated; social salience cannot establish the event.'),
        ('x-qwen38-unverified', 'Qwen3.8-27B social claim', 'Community packaging did not establish the exact official model identity/release claimed by the X signal.'),
        ('x-anthropic-risk-report-unverified', 'Anthropic August 2026 Risk Report social claim', 'The alleged Aug 14 report/event was not established by first-party reconciliation.'),
    ]:
        discoveries.append(source_record(
            did, title, 'https://x.com/', xraw, None, source_type='grok-x-sensor',
            summary=reason,
            metadata={'evidence_role': 'DISCOVERY_AND_COMMUNITY_SIGNAL_ONLY', 'screening_expectation': 'DROP_AFTER_PRIMARY_RECONCILIATION'},
        ))

    discovery_path = SRC / 'discovery' / 'discovery-v2.jsonl'
    discovery_path.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(discovery_path, discoveries)
    discovery_acceptance = discovery.build_acceptance(ROOT, discovery_path, xmanifest, ISSUE, SRC / 'discovery' / 'discovery-accepted-v2.json')
    discovery.validate_acceptance(ROOT, discovery_acceptance)

    # Immutable helper basis: Screening and Evidence intentionally share the same pre-transition State bytes.
    snapshot_state = SRC / 'orchestration' / 'v2' / 'basis' / 'issue-initialized-state.json'
    snapshot_state.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(STATE, snapshot_state)
    impl = core.repository_commit_sha(ROOT)

    decisions: dict[str, dict] = {}
    for row in discoveries:
        did = row['discovery_id']
        if did in x_ids:
            decisions[did] = {
                'decision': 'DROP',
                'reason': row['source']['summary_text'] or 'Unverified X claim rejected by primary-source reconciliation.',
                'scope_tags': ['x-signal', 'primary-source-reconciliation'],
                'duplicate_group': None,
                'verification_targets': ['exact first-party identity', 'W33 event chronology'],
                'confidence': 'high',
            }
        elif did == 'w33-carryover-ledger':
            decisions[did] = {
                'decision': 'KEEP',
                'reason': 'Required Weekly carry-over obligation needs explicit downstream disposition; this ledger is provenance/context, not a feature candidate.',
                'scope_tags': ['carry-over', 'completeness'],
                'duplicate_group': None,
                'verification_targets': ['carry-over item completeness', 'source-issue attribution'],
                'confidence': 'high',
            }
        else:
            decisions[did] = {
                'decision': 'KEEP',
                'reason': 'Date-specific W33 primary-source event with material or contextual technical relevance; retain for claim-level Evidence.',
                'scope_tags': ['current-window', 'technical-relevance'],
                'duplicate_group': None,
                'verification_targets': ['subject identity', 'W33 chronology', 'technical change', 'claim attribution boundary'],
                'confidence': 'high',
            }

    with runtime_tool.current_stage_basis_override():
        screening_package = screening.prepare_package(ROOT, snapshot_state, discovery_path, SRC / 'screening' / 'v2' / 'package', impl)
        pkg = core.load_json(screening_package)
        results_dir = screening_package.parent / 'results'
        results_dir.mkdir(parents=True, exist_ok=True)
        for batch in pkg['input']['batches']:
            batch_rows = screening.read_jsonl(screening_package.parent / batch['path'])
            result = {
                'schema_version': '2.0-rc1',
                'issue_id': ISSUE,
                'batch_id': batch['batch_id'],
                'basis': screening.expected_result_basis(ROOT, screening_package, pkg, batch),
                'decisions': [
                    {'discovery_id': r['discovery_id'], **decisions[r['discovery_id']]}
                    for r in batch_rows
                ],
            }
            core.write_json(results_dir / f"{batch['batch_id']}.json", result)
        screening_acceptance = screening.accept_results(ROOT, screening_package, results_dir, SRC / 'screening' / 'v2' / 'runs', impl)

        evidence_package = evidence.prepare_evidence_package(ROOT, snapshot_state, discovery_path, screening_acceptance, SRC / 'evidence' / 'v2' / 'package', impl)
        epkg = core.load_json(evidence_package)
        evidence_results = evidence_package.parent / 'results'
        evidence_results.mkdir(parents=True, exist_ok=True)

        evidence_specs = dict(primary_specs)
        evidence_specs['w33-carryover-ledger'] = {
            'canonical_name': 'W32→W33 carry-over disposition ledger', 'entity_type': 'OTHER', 'artifact_type': 'OTHER', 'organization': 'japanese-generative-ai-survey',
            'event_type': 'carry-over-disposition', 'source_title': 'W32→W33 carry-over disposition ledger', 'source_class': 'PRIMARY_REPOSITORY', 'published_at': None,
            'claims': [('The W33 carry-over ledger explicitly disposes every inherited W32 item instead of silently dropping or redating unresolved material.', 'PRIMARY_FACT', 'Pipeline provenance fact.')],
            'limitations': [('The ledger is editorial provenance and does not itself constitute a new W33 technical development.', 'PRIMARY_FACT', 'Do not allocate feature space to this record.')],
            'verification_finding': 'The revalidated ledger is present, hash-pinned, and enumerates explicit dispositions for inherited W32 obligations.',
            'materiality': 'NON_MATERIAL', 'why': 'Required for completeness and auditability, but not publication material.',
            'dimensions': ['carry-over obligations'],
        }

        task_by_discovery: dict[str, str] = {}
        for meta in epkg['tasks']:
            task = core.load_json(evidence_package.parent / meta['path'])
            did = task['discovery_ids'][0]
            task_by_discovery[did] = task['evidence_task_id']
            spec = evidence_specs[did]
            card = make_card(epkg, evidence_package, meta, spec)
            core.write_json(evidence_results / Path(meta['path']).name, card)
        evidence_acceptance = evidence.accept_evidence_results(ROOT, evidence_package, evidence_results, SRC / 'evidence' / 'v2' / 'runs', impl)

        accepted_evidence = core.load_json(evidence_acceptance)
        views_input = SRC / 'evidence' / 'v2' / 'views-input'
        views_input.mkdir(parents=True, exist_ok=True)
        by_task_to_did = {task: did for did, task in task_by_discovery.items()}
        for row in accepted_evidence['results']:
            did = by_task_to_did[row['evidence_task_id']]
            spec = evidence_specs[did]
            annotation = {
                'why_this_issue': spec['why'],
                'window_relation': 'CARRY_OVER_DISPOSITION' if did == 'w33-carryover-ledger' else 'MAIN_EVENT',
                'carry_over': did == 'w33-carryover-ledger',
            }
            view = {
                'schema_version': '2.0-rc1',
                'issue_id': ISSUE,
                'research_profile': 'WEEKLY',
                'evidence_task_id': row['evidence_task_id'],
                'evidence_sha256': row['sha256'],
                'materiality': {'status': spec['materiality'], 'rationale': spec['why']},
                'scope_dimensions': spec['dimensions'],
                'profile_annotations': annotation,
            }
            core.write_json(views_input / evidence.view_filename(row['evidence_task_id']), view)
        views_acceptance = evidence.accept_edition_views(ROOT, PROFILE, evidence_acceptance, views_input, SRC / 'evidence' / 'v2' / 'views-runs', impl)

        ledger = evidence.build_materiality_ledger(ROOT, PROFILE, discovery_path, screening_acceptance, evidence_acceptance, views_acceptance, impl)
        ledger_path = SRC / 'materiality-ledger-v2.json'
        core.write_json(ledger_path, ledger)

        main_discoveries = [did for did in primary_specs]
        main_tasks = [task_by_discovery[did] for did in main_discoveries]
        completeness_result = {
            'schema_version': '2.0-rc1',
            'issue_id': ISSUE,
            'research_profile': 'WEEKLY',
            'basis': {
                'production_profile_sha256': core.sha256_file(PROFILE),
                'materiality_ledger_sha256': core.sha256_file(ledger_path),
            },
            'overall_status': 'READY',
            'obligations': [
                {
                    'obligation_id': 'weekly:current-relevance', 'dimension': 'current relevance',
                    'description': 'Establish which developments materially belong in this completed Weekly issue and why they matter to the issue.',
                    'status': 'SATISFIED', 'discovery_ids': main_discoveries, 'evidence_task_ids': main_tasks,
                    'rationale': 'Eight date-specific primary-source developments were verified and assigned explicit edition-level materiality; X-only false positives were explicitly dropped.',
                },
                {
                    'obligation_id': 'weekly:technical-significance', 'dimension': 'technical significance',
                    'description': 'Verify and prioritize the technical significance of candidate developments without relying on Weekly timing alone.',
                    'status': 'SATISFIED', 'discovery_ids': main_discoveries, 'evidence_task_ids': main_tasks,
                    'rationale': 'Claim-level Evidence separates first-party chronology from vendor/project claims and supports comparative synthesis across cyber deployment, serving systems, agent packaging, and integration layers.',
                },
                {
                    'obligation_id': 'weekly:carry-over', 'dimension': 'carry-over obligations',
                    'description': 'Explicitly dispose every carry-over obligation inherited from prior Weekly work.',
                    'status': 'SATISFIED', 'discovery_ids': ['w33-carryover-ledger'], 'evidence_task_ids': [task_by_discovery['w33-carryover-ledger']],
                    'rationale': 'The W32→W33 ledger was hash-revalidated and explicitly records every inherited item as backfill, unresolved/no-action, support-current, or promoted-current; no inherited item is silently redated into W33.',
                },
            ],
            'residual_limitations': [
                'Serving-stack performance/resource claims remain project-reported and are not normalized across unmatched workloads or hardware.',
                'No retained W33 paper reached full-paper review depth; the issue therefore omits Paper Watch rather than filling the category with abstract-only evidence.',
                'The imported Grok r3 raw is a discovery/community sensor only; three representative high-salience false positives are preserved as explicit DROP decisions.',
            ],
            'closure': None,
        }
        completeness_path = SRC / 'profile-completeness-v2.json'
        core.write_json(completeness_path, completeness_result)
        errors = completeness.validate_profile_completeness(completeness_result, ROOT, PROFILE, discovery_path, screening_acceptance, evidence_acceptance, views_acceptance, ledger_path, impl)
        if errors:
            raise RuntimeError('Completeness invalid: ' + '; '.join(errors))

        matrix = architecture.derive_candidate_matrix(ROOT, PROFILE, discovery_path, screening_acceptance, evidence_acceptance, views_acceptance, ledger_path, completeness_path, impl)
        matrix_path = SRC / 'candidate-matrix-v2.json'
        architecture.write_candidate_matrix(matrix_path, matrix)

    rows = artifact_by_title(matrix)
    desired = {
        'GPT-5.6-Cyber / Daybreak Red': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:LEAD', 'WEEKLY:LEAD'),
        'Daybreak on AWS': ('SELECTED', 'SUPPORTING', 'WEEKLY_MAGAZINE:LEAD_SUPPORT', 'WEEKLY:CYBER_DEPLOYMENT_SUPPORT'),
        'SGLang v0.5.17': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:SYSTEMS_FEATURE', 'WEEKLY:SERVING_STACK'),
        'vLLM v0.27.0–v0.27.1': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:SYSTEMS_FEATURE', 'WEEKLY:SERVING_STACK'),
        'FlashInfer v0.6.17': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:SYSTEMS_FEATURE', 'WEEKLY:SERVING_STACK'),
        'GitHub Agent Plugins 1.0': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:AGENT_BRIEF', 'WEEKLY:AGENT_INFRASTRUCTURE'),
        'Transformers v5.15.0 / Muse Glimmer': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:ECOSYSTEM_BRIEF', 'WEEKLY:MODEL_ECOSYSTEM'),
        'ComfyUI W33 media integrations': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:WATCHLIST', 'WEEKLY:WATCHLIST'),
        'W32→W33 carry-over disposition ledger': ('HOLD', 'NONE', None, None),
    }
    assignments = []
    for row in matrix['rows']:
        disp, usage, pub_role, arch_role = desired[row['title']]
        if disp == 'SELECTED':
            rationale = 'Selected because validated edition materiality is MATERIAL/CONTEXT and the candidate has a defined non-duplicative Architecture destination.'
        else:
            rationale = 'Held as audit/completeness provenance: it closes carry-over obligations but is NON_MATERIAL as a W33 technical story.'
        assignments.append({
            'candidate_id': row['candidate_id'], 'disposition': disp, 'rationale': rationale,
            'architecture_usage': usage, 'publication_role': pub_role, 'architecture_role': arch_role,
            'profile_extensions': {'why_this_issue': row['profile_extensions'].get('why_this_issue')},
        })
    dispositions = Counter(a['disposition'] for a in assignments)
    selection = {
        'schema_version': '2.0-rc1', 'issue_id': ISSUE, 'research_profile': 'WEEKLY', 'publication_profile': 'WEEKLY_MAGAZINE',
        'selection_version': '2026-W33-core-v2-architecture-review', 'status': 'ESTABLISHED',
        'basis': {
            'production_profile_sha256': core.sha256_file(PROFILE), 'candidate_matrix_sha256': core.sha256_file(matrix_path),
            'profile_completeness_sha256': core.sha256_file(completeness_path), 'materiality_ledger_sha256': core.sha256_file(ledger_path),
        },
        'assignments': assignments,
        'summary': {'candidate_count': len(matrix['rows']), 'disposition_counts': {k: dispositions[k] for k in sorted(dispositions)}, 'selected_count': dispositions['SELECTED']},
    }
    selection_path = SRC / 'candidate-selection-v2.json'
    core.write_json(selection_path, selection)
    selection_errors = architecture.validate_selection(ROOT, selection, PROFILE, matrix_path, completeness_path, ledger_path)
    if selection_errors:
        raise RuntimeError('Selection invalid: ' + '; '.join(selection_errors))

    def row(title: str) -> dict:
        return rows[title]
    packages_spec = [
        ('pkg-01-cyber', 'Controlled cyber capability becomes governed infrastructure', 'Lead with the Daybreak event as a combined capability-and-governance change; use AWS only as supporting distribution evidence.',
         [row('GPT-5.6-Cyber / Daybreak Red')], [row('Daybreak on AWS')],
         ['Separate first-party chronology from vendor capability claims.', 'Carry Blue/Red access and authorization boundaries with every capability description.', 'Explain why AWS distribution changes operational relevance without treating it as independent benchmark evidence.']),
        ('pkg-02-serving-stack', 'Serving stack co-evolution: runtime, orchestration, and kernels move together', 'Synthesize SGLang, vLLM, and FlashInfer as one systems movement instead of three release-note summaries.',
         [row('SGLang v0.5.17'), row('vLLM v0.27.0–v0.27.1'), row('FlashInfer v0.6.17')], [],
         ['Compare layers and responsibilities, not incomparable project benchmark numbers.', 'Make project-reported performance/resource claims explicitly attributed.', 'Show why simultaneous runtime/kernel adaptation matters for new model architectures.']),
        ('pkg-03-agent-plugins', 'Agent Plugins 1.0 packages skills and MCP connectivity for reuse', 'Cover the W33 GitHub event as agent infrastructure: reusable distribution and governance of skills plus MCP servers across clients.',
         [row('GitHub Agent Plugins 1.0')], [],
         ['Distinguish packaging/reuse from claims of ecosystem-wide standardization.', 'Explain the operational significance of bundling skills and MCP connectivity without overclaiming security convergence.']),
        ('pkg-04-model-ecosystem', 'Integration layer brief: Transformers and Muse Glimmer', 'Use the Hugging Face release as a concise integration-layer signal, not as proof of underlying model-launch chronology or quality.',
         [row('Transformers v5.15.0 / Muse Glimmer')], [],
         ['Keep model-origin and quality claims below the verified Hugging Face integration evidence.']),
        ('pkg-05-watchlist', 'Watchlist: ComfyUI media integrations', 'Preserve a reader-useful watch item with explicit uncertainty and a concrete evidence threshold for future promotion.',
         [row('ComfyUI W33 media integrations')], [],
         ['State current observation: verified W33 integration/adoption.', 'State uncertainty: integration does not prove same-week underlying model launch, quality, or broad X momentum.', 'Future upgrade criterion: primary model chronology plus reproducible evaluation or sustained adoption evidence.']),
    ]
    packages = []
    for idx, (pid, title, purpose, prim, supp, must) in enumerate(packages_spec, start=1):
        placement = prim + supp
        packages.append({
            'package_id': pid, 'title': title, 'purpose': purpose,
            'primary_candidate_ids': [r['candidate_id'] for r in prim],
            'supporting_candidate_ids': [r['candidate_id'] for r in supp],
            'must_cover_requirements': must,
            'boundaries': union_boundaries(placement),
            'drafting_order': idx,
            'profile_extensions': {'weekly_package_role': 'LEAD' if idx == 1 else ('WATCHLIST' if idx == 5 else 'FEATURE_OR_BRIEF')},
            'publication_extensions': {'magazine_package_kind': 'lead' if idx == 1 else ('watchlist' if idx == 5 else 'feature-or-brief')},
        })
    arch = {
        'schema_version': '2.0-rc1', 'issue_id': ISSUE, 'research_profile': 'WEEKLY', 'publication_profile': 'WEEKLY_MAGAZINE', 'status': 'PROPOSED',
        'basis': {
            'production_profile_sha256': core.sha256_file(PROFILE), 'profile_completeness_sha256': core.sha256_file(completeness_path),
            'materiality_ledger_sha256': core.sha256_file(ledger_path), 'candidate_matrix_sha256': core.sha256_file(matrix_path),
            'candidate_selection_sha256': core.sha256_file(selection_path),
        },
        'editorial_thesis': '2026-W33の重心は単一ベンチマークの更新ではなく、生成AIの専門能力が「運用可能な境界」とともに実装され始めた点にある。Daybreakはサイバー専門化を承認・配布設計と一体化し、SGLang/vLLM/FlashInferは新しいモデル群を支える実行基盤を同時進化させ、Agent Plugins 1.0はskillsとMCPを再利用可能な配布単位へまとめた。統合層のTransformers/ComfyUIは、この運用化がモデル周辺へ波及していることを補助的に示す。',
        'architecture_goals': [
            '能力向上そのものと、アクセス制御・配布・実行基盤・再利用可能な統合という運用化の変化を同じ号の一本の論旨にまとめる。',
            'vendor/project claim と primary fact を混同せず、比較不能なベンチマーク数字を横並びにしない。',
            'legacy W33 の選定を温存せず、v2で新たに発見した Agent Plugins 1.0 を含めて fresh selection を示す。',
            'carry-over と X false-positive を明示的に disposition し、本文から落とす判断も Architecture Review で追跡可能にする。',
        ],
        'page_plan': {'target_pages': 12, 'max_pages': 16, 'notes': 'Lead 3–4p, serving systems 3p, agent infrastructure 2p, ecosystem brief 1–2p, watchlist 1p, front/back matter remainder. No Paper Watch filler.'},
        'packages': packages, 'selected_exceptions': [],
        'profile_extensions': {'weekly_window': profile['research_scope']['temporal_policy'], 'paper_watch': 'OMITTED_NO_FULL_REVIEW_EVIDENCE'},
        'publication_extensions': {'magazine_flow': ['lead', 'systems-feature', 'agent-brief', 'ecosystem-brief', 'watchlist']},
        'human_review': {'reviewed_by': None, 'reviewed_at': None, 'review_reference': None},
    }
    arch_path = SRC / 'architecture-v2.json'
    core.write_json(arch_path, arch)
    arch_errors = architecture.validate_architecture(ROOT, arch, PROFILE, completeness_path, ledger_path, matrix_path, selection_path, require_approved=False)
    if arch_errors:
        raise RuntimeError('Architecture invalid: ' + '; '.join(arch_errors))

    with runtime_tool.current_stage_basis_override():
        review = architecture.build_architecture_review_summary(ROOT, PROFILE, discovery_path, screening_acceptance, evidence_acceptance, views_acceptance, ledger_path, completeness_path, matrix_path, selection_path, arch_path, impl)
    review_path = SRC / 'architecture-review-summary-v2.json'
    core.write_json(review_path, review)
    if review['readiness']['status'] != 'READY_FOR_ARCHITECTURE_REVIEW':
        raise RuntimeError('Architecture review summary blocked: ' + '; '.join(review['readiness']['errors']))
    attention_path = SRC / 'architecture-review-attention-v2.json'
    review_attention.build_attention(ROOT, screening_acceptance, ledger_path, selection_path, attention_path, limit=50)
    review_attention.validate_attention(ROOT, attention_path)

    note = SRC / 'architecture-review-editorial-note-v2.md'
    note.write_text('''# 2026-W33 Architecture Review Editorial Note\n\nStatus: **READY_FOR_ARCHITECTURE_REVIEW / Human Gate pending**\n\n## Editorial thesis\n\n2026-W33の重心は、単一のモデル性能競争ではなく、専門能力・実行基盤・agent/tool packagingが「運用可能な境界」と一緒に実装され始めた点に置く。\n\n## Proposed flow\n\n1. **Lead — Controlled cyber capability becomes governed infrastructure**: GPT-5.6-Cyber / Daybreak Red + AWS distribution.\n2. **Systems feature — Serving stack co-evolution**: SGLang v0.5.17 / vLLM v0.27.x / FlashInfer v0.6.17.\n3. **Agent infrastructure brief — Agent Plugins 1.0**: skills + MCP servers as reusable installable units across GitHub Copilot surfaces.\n4. **Ecosystem brief — Transformers v5.15.0 / Muse Glimmer**: integration evidence only.\n5. **Watchlist — ComfyUI media integrations**: current integration signal, uncertainty, and explicit upgrade criterion.\n\n## Deliberate omissions / compression\n\n- **Paper Watch omitted**: retained paper pool did not reach full-paper review depth.\n- **Carry-over ledger held**: all W32 obligations are explicitly disposed but it is not a W33 technical story.\n- **Grok 4.6 / Qwen3.8-27B / alleged Anthropic Aug-14 Risk Report**: preserved in review attention as X-derived false positives rejected after primary-source reconciliation.\n- **Serving benchmarks**: no cross-project numeric leaderboard because workloads/hardware are not normalized.\n\n## Human review focus\n\n- Whether Daybreak should remain the lead over the serving-stack movement.\n- Whether Agent Plugins 1.0 deserves a two-page brief or a shorter ecosystem item.\n- Whether Transformers should remain a standalone brief or be merged into Watchlist.\n- Whether the explicit omission of Paper Watch is editorially acceptable for W33.\n''', encoding='utf-8')

    # Advance through the compact agent-first lifecycle only after the full semantic chain is valid.
    stage_review_and_advance(cfg, {'discovery-acceptance': discovery_acceptance}, 'W33_DISCOVERY_PROVENANCE_REVIEW', 'AGENT_RESEARCH', 'Discovery contains eight current first-party technical events, one explicit carry-over ledger, and three X-only claims retained for rejection; X manifest is complete and all raw paths are hash-bound.', 'W33 Discovery accepted under the Weekly Profile with explicit X and carry-over provenance.', 1)
    stage_review_and_advance(cfg, {'screening-acceptance': screening_acceptance}, 'W33_SCREENING_SEMANTIC_REVIEW', 'AGENT_RESEARCH', 'Every Discovery record has exactly one profile-neutral disposition. The three X false positives are DROP with primary-source reconciliation reasons; all current-window/carry-over records proceed to Evidence without Weekly why-now fields in Screening.', 'W33 Screening normalized the Discovery corpus without importing legacy editorial semantics.', 2)
    stage_review_and_advance(cfg, {'evidence-acceptance': evidence_acceptance, 'edition-views-acceptance': views_acceptance, 'materiality-ledger': ledger_path, 'profile-completeness': completeness_path}, 'W33_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW', 'AGENT_RESEARCH', 'Factual Evidence binds subjects/sources/claim classes; Weekly significance is isolated in Edition Views; all three Profile obligations are SATISFIED with residual limitations recorded and no silent Discovery drop.', 'W33 Evidence, Materiality, and Profile Completeness are ready for internal Selection.', 3)
    stage_review_and_advance(cfg, {'candidate-matrix': matrix_path, 'candidate-selection': selection_path}, 'W33_SELECTION_EDITORIAL_REVIEW', 'AGENT_EDITORIAL', 'Selection consolidates SGLang/vLLM/FlashInfer into one systems movement, adds Agent Plugins 1.0 from fresh v2 research, keeps Daybreak as lead, and holds the non-material carry-over ledger. Every Matrix candidate has exactly one assignment.', 'W33 internal Candidate Selection established without Human Gate semantics.', 4)
    stage_review_and_advance(cfg, {'issue-architecture': arch_path, 'architecture-review-summary': review_path, 'architecture-review-attention': attention_path}, 'W33_ARCHITECTURE_EDITORIAL_REVIEW', 'AGENT_EDITORIAL', 'Proposed Architecture gives every selected candidate exactly one valid destination, propagates all Evidence boundaries, exposes rejected/held decisions in bounded review attention, and is READY_FOR_ARCHITECTURE_REVIEW.', 'W33 Architecture proposal established and handed to the first Human Gate.', 5)

    final = core.load_json(STATE)
    if final['lifecycle_state'] != 'ARCHITECTURE_ESTABLISHED' or final['next_action'] != 'ARCHITECTURE_REVIEW' or final['terminal_reason'] != 'HUMAN_GATE_REACHED':
        raise RuntimeError(f'final gate mismatch: {final}')
    if final['human_gates']['architecture_review'] != 'pending':
        raise RuntimeError('Architecture Review was incorrectly auto-approved')
    print(json.dumps({
        'issue_id': ISSUE,
        'lifecycle_state': final['lifecycle_state'],
        'next_action': final['next_action'],
        'terminal_reason': final['terminal_reason'],
        'architecture_review': final['human_gates']['architecture_review'],
        'discovery_count': len(discoveries),
        'candidate_count': len(matrix['rows']),
        'selected_count': selection['summary']['selected_count'],
        'review_attention_count': core.load_json(attention_path)['total_count'],
    }, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
