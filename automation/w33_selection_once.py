#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from scripts import survey_architecture_v2 as arch
from scripts import survey_production_v2 as core
from scripts.survey_agent_tool_v2 import current_stage_basis_override

ROOT=Path('.').resolve(); ISSUE='2026-W33'; SRC=ROOT/'sources'/ISSUE
PROFILE=SRC/'production-profile.json'; DISC=SRC/'discovery/discovery-v2.jsonl'
SCREEN=SRC/'screening/v2/accepted/a896f2347bc090e03f57faefe3a51e3caa40fc5f9f90f563d83a6d9daa916917/screening-accepted.json'
EACC=SRC/'evidence/v2/accepted/f5c19e5589b5ee0eb0db42e8c6d635dce8da1ec6a009445859c5ff00b3af8ec3/evidence-accepted.json'
VACC=SRC/'evidence/v2/edition-views/accepted/de6cd647f5a565a212b510263190432ec1877495f6c4e386a889fcae73bf14c6/edition-views-accepted.json'
LEDGER=SRC/'materiality-ledger-v2.json'; COMPLETE=SRC/'profile-completeness-v2.json'
MATRIX=SRC/'candidate-matrix-v2.json'; SELECT=SRC/'candidate-selection-v2.json'
REV=SRC/'orchestration/v2/reviews/selection-stage-reviews.json'
WORKLOG=ROOT/'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'

PRIMARY={
 'base-official-feed-081601c279be28d3ef5a':'WEEKLY:CYBER_LEAD',
 'base-official-feed-c0986f6628d189a1ac37':'WEEKLY:SERVING_SPEED_LEAD',
 'base-github-release-sgl-project-sglang-v0_5_17':'WEEKLY:SERVING_STACK_LEAD',
}
SUPPORT={
 'base-official-feed-29b0e61ec6cd1ed38342':'WEEKLY:CYBER_SUPPORT',
 'base-official-feed-5d3aff0aba5d0b8a3f2e':'WEEKLY:CYBER_DISTRIBUTION_SUPPORT',
 'base-github-release-vllm-project-vllm-v0_27_0':'WEEKLY:SERVING_STACK_SUPPORT',
 'base-github-release-flashinfer-ai-flashinfer-v0_6_17':'WEEKLY:SERVING_STACK_SUPPORT',
}

def main():
 impl=core.repository_commit_sha(ROOT)
 with current_stage_basis_override():
  matrix=arch.derive_candidate_matrix(ROOT,PROFILE,DISC,SCREEN,EACC,VACC,LEDGER,COMPLETE,impl)
 if MATRIX.exists(): MATRIX.unlink()
 arch.write_candidate_matrix(MATRIX,matrix)
 assignments=[]
 for row in matrix['rows']:
  did=row['discovery_ids'][0]
  if did in PRIMARY:
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'SELECTED','rationale':'Fresh W33 MATERIAL candidate with verified first-party/project source and a distinct primary editorial role; preserve all source-owner claim boundaries.','architecture_usage':'PRIMARY','publication_role':'WEEKLY_MAGAZINE:FEATURE_OR_SECTION','architecture_role':PRIMARY[did],'profile_extensions':{'discovery_id':did}})
  elif did in SUPPORT:
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'SELECTED','rationale':'Fresh W33 MATERIAL candidate is best consumed as supporting evidence within a stronger same-theme package rather than as a duplicate standalone story.','architecture_usage':'SUPPORTING','publication_role':'WEEKLY_MAGAZINE:SUPPORTING_EVIDENCE','architecture_role':SUPPORT[did],'profile_extensions':{'discovery_id':did}})
  else:
   reason='Not selected for the W33 magazine architecture. '
   if row['materiality']=='HOLD':
    reason+='Upstream Evidence/Edition View remains HOLD, so no editorial promotion is allowed.'
   elif row['artifact_type']=='PAPER':
    reason+='The accepted Evidence is abstract-level only; the explicit completeness limitation says these papers should not anchor strong Paper Watch claims.'
   elif did=='x-weekly-signal-wave':
    reason+='Grok/X is retained as community context only and is not technical fact authority.'
   else:
    reason+='The candidate is CONTEXT rather than MATERIAL and does not justify scarce standalone space against the seven material developments.'
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'HOLD','rationale':reason,'architecture_usage':'NONE','publication_role':None,'architecture_role':None,'profile_extensions':{'discovery_id':did}})
 selection={
  'schema_version':'2.0-rc1','issue_id':ISSUE,'research_profile':'WEEKLY','publication_profile':'WEEKLY_MAGAZINE',
  'selection_version':'2026-W33-fresh-v2-selection-1','status':'ESTABLISHED',
  'basis':{'production_profile_sha256':core.sha256_file(PROFILE),'candidate_matrix_sha256':core.sha256_file(MATRIX),'profile_completeness_sha256':core.sha256_file(COMPLETE),'materiality_ledger_sha256':core.sha256_file(LEDGER)},
  'assignments':sorted(assignments,key=lambda x:x['candidate_id']),
  'summary':{'candidate_count':len(assignments),'disposition_counts':{},'selected_count':sum(a['disposition']=='SELECTED' for a in assignments)}
 }
 counts={}
 for a in assignments: counts[a['disposition']]=counts.get(a['disposition'],0)+1
 selection['summary']['disposition_counts']={k:counts[k] for k in sorted(counts)}
 errs=arch.validate_selection(ROOT,selection,PROFILE,MATRIX,COMPLETE,LEDGER)
 if errs: raise SystemExit('Selection invalid: '+'; '.join(errs))
 core.write_json(SELECT,selection)
 REV.parent.mkdir(parents=True,exist_ok=True)
 core.write_json(REV,{'reviews':[
  {'check_id':'CORE_STAGE_CONTRACT','kind':'DETERMINISTIC','executor':'survey_stage_validation_v2.py','evidence':'Candidate Matrix must exactly derive from accepted Evidence/View/Materiality/Completeness, and Candidate Selection must assign every Matrix candidate exactly once.','result_path':'sources/2026-W33/orchestration/v2/reviews/selection-core-stage-contract.json'},
  {'check_id':'WEEKLY_SELECTION_FOCUS','kind':'AGENT_EDITORIAL','executor':'ChatGPT','evidence':'Select exactly the seven MATERIAL candidates: three Daybreak/cyber items, Ultrafast, SGLang, vLLM, and FlashInfer. CONTEXT papers/integrations/X and all HOLD official-index items remain non-selected; no filler Paper Watch.'}
 ]})
 with WORKLOG.open('a',encoding='utf-8') as f:
  f.write('\n## Fresh Candidate Selection\n\n')
  f.write(f'- Candidate Matrix derived mechanically from the accepted fresh W33 Evidence chain: {len(matrix["rows"])} candidates; summary `{json.dumps(matrix["summary"],sort_keys=True)}`.\n')
  f.write(f'- Selection: {selection["summary"]["selected_count"]} SELECTED, {counts.get("HOLD",0)} HOLD.\n')
  f.write('- Selected primary roles: Daybreak/cyber lead, SGLang serving-stack lead, OpenAI Ultrafast serving-speed lead. Supporting roles: trusted-hands access policy, AWS Daybreak distribution, vLLM, FlashInfer.\n')
  f.write('- Abstract-only papers, official-index model signals, non-material integrations, and Grok/X context are not promoted to fill pages.\n')
 print(json.dumps({'matrix':str(MATRIX.relative_to(ROOT)),'selection':str(SELECT.relative_to(ROOT)),'matrix_summary':matrix['summary'],'selection_summary':selection['summary']},indent=2))

if __name__=='__main__': main()
