"""Stub DevAgent implementation for CAP-X.

This module provides a minimal DevAgent placeholder to allow
importing the package before the real logic is added. It will be
filled out in FS12.
"""


class DevAgent:
    """Minimal development agent stub."""

    def __init__(self) -> None:
        self.name = "DevAgent (stub)"

    def run(self, prompt: str) -> str:
        """Return a placeholder response."""
        return "\U0001f6e0\ufe0f  DevAgent stub here \u2013 implement me in FS12!"


# python -c "from agents.dev_agent import DevAgent; print(DevAgent().run('hi'))"
