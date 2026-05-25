# Planner Report

run_id:: run_20260524_095000_worker_node_planning_vs_rag_write_loop
executor_role:: cand_010_vs_rag_write_loop node-planning worker
candidate_id:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
decision:: generation_entry_pass

## Selection

`cand_010_vs_rag_write_loop` is ready for first-version generation. The current frontier marks it `ready_to_build`, `evidence_state=enough_for_first_version`, and `retrieval_required_before_build=false`. The source-mining delivery for `run_20260524_094000_worker_source_mining_vs_rag_write_loop` also reports `decision=ready_to_plan` with no blocking gaps.

## Planned Node

title:: LLM Wiki vs RAG: write-loop artifact boundary
version_target:: 1.0

The node should explain the minimum source-backed distinction between LLM Wiki and RAG-adjacent systems. It should not claim that LLM Wiki avoids retrieval. The supported framing is:

LLM Wiki and RAG both connect LLMs to external knowledge, and both may involve retrieval, indexes, summaries, citations, and iterative synthesis. The bounded difference is that LLM Wiki makes a maintained wiki/node artifact the central durable product: raw sources are compiled into a browsable markdown/wiki layer, query answers may be filed back, and lint/update/index/log/provenance workflows keep that artifact usable. RAG and GraphRAG are technical mechanisms for retrieval, graph indexing, summary construction, and answer synthesis; agent-memory systems add persistent read/write memory or temporal graphs, but those mechanisms are not automatically the same as an LLM Wiki raw/wiki/schema maintenance loop.

## Supported Claim Outline

1. LLM Wiki's canonical pattern contrasts ordinary query-time retrieval with an incrementally maintained wiki artifact between raw sources and the user.
2. LLM Wiki includes writeback and maintenance behavior: query answers can become pages, and lint/update workflows check contradictions, stale claims, orphan pages, missing links, and gaps.
3. Implementation evidence shows this boundary can coexist with retrieval/search: a compiler can use retrieval while also saving answers, rebuilding indexes, maintaining provenance, and linting generated wiki artifacts.
4. RAG and GraphRAG should be described without straw-manning: canonical RAG retrieves records for query-time generation, while GraphRAG builds graph indexes and pregenerated community summaries for answer synthesis.
5. Citation-oriented RAG evaluation overlaps with LLM Wiki's verifiability concerns, but citation/evidence generation alone does not define a maintained wiki artifact.
6. Agent-memory systems overlap on persistence, read/write tools, dynamic updates, and traceability, but the evidence only supports an adjacency claim, not equivalence with LLM Wiki.
7. Early HN discourse can frame why "just RAG" was debated, but it should not be used as technical authority for RAG definitions.

## Evidence Sufficiency

Evidence is sufficient for a bounded comparison node because each side of the boundary has direct support:

- LLM Wiki pattern and workflow: Karpathy gist plus atomicstrata implementation evidence.
- Early discourse/risk framing: HN thread.
- RAG/GraphRAG technical baseline: GraphRAG paper and Ragas paper.
- Citation/verifiability overlap: ALCE paper.
- Agent-memory adjacency: Zep paper and LangChain long-term memory docs.
- Prior-KB continuity: adopted origin/canon, working definition, architecture, and workflow nodes.

No new retrieval is required before generation if the generator stays within the planned claim outline and citation constraints.

## Non-Goals

- Do not write a broad product, vendor, ecosystem, or adoption comparison.
- Do not claim LLM Wiki is better than RAG.
- Do not claim RAG lacks indexes, summaries, citations, memory, durable artifacts, or write paths.
- Do not claim agent-memory stores are identical to LLM Wiki.
- Do not make empirical performance, token-efficiency, scale-threshold, enterprise-readiness, access-control, or adoption claims.
- Do not use Atlan as primary technical authority.

## Generation Risks

- Overcorrecting the "just RAG" debate into an anti-RAG node.
- Describing RAG as stateless/raw-chunk-only despite GraphRAG's graph indexes and summaries.
- Treating all persistence or memory writeback as LLM Wiki.
- Letting secondary/product framing drive technical claims.
- Using prior KB anchors as new evidence for RAG or agent-memory systems.

## Gate Result

Generation-entry gate passes. The next worker should generate only the version bundle under `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/` and must not adopt root metadata before audit passes.

