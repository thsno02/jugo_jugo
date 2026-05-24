# Source Notes

## Primary Implementation Patterns

`repo-nashsu-llm-wiki` supports a UI/desktop/web-app pattern. Its README describes a two-step ingest workflow, multimodal/image ingestion, graph relevance signals, clustering, vector semantic search, persistent queues, auto-watch, deep research, async review, web clipper, and a local HTTP API. Its `github_repo.json` snapshot records high surface activity among the local captures: 8658 stars, 1069 forks, 109 open issues, TypeScript, created 2026-04-08, updated 2026-05-21, pushed 2026-05-19.

`repo-samuraigpt-llm-wiki-agent` supports a coding-agent skill/template pattern. Its README lays out `raw/`, `wiki/`, `index.md`, `log.md`, `overview.md`, `sources/`, `entities/`, `concepts/`, `syntheses/`, and `graph/` artifacts; it documents ingest, query, lint, and graph commands, multi-format conversion, contradiction flags, graph visualization, and Obsidian browsing.

`repo-sdyckjq-llm-wiki-skill` supports a Chinese/multiplatform skill ecosystem pattern. Its README is useful for graph UX, confidence labels, cache, conversation crystallization, hooks, reports, comparison tables, and timeline outputs. Treat it as project self-description, not independent effectiveness evidence.

`repo-atomicstrata-llm-wiki-compiler` is strong engineering evidence for a CLI/MCP compiler family. It documents ingest, compile, query, view, lint, watch, review candidates, paragraph source markers, source-range citations, confidence and contradiction metadata, per-concept prompt budgets, chunked retrieval/reranking, and a roadmap that still leaves evaluation harness and some lifecycle controls as future work.

`repo-kytmanov-obsidian-local` is strong local-first evidence. It documents `olw` commands for init/run/ingest/compile/review/query/lint/watch, Obsidian vault output, provider switching across local and OpenAI-compatible endpoints, isolated compare previews, source hashes, rejection feedback injection, low-confidence/sparse-source draft annotations, no-vector query mode up to about 100 source notes, and hand-edit protection.

`repo-vectifyai-openkb` provides a long-document/OpenKB implementation adjacent to LLM Wiki. It supports the ecosystem node as a long-document/wiki-generator family, especially PageIndex-style long-PDF handling, MarkItDown conversion, multimodality, wiki foundation, query/chat generators, and skill factory. Do not use it as proof that every LLM Wiki handles long PDFs well.

`repo-ngmeyer-librarian-mcp` supports an adjacent MCP/graph-vault family. It productionizes the Karpathy LLM Wiki pattern as an MCP server for Obsidian/plain Markdown vaults with graph traversal, auto-wikilinks, trigram search, Louvain community detection, D3 graph visualization, and slash-command skill wrappers.

## Package and Plugin Signals

`pypi-my-llm-wiki` records package metadata for `my-llm-wiki` 0.9.0, beta, MIT, Python >=3.10, with a package summary about turning folders into queryable knowledge graphs. The page claims the implementation covers raw files, compiled wiki, and schema layers and supports code, markdown/text, documents, and images. This is registry/package evidence, not package download or adoption evidence.

`pypi-llm-wiki-mcp` records package metadata for `llm-wiki-mcp` 0.1.1, alpha, MIT, Python >=3.11, described as MCP server plus Claude Code skills. It documents four MCP tools (`wiki_read`, `wiki_write_page`, `wiki_log_append`, `wiki_inventory`), four skills (`wiki-init`, `wiki-ingest`, `wiki-query`, `wiki-lint`), atomic writes, etag conflict checks, append-only log integrity, path containment, and a local filesystem storage boundary.

`clawhub-llm-wiki-karpathy` is plugin-directory evidence for a runtime shipped as standalone CLI, stdio MCP server for Claude Code/Codex/Cursor/Gemini CLI and similar clients, config generator, and OpenClaw-compatible host entry. It also describes raw/wiki/schema structure, multimodal raw kinds, representation storage, source-id repair, compile-readiness tracking, gap mapping, and deterministic lint.

`llm-wiki-net` is project-page evidence for a command/plugin implementation across Claude Code, OpenAI Codex, OpenCode, Pi, and portable AGENTS.md. It describes a topic-hub model, immutable raw sources, compiled topic/concept/reference articles, inventory and dataset manifests, archive lifecycle, audit, output generation, and offline behavior for compile/query/lint once a wiki exists. Treat as project self-description.

## Adoption/Activity Signal Boundary

The local `github_repo.json` files for 15 acquired repos provide concrete metadata snapshots. In the local snapshot, the largest preserved star counts are `nashsu/llm_wiki` 8658, `AgriciDaniel/claude-obsidian` 5296, `SamurAIGPT/llm-wiki-agent` 2697, `VectifyAI/OpenKB` 1879, `sdyckjq-lab/llm-wiki-skill` 1589, `Ar9av/obsidian-wiki` 1408, and `atomicstrata/llm-wiki-compiler` 1250. These are surface repository signals only. They do not prove usage, quality, production deployment, package downloads, or community consensus.

## Secondary/Process Notes

`reports/source_gap_review.md` says UX/tooling/ecosystem coverage is strong enough for a preliminary landscape memo, but adoption/community discourse remains incomplete because Reddit is blocked, package downloads are absent, and directory/plugin pages often lack usage counts.

`reports/coverage_framework.md` requires representative implementation survey without treating any single implementation as definitive; it lists tool families such as Obsidian templates, coding-agent workflows, MCP servers, repo templates, desktop apps, local-first systems, research prototypes, enterprise tools, graph tools, retrieval-first tools, and documentation compilers.

