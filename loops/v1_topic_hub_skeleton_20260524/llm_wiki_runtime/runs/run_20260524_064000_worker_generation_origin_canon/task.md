# Task

run_id:: run_20260524_064000_worker_generation_origin_canon
executor_role:: worker_executor
phase:: version_bundle_generation
task_packet:: .llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/next_task_packet.md
target_candidate_id:: cand_001_origin_and_canon
target_node_id:: 20260524_062000_llm_wiki_origin_and_canon
version_target:: 1.0

## Objective

Generate a bounded, non-adopted candidate version bundle for the LLM Wiki origin/canon node.

## Allowed outputs

- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/node.yaml`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/change.md`
- `.llmwiki/runs/run_20260524_064000_worker_generation_origin_canon/task.md`
- `.llmwiki/runs/run_20260524_064000_worker_generation_origin_canon/generator_trace.md`
- `.llmwiki/runs/run_20260524_064000_worker_generation_origin_canon/loop_status.md`
- `.llmwiki/runs/run_20260524_064000_worker_generation_origin_canon/loop_delivery.md`

## Forbidden outputs

- `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml`
- `kb/`
- `generated/`

## Completion rule

Write `LOOP_DONE` only if all four version bundle files exist and remain inside the repaired evidence boundaries. Otherwise write `LOOP_BLOCKED`.
