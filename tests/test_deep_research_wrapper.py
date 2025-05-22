import sys, os
from pathlib import Path

# ensure repo root is on PYTHONPATH
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, repo_root)

# import the module's main entrypoint
import scripts.run_deep_research as rdr

def test_deep_research_wrapper_creates_plan(tmp_path, monkeypatch):
    """
    Verify that running the Deep Research wrapper creates the plan file.
    """
    # Arrange: fresh reports directory, switch CWD
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()
    monkeypatch.chdir(tmp_path)

    # Stub out FS27 dependencies to avoid real file/API/git calls
    monkeypatch.setattr(rdr, "parse_roadmap", lambda: [])
    monkeypatch.setattr(rdr, "call_deep_research", lambda client, prompt: "DUMMY PLAN")
    monkeypatch.setattr(rdr, "load_credentials", lambda: None)
    monkeypatch.setattr(rdr.subprocess, "run", lambda *args, **kwargs: None)

    # Point the wrapper at our tmp_path output
    output_path = reports_dir / "FS23_deep_research_plan.md"
    monkeypatch.setattr(sys, "argv", ["run_deep_research.py", "--output", str(output_path)])

    # Act: invoke the wrapper in-process
    rdr.main()

    # Assert: the plan file was created
    assert output_path.exists(), f"Expected plan file at {output_path}"  # nosec B101 