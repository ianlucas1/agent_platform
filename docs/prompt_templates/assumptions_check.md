# Assumptions\-Check Prompt Template

```
# <Task name> — assumptions check
| # | Assumption to verify |
|---|----------------------|
| 1 | main CI is green |
| 2 | … |

**Output**: Markdown table only — no extra prose.
| Check | Result | Evidence |
```

**Guidelines**

* Run on `main`; do **not** create or mention branches.
* Ask Mode only — no file edits or branch operations.
* Output table only (see header above).
* Embed exact reference `bootstrap.sh` for byte‑comparison.
* Skip checks that require mutating repo state (e.g., branch rename).
* Provide this prompt as a downloadable `.txt` via python_user_visible.
* Obtain current Codex setup script from the human collaborator before composing.
