# Assumptions\-Check Prompt Template

```
# <Task name> — assumptions check
| # | Assumption to verify |
|---|----------------------|
| 1 | main CI is green |
| 2 | … |

Return:

| # | TRUE/FALSE | Evidence | Notes if FALSE |
```

**Guidelines**
- Run on `main`; do **not** create or mention branches.
- No file edits; output table only.
- Provide this prompt as a downloadable .txt via python_user_visible.
- Before running, obtain the current Codex environment‑setup script from the human collaborator.
