#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from scripts import survey_architecture_v2 as arch
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as attention

ROOT=Path('.').resolve(); SRC=ROOT/'sources/2026-W33'
PROFILE=SRC/'production-profile.json'; STATE=SRC/'production-state.json'; LEDGER=SRC/'materiality-ledger-v2.json'; COMPLETE=SRC/'profile-completeness-v2.json'
MATRIX=SRC/'candidate-matrix-v2.json'; SELECTION=SRC/'candidate-selection-v2.json'
ARCH=SRC/'architecture-v2.json'; SUMMARY=SRC/'architecture-review-summary-v2.json'; ATTENTION=SRC/'architecture-review-attention-v2.json'
WORKLOG=ROOT/'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'

CYBER={'base-official-feed-081601c279be28d3ef5a','base-official-feed-29b0e61ec6cd1ed38342','base-official-feed-5d3aff0aba5d0b8a3f2e'}
SERVING={'base-github-release-sgl-project-sglang-v0_5_17','base-github-release-vllm-project-vllm-v0_27_0','base-github-release-flashinfer-ai-flashinfer-v0_6_17'}
ULTRA={'base-official-feed-c0986f6628d189a1ac37'}
COMMUNITY={'x-weekly-signal-wave'}
PAPERS={'base-arxiv-2608_08654v1','base-arxiv-2608_09072v1','base-arxiv-2608_08700v1','base-arxiv-2608_11888v1','base-arxiv-2608_13263v1','base-arxiv-2608_09666v1','base-arxiv-2608_08097v1','base-arxiv-2608_10669v1','base-arxiv-2608_14718v1'}
OSS={'base-github-release-Comfy-Org-ComfyUI-v0_31_0','base-github-release-ggml-org-llama_cpp-b10369','base-github-release-huggingface-transformers-v5_15_0'}

def checkpoint_artifacts():
 out={}
 for cp in sorted((SRC/'orchestration/v2/checkpoints').glob('*.json')):
  p=core.load_json(cp)
  for row in p.get('artifacts',[]):
   path=ROOT/row['path']; name=row['name']
   if name in out and out[name].resolve()!=path.resolve(): raise ValueError(f'checkpoint artifact divergence: {name}')
   out[name]=path
 return out

