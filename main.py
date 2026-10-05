from __future__ import annotations

from langchain_ollama import ChatOllama

from agent import build_agent
from rag import initialize_rag


MODEL_NAME = "llama3.2:3b"


def main():
    print("\nGrounded Travel Policy Assistant")
    print("--------------------------------")
    print("Preparing the local RAG knowledge base...")

    try:
        initialize_rag()
    except NotImplementedError as exc:
        print(f"\nAssignment is not complete yet: {exc}")
        return
    except Exception as exc:
        print(f"\nCould not initialize RAG: {exc}")
        return

    model = ChatOllama(model=MODEL_NAME, temperature=0)

    try:
        agent = build_agent(model)
    except NotImplementedError as exc:
        print(f"\nAssignment is not complete yet: {exc}")
        return

    print(f"Ready. Using Ollama model: {MODEL_NAME}")
    print("Ask a company travel-policy question. Type 'exit' or 'quit' to finish.\n")

    conversation = []
    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        conversation.append({"role": "user", "content": question})

        try:
            result = agent.invoke({"messages": conversation})
            final = result["messages"][-1]
            answer = getattr(final, "content", str(final))
            print(f"Agent: {answer}\n")
            conversation.append({"role": "assistant", "content": answer})
        except Exception as exc:
            print(f"Agent error: {exc}\n")


if __name__ == "__main__":
    main()
