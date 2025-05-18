# Implementation Roadmap

## Environment Setup

<!-- TASK:FS01 status=pending -->

* [ ] Develop a `scripts/bootstrap.sh` script to automate environment setup on a fresh Ubuntu 24.04 sandbox (and macOS) – update package lists, install Python3/pip if missing, and ensure Node.js + npm are available (use `apt-get` on Linux, Homebrew or preinstalled tools on macOS).

<!-- TASK:FS02 status=done -->

* [ ] In the bootstrap script, install required Python packages (via `pip install -r requirements.txt`) including **google-adk** (ADK) and **litellm** (Codex client). Also use npm to pre-install MCP server packages (e.g. `npm install -g @modelcontextprotocol/server-filesystem @modelcontextprotocol/server-github`) so they can run offline.

*(This ensures a one-command setup for the sandbox. All dependencies are fetched upfront before network is disabled, including ADK for agent orchestration and Node packages for MCP servers. Having a reproducible bootstrap script guarantees any new environment (or CI runner) can install the exact stack needed to run the agent.)*

## Repository Structure

<!-- TASK:FS03 status=done -->

* [ ] Create the base project folders: `agents/`, `mcp_servers/`, `configs/`, `reports/`, and `scripts/`. Add placeholder files or `.gitkeep` as needed so each directory is tracked in Git.

<!-- TASK:FS04 status=pending -->

* [ ] Under `agents/`, add an initial agent module. Create `agents/dev_agent.py` (the seeded development agent) and an empty `agents/__init__.py`. Ensure `dev_agent.py` at least defines a minimal agent class or instance (to be implemented in Agent Wiring tasks).

<!-- TASK:FS05 status=pending -->

* [ ] Under `configs/`, add `AGENTS.md` (a brief document describing available agents and how to extend them) and `ROADMAP_TODO.md` (initially empty or with example task format). These will hold agent configurations and the to-do task list, respectively.

<!-- TASK:FS06 status=pending -->

* [ ] Add an empty `reports/` directory for debrief files (no files yet; use a placeholder file if necessary to commit the directory).

<!-- TASK:FS07 status=pending -->

* [ ] Create a `requirements.txt` (or `pyproject.toml`) pinning all Python dependencies (e.g. `google-adk`, `litellm` with specific versions). Also include any other packages needed (for example, GitPython if used, etc.). Add a `.gitignore` (ignoring typical Python artifacts, node\_modules, and secret files).

<!-- TASK:FS08 status=pending -->

* [ ] Write a concise `README.md` for the project. Include a short overview of the platform’s purpose, the high-level workflow (bootstrap → agent runs tasks → PRs), and basic usage instructions. Document how to run the `bootstrap.sh` script and note that after setup, the agent operates inside the Codex sandbox with no outbound network. Also list the required environment variables (e.g. `OPENAI_API_KEY`, `GITHUB_PERSONAL_ACCESS_TOKEN`, etc.) and how they are provided (injected via UI) without exposing secrets in code.

*(Organizing the repository with clear directories separates agent code, config, and logs. The README acts as a quickstart guide for developers, while detailed agent info goes in `AGENTS.md`. Pinning dependencies in requirements ensures reproducible installs. The structure anticipates extension: multiple agents can reside in `agents/`, and new configuration or tool notes can live under `configs/` or `mcp_servers/` as needed.)*

## Model Context Protocol (MCP) Servers

<!-- TASK:FS09 status=pending -->

* [ ] Ensure the **Filesystem MCP** server can be launched for the project workspace. Provide a helper script or note (e.g. `mcp_servers/run_filesystem.sh`) to run: `npx -y @modelcontextprotocol/server-filesystem /workspace`. This grants the agent controlled access to the `/workspace` directory through tool calls (file read/write operations).

<!-- TASK:FS10 status=pending -->

* [ ] Similarly, prepare the **GitHub MCP** server usage. Include instructions or a script (`mcp_servers/run_github.sh`) to start the GitHub MCP (e.g. `npx -y @modelcontextprotocol/server-github`) with the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable set. This will allow the agent to interact with the GitHub repository (commit, open PRs) via an SSE connection, despite no direct network.

