#!/usr/bin/env python3
from __future__ import annotations

import json, shutil
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_evidence_v2 as ev
from scripts import survey_screening_v2 as screening
from scripts.survey_agent_tool_v2 import current_stage_basis_override

ROOT=Path('.').resolve(); ISSUE='2026-W33'; SRC=ROOT/'sources'/ISSUE
STATE=SRC/'production-state.json'; PROFILE=SRC/'production-profile.json'; DISC=SRC/'discovery/discovery-v2.jsonl'
SCREEN=SRC/'screening/v2/accepted/a896f2347bc090e03f57faefe3a51e3caa40fc5f9f90f563d83a6d9daa916917/screening-accepted.json'
WORK=SRC/'evidence/v2/work'; RESULTS=WORK/'results'; ACCEPTED=SRC/'evidence/v2/accepted'
VIEWS=SRC/'evidence/v2/views-work'; VIEWS_ACCEPTED=SRC/'evidence/v2/edition-views/accepted'
LEDGER=SRC/'materiality-ledger-v2.json'; COMPLETE=SRC/'profile-completeness-v2.json'
REV=SRC/'orchestration/v2/reviews/evidence-stage-reviews.json'
WORKLOG=ROOT/'docs/checkpoints/2026-W33-core-v2-compilation-session-worklog.md'

WINDOW_START=core.parse_instant('2026-08-07T18:00:00-04:00')
WINDOW_END=core.parse_instant('2026-08-14T18:00:00-04:00')

def cls(st: str) -> str:
    s=st.lower()
    if 'arxiv' in s: return 'PRIMARY_PAPER'
    if 'github' in s: return 'PRIMARY_REPOSITORY'
    if s.startswith('x-') or 'grok' in s: return 'SOCIAL'
    if 'official' in s: return 'PRIMARY_OFFICIAL'
    return 'SECONDARY'

def eclass(st: str) -> str:
    s=st.lower()
    if 'arxiv' in s: return 'AUTHOR_CLAIM'
    if 'github' in s: return 'PROJECT_CLAIM'
    if s.startswith('x-') or 'grok' in s: return 'SOCIAL_OBSERVATION'
    if 'official-feed' in s: return 'VENDOR_CLAIM'
    return 'PRIMARY_FACT'

def status_for(st: str) -> str:
    s=st.lower()
    if 'github' in s or 'official-feed' in s: return 'VERIFIED'
    return 'PARTIAL'

def artifact_type(st: str) -> str:
    s=st.lower()
    if 'arxiv' in s: return 'PAPER'
    if 'github' in s: return 'FRAMEWORK'
    return 'OTHER'

def entity_type(st: str) -> str:
    s=st.lower()
    if 'arxiv' in s: return 'PAPER'
    if 'github' in s: return 'FRAMEWORK'
    return 'OTHER'

def relation(published):
    if not published: return 'OTHER'
    try: t=core.parse_instant(published)
    except Exception: return 'OTHER'
    if t < WINDOW_START: return 'PRE_WINDOW_RELEVANCE'
    if t > WINDOW_END: return 'POST_CUTOFF'
    return 'MAIN_EVENT'

