import shutil
import subprocess  # nosec B404
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "status, expected_checkbox",
    [
        ("in_progress", "- [-]"),
        ("done", "- [x]"),
    ],
)
def test_status_updater(tmp_path, status, expected_checkbox):
    config_dir = tmp_path / "configs"
    config_dir.mkdir()
    src = REPO_ROOT / "configs" / "ROADMAP_TODO.md"
    dst = config_dir / "ROADMAP_TODO.md"
    shutil.copy(src, dst)

    script = REPO_ROOT / "scripts" / "status_updater.py"
    subprocess.run(  # nosec
        [
            "python",
            str(script),
            "FS16",
            status,
        ],
        cwd=tmp_path,
        check=True,
    )

    lines = dst.read_text().splitlines()
    for i, line in enumerate(lines):
        if "TASK:FS16" in line:
            comment_line = line
            bullet_line = lines[i + 1]
            break
    else:
        raise AssertionError("FS16 not found")

    assert f"status={status}" in comment_line  # nosec B101
    assert bullet_line.startswith(expected_checkbox)  # nosec B101
