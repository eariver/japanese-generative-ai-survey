# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://www.techrepublic.com/article/news-github-copilot-teams-conversations-coding-agent/
- observed_at: 2026-09-15T04:45:00Z
- published_at: 2026-08-25 (page date)
- retrieval: webfetch text; boilerplate trimmed; substantive claims preserved.
- authority_class: SECONDARY_TECHNICAL (tech press; Microsoft/GitHub first-party docs are verification targets)

# Retrieved content (substantive claims)

Title: GitHub Copilot Coding Agent Can Now Use Microsoft Teams Conversations. By Joseph Ofonagoro, Aug 25 2026.

GitHub Copilot's coding agent can now use Microsoft Teams conversations as context to investigate software tasks, change code, and create pull requests. Removes the step of reconstructing team discussion as a new coding prompt: developer @mentions the agent in the Teams conversation; agent combines discussion with connected GitHub repo info to investigate, implement, and open a PR.

Copilot in Teams introduced Sept 2025; this change makes the conversation itself a direct context source for the coding agent.

Controls: output subject to existing repo permissions and PR controls; changes reviewable before merge. Framing: decision-to-implementation distance shrinks; conversation becomes working context. Enterprise angle: approved-agent-in-managed-tooling vs shadow AI.

Availability: public preview via desktop and web apps; requires Teams environment + repo + Copilot coding-agent access.
