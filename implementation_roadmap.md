# CAP-X Implementation Roadmap (v2 – 2025-05-18)

## Who is this for?
You – a solo developer who wants an autonomous dev agent without drowning in details.  
Each phase is sized so you can finish a task or two in a single evening.

---

### Phase 1 · First Working Loop (Weeks 1 – 2)

| FS ID | Task | Outcome |
|-------|------|---------|
| FS04  | **Stub the agent** – add `agents/dev_agent.py` | Repo imports without errors |
| FS07  | **Add `.gitignore`** | Keeps cache & `node_modules` out of Git |
| FS09‒10 | **One-click MCP scripts** | `./run_filesystem.sh` & `./run_github.sh` start local servers |
| FS12‒14 | **Minimal agent + CI bootstrap** | Model answers, and CI ensures setup never breaks |
| **Phase result** | Running `python scripts/run_tasks.py --dry-run` shows the agent talking |

---

### Phase 2 · Automated PRs (Weeks 3 – 4)

| FS ID | Task | Outcome |
|-------|------|---------|
| FS15‒16 | **Parse & update roadmap** | Agent sees pending tasks and marks them done |
| FS17‒18 | **Wire filesystem & GitHub tools** | Agent edits code and pushes branches |
| FS19‒22 | **Loop + PR + debrief** | One command ➜ code change ➜ PR with summary |
| **Phase result** | You just review PRs instead of micromanaging the agent |

---

### Phase 3 · Strategic Power-ups (Weeks 5 – 8)

| FS ID | Task | Outcome |
|-------|------|---------|
| FS23‒24 | **Optional research/debug tools** | Agent can fetch docs, search code, parse stack traces |
| FS25 | **Session memory** | Remembers context across runs |
| FS26 | **Planner → Engineer → Verifier** | High-level goal broken into tasks & self-reviewed |
| FS27 | **Tests & safety rails** | PRs fail fast if build/tests break |
| FS28 | **Pluggable model backend** | Swap OpenAI Codex for a local model anytime |
| FS29 | **Natural-language goal intake** | Tell CAP-X *what*, it figures *how* |
| **Phase result** | A fully autonomous, self-reviewing, extensible dev companion |

---

**How to use this roadmap**

1. Pick the **topmost pending FS task**.  
2. Open a feature branch named `capx/FSxx-short-slug`.  
3. Complete the task, open a PR, and tick it off in `configs/ROADMAP_TODO.md`.

_Updated 2025-05-18._
