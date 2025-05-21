#!/usr/bin/env python3
"""FS19 – Task loop MVP.

Reads `configs/ROADMAP_TODO.md`, finds the first `status=pending` task,
and prints its FS number and title.
"""

import pathlib
import re
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "configs" / "ROADMAP_TODO.md"

PATTERN = re.compile(
    r"<!-- TASK:(FS\d+) status=pending -->"  # HTML task marker
    r"(?:\s*- \[ ] \*\*(.*?)\*\*)",          # Markdown checklist line
)


def main() -> None:
    match = PATTERN.search(ROADMAP.read_text())
    if match is None:
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
