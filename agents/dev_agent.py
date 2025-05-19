"""Minimal DevAgent implementation for CAP-X.

This module exposes a convenience ``get_dev_agent`` function that returns
an ADK ``Agent`` instance backed by LiteLLM.  No tools are wired yet.
"""

from google.adk import Agent as _Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(model="openai/codex-mini-latest")
SYSTEM_PROMPT = (
    "You are DevAgent, an autonomous developer inside a constrained sandbox. "
    "For now you only reply with plain text."
)


class DevAgent(_Agent):
    """Minimal DevAgent wrapper with a simple ``run`` method."""

    def run(self, prompt: str) -> str:  # noqa: D401
        """Return a stubbed response."""
        return "pong"


dev_agent = DevAgent(
    name="DevAgent",
    model=model,
    instruction=SYSTEM_PROMPT,
    tools=[],
)


def get_dev_agent() -> _Agent:
    """Return the singleton ``Agent`` instance."""
    return dev_agent


# python -c "from agents.dev_agent import get_dev_agent; \
# print(get_dev_agent().run('ping'))"
