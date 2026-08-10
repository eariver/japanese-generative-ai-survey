#!/usr/bin/env python3
"""Materialize one validated structured Article Draft into LaTeX + BibTeX.

The LLM never chooses bibliography keys or emits citation commands. Evidence refs
are resolved back to Evidence Card source_ids and citations are generated
deterministically from canonical source URLs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import validate_article_draft as draft_validator


BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
CODE_RE = re.compile(r"`([^`]+)`")
URL_RE = re.compile(r"https?://[^\s<>]+")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def citation_key(url: str) -> str:
    return "src-" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:14]


def escape_tex_plain(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def escape_tex(text: str) -> str:
    """Escape prose and support minimal **bold**, `code`, and URL markup."""
    tokens: list[tuple[str, str]] = []

    def protect(kind: str, content: str) -> str:
        token = f"@@JGAI{len(tokens)}@@"
        tokens.append((kind, content))
        return token

    protected = URL_RE.sub(lambda m: protect("url", m.group(0)), text)
    protected = CODE_RE.sub(lambda m: protect("code", m.group(1)), protected)
    protected = BOLD_RE.sub(lambda m: protect("bold", m.group(1)), protected)
    escaped = escape_tex_plain(protected)
    for index, (kind, content) in enumerate(tokens):
        token = f"@@JGAI{index}@@"
        if kind == "url":
            replacement = r"\url{" + content.replace("%", r"\%") + "}"
        elif kind == "code":
            replacement = r"\texttt{" + escape_tex_plain(content) + "}"
        else:
            replacement = r"\textbf{" + escape_tex_plain(content) + "}"
        escaped = escaped.replace(token, replacement)
    return escaped


def evidence_cards(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    cards: dict[str, dict[str, Any]] = {}
    for field in ("primary_evidence", "supporting_evidence"):
        for item in package.get(field) or []:
            task_id = item["evidence_task_id"]
            if task_id in cards:
                raise ValueError(f"duplicate Evidence Task in Draft Package: {task_id}")
            cards[task_id] = item["card"]
    return cards


def evidence_object(card: dict[str, Any], kind: str, evidence_id: str) -> dict[str, Any]:
    if kind == "EVENT":
        values = card.get("temporal", {}).get("events") or []
        id_field = "event_id"
    elif kind == "CLAIM":
        values = card.get("claims") or []
        id_field = "claim_id"
    elif kind == "METRIC":
        values = card.get("metrics") or []
        id_field = "metric_id"
    elif kind == "LIMITATION":
        values = card.get("limitations") or []
        id_field = "limitation_id"
    else:
        raise ValueError(f"unsupported Evidence kind: {kind}")
    matches = [value for value in values if value.get(id_field) == evidence_id]
    if len(matches) != 1:
        raise ValueError(f"Evidence ref did not resolve uniquely: {kind}#{evidence_id}")
    return matches[0]


def source_index(cards: dict[str, dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}
    for task_id, card in cards.items():
        for source in card.get("sources") or []:
            source_id = source.get("source_id")
            if not isinstance(source_id, str) or not source_id:
                raise ValueError(f"Evidence Card source lacks source_id: {task_id}")
            result[(task_id, source_id)] = source
    return result


def sources_for_refs(
    refs: list[dict[str, Any]],
    cards: dict[str, dict[str, Any]],
    sources: dict[tuple[str, str], dict[str, Any]],
) -> list[dict[str, Any]]:
    resolved: dict[str, dict[str, Any]] = {}
    for ref in refs:
        task_id = ref["evidence_task_id"]
        card = cards[task_id]
        evidence = evidence_object(card, ref["kind"], ref["evidence_id"])
        for source_id in evidence.get("source_ids") or []:
            source = sources.get((task_id, source_id))
            if source is None:
                raise ValueError(f"Evidence source not found: {task_id}#{source_id}")
            url = source.get("url")
            if not isinstance(url, str) or not url:
                raise ValueError(f"Evidence source URL missing: {task_id}#{source_id}")
            existing = resolved.get(url)
            if existing is None:
                resolved[url] = source
            else:
                # A repeated URL must not silently disagree on its human title.
                if existing.get("title") != source.get("title"):
                    raise ValueError(f"same source URL has conflicting titles: {url}")
    return [resolved[url] for url in sorted(resolved)]


def cite_suffix(source_values: list[dict[str, Any]]) -> str:
    if not source_values:
        return ""
    keys = sorted({citation_key(source["url"]) for source in source_values})
    return r"\autocite{" + ",".join(keys) + "}"


def render_text_with_cite(text: str, refs: list[dict[str, Any]], cards, sources) -> str:
    rendered = escape_tex(text)
    cited = cite_suffix(sources_for_refs(refs, cards, sources))
    return rendered + ("" if not cited else cited)


def render_bullets(text: str, refs: list[dict[str, Any]], cards, sources) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""
    items = []
    for line in lines:
        value = line[2:].strip() if line.startswith(("- ", "* ")) else line
        items.append(r"\item " + escape_tex(value))
    cited = cite_suffix(sources_for_refs(refs, cards, sources))
    return "\n".join([r"\begin{itemize}", *items, r"\end{itemize}" + cited])


def parse_table(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    width: int | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("|") and line.endswith("|"):
            line = line[1:-1]
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) == 1:
            cells = [cell.strip() for cell in line.split("\t")]
        if len(cells) < 2:
            raise ValueError("TABLE block must contain at least two pipe- or tab-separated columns")
        if all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
            continue
        if width is None:
            width = len(cells)
        elif len(cells) != width:
            raise ValueError("TABLE block rows have inconsistent column counts")
        rows.append(cells)
    if len(rows) < 2:
        raise ValueError("TABLE block requires a header and at least one data row")
    return rows


def render_table(text: str, refs: list[dict[str, Any]], cards, sources) -> str:
    rows = parse_table(text)
    width = len(rows[0])
    colspec = "@{}" + "X" * width + "@{}"
    header = " & ".join(r"\textbf{" + escape_tex(cell) + "}" for cell in rows[0]) + r" \\"
    body = [" & ".join(escape_tex(cell) for cell in row) + r" \\" for row in rows[1:]]
    cited = cite_suffix(sources_for_refs(refs, cards, sources))
    return "\n".join([
        r"\begin{center}",
        r"\small",
        rf"\begin{{tabularx}}{{\linewidth}}{{{colspec}}}",
        r"\toprule",
        header,
        r"\midrule",
        *body,
        r"\bottomrule",
        r"\end{tabularx}" + cited,
        r"\end{center}",
    ])


def render_block(block: dict[str, Any], cards, sources) -> str:
    block_type = block["block_type"]
    text = block["text"]
    refs = block.get("evidence_refs") or []
    if block_type == "HEADING":
        return r"\subsection*{" + escape_tex(text) + "}"
    if block_type == "PARAGRAPH":
        return render_text_with_cite(text, refs, cards, sources)
    if block_type == "BULLET_LIST":
        return render_bullets(text, refs, cards, sources)
    if block_type == "TABLE":
        return render_table(text, refs, cards, sources)
    if block_type == "CLAIM_BOUNDARY":
        body = render_text_with_cite(text, refs, cards, sources)
        return "\n".join([r"\begin{claimboundary}", body, r"\end{claimboundary}"])
    if block_type == "COMMUNITY_NOTE":
        body = render_text_with_cite(text, refs, cards, sources)
        return "\n".join([r"\begin{communitynote}", body, r"\end{communitynote}"])
    if block_type == "LATE_BREAKING_NOTE":
        body = render_text_with_cite(text, refs, cards, sources)
        return "\n".join([r"\begin{latebreaking}", body, r"\end{latebreaking}"])
    raise ValueError(f"unsupported block_type: {block_type}")


def bib_date_fields(source: dict[str, Any]) -> list[str]:
    fields: list[str] = []
    published = source.get("published_at")
    if isinstance(published, str) and published:
        day = published[:10]
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            fields.append(f"  date = {{{day}}},")
    accessed = source.get("accessed_at")
    if isinstance(accessed, str) and accessed:
        day = accessed[:10]
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            fields.append(f"  urldate = {{{day}}},")
    return fields


def bib_entry(source: dict[str, Any]) -> str:
    url = source["url"]
    key = citation_key(url)
    title = str(source.get("title") or url).replace("{", "").replace("}", "")
    source_class = str(source.get("source_class") or "UNKNOWN")
    role = str(source.get("role") or "")
    fields = [
        f"@online{{{key},",
        f"  title = {{{title}}},",
        f"  url = {{{url}}},",
        *bib_date_fields(source),
        f"  note = {{{source_class}; {role}}},",
        "}",
    ]
    return "\n".join(fields)


def materialize(package_path: Path, draft_path: Path, prompt_path: Path, output_dir: Path) -> tuple[dict[str, Any], bool]:
    validation, passed = draft_validator.validate(package_path, draft_path, prompt_path)
    if not passed:
        raise ValueError(f"Article Draft is not materialization-ready: {validation['errors']}")

    package = load_json(package_path)
    draft = load_json(draft_path)
    cards = evidence_cards(package)
    sources = source_index(cards)

    used_sources: dict[str, dict[str, Any]] = {}
    all_refs = list(draft.get("deck_evidence_refs") or [])
    for block in draft.get("blocks") or []:
        all_refs.extend(block.get("evidence_refs") or [])
    for source in sources_for_refs(all_refs, cards, sources):
        used_sources[source["url"]] = source

    deck = render_text_with_cite(draft["deck"], draft.get("deck_evidence_refs") or [], cards, sources)
    blocks = [render_block(block, cards, sources) for block in draft["blocks"]]
    tex = "\n\n".join([
        r"\section{" + escape_tex(draft["headline"]) + "}",
        r"\textbf{" + deck + "}",
        *blocks,
        "",
    ])

    output_dir.mkdir(parents=True, exist_ok=True)
    tex_path = output_dir / f"{package['package_id']}.tex"
    bib_path = output_dir / f"{package['package_id']}.bib"
    tex_path.write_text(tex, encoding="utf-8")
    bib_path.write_text("\n\n".join(bib_entry(used_sources[url]) for url in sorted(used_sources)) + ("\n" if used_sources else ""), encoding="utf-8")

    manifest = {
        "schema_version": "1.0",
        "issue_id": package["issue_id"],
        "package_id": package["package_id"],
        "passed": True,
        "basis": {
            "draft_package_sha256": sha256_file(package_path),
            "draft_result_sha256": sha256_file(draft_path),
            "prompt_sha256": sha256_file(prompt_path),
        },
        "outputs": {
            "tex": tex_path.name,
            "tex_sha256": sha256_file(tex_path),
            "bib": bib_path.name,
            "bib_sha256": sha256_file(bib_path),
        },
        "citation_count": len(used_sources),
        "citation_keys": [citation_key(url) for url in sorted(used_sources)],
        "rules": [
            "LaTeX citations are derived from Evidence refs; the drafting model does not choose bibliography keys.",
            "BibTeX entries are deduplicated by exact source URL within the package.",
            "Structured block types map deterministically to survey LaTeX semantics.",
        ],
    }
    write_json(output_dir / f"{package['package_id']}-materialization.json", manifest)
    return manifest, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--draft", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = materialize(Path(args.package), Path(args.draft), Path(args.prompt), Path(args.output_dir))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
