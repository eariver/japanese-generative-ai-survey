#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core

ROOT=Path('.').resolve(); ISSUE='2026-W33'; SRC=ROOT/'sources'/ISSUE
SEED=SRC/'source-intake-v2/fresh-non-x-screening-seed/screening-index.jsonl'
XRAW='sources/2026-W33/external/x/weekly-x-2026-W33-fresh-r1/raw/grok-x-result.md'
XMAN=SRC/'external/x/x-source-intake-v2.json'
OUTDIR=SRC/'discovery'; RECORDS=OUTDIR/'discovery-v2.jsonl'; ACCEPT=OUTDIR/'discovery-accepted-v2.json'
REV=SRC/'orchestration/v2/reviews/discovery-stage-reviews.json'
WORKLOG=ROOT/'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'

SELECTED_IDS=[
'github-release:sgl-project/sglang@v0.5.17',
'github-release:flashinfer-ai/flashinfer@v0.6.17',
'github-release:huggingface/transformers@v5.15.0',
'github-release:vllm-project/vllm@v0.27.0',
'github-release:Comfy-Org/ComfyUI@v0.31.0',
'github-release:ggml-org/llama.cpp@b10369',
'official-feed:081601c279be28d3ef5a',
'official-feed:29b0e61ec6cd1ed38342',
'official-feed:5d3aff0aba5d0b8a3f2e',
'official-feed:c0986f6628d189a1ac37',
'official-index:xai-news',
'official-index:google-gemini-api-release-notes',
'official-index:deepseek-api-updates',
'official-index:zai-release-notes',
'official-index:nvidia-generative-ai-blog',
'official-index:meta-ai-blog',
'official-index:qwen-blog',
'official-index:minimax-news',
'arxiv:2608.09072v1',
'arxiv:2608.08654v1',
'arxiv:2608.11888v1',
'arxiv:2608.14718v1',
'arxiv:2608.13613v1',
'arxiv:2608.08097v1',
'arxiv:2608.13263v1',
'arxiv:2608.08700v1',
'arxiv:2608.10669v1',
'arxiv:2608.09666v1',
'arxiv:2608.11742v1',
'arxiv:2608.13900v1',
]

CARRY=[
('carry-w32-openai-gpt56-update','openai-gpt-5.6-w32-update','Distinct W32 GPT-5.6 update was unresolved; re-check whether W33 contains a new material event.'),
('carry-w32-kimi-k3-copilot','kimi-k3-github-copilot','W32 Copilot integration lacked primary confirmation; re-check only if W33 has authoritative confirmation.'),
('carry-w32-copilot-cloud-agent','github-copilot-cloud-agent-w32','Exact W32 cloud-agent event was unresolved; dispose against fresh W33 sources.'),
('carry-w32-claude-retirement','claude-opus-4.1-api-retirement','Exact Anthropic retirement notice was unresolved; re-check against fresh official snapshot.'),
('carry-w32-repowise','repowise-agent-tool-efficiency','Repository/method/numeric claims were unresolved; do not promote absent fresh evidence.'),
('carry-w32-qwen38-27b','qwen3.8-27b-local-expectation-late','Speculative Qwen3.8-27B social claim lacked official model/weights confirmation; re-check against fresh Qwen authority.'),
]

def source_record(seed:dict, did:str)->dict:
 return {'schema_version':'2.0-rc1','issue_id':ISSUE,'discovery_id':did,'provenance':{'origin':'BASE','research_pass':0,'parent_refs':[],'obligation_ids':['weekly:current-relevance','weekly:technical-significance'],'reason':'Selected from the fresh W33 v2 Source Intake coverage review for semantic Screening; no legacy W33 result used.'},'source':{k:seed.get(k) for k in ['source_type','collector_id','collector_run_id','observed_at','title','locator','raw_paths','published_at','summary_text','metadata']}}

