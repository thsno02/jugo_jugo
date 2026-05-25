# Generation Entry Gate

run_id:: run_20260524_095000_worker_node_planning_vs_rag_write_loop
candidate_id:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
decision:: pass
controller_decision_label:: generation_entry_pass

## Gate Inputs Checked

- Frontier candidate exists: yes.
- Frontier candidate status is `ready_to_build`: yes.
- Source-mining run exists and is worker-attributed: yes, `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop`.
- Source-mining decision supports planning: yes, `ready_to_plan`.
- Evidence state is sufficient for first version: yes, `enough_for_first_version`.
- Retrieval required before build: no.
- Planner artifacts present in this run: yes.
- Generator task packet names candidate, source-mining run, allowed inputs, forbidden inputs, version target, and output paths: yes.

## Basis

The local evidence supports a narrow first-version node if the generator stays on the artifact/workflow boundary:

- Karpathy gist and atomicstrata README support the LLM Wiki side: persistent wiki/node artifact, writeback/file-back, lint/update/index/log/provenance workflow, and retrieval/search coexistence.
- GraphRAG and Ragas support the RAG/GraphRAG side without straw-manning RAG as only raw chunk retrieval.
- ALCE supports citation/evidence-generation overlap.
- Zep and LangChain docs support adjacent memory read/write systems without collapsing them into LLM Wiki.
- HN supports early "just RAG" discourse only.
- Prior KB anchors support continuity and boundaries only.

## Conditions For Generation

- Generate only `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/node.yaml`, `card.md`, `provenance.md`, and `change.md`.
- Do not write root `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/node.yaml`.
- Do not adopt or view-build.
- Do not retrieve new sources.
- If the generator needs broader claims, stop with `LOOP_BLOCKED` and request source mining rather than expanding scope.

## Failure Modes To Audit

- Anti-RAG or superiority framing.
- Uncited generic RAG/GraphRAG/agent-memory facts.
- Treating Atlan as primary technical evidence.
- Treating prior KB anchors as primary evidence for new adjacent-system facts.
- Forgetting that LLM Wiki may use retrieval/search.
- Forgetting that GraphRAG already includes graph indexes and pregenerated summaries.

