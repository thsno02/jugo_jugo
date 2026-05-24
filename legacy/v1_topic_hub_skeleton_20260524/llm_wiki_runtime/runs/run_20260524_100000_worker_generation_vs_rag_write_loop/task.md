# Task

run_id:: run_20260524_100000_worker_generation_vs_rag_write_loop
executor_role:: worker_executor
worker_role:: cand_010_vs_rag_write_loop generation worker
task_packet:: .llmwiki/runs/run_20260524_095000_worker_node_planning_vs_rag_write_loop/next_task_packet.md
target_candidate:: cand_010_vs_rag_write_loop
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version_target:: 1.0

## Objective

Generate the candidate first-version node bundle for the bounded artifact/workflow boundary between LLM Wiki and RAG/write-loop adjacent systems. Do not adopt the node.

## Allowed writes

- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/node.yaml`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/provenance.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/change.md`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/task.md`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/generator_trace.md`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/validation_trace.md`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/loop_status.md`
- `.llmwiki/runs/run_20260524_100000_worker_generation_vs_rag_write_loop/loop_delivery.md`

## Forbidden writes respected

- Root `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/node.yaml`
- `kb/`
- `generated/`
- source evidence
- skills
- protocol/archive files
- other node bodies
