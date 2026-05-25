# Evidence Scope

run_id:: run_20260524_095000_worker_node_planning_vs_rag_write_loop
candidate_id:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
source_mining_run:: .llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop

## Primary / Local LLM Wiki Sources

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`: primary source for the LLM Wiki idea, including RAG contrast, persistent wiki artifact, raw/wiki/schema model, ingest/query/lint operations, filed-back query answers, and index/log maintenance.
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`: early discourse source for the "just RAG" debate, write-loop framing, and risk vocabulary. Do not use as technical authority for RAG definitions.
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`: implementation evidence for persistent artifact, `query --save`, index rebuild, provenance, source markers, lint, review, MCP, and retrieval/search coexistence.
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`: optional implementation/runtime listing only; use sparingly if needed for implementation support, not adoption or empirical claims.

## Primary / Technical Adjacent Sources

- `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex`: primary RAG/GraphRAG boundary source for query-time retrieval, graph index, community summaries, and map-reduce answer synthesis.
- `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex`: primary RAG evaluation source for retrieval plus LLM generation modules and faithfulness/relevance/context evaluation axes.
- `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex`: citation/evidence-generation source for overlap around retrieval-supported answers and citation quality.
- `data/raw/arxiv/arxiv-zep/source/main.tex`: adjacent agent-memory source for temporal KG memory, dynamic updates, contradiction invalidation, and episode traceability.
- `data/raw/webpage/langchain-long-term-memory-docs/text.txt`: adjacent agent-memory docs source for persistent JSON documents, namespace/key organization, read/write tools, and search.

## Secondary Process / Framing Source

- `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`: optional secondary/product framing only. If used, label it as secondary and do not let it support technical definitions, enterprise readiness, adoption, performance, or scale claims.

## Prior-KB Anchors

Use prior KB anchors only for continuity, terminology, and overclaim boundaries:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`

They must not be treated as primary evidence for new RAG, GraphRAG, ALCE, Zep, LangChain, enterprise, adoption, or empirical-performance facts.

## Citation Constraints

- Cite Karpathy gist for LLM Wiki canonical pattern claims.
- Cite atomicstrata README only as implementation evidence, not universal definition.
- Cite HN only for early discourse framing.
- Cite GraphRAG and Ragas for RAG/GraphRAG technical definitions and evaluation axes.
- Cite ALCE only for citation/evidence-generation overlap.
- Cite Zep and LangChain only for adjacent agent-memory write/read systems.
- Cite Atlan only as secondary/product framing if used at all.
- Do not import outside knowledge about RAG, GraphRAG, or agent memory unless it is cited to the allowed local sources.

## Forbidden Claims

- LLM Wiki is better than RAG.
- RAG is always stateless, raw-chunk-only, lacks indexes, lacks summaries, lacks citations, or lacks durable internal artifacts.
- GraphRAG is just ordinary RAG without precomputed structure.
- Agent memory writeback is identical to LLM Wiki.
- The comparison proves adoption, enterprise readiness, empirical quality, token savings, or scale thresholds.
- Broad PKM/documentation-system/data-catalog/knowledge-graph comparisons.

## Evidence Sufficiency

Decision: sufficient for bounded first-version generation.

No retrieval is required before generation because the local source batch directly supports the limited node scope. If generation needs broader product, enterprise, scale, adoption, or taxonomy claims, it must stop and request additional mining instead of expanding the node.