<!-- TASK:FS11 status=pending -->

* [ ] Note in documentation that additional community or cloud MCP servers (like Cloudflare or others) are not started by default. They can be installed and launched on demand if a task requires them. Keep the sandbox lean by only running the filesystem and GitHub MCPs when necessary.

*(MCP servers provide a bridge for the agent to perform actions that would normally require network or OS access. By running a filesystem server, the agent gains sandboxed file system tools. The GitHub MCP uses the personal access token to push commits or create pull requests externally. We include simple launch scripts and instructions so a developer (or automation) can start these servers prior to running the agent. This design keeps the core platform secure and extensible—other MCP servers (Cloudflare, search, etc.) can be added later as needed.)*

## Agent Wiring

<!-- TASK:FS12 status=pending -->

* [ ] Implement the `dev_agent.py` with a minimal ADK agent instance. Use the ADK’s `Agent` (or `LlmAgent`) class with **LiteLLM** as the model backend. For example, initialize the agent with `model=LiteLlm(model="openai/codex-mini-latest")` (which will use the `OPENAI_API_KEY`), a placeholder system instruction (e.g. `"You are an autonomous development agent..."`), and `tools=[]` (no tools at first).

<!-- TASK:FS13 status=pending -->

* [ ] Include a clear docstring in `dev_agent.py` explaining the agent’s purpose and how to extend it. Document that this is a base development agent using Codex, and describe how to subclass or modify the agent (e.g. adding tools or changing the prompt) to create new agents in the `agents/` package.

*(At this stage, the development agent is set up to use OpenAI Codex via ADK’s integration with LiteLLM. The agent has no tools enabled yet, meaning it will only produce reasoning or code as output without taking external actions. The code and docstring in `dev_agent.py` establish a template for adding functionality. This modular design allows solo developers to create new agents or adjust the AI’s behavior by subclassing or changing parameters, without altering the core loop.)*

## CI and Continuous Integration

<!-- TASK:FS14 status=pending -->

* [ ] Create a GitHub Actions workflow (e.g. `.github/workflows/bootstrap.yml`) to validate the setup on each commit. Use a **macOS (M1/M2)** runner for parity with Apple Silicon dev environments. The job should checkout the repo, run `scripts/bootstrap.sh`, and verify it completes without errors (this ensures a fresh clone + bootstrap is always sufficient to set up the project).

*(This CI step guarantees that the bootstrap process is reliable and cross-platform. By running on macOS in CI, we catch any platform-specific issues (e.g. ARM architecture or Homebrew quirks) early. A green CI means a developer can clone the repo and run `./scripts/bootstrap.sh` on their machine (or Codespace) with confidence. This also enforces discipline: whenever dependencies or workflows change, the bootstrap script and README must be updated accordingly to keep CI passing.)*

## Automation Loop

<!-- TASK:FS15 status=pending -->

* [ ] Implement a parser that reads `configs/ROADMAP_TODO.md` and identifies tasks with `status=pending`. The parser should recognize the task format (HTML comment tags and list items) and collect each pending task’s ID and description.

<!-- TASK:FS16 status=pending -->

* [ ] Add logic to update the status of a task in the markdown file. For example, when the agent begins work on a task, mark it `in_progress`, and when completed, mark it `done`. This can be done by editing the `ROADMAP_TODO.md` file in place (using the filesystem tool or Python file I/O) and will provide traceability of task execution.

<!-- TASK:FS17 status=pending -->

* [ ] Integrate the **Filesystem MCP tool** into the agent. Register the file system tools (from the running filesystem MCP server) with the dev agent so it can read from and write to project files autonomously. This may involve using ADK’s MCP tool integration (ensuring the agent’s `tools` list now includes file read/write capabilities exposed by the MCP server).

<!-- TASK:FS18 status=pending -->

* [ ] Integrate the **GitHub MCP tool** into the agent. Add the GitHub-specific tool(s) (from the running GitHub MCP server) to enable actions like creating branches and opening pull requests. With this tool, the agent can commit changes and initiate a PR via the GitHub API (using the token provided), all from within the sandbox.

<!-- TASK:FS19 status=pending -->

