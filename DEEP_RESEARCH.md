Deep Research – Standard Operating Procedures
codex\_agent\_platform · established 2025-05-19

This guide distills every hard-won lesson about running Deep Research and Codex web agents in this repository. Follow it before drafting any new research prompt or technical roadmap.

---

IMPORTANT: ## FS14.5 Required Before FS15+

Before running any roadmap task FS15 or higher, the agent must verify that FS14.5 (Repo Hygiene & Onboarding Prep) is complete.

This includes:
- Shell scripts are marked executable (`100755`) and pass `git ls-files -s`
- Lockfiles exist for Python and Node dependencies
- LICENSE file is present at repo root
- `scripts/run_tasks.py` is removed or implemented
- `ROADMAP_TODO.md` and `README.md` are in sync on task status
- No formatting errors exist in the README quickstart block
- The Planner → Coder → Reviewer flow is documented visually

If FS14.5 is not marked complete, the agent should begin there instead.

Reference: docs/fs14.5_plan.md

---

1 Golden Rules

1. Start with an assumptions-check (section 2) – Keeps mental models in sync with the evolving codebase.
2. Read AGENTS.md first – Codex adapts to its branching, lint, and CI conventions.
3. One clear goal per prompt – Codex is most reliable with tightly scoped tasks.
4. Always mark the previous FS task done (ROADMAP\_TODO.md) – Prevents duplicate work and drives the task loop.
5. Embed acceptance-criteria bullets – Lets Codex prove success (or show failures) in its logs.
6. Show lint/test output (ruff, black, bandit, pytest) – Reviewers see green checks inline; failures surface early.
7. Respect sandbox limits – no outbound net after NO\_NET=1, CPU-only, 4 GB RAM – Heavy models or late installs will crash the run.

2 Assumptions Check Template

Paste this into Codex before running a task that touches CI, dependencies, or tools. Adjust as needed.

Assumptions-check Task
Instructions:

1. Inspect the main branch.
2. Respond in a MARKDOWN table like this:
   \| # | PASS/FAIL | Evidence |
3. No code changes; read-only.
4. End with the word “Done”.

Checklist:

1. scripts/bootstrap.sh installs dev tools via requirements-dev.txt.
2. requirements-dev.txt pins ruff, black, bandit to fixed versions.
3. AGENTS.md contains the heading “Prompt checklist”.
4. ROADMAP\_TODO.md lists FS07 through FS10 as status=done.
5. .github/workflows/bootstrap.yml does NOT yet exist.
6. mcp\_servers/\*.sh are executable.
7. agents/dev\_agent.py imports from google.adk and returns "pong".
8. NO\_NET=1 is exported at end of bootstrap.

If any assumption fails, fix the repo or the assumption before moving forward.

3 Codex-Web Agent Capabilities and Limits

Can: edit code, run tests/lint, stage branches, and commit.
Cannot: push code, open PRs, merge, or inspect CI outcomes.
Reads: the entire repo (especially AGENTS.md).
Requires: accurate assumptions, structured prompt, correct branch naming.
Offline after bootstrap: NO\_NET=1 means no downloading or API calls.

4 Bootstrap Expectations

The bootstrap.sh script must:

* Install python3, pip3, node, and npm
* pip install -r requirements.txt (includes google-adk, litellm)
* pip install -r requirements-dev.txt (includes ruff, black, bandit pinned)
* Use apt-get -qq and npm --quiet --no-fund --omit=dev
* Contain trap 'BOOTSTRAP FAILED on line \$LINENO' ERR
* End by exporting NO\_NET=1 and echoing a success message

5 Prompt Checklist

* Previous FS task marked done in ROADMAP\_TODO.md
* Only one task in prompt
* Acceptance bullets included
* Branch named capx/FS<ID>-slug
* Lint/test tools expected: ruff, black, bandit, pytest
* End with "# Begin."

6 Codex Task SOP – Full Workflow

Step 1 – Codex Environment Inquiry (Ask Mode)

Before running any implementation, ask Codex in Ask Mode:

* Do you clone the repo and execute the setup script from the Codex web UI?
* When does Internet access end?
* Can you access APIs or download packages after NO\_NET=1 is set?
* What OS do you use (Linux/macOS)?
* Given the current setup script, is anything missing or broken?
* Are all dependencies pinned and correctly installed from requirements.txt and requirements-dev.txt?
* Are all required scripts executable?

Update bootstrap.sh immediately if Codex flags any issues.

Step 2 – Run Assumptions Check

Use the checklist in section 2, customized to match the next FS task.
Have Codex run this and verify that all critical infrastructure is in place.

Step 3 – Write the Task Prompt

* Include the FS goal and what success looks like
* Use a single responsibility
* Reference the assumptions if relevant
* Include the branch name, test expectations, and acceptance bullets
* End with: # Begin.

Step 4 – Review the Output

* Review code diffs, logs, and test output
* Confirm that Codex followed expectations
* Look for hallucinations, config drift, or uninstalled tools
* If clean, human pushes the code and opens the PR

Step 5 – CI Handling

* If CI fails, tell Codex to run gh pr view --web or gh run list
* Have it remediate and stage a new commit
* Codex cannot push — user must do this
* Do not let Codex open a new PR for the same task unless needed
* Manually close stale PRs as needed

Step 6 – Optional Debrief

Prompt Codex to write a brief debrief:

* What it did
* What assumptions were involved
* Any known limitations
  Save this as agent\_logs/FS<ID>\_debrief.md

7 Error Signals in Logs

* ModuleNotFoundError = dependency not in requirements.txt
* Permission denied = chmod +x missing
* Network error after NO\_NET=1 = late install or API call
* Ruff/Black/Bandit fails = lint rules violated or tool missing
* bandit N/A = wheel not installed or vendored

8 Future Enhancements

* Add a CI job to automatically check assumptions drift
* Build memory tooling for summarizing agent debriefs
* Support Codex running in headless mode with env and SOP preloaded

Updated 2025-05-20

### UI & Workflow Tips  *(added after FS15)*
- **Assumptions-check stage** – run only on `main`; avoid any branch-creation hints.  
  Create the feature branch in the *implementation* prompt to keep SOP stages atomic.
- **Codex Push controls** – branches created inside a Codex task and prefixed  
  `codex/…` automatically expose the **Push ▾ / Create PR** buttons.
  If a task ends with “unknown error” but a commit exists, run a no-op follow-up
  task (or use the Push menu) to surface the diff and push the branch.

See **docs/prompt_templates/README.md** for copy-paste instructions.  
For long prompts, generate a downloadable `.txt` via `python_user_visible`
to bypass ChatGPT UI escaping.
