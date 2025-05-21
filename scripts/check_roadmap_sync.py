#!/usr/bin/env python3
"""Verify ROADMAP_TODO.md comment and checkbox status match."""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Regex patterns reused from status_updater
TASK_RE = re.compile(r"<!--\s*TASK:(FS\d+)\s+status=([a-z_]+)\s*-->")
BULLET_RE = re.compile(r"^- \[([xX\- ])\]")

STATUS_FROM_CHECKBOX = {
    " ": "pending",
    "-": "in_progress",
    "x": "done",
    "X": "done",
}


def check_sync(path: Path) -> list[str]:
    """Return a list of mismatch errors for the given roadmap."""
    errors: list[str] = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        match = TASK_RE.search(line)
        if not match:
            continue
        task_id, status = match.groups()
        if i + 1 >= len(lines):
            errors.append(f"{task_id}: missing checkbox line")
            continue
        bullet_line = lines[i + 1].strip()
        bullet_match = BULLET_RE.match(bullet_line)
        if not bullet_match:
            errors.append(f"{task_id}: malformed checkbox line")
            continue
        cb_char = bullet_match.group(1)
        bullet_status = STATUS_FROM_CHECKBOX.get(cb_char)
        if bullet_status != status:
            errors.append(
                f"{task_id}: comment status '{status}' mismatch checkbox '{cb_char}'"
            )
        if status in {"in_progress", "done"} and cb_char == " ":
            errors.append(f"{task_id}: checkbox unchecked for status '{status}'")
    return errors


def main(argv: list[str] | None = None) -> None:
    path = Path("configs/ROADMAP_TODO.md")
    errors = check_sync(path)
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        raise SystemExit(1)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