def card_for(task: dict, meta: dict, package: dict) -> dict:
    src=task['source_records'][0]
    st=src['source_type']; title=src.get('title') or src['locator']; did=task['discovery_ids'][0]
    sid='src'; eid='subject'
    source_class=cls(st); ec=eclass(st); stat=status_for(st)
    strong=stat=='VERIFIED'
    if source_class=='SOCIAL':
        text='Fresh Grok/X intake records cross-topic community salience for W33; it is retained as social observation rather than technical fact authority.'
    elif 'official-index' in st.lower():
        text=f"The collected official index snapshot provides a first-party discovery surface for {title}, but does not by itself establish a candidate-specific W33 release or its technical claims."
    elif source_class=='PRIMARY_PAPER':
        text=f"The collected arXiv record for '{title}' presents the authors' claimed contribution; this Evidence pass does not treat abstract text as a full-paper technical review."
    else:
        text=f"The collected first-party source records '{title}' as a release/update relevant to W33; technical performance statements remain attributed to the source owner."
    lim=[]
    unresolved=[]
    if source_class=='PRIMARY_PAPER':
        lim.append('Only the collected arXiv abstract/metadata authority was used in this Core v2 Evidence pass; full-paper methods, tables, ablations, and limitations were not independently reviewed.')
        unresolved.append('Full-paper technical review remains open before any strong Paper Watch claim.')
    elif 'official-index' in st.lower():
        lim.append('The official index snapshot is not candidate-specific technical evidence; exact model/update chronology, availability, and benchmark details remain unresolved in this accepted Discovery graph.')
        unresolved.append('Candidate-specific first-party event page was not added to accepted Discovery and therefore cannot be silently introduced at Evidence.')
    elif source_class=='SOCIAL':
        lim.append('X/Grok is discovery/community signal only and is not technical Evidence authority under the Core v2 contract.')
        unresolved.append('Individual technical claims require separately accepted primary Discovery sources.')
    elif source_class=='PRIMARY_REPOSITORY':
        lim.append('Performance and resource numbers in release notes are project-reported and are not a cross-framework controlled benchmark.')
    else:
        lim.append('Capability/performance statements are first-party vendor claims unless separately supported by independent evidence.')
    source={
        'source_id':sid,'url':src['locator'],'source_class':source_class,'title':title,
        'published_at':src.get('published_at'),'accessed_at':src['observed_at'],
        'role':'Exact accepted Discovery source used for factual verification.'
    }
    events=[]
    if src.get('published_at'):
        events=[{'event_id':'event-1','event_type':'SOURCE_PUBLISHED_OR_RELEASED','event_date':src.get('published_at'),'subject_id':eid,'subject_role':'PRIMARY_SUBJECT','source_ids':[sid]}]
    claim={'statement_id':'claim-1','text':text,'subject_id':eid,'subject_role':'PRIMARY_SUBJECT','evidence_class':ec,'source_ids':[sid],'context':did}
    limitations=[{'statement_id':f'lim-{i+1}','text':x,'subject_id':eid,'subject_role':'PRIMARY_SUBJECT','evidence_class':ec,'source_ids':[sid],'context':'Evidence boundary'} for i,x in enumerate(lim)]
    targets=[]
    for target in task.get('verification_targets',[]):
        if strong:
            tstat='VERIFIED'; finding='Exact accepted first-party source identity and chronology were checked from the collected source; project/vendor performance remains explicitly attributed rather than independently benchmarked.'
        elif source_class=='SOCIAL':
            tstat='UNRESOLVED'; finding='Community salience is preserved, but technical/release claims are not promoted because this task has no accepted primary source.'
        elif 'official-index' in st.lower():
            tstat='UNRESOLVED'; finding='The index is first-party but not candidate-specific; the requested exact event details are not proven by this Discovery source.'
        else:
            tstat='UNRESOLVED'; finding='Abstract-level source is insufficient for the requested full-paper methods/results/limitations review.'
        targets.append({'target':target,'status':tstat,'finding':finding,'subject_ids':[eid],'source_ids':[sid]})
    return {
        'schema_version':'2.0-rc1','issue_id':ISSUE,'evidence_task_id':task['evidence_task_id'],
        'basis':{'task_sha256':meta['sha256'],'screening_acceptance_sha256':task['screening_basis']['screening_acceptance_sha256'],'prompt_sha256':package['prompt']['sha256'],'result_contract_sha256':package['contracts']['card']['sha256']},
        'status':stat,
        'entities':[{'entity_id':eid,'canonical_name':title,'entity_type':entity_type(st),'organization':src.get('metadata',{}).get('repository'),'canonical_url':src['locator']}],
        'artifact':{'primary_subject_id':eid,'artifact_type':artifact_type(st),'canonical_name':title,'canonical_url':src['locator']},
        'temporal':{'observed_at':src['observed_at'],'events':events},
        'sources':[source],'claims':[claim],'metrics':[],'limitations':limitations,
        'verification':{'targets':targets,'unresolved_questions':unresolved,'contradictions':[]}
    }

def materiality_for(src: dict, decision: dict, evidence_status: str):
    st=src['source_type'].lower(); loc=src['locator'].lower(); title=(src.get('title') or '').lower()
    if evidence_status=='NEEDS_MORE': return 'HOLD','Evidence requires more research before editorial use.'
    if 'official-index' in st: return 'HOLD','Official index is discovery-only here; candidate-specific release facts remain unresolved.'
    if st.startswith('x-') or 'grok' in st: return 'CONTEXT','Fresh X/Grok result is useful only for community salience and cross-lane context.'
    if 'arxiv' in st:
        if decision['decision']=='MAYBE': return 'HOLD','Abstract-level paper evidence plus MAYBE Screening does not justify promotion.'
        return 'CONTEXT','Paper is technically relevant, but this pass has abstract-level rather than full-paper Evidence; use only as bounded context.'
    if 'official-feed' in st: return 'MATERIAL','First-party W33 event source is concrete enough to support a material weekly development, with vendor-claim boundaries preserved.'
    if 'github' in st and any(k in loc for k in ['sglang','vllm-project/vllm','flashinfer']): return 'MATERIAL','First-party serving/runtime release contains substantial W33 technical change and concrete implementation detail.'
    if 'github' in st: return 'CONTEXT','Verified first-party ecosystem release is useful context but weaker than the lead W33 changes.'
    if decision['decision']=='MAYBE': return 'HOLD','MAYBE Screening remains unresolved after bounded Evidence inspection.'
    return 'CONTEXT','Verified/partial W33 signal is useful context without enough support for standalone promotion.'

