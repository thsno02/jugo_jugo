# LLM Wiki 与 RAG/write-loop 系统的 artifact/workflow 边界

这个节点的工作定义是：LLM Wiki 与 RAG 的关键边界不是“有没有 retrieval”，而是中心产物不同。LLM Wiki 把 raw sources 编译并维护成可浏览、可链接、可被人和 agent 反复检查的 wiki/node/card artifact；RAG、GraphRAG 和 agent-memory 系统则主要提供 retrieval、index、summarization、answer synthesis 或 memory read/write 机制。两边会重叠，但不应被合并成“有 retrieval 就都是 RAG”或“有 writeback 就都是 LLM Wiki”。[^1][^2][^3]

**来源支持的观察：LLM Wiki 的 artifact 边界。** Karpathy gist 明确把常见文档体验写成 query-time chunk retrieval，再提出不同点：LLM 逐步构建和维护一个位于用户与 raw sources 之间的 persistent markdown wiki。这个 wiki 会随新来源和新问题积累，页面、cross-reference、矛盾提示和综合不是每次问答从零重做，而是被保存在 durable artifact 中。这里的“durable”不是说不需要检索，而是说检索和综合服务于一个持续维护的 wiki 层。[^1]

**来源支持的观察：writeback/lint/update loop。** LLM Wiki 一侧还包括维护动作：新来源进入 raw collection 后，LLM 读取、摘要、更新 index 和相关 entity/concept pages，并向 log 追加记录；query 生成的有价值答案可以 filed back into the wiki；lint 检查 contradiction、stale claim、orphan page、missing page、missing cross-reference 和 data gap。这支持“artifact/workflow boundary”，但不支持自动推出质量、规模、成本或企业治理结论。[^1][^9]

**实现证据：retrieval 可以共存。** `llm-wiki-compiler` README 把自身描述为把来源编译成 persistent browsable artifact，并将 `query --save` 写成把答案保存为 wiki page、立即重建 index、让保存答案进入后续查询上下文。同时，这个实现也有 chunked retrieval、semantic search、embeddings、MCP、lint、review queue、claim-level provenance 和 viewer citation chips。它说明 LLM Wiki 实现可以包含 retrieval/search；因此，把边界写成 retrieval vs no retrieval 会误伤证据。[^2]

**RAG/GraphRAG 的相邻边界。** GraphRAG paper 对 canonical RAG 的描述是：系统从外部 corpus 检索与 query 相关且能放入 context window 的 records，再基于 query 与 retrieved records 生成回答。GraphRAG 进一步用 LLM 构建 graph index，生成 community summaries，并用 map-reduce over summaries 来回答 global questions。Ragas paper 也把 RAG systems 写成 retrieval module 与 LLM generation module，并评价 context relevance、faithfulness 和 answer relevance。基于这些证据，RAG/GraphRAG 不能被简化为“只会 raw chunk lookup”或“没有持久中间结构”。[^4][^5]

**最小差异不是是否有 index，而是 index/artifact 的用途。** GraphRAG 的 graph index 和 community summaries 是回答全局问题的 retrieval/summarization infrastructure；LLM Wiki 的 wiki/node artifact 是被维护、被浏览、被引用、被 lint、被写回的知识层。这个说法是综合性解释：它不是说 GraphRAG 没有 durable intermediate artifacts，也不是说 LLM Wiki 不需要检索；它只是把当前证据支持的中心对象分开。[^1][^2][^4]

**citation/provenance 的重叠不等于等价。** ALCE 关注端到端系统 retrieval supporting evidence 并生成带 citations 的答案，评价 fluency、correctness 和 citation quality；Ragas 也把 faithful use of passages 作为 RAG 评价维度。这些工作与 LLM Wiki 的 provenance/citation 关切重叠：都关心答案是否受证据支持。但 citation-quality evaluation 本身不等于维护一个 wiki/node/card artifact，也不自动提供 file-back、lint、index/log、版本化 provenance 或 node adoption workflow。[^5][^6][^2]

