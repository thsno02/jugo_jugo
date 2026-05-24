# Generation Task

run_id:: run_20260524_073500_worker_generation_working_definition
executor_role:: worker_executor
task_packet:: .llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/next_task_packet.md
candidate_id:: cand_002_working_definition
target_node_id:: 20260524_072000_llm_wiki_working_definition
version_target:: 1.0

## Task

Generate a candidate first-version bundle for the LLM Wiki working definition node. Do not adopt the node.

## Allowed outputs

- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/node.yaml`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/provenance.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/change.md`
- `.llmwiki/runs/run_20260524_073500_worker_generation_working_definition/task.md`
- `.llmwiki/runs/run_20260524_073500_worker_generation_working_definition/generator_trace.md`
- `.llmwiki/runs/run_20260524_073500_worker_generation_working_definition/loop_status.md`
- `.llmwiki/runs/run_20260524_073500_worker_generation_working_definition/loop_delivery.md`

## Forbidden outputs

- `nodes/20260524_072000_llm_wiki_working_definition/node.yaml`
- `kb/`
- `generated/`

## Completion rule

Mark `LOOP_DONE` only if all four version-bundle files exist and the stated evidence boundaries are respected.
