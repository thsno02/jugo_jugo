# LLM Wiki Raw Knowledge Database

This repository is a raw-source acquisition workspace for researching the LLM Wiki pattern: Andrej Karpathy's original "LLM Knowledge Bases" idea file, community implementations, blog posts, papers, package pages, and discussions.

The current stage is intentionally raw. We preserve source material and metadata first; synthesis into a wiki comes later.

## Layout

- `data/manifests/seed_sources.json`: curated source queue.
- `data/manifests/sources.jsonl`: latest fetch result for each source.
- `data/logs/source_access_log.jsonl`: append-only access log.
- `data/raw/`: downloaded HTML, text, arXiv source bundles, JSON, and shallow GitHub clones.
- `scripts/fetch_sources.py`: dependency-light fetcher for the current stage.
- `docs/RESEARCH_PROTOCOL.md`: acquisition protocol and operating rules.

## Run

```bash
python3 scripts/fetch_sources.py --manifest data/manifests/seed_sources.json
```

Use `--skip-repos` for a fast webpage-only pass, or `--only ID` to refetch a single source.

For arXiv entries, the fetcher prioritizes `https://arxiv.org/e-print/<id>` source bundles and extracts TeX/BibTeX-style files into an agent-readable `agent_source_bundle.txt`. PDF is kept only when arXiv does not expose TeX source.
