# Deep Research – Standard Operating Procedures  
*codex_agent_platform*

This guide distills the **current** best practices for collaborating with Codex web agents in this repository.  
It is to remain version‑agnostic—no task numbers or dated milestones—so it remains valid as the roadmap evolves.

---

## 0 Share the Current Setup Script

**Before any agent prompt (Ask Mode or Code Mode):**

1. Request the exact contents of the *environment‑setup script* configured in the Codex UI so assumptions reflect the live sandbox.

---

## 1 Golden Rules

1. **Begin with an assumptions‑check** (Section 2).  
2. Read **AGENTS.md** first—branching, lint, and CI conventions live there.  
3. One clear goal per prompt—Codex is most reliable with tightly scoped tasks.  
4. Maintain **ROADMAP_TODO.md** status ticks to prevent duplicate work.  
5. Embed *acceptance‑criteria* bullets so Codex can prove success in its logs.  
6. Show lint/test output (ruff · black · bandit · pytest) in every Code Mode run.  
7. Respect sandbox limits: no outbound net after `NO_NET=1`, CPU‑only, ≈4 GB RAM.

---

## 2 Assumptions‑Check Prompt Template

See **docs/prompt_templates/assumptions_check.md** for a copy‑ready scaffold.  
Always supply it to Codex as a downloadable `.txt` file—no narrative wrapper.

*Run on* **main** only; no branch creation; result is a TRUE/FALSE table.

---

## 3 Codex‑Web Agent — Capabilities & Limits

| Can | Cannot |
|-----|--------|
| Edit code, run lints/tests, stage commits. | Push, open PRs, merge, or view CI directly. |
| Read full repo (esp. AGENTS.md). | Access internet after `NO_NET=1`. |

---

## 4 Bootstrap Expectations

`scripts/bootstrap.sh` must:

* Install Python 3, pip, Node, npm.  
* `pip install -r requirements.txt` (includes **google‑adk** & **litellm**).  
* `pip install -r requirements-dev.txt` (pinned ruff, black, bandit).  
* Gracefully handle apt/brew differences, set `PIP_BREAK_SYSTEM_PACKAGES=1`.  
* Export `NO_NET=1` and print success.

---

## 5 Prompt Templates

Templates live in **docs/prompt_templates**:

| File | Purpose |
|------|---------|
| **assumptions_check.md** | Verifies repo state on `main`. |
| **tasking.md** | Creates `codex/…` branch, applies patches, commits, ends with `echo DONE`. |

> **Copy prompts as downloadable `.txt` files (via `python_user_visible`)—no narrative text—to avoid UI escaping issues for *every* prompt, short or long.*

---

## 6 Codex Task SOP – Full Workflow

| Step | Who | Action |
|------|-----|--------|
| **0. Provide setup script** | Human | Paste current environment‑setup script. |
| **1. Assumptions check** | Codex | Use template; human reviews table. |
| **2. Write task prompt** | Human | Derive from `tasking.md`; include branch, patches, tests, `echo DONE`. |
| **3. Codex runs Code Mode** | Codex | Shows diff, lint/test output, ends **DONE**. |
| **4. Push & PR** | Human | Click **Push ▾ / Create PR**; watch CI. |
| **5. Optional doc sync** | Codex or Human | Update README.md, AGENTS.md, DEEP_RESEARCH.md to reflect work done. |
| **6. Optional debrief** | Codex | Save `reports/<task>_debrief.md` (what changed, assumptions, limits). |

---

## 7 Error Signals to Watch

* `ModuleNotFoundError` → dep missing in requirements.  
* `Permission denied` → forgot `chmod +x`.  
* Network call after `NO_NET=1` → late install or external API.  
* Ruff/Black/Bandit fail → lint rules violated or tool missing.

---

## 8 UI & Workflow Tips

* **Assumptions check runs on `main`**, no branch hints.  
* **Push controls appear** when branch name starts with `codex/…` and the task exits cleanly (`echo DONE`).  
  If “unknown error” hides the button but a commit exists, run a no‑op follow‑up task or use the Push menu.

---

*Updated 2025-05-20*