* [ ] Orchestrate the task execution loop. For each pending task:

  1. Load the task description and context,
  2. Invoke the `dev_agent` to address the task (e.g. improve code, add a feature) – the agent will use its tools (filesystem, etc.) to make changes in the workspace.
  3. Once the agent signals completion or no further actions, capture the result.

<!-- TASK:FS20 status=pending -->

* [ ] After the agent finishes a task, use the GitHub tool to create a pull request with the changes. The PR should be on a new branch (e.g. named after the task ID) and include a descriptive title (perhaps the task description) and body.

<!-- TASK:FS21 status=pending -->

* [ ] Have the agent (or controlling script) generate a debrief report for the task. This is a short markdown summary of what was done, why, and any follow-up notes. Save each report as `reports/NNN_debrief.md` (where NNN is the task identifier or sequence number).

<!-- TASK:FS22 status=pending -->

* [ ] Include the content of the debrief in the pull request (for example, in the PR description or as a comment) so the human reviewer can easily see the rationale and changes made without opening the report file separately. Link to the `reports/` file in the PR for traceability.

*(These steps close the development loop with the AI agent at the center. The system will autonomously take tasks from the ROADMAP\_TODO list, implement them, and create pull requests for review. By parsing and updating the task file, the agent keeps track of progress. Using the filesystem tool, the agent can modify code directly; using the GitHub tool, it can push those modifications as a PR. Each task’s outcome is documented in a debrief report, which is also shared in the PR, ensuring transparency. Human oversight is preserved at the PR review stage – the solo developer can review the changes and merge them. This loop can be triggered manually for each task or run sequentially for multiple tasks, enabling continuous development inside the Codex sandbox.)*

## Extension Plan

<!-- TASK:FS23 status=pending -->

* [ ] **Additional MCP integrations**: Incorporate optional MCP servers such as Cloudflare Workers or other community-provided tools on demand. For example, if web browsing or data retrieval is needed, a Cloudflare MCP (with `CLOUDFLARE_API_TOKEN`) or a local search MCP could be added to the agent’s toolset temporarily to handle that specific task.

<!-- TASK:FS24 status=pending -->

* [ ] **Enhanced agent capabilities**: Expand the agent’s tool list with more built-in or custom tools. This could include a Google Search tool (leveraging `GOOGLE_API_KEY` for custom search) or other APIs, enabling the agent to gather information or perform complex tasks beyond code edits. Ensure new tools are integrated via ADK’s tool interface and are only loaded when necessary to keep the system efficient and secure.

<!-- TASK:FS25 status=pending -->

* [ ] **Memory and state improvements**: Implement a session memory for the agent so it can remember context across tasks or iterative steps. Using ADK’s session/state management, the agent could maintain knowledge of previous decisions or project architecture, leading to more coherent multi-step development work.

<!-- TASK:FS26 status=pending -->

* [ ] **Multi-agent workflows**: If beneficial, introduce additional specialized agents (e.g. a testing agent, documentation agent) that can be spawned or coordinated via ADK’s multi-agent orchestration. This would allow splitting tasks (for instance, one agent writes code and another reviews or writes tests) to improve reliability of outcomes.

<!-- TASK:FS27 status=pending -->

* [ ] **Robustness and testing**: Add automated tests and safety checks. For example, include a suite of unit tests for critical components and a step in CI to run them. Implement guardrails in the agent’s prompting or tools to prevent destructive actions (since the agent has file system access, include checks or confirmations for dangerous operations like file deletions or large changes). Continually refine the agent’s system prompt and few-shot examples to improve quality and alignment with the developer’s goals.

*(The extension tasks outline how the platform can evolve beyond the minimal viable agent. New MCP servers (Cloudflare, database connectors, etc.) can be added to extend the agent’s reach when needed. Enhancing the agent with search or other tools will make it more autonomous and powerful in tackling high-level tasks. Introducing memory or multiple agents can handle more complex development workflows, allowing the system to scale from a single-agent assistant to a coordinated team of agent specialists. Finally, adding tests and safety mechanisms will increase trust in the agent’s changes – ensuring the platform remains a reliable, secure toolbox for solo developers. These extensions can be implemented incrementally as the user’s needs grow, building on the solid foundation established in this roadmap.)*
