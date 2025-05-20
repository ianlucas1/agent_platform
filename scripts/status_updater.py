#!/usr/bin/env python3
"""Update roadmap task status in-place.

Usage:
  python scripts/status_updater.py FS16 in_progress
  python scripts/status_updater.py FS16 done
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TASK_RE = re.compile(r"(<!--\s*TASK:(FS\d+)\s+status=)([a-z_]+)(\s*-->)")
BULLET_RE = re.compile(r"^(- \[[xX\- ]\])")


def update_status(path: Path, task_id: str, new_status: str) -> None:
    """Update the given task's status and checkbox."""
    lines = path.read_text().splitlines()
    updated = False
    for idx, line in enumerate(lines):
        m = TASK_RE.search(line)
        if m and m.group(2) == task_id:
            prefix, _, _, suffix = m.groups()
            lines[idx] = f"{prefix}{new_status}{suffix}"
            # next line expected to be bullet
            if idx + 1 < len(lines) and BULLET_RE.match(lines[idx + 1]):
                bullet_rest = BULLET_RE.sub("", lines[idx + 1])
                if new_status == "done":
                    checkbox = "- [x]"
                elif new_status == "in_progress":
                    checkbox = "- [-]"
                else:
                    checkbox = "- [ ]"
                lines[idx + 1] = f"{checkbox}{bullet_rest}"
            updated = True
            break
    if not updated:
        raise SystemExit(f"Task {task_id} not found in {path}")
    path.write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_id", help="Task ID, e.g. FS16")
    parser.add_argument(
        "status",
        choices=["pending", "in_progress", "done"],
        help="New status for the task",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=Path("configs/ROADMAP_TODO.md"),
        help="Roadmap file to modify",
    )
    args = parser.parse_args(argv)

    update_status(args.file, args.task_id, args.status)


if __name__ == "__main__":
    main()
