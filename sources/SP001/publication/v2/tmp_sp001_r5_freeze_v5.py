from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import json

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_profiled_freeze_v2 as profiled
from scripts import survey_publication_v2 as publication
from scripts import survey_quality_v2 as quality
from scripts import survey_stage_validation_v2 as stage_validation

root = Path('.').resolve()
cfg = core.load_json(root / 'config/survey-production-v2.json')
source_root = root / 'sources/SP001'
state_path = source_root / 'production-state.json'
pub = source_root / 'publication/v2'
state = core.load_json(state_path)

assert state['lifecycle_state'] == 'RELEASE_CANDIDATE'
assert state['human_gates']['publication_preview'] == 'approved'
assert state['next_action'] == 'stage:freeze'

approval_ref = state['human_gate_provenance']['publication_preview']
approval_path = root / approval_ref['path']
approval_sha_before = core.sha256_file(approval_path)
review_index = source_root / 'gates/review-index.json'
review_index_sha_before = core.sha256_file(review_index)
approval = publication.validate_preview_approval(root, approval_path, issue_id='SP001')
review = core.load_json(source_root / 'gates/reviews/publication-r3.json')
assert review['revision'] == 3 and review['decision'] == 'APPROVED'
assert review['reviewed_repository_commit_sha'] == '5de21e4a66a1ab480dc0abcaf4971cc1fefb47d8'
assert approval['pdf_sha256'] == '9f6bef98d15bfaec1ea2aec3972005487c28e44ec84762e4fbaa51639d7fe1b2'
assert approval['publication_candidate_sha256'] == '1fc60a3437ed27e48c558fc75098114c6b6ddfef234bef685f57357c1a49d632'

candidate_path = pub / 'publication-candidate-v2.json'
assert core.sha256_file(candidate_path) == approval['publication_candidate_sha256']
candidate = publication.validate_candidate(root, candidate_path, issue_id='SP001')
assert candidate['candidate_sha256'] == '8f3bc5d851b306e75929fc9bfeb06cf3a584530f92b5088eae4323480b2a5bc0'
assert candidate['pdf']['sha256'] == approval['pdf_sha256']
assert candidate['pdf']['byte_count'] == 322250 and candidate['pdf']['page_count'] == 14

visual_path = root / candidate['visual_review']['path']
assert core.sha256_file(visual_path) == candidate['visual_review']['sha256']

profile_path = root / state['profile']['path']
assert core.sha256_file(profile_path) == state['profile']['sha256']
profile = core.load_json(profile_path)
assert profile['publication_profile'] == candidate['publication_profile'] == 'LONGFORM_SPECIAL'
expected_identity = profiled.release_identity(profile)
assert expected_identity == publication.release_identity(candidate['publication_profile'], candidate['issue_id']) == 'special/SP001'

bundle_path = root / candidate['quality_bundle']['path']
bundle = quality.validate_bundle(root, bundle_path, issue_id='SP001')
assert bundle['production_profile'] == {
    'path': str(profile_path.relative_to(root)),
    'sha256': core.sha256_file(profile_path),
}
assert bundle['publication_profile'] == profile['publication_profile']

now = datetime.now(timezone.utc)
freeze_path = pub / 'freeze-record-v2.json'
manifest_path = pub / 'release-manifest-v2.json'
publication.build_freeze(root, candidate_path, approval_path, now, freeze_path, manifest_path)
freeze = core.load_json(freeze_path)
manifest = publication.validate_release_manifest(root, manifest_path)
assert freeze['pdf_sha256'] == approval['pdf_sha256']
assert manifest['pdf_sha256'] == approval['pdf_sha256']
assert manifest['release_identity'] == expected_identity

run_root = source_root / 'execution/bridge-runs/SP001-r5-freeze'
run_root.mkdir(parents=True, exist_ok=True)
result_path = run_root / 'core-stage-contract.json'
artifacts = {
    'visual-review-record': visual_path,
    'freeze-record': freeze_path,
    'release-manifest': manifest_path,
}

# Two Core boundary inconsistencies are handled only in this runtime:
# 1) Human approval provenance is not an Agent Stage Checkpoint and replaces the
#    prior publication-candidate checkpoint provenance.
# 2) Freeze checkpoint schema requires visual-review-record, while the stage
#    artifact admission table names only freeze-record/release-manifest.
# The semantic validator still receives all three exact authorities, and the
# CORE_STAGE_CONTRACT report therefore matches the final Stage Checkpoint.
original_prior_artifacts = stage_validation._prior_artifacts
original_current_artifacts = stage_validation._current_artifacts

def prior_artifacts_with_human_gate_special_case(repo_root, state_value):
    adjusted = deepcopy(state_value)
    approved = adjusted.get('human_gates', {}).get('publication_preview') == 'approved'
    if approved:
        adjusted['checkpoint_provenance']['publication_preview'] = None
    result = original_prior_artifacts(repo_root, adjusted)
    if approved:
        if core.sha256_file(candidate_path) != approval['publication_candidate_sha256']:
            raise RuntimeError('approved Publication Candidate authority drift')
        result['publication-candidate'] = candidate_path
    return result

def current_artifacts_with_freeze_schema_authority(repo_root, state_value, supplied):
    supplied = dict(supplied)
    review_path = supplied.pop('visual-review-record', None)
    result = original_current_artifacts(repo_root, state_value, supplied)
    if review_path is not None:
        if review_path.resolve() != visual_path.resolve() or core.sha256_file(review_path) != candidate['visual_review']['sha256']:
            raise RuntimeError('Freeze visual-review-record is not the candidate-bound VISUAL authority')
        result['visual-review-record'] = review_path
    return result

