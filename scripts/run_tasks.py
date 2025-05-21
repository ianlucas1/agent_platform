#!/usr/bin/env python3
"""
FS19: Task loop MVP.
Reads configs/ROADMAP_TODO.md, finds first `status=pending` task,
and prints its FS number + title. (Editing comes later.)
"""
import pathlib
import re
import sys
import textwrap

ROADMAP = pathlib.Path(__file__).parents[1] / "configs/ROADMAP_TODO.md"
PATTERN = re.compile(
    r"<!-- TASK:(FS\\d+) status=pending -->"
    r"(?:\\s*- \\[ ] \\*\\*(.*?)\\*\\*)"
)

md = ROADMAP.read_text()
match = PATTERN.search(md)
if not match:
    sys.exit("No pending tasks.")
print(textwrap.dedent(f"""
    Next task: {match.group(1)}
    Title: {match.group(2)}
"""))
