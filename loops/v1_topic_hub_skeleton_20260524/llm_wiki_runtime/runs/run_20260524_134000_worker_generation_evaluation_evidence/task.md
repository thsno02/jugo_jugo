# Task

- Role: generation worker for `cand_007_evaluation_evidence`
- Node id: `20260524_132000_llm_wiki_evaluation_evidence`
- Version: `1.0`
- Objective: generate a candidate node bundle for audit, without adopting it.
- Generation run: `.llmwiki/runs/run_20260524_134000_worker_generation_evaluation_evidence/`

## Required Outputs

- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/provenance.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/change.md`
- `task.md`, `generator_trace.md`, `validation_trace.md`, `loop_status.md`, `loop_delivery.md`

## Initial Constraints

- Do not adopt the node or write root node files.
- Keep the topic bounded to LLM Wiki evaluation/evidence, evidence quality, citation auditability, evaluation boundaries, verifiable versus unverifiable claims, source gaps/deferred retrieval, and KB trust expression.
- Use evidence conservatively; downgrade or remove claims without citation targets.
- Ensure `## References` appears before `## Footnotes`, and `## Footnotes` is the final top-level section.

