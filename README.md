# Day 2 Local Assignment - Grounded Travel Policy Deep Agent

This starter project is intentionally incomplete. Complete the TODOs in `rag.py` and `agent.py`, then run the finished assistant locally with `python main.py`.

## Files you should edit

- `rag.py`
- `agent.py`

Do not change the travel-policy facts in `knowledge/`.

## Local setup

1. Install Python 3.11+.
2. Install Ollama and make sure it is running.
3. Pull the local model:
   `ollama pull llama3.2:3b`
4. Create and activate a virtual environment.
5. Install dependencies:
   `pip install -r requirements.txt`
6. Complete all TODOs in `rag.py` and `agent.py`.
7. Run:
   `python main.py`

The first run of the embedding model may download `sentence-transformers/all-MiniLM-L6-v2` if it is not already cached on your computer.

See the separate assignment instruction document for the full requirements and submission expectations.
