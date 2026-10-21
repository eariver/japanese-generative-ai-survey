# W42 r2 bundle — GitHub HydraFusion + Autofix + AI Scan + Argon distribution + changelog survey (full bodies, 2026-10-17)

Collector run: `20261017T071000Z-muse-r2` / collector_id `primary-webfetch`
Observed at: `2026-10-17T07:18:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. Official: HydraFusion updates + Max option (github.blog/changelog, Oct 14, 2026) — BODY CONSUMED
- URL: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option/
- Dated Oct 14, 2026 → IN-WINDOW. Status: research preview (both options).
- Core facts:
  - Multi-model orchestration (no per-task model choice); pool now: Claude Opus 5.5, GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna (per-task selection varies).
  - Effort tailoring per stage (medium draft / high review); Cascade adds judging step (repair-on-need); Critique moves to workspace tools + parallel critics.
  - Max = same architecture/workflows, higher effort for demanding tasks with token-efficiency via orchestration; HydraFusion = balanced.
  - Clients: VS Code, Copilot app, CLI; plans Pro/Pro+/Business/Enterprise with preview features + org model policies.
- Separate platform-agent candidate (orchestration product), not a model release. AUTHORITY_CONSUMED.

## 2. Official: Agentic autofix GA (github.blog/changelog, Oct 15, 2026) — BODY CONSUMED
- URL: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
- Dated Oct 15 → IN-WINDOW.
- Core facts: cross-file investigation → proposed fix → CodeQL rerun → draft PR (summary + validation steps); Assign-to-Copilot replaces Generate Fix; ≤25 alerts per single PR; default-branch alerts only (PR/other-branch alerts excluded); REST API assignees copilot-swe-agent[bot]; enterprise policy-gated + org/repo enablement; Copilot billing method required; consumes Code Security AI Credits + Actions minutes.
- Narrow eligibility + paid budget constraints as Sol noted. AUTHORITY_CONSUMED. Distinct product from AI Scan (fix vs detect).

## 3. Official: AI Scan for PRs GA (github.blog/changelog, Oct 15, 2026) — BODY CONSUMED
- URL: https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/
- Dated Oct 15 → IN-WINDOW.
- Core facts: complements CodeQL for uncovered languages (PHP, Shell/Bash, Terraform HCL, Dockerfiles, JSP, Blazor, +more); auto-run on PRs; AI indicator; explanation + suggested autofix; ADVISORY (never fails check, cannot block merge via rulesets); NO forks, NO Dependabot; public org/personal repos included; private/internal needs Code Security/Advanced Security; NO Copilot license required; consumes Code Security AI Credits.
- Fold editorially with autofix only as Security-GA pair, never conflated (detect-advisory vs fix-PR). AUTHORITY_CONSUMED.

## 4. Supporting: Gemini 4 Argon in GitHub Copilot (changelog, Oct 13, 2026) — LOCATOR + month-page confirmation
- Month page https://github.blog/changelog/month/10-2026/ lists "Gemini 4 Argon in GitHub Copilot" (Oct 13, GA in Copilot for complex coding/agentic/reasoning) — confirms distribution event; full per-model page not separately fetched (supporting link only).
- Treatment: supporting distribution evidence for existing w42-primary-gemini4-argon-20261013, NOT a duplicate model event. New support record with parent link in reason text (origin BASE to keep schema parents empty; linkage documented here + handoff).

## 5. Changelog month-page survey (Oct 2026, p.1 — first-party negative-space)
- In-window AI/security items confirmed present: Argon-in-Copilot (10-13), secret-scanning Anthropic-keys-by-default + Salesforce (10-13), Code Quality audit log (10-13), HydraFusion (10-14), Actions workflow lockfiles preview (10-14), Autofix GA + AI Scan GA (10-15), Copilot model deprecation notice (10-15, effective Nov 16 — FUTURE, outside window; recorded, not proposed), Slack/Teams multi-repo (10-15), license-compliance GA (10-16, non-AI admin; recorded, not proposed), Xcode runner (10-15, non-AI).
- Deliberately NOT proposed with reasons: Nov-16 deprecation (future effect, admin notice), license-compliance/Xcode/Slack (non-generative-AI), secret-scanning keys (detection SKU, not gen-AI event; noted), lockfiles (CI feature, not gen-AI).
- Scion article Oct 15 revision: per Sol, current-version provenance of existing Scion record (page updated Oct 15 per r1 body note); no standalone record.
