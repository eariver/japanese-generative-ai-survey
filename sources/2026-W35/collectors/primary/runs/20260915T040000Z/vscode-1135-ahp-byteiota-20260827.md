# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://byteiota.com/vs-code-1-135-agent-host-protocol-ships-sessions-go-portable/
- observed_at: 2026-09-15T04:30:00Z
- published_at: 2026-08-27 (page date; shipped version event 2026-08-26)
- retrieval: webfetch text; boilerplate trimmed; substantive claims preserved.
- authority_class: SECONDARY_TECHNICAL (dev press; VS Code release notes + AHP spec are verification targets)

# Retrieved content (substantive claims)

Title: VS Code 1.135: Agent Host Protocol Ships, Sessions Go Portable. By ByteBot.

VS Code 1.135 shipped August 26: Agent Host Protocol (AHP) decouples agent sessions from the editor window (LSP/DAP analogy: editors share agents the way LSP shared language servers).

AHP: open MIT-licensed spec published by Microsoft on GitHub; host process runs the agent, communicates with client windows over JSON-RPC + WebSocket; sessions run in own process, persist independently, immutable state with sequence numbers. Draft pre-1.0 protocol — wire types/actions/state may break; third-party implementation exists from opencode project; do not bake into production CI/CD yet.

Portable sessions: VS Code Sessions list shows recent Copilot and Claude sessions started in other apps — Copilot CLI, GitHub Copilot app, Claude Code, Codex. Cross-window continue (terminal Claude Code -> VS Code diff view). Hidden by default, requires Copilot subscription; visibility settings None/Recent/24h/7d/All. Multiple windows can attach to same local session.

Rubber Duck: experimental review agent on a different model family than the orchestrator (e.g. Claude Sonnet orchestrator + GPT-5.4 reviewer); activates after plan draft, complex multi-file implementation, post-test pre-run. Claimed SWE-Bench Pro result: Sonnet+Rubber Duck closed 74.7% of Sonnet-to-Opus gap on hardest class (3+ files, 70+ steps); 4.8% lift on hardest problems; smaller benefit on average tasks. Off by default. (Vendor/press-reported benchmark; needs primary verification.)

Per-model token breakdowns per chat turn (input/cached/output) + cumulative session credits.

Editorial framing: AHP weakens fork moat (Cursor, Antigravity, Kiro) built on owning the session; editor becomes client.
