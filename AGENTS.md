# Contributor Guide

## Repo layout (minimum viable)
- `agents/` → ADK agent code (only `dev_agent.py` for now)
- `configs/` → `ROADMAP_TODO.md` task queue, `AGENTS.md` (this file)
- `scripts/` → `bootstrap.sh` (created by TASK FS01)
- `mcp_servers/` / `reports/` / etc. created as tasks proceed

## How Codex should work
1. Read the next **`status=pending`** task in `configs/ROADMAP_TODO.md`.
2. Implement it inside the sandbox.
3. Open a PR + write `reports/NNN_debrief.md`.
4. Wait for human review before merging.

## Style & validation
- - Use Python 3.11 syntax, black + isort defaults (to be added later).
- - All shell scripts must be Unix-LF and executable (`chmod +x`).
- - Unit-tests will be introduced in later tasks; keep code modular.

## Pull-Request Guidelines

### Branch name
`codex/task-<ID>-<slug>`

### PR title
`[FS<ID>] <imperative verb phrase>`  (≤ 60 chars)

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

