# Next Task Packet

task_name:: cand_010_vs_rag_write_loop_node_planning
target_candidate:: cand_010_vs_rag_write_loop
decision:: ready_to_plan
recommended_target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
recommended_node_slug:: llm_wiki_vs_rag_write_loop

## Objective

Plan the first-version node for the bounded comparison slice: LLM Wiki vs RAG/write-loop systems. Do not plan a broad hub node for all adjacent systems. The node should answer one constrained question: what is the minimum source-backed difference between LLM Wiki's maintained wiki/node artifact and RAG/GraphRAG/agent-memory retrieval, synthesis, and update mechanisms?

## Evidence Scope

Use primary/technical sources directly:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex`
- `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex`
- `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex`
- `data/raw/arxiv/arxiv-zep/source/main.tex`
- `data/raw/webpage/langchain-long-term-memory-docs/text.txt`

Use optional secondary framing only if clearly labeled:

- `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`

Use prior KB anchors only as continuity/boundary constraints, not as new fact sources:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`

## Required Planning Artifacts

- `planner_report.md`
- `evidence_scope.yaml`
- `generation_entry_gate.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`

## Non-Goals

- Do not write "LLM Wiki is better than RAG."
- Do not claim RAG lacks indexes, summaries, citations, memory, or durable internal artifacts.
- Do not write a broad comparison with PKM, knowledge graphs, documentation systems, data catalogs, or enterprise platforms.
- Do not claim empirical performance, token savings, scale thresholds, adoption, or enterprise readiness unless supported by a dedicated source and scoped as secondary/adjacent.
- Do not treat prior KB anchors as primary evidence for new RAG/agent-memory facts.

## Citation Constraints

- Cite Karpathy gist for original LLM Wiki pattern claims.
- Cite atomicstrata README only as implementation evidence, not universal definition.
- Cite HN only as early discourse/risk framing.
- Cite GraphRAG and Ragas for RAG/GraphRAG technical definitions and evaluation axes.
- Cite ALCE only for citation/evidence-generation evaluation overlap.
- Cite Zep and LangChain docs only for adjacent agent-memory read/write systems.
- If using Atlan, label it as secondary/product framing.

## Generation Risks

- The main risk is overcorrecting the "just RAG" debate into an anti-RAG claim. The safer framing is "not retrieval vs no retrieval; artifact boundary and maintenance loop."
- GraphRAG already has precomputed summaries and a graph index, so do not describe RAG as always stateless or always raw-chunk-only.
- Agent memory systems can write durable stores. The distinction must be artifact shape and governance loop, not mere persistence.
- Keep the first version focused on boundary, similarity, and difference; defer broad taxonomy.

