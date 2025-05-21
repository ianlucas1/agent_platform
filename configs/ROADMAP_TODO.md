# Task Backlog

Legend  

* `[ ]` pending   `[-]` in progress   `[x]` done  
* Each task is preceded by an HTML comment the automation loop can patch.

---

*Note: Former FS30A–FS30D have been renumbered FS23–FS26 to preserve chronological order.*

<!-- TASK:FS01 status=done -->
* [x] **FS01 – Bootstrap script** — `scripts/bootstrap.sh` installs Python 3.11, Node 18, apt/brew packages.

<!-- TASK:FS02 status=done -->
* [x] **FS02 – Offline dependency install** — pre-pin Python wheels & NPM MCP servers for `NO_NET=1` runs.

<!-- TASK:FS03 status=done -->
* [x] **FS03 – Create base folders** — `agents/ mcp_servers/ configs/ reports/ scripts/` committed (with `.gitkeep`).

<!-- TASK:FS04 status=done -->
* [x] **FS04 – Stub `dev_agent.py`** — add minimal `DevAgent` class (google-adk, no tools yet); must import cleanly.

<!-- TASK:FS05 status=done -->
* [x] **FS05 – Add AGENTS.md** — brief agent catalogue & contribution tips.

<!-- TASK:FS06 status=done -->
* [x] **FS06 – Empty reports/ dir** — committed with placeholder to track debriefs.

<!-- TASK:FS07 status=done -->
* [x] **FS07 – vision_roadmap.md** — outline MVP milestones and long‑term ambitions.

<!-- TASK:FS08 status=done -->
* [x] **FS08 – README scaffold** — quick‑start + high‑level pitch.

<!-- TASK:FS09 status=done -->
* [x] **FS09 – Makefile helpers** — `make setup lint test run_tasks`.

<!-- TASK:FS10 status=done -->
* [x] **FS10 – Ruff & Black** — formatting/flake8 parity; pre‑commit config.

<!-- TASK:FS11 status=done -->
* [x] **FS11 – Pytest smoke** — empty test to keep CI green.

<!-- TASK:FS12 status=done -->
* [x] **FS12 – Bandit CI** — basic security scan.

<!-- TASK:FS13 status=done -->
* [x] **FS13 – GitHub Actions CI** — lint+test matrix.

<!-- TASK:FS14 status=done -->
* [x] **FS14 – mkdocs site** — docs auto‑build.

<!-- TASK:FS15 status=done -->
* [x] **FS15 – Roadmap parser** — code that lists `status=pending` tasks from this file. *(done 2025-05-20)*

<!-- TASK:FS16 status=done -->
* [x] **FS16 – Status updater** — helper to flip `status=in_progress/done` in place.

<!-- TASK:FS17 status=done -->
* [x] **FS17 – Filesystem tool** — add ADK tool pointing at `http://localhost:8787`.

<!-- TASK:FS18 status=done -->
* [x] **FS18 – GitHub tool** — add ADK tool for commits/PRs via `http://localhost:8788`.

<!-- TASK:FS19 status=done -->
* [x] **FS19 – Task loop** — `scripts/run_tasks.py` pulls first pending task, invokes agent, updates status.

<!-- TASK:FS20 status=pending -->
* [ ] **FS20 – Auto‑PR** — after edits, push branch `capx/FSxx‑<slug>` & open PR with template.

<!-- TASK:FS21 status=pending -->
* [ ] **FS21 – Debrief file** — agent writes `reports/FSxx_debrief.md` summarising work.

<!-- TASK:FS22 status=pending -->
* [ ] **FS22 – Debrief in PR** — embed or link the debrief in the PR description.

<!-- TASK:FS23 status=pending -->
* [ ] **FS23 – Register remote MCP servers** — add `configs/mcp_servers.yaml` (Filesystem & GitHub endpoints).

<!-- TASK:FS24 status=pending -->
* [ ] **FS24 – Responses‑API client wrapper** — helper that calls Deep‑Research/Responses API with `tool_server_url`.

<!-- TASK:FS25 status=pending -->
* [ ] **FS25 – Remove local FastAPI bootstraps** — drop local server scripts & related CI steps.

<!-- TASK:FS26 status=pending -->
* [ ] **FS26 – MCP smoke‑test in CI** — pytest hits `/health` on remote MCP servers via Responses API.

<!-- TASK:FS27 status=pending -->
* [ ] **FS27 – Deep Research wrapper tool** — call Deep Research API or headless Playwright; store audit markdown in `reports/`.

<!-- TASK:FS28 status=pending -->
* [ ] **FS28 – Codex automation harness** — programmatic interface or Playwright driver; triggers task prompt, saves patches & logs.

<!-- TASK:FS29 status=pending -->
* [ ] **FS29 – Orchestrator agent MVP** — orchestrates Deep‑Research Planner and Codex harness; loops tasks until none pending, schedules next cycle.

<!-- TASK:FS30 status=pending -->
* [ ] **FS30 – Cost monitor & throttle** — track monthly token spend; halt cycles when spend nears budget cap.

<!-- TASK:FS31 status=pending -->
* [ ] **FS31 – Knowledge graph index** — add DuckDB/Chroma vector store for code base.

<!-- TASK:FS32 status=pending -->
* [ ] **FS32 – Search tool** — agent tool to query the vector store.

<!-- TASK:FS33 status=pending -->
* [ ] **FS33 – Session memory** — persist last N debriefs to JSON; feed them into agent context.

<!-- TASK:FS34 status=pending -->
* [ ] **FS34 – Planner ➜ Engineer ➜ Verifier** — multi‑agent roles, handshake schema.

<!-- TASK:FS35 status=pending -->
* [ ] **FS35 – Unit tests & safety rails** — pytest smoke tests, Ruff/Black CI enforcement, write‑whitelist.

<!-- TASK:FS36 status=pending -->
* [ ] **FS36 – Pluggable model backend** — LiteLLM config file to swap Codex with local model easily.

<!-- TASK:FS37 status=pending -->
* [ ] **FS37 – Natural‑language goal intake** — CLI or API endpoint that converts a plain‑English goal into FS‑tasks.

<!-- TASK:FS38 status=pending -->
* [ ] **FS38 – Plugin Discovery** — detect opportunities to replace custom code with MIT/Apache libraries.

<!-- TASK:FS39 status=pending -->
* [ ] **FS39 – Plugin Voting** — evaluate candidate plugins for correctness & community health.

<!-- TASK:FS40 status=pending -->
* [ ] **FS40 – Plugin Benchmark** — compare plugin performance & correctness vs. existing implementation.

<!-- TASK:FS41 status=pending -->
* [ ] **FS41 – Auto‑Wrap Integration** — refactor code to use approved plugin via wrapper/adapter.

<!-- TASK:FS42 status=pending -->
* [ ] **FS42 – PR Bot Automation** — bot manages plugin‑integration PRs; auto‑merge on green CI per policy.

<!-- TASK:FS43 status=pending -->
* [ ] **FS43 – Nightly “Borg” Run** — scheduled job runs agent in maintenance mode to assimilate improvements.

---
