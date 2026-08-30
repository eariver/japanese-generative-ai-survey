# Repowise project identity and tool surface

- Source URL: https://github.com/repowise-dev/repowise
- Source/page title: Know the code. Know what breaks. Change it with confidence.
- Retrieved at (UTC): 2026-08-30T10:16:12Z
- Explicit project/repository date stated by the source: not stated on the README page.

## Source-local observations

- The repository describes Repowise as evidence-backed codebase intelligence for humans and AI agents. It indexes code, call graphs, Git history, tests, and architectural decisions, and returns cited context, blast radius, test impact, and code-health fixes.
- The README says core analysis is local and deterministic and that optional synthesis is the only LLM layer. It presents the project as free/self-hosted and says core analysis needs no API key.
- The documented agent surface is task-shaped MCP tooling covering graph, Git, docs, decisions, health, and related repository intelligence; the README describes ten MCP tools. The README also documents CLI surfaces including `search`, `ask`, `context`, `symbol`, `why`, `health`, `risk`, `impacted-tests`, `dead-code`, `decision`, `distill`, and `saved`, alongside indexing/serve/update commands.
- The project README displays project-reported workflow figures of 31.6% less agent-generated output across 43 repository questions and 3.8 versus 7.2 tool calls; it separately labels 393 versus 13,984 tokens as one retrieval payload rather than end-to-end agent savings.

## Attribution and limitations

- Project identity, feature/tool descriptions, and displayed measurements are Repowise's own README claims.
- The README itself distinguishes retrieval-payload reduction from end-to-end agent savings; this capture preserves that distinction and does not treat product marketing text as independent performance evidence.
