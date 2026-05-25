# Generation Task

run_id:: run_20260524_081500_worker_generation_architecture
executor_role:: worker_executor
task_packet:: .llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/next_task_packet.md
candidate_id:: cand_003_architecture
target_node_id:: 20260524_080000_llm_wiki_three_layer_architecture
version_target:: 1.0

## Objective

Generate a candidate version bundle for the LLM Wiki three-layer architecture node. Do not adopt the node and do not write root node metadata, `kb/`, or `generated/`.

## Allowed Inputs

Used only the allowed primary gist source, adopted prior KB anchors, implementation-flavored sources, and secondary process/report sources named in the architecture packet and evidence scope.

## Allowed Outputs

- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/node.yaml`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/provenance.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/change.md`
- `.llmwiki/runs/run_20260524_081500_worker_generation_architecture/task.md`
- `.llmwiki/runs/run_20260524_081500_worker_generation_architecture/generator_trace.md`
- `.llmwiki/runs/run_20260524_081500_worker_generation_architecture/loop_status.md`
- `.llmwiki/runs/run_20260524_081500_worker_generation_architecture/loop_delivery.md`

## Completion Contract

Return `LOOP_DONE` only if all four bundle files exist, the version metadata remains `candidate_pending_audit`, citation blocks include required fields, and the content stays inside the architecture boundary.
