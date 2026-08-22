#!/usr/bin/env python3
from __future__ import annotations
import json, shutil
from pathlib import Path
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts.survey_agent_tool_v2 import current_stage_basis_override

ROOT=Path('.').resolve(); ISSUE='2026-W33'; SRC=ROOT/'sources'/ISSUE
STATE=SRC/'production-state.json'; DISC=SRC/'discovery/discovery-v2.jsonl'
WORK=SRC/'screening/v2/work'; RESULTS=WORK/'results'; ACCEPTED=SRC/'screening/v2/accepted'
REV=SRC/'orchestration/v2/reviews/screening-stage-reviews.json'
WORKLOG=ROOT/'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'

KEEP_EXACT={
'base-github-release-sgl-project-sglang-v0_5_17','base-github-release-flashinfer-ai-flashinfer-v0_6_17','base-github-release-huggingface-transformers-v5_15_0','base-github-release-vllm-project-vllm-v0_27_0','base-official-feed-081601c279be28d3ef5a','base-official-feed-29b0e61ec6cd1ed38342','base-official-feed-5d3aff0aba5d0b8a3f2e','base-official-feed-c0986f6628d189a1ac37','x-weekly-signal-wave','base-arxiv-2608_09072v1','base-arxiv-2608_08654v1','base-arxiv-2608_11888v1','base-arxiv-2608_14718v1','base-arxiv-2608_08097v1','base-arxiv-2608_13263v1','base-arxiv-2608_08700v1','base-arxiv-2608_10669v1','base-arxiv-2608_09666v1'}
MAYBE_EXACT={'base-github-release-Comfy-Org-ComfyUI-v0_31_0','base-github-release-ggml-org-llama_cpp-b10369','base-official-index-minimax-news','base-arxiv-2608_13613v1','base-arxiv-2608_11742v1','base-arxiv-2608_13900v1'}
INSPECT_EXACT={'base-official-index-xai-news','base-official-index-google-gemini-api-release-notes','base-official-index-deepseek-api-updates','base-official-index-zai-release-notes','base-official-index-nvidia-generative-ai-blog','base-official-index-meta-ai-blog','base-official-index-qwen-blog'}
DROP_PREFIX='carry-w32-'

def decision_for(r):
 d=r['discovery_id']; title=(r.get('source') or {}).get('title') or ''
 if d.startswith(DROP_PREFIX):
  reason={
   'openai-gpt-5.6-w32-update':'The unresolved W32 generic GPT-5.6 update is superseded for W33 screening by distinct fresh W33 primary-source events (Daybreak/Ultrafast); do not carry the unresolved old item forward as a duplicate story.',
   'kimi-k3-github-copilot':'Fresh W33 intake does not establish the previously unresolved Kimi K3 GitHub Copilot integration as a distinct W33 event; drop the carry-over unless new primary evidence appears later.',
   'github-copilot-cloud-agent-w32':'Fresh W33 intake did not establish the unresolved W32 cloud-agent event as a material W33 development.',
   'claude-opus-4.1-api-retirement':'Fresh W33 Anthropic coverage did not establish the unresolved retirement notice as a material W33 event.',
   'repowise-agent-tool-efficiency':'Fresh W33 intake still lacks authoritative support for the unresolved repository/method/numeric claims.',
   'qwen3.8-27b-local-expectation-late':'Fresh W33 X signal mentions Qwen3.8-27B, but the fresh official Qwen index does not itself verify the exact model/weights chronology; the old speculative carry-over remains excluded pending primary proof.'}.get(title,'Fresh W33 intake does not independently resolve this W32 HOLD_OUT item.')
  return {'discovery_id':d,'decision':'DROP','reason':reason,'scope_tags':['carry-over-recheck','prior-week-unresolved'],'duplicate_group':None,'verification_targets':[],'confidence':'high'}
 if d in KEEP_EXACT:
  tags=[]; vt=[]; reason='Fresh W33 source is materially relevant and sufficiently concrete to justify Evidence verification.'
  if d=='x-weekly-signal-wave':
   tags=['community-signal','cross-lane']; vt=['Verify each technical/release/pricing/benchmark claim from first-party sources before Evidence; use X only for salience/reception.']; reason='Fresh Grok/X coverage establishes material community salience across several W33 developments; retain only as community/discovery evidence, never as technical fact authority.'
  elif 'official-feed' in d:
   tags=['first-party-event']; vt=['Verify exact first-party page content, chronology, access scope, and vendor-claim boundaries.']
  elif 'github-release' in d:
   tags=['serving-or-integration','first-party-repository']; vt=['Verify release chronology and distinguish project-reported performance from cross-project comparable evidence.']
  elif 'arxiv' in d:
   tags=['paper-candidate']; vt=['Review full paper/method/results/limitations before promotion; abstract alone is insufficient for strong claims.']
  return {'discovery_id':d,'decision':'KEEP','reason':reason,'scope_tags':tags,'duplicate_group':None,'verification_targets':vt,'confidence':'high'}
 if d in INSPECT_EXACT:
  return {'discovery_id':d,'decision':'INSPECT','reason':'Fresh official index snapshot plus fresh X signal suggests a potentially material W33 event, but the index snapshot is not candidate-specific technical Evidence. Inspect and fetch the exact first-party item before deciding materiality.','scope_tags':['primary-source-gap-fill','model-release-wave'],'duplicate_group':'w33-model-wave','verification_targets':[f'Locate and verify exact W33 first-party release/update for {title}; establish timestamp relative to cutoff, model identity, availability, and claim boundaries.'],'confidence':'medium'}
 if d in MAYBE_EXACT:
  vt=['Verify technical novelty and whether it adds orthogonal W33 value beyond stronger selected themes.']
  if 'arxiv' in d: vt=['Review full paper and assess whether contribution merits Paper Watch/feature support rather than abstract-only mention.']
  return {'discovery_id':d,'decision':'MAYBE','reason':'Fresh W33 signal is valid but relative materiality is uncertain versus stronger candidates; retain for bounded Evidence inspection without reserving editorial space.','scope_tags':['watchlist-or-paper'],'duplicate_group':None,'verification_targets':vt,'confidence':'medium'}
 return {'discovery_id':d,'decision':'DROP','reason':'Fresh W33 discovery record does not clear the materiality threshold for further Evidence work after comparison with stronger same-week candidates.','scope_tags':['low-relative-priority'],'duplicate_group':None,'verification_targets':[],'confidence':'medium'}

