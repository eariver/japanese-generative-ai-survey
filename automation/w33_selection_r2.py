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
EACC=SRC/'evidence/v2/accepted/48e9709c64f871dc2e5356984e0aee1073c7234f2976e656475cd82b3da16093/evidence-accepted.json'
VACC=SRC/'evidence/v2/edition-views/accepted/7ed8209758a5dfe105da573feb805010bd3ce5f5be406bda3172bcb40f9e088e/edition-views-accepted.json'
LEDGER=SRC/'materiality-ledger-v2.json'; COMPLETE=SRC/'profile-completeness-v2.json'
MATRIX=SRC/'candidate-matrix-v2.json'; SELECT=SRC/'candidate-selection-v2.json'
REV=SRC/'orchestration/v2/reviews/selection-r2-stage-reviews.json'
WORKLOG=ROOT/'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'

PRIMARY={
 'base-official-feed-081601c279be28d3ef5a':'WEEKLY:CYBER_LEAD',
 'base-official-feed-c0986f6628d189a1ac37':'WEEKLY:SERVING_SPEED_LEAD',
 'base-github-release-sgl-project-sglang-v0_5_17':'WEEKLY:SERVING_STACK_LEAD',
 'x-weekly-signal-wave':'WEEKLY:COMMUNITY_PULSE_LEAD',
}
SUPPORT_MATERIAL={
 'base-official-feed-29b0e61ec6cd1ed38342':'WEEKLY:CYBER_SUPPORT',
 'base-official-feed-5d3aff0aba5d0b8a3f2e':'WEEKLY:CYBER_DISTRIBUTION_SUPPORT',
 'base-github-release-vllm-project-vllm-v0_27_0':'WEEKLY:SERVING_STACK_SUPPORT',
 'base-github-release-flashinfer-ai-flashinfer-v0_6_17':'WEEKLY:SERVING_STACK_SUPPORT',
}
PAPERS={
 'base-arxiv-2608_08654v1','base-arxiv-2608_09072v1','base-arxiv-2608_08700v1',
 'base-arxiv-2608_11888v1','base-arxiv-2608_13263v1','base-arxiv-2608_09666v1',
 'base-arxiv-2608_08097v1','base-arxiv-2608_10669v1','base-arxiv-2608_14718v1'
}
OSS={
 'base-github-release-Comfy-Org-ComfyUI-v0_31_0',
 'base-github-release-ggml-org-llama_cpp-b10369',
 'base-github-release-huggingface-transformers-v5_15_0'
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
   is_x = did == 'x-weekly-signal-wave'
   assignments.append({
    'candidate_id':row['candidate_id'],'disposition':'SELECTED',
    'rationale':('Recurring Weekly Community Pulse authority: preserve what was salient on X as SOCIAL_OBSERVATION without promoting underlying technical claims.' if is_x else 'Fresh W33 MATERIAL candidate with verified first-party/project source and a distinct feature-level editorial role; preserve all source-owner claim boundaries.'),
    'architecture_usage':'PRIMARY',
    'publication_role':('WEEKLY_MAGAZINE:X_COMMUNITY_WATCH' if is_x else 'WEEKLY_MAGAZINE:FEATURE_OR_SECTION'),
    'architecture_role':PRIMARY[did],'profile_extensions':{'discovery_id':did}
   })
  elif did in SUPPORT_MATERIAL:
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'SELECTED','rationale':'Fresh W33 MATERIAL candidate is best consumed as supporting evidence within a stronger same-theme feature rather than as a duplicate standalone story.','architecture_usage':'SUPPORTING','publication_role':'WEEKLY_MAGAZINE:SUPPORTING_EVIDENCE','architecture_role':SUPPORT_MATERIAL[did],'profile_extensions':{'discovery_id':did}})
  elif did in PAPERS:
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'SELECTED','rationale':'Reader-useful W33 CONTEXT candidate routed to recurring Research Paper Watch. Accepted Evidence is abstract-level, so the item must remain bounded to author-claim/abstract context and must not be written as a full-paper verification.','architecture_usage':'SUPPORTING','publication_role':'WEEKLY_MAGAZINE:RESEARCH_PAPER_WATCH','architecture_role':'WEEKLY:RESEARCH_WATCH_SUPPORT','profile_extensions':{'discovery_id':did}})
  elif did in OSS:
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'SELECTED','rationale':'Verified W33 CONTEXT release routed to recurring OSS & GitHub Watch so non-feature ecosystem movement remains visible to readers.','architecture_usage':'SUPPORTING','publication_role':'WEEKLY_MAGAZINE:OSS_GITHUB_WATCH','architecture_role':'WEEKLY:OSS_WATCH_SUPPORT','profile_extensions':{'discovery_id':did}})
  else:
   reason='Not selected for W33 r2. '
   if row['materiality']=='HOLD': reason+='Upstream Evidence/Edition View remains HOLD; unresolved candidate-specific facts must not be promoted.'
   else: reason+='Candidate is outside the validated Feature/Community/Research/OSS weekly coverage set.'
   assignments.append({'candidate_id':row['candidate_id'],'disposition':'HOLD','rationale':reason,'architecture_usage':'NONE','publication_role':None,'architecture_role':None,'profile_extensions':{'discovery_id':did}})
 selection={
  'schema_version':'2.0-rc1','issue_id':ISSUE,'research_profile':'WEEKLY','publication_profile':'WEEKLY_MAGAZINE',
  'selection_version':'2026-W33-fresh-v2-selection-r2','status':'ESTABLISHED',
  'basis':{'production_profile_sha256':core.sha256_file(PROFILE),'candidate_matrix_sha256':core.sha256_file(MATRIX),'profile_completeness_sha256':core.sha256_file(COMPLETE),'materiality_ledger_sha256':core.sha256_file(LEDGER)},
  'assignments':sorted(assignments,key=lambda x:x['candidate_id']),
  'summary':{'candidate_count':len(assignments),'disposition_counts':{},'selected_count':sum(a['disposition']=='SELECTED' for a in assignments)}
 }
 counts={}
 for a in assignments: counts[a['disposition']]=counts.get(a['disposition'],0)+1
 selection['summary']['disposition_counts']={k:counts[k] for k in sorted(counts)}
 errs=arch.validate_selection(ROOT,selection,PROFILE,MATRIX,COMPLETE,LEDGER)
 if errs: raise SystemExit('Selection r2 invalid: '+'; '.join(errs))
 if selection['summary']['selected_count'] != 20 or counts.get('HOLD') != 11:
  raise SystemExit(f'unexpected r2 selection counts: {selection["summary"]}')
 core.write_json(SELECT,selection)
 REV.parent.mkdir(parents=True,exist_ok=True)
 core.write_json(REV,{'reviews':[
  {'check_id':'CORE_STAGE_CONTRACT','kind':'DETERMINISTIC','executor':'survey_stage_validation_v2.py','evidence':'Candidate Matrix must exactly derive from accepted r2 Evidence/View/Materiality/Completeness, and Candidate Selection must assign every Matrix candidate exactly once.','result_path':'sources/2026-W33/orchestration/v2/reviews/selection-r2-core-stage-contract.json'},
  {'check_id':'WEEKLY_SELECTION_COVERAGE','kind':'AGENT_EDITORIAL','executor':'ChatGPT','evidence':'W33 r2 distinguishes Feature-level selection from recurring Weekly coverage: 7 MATERIAL candidates feed three features, 1 X CONTEXT candidate feeds Community Pulse, 9 paper CONTEXT candidates feed bounded Research Watch, and 3 OSS CONTEXT candidates feed OSS/GitHub Watch; 11 HOLD items remain non-selected.'}
 ]})
 with WORKLOG.open('a',encoding='utf-8') as f:
  f.write('\n\n## W33 r2 Candidate Selection\n\n')
  f.write(f'- Candidate Matrix derived from r2 Evidence: {len(matrix["rows"])} candidates.\n')
  f.write(f'- Selection r2: {selection["summary"]["selected_count"]} SELECTED, {counts.get("HOLD",0)} HOLD.\n')
  f.write('- Coverage distinction: 7 MATERIAL feature/support candidates plus 13 CONTEXT candidates for X Community Pulse, Research Paper Watch, and OSS & GitHub Watch. Feature count is no longer treated as the total number of weekly topics.\n')
 print(json.dumps({'matrix_summary':matrix['summary'],'selection_summary':selection['summary']},indent=2))

if __name__=='__main__': main()
