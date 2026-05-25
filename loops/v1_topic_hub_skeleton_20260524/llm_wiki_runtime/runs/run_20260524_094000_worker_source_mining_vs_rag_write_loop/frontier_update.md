# Frontier Update

run_id:: run_20260524_094000_worker_source_mining_vs_rag_write_loop
executor_role:: cand_010_vs_rag_write_loop source-mining + frontier-update worker
target_candidate:: cand_010_vs_rag_write_loop
decision:: ready_to_plan

## Decision

`cand_010_vs_rag_write_loop` is ready_to_plan. In canonical frontier terms, the candidate should be moved to `ready_to_build` because source mining has established enough evidence for a bounded first version and no unresolved retrieval blocker remains.

## Evidence State

evidence_state:: enough_for_first_version
retrieval_required_before_build:: false
citation_feasibility:: strong_for_bounded_comparison_node

The first version can cite local primary/technical sources directly:

- LLM Wiki side: Karpathy gist, HN thread for early discourse, atomicstrata compiler implementation.
- RAG/GraphRAG side: GraphRAG and Ragas primary papers; ALCE for citation-generation/evidence overlap.
- Agent-memory/write-loop adjacency: Zep technical paper and LangChain long-term memory docs.
- Secondary vocabulary only: Atlan explainer.
- Prior KB anchors only for boundary and continuity: adopted origin, definition, architecture, and workflow nodes.

## Candidate Statement

LLM Wiki and RAG both connect LLMs to external knowledge and may both use retrieval, indexing, summaries, citations, and iterative synthesis. The bounded first-version difference is not "retrieval vs no retrieval"; it is that LLM Wiki centers a durable, human/agent-browsable wiki/node artifact maintained by ingest, compile, query, lint, update/file-back, provenance, index, and log workflows. RAG and GraphRAG center retrieval or graph/summarization indexes for grounding query-time generation; adjacent agent-memory systems add persistent read/write stores or temporal graphs, but those are not automatically the same artifact boundary as LLM Wiki's raw/wiki/schema maintenance loop.

## Status Recommendation

- frontier status: `ready_to_build`
- node-planning decision label: `ready_to_plan`
- next_action: `node_planning`
- proposed_node_slug: `llm_wiki_vs_rag_write_loop`
- proposed_node_id: `20260524_094000_llm_wiki_vs_rag_write_loop`

## Remaining Gaps

No blocker for a bounded first version. Later broader comparison work should still mine separate candidates for:

- PKM/documentation systems beyond this RAG/write-loop slice.
- Enterprise scale and governance limits using better primary/non-vendor sources.
- Empirical claims about superiority, quality, scale, or token efficiency.
- Broad agent-memory taxonomy beyond Zep/LangChain examples.