def main():
 if WORK.exists(): shutil.rmtree(WORK)
 if ACCEPTED.exists(): shutil.rmtree(ACCEPTED)
 ACCEPTED.mkdir(parents=True,exist_ok=True)
 impl=core.repository_commit_sha(ROOT)
 with current_stage_basis_override():
  pkg=screening.prepare_package(ROOT,STATE,DISC,WORK,impl,max_records=12,max_json_chars=200000)
 RESULTS.mkdir(parents=True,exist_ok=True)
 package=core.load_json(pkg)
 for b in package['input']['batches']:
  inp=screening.read_jsonl(WORK/b['path'])
  out={'schema_version':'2.0-rc1','issue_id':ISSUE,'batch_id':b['batch_id'],'basis':screening.expected_result_basis(ROOT,pkg,package,b),'decisions':[decision_for(r) for r in inp]}
  core.write_json(RESULTS/f"{b['batch_id']}.json",out)
 with current_stage_basis_override():
  acc=screening.accept_results(ROOT,pkg,RESULTS,ACCEPTED,impl)
 accepted=core.load_json(acc)
 counts={k:0 for k in ['KEEP','MAYBE','DROP','INSPECT']}
 for row in accepted['decisions']: counts[row['decision']]+=1
 REV.parent.mkdir(parents=True,exist_ok=True)
 core.write_json(REV,{'reviews':[{'check_id':'CORE_STAGE_CONTRACT','kind':'DETERMINISTIC','executor':'survey_stage_validation_v2.py','evidence':'Accepted Screening result set must bind exact Discovery, State, prompt, result schema and complete per-record decisions.','result_path':'sources/2026-W33/orchestration/v2/reviews/screening-core-stage-contract.json'},{'check_id':'FRESH_W33_SCREENING','kind':'AGENT_RESEARCH','executor':'ChatGPT','evidence':f'All {accepted["record_count"]} fresh Discovery records received explicit Screening decisions. X is retained only as community signal; official-index records require candidate-specific primary verification; all six W32 HOLD_OUT rechecks were explicitly disposed without old W33 conclusions. Decision counts: {counts}.'}]})
 with WORKLOG.open('a',encoding='utf-8') as f:
  f.write('\n## Fresh Screening\n\n'); f.write(f'- Screened all {accepted["record_count"]} accepted Discovery records under Core v2.\n'); f.write(f'- Decision counts: `{json.dumps(counts,sort_keys=True)}`.\n'); f.write('- Fresh X aggregate retained only as community-signal Evidence input; candidate-specific technical claims require primary verification.\n'); f.write('- All six W32 current-main HOLD_OUT rechecks were explicitly DROP at Screening because fresh W33 intake did not independently justify carrying those unresolved old items as W33 stories; distinct fresh W33 events remain separate candidates.\n')
 print(json.dumps({'acceptance':str(acc.relative_to(ROOT)),'counts':counts,'record_count':accepted['record_count']},indent=2))
if __name__=='__main__': main()