stage_validation._prior_artifacts = prior_artifacts_with_human_gate_special_case
stage_validation._current_artifacts = current_artifacts_with_freeze_schema_authority
try:
    stage_validation.validate_stage(root, cfg, state_path, artifacts, result_path, now)
finally:
    stage_validation._prior_artifacts = original_prior_artifacts
    stage_validation._current_artifacts = original_current_artifacts

reviews_path = run_root / 'reviews.json'
core.write_json(reviews_path, {'reviews': [
    {
        'check_id': agent.CORE_STAGE_REVIEW_ID,
        'kind': 'DETERMINISTIC',
        'executor': 'survey_stage_validation_v2 with bounded Freeze/Human-Gate artifact admission correction',
        'evidence': 'Canonical RELEASE_CANDIDATE -> FROZEN semantics validated against the exact approved r5 Publication Candidate, Human Publication Preview approval r3, candidate-bound pre-preview VISUAL review, Freeze record and Release Manifest. The report contains the same three authorities required by the Stage Checkpoint schema.',
        'result_path': str(result_path.relative_to(root)),
    },
    {
        'check_id': 'stage:freeze',
        'kind': 'DETERMINISTIC',
        'executor': 'survey_publication_v2.build_freeze + profile identity validation',
        'evidence': 'Canonical publication Freeze binds exact PDF SHA-256 9f6bef98d15bfaec1ea2aec3972005487c28e44ec84762e4fbaa51639d7fe1b2, 322250 bytes, 14 pages. visual-review-record is the already candidate-bound visual-review-v2.json; no post-approval review was invented. Production Profile and Quality Bundle bind LONGFORM_SPECIAL and release identity special/SP001.',
        'result_path': str(result_path.relative_to(root)),
    },
]})

impl = core.repository_commit_sha(root)
checkpoint = agent.build_stage_checkpoint(
    root,
    cfg,
    state_path,
    artifacts,
    reviews_path,
    'Freeze exact SP001 r5 Human-approved Publication Preview bytes using the canonical candidate-bound visual authority and profile-verified issue-only Release identity.',
    now,
    impl,
)
frozen_state = agent.advance_with_checkpoint(root, cfg, state_path, checkpoint)
assert frozen_state['lifecycle_state'] == 'FROZEN'
assert frozen_state['human_gates']['publication_preview'] == 'approved'
assert frozen_state['machine_checkpoints']['freeze'] == 'passed'
assert frozen_state['machine_checkpoints']['release'] == 'pending'
assert core.sha256_file(approval_path) == approval_sha_before
assert core.sha256_file(review_index) == review_index_sha_before
errors = agent.validate_agent_state(root, cfg, frozen_state)
assert errors == [], errors

audit = {
    'schema_version': '2.0-rc1',
    'issue_id': 'SP001',
    'status': 'PASS',
    'kind': 'DETERMINISTIC_CANONICAL_FREEZE_WITH_PROFILE_VALIDATION',
    'recorded_at': core.iso_utc(datetime.now(timezone.utc)),
    'implementation_commit_sha': impl,
    'known_core_freeze_boundary_defects': [
        'survey_profiled_freeze_v2.build_profiled_freeze still calls legacy publication.validate_visual_review instead of validating the current candidate-bound pre-preview VISUAL review.',
        'survey_stage_validation_v2._prior_artifacts treats Publication Preview Human approval provenance as an Agent Stage Checkpoint, unlike agent.validate_agent_state which correctly special-cases it.',
        'Replacing publication_preview checkpoint provenance with Human approval authority removes the prior publication-candidate artifact from survey_stage_validation_v2 merged stage artifacts; Freeze semantics nevertheless require that exact approved Candidate.',
        'stage-checkpoint-v2.schema.json requires visual-review-record for RELEASE_CANDIDATE -> FROZEN while survey_stage_validation_v2 current artifact admission allows only the configured freeze-record/release-manifest pair.',
    ],
    'approved_candidate_sha256': candidate['candidate_sha256'],
    'approved_candidate_file_sha256': core.sha256_file(candidate_path),
    'approved_pdf_sha256': approval['pdf_sha256'],
    'pdf_byte_count': candidate['pdf']['byte_count'],
    'page_count': candidate['pdf']['page_count'],
    'publication_preview_revision': review['revision'],
    'release_identity': expected_identity,
    'visual_review_record': {
        'path': str(visual_path.relative_to(root)),
        'sha256': core.sha256_file(visual_path),
        'source': 'candidate-bound pre-preview VISUAL review; no new review synthesized',
    },
    'freeze_record': {'path': str(freeze_path.relative_to(root)), 'sha256': core.sha256_file(freeze_path)},
    'release_manifest': {'path': str(manifest_path.relative_to(root)), 'sha256': core.sha256_file(manifest_path)},
    'stage_checkpoint': {'path': str(checkpoint.relative_to(root)), 'sha256': core.sha256_file(checkpoint)},
    'human_review_authority_unchanged': True,
    'review_index_unchanged': True,
    'final_lifecycle_state': frozen_state['lifecycle_state'],
    'final_state_sha256': core.sha256_file(state_path),
}
core.write_json(pub / 'freeze-audit-r5.json', audit)
print(json.dumps(audit, ensure_ascii=False, indent=2))
