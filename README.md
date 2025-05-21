# Agent Platform

A turn‑key starter kit for building a **Planner → Coder → Verifier** multi‑agent loop.  
Connect to OpenAI’s Deep Research (Planner) and Codex (Coder/Reviewer) through **remote MCP servers** and let the platform ship pull‑requests *autonomously*.

---

## Why this exists

* **Single‑command UX** – `make run_tasks` plans, codes, reviews, and opens a PR.  
* **Deterministic bootstrap** – Offline wheel cache; external APIs accessed via declarative MCP servers.  
* **Budget‑aware** – Prometheus counter halts jobs when token spend nears your cap.  
* **Incremental roadmap** – Feature Steps (FS) keep scope small and CI green at every stage.

---

## Roadmap Snapshot (2025‑05‑21)

| Phase | Purpose | Feature Steps |
|-------|---------|---------------|
| Foundations | Offline bootstrap, lint/test CI | **FS01‑16** ✔️ |
| **Plumbing** | Filesystem & GitHub tools, task loop, auto‑PR, debrief | **FS17‑22** |
| **Core Automation (in‑flight)** | **Remote MCP + unattended Planner/Coder** | **FS23‑26** |
| Knowledge & Memory | Vector search, session memory, multi‑agent roles | FS27‑33 |
| Plugin Ecosystem | Discover, benchmark, auto‑wrap libraries | FS34‑38 |
| Self‑Healing | Nightly “Borg” run assimilates improvements | FS39 |

---

## Quick Start

```bash
git clone https://github.com/ianlucas1/agent_platform.git
cd agent_platform
make setup          # installs Python/Node toolchain with offline wheels
make lint test      # Ruff, Black, Bandit, Pytest
make run_tasks      # orchestrator (requires FS23‑26 complete)
```

> Until FS23‑26 land, `run_tasks` is a no‑op; follow the issues/PRs for progress.

---

## Repo Tour

| Path | Contents |
|------|----------|
| `agents/` | Agent definitions & tools |
| `configs/` | [`ROADMAP_TODO.md`](configs/ROADMAP_TODO.md), settings |
| `mcp_servers/` | *Legacy* mock servers (to be removed in FS25) |
| `reports/` | Planner audits & Verifier debriefs |
| `scripts/` | Bootstrap, task loop, utilities |
| `docs/` | MkDocs site (auto‑built on CI) |

---

## Contributing

1. Pick the next **unchecked** task in `configs/ROADMAP_TODO.md`.  
2. Create a branch `capx/FSXX-short-slug`.  
3. Follow coding standards (`ruff`, `black`).  
4. Push & open a PR – CI must pass.  
5. The Reviewer agent (or a maintainer) will merge when green.

See **AGENTS.md** and **LLM_COLLABORATOR.md** for SOPs.

---

## License

MIT. Build cool things!
