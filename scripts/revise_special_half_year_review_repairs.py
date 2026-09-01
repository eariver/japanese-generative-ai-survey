#!/usr/bin/env python3
"""Repair Half-year Special Publication Preview issues without mutating Evidence.

This immutable derived-source pass is intentionally limited to RETROSPECTIVE_PERIOD
editions. It adds the reusable half-year analysis layers established by H1, repairs
reader-facing taxonomy and source-specific Technical Notes text, removes redundant
final-synthesis card reprints from the publication flow, and compacts References.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import postprocess_special_reader_facing_notes as reader_notes
from scripts.render_article_draft_tex import tex_escape

_GENERIC_FALLBACKS = (
    '一次資料で確認できる公開・提供・機能・時系列上の事実を要約した項目',
    '提供元・プロジェクト・著者側の評価または説明として記録された項目',
    '一次資料と時系列から導いた編集上の整理。根拠となる事実と推論を区別して扱う',
)
_NOTE_RE = re.compile(r"\\begin\{technicalnote\}\{(.+?)\}\{.*?\\end\{technicalnote\}", re.DOTALL)
_ITEM_RE = re.compile(r"^\\item\s+(.+)$", re.MULTILINE)
_CITE_RE = re.compile(r"\\(?:auto)?cite\{([^}]+)\}")
_COMMON_REF_NOTE_RE = re.compile(
    r"^\s*note\s*=\s*\{Primary source used for chronology and technical verification\}\s*,?\s*$",
    re.MULTILINE,
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError(f'{path}: expected object')
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_analysis(repo_root: Path, issue_id: str, changes: dict[str, Any], references: str) -> tuple[Path, Path, dict[str, Any]]:
    artifact_rel = str(changes.get('half_year_analysis_artifact_path') or '')
    tex_rel = str(changes.get('half_year_analysis_source_path') or '')
    if not artifact_rel or not tex_rel:
        raise ValueError('half-year analysis artifact/source paths are required')
    artifact_path = repo_root / artifact_rel
    tex_path = repo_root / tex_rel
    if not artifact_path.is_file() or not tex_path.is_file():
        raise ValueError('half-year analysis artifact/source missing')
    artifact = load_json(artifact_path)
    if artifact.get('issue_id') != issue_id:
        raise ValueError('half-year analysis issue mismatch')
    if artifact.get('selected_evidence_only') is not True or artifact.get('new_external_evidence') is not False:
        raise ValueError('half-year analysis must remain selected-Evidence-only')
    required = {'HALF_YEAR_RECLASSIFICATION', 'CROSS_MONTH_COMPARISON', 'CROSS_LAYER_SYNTHESIS'}
    layers = {str(x) for x in artifact.get('analysis_layers') or []}
    if not required.issubset(layers):
        raise ValueError(f'half-year analysis layers missing: {sorted(required-layers)}')
    if str(artifact.get('tex_path') or '') != tex_rel or str(artifact.get('tex_sha256') or '') != sha(tex_path):
        raise ValueError('half-year analysis TeX binding mismatch')
    tex = tex_path.read_text(encoding='utf-8')
    for heading in ('半年単位で再分類する', 'Cross-month Comparison', 'Cross-layer Synthesis'):
        if heading not in tex:
            raise ValueError(f'half-year analysis heading missing: {heading}')
    keys: set[str] = set()
    for match in _CITE_RE.finditer(tex):
        keys.update(k.strip() for k in match.group(1).split(',') if k.strip())
    if not keys:
        raise ValueError('half-year analysis must cite selected Evidence')
    missing = sorted(k for k in keys if ('{' + k + ',') not in references)
    if missing:
        raise ValueError(f'half-year analysis cites missing References keys: {missing}')
    return artifact_path, tex_path, artifact


def load_note_repairs(repo_root: Path, issue_id: str, changes: dict[str, Any]) -> tuple[Path, dict[str, list[dict[str, str]]]]:
    rel = str(changes.get('technical_notes_repair_path') or '')
    if not rel:
        raise ValueError('technical_notes_repair_path is required')
    path = repo_root / rel
    data = load_json(path)
    if data.get('issue_id') != issue_id or data.get('selected_evidence_only') is not True:
        raise ValueError('Technical Notes repair artifact mismatch')
    records: dict[str, list[dict[str, str]]] = {}
    for record in data.get('records') or []:
        title = str(record.get('artifact_name') or '')
        items = record.get('items') or []
        if not title or not isinstance(items, list) or not items:
            raise ValueError('Technical Notes repair record malformed')
        prepared: list[dict[str, str]] = []
        for item in items:
            label = str(item.get('label') or '')
            text = str(item.get('text_ja') or '').strip()
            if not label or not text:
                raise ValueError(f'empty Technical Notes repair item: {title}')
            prepared.append({'label': label, 'text_ja': text})
        records[title] = prepared
    if not records:
        raise ValueError('Technical Notes repair artifact has no records')
    return path, records


def replace_generic_items(block: str, title: str, replacements: dict[str, list[dict[str, str]]]) -> tuple[str, int]:
    generic_lines = [line for line in block.splitlines() if line.startswith(r'\item ') and any(p in line for p in _GENERIC_FALLBACKS)]
    if not generic_lines:
        return block, 0
    items = replacements.get(title)
    if items is None:
        raise ValueError(f'generic Technical Notes fallback has no reviewed replacement: {title}')
    if len(items) != len(generic_lines):
        raise ValueError(f'Technical Notes replacement count mismatch for {title}: {len(generic_lines)} != {len(items)}')
    revised = block
    for old, item in zip(generic_lines, items):
        new = r'\item \textbf{' + tex_escape(item['label']) + '}: ' + tex_escape(item['text_ja'])
        if revised.count(old) != 1:
            raise ValueError(f'expected one fallback bullet in {title}')
        revised = revised.replace(old, new, 1)
    return revised, len(items)


def validate_note_text(text: str, rel: str) -> tuple[int, int]:
    fallback_count = sum(text.count(p) for p in _GENERIC_FALLBACKS)
    taxonomy = reader_notes.reader_taxonomy_findings(text)
    if fallback_count:
        raise ValueError(f'{rel}: generic Technical Notes fallback remains: {fallback_count}')
    if taxonomy:
        raise ValueError(f'{rel}: reader taxonomy leak remains: {taxonomy}')
    duplicate_count = 0
    for match in _NOTE_RE.finditer(text):
        seen: set[str] = set()
        duplicate: set[str] = set()
        for item in _ITEM_RE.findall(match.group(0)):
            normalized = re.sub(r'\s+', ' ', item).strip()
            if normalized in seen:
                duplicate.add(normalized)
            seen.add(normalized)
        if duplicate:
            duplicate_count += len(duplicate)
            raise ValueError(f'{rel}: duplicate Technical Notes bullet: {sorted(duplicate)}')
    return fallback_count, duplicate_count


def repair_note(path: Path, replacements: dict[str, list[dict[str, str]]]) -> tuple[int, int]:
    original = path.read_text(encoding='utf-8')
    text = reader_notes.translate_machine_labels_compat(original)
    blocks = list(_NOTE_RE.finditer(text))
    changes: list[tuple[int, int, str]] = []
    replaced = 0
    for match in blocks:
        block = match.group(0)
        title = match.group(1)
        revised, count = replace_generic_items(block, title, replacements)
        if revised != block:
            changes.append((match.start(), match.end(), revised))
            replaced += count
    for start, end, revised in reversed(changes):
        text = text[:start] + revised + text[end:]
    validate_note_text(text, path.name)
    if text != original:
        path.write_text(text, encoding='utf-8')
    return replaced, len(changes)


def compact_references(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    revised, count = _COMMON_REF_NOTE_RE.subn('', text)
    revised = re.sub(r'\n{3,}', '\n\n', revised)
    if count < 1:
        raise ValueError('expected repeated References boilerplate was not found')
    if 'Primary source used for chronology and technical verification' in revised:
        raise ValueError('References boilerplate remains after compaction')
    path.write_text(revised, encoding='utf-8')
    return count


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    edition = load_json(repo_root / 'specials' / special_slug / 'edition.json')
    if edition.get('special_id') != issue_id or edition.get('edition_kind') != 'RETROSPECTIVE_PERIOD':
        raise ValueError('half-year review repair is only valid for RETROSPECTIVE_PERIOD')
    budget = edition.get('page_budget') or {}
    soft_target, hard_max = int(budget['target']), int(budget['max'])

    marker_path = repo_root / 'sources' / issue_id / 'editorial' / f'layout-revision-{source_version}.json'
    marker = load_json(marker_path)
    if marker.get('issue_id') != issue_id or marker.get('revision') != source_version:
        raise ValueError('half-year review marker mismatch')
    changes = marker.get('layout_changes') or {}
    if changes.get('half_year_review_repairs') is not True:
        raise ValueError('marker does not request half_year_review_repairs')
    constraints = marker.get('constraints') or {}
    if constraints.get('new_external_evidence_allowed') is not False or constraints.get('selected_evidence_only') is not True:
        raise ValueError('repair must be selected-Evidence-only with no new external Evidence')
    if constraints.get('accepted_article_claims_changed') is not False or constraints.get('evidence_cards_mutated') is not False:
        raise ValueError('repair must preserve accepted articles and Evidence cards')

    state_path = repo_root / 'sources' / issue_id / 'pipeline-state.json'
    state = load_json(state_path)
    gates = state.get('gates') or {}
    if state.get('lifecycle_state') != 'RELEASE_CANDIDATE' or gates.get('latex_build') != 'passed':
        raise ValueError('half-year review repair requires built RELEASE_CANDIDATE')
    if gates.get('visual_review') != 'pending' or gates.get('freeze') != 'pending':
        raise ValueError('Visual Review and Freeze must remain pending')

    current = deepcopy((state.get('provenance') or {}).get('validated_issue_source') or {})
    manifest_path = repo_root / str(current.get('path') or '')
    if not manifest_path.is_file() or sha(manifest_path) != current.get('sha256'):
        raise ValueError('current validated source digest mismatch')
    current_manifest = load_json(manifest_path)
    current_dir = manifest_path.parent
    out = repo_root / 'surveys' / 'special' / special_slug / 'revisions' / source_version
    if out.exists():
        raise ValueError(f'source revision already exists: {out}')
    shutil.copytree(current_dir, out)

    new_manifest = deepcopy(current_manifest)
    refs_rel = str((new_manifest.get('references') or {}).get('path') or 'references.bib')
    refs_path = out / refs_rel
    refs_before = refs_path.read_text(encoding='utf-8')
    analysis_artifact_path, analysis_source_path, analysis_artifact = validate_analysis(
        repo_root, issue_id, changes, refs_before
    )
    notes_artifact_path, note_replacements = load_note_repairs(repo_root, issue_id, changes)

    note_replacement_count = 0
    note_files_changed = 0
    for article in new_manifest.get('articles') or []:
        rel = str(article.get('technical_notes_path') or '')
        if not rel:
            continue
        path = out / rel
        before = sha(path)
        replaced, _ = repair_note(path, note_replacements)
        note_replacement_count += replaced
        if sha(path) != before:
            note_files_changed += 1
        article['technical_notes_sha256'] = sha(path)
        article['technical_notes_reader_facing'] = str(article.get('package_id')) != 'synth'

    removed_ref_notes = compact_references(refs_path)
    new_manifest['references'] = {'path': refs_rel, 'sha256': sha(refs_path)}

    analysis_dir = out / 'half-year-analysis'
    analysis_dir.mkdir(parents=True, exist_ok=True)
    analysis_target = analysis_dir / '80-half-year-analysis.tex'
    shutil.copyfile(analysis_source_path, analysis_target)

    main_rel = str((new_manifest.get('main_tex') or {}).get('path') or 'main.tex')
    main_path = out / main_rel
    main_text = main_path.read_text(encoding='utf-8')
    redundant = r'\input{theme-synthesis/07-synth-synthesis}' + '\n' + r'\medskip' + '\n' + r'\input{technical-notes/70-synth-notes}'
    if redundant not in main_text:
        raise ValueError('expected final-synthesis Technical Notes input was not found')
    main_text = main_text.replace(redundant, r'\input{theme-synthesis/07-synth-synthesis}', 1)
    if r'\input{technical-notes/70-synth-notes}' in main_text:
        raise ValueError('redundant final-synthesis Technical Notes input remains')

    half_year_heading = r'\section{Half-year Synthesis — 進歩の単位はModelからExecution Stackへ}'
    if main_text.count(half_year_heading) != 1:
        raise ValueError('expected one Half-year Synthesis section')
    insertion = (
        r'\Needspace{0.40\textheight}' + '\n' + r'\bigskip' + '\n'
        + r'\input{half-year-analysis/80-half-year-analysis}' + '\n\n'
        + r'\Needspace{0.40\textheight}' + '\n' + r'\bigskip' + '\n'
        + half_year_heading
    )
    main_text = main_text.replace(
        r'\Needspace{0.45\textheight}' + '\n' + r'\bigskip' + '\n' + half_year_heading,
        insertion,
        1,
    )
    if r'\input{half-year-analysis/80-half-year-analysis}' not in main_text:
        raise ValueError('half-year analysis insertion failed')

    bib = r'\printbibliography[title={References / Source Notes}]'
    if main_text.count(bib) != 1:
        raise ValueError('expected one bibliography command')
    common_note = (
        r'\noindent{\small\textit{以下の一次資料は本号の年表と技術的確認に使用した。資料名、組織、URL、参照日は各entryに示す。}}\par'
        + '\n' + r'\smallskip' + '\n' + bib
    )
    main_text = main_text.replace(bib, common_note, 1)
    main_path.write_text(main_text, encoding='utf-8')

    new_manifest['source_version'] = source_version
    new_manifest['status'] = 'VALIDATED_HALF_YEAR_REVIEW_REPAIR_REVISION'
    new_manifest['derivation'] = (
        'Publication Preview repair for Half-year Special issues #128, #54, #139, and #140. '
        'Accepted Article Drafts and Evidence cards remain immutable; the derived reader-facing source adds '
        'half-year reclassification/cross-month/cross-layer analysis, source-specific Technical Notes, and compact References.'
    )
    new_manifest['basis'] = dict(current_manifest.get('basis') or {})
    new_manifest['basis']['previous_source_manifest_path'] = current['path']
    new_manifest['basis']['previous_source_manifest_sha256'] = current['sha256']
    new_manifest['basis']['half_year_analysis_artifact_path'] = analysis_artifact_path.relative_to(repo_root).as_posix()
    new_manifest['basis']['half_year_analysis_artifact_sha256'] = sha(analysis_artifact_path)
    new_manifest['basis']['technical_notes_repair_artifact_path'] = notes_artifact_path.relative_to(repo_root).as_posix()
    new_manifest['basis']['technical_notes_repair_artifact_sha256'] = sha(notes_artifact_path)
    new_manifest['main_tex'] = {'path': main_rel, 'sha256': sha(main_path)}
    new_manifest['half_year_analysis'] = {
        'path': analysis_target.relative_to(out).as_posix(),
        'sha256': sha(analysis_target),
        'structured_source_path': analysis_artifact_path.relative_to(repo_root).as_posix(),
        'structured_source_sha256': sha(analysis_artifact_path),
        'analysis_layers': analysis_artifact['analysis_layers'],
        'selected_evidence_only': True,
        'new_external_evidence': False,
    }
    layout = dict(new_manifest.get('layout') or {})
    layout['half_year_analysis_policy'] = 'independent reclassification + cross-month comparison + cross-layer synthesis before final Half-year Synthesis'
    layout['final_synthesis_technical_notes_policy'] = 'provenance retained but redundant card reprint omitted from publication flow'
    layout['references_policy'] = 'common verification purpose stated once before bibliography; entry-specific identity metadata retained'
    layout['page_count_policy'] = f'{soft_target}-page soft editorial target; {hard_max}-page hard ceiling from edition manifest; no padding solely to meet soft target'
    new_manifest['layout'] = layout
    reader = dict(new_manifest.get('reader_facing_technical_notes') or {})
    reader.update({
        'machine_enum_policy': 'reader-facing-labels-v7-no-generic-event-fallback',
        'generic_fallback_policy': 'forbidden-fail-closed',
        'generic_fallback_findings': 0,
        'duplicate_bullet_findings': 0,
        'source_specific_replacement_count': note_replacement_count,
    })
    new_manifest['reader_facing_technical_notes'] = reader
    new_manifest['layout_revision'] = {
        'from_source_version': current_manifest.get('source_version'),
        'half_year_review_repairs': True,
        'issue_refs': [int(x) for x in marker.get('review_issues') or []],
        'reader_content_changed': True,
        'reader_content_change_scope': 'selected-Evidence half-year synthesis plus reader-facing Technical Notes/References presentation',
        'new_external_evidence': False,
        'accepted_article_sections_changed': False,
        'evidence_cards_changed': False,
        'half_year_analysis_layers_added': analysis_artifact['analysis_layers'],
        'final_synthesis_technical_notes_included': False,
        'technical_notes_files_changed': note_files_changed,
        'technical_notes_source_specific_replacement_count': note_replacement_count,
        'references_common_note_removed_count': removed_ref_notes,
        'references_common_note_consolidated': True,
        'page_target_soft': soft_target,
        'page_target_hard_max': hard_max,
        'page_budget_source': f'specials/{special_slug}/edition.json',
    }
    new_manifest_path = out / 'source-manifest.json'
    write_json(new_manifest_path, new_manifest)
    manifest_sha = sha(new_manifest_path)

    history = state.setdefault('provenance_history', {})
    history.setdefault('validated_issue_source', []).append(current)
    previous_build = deepcopy((state.get('provenance') or {}).get('latex_build') or {})
    if previous_build:
        history.setdefault('latex_build', []).append(previous_build)
    state['lifecycle_state'] = 'VALIDATED_DRAFT'
    state['gates']['latex_build'] = 'pending'
    state['gates']['visual_review'] = 'pending'
    state['gates']['freeze'] = 'pending'
    state['provenance']['validated_issue_source'] = {
        'path': new_manifest_path.relative_to(repo_root).as_posix(),
        'sha256': manifest_sha,
        'source_version': source_version,
        'layout_mode': str(layout.get('body_mode') or current.get('layout_mode') or 'mixed'),
        'layout_revision_sha256': sha(marker_path),
    }
    state['provenance'].pop('latex_build', None)
    state['provenance']['reader_layout_revision'] = {
        'source_version': source_version,
        'layout_revision_path': marker_path.relative_to(repo_root).as_posix(),
        'layout_revision_sha256': sha(marker_path),
        'reason': str(marker.get('reason') or 'Apply Half-year Publication Preview issue repairs.'),
    }
    write_json(state_path, state)

    return {
        'schema_version': '1.0', 'issue_id': issue_id, 'special_slug': special_slug,
        'source_version': source_version, 'previous_source_version': current_manifest.get('source_version'),
        'source_manifest': new_manifest_path.relative_to(repo_root).as_posix(),
        'source_manifest_sha256': manifest_sha,
        'issue_refs': new_manifest['layout_revision']['issue_refs'],
        'half_year_analysis_layers': analysis_artifact['analysis_layers'],
        'technical_notes_source_specific_replacement_count': note_replacement_count,
        'references_common_note_removed_count': removed_ref_notes,
        'page_target_soft': soft_target, 'page_target_hard_max': hard_max,
        'new_external_evidence': False, 'lifecycle_state': state['lifecycle_state'],
        'latex_build_gate': state['gates']['latex_build'], 'visual_review_gate': state['gates']['visual_review'],
        'freeze_gate': state['gates']['freeze'],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', default='.')
    parser.add_argument('--special-slug', required=True)
    parser.add_argument('--issue-id', required=True)
    parser.add_argument('--source-version', required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
