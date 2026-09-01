#!/usr/bin/env python3
"""Repair Half-year Publication Preview regressions with Evidence-derived presentation data.

This immutable derived-source pass addresses the common Half-year review contract:
- source-specific Technical Notes facts derived only from selected structured Evidence;
- source-semantic reader taxonomy without treating all safety research as incidents;
- URL/path/code identifiers preserved byte-for-byte and checked against Evidence/References;
- explicit half-year reclassification, cross-month comparison, and cross-layer synthesis;
- compact dated Detailed Chronology with item-level source mapping;
- common References boilerplate consolidated once.

Accepted Article Drafts and Evidence cards are never mutated.
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

from scripts import postprocess_special_reader_facing_notes_v2 as reader_notes
from scripts import revise_special_half_year_review_repairs as base
from scripts.render_article_draft_tex import tex_escape

NOTE_RE = re.compile(r"\\begin\{technicalnote\}\{(.+?)\}\{.*?\\end\{technicalnote\}", re.DOTALL)
URL_RE = re.compile(r"\\url\{([^}]*)\}")
GENERIC_FACT_MARKERS = (
    '一次資料で「',
    '数値や能力に関する評価は、提供元・プロジェクト・著者の主張として扱う',
)
GENERIC_LIMITATION = (
    '一次資料で確認できる範囲の事実を記録しており、'
    '提供元・プロジェクト・著者による評価を独立再現済みの結果として扱わない。'
)
COMMON_BOUNDARY = (
    r"\noindent{\small\textit{Technical Notesでは、一次資料から確認した公開・提供・研究上の事実を記載する。"
    r"数値・能力評価や提供元・著者による比較表現は、独立再現済みの結果ではなく帰属claimとして扱う。}}\par"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evidence_records(package: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for key in ('primary_evidence', 'supporting_evidence'):
        for record in package.get(key) or []:
            if isinstance(record, dict):
                records.append(record)
    return records


def merge_evidence_index(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Index selected Evidence by canonical artifact name from hash-pinned Draft Packages."""
    index: dict[str, dict[str, Any]] = {}
    for article in manifest.get('articles') or []:
        rel = str(article.get('draft_package_path') or '')
        if not rel:
            continue
        path = repo_root / rel
        if not path.is_file():
            raise ValueError(f'Draft Package missing: {path}')
        expected = str(article.get('draft_package_sha256') or '')
        if expected and sha(path) != expected:
            raise ValueError(f'Draft Package digest mismatch: {path}')
        package = base.load_json(path)
        for record in evidence_records(package):
            card = record.get('card') or {}
            artifact = card.get('artifact') or {}
            title = str(artifact.get('canonical_name') or '').strip()
            if not title:
                continue
            organization = str(artifact.get('organization') or '').strip()
            artifact_type = str(artifact.get('artifact_type') or '').strip()
            temporal = card.get('temporal') or {}
            events: list[tuple[str, str]] = []
            for event in temporal.get('events') or []:
                if not isinstance(event, dict):
                    continue
                date = str(event.get('event_date') or event.get('occurred_at') or '').strip()
                kind = str(event.get('event_type') or event.get('event_kind') or '').strip()
                if date:
                    events.append((date, kind))
            if not events:
                announced = str(temporal.get('artifact_first_announced') or '').strip()
                if announced:
                    events.append((announced, artifact_type or 'OFFICIAL_PUBLICATION'))
            urls = {
                str(source.get('url') or '').strip()
                for source in card.get('sources') or []
                if isinstance(source, dict) and str(source.get('url') or '').strip()
            }
            current = index.setdefault(
                title,
                {
                    'organization': organization,
                    'artifact_type': artifact_type,
                    'events': [],
                    'urls': set(),
                },
            )
            if organization and current['organization'] and current['organization'] != organization:
                raise ValueError(f'conflicting organizations for {title}')
            if organization:
                current['organization'] = organization
            if artifact_type:
                current['artifact_type'] = artifact_type
            for item in events:
                if item not in current['events']:
                    current['events'].append(item)
            current['urls'].update(urls)
    if not index:
        raise ValueError('selected Evidence index is empty')
    for value in index.values():
        value['events'] = sorted(value['events'])
        value['urls'] = sorted(value['urls'])
    return index


