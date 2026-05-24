# Next Task Packet

task_name:: cand_010_vs_rag_write_loop_generation
target_candidate:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version_target:: 1.0
decision:: generation_entry_pass

## Objective

Generate the first-version node bundle for a bounded comparison node: LLM Wiki vs RAG as a write-loop artifact boundary. The node must explain that the distinction is not retrieval vs no retrieval; it is the durable maintained wiki/node artifact and its writeback/lint/update/provenance workflow versus RAG/GraphRAG/agent-memory retrieval, index, synthesis, and memory mechanisms.

## Allowed Inputs

Planning and gate artifacts:

- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/planner_report.md`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/node_plan.yaml`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.md`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/generation_entry_gate.md`

Source-mining artifacts:

- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_scope.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_inventory.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/source_notes.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_094000_worker_source_mining_vs_rag_write_loop/retrieval_requests.md`

Primary/local sources:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`

Technical adjacent sources:

- `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex`
- `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex`
- `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex`
- `data/raw/arxiv/arxiv-zep/source/main.tex`
- `data/raw/webpage/langchain-long-term-memory-docs/text.txt`

Optional secondary framing:

- `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`

Prior KB anchors for continuity and boundary only:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`

## Forbidden Inputs

- New web retrieval.
- Unlisted external RAG/GraphRAG/agent-memory facts from model memory.
- Controller drift sample artifacts as authority.
- Any source evidence content not included in the approved scope unless generation stops and records a retrieval/source-mining request.

## Allowed Writes

Only write the first-version bundle:

- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/node.yaml`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/provenance.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/change.md`

Also write normal generation run status/delivery artifacts under the generation worker's own run directory.

## Forbidden Writes

- Do not write `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/node.yaml`.
- Do not update `kb/` or `generated/`.
- Do not adopt, audit, view-build, or modify control state beyond generation status artifacts unless a separate controller packet authorizes it.
- Do not alter source evidence, skills, protocols, or archive files.

## Required Artifacts

- Version bundle `node.yaml`
- `card.md`
- `provenance.md`
- `change.md`
- generation `loop_status.md`
- generation `loop_delivery.md`

## Citation / Provenance / Change Constraints

- Every factual claim about RAG, GraphRAG, ALCE, Zep, or LangChain must cite the corresponding allowed local source.
- Use Karpathy gist for canonical LLM Wiki pattern claims.
- Use atomicstrata README only as implementation evidence.
- Use HN only for early discourse framing.
- Use Atlan only as labeled secondary/product framing if used at all.
- Mark prior KB anchors as prior-KB continuity, not as direct evidence for new adjacent-system facts.
- Preserve the first-version scope: artifact/workflow boundary only.

## Audit Concerns

- Audit for anti-RAG framing and unsupported superiority claims.
- Audit for uncited outside knowledge about RAG/GraphRAG/agent memory.
- Audit that GraphRAG is not reduced to plain raw chunk retrieval.
- Audit that agent memory persistence is treated as adjacent, not equivalent.
- Audit that root metadata is not written before adoption.

## Completion Marker

End generation delivery with `LOOP_DONE` if all required version bundle artifacts are written and no scope violation occurs. End with `LOOP_BLOCKED` if generation needs broader evidence or retrieval.

