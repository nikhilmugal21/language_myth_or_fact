# language_myth_or_fact

An interactive Streamlit flashcard game that challenges common myths and facts about languages, featuring explanations and discussion prompts for classroom or self-study use.

## Run locally

```bash
pip install -r requirements.txt
streamlit run myth_or_fact.py
```

## Run in GitHub Codespaces

The repository includes `.streamlit/config.toml` so Streamlit binds to `0.0.0.0:8501` by default (required for port forwarding in Codespaces).

Start it with:

```bash
streamlit run myth_or_fact.py --server.port 8501 --server.headless true
```

If port `8501` is already in use, run:

```bash
streamlit run myth_or_fact.py --server.port 8502 --server.headless true
```
