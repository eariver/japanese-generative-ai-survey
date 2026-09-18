# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://blog.kilo.ai/p/kilo-for-jetbrains-a-multi-agent-control-room
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-01
- retrieval: webfetch markdown of Kilo Blog "Kilo for JetBrains is now a multi-agent control room"; stored verbatim as returned. Byline shows Arkadiy Kondrashov and Job Rietbergen, Sep 01, 2026.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

# Kilo for JetBrains is now a multi-agent control room

### Run parallel coding agents in isolated worktrees, test their changes, follow every diff and PR, and choose from 600+ models — without leaving JetBrains.

Arkadiy Kondrashov and Job Rietbergen. Sep 01, 2026.

A few weeks ago, we wrote about why we rebuilt Kilo Code for JetBrains as a native Kotlin plugin designed for JetBrains split mode from day one.

The new version of Kilo Code for JetBrains shows why we made that investment. You can now run multiple coding agents on different tasks at the same time, give each one an isolated git worktree, run the result using your existing Run Configurations, and track its diff and GitHub PR — all from one IDE frame.

In other words, Kilo turns JetBrains into a multi-agent control room.

We're live on Product Hunt today with the new Kilo for JetBrains.

## One task per agent, one worktree per task

Running agents in parallel sounds useful until two agents work on the same checkout.

Kilo avoids agent coordination problems by giving every task its own git worktree. Each agent gets its own branch, working directory, and uncommitted changes. The tasks can move independently without stepping on one another's files.

You can create a new worktree from a base branch, check out an existing branch, or import a GitHub PR directly from its URL. All of them appear in the Agent Manager, inside the JetBrains window you already have open.

Each worktree also keeps its own session history, so you can return to an earlier conversation without losing the branch-level view.

There is also a **Continue in Worktree** action for the moment when a conversation becomes a bigger piece of work. You can start an agent in your current checkout, explore the problem, and then move the session and its uncommitted changes into a fresh worktree without doing the git choreography yourself.

## Run the result without window-juggling

An agent finishing a code change is not the same as the change working.

Kilo takes your existing Run Configurations and adapts them to the selected worktree. It updates the working directory and relevant paths automatically, so you can launch an app from any task without rebuilding the configuration by hand.

The Agent Manager shows which worktrees have a process running. Build and Rebuild are available from the same place.

For full debugging — breakpoints, stepping through a JVM process, inspecting state — you can open one worktree in a dedicated IDE frame with one click. Kilo reuses the frame if that worktree is already open; otherwise it opens a new one.

## GitHub context belongs next to the task

Kilo shows the linked pull request number, title, and state in the session. You can open the PR in the browser, compare the worktree with its base branch, and see file and line counts without hunting through terminals or tabs.

Uncommitted changes are shown separately from the branch diff.

You can also paste a GitHub PR URL to create a worktree from it. That makes the same workflow useful beyond generation: pull down a teammate's PR, ask an agent to review or continue it, run the app, and open the worktree in a full frame if you need to debug it.

## Still built for the machine where your code actually lives

In JetBrains Remote Development, the UI runs on your laptop while indexing, project access, and execution happen on a remote host. Kilo's interface is native IntelliJ-platform Swing — there is no embedded Chromium UI — and the plugin is split into frontend, backend, and shared modules. The UI stays responsive on the client. The bundled agent server runs on the backend, next to the repository.

Kilo also ships a native CLI binary for the host's operating system and architecture, so you do not need to install or reconcile a Node.js runtime first.

## Choose the model for the task

Kilo gives you access to more than 600 models across major providers. You can use Kilo credits or bring your own API keys, then switch models without leaving the IDE.

Custom agents can be pinned to a specific model, so a carefully configured agent does not silently drift to a different model between sessions. You can also configure a separate small model for frequent, lower-cost operations while reserving a larger model for the main task.

Model badges surface relevant data-use information, including whether a model may train on prompts. For organizations, model access controls can block providers or individual models based on policies such as data training, retention, or datacenter location.

## One runtime behind every Kilo client

The JetBrains plugin is powered by Kilo CLI, the same open-source agent runtime behind Kilo's command-line interface, VS Code extension, and cloud.

The runtime handles model routing, tool execution, agent orchestration, and session persistence. JetBrains reads and writes the same kilo.jsonc configuration used by the CLI and VS Code. Your providers, custom agents, skills, and MCP servers can follow you across surfaces.

One agent server serves the main workspace and its open worktrees for each IDE instance. Parallelism also exists inside an individual session. Subagents can work on separate pieces of a problem and open in their own editor tabs, while the parent session keeps the overall task together.

Search for **Kilo Code** under **Settings → Plugins** in IntelliJ IDEA, WebStorm, PyCharm, GoLand, PhpStorm, Rider, CLion, or RubyMine. It works in Community and paid editions, with local projects and JetBrains Remote Development.

[truncated for edition-local storage: images, comments, and footer omitted; core article text preserved verbatim]
