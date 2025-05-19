# CAP-X Task Backlog  
_Last updated 2025-05-18_

Legend  
* `[ ]` pending   `[-]` in progress   `[x]` done  
* Each task is preceded by an HTML comment the automation loop can patch.

---

<!-- TASK:FS01 status=done -->
- [x] **FS01 – Bootstrap script** — `scripts/bootstrap.sh` installs Python 3.11, Node 18, apt/brew packages.

<!-- TASK:FS02 status=done -->
- [x] **FS02 – Offline dependency install** — pre-pin Python wheels & NPM MCP servers for `NO_NET=1` runs.

<!-- TASK:FS03 status=done -->
- [x] **FS03 – Create base folders** — `agents/ mcp_servers/ configs/ reports/ scripts/` committed (with `.gitkeep`).

<!-- TASK:FS04 status=done -->
- [x] **FS04 – Stub `dev_agent.py`** — add minimal `DevAgent` class (google-adk, no tools yet); must import cleanly.

<!-- TASK:FS05 status=done -->
- [x] **FS05 – Add AGENTS.md** — brief agent catalogue & contribution tips.

<!-- TASK:FS06 status=done -->
- [x] **FS06 – Empty reports/ dir** — committed with placeholder to track debriefs.

<!-- TASK:FS07 status=pending -->
- [x] **FS07 – Project `.gitignore`** — ignore `node_modules/`, `__pycache__/`, `.venv/`, logs, vendor wheels.

<!-- TASK:FS08 status=done -->
- [x] **FS08 – Write README** — purpose, bootstrap, offline caveats, env vars.

<!-- TASK:FS09 status=pending -->
- [ ] **FS09 – `run_filesystem.sh`** — one-liner script to start Filesystem MCP on port 8787.

<!-- TASK:FS10 status=pending -->
- [ ] **FS10 – `run_github.sh`** — script to start GitHub MCP (uses `GITHUB_PERSONAL_ACCESS_TOKEN`) on port 8788.

<!-- TASK:FS11 status=pending -->
- [ ] **FS11 – Optional MCP docs** — new `docs/optional_mcp.md` listing extra servers & env vars.

<!-- TASK:FS12 status=pending -->
- [ ] **FS12 – Minimal ADK agent** — instantiate `DevAgent` with LiteLLM (model `openai/codex-mini-latest`).

<!-- TASK:FS13 status=pending -->
- [ ] **FS13 – Agent docstring** — explain extension points & tool wiring in `dev_agent.py`.

<!-- TASK:FS14 status=pending -->
- [ ] **FS14 – CI bootstrap workflow** — `.github/workflows/bootstrap.yml` (macOS + Ubuntu) runs bootstrap.

<!-- TASK:FS15 status=pending -->
- [ ] **FS15 – Roadmap parser** — code that lists `status=pending` tasks from this file.

<!-- TASK:FS16 status=pending -->
- [ ] **FS16 – Status updater** — helper to flip `status=in_progress/done` in place.

<!-- TASK:FS17 status=pending -->
- [ ] **FS17 – Filesystem tool** — add ADK tool pointing at `http://localhost:8787`.

<!-- TASK:FS18 status=pending -->
- [ ] **FS18 – GitHub tool** — add ADK tool for commits/PRs via `http://localhost:8788`.

<!-- TASK:FS19 status=pending -->
- [ ] **FS19 – Task loop** — `scripts/run_tasks.py` pulls first pending task, invokes agent, updates status.

<!-- TASK:FS20 status=pending -->
- [ ] **FS20 – Auto-PR** — after edits, push branch `capx/FSxx-slug` & open PR with template.

<!-- TASK:FS21 status=pending -->
- [ ] **FS21 – Debrief file** — agent writes `reports/FSxx_debrief.md` summarising work.

<!-- TASK:FS22 status=pending -->
- [ ] **FS22 – Debrief in PR** — embed or link the debrief in the PR description.

<!-- TASK:FS23 status=pending -->
- [ ] **FS23 – Search tool integration** — optional MCP server + ADK tool for doc/code search.

<!-- TASK:FS24 status=pending -->
- [ ] **FS24 – Debug tool integration** — stack-trace analyser MCP & tool (optional, behind feature flag).

<!-- TASK:FS25 status=pending -->
- [ ] **FS25 – Session memory** — persist last N debriefs to JSON; feed them into agent context.

<!-- TASK:FS26 status=pending -->
- [ ] **FS26 – Planner → Engineer → Verifier** — multi-agent roles, handshake schema.

<!-- TASK:FS27 status=pending -->
- [ ] **FS27 – Unit tests & safety rails** — pytest smoke tests, Ruff/Black CI enforcement, write-whitelist.

<!-- TASK:FS28 status=pending -->
- [ ] **FS28 – Pluggable model backend** — LiteLLM config file to swap Codex with local model easily.

<!-- TASK:FS29 status=pending -->
- [ ] **FS29 – Natural-language goal intake** — CLI or API endpoint that converts a plain-English goal into FS-tasks.

---
