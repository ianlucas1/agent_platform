# LLM Collaborator Guide – Standard Operating Procedures  
*agent_platform*

This document defines the evergreen SOP for a human ↔ LLM ↔ Codex workflow.  
It is version‑agnostic and free of roadmap task numbers.

---

## 0 Share the Current Setup Script

The **human** must copy the exact *environment‑setup script* from  
**Codex UI → Settings → Environment setup** and paste it here **before any prompt**.  
The collaborating LLM embeds this script in the upcoming assumptions check.

---

## 1 Golden Rules

1. Always start with an **assumptions‑check** (Section 2).  
2. Read **AGENTS.md** first—branch, lint, and CI conventions live there.  
3. One clear goal per prompt; Codex performs best with tightly scoped tasks.  
4. Keep **ROADMAP_TODO.md** status ticks current to avoid duplicate work.  
5. Include acceptance‑criteria bullets so Codex can demonstrate success.  
6. Show lint/test output (ruff · black · bandit · pytest) in every Code Mode task.  
7. Sandbox limits: CPU‑only, ≈4 GB RAM, **no outbound net once `NO_NET=1`**.
8. Codex always spawns on the **`main`** branch — never create branch‑rename tasks.  
9. Keep chat replies ≤ 100 words unless the user explicitly requests depth.  
10. Offer *one* discrete task per message; never bundle multi‑step sequences.  
11. **At the start of any complex FS task, provide a concise bullet list of all planned sub‑tasks (e.g., B1–B6) with one‑sentence descriptions for situational awareness.**
12. **Review brevity:** When evaluating Codex output, reply with a simple “✓ good to push” **or** list only the blocking issues that would fail CI. Avoid long narrative reviews.

---

## 2 Assumptions‑Check Prompt Template

Template file: **docs/prompt_templates/assumptions_check.md**  
Provide it to Codex as a downloadable `.txt` file—no narrative wrapper.  
Runs on **main** only; returns a TRUE/FALSE evidence table.

*(Ask Mode = Codex run with no file edits.)*

---

## 3 Prompt Templates & Delivery

* **assumptions_check.md** – verifies repo state on `main`.  
* **tasking.md** – creates `codex/…` branch, applies patches, commits, ends `echo DONE`.

> **All prompts (short or long) must be delivered as downloadable `.txt`
> files via `python_user_visible`, with no extra narrative, to avoid UI escaping.**

---

## 4 Bootstrap Expectations

`scripts/bootstrap.sh` installs Python 3, pip, Node, npm; installs from lock‑files; pins MCP versions; sets `PIP_BREAK_SYSTEM_PACKAGES=1`; exports `NO_NET=1`; prints tool versions.

---

## 5 Codex Task SOP – Full Workflow

| Step | Actor | Action |
|------|-------|--------|
| **0 Setup script** | Human | Share current `bootstrap.sh` (environment‑setup) with LLM. |
| **1 Assumptions check** | LLM → Codex (Ask Mode) | LLM drafts `.txt` prompt → human submits to Codex; copy result table back for review. |
| **2 Task prompt** | LLM | Draft Code Mode prompt (`tasking.md` style) and save as `.txt`. |
| **3 Codex Code Mode** | Human → Codex | Paste prompt; after run, share screenshot, `patch.txt`, `logs.txt` with LLM. |
| **4 Push & PR / CI** | Human | Click **Push ▾ / Create PR**; monitor CI; report failures to LLM. |
| **5 Doc sync (if needed)** | Codex or Human | Trigger when code changes outdate docs. LLM supplies `.txt` patch for affected docs only → commit on branch `codex/doc-sync-<slug>` with message `docs: sync <file> after <change>`. |
| **6 Debrief (optional)** | LLM | Provide `reports/<task>_debrief.md` as `.txt`; human commits with given message. |
| **7 Roadmap drift CI** | CI | `.github/workflows/bootstrap.yml` runs `scripts/check_roadmap_sync.py`; PRs fail if ROADMAP comments and checkboxes diverge. |

---

## 6 UI & Workflow Tips

* Use terse, action-oriented language; reserve extended narrative for reports/debriefs.
* When screenshot, diff, and logs are supplied, **analyze all three**: Codex summary, patch correctness, logs for hidden warnings; surface only insights that reduce CI friction or clarify future prompts.
* Assumptions check stays on **main**; branch only in tasking prompt.  
* **Push controls appear** when branch name starts with `codex/…` and task exits cleanly (`echo DONE`).  
  If “unknown error” hides the button but a commit exists, run a no‑op task or use Push menu.