def event_label(kind: str) -> str:
    if not kind:
        return '公開・提供'
    rendered = reader_notes.readable_taxonomy_label(kind)
    return rendered.replace('（', '').replace('）', '')


def source_specific_fact(title: str, info: dict[str, Any]) -> str:
    organization = str(info.get('organization') or '提供元')
    events = list(info.get('events') or [])
    if not events:
        raise ValueError(f'no structured chronology available for Technical Notes fact: {title}')
    phrases = [f"{date}に{event_label(kind)}" for date, kind in events]
    chronology = '、'.join(phrases)
    return f"{organization}の一次資料により、{title}について{chronology}を確認した。"


def _replace_generic_fact(block: str, title: str, info: dict[str, Any]) -> tuple[str, int]:
    lines = block.splitlines()
    replaced = 0
    for i, line in enumerate(lines):
        if line.startswith(r'\item ') and all(marker in line for marker in GENERIC_FACT_MARKERS):
            lines[i] = (
                r'\item \textbf{一次情報で確認できる事実}: '
                + tex_escape(source_specific_fact(title, info))
            )
            replaced += 1
    if replaced > 1:
        raise ValueError(f'multiple generic primary-fact bullets in {title}: {replaced}')
    return '\n'.join(lines), replaced


def _remove_common_limitation(block: str) -> tuple[str, int]:
    pattern = re.compile(
        r"\{\\bfseries 読む際の境界\}\s*\n"
        r"\\begin\{itemize\}\[leftmargin=1\.5em,itemsep=0\.35em\]\s*\n"
        r"\\item \\textbf\{分析上の留意点\}: " + re.escape(GENERIC_LIMITATION) + r"\s*\n"
        r"\\end\{itemize\}\s*\n",
        re.MULTILINE,
    )
    return pattern.subn('', block, count=1)


def _add_common_boundary_once(text: str) -> str:
    if COMMON_BOUNDARY in text:
        return text
    anchor = '\n\\medskip\n'
    if anchor not in text:
        raise ValueError('Technical Notes intro anchor missing')
    return text.replace(anchor, '\n\\smallskip\n' + COMMON_BOUNDARY + '\n\\medskip\n', 1)


def repair_note_file(path: Path, evidence: dict[str, dict[str, Any]]) -> tuple[int, int, int]:
    original = path.read_text(encoding='utf-8')
    text = reader_notes.translate_machine_labels_compat(original)
    text = reader_notes.core.apply_type_overrides(text)
    text = _add_common_boundary_once(text)

    matches = list(NOTE_RE.finditer(text))
    changes: list[tuple[int, int, str]] = []
    fact_replacements = 0
    limitations_removed = 0
    checked_urls = 0
    for match in matches:
        block = match.group(0)
        title = match.group(1)
        info = evidence.get(title)
        if info is None:
            raise ValueError(f'Technical Notes title not bound to selected Evidence: {title}')
        revised, count = _replace_generic_fact(block, title, info)
        fact_replacements += count
        revised, removed = _remove_common_limitation(revised)
        limitations_removed += removed
        actual_urls = set(URL_RE.findall(revised))
        expected_urls = set(info.get('urls') or [])
        if actual_urls != expected_urls:
            raise ValueError(
                f'Technical Notes URL mismatch for {title}: actual={sorted(actual_urls)} expected={sorted(expected_urls)}'
            )
        checked_urls += len(actual_urls)
        if revised != block:
            changes.append((match.start(), match.end(), revised))
    for start, end, revised in reversed(changes):
        text = text[:start] + revised + text[end:]

    for phrase in base._GENERIC_FALLBACKS:
        if phrase in text:
            raise ValueError(f'{path.name}: legacy generic fallback remains: {phrase}')
    if '一次資料で「' in text and '数値や能力に関する評価は、提供元・プロジェクト・著者の主張として扱う' in text:
        raise ValueError(f'{path.name}: 2024-H2 generic source-title fallback remains')
    if GENERIC_LIMITATION in text:
        raise ValueError(f'{path.name}: repeated generic limitation remains')
    findings = reader_notes.reader_taxonomy_findings(text)
    if findings:
        raise ValueError(f'{path.name}: reader taxonomy leak remains: {findings}')
    if text != original:
        path.write_text(text, encoding='utf-8')
    return fact_replacements, limitations_removed, checked_urls


