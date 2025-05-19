### 📘 Final Content of `DEEP_RESEARCH.md`

```markdown
# Deep Research – Standard Operating Procedures  
*codex_agent_platform · established 2025-05-19*

This guide distills every hard-won lesson about running Deep Research and Codex web agents in this repository. Follow it **before** drafting any new research prompt or technical roadmap.

---

## 1 ▪ Golden Rules

| # | Rule | Why it matters |
|---|------|----------------|
| 1 | **Start with an assumptions-check** (section 2) | Keeps mental models in sync with the evolving codebase. |
| 2 | **Read `AGENTS.md` first** | Codex adapts to its branching, lint, and CI conventions. |
| 3 | **One clear goal per prompt** | Codex is most reliable with tightly scoped tasks. |
| 4 | **Always mark the previous FS task done** (`ROADMAP_TODO.md`) | Prevents duplicate work and drives the task loop. |
| 5 | **Embed acceptance-criteria bullets** | Lets Codex prove success (or show failures) in its logs. |
| 6 | **Show lint/test output** (`ruff`, `black`, `bandit`, `pytest`) | Reviewers see green checks inline; failures surface early. |
| 7 | **Respect sandbox limits** – no outbound net after `NO_NET=1`, CPU-only, 4 GB RAM | Heavy models or late installs will crash the run. |

---

## 2 ▪ Assumptions-Check Template

Paste the following into Codex when planning tasks that depend on CI, environment, or tooling setup. Adjust items as needed.

```

# 🔍  Assumptions-check Task

## Instructions:

1. Inspect the main branch.
2. Respond in a MARKDOWN table:
   \| # | PASS/FAIL | Evidence |
3. No code changes; read-only.
4. End with the word “Done”.

## Assumptions

1. scripts/bootstrap.sh installs dev tools via requirements-dev.txt.
2. requirements-dev.txt pins ruff, black, bandit to fixed versions.
3. AGENTS.md contains the heading “Prompt checklist”.
4. ROADMAP\_TODO.md lists FS07 ... FS10 as status=done.
5. .github/workflows/bootstrap.yml does NOT yet exist.
6. mcp\_servers/\*.sh are executable.
7. agents/dev\_agent.py imports from google.adk and returns "pong".
8. NO\_NET=1 is exported at end of bootstrap.

```

If any row **FAIL**s, patch the repo or assumptions before proceeding.

---

## 3 ▪ Codex-Web Agent Capabilities & Limits

- **Can:** edit code, run tests/lint, create commits, stage branches.
- **Cannot:** push, open PRs, merge, inspect CI results.
- **Reads:** anything in the repo (esp. `AGENTS.md`).
- **Requires:** valid assumptions, clear prompt structure, correct branch naming.
- **Offline after bootstrap:** all dependencies must be installed before `NO_NET=1`.

---

## 4 ▪ Bootstrap Expectations

| Item | Expected in `scripts/bootstrap.sh` |
|------|-------------------------------------|
| Core runtimes | `python3 pip3 node npm` (Ubuntu 24.04 → Python 3.12) |
| Core deps | `pip install -r requirements.txt` for pinned `google-adk`, `litellm` |
| Dev deps | `pip install -r requirements-dev.txt` (ruff==0.11.10, black==25.1.0, bandit==1.7.7) |
| Quiet flags | `apt-get -qq`, `npm --quiet --no-fund --omit=dev` |
| Safety | `trap 'BOOTSTRAP FAILED on line $LINENO' ERR` |
| Offline flag | `export NO_NET=1` and “✅ Bootstrap complete” message printed at end |

---

## 5 ▪ Prompt Checklist (Quick Copy)

```

* Mark previous FS task done in ROADMAP\_TODO.md.
* Single clear goal (one FS task).
* List acceptance bullets (objectively testable).
* Branch name: capx/FS<ID>-slug.
* Include ruff, black, bandit (and pytest if present).
* End with “# Begin.” to cue Codex.

```

---

## 6 ▪ Codex Task SOP – End-to-End Workflow

### 6.1 Sanity Check the Codex Environment

**Ask Codex the following in Ask Mode before *any* implementation task:**

```

When you begin a task in Code Mode, do you clone the repo and execute the setup script as defined in the web UI?
At what point is Internet access disabled?
Once NO\_NET=1 is exported, can you still install packages or access remote APIs?
Do you use Linux or macOS runners?

Please also evaluate this setup script (paste it below):

* Is it complete and effective for future roadmap tasks?
* Do requirements.txt / requirements-dev.txt cover all needed packages?
* Will you encounter issues with file permissions, version drift, or runtime tools?
* What specific improvements would you suggest?

```

→ Review Codex’s output and update the bootstrap script if needed. This inquiry saves debugging time later and ensures setup drift is caught proactively.

---

### 6.2 Generate Task-Specific Assumptions Check

- Use the template from §2 and tailor it to the FS task ahead.
- Run it in Code Mode before issuing the task prompt.

---

### 6.3 Task Prompting

1. Write a **one-task prompt** referencing the assumptions check.
2. Include:
   - A summary of the goal
   - Acceptance criteria (testable)
   - Correct branch name (`capx/FS<ID>-slug`)
   - Expected file changes and CI outcomes
3. End with:
```
Begin.
```

````

---

### 6.4 Output Review

- Examine Codex's commit diffs and logs.
- Look for:
- Misunderstood assumptions
- Missing env variables
- CI/test formatting issues
- If clean, **you (human) push** the PR to trigger CI.

---

### 6.5 CI Handling

1. If CI fails:
- Ask Codex to run:
  ```
  gh pr view --web
  gh run list
  ```
- Then instruct Codex to remediate based on CI logs.
2. You must push; Codex cannot.
3. Best practice:
- Use one PR per branch.
- If confusion arises, document and close stale PRs manually.

---

### 6.6 Post-Task Debrief (Optional)

1. Ask Codex to write a short debrief:
- What it did
- Assumptions it verified
- Any known limitations or TODOs
2. Save in:
````

agent\_logs/FS<ID>\_debrief.md

```
3. Annotate key lessons for future prompt refinement.

---

## 7 ▪ Task-Log & Error Review

| Symptom | Meaning | Action |
|--------|---------|--------|
| `ModuleNotFoundError` | Missing pip package | Add to `requirements.txt` or vendor it |
| `Permission denied` | Shell script not executable | `chmod +x` and commit |
| `OpenAI/network error` after NO_NET=1 | Late API call | Move to online phase or stub |
| `ruff / black / bandit` fails | Formatting or lint error | Update prompt/code rules |
| `bandit N/A` | Dev wheel not vendored | Add to dev requirements or pin |

---

## 8 ▪ Future Improvements

- Add “assumptions-check” as a CI workflow
- Build persistent memory tooling for Deep Research debriefs
- Enable headless Codex invocation with prefilled env + SOP bundles

---

*Updated 2025-05-20.*
```
