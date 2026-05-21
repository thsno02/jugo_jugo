# Resource Acquisition Protocol

## Goal

Build a local raw knowledge database for the LLM Wiki research project. The database should cover:

- Karpathy's original post / gist and related launch discussion.
- Community implementations, plugins, templates, and frameworks.
- Blog posts and guides explaining or critiquing the pattern.
- Papers, package pages, directories, and discussion threads.

## Current Stage

Only acquire and preserve raw material. Do not summarize, rank, deduplicate aggressively, or compile a final wiki yet.

## Source Rules

- Store immutable raw files whenever possible.
- Store extracted readable text as a convenience artifact, but keep the original HTML/PDF/JSON.
- Keep source URL, final URL, content type, status, hash, fetch time, and local paths in manifests.
- For GitHub repositories, shallow clone the repository and save GitHub API metadata when available.
- For arXiv papers, prefer source bundles from `https://arxiv.org/e-print/<id>` over PDFs. Extract `.tex`, `.bib`, `.bbl`, `.sty`, `.cls`, `.md`, `.txt`, and metadata files into an agent-readable bundle.
- For discussion platforms, preserve both the HTML page and any public JSON endpoint that is reachable.
- Do not bypass auth, paywalls, robots restrictions, or private content.

## Tooling Policy

The first pass uses only already-installed tools: `git`, `gh`, `curl`/`wget`, Python, and `requests`.

Optional extraction packages such as `beautifulsoup4`, `trafilatura`, and `readability-lxml` require user approval before installation. They are useful for higher-quality extraction but are not required for raw acquisition. Avoid relying on PDF parsing for arXiv when TeX/source is available.