**agent memory 是相邻系统，不是同义词。** Zep/Graphiti 把 agent memory 做成 temporal knowledge graph：episodes 保存 message/text/JSON，semantic artifacts 可追溯到 source episodes，新信息可动态更新并使矛盾 edge invalidated。LangChain long-term memory docs 则描述跨 conversations/sessions 持久化的 JSON documents，按 namespace/key 组织，并由 tools read/write/search。这些都支持“persistent memory/write-read mechanisms are adjacent”。但当前证据只支持相邻比较，不支持把 temporal KG memory service、JSON memory store 与 LLM Wiki markdown/wiki/node artifact 直接等同。[^7][^8]

**早期 discourse 解释为什么边界要这样写。** HN thread 中同时出现了 “just RAG” 或 “persistent memory RAG” 的说法，也出现了把 distinctive element 放在 write loop、backlinks、filed-back outputs 和 linting 的反驳。这只是 discourse framing，不是 RAG 技术定义的 primary authority。它提示本节点应避免两种偏差：一是把 LLM Wiki 写成反 RAG；二是因为存在 retrieval 就抹掉 durable wiki artifact 和 maintenance workflow 的差异。[^3]

**可采用的窄结论。** 在当前证据范围内，最稳妥的表述是：LLM Wiki 是一种把 preserved raw sources 编译为 maintained wiki/node artifact 的工作流模式，围绕 writeback、lint、update、index/log、citation/provenance 做维护；RAG/GraphRAG 是 retrieval、index、summary 和 answer-synthesis 机制；agent memory 是 persistent memory/read-write/traceability 机制。它们可以互补、组合、互相借用工具，但本节点不声称谁优于谁，也不做 broad benchmark、adoption、scale 或 product comparison。[^1][^2][^4][^7][^8]

**证据缺口。** 当前材料不足以支持：LLM Wiki 比 RAG 更好、RAG 缺少 durable artifacts、GraphRAG 只是普通 chunk retrieval、agent memory 等同 LLM Wiki、任何系统的企业可用性、采用情况、成本/速度/质量优势、scale threshold、访问控制、并发治理或 broad ecosystem ranking。若需要这些结论，应回到 source mining，而不是在本节点中凭常识扩展。[^9]

## References

### [R1] Karpathy LLM Wiki idea file

target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
target_version: raw_snapshot
pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
citation_role: primary_llm_wiki_source
why_cited: Provides the primary local source for LLM Wiki as a persistent maintained wiki artifact with ingest, query file-back, lint, index, and log operations.
evidence_summary: The gist defines the pattern as a structured interlinked markdown wiki maintained between raw sources and user interaction, with human sourcing/question steering and LLM maintenance work.

### [R2] llm-wiki-compiler README

target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
citation_role: implementation_variant_source
why_cited: Provides implementation evidence for persistent artifacts, query save, index rebuild, provenance, lint/review, MCP, and retrieval/search coexistence.
evidence_summary: The README describes compiling sources into a persistent artifact, query --save, candidate review, source markers, claim-level provenance, lint diagnostics, local viewer, MCP server, semantic search, embeddings, and reranking.

### [R3] Hacker News original thread

target: data/raw/hacker_news/hacker-news-original-thread/text.txt
target_version: raw_snapshot
pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
citation_role: discourse_context_source
why_cited: Provides early discussion context for the just-RAG/write-loop boundary debate without serving as primary technical authority.
evidence_summary: The thread contains both just-RAG and persistent-memory-RAG interpretations and responses emphasizing write loop, backlinks, file-back, linting, staleness, and maintenance concerns.

### [R4] GraphRAG paper

