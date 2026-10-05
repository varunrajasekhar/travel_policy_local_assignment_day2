from __future__ import annotations

from deepagents import create_deep_agent
from langchain_ollama import ChatOllama

from rag import search_travel_knowledge



MODEL_NAME = "llama3.2:3b"
model = ChatOllama(model=MODEL_NAME, temperature=0)


TRAVEL_AGENT_INSTRUCTIONS = """
You are a travel-policy assistant. For every company-specific travel question,
first use the search_travel_knowledge tool to retrieve relevant policy content.
Base your answer only on the retrieved content, and cite the source filename or
filenames provided with the relevant results.

Do not invent or infer policy rules, limits, approval requirements, or exceptions.
Do not create new hallucinations of travel rules or policies.
If the knowledge base does not contain enough information to answer, say so
clearly and identify what information is missing. Distinguish policy facts from
any general guidance, and do not present general guidance as company policy.

The rules are clearly defined in the company's travel policy documents. The knowledge base contains these rules, and you should rely on it for accurate information. If anything is unclear or missing, clearly indicate it with soft error or warning note.
""".strip()


def build_agent(model):
    """Create the Deep Agent for the local travel-policy assistant."""

    # TODO 5
    # Build the agent with create_deep_agent using:
    # - model=model
    # - tools=[search_travel_knowledge]
    # - system_prompt=TRAVEL_AGENT_INSTRUCTIONS
    # - subagents=[]
    #
    # # TODO: implement
    # raise NotImplementedError("TODO 5: build the Deep Agent")

    agent = create_deep_agent(
        model=model,
        tools=[search_travel_knowledge],
        system_prompt=TRAVEL_AGENT_INSTRUCTIONS,
        subagents=[]
    )
    return agent
