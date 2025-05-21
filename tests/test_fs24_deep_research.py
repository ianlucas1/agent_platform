import sys
import os
from pathlib import Path

# Ensure the repo root is on sys.path so we can import scripts
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, repo_root)

# import the module's main entrypoint
from scripts.run_deep_research import main as run_deep_research_main

def test_fs24_deep_research_plan_created(tmp_path, monkeypatch):
    """
    FS24: Verify that running the Deep Research wrapper creates the plan file.
    """
    # Arrange: fresh reports directory, switch CWD
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()
    monkeypatch.chdir(tmp_path)

    # Point the wrapper at our tmp_path output
    output_path = reports_dir / "FS23_deep_research_plan.md"
    monkeypatch.setattr(sys, "argv", ["run_deep_research.py", "--output", str(output_path)])

    # Act: call in-process
    run_deep_research_main()

    # Assert: the plan file was created
    assert output_path.exists(), f"Expected plan file at {output_path}"  # nosec B101
