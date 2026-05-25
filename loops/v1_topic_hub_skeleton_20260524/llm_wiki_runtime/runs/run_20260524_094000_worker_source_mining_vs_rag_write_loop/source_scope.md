# Source Scope

run_id:: run_20260524_094000_worker_source_mining_vs_rag_write_loop
executor_role:: cand_010_vs_rag_write_loop source-mining worker
target_candidate:: cand_010_vs_rag_write_loop

## Scope Rationale

This source batch covers the smallest comparison needed before planning a node: LLM Wiki's durable wiki/writeback maintenance loop versus RAG, GraphRAG, and adjacent agent-memory systems. It intentionally excludes broad enterprise comparison, implementation ecosystem survey, empirical superiority claims, and PKM/documentation taxonomy.

## In-Scope Sources

Primary LLM Wiki pattern and discourse:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`

LLM Wiki implementation evidence:

- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`

RAG / GraphRAG / citation technical evidence:

- `data/raw/arxiv/arxiv-graphrag/text.txt`
- `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex`
- `data/raw/arxiv/arxiv-ragas/text.txt`
- `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex`
- `data/raw/arxiv/arxiv-alce/text.txt`
- `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex`

Agent memory adjacency:

- `data/raw/arxiv/arxiv-zep/text.txt`
- `data/raw/arxiv/arxiv-zep/source/main.tex`
- `data/raw/webpage/langchain-long-term-memory-docs/text.txt`

Secondary framing:

- `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`

Prior KB anchors:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`

## Readability Verification

Byte-size/readability checks were run for the main local source files:

- `karpathy-gist-llm-wiki/text.txt`: 11985 bytes, readable by `sed`.
- `hacker-news-original-thread/text.txt`: 50430 bytes, readable by `rg`.
- `repo-atomicstrata-llm-wiki-compiler/repo/README.md`: 23143 bytes, readable by `rg`.
- `clawhub-llm-wiki-karpathy/text.txt`: 8201 bytes, readable.
- `atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`: 33045 bytes, readable by `sed`/`rg`.
- `arxiv-graphrag/text.txt`: 5465 bytes, readable; TeX source also readable.
- `arxiv-ragas/text.txt`: 5020 bytes, readable; TeX source also readable.
- `arxiv-alce/text.txt`: 5177 bytes, readable; TeX source also readable.
- `arxiv-zep/text.txt`: 5435 bytes, readable; TeX source also readable.
- `langchain-long-term-memory-docs/text.txt`: 11355 bytes, readable.

No in-scope raw path was declared empty.