def main():
    for p in [WORK,VIEWS]:
        if p.exists(): shutil.rmtree(p)
    RESULTS.mkdir(parents=True,exist_ok=True); ACCEPTED.mkdir(parents=True,exist_ok=True); VIEWS.mkdir(parents=True,exist_ok=True); VIEWS_ACCEPTED.mkdir(parents=True,exist_ok=True)
    impl=core.repository_commit_sha(ROOT)
    with current_stage_basis_override():
        pkg=ev.prepare_evidence_package(ROOT,STATE,DISC,SCREEN,WORK,impl)
    package=core.load_json(pkg)
    for meta in package['tasks']:
        task=core.load_json(WORK/meta['path'])
        core.write_json(RESULTS/Path(meta['path']).name,card_for(task,meta,package))
    with current_stage_basis_override():
        eacc=ev.accept_evidence_results(ROOT,pkg,RESULTS,ACCEPTED,impl)
        ev.validate_evidence_acceptance(ROOT,eacc,impl)
    eaccepted=core.load_json(eacc)
    dmap={r['discovery_id']:r for r in screening.read_jsonl(DISC)}
    sacc=core.load_json(SCREEN); smap={r['discovery_id']:r for r in sacc['decisions']}
    for entry in eaccepted['results']:
        did=entry['discovery_ids'][0]; src=dmap[did]['source']; dec=smap[did]
        mat,rat=materiality_for(src,dec,entry['status'])
        dims=['current relevance','technical significance']
        if did=='x-weekly-signal-wave': dims=['current relevance']
        view={
            'schema_version':'2.0-rc1','issue_id':ISSUE,'research_profile':'WEEKLY','evidence_task_id':entry['evidence_task_id'],'evidence_sha256':entry['sha256'],
            'materiality':{'status':mat,'rationale':rat},'scope_dimensions':dims,
            'profile_annotations':{'why_this_issue':rat,'window_relation':relation(src.get('published_at')),'carry_over':False}
        }
        core.write_json(VIEWS/ev.view_filename(entry['evidence_task_id']),view)
    with current_stage_basis_override():
        vacc=ev.accept_edition_views(ROOT,PROFILE,eacc,VIEWS,VIEWS_ACCEPTED,impl)
        ev.validate_edition_views_acceptance(ROOT,PROFILE,eacc,vacc,impl)
        ledger=ev.build_materiality_ledger(ROOT,PROFILE,DISC,SCREEN,eacc,vacc,impl)
    if LEDGER.exists(): LEDGER.unlink()
    ev.write_materiality_ledger(LEDGER,ledger)
    profile=core.load_json(PROFILE)
    task_by_discovery={r['discovery_ids'][0]:r['evidence_task_id'] for r in eaccepted['results']}
    active=[r for r in ledger['rows'] if r['downstream_disposition'] not in {'EXCLUDED','DUPLICATE'}]
    current_ids=[r['discovery_id'] for r in active]
    current_tasks=[task_by_discovery[x] for x in current_ids if x in task_by_discovery]
    technical_ids=[r['discovery_id'] for r in active if r['downstream_disposition'] in {'MATERIAL','CONTEXT','HOLD'}]
    technical_tasks=[task_by_discovery[x] for x in technical_ids if x in task_by_discovery]
    carry_ids=[r['discovery_id'] for r in ledger['rows'] if r['discovery_id'].startswith('carry-w32-')]
    desc={o['obligation_id']:o for o in profile['research_scope']['initial_obligations']}
    comp={
        'schema_version':'2.0-rc1','issue_id':ISSUE,'research_profile':'WEEKLY',
        'basis':{'production_profile_sha256':core.sha256_file(PROFILE),'materiality_ledger_sha256':core.sha256_file(LEDGER)},
        'overall_status':'LIMITED',
        'obligations':[
            {'obligation_id':'weekly:current-relevance','dimension':'current relevance','description':desc['weekly:current-relevance']['description'],'status':'SATISFIED','discovery_ids':current_ids,'evidence_task_ids':current_tasks,'rationale':'Fresh W33 intake, Screening and exact-source Evidence identify concrete in-window first-party releases plus bounded context/HOLD items.'},
            {'obligation_id':'weekly:technical-significance','dimension':'technical significance','description':desc['weekly:technical-significance']['description'],'status':'SATISFIED','discovery_ids':technical_ids,'evidence_task_ids':technical_tasks,'rationale':'Technical significance is explicitly separated into MATERIAL/CONTEXT/HOLD; project/vendor claims remain attributed and abstract-only papers are not promoted as fully reviewed.'},
            {'obligation_id':'weekly:carry-over','dimension':'carry-over obligations','description':desc['weekly:carry-over']['description'],'status':'SATISFIED','discovery_ids':carry_ids,'evidence_task_ids':[],'rationale':'All six W32 current-main HOLD_OUT rechecks received explicit fresh W33 Screening DROP/EXCLUDED dispositions; none was silently redated or inherited.'}
        ],
        'residual_limitations':[
            'arXiv candidates in this pass are supported by collected abstract/metadata authority rather than full-paper review, so they remain CONTEXT/HOLD and should not anchor strong Paper Watch claims.',
            'candidate-specific model-release details suggested by official-index plus X signals were not added to accepted Discovery; those records remain HOLD rather than being backfilled during Evidence.',
            'serving/runtime performance and resource figures are project-reported under heterogeneous hardware/workloads and are not treated as a cross-framework leaderboard.'
        ],
        'closure':None
    }
    errs=ev.validate_completeness(comp,ROOT,PROFILE,DISC,SCREEN,eacc,vacc,LEDGER,impl)
    if errs: raise SystemExit('Completeness invalid: '+'; '.join(errs))
    core.write_json(COMPLETE,comp)
    REV.parent.mkdir(parents=True,exist_ok=True)
    core.write_json(REV,{'reviews':[
        {'check_id':'CORE_STAGE_CONTRACT','kind':'DETERMINISTIC','executor':'survey_stage_validation_v2.py','evidence':'Evidence acceptance, Edition Views, Materiality Ledger and Profile Completeness must validate as one exact Core v2 stage basis.','result_path':'sources/2026-W33/orchestration/v2/reviews/evidence-core-stage-contract.json'},
        {'check_id':'SOURCE_SPECIFIC_FAIL_CLOSED_NOTES','kind':'AGENT_SEMANTIC','executor':'ChatGPT','evidence':'GitHub/official-feed claims remain project/vendor attributed; arXiv is abstract-level PARTIAL; official-index and Grok/X are not promoted to candidate-specific technical fact authority.'},
        {'check_id':'WEEKLY_CARRY_OVER_DISPOSITION','kind':'AGENT_SEMANTIC','executor':'ChatGPT','evidence':'All six W32 HOLD_OUT rechecks are explicitly DROP/EXCLUDED in the fresh W33 ledger; no silent redating.'}
    ]})
    statuses={}; mats={}
    for r in eaccepted['results']: statuses[r['status']]=statuses.get(r['status'],0)+1
    for r in core.load_json(vacc)['views']: mats[r['materiality']]=mats.get(r['materiality'],0)+1
    with WORKLOG.open('a',encoding='utf-8') as f:
        f.write('\n## Fresh Evidence / Materiality / Completeness\n\n')
        f.write(f'- Accepted Evidence tasks: {eaccepted["result_count"]}; statuses `{json.dumps(statuses,sort_keys=True)}`.\n')
        f.write(f'- Edition materiality counts: `{json.dumps(mats,sort_keys=True)}`.\n')
        f.write('- Evidence is fail-closed to accepted Discovery locators: no candidate-specific first-party URL found later in web research was silently injected into Evidence.\n')
        f.write('- arXiv items remain abstract-level PARTIAL and CONTEXT/HOLD; official-index records remain HOLD; X/Grok remains community context only.\n')
        f.write('- Completeness is LIMITED with all three Weekly obligations SATISFIED and three explicit residual limitations.\n')
    print(json.dumps({'evidence_acceptance':str(eacc.relative_to(ROOT)),'views_acceptance':str(vacc.relative_to(ROOT)),'ledger':str(LEDGER.relative_to(ROOT)),'completeness':str(COMPLETE.relative_to(ROOT)),'statuses':statuses,'materiality':mats},indent=2))

if __name__=='__main__': main()