def main():
 state=core.load_json(STATE)
 if state['lifecycle_state']!='SELECTION_COMPLETE': raise ValueError(f'expected SELECTION_COMPLETE, got {state["lifecycle_state"]}')
 matrix=core.load_json(MATRIX); selection=core.load_json(SELECTION)
 if selection['summary']['selected_count']!=20: raise ValueError('W33 r2 Architecture expects 20 selected candidates')
 rows={r['candidate_id']:r for r in matrix['rows']}
 selected={a['candidate_id']:a for a in selection['assignments'] if a['disposition']=='SELECTED'}
 did_to_cid={a['profile_extensions']['discovery_id']:cid for cid,a in selected.items()}
 def cids(group): return sorted(did_to_cid[x] for x in group)
 def boundary_union(ids):
  vals=[]
  for cid in ids:
   for b in rows[cid]['remaining_boundaries']:
    if b not in vals: vals.append(b)
  return vals
 cyber=cids(CYBER); serving=cids(SERVING); ultra=cids(ULTRA); community=cids(COMMUNITY); papers=cids(PAPERS); oss=cids(OSS)
 cyber_primary=[cid for cid in cyber if selected[cid]['architecture_usage']=='PRIMARY']; cyber_support=[cid for cid in cyber if selected[cid]['architecture_usage']=='SUPPORTING']
 serving_primary=[cid for cid in serving if selected[cid]['architecture_usage']=='PRIMARY']; serving_support=[cid for cid in serving if selected[cid]['architecture_usage']=='SUPPORTING']
 ultra_primary=ultra; community_primary=community
 packages=[
  {'package_id':'pkg-01-cyber','title':'Controlled cyber capability becomes governed infrastructure','purpose':'Explain Daybreak as a W33 capability-plus-governance story: model capability, trusted access, and AWS distribution are one operational development rather than three unrelated launches.','primary_candidate_ids':cyber_primary,'supporting_candidate_ids':cyber_support,'must_cover_requirements':['Separate cyber capability claims from the controls governing access to higher-risk capability.','Use trusted-hands policy and AWS distribution as governance/distribution evidence, not independent performance validation.','Preserve first-party attribution for capability and performance statements.'],'boundaries':boundary_union(cyber),'drafting_order':1,'profile_extensions':{'section_kind':'FEATURE'},'publication_extensions':{'section_label':'Feature'}},
  {'package_id':'pkg-02-serving-stack','title':'Serving stack co-evolution: runtime, orchestration, and kernels move together','purpose':'Synthesize SGLang, vLLM, and FlashInfer as W33 serving-stack movement without turning heterogeneous project-reported measurements into a cross-framework leaderboard.','primary_candidate_ids':serving_primary,'supporting_candidate_ids':serving_support,'must_cover_requirements':['Describe concrete release-level engineering movement across the three projects.','Avoid comparative benchmark ranking across different hardware, workloads, and measurement conditions.','Present the releases as stack-wide movement rather than three redundant release notes.'],'boundaries':boundary_union(serving),'drafting_order':2,'profile_extensions':{'section_kind':'FEATURE'},'publication_extensions':{'section_label':'Feature'}},
  {'package_id':'pkg-03-ultrafast','title':'Ultrafast preview: inference speed becomes a product mode','purpose':'Cover the Ultrafast preview as a distinct product/deployment signal while keeping the advertised speed claim preview-bounded and vendor-attributed.','primary_candidate_ids':ultra_primary,'supporting_candidate_ids':[],'must_cover_requirements':['State clearly that Ultrafast is a preview.','Attribute speed claims to the first-party source; do not convert them into independent benchmark conclusions.','Connect the preview to the infrastructure theme without conflating it with open-source serving releases.'],'boundaries':boundary_union(ultra),'drafting_order':3,'profile_extensions':{'section_kind':'FEATURE'},'publication_extensions':{'section_label':'Feature'}},
  {'package_id':'pkg-04-community-pulse','title':'X Community Pulse: a release-wave week shifts attention toward agents, cost, and integration speed','purpose':'Report what became salient in the fresh Grok/X observation layer during W33: dense multi-lab release comparisons, agent/coding and cost-per-success focus, local/open-weight momentum, rapid harness integrations, practitioner testing, and correction signals.','primary_candidate_ids':community_primary,'supporting_candidate_ids':[],'must_cover_requirements':['Describe these as observed community salience, not as independent proof that named technical claims are true.','Include the dense same-week multi-lab release wave as the central community context.','Cover the shift toward agent/coding capability and cost per successful run, the local/open-weight narrative, harness/IDE integration speed, rapid hands-on testing, and visible counter-signals/corrections.','Where named model, benchmark, pricing, date, or performance details are not separately supported by accepted primary Evidence, phrase only that they were discussed or claimed on X.'],'boundaries':boundary_union(community),'drafting_order':4,'profile_extensions':{'section_kind':'COMMUNITY_PULSE'},'publication_extensions':{'section_label':'X Community Watch','recurring':True}},
  {'package_id':'pkg-05-research-watch','title':'Research Paper Watch: agents, evaluation, KV cache, and multimodal benchmarks','purpose':'Give readers a bounded scan of nine technically relevant W33 research papers that did not warrant feature treatment but collectively show active directions in agent evaluation/scaffolding, safety/red teaming, KV-cache systems, visual-generation evaluation, and video-agent benchmarks.','primary_candidate_ids':[],'supporting_candidate_ids':papers,'must_cover_requirements':['Treat every item as abstract/metadata-level author-claim context; do not imply full-paper methods or results were independently reviewed.','Group papers by reader-useful theme rather than giving nine equal mini-articles.','Keep claims concise and explicitly bounded by the accepted abstract-level Evidence limitation.'],'boundaries':boundary_union(papers),'drafting_order':5,'profile_extensions':{'section_kind':'RESEARCH_WATCH'},'publication_extensions':{'section_label':'Research Paper Watch','recurring':True}},
  {'package_id':'pkg-06-oss-watch','title':'OSS & GitHub Watch: ComfyUI, llama.cpp, and Transformers keep the ecosystem moving','purpose':'Preserve verified non-feature ecosystem movement from ComfyUI, llama.cpp, and Transformers as a compact recurring OSS/GitHub Watch.','primary_candidate_ids':[],'supporting_candidate_ids':oss,'must_cover_requirements':['Summarize concrete first-party release movement without inflating it to feature-level significance.','Preserve project-reported performance/resource boundaries.','Keep the section compact and reader-oriented as a weekly ecosystem scan.'],'boundaries':boundary_union(oss),'drafting_order':6,'profile_extensions':{'section_kind':'OSS_WATCH'},'publication_extensions':{'section_label':'OSS & GitHub Watch','recurring':True}},
 ]
 payload={
  'schema_version':'2.0-rc1','issue_id':'2026-W33','research_profile':'WEEKLY','publication_profile':'WEEKLY_MAGAZINE','status':'PROPOSED',
  'basis':{'production_profile_sha256':core.sha256_file(PROFILE),'profile_completeness_sha256':core.sha256_file(COMPLETE),'materiality_ledger_sha256':core.sha256_file(LEDGER),'candidate_matrix_sha256':core.sha256_file(MATRIX),'candidate_selection_sha256':core.sha256_file(SELECTION)},
  'editorial_thesis':'W33 was not a three-story week. Three feature-level developments anchor the issue, but the broader week was characterized by a dense community release wave, active research on agent evaluation and systems, and continuing OSS movement. The issue must distinguish feature significance from weekly situational awareness and close by synthesizing what these parallel signals mean together.',
  'architecture_goals':['Preserve three feature-level themes without presenting them as the complete set of weekly developments.','Publish a recurring X Community Pulse whenever Weekly X intake is required; X is authority for observed community movement only, not underlying technical truth.','Route reader-useful CONTEXT candidates into recurring Research Paper Watch and OSS & GitHub Watch instead of silently dropping them because they are not feature-level.','Keep HOLD candidates out until candidate-specific evidence resolves them.','End the issue with a mandatory Japanese heading 「今週の総括」 derived from Weekly Profile Synthesis `current_interpretation`, integrating feature, community, research, OSS, and carry-over signals without introducing new unsupported facts.'],
  'page_plan':{'target_pages':18,'max_pages':24,'notes':'Three feature packages plus recurring Community Pulse, Research Paper Watch, OSS/GitHub Watch, and a final synthesis. Feature count is not total topic count; do not pad with HOLD items.'},
  'packages':packages,'selected_exceptions':[],
  'profile_extensions':{'weekly_closing_summary':{'required':True,'source':'profile_synthesis.current_interpretation','must_integrate':['feature_signals','community_signals','research_watch','oss_watch','carry_over_disposition']}},
  'publication_extensions':{'closing_summary':{'required':True,'heading':'今週の総括','placement':'after_body_before_references'},'weekly_recurring_sections':['X Community Watch','Research Paper Watch','OSS & GitHub Watch']},
  'human_review':{'reviewed_by':None,'reviewed_at':None,'review_reference':None}
 }
 core.write_json(ARCH,payload)
 errs=arch.validate_architecture(ROOT,payload,PROFILE,COMPLETE,LEDGER,MATRIX,SELECTION)
 if errs: raise ValueError('Architecture r2 invalid: '+'; '.join(errs))
 accepted=checkpoint_artifacts(); discovery=ROOT/core.load_json(accepted['discovery-acceptance'])['discovery_path']
 impl=core.repository_commit_sha(ROOT)
 with runtime_tool.current_stage_basis_override():
  summary=arch.build_architecture_review_summary(ROOT,PROFILE,discovery,accepted['screening-acceptance'],accepted['evidence-acceptance'],accepted['edition-views-acceptance'],LEDGER,COMPLETE,MATRIX,SELECTION,ARCH,impl)
 if summary['readiness']['status']!='READY_FOR_ARCHITECTURE_REVIEW': raise ValueError('Architecture r2 review blocked: '+'; '.join(summary['readiness']['errors']))
 core.write_json(SUMMARY,summary)
 attention.build_attention(ROOT,accepted['screening-acceptance'],LEDGER,SELECTION,ATTENTION,limit=50)
 attention.validate_attention(ROOT,ATTENTION)
 with WORKLOG.open('a',encoding='utf-8') as f:
  f.write('\n\n## W33 Architecture Review r2\n\n- Revised Architecture contains six draftable packages: three Features plus X Community Pulse, Research Paper Watch, and OSS & GitHub Watch.\n- Selection r2 contains 20 selected candidates (7 MATERIAL + 13 CONTEXT) and 11 HOLD candidates.\n- X Community Pulse preserves concrete Grok/X weekly movement as SOCIAL_OBSERVATION only; underlying technical claims remain primary-source bounded.\n- Final publication must render `profile_synthesis.current_interpretation` under the heading `今週の総括` after body sections and before references.\n- Architecture remains PROPOSED with Human Review metadata null.\n')
 print(ARCH); print(SUMMARY); print(ATTENTION)

if __name__=='__main__': main()
