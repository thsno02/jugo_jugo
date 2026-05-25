# Source Notes

## Source-Backed Observations

### `karpathy-gist-llm-wiki`

- observed fact: The idea file explicitly contrasts the common document experience with RAG: files are retrieved at query time and the answer is generated from relevant chunks.
- observed fact: The proposed difference is not absence of retrieval. It is that the LLM incrementally builds and maintains a persistent markdown wiki between user and raw sources.
- observed fact: New sources are read, key information is extracted, and existing entity/concept/topic pages are updated; contradictions and evolving synthesis are handled in the wiki layer.
- observed fact: Query answers can be filed back into the wiki as new pages so explorations compound rather than disappearing into chat history.
- observed fact: Lint/health-check passes look for contradictions, stale claims, orphan pages, missing pages, missing cross-references, and data gaps.
- observed fact: `index.md` and `log.md` are maintained artifacts used for navigation and history; optional search tooling can be added later.
- interpretation: The LLM Wiki side of the comparison should be written as a maintained artifact/workflow pattern, not as an anti-retrieval claim.

### `hacker-news-original-thread`

- discourse note: Multiple early comments describe LLM Wiki as "just RAG" or "persistent memory RAG" because retrieval is still needed to select relevant wiki/source material.
- discourse note: Pushback in the thread identifies the "interesting bit" as the write loop: the LLM authors and maintains the wiki, builds backlinks, files outputs back in, and runs linting/auditing passes.
- discourse note: The thread also surfaces risk/limit language: scale of linting, stale claims, second-order information, context bloat, and keeping the wiki up to date.
- candidate use: The HN thread can support early debate framing and boundary risks, but should not serve as technical proof of RAG definitions.

### `repo-atomicstrata-llm-wiki-compiler`

- implementation evidence: README explicitly states that RAG retrieves chunks at query time and "nothing accumulates"; the compiler compiles sources into a persistent browsable artifact that compounds over time.
- implementation evidence: The implementation has `query --save`, which writes answers as wiki pages and rebuilds the index so saved answers can appear in future query context.
- implementation evidence: The README documents source attribution in frontmatter, paragraph-level source markers, claim-level provenance, lint rules, candidate review, MCP tools, and viewer provenance/citation chips.
- implementation evidence: The implementation also uses retrieval/search and embeddings for query routing, showing LLM Wiki can include retrieval while still retaining a maintained wiki/writeback loop as the differentiator.
- candidate use: This is strong implementation evidence for the minimal difference: compile and save into durable markdown artifacts, with provenance/lint/review support.

### `arxiv-graphrag`

- observed fact: The paper describes canonical RAG as retrieving a subset of external corpus records small enough to fit the LLM context, then generating a response from the query and retrieved records.
- observed fact: GraphRAG builds a graph index and pregenerates community summaries, then answers by producing partial answers from summaries and reducing them into a global answer.
- interpretation: GraphRAG adds maintained intermediate indexes/summaries, so a simplistic "RAG is always stateless" claim would be wrong. The narrower distinction is that GraphRAG's durable artifacts are retrieval/summarization indexes for answering, while LLM Wiki's durable artifact is a human/agent-browsable wiki that is itself the maintained knowledge layer.
- candidate use: Use GraphRAG to avoid straw-manning RAG and to show overlap in precomputed summaries and indexing.

### `arxiv-ragas`

- observed fact: Ragas defines RAG systems as composed of retrieval and LLM-based generation modules over a reference textual database.
- observed fact: Its evaluation dimensions include whether retrieval identifies relevant/focused context, whether generation uses passages faithfully, and output quality.
- candidate use: Use as primary technical support for RAG's retrieval-generation evaluation frame. It does not support claims about durable wiki maintenance or writeback as core RAG features.

### `arxiv-alce`

- observed fact: ALCE focuses on retrieving supporting evidence and generating answers with citations; its metrics include fluency, correctness, and citation quality.
- observed fact: The paper reports room for improvement in complete citation support and synthesis from multiple sources.
- candidate use: Use to connect both systems to citation/verifiability concerns without claiming ALCE is an LLM Wiki source.

### `arxiv-zep`

- observed fact: Zep argues existing RAG frameworks for agents are limited to static document retrieval and proposes dynamic knowledge integration through a temporal knowledge graph.
- observed fact: Graphiti dynamically synthesizes conversational and business data, maintains historical relationships, invalidates contradicted edges, and supports tracing semantic artifacts back to source episodes.
- interpretation: Agent-memory systems overlap with LLM Wiki in dynamic update, traceability, and maintained intermediate representations. They differ in storage/serving abstraction: temporal KG memory service vs markdown/wiki/node artifact maintained for human and agent browsing.
- candidate use: Use to keep the downstream node honest about write-loop adjacency; do not collapse LLM Wiki into all agent memory.

### `langchain-long-term-memory-docs`

- observed fact: LangChain long-term memory stores and recalls data across conversations/sessions using JSON documents in namespaces/keys, with tool-level read/write access and search.
- candidate use: Use as docs evidence for agent memory write/read loops. It supports an adjacent comparison point, not the RAG core definition.

### `atlan-llm-wiki-vs-rag-dynamic-20260524`

- secondary/process note: The page frames the difference as compile-time vs query-time knowledge assembly and discusses scale/governance limits.
- limitation: It is a vendor/product explainer and includes broad enterprise claims; use only as secondary framing if necessary, not as primary support.

## Minimal Synthesis For Planning

The evidence supports a first-version node with this bounded claim:

LLM Wiki and RAG both connect LLMs to external knowledge and may both use retrieval, indexes, summaries, citations, and iterative processing. The least overclaimed difference is that LLM Wiki makes the maintained intermediate artifact the central durable product: raw sources are compiled into a browsable markdown/wiki/node layer, query answers can be filed back, and lint/update/index/log/provenance workflows keep that artifact usable over time. RAG and GraphRAG primarily define retrieval or index/summarization mechanisms for grounding query-time generation; adjacent agent-memory systems add write/read memory and temporal graphs, but that is not automatically the same as a human-readable wiki artifact governed by LLM Wiki's raw/wiki/schema workflow.

