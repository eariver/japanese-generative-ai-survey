# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://grith.ai/blog/grith-is-live
- observed_at: 2026-09-15T04:50:00Z
- published_at: 2026-08-25 (page date)
- retrieval: webfetch text; nav/footer/blogroll trimmed; launch claims preserved.
- authority_class: PRIMARY_OFFICIAL (vendor first-party launch post)

# Retrieved content (substantive claims)

Title: grith is live. grith team, August 25, 2026.

grith: security proxy for AI coding agents enforced at OS level. v0.3.2 installable on Linux x86_64 and arm64; repo public under MPL-2.0; security core free. Supports Claude Code, Codex, Aider, Cline, Goose (+ agent mode routing any OpenAI-compatible API or local Ollama model through same pipeline).

Thesis: permission prompts -> auto-approve fatigue means the agent approves its own actions; security decision must not live inside the thing secured. OS-level supervisor: ptrace + seccomp-BPF pre-filter intercepting file/process/network syscalls; 18 filters in 3 phases (static checks; pattern matching incl. 1617-pattern secret scanning, egress policy, destructive-op detection; contextual incl. taint tracking). Deterministic matching; no LLM in enforcement path.

Verdicts: ALLOW (<3.0), QUEUE (3.0–8.0, process frozen pending human review), DENY (>8.0, EPERM injected). Median scoring 0.02ms.

Release path: v0.2.2 no cold-start widening; v0.2.3 supervision-escape enforcement (systemd-run/docker/tmux/crontab spawns, D-Bus/tmux/X11 socket connects); v0.2.4 arm64, credential-store trust fix, rename-destination scoring; v0.2.5 escape enforcement on by default (queue-escalation, read-only never prompts, non-interactive fail-safe deny); v0.3.0 team analytics/sharing/D-Bus coverage; v0.3.1 verifiable archives, less prompt noise; v0.3.2 outcome-aware egress-rate state.

Stated gaps: supervised process tree is the boundary; delegation to pre-existing outside processes is structural escape class; not a VM/container replacement for fully untrusted code.

Free: full security core forever (proxy, 18 filters, supervisor, quarantine digest, SQLite audit log, CLI, localhost:3141 dashboard); no account, offline; cap 2 concurrent sessions. MPL-2.0 code; paid = team features via signed licenses. Releases: cosign keyless, SLSA provenance, CycloneDX SBOM, SHA-256, static musl.

Scope: Linux only (x86_64 kernel 4.8+, aarch64 5.3+); macOS (Endpoint Security) + Windows (ETW) are v2.0 work.

Motivation traces (vendor-reported): Claude Code attempted 752 /proc/*/environ reads in one benchmark run (methodology public); dogfood freeze of Codex disk-sweep for credentials during routine task.
