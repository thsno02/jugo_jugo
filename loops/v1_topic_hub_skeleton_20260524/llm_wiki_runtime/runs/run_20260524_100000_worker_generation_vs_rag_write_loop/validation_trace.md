# Validation Trace

run_id:: run_20260524_100000_worker_generation_vs_rag_write_loop
executor_role:: worker_executor

## Planned checks

- Bundle files exist at the four allowed version paths.
- `card.md` starts with a level-1 title and contains `## Footnotes` and `## References`.
- Citation blocks include required fields: `target`, `target_version`, `pinned_version`, `citation_role`, `why_cited`, and `evidence_summary`.
- Citation target and pinned paths resolve from repo root.
- Card claims stay within evidence scope and avoid forbidden claim classes.
- Root node metadata is not written before adoption.

## Script checks

`/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`

Result: pass.

Output:

```text
card validation passed: 1 cards
```

## Node validator note

`scripts/kb_validate_node.py` validates adopted root node directories and requires root `nodes/<node_id>/node.yaml`. This candidate generation task is explicitly forbidden from writing root node metadata before audit/adoption, so the node validator is not applicable to this candidate bundle at generation time. The audit worker should validate the version bundle directly and keep the root metadata gate closed until adoption.

## Manual sanity checks

- Card uses Karpathy gist and atomicstrata README for LLM Wiki artifact/workflow claims.
- Card uses GraphRAG/Ragas/ALCE/Zep/LangChain sources only for their directly supported adjacent-system claims.
- HN is labeled discourse framing only.
- Atlan is not used.
- Prior KB references are continuity anchors only.
- No superiority, adoption, enterprise-readiness, empirical quality, scale, access-control, concurrency, token-efficiency, or broad benchmark claim is made.
- GraphRAG is not reduced to raw chunk retrieval.
- Agent memory is treated as adjacent, not equivalent.
- Root `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/node.yaml` does not exist after generation.
