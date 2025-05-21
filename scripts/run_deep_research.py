#!/usr/bin/env python3
"""
FS23: Wrap OpenAI Deep Research tool to generate an implementation plan
for roadmap tasks.
"""
import os
import re
import subprocess  # nosec
import pathlib
from openai import OpenAI
from dotenv import load_dotenv
# TODO: import Deep Research client (e.g., OpenAI or other SDK)

def load_credentials():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    # initialize Deep Research client using your OpenAI key
    client = OpenAI(api_key=api_key)
    return client

def parse_roadmap():
    fs_items = []
    with open("configs/ROADMAP_TODO.md") as f:
        for line in f:
            # match unchecked FS steps ≥23
            m = re.match(r"- \[ \] (FS(\d+)) – (.+)", line)
            if m and int(m.group(2)) >= 23:
                fs_items.append((m.group(1), m.group(3).strip()))
    return fs_items

def build_prompt(fs_list):
    """
    Given a list of FS items, compose a Deep Research prompt that
    asks for detailed implementation steps for each.
    """
    # build Deep Research prompt
    lines = ["Generate a detailed implementation plan for the following Feature Steps:\n"]
    for fs, desc in fs_list:
        lines.append(f"- **{fs}**: {desc}")
    lines.append("\nProvide a numbered list of actionable tasks for each FS.")
    return "\n".join(lines)

def call_deep_research(prompt: str) -> str:
    """
    Invoke the Deep Research API with `prompt` and return the raw result.
    """
    # invoke the Deep Research API
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role":"system","content":"You are a Deep Research assistant."},
            {"role":"user","content":prompt},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content

def write_report(content: str):
    """
    Write `content` to reports/FS23_deep_research_plan.md and commit it.
    """
    # write out and commit the plan
    plan_path = pathlib.Path("reports/FS23_deep_research_plan.md")
    plan_path.write_text(content)
    subprocess.run(["git", "add", str(plan_path)], check=True)    # nosec
    subprocess.run(
        ["git", "commit", "-m", "docs: add FS23 deep research plan"],
        check=True
    )  # nosec

def main():
    client = load_credentials()
    fs_items = parse_roadmap()
    prompt = build_prompt(fs_items)
    plan = call_deep_research(prompt)
    write_report(plan)

if __name__ == "__main__":
    main()
