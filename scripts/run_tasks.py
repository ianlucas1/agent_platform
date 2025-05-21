#!/usr/bin/env python3
"""
FS19 – Task loop MVP.

Reads configs/ROADMAP_TODO.md, finds the first `status=pending` task,
and prints its FS number and title.
"""

import pathlib
import re
import sys
import textwrap

ROADMAP = pathlib.Path(__file__).resolve().parents[1] / "configs/ROADMAP_TODO.md"

PATTERN = re.compile(
    r"<!-- TASK:(FS\d+) status=pending -->"
    r"(?:\s*- \[ ] \*\*(.*?)\*\*)",
)


def main() -> None:
    md = ROADMAP.read_text()
    match = PATTERN.search(md)
    if not match:
        sys.exit("No pending tasks.")
    print(
        textwrap.dedent(
            f"""
            Next task: {match.group(1)}
            Title: {match.group(2)}
            """,
        ).strip(),
    )


if __name__ == "__main__":  # pragma: no cover
    main()
