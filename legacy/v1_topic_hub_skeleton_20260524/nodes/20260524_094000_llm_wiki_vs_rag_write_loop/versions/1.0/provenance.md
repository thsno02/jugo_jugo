# Provenance

node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0

## Why this version exists

This first version exists because `cand_010_vs_rag_write_loop` reached `ready_to_build` with `evidence_state: enough_for_first_version` in the source-mining and node-planning runs. The bundle creates a candidate node for the bounded boundary between LLM Wiki as a durable wiki/node/card artifact with writeback/lint/update/provenance workflow and RAG/GraphRAG/agent-memory mechanisms for retrieval, indexing, synthesis, and memory.

This version is a candidate only. It does not adopt root metadata, write a `kb/` view, or update generated indexes.

## Inputs used

### Existing data

Read and used as primary/local LLM Wiki or discourse evidence:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`

Read and used as technical adjacent evidence:

- `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex`
- `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex`
- `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex`
- `data/raw/arxiv/arxiv-zep/source/main.tex`
- `data/raw/webpage/langchain-long-term-memory-docs/text.txt`

Read but not used in the candidate card:

- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`

### Dynamic retrieval, if any

None. No network retrieval was used.

### Prior KB nodes

Read and used only as continuity anchors and boundary controls:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`

### Process artifacts

Read and used:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/next_task_packet.md`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/node_plan.yaml`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.md`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_inventory.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_notes.md`

Out-of-scope reads: none for authority. Local `find`, `rg`, validator inspection, and existing node examples were read only to avoid overwriting other workers' files and to follow repository bundle conventions.

## Production rationale

The card centers on the selected comparison slice: artifact/workflow boundary, not product competition or broad RAG taxonomy. The LLM Wiki side is supported by the Karpathy gist and implementation evidence from the atomicstrata README. The adjacent-system side is supported directly by GraphRAG, Ragas, ALCE, Zep, and LangChain docs. The HN thread is used only to explain early discourse pressure around "just RAG" versus write-loop interpretations.

## Citation rationale

Primary factual claims about LLM Wiki cite `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` and, for implementation coexistence with retrieval/search, `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`. RAG and GraphRAG claims cite `graph_rag.tex` and `arxiv-version.tex`. Citation-quality overlap cites ALCE. Agent-memory adjacency cites Zep and LangChain docs. Prior KB citations are included only as references for continuity, not as footnote support for new adjacent-system facts.

## Synthesis decisions

- Source-backed observation: LLM Wiki is framed as a persistent markdown/wiki artifact maintained between users and raw sources.
- Source-backed observation: LLM Wiki operations include ingest, query file-back, lint, index, and log maintenance.
- Source-backed observation: a concrete llm-wiki-compiler implementation includes query save, index rebuild, provenance, lint/review, MCP, retrieval/search, and embeddings.
- Source-backed observation: canonical RAG retrieves relevant external records for query-time generation; GraphRAG uses a graph index, community summaries, and map-reduce answer synthesis.
- Source-backed observation: Ragas evaluates retrieval and LLM generation modules through context relevance, faithfulness, and answer relevance.
- Source-backed observation: ALCE evaluates retrieval-supported answers with citations through fluency, correctness, and citation quality.
- Source-backed observation: Zep/Graphiti and LangChain long-term memory provide adjacent persistent memory/write-read/traceability mechanisms.
- Interpretation: the least overclaimed boundary is not retrieval vs no retrieval, but maintained wiki/node/card artifact plus workflow versus retrieval/index/synthesis/memory mechanisms.
- Evidence gap: no superiority, adoption, scale, enterprise, benchmark, access-control, concurrency, token-efficiency, or broad ecosystem conclusion is made.

## Audit trail

The version bundle was generated by `worker_executor` from `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/next_task_packet.md`. The generation entry gate result was `pass`. The allowed output paths were limited to the version bundle and generation run artifacts. Root node metadata, `kb/`, and `generated/` were intentionally not written.

## Adoption rationale

Adoption is pending audit. This version is acceptable as a candidate because it keeps the comparison narrow, cites all adjacent-system technical claims to allowed local sources, labels HN as discourse, avoids Atlan as authority, and preserves the root metadata adoption gate. It should not be adopted until citation and adoption audit confirms parseability, source support, provenance completeness, overclaim control, and root metadata gating.

## Limits and uncertainty

This candidate does not prove that LLM Wiki is better than RAG, that RAG lacks durable artifacts or write paths, that GraphRAG is only raw chunk retrieval, or that agent memory is equivalent to LLM Wiki. It does not evaluate adoption, implementation maturity, scale, cost, speed, citation accuracy, governance, access control, privacy, concurrency, enterprise readiness, or broad benchmark performance.

## Revision triggers

- Audit finds citation parsing errors, unresolved paths, unsupported claims, or source/category confusion.
- Audit finds anti-RAG framing, superiority claims, or claims that exceed the artifact/workflow boundary.
- New authorized source mining adds broader RAG taxonomy, implementation comparison, enterprise/governance evidence, benchmark evidence, or neutral agent-memory taxonomy.
- Any prior adopted LLM Wiki anchor receives a major update that changes origin/canon, working definition, architecture, or workflow boundaries.
- A later audit or adoption worker requires a different schema field shape for candidate node metadata.
