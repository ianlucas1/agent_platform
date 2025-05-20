#!/usr/bin/env python3
"""Parse ROADMAP_TODO.md and list pending tasks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TASK_RE = re.compile(r"<!--\s*TASK:(FS\d+)\s+status=([a-z_]+)\s*-->")


def parse_tasks(path: Path) -> list[dict[str, str]]:
    """Return all tasks from the roadmap file."""
    tasks: list[dict[str, str]] = []
    lines = path.read_text().splitlines()
    i = 0
    while i < len(lines):
        match = TASK_RE.search(lines[i])
        if match:
            fs_id, status = match.groups()
            title = ""
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if TASK_RE.search(next_line):
                    break
                if next_line.startswith(("-", "*")):
                    bullet = next_line.lstrip("-*").strip()
                    bullet = re.sub(r"^\[[xX ]\]\s*", "", bullet)
                    title_match = re.search(r"\*\*(.*?)\*\*", bullet)
                    if title_match:
                        title_text = title_match.group(1)
                        title = re.sub(r"^FS\d+\s+\u2013\s+", "", title_text).strip()
                    else:
                        title = bullet
                    break
                j += 1
            tasks.append({"id": fs_id, "title": title, "status": status})
            i = j
        else:
            i += 1
    return tasks


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        type=Path,
        default=Path("configs/ROADMAP_TODO.md"),
        help="Roadmap file to parse",
    )
    parser.add_argument(
        "--format",
        choices=["table", "json"],
        default="table",
        help="Output format",
    )
    args = parser.parse_args(argv)

    tasks = [t for t in parse_tasks(args.file) if t["status"] == "pending"]

    if args.format == "json":
        json.dump(tasks, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print("| ID | Title | Status |")
        print("| --- | --- | --- |")
        for task in tasks:
            print(f"| {task['id']} | {task['title']} | {task['status']} |")


if __name__ == "__main__":
    main()
