# Source Inventory

## Primary LLM Wiki Sources

| source_id | path | type | readable state | use |
|---|---|---|---|---|
| `karpathy-gist-llm-wiki` | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | primary idea file | readable, 11985 bytes | Canonical LLM Wiki pattern: RAG contrast, persistent wiki, raw/wiki/schema, ingest/query/lint/index/log, filed-back answers. |
| `hacker-news-original-thread` | `data/raw/hacker_news/hacker-news-original-thread/text.txt` | primary early discussion record | readable, 50430 bytes | Early public boundary debate: "just RAG" claims, write-loop pushback, static corpus vs mutable wiki, scale and second-order risk concerns. |
| `repo-atomicstrata-llm-wiki-compiler` | `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` | implementation evidence | readable, 23143 bytes | Concrete implementation of compile, query `--save`, provenance, index rebuild, lint, retrieval/search, MCP, and explicit "Why not just RAG?" comparison. |
| `clawhub-llm-wiki-karpathy` | `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` | implementation/runtime listing | readable, 8201 bytes | Prior architecture/workflow support for raw/wiki/schema runtime, lint, index/log, and agent/tool boundary; used only as implementation support. |

## Primary / Technical Adjacent Sources

| source_id | path | type | readable state | use |
|---|---|---|---|---|
| `arxiv-graphrag` | `data/raw/arxiv/arxiv-graphrag/text.txt`; `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex` | primary technical paper | readable, 5465-byte abstract page plus TeX | RAG baseline and GraphRAG contrast: query-time retrieval, graph index, pregenerated community summaries, map-reduce answers. |
| `arxiv-ragas` | `data/raw/arxiv/arxiv-ragas/text.txt`; `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex` | primary technical paper | readable, 5020-byte abstract page plus TeX | RAG as retrieval + LLM generation over reference textual database; evaluation axes: faithfulness, answer relevance, context relevance. |
| `arxiv-alce` | `data/raw/arxiv/arxiv-alce/text.txt`; `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex` | primary technical paper | readable, 5177-byte abstract page plus TeX | Citation-generation benchmark; retrieval supporting evidence and generating answers with citations; complete citation support remains difficult. |
| `arxiv-zep` | `data/raw/arxiv/arxiv-zep/text.txt`; `data/raw/arxiv/arxiv-zep/source/main.tex` | primary technical paper | readable, 5435-byte abstract page plus TeX | Agent-memory adjacent system: dynamic temporal KG, memory retrieval, historical relationships, source traceability from semantic artifacts to episodes. |
| `langchain-long-term-memory-docs` | `data/raw/webpage/langchain-long-term-memory-docs/text.txt` | technical documentation | readable, 11355 bytes | Agent long-term memory store: persistent JSON documents, namespaces/keys, read/write tools, search. |

## Secondary / Market Framing

| source_id | path | type | readable state | use |
|---|---|---|---|---|
| `atlan-llm-wiki-vs-rag-dynamic-20260524` | `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` | secondary/product explainer | readable, 33045 bytes | Useful for comparison vocabulary and scale/governance framing; not primary authority for Karpathy's definition or RAG technical claims. |

## Prior KB Anchors

| node_id | path | role |
|---|---|---|
| `20260524_062000_llm_wiki_origin_and_canon` | `kb/20260524_062000_llm_wiki_origin_and_canon.md` | Prior adopted boundary: bounded canon and overclaim limits. |
| `20260524_072000_llm_wiki_working_definition` | `kb/20260524_072000_llm_wiki_working_definition.md` | Prior adopted definition: source-preserving, compiled wiki artifact, schema/instruction governance, maintenance loop. |
| `20260524_080000_llm_wiki_three_layer_architecture` | `kb/20260524_080000_llm_wiki_three_layer_architecture.md` | Prior adopted architecture: raw/wiki/schema layers and support infrastructure. |
| `20260524_084000_llm_wiki_ingest_compile_query_lint_workflow` | `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md` | Prior adopted workflow: ingest, compile, query, lint, update/file-back, index/log. |

## Source Class Boundary

Prior KB anchors are not new fact sources. They are planning anchors and citation-boundary constraints for the downstream node. Primary claims should cite raw local sources and technical papers/docs directly.

