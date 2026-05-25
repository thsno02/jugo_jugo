# Task

run_id:: run_20260524_121000_worker_frontier_status_sync_cand008
executor_role:: worker_executor
worker_role:: narrow control/frontier status sync worker
task_packet:: user_dispatch_2026-05-24_cand_008_frontier_status_sync
status:: accepted

## Scope

Synchronize control-plane status for `cand_008_risks_governance_provenance` after adoption/view and skill-eval confirmation.

Allowed writes:

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/runs/run_20260524_121000_worker_frontier_status_sync_cand008/`

Forbidden writes:

- `nodes/`
- `kb/`
- `generated/`
- `skills`
- `data`
- `archive`
- `reports`

Required outcome:

- Mark cand_008 frontier/action/status as built/adopted/closed using existing field style.
- Preserve next action as `dispatch_worker_task_packet_for_cand_006_implementation_ecosystem_source_mining_frontier`.
- Validate updated YAML control files.
- Confirm `generated/status.yaml` remains adopted_nodes=6, citation_edges=110, impact_queue_open=0.
