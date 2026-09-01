#!/usr/bin/env python3
"""Render a validated Article Draft Result into LaTeX plus generated BibLaTeX.

Citation keys are generated deterministically from underlying source URLs. The
LLM never chooses bibliography keys; it cites Evidence IDs, and this renderer
resolves Evidence -> source IDs -> URLs after validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import validate_article_draft as draft_validator


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tex_escape(value: str) -> str:
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
    return "".join(replacements.get(char, char) for char in value)


def bib_escape(value: str) -> str:
    return tex_escape(value)


def cite_key(url: str) -> str:
    return "src-" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]


def evidence_maps(package: dict[str, Any]) -> tuple[dict[tuple[str, str, str], list[tuple[str, dict[str, Any], str | None]]], dict[str, dict[str, Any]]]:
    refs: dict[tuple[str, str, str], list[tuple[str, dict[str, Any], str | None]]] = {}
    sources_by_key: dict[str, dict[str, Any]] = {}

    items = [*(package.get("primary_evidence") or []), *(package.get("supporting_evidence") or [])]
    items.sort(key=lambda item: item.get("evidence_task_id", ""))
    for item in items:
        task_id = item["evidence_task_id"]
        card = item["card"]
        organization = card.get("artifact", {}).get("organization")
        local_sources = {source["source_id"]: source for source in card.get("sources") or []}

        def register(kind: str, evidence_id: str, source_ids: list[str]) -> None:
            resolved: list[tuple[str, dict[str, Any], str | None]] = []
            for source_id in source_ids:
                source = local_sources.get(source_id)
                if source is None:
                    raise ValueError(f"Evidence {task_id}/{kind}/{evidence_id} references missing source {source_id}")
                url = source["url"]
                key = cite_key(url)
                resolved.append((key, source, organization))
                previous = sources_by_key.get(key)
                normalized = {
                    "source": source,
                    "organization": organization,
                    "url": url,
                }
                if previous is None:
                    sources_by_key[key] = normalized
                elif previous["url"] != url:
                    raise ValueError(f"bibliography key collision for {url}")
            refs[(task_id, kind, evidence_id)] = resolved

        for event in card.get("temporal", {}).get("events", []) or []:
            register("EVENT", event["event_id"], event["source_ids"])
        for field, kind, id_field in (
            ("claims", "CLAIM", "claim_id"),
            ("metrics", "METRIC", "metric_id"),
            ("limitations", "LIMITATION", "limitation_id"),
        ):
            for evidence in card.get(field, []) or []:
                register(kind, evidence[id_field], evidence["source_ids"])
    return refs, sources_by_key


def keys_for_refs(evidence_refs: list[dict[str, Any]], mapping: dict[tuple[str, str, str], list[tuple[str, dict[str, Any], str | None]]]) -> list[str]:
    keys: set[str] = set()
    for ref in evidence_refs:
        key = (ref["evidence_task_id"], ref["kind"], ref["evidence_id"])
        for cite, _, _ in mapping[key]:
            keys.add(cite)
    return sorted(keys)


def citation(keys: list[str]) -> str:
    return "" if not keys else r"\autocite{" + ",".join(keys) + "}"


def parse_bullets(text: str) -> list[str]:
    values = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"^(?:[-*•]|\d+[.)])\s*", "", line)
        values.append(line)
    return values or [text]


def parse_markdown_table(text: str) -> tuple[list[str], list[list[str]]] | None:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < 2 or "|" not in lines[0]:
        return None

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip("|").split("|")]

    header = cells(lines[0])
    start = 1
    if len(lines) > 1:
        separator = cells(lines[1])
        if len(separator) == len(header) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in separator):
            start = 2
    rows = [cells(line) for line in lines[start:]]
    if not header or any(len(row) != len(header) for row in rows):
        return None
    return header, rows


def render_table(text: str, cite: str) -> str:
    parsed = parse_markdown_table(text)
    if parsed is None:
        return tex_escape(text) + cite + "\n"
    header, rows = parsed
    columns = "|".join([">{\\raggedright\\arraybackslash}X"] * len(header))
    out = [r"\begin{center}", r"\small", rf"\begin{{tabularx}}{{\columnwidth}}{{{columns}}}", r"\toprule"]
    out.append(" & ".join(r"\textbf{" + tex_escape(cell) + "}" for cell in header) + r" \\")
    out.append(r"\midrule")
    for row in rows:
        out.append(" & ".join(tex_escape(cell) for cell in row) + r" \\")
    out.extend([r"\bottomrule", r"\end{tabularx}"])
    if cite:
        out.append(cite)
    out.append(r"\end{center}")
    return "\n".join(out) + "\n"


def render_block(block: dict[str, Any], mapping: dict[tuple[str, str, str], list[tuple[str, dict[str, Any], str | None]]]) -> str:
    block_type = block["block_type"]
    cite = citation(keys_for_refs(block.get("evidence_refs") or [], mapping))
    text = block["text"]
    if block_type == "HEADING":
        return r"\subsection{" + tex_escape(text) + "}\n"
    if block_type == "PARAGRAPH":
        return tex_escape(text) + cite + "\n\n"
    if block_type == "BULLET_LIST":
        out = [r"\begin{itemize}"]
        for value in parse_bullets(text):
            out.append(r"  \item " + tex_escape(value))
        out.append(r"\end{itemize}")
        if cite:
            out.append(cite)
        return "\n".join(out) + "\n"
    if block_type == "TABLE":
        return render_table(text, cite)
    environment = {
        "CLAIM_BOUNDARY": "claimboundary",
        "COMMUNITY_NOTE": "communitynote",
        "LATE_BREAKING_NOTE": "latebreaking",
    }.get(block_type)
    if environment:
        return f"\\begin{{{environment}}}\n{tex_escape(text)}{cite}\n\\end{{{environment}}}\n"
    raise ValueError(f"unsupported block_type: {block_type}")


def date_field(value: Any) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    if len(value) >= 10 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value[:10]):
        return value[:10]
    return None


def render_bibliography(sources: dict[str, dict[str, Any]]) -> str:
    entries: list[str] = []
    for key in sorted(sources):
        value = sources[key]
        source = value["source"]
        fields = [f"  title = {{{bib_escape(source['title'])}}}"]
        organization = value.get("organization")
        if isinstance(organization, str) and organization.strip():
            fields.append(f"  organization = {{{bib_escape(organization)}}}")
        published = date_field(source.get("published_at"))
        if published:
            fields.append(f"  date = {{{published}}}")
        fields.append(f"  url = {{{source['url']}}}")
        accessed = date_field(source.get("accessed_at"))
        if accessed:
            fields.append(f"  urldate = {{{accessed}}}")
        fields.append(f"  note = {{{bib_escape(source.get('role') or source.get('source_class') or 'Evidence source')}}}")
        entries.append(f"@online{{{key},\n" + ",\n".join(fields) + "\n}\n")
    return "\n".join(entries)


def render(package_path: Path, draft_path: Path, prompt_path: Path, tex_output: Path, bib_output: Path, manifest_output: Path) -> tuple[dict[str, Any], bool]:
    validation, passed = draft_validator.validate(package_path, draft_path, prompt_path)
    if not passed:
        raise ValueError(f"Article Draft did not validate: {validation['errors']}")
    package = load_json(package_path)
    draft = load_json(draft_path)
    mapping, sources = evidence_maps(package)

    deck_cite = citation(keys_for_refs(draft.get("deck_evidence_refs") or [], mapping))
    lines = [
        "% Generated from validated Article Draft Result. Do not hand-edit; revise the structured draft instead.",
        r"\section{" + tex_escape(draft["headline"]) + "}",
        r"\noindent\textbf{" + tex_escape(draft["deck"]) + "}" + deck_cite,
        "",
    ]
    for block in draft["blocks"]:
        lines.append(render_block(block, mapping))
    tex_output.parent.mkdir(parents=True, exist_ok=True)
    bib_output.parent.mkdir(parents=True, exist_ok=True)
    tex_output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    bib_output.write_text(render_bibliography(sources), encoding="utf-8")

    manifest = {
        "schema_version": "1.0",
        "issue_id": package["issue_id"],
        "package_id": package["package_id"],
        "passed": True,
        "basis": {
            "draft_package_sha256": sha256_file(package_path),
            "article_draft_sha256": sha256_file(draft_path),
            "prompt_sha256": sha256_file(prompt_path),
        },
        "tex": {"path": tex_output.as_posix(), "sha256": sha256_file(tex_output), "bytes": tex_output.stat().st_size},
        "bib": {"path": bib_output.as_posix(), "sha256": sha256_file(bib_output), "bytes": bib_output.stat().st_size, "entry_count": len(sources)},
        "citation_keys": sorted(sources),
        "note": "Cite keys are URL-hash-derived and were not supplied by the drafting model.",
    }
    manifest_output.parent.mkdir(parents=True, exist_ok=True)
    manifest_output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--draft", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    parser.add_argument("--tex-output", required=True)
    parser.add_argument("--bib-output", required=True)
    parser.add_argument("--manifest-output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, _ = render(
        Path(args.package), Path(args.draft), Path(args.prompt),
        Path(args.tex_output), Path(args.bib_output), Path(args.manifest_output),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