target: data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex
citation_role: technical_adjacent_source
why_cited: Provides source-backed RAG and GraphRAG baseline claims for retrieval, graph indexing, community summaries, and map-reduce answer synthesis.
evidence_summary: The paper describes canonical RAG retrieval into context and GraphRAG's graph index, community summarization, and global answer generation from community summaries.

### [R5] Ragas paper

target: data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex
citation_role: technical_adjacent_source
why_cited: Provides source-backed RAG pipeline and evaluation vocabulary without asserting maintained wiki artifacts.
evidence_summary: The paper describes RAG systems as retrieval plus LLM generation over reference textual databases and evaluates faithfulness, answer relevance, and context relevance.

### [R6] ALCE paper

target: data/raw/arxiv/arxiv-alce/source/emnlp2023.tex
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-alce/source/emnlp2023.tex
citation_role: citation_overlap_source
why_cited: Provides source-backed evidence that retrieval-grounded answer generation can include citation-quality evaluation.
evidence_summary: ALCE requires retrieval of supporting evidence and answers with citations, evaluates fluency, correctness, and citation quality, and notes limitations in complete citation support.

### [R7] Zep paper

target: data/raw/arxiv/arxiv-zep/source/main.tex
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-zep/source/main.tex
citation_role: agent_memory_source
why_cited: Provides source-backed evidence for dynamic temporal KG memory, traceability, and update mechanisms adjacent to LLM Wiki.
evidence_summary: The paper describes a memory layer based on Graphiti, with episode, semantic entity, and community subgraphs, dynamic updates, source episode traceability, and temporal contradiction invalidation.

### [R8] LangChain long-term memory docs

target: data/raw/webpage/langchain-long-term-memory-docs/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/langchain-long-term-memory-docs/text.txt
citation_role: agent_memory_source
why_cited: Provides documentation evidence for persistent JSON memory stores with tool-mediated read/write/search.
evidence_summary: The docs describe long-term memory across sessions and conversations, JSON documents organized by namespace/key, store.put/get/search operations, and read/write tools.

### [R9] Evidence scope for cand_010

target: .llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml
target_version: planning_snapshot
pinned_version: .llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml
citation_role: process_scope_source
why_cited: Pins the generation boundary, allowed sources, prior-KB roles, and forbidden claim classes for audit.
evidence_summary: The evidence scope authorizes bounded generation and forbids anti-RAG, superiority, empirical, adoption, enterprise, scale, broad comparison, and uncited adjacent-system claims.

### [R10] Adopted origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around the local canon and overclaim boundaries for LLM Wiki nodes.
evidence_summary: The adopted node treats the Karpathy gist as bounded canon and limits broader launch, adoption, ecosystem, and empirical claims.

### [R11] Adopted working definition node

target: kb/20260524_072000_llm_wiki_working_definition.md
target_version: "1.0"
pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around LLM Wiki as source-preserving maintained artifact, not as authority for new RAG facts.
evidence_summary: The adopted node defines LLM Wiki through raw sources, persistent compiled wiki artifacts, schema/instruction governance, and maintenance loops.

### [R12] Adopted three-layer architecture node

target: kb/20260524_080000_llm_wiki_three_layer_architecture.md
target_version: "1.0"
pinned_version: nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around raw/wiki/schema architecture while keeping adjacent-system claims tied to primary sources.
evidence_summary: The adopted node distinguishes raw source layer, compiled wiki layer, schema/instruction layer, and supporting infrastructure such as index/log/tooling.

### [R13] Adopted ingest/compile/query/lint workflow node

target: kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md
target_version: "1.0"
pinned_version: nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around the LLM Wiki maintenance workflow, not primary evidence for RAG or memory systems.
evidence_summary: The adopted node bounds the LLM Wiki workflow around ingest/source intake, compile/wiki update, query/synthesis, file-back/update, lint/health-check, and index/log maintenance.

## Footnotes

