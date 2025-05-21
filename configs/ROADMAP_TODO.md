# Task Backlog

Legend  

* `[ ]` pending   `[-]` in progress   `[x]` done  
* Each task is preceded by an HTML comment the automation loop can patch.

---

*Note: Former FS30A–FS30D have been renumbered FS23–FS26 to preserve chronological order.*

<!-- FS01 -->
* [x] Bootstrap script — `scripts/bootstrap.sh` installs Python 3.11, Node 18, apt/brew packages.

<!-- FS02 -->
* [x] Offline dependency install — pre-pin Python wheels & NPM MCP servers for `NO_NET=1` runs.

<!-- FS03 -->
* [x] Create base folders — `agents/ mcp_servers/ configs/ reports/ scripts/` committed (with `.gitkeep`).

<!-- FS04 -->
* [x] Stub `dev_agent.py` — add minimal `DevAgent` class (google-adk, no tools yet); must import cleanly.

<!-- FS05 -->
* [x] Add AGENTS.md — brief agent catalogue & contribution tips.

<!-- FS06 -->
* [x] Empty reports/ dir — committed with placeholder to track debriefs.

<!-- FS07 -->
* [x] vision_roadmap.md — outline MVP milestones and long‑term ambitions.

<!-- FS08 -->
* [x] README scaffold — quick‑start + high‑level pitch.

<!-- FS09 -->
* [x] Makefile helpers — `make setup lint test run_tasks`.

<!-- FS10 -->
* [x] Ruff & Black — formatting/flake8 parity; pre‑commit config.

<!-- FS11 -->
* [x] Pytest smoke — empty test to keep CI green.

<!-- FS12 -->
* [x] Bandit CI — basic security scan.

<!-- FS13 -->
* [x] GitHub Actions CI — lint+test matrix.

<!-- FS14 -->
* [x] mkdocs site — docs auto‑build.

<!-- FS15 -->
* [x] Roadmap parser — code that lists `status=pending` tasks from this file. *(done 2025-05-20)*

<!-- FS16 -->
* [x] Status updater — helper to flip `status=in_progress/done` in place.

<!-- FS17 -->
* [x] Filesystem tool — add ADK tool pointing at `http://localhost:8787`.

<!-- FS18 -->
* [x] GitHub tool — add ADK tool for commits/PRs via `http://localhost:8788`.

<!-- FS19 -->
* [x] Task loop — `scripts/run_tasks.py` pulls first pending task, invokes agent, updates status.

<!-- FS20 -->
* [x] Auto‑PR — after edits, push branch `capx/FSxx‑<slug>` & open PR with template.

<!-- FS21 -->
* [x] Debrief file — agent writes `reports/FSxx_debrief.md` summarising work.

<!-- FS22 -->
* [ ] Debrief in PR — embed or link the debrief in the PR description.

<!-- FS23 -->
* [ ] Register remote MCP servers — add `configs/mcp_servers.yaml` (Filesystem & GitHub endpoints).

<!-- FS24 -->
* [ ] Responses‑API client wrapper — helper that calls Deep‑Research/Responses API with `tool_server_url`.

<!-- FS25 -->
* [ ] Remove local FastAPI bootstraps — drop local server scripts & related CI steps.

<!-- FS26 -->
* [ ] MCP smoke‑test in CI — pytest hits `/health` on remote MCP servers via Responses API.

<!-- FS27 -->
* [ ] Deep Research wrapper tool — call Deep Research API or headless Playwright; store audit markdown in `reports/`.

<!-- FS28 -->
* [ ] Codex automation harness — programmatic interface or Playwright driver; triggers task prompt, saves patches & logs.

<!-- FS29 -->
* [ ] Orchestrator agent MVP — orchestrates Deep‑Research Planner and Codex harness; loops tasks until none pending, schedules next cycle.

<!-- FS30 -->
* [ ] Cost monitor & throttle — track monthly token spend; halt cycles when spend nears budget cap.

<!-- FS31 -->
* [ ] Knowledge graph index — add DuckDB/Chroma vector store for code base.

<!-- FS32 -->
* [ ] Search tool — agent tool to query the vector store.

<!-- FS33 -->
* [ ] Session memory — persist last N debriefs to JSON; feed them into agent context.

<!-- FS34 -->
* [ ] Planner ➜ Engineer ➜ Verifier — multi‑agent roles, handshake schema.

<!-- FS35 -->
* [ ] Unit tests & safety rails — pytest smoke tests, Ruff/Black CI enforcement, write‑whitelist.

<!-- FS36 -->
* [ ] Pluggable model backend — LiteLLM config file to swap Codex with local model easily.

<!-- FS37 -->
* [ ] Natural‑language goal intake — CLI or API endpoint that converts a plain‑English goal into FS‑tasks.

<!-- FS38 -->
* [ ] Plugin Discovery — detect opportunities to replace custom code with MIT/Apache libraries.

<!-- FS39 -->
* [ ] Plugin Voting — evaluate candidate plugins for correctness & community health.

<!-- FS40 -->
* [ ] Plugin Benchmark — compare plugin performance & correctness vs. existing implementation.

<!-- FS41 -->
* [ ] Auto‑Wrap Integration — refactor code to use approved plugin via wrapper/adapter.

<!-- FS42 -->
* [ ] PR Bot Automation — bot manages plugin‑integration PRs; auto‑merge on green CI per policy.

<!-- FS43 -->
* [ ] Nightly “Borg” Run — scheduled job runs agent in maintenance mode to assimilate improvements.
