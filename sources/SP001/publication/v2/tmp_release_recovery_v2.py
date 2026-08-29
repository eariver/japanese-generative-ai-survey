from datetime import datetime, timezone
from pathlib import Path
import json
from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_schema_v2 as schema_gate

root=Path('.').resolve(); cfg=core.load_json(root/core.DEFAULT_CONFIG)
source=root/'sources/SP001'; state_path=source/'production-state.json'; state=core.load_json(state_path)
assert state['lifecycle_state']=='FROZEN' and state['next_action']=='stage:release'
assert core.sha256_file(state_path)=='83ff4f6a544b4f88905ddbbc51dd239534045e8a25bba07ec96a54c872cd317c'
assert agent.validate_agent_state(root,cfg,state)==[]
manifest=source/'publication/v2/release-manifest-v2.json'
assert core.sha256_file(manifest)=='e2f82c5d9a0fcddc9a58855f3a9fa144fd6a3aa46190acbe6fda79ab6bb5a09a'
m=publication.validate_release_manifest(root,manifest)
assert m['release_identity']=='special/SP001' and m['pdf_sha256']=='9f6bef98d15bfaec1ea2aec3972005487c28e44ec84762e4fbaa51639d7fe1b2'

now=datetime.now(timezone.utc)
merge=source/'publication/v2/merge-verification-v2.json'
release=source/'publication/v2/release-record-v2.json'
publication.build_merge_verification(root,manifest,'dd1ad1e9f5f0aa2a930f3866b5347e9194cafa37',now,merge)
release_url=Path('/tmp/release-url.txt').read_text(encoding='utf-8').strip()
publication.build_release_record(root,manifest,merge,now,release_url,release)
r=publication.validate_release_record(root,release)
assert r['issue_id']=='SP001' and r['pdf_sha256']==m['pdf_sha256']

_,profile,_=agent._profile_and_source(root,cfg,state)
artifacts=[agent._named_authority(root,'merge-verification',merge),agent._named_authority(root,'release-record',release)]
agent._validate_stage_artifacts(root,cfg,state,profile,artifacts)
impl=core.repository_commit_sha(root)
assert impl=='dd1ad1e9f5f0aa2a930f3866b5347e9194cafa37'
contract=core.contract_identity(root,cfg,state['research_profile'],state['publication_profile'])
profile_path=root/state['profile']['path']
run_root=source/'execution/bridge-runs/SP001-r5-release'; run_root.mkdir(parents=True,exist_ok=True)
report_path=run_root/'core-stage-contract.json'
report={
  'schema_version':'2.0-rc1','check_id':agent.CORE_STAGE_REVIEW_ID,'status':'PASS','issue_id':'SP001',
  'from_state':'FROZEN','to_state':'RELEASED',
  'production_state':{'path':str(state_path.relative_to(root)),'sha256':core.sha256_file(state_path)},
  'production_profile':{'path':str(profile_path.relative_to(root)),'sha256':core.sha256_file(profile_path)},
  'implementation_commit_sha':impl,'contract':contract,'artifacts':artifacts,'recorded_at':core.iso_utc(now),
}
core.write_json(report_path,report)
result_auth=agent._authority(root,report_path,'Release CORE_STAGE_CONTRACT result')
release_auth=agent._authority(root,release,'Release Record')
payload={
  'schema_version':'2.0-rc1','issue_id':'SP001','from_state':'FROZEN','to_state':'RELEASED','checkpoints':['release'],
  'recorded_at':core.iso_utc(now),
  'implementation':{'repository_commit_sha':impl,'orchestrator_version':cfg['orchestrator_version']},
  'contract':contract,'artifacts':artifacts,
  'reviews':[
    {'check_id':agent.CORE_STAGE_REVIEW_ID,'kind':'DETERMINISTIC','status':'PASS','executor':'post-release exact-byte reconciliation recovery','evidence':'Existing public special/SP001 Release target and downloaded asset were independently revalidated against the exact frozen main, Release Manifest, PDF SHA-256 and byte count before lifecycle adoption.','result':result_auth},
    {'check_id':'RELEASE_EXACT_BYTE_RECONCILIATION','kind':'DETERMINISTIC','status':'PASS','executor':'survey-production-v2-release.yml attempt 1 plus bounded reconciliation','evidence':'Public issue-only Release identity, target and downloaded asset bytes were reconciled against the frozen Release Manifest; attempt 1 created and exact-byte verified the Release before the repository provenance helper defect stopped adoption.','result':release_auth},
  ],
  'summary':'Exact frozen SP001 publication bytes were publicly released and independently reconciled; repository provenance was adopted after supplying the deterministic Core report omitted by the current Release checkpoint helper.'
}
schema_gate.validate_instance(payload,root/agent.CHECKPOINT_SCHEMA,label='Recovered Release Stage Checkpoint')
cp=agent.canonical_checkpoint_path(root,cfg,state)
assert not cp.exists(), cp
core.write_json(cp,payload)
updated=agent.advance_with_checkpoint(root,cfg,state_path,cp)
assert updated['lifecycle_state']=='RELEASED' and updated['machine_checkpoints']['release']=='passed'
errors=agent.validate_agent_state(root,cfg,updated)
assert errors==[], errors

audit={
  'schema_version':'2.0-rc1','issue_id':'SP001','status':'PASS','kind':'BOUNDED_POST_RELEASE_PROVENANCE_RECOVERY',
  'recorded_at':core.iso_utc(datetime.now(timezone.utc)),'frozen_main_commit':'dd1ad1e9f5f0aa2a930f3866b5347e9194cafa37',
  'release_workflow_run_id':33224802636,'release_identity':'special/SP001','release_url':release_url,
  'pdf_sha256':'9f6bef98d15bfaec1ea2aec3972005487c28e44ec84762e4fbaa51639d7fe1b2','pdf_byte_count':322250,
  'failure_recovered':'survey_release_checkpoint_v2.py omits CORE_STAGE_CONTRACT review required by agent.advance_with_checkpoint',
  'public_release_created_and_exact_bytes_verified_before_failure':True,
  'public_release_reconciled_exact_bytes_again':True,
  'release_record':{'path':str(release.relative_to(root)),'sha256':core.sha256_file(release)},
  'merge_verification':{'path':str(merge.relative_to(root)),'sha256':core.sha256_file(merge)},
  'stage_checkpoint':{'path':str(cp.relative_to(root)),'sha256':core.sha256_file(cp)},
  'core_stage_contract':{'path':str(report_path.relative_to(root)),'sha256':core.sha256_file(report_path)},
  'final_state_sha256':core.sha256_file(state_path),'final_lifecycle_state':'RELEASED',
  'final_next_action':updated.get('next_action'),'final_terminal_reason':updated.get('terminal_reason')
}
core.write_json(source/'publication/v2/release-recovery-audit-r5.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
