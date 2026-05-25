# Citation Audit

run_id:: run_20260524_101000_worker_audit_vs_rag_write_loop
executor_role:: worker_executor
worker_role:: cand_010_vs_rag_write_loop citation/adoption audit worker
candidate_id:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0
decision:: adopt_recommended

## Validator

Result: pass.

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md
```

Observed output:

```text
card validation passed: 1 cards
```

## Citation Format

Result: pass.

- `## Footnotes` exists.
- `## References` exists.
- Footnotes `[1]` through `[9]` include `target`, `target_version`, `pinned_version`, `citation_role`, `why_cited`, and `evidence_summary`.
- References `[R1]` through `[R13]` include `target`, `target_version`, `pinned_version`, `citation_role`, `why_cited`, and `evidence_summary`.
- `why_cited` fields are specific to the claim role rather than generic source mentions.
- `evidence_summary` fields are consistent with source categories and do not promote secondary or prior-KB anchors into primary evidence.

## Target And Pinned Path Resolution

Result: pass.

All card targets and pinned versions checked in this audit exist locally:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/arxiv/arxiv-graphrag/source/graph_rag.tex`
- `data/raw/arxiv/arxiv-ragas/source/arxiv-version.tex`
- `data/raw/arxiv/arxiv-alce/source/emnlp2023.tex`
- `data/raw/arxiv/arxiv-zep/source/main.tex`
- `data/raw/webpage/langchain-long-term-memory-docs/text.txt`
- `.llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/evidence_scope.yaml`
- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`

## Evidence Matrix Traceability

Result: pass.

- `[^1]` and `[R1]` map to evidence matrix source `karpathy-gist-llm-wiki`.
- `[^2]` and `[R2]` map to `repo-atomicstrata-llm-wiki-compiler`.
- `[^3]` and `[R3]` map to `hacker-news-original-thread`.
- `[^4]` and `[R4]` map to `arxiv-graphrag`.
- `[^5]` and `[R5]` map to `arxiv-ragas`.
- `[^6]` and `[R6]` map to `arxiv-alce`.
- `[^7]` and `[R7]` map to `arxiv-zep`.
- `[^8]` and `[R8]` map to `langchain-long-term-memory-docs`.
- `[^9]` and `[R9]` map to the planner evidence scope for source boundary and forbidden-claim control.
- `[R10]` through `[R13]` are prior KB anchors and are labeled as continuity anchors.

## Semantic Support Sampling

Result: pass.

- Karpathy gist supports persistent wiki, raw/wiki/schema, ingest, filed-back query answers, lint, index, and log claims.
- The `llm-wiki-compiler` README supports persistent artifact, `query --save`, index rebuild, provenance, lint/review, MCP, and retrieval/search/embeddings coexistence claims.
- GraphRAG source supports canonical RAG retrieval into context and GraphRAG graph index, community summaries, and map-reduce over summaries.
- Ragas source supports RAG as retrieval plus LLM generation and the context relevance, faithfulness, and answer relevance evaluation vocabulary.
- ALCE source supports retrieval of evidence, generated answers with citations, and fluency/correctness/citation-quality metrics.
- Zep source supports temporal KG memory, episode/semantic/community subgraphs, source-episode traceability, and contradiction invalidation.
- LangChain docs support long-term memory as JSON documents organized by namespace/key with tool-mediated read/write/search.
- HN source supports early discourse framing around "just RAG", persistent memory RAG, write loop, backlinks, file-back, and linting, and is not used as technical authority.

## Overclaim And Category Control

Result: pass.

- No citation treats HN as primary technical authority for RAG.
- No citation treats Atlan as authority; Atlan is not used in the candidate card.
- No prior KB citation is used to support new RAG, GraphRAG, ALCE, Zep, LangChain, enterprise, adoption, or empirical-performance facts.
- The card states evidence gaps explicitly and does not cite a manifest as factual source except for scope/process boundaries.

## Repair Tasks

None required for citation adoption.

