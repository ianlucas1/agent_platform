# FS14 Debrief – Bootstrap CI Workflow (Resolved May 20, 2025)

## Objective

Create a cross-platform CI job to:
- Run `scripts/bootstrap.sh` on Ubuntu and macOS GitHub runners
- Validate code health using `ruff`, `black`, and `bandit`
- Ensure reproducibility, executable integrity, and CI compatibility

## Outcome

✅ CI workflow added  
✅ Bootstrap script hardened  
✅ FS14 marked complete  
✅ CI passes across all platforms

---

## Failures and Lessons Learned

### 1. 🔥 Permission Errors from Git Mode Drift

**What happened:**
- `scripts/bootstrap.sh` lost its `+x` permission in Git repeatedly.
- Even though `chmod +x` was applied locally, it wasn’t staged via:
  ```bash
  git update-index --chmod=+x scripts/bootstrap.sh
  ```

* This caused CI to fail silently or with `exit code 126`.

**Resolution:**

* Explicitly committed the mode using `update-index`.
* Added a CI `chmod +x` step as a backup in the workflow.

**Lesson:**
File system `chmod` ≠ Git mode. Always commit mode with `update-index`.

---

### 2. 🧩 PEP 668 Breakage on macOS (pip install)

**What happened:**

* macOS runners use Homebrew Python with PEP 668, which blocks global pip installs.
* CI failed silently unless `PIP_BREAK_SYSTEM_PACKAGES=1` was exported.

**Resolution:**

* Added:

  ```bash
  export PIP_BREAK_SYSTEM_PACKAGES=1
  ```

  inside the `Darwin` block of `scripts/bootstrap.sh`.

**Lesson:**
macOS bootstrap requires the above export or pip will silently refuse installs.

---

### 3. 🌀 Codex UI Instability

**What happened:**

* Multiple Codex sessions completed the shell work, but failed to surface the push button.
* Codex sometimes amended commits on the wrong branch (`work`, `main`, or post-merge `HEAD`).
* Tasking often failed with “unknown error” after successful execution.

**Resolution:**

* Reset FS14 under a new branch: `capx/FS14-bootstrap-ci-reboot`
* Avoided `--amend`, started clean from `main`

**Lesson:**

* Never amend Codex commits unless absolutely necessary
* Restart clean from `main` if tasking repeatedly fails

---

### 4. 🧠 Debrief Trigger for Future Agents

FS14’s CI bootstrapping revealed the need for pre-FS15 hygiene enforcement:

* Mode validation
* Lockfiles
* README/ROADMAP sync
* LICENSE presence
* `run_tasks.py` removal

These are now encapsulated in:

* `ROADMAP_TODO.md` → FS14.5
* `docs/fs14.5_plan.md`
* `DEEP_RESEARCH.md` SOP section

---

## Final Commit Summary

Branch: `capx/FS14-bootstrap-ci-reboot`
Commit: `5fc3d2a`
PR: [https://github.com/ianlucas1/codex\_agent\_platform/pull/19](https://github.com/ianlucas1/codex_agent_platform/pull/19)
Status: ✅ Merged — all checks passed

---

## Tags

`ci` `shell-mode` `macos` `pip` `permission` `pep-668` `reboot` `codex-unstable` `fs14-done`

```
