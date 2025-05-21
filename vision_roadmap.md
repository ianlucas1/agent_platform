# Vision & Roadmap

## One‑Command Autonomous Dev Platform

The north‑star is **a single CLI** that accepts a plain‑English goal then, without any human touch, runs a Planner → Coder → Verifier loop until the improvement is merged.

---

## Phases

| Phase | Scope | Key Feature Steps |
|-------|-------|-------------------|
| **0 – Foundations (✅)** | Deterministic offline bootstrap, lint/test CI, empty agent stubs | FS01‑16 |
| **1 – Plumbing (🚧)** | Filesystem & GitHub tools, task loop, auto‑PR, debrief file/PR | FS17‑22 |
| **2 – Core Automation** | **Remote MCP integration + unattended Planner → Coder** | **FS23‑26** |
| **3 – Knowledge & Memory** | Vector search, session memory, multi‑agent roles, write‑safety | FS27‑33 |
| **4 – Plugin Ecosystem** | Discovery, voting, benchmark & auto‑wrap integration | FS34‑38 |
| **5 – Self‑Healing** | Nightly “Borg” maintenance run assimilates improvements | FS39 |

> **2025‑05‑21:** Former FS30A‑D became **FS23‑26** and were pulled into Phase 2 to unlock the Remote MCP workflow sooner.

---

## Success Criteria

1. **Plumbing:** An ADK agent edits files, pushes a branch, opens a PR with a debrief; CI stays green.  
2. **Core Automation:** A cron‑driven orchestrator calls Deep Research (Planner) via **remote MCP servers** and Codex (Coder); cost monitor halts if nearing budget.  
3. **Knowledge & Memory:** Agents answer context‑heavy questions without rescanning GitHub; previous debriefs are recalled.  
4. **Plugin Ecosystem:** The system benchmarks and adopts best‑of‑breed open‑source replacements automatically.  
5. **Self‑Healing:** Nightly run fixes lint, updates deps, and merges safe PRs without help.

---

## Budget Guardrails

* Primary compute stays **inside the ChatGPT Pro plan** (Deep Research & Codex via web).  
* OpenAI/Gemini API keys used sparingly; Prometheus cost monitor (FS30) enforces the quota.

---

## Current Focus

🚀 **Finish FS23‑26** – register remote MCP servers, drop local FastAPI bootstraps, wrap the Responses API, and smoke‑test the endpoints – to prove the fully unattended Planner → Coder loop. Everything else is polish once that backbone is solid.
