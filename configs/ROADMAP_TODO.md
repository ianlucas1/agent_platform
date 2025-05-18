<!-- TASK:FS01 status=done -->
* [x] Develop a `scripts/bootstrap.sh` script to automate environment setup on a fresh Ubuntu 24.04 sandbox (and macOS) – update package lists, install Python3/pip if missing, and ensure Node.js + npm are available (use `apt-get` on Linux, Homebrew or pre-installed tools on macOS).
<!-- /TASK -->

<!-- TASK:FS02 status=pending -->
* [ ] In the bootstrap script, install required Python packages (via `pip install -r requirements.txt`) including **google-adk** and **litellm**. Also pre-install MCP server packages with `npm install -g @modelcontextprotocol/server-filesystem @modelcontextprotocol/server-github` so they can run offline.
<!-- /TASK -->

<!-- TASK:FS03 status=pending -->
* [ ] Create base folders: `agents/`, `mcp_servers/`, `configs/`, `reports/`, `scripts/` (add `.gitkeep` or placeholder files so each is tracked).
<!-- /TASK -->

<!-- TASK:FS04 status=pending -->
* [ ] In `agents/`, add `agents/dev_agent.py` and empty `agents/__init__.py`. `dev_agent.py` should stub a minimal agent class or instance (to be wired later).
<!-- /TASK -->

<!-- TASK:FS05 status=pending -->
* [ ] Under `configs/`, add `AGENTS.md` (brief agent catalog) and an **empty** `ROADMAP_TODO.md` (this file).
<!-- /TASK -->

<!-- TASK:FS06 status=pending -->
* [ ] Add an empty `reports/` directory for debrief files (commit with `.gitkeep` if needed).
<!-- /TASK -->

<!-- TASK:FS07 status=pending -->
* [ ] Create `requirements.txt` (or `pyproject.toml`) pinning dependencies (`google-adk`, `litellm`, etc.) and add a `.gitignore` ignoring Python artifacts, `node_modules/`, secrets.
<!-- /TASK -->

<!-- TASK:FS08 status=pending -->
* [ ] Write a concise `README.md` covering project purpose, bootstrap usage, and required environment variables (`OPENAI_API_KEY`, `GITHUB_PERSONAL_ACCESS_TOKEN`, …).
<!-- /TASK -->

<!-- TASK:FS09 status=pending -->
* [ ] Provide `mcp_servers/run_filesystem.sh` that runs `npx -y @modelcontextprotocol/server-filesystem /workspace` to expose the Filesystem MCP.
<!-- /TASK -->

<!-- TASK:FS10 status=pending -->
* [ ] Provide `mcp_servers/run_github.sh` that runs `npx -y @modelcontextprotocol/server-github` with `GITHUB_PERSONAL_ACCESS_TOKEN` exported for GitHub MCP access.
<!-- /TASK -->

<!-- TASK:FS11 status=pending -->
* [ ] Document (in README or separate note) how optional community MCP servers (e.g. Cloudflare) can be installed and launched only when required.
<!-- /TASK -->

<!-- TASK:FS12 status=pending -->
* [ ] Implement `dev_agent.py` as a minimal ADK agent using `LiteLlm(model="openai/codex-mini-latest")`, placeholder system prompt, and `tools=[]`.
<!-- /TASK -->

<!-- TASK:FS13 status=pending -->
* [ ] Add a clear module-level docstring to `dev_agent.py` explaining purpose and how to extend/subclass for specialised roles.
<!-- /TASK -->

<!-- TASK:FS14 status=pending -->
* [ ] Create `.github/workflows/bootstrap.yml` that checks out the repo on a macOS runner, runs `scripts/bootstrap.sh`, and fails on any error.
<!-- /TASK -->

<!-- TASK:FS15 status=pending -->
* [ ] Implement a parser that scans this file for `<!-- TASK:* status=pending -->` blocks and extracts each task’s ID + text.
<!-- /TASK -->

<!-- TASK:FS16 status=pending -->
* [ ] Add logic that updates a task’s comment line from `status=pending` → `status=in_progress` → `status=done`.
<!-- /TASK -->

<!-- TASK:FS17 status=pending -->
* [ ] Register Filesystem MCP tools with the dev agent so it can read/write project files autonomously.
<!-- /TASK -->

<!-- TASK:FS18 status=pending -->
* [ ] Register GitHub MCP tools with the dev agent so it can commit, push, and open PRs from inside the sandbox.
<!-- /TASK -->

<!-- TASK:FS19 status=pending -->
* [ ] Orchestrate the execution loop:  
  1. Load next pending task.  
  2. Invoke `dev_agent` to perform work using its tools.  
  3. Capture completion signal or fallback if no further actions.
<!-- /TASK -->

<!-- TASK:FS20 status=pending -->
* [ ] After completing a task, use GitHub tool to create a PR on a new branch named after the task ID; include descriptive title/body.
<!-- /TASK -->

<!-- TASK:FS21 status=pending -->
* [ ] Generate `reports/NNN_debrief.md` summarising what was done, why, and any follow-ups.
<!-- /TASK -->

<!-- TASK:FS22 status=pending -->
* [ ] Inject the debrief content (or link) into the PR description/comment so human reviewers get full context.
<!-- /TASK -->

<!-- TASK:FS23 status=pending -->
* [ ] Add optional MCP integrations (e.g. Cloudflare Workers) behind feature flags; load only when a task requires them.
<!-- /TASK -->

<!-- TASK:FS24 status=pending -->
* [ ] Expand agent toolset (e.g. Google Search using `GOOGLE_API_KEY`) via ADK tool interface; load tools lazily to keep runtime lean.
<!-- /TASK -->

<!-- TASK:FS25 status=pending -->
* [ ] Implement session memory so the agent can retain context across tasks via ADK’s state management.
<!-- /TASK -->

<!-- TASK:FS26 status=pending -->
* [ ] Introduce additional specialised agents (tester, docs, planner) coordinated via ADK multi-agent orchestration.
<!-- /TASK -->

<!-- TASK:FS27 status=pending -->
* [ ] Add unit tests, CI safety checks, and guardrails (e.g. prevent destructive file ops); refine prompts/few-shots for quality and alignment.
<!-- /TASK -->
