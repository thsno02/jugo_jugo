# Change: genesis -> 1.0

node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T10:00:00+08:00
run_id:: run_20260524_100000_worker_generation_vs_rag_write_loop
adoption_status:: pending_audit

## Why this node was created

This node was created to capture `cand_010_vs_rag_write_loop`: a bounded comparison between LLM Wiki and RAG/write-loop adjacent systems. The planner selected this node because existing KB anchors describe LLM Wiki origin, working definition, architecture, and workflow, but do not yet state the narrow boundary between durable maintained wiki/node/card artifacts and RAG/GraphRAG/agent-memory retrieval, indexing, synthesis, and memory mechanisms.

## Why this first version is acceptable

This first version is acceptable as a candidate because the source-mining run marked the evidence as `enough_for_first_version`, the planning run passed the generation entry gate, and the card stays within the approved artifact/workflow boundary. It does not adopt root metadata, does not write `kb/` or `generated/`, and does not claim empirical superiority, broad adoption, enterprise readiness, scale behavior, or broad product comparison.

## Evidence basis

- Karpathy gist supports LLM Wiki as a persistent maintained markdown/wiki artifact with ingest, query file-back, lint, index, and log operations.
- Atomicstrata README supports implementation evidence for persistent artifacts, `query --save`, index rebuild, provenance, lint/review, MCP, and retrieval/search/embeddings coexistence.
- GraphRAG and Ragas support the RAG/GraphRAG side as retrieval, graph indexing, community-summary, answer-synthesis, and retrieval-generation evaluation mechanisms.
- ALCE supports citation/evidence-generation overlap without proving maintained wiki artifact equivalence.
- Zep and LangChain docs support adjacent persistent memory/write-read/traceability mechanisms without proving equivalence to LLM Wiki.
- HN supports early discourse framing around "just RAG" and write-loop interpretations only.
- Prior KB nodes are used only as continuity anchors and boundary controls.

## Known limits

The version is not adopted and awaits citation/adoption audit. It does not evaluate quality, cost, latency, scale, access control, privacy/security, governance, enterprise readiness, adoption, or benchmark performance. It does not make a broad taxonomy of RAG, GraphRAG, memory, PKM, data catalogs, documentation systems, or knowledge graphs.

## Expected future changes

Future revisions may add stronger adjacent-system taxonomy, broader RAG/GraphRAG implementation evidence, memory-system taxonomy, benchmark/evaluation evidence, or governance/scale evidence if separately mined and scoped. If this candidate is adopted, later major changes should trigger impact review for nodes that cite this boundary as a dependency.
