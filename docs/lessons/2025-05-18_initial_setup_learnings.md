<!-- docs/lessons/2025-05-18_initial_setup_learnings.md -->

# Lessons Learned — Initial Repo & Codex Bring-up  

*codex-agent-platform • 18 May 2025*

## 1 Context

This document captures tacit knowledge discovered while (a) seeding a minimal repo for Codex agents and (b) steering the OpenAI Codex UI through FS01.  
It is written for **future Deep-Research agents** (or maintainers) who will analyse the code-base before taking new actions.

## 2 Repository-structure insights

| Area | Current state | Recommendation |
| --- | --- | --- |
| **Contributor file** | Named `AGENT.md` (singular). | Rename to **`AGENTS.md`** (plural) — Codex looks for that exact filename. |
| **Task queue** | `configs/ROADMAP_TODO.md` with HTML comments (`<!-- TASK:id status=... -->`). | Keep format; add parser unit-tests once FS15/FS16 land. |
| **Reports** | `reports/NNN_debrief.md` added manually. | Automate creation in task-loop; link in every PR body. |
| **Scripts** | `scripts/bootstrap.sh` created in FS01. | File must succeed **offline** & without `apt-get`; treat network as unavailable. |

## 3 Codex-UI & environment learnings

1. **No outbound network** inside the “universal” container → any `apt-get`/`git push` will fail.  
2. Codex only shows a *Push* ▾ button after a successful task run; any uncaught error (even post-commit) hides it.  
3. Use *commit-only* workflows inside Codex; let a human open the PR if the Push menu is missing.

## 4 Bootstrap-script pitfalls

| Pitfall | Mitigation |
| --- | --- |
| `apt-get` not found in stripped-down Ubuntu | Detect & skip; assume python3/pip & node/npm pre-installed. |
| Sudo resolves hostnames (#warning) | Harmless in container; suppress with `sudo -n` if script evolves. |

## 5 Pull-request hygiene (agreed template)

See **AGENTS.md → “Pull-Request Guidelines”** once PR #\<next> merges; every PR should follow that skeleton so Deep-Research agents can extract rationale programmatically.

## 6 Recommended follow-ups

1. **FS02** — extend `bootstrap.sh` to pre-install Python packages & MCP servers *without* network (use wheels/tarballs checked into `vendor/` if needed).  
2. **CI** — create `.github/workflows/bootstrap.yml` that runs the script on macOS (ARM) to catch Homebrew regressions.  
3. **Lesson index** — keep an index file (`docs/lessons/README.md`) linking to each dated report.

*End of report*
