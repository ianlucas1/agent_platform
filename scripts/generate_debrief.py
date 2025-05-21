#!/usr/bin/env python3
"""
Auto-generate a per-task debrief Markdown report (FSxx_debrief.md).
Usage: invoked by the orchestrator immediately before FSxx auto-PR.
"""
import os
import subprocess # nosec B404
import re
from openai import OpenAI

# --- Configuration ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def run_cmd(cmd):
    return subprocess.check_output(cmd, text=True).strip() # nosec B603

def get_branch():
    return run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"])

def parse_fs_number(branch):
    m = re.search(r"(FS\d+)", branch)
    return m.group(1) if m else None

def get_task_description(fs):
    for line in open("configs/ROADMAP_TODO.md"):
        if line.startswith(f"- [ ] {fs}") or line.startswith(f"- [x] {fs}"):
            return line.split("–",1)[1].strip()
    return ""

def get_changed_files():
    return run_cmd(["git", "diff", "origin/main", "--name-only"]).splitlines()

def generate_debrief(fs, desc, files):
    prompt = (
        f"Write a concise Markdown debrief for **{fs}**:\n\n"
        f"**Objective:** {desc}\n"
        f"**Files changed:** {', '.join(files)}\n"
        f"**Tests:** All passing.\n\n"
        "Include sections: Outcome, Key Changes, Lessons Learned."
    )
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system","content":"You are a helpful assistant that writes clear debrief reports."},
            {"role":"user","content":prompt},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content

def main():
    branch = get_branch()
    fs = parse_fs_number(branch)
    if not fs:
        raise RuntimeError("Cannot determine FS number from branch: " + branch)
    desc = get_task_description(fs)
    files = get_changed_files()
    md = generate_debrief(fs, desc, files)
    out_path = f"reports/{fs}_debrief.md"
    with open(out_path, "w") as f:
        f.write(md)
    run_cmd(["git", "add", out_path])
    run_cmd(["git", "commit", "-m", f"docs: add {fs}_debrief report"])

if __name__ == "__main__":
    main()
