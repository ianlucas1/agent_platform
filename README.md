# Agent Platform

A turn‑key starter kit for building a **Planner → Coder → Reviewer** multi‑agent loop.  
Plug in OpenAI’s Deep Research (Planner) and Codex (Coder/Verifier) and let the platform ship pull‑requests **autonomously**.

---

## Why this exists

* **Single‑command UX** – Run `make run_tasks` and the agents plan, code, review, and open a PR.  
* **Deterministic bootstrap** – Offline wheel cache & MCP servers guarantee reproducible runs.  
* **Budget‑aware** – Prometheus counter halts jobs when token spend nears your cap.  
* **Incremental roadmap** – Feature Steps (FS) keep scope small and CI green at every stage.

---

## Current Roadmap Snapshot

| Phase | Purpose | Feature Steps |
|-------|---------|---------------|
| Foundations | Offline bootstrap, lint/test CI | **FS01‑16** ✔️ |
| **Plumbing** | Filesystem & GitHub tools, task loop, auto‑PR, debrief | **FS17‑22** |
| **Core Automation (in‑flight)** | Deep Research + Codex orchestration, cost monitor | **FS23‑26** |
| Knowledge & Memory | Vector search, session memory, multi‑agent roles | FS27‑33 |
| Plugin Ecosystem | Discover, benchmark, auto‑wrap libraries | FS34‑38 |
| Self‑Healing | Nightly “Borg” run assimilates improvements | FS39 |

We recently **renumbered FS23‑26** (formerly 30A‑D) and pulled them forward to accelerate unattended automation.

---

## Quick Start

```bash
git clone https://github.com/ianlucas1/agent_platform.git
cd agent_platform
make setup         # installs Python/Node toolchain with offline wheels
make lint test     # run Ruff, Black, Bandit, Pytest
make run_tasks     # invoke the task orchestrator (once FS17‑26 are complete)
```

> **Note:** Until FS17‑22 land, `run_tasks` is a no‑op. Follow the issues/PRs for progress.

---

## Repo Tour

| Path | What lives there |
|------|------------------|
| `agents/` | ADK agent definitions and tools |
| `configs/` | [`ROADMAP_TODO.md`](configs/ROADMAP_TODO.md), settings |
| `mcp_servers/` | Filesystem & GitHub mock servers for offline runs |
| `reports/` | Planner audits and Reviewer debriefs |
| `scripts/` | Bootstrap, task loop, helper utilities |
| `docs/` | MkDocs site (auto‑built on CI) |

---

## Contributing

1. Pick the next **`[ ]`** task in `configs/ROADMAP_TODO.md`.  
2. Create a branch `capx/FSXX-short-slug`.  
3. Follow the coding standards (`ruff`, `black`).  
4. Push and open a PR – CI must pass.  
5. The Reviewer agent (or a maintainer) will merge when green.

See **AGENTS.md** and **LLM_COLLABORATOR.md** for collaboration SOPs.

---

## License

MIT. Have fun!
