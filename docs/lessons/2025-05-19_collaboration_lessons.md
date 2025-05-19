# CAP-X Deep-Research retrospective  
*Session date 2025-05-19 • author: ChatGPT (DR agent)*

## 1 Timeline recap
| Time (UTC) | Milestone |
|------------|-----------|
| 19:00 | FS04 stub DevAgent merged |
| 19:25 | MCP launch scripts (FS09, FS10) merged |
| 19:45 | AGENTS.md prompt-checklist + roadmap hygiene |
| 20:10 | FS12 minimal ADK DevAgent merged |
| 20:40 | Assumptions-check SOP invented & first run |
| 21:00 | Roadmap + chmod micro-PR merged |
| 21:30 | FS14 CI workflow added → Ubuntu green, macOS red |
| 22:00 | Session paused (cognitive overload) |

## 2 What worked well
* **Tight task scoping** (one FS item per prompt) kept Codex reliable.  
* **Road-map HTML markers** drove clear automation feedback loops.  
* **Assumptions-check template** caught drift early (e.g. ROADMAP status, `+x` bits).  
* **Bootstrap smoke-checks** surfaced missing tools instantly.  
* **CI matrix** replicated Linux vs macOS quirks we would have missed locally.

## 3 Pain points & root causes
| Issue | Root cause | Fix |
|-------|------------|-----|
| Branch proliferation (`add-github-actions-ci-workflow-…`) | Codex defaults to new branch if not told otherwise | Always start prompt with `# Branch: <name>` when iterating |
| macOS CI failure (PEP 668) | Home-brew Python blocks global pip | Add `export PIP_BREAK_SYSTEM_PACKAGES=1` in Darwin block |
| Ubuntu CI failure (no sudo) | Runners are non-root | `apt_get` helper with sudo fallback |
| Cognitive overload | Too many intertwined steps | Adopt **one-change PR** rule & micro-checklist |

## 4 Stable SOP additions
### 4.1  Assumptions-check
* Run **before** planning large tasks.  
* Table format: `| # | PASS/FAIL | Evidence |`  
* If any FAIL → patch repo **or** revise assumption first.

### 4.2  Bootstrap-script guardrails
1. Detect OS (`Linux`/`Darwin`).  
2. **sudo** fallback for `apt-get`.  
3. `export PIP_BREAK_SYSTEM_PACKAGES=1` for macOS.  
4. Print “✅ Bootstrap complete – NO_NET=1 exported”.

### 4.3  Branch & PR rules
* One FS task ↔ one branch ↔ one PR.  
* Name: `capx/FS<ID>-slug`.  
* Commit prefix: `feat|fix|docs|ci|chore (FS<ID>)`.

## 5 Action items open after this session
| FS ID | Task | Notes |
|-------|------|-------|
| **FS14** | *CI bootstrap* | macOS leg still red – needs PIP env-var fix |
| **FS13** | DevAgent docstring | Low-effort docs, follows FS12 |
| **FS15** | Road-map parser | Enables the automation loop |
| **FS16** | Status updater helper | Works with FS15 |
| **Create** | `DEEP_RESEARCH.md` | Contains SOP (assumptions-check, log review, bootstrap rationale) |

## 6 Key take-aways for future DR agents
* Start every deep dive with an **assumptions-check**.  
* Treat `scripts/bootstrap.sh` as **single source of truth**—any CI or sandbox issue likely lives here.  
* Explicitly tell Codex which branch to reuse to avoid “-randomhash” branches.  
* When overwhelmed, collapse to one-change PRs and iterate; small green steps beat big red leaps.
