from __future__ import annotations

from deepagents import create_deep_agent

from rag import search_travel_knowledge


TRAVEL_AGENT_INSTRUCTIONS = """
TODO 4: Replace this placeholder with the system instructions for the travel-policy assistant.

Your completed prompt must make the agent:
- retrieve relevant company policy before answering company-specific travel questions
- treat retrieved policy content as the source of truth
- cite the source filename(s) it used
- never invent policy rules, limits, approvals, or exceptions
- clearly state when the knowledge base does not contain enough information
""".strip()


def build_agent(model):
    """Create the Deep Agent for the local travel-policy assistant.

    TODO 5
    Build the agent with create_deep_agent using:
    - model=model
    - tools=[search_travel_knowledge]
    - system_prompt=TRAVEL_AGENT_INSTRUCTIONS
    - subagents=[]
    """
    # TODO: implement
    raise NotImplementedError("TODO 5: build the Deep Agent")
