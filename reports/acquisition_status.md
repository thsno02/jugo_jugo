# LLM Wiki Resource Acquisition Status

Last updated: 2026-05-21 19:06:31 +0800

## Snapshot

- Seed sources: 45
- Successful acquisitions: 38
- Blocked sources: 6
- HTTP/network-intercept failures: 1
- Raw data size: about 162 MB
- Raw files: 2,765
- GitHub repositories cloned: 15
- arXiv source entries: 3
- arXiv TeX/source archives extracted: 2
- arXiv PDF-only source entries: 1

## Acquired Coverage

- Origin material: Karpathy gist raw text, X launch-post JSON mirror, Hacker News original thread and mirror.
- Web/blog/directory material: LLM Wiki directories, conceptual explainers, Obsidian/OpenClaw plugin pages, multilingual guides, enterprise/case-study posts.
- Package/paper material: PyPI package pages/JSON for `my-llm-wiki` and `llm-wiki-mcp`; arXiv abstract pages plus source-oriented e-print downloads for three related papers. Two papers now have extracted TeX bundles and `agent_source_bundle.txt`; one arXiv e-print endpoint only returned PDF and is marked `pdf_only`.
- GitHub material: 15 shallow-cloned repositories plus GitHub API metadata and remote READMEs.
- Discovery evidence: three GitHub search result exports in `data/discovery/`.

## Known Gaps

- Reddit is currently blocked from the terminal and browser capture paths. The seed URLs and block pages are preserved under `data/raw/reddit/`; the web search channel can see the pages, so a later pass should retry via an approved Reddit-capable API, alternate network, or manual export.
- `aicritique-enterprise-knowledge` is intercepted by a network safety page in the terminal environment. The intercepted response is preserved, but the article body was not acquired locally.
- One arXiv source endpoint returned only PDF (`arxiv-knowledge-compounding`). This is preserved as `source.pdf` with a `pdf_only` metadata note because no TeX source was available from `e-print`.

## Next Pass

- Add more source discovery around Hacker News descendants, GitHub topic pages, Claude/Obsidian plugin hubs, OpenClaw/ClawHub listings, and package registries.
- Retry blocked Reddit and AICritique sources before synthesis.
- Prefer TeX/source bundles for all future arXiv additions. Consider an approved install of `beautifulsoup4 trafilatura readability-lxml` only if the next stage needs cleaner HTML extraction rather than raw preservation.