[^1]:
    target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    citation_role: primary_llm_wiki_boundary_support
    why_cited: Supports the core claim that LLM Wiki centers a persistent markdown wiki maintained between user and raw sources, with ingest, query file-back, lint, index, and log operations.
    evidence_summary: The gist contrasts query-time retrieval from raw documents with incrementally building and maintaining a persistent wiki; it describes raw/wiki/schema layers, ingest updates, query answers filed back, lint checks, index.md, and log.md.

[^2]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: implementation_boundary_support
    why_cited: Supports implementation-level claims that a concrete LLM Wiki compiler uses persistent artifacts, query --save writeback, index rebuild, provenance, lint/review, and retrieval/search/embeddings.
    evidence_summary: The README contrasts RAG with compiling sources into a persistent artifact, describes query --save and index rebuild, documents provenance/lint/review/MCP/viewer surfaces, and lists chunked retrieval, semantic search, embeddings, and reranking.

[^3]:
    target: data/raw/hacker_news/hacker-news-original-thread/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
    citation_role: discourse_framing
    why_cited: Frames why the node must address both just-RAG interpretations and write-loop interpretations without treating HN as technical authority.
    evidence_summary: The thread includes comments calling the pattern just RAG or persistent memory RAG, and counter-comments identifying the write loop, backlinks, filed-back outputs, and linting as the distinctive part.

[^4]:
    target: data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex
    citation_role: technical_adjacent_boundary
    why_cited: Supports the RAG and GraphRAG baseline without straw-manning RAG as only raw chunk lookup.
    evidence_summary: The paper describes canonical RAG as retrieving external corpus records for a query and generating from those records; GraphRAG builds a graph index, pregenerates community summaries, and uses map-reduce over summaries for global questions.

[^5]:
    target: data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex
    citation_role: rag_evaluation_boundary
    why_cited: Supports the claim that RAG is a retrieval plus LLM generation pipeline with evaluation dimensions for retrieval focus and faithful answer generation.
    evidence_summary: The paper describes RAG systems as composed of retrieval and LLM-based generation modules and evaluates context relevance, faithfulness, and answer relevance.

[^6]:
    target: data/raw/arxiv/arxiv-alce/source/emnlp2023.tex
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-alce/source/emnlp2023.tex
    citation_role: citation_overlap_support
    why_cited: Supports the limited overlap claim that retrieval-grounded answer systems can evaluate citation quality and verifiability.
    evidence_summary: ALCE requires systems to retrieve supporting evidence and generate answers with citations, with metrics for fluency, correctness, and citation quality; it also reports incomplete citation support as an open difficulty.

[^7]:
    target: data/raw/arxiv/arxiv-zep/source/main.tex
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-zep/source/main.tex
    citation_role: agent_memory_adjacency
    why_cited: Supports the adjacent-memory comparison for dynamic temporal knowledge graphs, episode traceability, and contradiction invalidation.
    evidence_summary: The Zep paper describes Graphiti as a dynamic temporally aware knowledge graph with episode, semantic entity, and community subgraphs; semantic artifacts can be traced to source episodes and new edges can invalidate contradictory older edges.

[^8]:
    target: data/raw/webpage/langchain-long-term-memory-docs/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/langchain-long-term-memory-docs/text.txt
    citation_role: agent_memory_adjacency
    why_cited: Supports the adjacent-memory comparison for persistent JSON memories with read/write/search tools.
    evidence_summary: The docs describe long-term memory persisting across conversations and sessions as JSON documents organized by namespace and key, with stores accessible to tools for read, write, and search operations.

[^9]:
    target: .llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml
    target_version: planning_snapshot
    pinned_version: .llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml
    citation_role: scope_boundary
    why_cited: Records the planner-authorized evidence boundaries and forbidden claims for this first-version candidate.
    evidence_summary: The evidence scope marks local evidence sufficient only for a bounded first version and forbids superiority, adoption, enterprise-readiness, empirical, scale, access-control, concurrency, broad comparison, and uncited adjacent-system claims.
