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

```

# 🔍  Assumptions-check Task

#

# Instructions

# 1. For each numbered assumption, inspect the main branch.

# 2. Respond in a MARKDOWN table:

# | # | PASS/FAIL | Evidence |

# 3. No code changes; read-only.

# 4. End with the single word “Done”.

#

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

If any row **FAIL**s, fix the repo **or the assumption** before proceeding with planning.

---

## 3 ▪ Codex-web agent capabilities & limitations

* **Can:** write/modify files, stage a branch, run tests/lint, display full logs.  
* **Cannot:** click “Push”, open PRs, or merge; the human does that.  
* **Reads:** any file in the repo and especially **AGENTS.md** for norms.  
* **Requires:** exact branch naming (`capx/FS<ID>-slug`) and acceptance bullets to satisfy.  
* **Offline after bootstrap:** add all packages during the online phase or vendor wheels.

---

## 4 ▪ Bootstrap expectations

| Item | Expected in `bootstrap.sh` |
|------|----------------------------|
| Core runtimes | `python3 pip3 node npm` installed (Ubuntu 24.04 → Python 3.12). |
| Core deps | `pip install google-adk litellm` |
| Dev deps | `pip install -r requirements-dev.txt` (ruff 0.11.10, black 25.1.0, bandit 1.7.7). |
| Quiet flags | `apt-get -qq`, `npm --quiet --no-fund --omit=dev`. |
| Safety | `trap 'BOOTSTRAP FAILED on line $LINENO' ERR` |
| Offline flag | `export NO_NET=1` printed as final line. |

---

## 5 ▪ Prompt checklist (quick copy)

```

* Mark previous FS task done in ROADMAP\_TODO.md.
* Single clear goal (one FS task).
* List acceptance bullets (objectively testable).
* Branch name capx/FS<ID>-slug.
* Include ruff, black, bandit (and pytest if present) commands.
* End with “# Begin.” to cue Codex.

```

---

## 6 ▪ Future improvements

* Add “assumptions-check” as a CI job to warn when expectations drift.  
* Expand memory tooling (FS25) so Deep Research can query long-term artefacts.

---

_Updated 2025-05-19._
```
