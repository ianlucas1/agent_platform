# Vision & Roadmap

## One‑Command Autonomous Dev Platform

The long‑term goal is **a single CLI entry‑point** that accepts a plain‑English goal and then, without human intervention, runs a Planner → Coder → Reviewer loop until the improvement is shipped and merged.

---

## Phases

| Phase | Scope | Key Feature Steps |
|-------|-------|-------------------|
| **0 – Foundations (✅)** | Deterministic offline bootstrap, lint/test CI, empty agent stubs | FS01‑16 |
| **1 – Plumbing (🚧)** | Filesystem & GitHub tools, task loop, auto‑PR, debrief file/PR integration | FS17‑22 |
| **2 – Core Automation** | **Moved forward** to unlock headless Planner → Coder → Reviewer ASAP | **FS23‑26** |
| **3 – Knowledge & Memory** | Vector search, session memory, multi‑agent roles, write‑safety | FS27‑33 |
| **4 – Plugin Ecosystem** | Discovery, voting, benchmark & auto‑wrap integration | FS34‑38 |
| **5 – Self‑Healing & Nightlies** | Nightly “Borg” maintenance run assimilates improvements | FS39 |

> **Change‑log 2025‑05‑21:** Former FS30A‑D renamed **FS23‑26** and pulled into Phase 2 to accelerate end‑to‑end automation.

---

## Success Criteria per Phase

1. **Plumbing:** An ADK agent can edit files, push a branch, open a PR, and attach a debrief; CI stays green.  
2. **Core Automation:** A cron‑driven orchestrator calls Deep Research (Planner) and Codex (Coder); token spend monitor halts if nearing budget.  
3. **Knowledge & Memory:** Agents answer context‑heavy questions without re‑scraping GitHub; previous debriefs are recalled.  
4. **Plugin Ecosystem:** The system routinely benchmarks and swaps in best‑of‑breed open‑source replacements.  
5. **Self‑Healing:** Nightly run fixes lint, updates deps, and merges safe PRs automatically.

---

## Budget Guardrails

* Primary compute stays **within the ChatGPT Pro plan** (Deep Research & Codex via web).  
* OpenAI/Gemini API keys used sparingly; the Prometheus cost monitor (FS26) enforces quota.

---

## Current Focus

🚀 **Finish FS17‑26** to prove the unattended Planner → Coder → Reviewer loop. Everything else is polish once that backbone is solid.
