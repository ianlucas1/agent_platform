# Contributor Guide (AGENTS.md)

This file gives Codex web agents and human collaborators a shared set of
conventions for working in **codex_agent_platform**.  
Read this first before opening a PR or drafting an agent prompt.

---

## Repo layout (minimum viable)

| Path | Purpose |
|------|---------|
| `agents/` | Small agent wrappers & helper code |
| `configs/` | Roadmap, CI configs, etc. |
| `scripts/` | Bootstrap & utility scripts |
| `mcp_servers/` | Local Model‑Context‑Protocol servers |
| `docs/` | SOP & prompt templates (**LLM_COLLABORATOR.md**, `prompt_templates/`) |
| `reports/` | Per‑task debriefs |
| `tests/`  | _(placeholder)_ unit/integ tests as they land |

---

## Branch naming

`codex/<task‑slug>` — always prefix with **`codex/`** so the Push ▾ / PR
buttons appear in the Codex UI.

Examples:

* `codex/fix-bootstrap-perms`
* `codex/roadmap-parser`

---

## Commit message style

| Prefix | When to use |
|--------|-------------|
| `feat:` | new feature / script |
| `fix:`  | bug fix |
| `docs:` | documentation changes |
| `chore:`| misc repo upkeep |
| `ci:`   | CI config or workflow |

---

## Contribution checklist (use in PR body)

```markdown
### Checklist
- [ ] Branch name starts with codex/
- [ ] Ruff / Black / Bandit exit 0
- [ ] `pytest -q` (once tests exist) exits 0
- [ ] Updated ROADMAP_TODO.md: tick completed task
- [ ] Docs updated if behaviour changed
```

---

## Style & tooling

* **Python ≥ 3.12**; code must pass **Ruff**, **Black**, **Bandit**.  
* Pre‑commit hook enforces executability of `*.sh` files.  
* Use the prompt scaffolds in **`docs/prompt_templates`** when drafting
  assumptions‑check or task prompts.

---

## Validating changes locally

```bash
# lint
ruff check .
black --check .
bandit -r .

# tests (will be added incrementally)
pytest -q
```

---

## Finding pending roadmap tasks

```bash
python scripts/parse_roadmap.py            # Markdown table
python scripts/parse_roadmap.py --format json | jq .
```

---

## PR instructions

* **Title:** `[<area>] <concise description>`  
  Example: `[scripts] make bootstrap lock‑file aware`
* **Body:** Include the *Contribution checklist* above.
* After Codex run ends with `echo DONE`, click **Push ▾ → Create PR**,
  wait for CI, then merge or fix.

---

_Last updated: 2025-05-20_