BIB_ENTRY_RE = re.compile(r"@\w+\{([^,]+),(.*?)\n\}", re.DOTALL)
BIB_URL_RE = re.compile(r"\n\s*url\s*=\s*\{([^}]*)\},")


def bibliography_keys_by_url(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for match in BIB_ENTRY_RE.finditer(text):
        key = match.group(1).strip()
        url_match = BIB_URL_RE.search(match.group(2))
        if not url_match:
            continue
        url = url_match.group(1).strip()
        existing = result.get(url)
        if existing is not None and existing != key:
            raise ValueError(f'duplicate bibliography URL with multiple keys: {url}')
        result[url] = key
    return result


def chronology_records(repo_root: Path, manifest: dict[str, Any], bib_by_url: dict[str, str]) -> tuple[list[dict[str, str]], dict[str, Any]]:
    chronology_article = next(
        (article for article in manifest.get('articles') or [] if str(article.get('package_id')) == 'chronology'),
        None,
    )
    if chronology_article is None:
        raise ValueError('chronology article missing from manifest')
    package_path = repo_root / str(chronology_article.get('draft_package_path') or '')
    package = base.load_json(package_path)
    records: list[dict[str, str]] = []
    for record in evidence_records(package):
        card = record.get('card') or {}
        artifact = card.get('artifact') or {}
        title = str(artifact.get('canonical_name') or '').strip()
        organization = str(artifact.get('organization') or '').strip()
        sources = [
            str(source.get('url') or '').strip()
            for source in card.get('sources') or []
            if isinstance(source, dict) and str(source.get('url') or '').strip()
        ]
        source_key = next((bib_by_url[url] for url in sources if url in bib_by_url), '')
        if not source_key:
            raise ValueError(f'chronology Evidence has no bibliography mapping: {title}')
        for event in (card.get('temporal') or {}).get('events') or []:
            if not isinstance(event, dict):
                continue
            date = str(event.get('event_date') or event.get('occurred_at') or '').strip()
            kind = str(event.get('event_type') or event.get('event_kind') or '').strip()
            if not date:
                continue
            records.append(
                {
                    'date': date,
                    'title': title,
                    'organization': organization,
                    'event_label': event_label(kind),
                    'bib_key': source_key,
                }
            )
    records.sort(key=lambda row: (row['date'], row['title'], row['event_label']))
    if not records:
        raise ValueError('chronology has no dated events')
    return records, chronology_article


def render_chronology(records: list[dict[str, str]]) -> str:
    lines = [
        r'\begin{itemize}[leftmargin=1.5em,itemsep=0.45em]',
    ]
    for row in records:
        event = f"{row['organization']}の一次資料で{row['event_label']}を確認。" if row['organization'] else f"一次資料で{row['event_label']}を確認。"
        lines.append(
            r'\item '
            + tex_escape(row['date'])
            + ' — '
            + r'\textbf{'
            + tex_escape(row['title'])
            + '}: '
            + tex_escape(event)
            + rf" \autocite{{{row['bib_key']}}}"
        )
    lines.append(r'\end{itemize}')
    lines.append('')
    lines.append(
        'preview、beta、GA、model release、API availability、research/publicationは別eventとして扱い、'
        '同じfamily名の後続更新へ吸収しない。上の各項目はevent dateとidentityを示す年表であり、'
        '性能比較やbenchmark上の優位を独立再現したことを意味しない。'
    )
    lines.append('')
    return '\n'.join(lines)


def remove_article_notes_input(main_text: str, technical_notes_path: str) -> str:
    rel = Path(technical_notes_path).with_suffix('').as_posix()
    needle = rf'\input{{{rel}}}'
    if needle not in main_text:
        raise ValueError(f'expected Technical Notes input not found: {needle}')
    main_text = main_text.replace(r'\medskip' + '\n' + needle + '\n', '', 1)
    if needle in main_text:
        raise ValueError(f'Technical Notes input remains after removal: {needle}')
    return main_text


def insert_half_year_analysis(main_text: str, analysis_rel: str) -> str:
    if rf'\input{{{analysis_rel}}}' in main_text:
        raise ValueError('half-year analysis already present')
    pattern = re.compile(
        r"(\\Needspace\{0\.45\\textheight\}\n\\bigskip\n)(\\section\{Half-year Synthesis[^\n]*\})"
    )
    match = pattern.search(main_text)
    if not match:
        raise ValueError('Half-year Synthesis insertion point not found')
    insertion = (
        r'\Needspace{0.35\textheight}' + '\n' + r'\bigskip' + '\n'
        + rf'\input{{{analysis_rel}}}' + '\n\n'
        + match.group(1) + match.group(2)
    )
    return main_text[:match.start()] + insertion + main_text[match.end():]


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    edition = base.load_json(repo_root / 'specials' / special_slug / 'edition.json')
    if edition.get('special_id') != issue_id or edition.get('edition_kind') != 'RETROSPECTIVE_PERIOD':
        raise ValueError('half-year review v3 requires RETROSPECTIVE_PERIOD')
    budget = edition.get('page_budget') or {}
    soft_target, hard_max = int(budget['target']), int(budget['max'])

    marker_path = repo_root / 'sources' / issue_id / 'editorial' / f'layout-revision-{source_version}.json'
    marker = base.load_json(marker_path)
    changes = marker.get('layout_changes') or {}
    if changes.get('half_year_review_repairs_v3') is not True:
        raise ValueError('marker does not request half_year_review_repairs_v3')
    constraints = marker.get('constraints') or {}
    if constraints.get('new_external_evidence_allowed') is not False or constraints.get('selected_evidence_only') is not True:
        raise ValueError('repair must be selected-Evidence-only with no new external Evidence')
    if constraints.get('accepted_article_claims_changed') is not False or constraints.get('evidence_cards_mutated') is not False:
        raise ValueError('repair must preserve accepted Article Drafts and Evidence cards')

    state_path = repo_root / 'sources' / issue_id / 'pipeline-state.json'
    state = base.load_json(state_path)
    gates = state.get('gates') or {}
    if state.get('lifecycle_state') != 'RELEASE_CANDIDATE' or gates.get('latex_build') != 'passed':
        raise ValueError('half-year review v3 requires built RELEASE_CANDIDATE')
    if gates.get('visual_review') != 'pending' or gates.get('freeze') != 'pending':
        raise ValueError('Visual Review and Freeze must remain pending')

    current = deepcopy((state.get('provenance') or {}).get('validated_issue_source') or {})
    manifest_path = repo_root / str(current.get('path') or '')
    if not manifest_path.is_file() or sha(manifest_path) != current.get('sha256'):
        raise ValueError('current validated source digest mismatch')
    current_manifest = base.load_json(manifest_path)
    out = repo_root / 'surveys' / 'special' / special_slug / 'revisions' / source_version
    if out.exists():
        raise ValueError(f'source revision already exists: {out}')
    shutil.copytree(manifest_path.parent, out)
    manifest = deepcopy(current_manifest)

    refs_rel = str((manifest.get('references') or {}).get('path') or 'references.bib')
    refs_path = out / refs_rel
    refs_before = refs_path.read_text(encoding='utf-8')
    bib_by_url = bibliography_keys_by_url(refs_before)

    analysis_artifact_path, analysis_source_path, analysis_artifact = base.validate_analysis(
        repo_root, issue_id, changes, refs_before
    )
    evidence = merge_evidence_index(repo_root, manifest)

    fact_replacements = 0
    limitations_removed = 0
    note_files_changed = 0
    url_checks = 0
    for article in manifest.get('articles') or []:
        rel = str(article.get('technical_notes_path') or '')
        if not rel:
            continue
        path = out / rel
        before = sha(path)
        facts, limitations, checked = repair_note_file(path, evidence)
        fact_replacements += facts
        limitations_removed += limitations
        url_checks += checked
        if sha(path) != before:
            note_files_changed += 1
        article['technical_notes_sha256'] = sha(path)
        article['technical_notes_reader_facing'] = str(article.get('package_id')) not in {'synthesis', 'chronology'}

    if fact_replacements < 1:
        raise ValueError('no generic 2024-H2 Technical Notes facts were replaced')
    if limitations_removed < 1:
        raise ValueError('no repeated 2024-H2 Technical Notes limitations were removed')

    chronology, chronology_article = chronology_records(repo_root, manifest, bib_by_url)
    chronology_body_rel = str(chronology_article.get('layout_body_path') or '')
    if not chronology_body_rel:
        raise ValueError('chronology layout body path missing')
    chronology_body_path = out / chronology_body_rel
    chronology_body_path.write_text(render_chronology(chronology), encoding='utf-8')
    chronology_article['layout_body_sha256'] = sha(chronology_body_path)
    chronology_article['chronology_source_mapping'] = 'compact dated event list with item-level bibliography citations'

    removed_ref_notes = base.compact_references(refs_path)
    manifest['references'] = {'path': refs_rel, 'sha256': sha(refs_path)}

    analysis_dir = out / 'half-year-analysis'
    analysis_dir.mkdir(parents=True, exist_ok=True)
    analysis_target = analysis_dir / '80-half-year-analysis.tex'
    shutil.copyfile(analysis_source_path, analysis_target)
    analysis_rel = analysis_target.relative_to(out).with_suffix('').as_posix()

    main_rel = str((manifest.get('main_tex') or {}).get('path') or 'main.tex')
    main_path = out / main_rel
    main_text = main_path.read_text(encoding='utf-8')
    synthesis_article = next(
        (article for article in manifest.get('articles') or [] if str(article.get('package_id')) in {'synth', 'synthesis'}),
        None,
    )
    if synthesis_article is None:
        raise ValueError('Half-year Synthesis article missing')
    main_text = remove_article_notes_input(main_text, str(synthesis_article.get('technical_notes_path') or ''))
    main_text = remove_article_notes_input(main_text, str(chronology_article.get('technical_notes_path') or ''))
    main_text = insert_half_year_analysis(main_text, analysis_rel)

    bib = r'\printbibliography[title={References / Source Notes}]'
    if main_text.count(bib) != 1:
        raise ValueError('expected one bibliography command')
    common_note = (
        r'\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。'
        r'各entryでは識別・追跡に必要な資料名、組織、URL、参照日を示す。}}\par'
        + '\n' + r'\smallskip' + '\n' + bib
    )
    main_text = main_text.replace(bib, common_note, 1)
    main_path.write_text(main_text, encoding='utf-8')

    manifest['source_version'] = source_version
    manifest['status'] = 'VALIDATED_HALF_YEAR_REVIEW_REPAIR_V3_REVISION'
    manifest['derivation'] = (
        'Publication Preview repair for Half-year issues #128, #139, #153, #140, #54, and #172. '
        'Selected Evidence and accepted Article Drafts remain immutable. Reader-facing Technical Notes are '
        'made source-specific from structured Evidence, opaque identifiers are preserved, half-year analysis '
        'is made explicit, chronology is compacted, and repeated References boilerplate is consolidated.'
    )
    manifest['basis'] = dict(current_manifest.get('basis') or {})
    manifest['basis']['previous_source_manifest_path'] = current['path']
    manifest['basis']['previous_source_manifest_sha256'] = current['sha256']
    manifest['basis']['half_year_analysis_artifact_path'] = analysis_artifact_path.relative_to(repo_root).as_posix()
    manifest['basis']['half_year_analysis_artifact_sha256'] = sha(analysis_artifact_path)
    manifest['main_tex'] = {'path': main_rel, 'sha256': sha(main_path)}
    manifest['half_year_analysis'] = {
        'path': analysis_target.relative_to(out).as_posix(),
        'sha256': sha(analysis_target),
        'structured_source_path': analysis_artifact_path.relative_to(repo_root).as_posix(),
        'structured_source_sha256': sha(analysis_artifact_path),
        'analysis_layers': analysis_artifact['analysis_layers'],
        'selected_evidence_only': True,
        'new_external_evidence': False,
    }
    layout = dict(manifest.get('layout') or {})
    layout['half_year_analysis_policy'] = 'independent half-year reclassification + cross-month comparison + cross-layer synthesis before final Half-year Synthesis'
    layout['chronology_policy'] = 'compact dated event list with item-level source mapping; no full Technical Notes appendix'
    layout['final_synthesis_technical_notes_policy'] = 'provenance retained; redundant reader-facing card reprint omitted'
    layout['references_policy'] = 'common purpose stated once; entry-specific identity metadata retained'
    layout['page_count_policy'] = f'{soft_target}-page soft target; {hard_max}-page hard ceiling; no padding to meet soft target'
    manifest['layout'] = layout
    reader = dict(manifest.get('reader_facing_technical_notes') or {})
    reader.update(
        {
            'machine_enum_policy': 'reader-facing-labels-v8-opaque-identifiers-preserved',
            'generic_fallback_policy': 'forbidden-fail-closed',
            'generic_fallback_findings': 0,
            'duplicate_bullet_findings': 0,
            'source_specific_replacement_count': fact_replacements,
            'common_limitation_removed_count': limitations_removed,
            'url_identity_checks': url_checks,
        }
    )
    manifest['reader_facing_technical_notes'] = reader
    manifest['layout_revision'] = {
        'from_source_version': current_manifest.get('source_version'),
        'half_year_review_repairs_v3': True,
        'issue_refs': [int(x) for x in marker.get('review_issues') or []],
        'reader_content_changed': True,
        'reader_content_change_scope': 'selected-Evidence reader-facing facts/analysis/chronology/reference presentation only',
        'new_external_evidence': False,
        'accepted_article_sections_changed': False,
        'evidence_cards_changed': False,
        'half_year_analysis_layers_added': analysis_artifact['analysis_layers'],
        'technical_notes_files_changed': note_files_changed,
        'technical_notes_source_specific_replacement_count': fact_replacements,
        'technical_notes_common_limitation_removed_count': limitations_removed,
        'technical_notes_url_identity_checks': url_checks,
        'semantic_taxonomy_overrides': sorted(reader_notes.core.TYPE_OVERRIDES),
        'final_synthesis_technical_notes_included': False,
        'chronology_technical_notes_included': False,
        'chronology_event_count': len(chronology),
        'chronology_item_level_source_mapping': True,
        'references_common_note_removed_count': removed_ref_notes,
        'references_common_note_consolidated': True,
        'page_target_soft': soft_target,
        'page_target_hard_max': hard_max,
    }
    new_manifest_path = out / 'source-manifest.json'
    base.write_json(new_manifest_path, manifest)
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
        'reason': str(marker.get('reason') or 'Apply Half-year Publication Preview regression repairs.'),
    }
    base.write_json(state_path, state)

    return {
        'schema_version': '1.0',
        'issue_id': issue_id,
        'special_slug': special_slug,
        'source_version': source_version,
        'previous_source_version': current_manifest.get('source_version'),
        'source_manifest': new_manifest_path.relative_to(repo_root).as_posix(),
        'source_manifest_sha256': manifest_sha,
        'issue_refs': manifest['layout_revision']['issue_refs'],
        'half_year_analysis_layers': analysis_artifact['analysis_layers'],
        'technical_notes_source_specific_replacement_count': fact_replacements,
        'technical_notes_common_limitation_removed_count': limitations_removed,
        'technical_notes_url_identity_checks': url_checks,
        'chronology_event_count': len(chronology),
        'references_common_note_removed_count': removed_ref_notes,
        'new_external_evidence': False,
        'lifecycle_state': state['lifecycle_state'],
        'latex_build_gate': state['gates']['latex_build'],
        'visual_review_gate': state['gates']['visual_review'],
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
