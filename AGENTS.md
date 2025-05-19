# Contributor Guide

## Repo layout (minimum viable)
- `agents/` → ADK agent code (only `dev_agent.py` for now)
- `configs/` → `ROADMAP_TODO.md` task queue, `AGENTS.md` (this file)
- `scripts/` → `bootstrap.sh` (created by TASK FS01)
- `mcp_servers/` / `reports/` / etc. created as tasks proceed

## How Codex should work

### Prompt checklist (what every Codex task prompt must include)

* **Mark the previous FS task done** – update `configs/ROADMAP_TODO.md` (`status=done`, checkbox ☑).
* **Single clear goal** – one FS task (or tight bundle) only.
* **Acceptance-criteria bullets** – each is objectively testable.
* **Branch name** – `capx/FSxx-short-slug` (no spaces, lower-case).
* **Include test commands in prompt** – `ruff check .`, `black --check .`, and `bandit -r .` (always required).
* **End with `# Begin.`** – cues Codex to start the implementation chain-of-thought.

1. Read the next **`status=pending`** task in `configs/ROADMAP_TODO.md`.
2. Implement it inside the sandbox and stage the changes on a branch named `capx/FSxx-slug` (the **Push** button appears).
3. Stop and present the diff — the **human clicks Push** to send the branch to GitHub.
4. Human opens the pull request; CI runs.  If checks fail, the human may ask Codex to inspect logs and fix.
5. Human merges the pull request once all checks pass.

### ADK quick-reference (dev_agent stubs)

```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
# google-adk==0.3.1 is no longer available
# Requires google-adk>=0.5.0 (check requirements.txt)

model = LiteLlm(model="openai/codex-mini-latest")  # string, not LiteLLM()
dev_agent = Agent(
    name="DevAgent",
    model=model,
    instruction="You are DevAgent inside an offline sandbox.",
    tools=[],         # no tools wired yet
)

# Synchronous helper (for smoke-tests only)
Agent.run = lambda self, p: "pong"  # avoid live calls while NO_NET=1

## Style & validation
- - Use Python 3.12-compatible syntax (Ubuntu 24.04 default) and Black formatting (isort rules will be added later).
- - All shell scripts must be Unix-LF and executable (`chmod +x`).
- - Unit-tests will be introduced in later tasks; keep code modular.
- Run `ruff check --fix && black . && bandit -r .` before commit.
- If you’re working **offline**, run `pip install -r requirements-dev.txt` once to cache the formatter/linter wheels, then use  
  `ruff check --fix . && black . --check && bandit -r .` before committing.

## Pull-Request Guidelines

### Branch name
`capx/FS<ID>-<slug>`

### PR title
`[FS<ID>] <imperative verb phrase>`  (≤ 60 chars)

### Commit-message prefixes
| Prefix | Purpose |
| ------ | ------- |
| `feat:` | New feature or enhancement |
| `fix:` | Bug fix |
| `chore:` | Maintenance or tooling |

### PR body template
```markdown
## Summary
<single sentence purpose>

## Changes
- Bullet list of key file additions / edits
- Link to debrief file (e.g. `reports/NNN_debrief.md`)

## Testing
```bash
# commands run
<command list>
```
* Result: <green output / exit 0>

## References

Closes FS<ID>

## Codex-Cloud Constraints (#1–#10)

| #      | Reality of the sandbox                                         | Risk it creates                          | How to design tasks to cope / exploit                                                                    |
| ------ | -------------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **1**  | `No outbound internet` after bootstrap (except GitHub via MCP) | Package installs or API calls can hang   | Pre-cache wheels/tarballs in bootstrap; embed docs under `docs/reference/`; avoid `curl`/`wget` in tasks |
| **2**  | *Ephemeral VM* (workspace resets wipe storage)                 | Long jobs lose state                     | Write checkpoints to `reports/`; keep tasks ≤ 5 min; push branches early & often                         |
| **3**  | *Single shared container* (no Docker-in-Docker)                | Services like Redis/Postgres unavailable | Use SQLite/TinyDB/DuckDB; abstract external services behind thin adapters                                |
| **4**  | *Non-root user*                                                | Kernel modules/systemd off-limits        | Limit `apt-get` to essential packages in bootstrap; prefer user-space installs                           |
| **5**  | *CPU-only, \~4 GB RAM*                                         | Heavy ML builds slow/fail                | Stick to lightweight models (e.g., codex-mini); cap pytest workers ≤ 2                                   |
| **6**  | *Fixed port forwarding* (first 5 ports)                        | Port exhaustion                          | Reuse ports 8787+; kill servers after tests                                                              |
| **7**  | *Integrated file explorer & diff*                              | Large binaries clutter UI                | `.gitignore` `node_modules/`, `.venv/`, artifacts; keep patches < 500 LOC                                |
| **8**  | *Git UI favors linear history*                                 | Force-pushes confuse reviewers           | Use additive commits; branch names like `[FS##]-slug`                                                    |
| **9**  | *No background cron*                                           | Automation loops die when tab closes     | Run loops with `--max-tasks N`; trigger via CI on each push                                              |
| **10** | *30 min idle timeout*                                          | Lost terminal sessions                   | Autosave progress to `reports/`; break interactive debugging into small snippets                         |

