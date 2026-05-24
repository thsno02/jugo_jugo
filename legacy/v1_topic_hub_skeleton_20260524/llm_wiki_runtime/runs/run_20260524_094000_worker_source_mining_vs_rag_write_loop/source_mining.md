# Source Mining

run_id:: run_20260524_094000_worker_source_mining_vs_rag_write_loop
target_candidate:: cand_010_vs_rag_write_loop

## Mined Observations

| source_id | evidence class | observation | candidate implication |
|---|---|---|---|
| `karpathy-gist-llm-wiki` | observed fact | RAG is described as uploading files, retrieving chunks at query time, and generating an answer. | RAG is an explicit comparison target in the canonical idea file. |
| `karpathy-gist-llm-wiki` | observed fact | The proposed pattern incrementally builds and maintains a persistent wiki between user and raw sources. | The distinction is durable compiled artifact and maintenance, not "no retrieval." |
| `karpathy-gist-llm-wiki` | observed fact | Ingest updates summaries, entity/concept pages, index, and log; query answers can be filed back; lint checks contradictions, stale claims, orphans, gaps, and links. | First-version node can center writeback/lint/index/log as the LLM Wiki side of the boundary. |
| `hacker-news-original-thread` | discourse note | Early commenters argued both sides: "just RAG" because retrieval remains, versus "write loop" because the LLM authors/maintains the wiki and files outputs back. | Use HN as evidence that the boundary question existed immediately, while avoiding technical overclaim. |
| `repo-atomicstrata-llm-wiki-compiler` | implementation evidence | README states RAG retrieves chunks at query time and "nothing accumulates"; `llmwiki` compiles sources into a persistent, browsable artifact. | Strong implementation support for durable artifact and compounding query semantics. |
| `repo-atomicstrata-llm-wiki-compiler` | implementation evidence | `query --save` writes answers as pages and rebuilds the index; README also documents citation/provenance markers, lint validation, candidates, MCP, search, and embeddings. | Retrieval can be part of LLM Wiki implementation; writeback/provenance/lint make the boundary more precise. |
| `arxiv-graphrag` | observed fact | RAG retrieves records relevant to a query and fits them into context; GraphRAG builds a graph index and pregenerated community summaries for global sensemaking. | Do not describe RAG as always stateless or only raw chunk search; GraphRAG has durable indexing/summarization artifacts. |
| `arxiv-ragas` | observed fact | RAG systems consist of retrieval and LLM generation over a reference textual database; evaluation covers faithfulness, answer relevance, and context relevance. | Supports RAG side as retrieval-generation/evaluation frame. |
| `arxiv-alce` | observed fact | Citation-generation systems retrieve supporting evidence and generate answers with citations; complete citation support remains difficult. | Supports citation/verifiability overlap; does not imply LLM Wiki superiority. |
| `arxiv-zep` | observed fact | Zep/Graphiti dynamically synthesizes message/business data into a temporal KG, maintains historical relationships, invalidates contradictions, and traces artifacts back to source episodes. | Agent memory overlaps with write/update and traceability; distinguish by artifact surface and workflow objective. |
| `langchain-long-term-memory-docs` | observed fact | LangChain long-term memory stores persistent JSON documents by namespace/key and exposes read/write/search through tools. | Adjacent memory write loop; not equivalent to a maintained wiki/node artifact. |
| `atlan-llm-wiki-vs-rag-dynamic-20260524` | secondary/process note | Frames compile-time vs query-time knowledge assembly and scale/governance caveats. | Optional secondary framing only; avoid using vendor claims as primary evidence. |

## Candidate Knowledge

LLM Wiki and RAG overlap on external knowledge access, retrieval, synthesis, citations, and indexing. A bounded node should therefore avoid "LLM Wiki bypasses RAG" as a blanket claim. The source-backed distinction is artifact/workflow-centered: LLM Wiki treats the compiled wiki/node/card layer as the durable knowledge artifact that humans and agents can browse, cite, lint, update, and extend through writeback. RAG and GraphRAG define retrieval or index/summarization mechanisms that ground answer generation; agent memory systems add persistence and update mechanisms, but their durable artifacts are stores/graphs/memory services rather than necessarily a maintained wiki layer.

## Citation Feasibility

Strong for bounded first version. Direct citations can support each side of the comparison without new retrieval.