def main():
 rows=[json.loads(x) for x in SEED.read_text(encoding='utf-8').splitlines() if x.strip()]
 by={r['screening_id']:r for r in rows}
 missing=[x for x in SELECTED_IDS if x not in by]
 if missing: raise SystemExit('selected fresh IDs missing: '+repr(missing))
 records=[]
 for sid in SELECTED_IDS:
  did='base-'+sid.replace(':','-').replace('/','-').replace('@','-').replace('.','_')
  records.append(source_record(by[sid],did))
 records.append({'schema_version':'2.0-rc1','issue_id':ISSUE,'discovery_id':'x-weekly-signal-wave','provenance':{'origin':'BASE','research_pass':0,'parent_refs':[],'obligation_ids':['weekly:current-relevance','weekly:technical-significance'],'reason':'Fresh Grok/X Weekly coverage scan returned material community signal across model releases, agents, multimodal, local inference, evaluation, and security. Raw X claims remain non-authoritative pending primary-source verification.'},'source':{'source_type':'x-community-signal','collector_id':'grok-x-source-intake','collector_run_id':'weekly-x-2026-W33-fresh-r1','observed_at':'2026-08-22T15:59:41Z','title':'Fresh W33 X community signal wave','locator':'Grok_X_SourseIntake/Weekly/2026-W33/weekly-x-2026-W33-fresh-r1/grok-x-result.md','raw_paths':[XRAW],'published_at':None,'summary_text':'Fresh X scan surfaced Grok 4.6, Gemini 3.7 Flash, DeepSeek V4-Pro-0813, GLM-5.3, Nemotron 3.5 Lightning, Muse Glimmer, Qwen-related local interest, and secondary video/audio signals; every technical claim requires authoritative verification.','metadata':{'role':'DISCOVERY_AND_COMMUNITY_SIGNAL_ONLY','coverage_lanes':'A-L'}}})
 prior='sources/2026-W32/candidate-selection-v0.1.md'
 for did,prior_id,summary in CARRY:
  records.append({'schema_version':'2.0-rc1','issue_id':ISSUE,'discovery_id':did,'provenance':{'origin':'GAP_FILL','research_pass':1,'parent_refs':[],'obligation_ids':['weekly:carry-over'],'reason':'Fresh W33 re-check of a HOLD_OUT item in the current-main W32 selection authority; old W33 disposition is not consulted.'},'source':{'source_type':'prior-week-authority','collector_id':'repository-current-main','collector_run_id':'2026-W32-selection-current-main','observed_at':'2026-08-22T16:14:00Z','title':prior_id,'locator':'https://github.com/eariver/japanese-generative-ai-survey/blob/main/sources/2026-W32/candidate-selection-v0.1.md','raw_paths':[prior],'published_at':None,'summary_text':summary,'metadata':{'prior_issue':'2026-W32','prior_role':'HOLD_OUT','recheck_required':True}}})
 OUTDIR.mkdir(parents=True,exist_ok=True)
 RECORDS.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in records)+'\n',encoding='utf-8')
 if ACCEPT.exists(): ACCEPT.unlink()
 discovery.build_acceptance(ROOT,RECORDS,XMAN,ISSUE,ACCEPT)
 REV.parent.mkdir(parents=True,exist_ok=True)
 REV.write_text(json.dumps({'reviews':[
  {'check_id':'CORE_STAGE_CONTRACT','kind':'DETERMINISTIC','executor':'survey_stage_validation_v2.py','evidence':'Exact Core v2 Discovery acceptance, X integration, graph and Raw byte authority must validate before adoption.','result_path':'sources/2026-W33/orchestration/v2/reviews/discovery-core-stage-contract.json'},
  {'check_id':'FRESH_W33_DISCOVERY_COVERAGE','kind':'AGENT_RESEARCH','executor':'ChatGPT','evidence':'Reviewed all 96 fresh non-paper candidates via compact set and lexical-prioritized paper candidates across A-L lanes; accepted 30 fresh non-X records, one fresh X aggregate signal, and six W32 HOLD_OUT re-checks. No legacy W33 intake or shortlist used.'},
  {'check_id':'WEEKLY_CARRY_OVER_RECHECK','kind':'AGENT_RESEARCH','executor':'ChatGPT','evidence':'Carry-over input is current-main W32 HOLD_OUT authority only. Six unresolved W32 items are explicitly represented for fresh W33 disposal; no old W33 carry-over conclusions are reused.'}
 ]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 with WORKLOG.open('a',encoding='utf-8') as f:
  f.write('\n## Fresh Discovery construction\n\n')
  f.write(f'- Built Core v2 Discovery from {len(SELECTED_IDS)} fresh non-X candidates, one fresh Grok/X aggregate signal, and {len(CARRY)} W32 current-main HOLD_OUT re-check records.\n')
  f.write('- Legacy W33 Source Intake, Screening, Evidence, Selection, and Architecture were not used.\n')
  f.write('- Paper candidates were selected only after compact review of the fresh 2,569-paper seed across A-L technical lanes.\n')
  f.write('- W32 carry-over uses the current-main W32 selection authority as a GAP_FILL research input; old W33 carry-over dispositions are excluded.\n')
 print(json.dumps({'records':len(records),'fresh_non_x':len(SELECTED_IDS),'x':1,'carry_rechecks':len(CARRY),'acceptance':str(ACCEPT.relative_to(ROOT))},indent=2))
if __name__=='__main__': main()
