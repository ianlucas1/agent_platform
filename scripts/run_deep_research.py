#!/usr/bin/env python3
"""
FS23: Wrap OpenAI Deep Research tool to generate an implementation plan
for roadmap tasks.
"""
import os
import re
from dotenv import load_dotenv
# TODO: import Deep Research client (e.g., OpenAI or other SDK)

def load_credentials():
    load_dotenv()
    dr_key = os.getenv("DEEP_RESEARCH_API_KEY")
    if not dr_key:
        raise RuntimeError("DEEP_RESEARCH_API_KEY not set in environment")
    # Expose for downstream calls (or initialize your Deep Research client here)
    os.environ["DR_API_KEY"] = dr_key

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
    # TODO

def call_deep_research(prompt: str) -> str:
    """
    Invoke the Deep Research API with `prompt` and return the raw result.
    """
    # TODO

def write_report(content: str):
    """
    Write `content` to reports/FS23_deep_research_plan.md and commit it.
    """
    # TODO

def main():
    load_credentials()
    fs_items = parse_roadmap()
    prompt = build_prompt(fs_items)
    plan = call_deep_research(prompt)
    write_report(plan)

if __name__ == "__main__":
    main()
