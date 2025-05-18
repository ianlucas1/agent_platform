<!-- docs/lessons/2025-05-18_deep_research_follow-up.md -->

# Deep-Research Follow-up — Key Learnings & Heuristics

*codex-agent-platform • 18 May 2025*

---

## 1 Context

This note distils insights gathered while auditing and extending the **codex\_agent\_platform** through FS02 – FS03 and the bootstrap-offline hardening work.
It is written for **future Deep-Research agents** so they can shortcut discovery time and avoid recurring pitfalls.

---

## 2 Repository & Process Insights

| Area            | Current state (May 2025)                                                                        | Recommendation / guard-rail                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Task queue**  | `configs/ROADMAP_TODO.md` with `<!-- TASK:FSNN status=... -->` comments; FS01-03 marked `done`. | Keep this single source of truth. Always sync `implementation_roadmap.md` after closing tasks to avoid drift. |
| **Bootstrap**   | Installs Python/Node/MCP; honours `NO_NET` flag; Linux branch exits if no root privileges.      | Future packages → vendor wheels or set up cache; CI job should export `NO_NET=1` to cover sandbox case.       |
| **Repo layout** | `agents/`, `mcp_servers/`, `scripts/`, `reports/`, `docs/`, etc. skeleton in place.             | When adding new dirs, include `.gitkeep` and document in README table.                                        |
| **Docs**        | Minimal `README.md`, offline guide, contributor guide (`AGENTS.md`).                            | README should always show **Quick-start**, env-vars, and roadmap snapshot.                                    |
| **CI**          | Workflow only runs bootstrap syntax-check (planned FS14).                                       | Expand matrix to macOS+Ubuntu; add Ruff/Black/Bandit lint steps once style guide lands.                       |
| **Security**    | Agent toolset still limited to FS & GitHub MCP; no destructive ops allowed.                     | Introduce FS write-whitelist (`/workspace/app/src/**`) before adding more tools.                              |

---

## 3 Codex-Cloud Constraints Cheatsheet

Constraint IDs below are referenced across docs & prompts.

| #  | Constraint                  | Impact                  | Mitigation                            |
| -- | --------------------------- | ----------------------- | ------------------------------------- |
| 1  | No outbound net after setup | Pip/npm fail            | Pre-cache deps, `NO_NET=1` guard      |
| 2  | Ephemeral VM                | Lost state on idle      | Checkpoint to `reports/`              |
| 3  | Single container, no DinD   | No services like Redis  | Use SQLite / mock layers              |
| 4  | Non-root user               | `sudo` forbidden        | Attempt `apt-get` only if root        |
| 5  | CPU-only, 4 GB              | Large builds slow       | Use lightweight models                |
| 6  | Limited port expose         | 5 ports max             | Re-use 8787/8788, kill after tests    |
| 7  | File-explorer diff noise    | Large artefacts clutter | `.gitignore` `node_modules` etc.      |
| 8  | Linear git history UI       | Force-push confusing    | Always additive commits               |
| 9  | No background cron          | Long loops die          | Use `--max-tasks` flag + CI triggers  |
| 10 | 30 min idle timeout         | Lost shells             | Script checkpoints + small iterations |

---

## 4 Recommended Agent Loop Architecture

```
Human (objective)  →  Planner Agent  →  Executor Agent  →  Verifier Agent  →  PR
         ↑                                                                         ↓
         └─────────────── Reflection / re-plan every N tasks ───────────────────────┘
```

* **Planner** emits 3-10 atomic tasks → `ROADMAP_TODO.md`.
* **Executor** works one task per run with MCP tools, opens PR, writes `reports/NNN_debrief.md`.
* **Verifier** runs Ruff/Black/Bandit/tests, comments confidence; can auto-close bad PRs.
* **Human** only sets high-level objectives and reviews PRs.

---

## 5 Roadmap Snapshot

*Done (✓)*: FS01 Bootstrap skeleton • FS02 Dependencies install • FS03 Repo scaffold
*Next*: FS04 stub `agents/dev_agent.py` → FS12 minimal ADK agent → FS14 CI lint matrix

---

## 6 Immediate Infra Upgrades Worth Automating

1. **Style baseline** – add `pyproject.toml` (Black, Ruff, isort) and `.editorconfig`; gate via CI.
2. **Docstring template** – `docs/style/docstring_template.md` so agents paste compliant docstrings.
3. **Stub typings** – `stubs/mcp.pyi` for MCP APIs; run `mypy` later.
4. **Write-whitelist** – configure FS MCP to restrict write paths before enabling file-deleting tools.
5. **Reflection checkpoint** – every 5 tasks, Planner reviews progress vs. objective.

---

## 7 Key Heuristics for Future Deep-Research Agents

* **Change one layer per PR** – infra, agent code, docs, or roadmap, but not all together.
* **Fail fast** – run `bash -n`, `ruff --fix`, `black .` locally before invoking CI to save tokens.
* **Document constraints** – reference Constraint #n instead of restating sandbox details in every PR.
* **Always update both roadmap files** to keep human reviewers and agents aligned.
* **Checkpoint early** – new lessons go under `docs/lessons/` with ISO-date prefix for easy diffing.

---

*End of file*
