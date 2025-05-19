### 🧠 `DEEP_RESEARCH.md`

# Deep Research – Standard Operating Procedures  
*codex_agent_platform · established 2025-05-19*

This guide distills every hard-won lesson about running Deep Research and Codex web agents in this repository. Follow it **before** drafting any new research prompt or technical roadmap.

---

## 1 ▪ Golden rules

| # | Rule | Why it matters |
|---|------|----------------|
| 1 | **Start with an assumptions-check** (section 2) | Keeps mental models in sync with the evolving codebase. |
| 2 | **Read `AGENTS.md` first** | Codex adapts to its branching, lint, and CI conventions. |
| 3 | **One clear goal per prompt** | Codex is most reliable with tightly scoped tasks. |
| 4 | **Always mark the previous FS task done** (`ROADMAP_TODO.md`) | Prevents duplicate work and drives the task loop. |
| 5 | **Embed acceptance-criteria bullets** | Lets Codex prove success (or show failures) in its logs. |
| 6 | **Show lint / test output** (`ruff`, `black`, `bandit`, `pytest`) | Reviewers see green checks inline; failures surface early. |
| 7 | **Respect sandbox limits** – no outbound net after `NO_NET=1`, CPU-only, 4 GB RAM | Heavy models or late installs will crash the run. |

---

## 2 ▪ Assumptions-check template

Deep Research should **verify repo state before planning**. Paste the skeleton below into a Codex task whenever major structure or tooling may have changed. Adjust assumptions as needed.

# 🔍  Assumptions-check Task

# Instructions:

# 1. Inspect the main branch.

# 2. Respond in a MARKDOWN table:

# | # | PASS/FAIL | Evidence |

# 3. No code changes; read-only.

# 4. End with the word “Done”.

## Assumptions

1. scripts/bootstrap.sh installs dev tools via requirements-dev.txt.
2. requirements-dev.txt pins ruff, black, bandit to fixed versions.
3. AGENTS.md contains the heading “Prompt checklist”.
4. ROADMAP\_TODO.md lists FS07 ... FS10 as status=done.
5. .github/workflows/bootstrap.yml does NOT yet exist.
6. mcp\_servers/\*.sh are executable.
7. agents/dev\_agent.py imports from google.adk and returns "pong".
8. NO\_NET=1 is exported at end of bootstrap.

If any row **FAIL**s, fix the repo **or the assumption** before proceeding with planning.

---

## 3 ▪ Codex-web agent capabilities & limits

* **Can:** edit code, run tests/lint, create commits, stage branches.
* **Cannot:** push, open PRs, merge, or inspect CI outcomes.
* **Reads:** anything in the repo (esp. `AGENTS.md`).
* **Requires:** accurate assumptions, branch naming, and acceptance bullets.
* **Goes offline after bootstrap:** nothing can be downloaded post-`NO_NET=1`.

---

## 4 ▪ Bootstrap expectations

| Item | Expected in `scripts/bootstrap.sh` |
|------|----------------------------|
| Core runtimes | `python3 pip3 node npm` (Ubuntu 24.04 → Python 3.12). |
| Core deps | `pip install google-adk litellm`. |
| Dev deps | `pip install -r requirements-dev.txt` (ruff==0.11.10, black==25.1.0, bandit==1.7.7). |
| Quiet flags | `apt-get -qq`, `npm --quiet --no-fund --omit=dev`. |
| Safety | `trap 'BOOTSTRAP FAILED on line $LINENO' ERR`. |
| Offline flag | `export NO_NET=1` and “✅ Bootstrap complete” printed at end. |

---

## 5 ▪ Prompt checklist (quick copy)

* Mark previous FS task done in ROADMAP\_TODO.md.
* Single clear goal (one FS task).
* List acceptance bullets (objectively testable).
* Branch name: capx/FS<ID>-slug.
* Include ruff, black, bandit (and pytest if present).
* End with “# Begin.” to cue Codex.

---

## 6 ▪ Codex Task SOP – End-to-End Workflow

### 6.1 Pre-task: Bootstrap & Assumptions

1. **Check the Codex Environment UI** (https://chatgpt.com/codex/settings/)
   - Confirm setup script includes:
     - `PIP_BREAK_SYSTEM_PACKAGES=1` for macOS
     - `export NO_NET=1` as final line
     - All required tools in apt/brew + pip
   - If setup is incomplete → patch `scripts/bootstrap.sh` and commit.

2. **Generate task-specific assumptions-check**
   - Use template in §2 and adjust assumptions based on the FS task ahead.
   - Deliver this to Codex first, before prompting work.

---

### 6.2 Task Prompting

1. **Write one-task prompt** per FS item.
2. **Include:**
   - Summary of goal.
   - Acceptance bullets.
   - Branch name: `capx/FS<ID>-slug`.
   - Expected commits, file changes, and CI prep steps.
3. **End with:**  
   ```bash
   # Begin.

---

### 6.3 Output Review

1. Share Codex's diffs + logs with Deep Research.
2. Look for:

   * Agent confusion or hallucination
   * Broken assumptions (wrong file paths, test names, etc.)
   * Missing env flags, silent errors
3. If work is clean, **you (human) push PR** to trigger CI.

---

### 6.4 CI Handling

1. If CI fails:

   * Ask Codex to `gh pr view --web` or `gh run list` to inspect failure.
   * Agent should patch and recommit.
2. You must push; Codex cannot.
3. Be aware:

   * Pushing a new commit to the same branch updates the PR.
   * Avoid opening duplicate PRs from Codex unless task requires it.
4. Optionally consolidate PR lineage post-merge if needed.

---

### 6.5 Task Debrief (Optional)

1. Prompt Codex to write a **short markdown debrief**:

   * What it did
   * What assumptions were tested
   * Any known limitations or TODOs
2. Store in:

   ```
   agent_logs/FS<ID>_debrief.md
   ```
3. Flag tasks with structural lessons learned for future prompt refinement.

---

## 7 ▪ Task-log & failure interpretation

| Look for                               | Meaning                    | Action                                   |
| -------------------------------------- | -------------------------- | ---------------------------------------- |
| `ModuleNotFoundError`                  | Missing pip package.       | Add to `requirements*.txt` or vendor it. |
| `Permission denied`                    | Script isn’t executable.   | `chmod +x` and commit.                   |
| `OpenAI/network error` post-`NO_NET=1` | Late API call attempt.     | Stub or move to online phase.            |
| `ruff / black / bandit` fails          | Formatting issues.         | Codex needs clearer rules.               |
| `bandit N/A`                           | Bandit wheel not vendored. | Pin in dev reqs.                         |

---

## 8 ▪ Future improvements

* Add “assumptions-check” as CI job.
* Create long-term memory tooling for agent retrospectives.
* Support headless Codex invocation with prefilled env + SOP references.

---

*Updated 2025-05-20.*
